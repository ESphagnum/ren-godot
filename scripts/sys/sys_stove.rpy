image d5_stove_thumb = "minigame/stove/spoon.png"
image d5_stove_heart_yes = "minigame/stove/hart.png"
image d5_stove_heart_no = "minigame/stove/hart0.png"

image d5_stove_lifes3 = Composite((1920, 1080),
    (0, 0), "d5_stove_heart_yes",
    (0, 100), "d5_stove_heart_yes",
    (0, 200), "d5_stove_heart_yes",
)
image d5_stove_lifes2 = Composite((1920, 1080),
    (0, 0), "d5_stove_heart_yes",
    (0, 100), "d5_stove_heart_yes",
    (0, 200), "d5_stove_heart_no",
)
image d5_stove_lifes1 = Composite((1920, 1080),
    (0, 0), "d5_stove_heart_yes",
    (0, 100), "d5_stove_heart_no",
    (0, 200), "d5_stove_heart_no",
)
image d5_stove_lifes0 = Composite((1920, 1080),
    (0, 0), "d5_stove_heart_no",
    (0, 100), "d5_stove_heart_no",
    (0, 200), "d5_stove_heart_no",
)

transform reduce_health(spr_old, spr_new):
    spr_old
    block:
        spr_new
        .125
        spr_old
        .125
        repeat 2
    spr_new

image d5_stove_lifes_reduce_2:
    contains reduce_health("d5_stove_lifes3", "d5_stove_lifes2")
image d5_stove_lifes_reduce_1:
    contains reduce_health("d5_stove_lifes2", "d5_stove_lifes1")
image d5_stove_lifes_reduce_0:
    contains reduce_health("d5_stove_lifes1", "d5_stove_lifes0")

image d5_stove_line_1 = "minigame/stove/line1.png"
image d5_stove_line_2 = "minigame/stove/line2.png"
image d5_stove_line_3 = "minigame/stove/line3.png"

image d5_stove_line_2_ = Solid("#C6C6C6", xysize=(270, 40))
image d5_stove_line_3_ = Solid("#fff", xysize=(80, 40))

define stove_turnoff_text = _("ВЫКЛ")





