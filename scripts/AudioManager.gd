extends Node
## Глобальный аудио-менеджер: музыка, SFX, озвучка.
## Из .dialogue вызывается как: AudioManager.play_music("res://audio/theme.ogg")

# ==================== НАСТРОЙКИ ====================

@export var default_fade_time: float = 1.5      ## Кроссфейд музыки по умолчанию
@export var sfx_pool_size: int = 8               ## Сколько SFX-плееров держать в пуле
@export var debug_audio: bool = false            ## Логировать каждое воспроизведение

# Имена шин. Если переименуешь шины — поменяй и тут.
const BUS_MASTER := "Master"
const BUS_MUSIC  := "Music"
const BUS_SFX    := "SFX"
const BUS_VOICE  := "Voice"
const BUS_FON    := "Fon"

# ==================== ВНУТРЕННЕЕ ====================

var _music_player: AudioStreamPlayer
var _music_prev: AudioStreamPlayer          ## Второй плеер для кроссфейда
var _voice_player: AudioStreamPlayer
var _fon_player: AudioStreamPlayer
var _fon_prev: AudioStreamPlayer
var _sfx_pool: Array[AudioStreamPlayer] = []
var _sfx_index: int = 0

var _current_music_path: String = ""
var _current_voice_path: String = ""
var _current_fon_path
var _cache: Dictionary = {}                 ## path -> AudioStream

# --- Очереди треков ---
var _music_queue: Array[Dictionary] = []   # [{path, fade, loop}, ...]
var _fon_queue: Array[Dictionary] = []

# ==================== ЖИЗНЕННЫЙ ЦИКЛ ====================

func _ready() -> void:
	# Два плеера для музыки (кроссфейд)
	_music_player = _make_player(BUS_MUSIC, "MusicA")
	_music_prev   = _make_player(BUS_MUSIC, "MusicB")
	_voice_player = _make_player(BUS_VOICE, "Voice")
	_fon_player   = _make_player(BUS_FON, "FonB")
	_fon_prev   = _make_player(BUS_FON, "FonA")
	
	_music_player.finished.connect(_on_music_finished)
	_fon_player.finished.connect(_on_fon_finished)
	
	# Пул SFX
	for i in sfx_pool_size:
		var p := _make_player(BUS_SFX, "SFX_%d" % i)
		_sfx_pool.append(p)

	process_mode = Node.PROCESS_MODE_ALWAYS

func _make_player(bus: String, node_name: String) -> AudioStreamPlayer:
	var p := AudioStreamPlayer.new()
	p.bus = bus
	p.name = node_name
	add_child(p)
	return p

# ==================== МУЗЫКА ====================

## Проиграть музыку. Если играет другая — плавно заменит (кроссфейд).
func play_music(path: String, fade: float = -1.0, loop: bool = true, volume: float = 1.0) -> void:
	if not _music_queue.is_empty():
		_music_queue.clear()
	if path == _current_music_path and _music_player.playing:
		return  # Уже играет эта же — ничего не делаем
	path = sys.res_check_and_replace(path)
	if path.right(4) != ".ogg":
		printerr("[AudioManager] Не указано расширение трека: %s" % path, ". Заменяется на .ogg")
		path += ".ogg"
	var stream: AudioStream = _load(path)
	if stream == null:
		push_warning("[AudioManager] Не найден трек: %s" % path)
		return

	if loop and stream is AudioStreamOggVorbis:
		(stream as AudioStreamOggVorbis).loop = true
	elif loop and stream is AudioStreamMP3:
		(stream as AudioStreamMP3).loop = true

	var ft: float = default_fade_time if fade < 0.0 else fade

	# Если что-то уже играет — перекидываем его в _music_prev и гасим.
	if _music_player.playing:
		_swap_music_players()
		_fade_out(_music_prev, ft)

	_music_player.stream = stream
	_music_player.volume_db = -80.0
	_music_player.play()
	_fade_in(_music_player, ft)
	if volume < 1.0:
		var target_db := linear_to_db(max(volume, 0.0001))
		var t2 := create_tween()
		t2.tween_property(_music_player, "volume_db", target_db, ft)

	_current_music_path = path
	if not debug_audio:
		print("[AudioManager] Music: ", path, " (fade ", ft, ")")

