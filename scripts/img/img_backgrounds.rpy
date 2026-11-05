init:
    image bg_white = "#F8F8FF"
    image bg_white1 = "#F8F8FF"
    image bg_white2 = "#efefef"
    image bg_black = "#000000"
    image bg_grey = "#808080"
    $ chet_time = 0.3
    image bg_logo = "interface/Lang2.jpg"
    image bg_logo2 = "interface/demo_end/bye.jpg"
    image bg_logo3 = "interface/Lang.jpg"
    image wh_bg:
        alpha 0.0
        "bg_white"
        linear 1.0 alpha 1.0

    image bg_win_f_0 = "locate/home/in_side/1st_floor/kitchen/widow/win_f_0.jpg"
    image bg_win_f_50 = "locate/home/in_side/1st_floor/kitchen/widow/win_f_50.jpg"
    image bg_win_f_100 = "locate/home/in_side/1st_floor/kitchen/widow/win_f_100.jpg"

    image bg_win_f_0_1:
        "bg_win_f_0"
        alpha 0.0
        xalign 0.5
        yalign 0.5
        zoom 1.78
        parallel:
            ease 12.0 zoom 1.00
        parallel:
            linear 12.0 alpha 1.0

    image bg_win_f_50_1:
        "bg_win_f_50"
        alpha 0.0
        linear 3.0 alpha 1.0

    image bg_win_f_100_1:
        "bg_win_f_100"
        alpha 0.0
        linear 1.5 alpha 1.0


    image bg room_day_open_empty = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day.jpg",
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day06.png")

    image bg room_day_open_anton = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day.jpg",
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day05.png")

    image bg room_day_open_olya = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day.jpg",
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day04.png")

    image bg room_day_close_door = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day.jpg")

    image bg_room_day_close_door_blur = LiveComposite((1920, 1080),
        (0, 0), im.Blur("locate/home/in_side/2st_floor/anton_room/room_day/room_day.jpg", 0.8))

    image bg room_day_open_curtain = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day_c.jpg",
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day08.png")

    image bg room_day_open_curtain_anton = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day_c.jpg",
        (0, 0), "locate/home/in_side/2st_floor/anton_room/room_day/room_day07.png")

    image day1_roomday_nocurtain = "locate/home/in_side/2st_floor/anton_room/room_day/room_day_c.jpg"
    image day1_roomday_nocurtain_ door = "locate/home/in_side/2st_floor/anton_room/room_day/room_day08.png"
    image day1_roomday_nocurtain_ anton = "locate/home/in_side/2st_floor/anton_room/room_day/room_day07.png"


    image bg kitchen_dark1 = "locate/home/in_side/1st_floor/kitchen/ketcen_dark.jpg"

    image kalendar_08 = "locate/home/in_side/1st_floor/kitchen/Kal.png"
    image kalendar_07_dark = "locate/home/in_side/1st_floor/kitchen/Kal_3.png"

    image bg kitchen1_0 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Kal.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
        )

    image bg kitchen1_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Kal_2.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
        )

    image bg kitchen1_2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Kal_2.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_8.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/paper.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )


    image bg kitchen1_3 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_01.jpg",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Kal_2.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_7.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/paper.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen ol0 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/plate.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        )

    image kitchen ol1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol1/ol001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 8.50)
        )

    image kitchen ol2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol002.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol3/ol003.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye01.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 8.50)
        )

    image kitchen ol3_0_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol3/ol003.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye01.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye02.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol3/eye03.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 8.50)
        )

    image kitchen ol3_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol003.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3_2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol004.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kitchen_001.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/kasha_002.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3_1_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol003.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3_2_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol004.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3_gop = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol005.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen ol3_gop1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Eol2/ol006.png",
        (0, 0), Animation("locate/home/in_side/1st_floor/kitchen/Eol1/Eol2_28.png", 2.50,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_30.png", 0.20,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_29.png", 0.08,
            "locate/home/in_side/1st_floor/kitchen/Eol2/Eol2_28.png", 8.50)
        )

    image kitchen_book = "locate/home/in_side/1st_floor/kitchen/book.png"
    image kitchen_book_hover:
        "kitchen_book"
        matrixcolor BrightnessMatrix(0.2)

    image kitchen_ant0 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen_ant1_book = LiveComposite((1920, 1080),
        (0, 0), "kitchen_book",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/A1.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen_ant1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/A1.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen_ant2_book = LiveComposite((1920, 1080),
        (0, 0), "kitchen_book",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/A2.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen_ant2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/A2.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image kitchen_ant3 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/kitchen/A3.png",
        (0, 0), "locate/home/in_side/1st_floor/kitchen/Char.png",
        )

    image under_table = "locate/home/in_side/1st_floor/kitchen/Table_ka.jpg"

    image bg fridge1 = "locate/home/in_side/1st_floor/kitchen/holodoz.jpg"

    image bg fridge0 = LiveComposite((1920, 1080),
            (0, 0), "locate/home/in_side/1st_floor/kitchen/holodoz.jpg",
            (0, 0), "locate/home/in_side/1st_floor/kitchen/List001.png")

    image bg kitchen_window1 = "locate/home/in_side/1st_floor/kitchen/widow/dogs.jpg"
    image day1_myth = "locate/home/in_side/1st_floor/kitchen/widow/dogs_myth.png"
    image bg kitchen_window2 = "locate/home/in_side/1st_floor/kitchen/widow/road_2.jpg"
    image bg kitchen_window3 = "locate/home/in_side/1st_floor/kitchen/dogs_3.jpg"

    image bg in_fridge1 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_1.jpg"
    image bg in_fridge2 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_2.jpg"
    image bg in_fridge3 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_3.jpg"
    image bg in_fridge4 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_4.jpg"
    image bg in_fridge5 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_5.jpg"
    image bg in_fridge6 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_6.jpg"
    image bg in_fridge10 = "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_10.jpg"

    image pan 0 = "locate/forest/anton_nightmare/pan/00.jpg"
    image pan 1 = "locate/forest/anton_nightmare/pan/01.jpg"
    image pan 2 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/anton_nightmare/pan/A_00.jpg",
        (0, 0), Animation("locate/forest/anton_nightmare/pan/A_01.png", 0.15,
            "locate/forest/anton_nightmare/pan/A_02.png", 0.15,
            "locate/forest/anton_nightmare/pan/A_03.png", 0.15,
            "locate/forest/anton_nightmare/pan/A_04.png", 0.15,
            "locate/forest/anton_nightmare/pan/A_05.png", 0.15))

    image pan_1ani = Animation("locate/forest/anton_nightmare/pan/01.jpg", 0.1, "locate/forest/anton_nightmare/pan/02.jpg", 0.1, "locate/forest/anton_nightmare/pan/03.jpg", 0.1, "locate/forest/anton_nightmare/pan/01.jpg", 60.0)

    image vzih_bg:
        "locate/forest/anton_nightmare/Vzih/vzih.jpg"

    image vzih_anim1 = Animation("locate/forest/anton_nightmare/Vzih/vzih_01.jpg", 0.1,
        "locate/forest/anton_nightmare/Vzih/vzih_02.jpg", 0.1,
        "locate/forest/anton_nightmare/Vzih/vzih_03.jpg", 0.1,
        "locate/forest/anton_nightmare/Vzih/vzih_04.jpg", 0.1)

    image Dad_mask = im.MatrixColor("sprite/Dad/Mask/m_night/1_body/00.png", im.matrix.brightness(-1.0))
    image Mom_mask = im.MatrixColor("sprite/Mom/Mask/m_night/1_body/00.png", im.matrix.brightness(-1.0))
    image Olya_mask = im.MatrixColor("sprite/Olya/Mask/m_night/1_body/00.png", im.matrix.brightness(-1.0))

    image Zaichik_01 = Animation("locate/forest/anton_nightmare/Zaichik_01.png", 5.2,
        "locate/forest/anton_nightmare/Zaichik_03.png", 0.1,
        "locate/forest/anton_nightmare/Zaichik_04.png", 0.1,
        "locate/forest/anton_nightmare/Zaichik_03.png", 0.1,
        "locate/forest/anton_nightmare/Zaichik_01.png", 3.0)
    image Zaichik_02 = "locate/forest/anton_nightmare/Zaichik_02.png"

    image Wecup_00 = "locate/forest/anton_nightmare/Wecup_00.jpg"

    image Wecup_00_ani:
        contains:
            "locate/forest/anton_nightmare/Wecup_00.jpg"
            alpha 1.0 xpos 0 ypos 0
            parallel:
                xpos 0 ypos 0
                ease 0.1 xpos -10 ypos -10
                ease 0.1 xpos 10 ypos 10
                repeat
            parallel:
                ease 3.0 alpha 0.0

    image Wecup_01 = "locate/forest/anton_nightmare/Wecup_01.jpg"
    image Wecup_02 = "locate/forest/anton_nightmare/Wecup_02.jpg"

    image bg Anton_kovai = Ani_png("locate/home/in_side/2st_floor/anton_room/Anton_kovai0", 2, .2, effect=dd2)
    image bg Anton_kovai1 = "locate/home/in_side/2st_floor/anton_room/Anton_kovai01.png"


    image bg Olya_and_Owl0 = "locate/home/in_side/2st_floor/olga_room/Olya_and_Owl000.jpg"
    image bg Olya_and_Owl1 = "locate/home/in_side/2st_floor/olga_room/Olya_and_Owl001.jpg"
    image bg Olya_and_Owl2 = "locate/home/in_side/2st_floor/olga_room/Olya_and_Owl002.jpg"

    image bg Olya_and_Owl = Ani_jpg("locate/home/in_side/2st_floor/olga_room/Olya_and_Owl00", 2, .2, effect=dd2)

    image owl_screem_effect = Animation("effect/owl/Owl1.jpg", 0.22, "effect/owl/Owl2.jpg", 0.06, "effect/owl/Owl1.jpg", 0.26, "effect/owl/Owl2.jpg", 0.06, "effect/owl/Owl1.jpg", 0.22, "effect/owl/own_em.png", 30.0)


    image blossoms1 = SnowBlossom("effect/snow/s001.png", count=3, yspeed=(1300, 1400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms2 = SnowBlossom("effect/snow/s002.png", count=3, yspeed=(1200, 1300), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms3 = SnowBlossom("effect/snow/s003.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms4 = SnowBlossom("effect/snow/s004.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms5 = SnowBlossom("effect/snow/s005.png", count=12, yspeed=(650, 770), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms6 = SnowBlossom("effect/snow/s006.png", count=16, yspeed=(385, 400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms7 = SnowBlossom("effect/snow/s007.png", count=24, yspeed=(300, 380), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms8 = SnowBlossom("effect/snow/s008.png", count=27, yspeed=(265, 290), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms9 = SnowBlossom("effect/snow/s009.png", count=33, yspeed=(265, 270), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
    image blossoms10 = SnowBlossom("effect/snow/s010.png", count=50, yspeed=(150, 190), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear")
    image blossoms11 = SnowBlossom("effect/snow/s011.png", count=70, yspeed=(100, 115), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear")
    image blossoms12 = SnowBlossom("effect/snow/s012.png", count=195, yspeed=(100, 110), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear")
    image blossoms13 = SnowBlossom("effect/snow/s013.png", count=350, yspeed=(90, 100), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear")
    image blossoms14 = SnowBlossom("effect/snow/s014.png", count=900, yspeed=(60, 70), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear")

    image bg_pole0 = "locate/forest/pole/pole0.jpg"
    image bg_pole1 = "locate/forest/pole/pole1.png"
    image bg_pole2 = "locate/forest/pole/pole2.png"

    image dancing animal_off = "locate/forest/pole/tanech/p000.jpg"
    image dancing animal_on = Ani_jpg("locate/forest/pole/tanech/p00", 12, .2, effect=dd2)

    image over_dancing = LiveComposite((1920, 1080),
        (0, 0), "blossoms14",
        (0, 0), "blossoms13",
        (0, 0), "blossoms12",
        (0, 0), "blossoms11",
        (0, 0), "blossoms10",
        (0, 0), "bg_pole1",
        (0, 0), "blossoms9",
        (0, 0), "blossoms8",
        (0, 0), "blossoms7",
        (0, 0), "blossoms6",
        (0, 0), "bg_pole2",
        (0, 0), "blossoms5",
        (0, 0), "blossoms4",
        (0, 0), "blossoms3",
        (0, 0), "blossoms2",
        (0, 0), "blossoms1",
        )

    image over_dancing2 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=16, yspeed=(385, 400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=24, yspeed=(300, 380), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=27, yspeed=(265, 290), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s009.png", count=33, yspeed=(265, 270), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        )

    image dancing animal_wolf1 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/pole/pole0.jpg",
        (286, 233), "locate/forest/pole/volk/Beast_0.png")

    image dancing2 animal_wolf2 = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/forest/pole/volk/Beast_1.png", 0.10,
            "locate/forest/pole/volk/Beast_2.png", 0.10,
            "locate/forest/pole/volk/Beast_3.png", 0.10,
            "locate/forest/pole/volk/Beast_4.png", 0.10,
            "locate/forest/pole/volk/Beast_5.png", 0.10,
            "locate/forest/pole/volk/Beast_6.png", 0.10,
            "locate/forest/pole/volk/Beast_7.png", 0.10,
            "locate/forest/pole/volk/Beast_8.png", 0.10,
            "locate/forest/pole/volk/Beast_9.png", 0.10,
            "locate/forest/pole/volk/Beast_10.png", 0.10,
            Null(10,10), 5.10))


    image bg_room_night1 = "locate/home/in_side/2st_floor/anton_room/room_night.jpg"

    image bg_room_night2 = "locate/home/in_side/2st_floor/anton_room/room_night2.jpg"

    image bg_room_night3 = "locate/home/in_side/2st_floor/anton_room/room_night2(owl).jpg"

    image bg room_night_ZOOM = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/001.jpg"

    image room_night_zoom_door 1 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png"
    image room_night_zoom_door 2 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png"
    image room_night_zoom_door 3 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png"

    image door open_door1_1:
        Animation("locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.60,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.60,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 0.80,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.50,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.40,
            )
        alpha 1.0
        linear 3.0
        linear 0.01 alpha 0.0

    image door open_door1_2:
        Animation("locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.30,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.30,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 0.40,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.20,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.20,
            )
        alpha 1.0
        linear 1.4
        linear 0.01 alpha 0.0

    image door open_door1_3 = Animation(
            Null(), 0.10,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 0.10,
            )

    image bg room_night_ZOOM_2:
        LiveComposite((1920, 1080),
            (0, 0), "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/001.jpg",
            (0, 0), "door open_door1_3")
        parallel:
            xoffset 0
            yoffset 0
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            linear 0.07 xoffset renpy.random.randint(-4, 4) yoffset renpy.random.randint(-4, 4)
            repeat

    image door open_door1_4 = Animation("locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.60,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.60,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 0.50,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.30,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.30,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 0.20,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/002.png", 0.20,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/003.png", 0.20,
            "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/004.png", 5.10)

    image door open_door1 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/d004.png"

    image door open_door2 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/d005.png"

    image door open_door3 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/d006.png"

    image door open_door4 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/d007.png"

    image bg room_night_opendoor = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/007.jpg"

    image door open_door5 = "locate/home/in_side/2st_floor/anton_room/night_zoom_scrimer/d008.png"

    image wolf_scrimer = Animation("effect/wolf/scrimer2.png", 0.20, "effect/wolf/scrimer.png", 0.20, "effect/wolf/scrimer2.png", 0.15, "effect/wolf/scrimer.png", 9.25)

    image Ant_wakeup = Ani_jpg2("locate/home/in_side/2st_floor/anton_room/wekup/wekup_0", 47)


    image bg door_night = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/hall01_ivning.jpg",
        (0, 0), "locate/home/in_side/1st_floor/hall/hall01_ivning.png",
        )

    image bg door_open_night = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/hall01_ivning.jpg",
        )

    image bg door_night_blur = LiveComposite((1920, 1080),
        (0, 0), im.Blur("locate/home/in_side/1st_floor/hall/hall01_ivning.jpg", 1.5),
        (0, 0), im.Blur("locate/home/in_side/1st_floor/hall/hall01_ivning.png", 1.5),
        )

    image bg door_open_night_blur = LiveComposite((1920, 1080),
        (0, 0), im.Blur("locate/home/in_side/1st_floor/hall/hall01_ivning.jpg", 1.5),
        )

    image bg door_police = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/door_police.jpg",
        (0, 0), "locate/home/in_side/1st_floor/hall/cross_01.png",
        (0, 0), "locate/home/in_side/1st_floor/hall/yula_01.png",
        )

    image bg door = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/door.jpg"  ,
        (0, 0), "locate/home/in_side/1st_floor/hall/cross_02.png",
        (0, 0), "locate/home/in_side/1st_floor/hall/yula_02.png",
        )

    image bg door1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/door.jpg"  ,
        (0, 0), "locate/home/in_side/1st_floor/hall/cross_02.png",
        
        )

    image door_narco:
        contains:
            alpha 0.0
            linear 0.3 alpha 0.5
            contains:
                "locate/home/in_side/1st_floor/hall/Halll_2.png"
                alpha 1.0
                linear 0.35 xoffset -10 yoffset 0
                linear 0.35 xoffset 10 yoffset 0
                linear 0.55 xoffset -10 yoffset 0
                linear 0.45 xoffset 10 yoffset 0
                linear 0.35 xoffset -10 yoffset 0
                linear 0.65 xoffset 10 yoffset 0 alpha 0.0
            contains:
                "locate/home/in_side/1st_floor/hall/Halll.png"
                alpha 1.0
                linear 0.45 xoffset -10 yoffset 0
                linear 0.45 xoffset 10 yoffset 0
                linear 0.45 xoffset -10 yoffset 0
                linear 0.45 xoffset 10 yoffset 0
                linear 0.45 xoffset -10 yoffset 0
                linear 0.45 xoffset 10 yoffset 0 alpha 0.0
            contains:
                "old_movie_001_002"
                alpha 1.0
                linear 0.45 xoffset -10 yoffset 0 alpha 0.0
                linear 1.10
            contains:
                "old_movie_003_004"
                alpha 0.0
                linear 1.10
                alpha 1.0
                linear 0.45 xoffset -10 yoffset 0 alpha 0.0
            linear 15.00
            repeat

    image bg door_open = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/door_open.jpg"  ,
        (0, 0), "locate/home/in_side/1st_floor/hall/cross_01.png",
        (0, 0), "locate/home/in_side/1st_floor/hall/yula_01.png",
        )

    image open_pantry = "locate/home/in_side/1st_floor/hall/pantry_01.png"

    image bg fotoboy_man_and:
        contains:
            "locate/home/in_side/1st_floor/hall/fotoboy_fon.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/fotoboy_man.png"
            xpos -200 zoom 1.7
            yalign 1.0
            linear 4.3 yalign 0.0

    image bg fotoboy_man:
        contains:
            "locate/home/in_side/1st_floor/hall/fotoboy_fon.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/fotoboy_man.png"
            xpos -200 zoom 1.7 yalign 0.0

    image fotoboy_hand = "locate/home/in_side/1st_floor/hall/fotoboy_hand.png"

    image memory_scrimer1 = Animation("effect/memory1/field_001.jpg", 0.10,
        "effect/memory1/field_002.jpg", 0.10,
        "effect/memory1/field_003.jpg", 0.10,
        "effect/memory1/field_004.jpg", 0.10,
        "effect/memory1/field_005.jpg", 0.10,
        "effect/memory1/field_006.jpg", 0.10,
        "effect/memory1/field_007.jpg", 0.10,
        "effect/memory1/field_008.jpg", 0.10,
        "effect/memory1/field_009.jpg", 0.10,
        "effect/memory1/field_010.jpg", 0.10,
        "effect/memory1/field_011.jpg", 0.10,
        "effect/memory1/field_012.jpg", 0.10)

    image memory_scrimer_grandmother = Animation("effect/grandma/g_01.jpg", 0.10,
        "effect/grandma/g_02.jpg", 0.10,
        "effect/grandma/g_03.jpg", 0.10,
        "effect/grandma/g_04.jpg", 0.10,
        "effect/grandma/g_05.jpg", 0.10,
        "effect/grandma/g_06.jpg", 0.10)

    image memory_scrimer2 = Animation("effect/memory2/v_000.jpg", 0.10,
        "effect/memory2/v_001.jpg", 0.10,
        "effect/memory2/v_002.jpg", 0.10,
        "effect/memory2/v_003.jpg", 0.10,
        "effect/memory2/v_004.jpg", 0.10,
        "effect/memory2/v_005.jpg", 0.10,
        "effect/memory2/v_006.jpg", 0.10,
        "effect/memory2/v_007.jpg", 0.10,
        "effect/memory2/v_008.jpg", 0.10,
        "effect/memory2/v_009.jpg", 0.10,
        "effect/memory2/v_010.jpg", 0.10)

    image var_in_hand0 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/1st_floor/hall/var/var_0.jpg",
        (0, 0), Animation(
            "locate/home/in_side/1st_floor/hall/var/001.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/002.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/003.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/004.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/005.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/006.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/007.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/008.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/009.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/010.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/011.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/012.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/013.png", 0.10,
            "locate/home/in_side/1st_floor/hall/var/014.png", 0.10))
    image var_in_hand1 = "locate/home/in_side/1st_floor/hall/var/var.jpg"

    image bg hall_dlin = "locate/home/in_side/1st_floor/hall/fon_preh_02.jpg"


    image bg house_night1 = "locate/home/out_side/hOUSE_night06.jpg"

    image bg house_night6_snow = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/hOUSE6_1.png",
        (0, 0), SnowBlossom("effect/snow/s014.png", count=90, yspeed=(70, 80),   xspeed=(5, 20),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=35, yspeed=(80, 90),   xspeed=(5, 25),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=20, yspeed=(150, 175), xspeed=(5, 25),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s011.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=1000, yspeed=(100, 115), xspeed=(5, 15), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=1000, yspeed=(100, 115), xspeed=(5, 10), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/home/out_side/hOUSE6_2.png",
        (0, 0), SnowBlossom("effect/snow/s009.png", count=10, yspeed=(200, 215), xspeed=(10, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=10, yspeed=(200, 215), xspeed=(10, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/home/out_side/hOUSE6_3.png",
        (0, 0), SnowBlossom("effect/snow/s001.png", count=1, yspeed=(1300, 1400), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s002.png", count=1, yspeed=(1200, 1300), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s003.png", count=1, yspeed=(1000, 1100), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s005.png", count=10, yspeed=(650, 770), xspeed=(0, 10),  border=50, start=0, fast=True, distribution="linear"),
        )

    image bg house_night6_snow_blur = LiveComposite((1920, 1080),
        (0, 0), im.Blur("locate/home/out_side/hOUSE6_1.png", 1.5),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=90, yspeed=(70, 80),   xspeed=(5, 20),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=35, yspeed=(80, 90),   xspeed=(5, 25),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=20, yspeed=(150, 175), xspeed=(5, 25),  border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s011.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=1000, yspeed=(100, 115), xspeed=(5, 15), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=1000, yspeed=(100, 115), xspeed=(5, 10), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=1000, yspeed=(100, 115), xspeed=(5, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), im.Blur("locate/home/out_side/hOUSE6_2.png", 1.5),
        (0, 0), SnowBlossom("effect/snow/s009.png", count=10, yspeed=(200, 215), xspeed=(10, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=10, yspeed=(200, 215), xspeed=(10, 30), border=1, start=0, fast=True, distribution="linear"),
        (0, 0), im.Blur("locate/home/out_side/hOUSE6_3.png", 1.5),
        (0, 0), SnowBlossom("effect/snow/s001.png", count=1, yspeed=(1300, 1400), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s002.png", count=1, yspeed=(1200, 1300), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s003.png", count=1, yspeed=(1000, 1100), xspeed=(0, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s005.png", count=10, yspeed=(650, 770), xspeed=(0, 10),  border=50, start=0, fast=True, distribution="linear"),
        )

    image voron1:
        contains:
            Animation("locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20,
                "locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20,
                "locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20)
            xalign -0.1
            ypos 200
            alpha 0.9
            zoom 0.11
            linear 8.0
            linear 37.0 xalign 1.1 ypos 180 alpha 0.7 zoom 0.09
            repeat
    image voron2:
        contains:
            Animation("locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20,
                "locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20,
                "locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20)
            xalign -0.1
            ypos 200
            alpha 0.9
            zoom 0.1
            linear 10.0
            linear 38.0 xalign 1.1 ypos 160 alpha 0.7
            repeat
    image voron3:
        contains:
            Animation("locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20,
                "locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20,
                "locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20)
            xalign -0.1
            ypos 180
            alpha 0.8
            zoom 0.07
            linear 42.0 xalign 1.1 ypos 180 alpha 0.6
            repeat
    image voron4:
        contains:
            Animation("locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20,
                "locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20,
                "locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20)
            xalign -0.1
            ypos 100
            alpha 0.7
            zoom 0.07
            linear 4.0
            linear 43.0 xalign 1.1 ypos -200 alpha 0.5
            repeat
    image voron5:
        contains:
            Animation("locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20,
                "locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20,
                "locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20,
                "locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20)
            xalign -0.02
            ypos 150
            alpha 0.7
            zoom 0.06
            linear 44.0 xalign 1.1 ypos -100 alpha 0.5
            repeat
    image voron6:
        contains:
            Animation("locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20,
                "locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20,
                "locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20)
            xalign -0.1
            ypos 300
            alpha 0.9
            zoom 0.11
            linear 20.0
            linear 39.0 xalign 1.1 ypos 250 alpha 0.8
            repeat
    image voron7:
        contains:
            Animation("locate/home/out_side/voron/Voron005.png", 0.20,
                "locate/home/out_side/voron/Voron006.png", 0.20,
                "locate/home/out_side/voron/Voron007.png", 0.20,
                "locate/home/out_side/voron/Voron008.png", 0.20,
                "locate/home/out_side/voron/Voron009.png", 0.20,
                "locate/home/out_side/voron/Voron001.png", 0.20,
                "locate/home/out_side/voron/Voron002.png", 0.20,
                "locate/home/out_side/voron/Voron003.png", 0.20,
                "locate/home/out_side/voron/Voron004.png", 0.20)
            xalign -0.1
            ypos 280
            alpha 0.8
            zoom 0.07
            linear 18.0
            linear 42.0 xalign 1.1 ypos 270 alpha 0.6
            repeat

    image bg house_day = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/hOUSE_fon.jpg",
        (0, 0), "voron1",
        (0, 0), "voron2",
        (0, 0), "voron3",
        (0, 0), "voron4",
        (0, 0), "voron5",
        (0, 0), "voron6",
        (0, 0), "voron7",
        (0, 0), "locate/home/out_side/hOUSE_obj.png")


    image bg forest0_long = "locate/forest/wood.jpg"

    image bg_forest0_long_dark = LiveComposite((0, 1080),
        (0, 0), "locate/forest/wood_n.jpg",
        )
    image bg_forest0_long_dark_full = "locate/forest/wood_n.jpg"

    image varezka1 = Animation("locate/forest/varezka/varezka004.png", 1.45,
            "locate/forest/varezka/varezka003.png", 0.15,
            "locate/forest/varezka/varezka002.png", 0.10,
            "locate/forest/varezka/varezka001.png", 1.10,
            "locate/forest/varezka/varezka002.png", 0.10,
            "locate/forest/varezka/varezka003.png", 0.10,
            "locate/forest/varezka/varezka004.png", 0.20,
            "locate/forest/varezka/varezka005.png", 0.20,
            "locate/forest/varezka/varezka004.png", 0.15,
            "locate/forest/varezka/varezka003.png", 0.15,
            "locate/forest/varezka/varezka002.png", 0.10,
            "locate/forest/varezka/varezka001.png", 2.25,
            "locate/forest/varezka/varezka002.png", 0.15,
            "locate/forest/varezka/varezka001.png", 0.85,
            "locate/forest/varezka/varezka002.png", 0.20,
            "locate/forest/varezka/varezka003.png", 0.10,
            "locate/forest/varezka/varezka004.png", 0.10,
            "locate/forest/varezka/varezka005.png", 0.10,
            "locate/forest/varezka/varezka004.png", 0.20,
            "locate/forest/varezka/varezka003.png", 0.20,
            "locate/forest/varezka/varezka002.png", 0.35,
            "locate/forest/varezka/varezka001.png", 1.15,
            "locate/forest/varezka/varezka002.png", 0.50,
            "locate/forest/varezka/varezka001.png", 0.35,
            "locate/forest/varezka/varezka002.png", 0.15,
            "locate/forest/varezka/varezka001.png", 0.85,
            "locate/forest/varezka/varezka002.png", 0.20,
            "locate/forest/varezka/varezka003.png", 0.10,
            "locate/forest/varezka/varezka002.png", 0.20,
            "locate/forest/varezka/varezka001.png", 1.10,
            "locate/forest/varezka/varezka002.png", 0.10,
            "locate/forest/varezka/varezka003.png", 0.10)

    image bg forest0 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/wood06.jpg",
        (0, 0), "locate/forest/wood05.png",
        (0, 0), "locate/forest/wood04.png",
        (0, 0), "locate/forest/wood03.png",
        (0, 0), "locate/forest/wood02.png",
        (0, 0), "varezka1",
        (0, 500), SnowBlossom("interface/main_meny/partikl_002.png", count=120, yspeed=(-20, 80), xspeed=(-190, -280), border=-100, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/forest/wood01.png",
        (0, 700), SnowBlossom("effect/snow/s011.png", count=70, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear")
        )

    image bg forest1_anton = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/h001.jpg",
        (0, 0), "locate/home/out_side/h007.png",
        (0, 450), SnowBlossom("interface/main_meny/partikl_002.png", count=200, yspeed=(-20, 80), xspeed=(190, 280), border=-100, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/home/out_side/left.png",
        (0, 0), "locate/home/out_side/right.png",
        (0, 0), Animation("locate/home/out_side/var/v_001.png", 0.40,
            "locate/home/out_side/var/v_002(26_28_32).png", 0.10,
            "locate/home/out_side/var/v_003(17_25_29_31).png", 0.10,
            "locate/home/out_side/var/v_004(14_19).png", 0.10,
            "locate/home/out_side/var/v_005(13_20_22).png", 0.10,
            "locate/home/out_side/var/v_006(12_21).png", 0.10,
            "locate/home/out_side/var/v_007(11).png", 0.20,
            "locate/home/out_side/var/v_008.png", 0.50,
            "locate/home/out_side/var/v_009.png", 0.40,
            "locate/home/out_side/var/v_010.png", 0.10,
            "locate/home/out_side/var/v_007(11).png", 0.10,
            "locate/home/out_side/var/v_006(12_21).png", 0.10,
            "locate/home/out_side/var/v_005(13_20_22).png", 0.10,
            "locate/home/out_side/var/v_004(14_19).png", 0.10,
            "locate/home/out_side/var/v_015(18_23).png", 0.10,
            "locate/home/out_side/var/v_016(24).png", 0.10,
            "locate/home/out_side/var/v_003(17_25_29_31).png", 0.10,
            "locate/home/out_side/var/v_015(18_23).png", 0.10,
            "locate/home/out_side/var/v_004(14_19).png", 0.10,
            "locate/home/out_side/var/v_005(13_20_22).png", 0.10,
            "locate/home/out_side/var/v_006(12_21).png", 0.10,
            "locate/home/out_side/var/v_005(13_20_22).png", 0.10,
            "locate/home/out_side/var/v_015(18_23).png", 0.10,
            "locate/home/out_side/var/v_016(24).png", 0.10,
            "locate/home/out_side/var/v_003(17_25_29_31).png", 0.10,
            "locate/home/out_side/var/v_002(26_28_32).png", 0.10,
            "locate/home/out_side/var/v_027.png", 0.10,
            "locate/home/out_side/var/v_002(26_28_32).png", 0.10,
            "locate/home/out_side/var/v_003(17_25_29_31).png", 0.10,
            "locate/home/out_side/var/v_030.png", 0.10,
            "locate/home/out_side/var/v_003(17_25_29_31).png", 0.10,
            "locate/home/out_side/var/v_002(26_28_32).png", 0.10))

    image mid b000 = "locate/home/out_side/b00/b000.png"

    image mid b001 = Animation("locate/home/out_side/b00/b001.png", 0.10,
        "locate/home/out_side/b00/b002.png", 0.10,
        "locate/home/out_side/b00/b003.png", 0.10,
        "locate/home/out_side/b00/b004.png", 0.10,
        "locate/home/out_side/b00/b005.png", 0.10,
        "locate/home/out_side/b00/b006.png", 0.10,
        "locate/home/out_side/b00/b007.png", 0.10,
        "locate/home/out_side/b00/b008.png", 0.10,
        "locate/home/out_side/b00/b009.png", 0.10,
        "locate/home/out_side/b00/b010.png", 0.10)

    image snow_for_forest1_anton = LiveComposite((1920, 1080),
        (0, 600), SnowBlossom("effect/snow/s011.png", count=80, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=True, distribution="linear"),
        (0, 600), SnowBlossom("interface/main_meny/partikl_001.png", count=20, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=True, distribution="linear"))
    image snow_for_forest1_anton_02 = LiveComposite((1920, 1080),
        (0, 600), SnowBlossom("effect/snow/s011.png", count=80, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=True, distribution="linear"),
        (0, 600), SnowBlossom("interface/main_meny/partikl_001.png", count=20, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=True, distribution="linear"),
        (-20, 550), SnowBlossom("interface/main_meny/partikl_001.png", count=30, yspeed=(-21, 42), xspeed=(360, 450), border=1, start=0, fast=True, distribution="linear"))
    image snow_for_forest0 = LiveComposite((1920, 1080),
        (0, 500), SnowBlossom("interface/main_meny/partikl_002.png", count=120, yspeed=(-20, 80), xspeed=(-190, -280), border=-100, start=0, fast=True, distribution="linear"),
        (0, 700), SnowBlossom("effect/snow/s011.png", count=70, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear"))

    image an01_e = Animation("locate/home/out_side/Ean1/Eol1_00.png", 2.50,
        "locate/home/out_side/Ean1/Eol1_01.png", 0.08,
        "locate/home/out_side/Ean1/Eol1_02.png", 0.20,
        "locate/home/out_side/Ean1/Eol1_01.png", 0.08,
        "locate/home/out_side/Ean1/Eol1_00.png", 8.50)

    image forest1_A1_bigplan = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/bigplan_h001.jpg",
        (0, 0), "locate/home/out_side/bigplanA_01.png",
        (0, 0), "an01_e")

    image day1_frostforest_bg = "locate/home/out_side/bigplan_h001.jpg"
    image day1_frostforest_anton_base = "locate/home/out_side/bigplanA_01.png"
    image day1_frostforest_anton_eyes0 = "locate/home/out_side/Ean1/Eol1_00.png"
    image day1_frostforest_anton_eyes1 = "locate/home/out_side/Ean1/Eol1_01.png"
    image day1_frostforest_anton_eyes2 = "locate/home/out_side/Ean1/Eol1_02.png"
    image day1_frostforest_anton_blink:
        "day1_frostforest_anton_eyes0"
        choice:
            6.15
        choice:
            7.25
        choice:
            8.35
        "day1_frostforest_anton_eyes1"
        .1
        "day1_frostforest_anton_eyes2"
        .1
        "day1_frostforest_anton_eyes1"
        .1
        repeat
    image day1_frostforest_anton = LiveComposite((1920, 1080),
        (0, 0), "day1_frostforest_anton_base",
        (0, 0), "day1_frostforest_anton_blink")


    image forest1_A2_bigplan = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/bigplan_h001.jpg",
        (0, 0), "locate/home/out_side/bigplanA_02.png")

    image forest1_A3_bigplan = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/bigplan_h001.jpg",
        (0, 0), "locate/home/out_side/bigplanA_03.png")

    image bg forest1_anton2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/h001.jpg",
        (0, 0), "locate/home/out_side/h006.png",
        (0, 450), SnowBlossom("interface/main_meny/partikl_002.png", count=200, yspeed=(-20, 80), xspeed=(190, 280), border=-100, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/home/out_side/left.png",
        (0, 0), "locate/home/out_side/right.png",
        (0, 0), "locate/home/out_side/varezka_but0.png",
        (0, 600), SnowBlossom("effect/snow/s011.png", count=80, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=True, distribution="linear"),
        (0, 600), SnowBlossom("interface/main_meny/partikl_001.png", count=20, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=True, distribution="linear"))

    image bg forest1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/h001.jpg",
        (0, 450), SnowBlossom("interface/main_meny/partikl_002.png", count=200, yspeed=(-20, 80), xspeed=(190, 280), border=-100, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/home/out_side/left.png",
        (0, 0), "locate/home/out_side/right.png")

    image mid ant_for_forest1 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/h006.png",
        (0, 0), "locate/home/out_side/varezka_but0.png")

    image mid ant_for_forest2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/out_side/varezka_but0.png")

    image bg wood = "locate/forest/wood06.jpg"
    image lv1 wood05 = "locate/forest/wood05.png"
    image lv2 wood = Null(10,10)
    image lv3 wood04 = "locate/forest/wood04.png"
    image lv4 wood = Null(10,10)
    image lv5 wood03 = "locate/forest/wood03.png"
    image lv6 wood = Null(10,10)
    image lv7 wood02 = "locate/forest/wood02.png"
    image lv8 wood = Null(10,10)
    image lv9 wood01 = "locate/forest/wood01.png"

    image lv4 chel1 = Ani_png("locate/forest/chel/g00", 10, .1, effect=dd4)
    image lv4 chel2 = Ani_png("locate/forest/chel/h00", 10, .05, effect=dd4)
    image lv6 chel2 = Ani_png("locate/forest/chel/h00", 10, .05, effect=dd4)

    image bg_handblood = "locate/home/out_side/handblood_fon.jpg"
    image handblood_right = "locate/home/out_side/handblood_right.png"
    image handblood_left = "locate/home/out_side/handblood_left.png"

    image maska = "locate/forest/Romka_mask.png"
    image mask_00 = "locate/forest/Romka_mask_00.png"
    image mask_01 = "locate/forest/Romka_mask_01.png"
    image mask_02 = "locate/forest/Romka_mask_02.png"
    image mask_03 = "locate/forest/Romka_mask_03.png"

    image maska_up:
        "maska"
        xpos 960
        ypos 1000 + 1680
        alpha 0.90
        zoom 0.90
        pause 0.5
        ease 2.5 ypos -500+1600 alpha 1.00 zoom 1.00 xpos 955
        block:
            linear 1.0 xpos 955 yoffset 10
            linear 1.0 xpos 957 yoffset 5
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset 5
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset 5
            repeat

    image mask_00_up:
        "mask_00"
        xalign 0.5
        xpos 960
        ypos 1000+ 1450
        alpha 0.90
        zoom 0.90
        linear 0.1
        linear 0.2 ypos 900+ 1450 alpha 0.91 zoom 0.91 xpos 960
        linear 0.2 ypos 800+ 1450 alpha 0.92 zoom 0.92 xpos 960
        linear 0.2 ypos 700+ 1450 alpha 0.93 zoom 0.93 xpos 957
        linear 0.2 ypos 600+ 1450 alpha 0.94 zoom 0.94 xpos 955
        linear 0.2 ypos 500+ 1450 alpha 0.95 zoom 0.95 xpos 955
        linear 0.2 ypos 400+ 1450 alpha 0.96 zoom 0.96 xpos 955
        linear 0.2 ypos 300+ 1450 alpha 0.97 zoom 0.97 xpos 957
        linear 0.2 ypos 200+ 1450 alpha 0.98 zoom 0.98 xpos 957
        linear 0.2 ypos 100+ 1450 alpha 0.99 zoom 0.99 xpos 960
        linear 0.2 ypos 0  + 1450 alpha 1.00 zoom 1.00 xpos 960
        linear 0.2 ypos -100+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -175+ 1450 alpha 1.00 zoom 1.00 xpos 957
        linear 0.2 ypos -250+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -300+ 1450 alpha 1.00 zoom 1.00 xpos 957
        linear 0.2 ypos -325+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -350+ 1450 alpha 1.00 zoom 1.00 xpos 955
        block:
            linear 1.0 xpos 955 yoffset 10
            linear 1.0 xpos 957 yoffset 5
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset 5
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset 5
            repeat

    image mask_00_hand:
        "mask_00"
        xalign 0.5
        xpos 960
        ypos -350+ 1450
        parallel:
            linear 1.0 xpos 955 yoffset 10
            linear 1.0 xpos 957 yoffset 5
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset 5
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset 5
            repeat

    image mask_01_hand:
        "mask_01"
        xalign 0.5
        xpos 960
        ypos -350+ 1450
        parallel:
            linear 1.0 xpos 955 yoffset 10
            linear 1.0 xpos 957 yoffset 5
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset 5
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset 5
            repeat

    image mask_02_hand:
        "mask_02"
        xalign 0.5
        xpos 960
        ypos -350+ 1450
        parallel:
            linear 1.0 xpos 955 yoffset 3
            linear 1.0 xpos 957 yoffset -3
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset -3
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset -3
            repeat

    image mask_03_face:
        "mask_03"
        xalign 0.5
        yalign 0.5
        zoom 1.01
        parallel:
            linear 1.0 yoffset 3
            linear 1.0 yoffset -3
            linear 1.0 yoffset 0
            linear 1.0 yoffset -3
            linear 1.0 yoffset 1
            linear 1.0 yoffset -3
            repeat

    image mask_03_hide:
        "mask_03"
        xalign 0.5
        yalign 0.5
        zoom 1.01
        parallel:
            pause 1.5
            ease 3.0 alpha 0.0
        parallel:
            pause 0.5
            ease 4.0 zoom 1.71 xalign 0.5 yalign 0.5


    image bg_down night_window2_TANECH_down1 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/pole/pole0.jpg",
        (286, 233), Ani_jpg("locate/forest/pole/tanech/p00", 12, .2, effect=dd2))

    image bg_down night_window2_TANECH_down2 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/pole/pole0.jpg",
        (286, 233), "locate/forest/pole/p000.jpg")

    image bg_up bg_null = Null(10,10)

    image bg_mid night_window2_TANECH_up = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=9000, yspeed=(60, 70), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=3500, yspeed=(90, 100), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=1950, yspeed=(100, 110), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s011.png", count=700, yspeed=(100, 115), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s010.png", count=500, yspeed=(150, 190), xspeed=(-10, 0), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/forest/pole/pole1.png",
        (0, 0), SnowBlossom("effect/snow/s009.png", count=335, yspeed=(265, 270), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=275, yspeed=(265, 290), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=240, yspeed=(300, 380), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=85, yspeed=(385, 400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), "locate/forest/pole/pole2.png",
        (0, 0), SnowBlossom("effect/snow/s005.png", count=25, yspeed=(650, 770), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s004.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s003.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s002.png", count=3, yspeed=(1200, 1300), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s001.png", count=3, yspeed=(1300, 1400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear"))

    image bg_down night_window2_TANECH_down3 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/pole/pole0.jpg",
        (286, 233), "locate/forest/pole/volk/Beast_0.png")

    image bg_up night_window2_TANECH_up2 = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/forest/pole/volk/Beast_1.png", 0.10,
            "locate/forest/pole/volk/Beast_2.png", 0.10,
            "locate/forest/pole/volk/Beast_3.png", 0.10,
            "locate/forest/pole/volk/Beast_4.png", 0.10,
            "locate/forest/pole/volk/Beast_5.png", 0.10,
            "locate/forest/pole/volk/Beast_6.png", 0.10,
            "locate/forest/pole/volk/Beast_7.png", 0.10,
            "locate/forest/pole/volk/Beast_8.png", 0.10,
            "locate/forest/pole/volk/Beast_9.png", 0.10,
            "locate/forest/pole/volk/Beast_10.png", 0.10,
            Null(10,10), 5.10))


    image bg night_window1 = "locate/home/in_side/2st_floor/anton_room/window_par/001.jpg"
    image bg night_window2 = "locate/home/in_side/2st_floor/anton_room/window_par/002.jpg"
    image bg night_window2_sneg1 = LiveComposite((1920, 1080),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/002.jpg",
        (-259, 0), Animation("locate/home/in_side/2st_floor/anton_room/window_par/A001.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A001.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A002.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A004.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A005.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A006.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A007.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A008.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A009.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A010.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A011.png", 5.00))
    image bg night_window2_sneg2 = LiveComposite((1920, 1080),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/002.jpg",
        (-259, 0), Animation("locate/home/in_side/2st_floor/anton_room/window_par/A012.png", 2.50,
            "locate/home/in_side/2st_floor/anton_room/window_par/A013.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A014.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A013.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/A012.png", 8.50))
    image bg night_window3 = LiveComposite((1920, 1080),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/024.jpg",
        (-259, 0), Animation("locate/home/in_side/2st_floor/anton_room/window_par/O_001.png", 1.50,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_002.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_004.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_005.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_006.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_007.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_008.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_009.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_010.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_011.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_012.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_013.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_014.png", 0.10),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/Window02.png",
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/Window01.png")

    image bg night_window3_2 = LiveComposite((1920, 1080),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/024.jpg",
        (-259, 0), Animation("locate/home/in_side/2st_floor/anton_room/window_par/O_001.png", 1.50,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_002.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_004.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_005.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_006.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_007.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_008.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_009.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_010.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_011.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_012.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_013.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_014.png", 0.10))
    image bg night_window3_3 = "locate/home/in_side/2st_floor/anton_room/window_par/Window02.png"
    image bg night_window3_4 = "locate/home/in_side/2st_floor/anton_room/window_par/Window01.png"


    image bg_night_forest_meet1 = "locate/forest/forest_meet/Shab_001.jpg"
    image bg_night_forest_meet2 = "locate/forest/forest_meet/Shab_02.png"
    image bg_night_forest_meet3 = "locate/forest/forest_meet/Shab_03.png"
    image bg_night_forest_meet4 = "locate/forest/forest_meet/Shab.png"
    image bg_night_forest_meet5 = "locate/forest/forest_meet/Shab_04.png"
    image bg_night_forest_meet6 = "locate/forest/forest_meet/Shab_05.png"
    image bg_night_forest_meet7 = "locate/forest/forest_meet/Shab_06.png"


    image bg_runaway1 = At("locate/forest/runaway/0002.jpg",Move((2.0, -0.9), (0.0, -2.9), 1.0, xalign=(1.0), repeat=True))
    image bg_runaway2 = At("locate/forest/runaway/0002.jpg",Move((4.0, 1.9), (2.0, -0.9), 1.0, xalign=(1.0), repeat=True))

    image anton_run_full1 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/runaway/Anton/run_away_002.png",
        (0, 0), Animation("locate/forest/runaway/Anton/01.png", 0.05,
            "locate/forest/runaway/Anton/02.png", 0.05,
            "locate/forest/runaway/Anton/03.png", 0.05,
            "locate/forest/runaway/Anton/04.png", 0.05,
            "locate/forest/runaway/Anton/05.png", 0.05,
            "locate/forest/runaway/Anton/06.png", 0.05,
            "locate/forest/runaway/Anton/07.png", 0.05,
            "locate/forest/runaway/Anton/08.png", 0.05))

    image anton_run_full2 = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/runaway/Anton/run_away_003.png",
        (0, 0), Animation("locate/forest/runaway/Anton/01.png", 0.05,
            "locate/forest/runaway/Anton/02.png", 0.05,
            "locate/forest/runaway/Anton/03.png", 0.05,
            "locate/forest/runaway/Anton/04.png", 0.05,
            "locate/forest/runaway/Anton/05.png", 0.05,
            "locate/forest/runaway/Anton/06.png", 0.05,
            "locate/forest/runaway/Anton/07.png", 0.05,
            "locate/forest/runaway/Anton/08.png", 0.05))

    image bg_runaway1_rev = At("locate/forest/runaway/0002.jpg",Move((-2.0, -0.9), (0.0, -2.9), 1.0, xalign=(0.0), repeat=True))
    image bg_runaway2_rev = At("locate/forest/runaway/0002.jpg",Move((-4.0, 1.9), (-2.0, -0.9), 1.0, xalign=(0.0), repeat=True))

    image anton_run_reverse = LiveComposite((1920,1080), (0, 0),
            'locate/forest/runaway/Anton_reversed/run_000.png', (0, 0),
          Animation(
              'locate/forest/runaway/Anton_reversed/run_001.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_002.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_003.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_004.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_005.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_006.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_007.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_008.png', 0.05,
          ))

    image anton_run_rev:
        "anton_run_reverse"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset 22 yoffset -72
            linear 0.2 xoffset 122 yoffset -152
            linear 0.2 xoffset 50 yoffset -130
            linear 0.2 xoffset 122 yoffset -172
            repeat

    image anton_run_reverse_snowball = LiveComposite((1920,1080), (0, 0),
            'locate/forest/runaway/Anton_reversed/run_00.png', (0, 0),
          Animation(
              'locate/forest/runaway/Anton_reversed/run_001.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_002.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_003.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_004.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_005.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_006.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_007.png', 0.05,
              'locate/forest/runaway/Anton_reversed/run_008.png', 0.05,
          ))

    image anton_run_rev_snowball:
        "anton_run_reverse_snowball"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset 22 yoffset -72
            linear 0.2 xoffset 122 yoffset -152
            linear 0.2 xoffset 50 yoffset -130
            linear 0.2 xoffset 122 yoffset -172
            repeat

    image anton_run_full_speed1:
        "anton_run_full1"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset -22 yoffset -72
            linear 0.2 xoffset -122 yoffset -152
            linear 0.2 xoffset -50 yoffset -130
            linear 0.2 xoffset -122 yoffset -172
            repeat

    image anton_run_full_speed2:
        "anton_run_full2"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset -22 yoffset -72
            linear 0.2 xoffset -122 yoffset -152
            linear 0.2 xoffset -50 yoffset -130
            linear 0.2 xoffset -122 yoffset -172
            repeat

    image runaway_snow1 = At("locate/forest/runaway/snow4.png",Move((1.0, 0.1), (0.0, -0.9), 0.33, xalign=(1.0), repeat=True))
    image runaway_snow2 = At("locate/forest/runaway/snow4.png",Move((2.0, 1.1), (1.0, 0.1), 0.33, xalign=(1.0), repeat=True))


    image runaway_snow1_rev:
        "locate/forest/runaway/snow4.png"

        parallel:
            pos (0.0, 0.1)
            linear .25 pos (1.0, -0.9)
            repeat

    image runaway_snow2_rev:
        "locate/forest/runaway/snow4.png"
        parallel:
            pos (-1.0, 1.1)
            linear .25 pos (0.0, 0.1)
            repeat


    image bg_rep_senya = "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_fhoto.png"
    image vova_foto1 = "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_Photo_1.png"

    default dsen = .15
    image bg_rep_senya_crack:
        align (.5,.5)
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_fhoto.png"
        dsen*6
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_fhoto2.png"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_fhoto3.png"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_fhoto4.png"
        dsen*3

        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_01.jpg"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_02.jpg"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_03.jpg"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_04.jpg"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_05.jpg"
        dsen
        "locate/home/in_side/2st_floor/olga_room/Reportash/Tal/Tal_06.jpg"
        dsen*3

    default dvova = .15
    image bg_gar_vova_crack:
        align (.5,.5)
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_Photo_1.png"
        dvova*6
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_Photo_2.png"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_Photo_3.png"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_Photo_4.png"
        dvova*3

        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_01.jpg"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_02.jpg"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_03.jpg"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_04.jpg"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_05.jpg"
        dvova
        "locate/home/in_side/2st_floor/olga_room/Reportash/Vov/Vova_06.jpg"
        dvova*3

    image bg_rep_4_1 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/004.jpg",Move((0.0, 0.0), (1.0, 0.0), 80.0, xalign=(1.0), repeat=True))
    image bg_rep_4_2 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/004.jpg",Move((1.0, 0.0), (2.0, 0.0), 80.0, xalign=(1.0), repeat=True))
    image bg_rep_3_1 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/003.png",Move((0.0, 0.0), (1.0, 0.0), 60.0, xalign=(1.0), repeat=True))
    image bg_rep_3_2 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/003.png",Move((1.0, 0.0), (2.0, 0.0), 60.0, xalign=(1.0), repeat=True))
    image bg_rep_2_1 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/002.png",Move((0.0, 0.0), (1.0, 0.0), 40.0, xalign=(1.0), repeat=True))
    image bg_rep_2_2 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/002.png",Move((1.0, 0.0), (2.0, 0.0), 40.0, xalign=(1.0), repeat=True))
    image bg_rep_1_1 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/001.png",Move((0.0, 0.0), (2.0, 0.0), 20.0, xalign=(1.0), repeat=True))
    image bg_rep_1_2 = At("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/001.png",Move((2.0, 0.0), (4.0, 0.0), 20.0, xalign=(1.0), repeat=True))
    image bg_rep_0:
        "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/000.png"
        alpha 0.5
        parallel:
            xalign 0.5 yalign 1.0
            linear 1.1 yalign 0.1
            linear 0.8 yalign 0.8
            linear 0.4 yalign 0.3

        parallel:
            linear 0.3 alpha 0.1
            linear 0.4
            linear 0.3 alpha 0.9
            linear 0.1
            linear 0.2 alpha 0.2
            linear 0.3
            linear 0.4 alpha 0.7
            linear 0.1
            linear 0.2 alpha 0.0

    image bg_rep_0_2:
        "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/000.png"
        parallel:
            xalign 0.5 yalign 1.0
            linear 1.1 yalign 0.1
            linear 0.8 yalign 0.8
            linear 0.4 yalign 0.3
            repeat
        parallel:
            alpha 0.0
            linear 4.4
            alpha 0.5
            linear 0.3 alpha 0.1
            linear 0.4
            linear 0.3 alpha 0.9
            linear 0.1
            linear 0.2 alpha 0.2
            linear 0.3
            linear 0.4 alpha 0.7
            linear 0.1
            linear 0.2 alpha 0.0
            repeat
    image bg_glich_0:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/001.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/002.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/003.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/004.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/005.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/006.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/007.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/008.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/009.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/010.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/012.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/013.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/014.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/015.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/016.png", 0.1)
        xalign 0.5 ypos 960
        parallel:
            linear 0.8 ypos 1460
            ypos 200
            linear 0.4
            ypos 1700
            linear 0.8 ypos 60
            ypos 960
            linear 0.4
            ypos 260
            linear 0.4 ypos 360
            ypos 1560
            repeat
        parallel:
            linear 0.3 alpha 0.2
            linear 0.4
            linear 0.3 alpha 0.9
            linear 0.1
            linear 0.2 alpha 0.3
            linear 0.3
            linear 0.4 alpha 1.0
            linear 0.1
            linear 0.2 alpha 0.4
            alpha 0.0
            linear 2.0
            repeat
        parallel:
            xoffset 0
            linear 0.9
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            xoffset 0
            linear 3.3
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            xoffset 0
            linear 5.9
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            xoffset 0
            linear 2.3
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            xoffset 0
            linear 7.3
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            xoffset 0
            repeat

    image bg_rep_02:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_01.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_02.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_03.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_04.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_05.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_06.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_07.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_08.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_09.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_10.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_11.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_12.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_13.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_14.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_15.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_16.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_17.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_18.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_19.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_20.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_02/Rep_21.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_1.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_2.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_3.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_4.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_5.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_6.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_7.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_8.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_9.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_10.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_11.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_12.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_13.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_14.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_15.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_16.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_17.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_18.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_19.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_20.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_21.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_22.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_23.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_24.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_25.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_26.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_27.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_28.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_29.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_30.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_31.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_32.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_33.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_34.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_35.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_36.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_37.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_38.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_39.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_03/Rep_40.jpg", 0.1)

    image bg_rep_04:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/005.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/006.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/007.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/008.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/009.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/010.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/011.jpg", 0.1)
        parallel:
            xoffset 0
            linear 5.20
            linear 0.05 xoffset -7
            linear 0.05 xoffset 7
            xoffset 0
            linear 0.10
            repeat

    image bg_rep_05:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/005.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/006.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/007.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/008.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/009.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/010.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/011.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/000.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/000.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/000.jpg", 0.2,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/005.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/001.jpg", 0.2,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/006.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/007.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/008.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/009.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/010.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/002.jpg", 0.2,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/011.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/003.jpg", 0.2,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/004.jpg", 0.2,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/005.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_08/004.jpg", 0.3)
        parallel:
            xoffset 0
            linear 5.20
            linear 0.05 xoffset -7
            linear 0.05 xoffset 7
            xoffset 0
            linear 0.10
            repeat
        parallel:
            alpha 1.0
            linear 4.40
            alpha 0.0

    image bg_rep_06:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/K_001.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_02.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_03.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_04.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_05.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_06.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_07.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_08.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_09.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_10.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_11.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_12.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_13.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/rot/K_02.jpg", 1.1)

    image bg_rep_07:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/K_00.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/K_01.jpg", 0.1)
        parallel:
            yoffset 0
            linear 0.07 yoffset -3
            linear 0.07 yoffset 3
            yoffset 0
            linear 0.05 yoffset -2
            linear 0.05 yoffset 2
            yoffset 0
            linear 0.05
            repeat

    image rep_forest_one:
        "locate/home/in_side/2st_floor/olga_room/Reportash/b2.jpg"
        parallel:
            yoffset 0
            linear 0.07 yoffset -3
            linear 0.07 yoffset 3
            yoffset 0
            linear 0.05 yoffset -2
            linear 0.05 yoffset 2
            yoffset 0
            linear 0.05
            repeat

    image pshhh_forest:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.75,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.05,
            "locate/home/in_side/2st_floor/olga_room/Reportash/k_000.jpg", 2.00,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.05,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.05)
        parallel:
            alpha 0.0
            linear 0.70
            linear 0.05 alpha 1.0
            linear 2.10
            linear 0.05 alpha 0.0

    image pshhh_forest_repeat:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/001.jpg", 0.05,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/002.jpg", 0.05,
            "locate/home/in_side/2st_floor/olga_room/Reportash/k_000.jpg", 2.00,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/003.jpg", 0.05,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_04/004.jpg", 0.05)
        parallel:
            alpha 0.0
            linear 0.05 alpha 1.0

    image bg_rep_snow_1:
        "locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow2.jpg"
        xalign 0
        ypos 1080
        linear 12.00 ypos 3311 + 1080
        parallel:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 2.55
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 1.95
            repeat

    image bg_rep_glaz:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/List/List_001.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_002.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_003.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_004.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_005.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_006.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_007.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_008.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_009.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_010.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_011.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_012.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_013.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_014.jpg", 0.06,
            "locate/home/in_side/2st_floor/olga_room/Reportash/List/List_015.jpg", 0.06)
        alpha 1.0
        linear 0.70
        alpha 0.0

    image bg_rep_snow_2:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow4.jpg", 1.65,
            "locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow3.jpg", 0.50,
            "locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow4.jpg", 0.10,
            "locate/home/in_side/2st_floor/olga_room/Reportash/snow/snow4.jpg", 0.15)
        parallel:
            alpha 0.0
            linear 1.50
            linear 0.05 alpha 1.0
            linear 0.80
            linear 0.05 alpha 0.0

    image bg_tamara:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/tamara/tamara_narez.jpg", 5.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/tamara/tamara_narez_02.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/tamara/tamara_narez_03.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/tamara/tamara_narez_02.jpg", 0.1)
        parallel:
            xoffset 0
            linear 5.20
            linear 0.05 xoffset -7
            linear 0.05 xoffset 7
            xoffset 0
            linear 0.10
            repeat
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

    image bg_glitch_1:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/001.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/002.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/003.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/004.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/005.png", 0.1)
        xalign 0.5 ypos 960
        parallel:
            ypos 960
            linear 5.20
            linear 0.05 ypos 1960
            linear 0.05 ypos 60
            ypos 960
            linear 0.10
            repeat
        parallel:
            alpha 0.0
            linear 5.20
            linear 0.05 alpha 0.9
            linear 0.05 alpha 0.9
            linear 0.10
            alpha 0.0
            repeat

    image bg_glitch_final:
        Animation("locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/001.png", 0.1,
            "bg_black", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/002.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/003.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/004.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/005.png", 0.1,
            "bg_black", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/006.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/007.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/008.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/009.png", 0.1,
            "bg_black", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Reportash/Rep_01/glich/010.png", 0.1)
        xalign 0.5 ypos 960
        alpha 0.0

        parallel:
            ypos 960
            linear 0.25
            linear 0.05 ypos 1960
            linear 0.05 ypos 60
            ypos 960
            linear 0.10
            repeat
        parallel:
            alpha 0.0
            linear 0.25
            linear 0.05 alpha 0.9
            linear 0.05 alpha 0.9
            linear 0.10
            alpha 0.0
            repeat

    image 3TV = "locate/home/in_side/2st_floor/olga_room/Reportash/3TV.jpg"
    image VHS = "locate/home/in_side/2st_floor/olga_room/Reportash/VHS.jpg"
    image VHS_dark = im.MatrixColor("locate/home/in_side/2st_floor/olga_room/Reportash/VHS.jpg",
            im.matrix.brightness(-0.30))


    image bg_Olga_room_day = "locate/home/in_side/2st_floor/olga_room/Olga_room_day.jpg"

    image tv_1_up:
        "locate/home/in_side/2st_floor/olga_room/Olga_room_day_01TV.jpg"
        yalign 0.0

    image tv_1_up_pomehi:
        LiveComposite((1920, 1933),
        (0, 0), "locate/home/in_side/2st_floor/olga_room/Olga_room_day_01TV.jpg",
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/TV_01.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_02.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_03.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_04.png", 0.1))
        yalign 0.0

    image tv_2_up_pomehi:
        LiveComposite((1920, 1933),
        (0, 0), "locate/home/in_side/2st_floor/olga_room/Olga_room_day_02TV.jpg",
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/TV_01.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_02.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_03.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/TV_04.png", 0.1))
        yalign 0.0

    image tv_3:
        "locate/home/in_side/2st_floor/olga_room/Olga_room_day_03TV.jpg"

    image tv_pomehi:
        Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_0.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_1.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_2.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_3.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_4.png", 0.1)

    image tv_multiki:
        Animation("locate/home/in_side/2st_floor/olga_room/room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv3.png", 2.1)

    image tv_multiki_pen:
        "locate/home/in_side/2st_floor/olga_room/room_tv3.png"

    image bg_Olga_room_tv_multiki = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_1.jpg", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_2.jpg", 2.1),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv3.png", 2.1))

    image bg_Olga_room_Evil_tv_multiki = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Ev1.jpg", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Ev2.jpg", 2.1),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv3.png", 2.1))

    image bg_Olga_room_Evil_tv_pomehi = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Ev1.jpg", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Ev2.jpg", 0.1),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_0.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_1.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_2.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_3.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_4.png", 0.1))

    image bg_Olga_room_Evil_tv_okno:
        Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Ev01.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Ev02.png", 0.1)
        alpha 0.0
        linear 6.25 alpha 1.0

    image bg_Olga_room_Evil_full = "locate/home/in_side/2st_floor/olga_room/Olga_room_Ev3.jpg"

    image bg_Olga_room_n_1_bg = "locate/home/in_side/2st_floor/olga_room/Olga_room_n_1.jpg"
    image bg_Olga_room_n_1_light:
        "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_01.png"
        2.1
        "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_02.png"
        2.1
        "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_03.png"
        2.1
        repeat
    image bg_Olga_room_n_1_tv:
        "locate/home/in_side/2st_floor/olga_room/room_tv1.png"
        2.1
        "locate/home/in_side/2st_floor/olga_room/room_tv2.png"
        2.1
        "locate/home/in_side/2st_floor/olga_room/room_tv3.png"
        2.1
        repeat

    image bg_Olga_room_n_1:
        contains:
            "bg_Olga_room_n_1_bg"
        contains:
            "bg_Olga_room_n_1_light"
        contains:
            "bg_Olga_room_n_1_tv"

    image bg_Olga_room_n_2 = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/olga_room/Olga_room_n_2.jpg",
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Light_001.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_002.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_003.png", 2.1,),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv3.png", 2.1))

    image bg_Olga_room_n_2_evil = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/olga_room/Olga_room_n_2.jpg",
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Light_001.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_002.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_003.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_001.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_002.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_003.png", 0.1),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/O_room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/O_room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/O_room_tv3.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_1.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_2.png", 0.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_3.png", 0.1))

    image bg_Olga_room_n_1_back = LiveComposite((1920, 1080),
        (0, 0), "locate/home/in_side/2st_floor/olga_room/Olga_room_n_1.jpg")

    image Olga_room_Light = LiveComposite((1920, 1080),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/Olga_room_Light_01.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_02.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_03.png", 2.1,),
        (0, 0), Animation("locate/home/in_side/2st_floor/olga_room/room_tv1.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv2.png", 2.1,
            "locate/home/in_side/2st_floor/olga_room/room_tv3.png", 2.1))

    image Olya00 = "locate/home/in_side/2st_floor/olga_room/Olya00.jpg"
    image Olya01 = "locate/home/in_side/2st_floor/olga_room/Olya01.jpg"

    image Olya_sleep = "locate/home/in_side/2st_floor/olga_room/Olya_sleep.jpg"
    image Olya_sleep_up = "locate/home/in_side/2st_floor/olga_room/Olya_sleep_01.png"


    image snow_night_0 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(10, 20), border=150, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(30, 40), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(30, 40), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(25, 40), border=80, start=0, fast=True, distribution="linear"),
        )

    image snow_night_1 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(10, 20), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(30, 40), border=1000, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(25, 40), border=1000, start=0, fast=True, distribution="linear"),
        )

    image snow_night_1_left = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=300, yspeed=(40, 50), xspeed=(-10, -20), border=200, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=100, yspeed=(50, 80), xspeed=(-30, -40), border=200, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=80, yspeed=(60, 90), xspeed=(-30, -40), border=200, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=20, yspeed=(80, 100), xspeed=(-25, -40), border=200, start=0, fast=True, distribution="linear"),
        )

    image snow_night_2 = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(110, 120), border=150, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(130, 140), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(130, 140), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(125, 140), border=80, start=0, fast=True, distribution="linear"),
        )

    image snow_night_2_left = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(120, 110), border=150, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(140, 130), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(140, 130), border=100, start=0, fast=True, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(140, 125), border=80, start=0, fast=True, distribution="linear"),
        )

    image bg road_night snowless = LiveComposite((1920, 1080),
        (0, 0), "locate/street/road_night_001.jpg",
        )

    image bg road_night = LiveComposite((1920, 1080),
        (0, 0), "locate/street/road_night_001.jpg",
        (0, 0), "snow_night_1",
        )

    image bg road_night2 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/road_night_002.jpg",
        (0, 0), "snow_night_1",
        )

    image bg Fox_road1 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_road.jpg",
        (0, 0), "snow_night_1",
        )
    image bg Fox_school = LiveComposite((1920, 1080),
        (0, 0), "locate/school/out_side/Fox_give_hand_fon.jpg",
        (0, 0), "locate/school/out_side/Fox_give_hand.png",
        )


    image bg_Fox_road3:
        parallel:
            im.Blur("locate/street/meet_fox/Fox_road2.jpg", 2.5)
            zoom 0.9
            alpha 0.0
            parallel:
                ease 1.0 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 0.2 xalign 0.7
                ease 0.2 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 1.0 xalign 0.7
                repeat
            parallel:
                ease 0.8 yalign 0.2
                ease 0.8 yalign 0.5
                ease 0.8 yalign 0.3
                ease 0.8 yalign 0.7
                ease 0.2 yalign 0.5
                ease 0.8 yalign 0.2
                repeat
            parallel:
                pause 2.0
                ease 0.2 alpha 0.8
                ease 0.2 alpha 0.0
                repeat
    image bg Fox_road2:
        parallel:
            "locate/street/meet_fox/Fox_road2.jpg"
            zoom 0.9
            parallel:
                ease 1.0 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 0.2 xalign 0.7
                ease 0.2 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 1.0 xalign 0.7
                repeat
            parallel:
                ease 0.8 yalign 0.2
                ease 0.8 yalign 0.5
                ease 0.8 yalign 0.3
                ease 0.8 yalign 0.7
                ease 0.2 yalign 0.5
                ease 0.8 yalign 0.2
                repeat



    image bg vkladish = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/vkladish/vkladush_01.jpg",
        (0, 0), "snow_night_1",
        )

    image vkladish2 = "locate/street/meet_fox/vkladish/vkladush_02.png"

    image bg dog_01 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/dog_01.jpg",
        (0, 0), "snow_night_1",
        )

    image bg_dog_02_1 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/dog_02.jpg",
        (0, 0), "snow_night_1",
        )

    image bg_dog_02 = "locate/street/meet_fox/dog_02.jpg"
    image bg_dog_03 = "locate/street/meet_fox/dog_03.jpg"
    image bg_dog_04 = "locate/street/meet_fox/dog_04.jpg"
    image bg_dog_05 = "locate/street/meet_fox/dog_05.jpg"
    image bg_dog_06 = "locate/street/meet_fox/dog_06.jpg"
    image bg_dog_07 = "locate/street/dog_07.jpg"
    image bg_dog_08 = "locate/school/out_side/dog_08.jpg"
    image bg varishka2 = "locate/street/meet_fox/Varezka2.jpg"



    image bg Fox_give_candy0 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give01.jpg",
        )

    image bg Fox_give_candy1 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give01.jpg",
        )

    image bg Fox_give_candy2 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give02.png",
        )

    image bg Fox_give_candy3 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give01.png",
        (0, 0), "locate/street/meet_fox/Fox_give02.png",
        )

    image bg Fox_give_candy3_light = LiveComposite((1920, 1080),
        (0, 0), im.MatrixColor("locate/street/meet_fox/Fox_give01.png",
            im.matrix.brightness(0.10)),
        (0, 0), im.MatrixColor("locate/street/meet_fox/Fox_give02.png",
            im.matrix.brightness(0.10)),
        )

    image bg Fox_give_candy4 = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give01.jpg",
        (0, 0), "locate/street/meet_fox/Fox_give01.png",
        )

    image bg Fox_give_candy_full = LiveComposite((1920, 1080),
        (0, 0), "locate/street/meet_fox/Fox_give01.jpg",
        (0, 0), "locate/street/meet_fox/Fox_give01.png",
        (0, 0), "locate/street/meet_fox/Fox_give02.png",
        )

    image Fox_give_candy_bg = "locate/street/meet_fox/Fox_give01.jpg"
    image Fox_give_candy_gum = "locate/street/meet_fox/Fox_give02.png"
    image Fox_give_candy_01 = "locate/street/meet_fox/Fox_give01.png"
    image Fox_give_candy_04 = "locate/street/meet_fox/Fox_give04.png"
    image Fox_give_candy_05 = "locate/street/meet_fox/Fox_give05.png"

    $ SetParSpeed(120)

    image gohome01_evning:
        "locate/street/road_to_home/road01.jpg"
        xpos 0
        block:
            linear delay1 xpos 1920
            linear delay1 xpos 3840
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            repeat

    image gohome01_1_evning:
        "locate/street/road_to_home/road01.jpg"
        block:
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            linear delay1 xpos 1920
            linear delay1 xpos 3840
            repeat

    image gohome05:
        "locate/street/road_to_home/road05.png"
        xpos 0
        block:
            linear delay5 xpos 1920
            linear delay5 xpos 3840
            linear delay5 xpos 5760
            linear delay5 xpos 7680
            xpos -7680
            linear delay5 xpos -5760
            linear delay5 xpos -3840
            linear delay5 xpos -1920
            linear delay5 xpos 0
            repeat

    image gohome05_1:
        "locate/street/road_to_home/road05.png"
        block:
            xpos -7680
            linear delay5 xpos -5760
            linear delay5 xpos -3840
            linear delay5 xpos -1920
            linear delay5 xpos 0
            linear delay5 xpos 1920
            linear delay5 xpos 3841
            linear delay5 xpos 5760
            linear delay5 xpos 7680
            repeat

    image gohome05a:
        contains:
            "locate/street/road_to_home/road05.png"
            alpha 0
            pause delay5*8
            alpha 1
            block:
                xpos 0
                linear delay5*4 xpos 7680
                repeat

        contains:
            "locate/street/road_to_home/road05.png"
            alpha 0
            pause delay5*4
            alpha 1
            block:
                xpos -7680
                linear delay5*4 xpos 0
                repeat



    image gohome01:
        "locate/street/road_to_home/road00.jpg"
        xpos 0
        block:
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            repeat

    image gohome01_1:
        "locate/street/road_to_home/road00.jpg"
        block:
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            repeat

    image gohome02:
        "locate/street/road_to_home/road02.png"
        xpos 0
        block:
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            repeat

    image gohome02_1:
        "locate/street/road_to_home/road02.png"
        block:
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            repeat

    image gohome03:
        "locate/street/road_to_home/road03.png"
        xpos 0
        block:
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            repeat

    image gohome03_1:
        "locate/street/road_to_home/road03.png"
        block:
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            repeat

    image gohome04:
        "locate/street/road_to_home/road04.png"
        xpos 0
        block:
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            repeat

    image gohome04_1:
        "locate/street/road_to_home/road04.png"
        block:
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            repeat



    image gohome01_stop:
        "locate/street/road_to_home/road00.jpg"


    image gohome01_1_stop:
        "locate/street/road_to_home/road00.jpg"


    image gohome02_stop:
        "locate/street/road_to_home/road02.png"


    image gohome02_1_stop:
        "locate/street/road_to_home/road02.png"


    image gohome03_stop:
        "locate/street/road_to_home/road03.png"


    image gohome03_1_stop:
        "locate/street/road_to_home/road03.png"


    image gohome04_stop:
        "locate/street/road_to_home/road04.png"


    image gohome04_1_stop:
        "locate/street/road_to_home/road04.png"




    image gohome01_dark_reverse:
        "locate/street/road_to_home(N)/road01.png"
        xpos 0
        block:
            linear delay1 xpos -1920
            linear delay1 xpos -3840
            xpos 3840
            linear delay1 xpos 1920
            linear delay1 xpos 0
            repeat

    image gohome01_1_dark_reverse:
        "locate/street/road_to_home(N)/road01.png"
        block:
            xpos 3840
            linear delay1 xpos 1920
            linear delay1 xpos 0
            linear delay1 xpos -1920
            linear delay1 xpos -3840
            repeat

    image gohome02_dark_reverse:
        "locate/street/road_to_home(N)/road02.png"
        xpos 0
        block:
            linear delay2 xpos -1920
            linear delay2 xpos -3840
            xpos 3840
            linear delay2 xpos 1920
            linear delay2 xpos 0
            repeat

    image gohome02_1_dark_reverse:
        "locate/street/road_to_home(N)/road02.png"
        block:
            xpos 3840
            linear delay2 xpos 1920
            linear delay2 xpos 0
            linear delay2 xpos -1920
            linear delay2 xpos -3840
            repeat

    image gohome03_dark_reverse:
        "locate/street/road_to_home(N)/road03.png"
        xpos 0
        block:
            linear delay3 xpos -1920
            linear delay3 xpos -3840
            xpos 3840
            linear delay3 xpos 1920
            linear delay3 xpos 0
            repeat

    image gohome03_1_dark_reverse:
        "locate/street/road_to_home(N)/road03.png"
        block:
            xpos 3840
            linear delay3 xpos 1920
            linear delay3 xpos 0
            linear delay3 xpos -1920
            linear delay3 xpos -3840
            repeat

    image gohome04_dark_reverse:
        "locate/street/road_to_home(N)/road04.png"
        xpos 0
        block:
            linear delay4 xpos -1920
            linear delay4 xpos -3840
            linear delay4 xpos -5760
            linear delay4 xpos -7680
            xpos 7680
            linear delay4 xpos 5760
            linear delay4 xpos 3840
            linear delay4 xpos 1920
            linear delay4 xpos 0
            repeat

    image gohome04_1_dark_reverse:
        "locate/street/road_to_home(N)/road04.png"
        block:
            xpos 7680
            linear delay4 xpos 5760
            linear delay4 xpos 3840
            linear delay4 xpos 1920
            linear delay4 xpos 0
            linear delay4 xpos -1920
            linear delay4 xpos -3840
            linear delay4 xpos -5760
            linear delay4 xpos -7680
            repeat

    image gohome05_dark_reverse:
        "locate/street/road_to_home(N)/road05.png"
        xpos 0
        block:
            linear delay5 xpos -1920
            linear delay5 xpos -3840
            linear delay5 xpos -5760
            linear delay5 xpos -7680
            xpos 7680
            linear delay5 xpos 5760
            linear delay5 xpos 3840
            linear delay5 xpos 1920
            linear delay5 xpos 0
            repeat

    image gohome05_1_dark_reverse:
        "locate/street/road_to_home(N)/road05.png"
        block:
            xpos 7680
            linear delay5 xpos 5760
            linear delay5 xpos 3840
            linear delay5 xpos 1920
            linear delay5 xpos 0
            linear delay5 xpos -1920
            linear delay5 xpos -3841
            linear delay5 xpos -5760
            linear delay5 xpos -7680
            repeat

    image gohome01_dark_blur_stop = im.Blur("locate/street/road_to_home(N)/road01.png", 1.5)
    image gohome02_dark_blur_stop = im.Blur("locate/street/road_to_home(N)/road02.png", 1.5)
    image gohome03_dark_blur_stop = im.Blur("locate/street/road_to_home(N)/road03.png", 1.5)
    image gohome04_dark_blur_stop = im.Blur("locate/street/road_to_home(N)/road04.png", 1.5)
    image gohome05_dark_blur_stop = im.Blur("locate/street/road_to_home(N)/road05.png", 1.5)


    image gohome01_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road01.png", 1.5)
        xpos 0
        block:
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            repeat

    image gohome01_1_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road01.png", 1.5)
        block:
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            repeat

    image gohome02_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road02.png", 1.5)
        xpos 0
        block:
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            repeat

    image gohome02_1_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road02.png", 1.5)
        block:
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            repeat

    image gohome03_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road03.png", 1.5)
        xpos 0
        block:
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            repeat

    image gohome03_1_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road03.png", 1.5)
        block:
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            repeat

    image gohome04_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road04.png", 1.5)
        xpos 0
        block:
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            repeat

    image gohome04_1_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road04.png", 1.5)
        block:
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            repeat

    image gohome05_dark_blur:
        im.Blur("locate/street/road_to_home(N)/road05.png", 1.5)
        xpos 0
        block:
            linear delay5 xpos 1920
            linear delay5 xpos 3840
            linear delay5 xpos 5760
            linear delay5 xpos 7680-1
            xpos -7680
            linear delay5 xpos -5760
            linear delay5 xpos -3840
            linear delay5 xpos -1920
            linear delay5 xpos 0
            repeat

    image gohome05_1_dark_blur:
        im.Blur("locate/street/road_to_home/road05.png", 1.5)
        block:
            xpos -7680
            linear delay5 xpos -5760
            linear delay5 xpos -3840
            linear delay5 xpos -1920
            linear delay5 xpos 0
            linear delay5 xpos 1920
            linear delay5 xpos 3840
            linear delay5 xpos 5760
            linear delay5 xpos 7680-1
            repeat

    default lowblur_val = 1.2
    image gohome01_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road01.png", lowblur_val)
        xpos 0
        block:
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            repeat

    image gohome01_1_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road01.png", lowblur_val)
        block:
            xpos -3840
            linear delay1 xpos -1920
            linear delay1 xpos 0
            linear delay1 xpos 1920
            linear delay1 xpos 3840-1
            repeat

    image gohome02_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road02.png", lowblur_val)
        xpos 0
        block:
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            repeat

    image gohome02_1_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road02.png", lowblur_val)
        block:
            xpos -3840
            linear delay2 xpos -1920
            linear delay2 xpos 0
            linear delay2 xpos 1920
            linear delay2 xpos 3840-1
            repeat

    image gohome03_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road03.png", lowblur_val)
        xpos 0
        block:
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            repeat

    image gohome03_1_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road03.png", lowblur_val)
        block:
            xpos -3840
            linear delay3 xpos -1920
            linear delay3 xpos 0
            linear delay3 xpos 1920
            linear delay3 xpos 3840-1
            repeat

    image gohome04_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road04.png", lowblur_val)
        xpos 0
        block:
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            repeat

    image gohome04_1_dark_lowblur:
        im.Blur("locate/street/road_to_home(N)/road04.png", lowblur_val)
        block:
            xpos -7680
            linear delay4 xpos -5760
            linear delay4 xpos -3840
            linear delay4 xpos -1920
            linear delay4 xpos 0
            linear delay4 xpos 1920
            linear delay4 xpos 3840
            linear delay4 xpos 5760
            linear delay4 xpos 7680-1
            repeat

    image gohome_dark_stop = LiveComposite((1920, 1080),
        (0,0), "locate/street/road_to_home(N)/road01.png",
        (0,0), "locate/street/road_to_home(N)/road02.png",
        (0,0), "locate/street/road_to_home(N)/road03.png",
        (-900,0), "locate/street/road_to_home(N)/road04.png",
        (-2800,0), "locate/street/road_to_home(N)/road05.png")

    image gohome_day_stop1 = LiveComposite((1920, 1080),
        (0,0), "locate/street/road_to_home/road00.jpg",
        (-100,0), "locate/street/road_to_home/road02.png",
        (-150,0), "locate/street/road_to_home/road03.png",
        (-1200,0), "locate/street/road_to_home/road04.png")

    image gohome_day_stop2 = LiveComposite((1920, 1080),
        (0,0), "locate/street/road_to_home/road00.jpg",
        (-300,0), "locate/street/road_to_home/road02.png",
        (-950,0), "locate/street/road_to_home/road03.png",
        (-1800,0), "locate/street/road_to_home/road04.png")

    image gohome_evning_stop = LiveComposite((1920, 1080),
        (0,0), "locate/street/road_to_home/road01.jpg",
        (0,0), "locate/street/road_to_home/road02.png",
        (0,0), "locate/street/road_to_home/road03.png",
        (0,0), "locate/street/road_to_home/road04.png")

    image bg bridge = "locate/street/bridge.jpg"

    image walking_fox_11_dark:
        "locate/street/walking_fox/road_fox01.jpg"
        xpos 0
        block:
            linear delay1 xpos -1831
            linear delay1 xpos -3662
            xpos 3662
            linear delay1 xpos 1831
            linear delay1 xpos 0
            repeat

    image walking_fox_12_dark:
        "locate/street/walking_fox/road_fox01.jpg"
        block:
            xpos 3662
            linear delay1 xpos 1831
            linear delay1 xpos 0
            linear delay1 xpos -1831
            linear delay1 xpos -3662
            repeat

    image walking_fox_21_dark:
        "locate/street/walking_fox/road_fox02.png"
        xpos 0
        block:
            linear delay3 xpos -1831
            linear delay3 xpos -3662
            xpos 3662
            linear delay3 xpos 1831
            linear delay3 xpos 0
            repeat

    image walking_fox_22_dark:
        "locate/street/walking_fox/road_fox02.png"
        block:
            xpos 3662
            linear delay3 xpos 1831
            linear delay3 xpos 0
            linear delay3 xpos -1831
            linear delay3 xpos -3662
            repeat

    image walking_fox_31_dark:
        "locate/street/walking_fox/road_fox03.png"
        xpos 0
        block:
            linear delay5 xpos -1831
            linear delay5 xpos -3662
            xpos 3662
            linear delay5 xpos 1831
            linear delay5 xpos 0
            repeat

    image walking_fox_32_dark:
        "locate/street/walking_fox/road_fox03.png"
        block:
            xpos 3662
            linear delay5 xpos 1831
            linear delay5 xpos 0
            linear delay5 xpos -1831
            linear delay5 xpos -3662
            repeat

    image ant_walk:
        "locate/street/walking_fox/Ant.png"
        yalign 3.0
        xpos 400
        yoffset 0
        zoom 0.9
        parallel:
            linear 0.5 yoffset 10
            linear 0.5 yoffset 20
            linear 0.5 yoffset 10
            linear 0.5 yoffset 0
            repeat
        parallel:
            linear 3 xpos 420
            linear 3 xpos 440
            linear 3 xpos 450
            linear 3 xpos 440
            repeat

    image fox_walk:
        "locate/street/walking_fox/Fox.png"
        yalign 1.0
        xpos 1300
        yoffset 0
        zoom 0.8
        linear 0.1
        parallel:
            linear 1.0 yoffset 0
            linear 1.0 yoffset 30
            repeat
        parallel:
            linear 2 xpos 1325
            linear 3 xpos 1350
            linear 2 xpos 1325
            linear 3 xpos 1300
            repeat


    image walking_fox_11_day:
        contains:
            "locate/street/walking_fox_day/road_fox01.jpg"
            xpos 0
            linear delay1 xpos 1831
            linear delay1 xpos 3662
            xpos -3662
            linear delay1 xpos -1831
            linear delay1 xpos 0
            repeat

    image walking_fox_12_day:
        contains:
            "locate/street/walking_fox_day/road_fox01.jpg"
            xpos -3662
            linear delay1 xpos -1831
            linear delay1 xpos 0
            xpos 0
            linear delay1 xpos 1831
            linear delay1 xpos 3662
            repeat

    image walking_fox_21_day:
        contains:
            "locate/street/walking_fox_day/road_fox02.png"
            xpos 0
            linear delay3 xpos 1831
            linear delay3 xpos 3662
            xpos -3662
            linear delay3 xpos -1831
            linear delay3 xpos 0
            repeat

    image walking_fox_22_day:
        contains:
            "locate/street/walking_fox_day/road_fox02.png"
            xpos -3662
            linear delay3 xpos -1831
            linear delay3 xpos 0
            xpos 0
            linear delay3 xpos 1831
            linear delay3 xpos 3662
            repeat

    image walking_fox_31_day:
        contains:
            "locate/street/walking_fox_day/road_fox03.png"
            xpos 0
            linear delay5 xpos 1831
            linear delay5 xpos 3662
            xpos -3662
            linear delay5 xpos -1831
            linear delay5 xpos 0
            repeat

    image walking_fox_32_day:
        contains:
            "locate/street/walking_fox_day/road_fox03.png"
            xpos -3662
            linear delay5 xpos -1831
            linear delay5 xpos 0
            xpos 0
            linear delay5 xpos 1831
            linear delay5 xpos 3662
            repeat

    image ant_walk_day:
        "locate/street/walking_fox_day/Ant.png"
        yalign 3.0
        xpos 1400
        yoffset 0
        zoom 0.9
        parallel:
            linear 0.5 yoffset 10
            linear 0.5 yoffset 20
            linear 0.5 yoffset 10
            linear 0.5 yoffset 0
            repeat
        parallel:
            linear 3 xpos 1420
            linear 3 xpos 1440
            linear 3 xpos 1450
            linear 3 xpos 1440
            repeat

    default polina_face_state = 0
    image pol_walk_day_left:

        Composite((445, 882),
            (0,0), "locate/street/walking_fox_day/Polina.png",
            (0,0), ConditionSwitch(
                "polina_face_state == 2", "locate/street/walking_fox_day/Polina_2.png",
                "polina_face_state == 3", "locate/street/walking_fox_day/Polina_3.png",
                "polina_face_state == 4", "locate/street/walking_fox_day/Polina_4.png",
                "polina_face_state == 5", "locate/street/walking_fox_day/Polina_5.png",
                "True", Null(),)
            )
        yalign 1.0
        xpos 900
        yoffset 0
        xoffset 0
        xzoom -1.0
        parallel:
            linear 0.45 yoffset 10
            linear 0.45 yoffset 20
            linear 0.5 yoffset 10
            linear 0.5 yoffset 0
            repeat
        parallel:
            linear 3.1 xoffset 20
            linear 3.0 xoffset 40
            linear 2.9 xoffset 50
            linear 3.1 xoffset 40
            repeat

    default anton_face_polwalk_state = 0
    image ant_walk_day_left:
        Composite((707, 1080),
            (0,0), ConditionSwitch(
                "anton_face_polwalk_state == 2", "locate/street/walking_fox_day/Ant_left3.png",
                "True", "locate/street/walking_fox_day/Ant_left.png"),
            (0,0), ConditionSwitch(
                "anton_face_polwalk_state == 1", "locate/street/walking_fox_day/Ant_left2.png",
                "True", Null())
            )
        yalign 1.0
        xpos 1300
        yoffset 0
        xoffset 0
        parallel:
            linear 0.5 yoffset 10
            linear 0.5 yoffset 20
            linear 0.5 yoffset 10
            linear 0.5 yoffset 0
            repeat
        parallel:
            linear 3 xoffset 20
            linear 3 xoffset 40
            linear 3 xoffset 50
            linear 3 xoffset 40
            repeat

    image ant_walk_day_right:
        "locate/street/walking_fox_day/Ant_right.png"
        yalign 1.0
        xpos 1400
        yoffset 0
        parallel:
            linear 0.5 yoffset 10
            linear 0.5 yoffset 20
            linear 0.5 yoffset 10
            linear 0.5 yoffset 0
            repeat
        parallel:
            linear 3 xpos 1420
            linear 3 xpos 1440
            linear 3 xpos 1450
            linear 3 xpos 1440
            repeat


    image bg_road_wood = "locate/street/road_wood.jpg"
    image bg_forest_fox = LiveComposite((1920, 1080),
        (0, 0), "locate/forest/Fox_fon/Fox_fon.jpg",
        (0, 0), Animation("locate/forest/Fox_fon/001.png", 1.0,
            "locate/forest/Fox_fon/002.png", 0.1,
            "locate/forest/Fox_fon/003.png", 0.1,
            "locate/forest/Fox_fon/004.png", 0.1,
            "locate/forest/Fox_fon/005.png", 1.0,
            "locate/forest/Fox_fon/006.png", 0.1,
            "locate/forest/Fox_fon/007.png", 2.0,
            "locate/forest/Fox_fon/008.png", 0.1,
            "locate/forest/Fox_fon/009.png", 0.1,
            "locate/forest/Fox_fon/010.png", 0.1,
            ))
    image bg_road_wood_dark = im.MatrixColor("locate/street/road_wood.jpg",
            im.matrix.brightness(-0.10))


    image bg storage_in_table0 = "locate/home/in_side/2st_floor/anton_room/table/slot/table6.jpg"
    image bg storage_in_table1 = "locate/home/in_side/2st_floor/anton_room/table/slot/table5.jpg"
    image item_in_table_number = "locate/home/in_side/2st_floor/anton_room/table/slot/table06.png"

    image item_in_table_glove = "locate/home/in_side/2st_floor/anton_room/table/slot/table07.png"
    image item_in_table_record = "locate/home/in_side/2st_floor/anton_room/table/slot/table08.png"

    image bg storage_in_table0_dark = im.MatrixColor("locate/home/in_side/2st_floor/anton_room/table/slot/table6.jpg",
            im.matrix.brightness(-0.30))
    image bg storage_in_table1_dark = im.MatrixColor("locate/home/in_side/2st_floor/anton_room/table/slot/table5.jpg",
            im.matrix.brightness(-0.30))

    image item_in_table_number_dark = im.MatrixColor("locate/home/in_side/2st_floor/anton_room/table/slot/table06.png",
            im.matrix.brightness(-0.30))
    image item_in_table_glove_dark = im.MatrixColor("locate/home/in_side/2st_floor/anton_room/table/slot/table07.png",
            im.matrix.brightness(-0.30))
    image item_in_table_record_dark = im.MatrixColor("locate/home/in_side/2st_floor/anton_room/table/slot/table08.png",
            im.matrix.brightness(-0.30))


    image bg parta = "locate/school/in_side/Parta.jpg"



    image bg school_night = "locate/school/out_side/school00.jpg"

    image bg school_day = "locate/school/out_side/school.jpg"
    image bg school_day_dog = LiveComposite((4000, 2250),
        (0,0), "bg school_day",
        (0,0), "locate/school/out_side/dog.png"
        )

    image school_coner_01 = "locate/school/out_side/school_coner/school_coner_01.png"
    image bg school_corner_day = "locate/school/out_side/school_coner/school_coner_00.jpg"
    image bg school_corner_day1 = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        
        )
    image bg school_corner_day1_no_squirrel = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        (0,0), "locate/school/out_side/school_coner/no_squirrel.png"
        )
    image bg school_corner_day2 = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        (0,0), "locate/school/out_side/school_coner/school_coner_02.png"
        )
    image bg school_corner_day2_no_squirrel = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        (0,0), "locate/school/out_side/school_coner/school_coner_02.png",
        (0,0), "locate/school/out_side/school_coner/no_squirrel.png"
        )
    image bg school_corner_day3 = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        
        (0,0), "locate/school/out_side/school_coner/school_coner_02.png"
        )
    image bg school_corner_day3_no_squirrel = LiveComposite((2426, 1080),
        (0,0), "bg school_corner_day",
        
        (0,0), "locate/school/out_side/school_coner/school_coner_02.png",
        (0,0), "locate/school/out_side/school_coner/no_squirrel.png"
        )

    image fox_boo = Animation("locate/school/out_side/school_coner/001.png", 0.1, "locate/school/out_side/school_coner/002.png", 0.1, "locate/school/out_side/school_coner/003.png", 0.1, "locate/school/out_side/school_coner/002.png", 0.1)
    image fox_boo_snow = Animation("locate/school/out_side/school_coner/01.png", 0.1, "locate/school/out_side/school_coner/02.png", 0.1, "locate/school/out_side/school_coner/03.png", 0.1, Null(), 0.9)

    image bg school_night_maninblack0 = LiveComposite((1920, 1080),
        (0,0), "bg school_night",
        (0,0), "locate/school/out_side/school01.png",
        (0,0), "locate/school/out_side/school02.png")

    image bg school_night_maninblack1 = LiveComposite((1920, 1080),
        (0,0), "bg school_night",
        (0,0), "locate/school/out_side/school01.png",
        (0,0), "locate/school/out_side/school02.png",
        (0,0), "locate/school/out_side/school03.png")

    image bg school_night_maninblack2 = LiveComposite((1920, 1080),
        (0,0), "bg school_night",
        (0,0), "locate/school/out_side/school01.png",
        (0,0), "locate/school/out_side/school02.png",
        (0,0), "locate/school/out_side/school04.png")

    image man in_black1 = "locate/school/out_side/school06.png"
    image man in_black2 = "locate/school/out_side/school05.png"

    image d2_man_in_black 1 = "locate/school/out_side/school06.png"
    image d2_man_in_black 2 = "locate/school/out_side/school05.png"

    image d2_man_in_black 2_1 = "sprite/Visiter_1.png"
    image d2_man_in_black 2_2 = "sprite/Visiter_2.png"

    image man in_black1_heavyblur = im.Blur("locate/school/out_side/school06.png", 1.2)
    image man in_black3 = im.Blur("locate/street/walkaway/witness_01.png", 1.5)

    image man in_black0 = "sprite/Svedetel_01.png"
    image man in_black0_2 = "sprite/Svedetel_02.png"

    image man in_black1 = "sprite/Visiter_1.png"
    image man in_black1_2 = "sprite/Visiter_2.png"

    image bg school_corner_day_onshow:
        contains:
            "bg school_corner_day3"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "bg school_day"
            yalign 0.8 xoffset -2000+960
            parallel:
                ease 8.0 xoffset 0+2426-1960
            parallel:
                alpha 1.0
                pause 4.5
                ease 1.5 alpha 0.0
                pause 1.0

    image bg school_corner_day_onshow_snowpile:
        contains:
            "bg school_corner_day3"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "school_coner_01"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "bg school_day"
            yalign 0.8 xoffset -2000+960
            parallel:
                ease 8.0 xoffset 0+2426-1960
            parallel:
                alpha 1.0
                pause 4.5
                ease 1.5 alpha 0.0
                pause 1.0

    image bg school_corner_day_onshow_snowpile_myth:
        contains:
            "bg school_corner_day3"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "school_coner_01"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "day2_myth"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "bg school_day"
            yalign 0.8 xoffset -2000+960
            parallel:
                ease 8.0 xoffset 0+2426-1960
            parallel:
                alpha 1.0
                pause 4.5
                ease 1.5 alpha 0.0
                pause 1.0

    image bg school_corner_day3_onshow:
        contains:
            "bg school_corner_day1"
            xoffset -2000+960-2426+1960
            yalign 0.5
            ease 8.0 xoffset 0
        contains:
            "bg school_day"
            yalign 0.8 xoffset -2000+960
            parallel:
                ease 8.0 xoffset 0+2426-1960
            parallel:
                alpha 1.0
                pause 4.5
                ease 1.5 alpha 0.0
                pause 1.0

    image bg school_corner_day_onhide:
        contains:
            "bg school_corner_day"
            xoffset 0
            yalign 0.5
            ease 8.0 xoffset -2000+960-2426+1960
        contains:
            "bg school_day"
            yalign 0.8 xoffset 0+2426-1960
            parallel:
                ease 8.0 xoffset -2000+960
            parallel:
                alpha 0.0
                pause 2.5
                ease 1.5 alpha 1.0
                pause 3.0

    image bg school_corner_day_onhide_myth:
        contains:
            "bg school_corner_day"
            xoffset 0
            yalign 0.5
            ease 8.0 xoffset -2000+960-2426+1960
        contains:
            "day2_myth"
            xoffset 0
            yalign 0.5
            ease 8.0 xoffset -2000+960-2426+1960
        contains:
            "bg school_day"
            yalign 0.8 xoffset 0+2426-1960
            parallel:
                ease 8.0 xoffset -2000+960
            parallel:
                alpha 0.0
                pause 2.5
                ease 1.5 alpha 1.0
                pause 3.0


    image bg_koridorchic_mor = "locate/school/in_side/school_hall/koridorchic_mor.jpg"
    image bg_koridorchic_day = "locate/school/in_side/school_hall/koridorchic_Day.jpg"
    image bg_koridor_notice_mor = "locate/school/in_side/school_hall/koridorchic_mor.png"
    image bg_koridor_notice_day = "locate/school/in_side/school_hall/koridorchic_Day.png"
    image st_01 = "locate/school/in_side/school_hall/st_01.png"
    image st_02 = "locate/school/in_side/school_hall/st_02.png"
    image st_03 = "locate/school/in_side/school_hall/st_03.png"
    image airplane_school = 'locate/school/in_side/school_hall/airplane.png'
    image bucket_school = 'locate/school/in_side/school_hall/bucket.png'
    image shoes_school = 'locate/school/in_side/school_hall/shoes.png'
    image polina_door = 'locate/school/in_side/school_hall/001.png'
    image fox_window = 'locate/school/in_side/school_hall/002.png'

    image bg_kate_attacked:
        contains:
            "locate/school/in_side/kate_attacked/Fon.jpg"
        contains:
            "locate/school/in_side/kate_attacked/sh.png"
            xpos -300 alpha 0.5
            linear 10 xpos 0 alpha 1.0
        contains:
            "locate/school/in_side/kate_attacked/01.png"
            xpos -600
            linear 10 xpos 0

    transform hpunch2:
        xoffset 0
        pause 9.8
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset 0

    image bg hall_day = LiveComposite(
        (4329,1080),
        (0,0), 'bg_koridorchic_day',
        (0,0), "bg_koridor_notice_day",
        (0,0), 'airplane_school',
        (0,0), 'shoes_school',
        (0,0), 'bucket_school',
        (0,0), 'polina_door',
        (0,0), 'fox_window'
    )

    image bg hall_day_before_choice = LiveComposite(
        (4329,1080),
        (0,0), 'bg_koridorchic_day',
        (0,0), "bg_koridor_notice_day",
        (0,0), 'airplane_school',
        (0,0), 'shoes_school',
        (0,0), 'bucket_school'
    )

    image bg_hall_day_choice = LiveComposite(
        (4329,1080),
        (0,0), 'polina_door',
        (0,0), 'fox_window'
    )

    image bg koridorchic_mor_full = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "st_03",
        (0,0), "st_02",
        (0,0), "st_01",
        )
    image bg koridorchic_mor_open_1 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "st_03",
        (0,0), "st_02",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",
        )
    image bg koridorchic_mor_open_2 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "st_03",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",
        )
    image bg koridorchic_mor_open_3 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",
        )
    image bg koridorchic_mor_open_4 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "st_03",
        (0,0), "st_02",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",

        )
    image bg koridorchic_mor_open_5 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",
        )
    image bg koridorchic_mor_full_open = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "st_03",
        (0,0), "st_02",
        (0,0), "st_01",
        (0,0), "locate/school/in_side/school_hall/koridorchic_Door.png",
        )


    image bg_propalrebenok1 = "locate/school/in_side/propalrebenok.jpg"
    image bg_propalrebenok2 = "locate/school/in_side/propalrebenok02.jpg"

    image bg_raspisanie = LiveComposite((2844, 1600),
        (0,0), "locate/school/in_side/raspisanie.jpg",
        (0,0), "locate/school/in_side/raspisanie_but.png")


    image men_00:
        "locate/school/in_side/raspisanie/men_00.png"

    image men_01:
        "locate/school/in_side/raspisanie/men_01.png"

    image men_02:
        "locate/school/in_side/raspisanie/men_02.png"

    image men_03:
        "locate/school/in_side/raspisanie/men_03.png"

    image men_04:
        "locate/school/in_side/raspisanie/men_04.png"

    image men_05:
        "locate/school/in_side/raspisanie/men_05.png"

    image bg_white = "#ffffff"
    image Polina = "images/locate/school/in_side/Polina_00.png"
    image Polina1 = "images/locate/school/in_side/Polina_01.png"

    image bg_transition_01:
        "locate/school/in_side/transition_01.jpg"
        alpha 1.0
        xalign 0.5
        yalign 1.0
        ease 10.0 yalign 0.335

    image transition_01 = "locate/school/in_side/transition_01.jpg"
    image transition_02 = "locate/school/in_side/transition_02.png"
    image transition_03 = "locate/school/in_side/transition_03.png"
    image transition_04 = "locate/school/in_side/transition_04.png"
    image transition_05 = "locate/school/in_side/transition_05.png"

    image bg_bell = "locate/school/in_side/bell.jpg"

    image eyes_Sema = Animation(Null(), 5.00, "locate/school/in_side/semen/Sema_04.png", 0.10, "locate/school/in_side/semen/Sema_05.png", 0.10, "locate/school/in_side/semen/Sema_04.png", 0.10, Null(), 10)
    image eyes_Sema2 = Animation(Null(), 5.00, "locate/school/in_side/semen/Sema_eyes_01.png", 0.10, "locate/school/in_side/semen/Sema_eyes_02.png", 0.10, "locate/school/in_side/semen/Sema_eyes_01.png", 0.10, Null(), 10)
    image bg_shcool_hall_down = "locate/school/in_side/semen/Sema_00.jpg"

    image sema upper_01 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Sema_01.png",
        (0,0), "eyes_Sema",
        )
    image sema upper_02 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Sema_02.png",
        (0,0), "eyes_Sema",
        )
    image sema upper_03 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Sema_03.png",
        (0,0), "eyes_Sema",
        )
    image sema upper_04 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Sema_06.png",
        (0,0), "eyes_Sema",
        )

    image sema punch_01:
        parallel:
            "locate/school/in_side/semen/Sem001.jpg"
            0.05,
            "locate/school/in_side/semen/Sem002.jpg"
            0.05,
            "locate/school/in_side/semen/Sem003.jpg"
            0.05,
            "locate/school/in_side/semen/Sem004.jpg"
            0.05,
            "locate/school/in_side/semen/Sem005.jpg"
            0.05,
            "locate/school/in_side/semen/Sem004.jpg"
            0.05,
            "locate/school/in_side/semen/Sem003.jpg"
            0.05,
            "locate/school/in_side/semen/Sem002.jpg"
            0.05,
            "locate/school/in_side/semen/Sem001.jpg"

        parallel:
            yoffset 0
            linear 0.05 yoffset 9
            linear 0.1 yoffset 0
            linear 0.1 yoffset 9
            linear 0.1 yoffset 0

    image sema fight = Animation("locate/school/in_side/semen/Fight_00.jpg", 0.085,
        "locate/school/in_side/semen/Fight_01.jpg", 0.085,
        "locate/school/in_side/semen/Fight_02.jpg", 0.085,
        "locate/school/in_side/semen/Fight_03.jpg", 0.085,
        "locate/school/in_side/semen/Fight_04.jpg", 0.085,
        "locate/school/in_side/semen/Fight_05.jpg", 0.085,
        "locate/school/in_side/semen/Fight_06.jpg", 0.085,
        "locate/school/in_side/semen/Fight_07.jpg", 0.085,
        "locate/school/in_side/semen/Fight_08.jpg", 0.085,
        "locate/school/in_side/semen/Fight_09.jpg", 0.085,
        "locate/school/in_side/semen/Fight_010.jpg", 0.085,
        "locate/school/in_side/semen/Fight_011.jpg", 0.085,
        "locate/school/in_side/semen/Fight_012.jpg", 0.085,
        "locate/school/in_side/semen/Fight_013.jpg", 0.085,
        "locate/school/in_side/semen/Fight_014.jpg", 0.085,
        "locate/school/in_side/semen/Fight_015.jpg", 0.085,
        "locate/school/in_side/semen/Fight_016.jpg", 0.085,
        "locate/school/in_side/semen/Fight_017.jpg", 0.085,
        "locate/school/in_side/semen/Fight_018.jpg", 0.085,
        "locate/school/in_side/semen/Fight_019.jpg", 0.085,
        "locate/school/in_side/semen/Fight_020.jpg", 0.085,
        "locate/school/in_side/semen/Fight_021.jpg", 0.085,
        "locate/school/in_side/semen/Fight_022.jpg", 0.085,
        "locate/school/in_side/semen/Fight_023.jpg", 0.085,
        "locate/school/in_side/semen/Fight_024.jpg", 0.085,
        "locate/school/in_side/semen/Fight_025.jpg", 0.085,
        "locate/school/in_side/semen/Fight_026.jpg", 0.085,
        "locate/school/in_side/semen/Fight_027.jpg", 0.085,
        "locate/school/in_side/semen/Fight_028.jpg", 2.00,
        )

    image sema upper_05 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Fight_028.jpg",
        (0,0), "eyes_Sema2",
        )

    image sema upper_06 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/semen/Fight_029.jpg",
        (0,0), "eyes_Sema2",
        )

    image sema upper_07 = "locate/school/in_side/semen/Sema_0.png"

    image sema_friend1 = "locate/school/in_side/semen/Sema_frend01.png"
    image sema_friend2 = "locate/school/in_side/semen/Sema_frend02.png"


    transform for_sema_friend1:
        xpos -768
        ypos 1080
        alpha 0.0
        linear 0.5 xpos 0 ypos 1080-1560 alpha 1.0
    transform for_sema_friend2:
        xpos 1980
        ypos 1080
        alpha 0.0
        linear 0.5 xpos 1980-643 ypos 1080-1488 alpha 1.0

    image bg_class_for_child1:
        contains:
            "locate/school/in_side/ahaha/klass_00.jpg"
            ypos 0
            xpos 0
            linear delay1 xpos -1920
            linear delay1 xpos -3841
            xpos 3841
            linear delay1 xpos 1921
            linear delay1 xpos 0
            repeat

    image bg_class_for_child2:
        contains:
            "locate/school/in_side/ahaha/klass_00.jpg"
            ypos 0
            xpos 3841
            linear delay1 xpos 1921
            linear delay1 xpos 0
            xpos 0
            linear delay1 xpos -1920
            linear delay1 xpos -3841
            repeat


    image children_in_class1 = "locate/school/in_side/ahaha/child/klass_01.png"
    image children_in_class2 = "locate/school/in_side/ahaha/child/klass_02.png"
    image children_in_class3 = "locate/school/in_side/ahaha/child/klass_03.png"
    image children_in_class4 = "locate/school/in_side/ahaha/child/klass_04.png"
    image children_in_class5 = "locate/school/in_side/ahaha/child/klass_05.png"
    image children_in_class6 = "locate/school/in_side/ahaha/child/klass_06.png"
    image children_in_class7 = "locate/school/in_side/ahaha/child/klass_07.png"
    image children_in_class8 = "locate/school/in_side/ahaha/child/klass_08.png"
    image children_in_class9 = "locate/school/in_side/ahaha/child/klass_09.png"
    image children_in_class1_1 = "locate/school/in_side/ahaha/child/klass_01.png"
    image children_in_class2_1 = "locate/school/in_side/ahaha/child/klass_02.png"
    image children_in_class3_1 = "locate/school/in_side/ahaha/child/klass_03.png"
    image children_in_class4_1 = "locate/school/in_side/ahaha/child/klass_04.png"
    image children_in_class5_1 = "locate/school/in_side/ahaha/child/klass_05.png"
    image children_in_class6_1 = "locate/school/in_side/ahaha/child/klass_06.png"
    image children_in_class7_1 = "locate/school/in_side/ahaha/child/klass_07.png"
    image children_in_class8_1 = "locate/school/in_side/ahaha/child/klass_08.png"
    image children_in_class9_1 = "locate/school/in_side/ahaha/child/klass_09.png"

    image children_in_class:
        contains:
            "children_in_class5"
            ypos 353
            parallel:
                xpos 0
                linear delay3 xpos -1920
                linear delay3 xpos -3841
                xpos 3841
                linear delay3 xpos 1921
                linear delay3 xpos 0
                repeat
            parallel:
                linear 0.21 ypos 353
                linear 0.20 ypos 359
                repeat
        contains:
            "children_in_class5_1"
            ypos 353
            parallel:
                xpos 3841
                linear delay3 xpos 1921
                linear delay3 xpos 0
                xpos 0
                linear delay3 xpos -1920
                linear delay3 xpos -3841
                repeat
            parallel:
                linear 0.22 ypos 353
                linear 0.20 ypos 361
                repeat
        contains:
            "children_in_class6"
            ypos 228
            parallel:
                xpos 0+900
                linear delay3 xpos -1920+900
                linear delay3 xpos -3841+900
                xpos 3841+900
                linear delay3 xpos 1921+900
                linear delay3 xpos 0+900
                repeat
            parallel:
                linear 0.21 ypos 228
                linear 0.20 ypos 235
                repeat
        contains:
            "children_in_class6_1"
            ypos 228
            parallel:
                xpos 3841+900
                linear delay3 xpos 1921+900
                linear delay3 xpos 0+900
                xpos 0+900
                linear delay3 xpos -1920+900
                linear delay3 xpos -3841+900
                repeat
            parallel:
                linear 0.22 ypos 228
                linear 0.20 ypos 237
                repeat
        contains:
            "children_in_class7"
            ypos 311
            parallel:
                xpos 0+900+685
                linear delay3 xpos -1920+900+685
                linear delay3 xpos -3841+900+685
                xpos 3841+900+685
                linear delay3 xpos 1921+900+685
                linear delay3 xpos 0+900+685
                repeat
            parallel:
                linear 0.21 ypos 311
                linear 0.20 ypos 321
                repeat
        contains:
            "children_in_class7_1"
            ypos 311
            parallel:
                xpos 3841+900+685
                linear delay3 xpos 1921+900+685
                linear delay3 xpos 0+900+685
                xpos 0+900+685
                linear delay3 xpos -1920+900+685
                linear delay3 xpos -3841+900+685
                repeat
            parallel:
                linear 0.22 ypos 311
                linear 0.20 ypos 320
                repeat
        contains:
            "children_in_class8"
            ypos 263
            parallel:
                xpos 0+900+685+605
                linear delay3 xpos -1920+900+685+605
                linear delay3 xpos -3841+900+685+605
                xpos 3841+900+685+605
                linear delay3 xpos 1921+900+685+605
                linear delay3 xpos 0+900+685+605
                repeat
            parallel:
                linear 0.21 ypos 263
                linear 0.20 ypos 270
                repeat
        contains:
            "children_in_class8_1"
            ypos 263
            parallel:
                xpos 3841+900+685+605
                linear delay3 xpos 1921+900+685+605
                linear delay3 xpos 0+900+685+605
                xpos 0+900+685+605
                linear delay3 xpos -1920+900+685+605
                linear delay3 xpos -3841+900+685+605
                repeat
            parallel:
                linear 0.22 ypos 263
                linear 0.20 ypos 273
                repeat
        contains:
            "children_in_class9"
            ypos 313
            parallel:
                xpos 0+900+685+605+820
                linear delay3 xpos -1920+900+685+605+820
                linear delay3 xpos -3841+900+685+605+820
                xpos 3841+900+685+605+820
                linear delay3 xpos 1921+900+685+605+820
                linear delay3 xpos 0+900+685+605+820
                repeat
            parallel:
                linear 0.21 ypos 313
                linear 0.20 ypos 323
                repeat
        contains:
            "children_in_class9_1"
            ypos 313
            parallel:
                xpos 3841+900+685+605+820
                linear delay3 xpos 1921+900+685+605+820
                linear delay3 xpos 0+900+685+605+820
                xpos 0+900+685+605+820
                linear delay3 xpos -1920+900+685+605+820
                linear delay3 xpos -3841+900+685+605+820
                repeat
            parallel:
                linear 0.22 ypos 313
                linear 0.20 ypos 320
                repeat
        contains:
            "children_in_class1"
            ypos 49
            parallel:
                xpos 0
                linear delay4 xpos -1920
                linear delay4 xpos -3841
                xpos 3841
                linear delay4 xpos 1921
                linear delay4 xpos 0
                repeat
            parallel:
                linear 0.21 ypos 49
                linear 0.20 ypos 65
                repeat
        contains:
            "children_in_class1_1"
            ypos 49
            parallel:
                xpos 3841
                linear delay4 xpos 1921
                linear delay4 xpos 0
                xpos 0
                linear delay4 xpos -1920
                linear delay4 xpos -3841
                repeat
            parallel:
                linear 0.22 ypos 49
                linear 0.20 ypos 65
                repeat
        contains:
            "children_in_class2"
            ypos 0
            parallel:
                xpos 0+1010
                linear delay4 xpos -1920+1010
                linear delay4 xpos -3841+1010
                xpos 3841+1010
                linear delay4 xpos 1921+1010
                linear delay4 xpos 0+1010
                repeat
            parallel:
                linear 0.20 ypos 0
                linear 0.23 ypos 10
                repeat
        contains:
            "children_in_class2_1"
            ypos 0
            parallel:
                xpos 3841+1010
                linear delay4 xpos 1921+1010
                linear delay4 xpos 0+1010
                xpos 0+1010
                linear delay4 xpos -1920+1010
                linear delay4 xpos -3841+1010
                repeat
            parallel:
                linear 0.20 ypos 0
                linear 0.19 ypos 10
                repeat
        contains:
            "children_in_class3"
            ypos 50
            parallel:
                xpos 0+1010+960
                linear delay4 xpos -1920+1010+960
                linear delay4 xpos -3841+1010+960
                xpos 3841+1010+960
                linear delay4 xpos 1921+1010+960
                linear delay4 xpos 0+1010+960
                repeat
            parallel:
                linear 0.20 ypos 50
                linear 0.23 ypos 60
                repeat
        contains:
            "children_in_class3_1"
            ypos 50
            parallel:
                xpos 3841+1010+960
                linear delay4 xpos 1921+1010+960
                linear delay4 xpos 0+1010+960
                xpos 0+1010+960
                linear delay4 xpos -1920+1010+960
                linear delay4 xpos -3841+1010+960
                repeat
            parallel:
                linear 0.21 ypos 50
                linear 0.22 ypos 60
                repeat
        contains:
            "children_in_class4"
            ypos 143
            parallel:
                xpos 0+1010+960+1010
                linear delay4 xpos -1920+1010+960+1010
                linear delay4 xpos -3841+1010+960+1010
                xpos 3841+1010+960+1010
                linear delay4 xpos 1921+1010+960+1010
                linear delay4 xpos 0+1010+960+1010
                repeat
            parallel:
                linear 0.22 ypos 143
                linear 0.20 ypos 153
                repeat
        contains:
            "children_in_class4_1"
            ypos 143
            parallel:
                xpos 3841+1010+960+1010
                linear delay4 xpos 1921+1010+960+1010
                linear delay4 xpos 0+1010+960+1010
                xpos 0+1010+960+1010
                linear delay4 xpos -1920+1010+960+1010
                linear delay4 xpos -3841+1010+960+1010
                repeat
            parallel:
                linear 0.19 ypos 143
                linear 0.21 ypos 153
                repeat

    image children_in_class_rem_1:
        "children_in_class1"
        parallel:
            linear 0.20 yoffset 16
            linear 0.21 yoffset 0
            repeat
    image children_in_class_rem_2:
        "children_in_class2"
        parallel:
            linear 0.20 yoffset 0
            linear 0.23 yoffset 10
            repeat
    image children_in_class_rem_3:
        "children_in_class3"
        parallel:
            linear 0.23 yoffset 10
            linear 0.20 yoffset 0
            repeat
    image children_in_class_rem_4:
        "children_in_class4"
        parallel:
            linear 0.20 yoffset 10
            linear 0.22 yoffset 0
            repeat
    image children_in_class_rem_5:
        "children_in_class5"
        parallel:
            linear 0.20 yoffset 6
            linear 0.21 yoffset 0
            repeat
    image children_in_class_rem_6:
        "children_in_class6"
        parallel:
            linear 0.20 yoffset 7
            linear 0.21 yoffset 0
            repeat
    image children_in_class_rem_7:
        "children_in_class7"
        parallel:
            linear 0.20 yoffset 10
            linear 0.21 yoffset 0
            repeat
    image children_in_class_rem_8:
        "children_in_class8"
        parallel:
            linear 0.20 yoffset 7
            linear 0.21 yoffset 0
            repeat
    image children_in_class_rem_9:
        "children_in_class9"
        parallel:
            linear 0.20 yoffset 10
            linear 0.21 yoffset 0
            repeat

    image children_in_class_rem = LiveComposite((3840, 1080),
        (0+900+685+605+820, 313), "children_in_class_rem_9",
        (0+900+685+605,     263), "children_in_class_rem_8",
        (0+900+685,         311), "children_in_class_rem_7",
        (0+900,             228), "children_in_class_rem_6",
        (0,                 353), "children_in_class_rem_5",)
    image children_in_class_rem2 = LiveComposite((3840, 1080),
        (0+1010+960+1010, 143), "children_in_class_rem_4",
        (0+1010+960,       50), "children_in_class_rem_3",
        (0+1010,            0), "children_in_class_rem_2",
        (0,                49), "children_in_class_rem_1",)


    image bg_polina_look:
        contains:
            "locate/school/in_side/polina_look/Polina_look.jpg"
        contains:
            Animation(Null(), 2.0, "locate/school/in_side/polina_look/Polina_look01.png", 2.50, "locate/school/in_side/polina_look/Polina_look02.png", 0.10, "locate/school/in_side/polina_look/Polina_look03.png", 0.10, "locate/school/in_side/polina_look/Polina_look02.png", 0.10, "locate/school/in_side/polina_look/Polina_look01.png", 10)
            alpha 0.0
            pause 2.0
            linear 0.5 alpha 1.0

    image bg_teacher 01 01 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An001.png",
        (0,0), Animation("locate/school/in_side/teacher/An001/01.png", 4.10, "locate/school/in_side/teacher/An001/02.png", 0.10, "locate/school/in_side/teacher/An001/03.png", 0.10, "locate/school/in_side/teacher/An001/02.png", 0.10, "locate/school/in_side/teacher/An001/01.png", 6),
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        )

    image bg_teacher 02 01 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An001.png",
        (0,0), Animation("locate/school/in_side/teacher/An001/01.png", 4.10, "locate/school/in_side/teacher/An001/02.png", 0.10, "locate/school/in_side/teacher/An001/03.png", 0.10, "locate/school/in_side/teacher/An001/02.png", 0.10, "locate/school/in_side/teacher/An001/01.png", 6),
        (0,0), "locate/school/in_side/teacher/teacer2.png",
        )

    image bg_teacher 01 02 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An002.png",
        (0,0), Animation("locate/school/in_side/teacher/An002/01.png", 4.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/01.png", 6),
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        )

    image An002_aside:
        contains:
            Animation("locate/school/in_side/teacher/An002/01.png", 4.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/05.png", 0.10, "locate/school/in_side/teacher/An002/06.png", 6),
            alpha 1.0
            pause 6
            linear 0.1 alpha 0.0
        contains:
            Animation("locate/school/in_side/teacher/An002/06.png", 4.10, "locate/school/in_side/teacher/An002/05.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/05.png", 0.10, "locate/school/in_side/teacher/An002/06.png", 6),
            alpha 0.0
            pause 6
            linear 0.1 alpha 1.0

    image An002_ahead:
        contains:
            Animation("locate/school/in_side/teacher/An002/06.png", 4.10, "locate/school/in_side/teacher/An002/05.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/01.png", 6),
            alpha 1.0
            pause 6
            linear 0.1 alpha 0.0
        contains:
            Animation("locate/school/in_side/teacher/An002/01.png", 4.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/01.png", 6),
            alpha 0.0
            pause 6
            linear 0.1 alpha 1.0

    image bg_teacher 01 03 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An002.png",
        (0,0), "An002_aside",
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        )

    image bg_teacher 02 02 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An002.png",
        (0,0), Animation("locate/school/in_side/teacher/An002/01.png", 4.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/03.png", 0.10, "locate/school/in_side/teacher/An002/02.png", 0.10, "locate/school/in_side/teacher/An002/01.png", 6),
        (0,0), "locate/school/in_side/teacher/teacer2.png",
        )

    image bg_teacher 00 02 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/An002.png",
        (0,0), "An002_ahead",
        (0,0), "locate/school/in_side/teacher/teacer2.png",
        )

    image bg_classroom base = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/classroom001.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom006.png",
        )
    image bg_classroom base2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom006.png",
        )
    image bg_classroom base 2_1 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 2_1_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 2_1_no_chair_no_teach = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 3 1 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 3 2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 3 3 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 4 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 32 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )

    image bg_classroom base 3 1_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 3 1_no_chair2_ = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem2",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 3 1_no_chair_2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 2_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 3 3_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 4_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 5_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 3 32_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 33_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 3 33_no_chair_no_teach = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 4 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_3 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_4 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 4_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_00_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        )
    image bg_classroom base 4_01_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        )
    image bg_classroom base 4_2_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_3_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 4_4_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 5 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_3 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_4 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_4_2 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 5_5 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_6 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_6_Teach = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_7 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 5_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base 5_2_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_3_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_4_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_4_2_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )
    image bg_classroom base 5_4_3_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        )
    image bg_classroom base 5_5_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_2.png",
        (0,0), "locate/school/in_side/classroom/Kate_2.png",
        (0,0), "locate/school/in_side/classroom/Bysh_2.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_6_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_6_Teach_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_2.png",
        )
    image bg_classroom base 5_7_no_chair = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "empty_desk_sem",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/ment2.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        )

    image bg_classroom base mini_game = LiveComposite((1920, 1080),
        (0,0), "case_bg",
        (960,0), "guard_idle",
        (-1688,0), "teah_win",
        (0,0), "case_fg",
        )





    image bg_classroom ant = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/classroom001.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom006.png",
        )

    image bg_classroom ant_teacher = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/classroom001.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom006.png"
        )
    image bg_classroom ant_teacher_bag = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/classroom004.png",
        (0,0), "locate/school/in_side/classroom/classroom001.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom006.png"
        )
    image bg_classroom sem_back = LiveComposite((3911, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "locate/school/in_side/classroom/classroom002.png",
        (0,0), "locate/school/in_side/classroom/Polina_1.png",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        (0,0), "locate/school/in_side/classroom/Bysh_1.png",
        (0,0), "locate/school/in_side/classroom/Rom_1.png",
        (0,0), "locate/school/in_side/classroom/classroom003.png",
        )



    image bg_anton_on_board = "locate/school/in_side/pered.jpg"

    image bg_Sem1 = "locate/school/in_side/Sem_1.jpg"
    image bg_Sem2 = "locate/school/in_side/Sem_2.jpg"
    image bg_Sem3 = "locate/school/in_side/Sem_3.jpg"

    image bg_notebook:
        "locate/school/in_side/notebook.jpg"
        yalign 0.5835
        xalign 0.5
        zoom 1.00
        linear 20 rotate -15




image fox_snowball_forest:
    contains:
        "locate/forest/Fox_fon/Fox_fon.jpg"
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

image fox_snowball:
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

image fox_snowball_corner:
    contains:
        "bg school_corner_day"
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
image fox_snowball_corner_splash:
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


image bg_road_wood_dog1 = "locate/street/dog_07.jpg"
image bg_road_wood_dog2 = "locate/street/meet_fox/dog_06.jpg"
image bg_road_wood_no_dog = "locate/street/dog_bully/dog_08.jpg"

image bg_dog_bully:
    contains:
        "locate/street/dog_bully/dog_08.jpg"
    contains:
        "locate/street/dog_bully/dogee_10.png"
        xpos 200
        ypos 0
        linear 5 xpos 600 ypos -300
    contains:
        "locate/street/dog_bully/dogee_09.png"
        xpos 0
        ypos 0
        linear 5 xpos 100 ypos -100
    contains:
        "locate/street/dog_bully/dogee_11.png"
        xpos 900 ypos 760 alpha 1.0
        linear 5 xpos 1500 alpha 0.1


image bg gop_wood_1:
    "locate/street/gopstop/fon.jpg"

image bg gop_wood_1 blur:
    im.Blur("locate/street/gopstop/fon.jpg", 2.5)

image bg gop_wood_2:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton.png"

image bg gop_wood_3:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton2.png"

image bg gop_wood_4:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton_02.png"

image romka 01 01 01:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_01.png")

image romka 01 01 01 out:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_01.png")
        alpha 1
        linear 1 alpha 0

image romka 01 01 02:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_02.png")

image romka 01 01 04:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_04.png")

image romka 01 02 06:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_02.png",
        (0,0), "locate/street/gopstop/Ro_06.png")

