extends Control

## Скрипт-движок для визуальной новеллы.
## Управляет отображением диалога, именем персонажа и обработкой ввода.

# --- Экспортируемые переменные ---
## Сюда нужно перетащить твой .dialogue файл из FileSystem.
var dialogue_resource: DialogueResource = preload("res://scripts/scene/day_1.dialogue")
## Метка (label), с которой начнется диалог. В .dialogue файлах это строка после ~.
@export var start_label: String = "start"
@export var default_choice_layout: String = "center"
@export var choice_button_scene: PackedScene
var _current_choice_layout: String = "center"

# --- Ссылки на узлы сцены ---
@onready var background: TextureRect = $Background
@onready var window: TextureRect = $UI/Window
@onready var quick_close: TextureButton = $UI/Window/QuickClose
@onready var name_label: Label = $UI/Window/NameBox/Name
@onready var name_box: TextureRect = $UI/Window/NameBox
@onready var name_box_outline: TextureRect = $UI/Window/NameBoxOutline
@onready var text_label: Label = $UI/Window/Text
@onready var response_container: VBoxContainer = $UI/VBoxContainer
@onready var character_manager: CharacterManager = get_node("/root/Characters")

signal _continue_clicked

# --- Layout-пресеты для кнопок выбора ---
## anchor — точка на экране, к которой привязываем (0..1)
## origin — точка внутри VBox, которая совмещается с anchor (0..1)
## button_size — минимальный размер одной кнопки
## separation — отступ между кнопками
const CHOICE_LAYOUTS := {
	"center": {
		"anchor": Vector2(0.5, 0.5),
		"origin": Vector2(0.5, 0.5),
		"button_size": Vector2(600, 90),
		"separation": 25,
	},
	"bottom_center": {
		"anchor": Vector2(0.5, 0.92),
		"origin": Vector2(0.5, 1.0),
		"button_size": Vector2(700, 80),
		"separation": 15,
	},
	"bottom_left": {
		"anchor": Vector2(0.05, 0.92),
		"origin": Vector2(0.0, 1.0),
		"button_size": Vector2(500, 80),
		"separation": 15,
	},
	"bottom_right": {
		"anchor": Vector2(0.95, 0.92),
		"origin": Vector2(1.0, 1.0),
		"button_size": Vector2(500, 80),
		"separation": 15,
	},
	"top_left": {
		"anchor": Vector2(0.05, 0.08),
		"origin": Vector2(0.0, 0.0),
		"button_size": Vector2(500, 80),
		"separation": 15,
	},
	"top_right": {
		"anchor": Vector2(0.95, 0.08),
		"origin": Vector2(1.0, 0.0),
		"button_size": Vector2(500, 80),
		"separation": 15,
	},
	"left_middle": {
		"anchor": Vector2(0.03, 0.5),
		"origin": Vector2(0.0, 0.5),
		"button_size": Vector2(420, 75),
		"separation": 12,
	},
	"right_middle": {
		"anchor": Vector2(0.97, 0.5),
		"origin": Vector2(1.0, 0.5),
		"button_size": Vector2(420, 75),
		"separation": 12,
	},
}

# --- Внутреннее состояние ---
var _current_line: DialogueLine = null
var _is_waiting_for_input: bool = false

func _ready() -> void:
	window.hide()
	response_container.hide()
	quick_close.pressed.connect(_on_quick_close_pressed)

## Запускает диалог с указанной метки.
func start_dialogue(res: DialogueResource, label: String = "start") -> void:
	if not res:
		push_error("NovelScene: dialogue_resource == null")
		return
	dialogue_resource = res
	start_label = label
	#window.show()
	_current_line = await DialogueManager.get_next_dialogue_line(
		dialogue_resource,
		start_label,
		_get_extra_states()
	)
	_display_line()


## Отображает текущую строку диалога (имя и текст).
func _display_line() -> void:
	if _current_line == null:
		_end_dialogue()
		return
	
	# --- Обновляем имя персонажа ---
	if _current_line.character.is_empty() or _current_line.character == "Автор":
		name_label.text = ""
		name_box.hide()
		name_box_outline.hide()
	else:
		name_label.text = sys.name_check_and_replace(_current_line.character)
		name_box.show()
		name_box_outline.show()
		
	if character_manager and not _current_line.character.is_empty():
		# Имена спрайтов должны совпадать с именами персонажей в Dialogue Manager
		if character_manager.has_character(_current_line.character):
			character_manager.focus_character(_current_line.character)
	
	# --- Обновляем текст диалога ---
	# В твоей сцене "Text" — это Label. DialogueLine.text — это строка.
	#text_label.text = "\u0022" + _current_line.text + "\u0022"
	text_label.text = ""
	var tween : Tween = create_tween()
	var scrap_text : String
	if _current_line.text[0] == "\u0022" and _current_line.text[-1] == "\u0022":
		scrap_text = _current_line.text
	else:
		scrap_text = "\u0022" + _current_line.text + "\u0022"
	tween.tween_property(text_label, "text", scrap_text, 1)
	tween.finished
	#var m = []
	#m.clear()
	#for i in range(len(_current_line.text)):
		#m.append(_current_line.text[i])
		#text_label.text = "\u0022" + array_to_string(m) + "\u0022"
		#
	
	
	# --- Обрабатываем ответы (если есть) ---
	if _current_line.responses.size() > 0:
		_show_responses(_current_line.responses)
	else:
		_is_waiting_for_input = true

