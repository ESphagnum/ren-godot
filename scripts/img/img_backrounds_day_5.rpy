init:

    image bg_grey = "#999"

    python:
        d5_light = 0
        def set_light_off(trans, st, at):
            global d5_light
            d5_light = 0
            renpy.restart_interaction()
        def set_light_on(trans, st, at):
            global d5_light
            d5_light = 1
            renpy.restart_interaction()
        def set_light_yes(trans, st, at):
            global d5_light
            d5_light = 2
            renpy.restart_interaction()

    transform if_lights(spr, alpha=1.0):
        spr
        alpha alpha

    image black_blink = ConditionSwitch(
        "d5_light == 0", if_lights("bg_black", alpha = 0.50),
        "d5_light == 1", Null(),
        "d5_light == 2", Null(),
        )

    image perpetual_motion:
        Solid("#0001", xysize=(1, 1))
        linear 1 xoffset 100
        linear 1 xoffset 0
        repeat


    image d5_smoke:
        animation
        "d4_garage_smoke"
        block:
            xpan 0
            linear 30 xpan 360
            repeat



    image snow_day_5 = LiveComposite((1920, 1080),
            (0, 0), SnowBlossom("effect/snow/s001.png", count=10, yspeed=(1600, 2200), xspeed=(-620, -750), border=0, start=0, fast=False),
            (0, 0), SnowBlossom("effect/snow/s002.png", count=15, yspeed=(1600, 2200), xspeed=(-620, -750), border=0, start=0, fast=False),
        )

    image d5b_snow_00 = "effect/snow/snow00.png"
    image d5b_snow_01 = "effect/snow/snow01.png"
    image d5b_snow_02 = "effect/snow/snow02.png"
    image d5b_snow_03 = "effect/snow/snow03.png"

    image blizzard_d5_day:
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 0
                linear 3 ypan -360
                repeat
            parallel:
                xpan 0
                linear 5 xpan -360
                repeat
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 30
                linear 3 ypan -360+30
                repeat
        contains:
            "blizzard_d4_day_near"
            parallel:
                ypan 0
                linear 3 ypan -360
                repeat
            parallel:
                xpan 0
                linear 5 xpan -360
                repeat

    image blizzard_d5_day_inface:
        contains:
            "blizzard_d4_day_far"
            blur 4
            parallel:
                ypan 30
                linear 5 ypan -360+30
                repeat
            parallel:
                xpan 30
                linear 65 xpan 360+30
                repeat
        contains:
            "blizzard_d4_day_far"
            blur 2
            parallel:
                ypan 0
                linear 4 ypan -360
                repeat
            parallel:
                xpan 60
                linear 85 xpan 360+60
                repeat
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 90
                linear 3.5 ypan -360+90
                repeat
        contains:
            "blizzard_d4_day_near"
            blur 2
            parallel:
                xpan 0
                linear 5 xpan 360
                repeat
            parallel:
                ypan 60
                linear 2 ypan -360+60
                repeat
        contains:
            "blizzard_d4_day_near"
            parallel:
                xpan 40
                linear 10 xpan 360+40
                repeat
            parallel:
                ypan 0
                linear 2 ypan -360
                repeat
        contains:
            "snow_day_5"

    image blizzard_d5_day_inface2:
        contains:
            "blizzard_d4_day_far"
            blur 4
            parallel:
                ypan 30
                linear 5 ypan -360+30
                repeat
            parallel:
                xpan 30
                linear 65 xpan 360+30
                repeat
        contains:
            "blizzard_d4_day_far"
            blur 2
            parallel:
                ypan 0
                linear 4 ypan -360
                repeat
            parallel:
                xpan 60
                linear 85 xpan 360+60
                repeat
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 90
                linear 3.5 ypan -360+90
                repeat
        contains:
            "blizzard_d4_day_near"
            blur 2
            parallel:
                xpan 0
                linear 5 xpan 360
                repeat
            parallel:
                ypan 60
                linear 2 ypan -360+60
                repeat
        contains:
            "blizzard_d4_day_near"
            parallel:
                xpan 40
                linear 10 xpan 360+40
                repeat
            parallel:
                ypan 0
                linear 2 ypan -360
                repeat

    image blizzard_d5_day2_aux:
        contains:
            "blizzard_d4_day_far"
            blur 4
            parallel:
                ypan 30
                linear 5 ypan -360+30
                repeat
            parallel:
                xpan 30
                linear 65 xpan 360+30
                repeat
        contains:
            "blizzard_d4_day_far"
            blur 2
            parallel:
                ypan 0
                linear 4 ypan -360
                repeat
            parallel:
                xpan 60
                linear 85 xpan 360+60
                repeat
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 90
                linear 3.5 ypan -360+90
                repeat
        contains:
            "blizzard_d4_day_near"
            blur 2
            parallel:
                xpan 0
                linear 5 xpan 360
                repeat
            parallel:
                ypan 60
                linear 2 ypan -360+60
                repeat
        contains:
            "blizzard_d4_day_near"
            parallel:
                xpan 40
                linear 10 xpan 360+40
                repeat
            parallel:
                ypan 0
                linear 2 ypan -360
                repeat
    image blizzard_d5_day2:
        "blizzard_d5_day2_aux"
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
        parallel:
            ypan 44
            linear 10 ypan -360+44
            repeat

    image blizzard_d5_day2_back_aux:
        contains:
            "blizzard_d4_day_far"
            blur 4
            parallel:
                ypan 30
                linear 5 ypan -360+30
                repeat
            parallel:
                xpan 30
                linear 65 xpan 360+30
                repeat
        contains:
            "blizzard_d4_day_far"
            blur 2
            parallel:
                ypan 0
                linear 4 ypan -360
                repeat
            parallel:
                xpan 60
                linear 85 xpan 360+60
                repeat
        contains:
            "blizzard_d4_day_far"
            parallel:
                ypan 90
                linear 3.5 ypan -360+90
                repeat
    image blizzard_d5_day2_front_aux:
        contains:
            "blizzard_d4_day_near"
            blur 2
            parallel:
                xpan 0
                linear 5 xpan 360
                repeat
            parallel:
                ypan 60
                linear 2 ypan -360+60
                repeat
        contains:
            "blizzard_d4_day_near"
            parallel:
                xpan 40
                linear 10 xpan 360+40
                repeat
            parallel:
                ypan 0
                linear 2 ypan -360
                repeat
    image blizzard_d5_day2_a_back:
        "blizzard_d5_day2_back_aux"
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
        parallel:
            ypan 44
            linear 10 ypan -360+44
            repeat
    image blizzard_d5_day2_a_front:
        "blizzard_d5_day2_front_aux"
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
        parallel:
            ypan 44
            linear 10 ypan -360+44
            repeat

    image blizzard_d5_day3_aux:
        contains:
            "blizzard_d4_day_far"
            parallel:
                xpan 40
                linear 10 xpan 360+40
                repeat
            parallel:
                ypan 0
                linear 2 ypan -360
                repeat

    image blizzard_d5_day3:
        "blizzard_d5_day3_aux"
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
        parallel:
            ypan 44
            linear 10 ypan -360+44
            repeat


    image d5_snow_wind_1 = "effect/snow/wind/01.png"
    image d5_snow_wind_2 = "effect/snow/wind/02.png"
    image d5_snow_wind_3 = "effect/snow/wind/03.png"
    image d5_snow_wind_4 = "effect/snow/wind/04.png"
    image d5_snow_wind_5 = "effect/snow/wind/05.png"
    image d5_snow_wind_6 = "effect/snow/wind/06.png"

    image d5_snow_wind2_1 = "effect/snow/wind2/01.png"
    image d5_snow_wind2_2 = "effect/snow/wind2/02.png"
    image d5_snow_wind2_3 = "effect/snow/wind2/03.png"
    image d5_snow_wind2_4 = "effect/snow/wind2/04.png"
    image d5_snow_wind2_5 = "effect/snow/wind2/05.png"
    image d5_snow_wind2_6 = "effect/snow/wind2/06.png"

    default frame_dur = 1./24.
    default frame_amt = 3
    image d5_snow_wind:
        "d5_snow_wind_1"
        frame_dur * frame_amt
        "d5_snow_wind_2"
        frame_dur * frame_amt
        "d5_snow_wind_3"
        frame_dur * frame_amt
        "d5_snow_wind_4"
        frame_dur * frame_amt
        "d5_snow_wind_5"
        frame_dur * frame_amt
        "d5_snow_wind_6"
        frame_dur * frame_amt
        repeat
    image d5_snow_wind2:
        "d5_snow_wind2_1"
        frame_dur * frame_amt
        "d5_snow_wind2_2"
        frame_dur * frame_amt
        "d5_snow_wind2_3"
        frame_dur * frame_amt
        "d5_snow_wind2_4"
        frame_dur * frame_amt
        "d5_snow_wind2_5"
        frame_dur * frame_amt
        "d5_snow_wind2_6"
        frame_dur * frame_amt
        repeat
    image d5_snow_wind dark1 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0001"), "d5_snow_wind")
        )
    image d5_snow_wind dark2 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0002"), "d5_snow_wind")
        )
    image d5_snow_wind dark3 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0003"), "d5_snow_wind")
        )
    image d5_snow_wind dark4 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0004"), "d5_snow_wind")
        )
    image d5_snow_wind dark5 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0005"), "d5_snow_wind")
        )
    image d5_snow_wind dark6 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0006"), "d5_snow_wind")
        )
    image d5_snow_wind dark7 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0007"), "d5_snow_wind")
        )
    image d5_snow_wind dark8 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0008"), "d5_snow_wind")
        )
    image d5_snow_wind dark9 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#0009"), "d5_snow_wind")
        )
    image d5_snow_wind darka = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000a"), "d5_snow_wind")
        )
    image d5_snow_wind darkb = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000b"), "d5_snow_wind")
        )
    image d5_snow_wind darkc = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000c"), "d5_snow_wind")
        )
    image d5_snow_wind darkd = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000d"), "d5_snow_wind")
        )
    image d5_snow_wind darke = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000e"), "d5_snow_wind")
        )
    image d5_snow_wind darkf = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_wind",
        (0, 0),  AlphaMask(Solid("#000f"), "d5_snow_wind")
        )
    image d5_snow_up dark1 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0001"), "incar_snow_up")
        )
    image d5_snow_up dark2 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0002"), "incar_snow_up")
        )
    image d5_snow_up dark3 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0003"), "incar_snow_up")
        )
    image d5_snow_up dark4 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0004"), "incar_snow_up")
        )
    image d5_snow_up dark5 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0005"), "incar_snow_up")
        )
    image d5_snow_up dark6 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0006"), "incar_snow_up")
        )
    image d5_snow_up dark7 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0007"), "incar_snow_up")
        )
    image d5_snow_up dark8 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0008"), "incar_snow_up")
        )
    image d5_snow_up dark9 = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#0009"), "incar_snow_up")
        )
    image d5_snow_up darka = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000a"), "incar_snow_up")
        )
    image d5_snow_up darkb = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000b"), "incar_snow_up")
        )
    image d5_snow_up darkc = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000c"), "incar_snow_up")
        )
    image d5_snow_up darkd = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000d"), "incar_snow_up")
        )
    image d5_snow_up darke = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000e"), "incar_snow_up")
        )
    image d5_snow_up darkf = LiveComposite((1920, 1080),
        (0, 0), "incar_snow_up",
        (0, 0), AlphaMask(Solid("#000f"), "incar_snow_up")
        )

    $ snowspeed = 0.05
    image d5_snow_up_fast:
        "locate/incar/snow/1.png"
        snowspeed
        "locate/incar/snow/2.png"
        snowspeed
        "locate/incar/snow/3.png"
        snowspeed
        "locate/incar/snow/4.png"
        snowspeed
        "locate/incar/snow/5.png"
        snowspeed
        "locate/incar/snow/6.png"
        snowspeed
        "locate/incar/snow/7.png"
        snowspeed
        "locate/incar/snow/8.png"
        snowspeed
        "locate/incar/snow/9.png"
        snowspeed
        "locate/incar/snow/10.png"
        snowspeed
        "locate/incar/snow/11.png"
        snowspeed
        "locate/incar/snow/12.png"
        snowspeed
        "locate/incar/snow/13.png"
        snowspeed
        "locate/incar/snow/14.png"
        snowspeed
        "locate/incar/snow/15.png"
        snowspeed
        "locate/incar/snow/16.png"
        snowspeed
        "locate/incar/snow/17.png"
        snowspeed
        "locate/incar/snow/18.png"
        snowspeed
        "locate/incar/snow/19.png"
        snowspeed
        "locate/incar/snow/20.png"
        snowspeed
        repeat

    image d5_snow_up_fast dark1 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0001"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark2 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0002"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark3 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0003"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark4 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0004"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark5 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0005"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark6 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0006"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark7 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0007"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark8 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0008"), "d5_snow_up_fast")
        )
    image d5_snow_up_fast dark9 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_fast",
        (0, 0), AlphaMask(Solid("#0009"), "d5_snow_up_fast")
        )

    image d5_snow_up_rev:
        "images/locate/incar/snow/20.png"
        .1
        "images/locate/incar/snow/19.png"
        .1
        "images/locate/incar/snow/18.png"
        .1
        "images/locate/incar/snow/17.png"
        .1
        "images/locate/incar/snow/16.png"
        .1
        "images/locate/incar/snow/15.png"
        .1
        "images/locate/incar/snow/14.png"
        .1
        "images/locate/incar/snow/13.png"
        .1
        "images/locate/incar/snow/12.png"
        .1
        "images/locate/incar/snow/11.png"
        .1
        "images/locate/incar/snow/10.png"
        .1
        "images/locate/incar/snow/9.png"
        .1
        "images/locate/incar/snow/8.png"
        .1
        "images/locate/incar/snow/7.png"
        .1
        "images/locate/incar/snow/6.png"
        .1
        "images/locate/incar/snow/5.png"
        .1
        "images/locate/incar/snow/4.png"
        .1
        "images/locate/incar/snow/3.png"
        .1
        "images/locate/incar/snow/2.png"
        .1
        "images/locate/incar/snow/1.png"
        .1
        repeat

    image d5_snow_up_rev dark1 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0001"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark2 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0002"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark3 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0003"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark4 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0004"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark5 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0005"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark6 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0006"), "d5_snow_up_rev")
        )
    image d5_snow_up_rev dark7 = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_up_rev",
        (0, 0), AlphaMask(Solid("#0007"), "d5_snow_up_rev")
        )


    image d5_snow_roll_1:
        "blizzard_d4_day_far"
        matrixcolor BrightnessMatrix(-0.65)
        parallel:
            ypan 30
            linear 3 ypan -360+30
            repeat
    image d5_snow_roll_2:
        "blizzard_d5_day2"
        matrixcolor BrightnessMatrix(-0.65)
    image d5_snow_roll = LiveComposite((1920, 1080),
        (0, 0), "d5_snow_roll_1",
        (0, 0), "d5_snow_roll_2")

    image snow_night_1_bg = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(10, 20), border=1000, start=0, fast=True),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(30, 40), border=1000, start=0, fast=True),
        
        
        )
    image snow_night_1_fg = LiveComposite((1920, 1080),
        
        
        (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(30, 40), border=1000, start=0, fast=True),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(25, 40), border=1000, start=0, fast=True),
        )
    image snow_night_close_fg = LiveComposite((1920, 1080),
        
        
        
        (0, 0), SnowBlossom("effect/snow/s007.png", count=15, yspeed=(80, 100), xspeed=(25, 40), border=1000, start=0, fast=True),
        )


    image sparks_1_01 = "effect/sparks/1/001.png"
    image sparks_1_02 = "effect/sparks/1/002.png"
    image sparks_1_03 = "effect/sparks/1/003.png"
    image sparks_1_04 = "effect/sparks/1/004.png"
    image sparks_1_05 = "effect/sparks/1/005.png"
    image sparks_1_06 = "effect/sparks/1/006.png"
    image sparks_1_07 = "effect/sparks/1/007.png"
    image sparks_1_08 = "effect/sparks/1/008.png"
    image sparks_1_09 = "effect/sparks/1/009.png"
    image sparks_1_10 = "effect/sparks/1/010.png"
    image sparks_1_11 = "effect/sparks/1/011.png"
    image sparks_1_12 = "effect/sparks/1/012.png"
    image sparks_1_13 = "effect/sparks/1/013.png"
    image sparks_1_14 = "effect/sparks/1/014.png"
    image sparks_1:
        "sparks_1_01"
        .1
        "sparks_1_02"
        .1
        "sparks_1_03"
        .1
        "sparks_1_04"
        .1
        "sparks_1_05"
        .1
        "sparks_1_06"
        .1
        "sparks_1_07"
        .1
        "sparks_1_08"
        .1
        "sparks_1_09"
        .1
        "sparks_1_10"
        .1
        "sparks_1_11"
        .1
        "sparks_1_12"
        .1
        "sparks_1_13"
        .1
        "sparks_1_14"
        .1
        Null()
        2.
        repeat
    image sparks_1_2:
        "sparks_1_01"
        .07
        "sparks_1_02"
        .07
        "sparks_1_03"
        .07
        "sparks_1_04"
        .07
        "sparks_1_05"
        .07
        "sparks_1_06"
        .07
        "sparks_1_07"
        .07
        "sparks_1_08"
        .07
        "sparks_1_09"
        .07
        "sparks_1_10"
        .07
        "sparks_1_11"
        .07
        "sparks_1_12"
        .07
        "sparks_1_13"
        .07
        "sparks_1_14"
        .07
        Null()
    image sparks_1_2_2:
        "sparks_1_01"
        .07
        "sparks_1_02"
        .07
        "sparks_1_03"
        .07
        "sparks_1_04"
        .07
        "sparks_1_05"
        .07
        "sparks_1_06"
        .07
        "sparks_1_07"
        .07
        "sparks_1_08"
        .07
        "sparks_1_09"
        .07
        "sparks_1_10"
        .07
        "sparks_1_11"
        .07
        "sparks_1_12"
        .07
        "sparks_1_13"
        .07
        "sparks_1_14"
        .07
        Null()
        2.
        repeat
    image sparks_1_3:
        "sparks_1_01"
        .04
        "sparks_1_02"
        .04
        "sparks_1_03"
        .04
        "sparks_1_04"
        .04
        "sparks_1_05"
        .04
        "sparks_1_06"
        .04
        "sparks_1_07"
        .04
        "sparks_1_08"
        .04
        "sparks_1_09"
        .04
        "sparks_1_10"
        .04
        "sparks_1_11"
        .04
        "sparks_1_12"
        .04
        "sparks_1_13"
        .04
        "sparks_1_14"
        .04
        Null()
        2.
        repeat

    image sparks_2_01 = "effect/sparks/2/001.png"
    image sparks_2_02 = "effect/sparks/2/002.png"
    image sparks_2_03 = "effect/sparks/2/003.png"
    image sparks_2_04 = "effect/sparks/2/004.png"
    image sparks_2:
        "sparks_2_01"
        0.1
        "sparks_2_02"
        0.1
        "sparks_2_03"
        0.1
        "sparks_2_04"
        0.1
        repeat
    image sparks_2_dark_05:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.05)
    image sparks_2_dark_10:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.10)
    image sparks_2_dark_15:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.15)
    image sparks_2_dark_20:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.20)
    image sparks_2_dark_25:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.25)
    image sparks_2_dark_30:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.30)
    image sparks_2_dark_35:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.35)
    image sparks_2_dark_40:
        "sparks_2"
        matrixcolor BrightnessMatrix(-0.40)

    image sparks_3_01 = "effect/sparks/3/001.png"
    image sparks_3_02 = "effect/sparks/3/002.png"
    image sparks_3_03 = "effect/sparks/3/003.png"
    image sparks_3_04 = "effect/sparks/3/004.png"
    image sparks_3:
        "sparks_3_01"
        0.1
        "sparks_3_02"
        0.1
        "sparks_3_03"
        0.1
        "sparks_3_04"
        0.1
        repeat

    image sparks_4_01 = "effect/sparks/4/001.png"
    image sparks_4_02 = "effect/sparks/4/002.png"
    image sparks_4_03 = "effect/sparks/4/003.png"
    image sparks_4_04 = "effect/sparks/4/004.png"
    image sparks_4:
        "sparks_4_01"
        0.1
        "sparks_4_02"
        0.1
        "sparks_4_03"
        0.1
        "sparks_4_04"
        0.1
        repeat

    transform tr_sparks_halfhigh(spr, zoom=1.0, xal=0.5, delay=0, stable=2.0, disap=0.5, endy=0.5, xoffset=0.15):
        spr
        zoom zoom
        parallel:
            pause delay
            alpha 1
            stable
            linear disap alpha 0
            repeat
        parallel:
            ypos 1.0 yanchor 0.0 xalign xal
            pause delay
            linear stable+disap ypos endy yanchor 1 xalign xal + xoffset
            repeat

    transform tr_sparks_2(spr, zoom=1.0, xal=0.5, delay=0.25, stable=2.0, app=0.25, disap=0.5, starty=1.0, endy=0.5, xoffset=0.15, xreverse=False):
        spr
        xzoom 1.0 - 2.0*int(xreverse)
        zoom zoom
        parallel:
            alpha 0
            pause delay
            linear app alpha 1
            stable
            linear disap alpha 0
            repeat
        parallel:
            ypos starty yanchor 0.0 xalign xal
            pause delay
            linear app+stable+disap ypos endy yanchor 1 xalign xal + xoffset
            repeat



    image d5_ba_house_dark = "locate/home/out_side/hOUSE_night.jpg"

    image d5_ba_window_head 1 = "locate/home/in_side/2st_floor/anton_room/window/an1.png"
    image d5_ba_window_head 2 = "locate/home/in_side/2st_floor/anton_room/window/an2.png"

    image d5_ba_hall_walkup:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 0.
            linear 2. xalign 1.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign -1.
            linear 2. xalign 1.
        contains:
            "bg_black"
            alpha 0
            1.5
            linear 0.5 alpha 1

    image d5_ba_olya = "images/locate/home/in_side/2st_floor/olga_room/sleep.png"
    image d5_ba_antonback = "images/locate/home/in_side/2st_floor/olga_room/Antonback.png"

    image d5_ba_rodichi = "sprite/ant/rodichi.png"



    image d5_br_window_bg = "locate/home/in_side/2st_floor/anton_room/window/fon.png"
    image d5_br_window_frame = "locate/home/in_side/2st_floor/anton_room/window/rama.png"
    image d5_br_window_head 1 = "locate/home/in_side/2st_floor/anton_room/window/head01.png"
    image d5_br_window_head 2 = "locate/home/in_side/2st_floor/anton_room/window/head02.png"
    image d5_br_window_reflect 1 = "locate/home/in_side/2st_floor/anton_room/window/001-003_009.png"
    image d5_br_window_reflect 2 = "locate/home/in_side/2st_floor/anton_room/window/002.png"
    image d5_br_window_reflect 3 = "locate/home/in_side/2st_floor/anton_room/window/001-003_009.png"
    image d5_br_window_reflect 4 = "locate/home/in_side/2st_floor/anton_room/window/004.png"
    image d5_br_window_reflect 5 = "locate/home/in_side/2st_floor/anton_room/window/005.png"
    image d5_br_window_reflect 6 = "locate/home/in_side/2st_floor/anton_room/window/006.png"
    image d5_br_window_reflect 7 = "locate/home/in_side/2st_floor/anton_room/window/007.png"
    image d5_br_window_reflect 8 = "locate/home/in_side/2st_floor/anton_room/window/008.png"
    image d5_br_window_reflect 9 = "locate/home/in_side/2st_floor/anton_room/window/001-003_009.png"

    image d5_br_cry_0 = "locate/home/in_side/2st_floor/olga_room/cry00.png"
    image d5_br_cry 1 = "locate/home/in_side/2st_floor/olga_room/cry01.png"
    image d5_br_cry 2 = "locate/home/in_side/2st_floor/olga_room/cry02.png"
    image d5_br_olya 1 = "locate/home/in_side/2st_floor/olga_room/olya_sleep.png"
    image d5_br_olya_m = "locate/home/in_side/2st_floor/olga_room/olya_sleepm.png"
    image d5_br_anton = "locate/home/in_side/2st_floor/olga_room/fon_room.png"

    define ol_gli_dt = 0.05
    image d5_br_olya_glitch:
        "locate/home/in_side/2st_floor/olga_room/olya_d/001.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/002.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/003.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/004.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/005.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/006.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/007.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/008.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/009.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/010.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/011.png"
        ol_gli_dt
        "locate/home/in_side/2st_floor/olga_room/olya_d/012.png"
        ol_gli_dt
        repeat

    image d5_br_home_bg = "locate/home/out_side/hOUSE_fon.jpg"
    image d5_br_home = "locate/home/out_side/hOUSE_obj.png"

    image d5_br_room_door_opened = "locate/home/in_side/2st_floor/anton_room/room_day/room_day_door.png"

    image d5_br_hall_door_closed = "locate/home/in_side/1st_floor/hall/door.jpg"
    image d5_br_hall_door_open = "locate/home/in_side/1st_floor/hall/door_open.jpg"
    image d5_br_hall_door_open_overlay = "locate/home/in_side/1st_floor/hall/hall_day_door.png"

    image d5_br_anton_madness = "sprite/ant/anton_smile.png"

    image d5_br_phone_hall:

        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 1.
            linear 2.3 xalign 0.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign 1.
            linear 2.3 xalign -1.

    image d5_br_m_1 = "locate/home/in_side/2st_floor/olga_room/eye/m01.png"
    image d5_br_m_2 = "locate/home/in_side/2st_floor/olga_room/eye/m02.png"
    image d5_br_m_3 = "locate/home/in_side/2st_floor/olga_room/eye/m03.png"

    transform mouth_tr(img1, img2):
        alpha 0
        img1

        parallel:
            choice:
                linear 0.05 xoffset 2
                linear 0.05 xoffset -2
            choice:
                linear 0.05 xoffset 3
                linear 0.05 xoffset -3
            choice:
                linear 0.05 xoffset 5
                linear 0.05 xoffset -5
            repeat

        parallel:
            choice:
                yoffset -300
                linear 4 yoffset 300

            choice:
                yoffset 300
                linear 4 yoffset -300

            choice:
                yoffset -100
                linear 4 yoffset 100

            choice:
                yoffset 100
                linear 4 yoffset -100

        parallel:
            block:
                choice:
                    .25
                choice:
                    .75
                choice:
                    1.25

            linear .25 alpha 1

            block:
                choice:
                    .25
                choice:
                    .75
                choice:
                    1.25

            img2

            block:
                choice:
                    .25
                choice:
                    .75
                choice:
                    1.25

            img1

            block:
                choice:
                    .25
                choice:
                    .75
                choice:
                    1.25

            linear .5 alpha 0

    image d5_br_mouth_12:
        contains mouth_tr("d5_br_m_1", "d5_br_m_2")
    image d5_br_mouth_23:
        contains mouth_tr("d5_br_m_2", "d5_br_m_3")
    image d5_br_mouth_13:
        contains mouth_tr("d5_br_m_1", "d5_br_m_3")

    image d5_myth = "locate/home/in_side/2st_floor/anton_room/n05.png"


    image d5_zh_kitchen = "locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg"
    image d5_zh_window_bg = "locate/home/in_side/1st_floor/kitchen/widow/fon_r.png"
    image d5_zh_window_frame = "locate/home/in_side/1st_floor/kitchen/widow/RAMA.png"
    image d5_zh_window_zhu_blured = "locate/home/in_side/1st_floor/kitchen/widow/Zu1.png"
    image d5_zh_window_zhu_clear = "locate/home/in_side/1st_floor/kitchen/widow/Zu2.png"

    image d5_zh_hall_bg = "locate/home/in_side/1st_floor/hall/Fon_k.png"
    image d5_zh_hall_closed = "locate/home/in_side/1st_floor/hall/Fon_door.png"
    image d5_zh_hall_opened = "locate/home/in_side/1st_floor/hall/Fon_doorOP.png"

    image bg in_fridge0 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_0.jpg"
    image bg in_fridge00 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_00.jpg"
    image empty_pantry = "locate/home/in_side/1st_floor/hall/pantry_00.png"
    image bg_in_fridge_olya = "sprite/Olya/Olya_back.png"

    image d5_zhulka idle = "locate/home/in_side/1st_floor/hall/sobaken.png"
    image d5_zhulka dark:
        Composite((1920, 1080),
            (0, 0), "d5_zhulka idle",
            (0, 0), AlphaMask(Solid("#0004"), "d5_zhulka idle")
            )
        align (.5, .5)
        zoom 0.45
        offset (-150, 100)
    image d5_zhulka pickedup = "locate/home/in_side/1st_floor/dog.png"
    image d5_zhulka pat = "locate/home/in_side/1st_floor/kitchen/zul01.png"
    image d5_zhulka idle2 = "locate/home/in_side/1st_floor/kitchen/zul02.png"
    image d5_zhulka happy = "locate/home/in_side/1st_floor/kitchen/zul03.png"
    image d5_zhulka sosiska = "locate/home/in_side/1st_floor/kitchen/zul04.png"
    image d5_zhulka aside = "locate/home/in_side/1st_floor/kitchen/zul05.png"
    image d5_zhulka ahead = "locate/home/in_side/1st_floor/kitchen/zul06.png"
    image d5_zhulka scrap_happy = "locate/home/in_side/1st_floor/hall/sobaken2.png"
    image d5_zhulka scrap_angry = "locate/home/in_side/1st_floor/hall/sobaken02.png"
    image d5_zhulka angry = "locate/home/in_side/1st_floor/hall/sobaken3.png"

    image d5_zhulka angry dark:
        Composite((1920, 1080),
            (0, 0), "d5_zhulka angry",
            (0, 0), AlphaMask(Solid("#0004"), "d5_zhulka angry")
            )
        align (.5, .5)
        zoom 0.45
        offset (-150, 100)

    image d5_zhulka angrysmall = "locate/home/in_side/1st_floor/hall/sobaken4.png"
    image d5_zhulka happysmall = "locate/home/in_side/1st_floor/hall/sobaken5.png"
    image d5_zhulka angrybig = "locate/home/in_side/1st_floor/hall/sobaken6.png"
    image d5_zhulka happysmall2 = "locate/home/in_side/1st_floor/hall/sobaken7.png"
    image d5_zhulka cautious = "locate/home/in_side/1st_floor/kitchen/zul003.png"

    image d5_zhulka tail:
        block:
            "locate/home/in_side/1st_floor/kitchen/zul07.png"
            .15
            "locate/home/in_side/1st_floor/kitchen/zul08.png"
            .15
            "locate/home/in_side/1st_floor/kitchen/zul09.png"
            .15
            repeat

    image d5_zhulka tail_highlight:
        "d5_zhulka tail"
        matrixcolor BrightnessMatrix(0.1)

    image d5_zh_floor = "locate/home/in_side/1st_floor/kitchen/floor.png"

    image d5_zh_bones = "locate/home/in_side/1st_floor/kitchen/bones1.png"
    image d5_zh_paper = "locate/home/in_side/1st_floor/kitchen/bones_paper.png"

    image d5_axe 1 = "locate/home/in_side/1st_floor/kitchen/treat/001.png"
    image d5_axe 2 = "locate/home/in_side/1st_floor/kitchen/treat/002.png"
    image d5_axe 3 = "locate/home/in_side/1st_floor/kitchen/treat/003.png"
    image d5_axe 4 = "locate/home/in_side/1st_floor/kitchen/treat/004.png"
    image d5_axe 5 = "locate/home/in_side/1st_floor/kitchen/treat/005.png"
    image d5_axe 6 = "locate/home/in_side/1st_floor/kitchen/treat/006.png"
    image d5_axe 7 = "locate/home/in_side/1st_floor/kitchen/treat/007.png"
    image d5_axe 8 = "locate/home/in_side/1st_floor/kitchen/treat/008.png"
    image d5_axe 9 = "locate/home/in_side/1st_floor/kitchen/treat/009.png"
    image d5_axe 10 = "locate/home/in_side/1st_floor/kitchen/treat/010.png"
    image d5_axe 11 = "locate/home/in_side/1st_floor/kitchen/treat/011.png"
    image d5_axe 12 = "locate/home/in_side/1st_floor/kitchen/treat/012.png"

    image d5_axe raise:
        "d5_axe 1"
        0.1
        "d5_axe 2"
        0.1
        "d5_axe 3"
        0.1
        "d5_axe 4"
        0.1
        "d5_axe 5"
        0.1
        "d5_axe 6"
        0.1
        "d5_axe 7"
        0.1
        "d5_axe idle"
    image d5_axe idle:
        "d5_axe 7"
        0.1
        "d5_axe 8"
        0.1
        repeat
    image d5_axe kill:
        "d5_axe 9"
        0.1
        "d5_axe 10"
        0.1
        "d5_axe 11"
        0.1
        "d5_axe 12"
        0.1
        Null() with hpunch

    image d5_axe2 1 = "locate/home/in_side/1st_floor/kitchen/treat/3/001.png"
    image d5_axe2 2 = "locate/home/in_side/1st_floor/kitchen/treat/3/002.png"
    image d5_axe2 3 = "locate/home/in_side/1st_floor/kitchen/treat/3/003.png"
    image d5_axe2 4 = "locate/home/in_side/1st_floor/kitchen/treat/3/004.png"
    image d5_axe2 5 = "locate/home/in_side/1st_floor/kitchen/treat/3/005.png"
    image d5_axe2 6 = "locate/home/in_side/1st_floor/kitchen/treat/3/006.png"
    image d5_axe2 7 = "locate/home/in_side/1st_floor/kitchen/treat/3/007.png"
    image d5_axe2 8 = "locate/home/in_side/1st_floor/kitchen/treat/3/008.png"
    image d5_axe2 9 = "locate/home/in_side/1st_floor/kitchen/treat/3/009.png"
    image d5_axe2 10 = "locate/home/in_side/1st_floor/kitchen/treat/3/010.png"
    image d5_axe2 11 = "locate/home/in_side/1st_floor/kitchen/treat/3/011.png"
    image d5_axe2 12 = "locate/home/in_side/1st_floor/kitchen/treat/3/012.png"

    image d5_axe2 raise:
        "d5_axe2 1"
        0.1
        "d5_axe2 2"
        0.1
        "d5_axe2 3"
        0.1
        "d5_axe2 4"
        0.1
        "d5_axe2 5"
        0.1
        "d5_axe2 6"
        0.1
        "d5_axe2 7"
        0.1
        "d5_axe2 idle"
    image d5_axe2 idle:
        "d5_axe2 7"
        0.1
        "d5_axe2 8"
        0.1
        repeat
    image d5_axe2 kill:
        "d5_axe2 9"
        0.1
        "d5_axe2 10"
        0.1
        "d5_axe2 11"
        0.1
        "d5_axe2 12"
        0.1
        Null() with hpunch

    image d5_bloodied_axe 1 = "locate/home/in_side/1st_floor/kitchen/treat/2/001.png"
    image d5_bloodied_axe 2 = "locate/home/in_side/1st_floor/kitchen/treat/2/002.png"
    image d5_bloodied_axe 3 = "locate/home/in_side/1st_floor/kitchen/treat/2/003.png"
    image d5_bloodied_axe 4 = "locate/home/in_side/1st_floor/kitchen/treat/2/004.png"
    image d5_bloodied_axe 5 = "locate/home/in_side/1st_floor/kitchen/treat/2/005.png"
    image d5_bloodied_axe 6 = "locate/home/in_side/1st_floor/kitchen/treat/2/006.png"
    image d5_bloodied_axe 7 = "locate/home/in_side/1st_floor/kitchen/treat/2/007.png"
    image d5_bloodied_axe 8 = "locate/home/in_side/1st_floor/kitchen/treat/2/008.png"
    image d5_bloodied_axe 9 = "locate/home/in_side/1st_floor/kitchen/treat/2/009.png"
    image d5_bloodied_axe 10 = "locate/home/in_side/1st_floor/kitchen/treat/2/010.png"
    image d5_bloodied_axe 11 = "locate/home/in_side/1st_floor/kitchen/treat/2/011.png"
    image d5_bloodied_axe 12 = "locate/home/in_side/1st_floor/kitchen/treat/2/012.png"

    image d5_bloodied_axe raise:
        "d5_bloodied_axe 1"
        0.1
        "d5_bloodied_axe 2"
        0.1
        "d5_bloodied_axe 3"
        0.1
        "d5_bloodied_axe 4"
        0.1
        "d5_bloodied_axe 5"
        0.1
        "d5_bloodied_axe 6"
        0.1
        "d5_bloodied_axe 7"
        0.1
        "d5_bloodied_axe idle"
    image d5_bloodied_axe idle:
        "d5_bloodied_axe 7"
        0.1
        "d5_bloodied_axe 8"
        0.1
        repeat
    image d5_bloodied_axe kill:
        "d5_bloodied_axe 9"
        0.1
        "d5_bloodied_axe 10"
        0.1
        "d5_bloodied_axe 11"
        0.1
        "d5_bloodied_axe 12"
        0.1
        Null() with hpunch

    image d5_zhulka_hands 1 = "locate/cemetery/axe/axe1.png"
    image d5_zhulka_hands 2 = "locate/cemetery/axe/axe2.png"
    image d5_zhulka_hands 3 = "locate/cemetery/axe/axe3.png"

    image d5_zhulka_hands loop:
        animation
        block:
            "d5_zhulka_hands 1"
            .2
            "d5_zhulka_hands 2"
            .2
            repeat

    image d5_zhulka_hands loop_highlight:
        "d5_zhulka_hands loop"
        matrixcolor BrightnessMatrix(0.1)

    default d5_choice_zhulka_dog_hover = False
    default d5_choice_zhulka_hands_hover = False

    image d5_choice_zhulka_dog = ConditionSwitch(
        "d5_choice_zhulka_dog_hover", "d5_zhulka tail_highlight",
        True, "d5_zhulka cautious"
    )
    image d5_zhulka_hands choice = ConditionSwitch(
        "d5_choice_zhulka_hands_hover", "d5_zhulka_hands loop_highlight",
        True, "d5_zhulka_hands 1"
    )


    image d5_mercy_axedrop_bg = "locate/home/in_side/1st_floor/kitchen/afon.png"
    image d5_mercy_axedrop_hand = "locate/home/in_side/1st_floor/kitchen/ahend.png"
    image d5_mercy_axedrop_axe = "locate/home/in_side/1st_floor/kitchen/axe.png"

    image d5_mercy_axedrop_bloodiedhand = "locate/home/in_side/1st_floor/kitchen/ahend2.png"
    image d5_mercy_axedrop_bloodiedaxe = "locate/home/in_side/1st_floor/kitchen/Axe002.png"

    image d5_mercy_olyafall_bg = "locate/home/in_side/1st_floor/hall/bug/fonfloor.png"
    image d5_mercy_olyafall_ball = "locate/home/in_side/1st_floor/hall/bug/ball.png"
    image d5_mercy_olyafall = "locate/home/in_side/1st_floor/hall/bug/ol.png"
    image d5_mercy_olyafall2 = "locate/home/in_side/1st_floor/hall/bug/olya_sleep.png"
    image d5_mercy_olyafall2_talk = "locate/home/in_side/1st_floor/hall/bug/olya_sleep2.png"



    image d5_hall_runup:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 0.
            linear 4. xalign 1.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign -1.
            linear 4. xalign 1.
        contains:
            "bg_black"
            alpha 0
            3.5
            linear 0.5 alpha 1


    image d5_kill_blood_1 = "locate/home/in_side/1st_floor/kitchen/blood/001.png"
    image d5_kill_blood_2 = "locate/home/in_side/1st_floor/kitchen/blood/002.png"
    image d5_kill_blood_3 = "locate/home/in_side/1st_floor/kitchen/blood/003.png"
    image d5_kill_blood_4 = "locate/home/in_side/1st_floor/kitchen/blood/004.png"
    image d5_kill_blood_5 = "locate/home/in_side/1st_floor/kitchen/blood/005.png"
    image d5_kill_blood_6 = "locate/home/in_side/1st_floor/kitchen/blood/006.png"
    image d5_kill_blood_7 = "locate/home/in_side/1st_floor/kitchen/blood/007.png"
    image d5_kill_blood_8 = "locate/home/in_side/1st_floor/kitchen/blood/008.png"
    image d5_kill_blood_9 = "locate/home/in_side/1st_floor/kitchen/blood/009.png"
    image d5_kill_blood_10 = "locate/home/in_side/1st_floor/kitchen/blood/010.png"
    image d5_kill_blood_11 = "locate/home/in_side/1st_floor/kitchen/blood/011.png"
    image d5_kill_blood_12 = "locate/home/in_side/1st_floor/kitchen/blood/012.png"

    image d5_kill_blood_12_dark 15 = AlphaMask(Solid("#0002", xysize=(2563, 1080)), "d5_kill_blood_12")
    image d5_kill_blood_12_dark 30 = AlphaMask(Solid("#0004", xysize=(2563, 1080)), "d5_kill_blood_12")
    image d5_kill_blood_12_dark 40 = AlphaMask(Solid("#0006", xysize=(2563, 1080)), "d5_kill_blood_12")
    image d5_kill_blood_12_dark 50 = AlphaMask(Solid("#0008", xysize=(2563, 1080)), "d5_kill_blood_12")
    image d5_kill_blood_12_dark 60 = AlphaMask(Solid("#000a", xysize=(2563, 1080)), "d5_kill_blood_12")
    image d5_kill_blood_12_dark 70 = AlphaMask(Solid("#000c", xysize=(2563, 1080)), "d5_kill_blood_12")

    image d5_kill_blood_alert = "locate/home/in_side/1st_floor/kitchen/blood/1.png"
    image d5_kill_blood_overlay_1 = "locate/home/in_side/1st_floor/kitchen/blood/2.png"
    image d5_kill_blood_overlay_2 = "locate/home/in_side/1st_floor/kitchen/blood/3.png"

    image d5_kill_blood_bg = "locate/home/in_side/1st_floor/kitchen/blood/fon.png"
    image d5_kill_blood_bg2 = "locate/home/in_side/1st_floor/kitchen/blood/fon2.png"

    image d5_kill_blood_animation:
        "d5_kill_blood_1"
        1.
        "d5_kill_blood_2"
        .1
        "d5_kill_blood_3"
        .1
        "d5_kill_blood_4"
        .1
        "d5_kill_blood_5"
        .1
        "d5_kill_blood_6"
        .1
        "d5_kill_blood_7"
        .1
        "d5_kill_blood_8"
        .1
        "d5_kill_blood_9"
        .1
        "d5_kill_blood_10"

    image d5_kill_blood_blink:
        Null()
        4.
        "d5_kill_blood_overlay_1"
        .1
        "d5_kill_blood_overlay_2"
        .1
        "d5_kill_blood_overlay_1"
        .1
        repeat

    image d5_kill_blood_hand = "locate/home/in_side/1st_floor/hall/bug/bloodyhand.png"

    image d5_kill_blood_blinking:
        contains:
            "d5_kill_blood_1"
        contains:
            "d5_kill_blood_blink"

    image d5_kill_blood_01 = LiveComposite((2563, 1080),
        (0, 0), "d5_kill_blood_11",
        (643, 0), "d5_kill_blood_blinking")


    image d5_kill_blood 0 = "locate/home/in_side/1st_floor/hall/dog/blood0.png"
    image d5_kill_blood 1 = "locate/home/in_side/1st_floor/hall/dog/blood.png"
    image d5_kill_blood 2 = "locate/home/in_side/1st_floor/hall/dog/blood2.png"
    image d5_kill_blood 3 = "locate/home/in_side/1st_floor/hall/dog/blood3.png"
    image d5_kill_lock = "locate/home/in_side/1st_floor/hall/bug/lock.png"
    image d5_kill_dog_1 = "locate/home/in_side/1st_floor/hall/dog/dog01.png"
    image d5_kill_dog_2 = "locate/home/in_side/1st_floor/hall/dog/dog02.png"
    image d5_kill_dog_3 = "locate/home/in_side/1st_floor/hall/dog/dog03.png"
    image d5_kill_dog_4 = "locate/home/in_side/1st_floor/hall/dog/dog04.png"
    image d5_kill_dog_5 = "locate/home/in_side/1st_floor/hall/dog/dog05.png"
    image d5_kill_dog_6 = "locate/home/in_side/1st_floor/hall/dog/dog06.png"
    image d5_kill_dog_7 = "locate/home/in_side/1st_floor/hall/dog/dog07.png"
    image d5_kill_dog_8 = "locate/home/in_side/1st_floor/hall/dog/dog08.png"
    image d5_kill_dog_9 = "locate/home/in_side/1st_floor/hall/dog/dog09.png"
    image d5_kill_dog_10 = "locate/home/in_side/1st_floor/hall/dog/dog10.png"
    image d5_kill_dog_11 = "locate/home/in_side/1st_floor/hall/dog/dog11.png"
    image d5_kill_dog_loop 1:
        "d5_kill_dog_1"
        .3
        "d5_kill_dog_2"
        .3
        repeat
    image d5_kill_dog_loop 2:
        "d5_kill_dog_3"
        .3
        "d5_kill_dog_4"
        .3
        "d5_kill_dog_3"
        .3
        "d5_kill_dog_4"
        3.
        repeat
    image d5_kill_dog_loop 3:
        "d5_kill_dog_5"
        .15
        "d5_kill_dog_6"
        .15
        "d5_kill_dog_7"
        .15
        "d5_kill_dog_8"

    image d5_kill_anton = "locate/home/in_side/1st_floor/hall/Anton_blood.png"
    image d5_kill_anton_mouth = "locate/home/in_side/1st_floor/hall/Anton_blood_scream.png"

    image d5_kill_bug_1 = "locate/home/in_side/1st_floor/hall/bug/01.png"
    image d5_kill_bug_2 = "locate/home/in_side/1st_floor/hall/bug/02.png"
    image d5_kill_bug_3 = "locate/home/in_side/1st_floor/hall/bug/03.png"
    image d5_kill_bug_4 = "locate/home/in_side/1st_floor/hall/bug/04.png"
    image d5_kill_bug_5 = "locate/home/in_side/1st_floor/hall/bug/05.png"
    image d5_kill_bug_6 = "locate/home/in_side/1st_floor/hall/bug/06.png"
    image d5_kill_bug_7 = "locate/home/in_side/1st_floor/hall/bug/07.png"
    image d5_kill_bug_8 = "locate/home/in_side/1st_floor/hall/bug/08.png"
    image d5_kill_bug_9 = "locate/home/in_side/1st_floor/hall/bug/09.png"
    image d5_kill_bug_10 = "locate/home/in_side/1st_floor/hall/bug/10.png"
    image d5_kill_bug_11 = "locate/home/in_side/1st_floor/hall/bug/11.png"
    image d5_kill_bug_12 = "locate/home/in_side/1st_floor/hall/bug/12.png"

    image d5_kill_bug_phased = "locate/home/in_side/1st_floor/hall/bug/monsterspider.png"


    image d5_kill_bug_animation:
        "d5_kill_bug_1"
        .1
        "d5_kill_bug_2"
        .1
        "d5_kill_bug_3"
        .1
        "d5_kill_bug_4"
        .1
        "d5_kill_bug_5"
        .1
        "d5_kill_bug_6"
        .1
        "d5_kill_bug_7"
        .1
        "d5_kill_bug_8"
        .1
        "d5_kill_bug_9"
        .1
        "d5_kill_bug_10"
        .1
        "d5_kill_bug_11"
        .1
        "d5_kill_bug_12"
        .1
        repeat

    image d5_kill_olyaout_fonfloor = "locate/home/in_side/1st_floor/hall/bug/fonfloor.png"
    image d5_kill_olyaout_olya = "locate/home/in_side/1st_floor/hall/bug/ol.png"

    image d5_kill_alisa_1 = "locate/home/in_side/1st_floor/hall/bug/fox_01.png"
    image d5_kill_alisa_2 = "locate/home/in_side/1st_floor/hall/bug/fox_02.png"
    image d5_kill_alisa_3 = "locate/home/in_side/1st_floor/hall/bug/fox_03.png"
    image d5_kill_alisa_4 = "locate/home/in_side/1st_floor/hall/bug/fox_04.png"
    image d5_kill_alisa_5 = "locate/home/in_side/1st_floor/hall/bug/fox_05.png"
    image d5_kill_alisa_6 = "locate/home/in_side/1st_floor/hall/bug/fox_06.png"
    image d5_kill_alisa_7 = "locate/home/in_side/1st_floor/hall/bug/fox_07.png"
    image d5_kill_alisa_8 = "locate/home/in_side/1st_floor/hall/bug/fox_08.png"
    image d5_kill_alisa_9 = "locate/home/in_side/1st_floor/hall/bug/fox_09.png"
    image d5_kill_alisa_10 = "locate/home/in_side/1st_floor/hall/bug/fox_10.png"
    image d5_kill_alisa_11 = "locate/home/in_side/1st_floor/hall/bug/fox_11.png"
    image d5_kill_alisa_12 = "locate/home/in_side/1st_floor/hall/bug/fox_12.png"
    image d5_kill_alisa_13 = "locate/home/in_side/1st_floor/hall/bug/fox_13.png"
    image d5_kill_alisa_14 = "locate/home/in_side/1st_floor/hall/bug/fox_14.png"
    image d5_kill_alisa_15 = "locate/home/in_side/1st_floor/hall/bug/fox_15.png"
    image d5_kill_alisa_animation:
        "d5_kill_alisa_1"
        .1
        "d5_kill_alisa_2"
        .1
        "d5_kill_alisa_3"
        .1
        "d5_kill_alisa_4"
        .1
        "d5_kill_alisa_5"
        .1
        "d5_kill_alisa_6"
        .1
        "d5_kill_alisa_7"
        .1
        "d5_kill_alisa_8"
        .1
        "d5_kill_alisa_9"
        .1
        "d5_kill_alisa_10"
        .1
        "d5_kill_alisa_11"
        .1
        "d5_kill_alisa_12"
        .1
        "d5_kill_alisa_13"
        .1
        "d5_kill_alisa_14"
        .1
        "d5_kill_alisa_15"

    image d5_kill_olyasleep = "locate/home/in_side/1st_floor/hall/bug/olya_sleep.png"
    image d5_kill_olyasleep talk:
        contains:
            "d5_kill_olyasleep"
        contains:
            "locate/home/in_side/1st_floor/hall/bug/Olya_sleep2.png"
    image d5_kill_dirt = "locate/home/in_side/1st_floor/hall/bug/dirt.png"
    image d5_kill_dark_home = "locate/home/out_side/hOUSE_night10.png"

    image d5_kill_darkwindow_frame = "locate/home/in_side/1st_floor/kitchen/widow/rama_dark.png"
    image d5_kill_darkwindow_bg = "locate/home/in_side/1st_floor/kitchen/widow/fon_dark.png"


    default d5_md_drug_hover = False
    default d5_md_olya_hover = False

    image d5_medication_undertable 2 = "locate/home/in_side/1st_floor/kitchen/Table_ka2.png"
    image d5_medication_undertable 3 = "locate/home/in_side/1st_floor/kitchen/Table_ka3.png"
    image d5_medication_undertable 4 = "locate/home/in_side/1st_floor/kitchen/Table_ka4.png"
    image d5_medication_undertable 5 = "locate/home/in_side/1st_floor/kitchen/Table_ka5.png"
    image d5_medication_undertable 6 = "locate/home/in_side/1st_floor/kitchen/Table_ka6.png"
    image d5_medication_undertable 7 = "locate/home/in_side/1st_floor/kitchen/Table_ka7.png"
    image d5_medication_undertable 8 = "locate/home/in_side/1st_floor/kitchen/Table_ka8.png"
    image d5_medication_undertable 9 = "locate/home/in_side/1st_floor/kitchen/Table_ka9.png"

    image d5_medication_overlay_1 = "locate/home/in_side/1st_floor/kitchen/table_home1.png"
    image d5_medication_overlay_2 = "locate/home/in_side/1st_floor/kitchen/table_home2.png"
    image d5_medication_overlay_water = "locate/home/in_side/1st_floor/kitchen/water.png"

    image d5_medication_olya_eyes 1 = "locate/home/in_side/1st_floor/hall/bug/Olya_glas.png"
    image d5_medication_olya_eyes 2 = "locate/home/in_side/1st_floor/hall/bug/Olya_glas2.png"

    image d5_medication_forest = "locate/forest/wood_n.jpg"

    image d5_medication_hands = "locate/polina/rom_dark/hands.png"

    image d5_medication_drug_hand_img = "locate/home/in_side/1st_floor/hall/draghand.png"
    image d5_medication_drug_hand_shade = AlphaMask(Solid("#0008"), "d5_medication_drug_hand_img")
    image d5_medication_drug_hand:
        contains:
            "d5_medication_drug_hand_img"
        contains:
            "d5_medication_drug_hand_shade"
    image d5_medication_drug_hand_disp:
        animation
        "d5_medication_drug_hand"
        block:
            ease 2 xoffset 5 yoffset 5
            ease 2 xoffset 0 yoffset 0
            ease 2 xoffset -5 yoffset 5
            repeat

    image d5_medication_drug_hand2_img = "locate/home/in_side/1st_floor/hall/draghand2.png"
    image d5_medication_drug_hand2_shade = AlphaMask(Solid("#0008"), "d5_medication_drug_hand2_img")
    image d5_medication_drug_hand2:
        contains:
            "d5_medication_drug_hand2_img"
        contains:
            "d5_medication_drug_hand2_shade"
    image d5_medication_drug_hand2_disp:
        animation
        "d5_medication_drug_hand2"
        block:
            ease 2 xoffset 5 yoffset 5
            ease 2 xoffset 0 yoffset 0
            ease 2 xoffset -5 yoffset 5
            repeat

    image d5_medication_drug_hand_dark = ConditionSwitch(
        "d5_md_drug_hover", "d5_medication_drug_hand2_disp",
        "True", "d5_medication_drug_hand_disp",
    )

    image d5_medication_drug_hand_white:
        animation
        "d5_medication_drug_hand_img"
        block:
            ease 2 xoffset 5 yoffset 5
            ease 2 xoffset 0 yoffset 0
            ease 2 xoffset -5 yoffset 5
            repeat

    image d5_medication_dad = Composite((723, 1080),
        (0, 0), "sprite/Dad/Angry/m_day/1_body/01.png",
        (0, 0), "sprite/Dad/Angry/m_day/2_eyes/norm/ahead/01.png")

    image d5_medication_mom = Composite((674, 1080),
        (0, 0), "sprite/Mom/Normal/m_day/1_body/00.png",
        (0, 0), "sprite/Mom/Normal/m_day/2_eyes/norm/ahead/01.png")

    image d5_medication_kidnap_1 = "locate/polina/rom_dark/hands2.png"
    image d5_medication_kidnap_2 = "locate/polina/rom_dark/hands3.png"
    image d5_medication_kidnap_3 = "locate/polina/rom_dark/hands4.png"
    image d5_medication_kidnap_4 = "locate/polina/rom_dark/hands5.png"
    image d5_medication_kidnap_5 = "locate/polina/rom_dark/hands6.png"
    image d5_medication_kidnap:
        "d5_medication_kidnap_1"
        0.1
        "d5_medication_kidnap_2"
        0.1
        "d5_medication_kidnap_3"
        0.1
        "d5_medication_kidnap_4"
        0.1
        "d5_medication_kidnap_5"
        0.1
        "bg_black"


    image d5_mstory_mindwirl:
        animation
        block:
            "locate/school/in_side/Sem_gone/f_05.jpg" with Dissolve(0.25)
            0.5
            "locate/school/in_side/Sem_gone/f_04.jpg" with Dissolve(0.25)
            0.5
            "locate/school/in_side/Sem_gone/f_03.jpg" with Dissolve(0.25)
            0.5
            "locate/school/in_side/Sem_gone/f_02.jpg" with Dissolve(0.25)
            0.5
            "locate/school/in_side/Sem_gone/f_01.jpg" with Dissolve(0.25)
            0.5
            repeat

    image d5_mstory_garage_bg_high = "locate/katya/gar_ant/bg.png"

    image d5_mstory_garage_kavkaz_bg = "locate/katya/gar_ant/fon.png"
    image d5_mstory_garage_kavkaz_anton = "locate/katya/gar_ant/anton.png"
    image d5_mstory_garage_kavkaz_eyes_up = "locate/katya/gar_ant/up.png"
    image d5_mstory_garage_kavkaz_eyes_down = "locate/katya/gar_ant/down.png"
    image Ant Plen Up_base:
        contains:
            "d5_mstory_garage_kavkaz_anton"
        contains:
            "d5_mstory_garage_kavkaz_eyes_up"
    image Ant Plen Down_base:
        contains:
            "d5_mstory_garage_kavkaz_anton"
        contains:
            "d5_mstory_garage_kavkaz_eyes_down"

    image Ant Plen Up:
        animation
        "Ant Plen Up_base"
        subpixel True
        align (.65, .0)
        yoffset -25
        xoffset -300
        zoom 0.8
        transform_anchor True
        rotate -1
        parallel:
            ease 3 rotate 1
            ease 3 rotate -1
            repeat
    image Ant Plen Down:
        animation
        "Ant Plen Down_base"
        subpixel True
        align (.65, .0)
        yoffset -25
        xoffset -300
        zoom 0.8
        transform_anchor True
        rotate -1
        parallel:
            ease 3 rotate 1
            ease 3 rotate -1
            repeat

    image d5_garage_katya_bg = "locate/street/garage/katy3.png"
    image d5_garage_katya_mincer = "locate/street/garage/katy.png"
    image d5_garage_katya_person_base = "locate/street/garage/k1.png"
    image d5_garage_katya_person_eyes = "locate/street/garage/k2.png"
    image d5_garage_katya_person 1 = "d5_garage_katya_person_base"
    image d5_garage_katya_person 2:
        contains:
            "d5_garage_katya_person_base"
        contains:
            "d5_garage_katya_person_eyes"
            alpha 0
    image d5_garage_katya_person 3:
        contains:
            "d5_garage_katya_person_base"
        contains:
            "d5_garage_katya_person_eyes"

    image d5_mstory_garage_bg_1 = "locate/street/garage/gar/r001.png"
    image d5_mstory_garage_bg_2 = "locate/street/garage/gar/r002.png"
    image d5_mstory_garage_bg_3 = "locate/street/garage/gar/r003.png"
    image d5_mstory_garage_bg:
        "d5_mstory_garage_bg_1"
        0.2
        "d5_mstory_garage_bg_2"
        0.2
        "d5_mstory_garage_bg_3"
        0.2
        repeat

    image d5_mstory_garage_door_right = "locate/street/garage/gar/door_01.png"
    image d5_mstory_garage_door_left = "locate/street/garage/gar/door_04.png"
    image d5_mstory_garage_door_left_roma = "locate/street/garage/gar/door_03.png"

    image d5_mstory_garant_bg = "locate/Katya/gar_ant/bg2.png"
    image d5_mstory_garant_child 1 = "locate/Katya/gar_ant/o1.png"
    image d5_mstory_garant_child 2 = "locate/Katya/gar_ant/o2.png"
    image d5_mstory_garant_child 3 = "locate/Katya/gar_ant/o3.png"
    image d5_mstory_garant_child 4 = "locate/Katya/gar_ant/o4.png"
    image d5_mstory_garant_child 5 = "locate/Katya/gar_ant/o5.png"
    image d5_mstory_garant_child 6 = "locate/Katya/gar_ant/o6.png"
    image d5_mstory_garant_child 7 = "locate/Katya/gar_ant/o7.png"
    image d5_mstory_garant_child 8 = "locate/Katya/gar_ant/o8.png"

    image d5_mstory_garant_child loop:
        choice 3:
            "d5_mstory_garant_child 1"
            .1
            "d5_mstory_garant_child 2"
            .1
            "d5_mstory_garant_child 3"
            .1
            "d5_mstory_garant_child 4"
            .1
        choice 1:
            "d5_mstory_garant_child 5"
            .1
            "d5_mstory_garant_child 6"
            .1
            "d5_mstory_garant_child 7"
            .1
            "d5_mstory_garant_child 8"
            .1
        repeat

    image d5_mstory_garant_bg_full = LiveComposite((2160, 1960),
        (0, 0), "d5_mstory_garant_bg",
        (0, 0), "d5_mstory_garant_child loop")
    image d5_mstory_garant_bg_animated:
        animation
        "d5_mstory_garant_bg_full"
        subpixel True
        xalign .5
        yoffset 50
        block:
            parallel:
                easein 3. xalign 1.
                easeout 3. xalign .5
                easein 3. xalign 0.
                easeout 3. xalign .5
                repeat
            parallel:
                ease 3.0 yoffset 0
                ease 3.0 yoffset 50
                repeat

    image d5_mstory_romknife_smile = "locate/street/rom_knife/R_knife10.png"

    image d5_mstory_garage_ant = "locate/street/garage/an.png"

    image d5_mstory_mincer_1 = "locate/katya/mincer/4/1.png"
    image d5_mstory_mincer_2 = "locate/katya/mincer/4/2.png"
    image d5_mstory_mincer_3 = "locate/katya/mincer/4/3.png"
    image d5_mstory_mincer_4 = "locate/katya/mincer/4/4.png"
    image d5_mstory_mincer_5 = "locate/katya/mincer/4/5.png"
    image d5_mstory_mincer:
        "d5_mstory_mincer_1"
        .075
        "d5_mstory_mincer_2"
        .075
        "d5_mstory_mincer_3"
        .075
        "d5_mstory_mincer_4"
        .075
        "d5_mstory_mincer_5"
        .075
        repeat

    image d5_mstory_mincer_slowdown_1:
        "d5_mstory_mincer_1"
        .15
        "d5_mstory_mincer_2"
        .15
        "d5_mstory_mincer_3"
        .15
        "d5_mstory_mincer_4"
        .15
        "d5_mstory_mincer_5"
        .15
        repeat

    image d5_mstory_mincer_slowdown_2:
        "d5_mstory_mincer_1"
        .45
        "d5_mstory_mincer_2"
        .45
        "d5_mstory_mincer_3"
        .45
        "d5_mstory_mincer_4"
        .45
        "d5_mstory_mincer_5"

    image d5_mstory_mincer_slowdown:
        "d5_mstory_mincer"
        1.125
        "d5_mstory_mincer_slowdown_1"
        1.5
        "d5_mstory_mincer_slowdown_2"

    image d5_mstory_mincer_fastup:
        "d5_mstory_mincer_1"
        .75
        "d5_mstory_mincer_2"
        .75
        "d5_mstory_mincer_3"
        .5
        "d5_mstory_mincer_4"
        .5
        "d5_mstory_mincer_5"
        .35
        "d5_mstory_mincer_1"
        .35
        "d5_mstory_mincer_2"
        .15
        "d5_mstory_mincer_3"
        .15
        "d5_mstory_mincer_4"
        .15
        "d5_mstory_mincer_5"
        .15

        "d5_mstory_mincer"

    image d5_mstory_mincer_pull 1 = "locate/katya/mincer/Katya_tashim001.png"
    image d5_mstory_mincer_pull 2 = "locate/katya/mincer/Katya_tashim002.png"

    image d5_mstory_incar_sadroma = "sprite/Romka/Rom_sad.png"

    image d5_mstory_teacher_bg = "locate/school/in_side/teacher/teacer_fon.jpg"
    image d5_mstory_teacher 1 = "locate/school/in_side/teacher/teacer1.png"
    image d5_mstory_teacher 2 = "locate/school/in_side/teacher/teacer2.png"

    image d5_mstory_kaite_bg_base = "locate/school/in_side/Kaite/p04.png"
    image d5_mstory_kaite_bg_teach = "locate/school/in_side/Kaite/t.png"
    image d5_mstory_kaite_bg_kate = "locate/school/in_side/Kaite/Kait.png"
    image d5_mstory_kaite_bg_pol_1 = "locate/school/in_side/Kaite/P_001.png"
    image d5_mstory_kaite_bg_pol_2 = "locate/school/in_side/Kaite/P_002.png"
    image d5_mstory_kaite_bg_pol_3 = "locate/school/in_side/Kaite/P_003.png"
    image d5_mstory_kaite_bg_pol:
        "d5_mstory_kaite_bg_pol_1"
        6.
        "d5_mstory_kaite_bg_pol_2"
        .1
        "d5_mstory_kaite_bg_pol_3"
        .1
        "d5_mstory_kaite_bg_pol_2"
        .1
        repeat

    image d5_mstory_kaite_anton 1 = "locate/school/in_side/Anton_class/Anton.png"
    image d5_mstory_kaite_anton 2 = "locate/school/in_side/Anton_class/Anton2.png"

    image d5_mstory_kaite_puddle 1 = "locate/school/in_side/Tupichok/puddle1.png"
    image d5_mstory_kaite_puddle 2 = "locate/school/in_side/Tupichok/puddle2.png"

    image d5_mstory_kaite_tall_body = "locate/school/in_side/Kait/katya.png"
    image d5_mstory_kaite_tall_arm = "locate/school/in_side/Kait/arm.png"
    image d5_mstory_kaite_tall_k1 = "locate/school/in_side/Kait/k01.png"
    image d5_mstory_kaite_tall_k2 = "locate/school/in_side/Kait/k02.png"

    image d5_mstory_kaite_byasha_bg = "locate/Katya/mincer/fon.png"
    image d5_mstory_kaite_byasha_anton = "locate/Katya/mincer/anton.png"
    image d5_mstory_kaite_byasha_rom_base = "locate/Katya/mincer/rom.png"
    image d5_mstory_kaite_byasha_rom_overlay = "locate/Katya/mincer/rom2.png"
    image d5_mstory_kaite_byasha_rom:
        contains:
            "d5_mstory_kaite_byasha_rom_base"
        contains:
            "d5_mstory_kaite_byasha_rom_overlay"
            alpha 0

            block:
                choice:
                    .5
                choice:
                    1.
                alpha 1
                choice:
                    .5
                choice:
                    1.
                alpha 0
                repeat

    image d5_mstory_kaite_tihonov 1 = "locate/street/garage/trailer/T1.png"
    image d5_mstory_kaite_tihonov 2 = "locate/street/garage/trailer/T2.png"
    image d5_mstory_kaite_tihonov_overlay = "locate/street/garage/trailer/T0.png"
    image d5_mstory_kaite_tihonov 3 = Composite((1920, 1483),
        (0, 0), "d5_mstory_kaite_tihonov 1",
        (0, 0), "d5_mstory_kaite_tihonov_overlay")

    image d5_mstory_kaite_tihonov 4 = Composite((1920, 1483),
        (0, 0), "d5_mstory_kaite_tihonov 2",
        (0, 0), "d5_mstory_kaite_tihonov_overlay")

    image d5_mstory_trailer_base = "locate/street/garage/trailer/gar.png"
    image d5_mstory_trailer_light_1 = "locate/street/garage/trailer/L1.png"
    image d5_mstory_trailer_light_2 = "locate/street/garage/trailer/L2.png"
    image d5_mstory_trailer_light_3 = "locate/street/garage/trailer/L3.png"
    image d5_mstory_trailer_light_4 = "locate/street/garage/trailer/L4.png"
    image d5_mstory_trailer_light:
        "d5_mstory_trailer_light_1"
        .1
        "d5_mstory_trailer_light_2"
        .1
        "d5_mstory_trailer_light_3"
        .1
        "d5_mstory_trailer_light_4"
        .1
        repeat

    image d5_mstory_firstaid_bg = "locate/Katya/perevyazka/fon_k.png"
    image d5_mstory_firstaid_kate 1 = "locate/Katya/perevyazka/MK01.png"
    image d5_mstory_firstaid_kate 2 = "locate/Katya/perevyazka/MK02.png"
    image d5_mstory_firstaid_knot = "locate/Katya/perevyazka/knot.png"
    image d5_mstory_firstaid_anton_base = "locate/Katya/perevyazka/Annonio.png"
    image d5_mstory_firstaid_anton_eyes 1 = "locate/Katya/perevyazka/Annonio1.png"
    image d5_mstory_firstaid_anton_eyes 2 = "locate/Katya/perevyazka/Annonio2.png"
    image d5_mstory_firstaid_anton_eyes 3 = "locate/Katya/perevyazka/Annonio3.png"
    image d5_mstory_firstaid_anton_blink:
        "d5_mstory_firstaid_anton_eyes 1"
        choice:
            6.15
        choice:
            7.25
        choice:
            8.35
        "d5_mstory_firstaid_anton_eyes 2"
        .1
        "d5_mstory_firstaid_anton_eyes 3"
        .1
        "d5_mstory_firstaid_anton_eyes 2"
        .1
        repeat

    image d5_mstory_firstaid_hands = "locate/Katya/perevyazka/hands1.png"
    image d5_mstory_firstaid_anton 1:
        contains:
            "d5_mstory_firstaid_anton_base"
        contains:
            "d5_mstory_firstaid_anton_blink"
    image d5_mstory_firstaid_anton 2:
        contains:
            "d5_mstory_firstaid_anton 1"
        contains:
            "d5_mstory_firstaid_hands"

    image d5_mstory_trailer_tikhonov_base = "sprite/Tihonov/ment.png"
    image d5_mstory_trailer_tikhonov = Composite((1920, 2028),
        (0, 0), "d5_mstory_trailer_tikhonov_base",
        (0, 0), AlphaMask(Solid("#0002"), "sprite/Tihonov/ment.png")
        )
    image d5_mstory_trailer_tikhonov2 = Composite((1920, 2028),
        (0, 0), "d5_mstory_trailer_tikhonov_base",
        (0, 0), AlphaMask(Solid("#0003"), "sprite/Tihonov/ment.png")
        )

    image d5_mstory_bobik_base = "locate/Katya/perevyazka/Kait_Ant/bg.png"
    image d5_mstory_bobik_eyes1 = "locate/Katya/perevyazka/Kait_Ant/1.png"
    image d5_mstory_bobik_eyes2 = "locate/Katya/perevyazka/Kait_Ant/2.png"
    image d5_mstory_bobik_eyes3 = "locate/Katya/perevyazka/Kait_Ant/3.png"
    image d5_mstory_bobik_eyes blink:
        "d5_mstory_bobik_eyes1"

        choice:
            4.15
        choice:
            5.85
        choice:
            8.05

        "d5_mstory_bobik_eyes2"
        .1
        "d5_mstory_bobik_eyes3"
        .1
        "d5_mstory_bobik_eyes2"
        .1
        repeat

    image d5_mstory_bobik_eyes opening:
        "d5_mstory_bobik_eyes3"
        .1
        "d5_mstory_bobik_eyes2"
        .1
        "d5_mstory_bobik_eyes1"
        .1
        "d5_mstory_bobik_eyes blink"

    image d5_mstory_bobik_eyes closing:
        "d5_mstory_bobik_eyes1"
        .1
        "d5_mstory_bobik_eyes2"
        .1
        "d5_mstory_bobik_eyes3"

    image d5_mstory_bobik_hand_head = "locate/Katya/perevyazka/Kait_Ant/h1.png"
    image d5_mstory_bobik_hands 2 = "locate/Katya/perevyazka/Kait_Ant/h2.png"
    image d5_mstory_bobik_hands 3 = "locate/Katya/perevyazka/Kait_Ant/h3.png"

    image d5_mstory_bobik_mouth = "locate/Katya/perevyazka/Kait_Ant/m.png"

    image d5_classroom_ghost:
        animation
        "locate/school/in_side/classroom/Ol1.png" with Dissolve(.1)

        choice:
            renpy.random.random()*2 + 4
        choice:
            renpy.random.random()*2 + 5

        "locate/school/in_side/classroom/Ol2.png" with Dissolve(.1)
        .1
        "locate/school/in_side/classroom/Ol3.png" with Dissolve(.1)
        .1
        repeat

    image d5_classroom p0 t0 = "locate/school/in_side/classroom/classroom005.png"

    image d5_classroom p1 t0 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        )
    image d5_classroom p1 t1 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        )
    image d5_classroom p2 t1 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        )
    image d5_classroom p1 t1 m1 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        )
    image d5_classroom p2 t1 m1 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        )
    image d5_classroom p1 t1 m2 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        )
    image d5_classroom p2 t1 m2 = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        )

    image d5_classroom p1 t1 gh = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "d5_classroom_ghost",
        )
    image d5_classroom p2 t1 gh = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "d5_classroom_ghost",
        )

    image d5_mstory_kaite_anton_mouth = "locate/school/in_side/Anton_class/M_02.png"
    image d5_mstory_chair = "locate/school/in_side/classroom/chair .png"
    image d5_mstory_desk = "locate/school/in_side/classroom/desk1.png"
    image d5_mstory_anton_back = "locate/school/in_side/classroom/Anton_back.png"
    image d5_mstory_anton_back dark = LiveComposite((583, 1154),
        (0, 0), "d5_mstory_anton_back",
        (0, 0), AlphaMask("#000a", "d5_mstory_anton_back"))

    image d5_olya_winter_back dark = LiveComposite((1920, 1080),
        (0, 0), "d4_procession_olya",
        (0, 0), AlphaMask("#0003", "d4_procession_olya"))

    image d5_mstory_tovariscsh = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "teach 03",
        (0,0), "locate/school/in_side/ment/ment_02.png",
        )

    image d5_mstory_under_bg = "locate/school/in_side/Kaite/001.png"
    image d5_mstory_under_overlay = "locate/school/in_side/Kaite/002.png"
    image d5_desk = "locate/school/in_side/Parta.jpg"
    image d5_desk_paper_base = "locate/school/in_side/Kaite/paper.png"
    image d5_desk_paper_1 = "locate/school/in_side/Kaite/paper1.png"
    image d5_desk_paper_2 = "locate/school/in_side/Kaite/paper2.png"
    image d5_desk_paper_3 = "locate/school/in_side/Kaite/paper3.png"
    image d5_desk_paper 1:
        contains:
            "d5_desk_paper_base"
        contains:
            "d5_desk_paper_1"
    image d5_desk_paper 2:
        contains:
            "d5_desk_paper_base"
        contains:
            "d5_desk_paper_1"
        contains:
            "d5_desk_paper_2"
    image d5_desk_paper 3:
        contains:
            "d5_desk_paper_base"
        contains:
            "d5_desk_paper_1"
        contains:
            "d5_desk_paper_2"
        contains:
            "d5_desk_paper_3"

    image d5_mstory_kaite_head = "locate/school/in_side/Kaite/head_k.png"

    image d5_mstory_notice 1 = "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg"
    image d5_mstory_notice 2 = Composite((2844, 1600),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg",
        (0, 0), "locate/school/in_side/raspisanie_but2.png")

    image Kate_k Normal_m_day_winter_00_evil_ahead_01 = im.Composite((1920, 1080),
        (0, 0), "sprite/Kate_k/Normal/m_day_winter/1_body/00.png",
        (0, 0), "sprite/Kate_k/Normal/m_day_winter/2_eyes/evil/ahead/01.png",
        (0, 0), "sprite/Kate_k/Normal/m_day_winter/3_mouth/01.png"
        )



    image d5_katya_walk_bg_01 = "locate/street/walking_fox_day/road_fox01.jpg"
    image d5_katya_walk_bg_02 = "locate/street/walking_fox_day/road_fox02.png"
    image d5_katya_walk_bg_03 = "locate/street/walking_fox_day/road_fox03.png"

    image d5_katya_walk_base = "sprite/Kate_k/3_4/basa2.png"
    image d5_katya_walk_eyes = "sprite/Kate_k/3_4/1.png"
    image d5_katya_walk_smile = "sprite/Kate_k/3_4/2.png"
    image d5_katya_walk_sad = "sprite/Kate_k/3_4/3.png"
    image d5_katya_walk_unsmile = "sprite/Kate_k/3_4/4.png"












    image d5_katya_walk aside notsad norm = Composite((547, 882),
        (0, 0), "d5_katya_walk_base")

    image d5_katya_walk aside notsad smile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_smile")

    image d5_katya_walk aside notsad unsmile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_unsmile")

    image d5_katya_walk ahead notsad norm = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes")

    image d5_katya_walk ahead notsad smile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes",
        (0, 0), "d5_katya_walk_smile")

    image d5_katya_walk ahead notsad unsmile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes",
        (0, 0), "d5_katya_walk_unsmile")


    image d5_katya_walk aside sad norm = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_sad")

    image d5_katya_walk aside sad smile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_sad",
        (0, 0), "d5_katya_walk_smile")

    image d5_katya_walk aside sad unsmile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_sad",
        (0, 0), "d5_katya_walk_unsmile")

    image d5_katya_walk ahead sad norm = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes",
        (0, 0), "d5_katya_walk_sad")

    image d5_katya_walk ahead sad smile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes",
        (0, 0), "d5_katya_walk_sad",
        (0, 0), "d5_katya_walk_smile")

    image d5_katya_walk ahead sad unsmile = Composite((547, 882),
        (0, 0), "d5_katya_walk_base",
        (0, 0), "d5_katya_walk_eyes",
        (0, 0), "d5_katya_walk_sad",
        (0, 0), "d5_katya_walk_unsmile")

    image d5_anton_walk norm = "locate/street/walking_fox_day/Ant_right.png"
    image d5_anton_walk_sad:
        "locate/street/walking_fox_day/Ant_left2.png"
        xzoom -1
    image d5_anton_walk sad = Composite((707, 1080),
        (0, 0), "d5_anton_walk norm",
        (0, 0), "d5_anton_walk_sad")

    image d5_katya_fantasy_director = "locate/school/in_side/teacher/Direktor.png"
    image d5_katya_fantasy_teacher = "locate/school/in_side/teacheR_2.png"

    image d5_katya_cityscape_buildings = "locate/Katya/houses.png"
    image d5_katya_cityscape_sky = "locate/Katya/sky.png"
    image d5_katya_cityscape_crow1:
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        repeat
    image d5_katya_cityscape_crow2:
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        repeat
    image d5_katya_cityscape_crow3:
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        repeat
    image d5_katya_cityscape_crow4:
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        repeat
    image d5_katya_cityscape_crow5:
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        repeat
    image d5_katya_cityscape_crow6:
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        repeat
    image d5_katya_cityscape_crow7:
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        repeat
    image d5_katya_cityscape_crow8:
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        "locate/home/out_side/voron/Voron002.png"
        .2
        repeat
    image d5_katya_cityscape_crow9:
        "locate/home/out_side/voron/Voron002.png"
        .2
        "locate/home/out_side/voron/Voron003.png"
        .2
        "locate/home/out_side/voron/Voron004.png"
        .2
        "locate/home/out_side/voron/Voron005.png"
        .2
        "locate/home/out_side/voron/Voron006.png"
        .2
        "locate/home/out_side/voron/Voron007.png"
        .2
        "locate/home/out_side/voron/Voron008.png"
        .2
        "locate/home/out_side/voron/Voron009.png"
        .2
        "locate/home/out_side/voron/Voron001.png"
        .2
        repeat

    transform citycrow(cc_zoom, cc_align, cc_period, cc_aplitude):
        subpixel True
        choice:
            "d5_katya_cityscape_crow1"
        choice:
            "d5_katya_cityscape_crow2"
        choice:
            "d5_katya_cityscape_crow3"
        choice:
            "d5_katya_cityscape_crow4"
        choice:
            "d5_katya_cityscape_crow5"
        choice:
            "d5_katya_cityscape_crow6"
        choice:
            "d5_katya_cityscape_crow7"
        choice:
            "d5_katya_cityscape_crow8"
        choice:
            "d5_katya_cityscape_crow9"
        zoom cc_zoom
        yalign cc_align[1]
        parallel:
            choice:
                ease 20 yoffset cc_aplitude
                ease 20 yoffset -cc_aplitude
                ease 20 yoffset 0
            choice:
                ease 20 yoffset -cc_aplitude
                ease 20 yoffset cc_aplitude
                ease 20 yoffset 0
            choice:
                ease 30 yoffset -cc_aplitude
                ease 30 yoffset 0
            choice:
                ease 30 yoffset cc_aplitude
                ease 30 yoffset 0
            repeat
        parallel:
            xalign cc_align[0]
            linear cc_period*(1. - cc_align[0]) xpos 1. xanchor 0.
            block:
                xpos 0.0
                xanchor 1.
                linear cc_period xpos 1. xanchor 0.
                repeat

    image d5_katya_cityscape_crows:
        contains:
            contains citycrow(0.050, (.20, .05), 41, 10)

        contains:
            contains citycrow(0.055, (.24, .25), 42, 14)

        contains:
            contains citycrow(0.060, (.25, .20), 43, 18)

        contains:
            contains citycrow(0.062, (.27, .21), 44, 22)

        contains:
            contains citycrow(0.064, (.34, .15), 45, 24)

        contains:
            contains citycrow(0.068, (.61, .18), 46, 26)

        contains:
            contains citycrow(0.070, (.85, .30), 47, 30)

    image d5_katya_ladder_bg = "locate/Katya/ladder/bg.png"
    image d5_katya_ladder_mask = "locate/Katya/ladder/mask.png"
    image d5_katya_ladder_base = "locate/Katya/ladder/basa.png"
    image d5_katya_ladder_snow_base = LiveComposite((1920, 1080),
        (0, 0), "d5s_battle_bg_bright100",
        (0, 0), "d5s_battle_mid_bright100",)
    image d5_katya_ladder_snow = AlphaMask("d5_katya_ladder_snow_base", "d5_katya_ladder_mask")

    image d5_katya_ladder_ant_eye_1 = "locate/Katya/ladder/anton/eye/001.png"
    image d5_katya_ladder_ant_eye_2 = "locate/Katya/ladder/anton/eye/002.png"
    image d5_katya_ladder_ant_eye_3 = "locate/Katya/ladder/anton/eye/003.png"
    image d5_katya_ladder_ant_blink:
        animation
        Null()
        6.0
        "d5_katya_ladder_ant_eye_1"
        .1
        "d5_katya_ladder_ant_eye_2"
        .1
        "d5_katya_ladder_ant_eye_3"
        .1
        "d5_katya_ladder_ant_eye_2"
        .1
        "d5_katya_ladder_ant_eye_1"
        .1
        repeat

    image d5_katya_ladder_ant_norm = "locate/Katya/ladder/anton/m1.png"
    image d5_katya_ladder_ant_talk = "locate/Katya/ladder/anton/m2.png"
    image d5_katya_ladder_ant_sweat = "locate/Katya/ladder/anton/pot.png"
    image d5_katya_ladder_ant_red = "locate/Katya/ladder/anton/red.png"

    image Anton norm:
        contains:
            "d5_katya_ladder_ant_norm"
        contains:
            "d5_katya_ladder_ant_blink"

    image Anton talk:
        contains:
            "d5_katya_ladder_ant_talk"
        contains:
            "d5_katya_ladder_ant_blink"

    image Anton norm sweat:
        contains:
            "Anton norm"
        contains:
            "d5_katya_ladder_ant_sweat"
    image Anton talk sweat:
        contains:
            "Anton talk"
        contains:
            "d5_katya_ladder_ant_sweat"
    image Anton norm red:
        contains:
            "Anton norm"
        contains:
            "d5_katya_ladder_ant_red"
    image Anton talk red:
        contains:
            "Anton talk"
        contains:
            "d5_katya_ladder_ant_red"
    image Anton norm red sweat:
        contains:
            "Anton norm"
        contains:
            "d5_katya_ladder_ant_red"
        contains:
            "d5_katya_ladder_ant_sweat"
    image Anton talk red sweat:
        contains:
            "Anton talk"
        contains:
            "d5_katya_ladder_ant_red"
        contains:
            "d5_katya_ladder_ant_sweat"

    image d5_katya_ladder_kat_eye_norm_1_1 = "locate/Katya/ladder/Kite/eye/normal/1/001.png"
    image d5_katya_ladder_kat_eye_norm_1_2 = "locate/Katya/ladder/Kite/eye/normal/1/002.png"
    image d5_katya_ladder_kat_eye_norm_1_3 = "locate/Katya/ladder/Kite/eye/normal/1/003.png"
    image d5_katya_ladder_kat_eye_norm_1_blink:
        animation
        "d5_katya_ladder_kat_eye_norm_1_1"
        6.0
        "d5_katya_ladder_kat_eye_norm_1_2"
        .1
        "d5_katya_ladder_kat_eye_norm_1_3"
        .1
        "d5_katya_ladder_kat_eye_norm_1_2"
        .1
        repeat

    image d5_katya_ladder_kat_eye_norm_2_1 = "locate/Katya/ladder/Kite/eye/normal/2/001.png"
    image d5_katya_ladder_kat_eye_norm_2_2 = "locate/Katya/ladder/Kite/eye/normal/2/002.png"
    image d5_katya_ladder_kat_eye_norm_2_3 = "locate/Katya/ladder/Kite/eye/normal/2/003.png"
    image d5_katya_ladder_kat_eye_norm_2_blink:
        animation
        "d5_katya_ladder_kat_eye_norm_2_1"
        6.0
        "d5_katya_ladder_kat_eye_norm_2_2"
        .1
        "d5_katya_ladder_kat_eye_norm_2_3"
        .1
        "d5_katya_ladder_kat_eye_norm_2_2"
        .1
        repeat

    image d5_katya_ladder_kat_eye_norm_3_1 = "locate/Katya/ladder/Kite/eye/normal/3/001.png"
    image d5_katya_ladder_kat_eye_norm_3_2 = "locate/Katya/ladder/Kite/eye/normal/3/002.png"
    image d5_katya_ladder_kat_eye_norm_3_3 = "locate/Katya/ladder/Kite/eye/normal/3/003.png"
    image d5_katya_ladder_kat_eye_norm_3_blink:
        animation
        "d5_katya_ladder_kat_eye_norm_3_1"
        6.0
        "d5_katya_ladder_kat_eye_norm_3_2"
        .1
        "d5_katya_ladder_kat_eye_norm_3_3"
        .1
        "d5_katya_ladder_kat_eye_norm_3_2"
        .1
        repeat

    image d5_katya_ladder_kat_eye_red_1_1 = "locate/Katya/ladder/Kite/eye/red/1/001.png"
    image d5_katya_ladder_kat_eye_red_1_2 = "locate/Katya/ladder/Kite/eye/red/1/002.png"
    image d5_katya_ladder_kat_eye_red_1_3 = "locate/Katya/ladder/Kite/eye/red/1/003.png"
    image d5_katya_ladder_kat_eye_red_1_blink:
        animation
        "d5_katya_ladder_kat_eye_red_1_1"
        6.0
        "d5_katya_ladder_kat_eye_red_1_2"
        .1
        "d5_katya_ladder_kat_eye_red_1_3"
        .1
        "d5_katya_ladder_kat_eye_red_1_2"
        .1
        repeat

    image d5_katya_ladder_kat_eye_red_2_1 = "locate/Katya/ladder/Kite/eye/red/2/001.png"
    image d5_katya_ladder_kat_eye_red_2_2 = "locate/Katya/ladder/Kite/eye/red/2/002.png"
    image d5_katya_ladder_kat_eye_red_2_3 = "locate/Katya/ladder/Kite/eye/red/2/003.png"
    image d5_katya_ladder_kat_eye_red_2_blink:
        animation
        "d5_katya_ladder_kat_eye_red_2_1"
        6.0
        "d5_katya_ladder_kat_eye_red_2_2"
        .1
        "d5_katya_ladder_kat_eye_red_2_3"
        .1
        "d5_katya_ladder_kat_eye_red_2_2"
        .1
        repeat

    image d5_katya_ladder_kat_eye_red_3_1 = "locate/Katya/ladder/Kite/eye/red/3/001.png"
    image d5_katya_ladder_kat_eye_red_3_2 = "locate/Katya/ladder/Kite/eye/red/3/002.png"
    image d5_katya_ladder_kat_eye_red_3_3 = "locate/Katya/ladder/Kite/eye/red/3/003.png"
    image d5_katya_ladder_kat_eye_red_3_blink:
        animation
        "d5_katya_ladder_kat_eye_red_3_1"
        6.0
        "d5_katya_ladder_kat_eye_red_3_2"
        .1
        "d5_katya_ladder_kat_eye_red_3_3"
        .1
        "d5_katya_ladder_kat_eye_red_3_2"
        .1
        repeat

    image d5_katya_ladder_kat_mouth_01 = "locate/Katya/ladder/Kite/mouth/001.png"
    image d5_katya_ladder_kat_mouth_02 = "locate/Katya/ladder/Kite/mouth/002.png"
    image d5_katya_ladder_kat_mouth_03 = "locate/Katya/ladder/Kite/mouth/003.png"
    image d5_katya_ladder_kat_mouth_04 = "locate/Katya/ladder/Kite/mouth/004.png"
    image d5_katya_ladder_kat_mouth_05 = "locate/Katya/ladder/Kite/mouth/005.png"
    image d5_katya_ladder_kat_mouth_06 = "locate/Katya/ladder/Kite/mouth/006.png"
    image d5_katya_ladder_kat_mouth_07 = "locate/Katya/ladder/Kite/mouth/007.png"
    image d5_katya_ladder_kat_mouth_08 = "locate/Katya/ladder/Kite/mouth/008.png"
    image d5_katya_ladder_kat_mouth_09 = "locate/Katya/ladder/Kite/mouth/009.png"
    image d5_katya_ladder_kat_mouth_10 = "locate/Katya/ladder/Kite/mouth/010.png"
    image d5_katya_ladder_kat_mouth_11 = "locate/Katya/ladder/Kite/mouth/011.png"
    image d5_katya_ladder_kat_mouth_12 = "locate/Katya/ladder/Kite/mouth/012.png"

    image Kate norm ahead 01:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"
    image Kate norm aside 01:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"
    image Kate norm adown 01:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"

    image Kate norm ahead 02:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"
    image Kate norm aside 02:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"
    image Kate norm adown 02:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"

    image Kate norm ahead 03:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"
    image Kate norm aside 03:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"
    image Kate norm adown 03:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"

    image Kate norm ahead 04:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"
    image Kate norm aside 04:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"
    image Kate norm adown 04:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"

    image Kate norm ahead 05:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"
    image Kate norm aside 05:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"
    image Kate norm adown 05:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"

    image Kate norm ahead 06:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"
    image Kate norm aside 06:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"
    image Kate norm adown 06:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"

    image Kate norm ahead 07:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"
    image Kate norm aside 07:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"
    image Kate norm adown 07:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"

    image Kate norm ahead 08:
        contains:
            "d5_katya_ladder_kat_eye_norm_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"
    image Kate norm aside 08:
        contains:
            "d5_katya_ladder_kat_eye_norm_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"
    image Kate norm adown 08:
        contains:
            "d5_katya_ladder_kat_eye_norm_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"


    image Kate red ahead 01:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"
    image Kate red aside 01:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"
    image Kate red adown 01:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_01"

    image Kate red ahead 02:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"
    image Kate red aside 02:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"
    image Kate red adown 02:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_02"

    image Kate red ahead 03:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"
    image Kate red aside 03:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"
    image Kate red adown 03:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_03"

    image Kate red ahead 04:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"
    image Kate red aside 04:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"
    image Kate red adown 04:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_04"

    image Kate red ahead 05:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"
    image Kate red aside 05:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"
    image Kate red adown 05:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_05"

    image Kate red ahead 06:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"
    image Kate red aside 06:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"
    image Kate red adown 06:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_06"

    image Kate red ahead 07:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"
    image Kate red aside 07:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"
    image Kate red adown 07:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_07"

    image Kate red ahead 08:
        contains:
            "d5_katya_ladder_kat_eye_red_1_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"
    image Kate red aside 08:
        contains:
            "d5_katya_ladder_kat_eye_red_2_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"
    image Kate red adown 08:
        contains:
            "d5_katya_ladder_kat_eye_red_3_blink"
        contains:
            "d5_katya_ladder_kat_mouth_08"


    image d5_katya_dvor_1 = "locate/Katya/ladder/dvor/dvor1.png"
    image d5_katya_dvor_2 = "locate/Katya/ladder/dvor/dvor2.png"
    image d5_katya_dvor_3 = "locate/Katya/ladder/dvor/dvor3.png"
    image d5_katya_dvor_4 = "locate/Katya/ladder/dvor/dvor4.png"

    image d5_katya_janitor norm:
        contains:
            "d5_katya_dvor_1"
        contains:
            Null()
            4.0
            "d5_katya_dvor_2"
            .1
            "d5_katya_dvor_3"
            .1
            "d5_katya_dvor_2"
            .1
            repeat
    image d5_katya_janitor talk:
        contains:
            "d5_katya_janitor norm"
        contains:
            "d5_katya_dvor_4"

    image d5_katya_door_frame = "locate/Katya/door/00.png"
    image d5_katya_door_door 1 = "locate/Katya/door/01.png"
    image d5_katya_door_door 5 = "locate/Katya/door/05.png"
    image d5_katya_door_inner = "locate/Katya/door/bg.png"

    image d5_katya_room_bg = "locate/Katya/room/base.png"
    image d5_katya_room_crutch = "locate/Katya/room/k.png"
    image d5_katya_room_photo = "locate/Katya/room/foto.png"
    image d5_katya_room2_bg = "locate/Katya/room2/basa.png"
    image d5_katya_room2_aq = "locate/Katya/room2/aq.png"
    image d5_katya_room2_fg1 = "locate/Katya/room2/top.png"
    image d5_katya_room2_fg2 = "locate/Katya/room2/top2.png"
    image d5_katya_room2_fish_01 = "locate/Katya/room2/01.png"
    image d5_katya_room2_fish_02 = "locate/Katya/room2/02.png"
    image d5_katya_room2_fish_03 = "locate/Katya/room2/03.png"
    image d5_katya_room2_fish_04 = "locate/Katya/room2/04.png"
    image d5_katya_room2_fish_05 = "locate/Katya/room2/05.png"
    image d5_katya_room2_fish_06 = "locate/Katya/room2/06.png"
    image d5_katya_room2_fish_07 = "locate/Katya/room2/07.png"
    image d5_katya_room2_fish_08 = "locate/Katya/room2/08.png"
    image d5_katya_room2_fish_09 = "locate/Katya/room2/09.png"
    image d5_katya_room2_fish_10 = "locate/Katya/room2/10.png"
    image d5_katya_room2_fish_11 = "locate/Katya/room2/11.png"
    image d5_katya_room2_fish_12 = "locate/Katya/room2/12.png"

    image d5_katya_aqua_food = "locate/Katya/room2/korm.png"
    transform aqkorm(xbase, xoff=0, xdrift=0, ydepth=800, zm=1.0):
        subpixel True
        anchor (.5, .5)
        zoom zm
        matrixcolor BrightnessMatrix(zm - 1.0)
        ypos -12
        xpos xbase + xoff
        block:
            parallel:
                easein 30 ypos ydepth
            parallel:
                ease 10 xpos xbase -50 + xdrift
                ease 10 xpos xbase +50 + xdrift
                repeat


    image ant_clas_blink_aside:
        "locate/school/in_side/Anton_class/blink_01.png"
        choice:
            3.
        choice:
            4.
        choice:
            5.
        "locate/school/in_side/Anton_class/blink_02.png"
        .1
        "locate/school/in_side/Anton_class/blink_3.png"
        .1
        "locate/school/in_side/Anton_class/blink_02.png"
        .1
        repeat

    image d5_katya_room_base = "locate/katya/room/base.png"
    image d5_katya_room_kostil = "locate/katya/room/k.png"
    image d5_katya_room_blik = "locate/katya/room/blik.png"
    image d5_katya_room_s = "locate/katya/room/s.png"

    image d5_katya_roombig_bg = "locate/katya/room/bg_big.png"
    image d5_katya_roombig_fg = "locate/katya/room/room_big.png"
    image d5_katya_roombig_relfect = "locate/katya/room/kaite.png"

    image d5_katya_kitchen_bg = "locate/katya/kitchen/001.png"
    image d5_katya_kitchen_over = "locate/katya/kitchen/002.png"
    image d5_katya_kitchen_over_over = "locate/katya/kitchen/003.png"

    image d5_katya_kitchen_shelf = "locate/katya/kitchen/box.png"
    image d5_katya_kitchen_mincer_lay = "locate/katya/kitchen/mincer.png"
    image d5_katya_kitchen_mincer_hand = "locate/katya/kitchen/mincer2.png"

    image d5_katya_stove_bg = "minigame/stove/bg0.png"
    image d5_katya_stove_pan = "minigame/stove/pan.png"
    image d5_katya_stove on = "minigame/stove/on.png"
    image d5_katya_stove off = "minigame/stove/off.png"

    image d5_katya_stove_oil_base = "minigame/stove/oil.png"
    image d5_katya_stove_oil_1 = "minigame/stove/oil01.png"
    image d5_katya_stove_oil_2 = "minigame/stove/oil02.png"
    image d5_katya_stove_oil_3 = "minigame/stove/oil03.png"
    image d5_katya_stove_oil:
        contains:
            "d5_katya_stove_oil_base"
        contains:
            "d5_katya_stove_oil_1"
            .1
            "d5_katya_stove_oil_2"
            .1
            "d5_katya_stove_oil_3"
            .1
            repeat

    image d5_katya_stove_cutlet 1 = "minigame/stove/k_1.png"
    image d5_katya_stove_cutlet 2 = "minigame/stove/k_2.png"
    image d5_katya_stove_cutlet 3 = "minigame/stove/k_3.png"
    image d5_katya_stove_cutlet 4 = "minigame/stove/k_4.png"

    image d5_katya_stove_potato 1 = "minigame/stove/potato1.png"
    image d5_katya_stove_potato 2 = "minigame/stove/potato2.png"
    image d5_katya_stove_potato 3 = "minigame/stove/potato3.png"
    image d5_katya_stove_potato 4 = "minigame/stove/potato4.png"

    image d5_stove_pan still:
        contains:
            "d5_katya_stove_pan"
        contains:
            "d5_katya_stove_oil_base"

    image d5_stove_pan base:
        contains:
            "d5_katya_stove_pan"
        contains:
            "d5_katya_stove_oil"

    image d5_stove_pan cutlet1:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_cutlet 1"

    image d5_stove_pan cutlet2:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_cutlet 2"

    image d5_stove_pan cutlet3:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_cutlet 3"

    image d5_stove_pan cutlet4:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_cutlet 4"

    image d5_stove_pan potato1:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_potato 1"

    image d5_stove_pan potato2:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_potato 2"

    image d5_stove_pan potato3:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_potato 3"

    image d5_stove_pan potato4:
        contains:
            "d5_stove_pan base"
        contains:
            "d5_katya_stove_potato 4"

    image d5_katya_kitchen_bg_base = "locate/katya/ant_k/fon.png"
    image d5_katya_kitchen_bg_fork = "locate/katya/ant_k/fork.png"
    image d5_katya_kitchen_bg_paddle = "locate/katya/ant_k/paddle.png"
    image d5_katya_kitchen_bg_plug = "locate/katya/ant_k/plug.png"
    image d5_katya_kitchen_bg_smoke1_base = "locate/katya/ant_k/smoke1.png"
    image d5_katya_kitchen_bg_smoke2_base = "locate/katya/ant_k/smoke2.png"
    image d5_katya_kitchen_bg_smoke1:
        animation
        "d5_katya_kitchen_bg_smoke1_base"
        function WaveShader(amp=1, period=15, speed=.04, direction="horisontal")
    image d5_katya_kitchen_bg_smoke2:
        animation
        "d5_katya_kitchen_bg_smoke2_base"
        function WaveShader(amp=1.25, period=4, speed=.12, direction="horisontal")

    layeredimage d5_katya_kitchen2_bg:
        always:
            "d5_katya_kitchen_bg_base"
        attribute fork:
            "d5_katya_kitchen_bg_fork"
        attribute paddle:
            "d5_katya_kitchen_bg_paddle"
        attribute plug:
            "d5_katya_kitchen_bg_plug"
        always:
            "d5_katya_kitchen_bg_smoke1"
        always:
            "d5_katya_kitchen_bg_smoke2"

    image d5_katya_kitchen_pair 1 = "locate/katya/ant_k/new/01.png"
    image d5_katya_kitchen_pair 2 = "locate/katya/ant_k/new/02.png"
    image d5_katya_kitchen_pair2 1 = "locate/katya/ant_k/new2/01.png"
    image d5_katya_kitchen_pair2 2 = "locate/katya/ant_k/new2/02.png"
    image d5_katya_kitchen_pair2 3 = "locate/katya/ant_k/new2/03.png"

    image d5_katya_kitchen_ant_m bad = "locate/katya/ant_k/new/Ant/bad.png"
    image d5_katya_kitchen_ant_m good = "locate/katya/ant_k/new/Ant/good.png"
    image d5_katya_kitchen_ant_m m = "locate/katya/ant_k/new/Ant/m.png"
    image d5_katya_kitchen_ant_m shoked = "locate/katya/ant_k/new/Ant/shoked.png"

    image d5_katya_kitchen_ant_m 1 = "locate/katya/ant_k/new2/Ant/01.png"
    image d5_katya_kitchen_ant_m 2 = "locate/katya/ant_k/new2/Ant/02.png"
    image d5_katya_kitchen_ant_m 3 = "locate/katya/ant_k/new2/Ant/03.png"
    image d5_katya_kitchen_ant_m 4 = "locate/katya/ant_k/new2/Ant/04.png"

    transform transform_blink(img1, img2, img3, delay=0.0):
        img1
        choice:
            5. + delay
        choice:
            6. + delay*2
        choice:
            6.25 + delay*3
        img2
        .1
        img3
        .1
        img2
        .1
        repeat

    image d5_katya_kitchen_ant_Bad_1 = "locate/katya/ant_k/new/Ant/Bad/01.png"
    image d5_katya_kitchen_ant_Bad_2 = "locate/katya/ant_k/new/Ant/Bad/02.png"
    image d5_katya_kitchen_ant_Bad_3 = "locate/katya/ant_k/new/Ant/Bad/03.png"
    image d5_katya_kitchen_ant Bad:
        contains transform_blink("d5_katya_kitchen_ant_Bad_1", "d5_katya_kitchen_ant_Bad_2", "d5_katya_kitchen_ant_Bad_3")

    image d5_katya_kitchen_ant_Doun_1 = "locate/katya/ant_k/new/Ant/Doun/01.png"
    image d5_katya_kitchen_ant_Doun_2 = "locate/katya/ant_k/new/Ant/Doun/02.png"
    image d5_katya_kitchen_ant_Doun_3 = "locate/katya/ant_k/new/Ant/Doun/03.png"
    image d5_katya_kitchen_ant Doun:
        contains transform_blink("d5_katya_kitchen_ant_Doun_1", "d5_katya_kitchen_ant_Doun_2", "d5_katya_kitchen_ant_Doun_3")

    image d5_katya_kitchen_ant_Good_1 = "locate/katya/ant_k/new/Ant/Good/01.png"
    image d5_katya_kitchen_ant_Good_2 = "locate/katya/ant_k/new/Ant/Good/02.png"
    image d5_katya_kitchen_ant_Good_3 = "locate/katya/ant_k/new/Ant/Good/03.png"
    image d5_katya_kitchen_ant Good:
        contains transform_blink("d5_katya_kitchen_ant_Good_1", "d5_katya_kitchen_ant_Good_2", "d5_katya_kitchen_ant_Good_3")

    image d5_katya_kitchen_ant_Shoked_1 = "locate/katya/ant_k/new/Ant/Shoked/01.png"
    image d5_katya_kitchen_ant_Shoked_2 = "locate/katya/ant_k/new/Ant/Shoked/02.png"
    image d5_katya_kitchen_ant_Shoked_3 = "locate/katya/ant_k/new/Ant/Shoked/03.png"
    image d5_katya_kitchen_ant Shoked:
        contains transform_blink("d5_katya_kitchen_ant_Shoked_1", "d5_katya_kitchen_ant_Shoked_2", "d5_katya_kitchen_ant_Shoked_3")

    image d5_katya_kitchen_ant2_ahead_1 = "locate/katya/ant_k/new2/Ant/ahead/01.png"
    image d5_katya_kitchen_ant2_ahead_2 = "locate/katya/ant_k/new2/Ant/ahead/02.png"
    image d5_katya_kitchen_ant2_ahead_3 = "locate/katya/ant_k/new2/Ant/ahead/03.png"
    image d5_katya_kitchen_ant2 ahead:
        contains transform_blink("d5_katya_kitchen_ant2_ahead_1", "d5_katya_kitchen_ant2_ahead_2", "d5_katya_kitchen_ant2_ahead_3")

    image d5_katya_kitchen_ant2_aside_1 = "locate/katya/ant_k/new2/Ant/aside/01.png"
    image d5_katya_kitchen_ant2_aside_2 = "locate/katya/ant_k/new2/Ant/aside/02.png"
    image d5_katya_kitchen_ant2_aside_3 = "locate/katya/ant_k/new2/Ant/aside/03.png"
    image d5_katya_kitchen_ant2 aside:
        contains transform_blink("d5_katya_kitchen_ant2_aside_1", "d5_katya_kitchen_ant2_aside_2", "d5_katya_kitchen_ant2_aside_3")

    image d5_katya_kitchen_ant2_silly_1 = "locate/katya/ant_k/new2/Ant/silly/01.png"
    image d5_katya_kitchen_ant2_silly_2 = "locate/katya/ant_k/new2/Ant/silly/02.png"
    image d5_katya_kitchen_ant2_silly_3 = "locate/katya/ant_k/new2/Ant/silly/03.png"
    image d5_katya_kitchen_ant2 silly:
        contains transform_blink("d5_katya_kitchen_ant2_silly_1", "d5_katya_kitchen_ant2_silly_2", "d5_katya_kitchen_ant2_silly_3")

    image d5_katya_kitchen_ant2_doun_1 = "locate/katya/ant_k/new2/Ant/doun/01.png"
    image d5_katya_kitchen_ant2_doun_2 = "locate/katya/ant_k/new2/Ant/doun/02.png"
    image d5_katya_kitchen_ant2_doun_3 = "locate/katya/ant_k/new2/Ant/doun/03.png"
    image d5_katya_kitchen_ant2 doun:
        contains transform_blink("d5_katya_kitchen_ant2_doun_1", "d5_katya_kitchen_ant2_doun_2", "d5_katya_kitchen_ant2_doun_3")

    image d5_katya_kitchen_ant2_shocked_1 = "locate/katya/ant_k/new2/Ant/shocked/01.png"
    image d5_katya_kitchen_ant2_shocked_2 = "locate/katya/ant_k/new2/Ant/shocked/02.png"
    image d5_katya_kitchen_ant2_shocked_3 = "locate/katya/ant_k/new2/Ant/shocked/03.png"
    image d5_katya_kitchen_ant2 shocked:
        contains transform_blink("d5_katya_kitchen_ant2_shocked_1", "d5_katya_kitchen_ant2_shocked_2", "d5_katya_kitchen_ant2_shocked_3")

    image d5_katya_kitchen_kat_Bad_1 = "locate/katya/ant_k/new/Kaite/Bad/e01.png"
    image d5_katya_kitchen_kat_Bad_2 = "locate/katya/ant_k/new/Kaite/Bad/e02.png"
    image d5_katya_kitchen_kat_Bad_3 = "locate/katya/ant_k/new/Kaite/Bad/e03.png"
    image d5_katya_kitchen_kat_Bad_m1 = "locate/katya/ant_k/new/Kaite/Bad/m01.png"
    image d5_katya_kitchen_kat_Bad_m2 = "locate/katya/ant_k/new/Kaite/Bad/m02.png"
    image d5_katya_kitchen_kat_Bad_m3 = "locate/katya/ant_k/new/Kaite/Bad/m03.png"
    image d5_katya_kitchen_kat_Bad:
        contains transform_blink("d5_katya_kitchen_kat_Bad_1", "d5_katya_kitchen_kat_Bad_2", "d5_katya_kitchen_kat_Bad_3", delay=1.15)

    image d5_katya_kitchen_kat_Faint_1 = "locate/katya/ant_k/new/Kaite/Faint/e01.png"
    image d5_katya_kitchen_kat_Faint_2 = "locate/katya/ant_k/new/Kaite/Faint/e02.png"
    image d5_katya_kitchen_kat_Faint_3 = "locate/katya/ant_k/new/Kaite/Faint/e03.png"
    image d5_katya_kitchen_kat_Faint_m1 = "locate/katya/ant_k/new/Kaite/Faint/m01.png"
    image d5_katya_kitchen_kat_Faint_m2 = "locate/katya/ant_k/new/Kaite/Faint/m02.png"
    image d5_katya_kitchen_kat_Faint:
        contains transform_blink("d5_katya_kitchen_kat_Faint_1", "d5_katya_kitchen_kat_Faint_2", "d5_katya_kitchen_kat_Faint_3", delay=1.15)

    image d5_katya_kitchen_kat_Good_1 = "locate/katya/ant_k/new/Kaite/Good/e01.png"
    image d5_katya_kitchen_kat_Good_2 = "locate/katya/ant_k/new/Kaite/Good/e02.png"
    image d5_katya_kitchen_kat_Good_3 = "locate/katya/ant_k/new/Kaite/Good/e03.png"
    image d5_katya_kitchen_kat_Good_m1 = "locate/katya/ant_k/new/Kaite/Good/m01.png"
    image d5_katya_kitchen_kat_Good_m2 = "locate/katya/ant_k/new/Kaite/Good/m02.png"
    image d5_katya_kitchen_kat_Good_m3 = "locate/katya/ant_k/new/Kaite/Good/m03.png"
    image d5_katya_kitchen_kat_Good:
        contains transform_blink("d5_katya_kitchen_kat_Good_1", "d5_katya_kitchen_kat_Good_2", "d5_katya_kitchen_kat_Good_3", delay=1.15)

    image d5_katya_kitchen_kat bad m1:
        contains:
            "d5_katya_kitchen_kat_Bad"
        contains:
            "d5_katya_kitchen_kat_Bad_m1"
    image d5_katya_kitchen_kat bad m2:
        contains:
            "d5_katya_kitchen_kat_Bad"
        contains:
            "d5_katya_kitchen_kat_Bad_m2"
    image d5_katya_kitchen_kat bad m3:
        contains:
            "d5_katya_kitchen_kat_Bad"
        contains:
            "d5_katya_kitchen_kat_Bad_m3"

    image d5_katya_kitchen_kat faint m1:
        contains:
            "d5_katya_kitchen_kat_Faint"
        contains:
            "d5_katya_kitchen_kat_Faint_m1"
    image d5_katya_kitchen_kat faint m2:
        contains:
            "d5_katya_kitchen_kat_Faint"
        contains:
            "d5_katya_kitchen_kat_Faint_m2"

    image d5_katya_kitchen_kat good m1:
        contains:
            "d5_katya_kitchen_kat_Good"
        contains:
            "d5_katya_kitchen_kat_Good_m1"
    image d5_katya_kitchen_kat good m2:
        contains:
            "d5_katya_kitchen_kat_Good"
        contains:
            "d5_katya_kitchen_kat_Good_m2"
    image d5_katya_kitchen_kat good m3:
        contains:
            "d5_katya_kitchen_kat_Good"
        contains:
            "d5_katya_kitchen_kat_Good_m3"

    image d5_katya_kitchen_kat2_aside1_1 = "locate/katya/ant_k/new2/Kaite/eye/aside/01.png"
    image d5_katya_kitchen_kat2_aside1_2 = "locate/katya/ant_k/new2/Kaite/eye/aside/02.png"
    image d5_katya_kitchen_kat2_aside1_3 = "locate/katya/ant_k/new2/Kaite/eye/aside/03.png"
    image d5_katya_kitchen_kat2_aside:
        contains transform_blink("d5_katya_kitchen_kat2_aside1_1", "d5_katya_kitchen_kat2_aside1_2", "d5_katya_kitchen_kat2_aside1_3", delay=1.15)

    image d5_katya_kitchen_kat2_aside2_1 = "locate/katya/ant_k/new2/Kaite/eye/aside2/01.png"
    image d5_katya_kitchen_kat2_aside2_2 = "locate/katya/ant_k/new2/Kaite/eye/aside2/02.png"
    image d5_katya_kitchen_kat2_aside2_3 = "locate/katya/ant_k/new2/Kaite/eye/aside2/03.png"
    image d5_katya_kitchen_kat2_aside2:
        contains transform_blink("d5_katya_kitchen_kat2_aside2_1", "d5_katya_kitchen_kat2_aside2_2", "d5_katya_kitchen_kat2_aside2_3", delay=1.15)

    image d5_katya_kitchen_kat2_aside3_1 = "locate/katya/ant_k/new2/Kaite/eye/aside3/01.png"
    image d5_katya_kitchen_kat2_aside3_2 = "locate/katya/ant_k/new2/Kaite/eye/aside3/02.png"
    image d5_katya_kitchen_kat2_aside3_3 = "locate/katya/ant_k/new2/Kaite/eye/aside3/03.png"
    image d5_katya_kitchen_kat2_aside3:
        contains transform_blink("d5_katya_kitchen_kat2_aside3_1", "d5_katya_kitchen_kat2_aside3_2", "d5_katya_kitchen_kat2_aside3_3", delay=1.15)

    image d5_katya_kitchen_kat2_doun_1 = "locate/katya/ant_k/new2/Kaite/eye/doun/01.png"
    image d5_katya_kitchen_kat2_doun_2 = "locate/katya/ant_k/new2/Kaite/eye/doun/02.png"
    image d5_katya_kitchen_kat2_doun_3 = "locate/katya/ant_k/new2/Kaite/eye/doun/03.png"
    image d5_katya_kitchen_kat2_doun:
        contains transform_blink("d5_katya_kitchen_kat2_doun_1", "d5_katya_kitchen_kat2_doun_2", "d5_katya_kitchen_kat2_doun_3", delay=1.15)

    image d5_katya_kitchen_kat2_doun2_1 = "locate/katya/ant_k/new2/Kaite/eye/doun2/01.png"
    image d5_katya_kitchen_kat2_doun2_2 = "locate/katya/ant_k/new2/Kaite/eye/doun2/02.png"
    image d5_katya_kitchen_kat2_doun2_3 = "locate/katya/ant_k/new2/Kaite/eye/doun2/03.png"
    image d5_katya_kitchen_kat2_doun2:
        contains transform_blink("d5_katya_kitchen_kat2_doun2_1", "d5_katya_kitchen_kat2_doun2_2", "d5_katya_kitchen_kat2_doun2_3", delay=1.15)

    image d5_katya_kitchen_kat2_m0 = "locate/katya/ant_k/new2/Kaite/m00.png"
    image d5_katya_kitchen_kat2_m1 = "locate/katya/ant_k/new2/Kaite/m01.png"
    image d5_katya_kitchen_kat2_m2 = "locate/katya/ant_k/new2/Kaite/m02.png"
    image d5_katya_kitchen_kat2_m3 = "locate/katya/ant_k/new2/Kaite/m03.png"
    image d5_katya_kitchen_kat2_m4 = "locate/katya/ant_k/new2/Kaite/m04.png"
    image d5_katya_kitchen_kat2_m5 = "locate/katya/ant_k/new2/Kaite/m05.png"

    image d5_katya_kitchen_kat2 aside m0:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m0"
    image d5_katya_kitchen_kat2 aside m1:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m1"
    image d5_katya_kitchen_kat2 aside m2:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m2"
    image d5_katya_kitchen_kat2 aside m3:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m3"
    image d5_katya_kitchen_kat2 aside m4:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m4"
    image d5_katya_kitchen_kat2 aside m5:
        contains:
            "d5_katya_kitchen_kat2_aside"
        contains:
            "d5_katya_kitchen_kat2_m5"

    image d5_katya_kitchen_kat2 aside2 m0:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m0"
    image d5_katya_kitchen_kat2 aside2 m1:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m1"
    image d5_katya_kitchen_kat2 aside2 m2:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m2"
    image d5_katya_kitchen_kat2 aside2 m3:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m3"
    image d5_katya_kitchen_kat2 aside2 m4:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m4"
    image d5_katya_kitchen_kat2 aside2 m5:
        contains:
            "d5_katya_kitchen_kat2_aside2"
        contains:
            "d5_katya_kitchen_kat2_m5"

    image d5_katya_kitchen_kat2 aside3 m0:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m0"
    image d5_katya_kitchen_kat2 aside3 m1:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m1"
    image d5_katya_kitchen_kat2 aside3 m2:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m2"
    image d5_katya_kitchen_kat2 aside3 m3:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m3"
    image d5_katya_kitchen_kat2 aside3 m4:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m4"
    image d5_katya_kitchen_kat2 aside3 m5:
        contains:
            "d5_katya_kitchen_kat2_aside3"
        contains:
            "d5_katya_kitchen_kat2_m5"

    image d5_katya_kitchen_kat2 doun m0:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m0"
    image d5_katya_kitchen_kat2 doun m1:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m1"
    image d5_katya_kitchen_kat2 doun m2:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m2"
    image d5_katya_kitchen_kat2 doun m3:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m3"
    image d5_katya_kitchen_kat2 doun m4:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m4"
    image d5_katya_kitchen_kat2 doun m5:
        contains:
            "d5_katya_kitchen_kat2_doun"
        contains:
            "d5_katya_kitchen_kat2_m5"

    image d5_katya_kitchen_kat2 doun2 m0:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m0"
    image d5_katya_kitchen_kat2 doun2 m1:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m1"
    image d5_katya_kitchen_kat2 doun2 m2:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m2"
    image d5_katya_kitchen_kat2 doun2 m3:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m3"
    image d5_katya_kitchen_kat2 doun2 m4:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m4"
    image d5_katya_kitchen_kat2 doun2 m5:
        contains:
            "d5_katya_kitchen_kat2_doun2"
        contains:
            "d5_katya_kitchen_kat2_m5"

    image d5_katya_bed_bg1 = "locate/katya/bed/0001.png"
    image d5_katya_bed_bg2 = "locate/katya/bed/0002.png"
    image d5_katya_bed_bg3 = "locate/katya/bed/0004.png"
    image d5_katya_bed_bg4a = "locate/katya/bed/0005.png"
    image d5_katya_bed_bg4b = "locate/katya/bed/0006.png"
    image d5_katya_bed_bg4:
        "d5_katya_bed_bg4a"
        .3
        "d5_katya_bed_bg4b"
        .3
        repeat
    image d5_katya_bed_bg_overlay = "locate/katya/bed/0003.png"
    image d5_katya_bed_spot1 = "locate/katya/bed/pyatno/P1.png"
    image d5_katya_bed_spot2 = "locate/katya/bed/pyatno/P2.png"

    image d5_katya_bed_eyes_ahead_1 = "locate/katya/bed/ahead/01.png"
    image d5_katya_bed_eyes_ahead_2 = "locate/katya/bed/ahead/02.png"
    image d5_katya_bed_eyes_ahead_3 = "locate/katya/bed/ahead/03.png"
    image d5_katya_bed_eyes_ahead_blink:
        animation
        "d5_katya_bed_eyes_ahead_1"
        .5
        "d5_katya_bed_eyes_ahead_2"
        .1
        "d5_katya_bed_eyes_ahead_3"
        .1
        "d5_katya_bed_eyes_ahead_2"
        .1
        "d5_katya_bed_eyes_ahead_1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat

    image d5_katya_bed_eyes_aside_1 = "locate/katya/bed/aside/01.png"
    image d5_katya_bed_eyes_aside_2 = "locate/katya/bed/aside/02.png"
    image d5_katya_bed_eyes_aside_3 = "locate/katya/bed/aside/03.png"
    image d5_katya_bed_eyes_aside_blink:
        animation
        "d5_katya_bed_eyes_aside_1"
        .5
        "d5_katya_bed_eyes_aside_2"
        .1
        "d5_katya_bed_eyes_aside_3"
        .1
        "d5_katya_bed_eyes_aside_2"
        .1
        "d5_katya_bed_eyes_aside_1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat

    image d5_katya_bed_eyes_ahead_to_aside:
        "d5_katya_bed_eyes_ahead_1"
        .1
        "d5_katya_bed_eyes_ahead_2"
        .1
        "d5_katya_bed_eyes_aside_3"
        .1
        "d5_katya_bed_eyes_aside_2"
        .1
        "d5_katya_bed_eyes_aside_1"
        5.
        "d5_katya_bed_eyes_aside_blink"


    image d5_katya_bed_eyes_mouth_1 = "locate/katya/bed/m/01.png"
    image d5_katya_bed_eyes_mouth_2 = "locate/katya/bed/m/02.png"
    image d5_katya_bed_eyes_mouth_3 = "locate/katya/bed/m/03.png"

    image d5_katya_bed_eyes_cry1_1 = "locate/katya/bed/Cry1/001.png"
    image d5_katya_bed_eyes_cry1_2 = "locate/katya/bed/Cry1/002.png"
    image d5_katya_bed_eyes_cry1_3 = "locate/katya/bed/Cry1/003.png"
    image d5_katya_bed_eyes_cry1_blink:
        animation
        "d5_katya_bed_eyes_cry1_1"
        .5
        "d5_katya_bed_eyes_cry1_2"
        .1
        "d5_katya_bed_eyes_cry1_3"
        .1
        "d5_katya_bed_eyes_cry1_2"
        .1
        "d5_katya_bed_eyes_cry1_1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat

    image d5_katya_bed_eyes_cry2_1 = "locate/katya/bed/Cry2/01.png"
    image d5_katya_bed_eyes_cry2_2 = "locate/katya/bed/Cry2/02.png"
    image d5_katya_bed_eyes_cry2_3 = "locate/katya/bed/Cry2/03.png"
    image d5_katya_bed_eyes_cry2_blink:
        animation
        "d5_katya_bed_eyes_cry2_1"
        .5
        "d5_katya_bed_eyes_cry2_2"
        .1
        "d5_katya_bed_eyes_cry2_3"
        .1
        "d5_katya_bed_eyes_cry2_2"
        .1
        "d5_katya_bed_eyes_cry2_1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat



    layeredimage d5_katya_bed:
        group base:
            attribute bg1:
                "d5_katya_bed_bg1"
            attribute bg2:
                "d5_katya_bed_bg2"
            attribute bg3:
                "d5_katya_bed_bg3"
            attribute bg4:
                "d5_katya_bed_bg4"

        attribute overlay:
            "d5_katya_bed_bg_overlay"

        group eyes:
            attribute ahead:
                "d5_katya_bed_eyes_ahead_blink"
            attribute aside:
                "d5_katya_bed_eyes_aside_blink"
            attribute to_aside:
                "d5_katya_bed_eyes_ahead_to_aside"
            attribute cry1:
                "d5_katya_bed_eyes_cry1_blink"
            attribute cry2:
                "d5_katya_bed_eyes_cry2_blink"

        group mouth:
            attribute smile:
                "d5_katya_bed_eyes_mouth_1"
            attribute frown:
                "d5_katya_bed_eyes_mouth_2"
            attribute open:
                "d5_katya_bed_eyes_mouth_3"

        group spot:
            attribute plus:
                "d5_katya_bed_spot1"
            attribute minus:
                "d5_katya_bed_spot2"


    image d5_katya_bed_bg 1 = "locate/katya/bad/bg.png"
    image d5_katya_bed_bg 2 = "locate/katya/bad/bg02.png"
    image d5_katya_bed_bg 3 = "locate/katya/bad/bg03.png"
    image d5_katya_bed_bg 3b = "locate/katya/bad/bg03b.png"
    image d5_katya_bed_bg 4 = "locate/katya/bad/bg04.png"
    image d5_katya_bed_bg 5 = "locate/katya/bad/bg05.png"
    image d5_katya_bed_bg 6 = "locate/katya/bad/bg06.png"
    image d5_katya_bed_bg 7 = "locate/katya/bad/bg07.png"
    image d5_katya_bed_ahead_eyes1 = "locate/katya/bad/kaite01.png"
    image d5_katya_bed_ahead_eyes2 = "locate/katya/bad/kaite02.png"
    image d5_katya_bed_ahead_eyes3 = "locate/katya/bad/kaite03.png"
    image d5_katya_bed_ahead_blink:
        animation
        "d5_katya_bed_ahead_eyes1"
        .5
        "d5_katya_bed_ahead_eyes2"
        .1
        "d5_katya_bed_ahead_eyes3"
        .1
        "d5_katya_bed_ahead_eyes2"
        .1
        "d5_katya_bed_ahead_eyes1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat

    image d5_katya_bed_aside_eyes1 = "locate/katya/bad/aside/01.png"
    image d5_katya_bed_aside_eyes2 = "locate/katya/bad/aside/02.png"
    image d5_katya_bed_aside_eyes3 = "locate/katya/bad/aside/03.png"
    image d5_katya_bed_aside_blink:
        "d5_katya_bed_aside_eyes1"
        .1
        "d5_katya_bed_aside_eyes2"
        .1
        "d5_katya_bed_aside_eyes3"
        .1
        "d5_katya_bed_aside_eyes2"
        .1
        "d5_katya_bed_aside_eyes1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat

    image d5_katya_bed_ahead_to_aside:
        "d5_katya_bed_ahead_eyes1"
        .1
        "d5_katya_bed_ahead_eyes2"
        .1
        "d5_katya_bed_aside_eyes3"
        .1
        "d5_katya_bed_aside_eyes2"
        .1
        "d5_katya_bed_aside_eyes1"
        5.
        "d5_katya_bed_aside_blink"

    image d5_katya_bed_cry_eyes1 = "locate/katya/bad/cry01.png"
    image d5_katya_bed_cry_eyes2 = "locate/katya/bad/cry02.png"
    image d5_katya_bed_cry_eyes3 = "locate/katya/bad/cry03.png"
    image d5_katya_bed_cry_blink:
        animation
        "d5_katya_bed_cry_eyes1"
        .5
        "d5_katya_bed_cry_eyes2"
        .1
        "d5_katya_bed_cry_eyes3"
        .1
        "d5_katya_bed_cry_eyes2"
        .1
        "d5_katya_bed_cry_eyes1"
        choice:
            renpy.random.random() * 2 + 4
        choice:
            renpy.random.random() * 2 + 5
        choice:
            renpy.random.random() * 2 + 6
        repeat


    image d5_katya_bed 1:
        contains:
            "d5_katya_bed_bg 1"
        contains:
            "d5_katya_bed_ahead_blink"
    image d5_katya_bed 2:
        contains:
            "d5_katya_bed_bg 2"
        contains:
            "d5_katya_bed_ahead_to_aside"
    image d5_katya_bed 2a:
        contains:
            "d5_katya_bed_bg 2"
        contains:
            "d5_katya_bed_ahead_blink"
            .5
            "d5_katya_bed_ahead_to_aside"
    image d5_katya_bed 2b:
        contains:
            "d5_katya_bed_bg 2"
        contains:
            "d5_katya_bed_aside_blink"

    image d5_katya_bed 3:
        contains:
            "d5_katya_bed_bg 3"
        contains:
            "d5_katya_bed_aside_blink"
    image d5_katya_bed 3b:
        contains:
            "d5_katya_bed_bg 3b"
        contains:
            "d5_katya_bed_cry_blink"

    image d5_katya_bed 4 = "d5_katya_bed_bg 4"
    image d5_katya_bed 5 = "d5_katya_bed_bg 5"
    image d5_katya_bed 6:
        "d5_katya_bed_bg 6"
        .4
        "d5_katya_bed_bg 7"
        .4
        repeat


    image d5_katya_room3_bg = "locate/katya/room3/bg.png"
    image d5_katya_room3_g1 = "locate/katya/room3/00.png"
    image d5_katya_room3_g2 = "locate/katya/room3/01.png"
    image d5_katya_room3_g3 = "locate/katya/room3/02-06.png"
    image d5_katya_room3_g4 = "locate/katya/room3/03-05.png"
    image d5_katya_room3_g5 = "locate/katya/room3/04.png"
    image d5_katya_room3_ghost:
        "d5_katya_room3_g2"
        .1
        "d5_katya_room3_g3"
        .1
        "d5_katya_room3_g4"
        .1
        "d5_katya_room3_g5"
        .1
        "d5_katya_room3_g4"
        .1
        "d5_katya_room3_g3"
        .1
        repeat

    image d5_katya_room3_ghost_short_candidate1:
        "d5_katya_room3_g2"
        .1
        "d5_katya_room3_g3"
        .1
        "d5_katya_room3_g4"
        .1
        "d5_katya_room3_g3"
        .1
        "d5_katya_room3_g2"
        .1
        repeat

    image d5_katya_room3_ghost_short_candidate2:
        "d5_katya_room3_g2"




    image d5_mkd_olya ghost = "d5_katya_room3_ghost"

    image d5_mkd_olya stable = "d5_katya_room3_ghost_short_candidate2"
    image d5_mkd_olya short = "d5_katya_room3_ghost_short_candidate2"



    image d5_mkd_olya shade = "d5_katya_room3_g1"


    image d5_katya_refuse_bg_1 = "locate/katya/nightmare/bg.png"
    image d5_katya_refuse_bg_2 = "locate/katya/nightmare/bg1.png"
    image d5_katya_refuse_bg:
        contains:
            "d5_katya_refuse_bg_1"
        contains:
            "d5_katya_refuse_bg_2"

    image d5_katya_refuse_hare0 = "locate/katya/nightmare/Hare.png"
    image d5_katya_refuse_hare = "locate/katya/nightmare/Hare1.png"
    image d5_katya_refuse_hare_talk = "locate/katya/nightmare/Hare2.png"

    image d5_katya_poddon empty:
        "d4_poddon 1"
    image d5_katya_poddon_face = "locate/katya/nightmare/Kat0.png"
    image d5_katya_poddon_face2 = "locate/katya/nightmare/Kat1.png"
    image d5_katya_poddon_face3 = "locate/katya/nightmare/Kat2.png"
    image d5_katya_poddon faced:
        contains:
            "d5_katya_poddon empty"
        contains:
            "d5_katya_poddon_face"

    image d5_katya_refuse2_anton 1 = "sprite/ant/Ant_cry.png"
    image d5_katya_refuse2_anton 2 = "sprite/ant/Ant_cry2.png"
    image d5_katya_refuse2_anton_blood = "sprite/ant/Ant_cry_blood.png"
    image d5_katya_refuse2_anton 3 = Composite((1920, 1080),
        (0, 0), "d5_katya_refuse2_anton 2",
        (0, 0), "sprite/ant/Ant_cry3.png")
    image d5_katya_refuse2_anton = ConditionSwitch(
        "d4_palace_garage_light_on", "d5_katya_refuse2_anton 1",
        "True", "d5_katya_refuse2_anton 2")
    image d5_katya_refuse2_anton_kate = LiveComposite((1920, 1080),
        (0, 0), ConditionSwitch(
            "d4_palace_garage_light_on", "d5_katya_refuse2_anton 1",
            "True", "d5_katya_refuse2_anton 2"),
        (0, 0), "d5_katya_refuse2_anton_blood")

    image d5_katya_refuse2_hare = "locate/katya/nightmare/Hare0.png"

    image d5_katya_refuse2_claws_0 = "locate/katya/nightmare/kogti0.png"
    image d5_katya_refuse2_claws_1 = "locate/katya/nightmare/kogti1.png"
    image d5_katya_refuse2_claws_2 = "locate/katya/nightmare/kogti2.png"
    image d5_katya_refuse2_claws_3 = "locate/katya/nightmare/kogti3.png"

    image d5_katya_refuse3_mincer_slow_1 = "locate/katya/mincer/2/01.png"
    image d5_katya_refuse3_mincer_slow_2 = "locate/katya/mincer/2/02.png"
    image d5_katya_refuse3_mincer_slow_3 = "locate/katya/mincer/2/03.png"
    image d5_katya_refuse3_mincer_slow_4 = "locate/katya/mincer/2/04.png"
    image d5_katya_refuse3_mincer_slow_5 = "locate/katya/mincer/2/05.png"
    image d5_katya_refuse3_mincer_slow:
        "d5_katya_refuse3_mincer_slow_1"
        .1
        "d5_katya_refuse3_mincer_slow_2"
        .1
        "d5_katya_refuse3_mincer_slow_3"
        .1
        "d5_katya_refuse3_mincer_slow_4"
        .1
        "d5_katya_refuse3_mincer_slow_5"
        .1
        repeat

    image d5_katya_refuse3_mincer_fast_1 = "locate/katya/mincer/3/01.png"
    image d5_katya_refuse3_mincer_fast_2 = "locate/katya/mincer/3/02.png"
    image d5_katya_refuse3_mincer_fast_3 = "locate/katya/mincer/3/03.png"
    image d5_katya_refuse3_mincer_fast_4 = "locate/katya/mincer/3/04.png"
    image d5_katya_refuse3_mincer_fast:
        "d5_katya_refuse3_mincer_fast_1"
        .1
        "d5_katya_refuse3_mincer_fast_2"
        .1
        "d5_katya_refuse3_mincer_fast_3"
        .1
        "d5_katya_refuse3_mincer_fast_4"
        .1
        repeat

    image d5_katya_refuse_ceiling_01 = "locate/katya/ceiling/01.png"
    image d5_katya_refuse_ceiling_02 = "locate/katya/ceiling/02.png"
    image d5_katya_refuse_ceiling_03 = "locate/katya/ceiling/03.png"
    image d5_katya_refuse_ceiling_04 = "locate/katya/ceiling/04.png"
    image d5_katya_refuse_ceiling_05 = "locate/katya/ceiling/05.png"
    image d5_katya_refuse_ceiling_06 = "locate/katya/ceiling/06.png"
    image d5_katya_refuse_ceiling_07 = "locate/katya/ceiling/07.png"
    image d5_katya_refuse_ceiling_08 = "locate/katya/ceiling/08.png"
    image d5_katya_refuse_ceiling_09 = "locate/katya/ceiling/09.png"
    image d5_katya_refuse_ceiling_10 = "locate/katya/ceiling/10.png"
    image d5_katya_refuse_ceiling_11 = "locate/katya/ceiling/11.png"
    image d5_katya_refuse_ceiling_12 = "locate/katya/ceiling/12.png"
    image d5_katya_refuse_ceiling_13 = "locate/katya/ceiling/13.png"
    image d5_katya_refuse_ceiling_14 = "locate/katya/ceiling/14.png"
    image d5_katya_refuse_ceiling_15 = "locate/katya/ceiling/15.png"
    image d5_katya_refuse_ceiling:
        "d5_katya_refuse_ceiling_01"
        .1
        "d5_katya_refuse_ceiling_02"
        .1
        "d5_katya_refuse_ceiling_03"
        .1
        "d5_katya_refuse_ceiling_04"
        .1
        "d5_katya_refuse_ceiling_05"
        .1
        "d5_katya_refuse_ceiling_06"
        .1
        "d5_katya_refuse_ceiling_07"
        .1
        "d5_katya_refuse_ceiling_08"
        .1
        "d5_katya_refuse_ceiling_09"
        .1
        "d5_katya_refuse_ceiling_10"
        .1
        "d5_katya_refuse_ceiling_11"
        .1
        "d5_katya_refuse_ceiling_12"
        .1
        "d5_katya_refuse_ceiling_13"
        .1
        "d5_katya_refuse_ceiling_14"
        .1
        "d5_katya_refuse_ceiling_15"

    image d5_katya_refuse_ceiling_16 = "locate/katya/ceiling/16.png"

    image d5_katya_refuse3_mincer_ant_1 = "locate/katya/mincer/1/1.png"
    image d5_katya_refuse3_mincer_ant_2 = "locate/katya/mincer/1/2.png"
    image d5_katya_refuse3_mincer_ant_3 = "locate/katya/mincer/1/3.png"
    image d5_katya_refuse3_mincer_ant_4 = "locate/katya/mincer/1/4.png"
    image d5_katya_refuse3_mincer_ant:
        "d5_katya_refuse3_mincer_ant_1"
        .1
        "d5_katya_refuse3_mincer_ant_2"
        .1
        "d5_katya_refuse3_mincer_ant_3"
        .1
        "d5_katya_refuse3_mincer_ant_4"
        .1
        repeat

    image d5_katya_refuse3_ant_1 = "locate/katya/mincer/1/ant1.png"
    image d5_katya_refuse3_ant_2 = "locate/katya/mincer/1/ant2.png"

    image d5_katya_refuse3_ant_hands_1 = "locate/katya/mincer/1/hands1.png"
    image d5_katya_refuse3_ant_hands_2 = "locate/katya/mincer/1/hands2.png"
    image d5_katya_refuse3_ant_hands_3 = "locate/katya/mincer/1/hands3.png"

    image d5_katya_refuse3_blood_1 = "locate/katya/mincer/1/b1.png"
    image d5_katya_refuse3_blood_2 = "locate/katya/mincer/1/b2.png"
    image d5_katya_refuse3_blood_3 = "locate/katya/mincer/1/b3.png"
    image d5_katya_refuse3_blood_4 = "locate/katya/mincer/1/b4.png"
    image d5_katya_refuse3_blood_5 = "locate/katya/mincer/1/b5.png"
    image d5_katya_refuse3_blood_6 = "locate/katya/mincer/1/b6.png"
    image d5_katya_refuse3_blood_7 = "locate/katya/mincer/1/b7.png"
    image d5_katya_refuse3_blood_8 = "locate/katya/mincer/1/b8.png"

    image d5_katya_refuse3_blood:
        "d5_katya_refuse3_blood_1"
        0.3
        "d5_katya_refuse3_blood_2"
        0.3
        "d5_katya_refuse3_blood_3"
        0.3
        "d5_katya_refuse3_blood_4"
        0.3
        "d5_katya_refuse3_blood_5"
        0.3
        "d5_katya_refuse3_blood_6"
        0.3
        "d5_katya_refuse3_blood_7"
        0.3
        "d5_katya_refuse3_blood_8"
        0.3
        "black"

    image d5_katya_refuse_divan_bg = "locate/katya/mincer/5/bg.png"
    image d5_katya_refuse_divan_1 = "locate/katya/mincer/5/d3.png"
    image d5_katya_refuse_divan_2 = "locate/katya/mincer/5/d1.png"
    image d5_katya_refuse_divan_3 = "locate/katya/mincer/5/d2.png"
    image d5_katya_refuse_divk_1 = "locate/katya/mincer/5/k2.png"
    image d5_katya_refuse_divk_2 = "locate/katya/mincer/5/k1.png"

    define bd_dt = 0.05
    image d5_katya_refuse_blood:
        block:
            "d4_sk_katya_blood_1"
            bd_dt
            "d4_sk_katya_blood_2"
            bd_dt
            "d4_sk_katya_blood_3"
            bd_dt
            "d4_sk_katya_blood_4"
            bd_dt
            "d4_sk_katya_blood_5"
            bd_dt
            "d4_sk_katya_blood_6"
            bd_dt
            "d4_sk_katya_blood_7"
            bd_dt
            "d4_sk_katya_blood_8"
            bd_dt
            "d4_sk_katya_blood_9"
            bd_dt
            "d4_sk_katya_blood_10"
            bd_dt
            "d4_sk_katya_blood_11"
            bd_dt
            "d4_sk_katya_blood_12"
            bd_dt
            "d4_sk_katya_blood_13"
            bd_dt
            "d4_sk_katya_blood_14"
            bd_dt
            "d4_sk_katya_blood_15"
            bd_dt
            "d4_sk_katya_blood_16"
            bd_dt
            "d4_sk_katya_blood_17"
            bd_dt
            "d4_sk_katya_blood_18"
            bd_dt
            "d4_sk_katya_blood_19"
            bd_dt
            "d4_sk_katya_blood_20"
            bd_dt
            "d4_sk_katya_blood_21"
            bd_dt
            "d4_sk_katya_blood_22"
            bd_dt
            "d4_sk_katya_blood_23"
            bd_dt
            "d4_sk_katya_blood_24"
            bd_dt
            Null()
            choice:
                1.
            choice:
                2
            choice:
                3
            repeat

    image d5_katya_refuse_luxury = "locate/katya/mincer/k.png"

    image d5_katya_refuse6_bg = "locate/katya/mincer/6/fon.png"
    image d5_katya_refuse6_far = "locate/katya/mincer/6/1.png"
    image d5_katya_refuse6_close = "locate/katya/mincer/6/2.png"
    image d5_katya_refuse6_katya = "locate/katya/mincer/6/3.png"

    image d5_katya_refuse7_bg = "locate/katya/mincer/7/fon.png"
    image d5_katya_refuse7_far = "locate/katya/mincer/7/1.png"
    image d5_katya_refuse7_kbod = "locate/katya/mincer/7/k1.png"
    image d5_katya_refuse7_khea = "locate/katya/mincer/7/k2.png"

    image d5_katya_lever_bg = "locate/katya/mincer/8/Garage1.png"
    image d5_katya_lever_fg = "locate/katya/mincer/8/Garage2.png"

    image d5_katya_refuse_hand_left = "locate/home/in_side/1st_floor/hall/left.png"
    image d5_katya_refuse_hand_right = "locate/home/in_side/1st_floor/hall/right.png"


    image d5_polina_window1 = "images/locate/school/out_side/school_coner/Help001.png"
    image d5_polina_window2 = "images/locate/school/out_side/school_coner/Help002.png"

    image d5_polina_lonely = "images/locate/school/out_side/school_coner/lonely_katya.png"

    image d5_polka_anton shy = "images/locate/school/out_side/school_coner/Anton.png"
    image d5_polka_anton norm:
        contains:
            "d5_polka_anton shy"
        contains:
            "images/locate/school/out_side/school_coner/A01.png"
    image d5_polka_anton shy talk:
        contains:
            "d5_polka_anton shy"
        contains:
            "images/locate/school/out_side/school_coner/Anton02.png"
    image d5_polka_anton aside:
        contains:
            "d5_polka_anton shy"
        contains:
            "images/locate/school/out_side/school_coner/A02.png"
    image d5_polka_anton aside talk:
        contains:
            "d5_polka_anton shy"
        contains:
            "images/locate/school/out_side/school_coner/A02.png"
        contains:
            "images/locate/school/out_side/school_coner/Anton02.png"

    image d5_roadwalk_01 = "locate/street/walking_fox_day/road_fox01.jpg"
    image d5_roadwalk_02 = "locate/street/walking_fox_day/road_fox02.png"
    image d5_roadwalk_03 = "locate/street/walking_fox_day/road_fox03.png"

    image d5_roadwalk_anton_sadface_left = "locate/street/walking_fox_day/Ant_left2.png"
    image d5_roadwalk_anton_sadface_right:
        "d5_roadwalk_anton_sadface_left"
        xzoom -1

    default d5_roadwalk_state_anton = 0
    image d5_roadwalk_anton left = Composite((707, 1080),
        (0,0), ConditionSwitch(
            "d5_roadwalk_state_anton == 2", "locate/street/walking_fox_day/Ant_left3.png",
            "True", "locate/street/walking_fox_day/Ant_left.png"),
        (0,0), ConditionSwitch(
            "d5_roadwalk_state_anton == 1", "d5_roadwalk_anton_sadface_left",
            "True", Null())
        )
    image d5_roadwalk_anton right = Composite((707, 1080),
        (0,0), "locate/street/walking_fox_day/Ant_right.png",
        (0,0), ConditionSwitch(
            "d5_roadwalk_state_anton == 1", "d5_roadwalk_anton_sadface_right",
            "True", Null())
        )
    image d5_roadwalk_polina 1 = Composite((445, 882),
            (0,0), "locate/street/walking_fox_day/Polina.png",
            (0,0), ConditionSwitch(
                "polina_face_state == 2", "locate/street/walking_fox_day/Polina_2.png",
                "polina_face_state == 3", "locate/street/walking_fox_day/Polina_3.png",
                "polina_face_state == 4", "locate/street/walking_fox_day/Polina_4.png",
                "polina_face_state == 5", "locate/street/walking_fox_day/Polina_5.png",
                "True", Null(),)
            )
    image d5_roadwalk_polina 2 = Composite((445, 882),
            (0,0), "locate/street/walking_fox_day/Polina02.png",
            (0,0), ConditionSwitch(
                "polina_face_state == 2", "locate/street/walking_fox_day/Polina_2.png",
                "polina_face_state == 3", "locate/street/walking_fox_day/Polina_3.png",
                "polina_face_state == 4", "locate/street/walking_fox_day/Polina_4.png",
                "polina_face_state == 5", "locate/street/walking_fox_day/Polina_5.png",
                "True", Null(),)
            )

    image d5_polina_phone_bg = "locate/Polina/phone_bg.png"
    image d5_polina_phone 1 = "locate/Polina/phone_1.png"
    image d5_polina_phone 2 = "locate/Polina/phone_2.png"

    image d5_polina_phone_k_0_idle = "locate/Polina/phone/000.png"
    image d5_polina_phone_k_0_hover:
        "d5_polina_phone_k_0_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_0_pressed = "locate/Polina/phone/00.png"
    image d5_polina_phone_k_1_idle = "locate/Polina/phone/001.png"
    image d5_polina_phone_k_1_hover:
        "d5_polina_phone_k_1_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_1_pressed = "locate/Polina/phone/01.png"
    image d5_polina_phone_k_2_idle = "locate/Polina/phone/002.png"
    image d5_polina_phone_k_2_hover:
        "d5_polina_phone_k_2_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_2_pressed = "locate/Polina/phone/02.png"
    image d5_polina_phone_k_3_idle = "locate/Polina/phone/003.png"
    image d5_polina_phone_k_3_hover:
        "d5_polina_phone_k_3_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_3_pressed = "locate/Polina/phone/03.png"
    image d5_polina_phone_k_4_idle = "locate/Polina/phone/004.png"
    image d5_polina_phone_k_4_hover:
        "d5_polina_phone_k_4_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_4_pressed = "locate/Polina/phone/04.png"
    image d5_polina_phone_k_5_idle = "locate/Polina/phone/005.png"
    image d5_polina_phone_k_5_hover:
        "d5_polina_phone_k_5_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_5_pressed = "locate/Polina/phone/05.png"
    image d5_polina_phone_k_6_idle = "locate/Polina/phone/006.png"
    image d5_polina_phone_k_6_hover:
        "d5_polina_phone_k_6_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_6_pressed = "locate/Polina/phone/06.png"
    image d5_polina_phone_k_7_idle = "locate/Polina/phone/007.png"
    image d5_polina_phone_k_7_hover:
        "d5_polina_phone_k_7_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_7_pressed = "locate/Polina/phone/07.png"
    image d5_polina_phone_k_8_idle = "locate/Polina/phone/008.png"
    image d5_polina_phone_k_8_hover:
        "d5_polina_phone_k_8_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_8_pressed = "locate/Polina/phone/08.png"
    image d5_polina_phone_k_9_idle = "locate/Polina/phone/009.png"
    image d5_polina_phone_k_9_hover:
        "d5_polina_phone_k_9_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_9_pressed = "locate/Polina/phone/09.png"

    image d5_polina_phone_k_reset_idle = "locate/Polina/phone/010.png"
    image d5_polina_phone_k_reset_hover:
        "d5_polina_phone_k_reset_idle"
        matrixcolor BrightnessMatrix (0.1)
    image d5_polina_phone_k_reset_pressed = "locate/Polina/phone/10.png"

    image d5_polina_phone_hand = "locate/home/in_side/1st_floor/hall/anton_call/call_top.png"
    image d5_polina_phone_byasha = "locate/Polina/bysha.png"

    image d5_polina_number = "locate/Polina/phone/ant_ru.png"

    image d5_polina_mystic_ant1 = "locate/Polina/mistik/A1.png"
    image d5_polina_mystic_ant2_1 = "locate/Polina/mistik/A2.png"
    image d5_polina_mystic_ant2_2:
        "d5_polina_mystic_ant2_1"
        matrixcolor BrightnessMatrix(-0.02)

    image d5_polina_mystic_ant2:
        contains:
            "d5_polina_mystic_ant2_1"
        contains:
            "d5_polina_mystic_ant2_2"
            alpha 0

            block:
                linear .1 alpha .35
                linear .1 alpha .0
                linear .1 alpha .35
                linear .1 alpha .0
                linear .1 alpha .7
                linear .1 alpha .0
                repeat

    image d5_polina_mystic_bg1 = "locate/Polina/mistik/bg1.png"
    image d5_polina_mystic_bg2_1 = "locate/Polina/mistik/bg2png.png"
    image d5_polina_mystic_bg2_2:
        "d5_polina_mystic_bg2_1"
        matrixcolor BrightnessMatrix(-0.02)

    image d5_polina_mystic_bg2:
        contains:
            "d5_polina_mystic_bg2_1"
        contains:
            "d5_polina_mystic_bg2_2"
            alpha 0

            block:
                linear .1 alpha .35
                linear .1 alpha .0
                linear .1 alpha .35
                linear .1 alpha .0
                linear .1 alpha .7
                linear .1 alpha .0
                repeat

    image d5_polina_mystic_flame_1 = "locate/Polina/mistik/flame1.png"
    image d5_polina_mystic_flame_2 = "locate/Polina/mistik/flame2.png"
    image d5_polina_mystic_flame_3 = "locate/Polina/mistik/flame3.png"
    image d5_polina_mystic_flame_4 = "locate/Polina/mistik/flame4.png"
    image d5_polina_mystic_flame_5 = "locate/Polina/mistik/flame5.png"

    image d5_polina_mystic_flame:
        "d5_polina_mystic_flame_1"
        .1
        "d5_polina_mystic_flame_2"
        .1
        "d5_polina_mystic_flame_3"
        .1
        "d5_polina_mystic_flame_4"
        .1
        "d5_polina_mystic_flame_5"
        .1
        repeat

    image d5_polina_mystic_flame2_0 = "locate/Polina/mistik/flame00.png"
    image d5_polina_mystic_flame2_1 = "locate/Polina/mistik/flame01.png"
    image d5_polina_mystic_flame2_2 = "locate/Polina/mistik/flame02.png"
    image d5_polina_mystic_flame2_3 = "locate/Polina/mistik/flame03.png"

    image d5_polina_mystic_candle_base = "locate/Polina/mistik/candle.png"
    image d5_polina_mystic_candle_base_dark = "locate/Polina/mistik/candle0.png"

    image d5_polina_mystic_candle:
        contains:
            "d5_polina_mystic_candle_base"
        contains:
            "d5_polina_mystic_flame"

    image d5_polina_mystic_flame2:
        "d5_polina_mystic_flame2_0"
        .1
        "d5_polina_mystic_flame2_1"
        .1
        "d5_polina_mystic_flame2_2"
        .1
        "d5_polina_mystic_flame2_3"
        .1
        "d5_polina_mystic_flame"

    image d5_polina_mystic_candle_dark:
        contains:
            "d5_polina_mystic_candle_base_dark"
            "d5_polina_mystic_candle_base" with ImageDissolve("effect/imagedissolve/polmare/02.png", 0.5, reverse=True, ramplen=128)
        contains:
            "d5_polina_mystic_flame2"

    image d5_polina_mystic_ghost_1 = "locate/Polina/mistik/gost1.png"
    image d5_polina_mystic_ghost_2 = "locate/Polina/mistik/gost2.png"
    image d5_polina_mystic_ghost_3 = "locate/Polina/mistik/gost3.png"
    image d5_polina_mystic_ghost_4 = "locate/Polina/mistik/gost4.png"
    image d5_polina_mystic_ghost_5 = "locate/Polina/mistik/gost5.png"
    image d5_polina_mystic_ghost_6 = "locate/Polina/mistik/gost6.png"
    image d5_polina_mystic_ghost_7 = "locate/Polina/mistik/gost7.png"
    image d5_polina_mystic_ghost_8 = "locate/Polina/mistik/gost8.png"
    image d5_polina_mystic_ghost_9 = "locate/Polina/mistik/gost9.png"
    image d5_polina_mystic_ghost_10 = "locate/Polina/mistik/gost10.png"
    image d5_polina_mystic_ghost_11 = "locate/Polina/mistik/gost11.png"
    image d5_polina_mystic_ghost_12 = "locate/Polina/mistik/gost12.png"

    image d5_polina_mystic_ghost:
        "d5_polina_mystic_ghost_1"
        .1
        "d5_polina_mystic_ghost_2"
        .1
        "d5_polina_mystic_ghost_3"
        .1
        "d5_polina_mystic_ghost_4"
        .1
        "d5_polina_mystic_ghost_5"
        .1
        "d5_polina_mystic_ghost_6"
        .1
        "d5_polina_mystic_ghost_7"
        .1
        "d5_polina_mystic_ghost_8"
        .1
        "d5_polina_mystic_ghost_9"
        .1
        "d5_polina_mystic_ghost_10"
        .1
        "d5_polina_mystic_ghost_11"
        .1
        "d5_polina_mystic_ghost_12"
        .1
        repeat

    image d5_mpd_olya ghost = "d5_polina_mystic_ghost"
    image d5_mpd_olya short = "d5_polina_mystic_ghost_1"

    image d5_polina_home_clouds:
        contains:
            "locate/street/HousePol/Back.jpg"

        contains:
            "locate/street/HousePol/Cloud.png"
            subpixel True
            yalign 0
            xpos 0.95
            linear 5 xpos 1.0
            block:
                xpos 0.0
                linear 50 xpos 1.0
                repeat

        contains:
            "locate/street/HousePol/Cloud.png"
            subpixel True
            yalign 0
            xpos -.05
            linear 5 xpos 0.0
            block:
                xpos -1.0
                linear 50 xpos 0.0
                repeat

        contains:
            "locate/street/HousePol/Cloud2.png"
            subpixel True
            yalign 0
            block:
                xpos 0.0
                linear 30 xpos 1.0
                repeat

        contains:
            "locate/street/HousePol/Cloud2.png"
            subpixel True
            yalign 0
            block:
                xpos -1.0
                linear 30 xpos 0.0
                repeat

    image d5_pol_home_zoom = LiveComposite((1920, 1080),
        (0, 0), "polina_home_day_04",
        (0, 0), "Polina_home_door")

    image d5_pol_droom_bg:
        contains:
            "locate/Polina/darkroom.png"

        contains:
            "d5_pol_droom_pendulum"
    image d5_pol_droom_poster = "locate/Polina/darkroom_02.png"
    image d5_pol_droom_pendulum:
        contains:
            "locate/polina/darkpendulum.png"
            subpixel True
            anchor (.5, 0.)
            pos (955, 255)
            transform_anchor True
            rotate -10
            block:
                linear 1. rotate 10
                linear 1. rotate -10
                repeat
        contains:
            "locate/polina/darkring.png"

    image d5_polina_closet_bg = "locate/Polina/P01.png"
    image d5_polina_closet_fg = "locate/Polina/P02.png"

    image d5_polina_couch_bg = "locate/Polina/bg_pol_dark.png"
    image d5_polina_couch2_bg = "locate/Polina/bg_pol_dark2.png"

    image d5_polina_couch_anton gloom = LiveComposite((1920, 1080),
        (0, 0), "day3_ant_clas_anton 2",
        (0, 0), AlphaMask(Solid("#000a"), "day3_ant_clas_anton 2"),
        )
    image d5_polina_couch_anton smile = LiveComposite((1920, 1080),
        (0, 0), "day3_ant_clas_anton 1",
        (0, 0), AlphaMask(Solid("#000a"), "day3_ant_clas_anton 2"),
        )

    define d5_polina_cuddle_dark = "#0009"
    image d5_poline_cuddle_polina idle = LiveComposite((1920, 1080),
        (0, 0), "Polina Large b_day 01 sad aside 01",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "Polina Large b_day 01 sad aside 01"),
        )
    image d5_poline_cuddle_polina talk = LiveComposite((1920, 1080),
        (0, 0), "Polina Large b_day 01 sad aside 02",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "Polina Large b_day 01 sad aside 02"),
        )
    image d5_poline_cuddle_polina smile = LiveComposite((1920, 1080),
        (0, 0), "Polina Large b_day 01 norm ahead 03",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "Polina Large b_day 01 norm ahead 03"),
        )
    image d5_poline_cuddle_anton = LiveComposite((1920, 1080),
        (0, 0), "d4_polant",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "d4_polant"),
        )
    image d5_poline_cuddle_anton_back = LiveComposite((583, 1154),
        (0, 0), "d5_mstory_anton_back",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "d5_mstory_anton_back"),
        )
    image d5_poline_cuddle_hand = LiveComposite((1920, 1080),
        (0, 0), "d4_polhand",
        (0, 0), AlphaMask(Solid(d5_polina_cuddle_dark), "d4_polhand"),
        )


    image d5_mpol_acc_cup_bg = "locate/Polina/glass/bg.png"
    image d5_mpol_acc_cup_hand = "locate/Polina/glass/hand.png"



    image d5_mpol_ref_door 1 = "locate/Polina/1_1.png"
    image d5_mpol_ref_door 2 = "locate/Polina/1_2.png"
    image d5_mpol_ref_door 3 = "locate/Polina/1_3.png"
    image d5_mpol_ref_door knock:
        "d5_mpol_ref_door 1"
        .1
        "d5_mpol_ref_door 2"
        .1
        "d5_mpol_ref_door 3"
        .1
        "d5_mpol_ref_door 1"


    image d5_mpol_ref_window cat1 = "locate/Polina/nightmare1/curtains/001.png"
    image d5_mpol_ref_window cat2 = "locate/Polina/nightmare1/curtains/002.png"
    image d5_mpol_ref_window cat3 = "locate/Polina/nightmare1/curtains/003.png"
    image d5_mpol_ref_window cat4 = "locate/Polina/nightmare1/curtains/004.png"
    image d5_mpol_ref_window cat5 = "locate/Polina/nightmare1/curtains/005.png"
    image d5_mpol_ref_window cat6 = "locate/Polina/nightmare1/curtains/006.png"
    image d5_mpol_ref_window cat7 = "locate/Polina/nightmare1/curtains/007.png"
    image d5_mpol_ref_window cat8 = "locate/Polina/nightmare1/curtains/008.png"
    image d5_mpol_ref_window cat9 = "locate/Polina/nightmare1/curtains/009.png"
    image d5_mpol_ref_window cat10 = "locate/Polina/nightmare1/curtains/010.png"
    image d5_mpol_ref_window cat11 = "locate/Polina/nightmare1/curtains/011.png"
    image d5_mpol_ref_window cat:
        "d5_mpol_ref_window cat1"
        .1
        "d5_mpol_ref_window cat2"
        .1
        "d5_mpol_ref_window cat3"
        .1
        "d5_mpol_ref_window cat4"
        .1
        "d5_mpol_ref_window cat5"
        .1
        "d5_mpol_ref_window cat6"
        .1
        "d5_mpol_ref_window cat7"
        .1
        "d5_mpol_ref_window cat8"
        .1
        "d5_mpol_ref_window cat9"
        .1
        "d5_mpol_ref_window cat10"
        .1
        "d5_mpol_ref_window cat11"

    image d5_mpol_ref_window 1 = "locate/Polina/nightmare1/fon001.png"
    image d5_mpol_ref_window 2 = "locate/Polina/nightmare1/fon002.png"
    image d5_mpol_ref_window 2a:
        contains:
            "d5_mpol_ref_window 2"
        contains:
            "locate/Polina/nightmare1/fon003.png"
    image d5_mpol_ref_window 4 = "locate/Polina/nightmare1/fon004.png"
    image d5_mpol_ref_window 5 = "locate/Polina/nightmare1/fon005.png"
    image d5_mpol_ref_window 6 = "locate/Polina/nightmare1/fon006.png"
    image d5_mpol_ref_window 7 = "locate/Polina/nightmare1/fon007.png"
    image d5_mpol_ref_window 8 = "locate/Polina/nightmare1/fon008.png"
    image d5_mpol_ref_window 9 = "locate/Polina/nightmare1/fon009.png"
    image d5_mpol_ref_window 10 = "locate/Polina/nightmare1/10.png"

    image d5_mpol_ref_arm 1 = "locate/Polina/nightmare1/arm1.png"
    image d5_mpol_ref_arm 2 = "locate/Polina/nightmare1/arm2.png"

    image d5_mpol_ref_glass_1 = "locate/Polina/nightmare1/gl01.png"
    image d5_mpol_ref_glass_2 = "locate/Polina/nightmare1/gl02.png"
    image d5_mpol_ref_glass_3 = "locate/Polina/nightmare1/gl03.png"
    image d5_mpol_ref_glass_4 = "locate/Polina/nightmare1/gl04.png"

    image d5_mpol_ref_table_1 = "locate/Polina/nightmare1/p01.png"
    image d5_mpol_ref_table_2 = "locate/Polina/nightmare1/p02.png"

    image d5_mpol_ref_scratch = "locate/Polina/nightmare1/scratch.png"

    image d5_mpol_ref_scream = Composite((1920, 1080),
        (0, 0), "Polina Scream b_day 01 cry ahead 04",
        (0, 0), AlphaMask(Solid("#0006"), "Polina Scream b_day 01 cry ahead 04"))

    image d5_mpol_ref_nmare2_bg = "locate/Polina/nightmare2/bg.png"

    image d5_mpol_ref_nmare2_lamp = "locate/Polina/nightmare2/lamp.png"
    image d5_mpol_ref_nmare2_guts1 = "locate/Polina/nightmare2/guts.png"
    image d5_mpol_ref_nmare2_guts2 = "locate/Polina/nightmare2/gutsb.png"

    image d5_mpol_ref_nmare2_hpol 1 = "locate/Polina/nightmare2/pol1.png"
    image d5_mpol_ref_nmare2_hpol 2 = "locate/Polina/nightmare2/pol2.png"

    image d5_mpol_ref_nmare2_flame 1 = "locate/Polina/nightmare2/flame1.png"
    image d5_mpol_ref_nmare2_flame 2 = "locate/Polina/nightmare2/flame2.png"
    image d5_mpol_ref_nmare2_flame 3 = "locate/Polina/nightmare2/flame3.png"

    image d5_mpol_ref_nmare2_bunny 1 = "locate/Polina/nightmare2/bunny1.png"
    image d5_mpol_ref_nmare2_bunny 2 = "locate/Polina/nightmare2/bunny2.png"
    image d5_mpol_ref_nmare2_bunny 3 = "locate/Polina/nightmare2/bunny3.png"
    image d5_mpol_ref_nmare2_bunny_overlay = "locate/Polina/nightmare2/bunny4.png"
    image d5_mpol_ref_nmare2_bunny 4:
        contains:
            "d5_mpol_ref_nmare2_bunny 3"
        contains:
            "d5_mpol_ref_nmare2_bunny_overlay"

    image d5_mpol_ref_nmare2_wolf_1 1 = "locate/Polina/nightmare2/wolf1.png"
    image d5_mpol_ref_nmare2_wolf_1 2 = "locate/Polina/nightmare2/wolf2.png"
    image d5_mpol_ref_nmare2_wolf_1 3 = "locate/Polina/nightmare2/wolf3.png"
    image d5_mpol_ref_nmare2_wolf_2 1 = "locate/Polina/nightmare2/wolfs1.png"
    image d5_mpol_ref_nmare2_wolf_2 2 = "locate/Polina/nightmare2/wolfs2.png"
    image d5_mpol_ref_nmare2_wolf_2 3 = "locate/Polina/nightmare2/wolfs3.png"

    image d5_mpol_ref_nmare3_bg1 = "locate/Polina/nightmare3/bg.png"
    image d5_mpol_ref_nmare3_bg2 = "locate/Polina/nightmare3/bg2.png"

    image d5_mpol_ref_nmare3_polina 1 = "locate/Polina/nightmare3/p1.png"
    image d5_mpol_ref_nmare3_polina_overlay = "locate/Polina/nightmare3/p2.png"
    image d5_mpol_ref_nmare3_polina 2:
        contains:
            "d5_mpol_ref_nmare3_polina 1"
        contains:
            "d5_mpol_ref_nmare3_polina_overlay"
    image d5_mpol_ref_nmare3_polina 3 = "locate/Polina/nightmare3/p3.png"
    image d5_mpol_ref_nmare3_polina 4 = "locate/Polina/nightmare3/p4.png"

    image d5_mpol_ref_nmare3_hand 1 = "locate/Polina/nightmare3/hand1.png"
    image d5_mpol_ref_nmare3_hand 2 = "locate/Polina/nightmare3/hand2.png"
    image d5_mpol_ref_nmare3_hand_underlay = "locate/Polina/nightmare3/hand3.png"
    image d5_mpol_ref_nmare3_hand 3 = "locate/Polina/nightmare3/hand4.png"
    image d5_mpol_ref_nmare3_hand_blood = "locate/Polina/nightmare3/blood_trace.png"

    image d5_mpol_ref_nmare3_poltalk_base = "locate/Polina/nightmare3/P00.png"
    image d5_mpol_ref_nmare3_poltalk = "locate/Polina/nightmare3/P01.png"
    image d5_mpol_ref_nmare3_poltalk_2 = "locate/Polina/nightmare3/P02.png"
    image d5_mpol_ref_nmare3_poltalk_eye = "locate/Polina/nightmare3/eye.png"
    image d5_mpol_ref_nmare3_poltalk_bg = "locate/Polina/nightmare3/bgfaer.png"

    image d5_mpol_ref_nmare4_bg = "locate/Polina/nightmare4/bg.png"
    image d5_mpol_ref_nmare4_pol 1 = "locate/Polina/nightmare4/pol1.png"
    image d5_mpol_ref_nmare4_pol 2 = "locate/Polina/nightmare4/pol2.png"
    image d5_mpol_ref_nmare4_pol 3 = "locate/Polina/nightmare4/pol3.png"
    image d5_mpol_ref_nmare4_pol 4 = "locate/Polina/nightmare4/pol4.png"
    image d5_mpol_ref_nmare4_hand_1 = "locate/Polina/nightmare4/h1.png"
    image d5_mpol_ref_nmare4_hand_2 = "locate/Polina/nightmare4/h01.png"
    image d5_mpol_ref_nmare4_hand_3 = "locate/Polina/nightmare4/h001.png"

    image d5_mpol_agony_bg0 = "locate/Polina/agony/fon1.png"
    image d5_mpol_agony_bite_1 = "locate/Polina/agony/bite01.png"
    image d5_mpol_agony_bite_2 = "locate/Polina/agony/bite02.png"
    image d5_mpol_agony_transit = LiveComposite((4344, 2160),
        (0, 0), "locate/Polina/agony/ant0.png",
        (0, 0), "d5_mpol_agony_trans")
    image d5_mpol_agony_base = "locate/Polina/agony/ant_base.png"
    image d5_mpol_agony_base_eyes = LiveComposite((4344, 2160),
        (0, 0), "d5_mpol_agony_base",
        (0, 0), "d5_mpol_agony_eyes")
    image d5_mpol_agony_hand = "locate/Polina/agony/ant1.png"
    image d5_mpol_agony_eyes = "locate/Polina/agony/ant2.png"
    image d5_mpol_agony_trans:
        "d5_mpol_agony_base_eyes"
        alpha 0
        0.75
        linear .5 alpha 1

    image d5_mpol_agony_blood0 = "locate/Polina/agony/blood0.png"
    image d5_mpol_agony_blood1 = "locate/Polina/agony/blood1.png"
    image d5_mpol_agony_blood2 = "locate/Polina/agony/blood2.png"
    image d5_mpol_agony_blood3 = "locate/Polina/agony/blood3.png"
    image d5_mpol_agony_blood4 = "locate/Polina/agony/blood4.png"
    image d5_mpol_agony_blood5 = "locate/Polina/agony/blood5.png"
    image d5_mpol_agony_blood6 = "locate/Polina/agony/blood6.png"
    image d5_mpol_agony_blood7 = "locate/Polina/agony/blood7.png"
    image d5_mpol_agony_blood:
        "d5_mpol_agony_blood1"
        .1
        "d5_mpol_agony_blood2"
        .1
        "d5_mpol_agony_blood3"
        .1
        "d5_mpol_agony_blood4"
        .1
        "d5_mpol_agony_blood5"
        .1
        "d5_mpol_agony_blood6"
        .1
        "d5_mpol_agony_blood7"
        .1
        repeat


    image d5_phone_bg = "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
    image d5_phone_dropped = "locate/home/in_side/1st_floor/hall/h1/prih_001.png"
    image d5_phone_off = "locate/home/in_side/1st_floor/hall/h1/prih_002.png"
    image d5_phone_off2 = "locate/home/in_side/1st_floor/hall/h1/prih_003.png"
    image d5_phone_up = "locate/home/in_side/1st_floor/hall/h1/prih_004.png"

    image d5_phone_na = "locate/police/police-room_blood.png"

    image d5_phone_number = "locate/home/in_side/1st_floor/hall/Tihonov_tel/Tihonov_tel_ru.png"

    image d5_phone_goat = "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/004.jpg"

    image d5_phone_varezhka = "locate/home/in_side/1st_floor/hall/var/var_0.jpg"

    image d5_phone_nonote = "locate/home/in_side/1st_floor/hall/call_art/ff.jpg"
    image d5_phone_photo:
        contains:
            "d4_photo_hand"
        contains:
            "d4_photo_1"
        contains:
            "d4_photo_2"
    image d5_phone_note = "locate/home/in_side/1st_floor/hall/h1/prih_note.png"



    image d5_guests_phantom_dark = "locate/home/in_side/1st_floor/hall/hall_fantom0.png"
    image d5_guests_phantom_light = "locate/home/in_side/1st_floor/hall/hall_fantom1.png"
    image d5_guests_phantom_yes = "locate/home/in_side/1st_floor/hall/hall_fantom2.png"
    image d5_guests_phantom = ConditionSwitch(
        "d5_light == 0", "d5_guests_phantom_dark",
        "d5_light == 1", "d5_guests_phantom_light",
        "d5_light == 2", "d5_guests_phantom_yes",
    )

    image d5_guests_phantom2_dark = "locate/home/in_side/1st_floor/hall/hall_night.png"
    image d5_guests_phantom2_light = "locate/home/in_side/1st_floor/hall/hall01_ivning.png"
    image d5_guests_phantom2_yes = "locate/home/in_side/1st_floor/hall/hall_fantom.png"
    image d5_guests_phantom2 = ConditionSwitch(
        "d5_light == 0", "d5_guests_phantom2_dark",
        "d5_light == 1", "d5_guests_phantom2_light",
        "d5_light == 2", "d5_guests_phantom2_yes",
    )
    image d5_guests_phantom2_52 = "locate/home/in_side/1st_floor/hall/hall_fantom_52.png"

    image d5_guests_kitchen_base = "locate/home/in_side/1st_floor/kitchen/nails/bg1.png"
    image d5_guests_kitchen_table = "locate/home/in_side/1st_floor/kitchen/nails/teble.png"
    image d5_guests_kitchen_nails = "locate/home/in_side/1st_floor/kitchen/nails/nails.png"
    image d5_guests_kitchen_boards1 = "locate/home/in_side/1st_floor/kitchen/nails/boards1.png"
    image d5_guests_kitchen_boards2 = "locate/home/in_side/1st_floor/kitchen/nails/boards2.png"
    image d5_guests_kitchen_boards3 = "locate/home/in_side/1st_floor/kitchen/nails/boards3.png"

    image d5_guests_kitchen_window_full empty = "locate/home/in_side/1st_floor/kitchen/nails/bg2.png"
    image d5_guests_kitchen_window_full eyes = "locate/home/in_side/1st_floor/kitchen/nails/bg3.png"
    image d5_guests_kitchen_window_fg = "locate/home/in_side/1st_floor/kitchen/nails/Window.png"
    image d5_guests_kitchen_window_bg sky = "locate/home/in_side/1st_floor/kitchen/nails/Window_bg.png"
    image d5_guests_kitchen_window_bg eyes = "locate/home/in_side/1st_floor/kitchen/nails/Window_bg2.png"
    image d5_guests_kitchen_window_paws = "locate/home/in_side/1st_floor/kitchen/nails/hands.png"
    image d5_guests_kitchen_window_hand mask = "locate/home/in_side/1st_floor/kitchen/nails/new_bg5.png"
    image d5_guests_kitchen_window_hand empty = "locate/home/in_side/1st_floor/kitchen/nails/new_bg6.png"
    image d5_guests_kitchen_window_light = "locate/home/in_side/1st_floor/kitchen/nails/Window_hands_light.png"

    image d5_mom_kitchen3_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_kitchen_window_bg eyes",
        (0, 0), "d5_guests_kitchen_window_fg",
        (0, 0), "d5_guests_kitchen_window_paws",
        )


    image d5_kitchen_dark = "locate/home/in_side/1st_floor/kitchen/ketcen_dark.jpg"
    image d5_kitchen_dark_boards = "locate/home/in_side/1st_floor/kitchen/ketcen_dark2.png"

    image d5_guests_woodcutter = "locate/home/in_side/1st_floor/hall/sits.png"

    image d5_guests_peephole_fg = "locate/home/in_side/1st_floor/hall/h1/Outside4.png"
    image d5_guests_peephole_bg_pair = "locate/home/in_side/1st_floor/hall/h1/Outside3.jpg"
    image d5_guests_peephole_bg_solo = "locate/home/in_side/1st_floor/hall/h1/Outside5.png"
    image d5_guests_peephole_damper_animation:
        "locate/home/in_side/1st_floor/hall/h1/Outside2.png"
        pos (.5, -.32)
        anchor (.5, .0)
        subpixel True
        transform_anchor True
        linear 1.5 rotate 180

    image d5_guests_hall_stairs_lit = "locate/home/in_side/1st_floor/hall/stairs.png"
    image d5_guests_hall_stairs_dark = "locate/home/in_side/1st_floor/hall/stairs_dark.png"
    image d5_guests_hall_stairs = ConditionSwitch(
        "d5_light == 0", "d5_guests_hall_stairs_dark",
        "d5_light == 1", "d5_guests_hall_stairs_lit",
        "d5_light == 2", "d5_guests_hall_stairs_lit",
        )

    image d5_guests_hall_lit = "d4_home_door_evening"
    image d5_guests_hall_dark = "d4_home_door_dark"
    image d5_guests_hall = ConditionSwitch(
        "d5_light == 0", "d5_guests_hall_dark",
        "d5_light == 1", "d5_guests_hall_lit",
        "d5_light == 2", "d5_guests_hall_lit",
        )

    image d5_guests_hall_evening_dooropen_overlay = "locate/home/in_side/1st_floor/hall/hall01_ivning_overlay.png"
    image d5_guests_polina_lit = "locate/home/in_side/1st_floor/hall/g_polina.png"
    image d5_guests_polina_lit3 = "locate/home/in_side/1st_floor/hall/g_polina3.png"
    image d5_guests_polina_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_polina_lit",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_polina_lit"))
    image d5_guests_polina_dark3 = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_polina_lit3",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_polina_lit3"))
    image d5_guests_polina = ConditionSwitch(
        "d5_light == 0", "d5_guests_polina_dark",
        "d5_light == 1", "d5_guests_polina_lit",
        "d5_light == 2", "d5_guests_polina_lit",
        )
    image d5_guests_polina_nobag_lit = "locate/home/in_side/1st_floor/hall/g_polina2.png"
    image d5_guests_polina_nobag_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_polina_nobag_lit",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_polina_nobag_lit"))
    image d5_guests_polina_nobag = ConditionSwitch(
        "d5_light == 0", "d5_guests_polina_nobag_dark",
        "d5_light == 1", "d5_guests_polina_nobag_lit",
        "d5_light == 2", "d5_guests_polina_nobag_lit",
        )

    image d5_guests_roma_lit = "locate/home/in_side/1st_floor/hall/g_roma.png"
    image d5_guests_roma_lit3 = "locate/home/in_side/1st_floor/hall/g_roma3.png"
    image d5_guests_roma_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_roma_lit",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_roma_lit"))
    image d5_guests_roma_dark3 = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_roma_lit3",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_roma_lit3"))
    image d5_guests_roma = ConditionSwitch(
        "d5_light == 0", "d5_guests_roma_dark",
        "d5_light == 1", "d5_guests_roma_lit",
        "d5_light == 2", "d5_guests_roma_lit",
        )
    image d5_guests_roma_nobag_lit = "locate/home/in_side/1st_floor/hall/g_roma2.png"
    image d5_guests_roma_nobag_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_roma_nobag_lit",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_roma_nobag_lit"))
    image d5_guests_roma_nobag = ConditionSwitch(
        "d5_light == 0", "d5_guests_roma_nobag_dark",
        "d5_light == 1", "d5_guests_roma_nobag_lit",
        "d5_light == 2", "d5_guests_roma_nobag_lit",
        )

    image d5_guests_bag_lit = "locate/home/in_side/1st_floor/hall/backpack.png"
    image d5_guests_bag_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_bag_lit",
        (0, 0), AlphaMask(Solid("#000a"), "d5_guests_bag_lit"))
    image d5_guests_bag = ConditionSwitch(
        "d5_light == 0", "d5_guests_bag_dark",
        "d5_light == 1", "d5_guests_bag_lit",
        "d5_light == 2", "d5_guests_bag_lit",
        )

    image d5_guests_zadush = "locate/home/in_side/1st_floor/hall/zadush.png"

    image d5_guests_hall_close_lit = "locate/home/in_side/1st_floor/hall/Hall_big.jpg"
    image d5_guests_hall_close_dark = "locate/home/in_side/1st_floor/hall/Hall_big_N.png"
    image d5_guests_hall_close = ConditionSwitch(
        "d5_light == 0", "d5_guests_hall_close_dark",
        "d5_light == 1", "d5_guests_hall_close_lit",
        "d5_light == 2", "d5_guests_hall_close_lit",
        )

    image d5_guests_polina_close_lit = "Polina Front b_day_winter 02 serious ahead 03"
    image d5_guests_polina_close_dark = "Polina Front b_day_winter 02 serious ahead 03 dark 70"



    image d5_guests_polina_close = ConditionSwitch(
        "d5_light == 0", "d5_guests_polina_close_dark",
        "d5_light == 1", "d5_guests_polina_close_lit",
        "d5_light == 2", "d5_guests_polina_close_lit",
        )

    image d5_guests_treshold_l1 = "locate/home/out_side/threshold/threshold1.png"
    image d5_guests_treshold_l2 = "locate/home/out_side/threshold/threshold2.png"


    image d5_invite_zhulka normal = "locate/home/in_side/1st_floor/hall/Zulk/normal.png"
    image d5_invite_zhulka angry = "locate/home/in_side/1st_floor/hall/Zulk/angry.png"
    image d5_invite_zhulka happy = "locate/home/in_side/1st_floor/hall/Zulk/happy.png"
    image d5_invite_ruchka = "locate/home/in_side/1st_floor/hall/Zulk/ruchka.png"


    image d5_gfox_base = "locate/home/in_side/1st_floor/hall/Hugs/2/Basa.png"
    image d5_gfox_pol_mouth_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/rot1.png"
    image d5_gfox_rom_mouth_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/1.png"
    image d5_gfox_rom_mouth_2 = "locate/home/in_side/1st_floor/hall/Hugs/2/2.png"

    image d5_gfox_rom_ahead_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/ahead/01.png"
    image d5_gfox_rom_ahead_2 = "locate/home/in_side/1st_floor/hall/Hugs/2/ahead/02.png"
    image d5_gfox_rom_ahead_3 = "locate/home/in_side/1st_floor/hall/Hugs/2/ahead/03.png"
    image d5_gfox_rom_ahead_blink:
        contains transform_blink("d5_gfox_rom_ahead_1", "d5_gfox_rom_ahead_2", "d5_gfox_rom_ahead_3")

    image d5_gfox_rom_aside_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/aside/01.png"
    image d5_gfox_rom_aside_2 = "locate/home/in_side/1st_floor/hall/Hugs/2/aside/02.png"
    image d5_gfox_rom_aside_3 = "locate/home/in_side/1st_floor/hall/Hugs/2/aside/03.png"
    image d5_gfox_rom_aside_blink:
        contains transform_blink("d5_gfox_rom_aside_1", "d5_gfox_rom_aside_2", "d5_gfox_rom_aside_3")

    image d5_gfox_pol_ahead_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/ahead/01.png"
    image d5_gfox_pol_ahead_2 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/ahead/02.png"
    image d5_gfox_pol_ahead_3 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/ahead/03.png"
    image d5_gfox_pol_ahead_blink:
        contains transform_blink("d5_gfox_pol_ahead_1", "d5_gfox_pol_ahead_2", "d5_gfox_pol_ahead_3")

    image d5_gfox_pol_aside_1 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/aside/01.png"
    image d5_gfox_pol_aside_2 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/aside/02.png"
    image d5_gfox_pol_aside_3 = "locate/home/in_side/1st_floor/hall/Hugs/2/p/aside/03.png"
    image d5_gfox_pol_aside_blink:
        contains transform_blink("d5_gfox_pol_aside_1", "d5_gfox_pol_aside_2", "d5_gfox_pol_aside_3")

    layeredimage d5_gfox:
        always "d5_gfox_base"

        group r_eyes:
            attribute r_ahead:
                "d5_gfox_rom_ahead_blink"
            attribute r_aside:
                "d5_gfox_rom_aside_blink"

        group p_eyes:
            attribute p_ahead:
                "d5_gfox_pol_ahead_blink"
            attribute p_aside:
                "d5_gfox_pol_aside_blink"

        group r_mouth:
            attribute r01:
                "d5_gfox_rom_mouth_1"
            attribute r02:
                "d5_gfox_rom_mouth_2"

        always "d5_gfox_pol_mouth_1"






    image d5_gfox_p_aside_r_ahead_dark = AlphaMask(Solid("#0002"), "d5_gfox p_aside r_ahead")

    image d5_gfox_sparks 1 = "sprite/Romka/flame01.png"
    image d5_gfox_sparks 2 = "sprite/Romka/flame02.png"


    image d5_gpolina_base = "locate/home/in_side/1st_floor/hall/Hugs/1/Basa.png"
    image d5_gpolina_base2 = "locate/home/in_side/1st_floor/hall/Hugs/1/Basa2.png"
    image d5_gpolina_mouth = "locate/home/in_side/1st_floor/hall/Hugs/1/2.png"
    image d5_gpolina_eyes_1 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes/01.png"
    image d5_gpolina_eyes_2 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes/02.png"
    image d5_gpolina_eyes_3 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes/03.png"
    image d5_gpolina_eyes:
        animation
        "d5_gpolina_eyes_1"
        choice:
            5
        choice:
            6
        choice:
            7
        "d5_gpolina_eyes_2"
        .1
        "d5_gpolina_eyes_3"
        .1
        "d5_gpolina_eyes_2"
        .1
        repeat

    image d5_gpolina_eyes2_1 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes2/01.png"
    image d5_gpolina_eyes2_2 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes2/02.png"
    image d5_gpolina_eyes2_3 = "locate/home/in_side/1st_floor/hall/Hugs/1/eyes2/03.png"
    image d5_gpolina_eyes2:
        animation
        "d5_gpolina_eyes2_1"
        choice:
            5
        choice:
            6
        choice:
            7
        "d5_gpolina_eyes2_2"
        .1
        "d5_gpolina_eyes2_3"
        .1
        "d5_gpolina_eyes2_2"
        .1
        repeat

    image d5_gpolina_hug idle:
        contains:
            "d5_gpolina_base"
        contains:
            "d5_gpolina_eyes"
    image d5_gpolina_hug talk:
        contains:
            "d5_gpolina_base"
        contains:
            "d5_gpolina_mouth"
        contains:
            "d5_gpolina_eyes"

    image d5_gpolina_hug2 idle:
        contains:
            "d5_gpolina_base2"
        contains:
            "d5_gpolina_eyes2"
    image d5_gpolina_hug2 talk:
        contains:
            "d5_gpolina_base2"
        contains:
            "d5_gpolina_mouth"
        contains:
            "d5_gpolina_eyes2"

    image d5_gpolina_ded = "locate/home/in_side/1st_floor/hall/ded.png"



    image d5_mom_snow_vfx = LiveComposite((1920, 1080),
        (0, 540), SnowBlossom("effect/snow/s011.png", count=80, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear", horizontal=True),
        (0, 540), SnowBlossom("interface/main_meny/partikl_001.png", count=20, yspeed=(-20, 40), xspeed=(-340, -430), border=1, start=0, fast=True, distribution="linear", horizontal=True))

    image d5_mom_dark = "locate/home/in_side/1st_floor/hall/DarkMom.png"
    image d5_mom_snow = "locate/home/in_side/1st_floor/hall/SnowMom.png"

    image d5_mom_hall = "locate/home/in_side/1st_floor/hall/Hall_big_open.png"
    image d5_mom_hall_overlay = "locate/home/in_side/1st_floor/hall/Hall_Big_Open.png"
    image d5_mom_big = "locate/home/in_side/1st_floor/hall/Hall_Big_Open.png"

    image d5_mom_bg = "locate/home/in_side/1st_floor/hall/Fonhallway.png"
    image d5_mom_hug0 = "locate/home/in_side/1st_floor/hall/moml_big0.png"
    image d5_mom_hug1 = "locate/home/in_side/1st_floor/hall/moml_big1.png"
    image d5_mom_hug2 = "locate/home/in_side/1st_floor/hall/moml_big2.png"
    image d5_mom_hug02 = "locate/home/in_side/1st_floor/hall/moml_big02.png"
    image d5_mom_hug3 = "locate/home/in_side/1st_floor/hall/moml_big3.png"

    image d5_mom_ceiling_lit = "locate/home/in_side/1st_floor/hall/ceiling.png"
    image d5_mom_ceiling_dark = "locate/home/in_side/1st_floor/hall/ceiling2.png"
    image d5_mom_ceiling = ConditionSwitch(
        "d5_light == 0", "d5_mom_ceiling_dark",
        "d5_light == 1", "d5_mom_ceiling_lit",
        "d5_light == 2", "d5_mom_ceiling_lit",
        )


    image d5_mom_bunny1_lit = "locate/home/in_side/1st_floor/hall/rabbit.png"
    image d5_mom_bunny1_dark = "locate/home/in_side/1st_floor/hall/rabbit3.png"
    image d5_mom_bunny1 = ConditionSwitch(
        "d5_light == 0", "d5_mom_bunny1_dark",
        "d5_light == 1", "d5_mom_bunny1_lit",
        "d5_light == 2", "d5_mom_bunny1_lit",
        )

    image d5_mom_bunny2 = "locate/home/in_side/1st_floor/hall/rabbit2.png"

    image d5_mom_master1 = "locate/home/in_side/1st_floor/hall/master01.png"

    image d5_mom_master2_lit = "locate/home/in_side/1st_floor/hall/master02.png"
    image d5_mom_master2_dark:
        "d5_mom_master2_lit",
        matrixcolor BrightnessMatrix(-0.3)
    image d5_mom_master2 = ConditionSwitch(
        "d5_light == 0", "d5_mom_master2_dark",
        "d5_light == 1", "d5_mom_master2_lit",
        "d5_light == 2", "d5_mom_master2_lit",
        )

    image d5_mom_kitchen_lit = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_kitchen_base",
        (0, 0), "d5_guests_kitchen_boards1",
        (0, 0), "d5_guests_kitchen_boards2",
        (0, 0), "d5_guests_kitchen_boards3",
        (0, 0), "d5_guests_kitchen_table",
        )
    image d5_mom_kitchen_dark = LiveComposite((1920, 1080),
        (0, 0), "d5_guests_kitchen_window_full empty",
        )

    image d5_mom_kitchen = ConditionSwitch(
        "d5_light == 0", "d5_mom_kitchen_dark",
        "d5_light == 1", "d5_mom_kitchen_lit",
        "d5_light == 2", "d5_mom_kitchen_lit",
        )

    image d5_mom_kitchen2_lit = "locate/home/in_side/1st_floor/kitchen/nails/bg7.png"
    image d5_mom_kitchen2 = ConditionSwitch(
        "d5_light == 0", "d5_guests_kitchen_window_full eyes",
        "d5_light == 1", "d5_mom_kitchen2_lit",
        "d5_light == 2", "d5_mom_kitchen2_lit",
        )

    image d5_mom_kitchen3_lit = "d5_guests_kitchen_window_light"
    image d5_mom_kitchen3 = ConditionSwitch(
        "d5_light == 0", "d5_mom_kitchen3_dark",
        "d5_light == 1", "d5_mom_kitchen3_lit",
        "d5_light == 2", "d5_mom_kitchen3_lit",
        )


    image d5_mom_door = ConditionSwitch(
        "d5_light == 0", "d5_dog_ref_hall open",
        "d5_light == 1", "d5_mom_hall",
        "d5_light == 2", "d5_mom_hall",
        )


    image d5_theycame_axe 1 = "locate/home/in_side/1st_floor/hall/Axereflection.png"
    image d5_theycame_axe 2 = "locate/home/in_side/1st_floor/hall/Axereflection2.png"
    image d5_theycame_axe 3 = "locate/home/in_side/1st_floor/hall/Axereflection3.png"
    image d5_theycame_axe 1 dark = LiveComposite((1920, 1080),
        (0, 0), "d5_theycame_axe 1",
        (0, 0), AlphaMask(Solid("#000a"), "d5_theycame_axe 1"))
    image d5_theycame_axe 2 dark = LiveComposite((1920, 1080),
        (0, 0), "d5_theycame_axe 2",
        (0, 0), AlphaMask(Solid("#000a"), "d5_theycame_axe2"))
    image d5_theycame_axe 3 dark = LiveComposite((1920, 1080),
        (0, 0), "d5_theycame_axe 3",
        (0, 0), AlphaMask(Solid("#000a"), "d5_theycame_axe 3"))

    image d5_theycame_cross_bg = "locate/home/in_side/1st_floor/hall/menti/bg_dark.png"
    image d5_theycame_cross_cross_1 = im.Crop("locate/home/in_side/1st_floor/hall/menti/cross01.png", (0, 0, 1920, 1080))
    image d5_theycame_cross_cross_2 = im.Crop("locate/home/in_side/1st_floor/hall/menti/cross02.png", (0, 0, 1920, 1080))
    image d5_theycame_cross_cross_3 = "locate/home/in_side/1st_floor/hall/menti/cross03.png"
    image d5_theycame_cross_cross_0 = "locate/home/in_side/1st_floor/hall/menti/cross0.png"
    image d5_theycame_cross_cross_11 = "locate/home/in_side/1st_floor/hall/menti/cross01.png"
    image d5_theycame_cross_dust = "locate/home/in_side/1st_floor/hall/menti/dust.png"
    image d5_theycame_cross_ring 1 = "locate/home/in_side/1st_floor/hall/menti/s01.png"
    image d5_theycame_cross_ring 2 = "locate/home/in_side/1st_floor/hall/menti/s02.png"
    image d5_theycame_cross_ring 3 = "locate/home/in_side/1st_floor/hall/menti/s03.png"

    image tupichok_amulet_dark = Composite((1920, 1080),
        (0, 0), "tupichok_amulet",
        (0, 0), AlphaMask(Solid("#0006"), "tupichok_amulet"))


    image d5_faithdiscard_bg = "locate/home/in_side/1st_floor/hall/H1/fon_preh.jpg"
    image d5_faithdiscard_amulet = "locate/home/in_side/1st_floor/hall/Tihonov_tel/h0.png"
    image d5_faithdiscard_hand_1 = "locate/home/in_side/1st_floor/hall/Tihonov_tel/h1.png"
    image d5_faithdiscard_hand_2 = "locate/home/in_side/1st_floor/hall/Tihonov_tel/h2.png"
    image d5_faithdiscard_fg = "locate/home/in_side/1st_floor/hall/Tihonov_tel/h3.png"


    image d5_self_mask 1 = "locate/home/in_side/1st_floor/hall/mask_01.png"
    image d5_self_mask 2 = "locate/home/in_side/1st_floor/hall/mask_02.png"
    image d5_self_friend = "sprite/romka.png"

    image d5_self_mask 1 dark = LiveComposite((1920, 1080),
        (0, 0), "d5_self_mask 1",
        (0, 0), AlphaMask(Solid("#000a"), "d5_self_mask 1"))
    image d5_self_mask 2 dark = LiveComposite((1920, 1080),
        (0, 0), "d5_self_mask 2",
        (0, 0), AlphaMask(Solid("#000a"), "d5_self_mask 2"))

    image showB1f = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_01.png", count=250,  yspeed=(-100, -150), xspeed=(-10, 10), border=50, start=20, fast=True)
    image showB2f = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=200,  yspeed=(-150, -200), xspeed=(-10, 10), border=50, start=15, fast=True)
    image showB3f = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_03.png", count=100,  yspeed=(-200, -250), xspeed=(-10, 10), border=50, start=10, fast=True)

    image d5_self_treat 1 = "locate/home/in_side/1st_floor/hall/h1/treat/01.png"
    image d5_self_treat 2 = "locate/home/in_side/1st_floor/hall/h1/treat/02.png"
    image d5_self_treat 3 = "locate/home/in_side/1st_floor/hall/h1/treat/03.png"
    image d5_self_treat 4 = "locate/home/in_side/1st_floor/hall/h1/treat/04.png"

    image d5_self_reflection closed = "locate/home/in_side/1st_floor/hall/h1/treat/olga.png"
    image d5_self_reflection 1 = "locate/home/in_side/1st_floor/hall/h1/treat/olga_1.png"
    image d5_self_reflection 2 = "locate/home/in_side/1st_floor/hall/h1/treat/olga_2.png"
    image d5_self_reflection 3 = "locate/home/in_side/1st_floor/hall/h1/treat/olga3.png"
    image d5_self_reflection opened = "locate/home/in_side/1st_floor/hall/h1/treat/olga2.png"

    image d5_self_kitchen = "locate/home/in_side/1st_floor/hall/h1/treat/kitchen01.png"
    image d5_self_kitchen_door 1 = "locate/home/in_side/1st_floor/hall/h1/treat/kitchen02.png"
    image d5_self_kitchen_door 2 = "locate/home/in_side/1st_floor/hall/h1/treat/kitchen03.png"

    image d5_self_anya_door 1 = "locate/home/in_side/1st_floor/hall/h1/treat/anya.png"
    image d5_self_anya_door 2 = "locate/home/in_side/1st_floor/hall/h1/treat/anya_2.png"
    image d5_self_anya_door 3 = "locate/home/in_side/1st_floor/hall/h1/treat/anya_3.png"

    image d5_self_anya_corner idle = "locate/home/in_side/1st_floor/hall/h1/treat/Anya01.png"
    image d5_self_anya_corner talk = "locate/home/in_side/1st_floor/hall/h1/treat/Anya02.png"

    image d5_self_anya_fox = "locate/home/in_side/1st_floor/hall/h1/treat/Anya2.png"

    image d5_self_karina 1 = "locate/home/in_side/1st_floor/hall/h1/treat/karina.png"
    image d5_self_karina 2 = "locate/home/in_side/1st_floor/hall/h1/treat/Karina02.png"
    image d5_self_karina 3 = "locate/home/in_side/1st_floor/hall/h1/treat/Karina03.png"

    image d5_self_plita = "locate/home/in_side/1st_floor/hall/h1/treat/plita.png"
    image d5_self_spoon = "locate/home/in_side/1st_floor/hall/h1/treat/spoon.png"
    image d5_self_spoon2 = "locate/home/in_side/1st_floor/hall/h1/treat/spoon2.png"

    image d5_self_floor = "locate/home/in_side/1st_floor/hall/h1/treat/floor.png"
    image d5_self_shadow 1 = "locate/home/in_side/1st_floor/hall/h1/treat/shadow.png"
    image d5_self_shadow 2 = "locate/home/in_side/1st_floor/hall/h1/treat/shadow2.png"

    image d5_self_livingroom = "locate/home/in_side/1st_floor/hall/h1/treat/livingroom.png"
    image d5_self_childbed = "locate/home/in_side/1st_floor/hall/h1/treat/bed.png"
    image d5_self_mask = "locate/Polina/Rom_Dark/Baby/Mask.png"

    image d5_self_shock = "locate/home/in_side/1st_floor/hall/h1/treat/shok.png"

    image d5_self_liv_olya_norm_base = "locate/home/in_side/1st_floor/hall/h1/treat/olya/o.png"
    image d5_self_liv_olya_norm_blink1 = "locate/home/in_side/1st_floor/hall/h1/treat/olya/o2.png"
    image d5_self_liv_olya_norm_blink2 = "locate/home/in_side/1st_floor/hall/h1/treat/olya/o3.png"
    image d5_self_liv_olya norm:
        contains:
            "d5_self_liv_olya_norm_base"
        contains:
            Null()
            3.
            "d5_self_liv_olya_norm_blink1"
            .1
            "d5_self_liv_olya_norm_blink2"
            .1
            "d5_self_liv_olya_norm_blink1"
            .1
            Null()
            5.
            repeat

    image d5_self_liv_olya_shock_base = "locate/home/in_side/1st_floor/hall/h1/treat/olya/ol.png"
    image d5_self_liv_olya_shock_blink1 = "locate/home/in_side/1st_floor/hall/h1/treat/olya/ol2.png"
    image d5_self_liv_olya_shock_blink2 = "locate/home/in_side/1st_floor/hall/h1/treat/olya/ol3.png"
    image d5_self_liv_olya shock:
        contains:
            "d5_self_liv_olya_shock_base"
        contains:
            Null()
            3.
            "d5_self_liv_olya_shock_blink1"
            .1
            "d5_self_liv_olya_shock_blink2"
            .1
            "d5_self_liv_olya_shock_blink1"
            .1
            Null()
            5.
            repeat


    image d5_olya_refuse_base = "locate/home/in_side/1st_floor/hall/death/AxeMurder1.png"
    image d5_olya_refuse_overlay = "locate/home/in_side/1st_floor/hall/death/AxeMurder2.png"

    image d5_olya_refuse_blood:
        blur 4
        "d4_sk_katya_blood_1"
        bd_dt
        "d4_sk_katya_blood_2"
        bd_dt
        "d4_sk_katya_blood_3"
        bd_dt
        "d4_sk_katya_blood_4"
        bd_dt
        "d4_sk_katya_blood_5"
        bd_dt
        "d4_sk_katya_blood_6"
        bd_dt
        "d4_sk_katya_blood_7"
        bd_dt
        "d4_sk_katya_blood_8"
        bd_dt
        "d4_sk_katya_blood_9"
        bd_dt
        "d4_sk_katya_blood_10"
        bd_dt
        "d4_sk_katya_blood_11"
        bd_dt
        "d4_sk_katya_blood_12"
        bd_dt
        "d4_sk_katya_blood_13"
        bd_dt
        "d4_sk_katya_blood_14"
        bd_dt
        "d4_sk_katya_blood_15"
        bd_dt
        "d4_sk_katya_blood_16"
        bd_dt
        "d4_sk_katya_blood_17"
        bd_dt
        "d4_sk_katya_blood_18"
        bd_dt
        "d4_sk_katya_blood_19"
        bd_dt
        "d4_sk_katya_blood_20"
        bd_dt
        "d4_sk_katya_blood_21"
        bd_dt
        "d4_sk_katya_blood_22"
        bd_dt
        "d4_sk_katya_blood_23"
        bd_dt
        "d4_sk_katya_blood_24"
        bd_dt
        Null()


    image d5_roma_back 0 = "locate/home/in_side/1st_floor/hall/Kill_Romka/Rom1.png"
    image d5_roma_back 1 = "locate/home/in_side/1st_floor/hall/Kill_Romka/Rom2.png"
    image d5_roma_back 2 = "locate/home/in_side/1st_floor/hall/Kill_Romka/Rom3.png"

    transform transform_roma_psycho(img, alpha1=1.0, alpha2=1.0):
        contains:
            align (0.5, .5)
            img
            parallel:
                alpha alpha1
                0.25
                alpha (alpha1 * (1 - 0.25) + alpha2 * .25)
                xoffset 200
                .1
                alpha (alpha1 * (1 - 0.35) + alpha2 * .35)
                xoffset -100
                .1
                alpha (alpha1 * (1 - 0.45) + alpha2 * .45)
                xoffset 0
                .25
                alpha (alpha1 * (1 - 0.7) + alpha2 * .7)

                zoom 1.3
                xoffset -100
                .1
                alpha (alpha1 * (1 - 0.8) + alpha2 * .8)

                xoffset 50
                zoom 0.8
                .05
                alpha (alpha1 * (1 - 0.9) + alpha2 * .9)

                xoffset 0
                zoom 1.5
                .1
                alpha alpha2

                xoffset 0
                zoom 1.0


        contains:
            align (0.5, .5)
            img
            block:
                alpha 0.0
                0.25
                alpha 0.5 * alpha1
                xoffset 150
                .1
                xoffset -150
                .1
                alpha 0
                xoffset 0
                .25

                alpha 0.5
                zoom 1.3
                xoffset -200
                .1

                xoffset 150
                zoom 0.8
                .05

                xoffset -50
                zoom 1.5
                .1

                alpha 0.0
                xoffset 0
                zoom 1.0

    image d5_roma_glitch:
        contains transform_roma_psycho("Romka Angry m_day_winter 01 happy ahead 05", 1.0, 0.0)
    image d5_roma_meattron:
        contains transform_roma_psycho("locate/home/in_side/1st_floor/hall/Kill_Romka/Volt.png", 0.0, 1.0)

    image d5_roma_slayer_bg = "locate/home/in_side/1st_floor/hall/Kill_Romka/bg.png"
    image d5_roma_slayer_ant = "locate/home/in_side/1st_floor/hall/Kill_Romka/Ant.png"
    image d5_roma_slayer_axe = "locate/home/in_side/1st_floor/hall/Kill_Romka/Axe.png"
    image d5_roma_slayer_body 1 = "locate/home/in_side/1st_floor/hall/Kill_Romka/Rom01.png"
    image d5_roma_slayer_body 2 = "locate/home/in_side/1st_floor/hall/Kill_Romka/Rom02.png"

    image d5_roma_slayer_polina = "sprite/Polina/Polina_sad.png"


    image d5_polina_slayer = "locate/home/in_side/1st_floor/hall/Kill_Romka/Polina.png"
    image d5_polina_corruption 0 = "locate/home/in_side/1st_floor/hall/Kill_Romka/polin/00.png"
    image d5_polina_corruption_1 = "locate/home/in_side/1st_floor/hall/Kill_Romka/polin/01.png"
    image d5_polina_corruption_2 = "locate/home/in_side/1st_floor/hall/Kill_Romka/polin/02.png"
    image d5_polina_corruption 1:
        "d5_polina_corruption_1"
        .2
        "d5_polina_corruption_2"
        .2
        repeat

    image d5_polina_corruption_bg = "locate/home/in_side/1st_floor/hall/Kill_Romka/polin/bg.png"

    image d5_polina_slayer_roma = "sprite/Romka/Rom_sad2.png"


    image d5_olya_slayer = "locate/home/in_side/1st_floor/hall/Kill_Romka/Olya.png"



    image d5_child_bg = "locate/home/in_side/1st_floor/hall/menti/bg1.png"
    image d5_child_bg_0 = "locate/home/in_side/1st_floor/hall/menti/bg0.png"
    image d5_child_bg_1 a = "locate/home/in_side/1st_floor/hall/menti/bg.png"
    image d5_child_bg_1 b = "locate/home/in_side/1st_floor/hall/menti/0bg.png"

    image d5_child_door 1 = "locate/home/in_side/1st_floor/hall/menti/door1.png"
    image d5_child_door 2 = "locate/home/in_side/1st_floor/hall/menti/door2.png"
    image d5_child_door_dust = "locate/home/in_side/1st_floor/hall/menti/dust.png"

    image d5_child_menti_monsters = "locate/home/in_side/1st_floor/hall/menti/monsters.png"
    image d5_child_menti_m1 = "locate/home/in_side/1st_floor/hall/menti/ment1.png"
    image d5_child_menti_m2 = "locate/home/in_side/1st_floor/hall/menti/ment2.png"

    image d5_child_shock_bg_0 = "locate/home/in_side/1st_floor/hall/menti/bg0_b.png"
    image d5_child_shock_bg_1 a = "locate/home/in_side/1st_floor/hall/menti/bg_a.png"
    image d5_child_shock_bg_1 b = "locate/home/in_side/1st_floor/hall/menti/bg_b.png"
    image d5_child_shock_ment = "locate/home/in_side/1st_floor/hall/menti/ment1_b.png"
    image d5_child_shock_tih = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/Gorelnik/Tih7.png",
        (0, 0), "locate/forest/Gorelnik/Tih11.png",
        )
    image d5_child_shocktalk_tih = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/Gorelnik/Tih7.png",
        (0, 0), "locate/forest/Gorelnik/Tih11.png",
        (0, 0), "locate/forest/Gorelnik/Tih12.png",
        )
    image d5_child_sad_tih = "locate/forest/Gorelnik/Tih10.png"
    image d5_child_sadtalk_tih = LiveComposite((1920, 1080),
        (0, 0), "d5_child_sad_tih",
        (0, 0), "locate/forest/Gorelnik/Tih12.png",
        )

    image d5_child_light = "locate/home/in_side/1st_floor/kitchen/light.png"

    image d5_child_uaz1 = "locate/home/in_side/1st_floor/hall/H1/Uaz_01.png"
    image d5_child_uaz2 = "locate/home/in_side/1st_floor/hall/H1/Uaz_02.png"
    image d5_child_uaz3 = "locate/home/in_side/1st_floor/hall/H1/Uaz_03.png"
    image d5_child_uaz:
        "d5_child_uaz1"
        .1
        "d5_child_uaz2"
        .1
        "d5_child_uaz3"
        .1
        repeat

    image d5_child_police_room = "locate/police/room/room.png"
    image d5_child_police_room2 = "locate/police/room/room2.png"
    image d5_child_police_tih = "locate/police/room/tihonov.png"
    image d5_child_police_tih 2 = "locate/police/room/tihonov 2.png"
    image d5_child_police_tih_closeup = "locate/police/room/tih_closeup.png"
    image d5_child_police_anton = "locate/school/in_side/Anton_class/Anton_04.png"
    image d5_child_police_anton1 = "locate/school/in_side/Anton_class/Anton1.png"
    image d5_child_police_anton_scared = "locate/school/in_side/Anton_class/blink_4.png"
    image d5_child_police_table = "locate/police/room/table.png"
    image d5_child_police_fist = "locate/police/room/fist.png"
    image d5_child_police_drug = "locate/police/room/galaperidol.png"
    image d5_child_police_butsmoke = "locate/police/room/smoke.png"
    image d5_child_police_newspaper = "locate/police/room/gazeta.png"
    image d5_child_police_cigarbut = "locate/police/room/bichok.png"

    image d5_child_police_table_news = LiveComposite((1920, 1080),
        (0, 0), "d5_child_police_table",
        (0, 0), "d5_child_police_newspaper",
    )

    image d5_child_police_flashback = "locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow3.jpg"

    image d5_child_police_fb_semen:
        "locate/school/in_side/Sem_gone/Sem_fin/01.jpg"
        parallel:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat

    image d5_child_police_fb_vova:
        "locate/police/Vova.png"
        parallel:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat

    image d5_child_police_hand full = "sprite/ant/h01.png"
    image d5_child_police_hand empty = "sprite/ant/h02.png"

    image d5_child_police_canibal 1 = "sprite/ant/Kushat09.png"
    image d5_child_police_canibal 2 = "sprite/ant/Kushat10.png"


    image _d5_police_darkshadow = Solid("#0002", xysize = (1920, 1080))

    image _d5_anto_01 = "day3_ant_clas_anton 3"
    image _d5_anto_01_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_01")
    image Ant Suspect 01 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_01",
        (0, 0), "_d5_anto_01_dark")

    image _d5_anto_02 = "d5_child_police_anton"
    image _d5_anto_02_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_02")
    image Ant Suspect 02 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_02",
        (0, 0), "_d5_anto_02_dark")

    image _d5_anto_03 = "d5_child_police_anton1"
    image _d5_anto_03_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_03")
    image Ant Suspect 03 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_03",
        (0, 0), "_d5_anto_03_dark")
    image Ant Suspect 03b = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_03",
        (0, 0), "d5_child_police_anton_scared",
        (0, 0), "_d5_anto_03_dark")
    image Ant Suspect 03c idle = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_03",
        (0, 0), "ant_clas_m5",
        (0, 0), "_d5_anto_03_dark")
    image Ant Suspect 03c talk = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_03",
        (0, 0), "ant_clas_m2",
        (0, 0), "_d5_anto_03_dark")

    image _d5_anto_mouth = "ant_clas_m5"
    image _d5_anto_mouth_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_mouth")
    image d5_child_police_anton_mouth = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_mouth",
        (0, 0), "_d5_anto_mouth_dark")

    image _d5_anto_talk = "ant_clas_m2"
    image _d5_anto_talk_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_talk")
    image d5_child_police_anton_talk = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_talk",
        (0, 0), "_d5_anto_talk_dark")


    image _d5_anto_04 = "Ant ouch 2"
    image _d5_anto_04_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_04")
    image Ant Suspect 04 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_04",
        (0, 0), "_d5_anto_04_dark")


    image _d5_anto_1 = "sprite/ant/anto.png"
    image _d5_anto_1_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_1")
    image Ant Suspect 1 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_1",
        (0, 0), "_d5_anto_1_dark")

    image _d5_anto_2 = "sprite/ant/anto2.png"
    image _d5_anto_2_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_2")
    image Ant Suspect 2 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_2",
        (0, 0), "_d5_anto_2_dark")

    image _d5_anto_3 = "sprite/ant/anto3.png"
    image _d5_anto_3_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_3")
    image Ant Suspect 3 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_3",
        (0, 0), "_d5_anto_3_dark")

    image _d5_anto_4 = "sprite/ant/anto4.png"
    image _d5_anto_4_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_4")
    image Ant Suspect 4 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_4",
        (0, 0), "_d5_anto_4_dark")

    image _d5_anto_5 = "sprite/ant/anto5.png"
    image _d5_anto_5_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_5")
    image Ant Suspect 5 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_5",
        (0, 0), "_d5_anto_5_dark")

    image _d5_anto_6 = "sprite/ant/anton_zamena.png"
    image _d5_anto_6_dark = AlphaMask("_d5_police_darkshadow", "_d5_anto_6")
    image Ant Suspect 6 = LiveComposite((1920, 1080),
        (0, 0), "_d5_anto_6",
        (0, 0), "_d5_anto_6_dark")

    image _d5_anto_9 = "sprite/ant/anto9.png"

    image d5_child_police_smoke_1 = "locate/police/room/001.png"
    image d5_child_police_smoke_2 = "locate/police/room/002.png"
    image d5_child_police_smoke_3 = "locate/police/room/003.png"
    image d5_child_police_smoke_4 = "locate/police/room/004.png"
    image d5_child_police_smoke_5 = "locate/police/room/005.png"
    image d5_child_police_smoke_6 = "locate/police/room/006.png"
    image d5_child_police_smoke_7 = "locate/police/room/007.png"
    image d5_child_police_smoke_8 = "locate/police/room/008.png"
    image d5_child_police_smoke_9 = "locate/police/room/009.png"
    image d5_child_police_smoke_10 = "locate/police/room/010.png"
    image d5_child_police_smoke_11 = "locate/police/room/011.png"
    image d5_child_police_smoke_12 = "locate/police/room/012.png"
    image d5_child_police_smoke_13 = "locate/police/room/013.png"
    image d5_child_police_smoke_14 = "locate/police/room/014.png"
    image d5_child_police_smoke_15 = "locate/police/room/015.png"
    image d5_child_police_smoke_16 = "locate/police/room/016.png"
    image d5_child_police_smoke_17 = "locate/police/room/017.png"
    image d5_child_police_smoke_18 = "locate/police/room/018.png"
    image d5_child_police_smoke_19 = "locate/police/room/019.png"
    image d5_child_police_smoke_20 = "locate/police/room/020.png"
    image d5_child_police_smoke_21 = "locate/police/room/021.png"

    $ dt_child_smoke = 0.15
    $ dt_child_smoke_half = dt_child_smoke*0.5
    image d5_child_police_smoke:
        "d5_child_police_smoke_1" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_2" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_3" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_4" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_5" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_6" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_7" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_8" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_9" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_10" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_11" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_12" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_13" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_14" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_15" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_16" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_17" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_18" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_19" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_20" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        "d5_child_police_smoke_21" with Dissolve(dt_child_smoke_half)
        dt_child_smoke
        repeat

    image d5_child_police_headache_veil:
        "bg_black"
        block:
            linear .02 alpha .85
            linear .02 alpha 1.
            repeat

    image d5_child_psy_building = "locate/psycho/01.png"
    image d5_child_psy_clouds:
        animation
        "locate/psycho/00.png"
        block:
            xpan 0
            linear 60 xpan 360
            repeat
    image d5_child_psy_car = "locate/psycho/tiger.png"

    image d5_child_psy_scene 1 = Composite((1920, 1215),
        (0, 0), "d5_child_psy_clouds",
        (0, 0), "d5_child_psy_building")
    image d5_child_psy_scene 2 = Composite((1920, 1215),
        (0, 0), "d5_child_psy_clouds",
        (0, 0), "d5_child_psy_building",
        (0, 0), "d5_child_psy_car")
    image d5_child_psy_scene 3 = Composite((1920, 1215),
        (0, 0), "d5_child_psy_clouds",
        (0, 0), "d5_child_psy_building",
        (0, 0), "d5_crusade_psy_pair")
    image d5_child_psy_scene 4 = Composite((1920, 1215),
        (0, 0), "d5_child_psy_clouds",
        (0, 0), "d5_child_psy_building",
        (0, 0), "d5_crusade_psy_pair",
        (0, 0), "d5_child_psy_car")

    image d5_child_psy_room = "locate/police/room/durka.png"
    image d5_child_psy_clock = "locate/police/room/cloc.png"
    image d5_child_psy_anton = "locate/police/room/durka_ant.png"
    image d5_child_psy_window = "locate/police/room/window-durka.png"

    image d5_child_flashback_cemetery:


        contains:
            "bg_rep_4_1"
            for_tv_1
        contains:
            "bg_rep_4_2"
            for_tv_1
        contains:
            "bg_rep_3_1"
            for_tv_1
        contains:
            "bg_rep_3_2"
            for_tv_1
        contains:
            "bg_rep_2_1"
            for_tv_1
        contains:
            "bg_rep_2_2"
            for_tv_1
        contains:
            "bg_rep_1_1"
            for_tv_1
        contains:
            "bg_rep_1_2"
            for_tv_1







    image d5_dog_ref_hall closed = "locate/home/in_side/1st_floor/hall/Hall_big_N.png"
    image d5_dog_ref_hall open = "locate/home/in_side/1st_floor/hall/Hall_big_open_N.png"

    image d5_dog_hall_bg = "locate/home/in_side/1st_floor/hall/mirror1.png"
    image d5_dog_hall_1 = "locate/home/in_side/1st_floor/hall/mirror2.png"
    image d5_dog_hall_2 = "locate/home/in_side/1st_floor/hall/mirror3.png"
    image d5_dog_hall_3 = "locate/home/in_side/1st_floor/hall/mirror4.png"
    image d5_dog_hall 1 = Composite((3300, 1080),
        (0, 0), "d5_dog_hall_bg",
        (0, 0), "d5_dog_hall_1")
    image d5_dog_hall 2 = Composite((3300, 1080),
        (0, 0), "d5_dog_hall_bg",
        (0, 0), "d5_dog_hall_2")
    image d5_dog_hall 3 = Composite((3300, 1080),
        (0, 0), "d5_dog_hall_bg",
        (0, 0), "d5_dog_hall_3")

    image d5_dog_ref_bear 1 = "locate/home/in_side/1st_floor/hall/h1/treat/Bear.png"
    image d5_dog_ref_bear 2 = "locate/home/in_side/1st_floor/hall/h1/treat/Bear1.png"
    image d5_dog_ref_bear 3 = "locate/home/in_side/1st_floor/hall/h1/treat/Bear0.png"
    image d5_dog_ref_owl 1 = "locate/home/in_side/1st_floor/hall/h1/treat/Owl.png"
    image d5_dog_ref_owl 2 = "locate/home/in_side/1st_floor/hall/h1/treat/Owl1.png"
    image d5_dog_ref_dog = "locate/home/in_side/1st_floor/hall/h1/treat/dog.png"
    image d5_dog_ref_goat = "locate/home/in_side/1st_floor/hall/h1/treat/Goat.png"
    image d5_dog_ref_fox = "locate/home/in_side/1st_floor/hall/h1/treat/Fox.png"
    image d5_dog_ref_wolf = "locate/home/in_side/1st_floor/hall/h1/treat/Wolf.png"

    image d5_meat_kitchen_nolight = "locate/home/in_side/1st_floor/kitchen/ketcen_nolight.png"
    image d5_meat_kitchen_nolight_planks = "locate/home/in_side/1st_floor/kitchen/ketcen_nolight_planks.png"
    image d5_meat_fridge_nolight_1 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_7.jpg"
    image d5_meat_fridge_nolight_2 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_8.jpg"
    image d5_meat_fridge_nolight_3 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_9.jpg"

    image d5_dog_ref_olya_profile = "sprite/olya/profile_winter.png"
    image d5_dog_ref_olya_profile dark 15 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#0002"), "d5_dog_ref_olya_profile")
        )
    image d5_dog_ref_olya_profile dark 30 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#0004"), "d5_dog_ref_olya_profile")
        )
    image d5_dog_ref_olya_profile dark 40 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#0006"), "d5_dog_ref_olya_profile")
        )
    image d5_dog_ref_olya_profile dark 50 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#0008"), "d5_dog_ref_olya_profile")
        )
    image d5_dog_ref_olya_profile dark 60 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#000a"), "d5_dog_ref_olya_profile")
        )
    image d5_dog_ref_olya_profile dark 70 = Composite((1920, 1080),
        (0, 0), "d5_dog_ref_olya_profile",
        (0, 0), AlphaMask(Solid("#000c"), "d5_dog_ref_olya_profile")
        )

    image d5_meat_fire_1 = "locate/home/out_side/Flame_1.png"
    image d5_meat_fire_2 = "locate/home/out_side/Flame_2.png"
    image d5_meat_fire_3 = "locate/home/out_side/Flame_3.png"
    image d5_meat_fire_03 = "locate/home/out_side/Flame_03.png"
    image d5_meat_fire_4 = "locate/home/out_side/Flame_4.png"

    image d5_meat_fire_flamed_house:
        contains:
            "d5_meat_fire_3"
            subpixel True
            align (.5, .5)
            zoom 1.25
            parallel:
                easein 10 zoom 1.05
            parallel:
                linear .17 xoffset 3 yoffset -6
                linear .17 xoffset 3 yoffset 6
                linear .17 xoffset -3 yoffset -6
                linear .17 xoffset -3 yoffset 6
                repeat
        contains:
            "blizzard_d4_day_far"
            matrixcolor BrightnessMatrix(-0.5)
            parallel:
                ypan 30
                linear 3 ypan -360+30
                repeat

        contains:
            "d5_meat_fire_03"
            subpixel True
            align (.5, .5)
            zoom 1.25
            parallel:
                easein 10 zoom 1.05
            parallel:
                linear .17 xoffset 3 yoffset -6
                linear .17 xoffset 3 yoffset 6
                linear .17 xoffset -3 yoffset -6
                linear .17 xoffset -3 yoffset 6
                repeat
        contains:
            "blizzard_d5_day2"
            matrixcolor BrightnessMatrix(-0.5)
        contains:
            "blizzard_d4_day_near"
            matrixcolor BrightnessMatrix(-0.5)
            parallel:
                ypan 0
                linear 3 ypan -360
                repeat
            parallel:
                xpan 0
                linear 5 xpan -360
                repeat

    image d5_meat_goat = "locate/home/out_side/Flame/goat.png"
    image d5_meat_owl = "locate/home/out_side/Flame/owl.png"
    image d5_meat_fox = "locate/home/out_side/Flame/fox.png"
    image d5_meat_bear = "locate/home/out_side/Flame/bear.png"
    image d5_meat_wolf = "locate/home/out_side/Flame/wolf.png"
    image d5_meat_flame = "locate/home/out_side/Flame/hOUSE05.png"

    image d5_runaway_bg = "locate/forest/runaway/runaway_night/0002.jpg"
    image d5_runaway_anton = "locate/forest/runaway/runaway_night/anton/run_away_005.png"

    image d5_meat_runaway_bg:
        contains:
            "locate/forest/runaway/runaway_night/0002.jpg"
        contains:
            "day3_night_run_bg1"
        contains:
            "day3_night_run_bg2"
    image d5_meat_runaway_anton:
        "locate/forest/runaway/runaway_night/anton/run_away_006.png"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset -22 yoffset -72
            linear 0.2 xoffset -122 yoffset -152
            linear 0.2 xoffset -50 yoffset -130
            linear 0.2 xoffset -122 yoffset -172
            repeat
        parallel:
            block:
                linear .05 xpos 0.51
                linear .05 xpos 0.49
                repeat 4
            2.0
            repeat

    image d5_meat_polya_bg_base = "locate/home/out_side/fon_trap.png"
    image d5_meat_polya_beasts 1 = "locate/home/out_side/b001.png"
    image d5_meat_polya_beasts 2 = "locate/home/out_side/b002.png"
    image d5_meat_polya_olya base = "locate/home/out_side/olya.png"
    image d5_meat_polya_polina base = "locate/home/out_side/polina.png"
    image d5_meat_polya_olya_hover_img = "locate/home/out_side/olya_hover.png"
    image d5_meat_polya_polina_hover_img = "locate/home/out_side/polina_hover.png"

    image d5_meat_polya_olya_hover:
        "d5_meat_polya_olya_hover_img"
        matrixcolor BrightnessMatrix(0.10)

    image d5_meat_polya_polina_hover:
        "d5_meat_polya_polina_hover_img"
        matrixcolor BrightnessMatrix(0.10)

    default d5_polya_polina_hover = False
    default d5_polya_olya_hover = False

    image d5_meat_polya_olya choice = ConditionSwitch(
        "d5_polya_olya_hover", "d5_meat_polya_olya_hover",
        True, "d5_meat_polya_olya base"
    )
    image d5_meat_polya_polina choice = ConditionSwitch(
        "d5_polya_polina_hover", "d5_meat_polya_polina_hover",
        True, "d5_meat_polya_polina base"
    )

    define d5_snow_polina_offset = 200
    define d5_snow_olya_offset = -200
    define d5_snow_polina_xalign = 0.20
    define d5_snow_olya_xalign = 0.75
    define d5_snow_mid_align = 0.5
    image d5_meat_polya_bg 0 = LiveComposite((3840, 1080),
        (0, 0), "d5_meat_polya_bg_base",
        )
    image d5_meat_polya_bg 1 = LiveComposite((3840, 1080),
        (0, 0), "d5_meat_polya_bg_base",
        (0, 0), "d5_meat_polya_beasts 1",
        )
    image d5_meat_polya_bg 2 = LiveComposite((3840, 1080),
        (0, 0), "d5_meat_polya_bg_base",
        (0, 0), "d5_meat_polya_beasts 2",
        )

    image d5_meat_polya_girls = LiveComposite((3840, 1080),
        (d5_snow_olya_offset, 0), "d5_meat_polya_olya base",
        (d5_snow_polina_offset, 0), "d5_meat_polya_polina base"
        )
    image d5_meat_polya_olya:
        "d5_meat_polya_olya_base"
        xoffset d5_snow_olya_offset
    image d5_meat_polya_polina:
        "d5_meat_polya_polina_base"
        xoffset d5_snow_polina_offset

































    image d5_meat_post_bg_base = "locate/home/out_side/Meet_beasts/wood/pole4.png"
    image d5_meat_post_obstacle = "locate/home/out_side/Meet_beasts/wood/pole_stolb.png"
    image d5_meat_post_bg = LiveComposite((1920, 2531),
        (0, 0), "d5_meat_post_bg_base",
        (0, 0), "d5_meat_post_obstacle")


    image d5_meata_roof_debris1 = "locate/home/in_side/1st_floor/hall/death/0002.png"
    image d5_meata_roof_debris2 = "locate/home/in_side/1st_floor/hall/death/0002_2.png"
    image d5_meata_roof 1 = "locate/home/in_side/1st_floor/hall/death/001.png"
    image d5_meata_roof 2 = "locate/home/in_side/1st_floor/hall/death/002.png"
    image d5_meata_roof_3 = "locate/home/in_side/1st_floor/hall/death/003.png"
    image d5_meata_roof 4 = "locate/home/in_side/1st_floor/hall/death/004.png"
    image d5_meata_roof 5 = "locate/home/in_side/1st_floor/hall/death/005.png"
    image d5_meata_roof 5_2 = "locate/home/in_side/1st_floor/hall/death/005_2.png"
    image d5_meata_roof 6 = "locate/home/in_side/1st_floor/hall/death/006.png"
    image d5_meata_roof 7 = "locate/home/in_side/1st_floor/hall/death/007.png"
    image d5_meata_roof 8 = "locate/home/in_side/1st_floor/hall/death/008.png"

    image d5_meata_death_sky = "locate/home/in_side/1st_floor/hall/death/sky.png"
    image d5_meata_death_hand = "locate/home/in_side/1st_floor/hall/death/hand.png"
    image d5_meata_death_wall1 = "locate/home/in_side/1st_floor/hall/death/wall01.png"
    image d5_meata_death_wall2 = "locate/home/in_side/1st_floor/hall/death/wall02.png"

    image d5_meata_death_fox 1 = "locate/home/in_side/1st_floor/hall/death/Fox_1.png"
    image d5_meata_death_fox 2 = "locate/home/in_side/1st_floor/hall/death/Fox_6.png"
    image d5_meata_death_fox_claw = "locate/home/in_side/1st_floor/hall/death/003.png"
    image d5_meata_death_fox_hand 1 = "locate/home/in_side/1st_floor/hall/death/Fox_2.png"
    image d5_meata_death_fox_hand 2 = "locate/home/in_side/1st_floor/hall/death/Fox_3.png"
    image d5_meata_death_fox_hand 3 = "locate/home/in_side/1st_floor/hall/death/Fox_4.png"
    image d5_meata_death_fox_hand 4 = "locate/home/in_side/1st_floor/hall/death/Fox_5.png"

    image d5_meata_death_wolf = "locate/home/in_side/1st_floor/hall/death/Woolf_1.png"
    image d5_meata_death_wolf_hand = "locate/home/in_side/1st_floor/hall/death/Woolf_2.png"

    image d5_ending_canned_food_title_background 1 = "end/end_fox/001.png"
    image d5_ending_canned_food_title_background 2 = "end/end_fox/002.png"
    image d5_ending_canned_food_title_background 3 = "end/end_fox/003.png"





    image d5_polya_olya_away_2 = "locate/home/out_side/olya2.png"
    image d5_polya_olya_away_3 = "locate/home/out_side/olya3.png"
    image d5_polya_olya_away_4 = "locate/home/out_side/olya4.png"
    image d5_polya_olya_away_5 = "locate/home/out_side/olya5.png"
    image d5_polya_olya_away_6 = "locate/home/out_side/olya6.png"
    image d5_polya_olya_away_7 = "locate/home/out_side/olya7.png"
    image d5_polya_olya_away_8 = "locate/home/out_side/olya8.png"
    image d5_polya_olya_away_9 = "locate/home/out_side/olya9.png"
    image d5_polya_olya_away_10 = "locate/home/out_side/olya10.png"
    image d5_polya_olya_away_11 = "locate/home/out_side/olya11.png"
    image d5_polya_olya_away_12 = "locate/home/out_side/olya12.png"


    image d5_polya_olya_away_2_12:
        "d5_polya_olya_away_2"
        .1
        "d5_polya_olya_away_3"
        .1
        "d5_polya_olya_away_4"
        .1
        "d5_polya_olya_away_5"
        .1
        "d5_polya_olya_away_6"
        .1
        "d5_polya_olya_away_7"
        .1
        "d5_polya_olya_away_8"
        .1
        "d5_polya_olya_away_9"
        .1
        "d5_polya_olya_away_10"
        .1
        "d5_polya_olya_away_11"
        .1
        "d5_polya_olya_away_12" with Dissolve(1.)


    image d5_mopoam_bg = "locate/cemetery/amulet/bg.png"
    image d5_mopoam_ant = "locate/cemetery/amulet/Ant.png"
    image d5_mopoam_oly = "locate/cemetery/amulet/Oly.png"
    image d5_mopoam_pol = "locate/cemetery/amulet/Pol.png"
    image d5_mopoam_branch 1 = "locate/cemetery/amulet/01.png"
    image d5_mopoam_branch 2 = "locate/cemetery/amulet/02.png"
    image d5_mopoam_branch_overlay = "locate/cemetery/amulet/03.png"
    image d5_mopoam_neclace 1 = "locate/cemetery/amulet/00.png"
    image d5_mopoam_neclace 2 = "locate/cemetery/amulet/002.png"
    image d5_mopoam_shadow = "locate/cemetery/amulet/shadow.png"

    image d5_mopoam_toha_ant_base = "locate/school/out_side/school_coner/defense/Amulet5.png"
    image d5_mopoam_toha_ant = Composite((1920, 1080),
        (0, 0), "d5_mopoam_toha_ant_base",
        (0, 0), AlphaMask(Solid("#0009"), "d5_mopoam_toha_ant_base"))

    image d5_mopoam_vision = Movie(play="video/blood.webm")

    image d5_mopoam_oly neu = "locate/cemetery/amulet/Oly.png"
    image d5_mopoam_oly alt = "locate/cemetery/amulet/Oly2.png"

    image d5_mopoam_hand_amulet_base = "locate/forest/amulet.png"
    image d5_mopoam_hand amulet = LiveComposite((1920, 1080),
        (0, 0), "d5_mopoam_hand_amulet_base",
        (0, 0), AlphaMask(Solid("#0009"), "d5_mopoam_hand_amulet_base"))
    image d5_mopoam_hand_empty_base = "locate/forest/amulet_no.png"
    image d5_mopoam_hand empty = LiveComposite((1920, 1080),
        (0, 0), "d5_mopoam_hand_empty_base",
        (0, 0), AlphaMask(Solid("#0009"), "d5_mopoam_hand_empty_base"))


    image d5_blood = "locate/blood.png"

    image d5_over_head 1 = "d4_blood_head"
    image d5_over_head 2 = "d4_blood_head2"
    image d5_over_head 3 = "d4_blood_head 3"

    image d5_overol_blood1 = "locate/forest/Olyas_death/blood1.png"
    image d5_overol_blood2 = "locate/forest/Olyas_death/blood2.png"

    image d5_overol_hand = "locate/forest/Olyas_death/hand.png"
    image d5_overol_olya = "locate/forest/Olyas_death/olya.png"

    image d5_overol_fox 0 = "locate/forest/Olyas_death/fox0.png"
    image d5_overol_fox 1 = "locate/forest/Olyas_death/fox1.png"
    image d5_overol_fox 2 = "locate/forest/Olyas_death/fox2.png"

    image d5_overol_owl 0 = "locate/forest/Olyas_death/owl_0.png"
    image d5_overol_owl 1 = "locate/forest/Olyas_death/owl_1.png"
    image d5_overol_owl 2 = "locate/forest/Olyas_death/owl_2.png"
    image d5_overol_owl 3 = "locate/forest/Olyas_death/owl_3.png"
    image d5_overol_owl 4 = "locate/forest/Olyas_death/owl_4.png"

    image d5_overol_owl idle:
        "d5_overol_owl 4"
        block:
            .3
            "d5_overol_owl 2"
            .3
            "d5_overol_owl 4"
            3.
            repeat


    image d5_overol_bg = "locate/forest/Olyas_death/fon.png"
    image d5_overol_snowpile = "locate/forest/Olyas_death/fon_2.png"

    image d5_overol_bg 1 = LiveComposite((1920, 1482),
        (0, 0), "d5_overol_bg",
        (0, 0), "d5_overol_blood1",
        (0, 0), "d5_overol_olya",
    )
    image d5_overol_bg 2 = LiveComposite((1920, 1482),
        (0, 0), "d5_overol_bg",
        (0, 0), "d5_overol_blood1",
        (0, 0), "d5_overol_blood2",
        (0, 0), "d5_overol_olya",
    )

    image d5_overal_owl_pov = "locate/forest/Olyas_death/Olyadies.png"
    image d5_overal_owl_pov2 = "locate/forest/Olyas_death/Olyadies2.png"

    image d5_overol_kidnap_bg = "locate/home/out_side/Owl2/bg.png"
    image d5_overol_kidnap_oly 1 = "locate/home/out_side/Owl2/Ol1.png"
    image d5_overol_kidnap_oly 2 = "locate/home/out_side/Owl2/Ol2.png"
    image d5_overol_kidnap_oly 3 = "locate/home/out_side/Owl2/Ol3.png"
    image d5_overol_kidnap_oly 4 = "locate/home/out_side/Owl2/Ol4.png"
    image d5_overol_kidnap_oly 5 = "locate/home/out_side/Owl2/Ol5.png"
    image d5_overol_kidnap_oly 6 = "locate/home/out_side/Owl2/Ol6.png"
    image d5_overol_kidnap_oly 7 = "locate/home/out_side/Owl2/Ol7.png"
    image d5_overol_kidnap_oly 8 = "locate/home/out_side/Owl2/Ol8.png"

    image d5_overol_kidnap_anton 1 = "locate/forest/the_killers/polin/Ant0.png"
    image d5_overol_kidnap_anton 2 = "locate/forest/the_killers/polin/Ant1.png"
    image d5_overol_kidnap_anton 3 = "locate/forest/the_killers/polin/Ant2.png"
    image d5_overol_kidnap_anton 4 = "locate/forest/the_killers/polin/Ant3.png"
    image d5_overol_kidnap_anton_hand = "locate/home/out_side/Owl2/heand.png"

    image d5_overal_roma_bg = "locate/forest/romka/bg.png"
    image d5_overal_roma_body = "locate/forest/romka/rom.png"
    image d5_overal_roma_head = "locate/forest/romka/rom2.png"

    image d5_over_catch = "locate/cemetery/Catch0.png"

    image d5_overol_catch = "locate/cemetery/CatchA.png"


    image d5_overnool_roma = "locate/forest/romka/rom.png"
    image d5_overnool_roma_head = "locate/forest/romka/rom2.png"
    image d5_overnool_pol 1 = "locate/forest/Olyas_death/Openair0.png"
    image d5_overnool_pol 2 = "locate/forest/Olyas_death/Openair01.png"
    image d5_overnool_pol 3 = "locate/forest/Olyas_death/Openair02.png"
    image d5_overnool_pol_fg = "locate/forest/Olyas_death/Openair02_fg.png"

    image d5_overnool_blood_animation:
        "d4_sk_katya_blood_1"
        bd_dt
        "d4_sk_katya_blood_2"
        bd_dt
        "d4_sk_katya_blood_3"
        bd_dt
        "d4_sk_katya_blood_4"
        bd_dt
        "d4_sk_katya_blood_5"
        bd_dt
        "d4_sk_katya_blood_6"
        bd_dt
        "d4_sk_katya_blood_7"
        bd_dt
        "d4_sk_katya_blood_8"
        bd_dt
        "d4_sk_katya_blood_9"
        bd_dt
        "d4_sk_katya_blood_10"
        bd_dt
        "d4_sk_katya_blood_11"
        bd_dt
        "d4_sk_katya_blood_12"
        bd_dt
        "d4_sk_katya_blood_13"
        bd_dt
        "d4_sk_katya_blood_14"
        bd_dt
        "d4_sk_katya_blood_15"
        bd_dt
        "d4_sk_katya_blood_16"
        bd_dt
        "d4_sk_katya_blood_17"
        bd_dt
        "d4_sk_katya_blood_18"
        bd_dt
        "d4_sk_katya_blood_19"
        bd_dt
        "d4_sk_katya_blood_20"
        bd_dt
        "d4_sk_katya_blood_21"
        bd_dt
        "d4_sk_katya_blood_22"
        bd_dt
        "d4_sk_katya_blood_23"
        bd_dt
        "d4_sk_katya_blood_24"
        bd_dt
        Null()
        choice:
            2.
        choice:
            2.5
        choice:
            2.3
        repeat

    image d5_overnool_bear 1 = "locate/forest/Olyas_death/bear1.png"
    image d5_overnool_bear 2 = "locate/forest/Olyas_death/bear2.png"
    image d5_overnool_bear 3 = "locate/forest/Olyas_death/bear3.png"

    image d5_overnool_catch = "locate/cemetery/CatchB.png"



    image d5_1890_cry1 = "images/sprite/Ant/Cry.png"
    image d5_1890_cry2 = "images/sprite/Ant/Cry2.png"
    image d5_1890_cry3 = "images/sprite/Ant/Cry3.png"

    image d5_1890_cry:
        "d5_1890_cry1"
        .1
        "d5_1890_cry2"
        .1
        "d5_1890_cry3"
        .1
        repeat

    image d5_1890_cry_anton = "images/sprite/Ant/Cry_ant.png"
    image d5_1890_cry_anton_dark_overlay = AlphaMask(Solid("#000"), "d5_1890_cry_anton")

    image d5_1890_mirror_bg = "locate/home/in_side/1st_floor/hall/H1/Mirrow00.png"
    image d5_1890_mirror_ant = "locate/home/in_side/1st_floor/hall/H1/Mirrow_Ant.png"
    image d5_1890_mirror_reflect 1 = "locate/home/in_side/1st_floor/hall/H1/Mirrow_01.png"
    image d5_1890_mirror_reflect 2 = "locate/home/in_side/1st_floor/hall/H1/Mirrow_02.png"

    image d5_1890_eye_1 = "locate/home/in_side/2st_floor/olga_room/eye/001.png"
    image d5_1890_eye_2 = "locate/home/in_side/2st_floor/olga_room/eye/002.png"
    image d5_1890_eye_3 = "locate/home/in_side/2st_floor/olga_room/eye/003.png"
    image d5_1890_eye_4 = "locate/home/in_side/2st_floor/olga_room/eye/004.png"
    image d5_1890_eye_5 = "locate/home/in_side/2st_floor/olga_room/eye/005.png"
    image d5_1890_eye_6 = "locate/home/in_side/2st_floor/olga_room/eye/006.png"
    image d5_1890_eye_7 = "locate/home/in_side/2st_floor/olga_room/eye/007.png"
    image d5_1890_eye_8 = "locate/home/in_side/2st_floor/olga_room/eye/008.png"
    image d5_1890_eye_9 = "locate/home/in_side/2st_floor/olga_room/eye/009.png"
    image d5_1890_eye_10 = "locate/home/in_side/2st_floor/olga_room/eye/010.png"
    image d5_1890_eye_11 = "locate/home/in_side/2st_floor/olga_room/eye/011.png"
    image d5_1890_eye_12 = "locate/home/in_side/2st_floor/olga_room/eye/012.png"
    image d5_1890_eye_13 = "locate/home/in_side/2st_floor/olga_room/eye/013.png"

    define eye_dt = 0.1

    image d5_1890_eye_open:
        alpha 0

        "d5_1890_eye_1"

        linear .5 alpha 1

        "d5_1890_eye_2"
        eye_dt
        "d5_1890_eye_3"
        eye_dt
        "d5_1890_eye_4"
        eye_dt
        "d5_1890_eye_5"
    image d5_1890_eye_idle:
        "d5_1890_eye_6"
        eye_dt
        "d5_1890_eye_7"
        eye_dt
        "d5_1890_eye_8"
        eye_dt
        "d5_1890_eye_9"
        eye_dt
        "d5_1890_eye_10"
        eye_dt
        "d5_1890_eye_11"
        eye_dt
        "d5_1890_eye_12"
        eye_dt
        "d5_1890_eye_13"
        eye_dt
        repeat
    image d5_1890_eye_close:
        "d5_1890_eye_5"
        eye_dt
        "d5_1890_eye_4"
        eye_dt
        "d5_1890_eye_3"
        eye_dt
        "d5_1890_eye_2"
        eye_dt
        "d5_1890_eye_1"
        linear .5 alpha 0
    image d5_1890_eye_animation:
        Null()

        block:
            choice:
                zoom 0.8
            choice:
                zoom 0.9
            choice:
                zoom 1.0
            choice:
                zoom 1.4
            choice:
                zoom 1.4
            choice:
                zoom 1.4

        parallel:
            choice:
                linear 0.05 xoffset 2
                linear 0.05 xoffset -2
            choice:
                linear 0.05 xoffset 3
                linear 0.05 xoffset -3
            choice:
                linear 0.05 xoffset 5
                linear 0.05 xoffset -5
            repeat

        parallel:
            block:
                choice:
                    0.13
                choice:
                    .37
                choice:
                    .61
            block:
                choice:
                    0.13
                choice:
                    .37
                choice:
                    .61
            block:
                choice:
                    0.13
                choice:
                    .37
                choice:
                    .61
            choice:
                yoffset 0
            choice:
                yoffset 0

            choice:
                yoffset -150
                block:
                    ease 1 yoffset 150
                    ease 1 yoffset -150
                    repeat

            choice:
                yoffset 150
                block:
                    ease 1 yoffset -150
                    ease 1 yoffset 150
                    repeat

            choice:
                yoffset -50
                block:
                    ease 1 yoffset 50
                    ease 1 yoffset -50
                    repeat

            choice:
                yoffset 50
                block:
                    ease 1 yoffset -50
                    ease 1 yoffset 50
                    repeat

        parallel:
            block:
                choice 7:
                    1.
                choice 5:
                    3.
                choice 3:
                    5.
                choice 1:
                    7.

            block:
                choice:
                    0.13
                choice:
                    .37
                choice:
                    .61

            "d5_1890_eye_open"
            0.5 + eye_dt*4

            "d5_1890_eye_idle"
            block:
                choice:
                    eye_dt*8 *1
                choice:
                    eye_dt*8 *2
                choice:
                    eye_dt*8 *3

            "d5_1890_eye_close"
            0.5 + eye_dt*4
            Null()

            repeat

    image d5_1890_nightmare:
        "locate/school/in_side/Sem_gone/f_01.jpg"
        .1
        "locate/school/in_side/Sem_gone/f_02.jpg"
        .1
        "locate/school/in_side/Sem_gone/f_03.jpg"
        .1
        "locate/school/in_side/Sem_gone/f_04.jpg"
        .1
        "locate/school/in_side/Sem_gone/f_05.jpg"
        .1
        repeat

    image d5_1890_round_0:
        "d5_1890_nightmare"
    image d5_1890_round 1:
        animation
        contains:
            "d5_1890_nightmare"
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.728, .327)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.203, .016)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.938, .768)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.110, .467)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.351, .439)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.272, .353)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.676, .2779)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.194, .005)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.796, .678)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.913, .961)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.096, .571)
        contains:
            "d5_1890_eye_animation"
            anchor (.5, .5)
            pos (.978, .652)

    image d5_1890_prut_animation:
        contains:
            "prut_bg"
        contains:
            "prut_ment"
        contains:
            "prut_prut"

    image d5_1890_carry_olya2 = "locate/home/in_side/1st_floor/hall/Ant_Ol2.png"
    image d5_1890_carry_olya = "locate/home/in_side/1st_floor/hall/Ant_Olya.png"
    image d5_1890_carry_olya3 = "locate/home/in_side/1st_floor/hall/H1/Ant_Ol.png"

    image d5_1890_carry_olya_shade = AlphaMask(Solid("#000"), "d5_1890_carry_olya")
    image d5_1890_carry_olya_in_dark = Composite((1920, 1080),
        (0, 0), "d5_1890_carry_olya",
        (0, 0), AlphaMask(Solid("#000b"), "d5_1890_carry_olya"))

    image d5_1890_carry_olya4:
        contains:
            "d5_1890_carry_olya"
        contains:
            "d5_1890_carry_olya_shade"
            alpha 0.4

    image d5_1890_carry_beasts = "locate/home/in_side/1st_floor/hall/H1/beasts.png"

    image d5_1890_flay_bg = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/bg.png"
    image d5_1890_flay_body = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/body.png"
    image d5_1890_flay_head:
        animation
        "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/Head.png"
        subpixel True
        transform_anchor True
        align (.555, .100)
        parallel:
            rotate 15
            ease 3. rotate -15
            ease 3. rotate 15
            repeat
    image d5_1890_flay_blood_1 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/b01.png"
    image d5_1890_flay_blood_2 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/b02.png"
    image d5_1890_flay_meat_1 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/m01.png"
    image d5_1890_flay_meat_2 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/m02.png"
    image d5_1890_flay_meat_3 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/m03.png"
    image d5_1890_flay_meat_4 = "locate/home/in_side/1st_floor/hall/H1/Olya_flaying/m04.png"

    image d5_1890_kushat_blood = "sprite/Ant/blood.png"
    image d5_1890_kushat 0 = "sprite/Ant/Kushat00.png"
    image d5_1890_kushat 1 = "sprite/Ant/Kushat01.png"
    image d5_1890_kushat 2 = "sprite/Ant/Kushat02.png"
    image d5_1890_kushat 3 = "sprite/Ant/Kushat03.png"
    image d5_1890_kushat 4 = "sprite/Ant/Kushat04.png"
    image d5_1890_kushat 5 = "sprite/Ant/Kushat05.png"
    image d5_1890_kushat 6 = "sprite/Ant/Kushat06.png"
    image d5_1890_kushat_overlay 1 = "sprite/Ant/Kushat07.png"
    image d5_1890_kushat_overlay 2 = "sprite/Ant/Kushat08.png"

    image d5_1890_kushat 00 = "sprite/Ant/Kushat_00.png"
    image d5_1890_kushat 01 = "sprite/Ant/Kushat_01.png"
    image d5_1890_kushat 02 = "sprite/Ant/Kushat_02.png"
    image d5_1890_kushat 03 = "sprite/Ant/Kushat_03.png"
    image d5_1890_kushat 02_loop:
        "d5_1890_kushat 02"
        .2
        block:
            "d5_1890_kushat 03" with Dissolve(.1)
            .2
            "d5_1890_kushat 02" with Dissolve(.1)
            .2
            repeat

    image d5_1890_kushat_cry_base:
        "d5_1890_kushat 5"
        .1
        "d5_1890_kushat 6"
        .1
        repeat
    image d5_1890_kushat_cry:
        contains:
            "d5_1890_kushat_cry_base"
        contains:
            "d5_1890_kushat_overlay 2"

    image d5_1890_kushat eager:
        contains:
            "d5_1890_kushat 1"
        contains:
            "d5_1890_kushat_overlay 1"
        contains:
            "d5_1890_kushat_overlay 2"

    image d5_1890_kushat laugh:
        contains:
            "d5_1890_kushat 2"
        contains:
            "d5_1890_kushat_overlay 2"
        contains:
            "d5_1890_kushat_blood"

    image d5_1890_feast1_bg = "locate/home/in_side/1st_floor/hall/h1/fonA.png"
    image d5_1890_feast1_ant = "sprite/Ant/a1.png"
    image d5_1890_feast1_shadow = "sprite/Ant/a0.png"
    image d5_1890_feast1_alis = "d4_paw_wolf_body"

    image d5_1890_feast1_f1 = "locate/polina/polin_yard/anton/A01.png"
    image d5_1890_feast1_f2 = "locate/polina/polin_yard/anton/A02.png"
    image d5_1890_feast1_f3 = "locate/polina/polin_yard/anton/A03.png"
    image d5_1890_feast1_f:
        "d5_1890_feast1_f1"
        .1
        "d5_1890_feast1_f2"
        .1
        "d5_1890_feast1_f3"
        .1
        repeat

    image d5_handblood_left_d = AlphaMask(Solid("#0008"), "handblood_left")
    image d5_handblood_left = Composite((1920, 1080),
        (0, 0), "handblood_left",
        (0, 0), "d5_handblood_left_d")
    image d5_handblood_right_d = AlphaMask(Solid("#0008"), "handblood_right")
    image d5_handblood_right = Composite((1920, 1080),
        (0, 0), "handblood_right",
        (0, 0), "d5_handblood_right_d")

    image d5_1890_guts_bg = "locate/home/in_side/1st_floor/hall/h1/fonk.png"
    image d5_1890_guts_g = "locate/home/in_side/1st_floor/hall/h1/k.png"
    image d5_1890_guts_drops = "locate/home/in_side/1st_floor/hall/h1/k2.png"

    image d5_1890_parents_bg = "locate/home/in_side/1st_floor/hall/h1/p_fon.png"
    image d5_1890_parents_father = "locate/home/in_side/1st_floor/hall/h1/Baty.png"
    image d5_1890_parents_mother = "locate/home/in_side/1st_floor/hall/h1/Karina.png"

    image d5_1890_dadfin 0 = "sprite/dad/fin/00.png"
    image d5_1890_dadfin 1 = "sprite/dad/fin/01.png"
    image d5_1890_dadfin 2 = "sprite/dad/fin/02.png"
    image d5_1890_dadfin 3 = "sprite/dad/fin/03.png"
    image d5_1890_dadfin 4 = "sprite/dad/fin/04.png"
    image d5_1890_dadfin 5 = "sprite/dad/fin/05.png"
    image d5_1890_dadfin 6 = "sprite/dad/fin/06.png"
    image d5_1890_dadfin 7 = "sprite/dad/fin/07.png"
    image d5_1890_dadfin 8 = "sprite/dad/fin/08.png"
    image d5_1890_dadfin 9 = "sprite/dad/fin/09.png"
    image d5_1890_dadfin 10 = "sprite/dad/fin/10.png"
    image d5_1890_dadfin 11 = "sprite/dad/fin/11.png"
    image d5_1890_dadfin 12 = "sprite/dad/fin/12.png"
    image d5_1890_dadfin 13 = "sprite/dad/fin/13.png"
    image d5_1890_dadfin 14 = "sprite/dad/fin/14.png"

    image d5_1890_mom_tear 1 = "locate/home/in_side/1st_floor/hall/H1/mom/01.png"
    image d5_1890_mom_tear 2 = "locate/home/in_side/1st_floor/hall/H1/mom/02.png"
    image d5_1890_mom_tear 3 = "locate/home/in_side/1st_floor/hall/H1/mom/03.png"
    image d5_1890_mom_tear 4 = "locate/home/in_side/1st_floor/hall/H1/mom/04.png"
    image d5_1890_mom_tear 5 = "locate/home/in_side/1st_floor/hall/H1/mom/05.png"
    image d5_1890_mom_tear 6 = "locate/home/in_side/1st_floor/hall/H1/mom/06.png"
    image d5_1890_mom_tear 7 = "locate/home/in_side/1st_floor/hall/H1/mom/07.png"
    image d5_1890_mom_tear 8 = "locate/home/in_side/1st_floor/hall/H1/mom/08.png"
    image d5_1890_mom_tear 9 = "locate/home/in_side/1st_floor/hall/H1/mom/09.png"
    image d5_1890_mom_tear final:
        "d5_1890_mom_tear 3"
        .1
        "d5_1890_mom_tear 4"
        .1
        "d5_1890_mom_tear 5"
        .1
        "d5_1890_mom_tear 6"
        .1
        "d5_1890_mom_tear 7"
        .1
        "d5_1890_mom_tear 8"
        .1
        "d5_1890_mom_tear 9"

    image d5_1890_mom_memory = "locate/cemetery/end_p/mam01.png"
    image d5_1890_mom_memory2 = LiveComposite((1920, 1080),
        (0, 0), "locate/cemetery/end_p/mam02.png",
        (0, 0), "d4_noise",
        (0, 0), "old_movie_intense")

    image d5_1890_mom_memory3 = "locate/cemetery/end_p/mam03.png"

    image d5_1890_amask_p1 = LiveComposite((1920, 3570),
        (0, 2490), "d5_1890_mom_memory2")
    image d5_1890_amask_p2 = LiveComposite((1920, 3570),
        (0, 0), "d5_1890_mom_memory3")

    image d5_1890_amask_p3:
        "d5_1890_amask_p2"
        ypos 0
        easein 3 ypos 2490

    image d5_1890_amask = AlphaMask("d5_1890_amask_p1", "d5_1890_amask_p3", invert=False)

    image d5_1890_meet = "sprite/Ant/meet.png"
    image d5_1890_handmeat = "sprite/Ant/meat2.png"


    image d5_mom_meat_0 = "sprite/mom/meat/00.png"
    image d5_mom_meat_1 = "sprite/mom/meat/01.png"
    image d5_mom_meat_2 = "sprite/mom/meat/02.png"
    image d5_mom_meat_3 = "sprite/mom/meat/03.png"
    image d5_mom_meat_4 = "sprite/mom/meat/04.png"
    image d5_mom_meat_5 = "sprite/mom/meat/05.png"
    image d5_mom_meat:
        "d5_mom_meat_0"
        .1
        "d5_mom_meat_1"
        .1
        "d5_mom_meat_2"
        .1
        "d5_mom_meat_3"
        .1
        "d5_mom_meat_4"
        .1
        "d5_mom_meat_5"

    image d5_olya_meat_0 = "sprite/olya/meat/00.png"
    image d5_olya_meat_1 = "sprite/olya/meat/01.png"
    image d5_olya_meat_2 = "sprite/olya/meat/02.png"
    image d5_olya_meat_3 = "sprite/olya/meat/03.png"
    image d5_olya_meat_4 = "sprite/olya/meat/04.png"
    image d5_olya_meat_5 = "sprite/olya/meat/05.png"
    image d5_olya_meat:
        "d5_olya_meat_0"
        .1
        "d5_olya_meat_1"
        .1
        "d5_olya_meat_2"
        .1
        "d5_olya_meat_3"
        .1
        "d5_olya_meat_4"
        .1
        "d5_olya_meat_5"



    image d5_1890_forest_bg = "locate/home/in_side/1st_floor/hall/H1/str_forest.png"
    image d5_1890_forest_1 = "locate/home/in_side/1st_floor/hall/H1/str_forest01.png"
    image d5_1890_forest_2 = "locate/home/in_side/1st_floor/hall/H1/str_forest02.png"
    image d5_1890_forest_3 = "locate/home/in_side/1st_floor/hall/H1/str_forest03.png"
    image d5_1890_forest_fg = "locate/home/in_side/1st_floor/hall/H1/str_forest0.png"

    image d5_1890_forest_stars_1 = "locate/home/in_side/1st_floor/hall/H1/stars1.png"
    image d5_1890_forest_stars_2 = "locate/home/in_side/1st_floor/hall/H1/stars2.png"
    image d5_1890_forest_stars:
        "d5_1890_forest_stars_1"
        .3
        "d5_1890_forest_stars_2"
        .35
        repeat
    image d5_1890_forest_moon_1 = "locate/home/in_side/1st_floor/hall/H1/moon01.png"
    image d5_1890_forest_moon_2 = "locate/home/in_side/1st_floor/hall/H1/moon02.png"
    image d5_1890_forest_moon:
        "d5_1890_forest_moon_1"
        .3
        "d5_1890_forest_moon_2"
        .3
        repeat

    image d5_1890_picnik_base = "locate/home/in_side/1st_floor/hall/H1/picnik_fon.png"
    image d5_1890_picnik 1 = "locate/home/in_side/1st_floor/hall/H1/picnik01.png"
    image d5_1890_picnik 2 = "locate/home/in_side/1st_floor/hall/H1/picnik02.png"

    image d5_1890_alisa = "locate/home/in_side/1st_floor/hall/H1/alis.png"
    image d5_1890_alisa_full = "locate/home/in_side/1st_floor/hall/H1/Alis_full.png"
    image d5_1890_alisa_full_color = "locate/home/in_side/1st_floor/hall/H1/Alis_full_Color.png"

    image d5_1890_moon_bg = "locate/home/in_side/1st_floor/hall/H1/fon_moon.png"
    image d5_1890_moon_1 = "locate/home/in_side/1st_floor/hall/H1/moon.png"
    image d5_1890_moon_2 = "locate/home/in_side/1st_floor/hall/H1/moon2.png"
    image d5_1890_moon:
        "d5_1890_moon_1"
        .2
        "d5_1890_moon_2"
        .2
        repeat

    image d5_1890_fr_1 = "locate/home/in_side/1st_floor/hall/H1/fr01.png"
    image d5_1890_fr_2 = "locate/home/in_side/1st_floor/hall/H1/fr02.png"
    image d5_1890_fr_3 = "locate/home/in_side/1st_floor/hall/H1/fr03.png"
    image d5_1890_fr_4 = "locate/home/in_side/1st_floor/hall/H1/fr04.png"
    image d5_1890_fr_5 = "locate/home/in_side/1st_floor/hall/H1/fr05.png"
    image d5_1890_fr_6 = "locate/home/in_side/1st_floor/hall/H1/fr06.png"

    image d5_1890_fr_loop_1:
        "d5_1890_fr_1"
        .2
        "d5_1890_fr_2"
        .2
        repeat
    image d5_1890_fr_loop_2:
        "d5_1890_fr_3"
        .2
        "d5_1890_fr_4"
        .2
        repeat
    image d5_1890_fr_loop_3:
        "d5_1890_fr_5"
        .2
        "d5_1890_fr_6"
        .2
        repeat

    image d5_1890_bunny_monster_base = "locate/home/in_side/1st_floor/hall/H1/bunny_monster.png"
    image d5_1890_bunny_monster_belly_1 = "locate/home/in_side/1st_floor/hall/H1/bunny_monster2.png"
    image d5_1890_bunny_monster_belly_2 = "locate/home/in_side/1st_floor/hall/H1/bunny_monster3.png"

    image d5_1890_bunny_monster_belly:
        "d5_1890_bunny_monster_belly_1" with Dissolve(.1)
        .2
        "d5_1890_bunny_monster_belly_2" with Dissolve(.1)
        .2
        repeat

    image d5_1890_bunny_monster = LiveComposite((1191, 1138),
        (0, 0), "d5_1890_bunny_monster_base",
        (0, 0), "d5_1890_bunny_monster_belly")

    image d5_1890_jump_stars_only:
        align (.5,.5)
        block:
            choice:
                "locate/home/out_side/Meet_beasts/jump/Sky2.png"
                dstar
                "locate/home/out_side/Meet_beasts/jump/Sky3.png"
                dstar
                "locate/home/out_side/Meet_beasts/jump/Sky2.png"
                dstar
                Null()
            choice:
                "locate/home/out_side/Meet_beasts/jump/Sky4.png"
                dstar
                "locate/home/out_side/Meet_beasts/jump/Sky5.png"
                dstar
                "locate/home/out_side/Meet_beasts/jump/Sky4.png"
                dstar
                Null()
        block:
            2

        repeat

    image d5_1890_jump_stars:
        contains:
            align (.5,.5)
            "locate/home/out_side/Meet_beasts/jump/s_1.png"

        contains:
            "d5_1890_jump_stars_only"

    image d5_1890_veins_frame1 = "locate/home/in_side/1st_floor/hall/H1/frame.png"
    image d5_1890_veins_frame2 = "locate/home/in_side/1st_floor/hall/H1/frame2.png"
    image d5_1890_veins:
        align (.5, .5)
        "empty"
        1.
        "d5_1890_veins_frame1" with Dissolve(.25)
        .25
        "d5_1890_veins_frame2" with Dissolve(.25)
        .25
        "d5_1890_veins_frame1" with Dissolve(1.)
        1.
        "empty" with Dissolve(3.)
    image d5_1890_veins_p on:
        align (.5, .5)
        "empty"
        .5
        block:
            "d5_1890_veins_frame1" with Dissolve(.25)
            .25
            "d5_1890_veins_frame2" with Dissolve(.25)
            .25
            repeat
    image d5_1890_veins_p off:
        align (.5, .5)
        "d5_1890_veins_frame2"
        "d5_1890_veins_frame1" with Dissolve(.5)
        "empty" with Dissolve(1.)

    image d5_1890_veins_p stable:
        align (.5, .5)
        block:
            "d5_1890_veins_frame2" with Dissolve(.25)
            .5
            "d5_1890_veins_frame1" with Dissolve(1.5)
            1.5
            repeat

    image d5_1890_darkforest_bg = "locate/home/out_side/Meet_beasts/wood/fon2.jpg"

    image d5_1890_jump_bg = "locate/home/out_side/Meet_beasts/Jump/fon_3.png"
    image d5_1890_jump_fox bw = "locate/home/out_side/Meet_beasts/Jump/Fox-0.png"
    image d5_1890_jump_fox cl = "locate/home/out_side/Meet_beasts/Jump/Fox-1.png"
    image d5_1890_jump_fox_2 = "locate/home/out_side/Meet_beasts/Jump/Fox-2.png"
    image d5_1890_jump_fox_3 = "locate/home/out_side/Meet_beasts/Jump/Fox-3.png"
    image d5_1890_jump_fox_4 = "locate/home/out_side/Meet_beasts/Jump/Fox-4.png"
    image d5_1890_jump_fox_5 = "locate/home/out_side/Meet_beasts/Jump/Fox-5.png"
    image d5_1890_jump_fox_6 = "locate/home/out_side/Meet_beasts/Jump/Fox-6.png"
    image d5_1890_jump_fox_7 = "locate/home/out_side/Meet_beasts/Jump/Fox-7.png"
    image d5_1890_jump_fox_8 = "locate/home/out_side/Meet_beasts/Jump/Fox-8.png"
    image d5_1890_jump_fox_9 = "locate/home/out_side/Meet_beasts/Jump/Fox-9.png"

    image d5_1890_jump_planet = "locate/home/out_side/Meet_beasts/Jump/fon_3.png"

    image d5_1890_city_lights = "locate/home/in_side/1st_floor/hall/H1/city_lights.png"
    image d5_1890_city_clouds = "locate/home/in_side/1st_floor/hall/H1/clouds.png"

    image d5_1890_hunger_space = "locate/home/in_side/1st_floor/hall/H1/space.png"
    image d5_1890_hunger_bunny = "locate/home/in_side/1st_floor/hall/H1/bunny.png"
    image d5_1890_hunger_bunny_overlay = "locate/home/in_side/1st_floor/hall/H1/earth2.png"
    image d5_1890_hunger_earth = "locate/home/in_side/1st_floor/hall/H1/earth.png"
    image d5_1890_hunger_mir = "locate/home/in_side/1st_floor/hall/H1/mir.png"

    image d5_1890_planets1 = "locate/home/in_side/1st_floor/hall/H1/planets.png"
    image d5_1890_planets2 = "locate/home/in_side/1st_floor/hall/H1/planets2.png"

    image d5_1890_kaiju_bg = "locate/home/in_side/1st_floor/hall/H1/kaiju.png"
    image d5_1890_kaiju_particles_base = DustWall((3840, 2160)).sm
    image d5_1890_kaiju_particles_parallax_1:
        "d5_1890_kaiju_particles_base"
        zoom 2.0
        parallel:
            ypan 0
            linear 20 ypan 360
            repeat
        parallel:
            xpan 0
            linear 20 xpan 360
            repeat
    image d5_1890_kaiju_particles_parallax_2:
        "d5_1890_kaiju_particles_base"
        zoom 4.0
        parallel:
            ypan 180
            linear 20 ypan 360+180
            repeat
        parallel:
            xpan 0
            linear 60 xpan 360
            repeat
    image d5_1890_kaiju = LiveComposite((3840, 2160),
        (0, 0), "d5_1890_kaiju_bg",
        (0, 0), "d5_1890_kaiju_particles_parallax_1",
        (0, 0), "d5_1890_kaiju_particles_parallax_2",
        )

    transform transform_1890_memory_semen(img1, img2, img3):
        align (0.65, .75)
        block:
            img1
            zoom 1.3
            .1
            offset (200, 150)
            zoom 1.5
            .1
            offset (0, 0)
            zoom 1.0
            3.

            img2
            zoom 1.3
            .1
            offset (200, 150)
            zoom 1.5
            .1
            offset (0, 0)
            zoom 1.0
            3.

            img3
            zoom 1.3
            .1
            offset (200, 150)
            zoom 1.5
            .1
            offset (0, 0)
            zoom 1.0
            3.

            repeat

    image d5_1890_sema_02:
        contains transform_1890_memory_semen("sema upper_02", "sema upper_03", "sema upper_04")

    image d5_1890_sema 1:
        contains:
            align (0.65, .5)
            "d5_1890_sema_02"

        contains:
            "d4_noise"

        contains:
            align (0.65, .5)
            alpha .25
            "d5_1890_sema_02"


    transform transform_1890_memory_roma(img):
        contains:
            align (0.5, .5)
            img
            block:
                xoffset 200
                .1
                xoffset -100
                .1
                xoffset 0
                3.

                zoom 1.3
                xoffset -100
                .1

                xoffset 50
                zoom 0.8
                .05

                xoffset 0
                zoom 1.5
                .1

                xoffset 0
                zoom 1.0
                3.

                repeat
        contains:
            align (0.5, .5)
            img
            block:
                alpha 0.5
                xoffset 150
                .1
                xoffset -150
                .1
                alpha 0
                xoffset 0
                3.

                alpha 0.5
                zoom 1.3
                xoffset -200
                .1

                xoffset 150
                zoom 0.8
                .05

                xoffset -50
                zoom 1.5
                .1

                alpha 0.0
                xoffset 0
                zoom 1.0
                3.
                repeat


    image d5_1890_roma_tr:
        contains transform_1890_memory_roma("Romka Memory")

    image d5_1890_roma:
        contains:
            "d5_1890_roma_tr"

        contains:
            "d4_noise"

        contains:
            alpha .25
            "d5_1890_roma_tr"


    transform transform_1890_memory_byasha(img):
        contains:
            align (0.5, .5)
            img
            block:
                zoom 1.3
                xoffset 100
                .1

                xoffset -100
                zoom 0.8
                .05

                xoffset 0
                zoom 1.0
                3.

                repeat
        contains:
            align (0.5, .5)
            img
            block:
                alpha 0.5
                zoom 1.3
                xoffset 200
                .1

                xoffset -200
                zoom 0.8
                .05

                xoffset -50
                zoom 1.5
                .1

                alpha 0.0
                xoffset 0
                zoom 1.0
                2.9
                repeat


    image d5_1890_byasha_tr:
        contains transform_1890_memory_byasha("Byasha Memory")

    image d5_1890_byasha:
        contains:
            "d5_1890_byasha_tr"
            align (.5, .5)
            zoom 1.2

        contains:
            "d4_noise"

    image d5_1890_mom:
        xpos 1100
        contains transform_1890_memory_byasha("Mom Angry m_evening 00 norm ahead")
    image d5_1890_dad:
        xpos 2000
        contains transform_1890_memory_roma("Dad Angry m_evening 01 norm ahead")

    image d5_1890_milisia_1 = "locate/home/in_side/1st_floor/hall/H1/milisiya1.png"
    image d5_1890_milisia_2 = "locate/home/in_side/1st_floor/hall/H1/milisiya2.png"
    image d5_1890_milisia:
        "d5_1890_milisia_1"
        1.0
        "d5_1890_milisia_2"
        3.0
        repeat

    image d5_1890_milisia 3 = "locate/home/in_side/1st_floor/hall/H1/milisiya3.png"
    image d5_1890_milisia 4 = "locate/home/in_side/1st_floor/hall/H1/milisiya4.png"
    image d5_1890_milisia 5 = "locate/home/in_side/1st_floor/hall/H1/milisiya5.png"
    image d5_1890_milisia 6 = "locate/home/in_side/1st_floor/hall/H1/milisiya6.png"

    image d5_dust_wall = DustWall((1920, 1080)).sm

    image d5e_1890_bg = "end/1890/bg.png"
    image d5e_1890_cars = "end/1890/cars.png"
    image d5e_1890_gazeta = "end/1890/paper.png"
    image d5e_1890_particles = "end/1890/partikls.png"


    image d5_wear_axe = "locate/cemetery/goat_axe.png"
    image d5_mwear_forest_bg = "locate/forest/the_killers/fon1.png"
    image d5_mwear_forest_fg = "locate/forest/the_killers/fon2.png"
    image d5_polka_anton norm_dark = Composite((1920, 1412),
        (0, 332), "d5_polka_anton norm",
        (0, 332), AlphaMask(Solid("#0003"), "d5_unmasked_anton_base"))
    image d5_unmasked_anton_base = "locate/school/out_side/school_coner/Anton.png"
    image d5_unmasked_anton_base_2 1 = Composite((1920, 1412),
        (0, 332), "locate/street/Anton_battle/scene_04/Anton_00.png",
        (0, 332), "d5_unmasked_anton_eye_anim",
        (0, 332), AlphaMask(Solid("#0003"), "locate/street/Anton_battle/scene_04/Anton_00.png"))
    image d5_unmasked_anton_base_2 2 = Composite((1920, 1412),
        (0, 332), "locate/street/Anton_battle/scene_04/Anton_00.png",
        (0, 332), "d5_unmasked_anton_eye_anim",
        (0, 332), "d5_unmasked_anton_mouth_03",
        (0, 332), AlphaMask(Solid("#0003"), "locate/street/Anton_battle/scene_04/Anton_00.png"))
    image d5_unmasked_anton_mouth_03:
        "locate/street/Anton_battle/scene_04/mouthA_03.png"
    image d5_unmasked_anton_eye_anim:
        "locate/street/Anton_battle/scene_04/eyesA_001.png"
        pause .15
        "locate/street/Anton_battle/scene_04/eyesA_002.png"
        pause .15
        "locate/street/Anton_battle/scene_04/eyesA_003.png"
        pause .15
        "locate/street/Anton_battle/scene_04/eyesA_002.png"
        pause .15
        "locate/street/Anton_battle/scene_04/eyesA_001.png"
        pause 6.15
        repeat

    image d5_unmasked_anton = Composite((1920, 1412),
        (0, 332), "d5_unmasked_anton_base",
        (0, 332), AlphaMask(Solid("#0003"), "d5_unmasked_anton_base"))
    image d5_unmasked_anton_dark = Composite((1920, 1412),
        (0, 332), "d5_unmasked_anton_base",
        (0, 332), AlphaMask(Solid("#0006"), "d5_unmasked_anton_base"))

    image d5_masked_anton = Composite((1920, 1412),
        (0, 0), "d4_masked_anton",
        (0, 0), AlphaMask(Solid("#0003"), "d4_masked_anton"))


    image d5_masked_anton dark = Composite((1920, 1412),
        (0, 0), "d4_masked_anton",
        (0, 0), AlphaMask(Solid("#0006"), "d4_masked_anton"))

    image d5_mwear_doun_bg = "locate/forest/Milisiya/Ol_doun_bg.png"
    image d5_mwear_doun_olya = "locate/forest/Milisiya/Ol_doun.png"
    image d5_mwear_doun_fg = "locate/forest/Milisiya/Ol_doun_bg2.png"

    image d5_mwear_bmw_ant = "locate/cemetery/bmw/ant.png"
    image d5_mwear_bmw_antmask1 = "locate/cemetery/bmw/ant_mask.png"
    image d5_mwear_bmw_antmask2 = "locate/cemetery/bmw/ant_mask2.png"

    image d5_mwear_bmw_car = "locate/cemetery/bmw/bmw.png"
    image d5_mwear_bmw_car_snow_template = "locate/cemetery/bmw/snow_template_scene_c.png"
    image d5_mwear_bmw_alisa_fg = "locate/cemetery/bmw/lisa.png"
    image d5_mwear_bmw_alisa_small = "locate/cemetery/bmw/lisa2.png"
    image d5_mwear_bmw_olya = "locate/cemetery/bmw/olya.png"
    image d5_mwear_bmw_bunny = "locate/cemetery/bmw/zaichik.png"

    image d5_mwear_bmw_car appear:
        "d5_mwear_bmw_car"
        xpos 0.0
        xanchor 0.75
        easein 2.0 xanchor 0.0
        linear .05 xoffset 5 yoffset 5
        linear .15 xoffset 0 yoffset 0
    image d5_mwear_bmw_car idle:
        "d5_mwear_bmw_car"
        xpos 0.0
        xanchor 0.0
    image d5_mwear_bmw_car depart:
        "d5_mwear_bmw_car"
        xpos 1.
        xanchor 1.
        easeout_quad 3 xanchor .0
    image d5_mwear_bmw_car sit:
        "d5_mwear_bmw_car"
        ease .1 yoffset 5
        ease .1 yoffset 0

    image d5_mwear_bmw_template idle = "d5_mwear_bmw_car_snow_template"
    image d5_mwear_bmw_template arrive:
        "d5_mwear_bmw_car_snow_template"
        xpos 0.0
        xanchor 0.75
        easein 2.0 xanchor 0.0
        linear .05 xoffset 5 yoffset 5
        linear .15 xoffset 0 yoffset 0
    image d5_mwear_bmw_template depart:
        "d5_mwear_bmw_car_snow_template"
        xpos 1.
        xanchor 1.
        easeout_quad 3 xanchor .0
    image d5_mwear_bmw_template sit:
        "d5_mwear_bmw_car_snow_template"
        ease .1 yoffset 5
        ease .1 yoffset 0

    image d5_mwear_bmw_snow_scene idle = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5s_battle_bg_masked", "d5_mwear_bmw_template idle", invert = True),
        (0, 0), AlphaMask("d5s_battle_bg_bright100", "d5_mwear_bmw_template idle"),
        )
    image d5_mwear_bmw_snow_scene arrive = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5s_battle_bg_masked", "d5_mwear_bmw_template arrive", invert = True),
        (0, 0), AlphaMask("d5s_battle_bg_bright100", "d5_mwear_bmw_template arrive"),
        )
    image d5_mwear_bmw_snow_scene depart = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5s_battle_bg_masked", "d5_mwear_bmw_template depart", invert = True),
        (0, 0), AlphaMask("d5s_battle_bg_bright100", "d5_mwear_bmw_template depart"),
        )
    image d5_mwear_bmw_snow_scene sit = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5s_battle_bg_masked", "d5_mwear_bmw_template sit", invert = True),
        (0, 0), AlphaMask("d5s_battle_bg_bright100", "d5_mwear_bmw_template sit"),
        )

    image d5_mwear_bmw_father 1 = "locate/cemetery/bmw/batya1.png"
    image d5_mwear_bmw_father 2 = "locate/cemetery/bmw/batya2.png"
    image d5_mwear_bmw_father 3 = "locate/cemetery/bmw/batya3.png"

    image d5_mwear_bmw_bg1 = "locate/cemetery/bmw/fon01.png"
    image d5_mwear_bmw_bg3 = "locate/cemetery/bmw/fon03.png"
    image d5_mwear_bmw_bg4 = "locate/cemetery/bmw/fon04.png"
    image d5_mwear_bmw_bg5 = "locate/cemetery/bmw/fon05.png"
    image d5_mwear_bmw_bg6 = "locate/cemetery/bmw/fon06.png"

    image d5_mwear_bmw_deep_bg dark = "d5_mwear_bmw_bg1"
    image d5_mwear_bmw_deep_bg lit = "d5_mwear_bmw_bg3"
    image d5_mwear_bmw_close_bg dark = "d5_mwear_bmw_bg4"
    image d5_mwear_bmw_close_bg lit = "d5_mwear_bmw_bg5"
    image d5_mwear_bmw_fg = "d5_mwear_bmw_bg6"

    image d5_mwear_flame_fg = "locate/home/out_side/Flame_5.png"

    image d5_mwear_killer_sit 1 = "locate/forest/the_killers/zg1.png"
    image d5_mwear_killer_sit 2 = "locate/forest/the_killers/zg2.png"

    image d5_mwear_road_bg_1d = "locate/street/road_to_home/road01.jpg"
    image d5_mwear_road_bg_1l = "locate/street/road_to_home/road00.jpg"
    image d5_mwear_road_bg_2 = "locate/street/road_to_home/road02.png"
    image d5_mwear_road_bg_3 = "locate/street/road_to_home/road03.png"
    image d5_mwear_road_bg_4 = "locate/street/road_to_home/road04.png"
    image d5_mwear_road_bg_5 = "locate/street/road_to_home/road05.png"

    image d5_mwear_snow = "locate/forest/the_killers/snow.png"
    image d5_mwear_killer_away_1 = "locate/forest/the_killers/z01.png"
    image d5_mwear_killer_away_2 = "locate/forest/the_killers/z02.png"
    image d5_mwear_killer_away_3 = "locate/forest/the_killers/z03.png"

    image d5_mwear_killer_anton_bg = "locate/forest/the_killers/vfon.png"
    image d5_mwear_killer_anton_bunny = "locate/forest/the_killers/vanton.png"
    image d5_mwear_killer_anton_hand 0 = "locate/forest/the_killers/v00.png"
    image d5_mwear_killer_anton_hand 1 = "locate/forest/the_killers/v01.png"
    image d5_mwear_killer_anton_hand 2 = "locate/forest/the_killers/v02.png"
    image d5_mwear_killer_anton_hand 3 = "locate/forest/the_killers/v04.png"
    image d5_mwear_killer_anton_hand_blood = "locate/forest/the_killers/v03.png"

    image d5_mwear_killer_gun = "locate/forest/the_killers/killer01.png"
    image d5_mwear_killer_gun_bg = "locate/forest/the_killers/killerfon.png"

    image d5_mwear_killer_pistol = "locate/forest/the_killers/pistol.png"
    image d5_mwear_killer_pistol2 = "locate/forest/the_killers/pistol2.png"
    image d5_mwear_killer_pistol_bg = "locate/forest/the_killers/pistolfon.png"

    image d5_mwear_killer_pistol idle = "d5_mwear_killer_pistol"

    image d5_mwear_killer_pistol schelk:
        "locate/forest/the_killers/pistol_schelk.png"
        .3
        "d5_mwear_killer_pistol idle"

    image d5_mwear_closeup 1 = "locate/forest/the_killers/k1.png"
    image d5_mwear_closeup 2 = "locate/forest/the_killers/k2.png"

    image d5_mwear_fromside_bg = "sprite/bg.png"
    image d5_mwear_fromside_visiter = "sprite/Visiter_01.png"

    image d5_mwear_sideanton = "locate/forest/the_killers/bye/Ant.png"
    image d5_mwear_sideanton 2 = "locate/forest/the_killers/bye/Ant2.png"
    image d5_mwear_sideafox = "locate/forest/the_killers/bye/fox.png"


    image d5_mwear_heart_bg = "locate/forest/the_killers/k6.png"
    image d5_mwear_heart = "locate/forest/the_killers/k5.png"









    image d5_mwear_buddies_1 = "locate/forest/the_killers/buddie1.png"
    image d5_mwear_buddies_2 = "locate/forest/the_killers/buddie2.png"

    image d5_mwear_bunny = "locate/forest/the_killers/bunny.png"

    image d5_mwear_showoff_bg = "locate/forest/the_killers/background.png"
    image d5_mwear_showoff_scene1 = "locate/forest/the_killers/scene01.png"
    image d5_mwear_showoff_scene2 = "locate/forest/the_killers/scene02.png"
    image d5_mwear_showoff_scene3 = "locate/forest/the_killers/scene03.png"

    image d5_mwear_showoff_transition_1 = "locate/forest/the_killers/scene002_1.png"
    image d5_mwear_showoff_transition_2 = "locate/forest/the_killers/scene002_2.png"

    image d5_mwear_showoff_bunny idle = "locate/forest/the_killers/scene002.png"
    image d5_mwear_showoff_bunny transition:
        "locate/forest/the_killers/scene002_3.png"
        zoom 1.02
    image d5_mwear_showoff_bunny monster:
        "locate/forest/the_killers/scene003.png"
        zoom 1.05
    image d5_mwear_showoff_bunny monster2:
        "locate/forest/the_killers/scene004.png"
        zoom 1.07
        yoffset 200
        xoffset 75

    image d5_mwear_children_forest_bg = "locate/forest/the_killers/childrens/forest.png"
    image d5_mwear_children_forest_fg = "locate/forest/the_killers/childrens/forest2.png"

    image d5_mwear_children_outsiders 1 = "locate/forest/the_killers/childrens/childrens1.png"
    image d5_mwear_children_outsiders 2 = "locate/forest/the_killers/childrens/childrens2.png"

    image d5_mwear_children_buddies = "locate/forest/the_killers/childrens/buddies.png"

    image d5_mwear_children_play_1 = "locate/forest/the_killers/childrens/01.png"
    image d5_mwear_children_play_2 = "locate/forest/the_killers/childrens/02.png"
    image d5_mwear_children_play_3 = "locate/forest/the_killers/childrens/03.png"
    image d5_mwear_children_play_4 = "locate/forest/the_killers/childrens/04.png"
    image d5_mwear_children_play_5 = "locate/forest/the_killers/childrens/05.png"
    image d5_mwear_children_play_6 = "locate/forest/the_killers/childrens/06.png"
    image d5_mwear_children_play_7 = "locate/forest/the_killers/childrens/07.png"

    image d5_mwear_children_play_8 = "locate/forest/the_killers/childrens/08.png"
    image d5_mwear_children_play_9 = "locate/forest/the_killers/childrens/09.png"
    image d5_mwear_children_play_10 = "locate/forest/the_killers/childrens/010.png"
    image d5_mwear_children_play_11 = "locate/forest/the_killers/childrens/011.png"
    image d5_mwear_children_play_12 = "locate/forest/the_killers/childrens/012.png"

    image d5_mwear_children_play_bunny:
        block:
            choice:
                "d5_mwear_children_play_1" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_2" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_3" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_4" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_5" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_6" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_7" with Dissolve(.5)

        block:
            choice:
                1.0
            choice:
                2.0
            choice:
                3.0

        repeat

    image d5_mwear_children_play_fox:


        block:
            choice:
                "d5_mwear_children_play_9" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_10" with Dissolve(.5)
            choice:
                "d5_mwear_children_play_11" with Dissolve(.5)

        block:
            choice:
                2.22
            choice:
                3.33
            choice:
                4.44
        repeat

    image d5_mwear_color_bg = "locate/forest/happy_end/00bg.png"
    image d5_mwear_color_fg = "locate/forest/happy_end/01bg.png"
    image d5_mwear_color_coat = "locate/forest/happy_end/00fox.png"
    image d5_mwear_color_fox 1 = "locate/forest/happy_end/01fox.png"
    image d5_mwear_color_fox 2 = "locate/forest/happy_end/02fox.png"
    image d5_mwear_color_fox 3 = "locate/forest/happy_end/03fox.png"
    image d5_mwear_color_fox 4 = "locate/forest/happy_end/04fox.png"
    image d5_mwear_color_bunny = "locate/forest/happy_end/01bunny.png"

    image d5_mwear_color_were_bg = "locate/forest/happy_end/bg.png"
    image d5_mwear_color_were_fg = "locate/forest/happy_end/bg0.png"
    image d5_mwear_color_were_shadow 1 = "locate/forest/happy_end/shadow1.png"
    image d5_mwear_color_were_shadow 2 = "locate/forest/happy_end/shadow2.png"

    image d5_mwear_end = "locate/forest/end.png"



    image d5_police_scare_anton ahead = "locate/forest/scary/Scary/Scary1.png"
    image d5_police_scare_anton aside = "locate/forest/scary/Scary/Scary2.png"
    image d5_police_scare_anton_dark = AlphaMask(Solid("#0005"), "d5_police_scare_anton ahead")
    image d5_police_goat_bg = "locate/cemetery/goat/bg.png"
    image d5_police_goat_1 = "locate/cemetery/goat/goat.png"
    image d5_police_goat_2 = "locate/cemetery/goat/goat0.png"
    image d5_police_goat_3 = "locate/cemetery/goat/goat1.png"
    image d5_police_goat_4 = "locate/cemetery/goat/goat2.png"

    layeredimage d5_police_goat:
        always "d5_police_goat_1"

        attribute saliva if_not "talk":
            "d5_police_goat_2"

        attribute talk if_not "saliva":
            "d5_police_goat_4"

        attribute talk if_all "saliva":
            "d5_police_goat_3"

    image d5_police_road_bg_0 = "locate/forest/Road/000.png"
    image d5_police_road_bg_1 = "locate/forest/Road/001.png"
    image d5_police_road_lights 1 = "locate/forest/Road/002.png"
    image d5_police_road_lights 2 = "locate/forest/Road/003.png"
    image d5_police_road_flare1 = "locate/forest/Road/004.png"
    image d5_police_road_flare2 = "locate/forest/Road/005.png"
    image d5_police_road_car = "locate/forest/Road/006.png"

    image d5_police_snow_dark:
        "blizzard_d5_day2"
        matrixcolor BrightnessMatrix(-0.65)
    image d5_police_snow_light:
        "blizzard_d5_day2"

    image d5_police_snow_template_1 = "locate/forest/milisiya/snow_template_scene_a.png"
    image d5_police_snow_sceneA_far = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5_police_snow_dark", "d5_police_snow_template_1", invert = True),
        (0, 0), AlphaMask("d5_police_snow_light", "d5_police_snow_template_1"),
        )

    image d5_police_snow_template_2 = "locate/forest/milisiya/snow_template_scene_a2.png"
    image d5_police_snow_near_base:
        "blizzard_d4_day_near"
        parallel:
            ypan 0
            linear 3 ypan -360
            repeat
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
    image d5_police_snow_near_dark:
        "d5_police_snow_near_base"
        matrixcolor BrightnessMatrix(-0.65)
    image d5_police_snow_near_light:
        "d5_police_snow_near_base"
    image d5_police_snow_sceneA_near = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5_police_snow_near_dark", "d5_police_snow_template_2", invert = True),
        (0, 0), AlphaMask("d5_police_snow_near_light", "d5_police_snow_template_2"),
        )

    image d5_police_tihonov_1 = "locate/forest/milisiya/tih01.png"
    image d5_police_tihonov_2 = "locate/forest/milisiya/tih02.png"
    image d5_police_tihonov_3 = "locate/forest/milisiya/tih03.png"
    image d5_police_tihonov_4 = "locate/forest/milisiya/tih04.png"
    image d5_police_tihonov_fon = "locate/forest/milisiya/fon.png"

    image d5_police_tihonov:
        "d5_police_tihonov_1"
        .1
        "d5_police_tihonov_2"
        .1
        "d5_police_tihonov_3"
        .1
        "d5_police_tihonov_4"
        .1
        repeat

    image d5_police_tihonov_blink_1 = "locate/forest/milisiya/blink_big.png"
    image d5_police_tihonov_blink_2 = "locate/forest/milisiya/blink_small.png"
    image d5_police_tihonov_blink_3 = Null()
    image d5_police_tihonov_blink_4 = "locate/forest/milisiya/blink_big.png"
    image d5_police_tihonov_snow_template:
        "d5_police_tihonov_blink_1"
        .1
        "d5_police_tihonov_blink_2"
        .1
        "d5_police_tihonov_blink_3"
        .1
        "d5_police_tihonov_blink_4"
        .1
        repeat


    image d5_police_snow_sceneB_far = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5_police_snow_dark", "d5_police_tihonov_snow_template", invert = True),
        (0, 0), AlphaMask("d5_police_snow_light", "d5_police_tihonov_snow_template"),
        )
    image d5_police_snow_sceneB_near = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5_police_snow_near_dark", "d5_police_tihonov_snow_template", invert = True),
        (0, 0), AlphaMask("d5_police_snow_near_light", "d5_police_tihonov_snow_template"),
        )

    image d5_police_top_1 = "locate/forest/milisiya/top00.png"
    image d5_police_top_2 = "locate/forest/milisiya/top01.png"
    image d5_police_top_3 = "locate/forest/milisiya/top02.png"
    image d5_police_top_4 = "locate/forest/milisiya/top03.png"

    image d5_police_top_car:
        "d5_police_top_3"
        .1
        "d5_police_top_4"
        .1
        repeat

    image d5_police_uaz_1 = "locate/forest/milisiya/uaz1.png"
    image d5_police_uaz_2 = "locate/forest/milisiya/uaz2.png"
    image d5_police_uaz_3 = "locate/forest/milisiya/uaz3.png"
    image d5_police_uaz_fon = "locate/forest/milisiya/uazfon.png"
    image d5_police_uaz_fon_big = "locate/forest/milisiya/uazfon1.png"

    image d5_police_uaz_snow_dark:
        "blizzard_d5_day2"
        matrixcolor BrightnessMatrix(-0.65)
        block:
            xpan 0
            linear 2 xpan -360
            repeat
    image d5_police_uaz_snow_light:
        "blizzard_d5_day2"
        block:
            xpan 0
            linear 2 xpan -360
            repeat
    image d5_police_uaz_snow_template = "locate/forest/milisiya/snow_template_scene_c.png"
    image d5_police_snow_sceneC = LiveComposite((1920, 1080),
        (0, 0), AlphaMask("d5_police_uaz_snow_dark", "d5_police_uaz_snow_template", invert=True),
        (0, 0), AlphaMask("d5_police_uaz_snow_light", "d5_police_uaz_snow_template"),
        )

    image d5_police_uaz:
        "d5_police_uaz_1"
        .1
        "d5_police_uaz_2"
        .1
        "d5_police_uaz_3"
        .1
        repeat

    image d5_police_flash_1 = "locate/forest/milisiya/flash01.png"
    image d5_police_flash_2 = "locate/forest/milisiya/flash02.png"
    image d5_police_flash_3 = "locate/forest/milisiya/flash03.png"
    image d5_police_flash_4 = "locate/forest/milisiya/flash04.png"
    image d5_police_flash_fon = "locate/forest/milisiya/flashfon.png"

    image d5_police_flash:
        "d5_police_flash_1"
        .1
        "d5_police_flash_2"
        .1
        "d5_police_flash_3"
        .1
        "d5_police_flash_4"
        .1
        repeat

    image d5_police_pedal idle = "locate/cemetery/gaz/01.png"
    image d5_police_pedal brake = "locate/cemetery/gaz/Brake.png"
    image d5_police_pedal gas = "locate/cemetery/gaz/Gaz.png"

    image d5_police_incar_bg 1 = "locate/forest/scary/scary_fon.jpg"
    image d5_police_incar_bg 2 = "locate/cemetery/cab/fon.png"
    image d5_police_incar_cab = "locate/cemetery/cab/cab.png"
    image d5_police_incar_cab2 = "locate/cemetery/cab/cab2.png"
    image d5_police_incar_chair = "locate/cemetery/cab/chair.png"

    image d5_police_incar_z0 = "locate/cemetery/cab/z0.png"

    image d5_police_incar_anton 0 = "locate/cemetery/cab/ant0.png"
    image d5_police_incar_anton 1 = "locate/cemetery/cab/ant1.png"
    image d5_police_incar_anton 2 = "locate/cemetery/cab/ant2.png"
    image d5_police_incar_anton 3 = "locate/cemetery/cab/ant3.png"
    image d5_police_incar_anton 4:
        "locate/cemetery/cab/ant4.png"
        block:
            linear .07 yoffset -5
            linear .07 yoffset 5
            repeat

    image d5_police_incar_roma 1 = "locate/cemetery/cab/rom1.png"
    image d5_police_incar_roma 2 = "locate/cemetery/cab/rom2.png"

    image d5_police_incar_tih 1 = "locate/cemetery/cab/tih1.png"
    image d5_police_incar_tih 2 = "locate/cemetery/cab/tih2.png"
    image d5_police_incar_tih 3 = "locate/cemetery/cab/tih3.png"
    image d5_police_incar_tih 4 = "locate/cemetery/cab/tih4.png"

    image d5_police_incar_paw = "locate/cemetery/cab/lapa.png"

    image d5_police_incar_bear 1 = "locate/cemetery/cab/medv1.png"
    image d5_police_incar_bear 2 = "locate/cemetery/cab/medv2.png"
    image d5_police_incar_bear_loop:
        choice:
            "d5_police_incar_bear 2" with Dissolve(.25)
            .5
        choice:
            "d5_police_incar_bear 1" with Dissolve(.25)
            .5
        choice:
            "d5_police_incar_bear 2" with Dissolve(.25)
            1.
        choice:
            "d5_police_incar_bear 1" with Dissolve(.25)
            1.
        repeat
    image d5_police_incar_bear_anim:
        animation
        "d5_police_incar_bear_loop"
        parallel:
            easein .25 xoffset -20
            easeout .25 xoffset 20
            easein .25 xoffset -30
            easeout .25 xoffset 10
            easein .25 xoffset -10
            easeout .25 xoffset 30
            repeat
        parallel:
            easein .25 yoffset -10
            easeout .25 yoffset 110
            easein .25 yoffset 50
            easeout .25 yoffset 110
            repeat

    image d5_police_roll_car = "locate/cemetery/cab/cab01.png"
    image d5_police_roll_tih = "locate/cemetery/cab/cab02.png"
    image d5_police_roll_bg_base = "locate/cemetery/cab/cab03.png"
    image d5_police_roll_people = "locate/cemetery/cab/cab04.png"
    image d5_police_roll_bg = LiveComposite((1920, 1080),
        (0, 0), "d5_police_roll_bg_base",
        (0, 0), "d5_snow_roll")

    image d5_police_axe_bg = "locate/cemetery/axe/bg.png"
    image d5_police_axe_axe = "locate/cemetery/axe/Axe.png"
    image d5_police_axe_hum = "locate/cemetery/axe/chel.png"

    image d5_police_front_bg = "locate/cemetery/slfon.png"
    image d5_police_front_blood = "locate/cemetery/blood.png"
    image d5_police_front_owl = "locate/cemetery/cab/sova.png"
    image d5_police_front_feathers1 = "locate/cemetery/cab/feathers1.png"
    image d5_police_front_feathers2 = "locate/cemetery/cab/feathers2.png"
    image d5_police_front_sl_1 = "locate/cemetery/sl01.png"
    image d5_police_front_sl_1_dark:
        contains:
            "d5_police_front_sl_1"
        contains:
            AlphaMask(Solid("#0004"), "d5_police_front_sl_1")
    image d5_police_front_sl_2 = "locate/cemetery/sl02.png"
    image d5_police_front_sl_3 = "locate/cemetery/sl03.png"
    image d5_police_front_sl_4 = "locate/cemetery/sl04.png"
    image d5_police_front_sl_5 = "locate/cemetery/sl05.png"

    image d5_police_tihonov_heavy = "locate/cemetery/Tihonovu.png"

    image d5_police_rambo_bg = "locate/cemetery/Cab/Rambo_fon.png"
    image d5_police_rambo_uaz_1 = "locate/cemetery/Cab/uaz01.png"
    image d5_police_rambo_uaz_2 = "locate/cemetery/Cab/uaz02.png"
    image d5_police_rambo_uaz_3 = "locate/cemetery/Cab/uaz03.png"
    image d5_police_rambo_uaz:
        "d5_police_rambo_uaz_1"
        .1
        "d5_police_rambo_uaz_2"
        .1
        "d5_police_rambo_uaz_3"
        .1
        repeat
    image d5_police_rambo_uaz_olya_overlay = "locate/cemetery/Cab/uaz04.png"
    image d5_police_rambo_uaz_door = "locate/cemetery/Cab/uaz_door.png"

    image d5_police_rambo_anton 1empty = "locate/cemetery/Cab/Anton1.png"
    image d5_police_rambo_anton 2empty = "locate/cemetery/Cab/Anton2.png"
    image d5_police_rambo_anton 3empty:
        contains:
            "d5_police_rambo_anton 2empty"
        contains:
            "locate/cemetery/Cab/Anton3.png"
    image d5_police_rambo_anton 1axe = "locate/cemetery/Cab/Anton1_axe.png"
    image d5_police_rambo_anton 2axe = "locate/cemetery/Cab/Anton2_axe.png"
    image d5_police_rambo_anton 3axe:
        contains:
            "d5_police_rambo_anton 2axe"
        contains:
            "locate/cemetery/Cab/Anton3.png"
    image d5_police_rambo_polina = "locate/cemetery/Cab/pol.png"
    image d5_police_rambo_roma = "locate/cemetery/Cab/rom.png"
    image d5_police_rambo_roma2 = "locate/cemetery/Cab/rom0.png"


    image d5_flashback_0:
        contains:
            "bg_rep_04"
        contains:
            "bg_rep_4_1"
            for_tv_1
        contains:
            "bg_rep_4_2"
            for_tv_1
        contains:
            "bg_rep_3_1"
            for_tv_1
        contains:
            "bg_rep_3_2"
            for_tv_1
        contains:
            "bg_rep_2_1"
            for_tv_1
        contains:
            "bg_rep_2_2"
            for_tv_1
        contains:
            "bg_rep_1_1"
            for_tv_1
        contains:
            "bg_rep_1_2"
            for_tv_1
        contains:
            "bg_rep_0"
            for_tv_1
        contains:
            "bg_glich_0"

    image d5_flashback_1:
        "bg Fox_road1"

    image d5_flashback_2:
        contains:
            "bg_shcool_hall_down"
        contains:
            "d5_1890_sema_02"
            subpixel True
            align (.5,.5)

    image d5_flashback_3:
        contains:
            "nightmare_klass2"
            subpixel True
            yalign .9
            parallel:
                linear 0.5 yalign .95

            parallel:
                linear .05 yoffset -6
                linear .05 yoffset 0
                repeat

        contains:
            "ef_scrap"
            alpha 0.
            pause 4.
            alpha 1.

        contains:
            "bg_black"
            alpha 0.
            pause 4.
            block:
                linear .05 alpha 0.35
                linear .05 alpha 0.
                repeat

    image d5_flashback_4:
        "bg ment 002"

    image d5_flashback_5:
        "wolf_animation"

    image d5_flashback_6:
        contains:
            "fox_give_pidorka_bg"
        contains:
            "day3_beasts_scene2_snow1"
        contains:
            "day3_beasts_scene2_snow2"
        contains:
            "fox_give_beast"
        contains:
            "day3_beasts_scene2_snow3"
        contains:
            "day3_beasts_scene2_snow4"
        contains:
            "fox_give_mask"
        contains:
            "snow_for_forest1_anton"
        contains:
            "day3_beasts_scene2_snow5"

    image d5_flashback_7:
        contains:
            "tupichok_fon"
        contains:
            "Kate Hee m_day 00 evil ahead 02"
            xzoom -1
            xpos 660
            ypos 360
            zoom 0.7
            block:
                .5
                xpos 460 zoom .8
                .05
                xpos 750 zoom .6
                .05
                xpos 660 zoom 1.
                .05
                zoom 0.7
        contains:
            "tupichok_tup"
        contains:
            "Polina Front b_day 01 serious aside 04"
            xzoom -1
            xpos -500
            ypos 75
            xanchor .0
        contains:
            "cover_tup"

    image d5_flashback_8:
        "d4_home_arguing_bg"

    image d5_flashback_9:
        "d4_palace_ded_moroz"
        yalign .0

    image d5_flashback_10:
        contains:
            "d5_zh_kitchen"
        contains:
            "Olya Zulka b_day 00 good ahead 01"

    image d5_fog_1 = "interface/main_meny/meny_001.png"
    image d5_fog_2 = "interface/main_meny/meny_002.png"

    image d5_roll_1 = "locate/cemetery/Cab/roll_1.png"
    image d5_roll_2 = "locate/cemetery/Cab/roll_2.png"
    image d5_roll_3 = "locate/cemetery/Cab/roll_3.png"
    image d5_roll:
        "d5_roll_1"
        .2
        "d5_roll_2"
        .2
        "d5_roll_3"
        .2
        repeat

    image d5_uazin_bg_1 = "locate/forest/Milisiya/UAZin1.png"
    image d5_uazin_bg_bg = "locate/forest/Milisiya/UAZin_bg.png"
    image d5_uazin_bg_fg = "locate/forest/Milisiya/UAZin_bg.png"
    image d5_uazin_bg = Composite((1920, 1080),
        (0, 0), "d5_uazin_bg_bg",
        (0, 0), "d5_uazin_bg_1",
        )
    image d5_uazin_bg_2 = "locate/forest/Milisiya/UAZin2.png"
    image d5_uazin_tih = "locate/forest/Milisiya/mentura.png"
    image d5_uazin_ant = "locate/forest/Milisiya/Ant.png"
    image d5_uazin_ant1 = "locate/forest/Milisiya/Ant1.png"
    image d5_uazin_ant2 = "locate/forest/Milisiya/Ant2.png"
    image d5_uazin_rom = "locate/forest/Milisiya/Rom.png"
    image d5_uazin_rom_hand = "locate/forest/Milisiya/Rom3.png"
    image d5_uazin_rom_talk = "locate/forest/Milisiya/Rom_talk.png"
    image d5_uazin_pol = "locate/forest/Milisiya/pol.png"
    image d5_uazin_pol_shut = "locate/forest/Milisiya/pol_shut.png"
    image d5_uazin_olya = "locate/forest/Milisiya/Olya.png"
    image d5_uazin_olya_talk = "locate/forest/Milisiya/oly_talk.png"


    image d5_killer_p_talk_bg = "locate/cemetery/end_p/ant_pol1.png"

    image d5_killer_p_talk_anton_idle = "locate/cemetery/end_p/Anton/base_1.png"
    image d5_killer_p_talk_anton_talk = "locate/cemetery/end_p/Anton/base_2.png"

    image d5_killer_p_talk_anton_ahead_1 = "locate/cemetery/end_p/Anton/eyes/ahead/01.png"
    image d5_killer_p_talk_anton_ahead_2 = "locate/cemetery/end_p/Anton/eyes/ahead/02.png"
    image d5_killer_p_talk_anton_ahead_3 = "locate/cemetery/end_p/Anton/eyes/ahead/03.png"
    image d5_killer_p_talk_anton_ahead:
        animation
        "d5_killer_p_talk_anton_ahead_1"
        choice:
            5.60
        choice:
            6.20
        choice:
            7.40
        "d5_killer_p_talk_anton_ahead_2"
        .1
        "d5_killer_p_talk_anton_ahead_3"
        .1
        "d5_killer_p_talk_anton_ahead_2"
        .1
        repeat

    image d5_killer_p_talk_anton_aside_1 = "locate/cemetery/end_p/Anton/eyes/aside/01.png"
    image d5_killer_p_talk_anton_aside_2 = "locate/cemetery/end_p/Anton/eyes/aside/02.png"
    image d5_killer_p_talk_anton_aside_3 = "locate/cemetery/end_p/Anton/eyes/aside/03.png"
    image d5_killer_p_talk_anton_aside:
        animation
        "d5_killer_p_talk_anton_aside_1"
        choice:
            5.60
        choice:
            6.20
        choice:
            7.40
        "d5_killer_p_talk_anton_aside_2"
        .1
        "d5_killer_p_talk_anton_aside_3"
        .1
        "d5_killer_p_talk_anton_aside_2"
        .1
        repeat

    image Ant PKiller ahead idle = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_anton_idle",
        (0, 0), "d5_killer_p_talk_anton_ahead",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_anton_idle"),
        )
    image Ant PKiller ahead talk = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_anton_talk",
        (0, 0), "d5_killer_p_talk_anton_ahead",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_anton_idle"),
        )
    image Ant PKiller aside idle = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_anton_idle",
        (0, 0), "d5_killer_p_talk_anton_aside",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_anton_idle"),
        )
    image Ant PKiller aside talk = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_anton_talk",
        (0, 0), "d5_killer_p_talk_anton_aside",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_anton_idle"),
        )

    image d5_killer_p_talk_polina_base = "locate/cemetery/end_p/Polina/base.png"
    image d5_killer_p_talk_polina_talk = "locate/cemetery/end_p/Polina/open.png"
    image d5_killer_p_talk_polina_tears_1 = "locate/cemetery/end_p/Polina/tears.png"
    image d5_killer_p_talk_polina_tears_2 = "locate/cemetery/end_p/Polina/tears2.png"
    image Polina PKiller norm = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_polina_base",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_polina_base"),
        )
    image Polina PKiller talk = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_polina_base",
        (0, 0), "d5_killer_p_talk_polina_talk",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_polina_base"),
        )
    image Polina PKiller cry = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_polina_base",
        (0, 0), "d5_killer_p_talk_polina_tears_1",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_polina_base"),
        )
    image Polina PKiller crytalk = LiveComposite((1920, 1264),
        (0, 0), "d5_killer_p_talk_polina_base",
        (0, 0), "d5_killer_p_talk_polina_tears_2",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_p_talk_polina_base"),
        )

    image d5_killer_p_anton_back = "locate/cemetery/end_p/anton.png"
    image d5_killer_p_anton_lookback = "locate/cemetery/end_p/antonio.png"
    image d5_killer_p_killer1 = "locate/cemetery/end_p/killer.png"
    image d5_killer_p_killer2 = "locate/cemetery/end_p/killer2.png"
    image d5_killer_p_hug = "locate/cemetery/end_p/p_a.png"
    image d5_killer_p_cemetery1 = "locate/cemetery/end_p/cemetery.png"
    image d5_killer_p_cemetery2 = "locate/cemetery/end_p/cemetery2.png"
    image d5_killer_p_cemetery3 = "locate/cemetery/end_p/cemetery3.png"
    image d5_killer_p_grave = "locate/cemetery/end_p/deadparents.png"
    image d5_killer_p_moon = "locate/cemetery/end_p/moon.png"
    image d5_killer_p_choke = "locate/cemetery/end_p/murberant.png"

    image d5_killer_p_erun_anton 0 = "locate/forest/the_killers/polin/Ant0.png"
    image d5_killer_p_erun_anton 1 = "locate/forest/the_killers/polin/Ant1.png"
    image d5_killer_p_erun_anton 2 = "locate/forest/the_killers/polin/Ant2.png"
    image d5_killer_p_erun_anton 3 = "locate/forest/the_killers/polin/Ant3.png"

    image d5_killer_p_erun_polina_base = "locate/forest/the_killers/polin/Pol.png"
    image d5_killer_p_erun_polina_m1 = "locate/forest/the_killers/polin/m1.png"
    image d5_killer_p_erun_polina_m2 = "locate/forest/the_killers/polin/m2.png"
    image d5_killer_p_erun_polina_m3 = "locate/forest/the_killers/polin/m3.png"
    image d5_killer_p_erun_polina_e = "locate/forest/the_killers/polin/e1.png"
    image d5_killer_p_erun_polina dead = "locate/forest/the_killers/polin/Pol2.png"
    image d5_killer_p_erun_polina idle:
        contains:
            "d5_killer_p_erun_polina_base"
        contains:
            "d5_killer_p_erun_polina_m1"
    image d5_killer_p_erun_polina talk:
        contains:
            "d5_killer_p_erun_polina_base"
        contains:
            "d5_killer_p_erun_polina_m2"
    image d5_killer_p_erun_polina smiletalk:
        contains:
            "d5_killer_p_erun_polina_base"
        contains:
            "d5_killer_p_erun_polina_m3"
    image d5_killer_p_erun_polina idle0:
        contains:
            "d5_killer_p_erun_polina_base"
        contains:
            "d5_killer_p_erun_polina_m1"
        contains:
            "d5_killer_p_erun_polina_e"

    image d5_killer_p_erun_splash_01 = "locate/forest/the_killers/splashes/001.png"
    image d5_killer_p_erun_splash_02 = "locate/forest/the_killers/splashes/002.png"
    image d5_killer_p_erun_splash_03 = "locate/forest/the_killers/splashes/003.png"
    image d5_killer_p_erun_splash_04 = "locate/forest/the_killers/splashes/004.png"
    image d5_killer_p_erun_splash_05 = "locate/forest/the_killers/splashes/005.png"
    image d5_killer_p_erun_splash_06 = "locate/forest/the_killers/splashes/006.png"
    image d5_killer_p_erun_splash_07 = "locate/forest/the_killers/splashes/007.png"
    image d5_killer_p_erun_splash_08 = "locate/forest/the_killers/splashes/008.png"
    image d5_killer_p_erun_splash_09 = "locate/forest/the_killers/splashes/009.png"
    image d5_killer_p_erun_splash_10 = "locate/forest/the_killers/splashes/010.png"
    image d5_killer_p_erun_splash_11 = "locate/forest/the_killers/splashes/011.png"
    image d5_killer_p_erun_splash_12 = "locate/forest/the_killers/splashes/012.png"
    image d5_killer_p_erun_splash_13 = "locate/forest/the_killers/splashes/013.png"
    image d5_killer_p_erun_splash_14 = "locate/forest/the_killers/splashes/014.png"
    image d5_killer_p_erun_splash_15 = "locate/forest/the_killers/splashes/015.png"
    image d5_killer_p_erun_splash_16 = "locate/forest/the_killers/splashes/016.png"
    image d5_killer_p_erun_splash_17 = "locate/forest/the_killers/splashes/017.png"
    image d5_killer_p_erun_splash_18 = "locate/forest/the_killers/splashes/018.png"
    image d5_killer_p_erun_splash_19 = "locate/forest/the_killers/splashes/019.png"
    image d5_killer_p_erun_splash_20 = "locate/forest/the_killers/splashes/020.png"
    image d5_killer_p_erun_splash_21 = "locate/forest/the_killers/splashes/021.png"
    image d5_killer_p_erun_splash_22 = "locate/forest/the_killers/splashes/022.png"

    image d5_killer_p_erun_fallen = "locate/forest/the_killers/polin/Fallen.png"
    image d5_killer_p_erun_smoke = "locate/forest/the_killers/polin/smoke.png"


    $ dt_splash = 0.06
    image d5_killer_p_erun_splash:
        "d5_killer_p_erun_splash_01"
        dt_splash
        "d5_killer_p_erun_splash_02"
        dt_splash
        "d5_killer_p_erun_splash_03"
        dt_splash
        "d5_killer_p_erun_splash_04"
        dt_splash
        "d5_killer_p_erun_splash_05"
        dt_splash
        "d5_killer_p_erun_splash_06"
        dt_splash
        "d5_killer_p_erun_splash_07"
        dt_splash
        "d5_killer_p_erun_splash_08"
        dt_splash
        "d5_killer_p_erun_splash_09"
        dt_splash
        "d5_killer_p_erun_splash_10"
        dt_splash
        "d5_killer_p_erun_splash_11"
        dt_splash
        "d5_killer_p_erun_splash_12"
        dt_splash
        "d5_killer_p_erun_splash_13"
        dt_splash
        "d5_killer_p_erun_splash_14"
        dt_splash
        "d5_killer_p_erun_splash_15"
        dt_splash
        "d5_killer_p_erun_splash_16"
        dt_splash
        "d5_killer_p_erun_splash_17"
        dt_splash
        "d5_killer_p_erun_splash_18"
        dt_splash
        "d5_killer_p_erun_splash_19"
        dt_splash
        "d5_killer_p_erun_splash_20"
        dt_splash
        "d5_killer_p_erun_splash_21"
        dt_splash
        "d5_killer_p_erun_splash_22"
        dt_splash
        Null()

    image d5_killer_p_erun_splash_loop:
        "d5_killer_p_erun_splash_01"
        dt_splash
        "d5_killer_p_erun_splash_02"
        dt_splash
        "d5_killer_p_erun_splash_03"
        dt_splash
        "d5_killer_p_erun_splash_04"
        dt_splash
        "d5_killer_p_erun_splash_05"
        dt_splash
        "d5_killer_p_erun_splash_06"
        dt_splash
        "d5_killer_p_erun_splash_07"
        dt_splash
        "d5_killer_p_erun_splash_08"
        dt_splash
        "d5_killer_p_erun_splash_09"
        dt_splash
        "d5_killer_p_erun_splash_10"
        dt_splash
        "d5_killer_p_erun_splash_11"
        dt_splash
        "d5_killer_p_erun_splash_12"
        dt_splash
        "d5_killer_p_erun_splash_13"
        dt_splash
        "d5_killer_p_erun_splash_14"
        dt_splash
        "d5_killer_p_erun_splash_15"
        dt_splash
        "d5_killer_p_erun_splash_16"
        dt_splash
        "d5_killer_p_erun_splash_17"
        dt_splash
        "d5_killer_p_erun_splash_18"
        dt_splash
        "d5_killer_p_erun_splash_19"
        dt_splash
        "d5_killer_p_erun_splash_20"
        dt_splash
        "d5_killer_p_erun_splash_21"
        dt_splash
        "d5_killer_p_erun_splash_22"
        dt_splash
        Null()
        dt_splash
        repeat
    image d5_killer_p_erun_splash_loop2:
        "d5_killer_p_erun_splash_17"
        dt_splash
        "d5_killer_p_erun_splash_18"
        dt_splash
        "d5_killer_p_erun_splash_19"
        dt_splash
        "d5_killer_p_erun_splash_20"
        dt_splash
        "d5_killer_p_erun_splash_21"
        dt_splash
        "d5_killer_p_erun_splash_22"
        dt_splash
        Null()
        dt_splash
        "d5_killer_p_erun_splash_01"
        dt_splash
        "d5_killer_p_erun_splash_02"
        dt_splash
        "d5_killer_p_erun_splash_03"
        dt_splash
        "d5_killer_p_erun_splash_04"
        dt_splash
        "d5_killer_p_erun_splash_05"
        dt_splash
        "d5_killer_p_erun_splash_06"
        dt_splash
        "d5_killer_p_erun_splash_07"
        dt_splash
        "d5_killer_p_erun_splash_08"
        dt_splash
        "d5_killer_p_erun_splash_09"
        dt_splash
        "d5_killer_p_erun_splash_10"
        dt_splash
        "d5_killer_p_erun_splash_11"
        dt_splash
        "d5_killer_p_erun_splash_12"
        dt_splash
        "d5_killer_p_erun_splash_13"
        dt_splash
        "d5_killer_p_erun_splash_14"
        dt_splash
        "d5_killer_p_erun_splash_15"
        dt_splash
        "d5_killer_p_erun_splash_16"
        dt_splash
        repeat

    image d5_killer_p_killer1_dark:
        contains:
            "d5_killer_p_killer1"
        contains:
            AlphaMask(Solid("#0004"), "d5_killer_p_killer1")
    image d5_killer_p_killer2_dark:
        contains:
            "d5_killer_p_killer2"
        contains:
            AlphaMask(Solid("#0004"), "d5_killer_p_killer2")

    image d5_killer_p_pain:
        "d5_killer_p_choke"
        align (.5, .75)
        zoom 1.2
        alpha .0
        parallel:
            linear .04 xoffset 5
            linear .04 xoffset -5
            repeat
        parallel:
            ease 0.1 zoom 1.3
            ease 0.1 zoom 1.1
            ease 0.1 zoom 1.4
            ease 0.1 zoom 1.2
            repeat
        parallel:
            linear .07 alpha .2
            linear .07 alpha .1
            repeat

    image d5_killer_p_veil:
        "bg_black"
        block:
            linear .02 alpha .75
            linear .02 alpha 1.
            repeat

    image d5_killer_p_fin_dad = "sprite/Dad/Happy/m_day/1_body/00.png"
    image d5_killer_p_fin_mom = im.Composite((674, 1080),
        (0, 0), "sprite/Mom/Normal/m_day/1_body/04.png",
        (0, 0), "sprite/Mom/Normal/m_day/2_eyes/norm/ahead/01.png")
    image d5_killer_p_fin_pol = im.Composite((1920, 1080),
        (0, 0), "sprite/Polina/3_4/b_day/1_body/00.png",
        (0, 0), "sprite/Polina/3_4/b_day/3_mouth/05.png",
        )
    image d5_killer_p_fin_olya = im.Composite((1920, 1080),
        (0, 0), "sprite/Olya/Happy/b_day/1_body/00.png",
        (0, 0), "sprite/Olya/Happy/b_day/3_mouth/01.png",
        )



    image d5_killer_car_olya:
        "Olya Weeps b_evening_winter 02 good ahead 01 dark 40"
        xzoom -1
        xoffset 100
        yoffset 200

    image d5_killer_o_olya0 = "locate/forest/the_killers/Olya/Olya0.png"
    image d5_killer_o_disrupt_olya = "locate/forest/the_killers/Olya/Olya.png"
    image d5_killer_o_disrupt_killer 1 = "locate/forest/the_killers/Olya/killer1.png"
    image d5_killer_o_disrupt_killer 2 = "locate/forest/the_killers/Olya/killer2.png"
    image d5_killer_o_kick_olya_1 = "locate/forest/the_killers/Olya/Olya2.png"
    image d5_killer_o_kick_olya_2 = "locate/forest/the_killers/Olya/Olya3.png"
    image d5_killer_o_kick_leg = "locate/forest/the_killers/Olya/killer3.png"
    image d5_killer_o_bg = "locate/forest/the_killers/Olya/bg.png"
    image d5_killer_o_tomb_1 = "locate/forest/the_killers/Olya/Tomb1.png"
    image d5_killer_o_tomb_2 = "locate/forest/the_killers/Olya/Tomb2.png"
    image d5_killer_o_runaway = "locate/forest/runaway/Run_away_happy.png"

    image d5_killer_o_lookback_anton = "locate/forest/the_killers/polin/Ant0.png"
    image d5_killer_o_lookback_anton 1 = "locate/forest/the_killers/polin/Ant1.png"
    image d5_killer_o_lookback_anton 2 = "locate/forest/the_killers/polin/Ant2.png"
    image d5_killer_o_lookback_anton 3 = "locate/forest/the_killers/polin/Ant3.png"
    image d5_killer_o_polina_back = "sprite/polina/back3.png"
    image d5_killer_o_polina_back dark 15 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#0002"), "d5_killer_o_polina_back")
        )
    image d5_killer_o_polina_back dark 30 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#0004"), "d5_killer_o_polina_back")
        )
    image d5_killer_o_polina_back dark 40 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#0006"), "d5_killer_o_polina_back")
        )
    image d5_killer_o_polina_back dark 50 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#0008"), "d5_killer_o_polina_back")
        )
    image d5_killer_o_polina_back dark 60 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#000a"), "d5_killer_o_polina_back")
        )
    image d5_killer_o_polina_back dark 70 = Composite((1920, 1876),
        (0, 0), "d5_killer_o_polina_back",
        (0, 0), AlphaMask(Solid("#000c"), "d5_killer_o_polina_back")
        )

    image d5_killer_o_grave_bg = "locate/forest/the_killers/Olya/bg00.png"
    image d5_killer_o_grave_olya_base = "locate/forest/the_killers/Olya/Olya01.png"
    image d5_killer_o_grave_olya 0 = "d5_killer_o_grave_olya_base"
    image d5_killer_o_grave_olya 1 = Composite((1920, 1080),
        (0, 0), "d5_killer_o_grave_olya_base",
        (0, 0), "locate/forest/the_killers/Olya/Olya02.png")
    image d5_killer_o_grave_olya 2 = Composite((1920, 1080),
        (0, 0), "d5_killer_o_grave_olya_base",
        (0, 0), "locate/forest/the_killers/Olya/Olya03.png")



    image d5s_battle_bg:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_bg_bright100:
        contains:
            animation
            "d5b_snow_02"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_02"
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_bg_solo:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan -360
                repeat
    image d5s_battle_bg_solo_bright100:
        contains:
            animation
            "d5b_snow_02"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan -360
                repeat
    image d5s_battle_bg_solo_bright100_tile = Tile("d5s_battle_bg_solo_bright100", size=(1920*4, 1080*4))

    image d5s_battle_bg_masked = AlphaMask("d5s_battle_bg", "effect/ImageDissolve/shadow/03.png", invert=True)
    image d5s_battle_bg_rev_tr:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan -36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan 360
                    repeat
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan -36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan 360
                    repeat
    image d5s_battle_bg_rev_tr_back:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan 36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan -360
                    repeat
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan 36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan -360
                    repeat
    image d5s_battle_bg_rev:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_bg_rev_masked = AlphaMask("d5s_battle_bg_rev", "effect/ImageDissolve/shadow/03.png", invert=True)
    image d5s_battle_bg2:
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_02"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan -360
                repeat

    image d5s_battle_mid:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.67*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_mid_solo:
        animation
        "d5b_snow_01"
        matrixcolor BrightnessMatrix(-0.30)
        parallel:
            xpan 0
            linear 10*4.0 xpan -360
            repeat
        parallel:
            ypan 0
            linear 10*0.67 ypan -360
            repeat
    image d5s_battle_mid_masked = AlphaMask("d5s_battle_mid", "effect/ImageDissolve/shadow/03.png", invert=True)
    image d5s_battle_mid_double = LiveComposite((1920, 2160),
        (0, 0), "d5s_battle_mid",
        (0, 1080), "d5s_battle_mid",
        )
    image d5s_battle_mid_bright100:
        animation
        contains:
            "d5b_snow_01"

            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
        contains:
            "d5b_snow_01"

            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.67*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_mid_solo_bright100:
        animation
        contains:
            "d5b_snow_01"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
    image d5s_battle_mid_bright100_masked = AlphaMask("d5s_battle_mid_bright100", "effect/ImageDissolve/shadow/03.png", invert=True)
    image d5s_battle_mid_rev_tr:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan -36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan 360
                    repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan -36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan 360
                    repeat
    image d5s_battle_mid_rev_tr_back:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan 36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan -360
                    repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan 36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan -360
                    repeat
    image d5s_battle_mid_rev:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.30)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_mid_rev_bright100:
        contains:
            animation
            "d5b_snow_01"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
        contains:
            animation
            "d5b_snow_01"
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_mid_rev_bright100_masked = AlphaMask("d5s_battle_mid_rev_bright100", "effect/ImageDissolve/shadow/03.png", invert=True)

    image d5s_battle_mid2:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.67*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_mid2_masked = AlphaMask("d5s_battle_mid2", "effect/ImageDissolve/shadow/03.png", invert=True)
    image d5s_battle_mid2_rev:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_mid2_solo:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat

    image d5s_battle_mid3:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.50)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.67*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_mid3_solo:
        animation
        "d5b_snow_01"
        matrixcolor BrightnessMatrix(-0.50)
        parallel:
            xpan 0
            linear 10*4.0 xpan -360
            repeat
        parallel:
            ypan 0
            linear 10*0.67 ypan -360
            repeat

    image d5s_battle_mid4_solo:
        animation
        "d5b_snow_01"
        matrixcolor BrightnessMatrix(-0.15)
        parallel:
            xpan 0
            linear 10*4.0 xpan -360
            repeat
        parallel:
            ypan 0
            linear 10*0.67 ypan -360
            repeat


    image d5s_battle_fg:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.28 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 180
                linear 10*4.0*(1.0 - 0.15) xpan -360+180
                repeat
            parallel:
                ypan 0
                linear 10*0.28*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_fg_bright100:
        contains:
            "d5b_snow_00"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.28 ypan -360
                repeat
        contains:
            "d5b_snow_00"
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.28*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_fg_solo:
        animation
        "d5b_snow_00"
        matrixcolor BrightnessMatrix(-0.15)
        parallel:
            ypan 0
            linear 10*0.28 ypan -360
            repeat
    image d5s_battle_fg_solo_bright100:
        animation
        "d5b_snow_00"
        parallel:
            ypan 0
            linear 10*0.28 ypan -360
            repeat
    image d5s_battle_fg_rev_tr:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan -36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan 360
                    repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 180
                linear 10*4.0*(1.0 - 0.15) xpan -360+180
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan -36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan 360
                    repeat
    image d5s_battle_fg_rev_tr_back:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan 36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan -360
                    repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 180
                linear 10*4.0*(1.0 - 0.15) xpan -360+180
                repeat
            parallel:
                ypan 0
                easein 2*(1.0 + 0.15) ypan 36*2
                easeout 2*(1.0 + 0.15) ypan 0
                block:
                    ypan 0
                    linear 10*(1.0 - 0.15) ypan -360
                    repeat
    image d5s_battle_fg_rev:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 180
                linear 10*4.0*(1.0 - 0.15) xpan -360+180
                repeat
            parallel:
                ypan 0
                linear 10*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_fg_rev_solo:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10 ypan 360
                repeat
    image d5s_battle_fg_rev_tr_solo:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                easein 2 ypan -36*2
                easeout 2 ypan 0
                block:
                    ypan 0
                    linear 10 ypan 360
                    repeat
    image d5s_battle_fg_rev_bright100:
        contains:
            "d5b_snow_00"
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.28 ypan 360
                repeat
        contains:
            "d5b_snow_00"
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.28*(1.0 - 0.15) ypan 360
                repeat
    image d5s_battle_fg_rev_solo_bright100:
        "d5b_snow_00"
        parallel:
            xpan 0
            linear 10*4.0 xpan -360
            repeat
        parallel:
            ypan 0
            linear 10*0.28 ypan 360
            repeat

    image d5s_battle_fg2:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.35)
            parallel:
                xpan 0
                linear 10*4.0 xpan -360
                repeat
            parallel:
                ypan 0
                linear 10*0.28 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.35)
            parallel:
                xpan 70
                linear 10*4.0*(1.0 - 0.15) xpan -360+70
                repeat
            parallel:
                ypan 0
                linear 10*0.28*(1.0 - 0.15) ypan -360
                repeat
    image d5s_battle_fg2_solo:
        animation
        "d5b_snow_00"
        matrixcolor BrightnessMatrix(-0.35)
        parallel:
            ypan 0
            linear 10*0.28 ypan -360
            repeat
    image d5s_battle_fg2_rev_solo:
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.25)




            parallel:
                ypan 0
                linear 10*0.5 ypan 360
                repeat

    image d5s_battle_mix:
        contains:
            animation
            "d5b_snow_01"
            matrixcolor BrightnessMatrix(-0.40)
            parallel:
                transform_anchor True
                align (.5, .5)
                zoom 1.5
                rotate -15
            parallel:
                ypan 0
                linear 10*0.67 ypan -360
                repeat
        contains:
            animation
            "d5b_snow_00"
            matrixcolor BrightnessMatrix(-0.15)
            parallel:
                transform_anchor True
                align (.5, .5)
                zoom 1.5
                rotate -15
            parallel:
                ypan 0
                linear 10*0.28 ypan -360
                repeat

    image d5s_snow_night = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=40, yspeed=(40 *3, 50 *3), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=80, yspeed=(50 *3, 80 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=80, yspeed=(60 *3, 90 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )
    image d5s_snow_night 1 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=30, yspeed=(40 *3, 50 *3), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=60, yspeed=(50 *3, 80 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=60, yspeed=(60 *3, 90 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )
    image d5s_snow_night 2 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=15, yspeed=(40 *3, 50 *3), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=30, yspeed=(50 *3, 80 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=30, yspeed=(60 *3, 90 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )
    image d5s_snow_night 3 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=5, yspeed=(40 *3, 50 *3), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=10, yspeed=(50 *3, 80 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=10, yspeed=(60 *3, 90 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )

    image d5s_snow_night a = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=120, yspeed=(40 *3, 50 *3), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=160, yspeed=(50 *3, 80 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=160, yspeed=(60 *3, 90 *3), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )
    image d5s_snow_night inface = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s002.png", count=5, yspeed=(40 *9 *2, 50 *9 *2), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s005.png", count=10, yspeed=(60 *9 *2, 90 *9 *2), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        )


    image d5s_ravine_bg:
        "blizzard_d4_day_far"
        matrixcolor BrightnessMatrix(-0.2)
        parallel:
            ypan 0
            linear 3 ypan -360
            repeat
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat
    image d5s_ravine_fg:
        "blizzard_d4_day_near"
        matrixcolor BrightnessMatrix(-0.2)
        parallel:
            ypan 0
            linear 3 ypan -360
            repeat
        parallel:
            xpan 0
            linear 5 xpan -360
            repeat

    image d5_cemetery_master 1 = "locate/cemetery/master1.png"
    image d5_cemetery_master 2 = "locate/cemetery/master2.png"
    image d5_cemetery_master 3 = "locate/cemetery/master3.png"
    image d5_cemetery_master 4 = "locate/cemetery/master4.png"
    image d5_cemetery_landscape_0 = "locate/cemetery/00.png"
    image d5_cemetery_landscape_1 = "locate/cemetery/01.png"
    image d5_cemetery_landscape_2 = "locate/cemetery/02.png"
    image d5_cemetery_landscape_3 = "locate/cemetery/03.png"
    image d5_cemetery_landscape_4 = "locate/street/road_to_home(N)/road05.png"
    image d5_cemetery_bg_1 = "locate/cemetery/fon.png"
    image d5_cemetery_bg_1_over = "locate/cemetery/fon_overlay.png"
    image d5_cemetery_bg_2 = "locate/cemetery/fon2.png"
    image d5_cemetery_bg_3 = "locate/cemetery/bg_cem/bg.png"

    image d5_cemetery_bg_3_flute = LiveComposite((1920, 1080),
        (0, 0), "d5_cemetery_bg_3",
        (0, 0), "d5s_battle_bg_rev",
        (0, 0), "d5s_battle_mid_rev",
        )

    image d5_cemetery_bg_4 = "locate/cemetery/fon3.png"

    image d5_cemetery_goathand = "locate/cemetery/Goat_hand.png"
    image d5_cemetery_goathand1 = "locate/cemetery/goat/Goat_hand1.png"
    image d5_cemetery_goathand2 = "locate/cemetery/goat/Goat_hand2.png"

    image d5_battle_tea_bg = "locate/cemetery/goat/bg3.png"
    image d5_battle_goat_side = "locate/cemetery/goat/Goat00.png"
    image d5_battle_goat_back 1 = "locate/cemetery/goat/Goat01.png"
    image d5_battle_goat_back 2 = "locate/cemetery/goat/Goat02.png"
    image d5_battle_goat_back 3 = "locate/cemetery/goat/Goat03.png"
    image d5_battle_goat_back 4 = "locate/cemetery/goat/Goat04.png"
    image d5_battle_goat_back 5 = "locate/cemetery/goat/Goat05.png"
    image d5_battle_owl_back:
        "locate/cemetery/goat/Owl.png"
        xzoom -1
        xoffset -250
        yoffset 50
    image d5_battle_bear_back:
        "locate/cemetery/goat/bear2.png"
        xzoom -1
        xoffset 250
        yoffset 50
    image d5_battle_wolf_back = "locate/cemetery/b_oo.png"

    image d5_battle_moon = "locate/cemetery/goat/fon.png"
    image d5_battle_bunny 1 = "locate/cemetery/bg_cem/b1.png"
    image d5_battle_bunny 2 = "locate/cemetery/bg_cem/b2.png"
    image d5_battle_bunny 3 = "locate/cemetery/bg_cem/b3.png"
    image d5_battle_bunny 4 = "locate/cemetery/bg_cem/b4.png"
    image d5_battle_bunny 5 = "locate/cemetery/bg_cem/b5.png"
    image d5_battle_bunny 6 = "locate/cemetery/bg_cem/b6.png"

    image d5_battle_anton_back = LiveComposite((1920, 1080),
        (0, 0), "anton_sp_05",
        (0, 0), AlphaMask(Solid("#0008"), "anton_sp_05"))

    image d5_battle_anton_tears = "sprite/ant/ant_tears.png"

    image d5_battle_anton idle = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant",
        (0, 0), "d5_battle_anton_tears",
        (0, 0), AlphaMask(Solid("#0004"), "d4_gor_ant"))
    image d5_battle_anton talk = LiveComposite((2607, 2589),
        (0, 0), "d4_gor_ant 1",
        (0, 0), "d5_battle_anton_tears",
        (0, 0), AlphaMask(Solid("#0004"), "d4_gor_ant 1"))
    image d5_battle_anton_notears idle = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant",
        (0, 0), AlphaMask(Solid("#0004"), "d4_gor_ant"))
    image d5_battle_anton_notears talk = LiveComposite((2607, 2589),
        (0, 0), "d4_gor_ant 1",
        (0, 0), AlphaMask(Solid("#0004"), "d4_gor_ant 1"))

    image d5_conflict_car_bg = "locate/forest/Milisiya/V_kabine/by/bg.png"
    image d5_conflict_car_uaz1 = "locate/forest/Milisiya/V_kabine/by/1.png"
    image d5_conflict_car_uaz2 = "locate/forest/Milisiya/V_kabine/by/2.png"
    image d5_conflict_car_uaz:
        "d5_conflict_car_uaz1"
        .2
        "d5_conflict_car_uaz2"
        .2
        repeat

    image d5_bones_bg_base = "locate/cemetery/bones/bg.png"
    image d5_bones_bg_overlay = "locate/cemetery/bones/Bones.png"
    image d5_bones_bg_overlay2 = "locate/cemetery/bones/Bones2.png"
    image d5_bones_bg snow = "d5_bones_bg_base"
    image d5_bones_bg bones = LiveComposite((1920, 1080),
        (0, 0), "d5_bones_bg_base",
        (0, 0), "d5_bones_bg_overlay")
    image d5_bones_bg bones2 = LiveComposite((1920, 1080),
        (0, 0), "d5_bones_bg_base",
        (0, 0), "d5_bones_bg_overlay",
        (0, 0), "d5_bones_bg_overlay2")
    image d5_bones_mom_base = "locate/cemetery/bones/mom.png"
    image d5_bones_mom 0 = "locate/cemetery/bones/Arms_mom.png"
    image d5_bones_mom 1 = "locate/cemetery/bones/Arms_mom02.png"
    image d5_bones_mom 2 = "locate/cemetery/bones/Arms_mom2.png"
    image d5_bones_mom_smoke:
        animation
        "locate/cemetery/bones/smoke.png"
        function WaveShader(amp=1, period=15, speed=.04, direction="horisontal")
    image d5_bones_tih_base = "locate/cemetery/bones/ment.png"
    image d5_bones_tih 0 = "locate/cemetery/bones/ment_arm.png"
    image d5_bones_tih 1 = "locate/cemetery/bones/ment_arm02.png"
    image d5_bones_tih 2 = "locate/cemetery/bones/ment_arm2.png"
    image d5_bones_tih_smoke:
        animation
        "locate/cemetery/bones/smoke2.png"
        function WaveShader(amp=1.25, period=4, speed=.12, direction="horisontal")

    image d5_bones_bug_bg = "locate/cemetery/bones/Zuk_bg.png"
    image d5_bones_bug = "locate/cemetery/bones/Zuk.png"

    image d5_battle_shadow = LiveComposite((3488, 1080),
        (0, 0), "perehod",
        (0, 0), AlphaMask(Solid("#000e"), "perehod"))

    image d5_transform_smoke:
        animation
        "locate/cemetery/smoke2.png"
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 120
            linear 45 xpan 360+120
            repeat

    image d5_transform_wolf_1 = "locate/cemetery/bg_cem/v01.png"
    image d5_transform_wolf_2 = "locate/cemetery/bg_cem/v02.png"
    image d5_transform_bunny_1 = "locate/cemetery/bg_cem/ban01.png"
    image d5_transform_bunny_2 = "locate/cemetery/bg_cem/ban02.png"

    image d5_battle_tih_wolf turn talk = "sprite/Tihonov/00.png"
    image d5_battle_tih_wolf turn idle = "sprite/Tihonov/0.png"

    image d5_battle_wolfy_back = "locate/cemetery/back/woolf.png"
    image d5_battle_fox_back = "locate/cemetery/back/fox1.png"

    image d5_battle_hare_full = "sprite/Mom/Hare_Mom/Hare_Mom.png"
    image d5_battle_tih_wolf 1 = "sprite/Tihonov/001.png"
    image d5_battle_tih_wolf 4 = "sprite/Tihonov/004.png"

    image d5_battle_tih_wolf_m 0 = "sprite/Tihonov/w0.png"
    image d5_battle_tih_wolf_m 00 = "sprite/Tihonov/w00.png"
    image d5_battle_tih_wolf_m 01 = "sprite/Tihonov/w01.png"
    image d5_battle_tih_wolf_m 02 = "sprite/Tihonov/w02.png"
    image d5_battle_tih_wolf_m 03 = "sprite/Tihonov/w03.png"
    image d5_battle_tih_wolf_m 04 = "sprite/Tihonov/w04.png"
    image d5_battle_tih_wolf_m 05 = "sprite/Tihonov/w05.png"
    image d5_battle_tih_wolf_m 06 = "sprite/Tihonov/w06.png"
    image d5_battle_tih_wolf_m 07 = "sprite/Tihonov/w07.png"
    image d5_battle_tih_wolf_m 08 = "sprite/Tihonov/w08.png"
    image d5_battle_tih_wolf_m 09 = "sprite/Tihonov/w09.png"
    image d5_battle_tih_wolf_m 10 = "sprite/Tihonov/w10.png"
    image d5_battle_tih_wolf_m 11 = "sprite/Tihonov/w11.png"
    image d5_battle_tih_wolf_m 12 = "sprite/Tihonov/w12.png"
    image d5_battle_tih_wolf_m 13 = "sprite/Tihonov/w13.png"

    image d5_battle_tih_wolf_m assault:
        block:
            "d5_battle_tih_wolf_m 01"
            .08
            "d5_battle_tih_wolf_m 02"
            .08
            "d5_battle_tih_wolf_m 03"
            .08
            "d5_battle_tih_wolf_m 04"
            .08
            "d5_battle_tih_wolf_m 05"
            .08
            "d5_battle_tih_wolf_m 06"
            .08
            repeat 3
        "d5_battle_tih_wolf_m 00"
        1.
        repeat
    image d5_battle_tih_wolf_m burst:
        block:
            "d5_battle_tih_wolf_m 01"
            .08
            "d5_battle_tih_wolf_m 02"
            .08
            "d5_battle_tih_wolf_m 03"
            .08
            "d5_battle_tih_wolf_m 04"
            .08
            "d5_battle_tih_wolf_m 05"
            .08
            "d5_battle_tih_wolf_m 06"
            .08
            repeat 3
        "d5_battle_tih_wolf_m 00"

    image Tihonov Rifle assault1:
        "sprite/Tihonov/m_winter/1_body/01.png"
        .08
        "sprite/Tihonov/m_winter/1_body/02.png"
        .08
        "sprite/Tihonov/m_winter/1_body/03.png"
        .08
        repeat
    image Tihonov Rifle assault2:
        "sprite/Tihonov/m_winter/1_body/04.png"
        .08
        "sprite/Tihonov/m_winter/1_body/05.png"
        .08
        "sprite/Tihonov/m_winter/1_body/06.png"
        .08
        repeat

    define assault_bstorm = 0.08
    image d5_battle_bulletstorm_1 = "locate/cemetery/bullets/001.png"
    image d5_battle_bulletstorm_2 = "locate/cemetery/bullets/002.png"
    image d5_battle_bulletstorm_3 = "locate/cemetery/bullets/003.png"
    image d5_battle_bulletstorm_4 = "locate/cemetery/bullets/004.png"
    image d5_battle_bulletstorm_5 = "locate/cemetery/bullets/005.png"
    image d5_battle_bulletstorm_6 = "locate/cemetery/bullets/006.png"
    image d5_battle_bulletstorm_7 = "locate/cemetery/bullets/007.png"
    image d5_battle_bulletstorm_8 = "locate/cemetery/bullets/008.png"
    image d5_battle_bulletstorm_9 = "locate/cemetery/bullets/009.png"
    image d5_battle_bulletstorm_10 = "locate/cemetery/bullets/010.png"
    image d5_battle_bulletstorm_11 = "locate/cemetery/bullets/011.png"
    image d5_battle_bulletstorm_12 = "locate/cemetery/bullets/012.png"
    image d5_battle_bulletstorm_13 = "locate/cemetery/bullets/013.png"
    image d5_battle_bulletstorm_14 = "locate/cemetery/bullets/014.png"
    image d5_battle_bulletstorm_15 = "locate/cemetery/bullets/015.png"
    image d5_battle_bulletstorm_16 = "locate/cemetery/bullets/016.png"
    image d5_battle_bulletstorm_17 = "locate/cemetery/bullets/017.png"
    image d5_battle_bulletstorm_18 = "locate/cemetery/bullets/018.png"
    image d5_battle_bulletstorm_19 = "locate/cemetery/bullets/019.png"
    image d5_battle_bulletstorm_20 = "locate/cemetery/bullets/020.png"
    image d5_battle_bulletstorm_21 = "locate/cemetery/bullets/021.png"
    image d5_battle_bulletstorm_22 = "locate/cemetery/bullets/022.png"
    image d5_battle_bulletstorm_23 = "locate/cemetery/bullets/023.png"
    image d5_battle_bulletstorm:
        "d5_battle_bulletstorm_1"
        assault_bstorm
        "d5_battle_bulletstorm_2"
        assault_bstorm
        "d5_battle_bulletstorm_3"
        assault_bstorm
        "d5_battle_bulletstorm_4"
        assault_bstorm
        "d5_battle_bulletstorm_5"
        assault_bstorm
        "d5_battle_bulletstorm_6"
        assault_bstorm
        "d5_battle_bulletstorm_7"
        assault_bstorm
        "d5_battle_bulletstorm_8"
        assault_bstorm
        "d5_battle_bulletstorm_9"
        assault_bstorm
        "d5_battle_bulletstorm_10"
        assault_bstorm
        "d5_battle_bulletstorm_11"
        assault_bstorm
        "d5_battle_bulletstorm_12"
        assault_bstorm
        "d5_battle_bulletstorm_13"
        assault_bstorm
        "d5_battle_bulletstorm_14"
        assault_bstorm
        "d5_battle_bulletstorm_15"
        assault_bstorm
        "d5_battle_bulletstorm_16"
        assault_bstorm
        "d5_battle_bulletstorm_17"
        assault_bstorm
        "d5_battle_bulletstorm_18"
        assault_bstorm
        "d5_battle_bulletstorm_19"
        assault_bstorm
        "d5_battle_bulletstorm_20"
        assault_bstorm
        "d5_battle_bulletstorm_21"
        assault_bstorm
        "d5_battle_bulletstorm_22"
        assault_bstorm
        "d5_battle_bulletstorm_23"
        assault_bstorm
        repeat

    image d5_battle_goathand = "locate/cemetery/goat/Goat_hand.png"
    image d5_battle_combat_bunny = "locate/cemetery/Batla_10.png"

    image cpx_d5_cemetery_standoff:
        contains:
            "d5_cemetery_bg_1"
            align (.5, .1)
        contains:
            "d5_cemetery_master 3"
            align (.5, .1)
        contains:
            "d5_battle_combat_bunny"
            align (.5, .1)

    image d5_battle_wolf_knees = "locate/cemetery/bg_cem/knees.png"

    image d5_battle_incar_bg = "locate/forest/Milisiya/V_kabine/kab/kab.png"
    image d5_battle_incar_anton_base = "locate/forest/Milisiya/V_kabine/kab/profil.png"
    image d5_battle_incar_anton_eyes2 = "locate/forest/Milisiya/V_kabine/kab/profil2.png"
    image d5_battle_incar_anton_eyes3 = "locate/forest/Milisiya/V_kabine/kab/profil3.png"
    image d5_battle_incar_anton_blink:
        contains transform_blink(Null(), "d5_battle_incar_anton_eyes2", "d5_battle_incar_anton_eyes3", 2.0)

    image d5_battle_incar_anton = LiveComposite((1920, 1080),
        (0, 0), "d5_battle_incar_anton_base",
        (0, 0), "d5_battle_incar_anton_blink",
        (0, 0), AlphaMask(Solid("#0007"), "d5_battle_incar_anton_base"))

    image d5_battle_incarsolo_base = "locate/forest/Milisiya/Ant.png"
    image d5_battle_incarsolo_base2 = "locate/forest/Milisiya/Ant2.png"
    image d5_battle_incarsolo_talk = "locate/forest/Milisiya/Ant1.png"
    image d5_battle_incarsolo 1 = LiveComposite((1920, 1080),
        (0, 0), "d5_battle_incarsolo_base",
        (0, 0), AlphaMask(Solid("#0007"), "d5_battle_incarsolo_base"))
    image d5_battle_incarsolo 2 = LiveComposite((1920, 1080),
        (0, 0), "d5_battle_incarsolo_base2",
        (0, 0), AlphaMask(Solid("#0007"), "d5_battle_incarsolo_base2"))
    image d5_battle_incarsolo talk = LiveComposite((1920, 1080),
        (0, 0), "d5_battle_incarsolo_base",
        (0, 0), "d5_battle_incarsolo_talk",
        (0, 0), AlphaMask(Solid("#0007"), "d5_battle_incarsolo_base"))

    image d5_battle_incar_hand_base = "locate/forest/Milisiya/V_kabine/kab/hend.png"
    image d5_battle_incar_hand = LiveComposite((1920, 1688),
        (0, 0), "d5_battle_incar_hand_base",
        (0, 0), AlphaMask(Solid("#0007"), "d5_battle_incar_hand_base"))

    image d5_battle_incarhug_base = "locate/forest/Milisiya/V_kabine/Obnim/basa.png"
    image d5_battle_incarhug_olya_eyes_1 = "locate/forest/Milisiya/V_kabine/Obnim/e/Olya/2_eyes/01.png"
    image d5_battle_incarhug_olya_eyes_2 = "locate/forest/Milisiya/V_kabine/Obnim/e/Olya/2_eyes/02.png"
    image d5_battle_incarhug_olya_eyes_3 = "locate/forest/Milisiya/V_kabine/Obnim/e/Olya/2_eyes/03.png"
    image d5_battle_incarhug_olya_mouth_1 = "locate/forest/Milisiya/V_kabine/Obnim/e/Olya/3_mouth/1.png"
    image d5_battle_incarhug_olya_mouth_2 = "locate/forest/Milisiya/V_kabine/Obnim/e/Olya/3_mouth/2.png"
    image d5_battle_incarhug_olya_blink:
        contains transform_blink("d5_battle_incarhug_olya_eyes_1", "d5_battle_incarhug_olya_eyes_2", "d5_battle_incarhug_olya_eyes_3", 0.45)
    image d5_battle_incarhug_anton_eyes_1 = "locate/forest/Milisiya/V_kabine/Obnim/e/Ant/2_eyes/01.png"
    image d5_battle_incarhug_anton_eyes_2 = "locate/forest/Milisiya/V_kabine/Obnim/e/Ant/2_eyes/02.png"
    image d5_battle_incarhug_anton_eyes_3 = "locate/forest/Milisiya/V_kabine/Obnim/e/Ant/2_eyes/03.png"
    image d5_battle_incarhug_anton_mouth_1 = "locate/forest/Milisiya/V_kabine/Obnim/e/Ant/3_mouth/1.png"
    image d5_battle_incarhug_anton_mouth_2 = "locate/forest/Milisiya/V_kabine/Obnim/e/Ant/3_mouth/2.png"
    image d5_battle_incarhug_anton_blink:
        contains transform_blink("d5_battle_incarhug_anton_eyes_1", "d5_battle_incarhug_anton_eyes_2", "d5_battle_incarhug_anton_eyes_3", 1.35)

    layeredimage d5_incarhug:
        always:
            "d5_battle_incarhug_base"
        attribute oshut:
            "d5_battle_incarhug_olya_eyes_3"
        always if_not "oshut":
            "d5_battle_incarhug_olya_blink"
        always:
            "d5_battle_incarhug_anton_blink"

        attribute atalk:
            "d5_battle_incarhug_anton_mouth_2"
        always if_not "atalk":
            "d5_battle_incarhug_anton_mouth_1"

        attribute otalk:
            "d5_battle_incarhug_olya_mouth_2"
        always if_not "otalk":
            "d5_battle_incarhug_olya_mouth_1"

    image d5_battle_incar_choise_neu = "locate/forest/Milisiya/V_kabine/vs/neitral.png"
    image d5_battle_incar_choise_yes = "locate/forest/Milisiya/V_kabine/vs/yes.png"
    image d5_battle_incar_choise_no = "locate/forest/Milisiya/V_kabine/vs/no.png"
    image d5_battle_incar_choise_down = "locate/forest/Milisiya/V_kabine/vs/opustil.png"

    image d5_battle_incar_choise_solo_neu = "locate/forest/Milisiya/V_kabine/vs/neitral_solo.png"
    image d5_battle_incar_choise_solo_yes = "locate/forest/Milisiya/V_kabine/vs/yes_solo.png"
    image d5_battle_incar_choise_solo_no = "locate/forest/Milisiya/V_kabine/vs/no_solo.png"
    image d5_battle_incar_choise_solo_down = "locate/forest/Milisiya/V_kabine/vs/opustil_solo.png"

    image d5_battle_mask_hold_base = "locate/forest/Mask0.png"
    image d5_battle_mask_hold = LiveComposite((1920, 1436),
        (0, 0), "d5_battle_mask_hold_base",
        (0, 0), AlphaMask(Solid("#0007", xysize=(1920, 1436)), "d5_battle_mask_hold_base"))

    image d5_mask_throwaway = "locate/forest/Milisiya/car3/Mask.png"


    image d5_efiba_car0_bg = "locate/forest/Milisiya/car/bg.png"
    image d5_efiba_car0_car = "locate/forest/Milisiya/car/car.png"

    image d5_efiba_car0_anton = ConditionSwitch(
        "Flags.Has('day5 mask')", "d5_aib_forest_anton_big_mask",
        "True", "d5_aib_forest_anton_big_nomask")
    image d5_efiba_car2_olya 01 = "Olya Weeps b_evening_winter 02 good ahead 01 dark 40"
    image d5_efiba_car2_olya 02 = "Olya Weeps b_evening_winter 02 good ahead 05 dark 40"
    image d5_efiba_car2_olya 03 = "Olya Suffer b_evening_winter 02 good ahead 01 dark 40"
    image d5_efiba_car2_olya 04 = "Olya Suffer b_evening_winter 02 good ahead 05 dark 40"
    image d5_efiba_car2_olya 05 = "Olya Suffer b_evening_winter 02 good ahead 04 dark 40"

    image d5_efiba_car2_mask = "sprite/Ant/Anton_dark/mask.png"

    image d5_efiba_car2_arms:
        "locate/forest/Milisiya/car2/arms.png"
        subpixel True
        block:
            ease 2.0 xoffset 0 yoffset -5
            ease 2.0 xoffset 5 yoffset -10
            ease 2.0 xoffset 10 yoffset 0
            ease 2.0 xoffset 5 yoffset -5
            ease 2.0 xoffset 0 yoffset 0
            repeat
    image d5_efiba_car2_z6 = "locate/forest/Milisiya/car2/Z6.png"
    image d5_efiba_car2_bg = "locate/forest/Milisiya/car2/bg.png"
    image d5_efiba_car2_ant_base_1 = "locate/forest/Milisiya/car2/ant2/1.png"
    image d5_efiba_car2_ant_base_2 = "locate/forest/Milisiya/car2/ant2/2.png"
    image d5_efiba_car2_ant_base_3 = "locate/forest/Milisiya/car2/ant2/3.png"

    image d5_efiba_car2_ant_eye_ahead_2 = "locate/forest/Milisiya/car2/ant2/11.png"
    image d5_efiba_car2_ant_eye_ahead_3 = "locate/forest/Milisiya/car2/ant2/12.png"
    image d5_efiba_car2_ant_eye_aside_1 = "locate/forest/Milisiya/car2/ant2/20.png"
    image d5_efiba_car2_ant_eye_aside_2 = "locate/forest/Milisiya/car2/ant2/21.png"
    image d5_efiba_car2_ant_eye_aside_3 = "locate/forest/Milisiya/car2/ant2/22.png"

    image d5_efiba_car2_ant_eye ahead:
        Null()
        choice:
            5.
        choice:
            6.
        choice:
            6.5
        "d5_efiba_car2_ant_eye_ahead_2"
        .1
        "d5_efiba_car2_ant_eye_ahead_3"
        .1
        "d5_efiba_car2_ant_eye_ahead_2"
        .1
        repeat

    image d5_efiba_car2_ant_eye aside:
        "d5_efiba_car2_ant_eye_aside_1"
        choice:
            5.
        choice:
            6.
        choice:
            6.5
        "d5_efiba_car2_ant_eye_aside_2"
        .1
        "d5_efiba_car2_ant_eye_aside_3"
        .1
        "d5_efiba_car2_ant_eye_aside_2"
        .1
        repeat

    image d5_efiba_car2_ant_eye ahead_to_aside:
        Null()
        "d5_efiba_car2_ant_eye_ahead_2"
        .1
        "d5_efiba_car2_ant_eye_ahead_3"
        .1
        "d5_efiba_car2_ant_eye_aside_2"
        .1
        "d5_efiba_car2_ant_eye aside"

    define d5_efiba_car2_ant_base_dark = "#0004"
    image d5_efiba_car2_ant_base 1 ahead:
        contains:
            "d5_efiba_car2_ant_base_1"
        contains:
            "d5_efiba_car2_ant_eye ahead"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_1")
    image d5_efiba_car2_ant_base 2 ahead:
        contains:
            "d5_efiba_car2_ant_base_2"
        contains:
            "d5_efiba_car2_ant_eye ahead"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_2")
    image d5_efiba_car2_ant_base 3 ahead:
        contains:
            "d5_efiba_car2_ant_base_3"
        contains:
            "d5_efiba_car2_ant_eye ahead"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_3")
    image d5_efiba_car2_ant_base 3 ahead cry:
        contains:
            "d5_efiba_car2_ant_base_3"
        contains:
            "d5_efiba_car2_ant_eye ahead"
        contains:
            "d5_efiba_car2_ant_cry"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_3")
    image d5_efiba_car2_ant_base 1 aside:
        contains:
            "d5_efiba_car2_ant_base_1"
        contains:
            "d5_efiba_car2_ant_eye aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_1")
    image d5_efiba_car2_ant_base 2 aside:
        contains:
            "d5_efiba_car2_ant_base_2"
        contains:
            "d5_efiba_car2_ant_eye aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_2")
    image d5_efiba_car2_ant_base 3 aside:
        contains:
            "d5_efiba_car2_ant_base_3"
        contains:
            "d5_efiba_car2_ant_eye aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_3")

    image d5_efiba_car2_ant_base 1 ahead_to_aside:
        contains:
            "d5_efiba_car2_ant_base_1"
        contains:
            "d5_efiba_car2_ant_eye ahead_to_aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_1")
    image d5_efiba_car2_ant_base 2 ahead_to_aside:
        contains:
            "d5_efiba_car2_ant_base_2"
        contains:
            "d5_efiba_car2_ant_eye ahead_to_aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_2")
    image d5_efiba_car2_ant_base 3 ahead_to_aside:
        contains:
            "d5_efiba_car2_ant_base_3"
        contains:
            "d5_efiba_car2_ant_eye ahead_to_aside"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_3")

    image d5_efiba_car2_ant_cry = "locate/forest/Milisiya/car2/ant2/cry.png"

    image d5_efiba_car2_ant_base 1 cry:
        contains:
            "d5_efiba_car2_ant_base_1"
        contains:
            "d5_efiba_car2_ant_eye_aside_3"
        contains:
            "d5_efiba_car2_ant_cry"
        contains:
            AlphaMask(Solid(d5_efiba_car2_ant_base_dark), "d5_efiba_car2_ant_base_1")


    image d5_efiba_car3_bgbg = "locate/forest/Milisiya/car3/bg4.png"
    image d5_efiba_car3_bg 1 = "locate/forest/Milisiya/car3/bg1.png"
    image d5_efiba_car3_bg_overlay = "locate/forest/Milisiya/car3/bg2.png"
    image d5_efiba_car3_bg 2:
        contains:
            "d5_efiba_car3_bg 1"
        contains:
            "d5_efiba_car3_bg_overlay"
    image d5_efiba_car3_bg 3 = "locate/forest/Milisiya/car3/bg3.png"
    image d5_efiba_car3_door = "locate/forest/Milisiya/car3/door.png"

    image d5_efiba_beast_tears = "locate/forest/Milisiya/car3/Z5.png"
    image d5_efiba_beast_base 1 = "locate/forest/Milisiya/car3/Z1.png"
    image d5_efiba_beast_base 2 = "locate/forest/Milisiya/car3/Z2.png"
    image d5_efiba_beast_base 3 = "locate/forest/Milisiya/car3/Z3.png"
    image d5_efiba_beast_base 4 = "locate/forest/Milisiya/car3/Z4.png"
    image d5_efiba_beast_base 5:
        contains:
            "d5_efiba_beast_base 4"
        contains:
            "d5_efiba_beast_tears"
    image d5_efiba_beast_arm 1 = "locate/forest/Milisiya/car3/arm1.png"
    image d5_efiba_beast_arm 2 = "locate/forest/Milisiya/car3/arm2.png"

    image d5_efiba_betray = "locate/cemetery/Tih_end.png"
    image d5_efiba_betray2 = "locate/cemetery/Tih_end2.png"

    image d5_heir_bunny_full = "sprite/Mom/Hare_Mom/Hare_Mom.png"
    image d5_heir_bunny_blood = "sprite/Mom/Hare_Mom/blood.png"
    image d5_heir_bunny = Composite((1920, 3892),
        (0, 0), "d5_heir_bunny_full",
        (0, 0), "d5_heir_bunny_blood")

    image d5_heir_sky = "locate/home/out_side/Meet_beasts/jump/S_1_alt.png"
    image d5_heir_moon = "locate/home/out_side/Meet_beasts/jump/moon_alt.png"
    image d5_heir_trees = "locate/home/out_side/Meet_beasts/jump/S_2_alt.png"

    image d5_heir_hare 1 = "sprite/Mom/Hare_Mom/Hare_01.png"
    image d5_heir_hare 2 = "sprite/Mom/Hare_Mom/Hare_02.png"

    image d5_ekiller_cross_bg = "locate/cemetery/bg_cem/bg.png"

    image d5_efiba_cross_bg = "locate/cemetery/cross_bg.png"
    image d5_efiba_cross_wolf = "locate/cemetery/Cross1.png"
    image d5_efiba_cross_jacket = "locate/cemetery/Cross2.png"
    image d5_efiba_cross_wolf_far = "locate/cemetery/Cross01.png"
    image d5_efiba_cross_jacket_far = "locate/cemetery/Cross02.png"
    image d5_efiba_cross_wolf_far2 = "locate/cemetery/Cross001.png"
    image d5_efiba_cross_jacket_far2 = "locate/cemetery/Cross002.png"


    image d5_slaughter_tihonov_base = "locate/cemetery/tihonov.png"
    image d5_slaughter_tihonov_2 = "locate/cemetery/tihonov02.png"
    image d5_slaughter_tihonov_3 = "locate/cemetery/tihonov03.png"
    image d5_slaughter_tihonov_empty = "locate/cemetery/tihonov05.png"
    image d5_slaughter_tihonov_talk = "locate/cemetery/tihonov04.png"
    image d5_slaughter_tihonov_blink:
        Null()
        1.
        "d5_slaughter_tihonov_2"
        .1
        "d5_slaughter_tihonov_3"
        .1
        "d5_slaughter_tihonov_2"
        .1
        Null()
        block:
            choice:
                5.
            choice:
                7.
        repeat

    image d5_slaughter_tihonov idle:
        contains:
            "d5_slaughter_tihonov_base"
        contains:
            "d5_slaughter_tihonov_blink"

    image d5_slaughter_tihonov talk:
        contains:
            "d5_slaughter_tihonov_base"
        contains:
            "d5_slaughter_tihonov_talk"
        contains:
            "d5_slaughter_tihonov_blink"

    image d5_slaughter_master_bg = "locate/cemetery/goat_fon.png"
    image d5_slaughter_master_fg = "locate/cemetery/goat_00.png"
    image d5_slaughter_master 1 = "locate/cemetery/goat_1.png"
    image d5_slaughter_master 2 = "locate/cemetery/goat_2.png"
    image d5_slaughter_master 3 = "locate/cemetery/goat_3.png"
    image d5_slaughter_master 4 = "locate/cemetery/goat_4.png"
    image d5_slaughter_master 5 = "locate/cemetery/goat_5.png"
    image d5_slaughter_master 6 = "locate/cemetery/goat_6.png"
    image d5_slaughter_master 7 = "locate/cemetery/goat_7.png"
    image d5_slaughter_master 8 = "locate/cemetery/goat_8.png"
    image d5_slaughter_master_tihonov = "locate/cemetery/dead_goat_000.png"

    image d5_slaughter_fox 1 = "locate/cemetery/fox.png"
    image d5_slaughter_fox 2 = "locate/cemetery/fox2.png"
    image d5_slaughter_fox 3 = "locate/cemetery/fox3.png"
    image d5_slaughter_fox 4 = "locate/cemetery/fox4.png"
    image d5_slaughter_fox 5 = "locate/cemetery/fox5.png"

    image d5_slaughter_master 4_hightlight:
        "d5_slaughter_master 4"
        matrixcolor BrightnessMatrix(0.1)

    image d5_slaughter_smoke:
        animation
        "locate/cemetery/smoke2.png"
        yoffset -300
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 120
            linear 45 xpan 360+120
            repeat

    image d5_slaughter_axe_1 = "locate/cemetery/axe/axe01.png"
    image d5_slaughter_axe_2 = "locate/cemetery/axe/axe02.png"
    image d5_slaughter_axe_3 = "locate/cemetery/axe/axe03.png"

    image d5_slaughter_axe dark = Composite((1920, 1080),
        (0, 0), "d5_slaughter_axe_1",
        (0, 0), AlphaMask(Solid("#0008"), "d5_slaughter_axe_1"))

    image d5_slaughter_axe loop:
        animation
        block:
            "d5_slaughter_axe_1"
            .2
            "d5_slaughter_axe_2"
            .2
            repeat

    image d5_slaughter_axe loop_highlight:
        "d5_slaughter_axe loop"
        matrixcolor BrightnessMatrix(0.1)

    default d5_choice_mask_mask_hover = False
    default d5_choice_mask_axe_hover = False

    image d5_slaughter_mask choice = ConditionSwitch(
        "d5_choice_mask_mask_hover", "d5_slaughter_master 4_hightlight",
        True, "d5_slaughter_master 2"
    )
    image d5_slaughter_axe choice = ConditionSwitch(
        "d5_choice_mask_axe_hover", "d5_slaughter_axe loop_highlight",
        True, "d5_slaughter_axe_1"
    )


    image d5_hand:
        "locate/street/gopstop/roma_fight/d5.png"
        subpixel True
        block:
            ease 2.0 xoffset -5 yoffset 10
            ease 2.0 xoffset 2 yoffset 5
            ease 2.0 xoffset 0 yoffset 0
            ease 2.0 xoffset -2 yoffset 5
            ease 2.0 xoffset 5 yoffset 0
            ease 2.0 xoffset 0 yoffset 5
            repeat

    image d5_aib_cross_bg = "locate/forest/salvation/cross/bg.png"
    image d5_aib_cross_cross 1 = "locate/forest/salvation/cross/Cross1.png"
    image d5_aib_cross_cross 2 = "locate/forest/salvation/cross/Cross02.png"
    image d5_aib_cross_cross_smoke = "locate/forest/salvation/cross/Cross03.png"
    image d5_aib_cross_cross 0 = "locate/forest/salvation/cross/Cross_0.png"
    image d5_aib_cross_cross 3 = "locate/forest/salvation/cross/Cross_1.png"
    image d5_aib_cross_cross_4 = "locate/forest/salvation/cross/Cross_2.png"
    image d5_aib_cross_cross_5 = "locate/forest/salvation/cross/Cross_3.png"

    transform d5_shake:
        animation
        subpixel True
        block:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset -5 yoffset -10
            ease 2. xoffset 5 yoffset 0
            ease 2. xoffset 0 yoffset 10
            repeat

    image d5_aib_cross_choice2_hand = "locate/forest/salvation/cross/Cross_0.png"
    image d5_aib_cross_choice2 0 = "d5_aib_cross_choice2_hand"
    image d5_aib_cross_choice2 1 = Composite((1920, 1080),
        (0, 0), "d5_aib_cross_choice2_hand",
        (0, 0), "d5_aib_cross_cross_4")
    image d5_aib_cross_choice2 2 = "d5_aib_cross_cross 1"

    image d5_aib_cross2_bg = "locate/forest/salvation/cross2/bg.png"
    image d5_aib_cross2_cross 1 = "locate/forest/salvation/cross2/Cross-01.png"
    image d5_aib_cross2_cross 2 = "locate/forest/salvation/cross2/Cross-02.png"
    image d5_aib_cross2_cross 3 = "locate/forest/salvation/cross2/Cross-03.png"
    image d5_aib_cross2_cross_id = "locate/forest/salvation/cross2/Cross-04.png"

    image d5_aib_bg_1 = "locate/street/road_to_home(N)/road01.png"
    image d5_aib_bg_2 = "locate/street/road_to_home(N)/road02.png"
    image d5_aib_bg_3 = "locate/street/road_to_home(N)/road03.png"
    image d5_aib_bg_4 = "locate/street/road_to_home(N)/road04.png"

    image d5_aib_eye_bg = "locate/forest/salvation/glass/001.png"
    image d5_aib_eye_fg = "locate/forest/salvation/glass/002.png"
    image d5_aib_eye_blink_1 = "locate/forest/salvation/glass/003.png"
    image d5_aib_eye_blink_2 = "locate/forest/salvation/glass/004.png"
    image d5_aib_eye_blink:
        Null()
        .1
        "d5_aib_eye_blink_1"
        .1
        "d5_aib_eye_blink_2"
        .1
        "d5_aib_eye_blink_1"
        .1
        Null()

    image d5_aib_sky = "locate/home/out_side/Meet_beasts/fon.jpg"

    image d5_aib_forest_anton1_base = "sprite/ant/ant_d/A00.png"
    image d5_aib_forest_anton1_eyes1 = "sprite/ant/ant_d/A01.png"
    image d5_aib_forest_anton1_eyes2 = "sprite/ant/ant_d/A02.png"
    image d5_aib_forest_anton1_eyes3 = "sprite/ant/ant_d/A03.png"
    image d5_aib_forest_anton1_mouth = "sprite/ant/ant_d/m.png"
    image d5_aib_forest_anton1_blink:
        animation
        "d5_aib_forest_anton1_eyes1"
        choice:
            renpy.random.random() * 2 + 4

        choice:
            renpy.random.random() * 2 + 5

        choice:
            renpy.random.random() * 2 + 6
        "d5_aib_forest_anton1_eyes2"
        .1
        "d5_aib_forest_anton1_eyes3"
        .1
        "d5_aib_forest_anton1_eyes2"
        .1
        repeat
    image d5_aib_forest_anton1 idle:
        contains:
            "d5_aib_forest_anton1_base"
        contains:
            "d5_aib_forest_anton1_blink"
    image d5_aib_forest_anton1 talk:
        contains:
            "d5_aib_forest_anton1_base"
        contains:
            "d5_aib_forest_anton1_blink"
        contains:
            "d5_aib_forest_anton1_mouth"

    image d5_aib_forest_anton1 idle dark = LiveComposite((1920, 1080),
        (0, 0), "d5_aib_forest_anton1 idle",
        (0, 0), AlphaMask(Solid("#0002"), "d5_aib_forest_anton1_base"))
    image d5_aib_forest_anton1 talk dark = LiveComposite((1920, 1080),
        (0, 0), "d5_aib_forest_anton1 talk",
        (0, 0), AlphaMask(Solid("#0002"), "d5_aib_forest_anton1_base"))

    image d5_aib_forest_anton2_base = "sprite/ant/Anton_dark/An0.png"
    image d5_aib_forest_anton2_eyes1 = "sprite/ant/Anton_dark/An1.png"
    image d5_aib_forest_anton2_eyes2 = "sprite/ant/Anton_dark/An2.png"
    image d5_aib_forest_anton2_eyes3 = "sprite/ant/Anton_dark/An3.png"
    image d5_aib_forest_anton2_blink:
        animation
        "d5_aib_forest_anton2_eyes1"
        choice:
            renpy.random.random() * 2 + 4

        choice:
            renpy.random.random() * 2 + 5

        choice:
            renpy.random.random() * 2 + 6
        "d5_aib_forest_anton2_eyes2"
        .1
        "d5_aib_forest_anton2_eyes3"
        .1
        "d5_aib_forest_anton2_eyes2"
        .1
        repeat
    image d5_aib_forest_anton2 idle:
        contains:
            "d5_aib_forest_anton2_base"
        contains:
            "d5_aib_forest_anton2_blink"
    image d5_aib_forest_anton2 idle dark = LiveComposite((1920, 1080),
        (0, 0), "d5_aib_forest_anton2 idle",
        (0, 0), AlphaMask(Solid("#0004"), "d5_aib_forest_anton2 idle"))

    image d5_aib_forest_anton2_tears = "sprite/ant/Anton_dark/tears.png"

    image d5_aib_forest_anton_big_base = "sprite/ant/Anton_dark/An.png"
    image d5_aib_forest_anton_big_overlay = "sprite/ant/Anton_dark/mask.png"
    image d5_aib_forest_anton_big_nomask = LiveComposite((1920, 1504),
        (0, 0), "d5_aib_forest_anton_big_base",
        (0, 424), "d5_aib_forest_anton2_blink")
    image d5_aib_forest_anton_big_mask = LiveComposite((1920, 1504),
        (0, 0), "d5_aib_forest_anton_big_base",
        (0, 0), "d5_aib_forest_anton_big_overlay")

    image d5_aib_forest_bg = "locate/forest/salvation/bg.png"
    image d5_aib_forest_bg2 = "locate/forest/salvation/bg2.png"

    image d5_polina_back = "Polina Back small"
    image d5_aib_polina_back = LiveComposite((1920, 1080),
        (0, 0), "d5_polina_back",
        (0, 0), AlphaMask(Solid("#000a"), "d5_polina_back"))


    image d5_olya_back = "sprite/olya/back.png"
    image d5_aib_olya_back = LiveComposite((1920, 1080),
        (0, 0), "d5_olya_back",
        (0, 0), AlphaMask(Solid("#0005"), "d5_olya_back"))

    image d5_aib_fall_1 = "locate/forest/salvation/a01.png"
    image d5_aib_fall_2 = "locate/forest/salvation/a02.png"
    image d5_aib_fall_3 = "locate/forest/salvation/a03.png"
    image d5_aib_fall_4 = "locate/forest/salvation/a04.png"
    image d5_aib_fall_5 = "locate/forest/salvation/a05.png"
    image d5_aib_fall_6 = "locate/forest/salvation/a06.png"
    image d5_aib_fall_7 = "locate/forest/salvation/a07.png"
    image d5_aib_fall_8 = "locate/forest/salvation/a08.png"
    image d5_aib_fall_9 = "locate/forest/salvation/a09.png"
    image d5_aib_fall_10 = "locate/forest/salvation/a10.png"
    image d5_aib_fall_11 = "locate/forest/salvation/a11.png"
    image d5_aib_fall_12 = "locate/forest/salvation/a12.png"
    image d5_aib_fall_13 = "locate/forest/salvation/a13.png"
    image d5_aib_fall_14 = "locate/forest/salvation/a14.png"
    image d5_aib_fall_15 = "locate/forest/salvation/a15.png"
    image d5_aib_fall_16 = "locate/forest/salvation/a16.png"
    image d5_aib_fall_17 = "locate/forest/salvation/a17.png"
    image d5_aib_fall_18 = "locate/forest/salvation/a18.png"
    image d5_aib_fall_19 = "locate/forest/salvation/a19.png"
    image d5_aib_fall_20 = "locate/forest/salvation/a20.png"
    image d5_aib_fall_21 = "locate/forest/salvation/a21.png"
    image d5_aib_fall_22 = "locate/forest/salvation/a22.png"
    image d5_aib_fall_23 = "locate/forest/salvation/a23.png"

    image d5_aib_fall 0 = "d5_aib_fall_1"
    image d5_aib_fall 1:
        "d5_aib_fall_2"
        .1
        "d5_aib_fall_3"
        .1
        "d5_aib_fall_4"
        .1
        "d5_aib_fall_5"
        .1
        "d5_aib_fall_6"
        .1
        "d5_aib_fall_7"
        .1
        "d5_aib_fall_8"
        .1
        "d5_aib_fall_9"
        .1
        "d5_aib_fall_10"
        .1
        "d5_aib_fall_11"
        .1
        "d5_aib_fall_12"
        .1
        "d5_aib_fall_13"
        .1
        block:
            linear .1 yoffset -10
            linear .1 yoffset 10
            repeat 2
        block:
            linear .1 yoffset -4
            linear .1 yoffset 4
            repeat 2
        linear .05 yoffset 0
    image d5_aib_fall 2:
        "d5_aib_fall_14"
        .1
        "d5_aib_fall_15"
        .1
        "d5_aib_fall_16"
        .1
        "d5_aib_fall_17"
        .1
        "d5_aib_fall_18"
        .1
        "d5_aib_fall_19"
        .1
        "d5_aib_fall_20"
        .1
        "d5_aib_fall_21"
        .1
        "d5_aib_fall_22"
        .1
        "d5_aib_fall_23"
        .1
        "bg_black"

    image d5_aib_coming_bg 0 = "locate/forest/salvation/0.png"
    image d5_aib_coming_bg 1 = "locate/forest/salvation/001.png"
    image d5_aib_coming_bg 2 = "locate/forest/salvation/002.png"
    image d5_aib_coming_bg 3 = "locate/forest/salvation/003.png"
    image d5_aib_coming_bg 4 = "locate/forest/salvation/004.png"
    image d5_aib_coming_bg 5 = "locate/forest/salvation/005.png"
    image d5_aib_coming_bg 6 = "locate/forest/salvation/006.png"
    image d5_aib_coming_bg 7 = "locate/forest/salvation/007.png"

    image d5_aib_coming_fg 1 = "locate/forest/salvation/000.png"
    image d5_aib_coming_fg 2 = "locate/forest/salvation/0004.png"
    image d5_aib_coming_fg 3 = "locate/forest/salvation/0005.png"
    image d5_aib_coming_fg 4 = "locate/forest/salvation/0006.png"
    image d5_aib_coming_fg 5 = "locate/forest/salvation/0007.png"

    image d5_aib_coming_masks_bg = "locate/incar/Masks/bg.png"
    image d5_aib_coming_masks_1 = "locate/incar/Masks/mask1.png"
    image d5_aib_coming_masks_2 = "locate/incar/Masks/mask2.png"
    image d5_aib_coming_masks_3 = "locate/incar/Masks/mask3.png"

    image d5_aib_coming_sparks 1:
        contains:
            contains tr_sparks_halfhigh("sparks_2", delay=2.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.35, delay=1.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.55, delay=3.25, stable=0.75, disap=0.25)

    image d5_aib_coming_sparks 2:
        contains:
            contains tr_sparks_halfhigh("sparks_2", delay=2.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.35, delay=1.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.55, delay=3.25, stable=0.75, disap=0.25)

    image d5_aib_coming_sparks 3:
        contains:
            contains tr_sparks_halfhigh("sparks_2", delay=2.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.35, delay=1.5, stable=1., disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.55, delay=3.25, stable=0.75, disap=0.25)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=-0.05, delay=2.25, stable=0.75, disap=0.75)
        contains:
            contains tr_sparks_halfhigh("sparks_2", xal=0.05, delay=2.75, stable=0.75, disap=0.75)

    image d5_aib_coming_angel_base:
        "locate/forest/salvation/arhangel0.png"
        shader "MakeVisualNovels.AnimatedAberration"
        u_aberrationAmount (4.0)
        matrixcolor SaturationMatrix(0.0)

    image d5_aib_coming_angel_glow:
        "locate/forest/salvation/arhangel1.png"
        subpixel True
        alpha 1
        parallel:
            ease 3 alpha 0.0
            ease 3 alpha 1.0
            repeat
        parallel:
            ease 1.15 blur 12
            ease 2.15 blur 4
            ease 1.15 blur 12
            ease 2.15 blur 0
            repeat
    image d5_aib_coming_angel_thing1 = "locate/forest/salvation/arhangel2.png"
    image d5_aib_coming_angel_thing2 = "locate/forest/salvation/arhangel3.png"
    image d5_aib_coming_angel_thing3 = "locate/forest/salvation/arhangel4.png"

    image d5_aib_coming_angel_thing:
        contains:
            "d5_aib_coming_angel_thing1"
            anchor (.5, .5)
            subpixel True
            transform_anchor True
            parallel:
                rotate 0
                linear 15 rotate -360
                repeat
            parallel:
                ease 2 zoom 1.15
                ease 2 zoom 1.00
                repeat
        contains:
            "d5_aib_coming_angel_thing2"
            anchor (.5, .5)
            subpixel True
            transform_anchor True
            block:
                rotate 0
                linear 5 rotate 360
                repeat
        contains:
            "d5_aib_coming_angel_thing3"
            anchor (.5, .5)
            subpixel True
            transform_anchor True
    image d5_aib_coming_angel = LiveComposite( (1920, 1735),
        (0, 0), "d5_aib_coming_angel_base",
        (0, 0), "d5_aib_coming_angel_glow",
        (960, 932), "d5_aib_coming_angel_thing")
    image d5_aib_coming_angel2 = LiveComposite( (1920, 1735),
        (0, 0), "d5_aib_coming_angel_base",
        (0, 0), "d5_aib_coming_angel_glow")

    image d5_aib_car_bg = "incar_polina_bg"
    image d5_aib_car_frame = "body car"
    image d5_aib_car_olya = "locate/incar/mom/Ol.png"
    image d5_aib_car_pol = "locate/incar/mom/P01.png"
    image d5_aib_car_pol_blood = "locate/incar/mom/P02.png"

    image d5_aib_car_beads_1 = "locate/incar/car/Chetki/ch_01.png"
    image d5_aib_car_beads_2 = "locate/incar/car/Chetki/ch_02.png"
    image d5_aib_car_beads_3 = "locate/incar/car/Chetki/ch_03.png"
    image d5_aib_car_beads_4 = "locate/incar/car/Chetki/ch_04.png"
    image d5_aib_car_beads_5 = "locate/incar/car/Chetki/ch_05.png"
    image d5_aib_car_beads_6 = "locate/incar/car/Chetki/ch_06.png"
    image d5_aib_car_beads 1 = "d5_aib_car_beads_1"
    image d5_aib_car_beads loop:
        "d5_aib_car_beads_1"
        .3
        "d5_aib_car_beads_2"
        .3
        "d5_aib_car_beads_3"
        .3
        "d5_aib_car_beads_4"
        .3
        "d5_aib_car_beads_5"
        .3
        "d5_aib_car_beads_6"
        .3
        repeat

    image d5_aib_bstop_bg = "locate/cemetery/stop/bg1.png"
    image d5_aib_bstop_loc_base = "locate/cemetery/stop/bg2.png"
    image d5_aib_bstop_car 1 = "locate/cemetery/stop/m1.png"
    image d5_aib_bstop_car 2 = "locate/cemetery/stop/m2.png"
    image d5_aib_bstop_monster = "locate/cemetery/stop/f1.png"
    image d5_aib_bstop_glass1 = "locate/cemetery/stop/g1.png"
    image d5_aib_bstop_glass2 = "locate/cemetery/stop/g2.png"
    image d5_aib_bstop_stop_1 = "locate/cemetery/stop/o1.png"
    image d5_aib_bstop_stop_2 = "locate/cemetery/stop/o2.png"
    image d5_aib_bstop_polina = "locate/cemetery/stop/Pol.png"
    image d5_aib_bstop_polina_big = "locate/cemetery/stop/Pol2.png"

    image d5_aib_bstop_loc forest = "d5_aib_bstop_loc_base"

    image d5_aib_bstop_loc stop = LiveComposite((4004, 1880),
        (0, 0), "d5_aib_bstop_loc_base",
        (0, 0), "d5_aib_bstop_stop_1")
    image d5_aib_bstop_loc mom = LiveComposite((4004, 1880),
        (0, 0), "d5_aib_bstop_loc_base",
        (0, 0), "d5_aib_bstop_stop_2")
    image d5_aib_bstop_loc monster = LiveComposite((4004, 1880),
        (0, 0), "d5_aib_bstop_loc stop",
        (0, 0), "d5_aib_bstop_monster")
    image d5_aib_bstop_loc polina = LiveComposite((4004, 1880),
        (0, 0), "d5_aib_bstop_loc_base",
        (0, 0), "d5_aib_bstop_polina")

    image d5_anglepic = "locate/home/new/Christmas/picAngel.png"
    image d5_aib_card = "locate/home/new/Christmas/card.png"

    image d5_ending_aib_title_background 0 = "locate/street/Moscow/001.png"
    image d5_ending_aib_title_background 1 = "locate/street/Moscow/002.png"
    image d5_ending_aib_title_background 2 = "locate/street/Moscow/003.png"
    image d5_ending_aib_title_background 3 = "locate/street/Moscow/004.png"
    image d5_ending_aib_title_background 4 = "locate/street/Moscow/005.png"
    image d5_ending_aib_title_background 5 = "locate/street/Moscow/006.png"


    image d5_monchoice_bg = "locate/home/in_side/1st_floor/hall/Koridor/Bg.png"
    image d5_monchoice_planks = "locate/home/in_side/1st_floor/hall/Koridor/dos.png"
    image d5_monchoice_fridge_hover = im.MatrixColor("locate/home/in_side/1st_floor/hall/Koridor/door.png", im.matrix.brightness(0.1))
    image d5_monchoice_ant_idle = "locate/home/in_side/1st_floor/hall/Koridor/ant1.png"
    image d5_monchoice_ant_hover = im.MatrixColor("locate/home/in_side/1st_floor/hall/Koridor/ant2.png", im.matrix.brightness(0.1))
    image d5_monchoice_rom_idle = "locate/home/in_side/1st_floor/hall/Koridor/rom1.png"
    image d5_monchoice_rom_hover = im.MatrixColor("locate/home/in_side/1st_floor/hall/Koridor/rom2.png", im.matrix.brightness(0.1))
    image d5_monchoice_pol_idle = "locate/home/in_side/1st_floor/hall/Koridor/pol2.png"
    image d5_monchoice_pol_hover = im.MatrixColor("locate/home/in_side/1st_floor/hall/Koridor/pol1.png", im.matrix.brightness(0.1))
    image d5_monchoice_oly_idle = "locate/home/in_side/1st_floor/hall/Koridor/ol2.png"
    image d5_monchoice_oly_hover = im.MatrixColor("locate/home/in_side/1st_floor/hall/Koridor/ol1.png", im.matrix.brightness(0.1))


    image d5_aib_incar_scene:
        contains:
            "d5_aib_car_beads loop"
        contains:
            "d5_aib_car_frame"
        contains:
            "d5_aib_car_pol"
        contains:
            "dad car aside"
        contains:
            "mom incar 0"

    default d5_cake_light_state = 0
    python:
        def cake_light_0(trans, st, at):
            global d5_cake_light_state
            d5_cake_light_state = 0
            renpy.restart_interaction()

        def cake_light_1(trans, st, at):
            global d5_cake_light_state
            d5_cake_light_state = 1
            renpy.restart_interaction()

        def cake_light_2(trans, st, at):
            global d5_cake_light_state
            d5_cake_light_state = 2
            renpy.restart_interaction()

        def cake_light_next(trans, st, at):
            global d5_cake_light_state
            d5_cake_light_state = (d5_cake_light_state + 1) % 3
            renpy.restart_interaction()

        def cake_light_rnd(trans, st, at):
            global d5_cake_light_state
            d5_cake_light_state = renpy.random.randint(0, 2)
            renpy.restart_interaction()

    image d5_cake_light stable:
        function cake_light_next
        1.5
        repeat

    image d5_cake_light unstable:
        function cake_light_rnd
        choice:
            0.75
        choice:
            0.25
        repeat

    image d5_cake_kitchen_overlay = "locate/home/new/cake.png"

    image d5_cake_bg3 = "locate/home/new/BG3.png"

    image d5_cake_table = "locate/home/new/Christmas/Table1.png"
    image d5_cake_tree_1 = "locate/home/new/Christmas/Backgroung01.png"
    image d5_cake_tree_2 = "locate/home/new/Christmas/Backgroung02.png"
    image d5_cake_tree_3 = "locate/home/new/Christmas/Backgroung03.png"
    image d5_cake_tree = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_cake_tree_1",
        "d5_cake_light_state == 2", "d5_cake_tree_2",
        "True", "d5_cake_tree_3")
    image d5_cake_present_wrap_1 = "locate/home/new/Christmas/01.png"
    image d5_cake_present_wrap_2 = "locate/home/new/Christmas/02.png"
    image d5_cake_present_wrap_3 = "locate/home/new/Christmas/03.png"
    image d5_cake_present_wrap = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_cake_present_wrap_1",
        "d5_cake_light_state == 2", "d5_cake_present_wrap_2",
        "True", "d5_cake_present_wrap_3")
    image d5_cake_present_unwrap_1 = "locate/home/new/Christmas/e01.png"
    image d5_cake_present_unwrap_2 = "locate/home/new/Christmas/e02.png"
    image d5_cake_present_unwrap_3 = "locate/home/new/Christmas/e03.png"
    image d5_cake_present_unwrap = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_cake_present_unwrap_1",
        "d5_cake_light_state == 2", "d5_cake_present_unwrap_2",
        "True", "d5_cake_present_unwrap_3")
    image d5_cake_present_mask_1 = "locate/home/new/Christmas/m01.png"
    image d5_cake_present_mask_2 = "locate/home/new/Christmas/m02.png"
    image d5_cake_present_mask_3 = "locate/home/new/Christmas/m03.png"
    image d5_cake_present_mask = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_cake_present_mask_1",
        "d5_cake_light_state == 2", "d5_cake_present_mask_2",
        "True", "d5_cake_present_mask_3")
    image d5_cake_present_side_1 = "locate/home/new/Christmas/present01.png"
    image d5_cake_present_side_2 = "locate/home/new/Christmas/present02.png"
    image d5_cake_present_side_3 = "locate/home/new/Christmas/present03.png"
    image d5_cake_present_side = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_cake_present_side_1",
        "d5_cake_light_state == 2", "d5_cake_present_side_2",
        "True", "d5_cake_present_side_3")

    image d5_mask_03:
        "mask_03"
        xalign 0.5
        yalign 0.5
        zoom 1.01
        ease 4.0 zoom 1.71 xalign 0.5 yalign 0.5

    image d5_cake_vision_1 = "locate/home/new/Christmas/Moon1.png"
    image d5_cake_vision_2 = "locate/home/new/Christmas/Moon2.png"

    image d5_cake_glass_1 = "locate/home/new/Christmas/glass01.png"
    image d5_cake_glass_2 = "locate/home/new/Christmas/glass02.png"
    image d5_cake_glass_3 = "locate/home/new/Christmas/glass03.png"
    image d5_cake_glass_1_effect = "locate/home/new/Christmas/glass001.png"
    image d5_cake_glass_2_effect = "locate/home/new/Christmas/glass002.png"
    image d5_cake_glass_3_effect = "locate/home/new/Christmas/glass003.png"

    image d5_cake_knife_base = "locate/home/new/Christmas/Knife01.png"
    image d5_cake_knife_alt:
        "d5_cake_knife_base"
        yzoom 0.95

    image d5_cake_knife 1 = Composite((1920, 1080), (0, 0), "d5_cake_knife_alt")
    image d5_cake_knife 2 = "locate/home/new/Christmas/Knife02.png"


    image d5_crusade_psy_pair = "locate/psycho/pair.png"
    image d5_crusade_psy_polina_pre = "locate/psycho/Pol_big.png"
    image d5_crusade_psy_polina_light = "locate/psycho/Pol_big2.png"
    image d5_crusade_psy_psih = "locate/psycho/psih.png"
    image d5_crusade_psy_aton = "locate/psycho/aton.png"
    image d5_crusade_psy_aton_big = "locate/psycho/aton_big.png"
    image d5_crusade_psy_light1 = "locate/psycho/b/lifgh.png"
    image d5_crusade_psy_light2 = "locate/psycho/b/light2.png"

    image ByashaOld Normal b_day 01 normal ahead 00 dark 30 light = LiveComposite((1920, 1080),
        (0, 0), "ByashaOld Normal b_day 01 normal ahead 00 dark 30",
        (0, 0), "d5_crusade_psy_light1")
    image ByashaOld Normal b_day 01 normal ahead 01 dark 30 light = LiveComposite((1920, 1080),
        (0, 0), "ByashaOld Normal b_day 01 normal ahead 01 dark 30",
        (0, 0), "d5_crusade_psy_light1")
    image ByashaOld Scared b_day 01 shock ahead 00 dark 30 light = LiveComposite((1920, 1080),
        (0, 0), "ByashaOld Scared b_day 01 shock ahead 00 dark 30",
        (0, 0), "d5_crusade_psy_light2")
    image ByashaOld Scared b_day 01 shock ahead 01 dark 30 light = LiveComposite((1920, 1080),
        (0, 0), "ByashaOld Scared b_day 01 shock ahead 01 dark 30",
        (0, 0), "d5_crusade_psy_light2")
















    image d5_crusade_psy_polina_d = AlphaMask(Solid("#0004"), "d5_crusade_psy_polina_pre")
    image d5_crusade_psy_polina:
        contains:
            "d5_crusade_psy_polina_pre"
        contains:
            "d5_crusade_psy_polina_d"

    image ByashaOld ScaredPsy 00 = Composite((1920, 1080),
        (0, 0), "ByashaOld Scared b_day 01 shock ahead 00 dark 30",
        (0, 0), "d5_crusade_psy_light2")
    image ByashaOld ScaredPsy 01 = Composite((1920, 1080),
        (0, 0), "ByashaOld Scared b_day 01 shock ahead 01 dark 30",
        (0, 0), "d5_crusade_psy_light2")

    image d5_crusade_forest_bg = "images/locate/forest/Byash_end/bg.png"
    image d5_crusade_forest_kanistra = "images/locate/forest/Byash_end/kanistra.png"
    image d5_crusade_forest_masks = "images/locate/forest/Byash_end/masks.png"
    image d5_crusade_forest_masks2 = "images/locate/forest/Byash_end/masks2.png"
    image d5_crusade_forest_dudka = "images/locate/forest/Byash_end/dudka.png"
    image d5_crusade_forest_puddle = "images/locate/forest/Byash_end/luga.png"

    image d5_crusade_phone = "images/locate/forest/Byash_end/ant4.png"

    image d5_crusade_memo 0 = "images/locate/forest/Byash_end/memo.png"
    image d5_crusade_memo 1 = "images/locate/forest/Byash_end/memo1.png"
    image d5_crusade_memo 2 = "images/locate/forest/Byash_end/memo2.png"
    image d5_crusade_memo 3 = "images/locate/forest/Byash_end/memo3.png"
    image d5_crusade_memo 4 = "images/locate/forest/Byash_end/memo4.png"

    image d5_crusade_hall_1 = "images/locate/psycho/hallway1.png"
    image d5_crusade_hall_2 = "images/locate/psycho/hallway2.png"
    image d5_crusade_hall_3 = "images/locate/psycho/hallway3.png"

    image d5_crusade_roach 1 = "images/locate/psycho/cockroach1.png"
    image d5_crusade_roach 2 = "images/locate/psycho/cockroach2.png"

    image d5_crusade_stomp_1 = "images/locate/psycho/Pol_01.png"
    image d5_crusade_stomp_2 = "images/locate/psycho/Pol_02.png"
    image d5_crusade_stomp_3 = "images/locate/psycho/Pol_03.png"
    image d5_crusade_stomp_4 = "images/locate/psycho/Pol_04.png"
    image d5_crusade_stomp:
        "d5_crusade_stomp_1"
        .1
        "d5_crusade_stomp_2" with Dissolve(.25)
        .75
        "d5_crusade_stomp_3"
        .1
        "d5_crusade_stomp_4"

    image d5_crusade_durka2 = "images/locate/psycho/durka2.png"
    image d5_crusade_durka3 = "images/locate/psycho/durka3.png"
    image d5_crusade_durka4 = "images/locate/psycho/durka4.png"

    image d5_crusade_anton_gaze 1 = "images/sprite/ant/a001.png"
    image d5_crusade_anton_gaze 2 = "images/sprite/ant/a002.png"
    image d5_crusade_anton_gaze 3 = "images/sprite/ant/a003.png"
    image d5_crusade_anton_gaze 4 = "images/sprite/ant/a004.png"
    image d5_crusade_anton_gaze 5 = "images/sprite/ant/a005.png"
    image d5_crusade_anton_gaze 6 = "images/sprite/ant/a006.png"
    image d5_crusade_anton_gaze_7_1 = "images/sprite/ant/a007.png"
    image d5_crusade_anton_gaze_7_2 = "images/sprite/ant/a008.png"
    image d5_crusade_anton_gaze_7_3 = "images/sprite/ant/a009.png"
    image d5_crusade_anton_gaze 7 = ConditionSwitch(
        "d5_cake_light_state == 1", "d5_crusade_anton_gaze_7_1",
        "d5_cake_light_state == 2", "d5_crusade_anton_gaze_7_2",
        "True", "d5_crusade_anton_gaze_7_3")


    image d5_crusade_forest_anton_phone = "images/locate/forest/Byash_end/ant1.png"
    image d5_crusade_forest_anton_body = "images/locate/forest/Byash_end/ant2.png"
    image d5_crusade_forest_anton_cross = "images/locate/forest/Byash_end/ant3.png"

    image d5_crusade_incar = "images/locate/forest/Byash_end/4/Inside_Car.png"
    image d5_crusade_incar_bg = "images/locate/forest/Byash_end/4/bg.png"
    image d5_crusade_incar_race1 = "images/locate/forest/Byash_end/4/car01.png"
    image d5_crusade_incar_race2 = "images/locate/forest/Byash_end/4/car02.png"

    image d5_crusade_mirror_bg0 = "images/locate/forest/Byash_end/3/bg.png"
    image d5_crusade_mirror_bg1 = "images/locate/forest/Byash_end/3/bg1.png"
    image d5_crusade_mirror_bg2 = "images/locate/forest/Byash_end/3/bg2.png"

    image d5_crusade_mirror_bg_1:
        contains:
            "d5_crusade_mirror_bg0"

            align (0., .5)
            parallel:
                zoom 1.0
                linear 1 zoom 2.0
                repeat
    image d5_crusade_mirror_bg_2:
        contains:
            "d5_crusade_mirror_bg0"
            alpha 0
            align (0., .5)
            1.0
            parallel:
                alpha 1
                zoom 2.0
                linear 1 zoom 3.0 alpha 0
                repeat

    image d5_crusade_gun_hand = "images/locate/forest/Byash_end/hand.png"
    image d5_crusade_gun_bg = "images/locate/forest/Byash_end/kab.png"


    image d4_murder_gallery2_2 = "locate/polina/rom_dark/Gallary3.png"
    image d4_murder_gallery3:
        contains:
            subpixel True
            "d4_murder_gallery2"
            align (.5, .5)
            zoom 1.
            parallel:
                easein 20 zoom 0.68
        contains:
            subpixel True
            "d4_murder_gallery2_2"
            align (.5, .5)
            zoom 1.
            parallel:
                easein 20 zoom 0.80
    image d4_murder_gallery4:
        contains:
            subpixel True
            "d4_murder_gallery2"
            align (.5, .5)
            zoom 2.5
            parallel:
                easein 120 zoom 0.68
        contains:
            subpixel True
            "d4_murder_gallery2_2"
            align (.5, .5)
            zoom 2.5
            parallel:
                easein 120 zoom 0.80

    image byasha_end_body_1 = "images/locate/forest/Byash_end/1/b1.png"
    image byasha_end_body_2 = "images/locate/forest/Byash_end/1/b2.png"
    image byasha_end_body_3 = "images/locate/forest/Byash_end/1/b3.png"
    image byasha_end_body_4 = "images/locate/forest/Byash_end/1/b4.png"
    image byasha_end_body_5 = "images/locate/forest/Byash_end/1/b5.png"
    image byasha_end_body_6 = "images/locate/forest/Byash_end/1/b6.png"
    image byasha_end_body_7 = "images/locate/forest/Byash_end/1/b7.png"
    image byasha_end_body_8 = "images/locate/forest/Byash_end/1/b8.png"
    image byasha_end_body_9 = "images/locate/forest/Byash_end/1/b9.png"
    image byasha_end_body_10 = "images/locate/forest/Byash_end/1/b10.png"
    image byasha_end_body_11 = "images/locate/forest/Byash_end/1/b11.png"
    image byasha_end_body_12 = "images/locate/forest/Byash_end/1/b12.png"
    image byasha_end_body_13 = "images/locate/forest/Byash_end/1/b13.png"
    image byasha_end_body_14 = "images/locate/forest/Byash_end/1/b14.png"
    image byasha_end_body_2_2 = "images/locate/forest/Byash_end/1/b2_2.png"

    image byasha_end_mouth_1 = "images/locate/forest/Byash_end/1/mouth/m_1.png"
    image byasha_end_mouth_2 = "images/locate/forest/Byash_end/1/mouth/m_2.png"
    image byasha_end_mouth_3 = "images/locate/forest/Byash_end/1/mouth/m_3.png"
    image byasha_end_mouth_4 = "images/locate/forest/Byash_end/1/mouth/m_4.png"
    image byasha_end_mouth_5 = "images/locate/forest/Byash_end/1/mouth/m_5.png"
    image byasha_end_mouth_6 = "images/locate/forest/Byash_end/1/mouth/m_6.png"

    image byasha_end_eyes_a_ahead = "images/locate/forest/Byash_end/1/2_eyes/001.png"
    image byasha_end_eyes_a_down = "images/locate/forest/Byash_end/1/2_eyes/01.png"
    image byasha_end_eyes_a_2 = "images/locate/forest/Byash_end/1/2_eyes/002.png"
    image byasha_end_eyes_a_3 = "images/locate/forest/Byash_end/1/2_eyes/003.png"
    image byasha_end_eyes_a blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_a_2"
        .1
        "byasha_end_eyes_a_3"
        .1
        "byasha_end_eyes_a_2"
        .1
        repeat

    image byasha_end_eyes_b_2 = "images/locate/forest/Byash_end/1/4_eyes/02.png"
    image byasha_end_eyes_b_3 = "images/locate/forest/Byash_end/1/4_eyes/03.png"
    image byasha_end_eyes_b blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_b_2"
        .1
        "byasha_end_eyes_b_3"
        .1
        "byasha_end_eyes_b_2"
        .1
        repeat

    image byasha_end_eyes_c_2 = "images/locate/forest/Byash_end/1/6_eyes/02.png"
    image byasha_end_eyes_c_3 = "images/locate/forest/Byash_end/1/6_eyes/03.png"
    image byasha_end_eyes_c blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_c_2"
        .1
        "byasha_end_eyes_c_3"
        .1
        "byasha_end_eyes_c_2"
        .1
        repeat

    image byasha_end_eyes_d_2 = "images/locate/forest/Byash_end/1/10_eyes/02.png"
    image byasha_end_eyes_d_3 = "images/locate/forest/Byash_end/1/10_eyes/03.png"
    image byasha_end_eyes_d blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_d_2"
        .1
        "byasha_end_eyes_d_3"
        .1
        "byasha_end_eyes_d_2"
        .1
        repeat

    image byasha_end_eyes_e1 = "images/locate/forest/Byash_end/1/13_eyes/01.png"
    image byasha_end_eyes_e1_1 = "images/locate/forest/Byash_end/1/13_eyes/01.png"
    image byasha_end_eyes_e1_2 = "images/locate/forest/Byash_end/1/13_eyes/02.png"
    image byasha_end_eyes_e1_3 = "images/locate/forest/Byash_end/1/13_eyes/03.png"
    image byasha_end_eyes_e ahead blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_e1_2"
        .1
        "byasha_end_eyes_e1_3"
        .1
        "byasha_end_eyes_e1_2"
        .1
        repeat

    image byasha_end_eyes_e2 = "images/locate/forest/Byash_end/1/13_eyes/down/01.png"
    image byasha_end_eyes_e2_1 = "images/locate/forest/Byash_end/1/13_eyes/down/01.png"
    image byasha_end_eyes_e2_2 = "images/locate/forest/Byash_end/1/13_eyes/down/02.png"
    image byasha_end_eyes_e2_3 = "images/locate/forest/Byash_end/1/13_eyes/down/03.png"
    image byasha_end_eyes_e down blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_e2_2"
        .1
        "byasha_end_eyes_e2_3"
        .1
        "byasha_end_eyes_e2_2"
        .1
        repeat

    image byasha_end_eyes_f_2 = "images/locate/forest/Byash_end/1/14_eyes/02.png"
    image byasha_end_eyes_f_3 = "images/locate/forest/Byash_end/1/14_eyes/03.png"
    image byasha_end_eyes_f blink:
        Null()
        choice:
            5
        choice:
            6
        choice:
            7
        "byasha_end_eyes_f_2"
        .1
        "byasha_end_eyes_f_3"
        .1
        "byasha_end_eyes_f_2"
        .1
        repeat

    image Byasha End 1 ahead:
        contains:
            "byasha_end_body_1"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 1 down:
        contains:
            "byasha_end_body_1"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 1 ahead talk:
        contains:
            "byasha_end_body_1"
        contains:
            "byasha_end_mouth_1"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 1 down talk:
        contains:
            "byasha_end_body_1"
        contains:
            "byasha_end_mouth_1"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 2 ahead:
        contains:
            "byasha_end_body_2"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 2 down:
        contains:
            "byasha_end_body_2"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 2 ahead talk:
        contains:
            "byasha_end_body_2"
        contains:
            "byasha_end_mouth_1"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 2 scream:
        contains:
            "byasha_end_body_2_2"

    image Byasha End 2 down talk:
        contains:
            "byasha_end_body_2"
        contains:
            "byasha_end_mouth_1"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 3:
        contains:
            "byasha_end_body_3"
    image Byasha End 3 talk:
        contains:
            "byasha_end_body_3"
        contains:
            "byasha_end_mouth_2"
    image Byasha End 4:
        contains:
            "byasha_end_body_4"
        contains:
            "byasha_end_eyes_b blink"
    image Byasha End 5:
        contains:
            "byasha_end_body_5"
        contains:
            "byasha_end_eyes_b blink"
    image Byasha End 6:
        contains:
            "byasha_end_body_6"
        contains:
            "byasha_end_eyes_c blink"
    image Byasha End 7:
        contains:
            "byasha_end_body_7"
        contains:
            "byasha_end_eyes_c blink"
    image Byasha End 8:
        contains:
            "byasha_end_body_8"
        contains:
            "byasha_end_eyes_b blink"
    image Byasha End 9:
        contains:
            "byasha_end_body_9"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 9 down:
        contains:
            "byasha_end_body_9"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 9 talk:
        contains:
            "byasha_end_body_9"
        contains:
            "byasha_end_mouth_3"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 9 down talk:
        contains:
            "byasha_end_body_9"
        contains:
            "byasha_end_mouth_3"
        contains:
            "byasha_end_eyes_a_down"
        contains:
            "byasha_end_eyes_a blink"
    image Byasha End 10:
        contains:
            "byasha_end_body_10"
        contains:
            "byasha_end_eyes_d blink"
    image Byasha End 11:
        contains:
            "byasha_end_body_11"


    image Byasha End 12:
        contains:
            "byasha_end_body_12"
        contains:
            "byasha_end_eyes_a_ahead"
        contains:
            "byasha_end_eyes_a blink"
        contains:
            "byasha_end_mouth_4"
    image Byasha End 13 ahead:
        contains:
            "byasha_end_body_13"
        contains:
            "byasha_end_eyes_e1"
        contains:
            "byasha_end_eyes_e ahead blink"


    image Byasha End 13 down:
        contains:
            "byasha_end_body_13"
        contains:
            "byasha_end_eyes_e2"
        contains:
            "byasha_end_eyes_e down blink"
    image Byasha End 13 ahead talk:
        contains:
            "byasha_end_body_13"
        contains:
            "byasha_end_eyes_e1"
        contains:
            "byasha_end_eyes_e ahead blink"
        contains:
            "byasha_end_mouth_6"
    image Byasha End 13 down talk:
        contains:
            "byasha_end_body_13"
        contains:
            "byasha_end_eyes_e2"
        contains:
            "byasha_end_eyes_e down blink"
        contains:
            "byasha_end_mouth_6"
    image Byasha End 14:
        contains:
            "byasha_end_body_14"
        contains:
            "byasha_end_eyes_f blink"


    image Byasha End 14 talk:
        contains:
            "byasha_end_body_14"
        contains:
            "byasha_end_eyes_f blink"
        contains:
            "byasha_end_mouth_5"

    image Byasha End Crazy:
        "Byasha End 2 ahead "
        choice:
            .2
        choice:
            .5
        "Byasha End 3"
        choice:
            .2
        choice:
            .5
        "Byasha End 2 ahead"
        choice:
            .2
        choice:
            .5
        "Byasha End 4"
        choice:
            .2
        choice:
            .5
        "Byasha End 2 ahead talk"
        choice:
            .2
        choice:
            .5
        "Byasha End 3 talk"
        choice:
            .2
        choice:
            .5
        "Byasha End 2 ahead talk"
        choice:
            .2
        choice:
            .5
        "Byasha End 4"
        choice:
            .2
        choice:
            .5
        repeat

    image d5_crusade_grand1 = "images/locate/forest/Byash_end/grand/01.png"
    image d5_crusade_grand2 = "images/locate/forest/Byash_end/grand/02.png"
    image d5_crusade_grand3 = "images/locate/forest/Byash_end/grand/03.png"
    image d5_crusade_grand:
        "d5_crusade_grand1"
        .1
        "d5_crusade_grand2"
        .1
        "d5_crusade_grand3"
        .1
        repeat

    image byasha_end_angel1 = "images/locate/forest/Byash_end/5/A01.png"
    image byasha_end_angel2 = "images/locate/forest/Byash_end/5/A02.png"
    image byasha_end_angel3 = "images/locate/forest/Byash_end/5/A03.png"

    image byasha_end_angel:
        "byasha_end_angel1"
        .1
        "byasha_end_angel2"
        .1
        "byasha_end_angel3"
        .1
        repeat

    image byasha_end_angel_once:
        "byasha_end_angel1"
        .1
        "byasha_end_angel2"
        .1
        "byasha_end_angel3"
        .1
        Null()

    image byasha_end_bushangel1 = "images/locate/forest/Byash_end/2/01.png"
    image byasha_end_bushangel2 = "images/locate/forest/Byash_end/2/02.png"
    image byasha_end_bushangel3 = "images/locate/forest/Byash_end/2/03.png"
    image byasha_end_bushangel4 = "images/locate/forest/Byash_end/2/04.png"
    image byasha_end_bushangel5 = "images/locate/forest/Byash_end/2/05.png"
    image byasha_end_bushangel:
        "byasha_end_bushangel1"
        .1
        "byasha_end_bushangel2"
        .1
        "byasha_end_bushangel3"
        .1
        "byasha_end_bushangel4"
        .1
        "byasha_end_bushangel5"
        .1
        repeat

    image byasha_end_forest_overview = "images/locate/forest/Byash_end/Trees_01.png"
    image byasha_end_forest_garage_overlay = "images/locate/forest/Byash_end/Trees_11.png"
    image byasha_end_forest_garage_dark_overlay = "images/locate/forest/Byash_end/Trees_12.png"
    image byasha_end_forest_garage_fire = "images/locate/forest/Byash_end/Trees_13.png"
    image byasha_end_forest_garage_fire_overlay = "images/locate/forest/Byash_end/Trees_14.png"
    image byasha_end_forest_angel_1 = "images/locate/forest/Byash_end/Trees_02.png"
    image byasha_end_forest_angel_2 = "images/locate/forest/Byash_end/Trees_03.png"
    image byasha_end_forest_angel_3 = "images/locate/forest/Byash_end/Trees_04.png"
    image byasha_end_forest_angel_4 = "images/locate/forest/Byash_end/Trees_05.png"
    image byasha_end_forest_angel_5 = "images/locate/forest/Byash_end/Trees_06.png"
    image byasha_end_forest_angel_6 = "images/locate/forest/Byash_end/Trees_07.png"
    image byasha_end_forest_angel_7 = "images/locate/forest/Byash_end/Trees_08.png"
    image byasha_end_forest_angel_8 = "images/locate/forest/Byash_end/Trees_09.png"
    image byasha_end_forest_angel_9 = "images/locate/forest/Byash_end/Trees_10.png"
    image byasha_end_forest_angel:
        animation
        "byasha_end_forest_angel_1"
        .1
        "byasha_end_forest_angel_2"
        .1
        "byasha_end_forest_angel_3"
        .1
        "byasha_end_forest_angel_4"
        .1
        "byasha_end_forest_angel_5"
        .1
        "byasha_end_forest_angel_6"
        .1
        "byasha_end_forest_angel_7"
        .1
        "byasha_end_forest_angel_8"
        .1
        "byasha_end_forest_angel_9"
        .1
        repeat

    image byasha_end_forest_overview_angel = Composite((3630, 1342),
        (0, 0), "byasha_end_forest_overview",
        (0, 0), "byasha_end_forest_angel")
    image byasha_end_forest_garage = Composite((3630, 1342),
        (0, 0), "byasha_end_forest_overview",
        (0, 0), "byasha_end_forest_garage_overlay")

    transform blink_transform_nodelay(img1, img2):
        img1


        block:
            function play_lamp_blink_1

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 3

            pause 6

            function play_lamp_blink_2

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 3

            pause 4

            function play_lamp_blink_3

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 2

            pause 6

            function play_lamp_blink_4

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 1

            pause 6

            function play_lamp_blink_5

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 2

            repeat
    image byasha_end_forest_garage_blink_overlay:
        contains blink_transform_nodelay("byasha_end_forest_garage_overlay", "byasha_end_forest_garage_dark_overlay")
    image byasha_end_forest_garage_blink = Composite((3630, 1342),
        (0, 0), "byasha_end_forest_overview",
        (0, 0), "byasha_end_forest_garage_blink_overlay")

    image byasha_end_forest_fire = Composite((3630, 1342),
        (0, 0), "byasha_end_forest_overview",
        (0, 0), "byasha_end_forest_garage_fire")

    image d5_crusade_fanatic_bg = "images/locate/forest/Byash_end/6/bg.png"
    image d5_crusade_fanatic_anton = "images/locate/forest/Byash_end/6/anton.png"
    image d5_crusade_fanatic_saliva = "images/locate/forest/Byash_end/6/saliva.png"

    image d5_crusade_drag_bg = "locate/psycho/byash/g00.png"
    image d5_crusade_drag_byasha = "locate/psycho/byash/b00.png"
    image d5_crusade_drag_polina 1 = "locate/psycho/byash/p01.png"
    image d5_crusade_drag_polina 2 = "locate/psycho/byash/p02.png"

    image d5_crusade_scar_base = "sprite/Polina/Adult/Polina.png"
    image d5_crusade_scar_noscar = "sprite/Polina/Adult/Polina00.png"
    image d5_crusade_scar_mouth = "sprite/Polina/Adult/Polina0.png"
    image d5_crusade_scar_mouth2 = "sprite/Polina/Adult/Polina02.png"
    image d5_crusade_scar_eyes1 = "sprite/Polina/Adult/Polina1.png"
    image d5_crusade_scar_eyes2 = "sprite/Polina/Adult/Polina2.png"
    image d5_crusade_scar_eyes3 = "sprite/Polina/Adult/Polina3.png"
    image d5_crusade_scar_blink:
        animation
        "d5_crusade_scar_eyes1"
        choice:
            6.
        choice:
            7.35
        choice:
            8.72
        "d5_crusade_scar_eyes2"
        .1
        "d5_crusade_scar_eyes3"
        .1
        "d5_crusade_scar_eyes2"
        .1
        repeat
    image d5_crusade_scar:
        contains:
            "d5_crusade_scar_base"
        contains:
            "d5_crusade_scar_blink"
    image d5_crusade_scar talk:
        contains:
            "d5_crusade_scar_base"
        contains:
            "d5_crusade_scar_blink"
        contains:
            "d5_crusade_scar_mouth"

    image d5_crusade_noscar:
        contains:
            "d5_crusade_scar_noscar"
        contains:
            "d5_crusade_scar_blink"
    image d5_crusade_noscar talk:
        contains:
            "d5_crusade_scar_noscar"
        contains:
            "d5_crusade_scar_blink"
        contains:
            "d5_crusade_scar_mouth2"

    image d5_crusade_garage_byasha_1 = "locate/street/garage/knok5/08.png"
    image d5_crusade_garage_byasha_2 = "locate/street/garage/knok5/07.png"
    image d5_crusade_garage_byasha_3 = "locate/street/garage/knok5/02.jpg"

    image d5_crusade_garage1 = "locate/street/garage/The_garage_02.jpg"
    image d5_crusade_garage2 = "locate/street/garage/The_garage_03.jpg"
    image d5_crusade_garage3 = "images/locate/forest/Byash_end/Garage_02.png"
    image d5_crusade_garage_cross = "images/locate/forest/Byash_end/Garage_002.png"
    image d5_crusade_garage4:
        contains:
            "d5_crusade_garage3"
        contains:
            "d5_crusade_garage_cross"
    image d5_crusade_garage5 = "images/locate/forest/Byash_end/Garage_03.png"
    image d5_crusade_garage6 = "images/locate/forest/Byash_end/Garage_04.png"

    image d5_crusade_pair1 = "images/locate/forest/Byash_end/pair.png"
    image d5_crusade_pair2 = "images/locate/forest/Byash_end/pair_02.png"
    image d5_crusade_pair3 = "images/locate/forest/Byash_end/pair_03.png"
    image d5_crusade_pair4 = "images/locate/forest/Byash_end/pair_04.png"
    image d5_crusade_pair_phone = "images/locate/forest/Byash_end/pair2.png"
    image d5_crusade_pair_phone2 = "images/locate/forest/Byash_end/pair3.png"


    image d5_newkozel_born_beasts = "locate/cemetery/b_o.png"
    image d5_newkozel_born_beasts_nowolf = "locate/cemetery/b_o_wolfless.png"

    image d5_newkozel_born_bg = "locate/cemetery/goat/fon.png"
    image d5_newkozel_born_tihonov 1 = "locate/cemetery/goat/GoatMask1.png"
    image d5_newkozel_born_tihonov 2 = "locate/cemetery/goat/GoatMask2.png"
    image d5_newkozel_born_tihonov 3 = "locate/cemetery/goat/GoatMask3.png"
    image d5_newkozel_born_bear = "locate/cemetery/goat/bear.png"
    image d5_newkozel_born_owl = "locate/cemetery/goat/sova.png"
    image d5_newkozel_born_wolf = "locate/cemetery/goat/wolf.png"
    image d5_newkozel_born_fox = "locate/cemetery/goat/fox.png"

    image d5_newkozel_hands_A = "locate/cemetery/end_p/hand_A.png"
    image d5_newkozel_hands_P = "locate/cemetery/end_p/hand_P.png"
    image d5_newkozel_hands_O = "locate/cemetery/end_p/hand_O.png"
    image d5_newkozel_hands_AP = "locate/cemetery/end_p/hands2.png"
    image d5_newkozel_hands_AO = "locate/cemetery/end_p/hands3.png"

    image d5_newkozel_torture_bg = "locate/cemetery/dead_bg.png"
    image d5_newkozel_torture_blood = "locate/cemetery/dead_blood.png"
    image d5_newkozel_torture_gut 1 = "locate/cemetery/Kishki/00.png"
    image d5_newkozel_torture_gut 2 = "locate/cemetery/Kishki/01.png"
    image d5_newkozel_torture_gut 3 = "locate/cemetery/Kishki/02.png"
    image d5_newkozel_torture_gut 4 = "locate/cemetery/Kishki/03.png"
    image d5_newkozel_torture_gut 5 = "locate/cemetery/Kishki/04.png"
    image d5_newkozel_torture_gut 6 = "locate/cemetery/Kishki/05.png"
    image d5_newkozel_torture_gut 7 = "locate/cemetery/Kishki/06.png"
    image d5_newkozel_torture_gut 8 = "locate/cemetery/Kishki/07.png"
    image d5_newkozel_torture_gut 9 = "locate/cemetery/Kishki/08.png"
    image d5_newkozel_torture_master = "locate/cemetery/dead_goat_0.png"
    image d5_newkozel_torture_goat = "locate/cemetery/dead_goat.png"
    image d5_newkozel_torture_goat 1 = "locate/cemetery/dead_goat_00.png"
    image d5_newkozel_torture_goat 2 = "locate/cemetery/dead_goat_01.png"
    image d5_newkozel_torture_goat 3 = "locate/cemetery/dead_goat_02.png"

    image d5_newkozel_torture_gut anim:
        "d5_newkozel_torture_gut 1"
        .1
        "d5_newkozel_torture_gut 2"
        .1
        "d5_newkozel_torture_gut 3"
        .1
        "d5_newkozel_torture_gut 4"
        .1
        "d5_newkozel_torture_gut 5"
        .1
        "d5_newkozel_torture_gut 6"
        .2
        "d5_newkozel_torture_gut 7"
        .1
        "d5_newkozel_torture_gut 8"
        .1
        "d5_newkozel_torture_gut 9"


    image d5_newkozel_dream_dad = "sprite/Dad/Happy/m_day/1_body/00.png"
    image d5_newkozel_dream_mom = Composite((674, 1080),
        (0, 0), "sprite/Mom/Normal/m_day/1_body/05.png",
        (0, 0), "sprite/Mom/Normal/m_day/2_eyes/norm/ahead/01.png")



    image d5_break_mask_bg = "locate/cemetery/mask_end01.png"
    image d5_break_mask = "locate/cemetery/mask_end02.png"

    image d5_break_car_bg = "locate/cemetery/go/Car1.png"
    image d5_break_car_fg = "locate/cemetery/go/Car2.png"

    image d5_break_car_pol = "locate/cemetery/go/Pol.png"
    image d5_break_car_pol2 = "locate/cemetery/go/Pol2.png"
    image d5_break_car_ant 1 = "locate/cemetery/go/Ant_1.png"
    image d5_break_car_ant 2 = "locate/cemetery/go/Ant_2.png"
    image d5_break_car_ant 3 = "locate/cemetery/go/Ant_3.png"
    image d5_break_car_oly 1 = "locate/cemetery/go/Ol_0.png"
    image d5_break_car_oly 2 = "locate/cemetery/go/Ol_1.png"
    image d5_break_car_oly 3 = "locate/cemetery/go/Ol_2.png"

    image d5_break_polcar_bg = "locate/cemetery/bmw/polina/Polina_00.png"
    image d5_break_polcar_polina 0 = "locate/cemetery/bmw/polina/Polina_01.png"
    image d5_break_polcar_smile1 = "locate/cemetery/bmw/polina/Polina_02.png"
    image d5_break_polcar_smile2 = "locate/cemetery/bmw/polina/Polina_03.png"

    image d5_break_polcar_polina 1 = Composite((2339, 1500),
        (0, 0), "d5_break_polcar_polina 0",
        (0, 0), "d5_break_polcar_smile1")
    image d5_break_polcar_polina 2 = Composite((2339, 1500),
        (0, 0), "d5_break_polcar_polina 0",
        (0, 0), "d5_break_polcar_smile2")
    image d5_break_polcar_polina_simp_hover:
        "d5_break_polcar_polina 2"
        matrixcolor BrightnessMatrix(0.15)
    image d5_break_polcar_polina_sigma_hover:
        "d5_break_polcar_polina 0"

    image d5_break_polcar_polina_choice = ConditionSwitch(
        "simp_hover", "d5_break_polcar_polina_simp_hover",
        "sigma_hover", "d5_break_polcar_polina_sigma_hover",
        "True", "d5_break_polcar_polina 1",
    )



    image d5_tale_s1_bg = "locate/tale/1/bg.png"
    image d5_tale_s1_hand_left:
        "locate/tale/1/Hand1.png"
        align (0., .5)
        transform_anchor True
        subpixel True
        xoffset -50
        parallel:
            ease 5 rotate 1
            ease 5 rotate -2
            repeat
    image d5_tale_s1_hand_right:
        "locate/tale/1/Hand2.png"
        align (1., .25)
        transform_anchor True
        subpixel True
        xoffset 50
        yoffset -25
        parallel:
            ease 5 rotate -1
            ease 5 rotate 2
            repeat
    image d5_tale_s1_fg:
        animation
        "locate/tale/1/top.png"
        function WaveShader(amp=1, period=4, speed=1., direction="horisontal")


    image d5_tale_s2_bg = "locate/tale/2/bg.png"
    image d5_tale_s2_star_1 = "locate/tale/2/star1.png"
    image d5_tale_s2_star_2 = "locate/tale/2/star2.png"
    image d5_tale_s2_stars:
        animation
        "d5_tale_s2_star_1"
        1.
        "d5_tale_s2_star_2"
        1.
        repeat

    image d5_tale_s2_moon 1 = "locate/tale/2/moon1.png"
    image d5_tale_s2_moon 2 = "locate/tale/2/moon2.png"
    image d5_tale_s2_moon 3 = "locate/tale/2/moon3.png"
    image d5_tale_s2_moon 4 = "locate/tale/2/moon4.png"
    image d5_tale_s2_moon 5 = "locate/tale/2/moon5.png"

    image d5_tale_s2_bunny = "locate/tale/2/bunny.png"
    image d5_tale_s2_bunny_5 = "locate/tale/2/bunny_5.png"

    image d5_tale_s2_bear_1 = "locate/tale/2/bear1.png"
    image d5_tale_s2_bear_2 = "locate/tale/2/bear2.png"
    image d5_tale_s2_bear_3 = "locate/tale/2/bear3.png"
    image d5_tale_s2_bear_1_5 = "locate/tale/2/bear1_5.png"

    image d5_tale_s2_fox_1 = "locate/tale/2/fox1.png"
    image d5_tale_s2_fox_2 = "locate/tale/2/fox2.png"
    image d5_tale_s2_fox_3 = "locate/tale/2/fox3.png"
    image d5_tale_s2_fox_1_5 = "locate/tale/2/fox1_5.png"

    image d5_tale_s2_owl_1 = "locate/tale/2/owl1.png"
    image d5_tale_s2_owl_2 = "locate/tale/2/owl2.png"
    image d5_tale_s2_owl_3 = "locate/tale/2/owl3.png"
    image d5_tale_s2_owl_1_5 = "locate/tale/2/owl1_5.png"

    image d5_tale_s2_wolf_1 = "locate/tale/2/wolf1.png"
    image d5_tale_s2_wolf_2 = "locate/tale/2/wolf2.png"
    image d5_tale_s2_wolf_3 = "locate/tale/2/wolf3.png"
    image d5_tale_s2_wolf_1_5 = "locate/tale/2/wolf1_5.png"

    image d5_tale_s2_full 1 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 1",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_1",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_1")
    image d5_tale_s2_full 2 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 1",
        (0, 0), "d5_tale_s2_bunny",
        
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_1")
    image d5_tale_s2_full 3 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 2",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_2",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_1",)
    image d5_tale_s2_full 4 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 2",
        (0, 0), "d5_tale_s2_bunny",
        
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_1",)
    image d5_tale_s2_full 5 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 2",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_1",)
    image d5_tale_s2_full 6 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 2",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        
        )
    image d5_tale_s2_full 7 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 3",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_2",
        )
    image d5_tale_s2_full 8 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 3",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        
        )
    image d5_tale_s2_full 9 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 3",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_1",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 10 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 3",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 11 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 4",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_2",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 12 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 4",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 13 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 4",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        (0, 0), "d5_tale_s2_owl_1",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 14 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 4",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 15 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 5",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        (0, 0), "d5_tale_s2_owl_2",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 16 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 5",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 17 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 5",
        (0, 0), "d5_tale_s2_bunny",
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        (0, 0), "d5_tale_s2_owl_3",
        (0, 0), "d5_tale_s2_wolf_3",
        )
    image d5_tale_s2_full 18 = Composite((1920, 2160),
        (0, 0), "d5_tale_s2_bg",
        (0, 0), "d5_tale_s2_stars",
        (0, 0), "d5_tale_s2_moon 5",
        
        (0, 0), "d5_tale_s2_bear_3",
        (0, 0), "d5_tale_s2_fox_3",
        (0, 0), "d5_tale_s2_owl_3",
        (0, 0), "d5_tale_s2_wolf_3",
        )


    image d5_tale_s3_bg = "locate/tale/3/bg.png"
    image d5_tale_s3_bunny_1 = "locate/tale/3/bunny.png"
    image d5_tale_s3_bunny_2 = "locate/tale/3/bunny2.png"


    image d5_end_amulet_ravine_bg_1 = "locate/cemetery/ravine/Bg1.png"
    image d5_end_amulet_ravine_bg_2 = "locate/cemetery/ravine/Bg2.png"
    image d5_end_amulet_ravine_polina = "locate/cemetery/ravine/polin.png"

    image d5_end_amulet_ravine_moon = "locate/cemetery/ravine/branches_sky.png"
    image d5_end_amulet_ravine_branches:
        "locate/cemetery/ravine/branches.png"
        subpixel True
        block:
            ypan 0
            linear 2 ypan 360
            repeat

    image d5_end_amulet_deepf_bg1 = "locate/cemetery/ravine/wood1.png"
    image d5_end_amulet_deepf_bg2 = "locate/cemetery/ravine/wood2.png"
    image d5_end_amulet_deepf_bg3 = "locate/cemetery/ravine/wood3.png"
    image d5_end_amulet_deepf_bg4 = "locate/cemetery/ravine/wood4.png"

    image d5_end_amulet_deepf_polina 11 = "locate/cemetery/ravine/Pol1.png"
    image d5_end_amulet_deepf_polina 12 = "locate/cemetery/ravine/Pol01.png"
    image d5_end_amulet_deepf_polina 21 = "locate/cemetery/ravine/Pol2.png"
    image d5_end_amulet_deepf_polina 22 = "locate/cemetery/ravine/Pol02.png"

    image d5_end_amulet_ravine_1_bg = "locate/cemetery/ravine/ravine03.png"
    image d5_end_amulet_ravine_2_bg = "locate/cemetery/ravine/ravine01.png"
    image d5_end_amulet_ravine_2_fg = "locate/cemetery/ravine/ravine02.png"

    image d5_end_amulet_ravine_bear 1 = "locate/cemetery/ravine/bear01.png"
    image d5_end_amulet_ravine_bear 2 = "locate/cemetery/ravine/bear02.png"

    image d5_end_amulet_ravine_wolf_m = "locate/cemetery/ravine/Wolf.png"
    image d5_end_amulet_ravine_wolf = "locate/cemetery/ravine/Wolf2.png"

    image d5_end_amulet_ravine_owl idle = "locate/cemetery/ravine/owl01.png"
    image d5_end_amulet_ravine_owl talk = "locate/cemetery/ravine/owl02.png"

    image d5_end_amulet_ravine_owl2 idle = "locate/cemetery/ravine/owl1.png"
    image d5_end_amulet_ravine_owl2 talk = "locate/cemetery/ravine/owl2.png"
    image d5_end_amulet_ravine_owl2 wings = "locate/cemetery/ravine/owl3.png"

    image d5_end_amulet_ravine_goat_b talk = "locate/cemetery/ravine/master_big.png"
    image d5_end_amulet_ravine_goat_b idle:
        contains:
            "d5_end_amulet_ravine_goat_b talk"
        contains:
            "locate/cemetery/ravine/master_big2.png"
    image d5_end_amulet_ravine_goat = "locate/cemetery/ravine/master.png"

    image Polina Bunnied m_winter 01 shut ahead 01:
        contains:
            "Polina Bunnied m_winter 01 afraid ahead 01"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/03.png"
            .1

    image Polina Bunnied m_winter 01 shut ahead 02:
        contains:
            "Polina Bunnied m_winter 01 afraid ahead 02"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/03.png"
            .1

    image Polina Bunnied m_winter 01 shut ahead 03:
        contains:
            "Polina Bunnied m_winter 01 afraid ahead 03"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/ahead/03.png"
            .1

    image Polina Bunnied m_winter 01 shut aside 01:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 01"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"
            .1

    image Polina Bunnied m_winter 01 shut aside 02:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 02"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"
            .1

    image Polina Bunnied m_winter 01 shut aside 03:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 03"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/01.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/02.png"
            .1
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"
            .1

    image Polina Bunnied m_winter 01 closed 01:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 01"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"
    image Polina Bunnied m_winter 01 closed 02:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 02"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"
    image Polina Bunnied m_winter 01 closed 03:
        contains:
            "Polina Bunnied m_winter 01 afraid aside 03"
        contains:
            "sprite/Polina/Bunnied/m_winter/2_eyes/afraid/aside/03.png"

    image d5_end_amulet_moth_1 = "locate/cemetery/ravine/end/Moth1.png"
    image d5_end_amulet_moth_2 = "locate/cemetery/ravine/end/Moth2.png"
    image d5_end_amulet_moth_3 = "locate/cemetery/ravine/end/Moth3.png"
    image d5_end_amulet_moth_4 = "locate/cemetery/ravine/end/Moth4.png"
    image d5_end_amulet_moth_5 = "locate/cemetery/ravine/end/Moth5.png"
    image d5_end_amulet_moth_6 = "locate/cemetery/ravine/end/Moth6.png"
    image d5_end_amulet_moth:
        animation
        "d5_end_amulet_moth_1"
        .1
        "d5_end_amulet_moth_2"
        .1
        "d5_end_amulet_moth_3"
        .1
        "d5_end_amulet_moth_4"
        .1
        "d5_end_amulet_moth_5"
        .1
        "d5_end_amulet_moth_6"
        .1
        repeat

    image d5_end_amulet_ladyb 1 = "locate/cemetery/ravine/end/Hare1.png"
    image d5_end_amulet_ladyb 2 = "locate/cemetery/ravine/end/Hare2.png"

    image d5_end_amulet_slides_bg = "locate/cemetery/slides/bg.png"
    image d5_end_amulet_slides_legs = "locate/cemetery/slides/legs.png"

    image d5_end_amulet_moon_bg = "locate/cemetery/ravine/Olya_moon/Bg1.png"
    image d5_end_amulet_moon_fg = "locate/cemetery/ravine/Olya_moon/Bg2.png"
    image d5_end_amulet_moon_olywl 1 = "locate/cemetery/ravine/Olya_moon/Olya.png"
    image d5_end_amulet_moon_olywl alt = "locate/cemetery/ravine/Olya_moon/Olya_amulet.png"
    image d5_end_amulet_moon_olywl 2 = "locate/cemetery/ravine/Olya_moon/Olya2.png"
    image d5_end_amulet_moon_olywl 3 = "locate/cemetery/ravine/Olya_moon/Olya3.png"
    image d5_end_amulet_moon_olywl 4 = "locate/cemetery/ravine/Olya_moon/Olya4.png"
    image d5_end_amulet_moon_olywl 5 = "locate/cemetery/ravine/Olya_moon/Olya5.png"
    image d5_end_amulet_moon_olywl 6 = "locate/cemetery/ravine/Olya_moon/Olya6.png"
    image d5_end_amulet_moon_olywl 7 = "locate/cemetery/ravine/Olya_moon/Olya7.png"
    image d5_end_amulet_moon_olywl 8 = "locate/cemetery/ravine/Olya_moon/Olya8.png"
    image d5_end_amulet_moon_olywl 9 = "locate/cemetery/ravine/Olya_moon/Olya9.png"
    image d5_end_amulet_moon_olywl 10 = "locate/cemetery/ravine/Olya_moon/Olya10.png"
    image d5_end_amulet_moon_owl 1 = "locate/cemetery/ravine/Olya_moon/Owl.png"
    image d5_end_amulet_moon_owl 2 = "locate/cemetery/ravine/Olya_moon/Owl1.png"
    image d5_end_amulet_moon_owl 3 = "locate/cemetery/ravine/Olya_moon/Owl2.png"

    image d5_end_amulet_were_bg = "locate/forest/woolf/bg.png"
    image d5_end_amulet_were_dust = "locate/forest/woolf/Dust.png"
    image d5_end_amulet_were_mask = "locate/forest/woolf/mask.png"
    image d5_end_amulet_were_mask2 = "locate/forest/woolf/mask0.png"
    image d5_end_amulet_were_smoke:
        "locate/forest/woolf/smoke.png"
        function WaveShader(amp=1, period=15, speed=.04, direction="horisontal")
    image d5_end_amulet_were_wolf 1a = "locate/forest/woolf/Wolf01.png"
    image d5_end_amulet_were_wolf 2 = "locate/forest/woolf/Wolf02.png"
    image d5_end_amulet_were_wolf 3 = "locate/forest/woolf/Wolf03.png"
    image d5_end_amulet_were_wolf 4 = "locate/forest/woolf/Wolf04.png"
    image d5_end_amulet_were_wolf 1b:
        contains:
            "d5_end_amulet_were_wolf 1a"
        contains:
            "d5_end_amulet_were_mask"

    image d5_end_amulet_stab_anton = "locate/cemetery/ravine/mask/Back01.png"
    image d5_end_amulet_stab_knife 0 = "locate/cemetery/ravine/mask/Back02.png"
    image d5_end_amulet_stab_knife 1 = "locate/cemetery/ravine/mask/Back03.png"

    image d5_eyeblind = "locate/cemetery/ravine/Mask/dark.png"

    image d5_end_amulet_convert_rom 1 = "locate/cemetery/ravine/mask/Rom1.png"
    image d5_end_amulet_convert_rom 2 = "locate/cemetery/ravine/mask/Rom2.png"
    image d5_end_amulet_convert_goat = "locate/cemetery/ravine/mask/k3.png"
    image d5_end_amulet_convert_goat_hand = "locate/cemetery/ravine/mask/k4.png"
    image d5_end_amulet_convert_sewing = "locate/cemetery/ravine/mask/k5.png"
    image d5_end_amulet_convert_drop_1_1 = "locate/cemetery/ravine/mask/Bl1.png"
    image d5_end_amulet_convert_drop_1_2 = "locate/cemetery/ravine/mask/Bl2.png"
    image d5_end_amulet_convert_drop_1_3 = "locate/cemetery/ravine/mask/Bl3.png"
    image d5_end_amulet_convert_drop_1_4 = "locate/cemetery/ravine/mask/Bl4.png"
    image d5_end_amulet_convert_drop_1_5 = "locate/cemetery/ravine/mask/Bl5.png"
    image d5_end_amulet_convert_drop_1_6 = "locate/cemetery/ravine/mask/Bl6.png"
    image d5_end_amulet_convert_drop_1:
        "d5_end_amulet_convert_drop_1_1"
        .1
        "d5_end_amulet_convert_drop_1_2"
        .1
        "d5_end_amulet_convert_drop_1_3"
        .1
        "d5_end_amulet_convert_drop_1_4"
        .1
        "d5_end_amulet_convert_drop_1_5"
        .1
        "d5_end_amulet_convert_drop_1_6"
        .1
        Null()

    image d5_end_amulet_convert_drop_2_1 = "locate/cemetery/ravine/mask/Blo1.png"
    image d5_end_amulet_convert_drop_2_2 = "locate/cemetery/ravine/mask/Blo2.png"
    image d5_end_amulet_convert_drop_2_3 = "locate/cemetery/ravine/mask/Blo3.png"
    image d5_end_amulet_convert_drop_2_4 = "locate/cemetery/ravine/mask/Blo4.png"
    image d5_end_amulet_convert_drop_2_5 = "locate/cemetery/ravine/mask/Blo5.png"
    image d5_end_amulet_convert_drop_2_6 = "locate/cemetery/ravine/mask/Blo6.png"
    image d5_end_amulet_convert_drop_2:
        "d5_end_amulet_convert_drop_2_1"
        .1
        "d5_end_amulet_convert_drop_2_2"
        .1
        "d5_end_amulet_convert_drop_2_3"
        .1
        "d5_end_amulet_convert_drop_2_4"
        .1
        "d5_end_amulet_convert_drop_2_5"
        .1
        "d5_end_amulet_convert_drop_2_6"
        .1
        Null()

    image d5_end_amulet_convert_drop_3_1 = "locate/cemetery/ravine/mask/Blod1.png"
    image d5_end_amulet_convert_drop_3_2 = "locate/cemetery/ravine/mask/Blod2.png"
    image d5_end_amulet_convert_drop_3_3 = "locate/cemetery/ravine/mask/Blod3.png"
    image d5_end_amulet_convert_drop_3_4 = "locate/cemetery/ravine/mask/Blod4.png"
    image d5_end_amulet_convert_drop_3_5 = "locate/cemetery/ravine/mask/Blod5.png"
    image d5_end_amulet_convert_drop_3_6 = "locate/cemetery/ravine/mask/Blod6.png"
    image d5_end_amulet_convert_drop_3:
        "d5_end_amulet_convert_drop_3_1"
        .1
        "d5_end_amulet_convert_drop_3_2"
        .1
        "d5_end_amulet_convert_drop_3_3"
        .1
        "d5_end_amulet_convert_drop_3_4"
        .1
        "d5_end_amulet_convert_drop_3_5"
        .1
        "d5_end_amulet_convert_drop_3_6"
        .1
        Null()

    image d5_end_amulet_convert_mask = "locate/cemetery/ravine/mask/Mask_9.png"
    image d5_end_amulet_convert_flash_1 = "locate/cemetery/ravine/mask/Mask_10.png"
    image d5_end_amulet_convert_flash_2 = "locate/cemetery/ravine/mask/Mask_11.png"
    image d5_end_amulet_convert_flash_3 = "locate/cemetery/ravine/mask/Mask_12.png"
    image d5_end_amulet_convert_flash_4 = "locate/cemetery/ravine/mask/Mask_13.png"
    image d5_end_amulet_convert_flash_blink:
        "d5_end_amulet_convert_flash_1"
        .1
        "d5_end_amulet_convert_flash_2" with Dissolve(.1)
        .1
        "d5_end_amulet_convert_flash_3" with Dissolve(.1)
        .1
        "d5_end_amulet_convert_flash_4" with Dissolve(.1)
        .1
        "d5_end_amulet_convert_flash_1" with Dissolve(.1)

    image d5_end_amulet_convert_mask glow = Composite((2273, 1614),
        (0, 0), "d5_end_amulet_convert_mask",
        (0, 0), "d5_end_amulet_convert_flash_1")

    image d5_end_amulet_convert_mask blink = Composite((2273, 1614),
        (0, 0), "d5_end_amulet_convert_mask",
        (0, 0), "d5_end_amulet_convert_flash_blink")

    image d5_end_ravine_bg = "locate/cemetery/ravine/the_end/bg.png"
    image d5_end_ravine_goat 0 = "locate/cemetery/ravine/the_end/goat0.png"
    image d5_end_ravine_goat 1_stable:
        "locate/cemetery/ravine/the_end/goat1.png"
    image d5_end_ravine_goat 1_wave:
        "locate/cemetery/ravine/the_end/goat1.png"
        function WaveShader(amp=4, period=2, speed=.3, direction="both", double="both", melt="both")
    image d5_end_ravine_goat 1:
        contains:
            "d5_end_ravine_goat 1_wave"
            alpha 1
            1.
            linear 1 alpha 0
        contains:
            "d5_end_ravine_goat 1_stable"
            alpha 0
            1.
            linear 1 alpha 1

    image d5_end_ravine_goat 2_stable:
        "locate/cemetery/ravine/the_end/goat2.png"
    image d5_end_ravine_goat 2_wave:
        "locate/cemetery/ravine/the_end/goat2.png"
        function WaveShader(amp=4, period=2, speed=.3, direction="both", double="both", melt="both")
    image d5_end_ravine_goat 2:
        contains:
            "d5_end_ravine_goat 2_wave"
            alpha 1
            1.
            linear 1 alpha 0
        contains:
            "d5_end_ravine_goat 2_stable"
            alpha 0
            1.
            linear 1 alpha 1

    image d5_end_ravine_wolf 0 = "locate/cemetery/ravine/the_end/Rom.png"
    image d5_end_ravine_wolf 1 = "locate/cemetery/ravine/the_end/Wolf.png"
    image d5_end_ravine_wolf 2:
        "d5_end_ravine_wolf 1"
        easein .25 yzoom .95
        parallel:
            easeout .5 xoffset -500
        parallel:
            easein .5 yoffset -100
        parallel:
            easeout .25 yzoom 1.
        parallel:
            linear .25 alpha 0

    image d5_end_ravine_big_wolf 1 = "locate/cemetery/ravine/the_end/Wolf01.png"
    image d5_end_ravine_big_wolf 2 = "locate/cemetery/ravine/the_end/Wolf02.png"
    image d5_end_ravine_big_wolf 3 = "locate/cemetery/ravine/the_end/Wolf03.png"

    image d5_end_ravine_bear 0 = "locate/cemetery/ravine/the_end/Bear0.png"
    image d5_end_ravine_bear 1_stable:
        "locate/cemetery/ravine/the_end/Bear.png"
    image d5_end_ravine_bear 1_wave:
        "locate/cemetery/ravine/the_end/Bear.png"
        function WaveShader(amp=4, period=2, speed=.3, direction="both", double="both", melt="both")
    image d5_end_ravine_bear 1:
        contains:
            "d5_end_ravine_bear 1_wave"
            alpha 1
            1.
            linear 1 alpha 0
        contains:
            "d5_end_ravine_bear 1_stable"
            alpha 0
            1.
            linear 1 alpha 1

    define er_zoom = 0.85
    define er_zoom_rev = 1.0 / er_zoom
    define er_align_l = (0.413, 0.764)
    define er_align_r = (0.936, 0.153)

    image d5_end_ravine_lins left:
        "locate/cemetery/ravine/the_end/linza_1.png"
        align er_align_l
        zoom er_zoom
    image d5_end_ravine_lins right:
        "locate/cemetery/ravine/the_end/linza_2.png"
        align er_align_r
        zoom er_zoom
    image d5_end_ravine_glasses = "locate/cemetery/ravine/the_end/glasses.png"

    layeredimage d5_end_ravine:
        always "d5_end_ravine_bg":
            align (.5, 1.)

        always "d5s_battle_mid":
            align (.5, 1.)

        attribute wolf0 "d5_end_ravine_wolf 0":
            align (.5, 1.)
        attribute wolf1 "d5_end_ravine_wolf 1":
            align (.5, 1.)
        attribute wolf2 "d5_end_ravine_wolf 2":
            align (.5, 1.)
        attribute bear0 "d5_end_ravine_bear 0":
            align (.5, 1.)
        attribute bear1_st "d5_end_ravine_bear 1_stable":
            align (.5, 1.)
        attribute bear1_tr "d5_end_ravine_bear 1":
            align (.5, 1.)
        attribute goat0 "d5_end_ravine_goat 0":
            align (.5, 1.)
        attribute goat1 "d5_end_ravine_goat 1":
            align (.5, 1.)
        attribute goat1_st "d5_end_ravine_goat 1_stable":
            align (.5, 1.)
        attribute goat2 "d5_end_ravine_goat 2":
            align (.5, 1.)

        always "d5s_battle_fg_solo":
            align (.5, 1.)

    image d5_end_ravine_lins goat0 bear0:
        contains:
            AlphaMask("d5_end_ravine goat0 bear0", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat0 bear0", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat0 bear0 wolf0:
        contains:
            AlphaMask("d5_end_ravine goat0 bear0 wolf0", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat0 bear0 wolf0", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat0 bear0 wolf1:
        contains:
            AlphaMask("d5_end_ravine goat0 bear0 wolf1", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat0 bear0 wolf1", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat1 bear1_tr wolf1:
        contains:
            AlphaMask("d5_end_ravine goat1 bear1_tr wolf1", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat1 bear1_tr wolf1", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat1 bear1_st wolf1:
        contains:
            AlphaMask("d5_end_ravine goat1 bear1_st wolf1", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat1 bear1_st wolf1", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat2 bear1_st wolf1:
        contains:
            AlphaMask("d5_end_ravine goat2 bear1_st wolf1", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat2 bear1_st wolf1", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat1_st bear1_st wolf2:
        contains:
            AlphaMask("d5_end_ravine goat1_st bear1_st wolf2", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat1_st bear1_st wolf2", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_ravine_lins goat1_st bear1_st:
        contains:
            AlphaMask("d5_end_ravine goat1_st bear1_st", "d5_end_ravine_lins left")
            align er_align_l
            zoom er_zoom_rev
        contains:
            AlphaMask("d5_end_ravine goat1_st bear1_st", "d5_end_ravine_lins right")
            align er_align_r
            zoom er_zoom_rev
        contains:
            "d5_end_ravine_glasses"

    image d5_end_blood:
        blur 4
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_1")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_2")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_3")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_4")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_5")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_6")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_7")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_8")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_9")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_10")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_11")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_12")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_13")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_14")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_15")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_16")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_17")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_18")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_19")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_20")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_21")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_22")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_23")
        bd_dt
        AlphaMask(Solid("#000", xysize=(1920, 1080)), "d4_sk_katya_blood_24")
        bd_dt
        Null()



    image d5e_smart = "end/Polina.png"

    image old_movie_superintense:
        "effect/old_movie/old_movie_001.png"
        .10
        Null()
        .10
        "effect/old_movie/old_movie_002.png"
        .10
        Null()
        .20
        "effect/old_movie/old_movie_003.png"
        .10
        Null()
        .10
        "effect/old_movie/old_movie_004.png"
        .10
        Null()
        .20
        repeat

    image d5_smart_kitchen_bg = "locate/home/new/BG1.png"
    image d5_smart_kitchen_bg2 = "locate/home/new/BG2.png"
    image d5_smart_kitchen_molbert = "locate/home/new/molbert.png"

    image d5_smart_molbert_0 = "locate/home/new/close_up/bg00.png"
    image d5_smart_molbert_1 = "locate/home/new/close_up/bg01.png"

    image d5_smart_bg_0 = "locate/home/new/close_up/bg0.png"
    image d5_smart_bg_1 = "locate/home/new/close_up/bg1.png"
    image d5_smart_bg_2 = "locate/home/new/close_up/bg2.png"
    image d5_smart_bg_3 = "locate/home/new/close_up/bg3.png"

    image d5_smart_edge = "locate/home/new/planshet/3/01.png"
    image d5_smart_gun = "locate/home/new/planshet/3/02.png"
    image d5_smart_last = "locate/home/new/planshet/3/03.png"

    image d5_smart_window 1 = "locate/home/new/Window01.png"
    image d5_smart_window 2 = "locate/home/new/Window02.png"
    image d5_smart_window_overlay = "locate/home/new/Window03.png"
    image d5_smart_window 4 = "locate/home/new/Window04.png"

    image d5_smart_diary = "locate/home/new/planshet/1/dairy.png"
    image d5_smart_tablet 0 = "locate/home/new/planshet/1/000.png"
    image d5_smart_tablet 1 = "locate/home/new/planshet/1/001.png"
    image d5_smart_tablet 2 = "locate/home/new/planshet/1/002.png"
    image d5_smart_tablet 3 = "locate/home/new/planshet/1/003.png"
    image d5_smart_tablet 4 = "locate/home/new/planshet/1/004.png"
    image d5_smart_tablet 5 = "locate/home/new/planshet/1/005.png"
    image d5_smart_tablet 6 = "locate/home/new/planshet/1/006.png"
    image d5_smart_tablet 7 = "locate/home/new/planshet/1/007.png"
    image d5_smart_tablet 8 = "locate/home/new/planshet/1/008.png"
    image d5_smart_tablet 9 = "locate/home/new/planshet/1/009.png"

    image d5_smart_tablet_bg = "locate/home/new/planshet/1/bg.png"
    image d5_smart_tablet_cup empty = "locate/home/new/planshet/1/cup.png"
    image d5_smart_tablet_cup full = "locate/home/new/planshet/1/cup2.png"
    image d5_smart_tablet_steam = "locate/home/new/planshet/1/smoke.png"
    image d5_smart_tablet_stain = "locate/home/new/planshet/1/stain.png"

    image d5_smart_wall_base = "locate/home/new/planshet/2/bg.png"
    image d5_smart_wall_hole = "locate/home/new/planshet/2/bg2.png"
    image d5_smart_wall_shadow = "locate/home/new/planshet/2/bg3.png"
    image d5_smart_wall_tablet = "locate/home/new/planshet/2/p0.png"
    image d5_smart_wall_broken = "locate/home/new/planshet/2/p2.png"
    image d5_smart_wall_shards1 = "locate/home/new/planshet/2/oskolki1.png"
    image d5_smart_wall_shards2 = "locate/home/new/planshet/2/oskolki2.png"

    image d5_smart_workshop1 = "locate/home/new/Workshop1.png"
    image d5_smart_workshop2 = "locate/home/new/Workshop2.png"
    image d5_smart_workshop3 = "locate/home/new/Workshop3.png"

    image d5_smart_manga = "locate/home/new/manga.png"

    image d5_smart_scene_kitchen = LiveComposite((1920, 1080),
        (0, 0), "d5_smart_kitchen_bg",
        (0, 0), "snow_night_1",
        (0, 0), "d5_smart_kitchen_bg2",
        (0, 0), "d5_smart_kitchen_molbert",
        )
    image d5_smart_scene_molbert = LiveComposite((1920, 1080),
        (0, 0), "d5_smart_bg_0",
        (0, 0), "snow_night_1",
        (0, 0), "d5_smart_bg_1",
        (0, 0), "d5_smart_bg_2",
        (0, 0), "d5_smart_bg_3",
        )
    image d5_smart_scene_table = LiveComposite((1920, 1080),
        (0, 0), "d5_smart_tablet_bg",
        (0, 0), "d5_smart_tablet_cup empty",
        )
    image d5_smart_scene_window = LiveComposite((1920, 1080),
        (0, 0), "d5_smart_window 2",
        (0, 0), "snow_night_1",
        (0, 0), "d5_smart_window_overlay",
        )






    image d5_drugged_sky = "locate/home/out_side/Meet_beasts/jump/s_1.png"
    image d5_drugged_eye = "locate/Katya/Ant_fin/bg000.png"
    image d5_drugged_bg = "locate/Katya/Ant_fin/bg.png"
    image d5_drugged_bunny_1 = "locate/Katya/Ant_fin/01.png"
    image d5_drugged_bunny_2 = "locate/Katya/Ant_fin/02.png"
    image d5_drugged_bunny_3 = "locate/Katya/Ant_fin/03.png"
    image d5_drugged_bunny_4 = "locate/Katya/Ant_fin/04.png"
    image d5_drugged_bunny:
        "d5_drugged_bunny_1"
        .1
        "d5_drugged_bunny_2"
        .1
        "d5_drugged_bunny_3"
        .1
        "d5_drugged_bunny_4"
        .1
        repeat


    image d5_pr_bg = "locate/cemetery/goat/bg2.png"
    image d5_pr_body_1 = "sprite/P_R/body/01.png"
    image d5_pr_body_2 = "sprite/P_R/body/02.png"
    image d5_pr_body_3 = "sprite/P_R/body/03.png"
    image d5_pr_body_4 = "sprite/P_R/body/04.png"

    image d5_pr_body_1_dark_15 = AlphaMask(Solid("#0002", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_30 = AlphaMask(Solid("#0004", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_40 = AlphaMask(Solid("#0006", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_50 = AlphaMask(Solid("#0008", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_60 = AlphaMask(Solid("#000a", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_70 = AlphaMask(Solid("#000b", xysize=(1920, 2913)), "d5_pr_body_1")
    image d5_pr_body_1_dark_90 = AlphaMask(Solid("#000c", xysize=(1920, 2913)), "d5_pr_body_1")

    image d5_pr_body_2_dark_15 = AlphaMask(Solid("#0002", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_30 = AlphaMask(Solid("#0004", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_40 = AlphaMask(Solid("#0006", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_50 = AlphaMask(Solid("#0008", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_60 = AlphaMask(Solid("#000a", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_70 = AlphaMask(Solid("#000b", xysize=(1920, 2913)), "d5_pr_body_2")
    image d5_pr_body_2_dark_90 = AlphaMask(Solid("#000c", xysize=(1920, 2913)), "d5_pr_body_2")

    image d5_pr_body_3_dark_15 = AlphaMask(Solid("#0002", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_30 = AlphaMask(Solid("#0004", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_40 = AlphaMask(Solid("#0006", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_50 = AlphaMask(Solid("#0008", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_60 = AlphaMask(Solid("#000a", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_70 = AlphaMask(Solid("#000b", xysize=(1920, 2913)), "d5_pr_body_3")
    image d5_pr_body_3_dark_90 = AlphaMask(Solid("#000c", xysize=(1920, 2913)), "d5_pr_body_3")











    image d5_pr_pol_sad_ahead_01 = "sprite/P_R/pol/eyes/sad/ahead/01.png"
    image d5_pr_pol_sad_ahead_02 = "sprite/P_R/pol/eyes/sad/ahead/02.png"
    image d5_pr_pol_sad_ahead_03 = "sprite/P_R/pol/eyes/sad/ahead/03.png"
    image d5_pr_pol_sad_ahead_blink:
        contains transform_blink("d5_pr_pol_sad_ahead_01", "d5_pr_pol_sad_ahead_02", "d5_pr_pol_sad_ahead_03", 0.75)

    image d5_pr_pol_sad_aside_01 = "sprite/P_R/pol/eyes/sad/aside/01.png"
    image d5_pr_pol_sad_aside_02 = "sprite/P_R/pol/eyes/sad/aside/02.png"
    image d5_pr_pol_sad_aside_03 = "sprite/P_R/pol/eyes/sad/aside/03.png"
    image d5_pr_pol_sad_aside_blink:
        contains transform_blink("d5_pr_pol_sad_aside_01", "d5_pr_pol_sad_aside_02", "d5_pr_pol_sad_aside_03", 0.75)

    image d5_pr_pol_cry_ahead_01 = "sprite/P_R/pol/eyes/cry/ahead/01.png"
    image d5_pr_pol_cry_ahead_02 = "sprite/P_R/pol/eyes/cry/ahead/02.png"
    image d5_pr_pol_cry_ahead_03 = "sprite/P_R/pol/eyes/cry/ahead/03.png"
    image d5_pr_pol_cry_ahead_blink:
        contains transform_blink("d5_pr_pol_cry_ahead_01", "d5_pr_pol_cry_ahead_02", "d5_pr_pol_cry_ahead_03", 0.75)

    image d5_pr_pol_cry_aside_01 = "sprite/P_R/pol/eyes/cry/aside/01.png"
    image d5_pr_pol_cry_aside_02 = "sprite/P_R/pol/eyes/cry/aside/02.png"
    image d5_pr_pol_cry_aside_03 = "sprite/P_R/pol/eyes/cry/aside/03.png"
    image d5_pr_pol_cry_aside_blink:
        contains transform_blink("d5_pr_pol_cry_aside_01", "d5_pr_pol_cry_aside_02", "d5_pr_pol_cry_aside_03", 0.75)

    image d5_pr_pol_sadly_ahead_01 = "sprite/P_R/pol/eyes/sadly/ahead/01.png"
    image d5_pr_pol_sadly_ahead_02 = "sprite/P_R/pol/eyes/sadly/ahead/02.png"
    image d5_pr_pol_sadly_ahead_03 = "sprite/P_R/pol/eyes/sadly/ahead/03.png"
    image d5_pr_pol_sadly_ahead_blink:
        contains transform_blink("d5_pr_pol_sadly_ahead_01", "d5_pr_pol_sadly_ahead_02", "d5_pr_pol_sadly_ahead_03", 0.75)

    image d5_pr_pol_sadly_aside_01 = "sprite/P_R/pol/eyes/sadly/aside/01.png"
    image d5_pr_pol_sadly_aside_02 = "sprite/P_R/pol/eyes/sadly/aside/02.png"
    image d5_pr_pol_sadly_aside_03 = "sprite/P_R/pol/eyes/sadly/aside/03.png"
    image d5_pr_pol_sadly_aside_blink:
        contains transform_blink("d5_pr_pol_sadly_aside_01", "d5_pr_pol_sadly_aside_02", "d5_pr_pol_sadly_aside_03", 0.75)

    image d5_pr_pol_mouth_01 = "sprite/P_R/pol/mouth/01.png"
    image d5_pr_pol_mouth_02 = "sprite/P_R/pol/mouth/02.png"
    image d5_pr_pol_mouth_03 = "sprite/P_R/pol/mouth/03.png"
    image d5_pr_pol_mouth_04 = "sprite/P_R/pol/mouth/04.png"


    image d5_pr_rom_norm_ahead_01 = "sprite/P_R/rom/eyes/norm/ahead/01.png"
    image d5_pr_rom_norm_ahead_02 = "sprite/P_R/rom/eyes/norm/ahead/02.png"
    image d5_pr_rom_norm_ahead_03 = "sprite/P_R/rom/eyes/norm/ahead/03.png"
    image d5_pr_rom_norm_ahead_blink:
        contains transform_blink("d5_pr_rom_norm_ahead_01", "d5_pr_rom_norm_ahead_02", "d5_pr_rom_norm_ahead_03")

    image d5_pr_rom_norm_aside_01 = "sprite/P_R/rom/eyes/norm/aside/01.png"
    image d5_pr_rom_norm_aside_02 = "sprite/P_R/rom/eyes/norm/aside/02.png"
    image d5_pr_rom_norm_aside_03 = "sprite/P_R/rom/eyes/norm/aside/03.png"
    image d5_pr_rom_norm_aside_blink:
        contains transform_blink("d5_pr_rom_norm_aside_01", "d5_pr_rom_norm_aside_02", "d5_pr_rom_norm_aside_03")

    image d5_pr_rom_worry_ahead_01 = "sprite/P_R/rom/eyes/worry/ahead/01.png"
    image d5_pr_rom_worry_ahead_02 = "sprite/P_R/rom/eyes/worry/ahead/02.png"
    image d5_pr_rom_worry_ahead_03 = "sprite/P_R/rom/eyes/worry/ahead/03.png"
    image d5_pr_rom_worry_ahead_blink:
        contains transform_blink("d5_pr_rom_worry_ahead_01", "d5_pr_rom_worry_ahead_02", "d5_pr_rom_worry_ahead_03")

    image d5_pr_rom_worry_aside_01 = "sprite/P_R/rom/eyes/worry/aside/01.png"
    image d5_pr_rom_worry_aside_02 = "sprite/P_R/rom/eyes/worry/aside/02.png"
    image d5_pr_rom_worry_aside_03 = "sprite/P_R/rom/eyes/worry/aside/03.png"
    image d5_pr_rom_worry_aside_blink:
        contains transform_blink("d5_pr_rom_worry_aside_01", "d5_pr_rom_worry_aside_02", "d5_pr_rom_worry_aside_03")

    image d5_pr_rom_mouth_01 = "sprite/P_R/rom/mouth/01.png"
    image d5_pr_rom_mouth_02 = "sprite/P_R/rom/mouth/02.png"


    layeredimage d5_pr:
        group base:
            attribute 01:
                "d5_pr_body_1"
            attribute 02:
                "d5_pr_body_2"
            attribute 03:
                "d5_pr_body_3"

        group p_eyes:
            attribute pah_sad:
                "d5_pr_pol_sad_ahead_blink"
            attribute pas_sad:
                "d5_pr_pol_sad_aside_blink"

            attribute pah_cry:
                "d5_pr_pol_cry_ahead_blink"
            attribute pas_cry:
                "d5_pr_pol_cry_aside_blink"

            attribute pah_sadly:
                "d5_pr_pol_sadly_ahead_blink"
            attribute pas_sadly:
                "d5_pr_pol_sadly_aside_blink"

        group r_eyes:
            attribute rah_norm:
                "d5_pr_rom_norm_ahead_blink"
            attribute ras_norm:
                "d5_pr_rom_norm_aside_blink"

            attribute rah_worry:
                "d5_pr_rom_worry_ahead_blink"
            attribute ras_worry:
                "d5_pr_rom_worry_aside_blink"

        group p_mouth:
            attribute p01:
                "d5_pr_pol_mouth_01"
            attribute p02:
                "d5_pr_pol_mouth_02"
            attribute p03:
                "d5_pr_pol_mouth_03"
            attribute p04:
                "d5_pr_pol_mouth_04"

        group r_mouth:
            attribute r01:
                "d5_pr_rom_mouth_01"
            attribute r02:
                "d5_pr_rom_mouth_02"

        group dark:
            attribute d15 if_any "01":
                "d5_pr_body_1_dark_15"
            attribute d15 if_any "02":
                "d5_pr_body_2_dark_15"
            attribute d15 if_any "03":
                "d5_pr_body_3_dark_15"

            attribute d30 if_any "01":
                "d5_pr_body_1_dark_30"
            attribute d30 if_any "02":
                "d5_pr_body_2_dark_30"
            attribute d30 if_any "03":
                "d5_pr_body_3_dark_30"

            attribute d40 if_any "01":
                "d5_pr_body_1_dark_40"
            attribute d40 if_any "02":
                "d5_pr_body_2_dark_40"
            attribute d40 if_any "03":
                "d5_pr_body_3_dark_40"

            attribute d50 if_any "01":
                "d5_pr_body_1_dark_50"
            attribute d50 if_any "02":
                "d5_pr_body_2_dark_50"
            attribute d50 if_any "03":
                "d5_pr_body_3_dark_50"

            attribute d60 if_any "01":
                "d5_pr_body_1_dark_60"
            attribute d60 if_any "02":
                "d5_pr_body_2_dark_60"
            attribute d60 if_any "03":
                "d5_pr_body_3_dark_60"

            attribute d70 if_any "01":
                "d5_pr_body_1_dark_70"
            attribute d70 if_any "02":
                "d5_pr_body_2_dark_70"
            attribute d70 if_any "03":
                "d5_pr_body_3_dark_70"

            attribute d90 if_any "01":
                "d5_pr_body_1_dark_90"
            attribute d90 if_any "02":
                "d5_pr_body_2_dark_90"
            attribute d90 if_any "03":
                "d5_pr_body_3_dark_90"



    image d5_titles_obaby_bg = "locate/home/in_side/1st_floor/hall/h1/treat/fon.png"

    image d5_titles_obaby_owl1 = "locate/home/in_side/1st_floor/hall/h1/treat/s01.png"
    image d5_titles_obaby_owl2 = "locate/home/in_side/1st_floor/hall/h1/treat/s02.png"
    image d5_titles_obaby_owl:
        "d5_titles_obaby_owl1"
        .2
        "d5_titles_obaby_owl2"
        .2
        repeat

    image d5_titles_obaby_window = "locate/home/in_side/1st_floor/hall/h1/treat/fon2.png"

    image d5_titles_obaby_olga_1 = "locate/home/in_side/1st_floor/hall/h1/treat/olga_big.png"
    image d5_titles_obaby_olga_2 = "locate/home/in_side/1st_floor/hall/h1/treat/olga_big2.png"
    image d5_titles_obaby_olga_3 = "locate/home/in_side/1st_floor/hall/h1/treat/olga_big3.png"
    image d5_titles_obaby_olga:
        contains:
            "d5_titles_obaby_olga_1"
        contains:
            Null()
            3.
            "d5_titles_obaby_olga_2"
            .1
            "d5_titles_obaby_olga_3"
            .1
            "d5_titles_obaby_olga_2"
            .1
            Null()
            5.
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