image romka 01 03 02:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_02.png")

image romka 01 03 04:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_04.png")

image romka byasha blur:
    contains:
        im.Blur("locate/street/gopstop/Romka_full.png", 1.5)

image romka 01 03 05:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_05.png")

image baysha 01 02 01:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_01.png")

image baysha 01 03 02:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_03.png",
        (0,0), "locate/street/gopstop/Baysh_02.png")

image baysha 01 02 03:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_03.png")

image baysha 01 02 04:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_04.png")

image baysha 01 02 05:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_05.png")

image baysha 01 03 04:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_03.png",
        (0,0), "locate/street/gopstop/Baysh_04.png")

image sema 01:
    contains:
        "locate/street/gopstop/Sema_01.png"

image sema 02:
    contains:
        "locate/street/gopstop/Sema_02.png"

image sema 07:
    contains:
        "locate/street/gopstop/Sema_07.png"

image sema 10:
    contains:
        "locate/street/gopstop/Sema_10.png"

image sema 10 blur:
    contains:
        im.Blur("locate/street/gopstop/Sema_10.png", 1.5)

image sema 11:
    contains:
        "locate/street/gopstop/Sema_11.png"

image sema 12:
    contains:
        "locate/street/gopstop/Sema_12.png"

image sema 12_13:
    contains:
        Animation("locate/street/gopstop/Sema_12.png",
        0.30, "locate/street/gopstop/Sema_13.png",2)