## Остановить музыку с затуханием.
func stop_music(fade: float = -1.0) -> void:
	if not _music_player.playing and not _music_prev.playing:
		return
	var ft: float = default_fade_time if fade < 0.0 else fade
	_fade_out(_music_player, ft)
	_fade_out(_music_prev, ft)
	_current_music_path = ""

## Мгновенно остановить музыку (без затухания).
func stop_music_immediate() -> void:
	_music_player.stop()
	_music_prev.stop()
	_current_music_path = ""

func _swap_music_players() -> void:
	var tmp := _music_player
	_music_player = _music_prev
	_music_prev = tmp

func _fade_in(player: AudioStreamPlayer, duration: float) -> void:
	if duration <= 0.0:
		player.volume_db = 0.0
		return
	var t := create_tween()
	t.tween_property(player, "volume_db", 0.0, duration)

func _fade_out(player: AudioStreamPlayer, duration: float) -> void:
	if not player.playing:
		return
	if duration <= 0.0:
		player.stop()
		return
	var t := create_tween()
	t.tween_property(player, "volume_db", -80.0, duration)
	t.tween_callback(player.stop)

# ==================== SFX ====================

## Проиграть звук один раз. Можно задать громкость в дБ и pitch scale.
func play_sfx(path: String, volume_db: float = 0.0, pitch: float = 1.0) -> void:
	if path.is_empty():
		return
	path = sys.res_check_and_replace(path)
	var stream: AudioStream = _load(path)
	if stream == null:
		push_warning("[AudioManager] Не найден SFX: %s" % path)
		return

	var player: AudioStreamPlayer = _sfx_pool[_sfx_index]
	_sfx_index = (_sfx_index + 1) % _sfx_pool.size()

	player.stream = stream
	player.volume_db = volume_db
	player.pitch_scale = pitch
	player.play()

	if debug_audio:
		print("[AudioManager] SFX: ", path)

## Удобный алиас, чтобы из диалога читалось естественно.
func sfx(path: String, volume_db: float = 0.0, pitch: float = 1.0) -> void:
	play_sfx(path, volume_db, pitch)

# ==================== ОЗВУЧКА ====================

## Проиграть реплику. Останавливает предыдущую, если играет.
func play_voice(path: String, volume_db: float = 0.0) -> void:
	if path.is_empty():
		return
	path = sys.res_check_and_replace(path)
	var stream: AudioStream = _load(path)
	if stream == null:
		push_warning("[AudioManager] Не найден голос: %s" % path)
		return

	_voice_player.stop()
	_voice_player.stream = stream
	_voice_player.volume_db = volume_db
	_voice_player.play()
	_current_voice_path = path

	if debug_audio:
		print("[AudioManager] Voice: ", path)

func stop_voice() -> void:
	_voice_player.stop()
	_current_voice_path = ""

func is_voice_playing() -> bool:
	return _voice_player.playing

# ==================== ГРОМКОСТЬ ====================

## 0.0 — тишина, 1.0 — обычная громкость.
func set_volume(bus: String, linear: float) -> void:
	var idx: int = AudioServer.get_bus_index(bus)
	if idx < 0:
		push_warning("[AudioManager] Нет шины: %s" % bus)
		return
	AudioServer.set_bus_volume_db(idx, linear_to_db(clampf(linear, 0.0001, 1.0)))
	AudioServer.set_bus_mute(idx, linear <= 0.0)

func get_volume(bus: String) -> float:
	var idx: int = AudioServer.get_bus_index(bus)
	if idx < 0:
		return 0.0
	if AudioServer.is_bus_mute(idx):
		return 0.0
	return db_to_linear(AudioServer.get_bus_volume_db(idx))

func set_music_volume(v: float) -> void: set_volume(BUS_MUSIC, v)
func set_sfx_volume(v: float)   -> void: set_volume(BUS_SFX, v)
func set_voice_volume(v: float) -> void: set_volume(BUS_VOICE, v)



