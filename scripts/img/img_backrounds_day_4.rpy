init:
    python:
        import math
        class DustWall(object):
            def __init__(self, xysize):
                
                self.sm = SpriteManager(update=self.update)
                
                self.xysize = xysize
                
                self.stars = [ ]
                
                d = Transform("effect/dust_1.png", zoom=.3)
                for i in range(0, 50):
                    self.add(d, 1)
                
                d = Transform("effect/dust_1.png", zoom=.5)
                for i in range(0, 10):
                    self.add(d, 2)
                
                d = Transform("effect/dust_1.png", zoom=.6)
                for i in range(0, 10):
                    self.add(d, 3)
                
                d = Transform("effect/dust_1.png", zoom=.8)
                for i in range(0, 10):
                    self.add(d, 5)
                
                d = Transform("effect/dust_1.png", zoom=1)
                for i in range(0, 15):
                    self.add(d, 7)
            
            def add(self, d, speed):
                s = self.sm.create(d)
                
                start = renpy.random.randint(1, 2)
                
                modifier = renpy.random.uniform(-0.9,0.9)
                
                x = renpy.random.randint(100, self.xysize[0]-100)
                y = renpy.random.randint(100, self.xysize[1]-100)
                self.stars.append((s, start, speed, modifier, x, y))
            
            def update(self, st):
                for s, start, speed, modifier, x, y in self.stars:
                    s.x = (x + start * math.cos(st*modifier) * speed)
                    s.y = (y + start * math.sin(st*modifier) * speed)
                return 0
    image d4_dust_norm = DustWall((1920, 1080)).sm
    image d4_dust_wide = DustWall((3911, 1080)).sm
    image d4_dust_wide2 = DustWall((4239, 1080)).sm
    define tetrad_dissolve = ImageDissolve("effect/imagedissolve/anketa/04.png", 1.5)
    image d4_kate_vision:
        "locate/school/in_side/Kaite_memo/001-006.jpg"
        .1
        "locate/school/in_side/Kaite_memo/002-010.jpg"
        .1
        "locate/school/in_side/Kaite_memo/003.jpg"
        .1
        "locate/school/in_side/Kaite_memo/004.jpg"
        .1
        "locate/school/in_side/Kaite_memo/005.jpg"
        .1
        "locate/school/in_side/Kaite_memo/001-006.jpg"
        .1
        "locate/school/in_side/Kaite_memo/007.jpg"
        .1
        "locate/school/in_side/Kaite_memo/008.jpg"
        .1
        "locate/school/in_side/Kaite_memo/009.jpg"
        .1
        "locate/school/in_side/Kaite_memo/002-010.jpg"
        .1
        block:
            "locate/school/in_side/Kaite_memo/005.jpg"

            choice:
                1.5
            choice:
                2.
            choice:
                2.5

            "locate/school/in_side/Kaite_memo/007.jpg"
            .1
            "locate/school/in_side/Kaite_memo/008.jpg"
            .1
            "locate/school/in_side/Kaite_memo/009.jpg"
            .1
            "locate/school/in_side/Kaite_memo/002-010.jpg"
            .1
            repeat

    image empty = Solid("#0000")


    image d4_classroom_day_base = "locate/school/in_side/classroom/classroom005.png"
    image d4_classroom_day_byash1 = "locate/school/in_side/classroom/Bysh_1.png"
    image d4_classroom_day_byash2 = "locate/school/in_side/classroom/Bysh_2.png"

    image d4_classroom_day_byash2_white = AlphaMask(Solid("#fff", xysize=(3911, 1080)), "d4_classroom_day_byash2")

    image d4_classroom_pol = "locate/school/in_side/classroom.jpg"

    image d4_anton = "locate/school/out_side/school_coner/Anton.png"
    image d4_anton 2 = "locate/street/Anton_battle/scene_04/Anton_00.png"
    image d4_anton rot:
        "sprite/Ant/Normal/b_day/3_mouth/08.png"

    image d4_masked_anton:
        contains:
            "locate/school/out_side/school_coner/Anton.png"
            align (.5, 1.)
        contains:
            "locate/school/out_side/school_coner/A_mask.png"
            align (.5, 1.)

    image d4_bg_backpack:
        contains:
            "locate/home/out_side/handblood_fon.jpg"

        contains:
            "blizzard_d4_day_far"
            matrixcolor BrightnessMatrix(0.2)
            yzoom -1

        contains:
            "locate/home/out_side/backpack/bag_03.png"
            yoffset -400
            linear 2 yoffset -200

        contains:
            "locate/home/out_side/backpack/bag_04.png"
            yoffset -400
            linear 2 yoffset -200

        contains:
            "blizzard_d4_day_near"
            matrixcolor BrightnessMatrix(0.2)
            yzoom -1

    image anton_zay_03 = "locate/street/gopstop/Anton3.png"

    image d4_polina_strike:
        "locate/school/out_side/school_coner/hit/01.png"
        .1
        "locate/school/out_side/school_coner/hit/02.png"
        .1
        "locate/school/out_side/school_coner/hit/03.png"
        .1
        "locate/school/out_side/school_coner/hit/04.png"
        .1

    image d4_polina_strike_1 = "locate/school/out_side/school_coner/hit/01.png"
    image d4_polina_strike_2 = "locate/school/out_side/school_coner/hit/02.png"
    image d4_polina_strike_3 = "locate/school/out_side/school_coner/hit/03.png"

    image d4_polina_strike_last = "locate/school/out_side/school_coner/hit/04.png"

    image d4_mask_in_hands_day:

        "mask_01"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            ease 0.8 xoffset -50 yoffset 0
            ease 0.8 xoffset 650 yoffset 0 alpha 0.0

    image bg school_corner_day_onshow_2:
        contains:
            "bg school_corner_day1_no_squirrel"
            xoffset -1000+960-2426+1960
            yalign 0.5
            ease 3.5 xoffset 0
        contains:
            "bg school_day"
            yalign 0.8 xoffset -2000+960
            parallel:
                ease 5.0 xoffset 0+2426-1960
            parallel:
                alpha 1.0
                pause 1.5
                ease 1.5 alpha 0.0
                pause 1.0

    image bg school_corner_day_onshow_3_bg:
        "bg school_corner_day1_no_squirrel"
        xalign .5
        yalign 0.5
        ease 3.5 xalign 1.

    image bg school_corner_day_onshow_3_fg:
        "bg school_day"
        yalign 0.8 xalign 0
        parallel:
            ease 5.0 xalign .5
        parallel:
            alpha 0.0
            pause 1.5
            linear 1.5 alpha 1.0



    image bg school_corner_day_onshow_4_fg:
        "bg school_corner_day1_no_squirrel"
        xalign 1.
        yalign 0.5

        parallel:
            ease 5.0 xalign .5
        parallel:
            alpha 0
            1.5
            linear 1.5 alpha 1


    image bg school_corner_day_onshow_4_bg:
        "bg school_day"
        yalign 0.8 xalign .5
        ease 5.0 xalign 0.0


    image d4_roma_sad_mono = "sprite/Romka/Sad/mono.png"

    image d4_polina_home_clouds:
        contains:
            "locate/street/HousePol/Back.jpg"

        contains:
            "locate/street/HousePol/Cloud.png"
            subpixel True
            yalign 0
            xpos 0.95
            linear 20 xpos 1.0
            block:
                xpos 0.0
                linear 200 xpos 1.0
                repeat

        contains:
            "locate/street/HousePol/Cloud.png"
            subpixel True
            yalign 0
            xpos -.05
            linear 20 xpos 0.0
            block:
                xpos -1.0
                linear 200 xpos 0.0
                repeat

        contains:
            "locate/street/HousePol/Cloud2.png"
            subpixel True
            yalign 0
            block:
                xpos 0.0
                linear 130 xpos 1.0
                repeat

        contains:
            "locate/street/HousePol/Cloud2.png"
            subpixel True
            yalign 0
            block:
                xpos -1.0
                linear 130 xpos 0.0
                repeat

    image d4_polina_home_house = "locate/street/HousePol/House.png"
    image ant_clas_1 ul:
        contains:
            "ant_clas_1 1"
        contains:
            "locate/school/in_side/Anton_class/M_01.png"

    image ant_clas_1 m6:
        contains:
            "ant_clas_1 1"
        contains:
            "ant_clas_m6"
    image ant_clas_1 m7:
        contains:
            "ant_clas_1 1"
        contains:
            "ant_clas_m7"
    image ant_clas_1 ul2:
        "ant_clas_1 1"
        pause .5
        "ant_clas_1 ul"

    image d4_flowers_on_snow = "locate/school/out_side/school_coner/flowers.png"

    image day4_fence_anton_eyes_ahead = "images/locate/school/out_side/school_coner/A01.png"
    image day4_fence_anton_eyes_aside = "images/locate/school/out_side/school_coner/A02.png"

    image d4_polina_03:
        contains:
            "sprite/Polina/Front/b_day_winter/1_body/03.png"
        contains:
            "sprite/Polina/Front/b_day_winter/3_mouth/03.png"
            yoffset 144

    image d4_byasha_doubt = "locate/school/out_side/002.png"

    image d4_voltron_art = "locate/school/out_side/Voltron.png"
    image d4_voltron_empty = "locate/school/out_side/empty.png"

    image d4_road = "locate/street/road.jpg"

    image bg school_day_animation:
        "bg school_day"
        yalign .8
        xalign .5
        zoom 1.10
        subpixel True
        alpha 1
        ease 8. zoom .5 yalign .5

    image d4_bridge = "locate/street/bridge_sunset.png"

    image d4_darkroad_01 = "locate/street/road_to_home(N)/road01.png"
    image d4_darkroad_02 = "locate/street/road_to_home(N)/road02.png"
    image d4_darkroad_03 = "locate/street/road_to_home(N)/road03.png"
    image d4_darkroad_04 = "locate/street/road_to_home(N)/road04.png"
    image d4_darkroad_05 = "locate/street/road_to_home(N)/road05.png"




init:

    image d4_forest_walk_day_1_0:
        "locate/street/road_to_home/road00.jpg"
        xpos 0
        block:
            linear delay1 xpos -1920
            linear delay1 xpos -3840+1
            xpos 3840
            linear delay1 xpos 1920
            linear delay1 xpos 0
            repeat

    image d4_forest_walk_day_1_1:
        "locate/street/road_to_home/road00.jpg"
        block:
            xpos 3840
            linear delay1 xpos 1920
            linear delay1 xpos 0
            linear delay1 xpos -1920
            linear delay1 xpos -3840+1
            repeat

    image d4_forest_walk_day_2_0:
        "locate/street/road_to_home/road02.png"
        xpos 0
        block:
            linear delay2 xpos -1920
            linear delay2 xpos -3840+1
            xpos 3840
            linear delay2 xpos 1920
            linear delay2 xpos 0
            repeat

    image d4_forest_walk_day_2_1:
        "locate/street/road_to_home/road02.png"
        block:
            xpos 3840
            linear delay2 xpos 1920
            linear delay2 xpos 0
            linear delay2 xpos -1920
            linear delay2 xpos -3840+1
            repeat

    image d4_forest_walk_day_3_0:
        "locate/street/road_to_home/road03.png"
        xpos 0
        block:
            linear delay3 xpos -1920
            linear delay3 xpos -3840+1
            xpos 3840
            linear delay3 xpos 1920
            linear delay3 xpos 0
            repeat

    image d4_forest_walk_day_3_1:
        "locate/street/road_to_home/road03.png"
        block:
            xpos 3840
            linear delay3 xpos 1920
            linear delay3 xpos 0
            linear delay3 xpos -1920
            linear delay3 xpos -3840+1
            repeat

    image d4_forest_walk_day_4_0:
        "locate/street/road_to_home/road04.png"
        xpos 0
        block:
            linear delay4 xpos -1920
            linear delay4 xpos -3840
            linear delay4 xpos -5760
            linear delay4 xpos -7680+1
            xpos 7680
            linear delay4 xpos 5760
            linear delay4 xpos 3840
            linear delay4 xpos 1920
            linear delay4 xpos 0
            repeat

    image d4_forest_walk_day_4_1:
        "locate/street/road_to_home/road04.png"
        block:
            xpos 7680
            linear delay4 xpos 5760
            linear delay4 xpos 3840
            linear delay4 xpos 1920
            linear delay4 xpos 0
            linear delay4 xpos -1920
            linear delay4 xpos -3840
            linear delay4 xpos -5760
            linear delay4 xpos -7680+1
            repeat
    image twain_rb_far = LiveComposite((4000, 2250),
        (800,0), "locate/school/out_side/twain.png"
        )
    image twain_rb = "locate/school/out_side/twain.png"

    image Anton_back_day_4 = "locate/street/Anton_battle/scene_01/Anton.png"
    image Polina_back_day_4 = "sprite/Polina/Back2.png"
    image fence2 = "locate/school/out_side/fence2.png"
    image Romka Worry fish:
        contains:
            "Romka Worry m_day_winter 01 worry ahead 01"
        contains:
            block:
                choice:
                    "sprite/Romka/Worry/m_day_winter/3_mouth/01.png"
                choice:
                    "sprite/Romka/Worry/m_day_winter/3_mouth/02.png"
            block:
                choice:
                    .10
                choice:
                    .15
            repeat

    image d4_forest_1 = "locate/forest/gorelnik/Forest1.png"
    image d4_forest_snow = "locate/forest/gorelnik/snow_fon.png"
    image d4_forest_purse = "locate/forest/gorelnik/purse.png"

    image d4_forest_purse_on_snow = LiveComposite((1920, 2160),
        (0, 0), "d4_forest_snow",
        (0, 0), "d4_forest_purse")

    image d4_forest_purse_in_hand = "locate/forest/gorelnik/purse_taken.png"

    image dark_forest = "locate/forest/Foresty.jpg"
    image dark_forest_day3_1 dark1 = im.MatrixColor("locate/forest/Foresty.jpg", im.matrix.brightness(-0.08))
    image dark_forest_day3_1 dark2 = im.MatrixColor("locate/forest/Foresty.jpg", im.matrix.brightness(-0.16))
    image dark_forest_day3_1 dark3 = im.MatrixColor("locate/forest/Foresty.jpg", im.matrix.brightness(-0.24))
    image dark_forest_day3_1 dark4 = im.MatrixColor("locate/forest/Foresty.jpg", im.matrix.brightness(-0.32))

    image d4_forest_1 dark1 = im.MatrixColor("locate/forest/gorelnik/Forest1.png", im.matrix.brightness(-0.08))
    image d4_forest_1 dark2 = im.MatrixColor("locate/forest/gorelnik/Forest1.png", im.matrix.brightness(-0.16))
    image d4_forest_1 dark3 = im.MatrixColor("locate/forest/gorelnik/Forest1.png", im.matrix.brightness(-0.24))
    image d4_forest_1 dark4 = im.MatrixColor("locate/forest/gorelnik/Forest1.png", im.matrix.brightness(-0.32))

    image d4_anton_back = "sprite/Ant/Anton0.png"
    image d4_anton_back_night = "sprite/Ant/Anton1.png"
    image d4_anton_shock = "sprite/Ant/big-plan00.png"

    image d4_byash_drop scared b_night_winter:
        "sprite/byasha/scared/b_night_winter/4_drop/01.png"
        .1
        "sprite/byasha/scared/b_night_winter/4_drop/02.png"
        .1
        "sprite/byasha/scared/b_night_winter/4_drop/03.png"
        .1
        "sprite/byasha/scared/b_night_winter/4_drop/04.png"
        .1
        "sprite/byasha/scared/b_night_winter/4_drop/05.png"
        .1
        "sprite/byasha/scared/b_night_winter/4_drop/06.png"
        .1
        Null()
        6.0
        repeat

    image Byasha Scared b_night_winter 02 shock ahead 02 drop:
        contains:
            "Byasha Scared b_night_winter 02 shock ahead 02"
        contains:
            "d4_byash_drop scared b_night_winter"

    image Byasha Scared b_night_winter 02 shock aside 02 drop:
        contains:
            "Byasha Scared b_night_winter 02 shock aside 02"
        contains:
            "d4_byash_drop scared b_night_winter"

    image d4_gorelnik_bg = "locate/forest/gorelnik/fon2.png"
    image d4_gorelnik_garage_1 = "locate/forest/gorelnik/Garaz1.png"
    image d4_gorelnik_garage_2 = "locate/forest/gorelnik/Garaz2.png"

    image d4_gorelnik_wide = LiveComposite((2442, 1080),
        (0, 0), "d4_gorelnik_bg",
        (1382, 0), "d4_gorelnik_garage_1")

    image d4_gorelnik_fg_1 = "locate/forest/gorelnik/Left.png"
    image d4_gorelnik_fg_2 = "locate/forest/gorelnik/right.png"
    image d4_gorelnik_fg:
        contains:
            "d4_gorelnik_fg_1"
        contains:
            "d4_gorelnik_fg_2"
            xpos 1600

    transform blink_transform(img1, img2):
        img1

        block:
            pause 4

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

    transform blink_transform_nosfx(img1, img2):
        img1

        block:
            pause 4

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 3

            pause 6

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 3

            pause 4

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 2

            pause 6

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 1

            pause 6

            block:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 2

            repeat

    transform blink_slow_transform(img1, img2):
        img1

        block:
            choice:
                pause 15
            choice:
                pause 20

            function play_lamp_blink_4

            block:
                img2
                pause 0.1
                img1
                pause 0.1
            repeat

    transform blink_fast_transform(img1, img2):
        img1


        block:

            choice:
                function play_lamp_blink_4

                block:
                    img2
                    pause 0.1
                    img1
                    pause 0.1

                    repeat 2



            choice:
                function play_lamp_blink_random

                img2
                pause 0.1
                img1
                pause 0.1

                repeat 5

                function play_lamp_blink_4

        choice:
            pause .5
        choice:
            pause 2

        repeat

    transform blink_fast_transform_nosfx(img1, img2):
        img1


        block:



            choice:
                block:
                    img2
                    pause 0.1
                    img1
                    pause 0.1

                    repeat 2





            choice:
                img2
                pause 0.1
                img1
                pause 0.1

                repeat 5



        choice:
            pause .5
        choice:
            pause 2

        repeat

    transform blink_veryfast_transform(img1, img2):

        block:
            function play_lamp_blink_1

            img2
            pause 0.1
            img1
            pause 0.1

            repeat 3

        block:
            img1


            block:

                choice:
                    function play_lamp_blink_5

                    img2
                    pause 0.1
                    img1
                    pause 0.1

                    repeat 1



                choice:
                    function play_lamp_blink_3

                    img2
                    pause 0.1
                    img1
                    pause 0.1

                    repeat 2


                choice:
                    function play_lamp_blink_1

                    img2
                    pause 0.1
                    img1
                    pause 0.1

                    repeat 3

            choice:
                pause .5
            choice:
                pause 2.

            repeat

    image d4_gorelnik_garage_blink:
        contains blink_transform_nosfx("d4_gorelnik_garage_1", "d4_gorelnik_garage_2")

    image d4_gorelnik_wide_blink = LiveComposite((2442, 1080),
        (0, 0), "d4_gorelnik_bg",
        (1382, 0), "d4_gorelnik_garage_blink")

    image d4_myth = "locate/forest/Gorelnik/Fox.png"

    image d4_gorelnik_slim = Crop((2442-1920, 0, 1920, 1080), "d4_gorelnik_wide_blink")
    image d4_gorelnik_fg_slim = Crop((350, 0, 1920, 1080), "d4_gorelnik_fg")

    image ant_and_pol_left:
        contains:
            xzoom -1.1
            yzoom 1.1
            xoffset -200
            yoffset 80
            "locate/street/walking_fox_day/Polina.png"
        contains:
            xzoom -1.1
            yzoom 1.1
            xoffset -200
            yoffset 80
            "locate/street/walking_fox_day/Polina_2.png"
        contains:
            zoom .95
            "locate/street/walking_fox_day/Ant_left.png"
        contains:
            zoom .95
            "locate/street/walking_fox_day/hand.png"
    image ant_and_pol_walk_left:
        contains:
            xzoom -1.1
            yzoom 1.1
            xoffset -200
            yoffset 80
            "locate/street/walking_fox_day/Polina.png"
        contains:
            xzoom -1.1
            yzoom 1.1
            xoffset -200
            yoffset 80
            "locate/street/walking_fox_day/Polina_2.png"
        contains:
            zoom .95
            "locate/street/walking_fox_day/Ant_left.png"
        contains:
            zoom .95
            "locate/street/walking_fox_day/hand.png"
        yoffset 0
        xoffset 0
        parallel:
            linear 0.35 yoffset 10
            linear 0.35 yoffset 20
            linear 0.35 yoffset 10
            linear 0.35 yoffset 0
            repeat
        parallel:
            linear 3 xoffset 20
            linear 3 xoffset 40
            linear 3 xoffset 50
            linear 3 xoffset 40
            repeat
    image polina_home_day_04:
        contains:
            "locate/Polina/Pol_home.png"
        contains:
            "d4_boarhead_scene"
    image d4_boarhead_scene = ConditionSwitch(
        "SceneFlags.Has('boarhead')", "locate/Polina/Pol_home4.png",
        "True", "locate/Polina/Pol_home3.png")

    image d4_gor_bg = "locate/forest/gorelnik/a_fon.png"
    image d4_gor_hnd = "locate/forest/gorelnik/a_hend.png"
    image d4_gor_drin = "locate/forest/gorelnik/drin.png"
    image d4_gor_ant_1 = "locate/forest/gorelnik/ant_1.png"
    image d4_gor_ant_2 = "locate/forest/gorelnik/ant_2.png"
    image d4_gor_ant_3 = "locate/forest/gorelnik/ant_3.png"
    image d4_gor_ant_4 = "locate/forest/gorelnik/ant_4.png"
    image d4_gor_rom_1 = "locate/forest/gorelnik/rom_1.png"
    image d4_gor_rom_2 = "locate/forest/gorelnik/rom_2.png"
    image d4_gor_rom_3 = "locate/forest/gorelnik/rom_3.png"
    image d4_gor_rom_4 = "locate/forest/gorelnik/rom_4.png"

    image d4_gor_tih_rot = "locate/forest/gorelnik/tih0.png"
    image d4_gor_tih 0 = "locate/forest/gorelnik/tih.png"
    image d4_gor_tih 1 = "locate/forest/gorelnik/tih1.png"
    image d4_gor_tih 2 = "locate/forest/gorelnik/tih2.png"
    image d4_gor_tih 3 = "locate/forest/gorelnik/tih3.png"
    image d4_gor_tih 4 = "locate/forest/gorelnik/tih4.png"
    image d4_gor_tih 5 = "locate/forest/gorelnik/tih5.png"
    image d4_gor_tih 6 = "locate/forest/gorelnik/tih6.png"
    image d4_gor_tih 7 = "locate/forest/gorelnik/tih7.png"
    image d4_gor_tih 8 = "locate/forest/gorelnik/tih8.png"
    image d4_gor_tih 9 = "locate/forest/gorelnik/tih9.png"

    image d4_gor_fon3 = "locate/forest/gorelnik/fon3.png"
    image d4_gor_ant_base = "locate/forest/gorelnik/Basa_Ant.png"
    image d4_gor_ant_face 1 = "locate/forest/gorelnik/Ant_001.png"
    image d4_gor_ant_face 2 = "locate/forest/gorelnik/Ant_002.png"
    image d4_gor_ant_face 3 = "locate/forest/gorelnik/Ant_003.png"
    image d4_gor_ant_face wtf = "locate/forest/gorelnik/Ant_wtf.png"
    image d4_gor_ant = "d4_gor_ant_base"
    image d4_gor_ant 1 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant_base",
        (0, 0), "d4_gor_ant_face 1")
    image d4_gor_ant 2 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant_base",
        (0, 0), "d4_gor_ant_face 2")
    image d4_gor_ant 3 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant_base",
        (0, 0), "d4_gor_ant_face 3")
    image d4_gor_ant wtf = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_ant_base",
        (0, 0), "d4_gor_ant_face wtf")


    image d4_gor_rom_base = "locate/forest/gorelnik/Rom_Base.png"
    image d4_gor_rom_base_wtf = "locate/forest/gorelnik/Rom_base_wtf.png"
    image d4_gor_rom_face 1 = "locate/forest/gorelnik/Rom_001.png"
    image d4_gor_rom_face 2 = "locate/forest/gorelnik/Rom_002.png"
    image d4_gor_rom_face 3 = "locate/forest/gorelnik/Rom_003.png"
    image d4_gor_rom_face 4 = "locate/forest/gorelnik/Rom_004.png"
    image d4_gor_rom_face 5 = "locate/forest/gorelnik/Rom_005.png"
    image d4_gor_rom_face 6 = "locate/forest/gorelnik/Rom_006.png"
    image d4_gor_rom_face 7 = "locate/forest/gorelnik/Rom_007.png"
    image d4_gor_rom_face 8 = "locate/forest/gorelnik/Rom_008.png"
    image d4_gor_rom_face wtf2 = "locate/forest/gorelnik/Rom_wtf02.png"
    image d4_gor_rom_face wtf3 = "locate/forest/gorelnik/Rom_wtf03.png"

    image d4_gor_rom = "d4_gor_rom_base"
    image d4_gor_rom 1 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 1")
    image d4_gor_rom 2 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 2")
    image d4_gor_rom 3 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 3")
    image d4_gor_rom 4 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 4")
    image d4_gor_rom 5 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 5")
    image d4_gor_rom 6 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 6")
    image d4_gor_rom 7 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 7")
    image d4_gor_rom 8 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base",
        (0, 0), "d4_gor_rom_face 8")
    image d4_gor_rom wtf = "d4_gor_rom_base_wtf"
    image d4_gor_rom wtf2 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base_wtf",
        (0, 0), "d4_gor_rom_face wtf2")
    image d4_gor_rom wtf3 = LiveComposite((1920, 1080),
        (0, 0), "d4_gor_rom_base_wtf",
        (0, 0), "d4_gor_rom_face wtf2")