image sema 13:
    contains:
        "locate/street/gopstop/Sema_13.png"

image sema 14:
    contains:
        "locate/street/gopstop/Sema_14.png"

image sema 15:
    contains:
        "locate/street/gopstop/Sema_15.png"

image sema 16:
    contains:
        "locate/street/gopstop/Sema_16.png"

image sema 17:
    contains:
        "locate/street/gopstop/Sema_17.png"

image sema 18:
    contains:
        "locate/street/gopstop/Sema_18.png"

image sema 20:
    contains:
        "locate/street/gopstop/Sema_20.png"

image sema 21:
    contains:
        "locate/street/gopstop/Sema_21.png"

image sema 24:
    contains:
        "locate/street/gopstop/Sema_24.png"


image bg_gop_wood_1_SemAnx:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_01.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_01.png")
    contains:
        "locate/street/gopstop/Sema_13.png"


image bg_gop_wood_1_SemAnx_Baysha_eyes:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_01.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_03.png",
        (0,0), "locate/street/gopstop/Baysh_02.png")
    contains:
        "locate/street/gopstop/Sema_13.png"


image bg_gop_wood_1_SemAnxAnim:
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_01.png",
        (0,0), "locate/street/gopstop/Ro_01.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_01.png")
    contains:
        Animation("locate/street/gopstop/Sema_12.png",
        0.30, "locate/street/gopstop/Sema_13.png",2)

