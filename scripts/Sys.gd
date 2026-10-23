extends Node

func res_check_and_replace(path : String) -> String:
	if path[0] == "r" and path[3] == ":":
		return path
	else:
		return "res://%s" % path

func name_check_and_replace(name: String) -> String:
	if name == "Gra":
		return "Бабушка"
	else:
		return name
