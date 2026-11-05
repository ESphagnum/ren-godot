
init:
    image guitar_bg = "minigame/guitar/bg.png"
    image guitar_candles_1 = "minigame/guitar/f01.png"
    image guitar_candles_2 = "minigame/guitar/f02.png"
    image guitar_candles_3 = "minigame/guitar/f03.png"
    image guitar_candles:
        "guitar_candles_1"
        .1
        "guitar_candles_2"
        .1
        "guitar_candles_3"
        .1
        repeat
    image guitar_body = "minigame/guitar/body.png"

    image guitar_button_1 = "minigame/guitar/1.png"
    image guitar_button_2 = "minigame/guitar/2.png"
    image guitar_button_3 = "minigame/guitar/3.png"
    image guitar_button_4 = "minigame/guitar/4.png"
    image guitar_button_5 = "minigame/guitar/5.png"
    image guitar_button_6 = "minigame/guitar/6.png"

    image guitar_string_1_idle = "minigame/guitar/strings/1/01.png"
    image guitar_string_1_pulled = "minigame/guitar/strings/1/02.png"
    image guitar_string_1_shake1 = "minigame/guitar/strings/1/03.png"
    image guitar_string_1_shake2:
        "minigame/guitar/strings/1/04.png"
        "guitar_string_1_idle" with Dissolve (.75)
    image guitar_string_1_shake:
        "guitar_string_1_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_1_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_1_idle" with Dissolve(guitar_strings_duration_half)

    image guitar_string_2_idle = "minigame/guitar/strings/2/01.png"
    image guitar_string_2_pulled = "minigame/guitar/strings/2/02.png"
    image guitar_string_2_shake1 = "minigame/guitar/strings/2/03.png"
    image guitar_string_2_shake2:
        "minigame/guitar/strings/2/04.png"
        "guitar_string_2_idle" with Dissolve (.75)
    image guitar_string_2_shake:
        "guitar_string_2_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_2_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_2_idle" with Dissolve(guitar_strings_duration_half)

    image guitar_string_3_idle = "minigame/guitar/strings/3/01.png"
    image guitar_string_3_pulled = "minigame/guitar/strings/3/02.png"
    image guitar_string_3_shake1 = "minigame/guitar/strings/3/03.png"
    image guitar_string_3_shake2:
        "minigame/guitar/strings/3/04.png"
        "guitar_string_3_idle" with Dissolve (.75)
    image guitar_string_3_shake:
        "guitar_string_3_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_3_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_3_idle" with Dissolve(guitar_strings_duration_half)

    image guitar_string_4_idle = "minigame/guitar/strings/4/01.png"
    image guitar_string_4_pulled = "minigame/guitar/strings/4/02.png"
    image guitar_string_4_shake1 = "minigame/guitar/strings/4/03.png"
    image guitar_string_4_shake2:
        "minigame/guitar/strings/4/04.png"
        "guitar_string_4_idle" with Dissolve (.75)
    image guitar_string_4_shake:
        "guitar_string_4_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_4_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_4_idle" with Dissolve(guitar_strings_duration_half)

    image guitar_string_5_idle = "minigame/guitar/strings/5/01.png"
    image guitar_string_5_pulled = "minigame/guitar/strings/5/02.png"
    image guitar_string_5_shake1 = "minigame/guitar/strings/5/03.png"
    image guitar_string_5_shake2:
        "minigame/guitar/strings/5/04.png"
        "guitar_string_5_idle" with Dissolve (.75)
    image guitar_string_5_shake:
        "guitar_string_5_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_5_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_5_idle" with Dissolve(guitar_strings_duration_half)

    image guitar_string_6_idle = "minigame/guitar/strings/6/01.png"
    image guitar_string_6_pulled = "minigame/guitar/strings/6/02.png"
    image guitar_string_6_shake1 = "minigame/guitar/strings/6/03.png"
    image guitar_string_6_shake2:
        "minigame/guitar/strings/6/04.png"
        "guitar_string_6_idle" with Dissolve (.75)
    image guitar_string_6_shake:
        "guitar_string_6_shake1" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_6_shake2" with Dissolve(guitar_strings_duration_half)
        guitar_strings_duration
        "guitar_string_6_idle" with Dissolve(guitar_strings_duration_half)


