init:
    $ generate_dark_version = True


    $ generate_img('Wolf', 'Normal', 'b', '00')
    $ generate_img('Wolf', 'Normal', 'b', '01')

    $ generate_img('Wolf', 'Normal', 'm', '00')
    $ generate_img('Wolf', 'Normal', 'm', '01')
    $ generate_img('Wolf', 'Normal', 'm', '05')



    image Wolf Normal m 02:
        "sprite/Wolf/Normal/m/1_body/02.png"
        .1
        "sprite/Wolf/Normal/m/1_body/03.png"
        .1
        "sprite/Wolf/Normal/m/1_body/04.png"
        .1
        repeat

    $ generate_dark_version = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
