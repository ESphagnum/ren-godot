init -1 python:

    def drag_activated_sound(*args, **kwargs):
        renpy.play(renpy.random.choice(day4_zigzag_activate_sfx), channel="sfx")

    def drag_dragged_sound(*args, **kwargs):
        renpy.play(renpy.random.choice(day4_zigzag_dragged_sfx), channel="sfx")

    class PuzzlePiece:
        def __init__(self, key, img, link = None, pos = (0,0), size = (0, 0), target = (0,0), eps = 0, is_valid = False):
            self.key = key
            self.img = img
            self.link = link
            self.pos = pos
            self.size = size
            self.target = target
            self.eps = eps
            self.is_valid = is_valid
        
        def reset(self, pos = None, eps = None, is_valid = None):
            if pos:
                self.pos = pos
            
            if eps:
                self.eps = eps
            
            if is_valid:
                self.is_valid = is_valid

    class PuzzleCipher:
        def __init__(self, pieces, victory_label, skip_label, background):
            self.pieces = {}
            for p in pieces:
                self.pieces[p.key] = p
            self.victory_label = victory_label
            self.skip_label = skip_label
            self.background = background
        
        def reset(self, **kw):
            for k in self.pieces:
                self.pieces[k].reset(**kw)
        
        def shuffle(self):
            w = config.screen_width
            h = config.screen_height
            
            for k in self.pieces:
                p = self.pieces[k]
                dx = w - p.size[0]
                dy = h - p.size[1]
                
                _x = int( renpy.random.random() * dx )
                _y = int( renpy.random.random() * dy )
                
                p.pos = (_x, _y)
        
        def update(self):
            for k in self.pieces:
                if self.pieces[k].link is None:
                    self.pieces[k].is_valid = True
                    continue
                
                link = self.pieces[k].link
                x0, y0 = self.pieces[link].pos
                
                x1, y1 = self.pieces[k].target
                
                x, y = self.pieces[k].pos
                x -= x0 + x1
                y -= y0 + y1
                
                if (x**2 + y**2)**.5 < self.pieces[k].eps:
                    self.pieces[k].is_valid = True
                else:
                    self.pieces[k].is_valid = False
            return
        
        def validate(self):
            for k in self.pieces:
                if not self.pieces[k].is_valid:
                    break
            else:
                renpy.jump(self.victory_label)
        
        def force_solve(self):
            for k in self.pieces:
                p = self.pieces[k]
                if p.link is None:
                    continue
                
                l = self.pieces[ p.link ]
                
                p.pos = (l.pos[0] + p.target[0], l.pos[1] + p.target[1])
            renpy.restart_interaction()
        
        def dragged(self, drags, drop):
            key = drags[0].drag_name
            self.pieces[key].pos = (drags[0].x, drags[0].y)
            self.update()
            self.validate()
            renpy.restart_interaction()

screen puzzle_cipher(puzzle, debug=False):
    add puzzle.background

    if config.developer:
        button:
            xpos 0 +100
            ypos 0 +100
            anchor (.5, .5)
            xysize (360, 284)
            action Function(puzzle.force_solve)
            hover_sound "sounds/menu/button-click-4.ogg"
            hover_background "ui_cloud 50"

            text _("dev СОБРАТЬ"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ff0"
                outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

    draggroup:
        for k in puzzle.pieces:
            drag:
                focus_mask True
                drag_name k
                draggable True
                droppable False
                activated drag_activated_sound
                dragged puzzle.dragged, drag_dragged_sound
                pos puzzle.pieces[k].pos


                add puzzle.pieces[k].img


    if not is_dcut:
        button:
            xpos 1920 -100
            ypos 0 +100
            anchor (.5, .5)
            xysize (360, 284)
            action Jump(puzzle.skip_label)
            hover_sound "sounds/menu/button-click-4.ogg"
            hover_background "ui_cloud 50"

            text _("ЗАВЕРШИТЬ"):
                anchor (.5,.5)
                style "imagemap_text"
                color "#ffffff"
                outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]


screen puzzle_static(puzzle):
    add puzzle.background

    for k in puzzle.pieces:
        add puzzle.pieces[k].img:
            pos puzzle.pieces[k].pos
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
