init python:
    last_adjustments = None
    class Widespan(renpy.Displayable):
        def __init__(self, x_adj, y_adj):
            super(renpy.Displayable, self).__init__()
            self.x_adj = x_adj
            self.y_adj = y_adj
        
        
        def render(self, width, height, st, at):
            global last_adjustments
            x, y = renpy.get_mouse_pos()
            x_value = self.x_adj.range * (x / config.screen_width)
            y_value = self.y_adj.range * (y / config.screen_height)
            self.x_adj.change(x_value)
            self.y_adj.change(y_value)
            
            
            last_adjustments = (self.x_adj, self.y_adj)
            
            renpy.redraw(self, 0)
            return renpy.Render(width, height)

    class Widespan_Dependant(renpy.Displayable):
        def __init__(self, x_adj, y_adj, parent_x_adj, parent_y_adj):
            super(renpy.Displayable, self).__init__()
            self.x_adj = x_adj
            self.y_adj = y_adj
            self.parent_x_adj = parent_x_adj
            self.parent_y_adj = parent_y_adj
        
        
        def render(self, width, height, st, at):
            
            
            
            
            if self.x_adj is not None:
                x_value = self.x_adj.range * (self.parent_x_adj.value / self.parent_x_adj.range)
            y_value = self.y_adj.range * (self.parent_y_adj.value / self.parent_y_adj.range)
            
            if self.x_adj is not None:
                self.x_adj.change(x_value)
            self.y_adj.change(y_value)
            
            renpy.redraw(self, 0)
            return renpy.Render(width, height)


screen ParallaxButtons(xy_size, bg_disp, buttons, adjustments=None):


    if adjustments is None:
        $ _x, _y = renpy.get_mouse_pos()
        $ x_value = xy_size[0] * (_x / config.screen_width)
        $ y_value = xy_size[1] * (_y / config.screen_height)

        default view_x = ui.adjustment(value = x_value, range=xy_size[0])
        default view_y = ui.adjustment(value = y_value, range=xy_size[1])


    else:
        default view_x = adjustments[0]
        default view_y = adjustments[1]


        $ _x = config.screen_width * (view_x.value / view_x.range)
        $ _y = config.screen_height * (view_y.value / view_y.range)
        on "show":
            action MouseMove(x=_x, y=_y, duration=.0)


    viewport:
        xfill True
        yfill True
        xadjustment view_x
        yadjustment view_y
        child_size xy_size


        add Widespan(view_x, view_y)


        if bg_disp:
            add bg_disp


        for btn in buttons:
            button:
                pos btn[0]
                anchor (.5, .5)
                xysize (300, 200)
                action btn[1]
                hover_sound btn[3]

                if len(btn) > 4:
                    hovered SetVariable(btn[4], True)
                    unhovered SetVariable(btn[4], False)

                text _(btn[2]):
                    anchor (.5,.5)
                    style "imagemap_text"
                    color "#ffffff"
                    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                    at conf_fon


screen ParallaxView(xy_size, bg_image, adjustments=None, sensitive=True):
    if adjustments is None:
        default view_x = ui.adjustment(value = 0, range=xy_size[0])
        default view_y = ui.adjustment(value = 0, range=xy_size[1])

    else:
        default view_x = adjustments[0]
        default view_y = adjustments[1]
        $ _x = config.screen_width * (view_x.value / view_x.range)
        $ _y = config.screen_height * (view_y.value / view_y.range)
        on "show":
            action MouseMove(x=_x, y=_y, duration=.0)

    viewport:
        xfill True
        yfill True
        xadjustment view_x
        yadjustment view_y
        child_size xy_size

        if sensitive:
            add Widespan(view_x, view_y)

        add bg_image


screen LayeredParallaxButtons(*layers):
    for L in layers:
        use ParallaxButtons(L[0], L[1], L[2], L[3])

screen LayeredParallaxView(*layers):
    for L in layers:
        use ParallaxView(L[0], L[1], L[2], L[3])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