init:
    image d4_garage_knok_0 = "locate/street/garage/knok5/00.jpg"
    image d4_garage_knok_1 = "locate/street/garage/knok5/01-03.jpg"
    image d4_garage_knok_2 = "locate/street/garage/knok5/02.jpg"
    image d4_garage_knok_3 = "locate/street/garage/knok5/01-03.jpg"
    image d4_garage_knok_4 = "locate/street/garage/knok5/04.jpg"
    image d4_garage_knok_5 = "locate/street/garage/knok5/05.jpg"
    image d4_garage_knok_6 = "locate/street/garage/knok5/06.jpg"

    image d4_garage_knok_open_animation:
        "d4_garage_knok_2"
        "d4_garage_knok_4" with Dissolve(.5)

    image garage_over_blink:
        contains blink_transform(Null(), "bg_black")

    image garage_over_slow_blink:
        contains blink_slow_transform(Null(), "bg_black")

    image garage_near_blinking_noblur:
        contains blink_transform("locate/street/garage/The_garage_02.jpg", "locate/street/garage/The_garage_01.jpg")

    image garage_near_blinking_1_noblur:
        contains blink_transform("d4_garage_knok_2", "bg_black")

    image garage_opened = "locate/street/garage/The_garage_03.jpg"
    image garage_opened_blink:
        contains blink_transform("garage_opened", "bg_black")

    image d4_choice_bg_blink:
        contains blink_transform("locate/street/garage/Garaz3.png", "bg_black")

    image d4_gar_bg:
        contains:
            "locate/street/garage/gar/fon.png"
        contains:
            "locate/street/garage/gar/light.png"


    image d4_gar_Roma = "locate/street/garage/gar/sprite.png"
    image d4_gar_Ant = "locate/street/garage/gar/sprite2.png"

    image d4_gar_fg:
        contains:
            "locate/street/garage/gar/chiain.png"

    image d4_gar_door 0:
        contains:
            "locate/street/garage/gar/door_01.png"
            xoffset 150
        contains:
            "locate/street/garage/gar/door_04.png"

    image d4_gar_door 1:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 150
        contains:
            "locate/street/garage/gar/door_03.png"

    image d4_gar_door 1_2:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 150
            linear .5 xoffset 300
        contains:
            "locate/street/garage/gar/door_03.png"
            linear .5 xoffset -450

    image d4_gar_door 2:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 300
        contains:
            "locate/street/garage/gar/door_03.png"
            xoffset -450

    image d4_gar_door 3:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 300
        contains:
            "locate/street/garage/gar/door_03.png"
            xoffset -450
            linear .25 xoffset -550

    image d4_gar_door 4:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 300
        contains:
            "locate/street/garage/gar/door_04.png"
            xoffset -550

    image d4_gar_door 5:
        contains:
            "locate/street/garage/gar/door_02.png"
            xoffset 300
            linear .5 xoffset 500
        contains:
            "locate/street/garage/gar/door_04.png"
            xoffset -550

    image d4_garage_in 1 = "locate/street/garage/garage_in1.png"
    image d4_garage_in 2 = "locate/street/garage/garage_in2.png"
    image d4_garage_in 3 = "locate/street/garage/garage_in3.png"
    image d4_garage_in 4 = "locate/street/garage/garage_in4.png"
    image d4_garage_in 5 = "locate/street/garage/garage_in5.png"

    image d4_garage_romka 1 = "locate/street/garage/R_01.png"
    image d4_garage_romka 2 = "locate/street/garage/R_02.png"
    image d4_garage_romka 3 = "locate/street/garage/R_03.png"
    image d4_garage_romka 4 = "locate/street/garage/R_04.png"

    image d4_rom_knife:
        contains:
            "locate/street/rom_knife/R_knife00.png"
        contains:
            "locate/street/rom_knife/R_knife01.png"
            0.1,
            "locate/street/rom_knife/R_knife02.png"
            0.1,
            "locate/street/rom_knife/R_knife03.png"
            0.1,
            "locate/street/rom_knife/R_knife04.png"
            0.1,
            "locate/street/rom_knife/R_knife05.png"
            0.1,
            "locate/street/rom_knife/R_knife06.png"
            0.1,
            "locate/street/rom_knife/R_knife08.png"
            0.1,
            "locate/street/rom_knife/R_knife09.png"

    image d4_garage_gate = "locate/street/garage/gate.png"

    image d4_garage_lookin_dark:
        contains:
            "d4_garage_in 2"
            align (.5, .5)
            zoom 0.92
        contains:
            "d4_garage_gate"

    image d4_garage_lookin_light r1 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 3",
        (0, 0), "d4_garage_romka 1")

    image d4_garage_lookin_light r2 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 3",
        (0, 0), "d4_garage_romka 2")

    image d4_garage_lookin_light r3 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 3",
        (0, 0), "d4_garage_romka 3")

    image d4_garage_lookin_light r4 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 3",
        (0, 0), "d4_garage_romka 4")

    image d4_garage_lookin_meat r1 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 5",
        (0, 0), "d4_garage_romka 1")

    image d4_garage_lookin_meat r2 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 5",
        (0, 0), "d4_garage_romka 2")

    image d4_garage_lookin_meat r3 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 5",
        (0, 0), "d4_garage_romka 3")

    image d4_garage_lookin_meat r4 = LiveComposite((2098, 1180),
        (0, 0), "d4_garage_in 5",
        (0, 0), "d4_garage_romka 4")

    image d4_garage_in_blink1:
        contains blink_slow_transform("d4_garage_in 3", "d4_garage_in 2")
    image d4_garage_in_blink2:
        contains blink_slow_transform("d4_garage_in 5", "d4_garage_in 4")

    image d4_garage_katya = "locate/street/garage/katya.png"
    image d4_garage_canvas = "locate/street/garage/canvas.png"
    image d4_garage_grinder = "locate/street/garage/grinder.png"
    image d4_garage_grinder_katya 1 = "locate/street/garage/katya1.png"
    image d4_garage_grinder_katya 2 = "locate/street/garage/katya2.png"
    image d4_garage_grinder_romka = "locate/street/garage/romka.png"
    image d4_garage_grinder_ant 1 = "locate/street/garage/anton1.png"
    image d4_garage_grinder_ant 2 = "locate/street/garage/anton.png"

    image d4_sk_bg = "minigame/sk/fon_game.png"
    image d4_sk_fg = "minigame/sk/fg.png"
    image d4_sk_katya 0 = "minigame/sk/katya_0.png"
    image d4_sk_katya 00 = "minigame/sk/katya_00.png"
    image d4_sk_katya_1 = "minigame/sk/katya_1.png"
    image d4_sk_katya_2 = "minigame/sk/katya_2.png"
    image d4_sk_katya_3 = "minigame/sk/katya_3.png"
    image d4_sk_katya_4 = "minigame/sk/katya_4.png"
    image d4_sk_katya_5 = "minigame/sk/katya_5.png"
    image d4_sk_katya_6 = "minigame/sk/katya_6.png"
    image d4_sk_katya_7 = "minigame/sk/katya_7.png"
    image d4_sk_katya_8 = "minigame/sk/katya_8.png"
    image d4_sk_katya_9 = "minigame/sk/katya_9.png"

    image d4_sk_katya_1_1 = "minigame/sk/1/01.png"
    image d4_sk_katya_1_2 = "minigame/sk/1/02.png"
    image d4_sk_katya_1_3 = "minigame/sk/1/03.png"
    image d4_sk_katya_1_4 = "minigame/sk/1/04.png"
    image d4_sk_katya_1_5 = "minigame/sk/1/05.png"
    image d4_sk_katya_1_6 = "minigame/sk/1/06.png"

    image d4_sk_katya_2_1 = "minigame/sk/2/01.png"
    image d4_sk_katya_2_2 = "minigame/sk/2/02.png"
    image d4_sk_katya_2_3 = "minigame/sk/2/03.png"
    image d4_sk_katya_2_4 = "minigame/sk/2/04.png"
    image d4_sk_katya_2_5 = "minigame/sk/2/05.png"
    image d4_sk_katya_2_6 = "minigame/sk/2/06.png"

    image d4_sk_katya_3_1 = "minigame/sk/3/01.png"
    image d4_sk_katya_3_2 = "minigame/sk/3/02.png"
    image d4_sk_katya_3_3 = "minigame/sk/3/03.png"
    image d4_sk_katya_3_4 = "minigame/sk/3/04.png"
    image d4_sk_katya_3_5 = "minigame/sk/3/05.png"
    image d4_sk_katya_3_6 = "minigame/sk/3/06.png"

    image d4_sk_katya_struggle_1 = Animation("d4_sk_katya_1", .2, "d4_sk_katya_2", .2)
    image d4_sk_katya_struggle_2 = Animation("d4_sk_katya_3", .2, "d4_sk_katya_4", .2)
    image d4_sk_katya_struggle_3 = Animation("d4_sk_katya_5", .2, "d4_sk_katya_6", .2)
    image d4_sk_katya_struggle_4 = Animation("d4_sk_katya_7", .2, "d4_sk_katya_8", .2)

    define sk_dt = .1

    image d4_sk_katya_struggle_easy = Animation(
        "d4_sk_katya_struggle_1", 3.4,
        "d4_sk_katya_1_1", sk_dt,
        "d4_sk_katya_1_2", sk_dt,
        "d4_sk_katya_1_3", sk_dt,
        "d4_sk_katya_1_4", sk_dt,
        "d4_sk_katya_1_5", sk_dt,
        "d4_sk_katya_1_6", sk_dt,
        "d4_sk_katya_struggle_2", 99999)

    image d4_sk_katya_struggle_hard = Animation(
        "d4_sk_katya_struggle_2", 2.,
        "d4_sk_katya_2_1", sk_dt,
        "d4_sk_katya_2_2", sk_dt,
        "d4_sk_katya_2_3", sk_dt,
        "d4_sk_katya_2_4", sk_dt,
        "d4_sk_katya_2_5", sk_dt,
        "d4_sk_katya_2_6", sk_dt,
        "d4_sk_katya_struggle_3", 2.,
        "d4_sk_katya_3_1", sk_dt,
        "d4_sk_katya_3_2", sk_dt,
        "d4_sk_katya_3_3", sk_dt,
        "d4_sk_katya_3_4", sk_dt,
        "d4_sk_katya_3_5", sk_dt,
        "d4_sk_katya_3_6", sk_dt,
        "d4_sk_katya_struggle_4", 99999)

    image d4_sk_katya_blood_1 = "locate/street/garage/blood/01.png"
    image d4_sk_katya_blood_2 = "locate/street/garage/blood/02.png"
    image d4_sk_katya_blood_3 = "locate/street/garage/blood/03.png"
    image d4_sk_katya_blood_4 = "locate/street/garage/blood/04.png"
    image d4_sk_katya_blood_5 = "locate/street/garage/blood/05.png"
    image d4_sk_katya_blood_6 = "locate/street/garage/blood/06.png"
    image d4_sk_katya_blood_7 = "locate/street/garage/blood/07.png"
    image d4_sk_katya_blood_8 = "locate/street/garage/blood/08.png"
    image d4_sk_katya_blood_9 = "locate/street/garage/blood/09.png"
    image d4_sk_katya_blood_10 = "locate/street/garage/blood/10.png"
    image d4_sk_katya_blood_11 = "locate/street/garage/blood/11.png"
    image d4_sk_katya_blood_12 = "locate/street/garage/blood/12.png"
    image d4_sk_katya_blood_13 = "locate/street/garage/blood/13.png"
    image d4_sk_katya_blood_14 = "locate/street/garage/blood/14.png"
    image d4_sk_katya_blood_15 = "locate/street/garage/blood/15.png"
    image d4_sk_katya_blood_16 = "locate/street/garage/blood/16.png"
    image d4_sk_katya_blood_17 = "locate/street/garage/blood/17.png"
    image d4_sk_katya_blood_18 = "locate/street/garage/blood/18.png"
    image d4_sk_katya_blood_19 = "locate/street/garage/blood/19.png"
    image d4_sk_katya_blood_20 = "locate/street/garage/blood/20.png"
    image d4_sk_katya_blood_21 = "locate/street/garage/blood/21.png"
    image d4_sk_katya_blood_22 = "locate/street/garage/blood/22.png"
    image d4_sk_katya_blood_23 = "locate/street/garage/blood/23.png"
    image d4_sk_katya_blood_24 = "locate/street/garage/blood/24.png"

    define bd_dt = 0.05
    image d4_sk_katya_blood_animation:
        Null()
        3.
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
                2.
            choice:
                2.5
            choice:
                2.3
            repeat

    image d4_sk_katya_fail = "locate/street/garage/blood/katya.png"
    image d4_sk_katya_fail2 = "locate/street/garage/blood/katya2.png"
    image d4_sk_katya_fail_blood_1 = "minigame/sk/blood/01.png"
    image d4_sk_katya_fail_blood_2 = "minigame/sk/blood/02.png"
    image d4_sk_katya_fail_blood_3 = "minigame/sk/blood/03.png"
    image d4_sk_katya_fail_blood_4 = "minigame/sk/blood/04.png"
    image d4_sk_katya_fail_blood_5 = "minigame/sk/blood/05.png"
    image d4_sk_katya_fail_blood_6 = "minigame/sk/blood/06.png"
    image d4_sk_katya_fail_blood_7 = "minigame/sk/blood/07.png"
    image d4_sk_katya_fail_blood_8 = "minigame/sk/blood/08.png"

    image d4_sk_katya_fail_first_bg = "locate/street/garage/kait/fon.png"
    image d4_sk_katya_fail_first_kate = "locate/street/garage/kait/kaite.png"
    image d4_sk_katya_fail_first_machine = "locate/street/garage/kait/machne.png"

    define bd_f_dt = 0.05
    image d4_sk_katya_fail_blood_animation:
        "d4_sk_katya_fail_blood_1"
        bd_f_dt
        "d4_sk_katya_fail_blood_2"
        bd_f_dt
        "d4_sk_katya_fail_blood_3"
        bd_f_dt
        "d4_sk_katya_fail_blood_4"
        bd_f_dt
        "d4_sk_katya_fail_blood_5"
        bd_f_dt
        "d4_sk_katya_fail_blood_6"
        bd_f_dt
        "d4_sk_katya_fail_blood_7"
        bd_f_dt
        "d4_sk_katya_fail_blood_8"
        bd_f_dt
        Null()

    image d4_garage_antonback = "locate/street/anton_battle/scene_01/Anton.png"

    image d4_blood_polaroid 1 = "locate/street/garage/poloroid_1.png"
    image d4_blood_polaroid 2 = "locate/street/garage/poloroid_2.png"
    image d4_blood_body = "locate/street/garage/blood/body.png"
    image d4_blood_bg = "locate/street/garage/blood/garage_fon.png"
    image d4_blood_head = "locate/street/garage/blood/head.png"
    image d4_blood_head2 = "locate/street/garage/blood/head2.png"
    image d4_blood_head 3 = "locate/street/garage/blood/head3.png"
    image d4_blood_head 4 = LiveComposite((2607, 2589),
        (0, 0), "d4_blood_head 3",
        (0, 0), "locate/street/garage/blood/head4.png")

    image d4_blood_head 5 = LiveComposite((2607, 2589),
        (0, 0), "d4_blood_head 3",
        (0, 0), "locate/street/garage/blood/head5.png")

    image d4_blood_head 6 = "locate/street/garage/blood/head6.png"
    image d4_blood_head 7 = LiveComposite((2607, 2589),
        (0, 0), "d4_blood_head 6",
        (0, 0), "locate/street/garage/blood/head5.png")

    image d4_polaroid_skapl_00 = "locate/street/garage/blood/skalp_00.png"

    image black_3_4:
        "bg_black"
        alpha .95

    image d4_sk_blink:
        contains blink_fast_transform(Null(), "black_3_4")

    image d4_poddon_blink:
        contains blink_transform(Null(), "black_3_4")

    image d4_poddon_blink_nosfx:
        contains blink_transform_nosfx(Null(), "black_3_4")

    image d4_blood_blink:
        contains blink_veryfast_transform("black_3_4", Null())

    image d4_poddon 1 = "locate/street/garage/poddon/01.png"
    image d4_poddon 2 = "locate/street/garage/poddon/02.png"
    image d4_poddon 3 = "locate/street/garage/poddon/03.png"
    image d4_poddon 4 = "locate/street/garage/poddon/04.png"
    image d4_poddon 5 = "locate/street/garage/poddon/05.png"
    image d4_poddon 6 = "locate/street/garage/poddon/06.png"
    image d4_poddon 7 = "locate/street/garage/poddon/07.png"
    image d4_poddon 8 = "locate/street/garage/poddon/08.png"
    image d4_poddon 9 = "locate/street/garage/poddon/09.png"
    image d4_poddon 10 = "locate/street/garage/poddon/10.png"
    image d4_poddon 11 = "locate/street/garage/poddon/11.png"

    image d4_poddon animation:
        "d4_poddon 1"
        .1
        "d4_poddon 2"
        .1
        "d4_poddon 3"
        .1
        "d4_poddon 4"
        .1
        "d4_poddon 5"
        .1
        "d4_poddon 6"
        .1
        "d4_poddon 7"
        .1
        "d4_poddon 8"
        .1
        "d4_poddon 9"
        .1
        "d4_poddon 10"
        .1
        "d4_poddon 11"
        .1
        Null()

    image d4_poddon animation_memory:
        "d4_poddon 1"
        .1
        "d4_poddon 2"
        .1
        "d4_poddon 3"
        .1
        "effect/memory1/field_004.jpg"
        .1
        "d4_poddon 5"
        .1
        "d4_poddon 6"
        .1
        "d4_poddon 7"
        .1
        "d4_poddon 8"
        .1
        "d4_poddon 9"
        .1
        "d4_poddon 10"
        .1
        "d4_poddon 11"
        .1
        "effect/memory1/field_012.jpg"
        .3
        "empty" with Dissolve(1.)

    image d4_help_bg = LiveComposite((2690, 1886),
        (0, 0), "locate/street/garage/blood/Katya_skalp_00.png",
        (0, 0), "locate/street/garage/blood/skalp_00.png")
    image d4_help_after_bg = "locate/street/garage/blood/Katya_skalp.png"
    image d4_help_after_skalp = "locate/street/garage/blood/skalp.png"

    image d4_help_fg = "locate/street/garage/blood/viewfinder.png"

    image d4_photo_hand = "locate/street/garage/foto_hand.png"
    image d4_photo_1 = "locate/street/garage/foto_1.png"
    image d4_photo_2 = "locate/street/garage/foto_2.png"
    image d4_photo_1_veil:
        "d4_photo_1"
        matrixcolor TintMatrix("#ffffff") * ContrastMatrix(0.0)

    image d4_photo:
        contains:
            "d4_photo_hand"
        contains:
            "d4_photo_1_veil"

            1.

            "d4_photo_1" with Dissolve(2.0)
        contains:
            "d4_photo_2"


