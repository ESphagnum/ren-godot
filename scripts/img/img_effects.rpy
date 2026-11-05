init:
    image empty_full = "interface/empty_full.png"


    image ramka = "effect/ramka/ramka4.png"
    image ramka1 = "effect/ramka/ramka1.png"
    image old_movie_001_002 = Animation(
        "effect/old_movie/old_movie_001.png", 0.10, 
        "effect/old_movie/old_movie_002.png", 0.10)
    image old_movie_003_004 = Animation(
        "effect/old_movie/old_movie_003.png", 0.10, 
        "effect/old_movie/old_movie_004.png", 0.10)
    image old_movie2_001_002_003_004 = Animation(
        Null(0,0), 1.0, 
        "effect/old_movie/old_movie_001.png", 0.10, 
        Null(0,0), 0.05, 
        "effect/old_movie/old_movie_002.png", 0.10, 
        Null(0,0), 0.05, 
        "effect/old_movie/old_movie_003.png", 0.10, 
        Null(0,0), 0.05, 
        "effect/old_movie/old_movie_004.png", 0.10, 
        Null(0,0), 3.0)

    image oframe_1:
        im.MatrixColor("effect/old_movie/old_movie_001.png", im.matrix.brightness(1.00))
    image oframe_2:
        im.MatrixColor("effect/old_movie/old_movie_002.png", im.matrix.brightness(1.00))
    image oframe_3:
        im.MatrixColor("effect/old_movie/old_movie_003.png", im.matrix.brightness(1.00))
    image oframe_4:
        im.MatrixColor("effect/old_movie/old_movie_004.png", im.matrix.brightness(1.00))


    define dtf = 0.1
    image old_movie2_gray:
        block:
            choice:
                alpha 1
                "oframe_1"
                pause dtf
                "oframe_2"
                pause dtf
                "oframe_3"
                pause dtf
                "oframe_4"
                pause dtf
                alpha 0

            choice:
                alpha 1
                "oframe_3"
                pause dtf
                "oframe_4"
                pause dtf
                "oframe_2"
                pause dtf
                "oframe_1"
                pause dtf
                alpha 0

            choice:
                alpha 1
                "oframe_2"
                pause dtf
                "oframe_4"
                pause dtf
                "oframe_3"
                pause dtf
                "oframe_4"
                pause dtf
                "oframe_1"
                pause dtf
                alpha 0

        block:
            choice:
                pause .5

            choice:
                pause dtf

            choice:
                pause 2.

        repeat

    image ef_scrap = Animation(Null(0,0), 1.0, "effect/scrap/001.png", 0.10, Null(0,0), 0.05, "effect/scrap/002.png", 0.10, Null(0,0), 0.05, "effect/scrap/003.png", 0.10, Null(0,0), 0.05, "effect/scrap/004.png", 0.10, Null(0,0), 3.0)

    image Veko_01 = "effect/veko/Veko_01.png"
    image Veko_02 = "effect/veko/Veko_02.png"

    image blizzard_big = "effect/snow/snow00.png"
    image blizzard_mid = "effect/snow/snow01.png"
    image blizzard_sml = "effect/snow/snow02.png"
    image blizzard_sparce = "effect/snow/snow03.png"

    image blizzard_d4_evening_far:
        "blizzard_sml"
        parallel:
            xpan 0
            linear 60 xpan -360
            repeat
        parallel:
            ypan 0
            linear 30 ypan -360
            repeat
    image blizzard_d4_evening_near:
        "blizzard_mid"
        parallel:
            xpan 0
            linear 30 xpan -360
            repeat
        parallel:
            ypan 0
            linear 15 ypan -360
            repeat
    image blizzard_d4_evening_big:
        "blizzard_big"
        parallel:
            xpan 0
            linear 20 xpan -360
            repeat
        parallel:
            ypan 0
            linear 8 ypan -360
            repeat
    image blizzard_d4_evening:
        contains:
            "blizzard_d4_evening_far"
        contains:
            "blizzard_d4_evening_near"
        contains:
            "snow_night_1"

    image blizzard_d4_evening2_far:
        animation
        "blizzard_d4_evening_far"
        matrixcolor BrightnessMatrix(-.30)
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    image blizzard_d4_evening2_far_zoomed:
        animation
        "blizzard_d4_evening2_far"
        zoom 2.0
    image blizzard_d4_evening2_far_bright100:
        animation
        "blizzard_d4_evening_far"
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    image blizzard_d4_evening2_far_zoomed_bright100:
        animation
        "blizzard_d4_evening2_far_bright100"
        zoom 2.0
    image blizzard_d4_evening2_near:
        animation
        "blizzard_d4_evening_near"
        matrixcolor BrightnessMatrix(-.30)
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    image blizzard_d4_evening2_near_zoomed:
        animation
        "blizzard_d4_evening2_near"
        zoom 2
    image blizzard_d4_evening2_near_bright100:
        animation
        "blizzard_d4_evening_near"
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    image blizzard_d4_evening2_near_zoomed_bright100:
        animation
        "blizzard_d4_evening2_near_bright100"
        zoom 2
    image blizzard_d4_evening2_big:
        "blizzard_d4_evening_big"
        matrixcolor BrightnessMatrix(-.20)
        block:
            ypan 0
            linear 20 ypan -360
            repeat

    image blizzard_d4_evening_far_run:
        "blizzard_sml"
        matrixcolor BrightnessMatrix(-.1)
        parallel:
            xpan 0
            linear 5 xpan 360
            repeat
        parallel:
            ypan 0
            linear 30 ypan -360
            repeat
    image blizzard_d4_evening_near_run:
        "blizzard_mid"
        matrixcolor BrightnessMatrix(-.1)
        parallel:
            xpan 0
            linear 5 xpan 360
            repeat
        parallel:
            ypan 0
            linear 15 ypan -360
            repeat

    image blizzard_d4_evening_face = SnowBlossom("effect/snow/s005.png", count=15, yspeed=(200, 350), xspeed=(150, 250), border=100, start=1, fast = True)
    image blizzard_d4_day_face = SnowBlossom("effect/snow/s005.png", count=15, yspeed=(200, 350), xspeed=(-10, 10), border=100, start=1, fast = True)

    image blizzard_d4_day_far:
        "blizzard_mid"
        matrixcolor BrightnessMatrix(0.2)
        block:
            ypan 0
            linear 10 ypan -360
            repeat
    image blizzard_d4_day_near:
        "blizzard_big"
        matrixcolor BrightnessMatrix(0.2)
        parallel:
            ypan 180
            linear 4.5 ypan -360+180
            repeat
        parallel:
            xpan 0
            linear 600 xpan -360
            repeat

    image blizzard_d4_day2_near:
        "blizzard_d4_day_near"
        matrixcolor BrightnessMatrix(0.2)

    image blizzard_d4_trip:
        "blizzard_big"
        matrixcolor TintMatrix("#9bd7ff") * BrightnessMatrix(.4)
        block:
            ypan 0
            linear 45 ypan 360
            repeat

    $ slow_mod = .5 **2
    image snow1_slow = SnowBlossom("effect/snow/s001.png", count=3, yspeed=(600*slow_mod, 700*slow_mod), xspeed=(-10, 10), border=50, start=50)
    image snow2_slow = SnowBlossom("effect/snow/s002.png", count=3, yspeed=(550*slow_mod, 650*slow_mod), xspeed=(-10, 10), border=50, start=30)
    image snow3_slow = SnowBlossom("effect/snow/s003.png", count=3, yspeed=(500*slow_mod, 600*slow_mod), xspeed=(-10, 10), border=50, start=10)

    image snow_up_d4_trip:
        "incar_snow_up"
        matrixcolor TintMatrix("#9bd7ff") * BrightnessMatrix(.4)

    image d4_snow_night = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=125, yspeed=(40, 50), xspeed=(10, 20), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=50, yspeed=(50, 80), xspeed=(30, 40), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=50, yspeed=(60, 90), xspeed=(30, 40), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=12, yspeed=(80, 100), xspeed=(25, 40), border=1000, start=5, fast=True),
        )

    image d4_snow_night2 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=60, yspeed=(40, 50), xspeed=(10, 20), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=25, yspeed=(50, 80), xspeed=(30, 40), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=25, yspeed=(60, 90), xspeed=(30, 40), border=1000, start=5, fast=True),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=6, yspeed=(80, 100), xspeed=(25, 40), border=1000, start=5, fast=True),
        )
    image d4_snow_night_full = LiveComposite((1920, 1080),
        (0, 0), "snow_night_1",
        (0, 0), "blizzard_d4_evening_face",
        )

