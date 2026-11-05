image snow1 = SnowBlossom("effect/snow/s001.png", count=3, yspeed=(1300, 1400), xspeed=(-10, 10), border=50, start=50, distribution="linear")
image snow2 = SnowBlossom("effect/snow/s002.png", count=3, yspeed=(1200, 1300), xspeed=(-10, 10), border=50, start=30, distribution="linear")
image snow3 = SnowBlossom("effect/snow/s003.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=10, distribution="linear")
image snow4 = SnowBlossom("effect/snow/s004.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, distribution="linear")
image snow5 = SnowBlossom("effect/snow/s005.png", count=25, yspeed=(650, 770), xspeed=(-10, 10), border=50, start=1, distribution="linear")

image snow6 = SnowBlossom("effect/snow/s006.png", count=85, yspeed=(385, 400), xspeed=(-10, 10), border=50, start=1, distribution="linear")
image snow7 = SnowBlossom("effect/snow/s007.png", count=240, yspeed=(300, 380), xspeed=(-10, 10), border=50, start=1, distribution="linear")
image snow8 = SnowBlossom("effect/snow/s008.png", count=275, yspeed=(265, 290), xspeed=(-10, 10), border=50, start=1, distribution="linear")
image snow9 = SnowBlossom("effect/snow/s009.png", count=335, yspeed=(265, 270), xspeed=(-10, 10), border=50, start=1, distribution="linear")

image snow10 = SnowBlossom("effect/snow/s010.png", count=500, yspeed=(150, 190), xspeed=(-10, 0), border=50, start=1, distribution="linear")
image snow11 = SnowBlossom("effect/snow/s011.png", count=700, yspeed=(100, 115), xspeed=(-10, 0), border=50, start=1, distribution="linear")
image snow12 = SnowBlossom("effect/snow/s012.png", count=1950, yspeed=(100, 110), xspeed=(-10, 0), border=50, start=1, distribution="linear")
image snow13 = SnowBlossom("effect/snow/s013.png", count=3500, yspeed=(90, 100), xspeed=(-10, 0), border=50, start=1, distribution="linear")
image snow14 = SnowBlossom("effect/snow/s014.png", count=9000, yspeed=(60, 70), xspeed=(-10, 0), border=50, start=1, distribution="linear")

default show_snow_1 = False
default show_snow_2 = False
default show_snow_3 = False

init python:
    def SnowDelay(arg):
        global delay1
        if arg == 1:
            return 1920.0/(delay1*1.00)
        if arg == 2:
            return 1920.0/(delay1*0.91)
        if arg == 3:
            return 1920.0/(delay1*0.82)
        if arg == 4:
            return 1920.0/(delay1*0.64)
        if arg == 5:
            return 1920.0/(delay1*0.40)
        return None

default xsped1 = 1920.0/(30*1.00)
default xsped2 = 1920.0/(30*0.91)
default xsped3 = 1920.0/(30*0.82)
default xsped4 = 1920.0/(30*0.64)
default xsped5 = 1920.0/(30*0.40)




default walkaway__delay = 100
default walkaway__delay2 = 20
default walkaway__delay3 = 20

image snow_walkaway_lay1:
    ConditionSwitch(
        "show_snow_1", LiveComposite((1920, 1080),
            
            
            (0, 0), SnowBlossom("effect/snow/s003.png", count=1, yspeed=(650, 770), xspeed=(SnowDelay(5), SnowDelay(5) + 20), border=50, start=walkaway__delay3 + 10, fast = False, distribution="linear"),
            
            (0, 0), SnowBlossom("effect/snow/s005.png", count=4, yspeed=(650, 770), xspeed=(SnowDelay(5), SnowDelay(5) + 20), border=50, start=walkaway__delay3 + 1, fast = False, distribution="linear")),
        "True", Null())

image snow_walkaway_lay2:
    ConditionSwitch(
        "show_snow_2", LiveComposite((1920, 1080),
            (0, 0), SnowBlossom("effect/snow/s006.png", count=25, yspeed=(385, 400), xspeed=(SnowDelay(4), SnowDelay(4) + 20), border=50, start=walkaway__delay2, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s007.png", count=24, yspeed=(300, 380), xspeed=(SnowDelay(4), SnowDelay(4) + 20), border=50, start=walkaway__delay2, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s008.png", count=27, yspeed=(265, 290), xspeed=(SnowDelay(4), SnowDelay(4) + 20), border=50, start=walkaway__delay2, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s009.png", count=33, yspeed=(265, 270), xspeed=(SnowDelay(4), SnowDelay(4) + 20), border=50, start=walkaway__delay2, fast = False, distribution="linear")),
        "True", Null())

image snow_walkaway_lay3:
    ConditionSwitch(
        "show_snow_3", LiveComposite((1920, 1080),
            (0, 0), SnowBlossom("effect/snow/s010.png", count=150, yspeed=(150, 190), xspeed=(SnowDelay(3), SnowDelay(3) + 20), border=50, start=walkaway__delay, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s011.png", count=200, yspeed=(100, 115), xspeed=(SnowDelay(3), SnowDelay(3) + 20), border=50, start=walkaway__delay, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s012.png", count=600, yspeed=(100, 110), xspeed=(SnowDelay(2), SnowDelay(2) + 20), border=50, start=walkaway__delay, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s013.png", count=1050, yspeed=(90, 100), xspeed=(SnowDelay(2), SnowDelay(2) + 20), border=50, start=walkaway__delay, fast = False, distribution="linear")
            
            ),
        "True", Null())




image snow_scare_reverted_1:
    ConditionSwitch(
        "show_snow_1", LiveComposite((1920, 1080),
            
            
            (0, 0), SnowBlossom("effect/snow/s003.png", count=1, yspeed=(650, 770), xspeed=(xsped5, xsped5 + 20), border=50, start=0 + 10, fast = False, distribution="linear"),
            
            (0, 0), SnowBlossom("effect/snow/s005.png", count=4, yspeed=(650, 770), xspeed=(xsped5, xsped5 + 20), border=50, start=0 + 1, fast = False, distribution="linear")),
        "True", Null())

image snow_scare_reverted_2:
    ConditionSwitch(
        "show_snow_2", LiveComposite((1920, 1080),
            (0, 0), SnowBlossom("effect/snow/s006.png", count=25, yspeed=(385, 400), xspeed=(xsped4, xsped4 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s007.png", count=24, yspeed=(300, 380), xspeed=(xsped4, xsped4 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s008.png", count=27, yspeed=(265, 290), xspeed=(xsped4, xsped4 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s009.png", count=33, yspeed=(265, 270), xspeed=(xsped4, xsped4 + 20), border=50, start=0, fast = False, distribution="linear")),
        "True", Null())

image snow_scare_reverted_3:
    ConditionSwitch(
        "show_snow_3", LiveComposite((1920, 1080),
            (0, 0), SnowBlossom("effect/snow/s010.png", count=150, yspeed=(150, 190), xspeed=(xsped3, xsped3 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s011.png", count=200, yspeed=(100, 115), xspeed=(xsped3, xsped3 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s012.png", count=600, yspeed=(100, 110), xspeed=(xsped2, xsped2 + 20), border=50, start=0, fast = False, distribution="linear"),
            (0, 0), SnowBlossom("effect/snow/s013.png", count=1050, yspeed=(90, 100), xspeed=(xsped2, xsped2 + 20), border=50, start=0, fast = False, distribution="linear")
            
            ),
        "True", Null())



image snow_boiz_1:
    LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s001.png", count=3, yspeed=(1300, 1400), xspeed=(-10, 10), border=50, start=50, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s002.png", count=3, yspeed=(1200, 1300), xspeed=(-10, 10), border=50, start=30, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s003.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=10, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s004.png", count=3, yspeed=(1000, 1100), xspeed=(-10, 10), border=50, start=0, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s005.png", count=25, yspeed=(650, 770), xspeed=(-10, 10), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s006.png", count=85, yspeed=(385, 400), xspeed=(-10, 10), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s007.png", count=240, yspeed=(300, 380), xspeed=(-10, 10), border=50, start=1, distribution="linear"))

image snow_boiz_2:
    LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s008.png", count=275, yspeed=(265, 290), xspeed=(-10, 10), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s009.png", count=335, yspeed=(265, 270), xspeed=(-10, 10), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s010.png", count=500, yspeed=(150, 190), xspeed=(-10, 0), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s011.png", count=700, yspeed=(100, 115), xspeed=(-10, 0), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s012.png", count=1950, yspeed=(100, 110), xspeed=(-10, 0), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s013.png", count=3500, yspeed=(90, 100), xspeed=(-10, 0), border=50, start=1, distribution="linear"),
        (0, 0), SnowBlossom("effect/snow/s014.png", count=9000, yspeed=(60, 70), xspeed=(-10, 0), border=50, start=1, distribution="linear"))























image snow_day_4:
    LiveComposite((1920, 1080),
        (0, 600), SnowBlossom("effect/snow/s011.png", count=5000, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=False, distribution="linear"),
        (0, 600), SnowBlossom("interface/main_meny/partikl_001.png", count=3200, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=False, distribution="linear"))

image snow_day_4_home:
    LiveComposite((1920, 1080),
        (0, 600), SnowBlossom("effect/snow/s011.png", count=500, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=False, distribution="linear"),
        (0, 600), SnowBlossom("interface/main_meny/partikl_001.png", count=320, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=False, distribution="linear"))

image snow_night_4 = LiveComposite((1920, 1080),
    (0, 0), SnowBlossom("effect/snow/s014.png", count=500, yspeed=(40, 50), xspeed=(220, 210), border=150, start=300, distribution="linear"),
    (0, 0), SnowBlossom("effect/snow/s013.png", count=200, yspeed=(50, 80), xspeed=(240, 230), border=100, start=150, distribution="linear"),
    (0, 0), SnowBlossom("effect/snow/s012.png", count=200, yspeed=(60, 90), xspeed=(240, 230), border=100, start=150, distribution="linear"),
    (0, 0), SnowBlossom("effect/snow/s007.png", count=50, yspeed=(80, 100), xspeed=(240, 225), border=80, start=40, distribution="linear"),
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
