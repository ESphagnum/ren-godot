define step_in = 1.05
define step_out = 1.0
define low_yoffset = 300
transform fox_pos(is_low=False):
    align (.5, 1.)
    xoffset fox_xoffset
    yoffset low_yoffset*is_low

transform owl_pos(is_low=False):
    align (.5, 1.)
    xoffset owl_xoffset
    yoffset low_yoffset*is_low

transform bear_pos(is_low=False):
    align (.5, 1.)
    xoffset bear_xoffset
    yoffset low_yoffset*is_low

transform wolf_pos(is_low=False):
    align (.5, 1.)
    xoffset wolf_xoffset
    yoffset low_yoffset*is_low

init python:
    w_pos_0 = .68
    w_pos_f = .40
    w_zoom_0 = 1.00
    w_zoom_f = 1.45
    w_yanc_0 = 1.00
    w_yanc_f = 0.85
    w_t_0 = 0.0
    w_t_1 = 0.35
    w_t_2 = 0.65
    w_t_3 = 1.00
    w_t_d = 0.02
    def w_pos(t):
        return w_pos_0 * (1 - t) + w_pos_f * t
    def w_zoom(t):
        return w_zoom_0 * (1 - t) + w_zoom_f * t
    def w_yanc(t):
        return w_yanc_0 * (1 - t) + w_yanc_f * t
    wpos = [
    w_pos(w_t_0),
    w_pos(w_t_1 + w_t_d),
    w_pos(w_t_1),
    w_pos(w_t_2 + w_t_d),
    w_pos(w_t_2),
    w_pos(w_t_3 + w_t_d),
    w_pos(w_t_3),
    ]
    wzoom = [
    w_zoom(w_t_0),
    w_zoom(w_t_1 + w_t_d),
    w_zoom(w_t_1),
    w_zoom(w_t_2 + w_t_d),
    w_zoom(w_t_2),
    w_zoom(w_t_3 + w_t_d),
    w_zoom(w_t_3),
    ]
    wyanc = [
    w_yanc(w_t_0),
    w_yanc(w_t_1 + w_t_d),
    w_yanc(w_t_1),
    w_yanc(w_t_2 + w_t_d),
    w_yanc(w_t_2),
    w_yanc(w_t_3 + w_t_d),
    w_yanc(w_t_3),
    ]
    wolf_Normal = "Wolf Normal m 00"
    wolf_Sad = "Wolf Normal m 05"

    bear_Normal = "Bear Normal m 00"
    bear_Alter = "Bear Normal m 01"
    bear_Sad = "Bear Normal m 03"
    bear_Paw = "Bear Normal m 04"

    owl_Normal = "Owl Normal m 00"
    owl_Alter = "Owl Normal m 01"
    owl_Sad = "Owl Normal m 03"

    fox_Normal = "Fox Normal m_night 00"
    fox_Fullface = "Fox Fullface m_night 00"
    fox_Nice = "Fox Nice m_night 00"
    fox_Flirt = "Fox Flirt m_night 00"
    fox_Oh = "Fox Oh m_night 00"
    fox_Sad = "Fox Feel m_night 00 good aside"
    fox_Sad2 = "Fox Feel m_night 00"

    wolf_xoffset = -250
    wolf_sprite_cur = wolf_Normal
    wolf_zoom_cur = step_out

    bear_xoffset = -700
    bear_sprite_cur = bear_Normal
    bear_zoom_cur = step_out

    owl_xoffset = 630
    owl_sprite_cur = owl_Normal
    owl_zoom_cur = step_out

    fox_xoffset = 200
    fox_sprite_cur = fox_Normal
    fox_zoom_cur = step_out

    zoom_new = None
    is_low = False
    jump_offset = 0
    jump_speed = 0.1
    jump_amt = 1
    sprite_new = None


label fox_upd(sprite_new=None, zoom_new=None, jump_amt=1, jump_offset=0, jump_speed=0.1, is_low=False):
    hide Fox
    hide fox_sprite_cur

    if sprite_new is None:
        $ sprite_new = fox_sprite_cur
    if zoom_new is None:
        $ zoom_new = fox_zoom_cur

    show expression fox_sprite_cur:
        fox_pos(is_low)
        parallel:
            zoom fox_zoom_cur
            linear .3 zoom zoom_new
        parallel:
            linear jump_speed yoffset jump_offset + low_yoffset*is_low
            linear jump_speed yoffset low_yoffset*is_low
            repeat jump_amt
        parallel:
            sprite_new with Dissolve(.2)

    pause .01
    $ fox_zoom_cur = zoom_new
    $ fox_sprite_cur = sprite_new

    return

label owl_upd(sprite_new=None, zoom_new=None, jump_amt=1, jump_offset=0, jump_speed=0.1, is_low=False):
    hide Owl
    hide owl_sprite_cur

    if sprite_new is None:
        $ sprite_new = owl_sprite_cur
    if zoom_new is None:
        $ zoom_new = owl_zoom_cur

    show expression owl_sprite_cur:
        owl_pos(is_low)
        parallel:
            zoom owl_zoom_cur
            linear .3 zoom zoom_new
        parallel:
            linear jump_speed yoffset jump_offset + low_yoffset*is_low
            linear jump_speed yoffset low_yoffset*is_low
            repeat jump_amt
        parallel:
            sprite_new with Dissolve(.2)

    pause .01
    $ owl_zoom_cur = zoom_new
    $ owl_sprite_cur = sprite_new

    return

