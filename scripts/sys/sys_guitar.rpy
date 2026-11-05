init:
    define guitar_strings_states = ["idle", "pulled", "shake1", "shake2"]
    define STRING_IDLE = 0
    define STRING_PULL = 1
    define STRING_SHAKE = 2
    define STRING_SHAKE2 = 3

    define guitar_strings_duration1 = 0.25
    define guitar_strings_duration2 = 0.75
    define guitar_strings_duration_half = 0.05

init -1 python:

    class GuitarString:
        def __init__(self, num):
            self.num = num
            self.imgs = [
            "guitar_string_{}_idle".format(num),
            "guitar_string_{}_pulled".format(num),
            "guitar_string_{}_shake1".format(num),
            "guitar_string_{}_shake2".format(num),
        ]
            self.SetState( STRING_IDLE )  
        
        def SetState(self, new_state):
            global guitar_strings_duration1, guitar_strings_duration2
            self.state = new_state
            self.disp = renpy.displayable( self.imgs[self.state] )
            
            if self.state == STRING_SHAKE:
                self.cd = guitar_strings_duration1
            elif self.state == STRING_SHAKE2:
                self.cd = guitar_strings_duration2
            else:
                self.cd = None
        
        def UpdateCD(self, dt):
            
            if self.cd is None:
                return
            self.cd -= dt
            
            if self.cd > 0:
                return
            
            if self.state == STRING_SHAKE2:
                self.SetState(STRING_IDLE)
                return
            if self.state == STRING_SHAKE:
                self.SetState(STRING_SHAKE2)
                return
            
            raise Exception("Something wrong with guitar string! {} string, {} state, timer triggered".format(self.num, self.state))