init:
    image d4_poldoor_1 = "locate/polina/door_polin/door_polin01.png"
    image d4_poldoor_2 = "locate/polina/door_polin/door_polin02.png"

    image d4_polroom_bg:
        contains:
            "locate/polina/room_01.png"
        contains:
            "d4_pendulum"
    image d4_polroom_poster = "locate/polina/room_02.png"
    image d4_polroom_piano = "locate/polina/room_03.png"
    image d4_polroom_cat:
        "locate/polina/d_1.png" with Dissolve(.2)
        .2
        "locate/polina/d_2.png" with Dissolve(.2)
        .2
        "locate/polina/d_3.png" with Dissolve(.2)
        .2
        "locate/polina/d_4.png" with Dissolve(.2)
        .2
        "locate/polina/d_3.png" with Dissolve(.2)
        .2
        "locate/polina/d_2.png" with Dissolve(.2)
        .2
        "locate/polina/d_1.png" with Dissolve(.2)
        4
        repeat
    image d4_polroom_polina_play = "locate/polina/Polina.png"

    image d4_polfon = "locate/polina/Pol_fon.png"

    image d4_pendulum:
        contains:
            "locate/polina/pendulum.png"
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
            "locate/polina/ring.png"

    image d4_polroom_magic_bg = "locate/polina/P_0.png"

    image d4_polroom_magic_polina_norm = "locate/polina/P_1.png"
    image d4_polroom_magic_polina_light = "locate/polina/P_2.png"
    image stone_pie 1 = "locate/school/in_side/Tupichok/pie.png"
    image stone_pie blur = im.Blur("locate/school/in_side/Tupichok/pie.png", 1.0)
    image Polina_home_door = "locate/Polina/Pol_home2.png"
    image shadow_pol_gf 0 = "locate/Polina/Shadow.png"
    image shadow_pol_gf 1 = "locate/Polina/Shadow_1.png"
    image shadow_pol_gf 2 = "locate/Polina/Shadow_2.png"
    image shadow_pol_gf 3 = "locate/Polina/Shadow_3.png"
    image pol_grandpa = "locate/Polina/Hariton.png"
    image pol_grandpa 2:
        xzoom -1
        "locate/Polina/Hariton.png"
    image pol_home_zoom = LiveComposite((1920, 1080),
        (0, 0), "polina_home_day_04",
        (0, 0), "Polina_home_door",
        (400, 0), "pol_grandpa 2")

    image ded_eyes 4 = "sprite/Ded/Happy/m_day/2_eyes/normal/ahead/04.png"
    image ded_eyes 5 = "sprite/Ded/Happy/m_day/2_eyes/normal/ahead/05.png"

    image old_movie_intense:
        "effect/old_movie/old_movie_001.png"
        .10
        Null()
        .20
        "effect/old_movie/old_movie_002.png"
        .10
        Null()
        .70
        "effect/old_movie/old_movie_003.png"
        .10
        Null()
        .20
        "effect/old_movie/old_movie_004.png"
        .10
        Null()
        .70
        repeat

    image koshmar ded 0:
        contains:
            "locate/polina/hariton_00.png"
        contains:
            "old_movie_intense"
    image koshmar ded 1:
        contains:
            "locate/polina/hariton_01.png"
        contains:
            "old_movie_intense"
    image koshmar ded 2:
        contains:
            "locate/polina/hariton_02.png"
        contains:
            "old_movie_intense"
    image koshmar ded 3:
        contains:
            "locate/polina/hariton_03.png"
        contains:
            "old_movie_intense"
    image koshmar ded 4:
        contains:
            "locate/polina/hariton_04.png"
        contains:
            "old_movie_intense"
    image koshmar ded 5:
        contains:
            "locate/polina/hariton_05.png"
        contains:
            "old_movie_intense"
            matrixcolor BrightnessMatrix(1.)
    image koshmar ded 6:
        contains:
            "locate/polina/hariton_06.png"
        contains:
            "old_movie_intense"
    image koshmar ded 7:
        contains:
            "locate/polina/hariton_07.png"
        contains:
            "old_movie_intense"
    image koshmar ded 8:
        contains:
            "locate/polina/hariton_08.png"
        contains:
            "old_movie_intense"
    image koshmar ded 9:
        contains:
            "locate/polina/hariton_09.png"
        contains:
            "old_movie_intense"

    image d4_deddoor 1 = "locate/polina/mirrow/door_big_idle.png"
    image d4_deddoor 2 = "locate/polina/mirrow/door_big_open_1.png"
    image d4_deddoor 3 = "locate/polina/mirrow/door_big_open_2.png"
    image d4_deddoor 4 = "locate/polina/mirrow/door_big_opened.png"
    image d4_deddoor_inside = "locate/polina/mirrow/inside.png"
    image d4_deddoor_inside2 = "locate/polina/mirrow/inside2.png"

    image d4_deddoor open:
        "locate/polina/mirrow/door_big_open_1.png"
        .1
        "locate/polina/mirrow/door_big_open_2.png"
        .1
        "locate/polina/mirrow/door_big_opened.png"


    image d4_polmirror_bg idle = "locate/polina/mirrow/door_1.png"
    image d4_polmirror_bg statter1:
        "locate/polina/mirrow/door_1.png"
        .1
        "locate/polina/mirrow/door_2.png"
        .1
        "locate/polina/mirrow/door_3.png"
        .1
        "locate/polina/mirrow/door_2.png"
        .1
        "locate/polina/mirrow/door_1.png"
    image d4_polmirror_bg statterloop:
        "d4_polmirror_bg statter1"
        .5
        "d4_polmirror_bg statter1"
        8.
        "d4_polmirror_bg statter1"
        8.
        repeat
    image d4_polmirror_ant down:
        "locate/polina/mirrow/An0.png"
        1.
        "locate/polina/mirrow/An2.png"
        .1
        "locate/polina/mirrow/An3.png"
        .1
        "locate/polina/mirrow/An2.png"
        .1
        "d4_polmirror_ant straight"

    image d4_polmirror_ant straight:
        "locate/polina/mirrow/An1.png"
        7
        "locate/polina/mirrow/An2.png"
        .1
        "locate/polina/mirrow/An3.png"
        .1
        "locate/polina/mirrow/An2.png"
        .1
        repeat

    image d4_boar_fall:
        "locate/polina/mirrow/K1.png"
        .1
        "locate/polina/mirrow/K2.png"



    image d4_boar scream:
        "locate/polina/mirrow/K4.png"
        .1
        "locate/polina/mirrow/K3.png"
        .1
        "locate/polina/mirrow/K4.png"
        .1
        "locate/polina/mirrow/K3.png"
        .1

    image d4_boar_bg:
        "locate/polina/mirrow/Kfon.png"

    image d4_boar_hand:
        "locate/polina/mirrow/K.png"
        block:
            linear .5 xoffset -5 yoffset 0
            linear .5 xoffset 0 yoffset -5
            linear .5 xoffset -5 yoffset 5
            linear .5 xoffset 5 yoffset 5
            linear .5 xoffset 0 yoffset 0
            repeat

    image d4_polmirror_ant scared = "locate/polina/mirrow/An4.png"
    image d4_polmirror_fg = "locate/polina/mirrow/MIRROW.png"
    image d4_polmirror_dust:
        "locate/polina/mirrow/Dust_01.png"
        .1
        "locate/polina/mirrow/Dust_02.png"
        .1
        "locate/polina/mirrow/Dust_03.png"
        .1
        "locate/polina/mirrow/Dust_04.png"
        .1
        "locate/polina/mirrow/Dust_05.png"
        .1
        Null()

    image d4_poster_close = "locate/polina/kiss/P001.png"
    image d4_poster_buster:
        "locate/polina/kiss/P001.png"
        .1
        "locate/polina/kiss/P002.png"
        .1
        "locate/polina/kiss/P003.png"
        .1
        "locate/polina/kiss/P004.png"
        .1
        "locate/polina/kiss/P005.png"
        .1
        "locate/polina/kiss/P006.png"
        .1
        "locate/polina/kiss/P007.png"
        .1
        "locate/polina/kiss/P008.png"
        .1
        "locate/polina/kiss/P009.png"
        .1
        "locate/polina/kiss/P010.png"

    image d4_piano 1 = "locate/polina/piano1.png"
    image d4_piano 2 = "locate/polina/piano2.png"
    image d4_piano 3 = "locate/polina/piano3.png"
    image d4_piano 4 = "locate/polina/piano4-6.png"
    image d4_piano 5 = "locate/polina/piano5.png"
    image d4_piano 6 = "locate/polina/piano4-6.png"
    image d4_piano:
        "d4_piano 1"
        .1
        "d4_piano 2"
        .1
        "d4_piano 3"
        .1
        "d4_piano 4"
        parallel:
            .1
            "d4_piano 5"
            .1
            "d4_piano 6"
        parallel:
            linear .05 yoffset 5
            linear .05 yoffset -5
            linear .05 yoffset 0

    image d4_dj_cat = "locate/polina/dj/cat.png"
    image d4_dj_cat_0 = "locate/polina/dj/cat0.png"
    image d4_dj_cat_1 = "locate/polina/dj/cat1.png"
    image d4_dj_cat_2 = "locate/polina/dj/cat2.png"
    image d4_dj_cat_3 = "locate/polina/dj/cat3.png"
    image d4_dj_cat_4 = "locate/polina/dj/cat4.png"
    image d4_dj 2 = "locate/polina/dj/Djoan_02.png"
    image d4_dj 3 = "locate/polina/dj/Djoan_03.png"
    image d4_dj 4 = "locate/polina/dj/Djoan_04.png"

    image d4_cat_stani:
        "d4_dj_cat_1"
        .25
        "d4_dj_cat_4"
        .25
        block:
            "d4_dj_cat_2"
            .3
            "d4_dj_cat_3"
            .3
            repeat

    image d4_ant_feet 1 = "locate/polina/foot_a_1.png"
    image d4_ant_feet 2 = "locate/polina/foot_a_2.png"
    image d4_ant_feet 3 = "locate/polina/foot_a_3.png"
    image d4_ant_feet 4 = "locate/polina/foot_a_4.png"
    image d4_ant_feet 5 = "locate/polina/foot_a_5.png"

    image d4_pol_feet 1 = "locate/polina/foot_p_1.png"
    image d4_pol_feet 2 = "locate/polina/foot_p_2.png"
    image d4_pol_feet 3 = "locate/polina/foot_p_3.png"

    image d4_dj_bg = "locate/polina/dj/d_fon.png"

    image d4_dj_scream:
        "locate/polina/dj/d01.png"
        .1
        "locate/polina/dj/d02.png"
        .1
        "locate/polina/dj/d03.png"
        .1
        "locate/polina/dj/d02.png"
        .1
        "locate/polina/dj/d01.png"
        .1
        repeat

    image d4_polup = "locate/polina/fon_up.png"

    image d4_polant = "locate/polina/a.png"
    image d4_polhand = "locate/polina/hand2.png"
    image d4_polstani = "locate/polina/stani.png"

    image d4_polvata = "locate/polina/vata.png"

    image d4_polvata_floor = "locate/polina/floor.png"
    image d4_polvata_feet = "locate/polina/foot.png"

    image d4_polina_kiss_eyes:
        "sprite/polina/up/b_day/2_eyes/norm/ahead/01.png"
        .1
        "sprite/polina/up/b_day/2_eyes/norm/ahead/02.png" with Dissolve(.15)
        .25
        "sprite/polina/up/b_day/2_eyes/norm/ahead/03.png" with Dissolve(.15)

    image d4_polina_kiss_mouth:
        "sprite/polina/up/b_day/3_mouth/03.png"
        "sprite/polina/up/b_day/3_mouth/02.png" with Dissolve(.5)

    image d4_polina_kiss_full = LiveComposite((1920, 1519),
        (0, 0), "sprite/polina/up/b_day/1_body/03.png",
        (0, 0), "d4_polina_kiss_eyes",
        (0, 0), "d4_polina_kiss_mouth")

    image d4_polina_kiss_kiss = "locate/polina/kiss/kiss.png"
    image d4_polina_kiss_eyes 0 = LiveComposite((2338, 1080),
        (0, 0), Null())
    image d4_polina_kiss_eyes 1 = "locate/polina/kiss/01.png"
    image d4_polina_kiss_eyes 2 = "locate/polina/kiss/02.png"

    image d4_polina_kiss_kiss_crop = Crop((0, 0, 1920, 1080), "d4_polina_kiss_kiss")
    image d4_polina_kiss_eyes 3 = Crop((0, 0, 1920, 1080), "locate/polina/kiss/03.png")

    image focus_line = "locate/street/Focus/Fok_1.png"

    image d4_polhar_bg = "locate/polina/kiss/fonh.png"

    image d4_polhar_witness 1 = "locate/polina/kiss/har.png"
    image d4_polhar_witness 2 = "locate/polina/kiss/har2.png"
    image d4_polhar_witness 3 = "locate/polina/kiss/har3.png"

    image d4_hysteria = "locate/polina/kiss/hysterics.png"

    image d4_hysteria2:
        "locate/polina/kiss/hysterics1.png" with Dissolve(.2)

        .5

        "locate/polina/kiss/hysterics2.png" with Dissolve(.2)

        1.

        block:
            "locate/polina/kiss/hysterics1.png" with Dissolve(.2)

            choice:
                pause 2
            choice:
                pause 2.5
            choice:
                pause 3

            "locate/polina/kiss/hysterics2.png" with Dissolve(.2)

            choice:
                pause 2
            choice:
                pause 2.5
            choice:
                pause 3

            repeat

    image d4_polhouse_night = "locate/polina/house_pol_night.png"

    image d4_anton_shy_blink:
        "locate/school/in_side/Anton_class/shy/01.png"
        choice:
            3.
        choice:
            4.
        choice:
            5.
        "locate/school/in_side/Anton_class/shy/02.png"
        .1
        "locate/school/in_side/Anton_class/shy/03.png"
        .1
        "locate/school/in_side/Anton_class/shy/02.png"
        .1
        repeat

    image d4_skirli = "locate/polina/Skirle.png"


