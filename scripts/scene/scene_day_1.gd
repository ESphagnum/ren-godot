extends "res://scenes/novel_scene.gd"

const day1 = preload("res://scripts/scene/day_1.dialogue")

func _ready() -> void:
	StageManager.set_parent($StageLayer)
	$"Backgroud2".modulate.a = 0.0
	$UI.hide()
	AudioManager.play_fon("res://sounds/fon/001wind.ogg", 5.0)
	var tween = create_tween().set_parallel(true)
		
	tween.tween_property($"Background", "scale", Vector2(1.0, 1.0), 12)\
		.set_trans(Tween.TRANS_CUBIC)\
		.set_ease(Tween.EASE_OUT)
		
	var target_alpha: float = 0.0
	tween.tween_property($"Background/bg_black", "modulate:a", target_alpha, 12)\
		.set_trans(Tween.TRANS_SINE)\
		.set_ease(Tween.EASE_IN_OUT)
	$UI/Window/NameBox.hide()
	$UI/Window/NameBoxOutline.hide()
	$"Backgroud2".show()
	await tween.finished
	$UI.show()                # сначала показываем
	await get_tree().process_frame  # даём кадр, чтобы UI отрисовался
	start_dialogue(day1, "day1")    # потом стартуем