init python:
    def set_string_1_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(1).SetState(STRING_PULL)
        renpy.restart_interaction()
    def set_string_2_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(2).SetState(STRING_PULL)
        renpy.restart_interaction()
    def set_string_3_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(3).SetState(STRING_PULL)
        renpy.restart_interaction()
    def set_string_4_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(4).SetState(STRING_PULL)
        renpy.restart_interaction()
    def set_string_5_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(5).SetState(STRING_PULL)
        renpy.restart_interaction()
    def set_string_6_pulled(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(6).SetState(STRING_PULL)
        renpy.restart_interaction()

    def set_string_1_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(1).SetState(STRING_SHAKE)
        renpy.restart_interaction()
    def set_string_2_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(2).SetState(STRING_SHAKE)
        renpy.restart_interaction()
    def set_string_3_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(3).SetState(STRING_SHAKE)
        renpy.restart_interaction()
    def set_string_4_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(4).SetState(STRING_SHAKE)
        renpy.restart_interaction()
    def set_string_5_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(5).SetState(STRING_SHAKE)
        renpy.restart_interaction()
    def set_string_6_shake(trans, st, at):
        global guitar_minigame_engine
        if guitar_minigame_engine is None:
            return
        guitar_minigame_engine.GetString(6).SetState(STRING_SHAKE)
        renpy.restart_interaction()

init python:

    guitar_minigame_engine = None
    class GuitarMinigameData:
        def __init__(self):
            global guitar_minigame_engine
            guitar_minigame_engine = self
            self.strings = [
            GuitarString(1),
            GuitarString(2),
            GuitarString(3),
            GuitarString(4),
            GuitarString(5),
            GuitarString(6),
        ]
            self._last_st = 0
        
        def GetString(self, num):
            if not (1 <= num <= 6):
                return
            
            return self.strings[num -1]
        
        def UpdateStrings(self, dt):
            if self.strings[0].cd is not None:
                print("up strings", dt)
            for s in self.strings:
                s.UpdateCD(dt)


    class GuitarMinigameEngine(renpy.Displayable):
        def __init__(self, data):
            renpy.Displayable.__init__(self)
            
            self.data = data
        
        def render(self, width, height, st, at):
            
            
            deltaTime = (st - self.data._last_st)
            self.data._last_st = st
            
            if self.data.strings[0].cd is not None:
                print("render", deltaTime)
            self.data.UpdateStrings(deltaTime)
            
            render = renpy.Render(width, height)
            
            for i in range(6):
                render.blit(self.data.GetString(i+1).disp.render(width, height, st, at), (0, 0))
            
            
            
            
            
            
            
            
            
            
            
            
            renpy.redraw(self, 0)
            return render

screen scr_guitar_minigame_strings(data):
    layer "master"
    add GuitarMinigameEngine(data)

label guitar_minigame:


    scene guitar_bg
    show guitar_candles
    show guitar_body

    show Polina guitar up 001
    show Ant guitar normal 004 zorder 1

    $ data = GuitarMinigameData()
    show screen scr_guitar_minigame_strings(data)

    show guitarplay ant_6_up


    show bg_black zorder 100:
        alpha .1
    show layer master:
        matrixcolor BrightnessMatrix(-0.05)
    with Dissolve(.5)

    window show
    call event_m_polina_guitar.intro_talk
    window hide

    call event_m_polina_guitar.r1_polina_before



    label guitar_minigame.r1:
    play sound "music/guitarm/masquerade_guitar_phrase_1s.ogg"
    show guitarplay polina_song_1
    pause 3.22

    call guitar_minigame.pol_play_6

    play sound "music/guitarm/masquerade_guitar_phrase_2s.ogg"
    show guitarplay polina_song_2
    pause 3.91

    call guitar_minigame.pol_play_4

    play sound "music/guitarm/masquerade_guitar_phrase_3s.ogg"
    show guitarplay polina_song_3
    pause 2.47

    call guitar_minigame.pol_play_3

    play sound "music/guitarm/masquerade_guitar_phrase_4s.ogg"
    show guitarplay polina_song_4
    pause 1.55

    call guitar_minigame.pol_play_2

    call event_m_polina_guitar.r1_polina_after

    play sound "music/guitarm/masquerade_guitar_phrase_1s.ogg"
    show guitarplay anton_song_1
    pause 3.22
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 6 and guitar_string_choice != "correct":
        jump guitar_minigame.r1_fail

    play sound "music/guitarm/masquerade_guitar_phrase_2s.ogg"
    show guitarplay anton_song_2
    pause 3.91
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 4 and guitar_string_choice != "correct":
        jump guitar_minigame.r1_fail

    play sound "music/guitarm/masquerade_guitar_phrase_3s.ogg"
    show guitarplay anton_song_3
    pause 2.47
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 3 and guitar_string_choice != "correct":
        jump guitar_minigame.r1_fail

    play sound "music/guitarm/masquerade_guitar_phrase_4s.ogg"
    show guitarplay anton_song_4
    pause 1.55
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 2 and guitar_string_choice != "correct":
        jump guitar_minigame.r1_fail

    show guitarplay ant_6_up

    call event_m_polina_guitar.r2_polina_before



    label guitar_minigame.r2:
    play sound "music/guitarm/masquerade_guitar_phrase_5s.ogg"
    show guitarplay polina_song_5
    pause 4.77
    call guitar_minigame.pol_play_1

    play sound "music/guitarm/masquerade_guitar_phrase_6s.ogg"
    show guitarplay polina_song_6
    pause 2.62
    call guitar_minigame.pol_play_5

    play sound "music/guitarm/masquerade_guitar_phrase_7s.ogg"
    show guitarplay polina_song_7
    pause 3.23
    call guitar_minigame.pol_play_6

    play sound "music/guitarm/masquerade_guitar_phrase_8s.ogg"
    show guitarplay polina_song_8
    pause 4.12
    call guitar_minigame.pol_play_5

    play sound "music/guitarm/masquerade_guitar_phrase_9s.ogg"
    show guitarplay polina_song_9
    pause 4.44
    call guitar_minigame.pol_play_1

    call event_m_polina_guitar.r2_polina_after

    play sound "music/guitarm/masquerade_guitar_phrase_5s.ogg"
    show guitarplay anton_song_5
    pause 4.77
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 1 and guitar_string_choice != "correct":
        jump guitar_minigame.r2_fail

    play sound "music/guitarm/masquerade_guitar_phrase_6s.ogg"
    show guitarplay anton_song_6
    pause 2.62
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 5 and guitar_string_choice != "correct":
        jump guitar_minigame.r2_fail

    play sound "music/guitarm/masquerade_guitar_phrase_7s.ogg"
    show guitarplay anton_song_7
    pause 3.23
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 6 and guitar_string_choice != "correct":
        jump guitar_minigame.r2_fail

    play sound "music/guitarm/masquerade_guitar_phrase_8s.ogg"
    show guitarplay anton_song_8
    pause 4.12
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 5 and guitar_string_choice != "correct":
        jump guitar_minigame.r2_fail

    play sound "music/guitarm/masquerade_guitar_phrase_9s.ogg"
    show guitarplay anton_song_9
    pause 4.44
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 1 and guitar_string_choice != "correct":
        jump guitar_minigame.r2_fail

    show guitarplay ant_6_up

    call event_m_polina_guitar.r3_polina_before



    label guitar_minigame.r3:
    play sound "music/guitarm/masquerade_guitar_phrase_10s.ogg"
    show guitarplay polina_song_10
    pause 2.59
    call guitar_minigame.pol_play_3

    play sound "music/guitarm/masquerade_guitar_phrase_11s.ogg"
    show guitarplay polina_song_11
    pause 4.02
    call guitar_minigame.pol_play_4

    play sound "music/guitarm/masquerade_guitar_phrase_12s.ogg"
    show guitarplay polina_song_12
    pause 1.69
    call guitar_minigame.pol_play_2

    play sound "music/guitarm/masquerade_guitar_phrase_13s.ogg"
    show guitarplay polina_song_13
    pause 5.08
    call guitar_minigame.pol_play_6

    play sound "music/guitarm/masquerade_guitar_phrase_14s.ogg"
    show guitarplay polina_song_14
    pause 2.67
    call guitar_minigame.pol_play_1

    play sound "music/guitarm/masquerade_guitar_phrase_15s.ogg"
    show guitarplay polina_song_15
    pause 1.69
    call guitar_minigame.pol_play_2

    call event_m_polina_guitar.r3_polina_after

    play sound "music/guitarm/masquerade_guitar_phrase_10s.ogg"
    show guitarplay anton_song_10
    pause 2.59
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 3 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    play sound "music/guitarm/masquerade_guitar_phrase_11s.ogg"
    show guitarplay anton_song_11
    pause 4.02
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 4 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    play sound "music/guitarm/masquerade_guitar_phrase_12s.ogg"
    show guitarplay anton_song_12
    pause 1.69
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 2 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    play sound "music/guitarm/masquerade_guitar_phrase_13s.ogg"
    show guitarplay anton_song_13
    pause 5.08
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 6 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    play sound "music/guitarm/masquerade_guitar_phrase_14s.ogg"
    show guitarplay anton_song_14
    pause 2.67
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 1 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    play sound "music/guitarm/masquerade_guitar_phrase_15s.ogg"
    show guitarplay anton_song_15
    pause 1.69
    call guitar_minigame.anton_choice
    if guitar_string_choice == "abort":
        jump guitar_minigame.abort
    if guitar_string_choice != 2 and guitar_string_choice != "correct":
        jump guitar_minigame.r3_fail

    show guitarplay ant_6_up


    jump guitar_minigame.success




    label guitar_minigame.pol_play_1:
        hide guitarplay
        show guitarplay pol_1_prep

        pause 0.25


        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_1.ogg"]
        show guitarplay pol_1_play

        pause 1.5
        return

    label guitar_minigame.pol_play_2:
        hide guitarplay
        show guitarplay pol_2_prep

        pause 0.25


        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_2.ogg"]
        show guitarplay pol_2_play

        pause 1.5
        return

    label guitar_minigame.pol_play_3:
        hide guitarplay
        show guitarplay pol_3_prep

        pause 0.25


        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_3.ogg"]
        show guitarplay pol_3_play

        pause 1.5
        return

    label guitar_minigame.pol_play_4:
        hide guitarplay
        show guitarplay pol_4_prep

        pause 0.25


        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_4.ogg"]
        show guitarplay pol_4_play

        pause 1.5
        return

    label guitar_minigame.pol_play_5:
        hide guitarplay
        show guitarplay pol_5_prep

        pause 0.25


        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_5.ogg"]
        show guitarplay pol_5_play

        pause 1.5
        return

    label guitar_minigame.pol_play_6:
        hide guitarplay
        show guitarplay pol_6_prep

        pause 0.25



        pause 0.5
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_6.ogg"]
        show guitarplay pol_6_play

        pause 1.5
        return

    label guitar_minigame.ant_play_1:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_1.ogg"]
        show guitarplay ant_1_play

        pause 1.5
        return

    label guitar_minigame.ant_play_2:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_2.ogg"]
        show guitarplay ant_2_play

        pause 1.5
        return

    label guitar_minigame.ant_play_3:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_3.ogg"]
        show guitarplay ant_3_play

        pause 1.5
        return

    label guitar_minigame.ant_play_4:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_4.ogg"]
        show guitarplay ant_4_play

        pause 1.5
        return

    label guitar_minigame.ant_play_5:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_5.ogg"]
        show guitarplay ant_5_play

        pause 1.5
        return

    label guitar_minigame.ant_play_6:
        play sound ["<silence 0.3>", "music/guitarm/masquerade_guitar_end_6.ogg"]
        show guitarplay ant_6_play

        pause 1.5
        return

    label guitar_minigame.anton_choice:
        pause 1.0

        hide guitarplay
        hide screen scr_guitar_minigame_strings

        call screen d5_guitar_minigame()
        show screen scr_guitar_minigame_strings(data)
        $ guitar_string_choice = _return
        if guitar_string_choice == "abort":
            return
        if guitar_string_choice == "correct":
            return

        $ lbl = "guitar_minigame.ant_play_" + str(guitar_string_choice)
        call expression lbl
        return


    label guitar_minigame.r1_fail:
        hide guitarplay
        show guitarplay ant_6_up
        window show
        call event_m_polina_guitar.r_fail
        window hide

        hide guitarplay
        show guitarplay pol_6_up
        with Dissolve(.5)
        jump guitar_minigame.r1

    label guitar_minigame.r2_fail:
        hide guitarplay
        show guitarplay ant_6_up
        window show
        call event_m_polina_guitar.r_fail
        window hide

        hide guitarplay
        show guitarplay pol_6_up
        with Dissolve(.5)
        jump guitar_minigame.r2

    label guitar_minigame.r3_fail:
        hide guitarplay
        show guitarplay ant_6_up
        window show
        call event_m_polina_guitar.r_fail
        window hide

        hide guitarplay
        show guitarplay pol_6_up
        with Dissolve(.5)
        jump guitar_minigame.r3

    label guitar_minigame.abort:
        hide guitarplay
        show guitarplay ant_6_up
        jump event_m_polina_guitar.abort

    label guitar_minigame.success:
        hide guitarplay
        show guitarplay ant_6_up
        jump event_m_polina_guitar.success
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
