extends RefCounted
const NAME := "Dad"
const ROOT := "res://images/sprite/Dad"

const TRANSFORMS := {
	"left": {
	"flip": true, "x": -100, "y": 0,
	"x_anchor": 0.0,
	},
	"income": {
		"flip": true, "alpha": 0.0, "x": -500, "y": 0,
		"x_anchor": 0.0,
		"tracks": [[
			{"time": 0.5, "alpha": 0.5, "x": -300, "y": 20},
			{"time": 0.5, "alpha": 1.0, "x": -150, "y": 0},
			{"time": 0.5, "alpha": 1.0, "x": -100, "y": 20},
			{"time": 0.5, "alpha": 1.0, "x": -100, "y": 0},
		]],
	},
	"out": {
		"flip": true, "alpha": 1.0, "x": -100, "y": 0,
		"x_anchor": 0.0,
		"tracks": [[
			{"time": 0.5, "alpha": 1.00, "x": -200, "y": 20},
			{"time": 0.5, "alpha": 0.75, "x": -400, "y": 0},
			{"time": 0.5, "alpha": 0.50, "x": -600, "y": 20},
			{"time": 0.5, "alpha": 0.00, "x": -900, "y": 0},
		]],
	},
}