init:
    image d4_rom_dark 0 = "locate/street/rom0.png"
    image d4_rom_dark 1 = "locate/street/rom1.png"
    image d4_rom_dark 2 = "locate/street/rom2.png"

    image road_night = "locate/street/road_night_002.jpg"

    image d4_rom_dark_knife:
        "locate/polina/rom_dark/r_dark.png"
        block:
            linear .2 xoffset 0 yoffset -5
            linear .2 xoffset -5 yoffset 0
            linear .2 xoffset 5 yoffset 0
            linear .2 xoffset 0 yoffset 5
            repeat

    image d4_rom_dark_road:
        contains:
            "locate/polina/rom_dark/road.png"
        contains:
            "locate/polina/rom_dark/road1.png" with Dissolve(.1)
            .1
            "locate/polina/rom_dark/road2.png" with Dissolve(.1)
            .1
            repeat

    image d4_traktor_anton_silhuete 4 = AlphaMask(Solid("#0004"), "locate/polina/rom_dark/anton.png")
    image d4_traktor_anton_silhuete 5 = AlphaMask(Solid("#0005"), "locate/polina/rom_dark/anton.png")

    image d4_traktor_anton = "locate/polina/rom_dark/anton.png"
    image d4_traktor_eyes = "locate/polina/rom_dark/anton2.png"

    image d4_traktor_shadow 1 = "locate/polina/rom_dark/shadow01.png"
    image d4_traktor_shadow 2 = "locate/polina/rom_dark/shadow02.png"
    image d4_traktor_shadow 3 = "locate/polina/rom_dark/shadow03.png"

    image d4_traktor_shadow:
        "d4_traktor_shadow 1"
        .1
        "d4_traktor_shadow 2"
        .1
        "d4_traktor_shadow 3"
        .1
        Null()
    image half_shadow:
        "bg_black"
        alpha .5
    image d4_fonari_blink:
        contains blink_fast_transform(Null(), "half_shadow")

    image d4_fonari_blink_slow:
        contains blink_transform(Null(), "half_shadow")

    image d4_selmag 1 = "locate/street/selmag01.png"
    image d4_selmag 2 = "locate/street/selmag02.png"
    image d4_selmag_full:
        contains blink_fast_transform("d4_selmag 1", "d4_selmag 2")

    image d4_selmag_full_nosfx:
        contains blink_fast_transform_nosfx("d4_selmag 1", "d4_selmag 2")

    image d4_selmag_close_fon = "locate/polina/rom_dark/selmag/fon.png"
    image d4_selmag_close_mag = "locate/polina/rom_dark/selmag/mag.png"

    image d4_selmag_close:
        contains:
            "d4_selmag_close_fon"
        contains:
            "d4_selmag_close_mag"

    image d4_selmag_shadow = "locate/polina/rom_dark/selmag/shadow_ant.png"

    image selmag_zaglushka:
        contains:
            "d4_selmag_close"
            align (0., .5)
        contains:
            "d4_selmag_shadow"
            yalign 1.

    image d4_selmag_reflect_anton = "locate/polina/rom_dark/selmag/anton1.png"

    image d4_selmag_phantom = "locate/polina/rom_dark/selmag/shadow3.png"
    image d4_selmag_phantom_shadow = "locate/polina/rom_dark/selmag/shadow2.png"

    image d4_night_run_anton_hair_base:
        contains:
            "locate/forest/runaway/runaway_night/anton/run_away_003.png"
        contains:
            "locate/forest/runaway/runaway_night/anton/01.png"
            .05
            "locate/forest/runaway/runaway_night/anton/02.png"
            .05
            "locate/forest/runaway/runaway_night/anton/03.png"
            .05
            "locate/forest/runaway/runaway_night/anton/04.png"
            .05
            "locate/forest/runaway/runaway_night/anton/05.png"
            .05
            "locate/forest/runaway/runaway_night/anton/06.png"
            .05
            "locate/forest/runaway/runaway_night/anton/07.png"
            .05
            "locate/forest/runaway/runaway_night/anton/08.png"
            .05
            repeat


    image d4_night_run_anton_hair_glow:
        contains:
            "d4_night_run_anton_hair_base"
        contains:
            "locate/forest/runaway/runaway_night/anton/00.png"


    image d4_night_run_anton_hair_noglow:
        contains:
            "d4_night_run_anton_hair_base"

    image d4_night_run_anton_glow:
        "d4_night_run_anton_hair_glow"
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

    image d4_night_run_anton_noglow:
        "d4_night_run_anton_hair_noglow"
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

    image d4_runaway_night:
        contains:
            "locate/forest/runaway/runaway_night/0002.jpg"
        contains:
            "day3_night_run_bg1"
        contains:
            "day3_night_run_bg2"
        contains:
            "d4_night_run_anton_glow"

    image d4_runaway_night_noglow:
        contains:
            "locate/forest/runaway/runaway_night/0002.jpg"
        contains:
            "day3_night_run_bg1"
        contains:
            "day3_night_run_bg2"
        contains:
            "d4_night_run_anton_noglow"

    image d4_runaway_night_bg:
        contains:
            "locate/forest/runaway/runaway_night/0002.jpg"
        contains:
            "day3_night_run_bg1"
        contains:
            "day3_night_run_bg2"

    image d4_roadwood = "locate/forest/road_wood03.jpg"

    image d4_forest_wolf 1 = "locate/polina/wolf/wolf1.png"
    image d4_forest_wolf 2 = "locate/polina/wolf/wolf2.png"

    image d4_scary_A = "locate/forest/scary/Scary_A.png"

    image d4_pol_drom_0 = "locate/polina/rom_dark/0.png"
    image d4_pol_drom_blood = "locate/polina/rom_dark/blood.png"
    image d4_pol_drom_boy1 = "locate/polina/rom_dark/boy1.png"
    image d4_pol_drom_boy2 = "locate/polina/rom_dark/boy2.png"
    image d4_pol_drom_hand 1 = "locate/polina/rom_dark/hand.png"
    image d4_pol_drom_hand 2 = "locate/polina/rom_dark/hand2.png"
    image d4_pol_drom_fonsnow = "locate/polina/rom_dark/fon_snow.png"

    image d4_pierce:
        contains:
            "d4_pol_drom_fonsnow"
        contains:
            "d4_pol_drom_boy1"
        contains:
            "d4_pol_drom_hand 1"
            align (.5, .5)
            ypos 500
        contains:
            "d4_pol_drom_boy2"

    image d4_murder 1 = "locate/polina/rom_dark/murder01.png"
    image d4_murder 2 = "locate/polina/rom_dark/murder02.png"

    python:
        def play_knife_stab(trans, st, at):
            rnd = renpy.random.randint(1, 6)
            renpy.play("sounds/sfx_knife_stab_" + str(rnd) + ".ogg", channel="sound")
    image d4_murder_loop_sfx:
        pause .6
        function play_knife_stab
        pause .7
        repeat
    image d4_murder loop:
        contains:
            animation
            yalign .7
            "d4_murder 1"
            linear .1 yalign 0.5
            .5
            "d4_murder 2"
            linear .1 yalign 0.7
            linear .05 yalign 0.65
            linear .05 yalign 0.7
            .5
            repeat
        contains:
            animation
            "d4_murder 2"
            yalign .7
            xalign .5
            alpha 0
            block:
                pause .6
                zoom 1
                alpha .5
                linear .5 zoom 1.1 alpha 0
                pause .2
                repeat
        contains:
            animation
            "bg_black"
            alpha 0
            .1
            .5
            .1
            alpha 0.1
            .05
            alpha 0
            .05
            .5
            repeat

    image d4_dr_wolf_body = "locate/polina/wolf/body.png"
    image d4_dr_wolf_hand 1 = "locate/polina/wolf/hand_1.png"
    image d4_dr_wolf_hand 2 = "locate/polina/wolf/hand_2.png"
    image d4_dr_wolf_knife = "locate/polina/wolf/khife.png"
    image d4_dr_wolf_shadow = "locate/polina/wolf/khife_shadow.png"

    image d4_dr_wolf_eyes static = "sprite/Wolf/eyes_wolf/02-04.png"

    image d4_dr_wolf_eyes animation:
        "sprite/Wolf/eyes_wolf/01.png"
        .1
        "sprite/Wolf/eyes_wolf/02-04.png"
        .1
        "sprite/Wolf/eyes_wolf/03.png"
        .1
        "sprite/Wolf/eyes_wolf/02-04.png"


    image d4_dr_scary_base = "locate/forest/scary/Scary/Scary.png"
    image d4_dr_scary_eyes = "locate/forest/scary/Scary/01.png"
    image d4_scary_eyes_glow = "locate/forest/scary/Scary/00.png"

    image d4_murder_gallery1 = "locate/polina/rom_dark/gallary1.png"
    image d4_murder_gallery2 = "locate/polina/rom_dark/gallary2.png"

    image d4_murder_moscow = "locate/polina/rom_dark/moscow.png"

    image d4_murder_baby_bg = "locate/polina/rom_dark/baby/fon0.png"
    image d4_murder_baby_noise 1 = "locate/polina/rom_dark/baby/01.png"
    image d4_murder_baby_noise 2 = "locate/polina/rom_dark/baby/02.png"
    image d4_murder_baby_noise 3 = "locate/polina/rom_dark/baby/03.png"
    image d4_murder_baby_noise 4 = "locate/polina/rom_dark/baby/04.png"
    image d4_murder_baby_noise:
        "d4_murder_baby_noise 1"
        .4
        "d4_murder_baby_noise 2"
        .4
        "d4_murder_baby_noise 3"
        .4
        "d4_murder_baby_noise 4"
        .4
        repeat


    image d4_murder_spots:
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

    image d4_father_old_noise:
        "sprite/dad/father_old_noise1.png"
        .4
        "sprite/dad/father_old_noise2.png"
        .4
        "sprite/dad/father_old_noise3.png"
        .4
        "sprite/dad/father_old_noise4.png"
        .4
        repeat
    image d4_mutter_old_noise:
        "sprite/mom/mother_old_noise3.png"
        .4
        "sprite/mom/mother_old_noise4.png"
        .4
        "sprite/mom/mother_old_noise1.png"
        .4
        "sprite/mom/mother_old_noise2.png"
        .4
        repeat

    image d4_father_old = LiveComposite((723, 1080),
        (0, 0), "sprite/dad/father_old.png",
        (0, 0), "d4_father_old_noise")

    image d4_mutter_old = LiveComposite((674, 1080),
        (0, 0), "sprite/mom/mother_old.png",
        (0, 0), "d4_mutter_old_noise")


init:
    image d4_tihonov:
        "minigame/case/Tihonov.png"
        zoom .9

    image d4_guard_blink:
        contains:
            "images/minigame/case/guard1.png"
        contains:
            Null()
            8.
            "images/minigame/case/guard2.png"
            .1
            "images/minigame/case/guard3.png"
            .1
            "images/minigame/case/guard2.png"
            .1
            repeat

    image d4_guard:
        "d4_guard_blink"
        zoom .9

    image d4_dep_shadow:
        "locate/police/man/shadow/01.png"
        .1
        "locate/police/man/shadow/02.png"
        .1
        "locate/police/man/shadow/03.png"
        .1
        "locate/police/man/shadow/04.png"
        .1
        "locate/police/man/shadow/05.png"
        .1
        "locate/police/man/shadow/06.png"
        .1
        "locate/police/man/shadow/07.png"
        .1
        "locate/police/man/shadow/08.png"
        .1
        "locate/police/man/shadow/09.png"
        .1
        "locate/police/man/shadow/10.png"
        .1
        repeat

    image d4_dep_bg:

        contains:
            "locate/police/police-room02.png"


        contains:
            "d4_dep_shadow"
            xzoom 1
            xoffset 1300
            yoffset 450
            pause 2.

            linear 3. xoffset 800

            pause 8.

            xzoom -1
            linear 3. xoffset 1300

            pause 14.

            repeat


        contains:
            "locate/police/police-room03.png"


        contains:
            "locate/police/police-room.png"

    image d4_dep_door = "locate/police/police-room_door.png"

    image d4_dep_board = "locate/police/doska.png"
    image d4_dep_board_witness = "locate/police/doska1.png"

    image d4_dep_mail = "locate/police/mail4.png"

    image d4_pavlovna 1 = "sprite/Liliya/Normal/m_day_winter/1_body/01.png"
    image d4_pavlovna 2 = "sprite/Liliya/Normal/m_day_winter/1_body/02.png"
    image d4_pavlovna 3 = "sprite/Liliya/Normal/m_day_winter/1_body/03.png"

    image d4_station = "locate/police/police_station.png"
    image d4_station_boy1 = "locate/police/boy1.png"
    image d4_station_boy2 = "locate/police/boy2.png"

    image d4_station_memory_img = "locate/home/in_side/2st_floor/olga_room/Reportash/b2.jpg"
    image d4_station_memory:
        contains:
            "d4_station_memory_img"
        contains:
            "ramka"


init:
    image d4_house_night_snowless:
        contains:
            "locate/home/out_side/hOUSE6_1.png"
        contains:
            "locate/home/out_side/hOUSE6_2.png"
        contains:
            "locate/home/out_side/hOUSE6_3.png"

    image d4_house_radio = "locate/home/in_side/1st_floor/kitchen/radio.png"

    image d4_hall_walkup 0:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 0.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign -1.
    image d4_hall_walkup 1:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 0.
            linear 12. xalign 1.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign -1.
            linear 12. xalign 1.
        contains:
            "bg_black"
            alpha 0
            10
            linear 2 alpha 1

    image d4_home_arguing_bg:
        "locate/home/in_side/2st_floor/hallway/row1.png"
        .2
        block:
            "locate/home/in_side/2st_floor/hallway/row2.png" with Dissolve(.5)
            .5
            "locate/home/in_side/2st_floor/hallway/row3.png" with Dissolve(.5)
            .5
            "locate/home/in_side/2st_floor/hallway/row1.png" with Dissolve(.5)
            .5
            repeat
    image d4_home_arguing_ant = "locate/home/in_side/2st_floor/hallway/row0.png"

    image d4_hall_ant = "locate/home/in_side/2st_floor/hallway/a2.png"
    image d4_hall_hug = "locate/home/in_side/2st_floor/hallway/a3.png"
    image d4_hall_olya 1 = "locate/home/in_side/2st_floor/hallway/ol_01.png"
    image d4_hall_olya 2 = "locate/home/in_side/2st_floor/hallway/ol_02.png"
    image d4_hall_corridor = "locate/home/in_side/2st_floor/hallway/corridor.png"
    image d4_hall_corridor_door1 = "locate/home/in_side/2st_floor/hallway/door_1.png"
    image d4_hall_corridor_door2 = "locate/home/in_side/2st_floor/hallway/door_2.png"
    image d4_room = "locate/home/in_side/2st_floor/olga_room/Ol_Ant.jpg"
    image d4_room_2 = "locate/home/in_side/2st_floor/olga_room/Ol_Ant2.png"

    image d4_hall_corridor d1:
        LiveComposite((2475, 1080),
        (0, 0), "d4_hall_corridor",
        (0, 0), "d4_hall_corridor_door1")
    image d4_hall_corridor d2:
        LiveComposite((2475, 1080),
        (0, 0), "d4_hall_corridor",
        (0, 0), "d4_hall_corridor_door2")
    image d4_hall_corridor d1 d2:
        LiveComposite((2475, 1080),
        (0, 0), "d4_hall_corridor",
        (0, 0), "d4_hall_corridor_door1",
        (0, 0), "d4_hall_corridor_door2")

    image d4_olya_darkness Suffer = AlphaMask("bg_black", "Olya Suffer m_evening 01 good ahead 01")
    image d4_olya_darkness Weeps = AlphaMask("bg_black", "Olya Weeps m_evening 01 good ahead 00")
    image d4_olya_darkness Suffer big = AlphaMask("bg_black", "Olya Suffer b_evening 01 good ahead 01")
    image d4_olya_darkness Weeps big = AlphaMask("bg_black", "Olya Weeps b_evening 01 good ahead 01")
    image d4_olya_darkness Prof = AlphaMask("bg_black", "Olya Prof m_evening 01 good aside 01")

    image d4_old_movie_black:
        "old_movie2_001_002_003_004"
        matrixcolor BrightnessMatrix(.0)

    image d4_old_movie_effect:
        contains blink_fast_transform("d4_old_movie_black", Null())

    image d4_table_bg = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table5.jpg"
    image d4_table_bg_closed = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table6.jpg"
    image d4_table_glove = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table07.png"
    image d4_table_number = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table06.png"
    image d4_table_record = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table08.png"
    image d4_table_finger = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table00.png"
    image d4_table_photo = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/foto.png"