image bg_gop_wood_ring_blick:
    Animation(Null(), 1.0,
        "locate/street/gopstop/BL_01.png", 0.1,
        "locate/street/gopstop/BL_02.png", 0.1,
        "locate/street/gopstop/BL_03.png", 0.1,
        "locate/street/gopstop/BL_04.png", 0.1,
        Null(), 5.0)
    alpha 1.0
    pause 2.0
    linear 0.1 alpha 0.0

image anton_zay_02:
    "locate/street/gopstop/Anton2.png"


image bg_gop_wood_sema_punch1:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton.png"
        linear 0.2 xpos -1000 ypos 100
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_05.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_01.png")
    contains:
        "locate/street/gopstop/Sema_18.png"

image bg_gop_wood_sema_punch2:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_05.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_04.png")
    contains:
        "locate/street/gopstop/Sema_02.png"

image bg_gop_wood_sema_punch1_2:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton_02.png"
        linear 0.2 xpos -1000 ypos 100
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_05.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_02.png",
        (0,0), "locate/street/gopstop/Baysh_01.png")
    contains:
        "locate/street/gopstop/Sema_18.png"

image bg_gop_wood_MASK:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        "locate/street/gopstop/Anton.png"
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_06.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_03.png",
        (0,0), "locate/street/gopstop/Baysh_02.png")
    contains:
        "locate/street/gopstop/Sema_21.png"