## Создает кнопки для вариантов ответа.
func _show_responses(responses: Array) -> void:
	_clear_responses()
	
	for response in responses:
		if response.is_allowed:
			var button := _create_choice_button(response)
			response_container.add_child(button)
	
	if response_container.get_child_count() > 0:
		response_container.show()
		_apply_choice_layout(_current_choice_layout)
		_is_waiting_for_input = false

		var first: Node = response_container.get_child(0)
		if first is Control:
			(first as Control).grab_focus()
		else:
			# Фолбэк: ищем первый BaseButton внутри сцены кнопки
			var btn: BaseButton = _find_first_button(first)
			if btn:
				btn.grab_focus()

func _apply_choice_layout(name: String) -> void:
	var layout: Dictionary = CHOICE_LAYOUTS.get(name, CHOICE_LAYOUTS["center"])
	var vp: Vector2 = get_viewport_rect().size
	var count: int = response_container.get_child_count()
	if count == 0:
		return

	var btn_size: Vector2 = layout.get("button_size", Vector2(500, 80))
	var sep: int = int(layout.get("separation", 20))
	var total_h: float = count * btn_size.y + (count - 1) * sep

	response_container.set_anchors_preset(Control.PRESET_TOP_LEFT)
	response_container.size = Vector2(btn_size.x, total_h)
	response_container.add_theme_constant_override("separation", sep)

	var anchor: Vector2 = layout.get("anchor", Vector2(0.5, 0.5))
	var origin: Vector2 = layout.get("origin", Vector2(0.5, 0.5))
	response_container.position = anchor * vp - origin * response_container.size

	# Все кнопки одного размера
	for child in response_container.get_children():
		if child is Control:
			var c := child as Control
			c.custom_minimum_size = btn_size
			c.size = btn_size
	
	for i in response_container.get_child_count():
		var c: Control = response_container.get_child(i)
		c.modulate.a = 0.0
		var t := create_tween()
		t.tween_interval(i * 0.06)
		t.tween_property(c, "modulate:a", 1.0, 0.25)

func _create_choice_button(response: DialogueResponse) -> Control:
	if choice_button_scene == null:
		push_error("[NovelScene] choice_button_scene не назначена в инспекторе!")
		var fallback := Button.new()
		fallback.text = response.text
		fallback.pressed.connect(_on_response_selected.bind(response))
		return fallback

	var btn: Control = choice_button_scene.instantiate()

	# --- Текст ---
	print("[BTN] root class = %s | has set_text = %s" % [btn.get_class(), btn.has_method("set_text")])
	if btn.has_method("set_text"):
		btn.set_text(response.text)
		print("[BTN] set_text called with: %s" % response.text)
	else:
		push_warning("[NovelScene] У choice_button.tscn нет метода set_text()")

	# --- Размер ---
	var layout: Dictionary = CHOICE_LAYOUTS.get(_current_choice_layout, CHOICE_LAYOUTS["center"])
	var btn_size: Vector2 = layout.get("button_size", Vector2(500, 80))
	btn.custom_minimum_size = btn_size
	btn.set_deferred("size", btn_size)     # ← через deferred, чтобы не было варнинга про анкоры

	# --- Сигнал ---
	if btn is BaseButton:
		(btn as BaseButton).pressed.connect(_on_response_selected.bind(response))
	else:
		var found_btn: BaseButton = _find_first_button(btn)
		if found_btn:
			found_btn.pressed.connect(_on_response_selected.bind(response))
		else:
			push_error("[NovelScene] В choice_button.tscn не найдено BaseButton!")

	return btn


## Рекурсивно ищет первый BaseButton в дереве узла.
func _find_first_button(node: Node) -> BaseButton:
	if node is BaseButton:
		return node
	for child in node.get_children():
		var found := _find_first_button(child)
		if found:
			return found
	return null

## Очищает контейнер с ответами.
func _clear_responses() -> void:
	for child in response_container.get_children():
		child.queue_free()
	response_container.hide()