## Проиграть музыку. Если играет другая — плавно заменит (кроссфейд).
func play_fon(path: String, fade: float = -1.0, loop: bool = true) -> void:
	if not _fon_queue.is_empty():
		_fon_queue.clear()
	if path == _current_fon_path and _fon_player.playing:
		return  # Уже играет эта же — ничего не делаем
	path = sys.res_check_and_replace(path)
	if path.right(4) != ".ogg":
		printerr("[AudioManager] Не указано расширение трека: %s" % path, ". Заменяется на .ogg")
		path += ".ogg"
	var stream: AudioStream = _load(path)
	if stream == null:
		push_warning("[AudioManager] Не найден трек: %s" % path)
		return

	if loop and stream is AudioStreamOggVorbis:
		(stream as AudioStreamOggVorbis).loop = true
	elif loop and stream is AudioStreamMP3:
		(stream as AudioStreamMP3).loop = true

	var ft: float = default_fade_time if fade < 0.0 else fade

	# Если что-то уже играет — перекидываем его в _music_prev и гасим.
	if _fon_player.playing:
		_swap_fon_players()
		_fade_out(_fon_prev, ft)

	_fon_player.stream = stream
	_fon_player.volume_db = -80.0
	_fon_player.play()
	_fade_in(_fon_player, ft)

	_current_fon_path = path
	if not debug_audio:
		print("[AudioManager] Fon ", path, " (fade ", ft, ")")

## Остановить музыку с затуханием.
func stop_fon(fade: float = -1.0) -> void:
	if not _fon_player.playing and not _fon_prev.playing:
		return
	var ft: float = default_fade_time if fade < 0.0 else fade
	_fade_out(_fon_player, ft)
	_fade_out(_fon_prev, ft)
	_current_fon_path = ""

## Мгновенно остановить музыку (без затухания).
func stop_fon_immediate() -> void:
	_fon_player.stop()
	_fon_prev.stop()
	_current_fon_path = ""

func _swap_fon_players() -> void:
	var tmp := _fon_player
	_fon_player = _fon_prev
	_fon_prev = tmp

# ==================== ЗАГРУЗКА ====================

func _load(path: String) -> AudioStream:
	if _cache.has(path):
		return _cache[path]
	if not ResourceLoader.exists(path):
		return null
	var res: Resource = load(path)
	if res is AudioStream:
		_cache[path] = res
		return res
	return null



# ==================== ОЧЕРЕДЬ ТРЕКОВ ====================

## Добавить трек в очередь музыки. Играет после текущего.
## Если сейчас ничего не играет — стартует немедленно.
func queue_music(path: String, fade: float = -1.0, loop: bool = false) -> void:
	if not _music_player.playing and _music_queue.is_empty():
		# Нечего ждать — играем сразу
		play_music(path, fade, loop)
		return
	_music_queue.append({"path": path, "fade": fade, "loop": loop})
	if debug_audio:
		print("[AudioManager] Music queued: ", path, " (queue size: ", _music_queue.size(), ")")

## Добавить трек в очередь фонового эмбиента.
func queue_fon(path: String, fade: float = -1.0, loop: bool = false) -> void:
	if not _fon_player.playing and _fon_queue.is_empty():
		play_fon(path, fade, loop)
		return
	_fon_queue.append({"path": path, "fade": fade, "loop": loop})
	if debug_audio:
		print("[AudioManager] Fon queued: ", path, " (queue size: ", _fon_queue.size(), ")")

## Очистить очередь музыки.
func clear_music_queue() -> void:
	_music_queue.clear()

## Очистить очередь фона.
func clear_fon_queue() -> void:
	_fon_queue.clear()

## Очистить все очереди.
func clear_all_queues() -> void:
	_music_queue.clear()
	_fon_queue.clear()

# ==================== ВНУТРЕННИЕ ОБРАБОТЧИКИ ====================

func _on_music_finished() -> void:
	if _music_queue.is_empty():
		_current_music_path = ""
		return
	var next: Dictionary = _music_queue.pop_front()
	play_music(str(next.path), float(next.fade), bool(next.loop))

func _on_fon_finished() -> void:
	if _fon_queue.is_empty():
		_current_fon_path = ""
		return
	var next: Dictionary = _fon_queue.pop_front()
	play_fon(str(next.path), float(next.fade), bool(next.loop))