image bg_gop_wood_MASK_choice:
    contains:
        "locate/street/gopstop/fon.jpg"
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Romka_01.png",
        (0,0), "locate/street/gopstop/Rom_03.png",
        (0,0), "locate/street/gopstop/Ro_06.png")
    contains:
        LiveComposite((2299, 1080),
        (0,0), "locate/street/gopstop/Baysha_01.png",
        (0,0), "locate/street/gopstop/Bay_03.png",
        (0,0), "locate/street/gopstop/Baysh_02.png")

image bg_lisa001 = "locate/street/fox_in_forest/Lisa_001.jpg"
image bg_lisa002 = "locate/street/fox_in_forest/Lisa_002.jpg"
image bg_lisa003 = "locate/street/fox_in_forest/Lisa_003.jpg"
image bg_lisa004 = "locate/street/fox_in_forest/Lisa_004.jpg"
image bg_lisa005 = "locate/street/fox_in_forest/Lisa_005.jpg"
image bg_lisa006 = "locate/street/fox_in_forest/Lisa_006.jpg"
image bg_lisa007 = "locate/street/fox_in_forest/Lisa_007.jpg"

image bg_lisa_smeh = "locate/street/fox_in_forest/1/001.jpg"
image bg_lisa_smeh1 = "locate/street/fox_in_forest/03/smeh_06.jpg"

image bg_lisa_anim:
    "locate/street/fox_in_forest/Lisa_001.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_002.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_003.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_004.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_005.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_006.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_007.jpg"
    pause 0.10
    "locate/street/fox_in_forest/Lisa_001.jpg"

image bg_lisa_anim_smeh:
    "locate/street/fox_in_forest/1/001.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/002.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/003.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/004.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/005.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/006.jpg"

image bg_lisa_anim_smeh_reverse:
    "locate/street/fox_in_forest/1/006.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/005.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/004.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/003.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/002.jpg"
    pause 0.05
    "locate/street/fox_in_forest/1/001.jpg"

image bg_lisa_anim_smeh1:
    "locate/street/fox_in_forest/03/smeh_01.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_02.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_03.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_04.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_05.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_06.jpg"

image bg_lisa_anim_smeh1_reverse:
    "locate/street/fox_in_forest/03/smeh_06.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_05.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_04.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_03.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_02.jpg"
    pause 0.07
    "locate/street/fox_in_forest/03/smeh_01.jpg"

image bg_lisa_anim_smeh1_1:
    "locate/street/fox_in_forest/03/7.png" with Dissolve(0.3, alpha=False)
    pause 0.07
    "locate/street/fox_in_forest/03/8.png" with Dissolve(0.3, alpha=False)
    pause 0.07
    "locate/street/fox_in_forest/03/9.png" with Dissolve(0.3, alpha=False)
    pause 0.07
    "locate/street/fox_in_forest/03/10.png" with Dissolve(0.3, alpha=False)

image bg_lisa_stand = LiveComposite((1920, 1080),
    (0, 0), "locate/street/fox_in_forest/Lisa_001.jpg",
    (0, 0), "locate/street/fox_in_forest/Lisa.png")

image bg_lisa_lying = LiveComposite((1920, 1080),
    (0, 0), "locate/street/fox_in_forest/Lisa_001.jpg",
    (0, 0), "locate/street/fox_in_forest/Lisa2.png")

image bg_gop_noga1 = "locate/street/gopstop/Noga.jpg"
image bg_gop_noga2 = "locate/street/gopstop/Noga_2.jpg"

image bg_gop_noga_rage:
    "bg_gop_noga2"
    zoom 1.0 xalign 0.5 yalign 0.5 alpha 0.0
    ease 0.4 zoom 1.5 xalign 0.5 yalign 0.5 alpha 1.0
    ease 0.9 zoom 1.0 xalign 0.5 yalign 0.5 alpha 0.0

image bg_anton_relax1 = "locate/street/Anton_full1.jpg"
image bg_anton_relax2 = "locate/street/Anton_full2.jpg"

image bg_anton_relax_rage:
    contains:
        "bg_anton_relax1"
    contains:
        "bg_anton_relax2"
        pause 0.5
        zoom 1.0 xalign 0.5 yalign 0.5 alpha 0.0
        ease 1.0 alpha 1.0
        ease 1.0 alpha 0.0
        pause 4.5
        repeat

image Polina blur = im.Blur("locate/forest/Polina_03.png", 1.5)

image bg_backpack_crash:
    contains:
        "locate/home/out_side/handblood_fon.jpg"

    contains:
        "locate/home/out_side/backpack/bag_03.png"
        xpos 0
        ypos -350
        linear 10 ypos -150
        linear 10 ypos -350

    contains:
        "locate/home/out_side/backpack/bag_02.png"
        xpos 0
        ypos 0
        linear 10 ypos 1100

    contains:
        "locate/home/out_side/backpack/bag_01.png"
        xpos 0
        ypos -240
        linear 10 ypos 1100

    contains:
        "locate/home/out_side/backpack/bag_04.png"
        xpos 0
        ypos -350
        linear 10 ypos -150
        linear 10 ypos -350


