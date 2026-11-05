init:
    $ generate_dark_version = True

    $ generate_img('ByashaOld', 'Normal', 'b_day', '01', 'normal', 'ahead', '00')
    $ generate_img('ByashaOld', 'Normal', 'b_day', '01', 'normal', 'ahead', '01')

    $ generate_img('ByashaOld', 'Normal', 'm_day', '01', 'normal', 'ahead', '00')
    $ generate_img('ByashaOld', 'Normal', 'm_day', '01', 'normal', 'ahead', '01')

    $ generate_img('ByashaOld', 'Sad', 'b_day', '01', 'normal', 'aside', '01')
    $ generate_img('ByashaOld', 'Sad', 'b_day', '01', 'normal', 'aside', '02')

    $ generate_img('ByashaOld', 'Sad', 'b_day', '02', 'profile', 'aside', '00')
    $ generate_img('ByashaOld', 'Sad', 'b_day', '03', 'profile', 'aside', '00')

    $ generate_img('ByashaOld', 'Shock', 'b_day', '01', 'shock', 'ahead', '00')
    $ generate_img('ByashaOld', 'Shock', 'b_day', '01', 'shock', 'ahead', '01')
    $ generate_img('ByashaOld', 'Shock', 'b_day', '02', 'shock', 'ahead', '00')
    $ generate_img('ByashaOld', 'Shock', 'b_day', '02', 'shock', 'ahead', '01')

    $ generate_img('ByashaOld', 'Scared', 'b_day', '01', 'shock', 'ahead', '00')
    $ generate_img('ByashaOld', 'Scared', 'b_day', '01', 'shock', 'ahead', '01')

    image ByashaOld Sad b_day 04 = "sprite/ByashaOld/Sad/b_day/1_body/04.png"
    image byashaold_sad_04_d = AlphaMask(Solid("#0008"), "sprite/ByashaOld/Sad/b_day/1_body/04.png")
    image ByashaOld Sad b_day 04 dark:
        contains:
            "ByashaOld Sad b_day 04"
        contains:
            "byashaold_sad_04_d"











    $ generate_img('ByashaOld', 'back', 'b_day', '01', 'normal', 'ahead', '00')
    $ generate_img('ByashaOld', 'back', 'b_day', '01', 'normal', 'ahead', '01')

    image byasha_b_body = "locate/psycho/b/1_body/01.png"
    image byasha_b_mouth = "locate/psycho/b/3_mouth/01.png"
    image byasha_b_eyes_1 = "locate/psycho/b/2_eyes/01.png"
    image byasha_b_eyes_2 = "locate/psycho/b/2_eyes/02.png"
    image byasha_b_eyes_3 = "locate/psycho/b/2_eyes/03.png"
    image byasha_b_eyes:
        "byasha_b_eyes_1"
        choice:
            5.
        choice:
            6.
        choice:
            6.5
        "byasha_b_eyes_2"
        .1
        "byasha_b_eyes_3"
        .1
        "byasha_b_eyes_2"
        .1
        repeat

    image ByashaOld Psy idle:
        contains:
            "byasha_b_body"
        contains:
            "byasha_b_eyes"
    image ByashaOld Psy talk:
        contains:
            "byasha_b_body"
        contains:
            "byasha_b_eyes"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
