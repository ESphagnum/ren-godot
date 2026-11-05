define starfall_endpos = [
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

transform starfall_1(idx):
    animation
    subpixel True
    pos (starfall_endpos[idx][0], -225)
    anchor (.5, .5)
    i*0.15
    linear (starfall_endpos[idx][1]+225) / 1200 ypos starfall_endpos[idx][1]
    block:
        easeout 1.5 xoffset -25
        ease 1.5 xoffset 25 yoffset -25
        ease 1.5 xoffset 0 yoffset 0
        repeat

transform starfall_2(idx):
    animation
    subpixel True
    pos (starfall_endpos[idx][0], -225)
    anchor (.5, .5)
    i*0.15
    linear (starfall_endpos[idx][1]+225) / 1200 ypos starfall_endpos[idx][1]
    block:
        ease 5 xoffset 5*3 yoffset 0
        ease 5 xoffset -5*3 yoffset -5*3
        ease 5 xoffset 0 yoffset 5*3
        ease 5 xoffset -5*3 yoffset 0
        repeat

transform starfall_3(idx):
    animation
    subpixel True
    pos (starfall_endpos[idx][0], -225)
    anchor (.5, .5)
    i*0.15
    linear (starfall_endpos[idx][1]+225) / 1200 ypos starfall_endpos[idx][1]
    parallel:
        ease 4.5 xoffset -25
        ease 4.5 xoffset 25
        repeat
    parallel:
        ease 2.5 yoffset -15
        ease 2.5 yoffset 15
        repeat

transform starfall_4(idx, pos):
    animation
    zoom .5
    subpixel True
    pos pos
    anchor (.5, .5)
    alpha 0
    parallel:
        idx * 0.25
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

label d4_starfall:
    show d4_color_star as s1 onlayer master1 at starfall_1 (0)
    pause .05
    show d4_color_star as s2 onlayer master1 at starfall_2 (1)
    pause .05
    show d4_color_star as s3 onlayer master1 at starfall_3 (2)
    pause .05
    show d4_color_star as s4 onlayer master1 at starfall_1 (3)
    pause .05
    show d4_color_star as s5 onlayer master1 at starfall_2 (4)
    pause .05
    show d4_color_star as s6 onlayer master1 at starfall_3 (5)
    pause .05
    show d4_color_star as s7 onlayer master1 at starfall_1 (6)
    pause .05
    show d4_color_star as s8 onlayer master1 at starfall_2 (7)
    pause .05
    show d4_color_star as s9 onlayer master1 at starfall_3 (8)
    pause .05

    pause .25

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss1 onlayer master1 at starfall_4(0, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss2 onlayer master1 at starfall_4(1, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss3 onlayer master1 at starfall_4(2, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss4 onlayer master1 at starfall_4(3, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss5 onlayer master1 at starfall_4(4, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss6 onlayer master1 at starfall_4(5, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss7 onlayer master1 at starfall_4(6, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss8 onlayer master1 at starfall_4(7, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss9 onlayer master1 at starfall_4(8, (xpos, ypos))

    $ xpos = int(renpy.random.random() * (1920-200) + 100)
    $ ypos = int(renpy.random.random() * (1080-500) + 100)
    show d4_color_star as ss10 onlayer master1 at starfall_4(9, (xpos, ypos))

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