init python:
    Cooking_Bad = -1
    Cooking_Good = 1
    Cooking_Skip = 10

    class CookSettings:
        def __init__(self, spd, range, good):
            self.spd = spd
            self.range = range
            self.good = good

    class CookGame:
        def __init__(self, settings, lifes):
            self.settings = settings
            self.lifes = lifes
            
            self.value = self.settings.range[0]
            self.direction = 1 
            
            self.key_result = None
            self.turnoff = False
            
            return
        
        def Reset(self, settings=None):
            if settings:
                self.settings = settings
                
                self.value = self.settings.range[0]
                self.direction = 1 
            
            self.key_result = None
            
            return
        
        def UpdateCursor(self, dt, is_turnoff):
            self.value += self.settings.spd * dt * self.direction
            if self.value > self.settings.range[1]:
                self.value = self.settings.range[1]
                self.direction = -1
            if self.value < self.settings.range[0]:
                self.value = self.settings.range[0]
                self.direction = 1
            self.turnoff = is_turnoff
            return
        
        def PressKey(self):
            if self.turnoff:
                return Cooking_Skip
            
            if self.settings.good[0] <= self.value < self.settings.good[1]:
                return Cooking_Good
            
            return Cooking_Bad

    class CookingDisplayable(renpy.Displayable):
        '''
    '''
        def __init__(self, game):
            renpy.Displayable.__init__(self)
            self.game = game
            self._last_st = 0
            self.cursor = renpy.displayable("d5_stove_thumb")
            self.playsection_d = renpy.displayable("d5_stove_line_1")
            self.good_d = renpy.displayable(Solid("#C6C6C6"))
            
            self.mx = 0
            self.my = 0
            
            self.turnoff_area = (930-75, 700, 150, 800)
            self.turnoff_disp = renpy.displayable("stove_turnoff_hover_img")
        
        def event(self, ev, x, y, st):
            import pygame
            
            if ev.type == pygame.MOUSEMOTION: 
                self.mx = x
                self.my = y
        
        def turnoff_is_highlight(self):
            _x, _y, w, h = self.turnoff_area
            if _x < self.mx < _x + w and _y < self.my < _y + h:
                return True
            return False
        
        
        def render(self, width, height, st, at):
            
            
            if self._last_st == None:
                self._last_st = 0
            
            deltaTime = (st - self._last_st)
            self._last_st = st
            
            if deltaTime > 0.04:
                deltaTime = 0.04
            
            
            self.game.UpdateCursor(deltaTime, self.turnoff_is_highlight())
            
            
            render = renpy.Render(width, height)
            
            playsection_render = self.playsection_d.render(width, height, st, at)
            render.blit(playsection_render, (0, 0))
            
            good_render = self.good_d.render(self.game.settings.good[1] - self.game.settings.good[0], 40, st, at)
            good_w, good_h = good_render.get_size()
            good_x = 960 - 505 + self.game.settings.good[0]
            good_y = 83 - (good_h // 2)
            render.blit(good_render, (good_x, good_y))
            
            cursor_render = self.cursor.render(width, height, st, at)
            cur_w, cur_h = cursor_render.get_size()
            cur_x = 960 - (cur_w // 2) - (self.game.settings.range[1]//2) + int(self.game.value)
            cur_y = 100 - (cur_h // 2)
            render.blit(cursor_render, (cur_x, cur_y))
            
            
            
            
            
            
            
            
            
            
            
            
            turnoff_render = Text(stove_turnoff_text, style="imagemap_text", color="#fff", outlines=[ (absolute(1), "#000", absolute(0), absolute(0)) ]).render(width, height, st, at)
            to_w, to_h = turnoff_render.get_size()
            to_x = 930 - (to_w // 2)
            to_y = 800 - (to_h // 2)
            render.blit(turnoff_render, (to_x, to_y))
            
            if self.turnoff_is_highlight():
                turnoff_img_render = self.turnoff_disp.render(width, height, st, at)
                render.blit(turnoff_img_render, (0, 0))
            
            
            renpy.redraw(self, 0)
            return render

image stove_turnoff_hover_img:
    "d5_katya_stove on"
    matrixcolor BrightnessMatrix(0.1)

image stove_turnoff_cond = ConditionSwitch(
    "stove_turnoff_hover", "stove_turnoff_hover_img",
    "True", "d5_katya_stove on"
    )

screen cook_g(game):
    layer "master"
    add CookingDisplayable(game):
        align .5,.5

    button:
        background None
        xfill True
        yfill True
        action Function(game.PressKey)

default stove_turnoff_hover = False
screen cook_turnoff():
    zorder 100
























screen stove_healths(amount):
    zorder 100

    if amount == 3:
        add "d5_stove_lifes3"
    if amount == 2:
        add "d5_stove_lifes2"
    if amount == 1:
        add "d5_stove_lifes1"
    if amount == 0:
        add "d5_stove_lifes0"
screen stove_healths_reduce(amount):
    zorder 100

    if amount == 2:
        add "d5_stove_lifes_reduce_2"
    if amount == 1:
        add "d5_stove_lifes_reduce_1"
    if amount == 0:
        add "d5_stove_lifes_reduce_0"

    timer 2. action Return()

label d5_stove_game:
    window hide
    scene d5_katya_stove_bg
    show d5_stove_pan still
    show d5_katya_stove off
    with Dissolve(.5)

    show d5_katya_stove on
    with Dissolve(.5)

    play test_two "sounds/loop_frying.ogg" fadein 2.
    play test_three "sounds/loop_pan_moving.ogg"

    show d5_stove_pan base:
        subpixel True
        2.
        ease 0.5 xoffset -15 yoffset -15
        ease 0.5 xoffset 15 yoffset 15
        ease 0.5 xoffset -15 yoffset -15
        ease 0.5 xoffset 15 yoffset 15
        ease 1 xoffset 0 yoffset 0
        repeat
    with Dissolve(.5)

    jump d5_stove_game.round_1







    label d5_stove_game.round_1:
        show d5_stove_pan potato1
        with Dissolve(.5)

        $ stove_spd = 800
        $ stove_range = 250
        $ stove_round = 1
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, 3)

        show d5_stove_pan potato2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan potato4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round1_lose


            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good

            show d5_stove_pan potato3
            with Dissolve(.5)

            call event_m_katya_round1_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5
        jump d5_stove_game.round_2

    label d5_stove_game.round_2:
        show d5_stove_pan cutlet1
        with Dissolve(.5)

        $ stove_spd = 800
        $ stove_range = 120
        $ stove_round = 2
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, game.lifes)

        show d5_stove_pan cutlet2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan cutlet4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round2_lose

            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good
            show d5_stove_pan cutlet3
            with Dissolve(.5)

            call event_m_katya_round2_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5

        jump d5_stove_game.round_3

    label d5_stove_game.round_3:
        show d5_stove_pan potato1
        with Dissolve(.5)

        $ stove_spd = 1000
        $ stove_range = 240
        $ stove_round = 3
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, game.lifes)

        show d5_stove_pan potato2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan potato4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round3_lose

            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good
            show d5_stove_pan potato3
            with Dissolve(.5)

            call event_m_katya_round3_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5

        jump d5_stove_game.round_4

    label d5_stove_game.round_4:
        show d5_stove_pan cutlet1
        with Dissolve(.5)

        $ stove_spd = 1000
        $ stove_range = 180
        $ stove_round = 4
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, game.lifes)

        show d5_stove_pan cutlet2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan cutlet4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round4_lose

            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good
            show d5_stove_pan cutlet3
            with Dissolve(.5)

            call event_m_katya_round4_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5

        jump d5_stove_game.round_5

    label d5_stove_game.round_5:
        show d5_stove_pan potato1
        with Dissolve(.5)

        $ stove_spd = 1200
        $ stove_range = 240
        $ stove_round = 5
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, game.lifes)

        show d5_stove_pan potato2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan potato4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round5_lose

            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good
            show d5_stove_pan potato3
            with Dissolve(.5)

            call event_m_katya_round5_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5

        jump d5_stove_game.round_6

    label d5_stove_game.round_6:
        show d5_stove_pan cutlet1
        with Dissolve(.5)

        $ stove_spd = 1200
        $ stove_range = 120
        $ stove_round = 6
        $ stove_offset = int(renpy.random.random() * (505 - stove_range // 2) ) * renpy.random.choice((1, -1))
        $ sett = CookSettings(stove_spd, (0, 1010), (505 + stove_offset - stove_range // 2, 505 + stove_offset + stove_range // 2))
        $ game = CookGame(sett, game.lifes)

        show d5_stove_pan cutlet2
        with Dissolve(.5)
        show screen stove_healths(game.lifes)
        with Dissolve(.5)
        show screen cook_g(game)
        with Dissolve(.5)
        call screen cook_g(game)
        if _return == Cooking_Bad:
            call d5_stove_sfx.bad
            $ game.lifes -=1

            show d5_stove_pan cutlet4
            with Dissolve(.5)

            hide screen stove_healths
            call d5_stove_sfx.heart
            call screen stove_healths_reduce(game.lifes)
            show screen stove_healths(game.lifes)
            with None

            call event_m_katya_round6_lose

            if game.lifes == 0:
                jump event_m_katya_bad_game

        if _return == Cooking_Good:
            call d5_stove_sfx.good
            show d5_stove_pan cutlet3
            with Dissolve(.5)

            call event_m_katya_round6_win

        if _return == Cooking_Skip:
            jump event_m_katya_skip_game

        show d5_stove_pan base
        with Dissolve(.5)
        pause 0.5

    label d5_stove_game.end:
        scene d5_katya_stove_bg
        show d5_stove_pan still
        show d5_katya_stove off
        with Dissolve(.5)
        pause 0.5

        jump event_m_katya_good_game

label d5_stove_sfx:
    label d5_stove_sfx.good:
        $ rnd = renpy.random.choice((1, 2, 3))
        play test_four "sounds/sfx_frying_accent_" + str(rnd) + ".ogg"
        return
    label d5_stove_sfx.bad:
        $ rnd = renpy.random.choice((1, 2))
        play test_four "sounds/sfx_frying_badend_" + str(rnd) + ".ogg"
        return
    label d5_stove_sfx.heart:
        play test_five "sounds/sfx_hp_lose.ogg"
        return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
