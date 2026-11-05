init python:
    generate_dark_version = True


init:



    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '00', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'serious', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'angry', 'ahead', '06')

    image Polina Adult b_day_winter 01 smile ahead 06 dark 30:
        contains:
            "sprite/Polina/Adult/b_day_winter/1_body/01.png"
        contains:
            "sprite/Polina/Adult/b_day_winter/2_eyes/smile/ahead/01.png"
            .1
            "sprite/Polina/Adult/b_day_winter/2_eyes/smile/ahead/02.png"
            .1
            "sprite/Polina/Adult/b_day_winter/2_eyes/smile/ahead/03.png"
            .1
            "sprite/Polina/Adult/b_day_winter/2_eyes/smile/ahead/02.png"
            .1
            "sprite/Polina/Adult/b_day_winter/2_eyes/smile/ahead/01.png"
            block:
                choice:
                    5.
                choice:
                    6.
                choice:
                    7.
            repeat
        contains:
            "sprite/Polina/Adult/b_day_winter/3_mouth/06.png"
        contains:
            AlphaMask(Solid("#0004"), "sprite/Polina/Adult/b_day_winter/1_body/01.png")

    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '01', 'smile2', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'angry', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'angry', 'ahead', '06')


    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'sad', 'ahead', '06')


    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'serious', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'serious', 'ahead', '06')


    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile', 'ahead', '06')


    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '02', 'smile2', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'b_day_winter', '03', 'smile2', 'ahead', '06')


    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'serious', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '01', 'smile2', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'serious', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '02', 'smile2', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'sad', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'serious', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile', 'ahead', '06')

    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '00')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '01')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '02')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '03')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '04')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '05')
    $ generate_img('Polina', 'Adult', 'm_day_winter', '03', 'smile2', 'ahead', '06')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