init -1:
    define guitar_frame_period = 0.15
    define guitar_frame_period_half = guitar_frame_period * 0.5

    define guitar_frame_period_slow = 0.25
    define guitar_frame_period_slow_half = guitar_frame_period_slow * 0.5

    define guitar_frame_period_fast = 0.04
    define guitar_frame_period_slow_half = guitar_frame_period_fast * 0.5


    image guitarplay ant_1_up = "minigame/guitar/ant_play/1up.png"
    image guitarplay ant_1_down = "minigame/guitar/ant_play/1down.png"
    image guitarplay ant_1_prep = "minigame/guitar/ant_play/1preparation.png"
    image guitarplay ant_1_pull = "minigame/guitar/ant_play/1pull.png"
    image guitarplay ant_1_release = "minigame/guitar/ant_play/1release.png"
    image guitarplay ant_1_play:
        "guitarplay ant_1_prep"
        guitar_frame_period
        "guitarplay ant_1_pull"
        function set_string_1_pulled
        guitar_frame_period
        "guitarplay ant_1_release"
        function set_string_1_shake
    image guitarplay ant_1_play_slow:
        "guitarplay ant_1_prep"
        guitar_frame_period_slow
        "guitarplay ant_1_pull"
        function set_string_1_pulled
        guitar_frame_period_slow
        "guitarplay ant_1_release"
        function set_string_1_shake
    image guitarplay ant_1_play_fast:
        "guitarplay ant_1_prep"
        guitar_frame_period_fast
        "guitarplay ant_1_pull"
        function set_string_1_pulled
        guitar_frame_period_fast
        "guitarplay ant_1_release"
        function set_string_1_shake

    image guitarplay ant_2_up = "minigame/guitar/ant_play/2up.png"
    image guitarplay ant_2_down = "minigame/guitar/ant_play/2down.png"
    image guitarplay ant_2_prep = "minigame/guitar/ant_play/2preparation.png"
    image guitarplay ant_2_pull = "minigame/guitar/ant_play/2pull.png"
    image guitarplay ant_2_release = "minigame/guitar/ant_play/2release.png"
    image guitarplay ant_2_play:
        "guitarplay ant_2_prep"
        guitar_frame_period
        "guitarplay ant_2_pull"
        function set_string_2_pulled
        guitar_frame_period
        "guitarplay ant_2_release"
        function set_string_2_shake
    image guitarplay ant_2_play_slow:
        "guitarplay ant_2_prep"
        guitar_frame_period_slow
        "guitarplay ant_2_pull"
        function set_string_2_pulled
        guitar_frame_period_slow
        "guitarplay ant_2_release"
        function set_string_2_shake
    image guitarplay ant_2_play_fast:
        "guitarplay ant_2_prep"
        guitar_frame_period_fast
        "guitarplay ant_2_pull"
        function set_string_2_pulled
        guitar_frame_period_fast
        "guitarplay ant_2_release"
        function set_string_2_shake

    image guitarplay ant_3_up = "minigame/guitar/ant_play/3up.png"
    image guitarplay ant_3_down = "minigame/guitar/ant_play/3down.png"
    image guitarplay ant_3_prep = "minigame/guitar/ant_play/3preparation.png"
    image guitarplay ant_3_pull = "minigame/guitar/ant_play/3pull.png"
    image guitarplay ant_3_release = "minigame/guitar/ant_play/3release.png"
    image guitarplay ant_3_play:
        "guitarplay ant_3_prep"
        guitar_frame_period
        "guitarplay ant_3_pull"
        function set_string_3_pulled
        guitar_frame_period
        "guitarplay ant_3_release"
        function set_string_3_shake
    image guitarplay ant_3_play_slow:
        "guitarplay ant_3_prep"
        guitar_frame_period_slow
        "guitarplay ant_3_pull"
        function set_string_3_pulled
        guitar_frame_period_slow
        "guitarplay ant_3_release"
        function set_string_3_shake
    image guitarplay ant_3_play_fast:
        "guitarplay ant_3_prep"
        guitar_frame_period_fast
        "guitarplay ant_3_pull"
        function set_string_3_pulled
        guitar_frame_period_fast
        "guitarplay ant_3_release"
        function set_string_3_shake

    image guitarplay ant_4_up = "minigame/guitar/ant_play/4up.png"
    image guitarplay ant_4_down = "minigame/guitar/ant_play/4down.png"
    image guitarplay ant_4_prep = "minigame/guitar/ant_play/4preparation.png"
    image guitarplay ant_4_pull = "minigame/guitar/ant_play/4pull.png"
    image guitarplay ant_4_release = "minigame/guitar/ant_play/4release.png"
    image guitarplay ant_4_play:
        "guitarplay ant_4_prep"
        guitar_frame_period
        "guitarplay ant_4_pull"
        function set_string_4_pulled
        guitar_frame_period
        "guitarplay ant_4_release"
        function set_string_4_shake
    image guitarplay ant_4_play_slow:
        "guitarplay ant_4_prep"
        guitar_frame_period_slow
        "guitarplay ant_4_pull"
        function set_string_4_pulled
        guitar_frame_period_slow
        "guitarplay ant_4_release"
        function set_string_4_shake
    image guitarplay ant_4_play_fast:
        "guitarplay ant_4_prep"
        guitar_frame_period_fast
        "guitarplay ant_4_pull"
        function set_string_4_pulled
        guitar_frame_period_fast
        "guitarplay ant_4_release"
        function set_string_4_shake

    image guitarplay ant_5_up = "minigame/guitar/ant_play/5up.png"
    image guitarplay ant_5_down = "minigame/guitar/ant_play/5down.png"
    image guitarplay ant_5_prep = "minigame/guitar/ant_play/5preparation.png"
    image guitarplay ant_5_pull = "minigame/guitar/ant_play/5pull.png"
    image guitarplay ant_5_release = "minigame/guitar/ant_play/5release.png"
    image guitarplay ant_5_play:
        "guitarplay ant_5_prep"
        guitar_frame_period
        "guitarplay ant_5_pull"
        function set_string_5_pulled
        guitar_frame_period
        "guitarplay ant_5_release"
        function set_string_5_shake
    image guitarplay ant_5_play_slow:
        "guitarplay ant_5_prep"
        guitar_frame_period_slow
        "guitarplay ant_5_pull"
        function set_string_5_pulled
        guitar_frame_period_slow
        "guitarplay ant_5_release"
        function set_string_5_shake
    image guitarplay ant_5_play_fast:
        "guitarplay ant_5_prep"
        guitar_frame_period_fast
        "guitarplay ant_5_pull"
        function set_string_5_pulled
        guitar_frame_period_fast
        "guitarplay ant_5_release"
        function set_string_5_shake

    image guitarplay ant_6_up = "minigame/guitar/ant_play/6up.png"
    image guitarplay ant_6_down = "minigame/guitar/ant_play/6down.png"
    image guitarplay ant_6_prep = "minigame/guitar/ant_play/6preparation.png"
    image guitarplay ant_6_pull = "minigame/guitar/ant_play/6pull.png"
    image guitarplay ant_6_release = "minigame/guitar/ant_play/6release.png"
    image guitarplay ant_6_play:
        "guitarplay ant_6_prep"
        guitar_frame_period
        "guitarplay ant_6_pull"
        function set_string_6_pulled
        guitar_frame_period
        "guitarplay ant_6_release"
        function set_string_6_shake
    image guitarplay ant_6_play_slow:
        "guitarplay ant_6_prep"
        guitar_frame_period_slow
        "guitarplay ant_6_pull"
        function set_string_6_pulled
        guitar_frame_period_slow
        "guitarplay ant_6_release"
        function set_string_6_shake
    image guitarplay ant_6_play_fast:
        "guitarplay ant_6_prep"
        guitar_frame_period_fast
        "guitarplay ant_6_pull"
        function set_string_6_pulled
        guitar_frame_period_fast
        "guitarplay ant_6_release"
        function set_string_6_shake


    image guitarplay pol_1_up = "minigame/guitar/pol_play/1up.png"
    image guitarplay pol_1_down = "minigame/guitar/pol_play/1down.png"
    image guitarplay pol_1_prep = "minigame/guitar/pol_play/1preparation.png"
    image guitarplay pol_1_pull = "minigame/guitar/pol_play/1pull.png"
    image guitarplay pol_1_release = "minigame/guitar/pol_play/1release.png"
    image guitarplay pol_1_play:
        "guitarplay pol_1_prep"
        guitar_frame_period
        "guitarplay pol_1_pull"
        function set_string_1_pulled
        guitar_frame_period
        "guitarplay pol_1_release"
        function set_string_1_shake
    image guitarplay pol_1_play_slow:
        "guitarplay pol_1_prep"
        guitar_frame_period_slow
        "guitarplay pol_1_pull"
        function set_string_1_pulled
        guitar_frame_period_slow
        "guitarplay pol_1_release"
        function set_string_1_shake
    image guitarplay pol_1_play_fast:
        "guitarplay pol_1_prep"
        guitar_frame_period_fast
        "guitarplay pol_1_pull"
        function set_string_1_pulled
        guitar_frame_period_fast
        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_2_up = "minigame/guitar/pol_play/2up.png"
    image guitarplay pol_2_down = "minigame/guitar/pol_play/2down.png"
    image guitarplay pol_2_prep = "minigame/guitar/pol_play/2preparation.png"
    image guitarplay pol_2_pull = "minigame/guitar/pol_play/2pull.png"
    image guitarplay pol_2_release = "minigame/guitar/pol_play/2release.png"
    image guitarplay pol_2_play:
        "guitarplay pol_2_prep"
        guitar_frame_period
        "guitarplay pol_2_pull"
        function set_string_2_pulled
        guitar_frame_period
        "guitarplay pol_2_release"
        function set_string_2_shake
    image guitarplay pol_2_play_slow:
        "guitarplay pol_2_prep"
        guitar_frame_period_slow
        "guitarplay pol_2_pull"
        function set_string_2_pulled
        guitar_frame_period_slow
        "guitarplay pol_2_release"
        function set_string_2_shake
    image guitarplay pol_2_play_fast:
        "guitarplay pol_2_prep"
        guitar_frame_period_fast
        "guitarplay pol_2_pull"
        function set_string_2_pulled
        guitar_frame_period_fast
        "guitarplay pol_2_release"
        function set_string_2_shake

    image guitarplay pol_3_up = "minigame/guitar/pol_play/3up.png"
    image guitarplay pol_3_down = "minigame/guitar/pol_play/3down.png"
    image guitarplay pol_3_prep = "minigame/guitar/pol_play/3preparation.png"
    image guitarplay pol_3_pull = "minigame/guitar/pol_play/3pull.png"
    image guitarplay pol_3_release = "minigame/guitar/pol_play/3release.png"
    image guitarplay pol_3_play:
        "guitarplay pol_3_prep"
        guitar_frame_period
        "guitarplay pol_3_pull"
        function set_string_3_pulled
        guitar_frame_period
        "guitarplay pol_3_release"
        function set_string_3_shake
    image guitarplay pol_3_play_slow:
        "guitarplay pol_3_prep"
        guitar_frame_period_slow
        "guitarplay pol_3_pull"
        function set_string_3_pulled
        guitar_frame_period_slow
        "guitarplay pol_3_release"
        function set_string_3_shake
    image guitarplay pol_3_play_fast:
        "guitarplay pol_3_prep"
        guitar_frame_period_fast
        "guitarplay pol_3_pull"
        function set_string_3_pulled
        guitar_frame_period_fast
        "guitarplay pol_3_release"
        function set_string_3_shake

    image guitarplay pol_4_up = "minigame/guitar/pol_play/4up.png"
    image guitarplay pol_4_down = "minigame/guitar/pol_play/4down.png"
    image guitarplay pol_4_prep = "minigame/guitar/pol_play/4preparation.png"
    image guitarplay pol_4_pull = "minigame/guitar/pol_play/4pull.png"
    image guitarplay pol_4_release = "minigame/guitar/pol_play/4release.png"
    image guitarplay pol_4_play:
        "guitarplay pol_4_prep"
        guitar_frame_period
        "guitarplay pol_4_pull"
        function set_string_4_pulled
        guitar_frame_period
        "guitarplay pol_4_release"
        function set_string_4_shake
    image guitarplay pol_4_play_slow:
        "guitarplay pol_4_prep"
        guitar_frame_period_slow
        "guitarplay pol_4_pull"
        function set_string_4_pulled
        guitar_frame_period_slow
        "guitarplay pol_4_release"
        function set_string_4_shake
    image guitarplay pol_4_play_fast:
        "guitarplay pol_4_prep"
        guitar_frame_period_fast
        "guitarplay pol_4_pull"
        function set_string_4_pulled
        guitar_frame_period_fast
        "guitarplay pol_4_release"
        function set_string_4_shake

    image guitarplay pol_5_up = "minigame/guitar/pol_play/5up.png"
    image guitarplay pol_5_down = "minigame/guitar/pol_play/5down.png"
    image guitarplay pol_5_prep = "minigame/guitar/pol_play/5preparation.png"
    image guitarplay pol_5_pull = "minigame/guitar/pol_play/5pull.png"
    image guitarplay pol_5_release = "minigame/guitar/pol_play/5release.png"
    image guitarplay pol_5_play:
        "guitarplay pol_5_prep"
        guitar_frame_period
        "guitarplay pol_5_pull"
        function set_string_5_pulled
        guitar_frame_period
        "guitarplay pol_5_release"
        function set_string_5_shake
    image guitarplay pol_5_play_slow:
        "guitarplay pol_5_prep"
        guitar_frame_period_slow
        "guitarplay pol_5_pull"
        function set_string_5_pulled
        guitar_frame_period_slow
        "guitarplay pol_5_release"
        function set_string_5_shake
    image guitarplay pol_5_play_fast:
        "guitarplay pol_5_prep"
        guitar_frame_period_fast
        "guitarplay pol_5_pull"
        function set_string_5_pulled
        guitar_frame_period_fast
        "guitarplay pol_5_release"
        function set_string_5_shake

    image guitarplay pol_6_up = "minigame/guitar/pol_play/6up.png"
    image guitarplay pol_6_down = "minigame/guitar/pol_play/6down.png"
    image guitarplay pol_6_prep = "minigame/guitar/pol_play/6preparation.png"
    image guitarplay pol_6_pull = "minigame/guitar/pol_play/6pull.png"
    image guitarplay pol_6_release = "minigame/guitar/pol_play/6release.png"
    image guitarplay pol_6_play:
        "guitarplay pol_6_prep"
        guitar_frame_period
        "guitarplay pol_6_pull"
        function set_string_6_pulled
        guitar_frame_period
        "guitarplay pol_6_release"
        function set_string_6_shake
    image guitarplay pol_6_play_slow:
        "guitarplay pol_6_prep"
        guitar_frame_period_slow
        "guitarplay pol_6_pull"
        function set_string_6_pulled
        guitar_frame_period_slow
        "guitarplay pol_6_release"
        function set_string_6_shake
    image guitarplay pol_6_play_fast:
        "guitarplay pol_6_prep"
        guitar_frame_period_fast
        "guitarplay pol_6_pull"
        function set_string_6_pulled
        guitar_frame_period_fast
        "guitarplay pol_6_release"
        function set_string_6_shake




    image guitarplay ant_strumm:
        "guitarplay ant_6_prep"

        0.02

        "guitarplay ant_6_pull"
        function set_string_6_pulled

        0.02

        "guitarplay ant_5_pull"
        function set_string_6_shake
        function set_string_5_pulled

        0.02

        "guitarplay ant_4_pull"
        function set_string_5_shake
        function set_string_4_pulled

        0.02

        "guitarplay ant_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay ant_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay ant_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay ant_1_release"
        function set_string_1_shake

    image guitarplay ant_strumm_1_2_3:
        "guitarplay ant_3_prep"

        guitar_frame_period

        "guitarplay ant_3_pull"
        function set_string_3_pulled

        0.02

        "guitarplay ant_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay ant_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay ant_1_release"
        function set_string_1_shake

    image guitarplay ant_strumm_2_3_4:
        "guitarplay ant_4_prep"

        guitar_frame_period

        "guitarplay ant_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay ant_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay ant_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay ant_2_release"
        function set_string_2_shake

    image guitarplay ant_strumm_3_4:
        "guitarplay ant_4_prep"

        guitar_frame_period

        "guitarplay ant_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay ant_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay ant_3_release"
        function set_string_3_shake

    image guitarplay ant_strumm_3_4_fast:
        "guitarplay ant_4_prep"

        0.04

        "guitarplay ant_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay ant_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay ant_3_release"
        function set_string_3_shake

    image guitarplay ant_strumm_2_3:
        "guitarplay ant_3_prep"

        guitar_frame_period

        "guitarplay ant_3_pull"
        function set_string_3_pulled

        0.02

        "guitarplay ant_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay ant_2_release"
        function set_string_2_shake

    image guitarplay ant_strumm_4_6:
        "guitarplay ant_6_prep"

        guitar_frame_period

        "guitarplay ant_6_pull"
        function set_string_6_pulled

        0.02

        "guitarplay ant_4_pull"
        function set_string_6_shake
        function set_string_4_pulled

        0.02

        "guitarplay ant_4_release"
        function set_string_4_shake

    image guitarplay ant_strumm_4_5:
        "guitarplay ant_5_prep"

        guitar_frame_period

        "guitarplay ant_5_pull"
        function set_string_5_pulled

        0.02

        "guitarplay ant_4_pull"
        function set_string_5_shake
        function set_string_4_pulled

        0.02

        "guitarplay ant_4_release"
        function set_string_4_shake



    image guitarplay pol_strumm:
        "guitarplay pol_6_prep"

        0.02

        "guitarplay pol_6_pull"
        function set_string_6_pulled

        0.02

        "guitarplay pol_5_pull"
        function set_string_6_shake
        function set_string_5_pulled

        0.02

        "guitarplay pol_4_pull"
        function set_string_5_shake
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_1_2:
        "guitarplay pol_2_prep"

        guitar_frame_period

        "guitarplay pol_2_pull"
        function set_string_2_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_1_3:
        "guitarplay pol_3_prep"

        guitar_frame_period

        "guitarplay pol_3_pull"
        function set_string_3_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_3_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_1_2_3:
        "guitarplay pol_3_prep"

        guitar_frame_period

        "guitarplay pol_3_pull"
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_1_2_3_4:
        "guitarplay pol_4_prep"

        guitar_frame_period

        "guitarplay pol_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_1_2_3_4_5:
        "guitarplay pol_5_prep"

        guitar_frame_period

        "guitarplay pol_5_pull"
        function set_string_5_pulled

        0.02

        "guitarplay pol_4_pull"
        function set_string_5_shake
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_1_pull"
        function set_string_2_shake
        function set_string_1_pulled

        0.02

        "guitarplay pol_1_release"
        function set_string_1_shake

    image guitarplay pol_strumm_2_3_4:
        "guitarplay pol_4_prep"

        guitar_frame_period

        "guitarplay pol_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_2_release"
        function set_string_2_shake

    image guitarplay pol_strumm_3_4:
        "guitarplay pol_4_prep"

        guitar_frame_period

        "guitarplay pol_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_3_release"
        function set_string_3_shake

    image guitarplay pol_strumm_3_4_fast:
        "guitarplay pol_4_prep"

        0.04

        "guitarplay pol_4_pull"
        function set_string_4_pulled

        0.02

        "guitarplay pol_3_pull"
        function set_string_4_shake
        function set_string_3_pulled

        0.02

        "guitarplay pol_3_release"
        function set_string_3_shake

    image guitarplay pol_strumm_2_3:
        "guitarplay pol_3_prep"

        guitar_frame_period

        "guitarplay pol_3_pull"
        function set_string_3_pulled

        0.02

        "guitarplay pol_2_pull"
        function set_string_3_shake
        function set_string_2_pulled

        0.02

        "guitarplay pol_2_release"
        function set_string_2_shake

    image guitarplay pol_strumm_4_6:
        "guitarplay pol_6_prep"

        guitar_frame_period

        "guitarplay pol_6_pull"
        function set_string_6_pulled

        0.02

        "guitarplay pol_4_pull"
        function set_string_6_shake
        function set_string_4_pulled

        0.02

        "guitarplay pol_4_release"
        function set_string_4_shake

    image guitarplay pol_strumm_4_5:
        "guitarplay pol_5_prep"

        guitar_frame_period

        "guitarplay pol_5_pull"
        function set_string_5_pulled

        0.02

        "guitarplay pol_4_pull"
        function set_string_5_shake
        function set_string_4_pulled

        0.02

        "guitarplay pol_4_release"
        function set_string_4_shake

    image guitarplay pol_strumm_5_6:
        "guitarplay pol_6_prep"

        guitar_frame_period

        "guitarplay pol_6_pull"
        function set_string_6_pulled

        0.02

        "guitarplay pol_4_pull"
        function set_string_6_shake
        function set_string_5_pulled

        0.02

        "guitarplay pol_5_release"
        function set_string_5_shake



