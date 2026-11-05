
define case_sfx_folder = "sounds/ka-fix-1.ogg"


define case_sfx_clock_hover = "sounds/ka-fix-1.ogg"


define case_sfx_clock_action = "sounds/ka-fix-1.ogg"

init python:

    def mplay(fn, chan = "test_two", fin = 1.0, fout = 1.0):
        renpy.play(fn, channel = chan, fadein = fin, fadeout = fout)

    def mpause(channel = "test_two"):
        c = renpy.audio.audio.get_channel(channel)
        c.pause()

    def munpause(channel = "test_two"):
        c = renpy.audio.audio.get_channel(channel)
        c.unpause()

    def mstop(chan = "test_two", fout=1.0):
        renpy.music.stop(channel = chan, fadeout = fout)


    def atl_sound(func, *args, **kw):
        def f(trans, st, at):
            func(*args, **kw)
        return f

default phase = 1
default hit_count = 0
default fail_count = 0
default guard_state = 0
default chalk_state_1 = None
default chalk_state_2 = None
default chalk_state_3 = None
default chalk_state_4 = None

image chalk_writing_1_on = "images/minigame/case/chalk-01.png"
image chalk_writing_2_on = "images/minigame/case/chalk-02.png"
image chalk_writing_3_on = "images/minigame/case/chalk-03.png"
image chalk_writing_4_on = "images/minigame/case/chalk-04.png"

image chalk_writing_1_big_on = "images/minigame/case/chalk-001.png"
image chalk_writing_2_big_on = "images/minigame/case/chalk-002.png"
image chalk_writing_3_big_on = "images/minigame/case/chalk-003.png"
image chalk_writing_4_big_on = "images/minigame/case/chalk-004.png"

image chalk_writing_1 = ConditionSwitch(
    "chalk_state_1 == True", "chalk_writing_1_on",
    "True", Null())
image chalk_writing_2 = ConditionSwitch(
    "chalk_state_2", "chalk_writing_2_on",
    "True", Null())
image chalk_writing_3 = ConditionSwitch(
    "chalk_state_3", "chalk_writing_3_on",
    "True", Null())
image chalk_writing_4 = ConditionSwitch(
    "chalk_state_4", "chalk_writing_4_on",
    "True", Null())


image chalk_writing_1_big = ConditionSwitch(
    "chalk_state_1 == True", "chalk_writing_1_big_on",
    "True", Null())
image chalk_writing_2_big = ConditionSwitch(
    "chalk_state_2", "chalk_writing_2_big_on",
    "True", Null())
image chalk_writing_3_big = ConditionSwitch(
    "chalk_state_3", "chalk_writing_3_big_on",
    "True", Null())
image chalk_writing_4_big = ConditionSwitch(
    "chalk_state_4", "chalk_writing_4_big_on",
    "True", Null())

image chalk_writings:
    contains:
        "chalk_writing_1"
    contains:
        "chalk_writing_2"
    contains:
        "chalk_writing_3"
    contains:
        "chalk_writing_4"

image chalk_writings_big:
    contains:
        "chalk_writing_1_big"
    contains:
        "chalk_writing_2_big"
    contains:
        "chalk_writing_3_big"
    contains:
        "chalk_writing_4_big"

image case_bg = "images/minigame/case/bg.png"
image case_fg = "images/minigame/case/fg.png"
image teah_win = "locate/school/in_side/classroom/teacher1_mg.png"

image case_folder_idle = "images/minigame/case/papka.png"
image case_folder_hover = im.MatrixColor("images/minigame/case/papka.png",
    im.matrix.brightness(0.10))

image case_clock = ConditionSwitch(
    "not case_mng_hightlight_clock", "images/minigame/case/time_1.png",
    "True", im.MatrixColor("images/minigame/case/time_1.png",
        im.matrix.brightness(0.10))
    )
image case_clock_arrow = ConditionSwitch(
    "not case_mng_hightlight_clock", "images/minigame/case/time_3.png",
    "True", im.MatrixColor("images/minigame/case/time_3.png",
        im.matrix.brightness(0.10))
    )
define case_clock_arrow_pos = (1020, 207)
define case_clock_arrow_anchor = (.5, .75)

image guard_writing:
    "images/minigame/case/m1.png"
    .5
    "images/minigame/case/m2.png"
    .5
    repeat
