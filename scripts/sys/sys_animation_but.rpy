init:
    $ x1 = 724
    $ x2 = 986
    $ x3 = 1673
    $ x4 = 310
    $ x5 = 965
    $ y1 = 821
    $ y2 = 821
    $ y3 = 821
    $ y4 = 126
    $ y5 = 126

    $ pref_b_x1 = 320
    $ pref_b_y1 = 245
    $ pref_b_x2 = 320
    $ pref_b_y2 = 347

    $ image_for_screen_navigation = "interface/save_load_menu/000.jpg"

transform conf_fon:
    alpha 0.0
    linear 0.35 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.35 alpha 0.0

transform conf_fon_slow:
    alpha 0.0
    linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.35 alpha 0.0


transform mm_but_lang:
    on idle:
        linear 0.25 alpha 0.5 ypos 0
    on hover:
        parallel:
            linear 0.25 alpha 1.0 ypos -20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)-20
            linear 0.01 xpos 0 ypos -20


transform mm_but:
    alpha 0.0
    on idle:
        linear 0.25 alpha 0.0 ypos 0 xpos 0
    on hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
            linear 0.01 xpos 0 ypos 0

    on selected_hover:
        alpha 1.0 ypos 0 xpos 0
    on selected_idle:
        alpha 1.0 ypos 0 xpos 0
    on insensitive:
        linear 0.05 alpha 0.2
    on hide:
        alpha 0.0 ypos 0 xpos 0

transform mm_bg_diss_1to0:
    alpha 1.0
    linear 3.0 alpha 0.0

transform mm_bg_diss_0to1:
    alpha 0.0
    linear 3.0 alpha 1.0

transform mm_elements:
    on show:
        alpha 0.0
        linear 3.0
        linear 1.55 alpha 1.0
    on replace:
        alpha 0.0
        linear 0.3
        linear 1.0 alpha 1.0

transform qm_elements:
    alpha 0.0
    linear 0.1
    linear 1.55 alpha 1.0

transform filepic_elements:
    alpha 0.45
    on insensitive:
        linear 0.05 alpha 0.15

transform pref_elements:
    alpha 1.0
    on insensitive:
        linear 0.05 alpha 0.15

transform filepic_but:
    ypos 0 xpos 0
    on hover:
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos 0 ypos 0
    on selected_hover:
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos 0 ypos 0

transform filepic_but1:
    alpha 1.0 ypos y1 xpos x1
    on hover:
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1+renpy.random.randint(-5,5) ypos y1+renpy.random.randint(-5,5)
        linear 0.01 xpos x1 ypos y1

transform filepic_but2:
    alpha 1.0 ypos y2 xpos x2
    on hover:
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2+renpy.random.randint(-5,5) ypos y2+renpy.random.randint(-5,5)
        linear 0.01 xpos x2 ypos y2

transform filepic_but3:
    alpha 1.0 ypos y3 xpos x3
    on hover:
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3+renpy.random.randint(-5,5) ypos y3+renpy.random.randint(-5,5)
        linear 0.01 xpos x3 ypos y3

transform filepic_but4:
    alpha 1.0 ypos y4 xpos x4
    on hover:
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
        linear 0.01 xpos x4 ypos y4
    on selected_idle:
        linear 0.45 alpha 0.0
    on replaced:
        linear 0.25 alpha 0.0

transform filepic_but4_2:
    alpha 0.0
    on idle:
        linear 0.25 alpha 0.0 ypos y4 xpos x4
    on hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4+renpy.random.randint(-5,5) ypos y4+renpy.random.randint(-5,5)
            linear 0.01 xpos x4 ypos y4

    on selected_idle:
        linear 0.05 alpha 1.0
    on insensitive:
        linear 0.05 alpha 0.2
    on replaced:
        linear 0.25 alpha 0.0

transform filepic_but5:
    alpha 1.0 ypos y5 xpos x5
    on hover:
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
        linear 0.01 xpos x5 ypos y5
    on selected_idle:
        linear 0.45 alpha 0.0
    on replaced:
        linear 0.25 alpha 0.0

transform filepic_but5_2:
    alpha 0.0
    on idle:
        linear 0.25 alpha 0.0 ypos y5 xpos x5
    on hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5+renpy.random.randint(-5,5) ypos y5+renpy.random.randint(-5,5)
            linear 0.01 xpos x5 ypos y5

    on selected_idle:
        linear 0.05 alpha 1.0
    on insensitive:
        linear 0.05 alpha 0.2
    on replaced:
        linear 0.25 alpha 0.0

transform for_show_save_load:
    alpha 0.0
    linear 0.95
    linear 0.15 alpha 1.0

transform for_show_quick_menu_3:
    alpha 0.0
    linear 0.3
    linear 0.15 alpha 1.0

transform for_yes_no_10:
    alpha 0.0
    linear 1.0
    linear 0.15 alpha 1.0

