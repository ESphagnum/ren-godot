

init:
    image menu001_1:
        contains:
            "interface/main_meny/meny_001.png"
            yalign 0.0
            xpos 0
            linear set_delay[2] xpos 1980
            linear set_delay[2] xpos 3960
            xpos -3961
            linear set_delay[2] xpos -1981
            linear set_delay[2] xpos 0
            repeat

    image menu001_2:
        contains:
            "interface/main_meny/meny_001.png"
            yalign 0.0
            xpos -3961
            linear set_delay[2] xpos -1981
            linear set_delay[2] xpos 0
            xpos 0
            linear set_delay[2] xpos 1980
            linear set_delay[2] xpos 3960
            repeat

    image menu002_1:
        contains:
            "interface/main_meny/meny_002.png"
            yalign 0.0
            xpos 0
            linear set_delay[8] xpos -1981
            linear set_delay[8] xpos -3961
            xpos 3960
            linear set_delay[8] xpos 1980
            linear set_delay[8] xpos 0
            repeat

    image menu002_2:
        contains:
            "interface/main_meny/meny_002.png"
            yalign 0.0
            xpos 3960
            linear set_delay[8] xpos 1980
            linear set_delay[8] xpos 0
            xpos 0
            linear set_delay[8] xpos -1981
            linear set_delay[8] xpos -3961
            repeat

    image chastichka_1_1 = SnowBlossom("interface/main_meny/partikl_001.png", count=60, yspeed=(-20, 20), xspeed=(100, 140), border=1, start=0, fast=False)

    image chastichka_1_2 = SnowBlossom("interface/main_meny/partikl_001.png", count=40, yspeed=(-20, 20), xspeed=(120, 150), border=1, start=0, fast=False)

    image chastichka_2 = SnowBlossom("interface/main_meny/partikl_002.png", count=300, yspeed=(-20, 20), xspeed=(50, 90), border=1, start=0, fast=False)

    image bg_menu_preferences:
        contains:
            alpha 0.0
            "interface/preferences/000.jpg"
            linear 0.15 alpha 1.0
            pause 0.10
            "interface/preferences/001.jpg"
            pause 0.10
            "interface/preferences/002.jpg"
            pause 0.10
            "interface/preferences/003.jpg"
            pause 0.10
            "interface/preferences/004.jpg"
            pause 0.10
            "interface/preferences/005.jpg"
            pause 0.10
            "interface/preferences/006.jpg"
            pause 0.10
            "interface/preferences/007.jpg"
            pause 0.10
            "interface/preferences/008.jpg"
            pause 0.10
            "interface/preferences/009.jpg"

    image bg_menu_quick:
        contains:
            alpha 0.0
            "interface/quick_menu/01.png"
            linear 0.15 alpha 1.0
            pause 0.10
            "interface/quick_menu/02.png"
            pause 0.10
            "interface/quick_menu/03.png"

    image bg_menu_yes_no:
        contains:
            alpha 0.0
            "interface/yes_no/000.jpg"
            linear 0.15 alpha 1.0
            pause 0.10
            "interface/yes_no/002.jpg"
            pause 0.10
            "interface/yes_no/003.jpg"
            pause 0.10
            "interface/yes_no/006.jpg"
            pause 0.10
            "interface/yes_no/005.jpg"
            pause 0.10
            "interface/yes_no/007.jpg"
            pause 0.10
            "interface/yes_no/008.jpg"
            pause 0.10
            "interface/yes_no/009.jpg"

    image bg_menu_save_load:
        contains:
            alpha 0.0
            "interface/save_load_menu/000.jpg"
            linear 0.15 alpha 1.0
            pause 0.10
            "interface/save_load_menu/001.jpg"
            pause 0.10
            "interface/save_load_menu/002.jpg"
            pause 0.10
            "interface/save_load_menu/003.jpg"
            pause 0.10
            "interface/save_load_menu/004.jpg"
            pause 0.10
            "interface/save_load_menu/007.jpg"
            pause 0.10
            "interface/save_load_menu/008.jpg"

    image bg_menu_about:
        contains:
            alpha 0.0
            "interface/about_menu/001.jpg"
            linear 0.15 alpha 1.0
            pause 0.10
            "interface/about_menu/002.jpg"
            pause 0.10
            "interface/about_menu/003.jpg"
            pause 0.10
            "interface/about_menu/004.jpg"
            pause 0.10
            "interface/about_menu/005.jpg"
            pause 0.10
            "interface/about_menu/006.jpg"
            pause 0.10
            "interface/about_menu/007.jpg"
            pause 0.10
            "interface/about_menu/008.jpg"
            pause 0.10
            "interface/about_menu/009.jpg"
            pause 0.10
            "interface/about_menu/010.jpg"
            pause 0.10

    image main_menu_bg:
        "interface/main_meny/01.png"

        pause 8

        block:
            "interface/main_meny/02.png"
            .1
            "interface/main_meny/03.png"
            .1
            "interface/main_meny/02.png"
            .1
            "interface/main_meny/01.png"
            .1

            pause 8

            repeat 2


        "interface/main_meny/04.png"
        .1
        "interface/main_meny/05.png"
        .1
        "interface/main_meny/04.png"
        .1
        "interface/main_meny/01.png"
        .1

        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
