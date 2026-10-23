extends TextureRect

const a = 1

func _draw() -> void:
	anim()

func anim() -> void:
	print("menu_001_2 ready")
	$".".position.x = -3961
	var tween = get_tree().create_tween().set_parallel(true)
	tween.tween_property($".", "position:x", -1981, 40)
	tween.tween_property($".", "position:x", 0, 40)
	$".".position.x = 0
	tween.tween_property($".", "position:x", 1980, 40)
	tween.tween_property($".", "position:x", 3960, 40)		
			
