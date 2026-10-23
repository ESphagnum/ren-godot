extends TextureButton
class_name ChoiceButton

var glitch_tween : Tween
var shake_tween : Tween

var original_position : Vector2
var position_saved : bool = false
var is_custom_hovered : bool = false
var execution_context: Object = null

@export var label_text : String = "Текст"
enum Command {
	NEWGAME,
	LOAD,
	SAVE,
	QUIT,
	SETTINGS,
	RESUME,
	CUSTOM,
}

@export var command: Command = Command.NEWGAME:
	set(v):
		command = v
@export var command_args: PackedStringArray = []
@export var hover_sound : String = "res://sounds/menu/menu-button-select-1.ogg"
@export var click_sound : String = "res://sounds/menu/menu-button-click-1.ogg"
@export var fade_in_on_hover_only: bool = false


signal choice_pressed(cmd: Command, args: PackedStringArray)

func _ready() -> void:
	setup_label()
	if fade_in_on_hover_only:
		self_modulate.a = 0.0
	if $Label.text.is_empty():
		$Label.text = label_text

func setup_label() -> void:
	var label: Label = get_node_or_null("Label") as Label
	if label == null:
		push_error("[ChoiceButton] Label не найден в choice_button.tscn!")
		return
	label.set_anchors_preset(Control.PRESET_FULL_RECT)
	label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	label.mouse_filter = Control.MOUSE_FILTER_IGNORE

func _on_mouse_entered() -> void:
	is_custom_hovered = true
	AudioManager.play_sfx(hover_sound)
	
	if not position_saved:
		original_position = position
		position_saved = true
	
	_kill_tweens()
	
	var fade_tween = create_tween()
	fade_tween.tween_property(self, "self_modulate:a", 1.0, 0.35)
	
	_start_glitch_loop()
	_start_shake_loop()
	$Label.modulate = Color(0, 0, 0, 1)

func _on_mouse_exited() -> void:
	is_custom_hovered = false
	
	if not position_saved:
		original_position = position
	
	_kill_tweens()
	

	var fade_black = create_tween()
	fade_black.set_parallel(true)
	fade_black.tween_property(self, "self_modulate:a", 0.0, 0.25).from_current()
	fade_black.tween_property(self, "position", original_position, 0.25)
	$Label.modulate = Color(1, 1, 1, 1)

func _start_glitch_loop():
	if not is_custom_hovered: return
	
	await get_tree().create_timer(10.0).timeout
	
	if not is_custom_hovered: return
	
	glitch_tween = create_tween()
	glitch_tween.tween_property(self, "self_modulate:a", 0.2, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.7, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.4, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.1, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.2, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.7, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.4, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.1, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 0.3, 0.05)
	glitch_tween.tween_property(self, "self_modulate:a", 1.0, 0.05)
	
	await glitch_tween.finished
	await get_tree().create_timer(6.0).timeout
	
	_start_glitch_loop()

func _start_shake_loop():
	if not is_custom_hovered: return
	
	shake_tween = create_tween()
	for i in range(18):
		var random_offset = Vector2(randf_range(-5, 5), randf_range(-5, 5))
		shake_tween.tween_property(self, "position", original_position + random_offset, 0.01)

	shake_tween.tween_property(self, "position", original_position, 0.01)

func _kill_tweens():
	if is_instance_valid(glitch_tween) and glitch_tween.is_valid():
		glitch_tween.kill()
	if is_instance_valid(shake_tween) and shake_tween.is_valid():
		shake_tween.kill()

func set_text(t: String) -> void:
	if $Label == null:
		push_warning("[ChoiceButton] Label не найден по пути %s" % $Label.get_path())
		return
	$Label.text = t

func get_text() -> String:
	return $Label.text if $Label else ""

func _on_pressed() -> void:
	AudioManager.play_sfx(click_sound)
	emit_signal("choice_pressed", command, command_args)
