extends TextureRect

const main_01 = preload("res://images/interface/main_meny/01.png")
const main_02 = preload("res://images/interface/main_meny/02.png")
const main_03 = preload("res://images/interface/main_meny/03.png")
const main_04 = preload("res://images/interface/main_meny/04.png")
const main_05 = preload("res://images/interface/main_meny/05.png")

var a = 0

func _ready() -> void:
	print("main_menu_bg ready")

func _draw() -> void:
	anim()

func anim() -> void:
	while a < 2:
		await get_tree().create_timer(8).timeout
		$".".texture = main_02
		await get_tree().create_timer(0.1).timeout
		$".".texture = main_03
		await get_tree().create_timer(0.1).timeout
		$".".texture = main_02
		await get_tree().create_timer(0.1).timeout
		$".".texture = main_01
		await get_tree().create_timer(8).timeout
		a += 1
	a = 0
	$".".texture = main_04
	await get_tree().create_timer(0.1).timeout
	$".".texture = main_05
	await get_tree().create_timer(0.1).timeout
	$".".texture = main_04
	await get_tree().create_timer(0.1).timeout
	$".".texture = main_01
	await get_tree().create_timer(0.1).timeout