image guard_looking = "images/minigame/case/m3.png"
image guard_idle = "images/minigame/case/m4.png"

image guard = ConditionSwitch(
    "guard_state == 0", "guard_writing",
    "guard_state == 1", "guard_idle",
    "guard_state == 2", "guard_looking"
    )

image guard_alert:
    contains:
        "images/minigame/case/guard_alert_bg.jpg"
    contains:
        "images/minigame/case/guard1.png"
    contains:
        Null()
        2.
        "images/minigame/case/guard2.png"
        .1
        "images/minigame/case/guard3.png"
        .1
        "images/minigame/case/guard2.png"
        .1
        repeat

init python:
    def set_guard_green(lenght):
        def _f(trans, st, at):
            mplay("<from 0.0 to {}>sounds/sfx_chalk_writing.ogg".format(lenght), fin = 0.2)
            global guard_state
            if guard_state == 1:
                mplay("sounds/steps/sfx_ment_turns_1.ogg", fin = 0.2, chan="test_four")
            guard_state = 0
            renpy.restart_interaction()
        return _f

    def set_guard_red(trans, st, at):
        mstop(fout = 0.2)
        global guard_state
        if guard_state != 1:
            mplay("sounds/steps/sfx_ment_turns_2.ogg", fin = 0.2, chan="test_four")
        guard_state = 1
        renpy.restart_interaction()

    def set_guard_yellow(trans, st, at):
        mstop(fout = 0.2)
        global guard_state
        if guard_state == 1:
            mplay("sounds/steps/sfx_ment_turns_1.ogg", fin = 0.2, chan="test_four")
        guard_state = 2
        renpy.restart_interaction()

define case_guard_jump_range = -5
transform phase1:
    subpixel True
    align (.60, .5)
    function set_guard_red

    pause 4

    function atl_sound(mplay, "sounds/steps/loop_ment_footsteps_1.ogg")

    block:
        parallel:
            linear 2.5 align (.38, .5)
        parallel:
            linear .25 yoffset case_guard_jump_range
            linear .25 yoffset 0
            repeat 5

    function atl_sound(mstop, fout=0.2)

    pause .5

    function atl_sound(mplay, "sounds/steps/loop_ment_footsteps_1.ogg")

    block:
        parallel:
            linear 4.5 align (.8, .5)
        parallel:
            linear .25 yoffset case_guard_jump_range
            linear .25 yoffset 0
            repeat 9

    function atl_sound(mstop, fout=0.2)

    pause 1.5

    function atl_sound(mplay, "sounds/steps/loop_ment_footsteps_1.ogg")

    block:
        parallel:
            linear 3.0 align (.5, .5)
        parallel:
            linear .25 yoffset case_guard_jump_range
            linear .25 yoffset 0
            repeat 6

    function atl_sound(mstop, fout=0.2)

    pause 1.5

    function set_guard_green(3.5)

transform phase2:
    subpixel True
    align (.5, .5)
    function set_guard_red

    function atl_sound(mplay, "sounds/steps/loop_ment_footsteps_1.ogg")

    block:
        parallel:
            linear 1.5 align (.38, .5)
        parallel:
            linear .25 yoffset case_guard_jump_range
            linear .25 yoffset 0
            repeat 3

    function atl_sound(mstop, fout=0.2)

    pause 1.5

    block:
        function set_guard_red
        pause 2.5
        function set_guard_green(1.5)
        pause 1.5
        repeat

transform phase3:
    subpixel True
    align (.38, .5)
    function set_guard_red

    function atl_sound(mplay, "sounds/steps/loop_ment_footsteps_1.ogg")

    block:
        parallel:
            linear 2.5 align (.60, .5)
        parallel:
            linear .25 yoffset case_guard_jump_range
            linear .25 yoffset 0
            repeat 5

    function atl_sound(mstop, fout=0.2)

    pause 1.5
    function set_guard_yellow
    pause 4
    function set_guard_green(3.0)

default case_mng_rot_lvl1 = 360.0 * (21.0/43.0)
default case_mng_rot_lvl2 = 360.0 * (21.0/43.0) + 360.0 * (11.0/43.0)
default case_mng_rot_lvl3 = 360.0 * (21.0/43.0) + 360.0 * (11.0/43.0) * 2