init:
    image d4_antroom_door = "locate/home/in_side/2st_floor/anton_room/room_night_door.png"
    image d4_window_bg_24 = "locate/home/in_side/2st_floor/anton_room/window_par/024.jpg"
    image d4_window_frame = "locate/home/in_side/2st_floor/anton_room/window_par/0000.png"
    image d4_window_frame2 = "locate/home/in_side/2st_floor/anton_room/window_par/Window3.png"

    image d4_window_bg_base = "locate/home/in_side/2st_floor/anton_room/window_par/000.jpg"

    image d4_window_bg_owl 1 = "locate/home/in_side/2st_floor/anton_room/window_par/S1.png"
    image d4_window_bg_owl 2 = "locate/home/in_side/2st_floor/anton_room/window_par/S2.png"
    image d4_window_bg_owl 3 = "locate/home/in_side/2st_floor/anton_room/window_par/S3.png"
    image d4_window_bg_owl 4 = "locate/home/in_side/2st_floor/anton_room/window_par/S4.png"
    image d4_window_bg_owl 5 = "locate/home/in_side/2st_floor/anton_room/window_par/S5.png"
    image d4_window_bg_owl 6 = "locate/home/in_side/2st_floor/anton_room/window_par/S6.png"
    image d4_window_bg_owl idle = "d4_window_bg_owl 1"
    define owl_wave_dt = .15
    image d4_window_bg_owl wave:
        "d4_window_bg_owl 2"
        owl_wave_dt
        "d4_window_bg_owl 3"
        owl_wave_dt
        block:
            "d4_window_bg_owl 4"
            owl_wave_dt
            "d4_window_bg_owl 5"
            owl_wave_dt
            "d4_window_bg_owl 6"
            owl_wave_dt
            "d4_window_bg_owl 5"
            owl_wave_dt
            repeat
    image d4_window_bg_owl waveoff:
        "d4_window_bg_owl 4"
        owl_wave_dt
        "d4_window_bg_owl 3"
        owl_wave_dt
        "d4_window_bg_owl 2"
        owl_wave_dt
        "d4_window_bg_owl 1"

    image d4_window_bg_fox 1 = "locate/home/in_side/2st_floor/anton_room/window_par/F1.png"
    image d4_window_bg_fox 2 = "locate/home/in_side/2st_floor/anton_room/window_par/F2.png"
    image d4_window_bg_fox 3 = "locate/home/in_side/2st_floor/anton_room/window_par/F3.png"
    image d4_window_bg_fox 4 = "locate/home/in_side/2st_floor/anton_room/window_par/F4.png"
    image d4_window_bg_fox 5 = "locate/home/in_side/2st_floor/anton_room/window_par/F5.png"
    image d4_window_bg_fox 6 = "locate/home/in_side/2st_floor/anton_room/window_par/F6.png"
    image d4_window_bg_fox idle = "d4_window_bg_fox 1"
    define fox_wave_dt = .1
    define fox_wave_ddt = fox_wave_dt * .25
    image d4_window_bg_fox wave:
        "d4_window_bg_fox 2" with Dissolve(fox_wave_ddt)
        fox_wave_dt
        "d4_window_bg_fox 3" with Dissolve(fox_wave_ddt)
        fox_wave_dt
        block:
            "d4_window_bg_fox 4" with Dissolve(fox_wave_ddt)
            fox_wave_dt
            "d4_window_bg_fox 5" with Dissolve(fox_wave_ddt)
            fox_wave_dt
            "d4_window_bg_fox 6" with Dissolve(fox_wave_ddt)
            fox_wave_dt
            "d4_window_bg_fox 5" with Dissolve(fox_wave_ddt)
            fox_wave_dt
            repeat
    image d4_window_bg_fox waveoff:
        "d4_window_bg_fox 4" with Dissolve(fox_wave_ddt)
        fox_wave_dt
        "d4_window_bg_fox 3" with Dissolve(fox_wave_ddt)
        fox_wave_dt
        "d4_window_bg_fox 2" with Dissolve(fox_wave_ddt)
        fox_wave_dt
        "d4_window_bg_fox 1" with Dissolve(fox_wave_ddt)

    image d4_window_bg_bear 1 = "locate/home/in_side/2st_floor/anton_room/window_par/B1.png"
    image d4_window_bg_bear 2 = "locate/home/in_side/2st_floor/anton_room/window_par/B2.png"
    image d4_window_bg_bear 3 = "locate/home/in_side/2st_floor/anton_room/window_par/B3.png"
    image d4_window_bg_bear 4 = "locate/home/in_side/2st_floor/anton_room/window_par/B4.png"
    image d4_window_bg_bear 5 = "locate/home/in_side/2st_floor/anton_room/window_par/B5.png"
    image d4_window_bg_bear 6 = "locate/home/in_side/2st_floor/anton_room/window_par/B6.png"
    image d4_window_bg_bear idle = "d4_window_bg_bear 1"
    define bear_wave_dt = .2
    image d4_window_bg_bear wave:
        "d4_window_bg_bear 2" with Dissolve(.2)
        bear_wave_dt
        "d4_window_bg_bear 3" with Dissolve(.2)
        bear_wave_dt
        block:
            "d4_window_bg_bear 4" with Dissolve(.2)
            bear_wave_dt *3
            "d4_window_bg_bear 5" with Dissolve(.2)
            bear_wave_dt
            "d4_window_bg_bear 6" with Dissolve(.2)
            bear_wave_dt *3
            "d4_window_bg_bear 5" with Dissolve(.2)
            bear_wave_dt
            repeat
    image d4_window_bg_bear waveoff:
        "d4_window_bg_bear 4"
        bear_wave_dt
        "d4_window_bg_bear 3"
        bear_wave_dt
        "d4_window_bg_bear 2"
        bear_wave_dt
        "d4_window_bg_bear 1"

    image d4_window_bg_wolf 1 = "locate/home/in_side/2st_floor/anton_room/window_par/W1.png"
    image d4_window_bg_wolf 2 = "locate/home/in_side/2st_floor/anton_room/window_par/W2.png"
    image d4_window_bg_wolf 3 = "locate/home/in_side/2st_floor/anton_room/window_par/W3.png"
    image d4_window_bg_wolf 4 = "locate/home/in_side/2st_floor/anton_room/window_par/W4.png"
    image d4_window_bg_wolf 5 = "locate/home/in_side/2st_floor/anton_room/window_par/W5.png"
    image d4_window_bg_wolf 6 = "locate/home/in_side/2st_floor/anton_room/window_par/W6.png"
    image d4_window_bg_wolf idle = "d4_window_bg_wolf 1"
    define wolf_wave_dt = .05
    image d4_window_bg_wolf wave:
        "d4_window_bg_wolf 2"
        wolf_wave_dt
        "d4_window_bg_wolf 3"
        wolf_wave_dt
        block:
            "d4_window_bg_wolf 4"
            wolf_wave_dt
            "d4_window_bg_wolf 5"
            wolf_wave_dt
            "d4_window_bg_wolf 6"
            wolf_wave_dt
            "d4_window_bg_wolf 5"
            wolf_wave_dt
            repeat
    image d4_window_bg_wolf waveoff:
        "d4_window_bg_wolf 4"
        wolf_wave_dt
        "d4_window_bg_wolf 3"
        wolf_wave_dt
        "d4_window_bg_wolf 2"
        wolf_wave_dt
        "d4_window_bg_wolf 1"

    image d4_fence = "locate/home/in_side/1st_floor/hall/H1/fence.png"

    image d4_hfence_bg = "locate/home/out_side/meet_beasts/FonH.jpg"
    image d4_hfence_fence = "locate/home/out_side/meet_beasts/HH.png"


    image roma_day4_bezumie 03 = "locate/Polina/Rom_Dark/road3.png"
    image roma_day4_bezumie 04 = "locate/Polina/Rom_Dark/road4.png"
    image roma_day4_bezumie 05 = "locate/Polina/Rom_Dark/road5.png"
    image roma_day4_bezumie 06 = "locate/Polina/Rom_Dark/road6.png"
    image roma_day4_bezumie 07 = "locate/Polina/Rom_Dark/road7.png"
    image romka_road_bg = "locate/Polina/Rom_Dark/road.png"
    image roma_road_anim:
        "roma_day4_bezumie 04"
        pause .1
        "roma_day4_bezumie 05"
        pause .1
        "roma_day4_bezumie 06"
        pause .1
        "roma_day4_bezumie 07"
    image traktor_02 = "locate/Polina/Rom_Dark/tractor.png"
    image police_station = "locate/police/police-station.png"
    image police_01 = "locate/police/police.png"
    image police_roma = "locate/police/boy1.png"
    image police_anton = "locate/police/boy2.png"
    image bg house_day_no_voron = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/hOUSE_fon.jpg",
        (0, 0), "locate/home/out_side/hOUSE_obj.png")

    image d4_bg_house_night_4 = "locate/home/out_side/hOUSE_night04.jpg"
    image d4_bg_house_night_7 = "locate/home/out_side/hOUSE_night07.jpg"
    image d4_bg_house_tree = "locate/home/out_side/hOUSE6_3.png"

    image d4_home_door_open_dark_bg = "locate/home/in_side/1st_floor/hall/hall_night_fon.png"
    image d4_home_door_open_dark = "locate/home/in_side/1st_floor/hall/hall_night_1.png"
    image d4_home_door_dark = "locate/home/in_side/1st_floor/hall/hall_night.png"
    image d4_home_door_evening = "locate/home/in_side/1st_floor/hall/hall01_ivning.png"

    image d4_fox_give_bg = "locate/home/out_side/Meet_beasts/fon.jpg"
    image d4_fox_give_3 = "locate/home/out_side/Meet_beasts/Fox_give3.png"
    image d4_fox_give_5 = "locate/home/out_side/Meet_beasts/Fox_give5.png"

    image d4_fox_give_owl 1 = "locate/home/out_side/Meet_beasts/Olw.png"
    image d4_fox_give_owl 2 = "locate/home/out_side/Meet_beasts/Olw2.png"

    image d4_fox_tail_0 = "sprite/Fox/fox_tail/00.png"
    image d4_fox_tail_1 = "sprite/Fox/fox_tail/01.png"
    image d4_fox_tail_2 = "sprite/Fox/fox_tail/02.png"
    image d4_fox_tail_3 = "sprite/Fox/fox_tail/03.png"
    image d4_fox_tail_4 = "sprite/Fox/fox_tail/04.png"
    image d4_fox_tail_5 = "sprite/Fox/fox_tail/05.png"
    image d4_fox_tail_6 = "sprite/Fox/fox_tail/06.png"
    image d4_fox_tail_7 = "sprite/Fox/fox_tail/07.png"

    image d4_fox_tail_animation:
        "d4_fox_tail_0"
        .5
        block:
            "d4_fox_tail_1"
            .08
            "d4_fox_tail_2"
            .08
            "d4_fox_tail_3"
            .08
            "d4_fox_tail_4"
            .08
            "d4_fox_tail_5"
            .08
            "d4_fox_tail_6"
            .08
            "d4_fox_tail_7"
            .08
            "d4_fox_tail_0"
            1.
            repeat 2

    image d4_procession_bg = "locate/home/out_side/Meet_beasts/procession/fon.png"
    image d4_procession_anton = "locate/home/out_side/Meet_beasts/procession/a.png"
    image d4_procession_fox = "locate/home/out_side/Meet_beasts/procession/f.png"
    image d4_procession_bear = "locate/home/out_side/Meet_beasts/procession/m1.png"
    image d4_procession_bear alter = "locate/home/out_side/Meet_beasts/procession/m2.png"
    image d4_procession_olya = "locate/home/out_side/Meet_beasts/procession/o.png"
    image d4_procession_olya_bright:
        "d4_procession_olya"
        matrixcolor BrightnessMatrix(.05)
    image d4_procession_owl = "locate/home/out_side/Meet_beasts/procession/s.png"
    image d4_procession_wolf = "locate/home/out_side/Meet_beasts/procession/v.png"
    image d4_procession_fg = "locate/home/out_side/Meet_beasts/procession/t.png"

    image d4_procession_talkback_bg_1 = "locate/street/road_to_home(N)/road01.png"
    image d4_procession_talkback_bg_2 = "locate/street/road_to_home(N)/road02.png"
    image d4_procession_talkback_bg_3 = "locate/street/road_to_home(N)/road03.png"

    image d4_procession_talkback_bg = LiveComposite((3840, 1080),
        (0, 0), "d4_procession_talkback_bg_1",
        (0, 0), "d4_procession_talkback_bg_2",
        (0, 0), "d4_procession_talkback_bg_3")
    image d4_procession_talkback_bg_crop = Crop((960, 0, 1920, 1080), "d4_procession_talkback_bg")

    image d4_procession_olya_hand:
        "sprite/olya/hand.png"
        subpixel True
        block:
            ease 2.2 xoffset -5 yoffset 0
            ease 2.2 xoffset 0 yoffset -5
            ease 2.2 xoffset 5 yoffset 5
            repeat

    image d4_candy_shower_0 = "locate/home/out_side/Meet_beasts/candy/00.png"
    image d4_candy_shower_1 = "locate/home/out_side/Meet_beasts/candy/01.png"
    image d4_candy_shower_2 = "locate/home/out_side/Meet_beasts/candy/02.png"
    image d4_candy_shower_3 = "locate/home/out_side/Meet_beasts/candy/03.png"
    image d4_candy_shower_4 = "locate/home/out_side/Meet_beasts/candy/04.png"
    image d4_candy_shower_5 = "locate/home/out_side/Meet_beasts/candy/05.png"
    image d4_candy_shower_6 = "locate/home/out_side/Meet_beasts/candy/06.png"
    image d4_candy_shower_7 = "locate/home/out_side/Meet_beasts/candy/07.png"
    image d4_candy_shower_8 = "locate/home/out_side/Meet_beasts/candy/08.png"
    image d4_candy_shower_9 = "locate/home/out_side/Meet_beasts/candy/09.png"
    image d4_candy_shower_10 = "locate/home/out_side/Meet_beasts/candy/10.png"
    image d4_candy_shower_11 = "locate/home/out_side/Meet_beasts/candy/11.png"
    image d4_candy_shower_12 = "locate/home/out_side/Meet_beasts/candy/12.png"
    image d4_candy_shower_13 = "locate/home/out_side/Meet_beasts/candy/13.png"

    define c_dt = 0.09
    image d4_candy_shower_animation:
        "d4_candy_shower_2"
        c_dt
        "d4_candy_shower_3"
        c_dt
        "d4_candy_shower_4"
        c_dt
        "d4_candy_shower_5"
        c_dt
        "d4_candy_shower_6"
        c_dt
        "d4_candy_shower_7"
        c_dt
        "d4_candy_shower_8"
        c_dt
        "d4_candy_shower_9"
        c_dt
        "d4_candy_shower_10"
        c_dt
        "d4_candy_shower_11"
        c_dt
        "d4_candy_shower_12"
        c_dt
        "d4_candy_shower_13"
        c_dt
        "d4_candy_shower_1"
        c_dt*.25
        repeat

    image d4_candy2_bg = "locate/home/out_side/Meet_beasts/candy2/snow.png"

    image d4_zefir_1 = "locate/home/out_side/Meet_beasts/candy2/zef_1.png"
    image d4_zefir_2 = "locate/home/out_side/Meet_beasts/candy2/zef_2.png"
    image d4_zefir_3 = "locate/home/out_side/Meet_beasts/candy2/zef_3.png"
    image d4_zefir_4 = "locate/home/out_side/Meet_beasts/candy2/zef_4.png"
    image d4_zefir_5 = "locate/home/out_side/Meet_beasts/candy2/zef_5.png"

    image d4_zefir_animation:
        contains:
            "d4_zefir_1"
            .1
            "d4_zefir_2"
            .1
            "d4_zefir_3"
            .1
            "d4_zefir_4"
            .1
            "d4_zefir_5"
            .1
        contains:
            alpha 0
            .5
            alpha 1
            align (.5, .5)
            zoom 1.01
            "d4_zefir_bg"
            block:
                linear .03 yoffset 5
                linear .03 yoffset -5
                repeat 5
            linear .03 yoffset 0 zoom 1.00
        contains:
            alpha 0
            .5
            alpha 1
            "d4_zefir_spark_animation"


    image d4_zefir_bg = "locate/home/out_side/Meet_beasts/candy2/snow2.png"
    image d4_zefir_spark_1 = "locate/home/out_side/Meet_beasts/candy2/001.png"
    image d4_zefir_spark_2 = "locate/home/out_side/Meet_beasts/candy2/002.png"
    image d4_zefir_spark_3 = "locate/home/out_side/Meet_beasts/candy2/003.png"
    image d4_zefir_spark_4 = "locate/home/out_side/Meet_beasts/candy2/004.png"

    image d4_zefir_olya = "locate/home/out_side/Meet_beasts/candy2/olya.png"
    image d4_zefir_anton = "locate/home/out_side/Meet_beasts/candy2/anton.png"
    image d4_zefir_bear = "locate/home/out_side/Meet_beasts/candy2/bear.png"
    image d4_zefir_fox = "locate/home/out_side/Meet_beasts/candy2/fox.png"

    define sp_dt = .5
    define spm_dt = 1.
    image d4_zefir_spark_animation:
        "d4_zefir_spark_1" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "d4_zefir_spark_2" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "d4_zefir_spark_3" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "d4_zefir_spark_4" with Dissolve(sp_dt*spm_dt)
        sp_dt
        repeat