image anton_battle_romka 1 = "locate/street/anton_battle/scene_01/Romka.png"
image anton_battle_byasha 1 = "locate/street/anton_battle/scene_01/Byasha.png"
image anton_battle_bg_2 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
            )

image anton_battle_anton 2 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/A_00.png",
            (0,0), Animation(
                "locate/street/anton_battle/scene_02/eyesA_03.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_02.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_01.png", 5,
                "locate/street/anton_battle/scene_02/eyesA_02.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_03.png", 0.10,
                ),
            (0,0), "locate/street/anton_battle/scene_02/mouthA.png",
            )

image anton_battle_anton 2_open = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/A_00.png",
            (0,0), Animation(
                "locate/street/anton_battle/scene_02/eyesA_03.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_02.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_01.png", 5,
                "locate/street/anton_battle/scene_02/eyesA_02.png", 0.10,
                "locate/street/anton_battle/scene_02/eyesA_03.png", 0.10,
                ),
            (0,0), "locate/street/anton_battle/scene_02/mouthA_02.png",
            )

image anton_battle_motion_2 = "locate/street/anton_battle/scene_02/motion.png"

image anton_battle_motion_4 = "locate/street/anton_battle/scene_04/motion02.png"

image anton_battle_anton 4 = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_001.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouth_A03.png",
        )

image anton_battle_anton 4_bad = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_001.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouthA_03.png",
        )

image anton_battle_anton 4_bad_open = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_001.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_002.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_003.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouth_A04.png",
        )

image anton_battle_anton 4_evil = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_04.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouthA_03.png",
        )

image anton_battle_anton 4_evil_open = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_04.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouth_A04.png",
        )

image anton_battle_anton 4_evil_grid = LiveComposite((1920, 1080),
        (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
        (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_04.png", 5,
            "locate/street/anton_battle/scene_04/eyesA_05.png", 0.10,
            "locate/street/anton_battle/scene_04/eyesA_06.png", 0.10,
            ),
        (0,0), "locate/street/anton_battle/scene_04/mouthA_04.png",
        )


image bg_anton_battle_wood_1:
    contains:
        "locate/street/road_wood.jpg"
        xpos -225
        linear 1 xpos -75
        linear 5 xpos 0

    contains:
        "locate/street/anton_battle/scene_01/Romka.png"
        xpos 1000
        linear 1 xpos 150
        linear 5 xpos 0

    contains:
        "locate/street/anton_battle/scene_01/Byasha.png"
        xpos 1000
        linear 1 xpos 200
        linear 5 xpos 0

    contains:
        "sprite/Semen/Serious/m_day_W/1_body/00.png"
        xpos 1000
        linear 1 xpos 250
        linear 5 xpos -70

    contains:
        LiveComposite((1920, 1080),
            (0, 500), SnowBlossom("interface/main_meny/partikl_002.png", count=120, yspeed=(-20, 80), xspeed=(-190, -280), border=-100, start=0, fast=True, distribution="linear"),
            (0, 700), SnowBlossom("effect/snow/s011.png", count=70, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear"))

    contains:
        "locate/street/anton_battle/scene_01/Anton.png"
        xpos -1000
        linear 1 xpos -200
        linear 5 xpos 0


image bg_anton_battle_wood_2:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
            )

        xpos -225
        linear 1 xpos -75
        linear 5 xpos 0

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/A_00.png",
            (0,0), Animation(
            "locate/street/anton_battle/scene_02/eyesA_03.png",
            0.10, "locate/street/anton_battle/scene_02/eyesA_02.png",
            0.10, "locate/street/anton_battle/scene_02/eyesA_01.png",5),
            (0,0), "locate/street/anton_battle/scene_02/mouthA.png",
            )
        xpos 1000
        linear 1 xpos 200
        linear 5 xpos 0

    contains:
        LiveComposite((1920, 1080),
            (0, 500), SnowBlossom("interface/main_meny/partikl_002.png", count=120, yspeed=(-20, 80), xspeed=(-190, -280), border=-100, start=0, fast=True, distribution="linear"),
            (0, 700), SnowBlossom("effect/snow/s011.png", count=70, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear"))

    contains:
        "locate/street/anton_battle/scene_02/motion.png"
        xpos -2000
        linear 0.5 xpos 2000


image bg_anton_battle_wood_2_1 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
            (0,0), "locate/street/anton_battle/scene_02/A_00.png",
            (0,0), Animation(
            "locate/street/anton_battle/scene_02/eyesA_03.png",
            0.10, "locate/street/anton_battle/scene_02/eyesA_02.png",
            0.10, "locate/street/anton_battle/scene_02/eyesA_01.png",5),
            (0,0), "locate/street/anton_battle/scene_02/mouthA_02.png",
            )


image bg_anton_battle_wood_3:
    contains:
        "locate/street/road_wood.jpg"
        xpos -225
        linear 1 xpos -75
        linear 5 xpos 0

    contains:
        LiveComposite((1920, 1080),
            (0,0), "sprite/Romka/Angry/m_day_winter/1_body/01.png",
            (0,0), Animation("sprite/Romka/Angry/m_day_winter/2_eyes/angry/ahead/03.png",
            0.10, "sprite/Romka/Angry/m_day_winter/2_eyes/angry/ahead/02.png",
            0.10, "sprite/Romka/Angry/m_day_winter/2_eyes/angry/ahead/01.png",11),
            (0,0), "sprite/Romka/Angry/m_day_winter/3_mouth/01.png",
            )
        xpos 1000
        ypos 100
        zoom 1.3
        linear 1 xpos 400
        linear 5 xpos 200
    contains:
        LiveComposite((1920, 1080),
            (0,0), "sprite/Byasha/Normal/m_day_winter/1_body/01.png",
            (0,0), Animation("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/03.png",
            0.10, "sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/02.png",
            0.10, "sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/01.png",7),
            (0,0), "sprite/Byasha/Normal/m_day_winter/3_mouth/01.png",
            )
        xpos 1000
        ypos 100
        zoom 1.3
        linear 1 xpos -600
        linear 5 xpos -850
    contains:
        LiveComposite((1920, 1080),
            (0,0), "sprite/Semen/Serious/b_day_W/1_body/00.png",
            (0,0), Animation("sprite/Semen/Serious/b_day_W/2_eyes/evil/ahead/03.png",
            0.10, "sprite/Semen/Serious/b_day_W/2_eyes/evil/ahead/02.png",
            0.10, "sprite/Semen/Serious/b_day_W/2_eyes/evil/ahead/01.png",10),
            (0,0), "sprite/Semen/Serious/b_day_W/3_mouth/01.png",
            )
        xpos 1000
        ypos 100
        linear 1 xpos 100
        linear 5 xpos -100
    contains:
        LiveComposite((1920, 1080),
            (0, 500), SnowBlossom("interface/main_meny/partikl_002.png", count=120, yspeed=(-20, 80), xspeed=(-190, -280), border=-100, start=0, fast=True, distribution="linear"),
            (0, 700), SnowBlossom("effect/snow/s011.png", count=70, yspeed=(-20, 60), xspeed=(-320, -350), border=0, start=0, fast=True, distribution="linear"))
    contains:
        "locate/street/anton_battle/scene_03/Anton_05.png"
        xpos -1000
        linear 1 xpos -200
        linear 5 xpos 0


image bg_anton_battle_wood_4:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
            )

        xpos -225
        linear 1 xpos -75
        linear 5 xpos 0

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
            (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_003.png",
            0.10, "locate/street/anton_battle/scene_04/eyesA_002.png",
            0.10, "locate/street/anton_battle/scene_04/eyesA_001.png",5),
            (0,0), "locate/street/anton_battle/scene_04/mouth_A03.png",
            )

        xpos 1000
        linear 1 xpos 200
        LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
            (0,0), Animation(
            "locate/street/anton_battle/scene_04/eyesA_003.png",
            0.10, "locate/street/anton_battle/scene_04/eyesA_002.png",
            0.10, "locate/street/anton_battle/scene_04/eyesA_001.png",5),
            (0,0), Animation(
            "locate/street/anton_battle/scene_04/mouth_A04.png",
            5.30,"locate/street/anton_battle/scene_04/mouth_A03.png"))
        linear 5 xpos 0

    contains:
        "locate/street/anton_battle/scene_04/motion02.png"
        xpos -2000
        linear 0.5 xpos 2000


image bg_anton_battle_wood_4_mouth_close = LiveComposite((1920, 1080),
    (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
    (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
    (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
    (0,0), Animation(
    "locate/street/anton_battle/scene_04/eyesA_06.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_05.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_04.png",5),
    (0,0), "locate/street/anton_battle/scene_04/mouthA_03.png",)


image bg_anton_battle_wood_4_mouth_open = LiveComposite((1920, 1080),
    (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
    (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
    (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
    (0,0), Animation(
    "locate/street/anton_battle/scene_04/eyesA_06.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_05.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_04.png",5),
    (0,0), "locate/street/anton_battle/scene_04/mouthA_04.png")


image bg_anton_battle_wood_4_mouth_open_grin = LiveComposite((1920, 1080),
    (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
    (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
    (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
    (0,0), Animation(
    "locate/street/anton_battle/scene_04/eyesA_06.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_05.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_04.png",5),
    (0,0), "locate/street/anton_battle/scene_04/mouth_A04.png")


image bg_anton_battle_wood_4_mouth_smile = LiveComposite((1920, 1080),
    (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
    (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
    (0,0), "locate/street/anton_battle/scene_04/Anton_00.png",
    (0,0), Animation(
    "locate/street/anton_battle/scene_04/eyesA_003.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_002.png",
    0.10, "locate/street/anton_battle/scene_04/eyesA_001.png",5),
    (0,0), "locate/street/anton_battle/scene_04/mouthA_05.png",)


image bg_anton_punch_semen = LiveComposite((1920, 1080),
    (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
    (0,0),"locate/street/anton_battle/scene_02/fon_02.png",
    (0,0), Animation(
    "locate/street/punch/p_001.jpg",
    0.10, "locate/street/punch/p_002.jpg",
    0.10, "locate/street/punch/p_003.jpg",
    0.10, "locate/street/punch/p_004.jpg",
    0.10, "locate/street/punch/p_005.jpg",
    0.10, "locate/street/punch/p_006.jpg",
    0.10, "locate/street/punch/p_007.jpg",
    0.10, "locate/street/punch/p_008.jpg",
    0.10, "locate/street/punch/p_009.jpg",
    0.10, "locate/street/punch/p_010.jpg",
    0.10, "locate/street/punch/p_011.jpg",
    0.10, "locate/street/punch/p_012.jpg",
    0.10, "locate/street/punch/p_013.jpg",
    0.10, "locate/street/punch/p_014.jpg",
    0.10, "locate/street/punch/p_015.jpg",
    0.10, "locate/street/punch/p_016.jpg", ))


image bg_sema_battle_appear:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos -2198
        linear 3.0 xpos 0
        linear 3.0 xpos 2197
        repeat

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 0
        linear 3.0 xpos 2197
        xpos -2198
        linear 3.0 xpos 0
        repeat

    contains:
        "snowman_snow_fast"

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/000.png"
            )
        xpos 1000
        ypos 50
        linear 0.5 xpos 200
        linear 2.5 xpos 0

    contains:
        SnowBlossom("effect/snow/s006.png", count=10,  yspeed=(10, 50), xspeed=(600, 650), border=50, start=0, fast=True, distribution="linear", horizontal = True)


image bg_sema_battle_disappear:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos -2198
        linear 3.0 xpos 0
        linear 3.0 xpos 2197
        repeat

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 0
        linear 3.0 xpos 2197
        xpos -2198
        linear 3.0 xpos 0
        repeat

    contains:
        "snowman_snow_fast"

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/000.png"
            )

        xpos 0
        ypos 50
        linear 1 xpos -10
        linear 0.5 xpos -2000

image bg_sema_battle_appear2:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 2197
        linear 3.0 xpos 0
        linear 3.0 xpos -2198
        repeat

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 0
        linear 3.0 xpos -2198
        xpos 2197
        linear 3.0 xpos 0
        repeat

    contains:
        "snowman_snow_fast_revers"

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/01.png"
            )
        xpos -1000
        ypos 50
        linear 0.5 xpos -200
        linear 2.5 xpos 0



    contains:
        SnowBlossom("effect/snow/s006.png", count=10,  yspeed=(10, 50), xspeed=(-600, -650), border=50, start=0, fast=True, distribution="linear", horizontal = True)


image bg_sema_battle_disappear2:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 2197
        linear 3.0 xpos 0
        linear 3.0 xpos -2198
        repeat

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 0
        linear 3.0 xpos -2198
        xpos 2197
        linear 3.0 xpos 0
        repeat

    contains:
        "snowman_snow_fast_revers"

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/01.png"
            )

        xpos 0
        ypos 50
        linear 1 xpos 10
        linear 0.5 xpos 2000



image bg_sema_kakahi = "locate/street/Sema_battle/Sema_kakhi.jpg"


image bg_sema_battle_revenge:
    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 2197
        linear 3.0 xpos 0
        linear 3.0 xpos -2198
        repeat

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/fon.jpg"
            )
        xpos 0
        linear 3.0 xpos -2198
        xpos 2197
        linear 3.0 xpos 0
        repeat

    contains:
        "snowman_snow_fast_revers"

    contains:
        LiveComposite((1920, 1080),
            (0,0), "locate/street/Sema_battle/001.png"
            )
        xpos -1000
        ypos 50
        linear 0.5 xpos -200
        linear 2.5 xpos 0

    contains:
        SnowBlossom("effect/snow/s006.png", count=10,  yspeed=(10, 50), xspeed=(-600, -650), border=50, start=0, fast=True, distribution="linear", horizontal = True)

image bg_sema attack_fon = "locate/street/Sema_battle/Draka_fon.jpg"

image bg_sema attack_fon blur = im.Blur("locate/street/Sema_battle/Draka_fon.jpg", 1.5)

image bg_sema attack_fon_day = im.MatrixColor(im.MatrixColor("locate/street/Sema_battle/Draka_fon.jpg", im.matrix.brightness(0.08)), im.matrix.contrast(1.08))

image sema attack_blurred = "locate/street/Sema_battle/Sem_01.png"

image Draka_fon2 = "locate/street/Sema_battle/Draka_fon2.jpg"
image Draka_fon3 = "locate/street/Sema_battle/Draka_fon3.jpg"
image Draka_fon4 = "locate/street/Sema_battle/Draka_fon4.jpg"

image Cup:
    contains:
        "locate/home/in_side/1st_floor/kitchen/Cup.jpg"
    contains:
        im.Blur("locate/home/in_side/1st_floor/kitchen/Cup.jpg", 3.0)

        ease 1.0 alpha 0.0
        ease 1.0 alpha 0.5
        ease 2.0 alpha 1.0

        repeat

image bg_sema_attack:
    contains:
        "locate/street/Sema_battle/Draka_fon.jpg"
    contains:
        "locate/street/Sema_battle/Sem_01.png"

image bg_sema_attack_day:
    contains:
        im.MatrixColor(im.MatrixColor("locate/street/Sema_battle/Draka_fon.jpg", im.matrix.brightness(0.08)), im.matrix.contrast(1.08))
    contains:
        im.MatrixColor(im.MatrixColor("locate/street/Sema_battle/Sem_01.png", im.matrix.brightness(0.08)), im.matrix.contrast(1.08))

image bg_sema attack_fon_dark:
    contains:
        "locate/street/Sema_battle/Draka_fon.jpg"
    contains:
        im.MatrixColor("locate/street/Sema_battle/Draka_fon.jpg", im.matrix.brightness(-0.08))
        alpha 0.0
        ease 10.0 alpha 1.0

image sema attack_blurred_dark:
    contains:
        "locate/street/Sema_battle/Sem_01.png"
    contains:
        im.MatrixColor("locate/street/Sema_battle/Sem_01.png", im.matrix.brightness(-0.08))
        alpha 0.0
        ease 10.0 alpha 1.0


image bg_sema_attack_juctice:
    contains:
        "locate/street/Sema_battle/Draka_fon.jpg"




    contains:
        "locate/street/Sema_battle/Sem_02.png"


image bg_sema_attack_juctice_punish:
    contains:
        "locate/street/Sema_battle/Draka_fon.jpg"




    contains:
        Animation(
            "locate/street/Sema_battle/G_01.png",
            0.10, "locate/street/Sema_battle/G_02.png",
            0.10, "locate/street/Sema_battle/G_03.png",
            0.10, "locate/street/Sema_battle/G_04.png",
            0.10, "locate/street/Sema_battle/G_05.png",
            0.10, "locate/street/Sema_battle/G_06.png",
            0.10, "locate/street/Sema_battle/G_07.png",
            0.10, "locate/street/Sema_battle/G_08.png",
            0.10, "locate/street/Sema_battle/G_09.png",
            0.10, "locate/street/Sema_battle/G_10.png",
            0.10, "locate/street/Sema_battle/G_11.png",
            0.10, "locate/street/Sema_battle/G_12.png",
            0.10, "locate/street/Sema_battle/G_13.png",
            0.10, "locate/street/Sema_battle/G_14.png",
            0.10, "locate/street/Sema_battle/G_15.png",0.10)

image bg_sema_attack_threat:
    contains:
        "bg_sema attack_fon_dark"
    contains:
        "locate/street/Sema_battle/Gopi_00.png"
    contains:
        "locate/street/Sema_battle/Gopi.png"
        alpha 0.0
        ease 10.0 alpha 1.0

image polina_lisa_bg = "#000000"
image polina_lisa_02 = "locate/school/in_side/Polina_Lisa/Polina_02.png"
image polina_lisa_03 = "locate/school/in_side/Polina_Lisa/Polina_03.png"
image polina_lisa_04 = "locate/school/in_side/Polina_Lisa/Lisa_03.png"
image polina_lisa_05 = "locate/school/in_side/Polina_Lisa/Lisa_02.png"
image polina_lisa_06 = "locate/school/in_side/Polina_Lisa/Lisa_01.png"

image showB1 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_01.png", count=250,  yspeed=(-100, -150), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
image showB2 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=200,  yspeed=(-150, -200), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
image showB3 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_03.png", count=100,  yspeed=(-200, -250), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
image showB4 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_04.png", count=20,  yspeed=(-300, -400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
image showB5 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_05.png", count=5,   yspeed=(-400, -500), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")

image showB4_1 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_04.png", count=20,  yspeed=(-300, -400), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")
image showB5_1 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_05.png", count=5,   yspeed=(-400, -500), xspeed=(-10, 10), border=50, start=0, fast=True, distribution="linear")

image showB6 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_06.png", count=15,   yspeed=(-700, -750), xspeed=(-10, 10), border=450, start=0, fast=True, distribution="linear")
image showB7 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_07.png", count=15,   yspeed=(-750, -800), xspeed=(-10, 10), border=450, start=0, fast=True, distribution="linear")
image showB8 = SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_08.png", count=10,   yspeed=(-800, -850), xspeed=(-10, 10), border=450, start=0, fast=True, distribution="linear")

image showB = LiveComposite((1920, 1080),
            (0,0), "showB1",
            (0,0), "showB2",
            (0,0), "showB3",
            (0,0), "showB4",
            (0,0), "showB5",
            )
image showC = LiveComposite((1920, 1080),
            (0,0), "showB4_1",
            (0,0), "showB5_1",
            )

image showD = LiveComposite((1920, 1080),
            (0,0), "showB6",
            (0,0), "showB7",
            (0,0), "showB8",
            )

image showE = LiveComposite((1920, 1080),
            (0,0), "showB6",
            (0,0), "showB7",
            (0,0), "showB8",
            )


image table_art_01 = "locate/home/in_side/2st_floor/anton_room/table/table001.jpg"
image table_art_02 = "locate/home/in_side/2st_floor/anton_room/table/table002.jpg"
image table_art_03 = "locate/home/in_side/2st_floor/anton_room/table/table003.jpg"
image table_art_04 = "locate/home/in_side/2st_floor/anton_room/table/table004.jpg"
image table_art_05 = "locate/home/in_side/2st_floor/anton_room/table/table005.jpg"
image table_art_06 = "locate/home/in_side/2st_floor/anton_room/table/table006.jpg"
image table_art_07 = "locate/home/in_side/2st_floor/anton_room/table/table007.jpg"
image table_art_07_1 = "locate/home/in_side/2st_floor/anton_room/table/table007_1.jpg"
image table_art_08 = "locate/home/in_side/2st_floor/anton_room/table/table008.jpg"
image table_art_09 = "locate/home/in_side/2st_floor/anton_room/table/table009.jpg"
image table_art_10 = "locate/home/in_side/2st_floor/anton_room/table/table010.jpg"
image table_art_11 = "locate/home/in_side/2st_floor/anton_room/table/table011.jpg"
image table_art_12 = "locate/home/in_side/2st_floor/anton_room/table/table012.jpg"
image table_art_13 = "locate/home/in_side/2st_floor/anton_room/table/table013.jpg"
image table_art_14 = "locate/home/in_side/2st_floor/anton_room/table/table014.jpg"

image miganie_t4_t5 = Animation(
    "table_art_04", 2.35,
    "table_art_05", 0.28,
    "table_art_04", 0.09,
    "table_art_05", 0.09,
    "table_art_04", 0.05,
    "table_art_05", 0.03,
    "table_art_04", 1.55,
    "table_art_05", 0.10,
    "table_art_04", 3.05,
    "table_art_05", 0.16,
    "table_art_04", 5.25,
    "table_art_05", 0.04)

image miganie_t6_t7 = Animation(
    "table_art_04", 0.85,
    "table_art_06", 0.05,
    "table_art_07_1", 0.10,
    "table_art_05", 0.09,
    "table_art_04", 1.35,
    "table_art_06", 0.10,
    "table_art_07_1", 0.10,
    "table_art_05", 0.04,
    "table_art_04", 0.20,
    "table_art_06", 0.09,
    "table_art_07_1", 0.7,
    "table_art_05", 0.04,
    "table_art_04", 0.05,
    "table_art_06", 0.09,
    "table_art_07_1", 10.0)

image scare_01:
    "locate/forest/scary/Scary_fon.jpg"
    subpixel True
    xalign 1.0
    yalign 0.5
    ease 30.0 zoom 1.2 xoffset -216 yoffset -216

image scare_02:
    "locate/forest/scary/Scary_A.png"
    subpixel True
    ease 30.0 xoffset -500

image scare_00 = LiveComposite((1920, 1080),
            (0,0), "scare_01",
            (0,0), "scare_02",
            )

image rom_knife_00 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0), "locate/street/rom_knife/R_knife00.png",
            )

image rom_knife_00_1 = LiveComposite((1920, 1080),
            (0,0), im.MatrixColor("locate/street/anton_battle/scene_02/fon_01.jpg",
                im.matrix.brightness(-0.20)),
            (0,0), "locate/street/rom_knife/R_knife00.png",
            )

image rom_knife_00_1_blur = LiveComposite((1920, 1080),
            (0,0), im.Blur(im.MatrixColor("locate/street/anton_battle/scene_02/fon_01.jpg",
                im.matrix.brightness(-0.15)), 3.5),
            (0,0), im.Blur("locate/street/rom_knife/R_knife00.png", 3.5),
            )


image rom_knife_01 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0), "locate/street/rom_knife/R_knife00.png",
            (0,0), "locate/street/rom_knife/R_knife09.png",
            )

image rom_knife_02 = LiveComposite((1920, 1080),
            (0,0), "locate/street/anton_battle/scene_02/fon_01.jpg",
            (0,0), "locate/street/rom_knife/R_knife00.png",
            (0,0), "locate/street/rom_knife/R_knife09.png",
            (0,0), "locate/street/rom_knife/R_knife10.png",
            )

image rom_knife_03 = Animation(
            "locate/street/rom_knife/R_knife01.png", 0.1,
            "locate/street/rom_knife/R_knife02.png", 0.1,
            "locate/street/rom_knife/R_knife03.png", 0.1,
            "locate/street/rom_knife/R_knife04.png", 0.1,
            "locate/street/rom_knife/R_knife05.png", 0.1,
            "locate/street/rom_knife/R_knife06.png", 0.1,
            "locate/street/rom_knife/R_knife08.png", 0.1,
            "locate/street/rom_knife/R_knife09.png", 2.00)

image roma_figth_bg = "locate/street/gopstop/roma_fight/Ro_fon.jpg"

image roma_figth_bg_chao:
    contains:
        "locate/street/gopstop/roma_fight/Ro_fon.jpg"
    contains:
        "locate/street/gopstop/roma_fight/Ro_fon_3.jpg"
        alpha 0.0 xalign 0.5 yalign 0.5
        pause 0.1
        linear 1.7 alpha 0.5 xoffset 30
        linear 0.8 alpha 0.0 xoffset 30
        alpha 0.0 xoffset 0
    contains:
        "locate/street/gopstop/roma_fight/Ro_fon_3.jpg"
        alpha 0.0 xalign 0.5 yalign 0.5
        pause 0.1
        linear 1.7 alpha 0.5 xoffset -30
        linear 0.8 alpha 0.0 xoffset -30
        alpha 0.0 xoffset 0


image hand_0:
    "locate/street/gopstop/roma_fight/hand.png"
    block:
        linear 1.0 xoffset -5 yoffset 10
        linear 1.0 xoffset 2 yoffset 5
        linear 1.0 xoffset 0 yoffset 0
        linear 1.0 xoffset -2 yoffset 5
        linear 1.0 xoffset 5 yoffset 0
        linear 1.0 xoffset 0 yoffset 5
        repeat

image hand_1:
    "locate/street/gopstop/roma_fight/hand.png"
    xpos 200
    linear 0.1 xoffset 40
    linear 0.1 xoffset 0

image hand_2:
    "locate/street/gopstop/roma_fight/hand.png"
    parallel:
        linear 1.0 xoffset -5 yoffset 10
        linear 1.0 xoffset 2 yoffset 5
        linear 1.0 xoffset 0 yoffset 0
        linear 1.0 xoffset -2 yoffset 5
        linear 1.0 xoffset 5 yoffset 0
        linear 1.0 xoffset 0 yoffset 5
        repeat
    parallel:
        xpos 1920 ypos 1080
        linear 4.0 xpos 600 ypos 150

image pol_sem_bya:
    "locate/street/gopstop/roma_fight/Pol.png"
    block:
        pause 5.0
        linear 0.2 xoffset -5 yoffset 0
        linear 0.2 xoffset 2 yoffset 5
        linear 0.2 xoffset 0 yoffset 0
        linear 0.2 xoffset -2 yoffset 5
        linear 0.2 xoffset 5 yoffset -2
        linear 0.2 xoffset 0 yoffset 0
        repeat

image pol_sem_bya2:
    "locate/street/gopstop/roma_fight/Pol.png"
    zoom 1.0
    linear 8.0 zoom 0.6 xoffset 350 yoffset 920

image roma_figth_0 = LiveComposite((1920, 1080),
            (0,0), "roma_figth_bg",
            (600,150), "hand_0"
            )

image roma_figth_01 = LiveComposite((1920, 1080),
            (0,0), "roma_figth_bg",
            (-200,0), "pol_sem_bya",
            (600,150), "hand_0"
            )

image roma_figth_02 = LiveComposite((1920, 1080),
            (0,0), "roma_figth_bg",
            (-200,0), "pol_sem_bya2",
            (600,150), "hand_0"
            )

image roma_figth_1 = LiveComposite((1920, 1080),
            (0,0), "roma_figth_bg",
            (600,150), "hand_0",
            (0,0), "locate/street/gopstop/roma_fight/Rom.png",
            )

image roma_figth_2 = LiveComposite((1920, 1080),
            (0,0), "roma_figth_bg",
            (600,150), "hand_1",
            (0,0), "locate/street/gopstop/roma_fight/Rom_2.png",
            )

image roma_figth_3 = LiveComposite((1920, 1080),
            (0,0), "locate/street/gopstop/roma_fight/Ro_fon_2.jpg",
            (600,150), "locate/street/gopstop/roma_fight/hand.png",
            (0,0), "locate/street/gopstop/roma_fight/Rom_3.png",
            )

image roma_figth_anim = Animation(
            "locate/street/gopstop/roma_fight/Roma_fight_01.jpg", 0.1,
            "locate/street/gopstop/roma_fight/Roma_fight_02.jpg", 0.1,
            "locate/street/gopstop/roma_fight/Roma_fight_03.jpg", 0.1,
            "locate/street/gopstop/roma_fight/Roma_fight_04.jpg", 2.1,
            )

image roma_figth_4 = "locate/street/gopstop/roma_fight/Roma_fight_04.jpg"

image dark_forest_day2_1 = LiveComposite((1920, 1080),
            (0,0), "locate/forest/road_wood03.jpg",
            (0,0), "locate/forest/Anton.png",
            (0,0), "locate/forest/BandR.png"
            )

image dark_forest_day2_2 = LiveComposite((1920, 1080),
            (0,0), "locate/forest/road_wood03.jpg",
            (0,0), "locate/forest/BandR.png"
            )

image dark_forest_day2_3 = LiveComposite((2887, 1080),
            (0,0), "locate/forest/road_wood04.jpg",
            (0,0), "locate/forest/Antonio.png",
            (0,0), "locate/forest/Polina.png"
            )

image dark_forest_day2_4 = LiveComposite((2887, 1080),
            (0,0), "locate/forest/road_wood04.jpg",
            (0,0), "locate/forest/Polina.png"
            )

image dark_forest_day2_5 = LiveComposite((2887, 1080),
            (0,0), "locate/forest/road_wood04.jpg",
            )

image dark_forest_day2_0 = im.MatrixColor("locate/street/Sema_battle/Draka_fon3.jpg", im.matrix.brightness(-0.05))

image dark_forest_day3_1 = LiveComposite((1920, 1080),
            (0,0), "locate/forest/Foresty.jpg",
            )

image traktor = im.MatrixColor("locate/street/Sema_battle/traktor.png", im.matrix.brightness(-0.10))

image bg kenti = "locate/forest/kenti/Fon_kenti.jpg"

image kenti1:
    contains:
        "locate/forest/kenti/01.png"
        alpha 1.0
    contains:
        "locate/forest/kenti/02.png"
        alpha 0.0
        ease 3.0 alpha 1.0
        ease 3.0 alpha 0.0
        repeat

image kenti2 = "locate/forest/kenti/01.png"
image kenti3 = Animation(
    "locate/forest/kenti/01.png", 0.13,
    "locate/forest/kenti/02.png", 0.13,
    "locate/forest/kenti/03.png", 0.13,
    "locate/forest/kenti/04.png", 0.13,
    "locate/forest/kenti/03.png", 0.13,
    "locate/forest/kenti/02.png", 0.13,
    "locate/forest/kenti/03.png", 0.13,
    "locate/forest/kenti/04.png", 0.13,
    "locate/forest/kenti/05.png", 0.13,
    "locate/forest/kenti/06.png", 0.13,
    "locate/forest/kenti/05.png", 0.13,
    "locate/forest/kenti/05.png", 10.00)

image kenti4:
    contains:
        "locate/forest/kenti/05.png"
        alpha 1.0
    contains:
        "locate/forest/kenti/06.png"
        alpha 0.0
        ease 3.0 alpha 1.0
        ease 3.0 alpha 0.0
        repeat

image kenti5 = LiveComposite((1920, 1080),
    (0,0), "locate/forest/kenti/05.png",
    (2300,0), "locate/forest/kenti/Kenti.png")

image kenti_army:
    contains:
        "locate/forest/kenti/Kenti.png"
        xpos -300
    contains:
        "locate/forest/kenti/Kenti_2.png"
        xpos 550

image semen_down = "locate/street/Sema_battle/Semen_down.jpg"


image bg_shaman2:
    parallel:
        im.Blur("locate/home/in_side/2st_floor/olga_room/Reportash/shaman.jpg", 2.5)
        zoom 0.9
        alpha 0.0
        parallel:
            ease 1.0 xalign 0.3
            ease 1.0 xalign 0.9
            ease 1.0 xalign 0.5
            ease 0.2 xalign 0.7
            ease 0.2 xalign 0.3
            ease 1.0 xalign 0.9
            ease 1.0 xalign 0.5
            ease 1.0 xalign 0.7
            repeat
        parallel:
            ease 0.8 yalign 0.2
            ease 0.8 yalign 0.5
            ease 0.8 yalign 0.3
            ease 0.8 yalign 0.7
            ease 0.2 yalign 0.5
            ease 0.8 yalign 0.2
            repeat
        parallel:
            pause 2.0
            ease 0.2 alpha 0.8
            ease 0.2 alpha 0.0
            repeat
image bg_shaman1:
    parallel:
        "locate/home/in_side/2st_floor/olga_room/Reportash/shaman.jpg"
        zoom 0.9
        parallel:
            ease 1.0 xalign 0.3
            ease 1.0 xalign 0.9
            ease 1.0 xalign 0.5
            ease 0.2 xalign 0.7
            ease 0.2 xalign 0.3
            ease 1.0 xalign 0.9
            ease 1.0 xalign 0.5
            ease 1.0 xalign 0.7
            repeat
        parallel:
            ease 0.8 yalign 0.2
            ease 0.8 yalign 0.5
            ease 0.8 yalign 0.3
            ease 0.8 yalign 0.7
            ease 0.2 yalign 0.5
            ease 0.8 yalign 0.2
            repeat

image snowman_snow = LiveComposite((1920, 1080),
    (0,700), SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=10,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,700), SnowBlossom("effect/snow/s014.png", count=100,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,700), SnowBlossom("effect/snow/s013.png", count=80,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True))

