init:
    $ generate_dark_version = True


    $ generate_img('Anya', 'Normal', 'b_day', '00', 'good', 'aside', '01')
    $ generate_img('Anya', 'Normal', 'b_day', '00', 'good', 'aside', '02')


    $ generate_img('Anya', 'Mask', 'b_day', '00', 'good', 'ahead')
    $ generate_img('Anya', 'Mask', 'b_day', '00', 'good', 'aside')

    image Anya dance:
        animation
        "Anya Mask b_day 00 good ahead"
        parallel:
            linear .25 xoffset -25 yoffset -25
            linear .25 xoffset -25 yoffset 0
            linear .25 xoffset 25 yoffset -25
            linear .25 xoffset 25 yoffset 0
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