transform clear_owl:
    alpha 1.0
    linear 30.0
    linear 1.0 alpha 0.0
init:


    transform loop_left(img, t=10):
        contains:
            img
            xalign .0 xpos 2.
            linear t xpos .0
            repeat
        contains:
            img
            xalign .0 xpos .0
            linear t xpos -2.
            repeat



    transform loop_right(img, t=10):
        contains:
            img
            xalign .0 xpos .0
            linear t xpos 2.
            repeat
        contains:
            img
            xalign .0 xpos -2.
            linear t xpos .0
            repeat




    transform my_shake(a=2):
        linear 0.1 xoffset -2 yoffset a
        linear 0.1 xoffset a+1 yoffset -3
        linear 0.1 xoffset a yoffset -2
        linear 0.1 xoffset -3 yoffset a+1
        linear 0.1 xoffset 0 yoffset 0
        repeat


    transform my_shake1(a=2):
        linear 0.1 xoffset -2 yoffset a
        linear 0.1 xoffset a+1 yoffset -3
        linear 0.1 xoffset a yoffset -2
        linear 0.1 xoffset -3 yoffset a+1
        linear 0.1 xoffset 0 yoffset 0
        5.0
        repeat

    transform my_shake2(a=2):
        linear 0.1 xoffset -2 yoffset a
        linear 0.3 xoffset a+1 yoffset -3
        linear 0.2 xoffset a yoffset -2
        linear 0.1 xoffset -3 yoffset a+1
        linear 0.2 xoffset 0 yoffset 0
        2.0
        repeat


init -999 python:























    def img2disp(image):
        return renpy.easy.displayable(image)



    def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=None, start=1, ext=None, **properties):
        args = []
        
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = img2disp(img_name + str(i))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                
                args.append(effect)
        if reverse: 
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = img2disp(img_name + str(i))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)       
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
