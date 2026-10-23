extends Node

## Менеджер сцены. Показывает изображения по алиасам с анимациями в стиле Ren'Py.
## Из .dialogue: do Stage.show("bg_win_f_0_1")

var stage_parent: Control = null

var _active: Dictionary = {}   # alias -> Control
var _cache: Dictionary = {}    # path -> Texture2D
var _tweens: Dictionary = {}   # alias -> Tween

const IMAGES := {
	"bg_white":  "#F8F8FF",
	"bg_black":  "#000000",
	"bg_grey":   "#808080",
	"bg_white_dissolve": {
		"color": "#F8F8FF", "alpha": 0.0,
		"transition": {"time": 1.0, "ease": "linear", "alpha": 1.0},
	},
	"bg_logo3": {
		"path": "res://images/interface/Lang.jpg",
		"shader": "res://objects/InvertMatrix.tres",
		"alpha": 1.0,
	},

	# Окно / ночь
	"bg_win_f_0": "res://images/locate/home/in_side/1st_floor/kitchen/widow/win_f_0.jpg",
	"bg_win_f_50": "res://images/locate/home/in_side/1st_floor/kitchen/widow/win_f_50.jpg",
	"bg_win_f_100": "res://images/locate/home/in_side/1st_floor/kitchen/widow/win_f_100.jpg",
	"bg_win_f_0_1": {
		"based_on": "bg_win_f_0", "alpha": 0.0,
		"xalign": 0.5, "yalign": 0.5, "zoom": 1.78,
		"parallel": [
			{"time": 12.0, "ease": "ease",   "zoom": 1.00},
			{"time": 12.0, "ease": "linear", "alpha": 1.0},
		],
	},
	"bg_win_f_50_1": {
		"based_on": "bg_win_f_50", "alpha": 0.0,
		"transition": {"time": 3.0, "alpha": 1.0, "ease": "linear"},
	},
	"bg_win_f_100_1": {
		"based_on": "bg_win_f_100", "alpha": 0.0,
		"transition": {"time": 1.5, "alpha": 1.0, "ease": "linear"},
	},

	# Кухня — композиты из init.rpy
	"kitchen1_1": {
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
			"res://images/locate/home/in_side/1st_floor/kitchen/Kal_2.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
		],
	},
	"kitchen1_2": {
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
			"res://images/locate/home/in_side/1st_floor/kitchen/Kal_2.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_8.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/paper.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ol0": {
		"group": "sprite.kitchen_ol",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/plate.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kasha_002.png",
		],
	},
	"kitchen_ol1": {
		"group": "sprite.kitchen_ol",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/Eol1/ol001.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kasha_002.png",
			{
				"frames": [
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", "time": 2.50},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_29.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_30.png", "time": 0.20},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_29.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", "time": 8.50},
				],
				"loop": true,
			},
		],
	},
	"kitchen_ol2": {
		"group": "sprite.kitchen_ol",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/Eol2/ol002.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kasha_002.png",
			{
				"frames": [
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", "time": 2.50},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", "time": 0.20},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", "time": 8.50},
				],
				"loop": true,
			},
		],
	},
	"kitchen_ol3": {
		"group": "sprite.kitchen_ol",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/Eol3/ol003.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/kasha_002.png",
			{
				"frames": [
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", "time": 2.50},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol3/eye01.png", "time": 0.20},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", "time": 0.08},
					{"path": "res://images/locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", "time": 8.50},
				],
				"loop": true,
			},
		],
	},

	"kitchen_ant0": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ant1": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/A1.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ant1_book": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/book.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/A1.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ant2": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/A2.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ant2_book": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/book.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/A2.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"kitchen_ant3": {
		"group": "sprite.kitchen_ant",
		"layers": [
			"res://images/locate/home/in_side/1st_floor/kitchen/A3.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},

	"under_table": "res://images/locate/home/in_side/1st_floor/kitchen/Table_ka.jpg",

	# Прихожая
	"bg_door_police": {
		"layers": [
			"res://images/locate/home/in_side/1st_floor/hall/door_police.jpg",
			"res://images/locate/home/in_side/1st_floor/hall/cross_01.png",
			"res://images/locate/home/in_side/1st_floor/hall/yula_01.png",
		],
		"transition": {"time": 1.5, "alpha": 1.0, "ease": "linear"},
	},
	"bg_door": {
		"layers": [
			"res://images/locate/home/in_side/1st_floor/hall/door.jpg",
			"res://images/locate/home/in_side/1st_floor/hall/cross_02.png",
			"res://images/locate/home/in_side/1st_floor/hall/yula_02.png",
		],
		"transition": {"time": 0.5, "alpha": 1.0, "ease": "linear"},
	},
	"bg_door_open": {
		"layers": [
			"res://images/locate/home/in_side/1st_floor/hall/door_open.jpg",
			"res://images/locate/home/in_side/1st_floor/hall/cross_01.png",
			"res://images/locate/home/in_side/1st_floor/hall/yula_01.png",
		],
		"transition": {"time": 1.0, "alpha": 1.0, "ease": "linear"},
	},
	"kitchen_ant2_book_bright": {
		"group": "sprite.kitchen_ant",
		"layers": [
			{
				"path": "res://images/locate/home/in_side/1st_floor/kitchen/book.png",
				"modulate": {"r": 1.3, "g": 1.3, "b": 1.3, "a": 1.0},
			},
			"res://images/locate/home/in_side/1st_floor/kitchen/A2.png",
			"res://images/locate/home/in_side/1st_floor/kitchen/Char.png",
		],
	},
	"ramka1": {
		"path": "res://images/effect/ramka/ramka1.png"
	},
	"grand_mather": {
		"path": "res://images/locate/grand_mather.jpg"
	},
	"Olya_and_Owl0":   "res://images/locate/home/in_side/2st_floor/olga_room/Olya_and_Owl000.jpg",
	"Olya_and_Owl":    "res://images/locate/home/in_side/2st_floor/olga_room/Olya_and_Owl001.jpg",
	"memory_ramka":    "res://images/effect/ramka/ramka4.png",
	"old_movie_003_004": "res://images/effect/old_movie/old_movie_003.png",
	"old_movie_001_002": "res://images/effect/old_movie/old_movie_001.png",
	"owl_screem_effect": "res://images/effect/owl/Owl1.jpg",
	# Сцена «ночь, танцующие звери»
	"bg_room_night1":       "res://images/locate/home/in_side/2st_floor/anton_room/room_night.jpg",
	"bg_room_night2":       "res://images/locate/home/in_side/2st_floor/anton_room/room_night2.jpg",
	"day1_kovai_0":         "res://images/locate/home/in_side/2st_floor/anton_room/Anton_kovai00.png",
	"day1_kovai_1":         "res://images/locate/home/in_side/2st_floor/anton_room/Anton_kovai01.png",
	"bg_pole0":             "res://images/locate/forest/pole/pole0.jpg",
	"bg_pole1":             "res://images/locate/forest/pole/pole1.png",
	"bg_pole2":             "res://images/locate/forest/pole/pole2.png",
	"over_dancing": {
		"layers": [
			"res://images/locate/forest/pole/pole1.png",
			"res://images/locate/forest/pole/pole2.png",
		],
	},
	"dancing_animal_on":    "res://images/locate/forest/pole/tanech/p000.jpg",  # ← первая картинка из Ani_jpg

	# Сон в классе
	"nightmare_klass0":     "res://images/locate/school/in_side/ahaha/klass_00.jpg",
	"children_in_class_rem":  "res://images/locate/school/in_side/ahaha/child/klass_05.png",
	"children_in_class_rem2": "res://images/locate/school/in_side/ahaha/child/klass_01.png",
	"old_movie_intense": {
		"layers": [
			{
				"frames": [
					{"path": "res://images/effect/old_movie/old_movie_001.png", "time": 0.10},
					{"null": true, "time": 0.20},
					{"path": "res://images/effect/old_movie/old_movie_002.png", "time": 0.10},
					{"null": true, "time": 0.70},
					{"path": "res://images/effect/old_movie/old_movie_003.png", "time": 0.10},
					{"null": true, "time": 0.20},
					{"path": "res://images/effect/old_movie/old_movie_004.png", "time": 0.10},
					{"null": true, "time": 0.70},
				],
				"loop": true,
			},
		],
	},
	"d4_noise": {
		"layers": [
			{
				"frames": [
					{"path": "res://images/locate/polina/polin_yard/noise/01.png", "time": 0.1},
					{"path": "res://images/locate/polina/polin_yard/noise/02.png", "time": 0.1},
					{"path": "res://images/locate/polina/polin_yard/noise/03.png", "time": 0.1},
					{"path": "res://images/locate/polina/polin_yard/noise/04.png", "time": 0.1},
				],
				"loop": true,
			},
		],
	},

	# Телефон
	"d5_phone_bg":          "res://images/locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg",
	"d5_phone_off":         "res://images/locate/home/in_side/1st_floor/hall/h1/prih_002.png",
	"polina_call_pickedup": {
		"layers": [
			"res://locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg",
			"res://locate/home/in_side/1st_floor/hall/h1/prih_004.png"
			]
	}
}

			

# ==================== API ====================

func set_parent(node: Control) -> void:
	stage_parent = node

func show(alias: String) -> void:
	_do_show(alias, false, -1.0)


## Внутренний показ.
## skip_group_hide — не снимать другие изображения той же группы.
## forced_alpha — если >= 0, принудительно ставит эту alpha (для кроссфейдов).
func _do_show(alias: String, skip_group_hide: bool, forced_alpha: float = -1.0) -> Control:
	var def: Dictionary = _resolve(alias)
	
	var group_name: String = str(def.get("group", ""))
	if not skip_group_hide and not group_name.is_empty():
		for active_alias in _active.keys().duplicate():
			if active_alias == alias:
				continue
			var active_def: Dictionary = _resolve(str(active_alias))
			if str(active_def.get("group", "")) == group_name:
				hide(active_alias, 0.0)

	# Прямой hex-цвет в диалоге: do StageManager.show("#F8F8FF")
	if def.is_empty() and alias.begins_with("#"):
		def = {"color": alias, "alpha": 1.0}

	if def.is_empty():
		push_error("[Stage] Нет определения: " + alias)
		return
	if stage_parent == null:
		push_error("[Stage] stage_parent не задан. Вызови Stage.set_parent($StageLayer).")
		return

	# Убираем старый инстанс, если есть — с корректной очисткой твина.
	if _active.has(alias):
		if _tweens.has(alias) and is_instance_valid(_tweens[alias]):
			_tweens[alias].kill()
		_tweens.erase(alias)
		if is_instance_valid(_active[alias]):
			_active[alias].queue_free()
		_active.erase(alias)

	var vp: Vector2 = stage_parent.size
	if vp.x <= 0.0 or vp.y <= 0.0:
		vp = get_viewport().get_visible_rect().size

	var align := Vector2(
		float(def.get("xalign", 0.5)),
		float(def.get("yalign", 0.5))
	)
	var zoom: float = float(def.get("zoom", 1.0))

	# --- Создаём визуал: composite / ColorRect / TextureRect ---
	var rect: Control
	var natural_size: Vector2
	var is_color: bool = def.has("color")
	var is_composite: bool = def.has("layers")

	if is_composite:
		var comp := _create_composite(alias, def.get("layers", []), vp)
		if comp.is_empty():
			return
		rect = comp.node
		natural_size = comp.size
	elif is_color:
		var hex: String = str(def.get("color", "#000000"))
		var cr := ColorRect.new()
		cr.color = Color.html(hex)
		rect = cr
		natural_size = vp
	else:
		var path: String = str(def.get("path", ""))
		var tex: Texture2D = _load_texture(path)
		if tex == null:
			push_error("[Stage] Не найдена текстура: " + path)
			return
		var tr := TextureRect.new()
		tr.texture = tex
		tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		rect = tr
		natural_size = tex.get_size()

	rect.name = alias
	rect.mouse_filter = Control.MOUSE_FILTER_IGNORE

	rect.size = natural_size
	rect.pivot_offset = natural_size * align
	rect.position = (vp - natural_size) * align
	rect.scale = Vector2.ONE * zoom
	if forced_alpha >= 0.0:
		rect.modulate.a = forced_alpha
	else:
		rect.modulate.a = float(def.get("alpha", 1.0))
	
	if def.has("shader"):
		var shader_path: String = str(def.get("shader", ""))
		var mat: Material = _load_material(shader_path)
		if mat:
			rect.material = mat
		else:
			push_warning("[Stage] Не удалось загрузить шейдер: " + shader_path)
	
	stage_parent.add_child(rect)
	_active[alias] = rect

	# --- Анимации ---
	var steps: Array = def.get("parallel", [])
	var trans: Dictionary = def.get("transition", {})
	
	if forced_alpha < 0.0:
		if not steps.is_empty():
			_tweens[alias] = _apply_parallel(rect, steps)
		elif not trans.is_empty():
			_tweens[alias] = _apply_parallel(rect, [trans])

	if not steps.is_empty():
		_tweens[alias] = _apply_parallel(rect, steps)
	elif not trans.is_empty():
		_tweens[alias] = _apply_parallel(rect, [trans])

	var what: String
	if is_composite:
		what = "composite[%d]" % (def.get("layers", []) as Array).size()
	elif is_color:
		what = "color " + str(def.get("color"))
	else:
		what = "→ " + str(def.get("path"))
	print("[Stage] show '%s' %s" % [alias, what])
	return rect

## Кроссфейд внутри группы: старое изображение группы гаснет параллельно
## с проявлением нового. Никаких «мёртвых» кадров.
func show_dissolve(alias: String, fade_time: float = 0.3) -> void:
	var def: Dictionary = _resolve(alias)
	if def.is_empty():
		push_error("[Stage] Нет определения: " + alias)
		return
	
	var group_name: String = str(def.get("group", ""))
	var old_nodes: Array = []
	if not group_name.is_empty():
		for active_alias in _active.keys().duplicate():
			if active_alias == alias:
				continue
			var active_def: Dictionary = _resolve(str(active_alias))
			if str(active_def.get("group", "")) == group_name:
				old_nodes.append({"alias": active_alias, "rect": _active[active_alias]})
				_active.erase(active_alias)
	
	var new_rect: Control = _do_show(alias, true, 0.0)
	if new_rect == null:
		return
	
	if _tweens.has(alias) and is_instance_valid(_tweens[alias]):
		_tweens[alias].kill()
		_tweens.erase(alias)
	
	var t := create_tween()
	t.set_parallel(true)
	t.tween_property(new_rect, "modulate:a", 1.0, fade_time)
	for entry in old_nodes:
		var old_rect: Control = entry.rect
		if is_instance_valid(old_rect):
			t.tween_property(old_rect, "modulate:a", 0.0, fade_time)
	
	t.chain()
	t.tween_callback(func():
		for entry in old_nodes:
			var old_rect: Control = entry.rect
			if is_instance_valid(old_rect):
				old_rect.queue_free()
	)
	
	_tweens[alias] = t
	

func hide(alias: String, fade_time: float = 0.0) -> void:
	if not _active.has(alias):
		return
	if _tweens.has(alias) and is_instance_valid(_tweens[alias]):
		_tweens[alias].kill()
		_tweens.erase(alias)

	var rect: Control = _active[alias]
	_active.erase(alias)

	if not is_instance_valid(rect):
		return

	if fade_time > 0.0:
		var t := rect.create_tween()
		t.tween_property(rect, "modulate:a", 0.0, fade_time)
		t.tween_callback(func():
			if is_instance_valid(rect):
				rect.queue_free()
		)
	else:
		rect.queue_free()

func hide_all(fade_time: float = 0.0) -> void:
	for a in _active.keys().duplicate():
		hide(a, fade_time)

func show_window():
	print("[Stage] Show Window Init")
	get_node("/root/NovelScene/UI/Window").show()

func hide_window(timer : int = 0):
	print("[Stage] Hide Window Init")
	if not Input.is_action_pressed("Space"):
		hide_window(timer)
	get_node("/root/NovelScene/UI/Window").hide()
	if timer > 0:
		await get_tree().create_timer(timer).timeout
		get_node("/root/NovelScene/UI/Window").show()
		print("[Stage] Window Showed with timer: %s" % timer)

func pause(timer : int = 1):
	await get_tree().create_timer(timer).timeout
# ==================== ВНУТРЕННЕЕ ====================

func _resolve(alias: String) -> Dictionary:
	if not IMAGES.has(alias):
		return {}
	var def = IMAGES[alias]

	if def is String:
		if (def as String).begins_with("#"):
			return {"color": def, "alpha": 1.0}
		return {"path": def, "alpha": 1.0}

	var result: Dictionary = {}
	if def.has("based_on"):
		result.merge(_resolve(str(def.based_on)))
	for key in def:
		if key == "based_on":
			continue
		result[key] = def[key]
	return result

func _load_texture(path: String) -> Texture2D:
	if _cache.has(path):
		return _cache[path]
	if not ResourceLoader.exists(path):
		return null
	var tex: Texture2D = load(path)
	if tex:
		_cache[path] = tex
	return tex

func _apply_parallel(rect: Control, steps: Array) -> Tween:
	var t := rect.create_tween()
	t.set_parallel(true)

	for step in steps:
		if not step is Dictionary:
			continue
		var time: float = float(step.get("time", 1.0))
		var ease_name: String = str(step.get("ease", "linear"))
		var trans: Tween.TransitionType = _ease_to_trans(ease_name)
		var ease: Tween.EaseType = _ease_to_ease(ease_name)

		if step.has("alpha"):
			t.tween_property(rect, "modulate:a", float(step.alpha), time) \
				.set_trans(trans).set_ease(ease)
		
		if step.has("modulate"):
			var m: Dictionary = step.modulate
			var target := Color(
				float(m.get("r", 1.0)),
				float(m.get("g", 1.0)),
				float(m.get("b", 1.0)),
				float(m.get("a", 1.0))
			)
			t.tween_property(rect, "modulate", target, time) \
				.set_trans(trans).set_ease(ease)
			
		if step.has("zoom"):
			t.tween_property(rect, "scale", Vector2.ONE * float(step.zoom), time) \
				.set_trans(trans).set_ease(ease)

		if step.has("offset_x") or step.has("offset_y"):
			var delta := Vector2(
				float(step.get("offset_x", 0.0)),
				float(step.get("offset_y", 0.0))
			)
			t.tween_property(rect, "position", rect.position + delta, time) \
				.set_trans(trans).set_ease(ease)
	return t

func _ease_to_trans(e: String) -> Tween.TransitionType:
	match e:
		"linear": return Tween.TRANS_LINEAR
		"ease", "ease_in", "ease_out", "ease_in_out": return Tween.TRANS_SINE
		"back": return Tween.TRANS_BACK
		"elastic": return Tween.TRANS_ELASTIC
		"cubic": return Tween.TRANS_CUBIC
		"expo": return Tween.TRANS_EXPO
		_: return Tween.TRANS_LINEAR

func _ease_to_ease(e: String) -> Tween.EaseType:
	match e:
		"ease_in": return Tween.EASE_IN
		"ease_out": return Tween.EASE_OUT
		_: return Tween.EASE_IN_OUT


func _load_material(path: String) -> Material:
	if path.is_empty():
		return null
	if _cache.has(path):
		return _cache[path]
	if not ResourceLoader.exists(path):
		push_error("[Stage] Файл шейдера не существует: " + path)
		return null
	var res: Resource = load(path)
	if res is Material:
		_cache[path] = res
		return res
	push_error("[Stage] '%s' не является Material (got %s)" % [path, res.get_class() if res else "null"])
	return null
	
	
## Ren'Py `scene`: скрывает всё старое и показывает новое.
## При fade_time > 0 делает кроссфейд: старое гаснет, новое проявляется — параллельно.
func scene(alias: String, fade_time: float = 0.0) -> void:
	if fade_time <= 0.0:
		hide_all(0.0)
		show(alias)
		return
	
	var old_keys: Array = _active.keys().duplicate()
	var new_rect: Control = _do_show(alias, false, 0.0)
	if new_rect == null:
		hide_all(0.0)
		show(alias)
		return
	
	if _tweens.has(alias) and is_instance_valid(_tweens[alias]):
		_tweens[alias].kill()
		_tweens.erase(alias)
	
	for k in old_keys:
		if k == alias:
			continue
		hide(k, fade_time)
	
	var t := create_tween()
	t.tween_property(new_rect, "modulate:a", 1.0, fade_time)
	_tweens[alias] = t
	await t.finished


## Показать несколько изображений одним dissolve-переходом.
## aliases — все алиасы для показа (проявляются одновременно).
## fade_time — длительность dissolve.
## backdrop — алиас непрозрачной подложки (например "bg_white").
##            Кладётся поверх старого, чтобы сквозь новые слои
##            не просвечивал старый фон.
func scene_multi(aliases: Array, fade_time: float = 0.0, backdrop: String = "") -> void:
	if aliases.is_empty():
		return
	
	if fade_time <= 0.0:
		hide_all(0.0)
		for a in aliases:
			show(str(a))
		return
	
	# 1. Мгновенно убрать всё старое
	hide_all(0.0)
	
	# 2. Подложка через обычный show() — он сам вычислит размер
	#    через IMAGES (is_color → natural_size = vp с fallback).
	var backdrop_node: Control = null
	if not backdrop.is_empty():
		show(backdrop)
		backdrop_node = _active.get(backdrop)
		# Убить автотвин, если у подложки был transition
		if backdrop_node and _tweens.has(backdrop):
			if is_instance_valid(_tweens[backdrop]):
				_tweens[backdrop].kill()
			_tweens.erase(backdrop)
			backdrop_node.modulate.a = 1.0
	
	# 3. Новые с alpha=0, поверх подложки
	var new_rects: Array = []
	for a in aliases:
		var r: Control = _do_show(str(a), true, 0.0)
		if r:
			new_rects.append(r)
	
	# 4. Проявить новые параллельно
	var t := create_tween().set_parallel(true)
	for r in new_rects:
		t.tween_property(r, "modulate:a", 1.0, fade_time)
	await t.finished
	
	# 5. Убрать подложку — всё новое уже непрозрачно
	if backdrop_node and is_instance_valid(backdrop_node):
		_active.erase(backdrop)
		backdrop_node.queue_free()
	

## Ren'Py-эквивалент `scene X with Dissolve(t)` через «шторку»:
## все новые элементы появляются мгновенно и непрозрачными,
## поверх них кладётся непрозрачная шторка (например bg_white),
## шторка плавно уходит — обнажая готовую сцену. 
## Ничего не проявляется сквозь ничего.
func reveal_scene(aliases: Array, curtain: String, fade_time: float = 1.0) -> void:
	if aliases.is_empty():
		return
	
	# 1. Убить старую шторку, если она висит с прошлого раза
	if _active.has(curtain):
		if _tweens.has(curtain) and is_instance_valid(_tweens[curtain]):
			_tweens[curtain].kill()
			_tweens.erase(curtain)
		var old_c: Control = _active[curtain]
		_active.erase(curtain)
		if is_instance_valid(old_c):
			old_c.queue_free()
	
	# 2. Запомнить всё, что активно сейчас (старый фон и т.д.)
	var old_entries: Array = []
	for k in _active.keys():
		old_entries.append({"alias": str(k), "rect": _active[k]})
	
	# 3. Показать все новые мгновенно и непрозрачно
	var new_set: Dictionary = {}
	for a in aliases:
		new_set[str(a)] = true
		_do_show(str(a), true, 1.0)
	
	# 4. Удалить старые (кроме тех, что мы только что показали)
	for entry in old_entries:
		var a: String = entry.alias
		if new_set.has(a):
			continue
		var r: Control = entry.rect
		if _active.has(a) and _active[a] == r:
			_active.erase(a)
		if is_instance_valid(r):
			r.queue_free()
	
	# 5. Шторка поверх — через show(), чтобы получить правильный размер
	show(curtain)
	var curtain_rect: Control = _active.get(curtain)
	if curtain_rect == null:
		return
	if _tweens.has(curtain) and is_instance_valid(_tweens[curtain]):
		_tweens[curtain].kill()
		_tweens.erase(curtain)
	curtain_rect.modulate.a = 1.0
	
	# 6. Гасим шторку — под ней уже готовая кухня с персонажами
	var t := create_tween()
	t.tween_property(curtain_rect, "modulate:a", 0.0, fade_time)
	await t.finished
	
	# 7. Удаляем шторку
	_active.erase(curtain)
	if is_instance_valid(curtain_rect):
		curtain_rect.queue_free()


## Ren'Py-семантика `scene X with Dissolve(t)`:
## Новое проявляется поверх, старое параллельно гаснет. Без «мёртвых» кадров.
## Новое изображение создаётся сразу прозрачным — никакого мгновенного появления.
func crossfade(alias: String, fade_time: float = 1.0) -> void:
	var old_keys: Array = _active.keys().duplicate()
	
	var new_rect: Control = _do_show(alias, false, 0.0)
	if new_rect == null:
		return
	
	if _tweens.has(alias) and is_instance_valid(_tweens[alias]):
		_tweens[alias].kill()
		_tweens.erase(alias)
	
	for k in old_keys:
		if k == alias:
			continue
		hide(k, fade_time)
	
	var t := create_tween()
	t.tween_property(new_rect, "modulate:a", 1.0, fade_time)
	_tweens[alias] = t
	await t.finished

## Создаёт Control-контейнер с наложенными друг на друга TextureRect-слоями.
## Аналог Ren'Py LiveComposite((w, h), (0,0), "a.png", (0,0), "b.png", ...).
##
## Слой может быть:
##   1) строка "res://path.png"                    — статичный в (0, 0)
##   2) словарь {"path": "...", "offset": [x, y]}  — статичный со сдвигом
##   3) словарь {"frames": [...], "loop": true}    — анимированный
func _create_composite(alias: String, layers: Array, vp: Vector2) -> Dictionary:
	if layers.is_empty():
		push_error("[Stage] Composite '%s' не содержит слоёв" % alias)
		return {}

	var root := Control.new()
	root.name = alias
	root.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.position = Vector2.ZERO

	var max_size := Vector2.ZERO
	var loaded_count: int = 0

	for i in layers.size():
		var entry = layers[i]
		var node: Control = null

		# --- 1) строка ---
		if entry is String:
			var path: String = entry
			var tex := _load_texture(path)
			if tex == null:
				push_error("[Stage] Composite '%s': слой %d не найден — %s"
					% [alias, i, path])
				continue
			var tr := TextureRect.new()
			tr.name = "layer_%d" % i
			tr.texture = tex
			tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
			tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
			tr.mouse_filter = Control.MOUSE_FILTER_IGNORE
			tr.position = Vector2.ZERO
			tr.size = tex.get_size()
			node = tr

		# --- 2/3) словарь ---
		elif entry is Dictionary:
			var ed := entry as Dictionary
			if ed.has("frames"):
				# Анимированный слой
				var anim := _make_animated_layer(ed)
				var off = ed.get("offset", null)
				if off is Array and off.size() >= 2:
					anim.position = Vector2(float(off[0]), float(off[1]))
				elif off is Vector2:
					anim.position = off
				node = anim
			else:
				# Статичный слой с offset
				var path: String = str(ed.get("path", ""))
				var tex := _load_texture(path)
				if tex == null:
					push_error("[Stage] Composite '%s': слой %d не найден — %s"
						% [alias, i, path])
					continue
				var tr := TextureRect.new()
				tr.name = "layer_%d" % i
				tr.texture = tex
				tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
				tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
				tr.mouse_filter = Control.MOUSE_FILTER_IGNORE
				var off = ed.get("offset", null)
				if off is Array and off.size() >= 2:
					tr.position = Vector2(float(off[0]), float(off[1]))
				elif off is Vector2:
					tr.position = off
				tr.size = tex.get_size()
				node = tr

		if node == null:
			push_warning("[Stage] Composite '%s': слой %d — неизвестный формат, пропускаю"
				% [alias, i])
			continue

		root.add_child(node)
		var extent: Vector2 = node.position + node.size
		max_size.x = maxf(max_size.x, extent.x)
		max_size.y = maxf(max_size.y, extent.y)
		loaded_count += 1

	if loaded_count == 0:
		push_error("[Stage] Composite '%s': ни один слой не загрузился" % alias)
		root.queue_free()
		return {}

	if max_size.x <= 0.0 or max_size.y <= 0.0:
		max_size = vp

	root.size = max_size

	print("[Stage] composite '%s': %d/%d слоёв, size=%s"
		% [alias, loaded_count, layers.size(), max_size])

	return {"node": root, "size": max_size}
	

## Создаёт TextureRect, циклически меняющий текстуру по расписанию кадров.
## Формат def:
##   { "frames": [{"path": "...", "time": 0.1}, ...], "loop": true }
##
## Кадр может быть:
##   {"path": "res://...", "time": 0.1}   — статичный кадр
##   {"null": true, "time": 0.2}          — пустой кадр (изображение скрыто)
##   {"path": null, "time": 0.2}          — то же самое
##   null                                 — пустой кадр (time = 0.1 по умолчанию)
func _make_animated_layer(def: Dictionary) -> TextureRect:
	var tr := TextureRect.new()
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	tr.mouse_filter = Control.MOUSE_FILTER_IGNORE

	var frames: Array = def.get("frames", [])
	if frames.is_empty():
		push_warning("[Stage] animated layer без frames")
		return tr

	# Первый кадр сразу (может быть Null → просто остаёмся прозрачными)
	var first = frames[0]
	if not _is_null_frame(first):
		var first_path: String = str((first as Dictionary).get("path", ""))
		var first_tex := _load_texture(first_path)
		if first_tex:
			tr.texture = first_tex
			tr.size = first_tex.get_size()

	# Циклический Tween
	var loop: bool = bool(def.get("loop", true))
	var t := tr.create_tween()
	if loop:
		t.set_loops()

	for i in frames.size():
		var f = frames[i]
		var wait: float = 0.1
		if f is Dictionary:
			wait = float(f.get("time", 0.1))

		var next = frames[(i + 1) % frames.size()]
		var next_is_null: bool = _is_null_frame(next)
		var next_path: String = ""
		if not next_is_null and next is Dictionary:
			next_path = str(next.get("path", ""))

		t.tween_interval(wait)
		t.tween_callback(func():
			if next_is_null:
				# Null(): «убираем» изображение — на это время экран чист
				tr.texture = null
			else:
				var tex := _load_texture(next_path)
				if tex:
					tr.texture = tex
					tr.size = tex.get_size()
		)

	return tr


## Проверяет, является ли кадр «пустым» (Ren'Py Null()).
## Поддерживает: null, {"null": true}, {"path": null}, {"path": ""}
static func _is_null_frame(f) -> bool:
	if f == null:
		return true
	if f is Dictionary:
		var d := f as Dictionary
		if bool(d.get("null", false)):
			return true
		var p = d.get("path", null)
		if p == null:
			return true
		if p is String and (p as String).is_empty():
			return true
	return false