image snowman_snow_more = LiveComposite((1920, 1080),
    (0,700), SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=20,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,700), SnowBlossom("effect/snow/s014.png", count=140,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,700), SnowBlossom("effect/snow/s013.png", count=120,  yspeed=(10, 50), xspeed=(200, 250), border=50, start=0, fast=True, distribution="linear", horizontal = True))

image snowman_snow_fast = LiveComposite((1920, 1080),
    (0,200), SnowBlossom("effect/snow/s006.png", count=30,  yspeed=(10, 50), xspeed=(600, 650), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=40,  yspeed=(10, 50), xspeed=(650, 700), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("effect/snow/s014.png", count=150,  yspeed=(10, 50), xspeed=(400, 450), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("effect/snow/s013.png", count=180,  yspeed=(10, 50), xspeed=(400, 450), border=50, start=0, fast=True, distribution="linear", horizontal = True))

image snowman_snow_revers = LiveComposite((1920, 1080),
    (0,600), SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=10,  yspeed=(10, 50), xspeed=(-200, -250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,600), SnowBlossom("effect/snow/s014.png", count=100,  yspeed=(10, 50), xspeed=(-200, -250), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,600), SnowBlossom("effect/snow/s013.png", count=80,  yspeed=(10, 50), xspeed=(-200, -250), border=50, start=0, fast=True, distribution="linear", horizontal = True))

image snowman_snow_fast_revers = LiveComposite((1920, 1080),
    (0,200), SnowBlossom("effect/snow/s006.png", count=30,  yspeed=(10, 50), xspeed=(-600, -650), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("locate/school/in_side/Polina_Lisa/Snow_02.png", count=40,  yspeed=(10, 50), xspeed=(-650, -700), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("effect/snow/s014.png", count=150,  yspeed=(10, 50), xspeed=(-400, -450), border=50, start=0, fast=True, distribution="linear", horizontal = True),
    (0,200), SnowBlossom("effect/snow/s013.png", count=180,  yspeed=(10, 50), xspeed=(-400, -450), border=50, start=0, fast=True, distribution="linear", horizontal = True))

image snowman 0 = LiveComposite((1920, 1080),
    (0,0), "locate/forest/Ant_Pol/fon.jpg",
    (0,0), "locate/forest/Ant_Pol/A_P.png")

image snowman 00 = LiveComposite((1920, 1080),
    (0,0), "locate/forest/Ant_Pol/fon.jpg",
    (0,0), "locate/forest/Ant_Pol/A_P2.png",
    (0,0), "locate/forest/Ant_Pol/A_P.png")

image snowman 1 = LiveComposite((1920, 1080),
    (0,0), "locate/forest/Ant_Pol/fon.jpg",
    (0,0), "locate/forest/Ant_Pol/snowman_1.png")

image snowman 2 = LiveComposite((1920, 1080),
    (0,0), "locate/forest/Ant_Pol/fon.jpg",
    (0,0), "locate/forest/Ant_Pol/snowman_2.png")

image bad_mask_bg:
    "locate/forest/bad_mask/Mask_Fon.jpg"

image bad_mask 0:
    contains:
        "locate/forest/bad_mask/Mask_00.png"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat

image bad_mask 0_blur_ne_blur:
    contains:
        "locate/forest/bad_mask/Mask_00.png"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
    contains:
        im.Blur("locate/forest/bad_mask/Mask_00.png", 0.6)
        alpha 0.0
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image bad_mask 1:
    contains:
        "locate/forest/bad_mask/Mask_00.png"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
    contains:
        Animation(
            "locate/forest/bad_mask/Mask_01.png", 0.13,
            "locate/forest/bad_mask/Mask_02.png", 0.13,
            "locate/forest/bad_mask/Mask_03.png", 0.13,
            "locate/forest/bad_mask/Mask_04.png", 0.13,
            "locate/forest/bad_mask/Mask_05.png", 0.13,
            "locate/forest/bad_mask/Mask_06.png", 0.13,
            "locate/forest/bad_mask/Mask_07.png", 0.13,
            "locate/forest/bad_mask/Mask_08.png", 0.13,
            "locate/forest/bad_mask/Mask_09.png", 0.13,
            "locate/forest/bad_mask/Mask_10.png", 0.13,
            "locate/forest/bad_mask/Mask_11.png", 0.13,
            "locate/forest/bad_mask/Mask_12.png", 0.13,
            "locate/forest/bad_mask/Mask_13.png", 0.13,
            "locate/forest/bad_mask/Mask_14.png", 0.13,
            "locate/forest/bad_mask/Mask_15.png", 0.13,
            "locate/forest/bad_mask/Mask_16.png", 0.13,
            "locate/forest/bad_mask/Mask_17.png", 0.13,
            "locate/forest/bad_mask/Mask_18.png", 0.13,
            "locate/forest/bad_mask/Mask_19.png", 0.13,
            )
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat

image bad_mask 3:
    contains:
        "locate/forest/bad_mask/Mask_00.png"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            ease 0.8 xoffset -50 yoffset 0
            ease 0.8 xoffset 650 yoffset 0 alpha 0.0

image bad_mask_bg_blur:
    im.Blur("locate/forest/bad_mask/Mask_Fon.jpg", 1.5)

image bad_mask 0_blur:
    contains:
        im.Blur("locate/forest/bad_mask/Mask_00.png", 1.5)
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat

image bad_mask 3_blur:
    contains:
        im.Blur("locate/forest/bad_mask/Mask_00.png", 1.5)
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            ease 0.8 xoffset -50 yoffset 0
            ease 0.8 xoffset 650 yoffset 0 alpha 0.0


image bg_road_wood blur = im.Blur("locate/street/road_wood.jpg", 1.5)
image bg_road_wood dark_blur = im.MatrixColor(im.MatrixColor(im.Blur("locate/street/road_wood.jpg", 1.5), im.matrix.brightness(-0.20)), im.matrix.contrast(0.9))
image bg_road_wood heavy_dark_blur = im.MatrixColor(im.MatrixColor(im.Blur("locate/street/road_wood.jpg", 2.5), im.matrix.brightness(-0.20)), im.matrix.contrast(0.9))

image Byasha Normal m_day_winter 01 normal ahead 01 blur = Composite((1920, 1080),
    (0,0), im.Blur("sprite/Byasha/Normal/m_day_winter/1_body/01.png", 0.5),
    (0,0), Animation(
        im.Blur("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/01.png", 0.5), 0.7,
        im.Blur("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/02.png", 0.5), 0.1,
        im.Blur("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/03.png", 0.5), 0.1,
        im.Blur("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/02.png", 0.5), 0.1,
        im.Blur("sprite/Byasha/Normal/m_day_winter/2_eyes/normal/ahead/01.png", 0.5), 6.0,
        ),
    (0,0), im.Blur("sprite/Byasha/Normal/m_day_winter/3_mouth/01.png", 0.1),
    )

image Byasha Hee m_day_winter 01 dark_blur = Composite((1920, 1080),
    (0,0), im.MatrixColor(im.MatrixColor(im.Blur("sprite/Byasha/Hee/m_day_winter/1_body/01.png", 0.7), im.matrix.brightness(-0.20)), im.matrix.contrast(0.95)),
    )

image Byasha Hee m_day_winter 01 heavy_dark_blur = Composite((1920, 1080),
    (0,0), im.MatrixColor(im.MatrixColor(im.Blur("sprite/Byasha/Hee/m_day_winter/1_body/01.png", 1.5), im.matrix.brightness(-0.20)), im.matrix.contrast(0.95)),
    )

image Romka Normal m_day_winter 00 norm ahead 01 blur = Composite((1920, 1080),
    (0,0), im.Blur("sprite/Romka/Normal/m_day_winter/1_body/00.png", 0.2),
    )

image Romka Normal m_day_winter 00 norm ahead 01 dark_blur = Composite((1920, 1080),
    (0,0), im.MatrixColor(im.MatrixColor(im.Blur("sprite/Romka/Normal/m_day_winter/1_body/00.png", 0.7), im.matrix.brightness(-0.20)), im.matrix.contrast(0.95)),
    )

image Romka Normal m_day_winter 00 norm ahead 01 heavy_dark_blur = Composite((1920, 1080),
    (0,0), im.MatrixColor(im.MatrixColor(im.Blur("sprite/Romka/Normal/m_day_winter/1_body/00.png", 1.5), im.matrix.brightness(-0.20)), im.matrix.contrast(0.95)),
    )

image Semen Normal m_day_W 00 evil ahead 01 blur = Composite((1920, 1080),
    (0,0), im.Blur("sprite/Semen/Normal/m_day_W/1_body/00.png", 0.5),
    (0,0), Animation(
        im.Blur("sprite/Semen/Normal/m_day_W/2_eyes/evil/ahead/01.png", 0.5), 1.0,
        im.Blur("sprite/Semen/Normal/m_day_W/2_eyes/evil/ahead/02.png", 0.5), 0.1,
        im.Blur("sprite/Semen/Normal/m_day_W/2_eyes/evil/ahead/03.png", 0.5), 0.1,
        im.Blur("sprite/Semen/Normal/m_day_W/2_eyes/evil/ahead/02.png", 0.5), 0.1,
        im.Blur("sprite/Semen/Normal/m_day_W/2_eyes/evil/ahead/01.png", 0.5), 8.0,
        ),
    (0,0), im.Blur("sprite/Semen/Normal/m_day_W/3_mouth/01.png", 0.5),
    )

image doggy_fon = "locate/forest/Dogee/fon2.jpg"
image doggy_fon blur = im.Blur("locate/forest/Dogee/fon2.jpg", 2.5)
image doggy_fly = "locate/forest/Dogee/Dogee.png"

image doggy_pol 01 = "locate/forest/Dogee/01.png"
image doggy_pol 02 = "locate/forest/Dogee/02.png"
image doggy_pol 03 = "locate/forest/Dogee/03.png"
image doggy_pol 04 = "locate/forest/Dogee/04.png"

image nightmare_ol_d1 = Composite((1920, 1080),
    (0,0), "locate/home/in_side/1st_floor/kitchen/Ol .png",
    (0,0), Animation(
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 2.0,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_03.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 4.0,
    ),
    (0,0), "locate/home/in_side/1st_floor/kitchen/M_1.png",
    )

image nightmare_ol_n1 = Composite((1920, 1080),
    (0,0), "locate/home/in_side/1st_floor/kitchen/Ol_n.png",
    (0,0), Animation(
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 2.0,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_03.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 4.0,
    ),
    (0,0), "locate/home/in_side/1st_floor/kitchen/M_n1.png",
    )

image nightmare_ol_d2 = Composite((1920, 1080),
    (0,0), "locate/home/in_side/1st_floor/kitchen/Ol .png",
    (0,0), Animation(
        "locate/home/in_side/1st_floor/kitchen/eye_04.png", 2.0,
    ),
    (0,0), "locate/home/in_side/1st_floor/kitchen/M_1.png",
    )

image nightmare_ol_d3 = Composite((1920, 1080),
    (0,0), "locate/home/in_side/1st_floor/kitchen/Ol .png",
    (0,0), Animation(
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 2.0,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_03.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_02.png", 0.1,
        "locate/home/in_side/1st_floor/kitchen/eye_01.png", 4.0,
    ),
    (0,0), "locate/home/in_side/1st_floor/kitchen/M_2.png",
    )

image nightmare_pen1 = "locate/home/in_side/1st_floor/kitchen/pen_day.png"
image nightmare_pen2 = "locate/home/in_side/1st_floor/kitchen/pen_night.png"

image ant_room_door_open_day = Animation(
    "locate/home/in_side/2st_floor/anton_room/room_day/room_day01.png", 0.1,
    "locate/home/in_side/2st_floor/anton_room/room_day/room_day02.png", 0.1,
    "locate/home/in_side/2st_floor/anton_room/room_day/room_day03.png", 3.1)

image bg_kitchen_dark2:
    contains:
        "locate/home/in_side/1st_floor/kitchen/ketcen_dark.jpg"
    contains:
        "nightmare_ol_n1"
    contains:
        "nightmare_pen2"
    alpha 0.0
    linear 10.0 alpha 1.0

image dad_happy_day = "sprite/Dad/Happy/m_day/1_body/00.png"
image mom_happy_day = Composite((1920, 1080),
    (0,0), "sprite/Mom/Normal/m_day/1_body/04.png",
    (0,0), "sprite/Mom/Normal/m_day/2_eyes/norm/ahead/01.png")

image dad_happy = "sprite/Dad/Happy/m_evening/1_body/00.png"
image mom_happy = Composite((1920, 1080),
    (0,0), "sprite/Mom/Normal/m_evening/1_body/04.png",
    (0,0), "sprite/Mom/Normal/m_evening/2_eyes/norm/ahead/01.png")




image sosni 0_blur_ne_blur:

    contains:
        "locate/forest/batya/Sosni.png"
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
    contains:
        im.Blur("locate/forest/batya/Sosni.png", 6.6)
        alpha 0.0
        xalign 0.5 yalign 0.5
        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood 0_blur_ne_blur:

    contains:
        "locate/forest/batya/Wood.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat


image batya wood2 0_blur_ne_blur:

    contains:
        "locate/forest/batya/Wood_2.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_2.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood3 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_3.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_3.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood4 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_4.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_4.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood_5 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_5.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_5.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0




        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood05 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_05.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_05.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0




        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood6 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_6.jpg"

        xoffset 0 yoffset 0




    contains:
        im.Blur("locate/forest/batya/Wood_6.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0




        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood7 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_7.jpg"

        xoffset 0 yoffset 0




    contains:
        im.Blur("locate/forest/batya/Wood_7.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0




        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood8 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_8.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_8.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image batya wood9 0_blur_ne_blur:
    contains:
        "locate/forest/batya/Wood_9.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/forest/batya/Wood_9.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image Hand_2:
    block:
        im.Blur("locate/forest/batya/Hand_2.png", .6)


        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat



image incar bg:
    contains:
        "locate/incar/fon2.jpg"

    contains:
        LiveComposite((1920, 1080),

            (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(10, 800), border=1, start=0, fast=True, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s013.png", count=500, yspeed=(40, 150), xspeed=(10, 800), border=1, start=0, fast=True, distribution="linear"),
            
            (0, 0), SnowBlossom("effect/snow/s014.png", count=2000, yspeed=(50, 80), xspeed=(30, 700), border=1, start=0, fast=True, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s012.png", count=2000, yspeed=(60, 90), xspeed=(30, 700), border=1, start=0, fast=True, distribution="linear"),

            (0, 0), SnowBlossom("effect/snow/s016.png", count=500, yspeed=(80, 100), xspeed=(10, 600), border=1, start=0, fast=True, distribution="linear"),
            
            
            )

default incar_state_bg = 0
default incar_state_snow = 0
default incar_state_chetki = 0
default incar_state_car = 0
default incar_state_dad = 0
default incar_state_box1 = 0
default incar_state_box2 = 0
default incar_state_at = 0
image incar_comp:
    Composite((1920, 1080),
        (0, 0), ConditionSwitch(
            "incar_state_chetki == 0", "chetki0",
            "incar_state_chetki == 1", "chetki_d0",
            "incar_state_chetki == 2", "chetki_d",
            "True", Null()),
        (0, 0), ConditionSwitch(
            "incar_state_car == 0", "body car",
            "incar_state_car == 1", "body car_d",
            "True", Null()),
        (0, 0), ConditionSwitch(
            "incar_state_dad == 0", "dad car ahead",
            "incar_state_dad == 1", "dad car aside",
            "incar_state_dad == 2", "dad car_d aside",
            "incar_state_dad == 3", "dad car_d ahead",
            "True", Null()),
        (0, 0), ConditionSwitch(
            "incar_state_box1 == 1", "incar_box1 0_blur_ne_blur",
            "True", Null()),
        (0, 0), ConditionSwitch(
            "incar_state_box2 == 1", "incar_box2 0_blur_ne_blur",
            "True", Null())
        )

image incar_polina_bg:
    "locate/incar/fon.jpg"

image incar_garage_bg:
    "locate/incar/fon_garaz.jpg"

default sssnow0 = SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(300, 400), border=1, start=0, fast=True, distribution="linear")
default sssnow1 = SnowBlossom("effect/snow/s013.png", count=500, yspeed=(40, 150), xspeed=(300, 400), border=1, start=0, fast=True, distribution="linear")
default sssnow2 = SnowBlossom("effect/snow/s014.png", count=2000, yspeed=(50, 80), xspeed=(250, 300), border=1, start=0, fast=True, distribution="linear")
default sssnow3 = SnowBlossom("effect/snow/s012.png", count=2000, yspeed=(60, 90), xspeed=(250, 300), border=1, start=0, fast=True, distribution="linear")
default sssnow4 = SnowBlossom("effect/snow/s016.png", count=500, yspeed=(80, 100), xspeed=(175, 200), border=1, start=0, fast=True, distribution="linear")

image incar_polina_snow:
    LiveComposite((1920, 1080),

        (0, 0), sssnow0,
        (0, 0), sssnow1,
        (0, 0), sssnow2,
        (0, 0), sssnow3,
        (0, 0), sssnow4,
        )



image chetki0 = "locate/incar/car/Chetki/ch_01.png"
image body car = "locate/incar/car/body_car.png"

image chetki_d0 = "locate/incar/dark_car/Chetki_dark/ch_d_01.png"
image body car_d = "locate/incar/dark_car/body_d.png"
$ chet_time = 0.3
image chetki_d = Animation ("locate/incar/dark_car/Chetki_dark/ch_d_01.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_02.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_03.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_04.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_05.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_04.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_03.png", chet_time,
    "locate/incar/dark_car/Chetki_dark/ch_d_02.png", chet_time,)



image incar_box1 0_blur_ne_blur:
    contains:
        "locate/incar/dark_car/dark_box_1.png"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat














image incar_box2 0_blur_ne_blur:
    contains:
        "locate/incar/dark_car/dark_box_2.png"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat














image incar_bord 0_blur_ne_blur:
    contains:
        "locate/incar/dark_car/Bord.jpg"

        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -1 yoffset 0

            repeat
    contains:
        im.Blur("locate/incar/dark_car/Bord.jpg", 0.6)
        alpha 0.0

        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset 1 yoffset 0

            repeat
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat


image incar_forest:
    contains:
        block:
            "locate/incar/Forest.jpg"
            zoom 1.5
            xpos 0
            xoffset -2000+960
            ypos -.1
            ease 8.0 zoom .55 xpos -.1 xoffset 0



image incar_car:
    contains:
        "locate/incar/avto.png"

        parallel:
            zoom 1.5
            ease 8.0 zoom .55
        parallel:
            xpos 1.4
            ypos -.1
            ease 15.0 xpos -.8




image incar_snow_up = Ani("images/locate/incar/snow/", 20, 0.1, reverse = False, ext = 'png')


image mask_before = "locate/forest/wear_mask/Mask_01.jpg"
image mask_after = "locate/forest/wear_mask/Mask_08.jpg"
image wear_mask = Animation(
    "locate/forest/wear_mask/Mask_02.jpg", 0.1,
    "locate/forest/wear_mask/Mask_03.jpg", 0.2,
    "locate/forest/wear_mask/Mask_04.jpg", 0.2,
    "locate/forest/wear_mask/Mask_05.jpg", 0.2,
    "locate/forest/wear_mask/Mask_06.jpg", 0.2,
    "locate/forest/wear_mask/Mask_07.jpg", 0.2,
    "locate/forest/wear_mask/Mask_08.jpg", 5.0,
)


label lamp0:
    return
    play test_four [
        "<silence 3.6>",
        "sounds/lamp/Lamp_001.ogg",
        "<silence 5.275>",
        "sounds/lamp/Lamp_002.ogg",
        "<silence 3.518>",
        "sounds/lamp/Lamp_003.ogg",
        "<silence 5.561>",
        "sounds/lamp/Lamp_004.ogg",
        "<silence 5.799>",
        "sounds/lamp/Lamp_005.ogg",
        ] loop












init python:

    def play_garage_blink(id):
        def f(trans, st, at):
            renpy.play("sounds/lamp/Lamp_00" + str(id) +".ogg", channel="test_four", relative_volume=lamp_volume)
        return f

    def play_lamp_blink_1(trans, st, at):
        renpy.play("sounds/lamp/Lamp_001.ogg", channel="lamp_sfx", relative_volume=lamp_volume)
    def play_lamp_blink_2(trans, st, at):
        renpy.play("sounds/lamp/Lamp_002.ogg", channel="lamp_sfx", relative_volume=lamp_volume)
    def play_lamp_blink_3(trans, st, at):
        renpy.play("sounds/lamp/Lamp_003.ogg", channel="lamp_sfx", relative_volume=lamp_volume)
    def play_lamp_blink_4(trans, st, at):
        renpy.play("sounds/lamp/Lamp_004.ogg", channel="lamp_sfx", relative_volume=lamp_volume)
    def play_lamp_blink_5(trans, st, at):
        renpy.play("sounds/lamp/Lamp_005.ogg", channel="lamp_sfx", relative_volume=lamp_volume)
    def play_lamp_blink_random(trans, st, at):
        id = renpy.random.randint(1, 5)
        renpy.play("sounds/lamp/Lamp_00" + str(id) +".ogg", channel="lamp_sfx", relative_volume=lamp_volume)


image test1:
    im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)

    block:
        pause 1
        function play_lamp_blink_1
        pause 1
        function play_lamp_blink_2
        pause 1
        function play_lamp_blink_3
        repeat

image garage_near_blinking:
    contains:
        im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)

        block:
            pause 4

            function play_lamp_blink_1

            block:
                im.Blur("locate/street/garage/The_garage_01.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 6

            function play_lamp_blink_2

            block:
                im.Blur("locate/street/garage/The_garage_01.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 4

            function play_lamp_blink_3

            block:
                im.Blur("locate/street/garage/The_garage_01.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)
                pause 0.1

                repeat 2

            pause 6

            function play_lamp_blink_4

            block:
                im.Blur("locate/street/garage/The_garage_01.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)
                pause 0.1

                repeat 1

            pause 6

            function play_lamp_blink_5

            block:
                im.Blur("locate/street/garage/The_garage_01.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/The_garage_02.jpg", 1.0)
                pause 0.1

                repeat 2

            repeat

image garage_blinking_blure:
    contains:
        im.Blur("locate/street/garage/garage_1.jpg", 1.5)

        block:
            choice:
                pause 2.0
            choice:
                pause 4.0
            choice:
                pause 6.0

        block:
            choice 1:
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1

            choice 2:
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_1.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1

            choice 1:
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_1.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_1.jpg", 1.5)
                pause 0.1
                im.Blur("locate/street/garage/garage_2.jpg", 1.5)
                pause 0.1
        repeat

default blink_dark = 0.5
image garage_blink_black:
    "black"
    alpha 0

    block:
        pause 2

        function play_lamp_blink_1

        block:
            alpha blink_dark
            pause 0.1
            alpha 0
            pause 0.05

            repeat 5

        pause 4

        function play_lamp_blink_2

        block:
            alpha blink_dark
            pause 0.15
            alpha 0
            pause 0.05

            repeat 4

        pause 3

        function play_lamp_blink_3

        block:
            alpha blink_dark
            pause 0.1
            alpha 0
            pause 0.1

            repeat 2

        pause 3

        function play_lamp_blink_4

        block:
            alpha blink_dark
            pause 0.15
            alpha 0
            pause 0.1

            repeat 1

        pause 2

        function play_lamp_blink_5

        block:
            alpha blink_dark
            pause 0.15
            alpha 0
            pause 0.1

            repeat 2

        repeat

image garage_blink_black2:
    "black"
    alpha 0

    block:
        pause .5

        block:
            alpha blink_dark
            pause 0.1
            alpha 0
            pause 0.1

            repeat 4

        repeat

image garage_near_blinking_0:
    contains:
        im.Blur("locate/street/garage/knok4/01.jpg", 1.0)

        block:
            pause 4

            function play_lamp_blink_1

            block:
                im.Blur("locate/street/garage/knok4/02.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/01.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 6

            function play_lamp_blink_2

            block:
                im.Blur("locate/street/garage/knok4/02.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/01.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 4

            function play_lamp_blink_3

            block:
                im.Blur("locate/street/garage/knok4/02.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/01.jpg", 1.0)
                pause 0.1

                repeat 2

            pause 6

            function play_lamp_blink_4

            block:
                im.Blur("locate/street/garage/knok4/02.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/01.jpg", 1.0)
                pause 0.1

                repeat 1

            pause 6

            function play_lamp_blink_5

            block:
                im.Blur("locate/street/garage/knok4/02.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/01.jpg", 1.0)
                pause 0.1

                repeat 2

            repeat

image garage_near_blinking_1:
    contains:
        im.Blur("locate/street/garage/knok4/03.jpg", 1.0)

        block:
            pause 4

            function play_lamp_blink_1

            block:
                im.Blur("locate/street/garage/knok4/04.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/03.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 6

            function play_lamp_blink_2

            block:
                im.Blur("locate/street/garage/knok4/04.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/03.jpg", 1.0)
                pause 0.1

                repeat 3

            pause 4

            function play_lamp_blink_3

            block:
                im.Blur("locate/street/garage/knok4/04.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/03.jpg", 1.0)
                pause 0.1

                repeat 2

            pause 6

            function play_lamp_blink_4

            block:
                im.Blur("locate/street/garage/knok4/04.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/03.jpg", 1.0)
                pause 0.1

                repeat 1

            pause 6

            function play_lamp_blink_5

            block:
                im.Blur("locate/street/garage/knok4/04.jpg", 1.0)
                pause 0.1
                im.Blur("locate/street/garage/knok4/03.jpg", 1.0)
                pause 0.1

                repeat 2

            repeat


image garage_near_blinking_static:
    im.Blur("locate/street/garage/knok5/01-03.jpg", 1.0)

image garage_near_blinking_anim:
    im.Blur("locate/street/garage/knok5/02.jpg", 1.0)
    0.10
    im.Blur("locate/street/garage/knok5/01-03.jpg", 1.0)
    0.10
    im.Blur("locate/street/garage/knok5/04.jpg", 1.0)
    0.10
    im.Blur("locate/street/garage/knok5/05.jpg", 1.0)
    0.10

    "locate/street/garage/knok2/t01.png"
    pause 0.10
    block:
        "locate/street/garage/knok2/t02.png"
        pause 0.10
        "locate/street/garage/knok2/t03.png"
        pause 0.10
        "locate/street/garage/knok2/t04.png"
        pause 0.10
        "locate/street/garage/knok2/t05.png"
        pause 0.10
        "locate/street/garage/knok2/t06.png"
        pause 0.10
        "locate/street/garage/knok2/t07.png"
        pause 0.10
        "locate/street/garage/knok2/t08.png"
        pause 0.10
        "locate/street/garage/knok2/t09.png"
        pause 0.10
        "locate/street/garage/knok2/t10.png"
        pause 0.10

        repeat 2

    "locate/street/garage/knok2/t11.png"
    pause 0.10
    "locate/street/garage/knok2/t12.png"
    pause 0.10
    "locate/street/garage/knok2/t13.png"


image garage_near_opened_blur:
    im.Blur("locate/street/garage/The_garage_03.jpg", 1.0)

image garage_smoke_1:
    im.Blur("locate/street/garage/smoke.png", 1.0)
    subpixel True
    block:
        xpos 0
        linear 45.0 xpos 1920
        repeat

image garage_smoke_2:
    im.Blur("locate/street/garage/smoke.png", 1.0)
    subpixel True
    block:
        xpos -1920
        linear 45.0 xpos 0
        repeat

image perehod:
    "locate/street/walkaway/Perehod_01.png"



image fkoz_bg:
    "locate/forest/kozel_first/bg.jpg"

image fkoz_1_1:
    "locate/forest/kozel_first/Tree_01.png"
image fkoz_1_2:
    "locate/forest/kozel_first/Tree_02.png"

image fkoz_2_1:
    "locate/forest/kozel_first/Tree_03.png"
image fkoz_2_2:
    "locate/forest/kozel_first/Tree_04.png"

image fkoz_beast:
    "locate/forest/kozel_first/Beast_00.png"

image fkoz_beast true:
    "locate/forest/kozel_first/Beast_01.png"

image kozel_eye1:
    "locate/forest/kozel_first/Eyes_1.png"
image kozel_eye2:
    "locate/forest/kozel_first/Eyes_2.png"
image kozel_eye3:
    "locate/forest/kozel_first/Eyes_3.png"
image kozel_eye4:
    "locate/forest/kozel_first/Eyes_4.png"
image kozel_eye5:
    "locate/forest/kozel_first/Eyes_5.png"

image kozel_hoof_1_blur:
    contains:
        "locate/forest/kozel_first/Kozel_001.jpg"
    contains:
        im.Blur("locate/forest/kozel_first/Kozel_001.jpg", 0.6)
        alpha 0.0
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image kozel_hoof_2_blur:
    contains:
        "locate/forest/kozel_first/Kozel_002.jpg"
    contains:
        im.Blur("locate/forest/kozel_first/Kozel_002.jpg", 0.6)
        alpha 0.0
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image kozel_hoof_3_blur:
    contains:
        "locate/forest/kozel_first/Kozel_003.jpg"
    contains:
        im.Blur("locate/forest/kozel_first/Kozel_003.jpg", 0.6)
        alpha 0.0
        parallel:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.0
            repeat

image kozel_loop:
    "locate/forest/kozel_first/loop/K_000.jpg"
    pause 3.0
    pause .15
    "locate/forest/kozel_first/loop/K_001.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_002.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_003.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_004.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_005.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_006.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_007.jpg"
    pause .15
    repeat

image kozel_loop_full:
    "locate/forest/kozel_first/loop/K_001.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_002.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_003.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_004.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_005.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_006.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_007.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_008.jpg"
    pause .15
    "locate/forest/kozel_first/loop/K_009.jpg"
    pause .2

    block:
        "locate/forest/kozel_first/loop/K_000.jpg"
        pause 3.0
        pause .15
        "locate/forest/kozel_first/loop/K_001.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_002.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_003.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_004.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_005.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_006.jpg"
        pause .15
        "locate/forest/kozel_first/loop/K_007.jpg"
        pause .15
        repeat

image kozel_phase2_2:
    contains:
        im.Blur("locate/forest/kozel_first/phase2/Koz_2.jpg", .3)

    contains:
        im.Blur("locate/forest/kozel_first/phase2/Koz_2.jpg", .8)
        linear 1 alpha 1.
        linear 1 alpha 0.
        repeat

    contains:
        "locate/forest/kozel_first/phase2/Hand.png"
        zoom .5
        ypos 100
        xoffset 0 yoffset 0
        block:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat

    contains:
        im.Blur("locate/forest/kozel_first/phase2/Hand.png", .6)
        zoom .5
        ypos 100
        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
        parallel:
            linear 1 alpha 1.
            linear 1 alpha 0.
            repeat

image kozel_phase2_2b:
    contains:
        im.Blur("locate/forest/kozel_first/phase2/Koz_1.jpg", .3)

    contains:
        im.Blur("locate/forest/kozel_first/phase2/Koz_1.jpg", .8)
        linear 1 alpha 1.
        linear 1 alpha 0.
        repeat

    contains:
        "locate/forest/kozel_first/phase2/Hand.png"
        zoom .57
        ypos 100
        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
        parallel:
            easein 3 zoom .5

    contains:
        im.Blur("locate/forest/kozel_first/phase2/Hand.png", .6)
        zoom .57
        ypos 100
        xoffset 0 yoffset 0
        parallel:
            linear 1.0 xoffset -5 yoffset 0
            linear 1.0 xoffset 0 yoffset -5
            linear 1.0 xoffset -5 yoffset 5
            linear 1.0 xoffset 5 yoffset 0
            linear 1.0 xoffset 0 yoffset 0
            linear 1.0 xoffset 5 yoffset -5
            repeat
        parallel:
            easein 3 zoom .5
        parallel:
            linear 1 alpha 1.
            linear 1 alpha 0.
            repeat

image kozel_light:
    contains:
        "locate/forest/kozel6/1.jpg"
        pause .08
        "locate/forest/kozel6/2.jpg"
        pause .08
        "locate/forest/kozel6/3.jpg"
        pause .08
        "locate/forest/kozel6/4.jpg"
        pause .08
        "locate/forest/kozel6/5.jpg"
        pause .08
        "locate/forest/kozel6/6.jpg"
        pause .08
        "locate/forest/kozel6/7.jpg"
        pause .08
        "locate/forest/kozel6/8.jpg"
        pause .08
        "locate/forest/kozel6/9.jpg"
        pause .08
        "locate/forest/kozel6/10.jpg"
        pause .16
        "locate/forest/kozel6/11.jpg"
        pause .08
        "locate/forest/kozel6/12.jpg"
        pause .08
        "locate/forest/kozel6/13.jpg"
        pause .08
        "locate/forest/kozel6/14.jpg"
        pause .08
        "locate/forest/kozel6/15.jpg"
        pause .08
        "locate/forest/kozel6/16.jpg"
        pause .08
        "locate/forest/kozel6/17.jpg"
    contains:
        pause 1.36
        alpha 0
        im.Blur("locate/forest/kozel6/17.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_17_reblur:
    contains:
        "locate/forest/kozel6/kozel_017.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_017.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_18_reblur:
    contains:
        "locate/forest/kozel6/kozel_018.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_018.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_19_reblur:
    contains:
        "locate/forest/kozel6/kozel_019.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_019.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_19_reblur:
    contains:
        "locate/forest/kozel6/kozel_019.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_019.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_20_reblur:
    contains:
        "locate/forest/kozel6/kozel_020.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_020.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_21_reblur:
    contains:
        "locate/forest/kozel6/kozel_021.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_021.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat

image batya_kozel_22_reblur:
    contains:
        "locate/forest/kozel6/kozel_022.jpg"
    contains:
        alpha 0
        im.Blur("locate/forest/kozel6/kozel_022.jpg", 0.6)
        block:
            linear 1. alpha 1
            linear 1. alpha 0
            repeat




image homework:
    "locate/home/in_side/2st_floor/anton_room/nightmare/evening_01.jpg"

image fist_0:
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist001.jpg"

image fist_loop:
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist001.jpg"
    pause .08
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist002.jpg"
    pause .08
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist003.jpg"
    pause .08
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist004.jpg"
    pause .08
    "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist005.jpg"
    pause .08

    block:
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist06.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist07.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist08.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist09.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist10.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist11.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist12.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist13.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist14.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist15.jpg"
        pause .12
        "locate/home/in_side/2st_floor/anton_room/nightmare/fist/fist16.jpg"
        pause .12
        repeat

image bunny_nightmare_bg:
    "locate/home/in_side/2st_floor/anton_room/nightmare/Fon_anim/Line_01.jpg"
    pause 0.2
    "locate/home/in_side/2st_floor/anton_room/nightmare/Fon_anim/Line_02.jpg"
    pause 0.2
    "locate/home/in_side/2st_floor/anton_room/nightmare/Fon_anim/Line_03.jpg"
    pause 0.2
    "locate/home/in_side/2st_floor/anton_room/nightmare/Fon_anim/Line_04.jpg"
    pause 0.2
    repeat

image bunny_nightmare_mask:
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_001.png"

    choice:
        pause 2.
    choice:
        pause 3.
    choice:
        pause 4.

    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_002.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_003.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_002.png"
    pause .1
    repeat

image bunny_nightmare_nose:
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_004.png"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_005.png"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny/Zaichik_006.png"
    pause .15
    repeat

image nightmare_klass0:
    "locate/school/in_side/ahaha/klass_00.jpg"

image nightmare_klass2:
    "locate/home/in_side/2st_floor/anton_room/nightmare/klass2.png"

image nightmare_kate1:
    "locate/home/in_side/2st_floor/anton_room/nightmare/Kate_1.png"

image nightmare_kate2:
    "locate/home/in_side/2st_floor/anton_room/nightmare/Kate_2.png"

image nightmare_animation_0:
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/0.jpg"

image nightmare_animation:
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/1.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/02.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/2.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/03.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/3.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/04.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/4.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/05.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/5.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/6.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/7.jpg"
    pause .15
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/8.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/09.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/10.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/11.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/nightmare/bunny2/012.jpg"


image shtora_0:
    "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_00.jpg"

image shtora_0 blur:
    contains:
        "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_00.jpg"
    contains:
        im.Blur("locate/home/in_side/2st_floor/anton_room/shtora/Shtora_00.jpg", .6)
        block:
            linear 1. alpha 0.
            linear 1. alpha 1.
            repeat


image shtora_1:
    "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_01.jpg"

image shtora_2:
    "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_02.jpg"

image shtora_3:
    "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_03.jpg"

image shtora_5:
    "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_05.jpg"


image day2_siluet_only:
    contains:
        alpha 1.
        "locate/home/in_side/2st_floor/anton_room/day2_evening/siluet_01.png"
        pause 0.0
        block:
            pause 1
            linear .5 alpha 0.
            pause .5
            linear .5 alpha 1.
            repeat
    contains:
        alpha 0.
        "locate/home/in_side/2st_floor/anton_room/day2_evening/siluet_02.png"
        pause .5
        block:
            linear .5 alpha 1.
            pause 1
            linear .5 alpha 0.
            pause .5
            repeat
    contains:
        alpha 0.
        "locate/home/in_side/2st_floor/anton_room/day2_evening/siluet_03.png"
        pause 1.0
        block:
            linear .5 alpha 1.
            pause 1
            linear .5 alpha 0.
            pause .5
            repeat
    contains:
        alpha 0.
        "locate/home/in_side/2st_floor/anton_room/day2_evening/siluet_04.png"
        pause 1.5
        block:
            linear .5 alpha 1.
            pause 1
            linear .5 alpha 0.
            pause .5
            repeat

image day2_siluet_room_bg = "locate/home/in_side/2st_floor/anton_room/day2_evening/room_evning_sova.jpg"

image day2_siluet_room = Composite(
    (2899, 1080),
    (0, 0), "day2_siluet_room_bg",
    (0, 0), "day2_siluet_only")

image day2_door5_overlay:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/door05.png"

image day2_door6_overlay:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/door06.png"

image shtora_flash:
    contains:
        "shtora_2"
        alpha 0
        pause .1
        alpha 1
        pause .1
        alpha 0
        pause .1
        alpha 1
        pause .1
        alpha 0
        pause .3
        alpha 1
        "bg_white"

    contains:
        "bg_black"
        alpha 0
        pause 0.8
        linear .5 alpha 1

image kovai:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai_01.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai_02.jpg"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai_03.jpg"
    pause .1
    repeat

image kovai2:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai2_01.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai2_02.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/kovai2_03.png"
    pause .1
    repeat

image window_fon:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/Window_fon.jpg"

image window_fon2:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/Window_fon2.jpg"

image window_plumage:
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_1.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_2.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_1.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_2.png"
    pause .1
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_1.png"
    pause .2
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_2.png"
    pause .2
    "locate/home/in_side/2st_floor/anton_room/day2_evening/glasses/plumage_1.png"
    pause .8
    repeat


image d2_end_idle:
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_001.jpg"

define dt_glass = .1
image d2_end_glasses:
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_002.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_003.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_004.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_005.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_006.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_007.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_008.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_009.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_010.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_011.jpg"
    pause dt_glass
    "locate/home/in_side/2st_floor/anton_room/day2_end/a_012.jpg"

image d2_end_glasses_blink:
    contains:
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_1.jpg"

    contains:
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_02.png"
        pause dt_glass
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_03.png"
        pause dt_glass
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_02.png"
        pause dt_glass
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_01.png"
        pause 4.
        repeat

image final_animation:

    contains:
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_1.jpg"
        pause 1
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_2.jpg"
        pause 2
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_4.jpg"
        pause 1
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_3.jpg"



    contains:
        alpha 0
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_2.jpg"
        linear 1. alpha 1
        alpha 0
        pause 1
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_4.jpg"
        linear 1. alpha 1
        alpha 0
        "locate/home/in_side/2st_floor/anton_room/day2_end/fon_3.jpg"
        linear 1. alpha 1
        alpha 0


    contains:
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_01.png"
        linear 1. alpha 0
        alpha 1.
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_04.png"
        pause 1
        align (.5, .5)
        linear 1. zoom 2. alpha .75



    contains:
        "locate/home/in_side/2st_floor/anton_room/day2_end/Anton_04.png"
        alpha 0
        linear 1. alpha 1
        alpha 0

image semen_ob:
    "locate/home/in_side/2st_floor/anton_room/day2_end/sem_ob.jpg"

image semen_ob2:
    "locate/home/in_side/2st_floor/anton_room/day2_end/sem_ob2.jpg"

image d2_end_rasp:
    "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg"
    align (.5,.5)

image d2_end_rasp_move:
    "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg"
    align (.5,.5)
    linear 3. zoom .675
image d2_end_rasp_zoom:
    "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg"
    align (.5,.5)
    zoom .675


image kk_bg:
    "locate/street/garage/knok1/fon.png"

image kk_hand_1:
    "locate/street/garage/knok1/hand_01.png"

image kk_hand_2:
    "locate/street/garage/knok1/hand_02.png"

image kk_shadow:
    "locate/street/garage/knok1/shadow.png"

image kk_wtf_0:
    "locate/street/garage/knok3/00.png"
image kk_wtf_1:
    "locate/street/garage/knok3/01.png"
image kk_wtf_2:
    "locate/street/garage/knok3/02.png"
image kk_wtf_3:
    "locate/street/garage/knok3/03.png"

image kk_wtf_blink:
    "locate/street/garage/knok3/04.png"
    .1
    "locate/street/garage/knok3/05.png"
    .1
    Null()
    pause 8


image kitchen_wide:
    "locate/home/in_side/1st_floor/kitchen/kitchen_nm.jpg"

image Mom Nightmare1:

    block:
        "sprite/Mom/Nightmare1/01.png"
        .1
        "sprite/Mom/Nightmare1/02.png"
        .1
        "sprite/Mom/Nightmare1/03.png"
        .1
        "sprite/Mom/Nightmare1/04.png"
        .1
        repeat 2

    "Mom Angry b_evening 01 norm ahead 01"

image Mom Nightmare2:
    contains:
        alpha 0
        "Mom Evil b_evening 01 norm ahead"
        .5

        linear .4 alpha 1

    contains:
        "Mom Angry b_evening 01 norm ahead 01"

        pause .5
        parallel:
            "sprite/Mom/Nightmare2/01.png"
            .1
            "sprite/Mom/Nightmare2/02.png"
            .1
            "sprite/Mom/Nightmare2/03.png"
            .1
            "sprite/Mom/Nightmare2/04.png"
            .1
            "sprite/Mom/Nightmare2/03.png"
            .1
            "sprite/Mom/Nightmare2/02.png"
            .1
            "sprite/Mom/Nightmare2/01.png"
            .1

        parallel:
            .0
            linear .8 alpha 0



image Dad Daun:

    contains:
        "sprite/Dad/Daun/b_evening/1_body/01.png"


    contains:
        "sprite/Dad/Daun/b_evening/2_eyes/norm/ahead/01.png"
        1.
        "sprite/Dad/Daun/b_evening/2_eyes/norm/ahead/02.png"
        .1
        "sprite/Dad/Daun/b_evening/2_eyes/norm/ahead/03.png"
        .1
        "sprite/Dad/Daun/b_evening/2_eyes/norm/ahead/02.png"
        .1
        "sprite/Dad/Daun/b_evening/2_eyes/norm/ahead/01.png"
        choice:
            6.
        choice:
            7.
        choice:
            8.
        repeat


    contains:
        "sprite/Dad/Daun/b_evening/2_eyes/norm/daun_brov1.png"
        .05
        "sprite/Dad/Daun/b_evening/2_eyes/norm/daun_brov2.png"
        .05
        "sprite/Dad/Daun/b_evening/2_eyes/norm/daun_brov1.png"
        .05
        "sprite/Dad/Daun/b_evening/2_eyes/norm/daun_brov2.png"
        .05
        Null()
        choice:
            3.
        choice:
            4.
        choice:
            5.
        repeat 4


    contains:
        "sprite/Dad/Daun/b_evening/3_mouth/01.png"
        .1
        "sprite/Dad/Daun/b_evening/3_mouth/02.png"
        .1
        "sprite/Dad/Daun/b_evening/3_mouth/03.png"
        .1
        "sprite/Dad/Daun/b_evening/3_mouth/04.png"
        2.
        repeat

image focus_lines:
    "locate/street/Focus/Fok_1.png"
    .2
    "locate/street/Focus/Fok_2.png"
    .2
    repeat

image focus_lines_bright:
    im.MatrixColor("locate/street/Focus/Fok_1.png", im.matrix.brightness(1.00))
    .2
    im.MatrixColor("locate/street/Focus/Fok_2.png", im.matrix.brightness(1.00))
    .2
    repeat


image Dad Normal m_night_winter 02 norm aside blur:
    im.Blur("sprite/Dad/Normal/m_night_winter/1_body/02.png", 1.5)

default mom_evil_mouth = False
image Mom Evil Nightmare:
    ConditionSwitch(
        "mom_evil_mouth", "Mom Evil b_evening 01 norm ahead 01",
        "True", "Mom Evil b_evening 01 norm ahead",
        )


image evening_screamer:
    "locate/home/in_side/2st_floor/anton_room/evening_Screeam.jpg"
    align (.5,.5)
    block:
        linear .05 zoom 1.010
        linear .05 zoom 1.005

        linear .05 zoom 1.015
        linear .05 zoom 1.010

        linear .05 zoom 1.020
        linear .05 zoom 1.015

        linear .05 zoom 1.025
        linear .05 zoom 1.020

        linear .05 zoom 1.030
        linear .05 zoom 1.025

        repeat


image day1_threshold 1 = "locate/home/out_side/threshold/001.png"
image day1_threshold 2 = "locate/home/out_side/threshold/002.png"
image day1_threshold 3 = "locate/home/out_side/threshold/003.png"
image day1_threshold 4 = "locate/home/out_side/threshold/004.png"
image day1_threshold 5 = "locate/home/out_side/threshold/005.png"
image day1_threshold loop:
    "day1_threshold 1" with Dissolve(.5)
    1.5
    "day1_threshold 2" with Dissolve(.5)
    1.5
    "day1_threshold 3" with Dissolve(.5)
    1.5
    repeat

image day1_threshold = "locate/home/out_side/threshold/threshold.png"

image day1_kovai_0 = "locate/home/in_side/2st_floor/anton_room/Anton_kovai00.png"
image day1_kovai_1 = "locate/home/in_side/2st_floor/anton_room/Anton_kovai01.png"
image day1_kovai_2 = "locate/home/in_side/2st_floor/anton_room/Anton_kovai02.png"
image day1_kovai_3 = "locate/home/in_side/2st_floor/anton_room/Anton_kovai03.png"

image day1_worms = "locate/home/out_side/worms.png"

image day2_stairs_1 = "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
image day2_stairs_2 = "locate/home/in_side/1st_floor/hall/h1/str.png"

image day2_myth = "locate/school/out_side/school_coner/garage.png"

image day1_corpse = "locate/home/in_side/2st_floor/anton_room/Grany.png"
image day1_ants = "locate/home/in_side/2st_floor/anton_room/Grany1.png"
image day1_nightmare = "locate/home/in_side/2st_floor/anton_room/Grany3.png"
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