## Вызывается при нажатии на кнопку ответа.
func _on_response_selected(response: DialogueResponse) -> void:
	_clear_responses()
	_advance_dialogue(response.next_id)

## Переходит к следующей строке диалога по указанному ID.
func _advance_dialogue(next_id: String) -> void:
	_is_waiting_for_input = false
	_current_line = await DialogueManager.get_next_dialogue_line(
		dialogue_resource,
		next_id,
		_get_extra_states()
	)
	_display_line()

## Список объектов, доступных из .dialogue файла как Game States.
## Ключ — имя, под которым узел виден в диалоге.
func _get_extra_states() -> Array:
	return [{"NovelScene": self}, character_manager]


## Завершает диалог и скрывает окно.
func _end_dialogue() -> void:
	window.hide()
	response_container.hide()
	_current_line = null
	_is_waiting_for_input = false

## Обработка ввода (клик или клавиша) для продвижения диалога.
func _input(event: InputEvent) -> void:
	# Клик для wait_for_click работает всегда — независимо от окна диалога
	if event.is_action_pressed("ui_accept") or \
	   (event is InputEventMouseButton and event.pressed):
		_continue_clicked.emit()

	# Продвижение диалога — только когда окно видимо и ждём ввода
	if not window.visible or not _is_waiting_for_input:
		return

	if event.is_action_pressed("ui_accept") or \
	   (event is InputEventMouseButton and event.pressed) or \
	   Input.is_action_pressed("Space"):
		if event is InputEventMouseButton:
			var mouse_pos := get_viewport().get_mouse_position()
			if quick_close.get_global_rect().has_point(mouse_pos):
				return
			if response_container.visible and \
			   response_container.get_global_rect().has_point(mouse_pos):
				return

		_is_waiting_for_input = false
		_advance_dialogue(_current_line.next_id)

## Обработчик кнопки закрытия окна.
func _on_quick_close_pressed() -> void:
	_end_dialogue()

## Публичный метод для смены фона (можно вызывать из диалога через мутации).
func set_background(texture: Texture2D) -> void:
	if background:
		background.texture = texture

func set_choice_layout(name: String) -> void:
	if not CHOICE_LAYOUTS.has(name):
		push_warning("[NovelScene] Неизвестный choice layout: %s. Остаётся '%s'." % [name, _current_choice_layout])
		return
	_current_choice_layout = name

## Приглушить музыку (0..1). 1.0 — полная громкость.
func music_duck(v: float) -> void:
	AudioManager.set_music_volume(v)
	if not AudioManager._fon_player.playing:
		return
	AudioManager.set_volume("Fon", v)

func invert_hex_string(hex_str: String) -> String:
	# Создаем объект Color из HEX-строки (поддерживает форматы #RGB, #RGBA, #RRGGBB, #RRGGBBAA)
	var color := Color(hex_str)
	
	# Инвертируем только каналы RGB, сохраняя оригинальную прозрачность (Alpha)
	var inverted_color := Color(1.0 - color.r, 1.0 - color.g, 1.0 - color.b, color.a)
	
	# Возвращаем в формате строки "#RRGGBB" (без альфа-канала)
	# Если нужен альфа-канал, используйте inverted_color.to_html(true)
	return "#" + inverted_color.to_html(false)


## Показать крупный текст по центру экрана (титул эпизода).
func show_chapter_title(text: String, hex_color: String, fade: float = 0.5) -> void:
	var lbl := Label.new()
	lbl.name = "_ChapterTitle"
	lbl.text = text
	lbl.set_anchors_preset(Control.PRESET_FULL_RECT)
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	lbl.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	lbl.add_theme_font_size_override("font_size", 64)
	lbl.label_settings = load("res://objects/russia_title_lableSettings.tres")
	if Color(hex_color): lbl.label_settings["font_color"] = hex_color
	if Color(hex_color): lbl.label_settings["outline_color"] = invert_hex_string(hex_color)
	lbl.modulate.a = 0.0
	lbl.mouse_filter = Control.MOUSE_FILTER_IGNORE
	$UI.add_child(lbl)
	var t := create_tween()
	t.tween_property(lbl, "modulate:a", 1.0, fade)
	await t.finished

## Скрыть титул.
func hide_chapter_title(fade: float = 0.5) -> void:
	var lbl: Label = $UI.get_node_or_null("_ChapterTitle")
	if lbl == null:
		return
	var t := create_tween()
	t.tween_property(lbl, "modulate:a", 0.0, fade)
	t.tween_callback(lbl.queue_free)
	await t.finished

## Ждать клика игрока. Аналог renpy `ui.interact()`.
func wait_for_click() -> void:
	await _continue_clicked
