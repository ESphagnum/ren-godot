extends Control
class_name CharacterManager

signal character_shown(char_name: String)
signal character_hidden(char_name: String)

const CHARACTER_MODULES := [
	preload("res://characters/mom.gd"),
	preload("res://characters/anton.gd"),
	preload("res://characters/olya.gd"),
	preload("res://characters/dad.gd"),
]

const SPRITES_DIR := "res://images/sprite"
const EYE_FRAME_HALF := 0.1
const EYE_FRAME_CLOSED := 0.1

@export var character_parent_path: NodePath = ^"/root/NovelScene/CharacterLayer/Characters"
@export var debug_load := false
@export var default_fade_duration := 0.3

var _characters: Dictionary = {}
var _cache: Dictionary = {}
var _modules: Dictionary = {}

func _ready() -> void:
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	for m in CHARACTER_MODULES:
		_modules[m.NAME] = m

# ==================== ПУБЛИЧНОЕ API ====================

## Универсальный вызов, повторяющий Ren'Py generate_img.
## show("Mom", "Normal", "m_day", "01", "norm", "aside")
## show("Dad", "Normal", "m_day_winter", "02", "norm2", "ahead", "01")
## show("Olya", "Weeps", "m_dark", "00", "good", "aside", "01")
## Показать персонажа. Ren'Py-эквивалент `show Mom Normal m_day 01 norm aside`.
func show_char(npc: String, emotion: String, view: String, body: String,
			   view2: String = "", eyes: String = "", mouth: String = "") -> void:
	var is_new: bool = not _characters.has(npc)
	_apply_expression(npc, emotion, view, body, view2, eyes, mouth, false)
	if is_new:
		_fade_in_character(npc)

## То же + именованный transform.
func show_t(npc: String, emotion: String, view: String, body: String,
			view2: String, eyes: String, mouth: String, transform: String) -> void:
	_apply_expression(npc, emotion, view, body, view2, eyes, mouth, false)
	if not transform.is_empty():
		play(npc, transform)

## То же, что show(), но без пересоздания контейнера — для смены выражения.
func set_expression(npc: String, emotion: String, view: String, body: String,
					view2: String = "", eyes: String = "", mouth: String = "") -> void:
	_apply_expression(npc, emotion, view, body, view2, eyes, mouth, true)

## Показать одиночный PNG/сцену как персонажа (для Mask, Dad Old, Ant ouch и т.п.).
func show_single(npc: String, path: String, position: String = "center") -> void:
	_ensure_container(npc)
	var info: Dictionary = _characters[npc]
	info.state = {"single": path, "position": position}
	# Скрываем все слои кроме Body
	info.body.texture = _load_texture(path)
	info.body.visible = info.body.texture != null
	info.eyes.visible = false
	info.mouth.visible = false
	info.drop.visible = false
	if info.body.texture:
		var tex_size: Vector2i = info.body.texture.get_size()
		var sz := Vector2(tex_size)
		info.body.size = sz
		info.body.position = Vector2.ZERO
		info.container.size = sz
	character_shown.emit(npc)


func hide_character(npc: String, fade: bool = true) -> void: _remove_or_fade(npc, fade)
func hide_all(fade: bool = true) -> void:
	for n in _characters.keys().duplicate():
		_remove_or_fade(n, fade)
func has_character(npc: String) -> bool: return _characters.has(npc)

## Применить именованный transform из модуля персонажа.
func play(npc: String, transform_name: String) -> void:
	if not _modules.has(npc):
		push_warning("[Characters] Нет модуля '%s'" % npc)
		return
	var tr: Dictionary = _modules[npc].TRANSFORMS.get(transform_name, {})
	if tr.is_empty():
		push_warning("[Characters] У '%s' нет transform '%s'" % [npc, transform_name])
		return
	if not _characters.has(npc):
		push_warning("[Characters] Персонаж '%s' не показан" % npc)
		return
	_apply_transform(npc, tr)


