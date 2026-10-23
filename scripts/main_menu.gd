extends Control

const LOGO_FRAMES := ["002", "003", "004", "005", "006", "007"]
const FADE_TIME := 0.5

func _ready() -> void:
	$bg_black.show()
	await get_tree().create_timer(1.0).timeout
	$Logo.show()
	$Disclaimer.show()
	await get_tree().create_timer(8.0).timeout

	# --- Fade out Disclaimer через твин ---
	$Disclaimer.modulate.a = 1.0
	AudioManager.play_sfx("res://sounds/logo.ogg")

	var disclaimer_tween := create_tween()
	disclaimer_tween.tween_property($Disclaimer, "modulate:a", 0.0, 1.0)
	await disclaimer_tween.finished

	# --- Пробегаем кадры лого ---
	for frame in LOGO_FRAMES:
		$Logo.texture = load("res://images/logo/%s.jpg" % frame)
		await get_tree().create_timer(0.1).timeout
	await get_tree().create_timer(0.5).timeout

	$Disclaimer.queue_free()
	$bg_black.hide()

	# --- Подключаем кнопки ---
	var new_game_btn: ChoiceButton = $UI/HBoxContainer/MainUI/HBoxContainer/ButtonContainer/NewGame
	var quit_btn: ChoiceButton     = $UI/HBoxContainer/MainUI/HBoxContainer/ButtonContainer/Exit

	new_game_btn.connect("choice_pressed",
		_matcher(ChoiceButton.Command.NEWGAME, new_game_btn.command_args))
	quit_btn.connect("choice_pressed",
		_matcher(ChoiceButton.Command.QUIT, PackedStringArray()))

	AudioManager.play_music("res://music/Menu_Tiny_Bunny.ogg")

	# --- Затухание лого через твин ---
	var logo_tween := create_tween()
	logo_tween.tween_property($Logo, "modulate:a", 0.0, 2.0)
	await logo_tween.finished
	$Logo.queue_free()


# cmd — enum ChoiceButton.Command, args — command_args из самой кнопки.
# Лямбда принимает те же 2 аргумента, что приходят от сигнала (иначе GDScript ругается),
# но матчим по переданному нами cmd, а не по тому, что пришло из сигнала.
func _matcher(cmd: int, _args: PackedStringArray) -> Callable:
	return func(_sig_cmd: int, _sig_args: PackedStringArray) -> void:
		match cmd:
			ChoiceButton.Command.NEWGAME:
				AudioManager.stop_music(-3)
				await _fade_out()
				get_tree().change_scene_to_file("res://scripts/scene/scene_day_1.tscn")
			ChoiceButton.Command.QUIT:
				await _fade_out()
				get_tree().quit()
			_:
				push_warning("Unknown command: %s" % cmd)


func _fade_out() -> void:
	$bg_black["modulate"] = Color(00000000)
	$bg_black.show()
	var tween := create_tween()
	tween.tween_property($bg_black, "modulate:a", 1.0, FADE_TIME)
	await tween.finished
