extends RefCounted
const NAME := "Mom"
const ROOT := "res://images/sprite/Mom"

const TRANSFORMS := {
	"left":  {"flip": false, "x": 300, "y": 0},
	"right": {
		"flip": true, "x": 100, "y": 0,
		"x_anchor": 1.0,
	},
	"income": {
		"flip": true, "alpha": 0.0, "x": -674, "y": 0,
		"x_anchor": 1.0,
		"tracks": [[
			{"time": 0.5, "alpha": 0.5, "x": -481, "y": 20},
			{"time": 0.5, "alpha": 1.0, "x": -288, "y": 0},
			{"time": 0.5, "alpha": 1.0, "x": -95,  "y": 20},
			{"time": 0.5, "alpha": 1.0, "x": 100,  "y": 0},
		]],
	},
	"income_left": {
		"flip": false, "alpha": 0.0, "x": -350, "y": 0,
		"tracks": [
			[{"time": 2.0, "x": 0}],
			[{"time": 0.5, "alpha": 0.5}, {"time": 0.5, "alpha": 1.0}],
			[{"time": 0.5, "y": 20}, {"time": 0.5, "y": 0},
			 {"time": 0.5, "y": 20}, {"time": 0.5, "y": 0}],
		],
	},
	"reverse_and_out1": {
		"flip": false, "x": 1346, "y": 0,
		"tracks": [[
			{"time": 0.25, "alpha": 1.00, "x": 1386, "y": 0},
			{"time": 0.25, "alpha": 1.00, "x": 1456, "y": 20},
			{"time": 0.25, "alpha": 0.75, "x": 1526, "y": 0},
			{"time": 0.25, "alpha": 0.50, "x": 1596, "y": 20},
			{"time": 0.25, "alpha": 0.00, "x": 1696, "y": 0},
		]],
	},
	"reverse_and_out_left": {
		"flip": true, "alpha": 1.0, "x": -1220, "y": 0,
		"tracks": [
			[{"time": 0.5, "x": -1260}, {"time": 0.5, "x": -1320},
			 {"time": 0.5, "x": -1370}, {"time": 0.5, "x": -1400}],
			[{"time": 1.0}, {"time": 1.0, "alpha": 0.0}],
			[{"time": 0.5, "y": 20}, {"time": 0.5, "y": 0},
			 {"time": 0.5, "y": 20}, {"time": 0.5, "y": 0}],
		],
	},
}