## Сменить текстуру конкретного слоя (для нестандартных случаев).
func set_layer_texture(npc: String, layer_name: String, path: String) -> void:
	var info: Dictionary = _characters.get(npc)
	if info == null:
		return
	var layer: TextureRect = info.get(layer_name.to_lower())
	if layer == null:
		return
	layer.texture = _load_texture(path)
	layer.visible = layer.texture != null

# ==================== ВНУТРЕННЕЕ ====================

func _apply_expression(npc: String, emotion: String, view: String, body: String,
					   view2: String, eyes: String, mouth: String, keep: bool) -> void:
	if not _modules.has(npc):
		push_error("[Characters] Нет модуля для '%s'" % npc)
		return
	var root: String = _modules[npc].ROOT
	if not keep or not _characters.has(npc):
		_ensure_container(npc)
	var info: Dictionary = _characters[npc]
	info.root = root
	info.state = {
		"emotion": emotion, "view": view, "body": body,
		"view2": view2, "eyes": eyes, "mouth": mouth,
	}
	_refresh_layers(npc)
	character_shown.emit(npc)


func _ensure_container(npc: String) -> void:
	if _characters.has(npc):
		return
	var parent := get_node_or_null(character_parent_path)
	if parent == null:
		push_error("[Characters] Не найден parent: %s" % character_parent_path)
		return
	var container := Control.new()
	container.name = npc
	container.mouse_filter = Control.MOUSE_FILTER_IGNORE
	container.pivot_offset = Vector2.ZERO
	container.modulate.a = 0.0
	parent.add_child(container)

	var body_l := _make_layer("Body")
	var eyes_l := _make_layer("Eyes")
	var mouth_l := _make_layer("Mouth")
	var drop_l := _make_layer("Drop")
	container.add_child(body_l)
	container.add_child(eyes_l)
	container.add_child(mouth_l)
	container.add_child(drop_l)

	_characters[npc] = {
		"container": container,
		"body": body_l, "eyes": eyes_l, "mouth": mouth_l, "drop": drop_l,
		"state": {}, "root": "",
		"eye_tween": null, "drop_tween": null, "transform_tweens": [],
	}
	# Fade-in теперь запускается вызывающим кодом — show_char или transform.


func _refresh_layers(npc: String) -> void:
	var info: Dictionary = _characters[npc]
	var s: Dictionary = info.state
	var root: String = info.root

	if s.has("single"):
		# Одиночный режим — уже загружено в show_single
		return

	var emo: String   = s.get("emotion", "Normal")
	var view: String  = s.get("view", "m_day")
	var body_name: String = s.get("body", "00")
	var view2: String = s.get("view2", "")
	var eyes_name: String = s.get("eyes", "")
	var mouth_name: String = s.get("mouth", "")

	# Body
	var body_path := "%s/%s/%s/1_body/%s.png" % [root, emo, view, body_name]
	var body_tex := _load_texture(body_path)
	if body_tex == null:
		push_error("[Characters] Нет тела: %s" % body_path)
		return
	var sz := body_tex.get_size()
	info.body.texture = body_tex
	info.body.size = sz
	info.body.position = Vector2.ZERO
	info.container.size = sz

	# Eyes — размер как body
	info.eyes.size = sz
	info.eyes.position = Vector2.ZERO

	# Mouth
	if mouth_name != "":
		var mouth_path := "%s/%s/%s/3_mouth/%s.png" % [root, emo, view, mouth_name]
		info.mouth.texture = _load_texture(mouth_path)
		info.mouth.visible = info.mouth.texture != null
		info.mouth.size = sz
	else:
		info.mouth.texture = null
		info.mouth.visible = false

	# Eyes
	if eyes_name != "" and view2 != "":
		info.eyes.visible = true
		_setup_eyes(npc, root, emo, view, view2, eyes_name)
	else:
		info.eyes.texture = null
		info.eyes.visible = false
		_kill_tween(info, "eye_tween")


