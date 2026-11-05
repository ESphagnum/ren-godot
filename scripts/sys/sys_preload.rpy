init -1:

    $ logo = _("interface/main_meny/logo.png")


    $ preferences.wait_voice = True


    default eyes_visible = False

    default preferences.fullscreen = True


    $ _game_menu_screen = "quick_menu"

    $ set_delay = [0,10,20,30,40,50,60,70,80,90,100]


    default persistent.first_start = True

    default persistent.animal_unlock = [False,False,False,False,False]
    default have_item = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default my_choose = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default talk_m = [False,False]
    default try_take_number = False
    default find_witness = [False,False]






























    default reserch = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]







    default Flags = FlagVault()



















    default SceneFlags = FlagVault()
init offset = -1



init python:
    def wait_animation(time):
        global doehal
        doehal = 0
        renpy.show_screen("for_timer_uni", time)

    def reset_reserch():
        global reserch
        reserch = []
        for i in range(30):
            reserch.append(False)

    def reset_item_and_choice():
        global dictionary_list, have_item, my_choose, talk_m
        dictionary_list = []
        have_item = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        my_choose = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        talk_m =  [False,False]
        reset_reserch()
        
        global Flags
        Flags.Reset()

    def SetParSpeed(delay):
        global delay1
        global delay2
        global delay3
        global delay4
        global delay5
        delay1 = delay
        delay2 = delay1 - delay1 * 9/100
        delay3 = delay1 - delay1 * 18/100
        delay4 = delay1 - delay1 * 36/100
        delay5 = delay1 - delay1 * 60/100
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