init:

    image d4_palace_shadows_0 = "locate/forest/forest_meet/light/shadow0.png"
    image d4_palace_shadows_00 = "locate/forest/forest_meet/light/shadow00.png"
    image d4_palace_shadows_1 = "locate/forest/forest_meet/light/shadow1.png"
    image d4_palace_shadows_2 = "locate/forest/forest_meet/light/shadow2.png"
    image d4_palace_shadows_3 = "locate/forest/forest_meet/light/shadow3.png"
    image d4_palace_shadows:
        "d4_palace_shadows_1" with Dissolve(.1)
        .4
        "d4_palace_shadows_2" with Dissolve(.1)
        .4
        "d4_palace_shadows_3" with Dissolve(.1)
        .4
        repeat

    define hor_dt = 0.2
    image d4_palace_horovod_bg_1 = "locate/forest/forest_meet/horovod/1.png"
    image d4_palace_horovod_bg_2 = "locate/forest/forest_meet/horovod/2.png"
    image d4_palace_horovod_bg_3 = "locate/forest/forest_meet/horovod/3.png"
    image d4_palace_horovod_bg_4 = "locate/forest/forest_meet/horovod/4.png"
    image d4_palace_horovod_bg_5 = "locate/forest/forest_meet/horovod/5.png"
    image d4_palace_horovod_bg_6 = "locate/forest/forest_meet/horovod/6.png"
    image d4_palace_horovod_bg_7 = "locate/forest/forest_meet/horovod/7.png"
    image d4_palace_horovod_bg_8 = "locate/forest/forest_meet/horovod/8.png"
    image d4_palace_horovod_bg:
        "d4_palace_horovod_bg_1"
        hor_dt
        "d4_palace_horovod_bg_2"
        hor_dt
        "d4_palace_horovod_bg_3"
        hor_dt
        "d4_palace_horovod_bg_4"
        hor_dt
        "d4_palace_horovod_bg_5"
        hor_dt
        "d4_palace_horovod_bg_6"
        hor_dt
        "d4_palace_horovod_bg_7"
        hor_dt
        "d4_palace_horovod_bg_8"
        hor_dt
        repeat

    image d4_palace_horovod_fg_1 = "locate/forest/forest_meet/horovod/01.png"
    image d4_palace_horovod_fg_2 = "locate/forest/forest_meet/horovod/02.png"
    image d4_palace_horovod_fg_3 = "locate/forest/forest_meet/horovod/03.png"
    image d4_palace_horovod_fg_4 = "locate/forest/forest_meet/horovod/04.png"
    image d4_palace_horovod_fg_5 = "locate/forest/forest_meet/horovod/05.png"
    image d4_palace_horovod_fg_6 = "locate/forest/forest_meet/horovod/06.png"
    image d4_palace_horovod_fg_7 = "locate/forest/forest_meet/horovod/07.png"
    image d4_palace_horovod_fg_8 = "locate/forest/forest_meet/horovod/08.png"
    image d4_palace_horovod_fg:
        "d4_palace_horovod_fg_1"
        hor_dt
        "d4_palace_horovod_fg_2"
        hor_dt
        "d4_palace_horovod_fg_3"
        hor_dt
        "d4_palace_horovod_fg_4"
        hor_dt
        "d4_palace_horovod_fg_5"
        hor_dt
        "d4_palace_horovod_fg_6"
        hor_dt
        "d4_palace_horovod_fg_7"
        hor_dt
        "d4_palace_horovod_fg_8"
        hor_dt
        repeat

    image d4_palace_beasts_bg = "locate/forest/forest_meet/beasts1/fon.png"
    image d4_palace_beasts_faces = "locate/forest/forest_meet/beasts1/beasts.png"
    image d4_palace_beasts_faces_dark = "locate/forest/forest_meet/beasts1/beasts2.png"
    image d4_palace_beasts_saliva_1 = "locate/forest/forest_meet/beasts1/01.png"
    image d4_palace_beasts_saliva_2 = "locate/forest/forest_meet/beasts1/02.png"
    image d4_palace_beasts_saliva_3 = "locate/forest/forest_meet/beasts1/03.png"
    image d4_palace_beasts_saliva_4 = "locate/forest/forest_meet/beasts1/04.png"
    image d4_palace_beasts_saliva_5 = "locate/forest/forest_meet/beasts1/05.png"
    image d4_palace_beasts_saliva_6 = "locate/forest/forest_meet/beasts1/06.png"
    image d4_palace_beasts_saliva_7 = "locate/forest/forest_meet/beasts1/07.png"
    image d4_palace_beasts_saliva_8 = "locate/forest/forest_meet/beasts1/08.png"
    image d4_palace_beasts_saliva_9 = "locate/forest/forest_meet/beasts1/09.png"
    image d4_palace_beasts_saliva_10 = "locate/forest/forest_meet/beasts1/010.png"

    image d4_palace_candy_bg = "locate/forest/forest_meet/choice/candy_fon.png"
    image d4_palace_candy 1 = "locate/forest/forest_meet/choice/candy_1.png"
    image d4_palace_candy 2 = "locate/forest/forest_meet/choice/candy_2.png"

    image d4_palace_candy_full 1 = "locate/forest/forest_meet/choice/candy/candy_1.png"
    image d4_palace_candy_full 2 = "locate/forest/forest_meet/choice/candy/candy_2.png"
    image d4_palace_candy_full 3 = "locate/forest/forest_meet/choice/candy/candy_3.png"
    image d4_palace_candy_full 4 = "locate/forest/forest_meet/choice/candy/candy_4.png"
    image d4_palace_candy_full 5 = "locate/forest/forest_meet/choice/candy/candy_5.png"
    image d4_palace_candy_full 6 = "locate/forest/forest_meet/choice/candy/candy_6.png"
    image d4_palace_candy_full 7 = "locate/forest/forest_meet/choice/candy/candy_7.png"
    image d4_palace_candy_full 8 = "locate/forest/forest_meet/choice/candy/candy_8.png"

    image d4_palace_candy_full anim:
        "d4_palace_candy_full 1"
        .1
        "d4_palace_candy_full 2"
        .1
        "d4_palace_candy_full 3"
        .1
        "d4_palace_candy_full 4"
        .1
        "d4_palace_candy_full 5"
        .1
        "d4_palace_candy_full 6"
        .1
        "d4_palace_candy_full 7"
        .1
        "d4_palace_candy_full 8"


    image d4_palace_glitter_1 = "locate/forest/forest_meet/choice/star_01.png"
    image d4_palace_glitter_2 = "locate/forest/forest_meet/choice/star_02.png"
    image d4_palace_glitter_3 = "locate/forest/forest_meet/choice/star_03.png"
    image d4_palace_glitter:
        "d4_palace_glitter_1" with Dissolve(.3)
        .3
        "d4_palace_glitter_2" with Dissolve(.3)
        .3
        "d4_palace_glitter_3" with Dissolve(.3)
        .3
        repeat

    define sal_dt = 0.1
    image d4_palace_beasts_saliva:
        "d4_palace_beasts_saliva_1"
        sal_dt
        "d4_palace_beasts_saliva_2"
        sal_dt
        "d4_palace_beasts_saliva_3"
        sal_dt
        "d4_palace_beasts_saliva_4"
        sal_dt
        "d4_palace_beasts_saliva_5"
        sal_dt
        "d4_palace_beasts_saliva_6"
        sal_dt
        "d4_palace_beasts_saliva_7"
        sal_dt
        "d4_palace_beasts_saliva_8"
        sal_dt
        "d4_palace_beasts_saliva_9"
        sal_dt
        "d4_palace_beasts_saliva_10"
        sal_dt
        repeat

    image d4_palace_beasts:
        contains:
            "d4_palace_beasts_faces"
        contains:
            "d4_palace_beasts_saliva"

    image d4_palace_choice_bg = "locate/forest/forest_meet/choice/fon.png"
    image d4_palace_choice_beasts 1 = "locate/forest/forest_meet/choice/beasts.png"
    image d4_palace_choice_beasts 2 = "locate/forest/forest_meet/choice/beasts2.png"
    image d4_palace_choice_beasts 3 = "locate/forest/forest_meet/choice/beasts3.png"
    image d4_palace_choice_olya 1 = "locate/forest/forest_meet/choice/01.png"
    image d4_palace_choice_olya 2 = "locate/forest/forest_meet/choice/02.png"
    image d4_palace_choice_olya 3 = "locate/forest/forest_meet/choice/03.png"
    image d4_palace_choice_candy = "locate/forest/forest_meet/choice/candy.png"
    image d4_palace_choice_bg2 = "locate/forest/forest_meet/choice/fon2.png"
    image d4_palace_choice_head = "locate/forest/forest_meet/choice/head.png"
    image d4_palace_choice_head_ 1 = "locate/forest/forest_meet/choice/head2.png"
    image d4_palace_choice_head_ 2 = "locate/forest/forest_meet/choice/head3.png"
    image d4_palace_choice_head_ 3 = "locate/forest/forest_meet/choice/head4.png"
    image d4_palace_choice_moroz = "locate/forest/forest_meet/choice/moroz5.png"

    image d4_anton_treat_choice:
        "d4_anton_back"
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -450
        zoom 1.15
        yoffset 150

    image d4_treat_choice2_bg color = "locate/forest/forest_meet/choice2/fon_ice_color.png"
    image d4_treat_choice2_alice_body color = "locate/forest/forest_meet/choice2/body_fox_color.png"
    image d4_treat_choice2_alice_hands color = "locate/forest/forest_meet/choice2/hand_fox_color.png"

    image d4_treat_choice2_bg nocolor = "locate/forest/forest_meet/choice2/fon_ice.png"
    image d4_treat_choice2_alice_body nocolor = "locate/forest/forest_meet/choice2/body_fox.png"
    image d4_treat_choice2_alice_hands nocolor = "locate/forest/forest_meet/choice2/hand_fox.png"

    image d4_treat_choice2_refuse_1 = "locate/forest/forest_meet/choice2/transition/choice01.png"
    image d4_treat_choice2_refuse_2 = "locate/forest/forest_meet/choice2/transition/choice02.png"
    image d4_treat_choice2_refuse_3 = "locate/forest/forest_meet/choice2/transition/choice03.png"
    image d4_treat_choice2_refuse_4 = "locate/forest/forest_meet/choice2/transition/choice04.png"
    image d4_treat_choice2_refuse_5 = "locate/forest/forest_meet/choice2/transition/choice05.png"
    image d4_treat_choice2_refuse_6 = "locate/forest/forest_meet/choice2/transition/choice06.png"
    image d4_treat_choice2_refuse_7 = "locate/forest/forest_meet/choice2/transition/choice07.png"
    image d4_treat_choice2_refuse_8 = "locate/forest/forest_meet/choice2/transition/choice08.png"

    define ref_dt = 0.1
    image d4_treat_choice2_refuse_full:
        "d4_treat_choice2_refuse_1"
        ref_dt
        "d4_treat_choice2_refuse_2"
        ref_dt
        "d4_treat_choice2_refuse_3"
        ref_dt
        "d4_treat_choice2_refuse_4"
        ref_dt
        "d4_treat_choice2_refuse_5"
        ref_dt
        "d4_treat_choice2_refuse_6"
        ref_dt
        "d4_treat_choice2_refuse_7"
        ref_dt
        "d4_treat_choice2_refuse_8"
        ref_dt
        Null()

    image d4_treat_choice2_refuse_blink:
        "d4_treat_choice2_refuse_7"
        ref_dt
        "d4_treat_choice2_refuse_6"
        ref_dt
        "d4_treat_choice2_refuse_7"
        ref_dt
        Null()

    image d4_treat_choice2_refuse_short:
        choice:
            "d4_treat_choice2_refuse_blink"
        choice:
            "d4_treat_choice2_refuse_blink"
            ref_dt*4
            "d4_treat_choice2_refuse_blink"
        3.0
        repeat

    $ hs_prm = (5, 2)
    transform handshake(dt=1.0, mod=1.0, xz=1.0, yz=1.0):
        subpixel True
        ease dt xoffset -5*mod*xz yoffset 0
        ease dt xoffset 5*mod*xz yoffset -5*mod*yz
        ease dt xoffset 0 yoffset 5*mod*yz
        ease dt xoffset 5*mod*xz yoffset 0
        repeat

    image d4_treat_ceiling_bg = "locate/forest/forest_meet/light/ceiling.png"
    image d4_treat_ceiling_ded = "locate/forest/forest_meet/light/ceiling_ded.png"
    image d4_treat_ded_close = "locate/forest/forest_meet/light/deda.png"

    image d4_lisa 1 = "locate/school/in_side/Polina_Lisa/Polina_02.png"
    image d4_lisa 2 = "locate/school/in_side/Polina_Lisa/Polina_03.png"
    image d4_lisa 3 = "locate/school/in_side/Polina_Lisa/Lisa_03.png"
    image d4_lisa 4 = "locate/school/in_side/Polina_Lisa/Lisa_02.png"
    image d4_lisa 5 = "locate/school/in_side/Polina_Lisa/Lisa_01.png"

    image d4_flute_olya = "locate/forest/forest_meet/choice/olya.png"
    image d4_flute_anton = "locate/forest/forest_meet/choice/anton.png"

    image d4_palace_ant_ol = "locate/forest/forest_meet/choice/ant_ol.png"

    image d4_palace_worms = "locate/forest/forest_meet/choice2/worms.png"

    image d4_palace_dark_bg_1 = "locate/forest/forest_meet/dark/garage_dark.png"
    image d4_palace_dark_bg_2 = "locate/forest/forest_meet/dark/garage_dark02.png"
    image d4_palace_dark_bg_3 = "locate/forest/forest_meet/dark/garage_dark03.png"
    image d4_palace_dark_bg_4 = "locate/forest/forest_meet/dark/garage_dark04.png"

    image d4_palace_dark_state_1:
        function garage_light_on
        "d4_palace_dark_bg_1"
    image d4_palace_dark_state_2:
        function garage_light_off
        "d4_palace_dark_bg_2"
    image d4_palace_dark_state_3:
        function garage_light_on
        contains:
            "d4_palace_dark_bg_1"
        contains:
            "d4_palace_dark_bg_3"
    image d4_palace_dark_state_4:
        function garage_light_on
        contains:
            "d4_palace_dark_bg_1"
        contains:
            "d4_palace_dark_bg_4"
    image d4_palace_dark_state_5:
        function garage_light_off
        contains:
            "d4_palace_dark_bg_2"
        contains:
            "d4_palace_dark_bg_3"

    transform blink_pattern_1(state2):
        function play_lamp_blink_4
        state2
        1.0
        function play_lamp_blink_2
        "d4_palace_dark_state_1"
        0.1
        state2
        0.1
        "d4_palace_dark_state_1"
    transform blink_pattern_2(state2):
        function play_lamp_blink_3
        "d4_palace_dark_state_2"
        0.1
        "d4_palace_dark_state_1"
        0.1
        "d4_palace_dark_state_2"
        1.0
        function play_lamp_blink_4
        state2
        1.0
        function play_lamp_blink_5
        "d4_palace_dark_state_1"
    transform blink_pattern_3(state2):
        function play_lamp_blink_1
        state2
        0.1
        "d4_palace_dark_state_1"
        0.1
        state2
        0.1
        "d4_palace_dark_state_1"
    transform blink_pattern_4(state2):
        function play_lamp_blink_1
        "d4_palace_dark_state_2"
        0.1
        "d4_palace_dark_state_1"
        0.1
        "d4_palace_dark_state_2"
        0.1
        state2
        1.0
        function play_lamp_blink_4
        "d4_palace_dark_state_1"

    python:
        def garage_light_on(trans, st, at):
            global d4_palace_garage_light_on
            d4_palace_garage_light_on = True
            renpy.restart_interaction()

        def garage_light_off(trans, st, at):
            global d4_palace_garage_light_on
            d4_palace_garage_light_on = False
            renpy.restart_interaction()

    image d4_palace_dark_loop_1_1:
        contains blink_pattern_1("d4_palace_dark_state_3")
    image d4_palace_dark_loop_1_2:
        contains blink_pattern_1("d4_palace_dark_state_4")
    image d4_palace_dark_loop_1_3:
        contains blink_pattern_1("d4_palace_dark_state_5")

    image d4_palace_dark_loop_2_1:
        contains blink_pattern_2("d4_palace_dark_state_3")
    image d4_palace_dark_loop_2_2:
        contains blink_pattern_2("d4_palace_dark_state_4")
    image d4_palace_dark_loop_2_3:
        contains blink_pattern_2("d4_palace_dark_state_5")

    image d4_palace_dark_loop_3_1:
        contains blink_pattern_3("d4_palace_dark_state_3")
    image d4_palace_dark_loop_3_2:
        contains blink_pattern_3("d4_palace_dark_state_4")
    image d4_palace_dark_loop_3_3:
        contains blink_pattern_3("d4_palace_dark_state_5")

    image d4_palace_dark_loop_4_1:
        contains blink_pattern_4("d4_palace_dark_state_3")
    image d4_palace_dark_loop_4_2:
        contains blink_pattern_4("d4_palace_dark_state_4")
    image d4_palace_dark_loop_4_3:
        contains blink_pattern_4("d4_palace_dark_state_5")

    image d4_palace_dark_blink:
        "d4_palace_dark_state_1"
        block:
            6.
            block:
                choice:
                    "d4_palace_dark_loop_2_1"
                    1.0
                choice:
                    "d4_palace_dark_loop_2_2"
                    1.0
                choice:
                    "d4_palace_dark_loop_2_3"
                    1.0

            repeat

    image cpx_d4_palace_showoff:
        contains:
            "d4_palace_dark_blink"
        contains:
            "d4_small_wolf"
            align (.5, 1.)
            xpos .68
        contains:
            "d4_small_owl"
            align (.5, 1.)
            xpos .82
        contains:
            "d4_small_bear"
            align (.5, 1.)
            xpos .17
        contains:
            "d4_small_fox"
            align (.5, 1.)
            xpos .32
            yoffset -75

    image d4_palace_garage_1 = "locate/forest/forest_meet/001.png"
    image d4_palace_garage_2 = "locate/forest/forest_meet/002.png"
    image d4_palace_garage_3 = "locate/forest/forest_meet/003.png"
    image d4_palace_garage_4 = "locate/forest/forest_meet/004.png"
    image d4_palace_garage_5 = "locate/forest/forest_meet/005.png"
    image d4_palace_garage_6 = "locate/forest/forest_meet/006.png"
    image d4_palace_garage_7 = "locate/forest/forest_meet/007.png"
    image d4_palace_garage_8 = "locate/forest/forest_meet/008.png"
    image d4_palace_garage_9 = "locate/forest/forest_meet/009.png"
    image d4_palace_garage_10 = "locate/forest/forest_meet/010.png"
    image d4_palace_garage_11 = "locate/forest/forest_meet/011.png"
    image d4_palace_garage_12 = "locate/forest/forest_meet/012.png"
    image d4_palace_garage_g1 = "locate/forest/forest_meet/G01.png"
    image d4_palace_garage_g2 = "locate/forest/forest_meet/G02.png"

    image d4_palace_garage_break:
        parallel:
            "d4_palace_garage_1"
            0.03 * 40
            "d4_palace_garage_2"
            .1
            "d4_palace_garage_3"
            .1
            "d4_palace_garage_4"
            .1
            "d4_palace_garage_5"
            .1
            "d4_palace_garage_6"
            .1
            "d4_palace_garage_7"
            .1
            "d4_palace_garage_8"
            .1
            "d4_palace_garage_9"
            .1
            "d4_palace_garage_10"
            .1
            "d4_palace_garage_11"
        parallel:
            block:
                linear .03 yoffset 4
                linear .03 yoffset -4
                repeat 10*3
                linear .03 yoffset 0

    image d4_palace_garage_blink:
        function play_lamp_blink_1
        "d4_palace_garage_12"
        .1
        "d4_palace_garage_11"
        .1
        "d4_palace_garage_12"
        .1
        "d4_palace_garage_11"
        .5
        "d4_palace_garage_12"

    image d4_pal_fox_transit_beast_bg = "locate/forest/forest_meet/beasts1/fox_fon.png"

    image d4_pal_fox_transit_beast_1 = "locate/forest/forest_meet/beasts1/fox01.png"
    image d4_pal_fox_transit_beast_2 = "locate/forest/forest_meet/beasts1/fox02.png"
    image d4_pal_fox_transit_beast_3 = "locate/forest/forest_meet/beasts1/fox03.png"
    image d4_pal_fox_transit_beast_4 = "locate/forest/forest_meet/beasts1/fox04-06.png"
    image d4_pal_fox_transit_beast_5 = "locate/forest/forest_meet/beasts1/fox05.png"
    image d4_pal_fox_transit_beast_6 = "locate/forest/forest_meet/beasts1/fox04-06.png"
    image d4_pal_fox_transit_beast_7 = "locate/forest/forest_meet/beasts1/fox07.png"
    image d4_pal_fox_transit_beast_8 = "locate/forest/forest_meet/beasts1/fox08.png"
    image d4_pal_fox_transit_beast_9 = "locate/forest/forest_meet/beasts1/fox09-011.png"
    image d4_pal_fox_transit_beast_10 = "locate/forest/forest_meet/beasts1/fox010-012.png"
    image d4_pal_fox_transit_beast_11 = "locate/forest/forest_meet/beasts1/fox09-011.png"
    image d4_pal_fox_transit_beast_12 = "locate/forest/forest_meet/beasts1/fox010-012.png"
    image d4_pal_fox_transit_beast_13 = "locate/forest/forest_meet/beasts1/fox013.png"
    image d4_pal_fox_transit_beast_14 = "locate/forest/forest_meet/beasts1/fox014.png"
    image d4_pal_fox_transit_beast_15 = "locate/forest/forest_meet/beasts1/fox015.png"

    image d4_garage_smoke = "locate/street/garage/smoke.png"

    image d4_pal_fox_transit_beast:
        "d4_pal_fox_transit_beast_1" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_2" with Dissolve(.3)
        .3
        "d4_pal_fox_transit_beast_3" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_4" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_5" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_6" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_7" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_8" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_9" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_10" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_11" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_12" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_13" with Dissolve(.1)
        .3
        "d4_pal_fox_transit_beast_15" with Dissolve(.1)

    image d4_big_master = "locate/forest/forest_meet/beasts1/big_master.png"

    default d4_palace_garage_light_on = True
    image d4_small_master = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/kozel2.png",
        "True", "locate/forest/forest_meet/dark/kozel.png")
    image d4_small_master_flute = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/kozel4.png",
        "True", "locate/forest/forest_meet/dark/kozel3.png")
    image d4_small_fox = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/foxy2.png",
        "True", "locate/forest/forest_meet/dark/foxy1.png")
    image d4_small_owl = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/Owl_01.png",
        "True", "locate/forest/forest_meet/dark/Owl_02.png")
    image d4_small_wolf = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/wolf02.png",
        "True", "locate/forest/forest_meet/dark/wolf01.png")
    image d4_small_bear = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/Bear2.png",
        "True", "locate/forest/forest_meet/dark/Bear.png")

    image d4_dark_fonback = "locate/forest/forest_meet/dark/garadge_fon.png"

    image d4_dark_floor = "locate/forest/forest_meet/dark/flooring.png"
    image d4_dark_meat = "locate/forest/forest_meet/dark/meat.png"
    image d4_dark_meat2 = "locate/forest/forest_meet/dark/meat2.png"
    image d4_dark_meat3 = "locate/forest/forest_meet/dark/meat3.png"

    image d4_icicle_1 = "locate/forest/forest_meet/light/ice1.png"
    image d4_icicle_2 = "locate/forest/forest_meet/light/ice2.png"
    image d4_icicle_3 = "locate/forest/forest_meet/light/ice3.png"

    image d4_icicle_1_dark = LiveComposite((796, 1424),
        (0, 0), "d4_icicle_1", 
        (0, 0), AlphaMask(Solid("#00000040"), "d4_icicle_1"))
    image d4_icicle_2_dark = LiveComposite((796, 1190),
        (0, 0), "d4_icicle_2", 
        (0, 0), AlphaMask(Solid("#00000040"), "d4_icicle_2"))
    image d4_icicle_3_dark = LiveComposite((635, 1190),
        (0, 0), "d4_icicle_3", 
        (0, 0), AlphaMask(Solid("#00000040"), "d4_icicle_3"))

    image d4_palace_monster_owl_bg = "locate/forest/forest_meet/beasts1/owl_fon.png"

    image d4_palace_monster_owl_0 = "locate/forest/forest_meet/beasts1/Owl0.png"
    image d4_palace_monster_owl_1 = "locate/forest/forest_meet/beasts1/Owl1.png"
    image d4_palace_monster_owl_2 = "locate/forest/forest_meet/beasts1/Owl2.png"
    image d4_palace_monster_owl_0_dark = "locate/forest/forest_meet/beasts1/Owl0_dark.png"
    image d4_palace_monster_owl_2_dark = "locate/forest/forest_meet/beasts1/Owl2_dark.png"

    image d4_palace_monster_owl_big idle = ConditionSwitch(
        "not d4_palace_garage_light_on", "d4_palace_monster_owl_0_dark",
        "True", "d4_palace_monster_owl_0")
    image d4_palace_monster_owl_big scream = ConditionSwitch(
        "not d4_palace_garage_light_on", "d4_palace_monster_owl_2_dark",
        "True", "d4_palace_monster_owl_2")

    image d4_palace_monster_owl:
        "d4_palace_monster_owl_0"
        .2
        "d4_palace_monster_owl_1"
        .2
        repeat

    image d4_palace_monster_wolf_1 = "locate/forest/forest_meet/beasts1/woolf1.png"
    image d4_palace_monster_wolf_2 = "locate/forest/forest_meet/beasts1/woolf2.png"
    image d4_palace_monster_wolf_3 = "locate/forest/forest_meet/beasts1/woolf3.png"

    image d4_palace_monster_wolf:
        "d4_palace_monster_wolf_1"
        .2
        "d4_palace_monster_wolf_2"
        .2
        repeat

    image d4_palace_monster_bear_1 = "locate/forest/forest_meet/beasts1/big-bear_1.png"
    image d4_palace_monster_bear_2 = "locate/forest/forest_meet/beasts1/big-bear_2.png"
    image d4_palace_monster_bear_3 = "locate/forest/forest_meet/beasts1/big-bear_3.png"

    image d4_palace_monster_bear:
        "d4_palace_monster_bear_1"
        .2
        "d4_palace_monster_bear_2"
        .2
        repeat

    image d4_palace_monster_fox_1 = "locate/forest/forest_meet/beasts1/foxes001.png"
    image d4_palace_monster_fox_2 = "locate/forest/forest_meet/beasts1/foxes002.png"
    image d4_palace_monster_fox_3 = "locate/forest/forest_meet/beasts1/foxes003.png"

    image d4_palace_monster_fox:
        "d4_palace_monster_fox_1"
        .2
        "d4_palace_monster_fox_2"
        .2
        repeat

    image d4_whiplash = "locate/forest/forest_meet/beasts1/Whiplash.png"

    image d4_big_master_flute = "locate/forest/forest_meet/beasts1/master_flute.png"