func _apply_transform(npc: String, tr: Dictionary) -> void:
	var info: Dictionary = _characters[npc]
	var container: Control = info.container
	var vp: Vector2 = get_viewport_rect().size

	for t in info.transform_tweens:
		if t and t.is_valid():
			t.kill()
	info.transform_tweens = []

	# Pivot: если flip — по центру X, иначе — левый верх
	if tr.get("flip", false):
		container.pivot_offset = Vector2(container.size.x * 0.5, 0)
		container.scale.x = -1.0
	else:
		container.pivot_offset = Vector2.ZERO
		container.scale.x = 1.0

	if tr.has("alpha"): container.modulate.a = float(tr.alpha)
	var x_anchor: float = float(tr.get("x_anchor", 0.0))

	if tr.has("x"):
		container.position.x = _resolve_x(float(tr.x), x_anchor, container, vp)
	if tr.has("y"):
		container.position.y = float(tr.y)

	for track in tr.get("tracks", []):
		var t := create_tween()
		t.set_parallel(true)   # ← один раз, снаружи цикла шагов
		for step in track:
			var time: float = float(step.get("time", 0.5))
			var tt := _ease_to_trans(str(step.get("ease", "linear")))
			var ee := _ease_to_ease(str(step.get("ease", "linear")))
			var has_prop: bool = step.has("x") or step.has("y") or step.has("alpha")
			if not has_prop:
				t.tween_interval(time)
				t.chain()
				continue

			if step.has("x"):
				var target_x := _resolve_x(float(step.x), x_anchor, container, vp)
				t.tween_property(container, "position:x", target_x, time).set_trans(tt).set_ease(ee)
			if step.has("y"):
				t.tween_property(container, "position:y", float(step.y), time).set_trans(tt).set_ease(ee)
			if step.has("alpha"):
				t.tween_property(container, "modulate:a", float(step.alpha), time).set_trans(tt).set_ease(ee)
			t.chain()
		info.transform_tweens.append(t)


func _setup_eyes(npc: String, root: String, emo: String, view: String,
				 view2: String, mode: String) -> void:
	var info: Dictionary = _characters[npc]
	_kill_tween(info, "eye_tween")
	match mode:
		"ahead_to_aside": _eyes_transition(npc, root, emo, view, view2, "ahead", "aside")
		"aside_to_ahead": _eyes_transition(npc, root, emo, view, view2, "aside", "ahead")
		"ahead_shock":    _eyes_shock(npc, root, emo, view, view2, "ahead")
		"aside_shock":    _eyes_shock(npc, root, emo, view, view2, "aside")
		"dark":           _set_eye_frame(npc, root, emo, view, view2, "dark", "01")
		_:                _eyes_blink_loop(npc, root, emo, view, view2, mode)


func _eyes_blink_loop(npc: String, root: String, emo: String, view: String,
					  view2: String, dir: String) -> void:
	_set_eye_frame(npc, root, emo, view, view2, dir, "01")
	var t := create_tween().set_loops()
	t.tween_interval(randf_range(0.0, 8.0))
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "02"))
	t.tween_interval(EYE_FRAME_HALF)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "03"))
	t.tween_interval(EYE_FRAME_CLOSED)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "02"))
	t.tween_interval(EYE_FRAME_HALF)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "01"))
	t.tween_interval(randf_range(6.0, 9.0))
	_characters[npc].eye_tween = t


func _eyes_transition(npc: String, root: String, emo: String, view: String,
					  view2: String, from_dir: String, to_dir: String) -> void:
	var t := create_tween()
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, from_dir, "01"))
	t.tween_interval(0.05)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, from_dir, "02"))
	t.tween_interval(EYE_FRAME_HALF)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, from_dir, "03"))
	t.tween_interval(EYE_FRAME_CLOSED)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, to_dir, "02"))
	t.tween_interval(EYE_FRAME_HALF)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, to_dir, "01"))
	_characters[npc].eye_tween = t


