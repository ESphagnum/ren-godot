init:
    image bg_grey = Solid("#777")

    transform walkaway(diff_x, diff_y=0, appear=0.01, loop_mod=1.0):
        yalign 1.0
        xpos 900
        yoffset 0
        xoffset 1420 + diff_x
        parallel:
            linear 0.95*loop_mod yoffset 10+diff_y
            linear 0.95*loop_mod yoffset 20+diff_y*2
            linear 1.0*loop_mod yoffset 10+diff_y
            linear 1.0*loop_mod yoffset 0
            repeat

        parallel:
            linear appear xoffset diff_x
            block:
                linear 3.1*loop_mod xoffset 20+diff_x
                linear 3.0*loop_mod xoffset 40+diff_x
                linear 2.9*loop_mod xoffset 50+diff_x
                linear 3.1*loop_mod xoffset 40+diff_x
                repeat

    default romka_walkaway_state = 0
    image romka_walkaway:
        Composite((549, 1080),
            (0,0), "locate/street/walkaway/Romka.png",
            (0,0), ConditionSwitch(
                "romka_walkaway_state == 1", "locate/street/walkaway/Romka2.png",
                "True", Null(),)
            )

    image anton_walkaway:
        "locate/street/walkaway/Antonio.png"

    image hands_walkaway:
        "locate/street/walkaway/Antonio_hand.png"

    default byasha_walkaway_state = 0
    image byasha_walkaway:
        Composite((636, 1080),
            (0,0), "locate/street/walkaway/Basha.png",
            (0,0), ConditionSwitch(
                "byasha_walkaway_state == 1", "locate/street/walkaway/Basha2.png",
                "byasha_walkaway_state == 2", "locate/street/walkaway/Basha3.png",
                "True", Null(),)
            )

    image koshmar:
        "effect/koshmar/Polosi_crepy_01.jpg"
        pause .2
        "effect/koshmar/Polosi_crepy_02.jpg"
        pause .2
        "effect/koshmar/Polosi_crepy_03.jpg"
        pause .2
        "effect/koshmar/Polosi_crepy_04.jpg"
        pause .2
        repeat

    transform walkaway2(diffY, appear=0.01):
        parallel:
            linear .5 yoffset 10 + diffY
            linear .5 yoffset 20 + diffY*2
            linear .5 yoffset 10 + diffY
            linear .5 yoffset 0
            repeat

        parallel:
            zoom .8
            easein appear zoom 1.

            block:
                linear 3.2 zoom .98
                linear 2.9 zoom 1.0
                repeat

        parallel:
            alpha .0
            linear appear*0.25 alpha 1.

    image scare_reverted:
        im.Blur("locate/forest/scary/Scary_fon.jpg", 0.6)
        subpixel True
        xalign 0.5
        yalign 1.0
        xzoom -1.0

    image scare_reverted_blur:
        im.Blur("locate/forest/scary/Scary_fon.jpg", 2.5)
        subpixel True
        xalign 0.5
        yalign 1.0
        xzoom -1.0

    image rom_walk2_1:
        "locate/street/walkaway/big_Rom_1.png"
        align (1.,1.)

    image ant_walk2_1:
        "locate/street/walkaway/big_Anton_1.png"
        align (1.,1.)

    image byash_walk2_1:
        "locate/street/walkaway/big_Byash_1.png"
        align (1.,1.)

    image rom_walk2_2:
        "locate/street/walkaway/big_Rom_2.png"
        align (1.,1.)

    image ant_walk2_2:
        "locate/street/walkaway/big_Anton_2.png"
        align (1.,1.)

    image byash_walk2_2:
        "locate/street/walkaway/big_Byash_2.png"
        align (1.,1.)

    image ant_walk2_3:
        "locate/street/walkaway/big_Anton_3.png"
        align (1.,1.)

    image ant_walk2_4:
        "locate/street/walkaway/big_Anton_4.png"
        align (1.,1.)

    image ant_walk2_5:
        "locate/street/walkaway/big_Anton_5.png"
        align (1.,1.)

    image dark_walk:
        "locate/street/walkaway/Dark.png"

    image fox_walkaway:
        "locate/street/walkaway/big_Fox.png"

    image foxanton_walkaway:
        "locate/street/walkaway/Antonio_2.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