init:
    image d4_darkgar_bear_mid_1 = "locate/forest/forest_meet/beasts1/Bear_mid.png"
    image d4_darkgar_bear_mid_2 = "locate/forest/forest_meet/beasts1/Bear_mid2.png"
    image d4_darkgar_bear_mid_3 = "locate/forest/forest_meet/beasts1/Bear_mid3.png"
    image d4_darkgar_bear_mid = ConditionSwitch(
        "not d4_palace_garage_light_on", "d4_darkgar_bear_mid_3",
        "True", "d4_darkgar_bear_mid_1")
    image d4_darkgar_wolf_mid_1 = "locate/forest/forest_meet/beasts1/woolf_mid1.png"
    image d4_darkgar_wolf_mid_2 = "locate/forest/forest_meet/beasts1/woolf_mid2.png"
    image d4_darkgar_wolf_mid_3 = "locate/forest/forest_meet/beasts1/woolf_mid3.png"
    image d4_darkgar_wolf_mid = ConditionSwitch(
        "not d4_palace_garage_light_on", "d4_darkgar_wolf_mid_3",
        "True", "d4_darkgar_wolf_mid_1")

    image d4_darkgar_alice_hug_1 = "locate/forest/forest_meet/dark/Alice_obnim.png"
    image d4_darkgar_alice_hug_2 = "locate/forest/forest_meet/dark/Alice_obnim2.png"
    image d4_darkgar_empty_garage_bg = "locate/forest/forest_meet/dark/garadge_fon.png"

    image d4_darkgar_empty_garage_bg_blink:
        function garage_light_on
        Null()

        choice:
            4.
        choice:
            5.5

        function play_lamp_blink_4
        function garage_light_off
        "black_3_4"
        .1
        repeat

    image d4_darkgar_alice_beast_1 = "locate/forest/forest_meet/beasts1/foxes001.png"
    image d4_darkgar_alice_beast_2 = "locate/forest/forest_meet/beasts1/foxes002.png"
    image d4_darkgar_alice_beast_3 = "locate/forest/forest_meet/beasts1/foxes003.png"
    image d4_darkgar_alice_beast_base = ConditionSwitch(
        "not d4_palace_garage_light_on", "d4_darkgar_alice_beast_3",
        "True", "d4_darkgar_alice_beast_1")
    image d4_darkgar_alice_beast:
        "d4_darkgar_alice_beast_base"
        choice:
            1.5
        choice:
            2.5
        choice:
            3.5
        "d4_darkgar_alice_beast_2"
        .1
        repeat

    image d4_darkgar_olya_out_1 = "locate/forest/forest_meet/dark/olya.png"
    image d4_darkgar_olya_out_2 = "locate/forest/forest_meet/dark/olya2.png"
    image d4_darkgar_olya_out_3 = "locate/forest/forest_meet/dark/olya3.png"

    image d4_darkgar_prava_1 = "locate/forest/forest_meet/dark/tuts/01.png"
    image d4_darkgar_prava_2 = "locate/forest/forest_meet/dark/tuts/02.png"
    image d4_darkgar_prava_3 = "locate/forest/forest_meet/dark/tuts/03.png"
    image d4_darkgar_prava_4 = "locate/forest/forest_meet/dark/tuts/04.png"
    image d4_darkgar_prava_5 = "locate/forest/forest_meet/dark/tuts/05.png"
    image d4_darkgar_prava_6 = "locate/forest/forest_meet/dark/tuts/06.png"
    image d4_darkgar_prava_7 = "locate/forest/forest_meet/dark/tuts/07.png"
    image d4_darkgar_prava_8 = "locate/forest/forest_meet/dark/tuts/08.png"
    image d4_darkgar_prava_9 = "locate/forest/forest_meet/dark/tuts/09.png"
    image d4_darkgar_prava_10 = "locate/forest/forest_meet/dark/tuts/010.png"
    image d4_darkgar_prava_11 = "locate/forest/forest_meet/dark/tuts/011.png"
    image d4_darkgar_prava_12 = "locate/forest/forest_meet/dark/tuts/012.png"
    image d4_darkgar_prava_13 = "locate/forest/forest_meet/dark/tuts/013.png"

    define dprava_dt = .1
    image d4_darkgar_prava:
        "d4_darkgar_prava_1"
        .25
        "d4_darkgar_prava_2" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_3" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_4" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_5" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_6" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_7" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_8" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_9" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_10" with Dissolve(dprava_dt)
        dprava_dt
        "d4_darkgar_prava_11" with Dissolve(dprava_dt)
        dprava_dt
        block:
            "d4_darkgar_prava_12" with Dissolve(dprava_dt)
            dprava_dt
            "d4_darkgar_prava_13" with Dissolve(dprava_dt)
            dprava_dt
            repeat

    image d4_domination_bg = "locate/forest/forest_meet/dark/floor.png"
    image d4_domination_anton = "locate/forest/forest_meet/dark/Anton_above.png"
    image d4_domination_master = "locate/forest/forest_meet/dark/master.png"
    image d4_domination_fox beast = "locate/forest/forest_meet/dark/foxsu1.png"
    image d4_domination_fox cute = "locate/forest/forest_meet/dark/foxsu3.png"
    image d4_domination_fox turned = "d4_procession_fox"

    image d4_domination_fox bright = "locate/school/in_side/Polina_Lisa/Aliska.png"
    image d4_domination_fox_bg = "locate/school/in_side/Polina_Lisa/Aliska_fon.png"

    image d4_protect_bg = "locate/forest/forest_meet/dark/garage_fon.png"
    image d4_protect_fox = "locate/forest/forest_meet/dark/foxx.png"
    image d4_protect_antfox = "locate/forest/forest_meet/beasts1/foxx2.png"

    image d4_darkgar_owl_master = ConditionSwitch(
        "not d4_palace_garage_light_on", "locate/forest/forest_meet/dark/mast2.png",
        "True", "locate/forest/forest_meet/dark/mast.png")

    image d4_antonmad_1 = "locate/forest/forest_meet/dark/Mad_Anton_1.png"
    image d4_antonmad_2 = "locate/forest/forest_meet/dark/Mad_Anton_2.png"
    image d4_antonmad_3 = "locate/forest/forest_meet/dark/Mad_Anton_3.png"
    image d4_antonmad_4 = "locate/forest/forest_meet/dark/Mad_Anton_4.png"
    image d4_antonmad_5 = "locate/forest/forest_meet/dark/Mad_Anton_5.png"

    define da_dt = .1
    image d4_antonmad:
        block:
            "d4_antonmad_1"
            da_dt
            "d4_antonmad_2"
            da_dt
            "d4_antonmad_3"
            da_dt
            "d4_antonmad_4"
            da_dt
            repeat 10
        "d4_antonmad_5"
        da_dt
        "d4_antonmad_2"
        da_dt
        "d4_antonmad_3"
        da_dt
        "d4_antonmad_4"
        da_dt
        repeat

    image d4_episode_end_olya_base = "locate/forest/forest_meet/olya01.png"
    image d4_episode_end_olya_overlay2 = "locate/forest/forest_meet/olya02.png"
    image d4_episode_end_olya_overlay3 = "locate/forest/forest_meet/olya03.png"
    image d4_episode_end_olya_overlay4 = "locate/forest/forest_meet/olya04.png"
    image d4_episode_end_olya_overlay5 = "locate/forest/forest_meet/olya05.png"
    image d4_episode_end_olya_overlay6 = "locate/forest/forest_meet/olya06.png"
    image d4_episode_end_olya_overlay7 = "locate/forest/forest_meet/olya07.png"
    image d4_episode_end_olya_overlay8 = "locate/forest/forest_meet/olya08.png"

    image d4_episode_end_olya_death_nokidding_trustme_she_died = "locate/forest/forest_meet/Olyadeath.png"
    image d4_episode_end_olya_death_nokidding_trustme_she_died_0 = "locate/forest/forest_meet/Olyadeath0.png"
    image d4_episode_end_olya_death_nokidding_trustme_she_died_1 = "locate/forest/forest_meet/Olyadeath1.png"
    image d4_episode_end_olya_death_nokidding_trustme_she_died_2 = "locate/forest/forest_meet/Olyadeath2.png"


init:
    image d4_palace_bg = "locate/forest/forest_meet/light/fon.png"
    image d4_palace_base = "locate/forest/forest_meet/light/castle_base.png"
    image d4_palace_light_1 = "locate/forest/forest_meet/light/Light01.png"
    image d4_palace_light_2 = "locate/forest/forest_meet/light/Light02.png"
    image d4_palace_light_blink:
        block:
            "empty" with Dissolve(.2)
            .2
            "d4_palace_light_1" with Dissolve(.2)
            .2

            repeat 8

        "d4_palace_light_2" with Dissolve(.2)
        .2
        "d4_palace_light_1" with Dissolve(.2)
        .2

        repeat

    image d4_palace_flags_1 = "locate/forest/forest_meet/light/f01.png"
    image d4_palace_flags_2 = "locate/forest/forest_meet/light/f02.png"
    image d4_palace_flags_3 = "locate/forest/forest_meet/light/f03.png"
    image d4_palace_flags_4 = "locate/forest/forest_meet/light/f04.png"
    image d4_palace_flags_5 = "locate/forest/forest_meet/light/f05.png"
    image d4_palace_flags_6 = "locate/forest/forest_meet/light/f06.png"
    image d4_palace_flags:
        "d4_palace_flags_1"
        .1
        "d4_palace_flags_2"
        .1
        "d4_palace_flags_3"
        .1
        "d4_palace_flags_4"
        .1
        "d4_palace_flags_5"
        .1
        "d4_palace_flags_6"
        .1
        repeat



    image d4_palace_mid = LiveComposite((2670, 1502),
        (0, 0), "d4_palace_base",
        (0, 0), "d4_palace_light_blink",
        (0, 0), "d4_palace_flags")


    define pal_fg_width = 3000
    image d4_palace_fg = LiveComposite((pal_fg_width, 1600),
        (0, 0), "d4_gorelnik_fg_1",
        (pal_fg_width - 1300, 0), "d4_gorelnik_fg_2")

    image d4_palace_fox = "locate/forest/forest_meet/light/Fox.png"
    image d4_palace_moroz 1 = "locate/forest/forest_meet/light/moroz.png"
    image d4_palace_moroz 2 = "locate/forest/forest_meet/light/moroz2.png"
    image d4_palace_moroz 3 = "locate/forest/forest_meet/light/moroz3.png"
    image d4_palace_moroz 4 = "locate/forest/forest_meet/light/moroz4.png"

    image d4_palace_ded_moroz = "locate/forest/forest_meet/light/castle_big.png"
    image d4_palace_children = "locate/forest/forest_meet/light/castle_big2.png"
    image d4_palace_room = "locate/forest/forest_meet/light/castle.png"



    image d4_palace_stars:
        "locate/home/out_side/Meet_beasts/wood/1.png" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "locate/home/out_side/Meet_beasts/wood/3.png" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "locate/home/out_side/Meet_beasts/wood/2.png" with Dissolve(sp_dt*spm_dt)
        sp_dt
        "locate/home/out_side/Meet_beasts/wood/4.png" with Dissolve(sp_dt*spm_dt)
        sp_dt
        repeat

    image d4_agree_bg = "locate/forest/forest_meet/color/color_fon2.png"
    image d4_agree_candyhand 1 = "locate/forest/forest_meet/color/candyhand.png"
    image d4_agree_candyhand 2 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/forest_meet/color/candyhand.png",
        (0, 0), "locate/forest/forest_meet/color/candyhand2.png")

    image d4_night_forest_moon1 = LiveComposite((1920, 2531),
        (0, 0), "locate/home/out_side/Meet_beasts/wood/pole4.png",
        (0, 0), "day3_forest_scene2_stars")

    image d4_night_forest_moon2 = LiveComposite((1920, 1524),
        (0, 0), "locate/home/out_side/Meet_beasts/wood/fon.jpg",
        (0, 0), "day3_forest_scene2_stars")

    image d4_wolf_candy 1 = "locate/forest/forest_meet/barf/01.png"
    image d4_wolf_candy 2 = "locate/forest/forest_meet/barf/02.png"
    image d4_wolf_candy 3 = "locate/forest/forest_meet/barf/03.png"
    image d4_wolf_candy 4 = "locate/forest/forest_meet/barf/04.png"
    image d4_wolf_candy 5 = "locate/forest/forest_meet/barf/05.png"
    image d4_wolf_candy 6 = "locate/forest/forest_meet/barf/06.png"
    image d4_wolf_candy 7 = "locate/forest/forest_meet/barf/07.png"
    image d4_wolf_candy 8 = "locate/forest/forest_meet/barf/08.png"

    image d4_wolf_candy anim:
        parallel:
            block:
                "d4_wolf_candy 1"
                .1
                "d4_wolf_candy 2"
                .1
                repeat 3
            "d4_wolf_candy 3"
            .1
            "d4_wolf_candy 4"
            .1
            "d4_wolf_candy 5"
            .1
            "d4_wolf_candy 6"
            .1
            "d4_wolf_candy 7"
            .1
            "d4_wolf_candy 8"
            .1
            "Wolf Normal m 00"
        parallel:
            .5
            easeout .1 yoffset 40
            .5
            ease .5 yoffset 0

    image bg_house_night = "locate/home/out_side/house_night05.jpg"
    image road_day = "locate/street/road_day.png"
    image snowball_corner_Polina:
        contains:
            "road_day"
            xalign .5
            yalign .5
            zoom 1.10
        contains:
            "locate/forest/fox_snowball/Snowboll_01.png"
            pause 0.1
            "locate/forest/fox_snowball/Snowboll_02.png"
            pause 0.1
            "locate/forest/fox_snowball/Snowboll_03.png"
            pause 0.1
            "locate/forest/fox_snowball/Snowboll_04.png"
            pause 0.1
            alpha 1.0
            pause 0.3
            linear 0.7 alpha 0.0
    image mini_Polina:
        "locate/street/HousePol/Polin.png"
    image d4_anton_serious = "locate/street/anton_battle/scene_04/Anton_00.png"
    image d4_anton_rot = "locate/school/in_side/Anton_class/M_02.png"
    image d4_hall_door = "locate/school/in_side/school_hall/koridorchic_Door_day.png"
    image d4_class_classmates_1 = "locate/school/in_side/classroom/classroom_Day2.png"
    image anton_class = "locate/school/in_side/Anton_class/Anton.png"
    image ant_clas_m2 = "locate/school/in_side/Anton_class/m_02.png"
    image ant_clas_m7 = "locate/school/in_side/Anton_class/m_07.png"

    image d4_album_bg = "locate/school/in_side/album/A_01.png"
    image d4_album 2 = "locate/school/in_side/album/A_02.png"
    image d4_album 3 = "locate/school/in_side/album/A_03.png"
    image d4_album 4 = "locate/school/in_side/album/A_04.png"
    image d4_album 5 = "locate/school/in_side/album/A_05.png"
    image d4_album 6 = "locate/school/in_side/album/A_06.png"
    image d4_album 7 = "locate/school/in_side/album/A_07.png"
    image d4_album 8 = "locate/school/in_side/album/A_08.png"
    image d4_album 9 = "locate/school/in_side/album/A_09.png"
    image d4_model_fon = "locate/school/in_side/album/A_fon.png"

    image d4_mess_def:
        contains:
            "bg parta"
        contains:
            "d4_album 9"

    image d4_mess_dark:
        contains:
            "d4_mess_def"
        contains:
            "bg_black"
            alpha .7

    image d4_mess_slow:
        contains blink_slow_transform("d4_mess_def", "d4_mess_dark")

    image d4_mess_fast:
        contains blink_fast_transform("d4_mess_def", "d4_mess_dark")

    image d4_palgar_bg2 = "locate/forest/forest_meet/dark/Fon_back2.png"
    image d4_palgar_master_hand = "locate/forest/forest_meet/dark/master_hand.png"
    image d4_palgar_shadow_blink:
        choice:
            "locate/forest/forest_meet/dark/Shadow1.png" with Dissolve(.1)
            .2
            "locate/forest/forest_meet/dark/Shadow2.png" with Dissolve(.1)
            .2
            Null()
        choice:
            "locate/forest/forest_meet/dark/Shadow2.png" with Dissolve(.1)
            .2
            "locate/forest/forest_meet/dark/Shadow1.png" with Dissolve(.1)
            .2
            Null()
        choice:
            .2
        choice:
            .4
        choice:
            .6
        repeat

    image d4_color1_bg = "locate/forest/forest_meet/color/color_fon.png"
    image d4_color1_roof = "locate/forest/forest_meet/color/roof.png"
    image d4_color1_moroz = "locate/forest/forest_meet/color/moroz.png"
    image d4_color1_moroz_hand = "locate/forest/forest_meet/color/hand.png"
    image d4_color1_elka = "locate/forest/forest_meet/color/el.png"
    image d4_color1_elka2 = "locate/forest/forest_meet/color/el2.png"

    image d4_color_star_1:
        "locate/forest/forest_meet/color/a1.png" with Dissolve(.2)
        .2
        "locate/forest/forest_meet/color/a2.png" with Dissolve(.2)
        .2
        repeat
    image d4_color_star_2:
        "locate/forest/forest_meet/color/b1.png" with Dissolve(.2)
        .2
        "locate/forest/forest_meet/color/b2.png" with Dissolve(.2)
        .2
        repeat

    image d4_color_star = ConditionSwitch(
        "not d4_startype", "d4_color_star_1",
        "True", "d4_color_star_2")

    image d4_color_bg3 = "locate/forest/forest_meet/color/colorfon3.png"
    image d4_color_alice = "locate/forest/forest_meet/color/Alisa.png"
    image d4_color_olya_hand1:
        "sprite/Olya/Color/default/left.png"
        yoffset 100
        block:
            ease .25 yoffset 0
            ease .25 yoffset 100
            ease .25 yoffset 0
            ease .25 yoffset 100
            ease .25 yoffset 200
            ease .25 yoffset 100
            ease .25 yoffset 200
            ease .25 yoffset 100
            repeat
    image d4_color_olya_hand2:
        "sprite/Olya/Color/default/right.png"
        yoffset 100
        block:
            ease .25 yoffset 200
            ease .25 yoffset 100
            ease .25 yoffset 200
            ease .25 yoffset 100
            ease .25 yoffset 0
            ease .25 yoffset 100
            ease .25 yoffset 0
            ease .25 yoffset 100
            repeat

    image d4_color_olya_dance:
        contains:
            "Olya Color default 00 good ahead 02"
        contains:
            "d4_color_olya_hand1"
        contains:
            "d4_color_olya_hand2"

    image d4_color_wolf_1 = "locate/forest/forest_meet/color/wolf01.png"
    image d4_color_wolf_2 = "locate/forest/forest_meet/color/wolf02.png"
    image d4_color_wolf_3 = "locate/forest/forest_meet/color/wolf03.png"
    image d4_color_wolf_4 = "locate/forest/forest_meet/color/wolf04.png"

    image d4_color_wolf:
        "d4_color_wolf_1"
        .1
        "d4_color_wolf_2"
        .1
        "d4_color_wolf_3"
        .1
        "d4_color_wolf_4"
        .1
        repeat

    image d4_color_gifts = "locate/forest/forest_meet/color/presents.png"
    image d4_color_polyana = LiveComposite((4000, 2250),
        (0, 0), "day3_jump_bg_cl",
        (0, 0), "d4_color_gifts")

    image d4_color_children = "locate/forest/forest_meet/color/childs.png"

screen starrise():
    layer "master"
    for i in range(27):
        if i < 10:
            $ idx = i
        elif i < 19:
            $ idx = 19 - i
        else:
            $ idx = i - 18
        add "d4_color_star_1":

            at transform:
                anchor (.5, .5)
                pos (380, 650)
                alpha 0
                i*0.05
                parallel:
                    linear .15 alpha 1
                parallel:
                    linear .5 xoffset -100+idx*25 ypos -225

screen starfall():
    layer "master1"
    $ starfall_endpos = [
        (1400, 900),
        (400, 500),
        (450, 800),
        (270, 400),
        (806, 650),
        (925, 350),
        (1909, 775),
        (500, 200),
        (1385, 350),
    ]
    for i in range(len(starfall_endpos)):
        add "d4_color_star_1":
            if i % 3 == 0:

                at transform:
                    animation
                    subpixel True
                    pos (starfall_endpos[i][0], -225)
                    anchor (.5, .5)
                    i*0.15
                    linear (starfall_endpos[i][1]+225) / 1200 ypos starfall_endpos[i][1]
                    block:
                        easeout 1.5 xoffset -25
                        ease 1.5 xoffset 25 yoffset -25
                        ease 1.5 xoffset 0 yoffset 0
                        repeat
            if i % 3 == 1:
                at transform:
                    animation
                    subpixel True
                    pos (starfall_endpos[i][0], -225)
                    anchor (.5, .5)
                    i*0.15
                    linear (starfall_endpos[i][1]+225) / 1200 ypos starfall_endpos[i][1]
                    block:
                        ease 5 xoffset 5*3 yoffset 0
                        ease 5 xoffset -5*3 yoffset -5*3
                        ease 5 xoffset 0 yoffset 5*3
                        ease 5 xoffset -5*3 yoffset 0
                        repeat
            if i % 3 == 2:
                at transform:
                    animation
                    subpixel True
                    pos (starfall_endpos[i][0], -225)
                    anchor (.5, .5)
                    i*0.15
                    linear (starfall_endpos[i][1]+225) / 1200 ypos starfall_endpos[i][1]
                    parallel:
                        ease 4.5 xoffset -25
                        ease 4.5 xoffset 25
                        repeat
                    parallel:
                        ease 2.5 yoffset -15
                        ease 2.5 yoffset 15
                        repeat
    for i in range(10):
        $ xpos = int(renpy.random.random() * (1920-200) + 100)
        $ ypos = int(renpy.random.random() * (1080-500) + 100)
        add "d4_color_star_1":

            at transform:
                animation
                zoom .5
                subpixel True
                pos (xpos, ypos)
                anchor (.5, .5)
                alpha 0
                parallel:
                    i * 0.25
                    block:
                        linear .25 alpha 1.
                        .5
                        linear .25 alpha 0.0
                        2.0
                        repeat
                parallel:
                    ease 2 rotate 30
                    ease 2 rotate -30
                    repeat