func _eyes_shock(npc: String, root: String, emo: String, view: String,
				 view2: String, dir: String) -> void:
	var t := create_tween()
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "01"))
	t.tween_interval(0.1)
	t.tween_callback(func(): _set_eye_frame(npc, root, emo, view, view2, dir, "04"))
	_characters[npc].eye_tween = t


func _set_eye_frame(npc: String, root: String, emo: String, view: String,
					view2: String, dir: String, frame: String) -> void:
	var info = _characters.get(npc)
	if info == null:
		return
	if not info.has("eyes") or not is_instance_valid(info.eyes):
		return
	var path := "%s/%s/%s/2_eyes/%s/%s/%s.png" % [root, emo, view, view2, dir, frame]
	var tex := _load_texture(path)
	if tex == null:
		return
	info.eyes.texture = tex
	info.eyes.visible = true


func _remove_or_fade(npc: String, fade: bool) -> void:
	if not _characters.has(npc): return
	var info: Dictionary = _characters[npc]
	# Убираем из реестра СРАЗУ
	_characters.erase(npc)
	character_hidden.emit(npc)

	var cont: Control = info.container
	if not is_instance_valid(cont):
		return

	if fade:
		var t := create_tween()
		t.tween_property(cont, "modulate:a", 0.0, default_fade_duration)
		t.tween_callback(func():
			if is_instance_valid(cont):
				cont.queue_free()
		)
	else:
		cont.queue_free()


func _remove_character(npc: String) -> void:
	if not _characters.has(npc): return
	var info: Dictionary = _characters[npc]
	for key in ["eye_tween", "drop_tween"]:
		_kill_tween(info, key)
	for t in info.transform_tweens:
		if t and t.is_valid(): t.kill()
	if is_instance_valid(info.container):
		info.container.queue_free()
	_characters.erase(npc)
	character_hidden.emit(npc)


func _kill_tween(info: Dictionary, key: String) -> void:
	var t = info.get(key)
	if t and t.is_valid(): t.kill()
	info[key] = null


func _make_layer(name: String) -> TextureRect:
	var tr := TextureRect.new()
	tr.name = name
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	tr.mouse_filter = Control.MOUSE_FILTER_IGNORE
	tr.position = Vector2.ZERO
	return tr


func _load_texture(path: String) -> Texture2D:
	if _cache.has(path): return _cache[path]
	if not ResourceLoader.exists(path):
		if debug_load: printerr("[Characters] Нет файла: %s" % path)
		return null
	var tex: Texture2D = load(path)
	if tex: _cache[path] = tex
	return tex


func _ease_to_trans(e: String) -> Tween.TransitionType:
	match e:
		"linear": return Tween.TRANS_LINEAR
		"ease", "ease_in", "ease_out", "ease_in_out": return Tween.TRANS_SINE
		"back": return Tween.TRANS_BACK
		"elastic": return Tween.TRANS_ELASTIC
		_: return Tween.TRANS_LINEAR


func _ease_to_ease(e: String) -> Tween.EaseType:
	match e:
		"ease_in": return Tween.EASE_IN
		"ease_out": return Tween.EASE_OUT
		_: return Tween.EASE_IN_OUT


## Преобразует «x» из transform в реальную позицию контейнера.
## x_anchor = 0.0 — x задаёт левый край (по умолчанию)
## x_anchor = 1.0 — x задаёт правый край (расстояние от правого края экрана)
## x_anchor = 0.5 — x задаёт центр
func _resolve_x(x: float, x_anchor: float, container: Control, vp: Vector2) -> float:
	var w: float = container.size.x
	if x_anchor >= 1.0:
		return vp.x - x - w
	elif x_anchor >= 0.5:
		return x - w * 0.5
	return x


func _fade_in_character(npc: String) -> void:
	var info: Dictionary = _characters.get(npc)
	if info == null:
		return
	info.container.modulate.a = 0.0
	var t := create_tween()
	t.tween_property(info.container, "modulate:a", 1.0, default_fade_duration)
