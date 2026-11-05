init -2 python:
    renpy.music.register_channel("video", loop=False, stop_on_mute=True, tight=False, movie=True)
    renpy.music.register_channel("video1", "video", loop=False, stop_on_mute=True, tight=False, movie=True)
    renpy.music.register_channel("video2", "video", loop=False, stop_on_mute=True, tight=False, movie=True)

image logo_publish = "interface/publish_logo.webp"


label splashscreen:
    stop music

    scene bg_black
    $ renpy.pause(1.0)

    if persistent.first_launch is None:




        show screen initial_language_select()
        show screen initial_language_message_eng()
        $ ui.interact()
        hide screen initial_language_select
        hide screen initial_language_message_eng
        hide screen initial_language_message_rus
        hide screen initial_language_message_chi
        $ persistent.first_launch = True

        scene expression "interface/Lang.jpg"
        show screen Disclaimer
        pause 10
        hide screen Disclaimer
    else:


        scene expression "interface/18plus.png"
        show screen Disclaimer(ypos = 250)
        pause 10
        hide screen Disclaimer

    play sound "sounds/logo.ogg"

    scene expression "logo/001.jpg"
    with Dissolve(.5)
    scene expression "logo/002.jpg"
    pause 0.1
    scene expression "logo/003.jpg"
    pause 0.1
    scene expression "logo/004.jpg"

    pause 2

    scene expression "logo/005.jpg"
    pause 0.1
    scene expression "logo/006.jpg"
    pause .5

    scene expression "logo/007.jpg"
    with Dissolve(.5)

    pause .5

    scene bg_black
    with Dissolve(.5)









    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