init:
    image d4_classroom_night_bg = "locate/school/in_side/classroom/classroom_Night.png"
    image d4_classroom_night_word = "locate/school/in_side/classroom/classroom_Night_word.png"

    image d4_grafit_bg = "locate/school/in_side/album/grafit/grafitfon.png"
    image d4_grafit_hand = "locate/school/in_side/album/grafit/hand.png"
    image d4_grafit_grafit_ok = "locate/school/in_side/album/grafit/grafit.png"
    image d4_grafit_grafit_broken = "locate/school/in_side/album/grafit/grafit3.png"
    image d4_grafit_spot = "locate/school/in_side/album/grafit/grafit4.png"
    image d4_grafit_fragments = "locate/school/in_side/album/grafit/grafit2.png"

    image d4_khoridor_night_bg = "locate/school/in_side/school_hall/koridorchic_night.png"
    image d4_khoridor_night_door = "locate/school/in_side/school_hall/koridorchic_night_door.png"

    image d4_school_night = "locate/school/out_side/school_dark.png"

    image d4_road_night = "locate/street/road_Dark.png"

    image d4_poldoor_dark_0 = "locate/polina/door_polin/door_polin_dark0.png"
    image d4_poldoor_dark_1 = "locate/polina/door_polin/door_polin_dark001.png"
    image d4_poldoor_dark_2 = "locate/polina/door_polin/door_polin_dark002.png"
    image d4_poldoor_dark_3 = "locate/polina/door_polin/door_polin_dark003.png"
    image d4_poldoor_dark_bg = "locate/polina/door_polin/door_polin_fon.png"

    image d4_selmag_fon_dark = "locate/polina/rom_dark/selmag/fon_dark.png"
    image d4_selmag_mag_dark = "locate/polina/rom_dark/selmag/mag_dark.png"

    image d4_road_dark_1 = "locate/street/walking_fox/road_dark01.jpg"
    image d4_road_dark_2 = "locate/street/walking_fox/road_dark02.png"
    image d4_road_dark_3 = "locate/street/walking_fox/road_dark03.png"

    image d4_road_dark:
        contains:
            "d4_road_dark_1"
            xpan 180
            linear 45 xpan 180 - 360
            repeat
        contains:
            "d4_road_dark_2"
            xpan 180
            linear 20 xpan 180 - 360
            repeat
        contains:
            "d4_road_dark_3"
            xpan 180
            linear 9 xpan 180 - 360
            repeat

    image d4_road_dark_shadow = "locate/street/walking_fox/Shadow_owl.png"

    image d4_polhouse_dark = "locate/polina/House_Pol_dark.png"
    image d4_polhouse_door_dark = "locate/polina/door_polin/Door_Polin_dark0.png"

    image d4_polhouse_door_dark_bg = "locate/polina/door_polin/Door_Polin_fon.png"
    image d4_polhouse_door_dark_001 = "locate/polina/door_polin/Door_Polin_dark001.png"
    image d4_polhouse_door_dark_002 = "locate/polina/door_polin/Door_Polin_dark002.png"
    image d4_polhouse_door_dark_003 = "locate/polina/door_polin/Door_Polin_dark003.png"

    image d4_polhouse_door_dark_anim:
        "d4_polhouse_door_dark_001"
        .1
        "d4_polhouse_door_dark_002"
        .1
        "d4_polhouse_door_dark_003"
        .1
        "d4_polhouse_door_dark_002"
        .1
        "d4_polhouse_door_dark_001"
        .1
        "d4_polhouse_door_dark_002"
        .1
        "d4_polhouse_door_dark_003"
        .1
        "d4_polhouse_door_dark_002"

    image d4_polhouse_door_r = "locate/polina/door_polin/Door_Polin_dark002_r.png"
    image d4_polhouse_door_l = "locate/polina/door_polin/Door_Polin_dark002_l.png"

    image d4_polhouse_chair = "locate/polina/door_polin/buggy.png"

    image d4_polhouse_dark_floor_1 = "locate/polina/door_polin/floor.png"
    image d4_polhouse_dark_floor_2 = "locate/polina/door_polin/floor2.png"

    image d4_polhouse_wolf_bg = "locate/polina/door_polin/wall.png"
    image d4_polhouse_wolf = "locate/polina/door_polin/woolf.png"
    image d4_polhouse_wolf_fg = "locate/polina/door_polin/wall2.png"

    image d4_polina_am_1 = "locate/polina/am/001.png"
    image d4_polina_am_2 = "locate/polina/am/002.png"
    image d4_polina_am_3 = "locate/polina/am/003.png"
    image d4_polina_am_4 = "locate/polina/am/004.png"
    image d4_polina_am_5 = "locate/polina/am/005.png"

    image d4_polina_am_clack:
        contains:
            zoom 1.05
            align (.5, .5)
            "d4_polina_am_1"
            1.
            "d4_polina_am_2"
            .1
            "d4_polina_am_3"
            block:
                linear .01 yoffset 15
                linear .02 yoffset -15
            linear .03 yoffset 0
        contains:
            Null()
            1.1
            "d4_polina_am_4"
            align (.5, .5)
            zoom 1.
            parallel:
                linear 60 xoffset -1800 zoom 4.
            parallel:
                59.
                linear 1. alpha 0
        contains:
            Null()
            1.1
            "d4_polina_am_5"
            align (.5, .5)
            zoom 1.
            parallel:
                linear 60 xoffset -600 zoom 1.6
            parallel:
                59.
                linear 1. alpha 0

    image d4_polyard_bg = "locate/polina/polin_yard/fon.png"

    image d4_polyard_full_1 = "locate/polina/polin_yard/01.png"
    image d4_polyard_full_2 = "locate/polina/polin_yard/02.png"
    image d4_polyard_full_3 = "locate/polina/polin_yard/03.png"
    image d4_polyard_full_animation:
        block:
            choice:
                "d4_polyard_full_1"
                .1
                "d4_polyard_full_2"
                .1
                "d4_polyard_full_3"
                .1
                repeat 1
            choice:
                "d4_polyard_full_1"
                .1
                "d4_polyard_full_2"
                .1
                "d4_polyard_full_3"
                .1
                repeat 2
            choice:
                "d4_polyard_full_1"
                .1
                "d4_polyard_full_2"
                .1
                "d4_polyard_full_3"
                .1
                repeat 3

        .5
        repeat

    image d4_polyard_wolf_1 = "locate/polina/polin_yard/woolf1.png"
    image d4_polyard_wolf_2 = "locate/polina/polin_yard/woolf2.png"
    image d4_polyard_wolf_3 = "locate/polina/polin_yard/woolf3.png"
    image d4_polyard_wolf_animation:
        block:
            choice:
                "d4_polyard_wolf_1"
                .1
                "d4_polyard_wolf_2"
                .1
                "d4_polyard_wolf_3"
                .1
                repeat 1
            choice:
                "d4_polyard_wolf_1"
                .1
                "d4_polyard_wolf_2"
                .1
                "d4_polyard_wolf_3"
                .1
                repeat 2

        1.5
        repeat

    image d4_polyard_owl = "locate/polina/polin_yard/owl.png"
    image d4_polyard_owl_2 = "locate/polina/polin_yard/olw2.png"
    image d4_polyard_owl_3 = "locate/polina/polin_yard/olw3.png"
    image d4_polyard_owl_4 = "locate/polina/polin_yard/olw4.png"
    image d4_polyard_owl_5 = "locate/polina/polin_yard/olw5.png"
    image d4_polyard_owl_animation:
        "d4_polyard_owl_2"
        .1
        "d4_polyard_owl_3"
        .1
        "d4_polyard_owl_4"
        .1
        "d4_polyard_owl_5"
        .1
        Null()

    image d4_polyard_snow_1 = "locate/polina/polin_yard/snow1.png"
    image d4_polyard_snow_2 = "locate/polina/polin_yard/snow2.png"
    image d4_polyard_snow_3 = "locate/polina/polin_yard/snow3.png"
    image d4_polyard_snow_4 = "locate/polina/polin_yard/snow4.png"
    image d4_polyard_snow_5 = "locate/polina/polin_yard/snow5.png"
    image d4_polyard_snow_6 = "locate/polina/polin_yard/snow6.png"
    image d4_polyard_snow_7 = "locate/polina/polin_yard/snow7.png"
    image d4_polyard_snow_8 = "locate/polina/polin_yard/snow8.png"
    image d4_polyard_snow_9 = "locate/polina/polin_yard/snow9.png"
    image d4_polyard_snow_10 = "locate/polina/polin_yard/snow10.png"
    image d4_polyard_snow_11 = "locate/polina/polin_yard/snow11.png"
    image d4_polyard_snow_12 = "locate/polina/polin_yard/snow12.png"
    image d4_polyard_snow_13 = "locate/polina/polin_yard/snow13.png"
    image d4_polyard_snow_14 = "locate/polina/polin_yard/snow14.png"
    image d4_polyard_snow_15 = "locate/polina/polin_yard/snow15.png"
    image d4_polyard_snow_16 = "locate/polina/polin_yard/snow16.png"
    image d4_polyard_snow_17 = "locate/polina/polin_yard/snow17.png"
    image d4_polyard_snow_18 = "locate/polina/polin_yard/snow18.png"
    image d4_polyard_snow_19 = "locate/polina/polin_yard/snow19.png"
    image d4_polyard_snow_20 = "locate/polina/polin_yard/snow20.png"
    image d4_polyard_snow_animation:
        "d4_polyard_snow_1"
        .1
        "d4_polyard_snow_2"
        .1
        "d4_polyard_snow_3"
        .1
        "d4_polyard_snow_4"
        .1
        "d4_polyard_snow_5"
        .1
        "d4_polyard_snow_6"
        .1
        "d4_polyard_snow_7"
        .1
        "d4_polyard_snow_8"
        .1
        "d4_polyard_snow_9"
        .1
        "d4_polyard_snow_10"
        .1
        "d4_polyard_snow_11"
        .1
        "d4_polyard_snow_12"
        .1
        "d4_polyard_snow_13"
        .1
        "d4_polyard_snow_14"
        .1
        "d4_polyard_snow_15"
        .1
        "d4_polyard_snow_16"
        .1
        "d4_polyard_snow_17"
        .1
        "d4_polyard_snow_18"
        .1
        "d4_polyard_snow_19"
        .1
        "d4_polyard_snow_20"

    image d4_polyard_anton 1 = "locate/polina/polin_yard/toh1.png"
    image d4_polyard_anton 2 = "locate/polina/polin_yard/toh2.png"
    image d4_polyard_anton 3 = "locate/polina/polin_yard/toh3.png"
    image d4_polyard_anton 4 = "locate/polina/polin_yard/toh4.png"

    image d4_polyard_alisa_1 = "locate/polina/polin_yard/Alisa01.png"
    image d4_polyard_alisa_2 = "locate/polina/polin_yard/Alisa02.png"
    image d4_polyard_alisa_3 = "locate/polina/polin_yard/Alisa03.png"
    image d4_polyard_alisa_4 = "locate/polina/polin_yard/Alisa04.png"
    image d4_polyard_alisa_5 = "locate/polina/polin_yard/Alisa05.png"
    image d4_polyard_alisa_6 = "locate/polina/polin_yard/Alisa06.png"
    image d4_polyard_alisa_7 = "locate/polina/polin_yard/Alisa07.png"
    image d4_polyard_alisa_8 = "locate/polina/polin_yard/Alisa08.png"
    image d4_polyard_alisa_9 = "locate/polina/polin_yard/Alisa09.png"
    image d4_polyard_alisa_animation:
        "d4_polyard_alisa_1"
        .5
        block:
            "d4_polyard_alisa_2"
            .1
            "d4_polyard_alisa_3"
            .1
            "d4_polyard_alisa_4"
            .1
            "d4_polyard_alisa_5"
            .1
            "d4_polyard_alisa_6"
            .1
            "d4_polyard_alisa_7"
            .1
            "d4_polyard_alisa_8"
            .1
            "d4_polyard_alisa_9"
            .1
            "d4_polyard_alisa_1"

            10.

            repeat

    image d4_beast_fox = "locate/polina/polin_yard/FOX01.png"
    image d4_beast_fox alter = "locate/polina/polin_yard/FOX02.png"

    image d4_beast_owl = "locate/polina/polin_yard/owl2.png"
    image d4_beast_bear = "locate/polina/polin_yard/bear.png"
    image d4_beast_wolf = "locate/polina/polin_yard/woolf.png"

    image d4_noise_1 = "locate/polina/polin_yard/noise/01.png"
    image d4_noise_2 = "locate/polina/polin_yard/noise/02.png"
    image d4_noise_3 = "locate/polina/polin_yard/noise/03.png"
    image d4_noise_4 = "locate/polina/polin_yard/noise/04.png"
    image d4_noise:
        "d4_noise_1"
        .1
        "d4_noise_2"
        .1
        "d4_noise_3"
        .1
        "d4_noise_4"
        .1
        repeat

    image d4_beast_fox_face:
        contains:
            "d4_beast_fox"
            subpixel True
            ypos .3
            yanchor .45
            xalign .5
            parallel:
                ease 2. xoffset -10 yoffset 0
                ease 2. xoffset 0 yoffset 10
                ease 2. xoffset 10 yoffset -10
                repeat
        contains:
            "d4_noise"
    image d4_beast_owl_face:
        contains:
            "d4_beast_owl"
            subpixel True
            ypos .3
            yanchor .45
            xalign .5
            parallel:
                ease 2. xoffset -10 yoffset 0
                ease 2. xoffset 0 yoffset 10
                ease 2. xoffset 10 yoffset -10
                repeat
        contains:
            "d4_noise"
    image d4_beast_bear_face:
        contains:
            "d4_beast_bear"
            subpixel True
            ypos .4
            yanchor .5
            xalign .5
            zoom .9
            parallel:
                ease 2. xoffset -10 yoffset 0
                ease 2. xoffset 0 yoffset 10
                ease 2. xoffset 10 yoffset -10
                repeat
        contains:
            "d4_noise"
    image d4_beast_wolf_face:
        contains:
            "d4_beast_wolf"
            subpixel True
            ypos .35
            yanchor .5
            xalign .5
            zoom .91
            parallel:
                ease 2. xoffset -10 yoffset 0
                ease 2. xoffset 0 yoffset 10
                ease 2. xoffset 10 yoffset -10
                repeat
        contains:
            "d4_noise"

    image d4_monster_alice = "locate/polina/polin_yard/beasts/alice.png"
    image d4_monster_alice_side = "locate/polina/polin_yard/beasts/alice_side.png"
    image d4_monster_bear_0 = "locate/polina/polin_yard/beasts/bear.png"
    image d4_monster_bear_1 = "locate/polina/polin_yard/beasts/bear002.png"
    image d4_monster_beast_0 = "locate/polina/polin_yard/beasts/beast_00.png"
    image d4_monster_beast_1 = "locate/polina/polin_yard/beasts/beast_01.png"
    image d4_monster_beast_2 = "locate/polina/polin_yard/beasts/beast_02.png"
    image d4_monster_beast_3 = "locate/polina/polin_yard/beasts/beast_03.png"
    image d4_monster_beast_4 = "locate/polina/polin_yard/beasts/beast_04.png"
    image d4_monster_beast:
        "d4_monster_beast_1"
        .2
        "d4_monster_beast_2"
        .2
        "d4_monster_beast_3"
        .2
        repeat
    image d4_monster_owl = "locate/polina/polin_yard/beasts/owl.png"
    image d4_monster_fox = "locate/polina/polin_yard/beasts/fox.png"
    image d4_monster_hooty = "locate/polina/polin_yard/beasts/hooty.png"
    image d4_monster_hooty_side = "locate/polina/polin_yard/beasts/hooty_side.png"
    image d4_monster_teddy = "locate/polina/polin_yard/beasts/teddy.png"
    image d4_monster_wolfy = "locate/polina/polin_yard/beasts/wolfy.png"

    image d4_monster_sky = "locate/polina/polin_yard/beasts/sky.png"

    image d4_paw_bg = "locate/polina/polin_yard/anton/fon_03.png"
    image d4_paw_anton_f1 = "locate/polina/polin_yard/anton/01.png"
    image d4_paw_anton_f2 = "locate/polina/polin_yard/anton/02.png"
    image d4_paw_anton_f3 = "locate/polina/polin_yard/anton/03.png"
    image d4_paw_anton_f4 = "locate/polina/polin_yard/anton/04.png"
    image d4_paw_anton_scream:
        "d4_paw_anton_f1"
        .2
        "d4_paw_anton_f2"
        .2
        "d4_paw_anton_f3"
        .2
        "d4_paw_anton_f4"
        .2
        repeat

    image d4_paw_anton_b = "locate/polina/polin_yard/anton/anton.png"
    image d4_paw_anton_m = "locate/polina/polin_yard/anton/anton01.png"
    image d4_paw_anton_m_shadow = "locate/polina/polin_yard/anton/anton02.png"

    image d4_paw_anton_b_shout = "locate/polina/polin_yard/anton/anton2.png"
    image d4_paw_anton_b_angry = "locate/polina/polin_yard/anton/anton3.png"

    image d4_paw_anton_b norm:
        "d4_paw_anton_b"
    image d4_paw_anton_b angry:
        contains:
            "d4_paw_anton_b"
        contains:
            "d4_paw_anton_b_angry"
    image d4_paw_anton_b shout:
        contains:
            "d4_paw_anton_b_shout"
        contains:
            "d4_paw_anton_b_angry"

    image d4_paw_owl_body = "locate/polina/polin_yard/anton/o.png"
    image d4_paw_owl_claw = "locate/polina/polin_yard/anton/o2.png"
    image d4_paw_wolf_body = "locate/polina/polin_yard/anton/w.png"
    image d4_paw_wolf_claw = "locate/polina/polin_yard/anton/w2.png"

    image d4_paw_fog = "interface/main_meny/meny_002.png"

    image d4_master_bg = "locate/forest/forest_meet/beasts1/big_master_fon2.png"
    image d4_master_base = "locate/forest/forest_meet/beasts1/big_masteru1.png"
    image d4_master_scream = "locate/forest/forest_meet/beasts1/big_masteru2.png"

    image d4_master idle = "d4_master_base"
    image d4_master dark = LiveComposite((2933, 1282),
        (0, 0), "d4_master_base", 
        (0, 0), AlphaMask(Solid("#00000080"), "d4_master_base"))
    image d4_master scream = LiveComposite((2933, 1282),
        (0, 0), "d4_master_base",
        (0, 0), "d4_master_scream")

    image d4_polbeast_talkback_bg = "locate/polina/beasts/fon.png"
    image d4_polbeast_talkback_anton 0 = "locate/polina/beasts/anton.png"

    image d4_polbeast_talkback_anton_a01 = "locate/polina/beasts/A01.png"
    image d4_polbeast_talkback_anton_a02 = "locate/polina/beasts/A02.png"
    image d4_polbeast_talkback_anton_a03 = "locate/polina/beasts/A03.png"
    image d4_polbeast_talkback_anton_a04 = "locate/polina/beasts/A04.png"
    image d4_polbeast_talkback_anton 1:
        "d4_polbeast_talkback_anton_a01"
        .1
        "d4_polbeast_talkback_anton_a02"
        .1
        "d4_polbeast_talkback_anton_a03"
        .1
        "d4_polbeast_talkback_anton_a04"
        .1
        repeat

    image d4_polbeast_talkback_anton_an01 = "locate/polina/beasts/An01.png"
    image d4_polbeast_talkback_anton_an02 = "locate/polina/beasts/An02.png"
    image d4_polbeast_talkback_anton_an03 = "locate/polina/beasts/An03.png"
    image d4_polbeast_talkback_anton_an04 = "locate/polina/beasts/An04.png"

    image d4_polbeast_talkback_anton 2:
        "d4_polbeast_talkback_anton_an01"
        .1
        "d4_polbeast_talkback_anton_an02"
        .1
        "d4_polbeast_talkback_anton_an03"
        .1
        "d4_polbeast_talkback_anton_an04"
        .1
        repeat



init:
    image d4e_scene1_bg = "locate/home/in_side/2st_floor/olga_room/Olga_room_day.jpg"
    image d4e_scene1_olya = "locate/Polina/Rom_Dark/END/Olya_Sad.png"

    image d4e_scene2 = "locate/Polina/Rom_Dark/END/tears.png"

    image d4e_scene3_bg = "locate/Polina/Rom_Dark/END/DeadBG.png"
    image d4e_scene3_fg = "locate/Polina/Rom_Dark/END/Dead.png"

    image d4e_scene4_bg = "locate/Polina/Rom_Dark/END/GraveBG.png"
    image d4e_scene4_fg = "locate/Polina/Rom_Dark/END/Grave.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
