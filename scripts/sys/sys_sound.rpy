init -2 python:
    renpy.music.register_channel("sfx", "sound", False)


    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)
    renpy.music.register_channel("test_seven", "sfx", False)

    renpy.music.register_channel("fon", "sfx", loop=True)
    renpy.music.register_channel("ambient", "sfx", loop=True)
    renpy.music.register_channel("ambient2", "sfx", loop=True)
    renpy.music.register_channel("ambient3", "sfx", loop=True)

    renpy.music.register_channel("music2", "music", loop=True)


    renpy.music.register_channel("wtf", None, loop=False)

    renpy.music.register_channel("lamp_sfx", "sfx", False)


    def random_f_step_sound():
        step_sound = renpy.random.randint(1,4)
        if step_sound == 1:
            step_sound = "sounds/steps/snow_stepF01.ogg"
        elif step_sound == 2:
            step_sound = "sounds/steps/snow_stepF02.ogg"
        elif step_sound == 3:
            step_sound = "sounds/steps/snow_stepF03.ogg"
        elif step_sound == 4:
            step_sound = "sounds/steps/snow_stepF04.ogg"
        renpy.sound.play(step_sound,"test_one")

    def random_s_step_sound():
        step_sound = renpy.random.randint(1,3)
        if step_sound == 1:
            step_sound = "sounds/steps/snow_stepS01.ogg"
        elif step_sound == 2:
            step_sound = "sounds/steps/snow_stepS02.ogg"
        elif step_sound == 3:
            step_sound = "sounds/steps/snow_stepS03.ogg"
        renpy.sound.play(step_sound,"test_one")

    def random_list_sound(lst):
        renpy.sound.play(renpy.random.choice(lst),"test_one")

    lamp_volume = 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
