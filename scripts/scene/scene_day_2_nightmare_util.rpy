define olya_pos = -350
define olya_center = -olya_pos
define dad_pos = 1150
define dad_center = -dad_pos
define mom_pos = -1725
define mom_center = -mom_pos
define bg_loop = 5450
define bg_center = -bg_loop / 2 + 960

define bg_black_alpha = .3

default dad_sprite = "Dad Happy b_evening 01"
default mom_sprite = "Mom Happy b_evening 01 norm ahead"
default olya_sprite = "Olya Happy b_evening 00 good ahead 07"

default camera_xoffset = dad_center
default camera_move_to = None
default camera_transition_time = 0

default olya_y = 250
default olya_special_flag = False
default olya_special_xoffset = 0

default bg_special_flag = None

default is_tapped = ""
label bunny2_happy_family:
    if camera_move_to is None:
        scene kitchen_wide:
            xalign .5
            xoffset camera_xoffset

        if bg_special_flag == True:
            show bg_black:
                alpha 0
                linear 6 alpha bg_black_alpha
            $ bg_special_flag = False

        elif bg_special_flag == False:
            show bg_black:
                alpha bg_black_alpha

        show expression dad_sprite:
            yalign 1.
            xalign .5
            xoffset dad_pos + camera_xoffset
        show expression mom_sprite:
            yalign 1.
            xalign .5
            xoffset mom_pos + camera_xoffset

        if not olya_special_flag:
            show expression olya_sprite:
                yalign 1.
                xalign .5
                yoffset olya_y
                xoffset olya_pos + camera_xoffset + olya_special_xoffset
        else:

            show expression olya_sprite:
                yalign 1.
                xalign .5
                yoffset olya_y
                xoffset olya_pos + camera_xoffset

                linear .1 xoffset olya_pos + camera_xoffset - 100
                .5
                xoffset olya_pos + camera_xoffset - 80
                .1
                xoffset olya_pos + camera_xoffset - 110
                linear .5 xoffset olya_pos + camera_xoffset - 150
                .1
                linear .05 xoffset olya_pos + camera_xoffset - 160
                .2
                linear .05 xoffset olya_pos + camera_xoffset - 170
                .2
                linear .1 xoffset olya_pos + camera_xoffset - 200
                xoffset olya_pos + camera_xoffset - 180
                linear .5 xoffset olya_pos + camera_xoffset - 300

                linear .5 xoffset olya_pos + camera_xoffset - 350
                .1
                linear .05 xoffset olya_pos + camera_xoffset - 410
                .2
                linear .05 xoffset olya_pos + camera_xoffset - 570
                .2
                linear .1 xoffset olya_pos + camera_xoffset - 700

                xoffset olya_pos + camera_xoffset - 650

                linear .5 xoffset olya_pos + camera_xoffset - 900
                .5
                linear .5 xoffset olya_pos + camera_xoffset - 900 - 50
                .1
                linear .05 xoffset olya_pos + camera_xoffset - 900 - 60
                .1
                linear .05 xoffset olya_pos + camera_xoffset - 900 - 70
                .1
                linear .05 xoffset olya_pos + camera_xoffset - 900 - 80
                1.
                ease 2. xoffset olya_pos + camera_xoffset - 1050
            $ olya_special_xoffset = -1050
            $ olya_special_flag = False
    else:

        scene kitchen_wide:
            xalign .5
            xoffset camera_xoffset
            linear camera_transition_time xoffset camera_move_to

        if bg_special_flag == True:
            show bg_black:
                alpha 0
                linear 6 alpha bg_black_alpha
            $ bg_special_flag = False

        elif bg_special_flag == False:
            show bg_black:
                alpha bg_black_alpha

        show expression dad_sprite:
            yalign 1.
            xalign .5
            xoffset dad_pos + camera_xoffset
            linear camera_transition_time xoffset dad_pos + camera_move_to
        show expression mom_sprite:
            yalign 1.
            xalign .5
            xoffset mom_pos + camera_xoffset
            linear camera_transition_time xoffset mom_pos + camera_move_to
        show expression olya_sprite:
            yalign 1.
            xalign .5
            yoffset olya_y
            xoffset olya_pos + camera_xoffset + olya_special_xoffset
            linear camera_transition_time xoffset olya_pos + camera_move_to + olya_special_xoffset

        pause 0.01
        $ camera_xoffset = camera_move_to
        $ camera_move_to = None

    if mom_sprite == "Mom Nightmare1":
        $ mom_sprite = "Mom Angry b_evening 01 norm ahead 01"

    if mom_sprite == "Mom Nightmare2":
        $ mom_sprite = "Mom Evil b_evening 01 norm ahead"

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
