extends TextureRect

const a = 1

func _draw() -> void:
	anim()

func anim() -> void:
	print("menu_002_1 ready")
	$".".position.x = 3960
	var tween = get_tree().create_tween().set_parallel(true)
	tween.tween_property($".", "position:x", 1980, 160)
	tween.tween_property($".", "position:x", 0, 160)
	$".".position.x = 0
	tween.tween_property($".", "position:x", -1981, 160)
	tween.tween_property($".", "position:x", -3961, 160)		
			