label bear_upd(sprite_new=None, zoom_new=None, jump_amt=1, jump_offset=0, jump_speed=0.1, is_low=False):
    hide Bear
    hide bear_sprite_cur

    if sprite_new is None:
        $ sprite_new = bear_sprite_cur
    if zoom_new is None:
        $ zoom_new = bear_zoom_cur

    show expression bear_sprite_cur:
        bear_pos(is_low)
        parallel:
            zoom bear_zoom_cur
            linear .3 zoom zoom_new
        parallel:
            linear jump_speed yoffset jump_offset + low_yoffset*is_low
            linear jump_speed yoffset low_yoffset*is_low
            repeat jump_amt
        parallel:
            sprite_new with Dissolve(.2)

    pause .01
    $ bear_zoom_cur = zoom_new
    $ bear_sprite_cur = sprite_new

    return

label wolf_upd(sprite_new=None, zoom_new=None, jump_amt=1, jump_offset=0, jump_speed=0.1, is_low=False):
    hide Wolf
    hide wolf_sprite_cur

    if sprite_new is None:
        $ sprite_new = wolf_sprite_cur
    if zoom_new is None:
        $ zoom_new = wolf_zoom_cur

    show expression wolf_sprite_cur:
        wolf_pos(is_low)
        parallel:
            zoom wolf_zoom_cur
            linear .3 zoom zoom_new
        parallel:
            linear jump_speed yoffset jump_offset + low_yoffset*is_low
            linear jump_speed yoffset low_yoffset*is_low
            repeat jump_amt
        parallel:
            sprite_new with Dissolve(.2)

    pause .01
    $ wolf_zoom_cur = zoom_new
    $ wolf_sprite_cur = sprite_new

    return

image fox_appear:
    contains:
        alpha 0
        "polina_lisa_05"
        linear .5 alpha 1
        linear .5 alpha 0
    contains:
        alpha 0
        "polina_lisa_06"
        pause .5
        linear .5 alpha 1
        pause .25
        linear .5 alpha 0
    contains:
        alpha 0
        "Fox Normal b_night 00"
        pause 1
        linear 1. alpha 1

image bd_snow_behind:
    contains:
        "day3_beasts_scene2_snow1"
    contains:
        "day3_beasts_scene2_snow2"
    contains:
        "day3_beasts_scene2_snow3"
    contains:
        "day3_beasts_scene2_snow4"

image beast_dance_1:


    contains:
        "Wolf Normal m 00"
        transform_anchor True
        anchor (.5, 1.)
        ypos 1.
        xpos .5
        4.0 + 2.0
        linear .5 rotate 20 xpos .6 ypos .7



    contains:
        "Bear Normal m 00"
        transform_anchor True
        anchor (.5, 1.)
        ypos 1.
        xpos .5
        4.0 + 1.0
        linear .5 rotate -30 xpos .4


    contains:
        "Owl Normal m 00"
        transform_anchor True
        anchor (.5, 1.)
        ypos 1.
        xpos .5
        4.0 + 0.0
        linear .5 rotate 45 xpos .6


    contains:
        "Fox Fullface b_night 00"
        align (.5, 1.)
        block:
            linear .1 yoffset 20
            linear .4 yoffset 0
            repeat

define bg_02 = 2.0
image beast_dance_2:


    contains:
        "Wolf Normal m 00"
        transform_anchor True
        subpixel True
        anchor (.5, 1.)
        rotate 20 xpos .6 ypos .7
        linear .5 rotate 0 xpos .5 ypos 1. alpha 0

        time 2
        pos (1., .33)
        anchor (.5, 0.)
        rotate 270
        alpha 1
        linear .5 yanchor (.75)
        linear .5 yanchor (.0)

        alpha 0
        yoffset 0
        rotate 0
        align (.5, 1.)
        xoffset wolf_xoffset
        time 4
        linear .5 yoffset 50 alpha 1
        block:
            linear .5 yoffset 0
            linear .5 yoffset 50
            repeat 1
        linear .5 yoffset 0

        1.5

        linear .25 yoffset 50
        linear 1. yoffset 0



    contains:
        "Bear Normal m 00"
        subpixel True
        transform_anchor True
        anchor (.5, 1.)
        ypos 1.
        rotate -30 xpos .4
        linear .5 rotate 0 xpos .5 alpha 0

        time 1
        pos (.0, .5)
        anchor (.5, 0.)
        rotate 90
        alpha 1
        linear .5 yanchor (.75)
        linear .5 yanchor (.0)

        alpha 0
        yoffset 50
        rotate 0
        align (.5, 1.)
        xoffset bear_xoffset
        time 4
        linear .5 yoffset 0 alpha 1
        block:
            linear .5 yoffset 50
            linear .5 yoffset 0
            repeat 2


    contains:
        "Owl Normal m 00"
        transform_anchor True
        subpixel True
        anchor (.5, 1.)
        ypos 1.
        rotate 45 xpos .6
        linear .5 rotate 0 xpos .5 alpha 0

        time 1.5
        pos (.25, .0)
        anchor (.5, 0.)
        rotate 180
        alpha 1
        linear .5 yanchor (.75)
        linear .5 yanchor (.0)

        alpha 0
        yoffset 0
        rotate 0
        align (.5, 1.)
        xoffset owl_xoffset
        time 5
        linear .5 yoffset 50 alpha 1
        block:
            linear .5 yoffset 0
            linear .5 yoffset 50
            repeat 1
        linear .5 yoffset 0


    contains:
        subpixel True
        "Fox Fullface b_night 00"
        align (.5, 1.)
        alpha 1
        .5
        alpha 0


        time 4
        "Fox Normal m_night 00"
        yoffset 50
        align (.5, 1.)
        xoffset fox_xoffset
        linear .5 yoffset 0 alpha 1
        block:
            linear .5 yoffset 50
            linear .5 yoffset 0
            repeat 2
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
