init:
    $ generate_img('Dad', 'Mask', 'b_night', '00')
    $ generate_img('Dad', 'Mask', 'm_night', '00')

    $ generate_img('Dad', 'Normal', 'm_day', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Normal', 'm_day', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Normal', 'm_day', '02', 'norm', 'aside')
    $ generate_img('Dad', 'Normal', 'm_day', '02', 'norm', 'ahead')
    $ generate_img('Dad', 'Normal', 'b_day', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Normal', 'b_day', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Normal', 'm_day', '01', 'norm', 'ahead', '01', size=(723, 1080), eyes_size=(723, 1080))
    $ generate_img('Dad', 'Normal', 'm_night_winter', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Normal', 'm_night_winter', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Normal', 'm_day_winter', '01', 'norm', 'aside')

    $ generate_img('Dad', 'Normal', 'm_day_winter', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Normal', 'm_day_winter', '02', 'norm2', 'aside', size=(723, 1125), eyes_size=(723, 1125))
    $ generate_img('Dad', 'Normal', 'm_day_winter', '02', 'norm2', 'ahead', size=(723, 1125), eyes_size=(723, 1125))
    $ generate_img('Dad', 'Normal', 'm_evening', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Normal', 'm_evening', '01', 'norm', 'ahead')



    $ generate_img('Dad', 'Angry', 'm_day', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Angry', 'm_day', '01', 'norm', 'aside')

    $ generate_img('Dad', 'Angry', 'b_day', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Angry', 'b_day', '01', 'norm', 'aside')

    $ generate_img('Dad', 'Angry', 'm_night_winter', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Angry', 'm_night_winter', '01', 'norm', 'ahead')
    $ generate_img('Dad', 'Angry', 'm_evening', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Angry', 'm_evening', '01', 'norm', 'ahead')

    $ generate_img('Dad', 'Happy', 'm_day', '00', 'norm', 'aside')
    $ generate_img('Dad', 'Happy', 'm_day', '00', 'norm', 'ahead')

    $ generate_img('Dad', 'Happy', 'm_evening', '01', 'norm', 'aside')
    $ generate_img('Dad', 'Happy', 'm_evening', '01', 'norm', 'ahead')

    $ generate_img('Dad', 'Happy', 'b_day', '01', 'norm', 'ahead')


    $ generate_img('Dad', 'Happy', 'b_evening', '01')
    $ generate_img('Dad', 'Normal', 'b_evening', '01', "norm", "ahead")
    $ generate_img('Dad', 'Angry', 'b_evening', '01', "norm", "ahead")



    image dad car aside:
        Animation("locate/incar/car/dad_car/aside/01.png", 4.10, "locate/incar/car/dad_car/aside/02.png", 0.10, "locate/incar/car/dad_car/aside/03.png", 0.10, "locate/incar/car/dad_car/aside/02.png", 0.10, "locate/incar/car/dad_car/aside/01.png", 6)

    image dad car ahead:
        Animation("locate/incar/car/dad_car/ahead/01.png", 4.10, "locate/incar/car/dad_car/ahead/02.png", 0.10, "locate/incar/car/dad_car/ahead/03.png", 0.10, "locate/incar/car/dad_car/ahead/02.png", 0.10, "locate/incar/car/dad_car/ahead/01.png", 6)

    image dad car_d aside:
        Animation("locate/incar/dark_car/dad_car_dark/aside/01.png", 4.10, "locate/incar/dark_car/dad_car_dark/aside/02.png", 0.10, "locate/incar/dark_car/dad_car_dark/aside/03.png", 0.10, "locate/incar/dark_car/dad_car_dark/aside/02.png", 0.10, "locate/incar/dark_car/dad_car_dark/aside/01.png", 6)

    image dad car_d ahead:
        Animation("locate/incar/dark_car/dad_car_dark/ahead/01.png", 4.10, "locate/incar/dark_car/dad_car_dark/ahead/02.png", 0.10, "locate/incar/dark_car/dad_car_dark/ahead/03.png", 0.10, "locate/incar/dark_car/dad_car_dark/ahead/02.png", 0.10, "locate/incar/dark_car/dad_car_dark/ahead/01.png", 6)

    image Dad Old = "sprite/dad/father_old.png"
    image Dad Old2 = "sprite/dad/father_old2.png"
    image Dad Old3 = "sprite/dad/father_old3.png"




transform dad_left:
    xpos 625-1920 ypos 0 xzoom -1.0

transform dad_income:
    xzoom -1.0
    alpha 0.0
    ypos 0
    xpos 275-1920
    linear 0.5 alpha 0.5 xpos 400-1920 ypos 20
    linear 0.5 alpha 1.0 xpos 500-1920 ypos 0
    linear 0.5 alpha 1.0 xpos 575-1920 ypos 20
    linear 0.5 alpha 1.0 xpos 625-1920 ypos 0

transform dad_out:
    xzoom -1.0
    alpha 1.0
    ypos 0
    xpos 625-1920
    linear 0.5 alpha 1.00 xpos 700-1920 ypos 20
    linear 0.5 alpha 0.75 xpos 800-1920 ypos 0
    linear 0.5 alpha 0.50 xpos 900-1920 ypos 20
    linear 0.5 alpha 0.00 xpos 1000-1920 ypos 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
