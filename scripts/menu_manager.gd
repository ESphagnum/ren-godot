extends Node

## Глобальный менеджер кнопок выбора. Аналог Ren'Py `call screen`.
## Из .dialogue:  do Menus.show_menu("day1_book")
## После:        Menus.last_choice  → id нажатой кнопки

signal choice_made(choice_id: String)

const LAYER_NAME := "MenusLayer"
const LAYER_INDEX := 5   ## выше UI (2), выше CharacterLayer (1)

## Определения меню. Ключ — id меню, значение — словарь с полем "buttons".
## Каждая кнопка:
##   id            — возвращается в last_choice
##   text          — текст на кнопке
##   x, y, w, h    — позиция и размер в пикселях
##   font_size     — размер шрифта (по умолчанию 40)
##   hover_show    — массив алиасов StageManager, показать при наведении
##   hover_hide    — массив алиасов, скрыть при наведении
##   unhover_show  — массив алиасов, показать при уходе курсора
##   unhover_hide  — массив алиасов, скрыть при уходе курсора
const MENUS := {
	"day1_book": {
		"buttons": [
			{
				"id": "remove",
				"text": "УБРАТЬ",
				"x": 1000, "y": 870, "w": 245, "h": 100,
				"hover_show":   ["kitchen_ant2_book_bright"],
				"hover_hide":   ["kitchen_ant1_book"],
				"unhover_show": ["kitchen_ant1_book"],
				"unhover_hide": ["kitchen_ant2_book"],
			},
		],
	},
}

## Результат последнего показанного меню.
var last_choice: String = ""

var _layer: CanvasLayer
var _active_buttons: Array = []

func _ready() -> void:
	_layer = CanvasLayer.new()
	_layer.name = LAYER_NAME
	_layer.layer = LAYER_INDEX
	add_child(_layer)

# ==================== ПУБЛИЧНОЕ API ====================

## Показать меню по id. Ждёт клика игрока.
## Результат попадает в last_choice.
func show_menu(menu_id: String) -> void:
	if not MENUS.has(menu_id):
		push_error("[Menus] Нет меню: " + menu_id)
		return
	
	_clear()
	last_choice = ""
	
	var menu: Dictionary = MENUS[menu_id]
	var buttons: Array = menu.get("buttons", [])
	if buttons.is_empty():
		push_warning("[Menus] Меню '%s' пустое" % menu_id)
		return
	
	for btn_def in buttons:
		var btn: Control = _create_button(btn_def)
		if btn:
			_layer.add_child(btn)
			_active_buttons.append(btn)
	
	# Ждём любой выбор
	var chosen: String = await choice_made
	last_choice = chosen
	_clear()

## Скрыть меню без ожидания (если игрок ушёл другим путём).
func clear() -> void:
	_clear()

# ==================== ВНУТРЕННЕЕ ====================

func _create_button(def: Dictionary) -> Control:
	var btn := Button.new()
	btn.text = str(def.get("text", ""))
	btn.position = Vector2(float(def.get("x", 0)), float(def.get("y", 0)))
	var sz := Vector2(float(def.get("w", 240)), float(def.get("h", 80)))
	btn.custom_minimum_size = sz
	btn.size = sz
	btn.mouse_filter = Control.MOUSE_FILTER_STOP
	btn.focus_mode = Control.FOCUS_NONE

	# Стили — прозрачный idle, лёгкий белый при наведении
	var sb_normal := StyleBoxFlat.new()
	sb_normal.bg_color = Color(0, 0, 0, 0.0)
	sb_normal.set_border_width_all(0)
	btn.add_theme_stylebox_override("normal", sb_normal)

	var sb_hover := StyleBoxFlat.new()
	sb_hover.bg_color = Color(1, 1, 1, 0.18)
	sb_hover.set_corner_radius_all(3)
	btn.add_theme_stylebox_override("hover", sb_hover)
	btn.add_theme_stylebox_override("pressed", sb_hover)
	btn.add_theme_stylebox_override("focus", sb_hover)

	var fs: int = int(def.get("font_size", 40))
	btn.add_theme_color_override("font_color", Color.WHITE)
	btn.add_theme_color_override("font_hover_color", Color.WHITE)
	btn.add_theme_color_override("font_pressed_color", Color.WHITE)
	btn.add_theme_font_size_override("font_size", fs)

	var hover_show: Array   = def.get("hover_show", [])
	var hover_hide: Array   = def.get("hover_hide", [])
	var unhover_show: Array = def.get("unhover_show", [])
	var unhover_hide: Array = def.get("unhover_hide", [])

	btn.mouse_entered.connect(func() -> void:
		for a in hover_show:
			StageManager.show(str(a))
		for a in hover_hide:
			StageManager.hide(str(a))
	)
	btn.mouse_exited.connect(func() -> void:
		for a in unhover_show:
			StageManager.show(str(a))
		for a in unhover_hide:
			StageManager.hide(str(a))
	)

	var choice_id: String = str(def.get("id", ""))
	btn.pressed.connect(func() -> void:
		choice_made.emit(choice_id)
	)

	return btn


func _clear() -> void:
	for b in _active_buttons:
		if is_instance_valid(b):
			b.queue_free()
	_active_buttons.clear()