screen clock_timer(phase):
    add "case_clock"

    add "case_clock_arrow":

        pos case_clock_arrow_pos
        anchor case_clock_arrow_anchor

        if phase == 1:

            at transform:
                subpixel True
                transform_anchor True
                rotate 0
                linear 21. rotate case_mng_rot_lvl1
        if phase == 2:
            at transform:
                subpixel True
                transform_anchor True
                rotate case_mng_rot_lvl1
                linear 11. rotate case_mng_rot_lvl2
        if phase == 3:
            at transform:
                subpixel True
                transform_anchor True
                rotate case_mng_rot_lvl2
                linear 11. rotate case_mng_rot_lvl3
default case_mng_hightlight_clock = False
screen minigame_case():

    add "case_bg"

    add "chalk_writings"

    add "guard":
        id "guard"
        if phase == 1:
            at phase1

        if phase == 2:
            at phase2

        if phase == 3:
            at phase3

    add "teah_win" xpos -1688
    add "case_fg"


    imagebutton:
        idle "case_folder_idle"
        hover "case_folder_hover"
        selected False
        focus_mask True

        if case_sfx_folder:
            hover_sound case_sfx_folder

        if guard_state == 0:
            action Return("hit")
        else:
            action Return("fail")

    text _("ОТКРЫТЬ"):
        xpos 940
        ypos 936
        anchor (.5,.5)
        style "imagemap_text"

    textbutton _("ПРОПУСТИТЬ"):
        xpos 1022
        ypos 118
        anchor (.5,.5)

        if case_sfx_clock_hover:
            hover_sound case_sfx_clock_hover

        hovered SetVariable("case_mng_hightlight_clock", True)
        unhovered SetVariable("case_mng_hightlight_clock", False)
        action Play("test_six", case_sfx_clock_action), Return("full_timeout")
        text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        style "imagemap_text"

    use clock_timer(phase)

    if phase == 1:
        timer 21.0 action Return("timeout")

    if phase == 2:
        timer 11.0 action Return("timeout")

    if phase == 3:
        timer 11.0 action Return("timeout")

    if config.developer == True:
        text "Phase: [phase]"

label minigame_case_start:

    $ phase = 1
    $ hit_count = 0
    $ fail_count = 0
    $ guard_state = 1
    $ guard_allert = False
    $ minigame_result = None

    label minigame_case_start.loop:

    if phase >= 4:

        label minigame_case_start.timeout:
            stop test_two

            jump minigame_timeout

    play test_three "sounds/tikanie.ogg" fadein 2.
    call screen minigame_case 
    stop test_three fadeout .2
    stop test_four fadeout .2
    $ phase += 1

    if _return == "hit":
        $ hit_count += 1

        if phase == 2:
            $ chalk_state_1 = True
        elif phase == 3:
            $ chalk_state_2 = True
        elif phase == 4:
            $ chalk_state_3 = True

        stop test_two fadeout 2

        if hit_count == 1:


            call minigame_folder_hit1

        if hit_count == 2:

            if chalk_state_1 is None:
                $ chalk_state_1 = True

            if chalk_state_2 is None:
                $ chalk_state_2 = True

            if chalk_state_3 is None:
                $ chalk_state_3 = True

            $ chalk_state_4 = True


            jump minigame_folder_hit2

    elif _return == "fail":
        $ fail_count += 1

        if phase == 2:
            $ chalk_state_1 = False
        elif phase == 3:
            $ chalk_state_2 = False
        elif phase == 4:
            $ chalk_state_3 = False

        stop test_two

        if fail_count == 1:


            call minigame_folder_fail1

        if fail_count == 2:


            jump minigame_folder_fail2


    elif _return == "timeout":

        if phase == 2:
            $ chalk_state_1 = True
        elif phase == 3:
            $ chalk_state_2 = True
        elif phase == 4:
            $ chalk_state_3 = True
        elif phase == 5:
            $ chalk_state_4 = True

    elif _return == "full_timeout":
        $ phase = 5

        if chalk_state_1 is None:
            $ chalk_state_1 = True

        if chalk_state_2 is None:
            $ chalk_state_2 = True

        if chalk_state_3 is None:
            $ chalk_state_3 = True

        stop test_two
    else:

        "Ошибка!"
        $ raise Exception("Непредвиденный возврат из мини-игры, свяжитесь с разработчиком mold.FF")
        return

    jump minigame_case_start.loop
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