init -1:
    image anton_guitar_angry_blink:
        "minigame/guitar/anton/eyes/angry/001.png"
        choice:
            5.
        choice:
            6.5
        choice:
            8.
        "minigame/guitar/anton/eyes/angry/002.png"
        0.1
        "minigame/guitar/anton/eyes/angry/003.png"
        0.1
        "minigame/guitar/anton/eyes/angry/002.png"
        0.1
        repeat
    image anton_guitar_happy_blink:
        "minigame/guitar/anton/eyes/happy/001.png"
        choice:
            5.
        choice:
            6.5
        choice:
            8.
        "minigame/guitar/anton/eyes/happy/002.png"
        0.1
        "minigame/guitar/anton/eyes/happy/003.png"
        0.1
        "minigame/guitar/anton/eyes/happy/002.png"
        0.1
        repeat
    image anton_guitar_normal_blink:
        "minigame/guitar/anton/eyes/normal/001.png"
        choice:
            5.
        choice:
            6.5
        choice:
            8.
        "minigame/guitar/anton/eyes/normal/002.png"
        0.1
        "minigame/guitar/anton/eyes/normal/003.png"
        0.1
        "minigame/guitar/anton/eyes/normal/002.png"
        0.1
        repeat

    image Ant guitar angry 001:
        contains:
            "anton_guitar_angry_blink"
        contains:
            "minigame/guitar/anton/mouth/001.png"
    image Ant guitar angry 002:
        contains:
            "anton_guitar_angry_blink"
        contains:
            "minigame/guitar/anton/mouth/002.png"
    image Ant guitar angry 003:
        contains:
            "anton_guitar_angry_blink"
        contains:
            "minigame/guitar/anton/mouth/003.png"
    image Ant guitar angry 004:
        contains:
            "anton_guitar_angry_blink"
        contains:
            "minigame/guitar/anton/mouth/004.png"

    image Ant guitar happy 001:
        contains:
            "anton_guitar_happy_blink"
        contains:
            "minigame/guitar/anton/mouth/001.png"
    image Ant guitar happy 002:
        contains:
            "anton_guitar_happy_blink"
        contains:
            "minigame/guitar/anton/mouth/002.png"
    image Ant guitar happy 003:
        contains:
            "anton_guitar_happy_blink"
        contains:
            "minigame/guitar/anton/mouth/003.png"
    image Ant guitar happy 004:
        contains:
            "anton_guitar_happy_blink"
        contains:
            "minigame/guitar/anton/mouth/004.png"

    image Ant guitar normal 001:
        contains:
            "anton_guitar_normal_blink"
        contains:
            "minigame/guitar/anton/mouth/001.png"
    image Ant guitar normal 002:
        contains:
            "anton_guitar_normal_blink"
        contains:
            "minigame/guitar/anton/mouth/002.png"
    image Ant guitar normal 003:
        contains:
            "anton_guitar_normal_blink"
        contains:
            "minigame/guitar/anton/mouth/003.png"
    image Ant guitar normal 004:
        contains:
            "anton_guitar_normal_blink"
        contains:
            "minigame/guitar/anton/mouth/004.png"

    image polina_guitar_down_blink:
        "minigame/guitar/polina/eyes/down/001.png"
        choice:
            5.
        choice:
            6.5
        choice:
            8.
        "minigame/guitar/polina/eyes/down/002.png"
        0.1
        "minigame/guitar/polina/eyes/down/003.png"
        0.1
        "minigame/guitar/polina/eyes/down/002.png"
        0.1
        repeat
    image polina_guitar_up_blink:
        "minigame/guitar/polina/eyes/up/001.png"
        choice:
            5.
        choice:
            6.5
        choice:
            8.
        "minigame/guitar/polina/eyes/up/002.png"
        0.1
        "minigame/guitar/polina/eyes/up/003.png"
        0.1
        "minigame/guitar/polina/eyes/up/002.png"
        0.1
        repeat

    image Polina guitar down 001:
        contains:
            "polina_guitar_down_blink"
        contains:
            "minigame/guitar/polina/mouth/001.png"
    image Polina guitar down 002:
        contains:
            "polina_guitar_down_blink"
        contains:
            "minigame/guitar/polina/mouth/002.png"

    image Polina guitar up 001:
        contains:
            "polina_guitar_up_blink"
        contains:
            "minigame/guitar/polina/mouth/001.png"
    image Polina guitar up 002:
        contains:
            "polina_guitar_up_blink"
        contains:
            "minigame/guitar/polina/mouth/002.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