transform pref_but1:
    alpha 1.0 ypos pref_b_y1 xpos pref_b_x1
    on idle:
        linear 0.25 ypos pref_b_y1 xpos pref_b_x1 alpha 1.0
    on hover:
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1 ypos pref_b_y1
    on selected_idle:
        linear 0.25 ypos pref_b_y1 xpos pref_b_x1 alpha 1.0
    on selected_hover:
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x1 ypos pref_b_y1
    on replaced:
        linear 0.25 alpha 1.0

transform pref_but1_2:
    alpha 0.0
    on idle:
        linear 0.25 alpha 0.0 ypos pref_b_y1 xpos pref_b_x1
    on hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1 ypos pref_b_y1

    on selected_idle:
        linear 0.25 alpha 0.0 ypos pref_b_y1 xpos pref_b_x1
    on selected_hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x1 ypos pref_b_y1
    on insensitive:
        linear 0.05 alpha 0.2
    on replaced:
        linear 0.25 alpha 0.0


transform pref_but2:
    alpha 1.0 ypos pref_b_y2 xpos pref_b_x2
    on idle:
        linear 0.25 alpha 1.0 ypos pref_b_y2 xpos pref_b_x2
    on hover:
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2 ypos pref_b_y2
    on selected_idle:
        linear 0.25 alpha 1.0 ypos pref_b_y2 xpos pref_b_x2
    on selected_hover:
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
        linear 0.01 xpos pref_b_x2 ypos pref_b_y2
    on replaced:
        linear 0.25 alpha 1.0

transform pref_but2_2:
    alpha 0.0
    on idle:
        linear 0.25 alpha 0.0 ypos pref_b_y2 xpos pref_b_x2
    on hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2 ypos pref_b_y2

    on selected_idle:
        linear 0.25 alpha 0.0 ypos pref_b_y2 xpos pref_b_x2
    on selected_hover:
        parallel:
            linear 0.35 alpha 1.0
            block:
                linear 10.0
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.2
                linear 0.05 alpha 0.7
                linear 0.05 alpha 0.4
                linear 0.05 alpha 0.1
                linear 0.05 alpha 0.3
                linear 0.05 alpha 1.0
                linear 6.0
                repeat
        parallel:
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2+renpy.random.randint(-5,5) ypos pref_b_y2+renpy.random.randint(-5,5)
            linear 0.01 xpos pref_b_x2 ypos pref_b_y2
    on insensitive:
        linear 0.05 alpha 0.2
    on replaced:
        linear 0.25 alpha 0.0

transform for_demo_end:
    alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.1
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.2
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.2
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.1
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.3
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.1
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.0
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.1
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.2
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 0.4
    linear 0.01 xpos pref_b_x1+renpy.random.randint(-5,5) ypos pref_b_y1+renpy.random.randint(-5,5) alpha 1.0

transform for_look_buttons:
    alpha 0.0
    xalign 0.5 yalign 0.5
    linear 0.45 alpha 0.5

    on show:
        linear 0.45 alpha 0.5

    on hide:
        linear 0.45 alpha 0.0
    on idle:
        linear 0.15 alpha 0.5
    on hover:
        linear 0.15 alpha 1.0

transform for_look_buttons_adv:
    alpha 0.0
    xanchor 0.5 yanchor 0.5
    linear 0.45 alpha 0.5

    on show:
        linear 0.45 alpha 0.5

    on hide:
        linear 0.45 alpha 0.0
    on idle:
        linear 0.15 alpha 0.5
    on hover:
        linear 0.15 alpha 1.0

transform for_hide_buttons:
    alpha 0.5
    xalign 0.5 yalign 0.5
    linear 0.45 alpha 0.0

transform for_hide_buttons_adv:

    xanchor 0.5 yanchor 0.5
    linear 0.45 alpha 0.0

transform for_look_buttons_0:
    alpha 0.0
    linear 0.45 alpha 1.0

transform for_look_buttons_1:
    alpha 1.0
    xalign 0.5 yalign 0.5
    on show:
        alpha 0.0
        linear 0.45 alpha 0.5
    on hide:
        alpha 0.5
        linear 0.45 alpha 0.0
    on idle:
        linear 0.15 alpha 0.5
    on hover:
        linear 0.15 alpha 1.0

transform for_look_buttons_2:
    alpha 1.0

transform for_look_buttons_3:
    alpha 0.0
    linear 0.3
    linear 0.45 alpha 1.0

transform for_say_buttons:
    alpha 0.5
    on idle:
        linear 0.15 alpha 0.5
    on hover:
        linear 0.15 alpha 1.0
    on selected_idle:
        alpha 1.0




    on selected_hover:
        linear 0.15 alpha 1.0

transform for_say_buttons_new:
    alpha 0.5
    on idle:
        linear 0.5 alpha .0 zoom 1.5
        zoom 1
        linear .5 alpha 1.
        repeat
    on hover:
        linear 0.15 alpha 1.0 zoom 1
    on selected_idle:
        alpha 1.0
    on selected_hover:
        linear 0.15 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
