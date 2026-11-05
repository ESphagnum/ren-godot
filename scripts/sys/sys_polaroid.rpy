init python:
    import pygame

    polaroid_text_ready_to_action_btn = _("СДЕЛАТЬ ФОТО{#PolaroidReadyToMakePhotoButton}")

    camera_speed_nodes = ((300, 0), (600, 300)) 
    camera_width = camera_speed_nodes[1][0] - camera_speed_nodes[0][0]
    clue_pos = (250, 200)
    clue_dist = 150

    class PhotoData:
        def __init__(self, child, next_label):
            self.d = renpy.displayable(child)
            self.pos = (None, None)
            self.next_label = next_label


    class PhotoEngine(renpy.Displayable):
        def __init__(self, data, start_pos):
            super(PhotoEngine, self).__init__()
            
            self.data = data
            self.data.pos = start_pos
            self.interactive = True
            
            self._last_st = None
            self._found_st = None
            
            self.dir = None
            self.inertia = 0
        
        def render(self, width, height, st, at):
            
            x, y = self.data.pos
            
            if self._last_st is None:
                self._last_st = st
            dt = st - self._last_st
            self._last_st = st
            
            if self.interactive:            
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - config.screen_width *.5
                dy = mouse_y - config.screen_height *.5
                
                dist = (dx**2 + dy**2)**.5
                speed = 0
                
                if dist < camera_speed_nodes[0][0]:
                    speed = camera_speed_nodes[0][1]
                
                elif camera_speed_nodes[1][0] < dist:
                    speed = camera_speed_nodes[1][1]
                
                else:
                    t = dist / camera_width
                    speed = camera_speed_nodes[0][1] * (1.0 - t) + camera_speed_nodes[1][1] * t
                
                nx = dx / dist
                ny = dy / dist
                
                x += nx*speed*dt
                y += ny*speed*dt
            
            else:
                dx = clue_pos[0] - x
                dy = clue_pos[1] - y
                dist = (dx**2 + dy**2)**.5
                speed = dist
                nx = dx / dist
                ny = dy / dist
                
                x += nx*speed*dt
                y += ny*speed*dt
            
            
            render = renpy.Render(width, height)
            child = renpy.render(self.data.d, width, height, st, at)
            
            d_width, d_height = child.get_size()
            
            x = min(max(x, 0), d_width - width)
            y = min(max(y, 0), d_height - height)
            
            self.data.pos = (x, y)
            render.blit(child, (-x, -y))
            
            pos_ui = Text("{}\n{}".format(str(self.dir), str(self.inertia)))
            render.blit(pos_ui.render(0, 0, st, at), (0, 0))
            renpy.redraw(self, 0)
            
            return render
        
        def event(self, ev, _x, _y, st):
            x, y = self.data.pos
            _dx = x - clue_pos[0]
            _dy = y - clue_pos[1]
            clue = (_dx**2 + _dy**2)**.5
            
            if clue > clue_dist or not self.interactive:
                return
            
            self.interactive = False
            renpy.restart_interaction()
            return



screen d4_polaroid(photo):
    fixed:
        xysize (1920, 1080)
        align (.5, .5)

        add photo:

            at transform:
                parallel:
                    ease .5 xoffset -15
                    ease .5 xoffset 15
                    repeat
                parallel:
                    ease .8 yoffset -5
                    ease .8 yoffset 5
                    repeat
                parallel:
                    linear .02 xpos 5
                    linear .02 xpos -5
                    repeat
        add "d4_help_fg"
screen d4_make_photo(photo):
    use d4_polaroid(photo)

    if not photo.interactive:
        button:
            xfill True
            yfill True

            action Jump(photo.data.next_label)

        text polaroid_text_ready_to_action_btn:
            align (.5, .23)
            xoffset 10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
