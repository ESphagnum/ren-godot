init:
    pass


    image d5_slaughter_bg_owl = "extra/ep5/fon1.png"
    image d5_slaughter_bg_noowl = "extra/ep5/fon2.png"

    image d5_slaughter_owl 0 = "extra/ep5/owl1.png"
    image d5_slaughter_owl 1 = "extra/ep5/owl2.png"
    image d5_slaughter_owl 2 = "extra/ep5/owl3.png"
    image d5_slaughter_owl 3 = "extra/ep5/owl4.png"
    image d5_slaughter_owl alive:
        "d5_slaughter_owl 2"
        1.0
        "d5_slaughter_owl 1" with Dissolve(.25)
        .5
        "d5_slaughter_owl 2" with Dissolve(.25)
        .25
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
