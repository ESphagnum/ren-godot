






























default true_detective_count4 = 0

label d4_setup hide:

    menu:
        "Настроить события":
            pass
        "Продолжить как есть":
            jump d4_begin
        "Выбрать пресет":
            jump d4_setup.presets

    scene black
    label d4_setup.mainloop:

        call d4_setup.check from _call_d4_setup_check

        menu:
            "День 1":
                jump d4_setup.d1_loop
            "День 2":
                jump d4_setup.d2_loop
            "День 3":
                jump d4_setup.d3_loop
            "Проверка":

                $ msg = str(Flags.vault)
                "[msg]"
                jump d4_setup.mainloop
            "Начать":

                jump d4_begin

    label d4_setup.check:
        if not Flags.Has("fight"):
            $ Flags.Raise("mask")
        if Flags.Has("mask"):
            $ Flags.Drop("polaroid")
            $ Flags.Drop("amulet")
            $ Flags.Drop("betray")
        if Flags.Has("day2 polina"):
            $ Flags.Drop("polaroid")
            $ Flags.Drop("betray")
        if Flags.Has("day2 fox"):
            $ Flags.Drop("amulet")
        if not Flags.Has("gum"):
            $ Flags.Drop("polaroid")


        $ ROUTE_SOLO = Flags.Has("mask")
        $ ROUTE_POLINA = not ROUTE_SOLO and Flags.Has("day2 polina")
        $ ROUTE_FOX = not ROUTE_SOLO and Flags.Has("day2 fox")
        return

    label d4_setup.d1_loop:
        call d4_setup.check from _call_d4_setup_check_1
        menu:
            "Назад":
                jump d4_setup.mainloop

            "Перчатка (-)" if not Flags.Has("glove"):
                $ Flags.Raise("glove")
            "Перчатка (+)" if Flags.Has("glove"):
                $ Flags.Drop("glove")

            "Номер (-)" if not Flags.Has("number"):
                $ Flags.Raise("number")
            "Номер (+)" if Flags.Has("number"):
                $ Flags.Drop("number")

            "Запись (-)" if not Flags.Has("record"):
                $ Flags.Raise("record")
            "Запись (+)" if Flags.Has("record"):
                $ Flags.Drop("record")

        jump d4_setup.d1_loop

    label d4_setup.d2_loop:
        call d4_setup.check from _call_d4_setup_check_2
        menu:
            "Назад":
                jump d4_setup.mainloop

            "Жвачка (-)" if not Flags.Has("gum"):
                $ Flags.Raise("gum")
            "Жвачка (+)" if Flags.Has("gum"):
                $ Flags.Drop("gum")

            "Отпор Семёну (-)" if not Flags.Has("fight"):
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
            "Отпор Семёну (Полина)" if Flags.Has("fight") and Flags.Has("day2 polina"):
                $ Flags.Drop("day2 polina")
                $ Flags.Raise("day2 fox")
            "Отпор Семёну (Лиса)" if Flags.Has("fight") and Flags.Has("day2 fox"):
                $ Flags.Drop("day2 fox")
                $ Flags.Drop("fight")
                $ Flags.Raise("mask")

            "Маска (-)" if not Flags.Has("mask"):
                $ Flags.Raise("mask")
            "Маска (+)" if Flags.Has("mask"):
                $ Flags.Drop("mask")

        jump d4_setup.d2_loop

    label d4_setup.d3_loop:
        call d4_setup.check from _call_d4_setup_check_3
        menu:
            "Назад":
                jump d4_setup.mainloop

            "Папка (-)" if not Flags.Has("doc"):
                $ Flags.Raise("doc")
            "Папка (1)" if Flags.Has("doc") and not Flags.Has("finger"):
                $ Flags.Raise("finger")
            "Папка (2)" if Flags.Has("finger"):
                $ Flags.Drop("doc")
                $ Flags.Drop("finger")

            "Фоторобот (-)" if not Flags.Has("silent") and not Flags.Has("witness"):
                $ Flags.Raise("silent")
            "Фоторобот (Промолчал)" if Flags.Has("silent"):
                $ Flags.Drop("silent")
                $ Flags.Raise("witness")
            "Фоторобот (Свидетель)" if Flags.Has("witness"):
                $ Flags.Drop("witness")

            "Полароид (N/A)" if not Flags.Has("gum"):
                pass
            "Полароид (-)" if Flags.Has("gum") and not Flags.Has("polaroid"):
                $ Flags.Raise("polaroid")
            "Полароид (+)" if Flags.Has("gum") and Flags.Has("polaroid"):
                $ Flags.Drop("polaroid")

            "Амулет (N/A)" if Flags.Has("mask") or Flags.Has("day2 fox"):
                pass
            "Амулет (-)" if not Flags.Has("mask") and Flags.Has("day2 polina") and not Flags.Has("amulet"):
                $ Flags.Raise("amulet")
            "Амулет (+)" if not Flags.Has("mask") and Flags.Has("day2 polina") and Flags.Has("amulet"):
                $ Flags.Drop("amulet")

            "Предательство (N/A)" if Flags.Has("mask") or Flags.Has("day2 polina"):
                pass
            "Предательство (-)" if not Flags.Has("mask") and Flags.Has("day2 fox") and not Flags.Has("betray"):
                $ Flags.Raise("betray")
            "Предательство (+)" if not Flags.Has("mask") and Flags.Has("day2 fox") and Flags.Has("betray"):
                $ Flags.Drop("betray")

        jump d4_setup.d3_loop

    label d4_setup.presets:
        menu:
            "Рут Соло":
                $ Flags.Raise("mask")
            "Рут Полины":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
            "Рут Полины (+Амулет)":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
                $ Flags.Raise("amulet")
            "Рут Лисы (Вольтрон)":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 fox")
            "Рут Лисы (Предатель)":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 fox")
                $ Flags.Raise("betray")
        call d4_setup.check from _call_d4_setup_check_4
        jump d4_begin








    return



label d4_begin:
    window hide
    scene bg_black with Dissolve(1.0)

    pause 1.0

    scene bg_logo3
    with Dissolve(1.0)

    show screen center_text(_("Эпизод IV: Бьём копытом оземь")) with Dissolve(.5)

    pause 1.

    show screen day5_continue_button(d5_logo_begin)
    with Dissolve(.5)
    $ ui.interact()

    hide screen day5_continue_button
    with Dissolve(.5)

    pause 1.

    hide screen center_text with Dissolve(.5)

    scene black with Dissolve(1.)

    if not Flags.Has("mask") and Flags.Has("day2 fox"):
        jump d4_begin_fox

    jump d4_begin_polina



label d4_begin_fox:
    $ story_manager.MarkEvent(("day4", "scene1a"))

    $ renpy.start_predict("koshmar")
    $ renpy.start_predict("d4_kate_vision")

    scene day3_end_class_bg:
        xalign 1.
    show Romka Angry b_day 01 happy ahead 01:
        xzoom -1
        xoffset -400
    show Byasha Scared b_day 01 shock aside 01:
        xoffset 600
        alpha 0
        1.0
        linear .5 xoffset 500 alpha 1
    with Dissolve(1.5)

    window show
    play music "music/Dark.ogg" volume 0.9 fadein 0.2

    play sound "sounds/sfx_Byasha_sit.ogg"

    "Бяша подсел к нам, озабоченно кусая губу."

    show Byasha Scared b_day 01 shock ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/158To.ogg"
    Bya "Тошик, ты же почти в этом сраном лесу живёшь..."

    show Byasha Scared b_day 01 shock ahead 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock ahead 02 with Dissolve(.15)

    voice "voice/byasha/4day/158 V.ogg"
    Bya "Вчера ничего странного не видел, на?"
    show Byasha Scared b_day 01 shock ahead 01 with Dissolve(.15)
    "Мой ответ был чистейшей ложью:"
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    voice "voice/anton/4day/4. N.ogg"
    Ant "Не-ет."
    show Romka Angry b_day 01 happy ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/69 Ya.ogg"
    Rom "Я тоже."
    show Romka Angry b_day 01 happy ahead 01 with Dissolve(.15)
    show Romka Angry b_day 01 happy ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/70 po.ogg"
    Rom "Повезло, что классуха моим родакам нажаловалась из-за оценок."
    show Romka Angry b_day 01 happy ahead 01 with Dissolve(.15)
    show Romka Angry b_day 01 happy ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/71 Vot.ogg"
    Rom "Вот меня и не выпустили вечером на репетицию."
    show Romka Angry b_day 01 happy ahead 01 with Dissolve(.15)
    show Romka Angry b_day 01 happy ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/72 A.ogg"
    Rom "А то на месте Катьки оказались бы мы."
    show Romka Angry b_day 01 happy ahead 01 with Dissolve(.15)

    play test_six "voice/byasha/4day/25 By.ogg"
    "Бяша судорожно почесал кадык."
    show Romka Angry b_day 01 happy aside 01 with Dissolve(.15)

    show bg_black:
        alpha 0.0
        linear 2. alpha 1.0

    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/159 E.ogg"
    Bya "Это... Я чё сказать хотел, на..."
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/160 Ya.ogg"
    Bya "Я кое-что слышал..."
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)

    show koshmar:
        alpha 0.0
        linear 4. alpha 1.0

    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)

    queue sound [ "<silence 5>", "<from 0 to 4>sounds/sfx_cry_Katya_distant.ogg"]

    voice "voice/byasha/4day/161 E.ogg"
    Bya "Этим утром я как обычно в школу шёл. Вдруг слышу плач за деревьями. Девчачий. Сечёте, на?"
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/162 Nu.ogg"
    Bya "Ну я про Катьку же не знал тогда. Да и знал бы — стрёмно оно, братки..."
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/163 Ut.ogg"
    Bya "Утро у нас не лучше ночи. Темно, на, как... как в жопе."
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/164 v.ogg"
    Bya "Вдруг это Катька была, а?"
    show Byasha Scared b_day 01 shock aside 01 with Dissolve(.15)
    show Byasha Scared b_day 01 shock aside 02 with Dissolve(.15)
    voice "voice/byasha/4day/165A.ogg"
    Bya "А главное, в месте таком паршивом, на, — в буреломе, что неподалёку от кладбища."

    scene day3_end_class_bg:
        xalign 1.

    show Romka Angry b_day 01 happy aside 02:
        xzoom -1
        xoffset -400

    show Byasha Normal b_day 01 shock aside 01:
        xzoom -1
        xoffset 500

    with Dissolve(.15)

    voice "voice/romka/4day/73 Hor.ogg"
    Rom "Хорош пургу гнать!"
    show Romka Angry b_day 01 happy aside 01 with Dissolve(.15)

    show Byasha Normal b_day 01 shock ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/166 Da.ogg"
    Bya "Да зуб даю, на! Сам слышал."
    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(.15)

    voice "voice/anton/4day/5. A.ogg"
    Ant "А вы уверены, что Катя действительно пропала?"

    show Romka Angry b_day 01 happy ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/74Vo.ogg"
    Rom "Вон Лилия Павловна, Катькина матушка, даже на работу не пришла."
    show Romka Angry b_day 01 happy ahead 01 with Dissolve(.15)



    scene day3_end_class_bg:
        xalign 1.
        linear .5 xalign .5

    show Byasha Normal b_day 01 shock ahead 02:
        xzoom -1
        xoffset 500
        linear .5 xoffset 1200

    show Romka Angry b_day 01 happy ahead 01:
        xzoom -1
        xoffset -400
        linear .5 xoffset 500

    voice "voice/byasha/4day/167 S.ogg"
    Bya "Слетела контрольная, на."

    scene day3_end_class_bg:
        xalign .5
        linear .5 xalign 1.

    show Byasha Normal b_day 01 shock ahead 02:
        xzoom -1
        xoffset 1200
        linear .5 xoffset 500

    show Romka Angry b_day 01 happy ahead 01:
        xzoom -1
        xoffset 500
        linear .5 xoffset -400

    show Byasha Normal b_day 01 shock ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/168 Ka.ogg"
    Bya "Как пить дать, пацаны, это Катька в тайге стонала."
    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(.15)
    show Byasha Normal b_day 01 shock ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/169 A.ogg"
    Bya "А значит, и до неё маньячелло добрался!"
    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(.15)
    "Я вспомнил Катю — такую красивую и такую подлую."
    play test_one "sounds/flashback.ogg"

    scene bg_white with Dissolve(.12)
    show d4_kate_vision with Dissolve(.2)

    "Первая девочка в классе, у которой на зависть подружкам успела округлиться грудь."
    "Первая сплетница, змея и гадина."
    play test_one "sounds/stick-echo-1.ogg" 

    scene bg_white with Dissolve(.12)
    scene day3_end_class_bg:
        xalign 1.

    show Romka Angry b_day 01 happy ahead 01:
        xzoom -1
        xoffset -400
        yoffset 20

    show Byasha Normal b_day 01 shock ahead 01:
        xzoom -1
        xoffset 500
        yoffset 20

    with Dissolve(.5)

    $ renpy.stop_predict("koshmar")
    $ renpy.stop_predict("d4_kate_vision")

    "Бяша загибал пальцы:"
    show Byasha Normal b_day 01 shock ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/170 Se.ogg"
    Bya "Сенечка, Вова, Семён, Катя... Четыре человека, на!"
    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(.15)



    "Рома хлопнул ладонями по парте."
    stop music fadeout 0.5
    show Romka Normal b_day 01 what ahead 03 with Dissolve(.15)
    play sound "sounds/sfx_table_clap.ogg"
    with hpunch
    play music "music/42_Talk.ogg" volume 0.7 fadein 2
    voice "voice/romka/4day/75 Ta.ogg"
    Rom "Так, пацаны, отныне смотреть в оба."
    show Romka Normal b_day 01 what ahead 01 with Dissolve(.15)
    show Romka Normal b_day 01 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/76 Da.ogg"
    Rom "Далеко друг от друга не отходим, как в дурацких ужастиках."
    show Romka Normal b_day 01 what ahead 01 with Dissolve(.15)

    show Byasha Normal b_day 01 normal ahead 01
    show Romka Normal b_day 01 what ahead 03
    with Dissolve(.15)
    voice "voice/romka/4day/77 Na.ogg"
    Rom "На остальных мне плевать, но вас я в обиду не дам."
    show Romka Normal b_day 01 what ahead 01 with Dissolve(.15)

    show Byasha Normal b_day 01 normal ahead 03
    show Romka Normal b_day 01 what ahead 03
    with Dissolve(.15)
    voice "voice/romka/4day/78 Kak.ogg"
    Rom "Как и Полинку..."

    show Byasha Normal b_day 01 normal ahead 01
    show Romka Normal b_day 01 what ahead 01
    with Dissolve(.15)
    "Пусть у вас с ней всё получится."
    "Я и думать забыл, что мне когда-то нравилась Полина."
    "После вчерашней ночи мои мысли занимала лишь одна девочка – Алиса."

    show Romka Normal b_day 01 what aside 01:
        xzoom -1
        xoffset -400
        yoffset 20
        parallel:
            linear 8 xoffset 1200
            linear .5 alpha 0 xoffset 1300
        parallel:
            linear .20 yoffset 0
            linear .20 yoffset 20
            repeat 24
    show Byasha Normal b_day 01 normal aside 01:
        xzoom -1
        xoffset 500
        yoffset 20
        .2
        parallel:
            linear 3.5 xoffset 1200
            linear .5 alpha 0 xoffset 1300
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 8

    stop music fadeout 3.5


    "Ребята направились в столовую, а я остался царапать ручкой в тетради, выводить пики сосен и две крошечные фигурки, летящие между кронами и полной луной."

    scene bg parta
    show tetrad 19
    with Dissolve(0.5)
    play sound "sounds/sfx_pencil_draw_1.ogg"
    play music2 "music/39_Dvar - Oramah Elahar.ogg" fadein 0.2
    "По предплечьям бежали ордой мурашки, ретиво заскакивая за шиворот."

    play sound "sounds/sfx_pencil_draw_1.ogg"

    show tetrad 19:
        "tetrad 20" with ImageDissolve("effect/imagedissolve/cross-t.jpg", 1.5)
    "И было вроде так просто взмыть к небесам... Но что-то злое гнуло до земли."
    show tetrad 20:
        "tetrad 17" with ImageDissolve("effect/imagedissolve/cross-t.jpg", 3.0)
    if Flags.Has("finger"):
        "То ли вес украденного перстня, то ли тяжёлые взгляды исчезнувших детей на доске."

    play sound "sounds/sfx_pencil_draw_2.ogg"

    "Кто-то в посёлке был явно к этому причастен, скрывал нечто ужасное за благочестивой маской."

    scene ant_clas_fon:
        align (.5,.5)
        zoom 1.3
    show day3_ant_clas_shadow 1:
        align (.5,.5)
    show day3_ant_clas_anton 2:
        align (.5,.5)
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)

    stop music2 fadeout 2
    play music "music/Winter(solo piano&cello).ogg" volume 0.8 fadein 1

    voice "voice/Polina/4day/134 R.ogg"
    Pol "Рисуешь?"
    play sound "sounds/sfx_notebook_close.ogg"
    scene bg parta
    show tetrad 17
    with Dissolve(.25)
    show tetrad 18 with Dissolve(.5)
    "Я стыдливо прикрыл тетрадь, будто было что-то зазорное в фигурках над лесом."

    jump d4_polkatya_general



label d4_begin_polina:
    $ story_manager.MarkEvent(("day4", "scene1b"))
    scene day3_end_class_bg:
        xalign 0.5

    show Polina Front b_day 01 sad ahead 03
    with Dissolve(1.5)

    play fon "sounds/fon/noise_klass.ogg" fadein 2
    play music "music/Winter(solo piano&cello).ogg" volume 0.8 fadein 1

    pause .5
    show Polina Front b_day 01 sad ahead 02 with Dissolve(.2)
    window show
    voice "voice/Polina/4day/Ya.ogg"
    Pol "Я сама не поверила, но Лилия Павловна на работу не вышла."
    show Polina Front b_day 01 sad ahead 03 with Dissolve(.2)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/4day/Kon.ogg"
    Pol "Контрольная отменяется."

    scene day3_end_class_bg:
        xalign 0.5
        linear .5 xalign 1.
    show Polina Front b_day 01 sad ahead 03:
        xoffset 0
        linear .5 xoffset 250
    "Я вспомнил Катю — такую красивую и такую подлую."
    play test_one "sounds/flashback.ogg"

    stop fon fadeout 2

    scene bg_white with Dissolve(.12)
    show d4_kate_vision with Dissolve(.2)
    "Катя. Первая девочка в классе, у которой на зависть подружкам успела округлиться грудь."
    "Первая сплетница, змея и гадина."
    play test_one "sounds/stick-echo-1.ogg" 
    play fon "sounds/fon/noise_klass.ogg" fadein 2

    scene bg_white with Dissolve(.12)
    scene day3_end_class_bg:
        xalign 1.
    show Polina Front b_day 01 sad ahead 03
    scene bg parta
    show tetrad 19
    with Dissolve(0.5)
    "Я продолжил царапать ручкой в тетради, выводить пики сосен и две крошечные фигурки, летящие между кронами и полной луной."
    "По предплечьям бежали ордой мурашки, ретиво заскакивая за шиворот."

    play sound "sounds/sfx_pencil_draw_1.ogg"

    show tetrad 19:
        "tetrad 20" with ImageDissolve("effect/imagedissolve/cross-t.jpg", 1.5)
    "И было вроде так просто взмыть к небесам... Но что-то злое гнуло до земли."

    play sound "sounds/sfx_pencil_draw_2.ogg"

    show tetrad 20:
        "tetrad 17" with ImageDissolve("effect/imagedissolve/cross-t.jpg", 3.0)
    if Flags.Has("finger"):
        "То ли вес украденного перстня, то ли тяжёлые взгляды исчезнувших детей на доске."
    "Кто-то в посёлке был явно к этому причастен, скрывал нечто ужасное за благочестивой маской."

    scene ant_clas_fon:
        align (.5,.5)
        zoom 1.3
    show day3_ant_clas_shadow 1:
        align (.5,.5)
    show day3_ant_clas_anton 2:
        align (.5,.5)
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)

    voice "voice/Polina/4day/Achto.ogg"
    Pol "А что ты рисуешь?"

    play sound "sounds/sfx_notebook_close.ogg"

    scene bg parta
    show tetrad 17
    with Dissolve(.25)
    show tetrad 18 with Dissolve(.5)

    "Я стыдливо прикрыл тетрадь, будто было что-то зазорное в фигурках над лесом."


    jump d4_polkatya_general



label d4_polkatya_general:

    $ story_manager.MarkEvent(("day4", "scene2"))

    voice "voice/anton/4day/8. Da.ogg"
    Ant "Да ничего... Так, дурака валяю."
    scene d4_classroom_pol
    show Polina Flirting b_day 01 norm ahead 01
    with Dissolve(.25)

    play sound "sounds/sfx_table_lean.ogg"

    "Полина облокотилась на парту."
    "Я уже и забыл, какая она лёгкая и изящная, словно скрипка."

    if Flags.Has("mask"):
        "Гнев и ярость, которые обуревали меня вчера во время телефонного разговора - отступили, спрятались в норе. Я уже забыл обижаться на Полину."

    stop fon fadeout 19 
    "Вот бы она тоже могла прыгать с нами, сняв маску притворной повседневности."

    scene ant_clas_fon:
        align (.5,.5)
        zoom 1.3
    show ant_clas_1 ul2:
        align (.5,.5)
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)

    "Я улыбнулся, представляя, как юбочка Полины порхает на ветру, как звёзды искрятся со всех сторон, и она удивлённо спрашивает, не сон ли это."
    "А я отвечаю, мол, какая разница..."

    show ant_clas_1 1
    with Dissolve(.5)

    play test_three "voice/Polina/4day/02 Vzdoh.ogg"
    "Лицо Полины снова помрачнело."

    scene day3_end_class_bg:
        xalign 1.
    if ROUTE_FOX:
        show Polina Front b_day 01 sadly ahead 03
        with Dissolve(.25)
        show Polina Front b_day 01 sadly ahead 02 with Dissolve(.25)
        play music "music/loss.ogg" fadein 1
        voice "voice/Polina/4day/134 Uze.ogg"
        Pol "Уже слышал про Катю?"

        show Polina Front b_day 01 sad ahead 03 with Dissolve(.25)
        voice "voice/anton/4day/9. Uzas.ogg"
        Ant "Ужасно."

        show Polina Front b_day 01 sad ahead 03 with Dissolve(.25)
        show Polina Front b_day 01 sad ahead 02 with Dissolve(.25)
        voice "voice/Polina/4day/135 Da.ogg"
        Pol "Да."

    show Polina Front b_day 01 sad ahead 03
    with Dissolve(.25)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/01 Uz.ogg"
    Pol "Ужасно ещё и то, что Катю мне жалеть сложно."

    show Polina Front b_day 01 sad ahead 03 with Dissolve(.25)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/02 Ya.ogg"
    Pol "Я правда ищу в себе сострадание, но вспоминаю её поступки, и..."

    show Polina Front b_day 01 sadly_down aside 03 with Dissolve(.25)
    "Полина покачала головой."

    show Polina Front b_day 01 sad ahead 03 with Dissolve(.25)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(.25)

    voice "voice/Polina/4day/03YaCh.ogg"
    Pol "Я чудовище, да?"
    show Polina Front b_day 01 sad ahead 03 with Dissolve(.25)



    if ROUTE_POLINA:
        scene ant_clas_fon:
            align (.5,.5)
            zoom 1.3
        show ant_clas_1 1:
            align (.5,.5)
        show day3_ant_clas_polina:
            align (1., 1.)
        show ant_clas_m6
        show d4_anton_shy_blink
        with Dissolve(.25)

        "«Нет, - подумал я, - ты одна из самых красивых девушек, кого я встречал.»"
    else:

        stop music fadeout 1.5
        play music2 "music/24_Fox.ogg" fadein 2.0
        window hide
        show Veko_01:
            xpos 0
            ypos -1500
            alpha 0.0
            linear 1.0 xpos 0 ypos -510 alpha 1.0
        show Veko_02:
            xpos 0
            ypos 1010
            alpha 1.0
            linear 1.0 xpos 0 ypos 0 alpha 1.0

        pause .5

        scene black
        show showB1
        show showB2
        show showB3
        show showB4
        show showB5 zorder 1
        with Dissolve(0.5)

        show polina_lisa_05
        with Dissolve(0.25)

        hide polina_lisa_05
        show polina_lisa_06
        with Dissolve(0.25)

        hide polina_lisa_06
        show Fox Normal b_night 00 good ahead
        with Dissolve(0.25)

        "«Нет, - подумал я, - ты одна из самых красивых девушек, кого я встречал. Но для меня, увы, ты только на втором месте.»"

    "Но вслух ничего не сказал."

    if not ROUTE_POLINA:
        scene d4_classroom_pol
        show Polina Flirting b_day 01 sad ahead 04

        show Veko_01:
            xpos 0
            ypos -510
            alpha 1.0
            linear 1.0 xpos 0 ypos -1500 alpha 0.0
        show Veko_02:
            xpos 0
            ypos 0
            alpha 1.0
            linear 1.0 xpos 0 ypos 1010 alpha 0.0

        with Dissolve(.25)
        show Polina Flirting b_day 01 sad ahead 05 with Dissolve(.25)

    if ROUTE_POLINA:
        hide ant_clas_m6
        hide d4_anton_shy_blink
        with Dissolve(.25)

    window show
    voice "voice/Polina/4day/04 Plo.ogg"
    Pol "Плохо, наверное, что исчезновение анкеты расстроило меня больше, чем пропажа одноклассницы."

    if not ROUTE_POLINA:
        show Polina Flirting b_day 01 sad ahead 04 with Dissolve(.25)

        "Ноздри словно уловили запах конфет, древесной смолы и фейерверков."

    if ROUTE_POLINA:
        show ant_clas_1 rot:
            align (.5,.5)

    voice "voice/anton/4day/10. T.ogg"
    Ant "Ты потеряла анкету?"

    if ROUTE_POLINA:
        scene d4_classroom_pol
        show Polina Flirting b_day 01 sad ahead 04
        with Dissolve(.25)

    show Polina Flirting b_day 01 sad ahead 05 with Dissolve(.25)

    voice "voice/Polina/4day/05da Ektoto.ogg"
    Pol "Да. И кто-то сейчас читает чужие секреты."
    show Polina Flirting b_day 01 sad ahead 04 with Dissolve(.25)
    "«Лес», - подумал я, вообразив, как скрюченные ветви поддевают страницы и листают их, трогая детский почерк обледенелыми сучками."
    show Polina Flirting b_day 01 sad ahead 04 with Dissolve(.25)
    show Polina Flirting b_day 01 sad ahead 05 with Dissolve(.25)
    voice "voice/Polina/4day/06 Na.ogg"
    Pol "Надеюсь, её найдут."
    show Polina Flirting b_day 01 sad ahead 04 with Dissolve(.25)
    "Я не понял, про Катю она говорит или про тетрадку."

    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    "Хотел уточнить, но увидел, что Полина пристально меня изучает."
    stop music fadeout 6

    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        align (.5,.5)
    show ant_clas_blink_1:
        xpos 0
        alpha 1
        pause .6
        linear .3 alpha 0
    show ant_clas_blink
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)
    pause .7
    show ant_clas_1 rot:
        align (.5,.5)
    with Dissolve(.25)

    voice "voice/anton/4day/11. Cht.ogg"
    Ant "Что?"
    show ant_clas_1 1 with Dissolve(.25)
    voice "voice/Polina/4day/07 Ti.ogg"
    Pol "Ты будто изменился."

    "Я пригладил волосы удивлённо."
    show ant_clas_1 rot with Dissolve(.25)
    voice "voice/anton/4day/12. Pros.ogg"
    Ant "Просто не выспался."
    stop music2 fadeout 3
    show ant_clas_1 1 with Dissolve(.25)

    play music "music/Flute 2(reverb).ogg" volume 0.50 fadein 1
    voice "voice/Polina/4day/08 Se.ogg"
    Pol "Сегодня ты точно какая-то другая мелодия. Очень древняя, таинственная..."

    "Я подумал о флейте, струящейся между косматыми деревьями."

    scene d4_classroom_pol
    show Polina Flirting b_day 01 norm ahead 01
    with Dissolve(.25)
    show Polina Flirting b_day 01 norm ahead 03 with Dissolve(.25)
    stop music fadeout 3


    voice "voice/Polina/4day/09 Nad.ogg"
    Pol "Надеюсь, ты никому не рассказал про наш вчерашний разговор?"
    play music2 "music/Romantic Piano Story.ogg" volume 0.6 fadein 1
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.25)
    voice "voice/anton/4day/13. Cto.ogg"
    Ant "Что ты!"
    "Она кивнула, словно признаваясь, что полностью мне доверяет."
    "Я не знал, заслуживаю ли такого доверия."
    if ROUTE_FOX:
        show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
        show Polina Flirting b_day 01 norm ahead 02 with Dissolve(.15)
        show Polina Flirting b_day 01 norm ahead 03 with Dissolve(.25)
        voice "voice/Polina/4day/15 A moz.ogg"
        Pol "А может, погуляем после уроков?"

        show Polina Flirting b_day 01 norm ahead 02 with Dissolve(.15)
        show Polina Flirting b_day 01 norm ahead 03 with Dissolve(.15)
        voice "voice/Polina/4day/16 Ded.ogg"
        Pol "Дедушка чувствует себя лучше — я могу задержаться вечером."


    show ant_clas_fon:
        xpos -300
    show ant_clas_1 ul:
        align (.5,.5)
    with Dissolve(.15)
    "Её волосы каскадом спадали на плечи и так удивительно пахли, что я взлетал без всяких чар к переливающимся звёздам какого-то внутреннего космоса."


    if Flags.Has("mask"):
        jump d4_school_solo


    if Flags.Has("day2 polina"):
        jump d4_school_polina


    if Flags.Has("betray"):
        jump d4_school_fox_betray


    jump d4_school_fox_voltron




label d4_school_polina:
    $ story_manager.MarkEvent(("day4", "scene_p"))
    $ renpy.start_predict("bad_mask_bg")
    $ renpy.start_predict("d4_rom_knife")
    $ renpy.start_predict("d4_noise_1")
    $ renpy.start_predict("d4_classroom_day_base")
    $ renpy.start_predict("d4_classroom_day_byash2")



    stop music2 fadeout 2
    play music "music/Phrases_06(loop).ogg" fadein 1
    scene d4_classroom_day_base:
        yalign .75
        xalign .5
        linear .5 xalign 0.25 zoom 1.2
    show d4_classroom_day_byash2:
        yalign .75
        xalign .5
        linear .5 xalign 0.25 zoom 1.2

    with Dissolve(0.5)
    "Вдруг я уловил на себе пристальный взгляд Бяши. Он явно следил за нами."

    show layer master:
        blur 0
        linear .5 blur 16
    "Я снял очки, чтобы не видеть его гадкую ухмылку."

    window hide
    play test_three "sounds/serdtse.ogg" loop

    scene bad_mask_bg
    play test_three "sounds/sfx_butterfly_knife_open_fast.ogg"
    show d4_rom_knife
    show d4_noise_1
    with Dissolve(.50)

    pause 0.50

    scene bg_black with Dissolve(1.00)

    $ renpy.stop_predict("bad_mask_bg")
    $ renpy.stop_predict("d4_rom_knife")
    $ renpy.stop_predict("d4_noise_1")

    "Но перед внутренним взором заблестел Ромкин нож — и мои ладони моментально вспотели."

    stop music fadeout 1
    stop test_three fadeout 1
    voice "voice/Polina/4day/10 Op.ogg"
    Pol "Опять уснул?"

    scene d4_classroom_pol
    show Polina Flirting b_day 01 norm ahead 01

    show Veko_01:
        xpos 0
        ypos -510
        alpha 1.0
        linear 1.0 xpos 0 ypos -1500 alpha 0.0
    show Veko_02:
        xpos 0
        ypos 0
        alpha 1.0
        linear 1.0 xpos 0 ypos 1010 alpha 0.0


    window show

    play music2 "music/29_Polina.ogg" volume 0.7 fadein 2.0
    voice "voice/anton/4day/14. Po.ogg"
    Ant "Полина..."
    "«{i}Расскажи ей{/i}, - шепнул голос в голове, - {i}а там будь что будет{/i}»."
    voice "voice/anton/4day/15. k.ogg"
    Ant "Кажется, Ромка на тебя глаз положил."
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/11 Du.ogg"
    Pol "Думаешь, я не знаю?"
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/16. Ot.ogg"
    Ant "Откуда?"
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/12 Sch.ogg"
    Pol "Считай, это моя, интуиция."
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 05 with Dissolve(.25)
    voice "voice/Polina/4day/13 Pya.ogg"
    Pol "Только вот Пятифанов мне безразличен."
    show Polina Flirting b_day 01 norm ahead 04 with Dissolve(.15)
    "От радости я осмелел."
    voice "voice/anton/4day/17. Mn.ogg"
    Ant "Мне кажется, ему не хватит мозгов, чтобы завоевать тебя."
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 02 with Dissolve(.15)
    "Полина пленительно улыбнулась."
    show Polina Flirting b_day 01 norm ahead 02 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 06 with Dissolve(.15)
    voice "voice/Polina/4day/14Ho.ogg"
    Pol "Хорошо, что у меня есть ты."
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 06 with Dissolve(.15)
    voice "voice/Polina/4day/15 A.ogg"
    Pol "А может, погуляем после уроков?"
    show Polina Flirting b_day 01 norm ahead 01 with Dissolve(.15)
    show Polina Flirting b_day 01 norm ahead 06 with Dissolve(.15)
    voice "voice/Polina/4day/16 De.ogg"
    Pol "Дедушка чувствует себя лучше — я могу задержаться вечером."
    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        align (.5,.5)
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)
    "Мой ответ был равносилен самоубийству."
    show ant_clas_1 m6 with Dissolve(.25)
    show ant_clas_1 m7 with Dissolve(.25)
    voice "voice/anton/4day/20. Ko.ogg"
    Ant "Конечно, давай!"
    show ant_clas_1 m6 with Dissolve(.25)
    scene day3_end_class_bg
    show Polina Front b_day 01 smile2 ahead 014
    with Dissolve(.25)
    voice "voice/Polina/4day/17 To.ogg"
    Pol "Тогда до встречи."
    play sound "sounds/sfx_girl_comes3.ogg"
    show Polina Front b_day 01 smile ahead 04 with Dissolve(.25)
    show Polina Front m_day 02 smile ahead 04 with Dissolve(.25):
        zoom 1.15
        yoffset 75
    "Она привстала и снова посмотрела на меня своими пронзительными глазами."
    "Пробормотала, гадая:"
    show Polina Front m_day 03 smile ahead 04 with Dissolve(.25):
        zoom 1.15
        yoffset 75
    show Polina Front m_day 03 smile ahead 09 with Dissolve(.25):
        zoom 1.15
        yoffset 75
    voice "voice/Polina/4day/18 Ch.ogg"
    Pol "Что-то из Мусоргского?"
    show Polina Front m_day 03 smile ahead 04 with Dissolve(.25):
        zoom 1.15
        yoffset 75
    show Polina Front m_day 03 smile ahead 09 with Dissolve(.25):
        zoom 1.15
        yoffset 75
    voice "voice/Polina/4day/19 Ne.ogg"
    Pol "Нет, пожалуй."
    play test_two "sounds/steps/Polina_step_01.ogg"
    stop music2 fadeout 3
    hide Polina
    play music "music/Phrases_06(loop).ogg" fadein 2
    show sprite_polina_d3:
        zoom 1.15
        xpos -144
        ypos -87
        parallel:
            linear 2. xoffset 160
        parallel:
            linear 1.5 alpha 0
        parallel:
            linear .5 ypos -67
            linear .5 ypos -87
            linear .5 ypos -67
            linear .5 ypos -87
            repeat 2
    with Dissolve(.25)
    show d4_classroom_day_base:
        yalign .75
        xalign .5
        alpha 0
        .75
        linear .5 xalign 0.25 zoom 1.2 alpha 1
    show d4_classroom_day_byash2:
        yalign .75
        xalign .5
        alpha 0
        .75
        linear .5 xalign 0.25 zoom 1.2 alpha 1
    "И ушла, а вместо неё в меня вперился взглядом Ромкин подручный."

    scene d4_classroom_day_base:
        yalign .75
        xalign .25
        zoom 1.2
    show d4_classroom_day_byash2:
        yalign .75
        xalign .25
        zoom 1.2
    with Dissolve(.25)
    "Его указательный палец прошёлся под кадыком, сообщая: «Тебе конец»."

    window hide

    hide d4_classroom_day_byash2
    show d4_classroom_day_byash1:
        yalign .75
        xalign .25
        zoom 1.2
    with Dissolve(.25)

    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)
    $ renpy.stop_predict("d4_classroom_day_base")
    $ renpy.stop_predict("d4_classroom_day_byash2")
    window show
    stop music fadeout 1
    "Прозвенел звонок."

    scene bg school_day:
        yalign 0.8 xalign 0.5
    show blizzard_d4_day_far
    show blizzard_d4_day_near
    with Dissolve(.5)

    play music "music/11_Poryadok.ogg" volume 0.65 fadein 0.5
    play test_two "sounds/school_door-close-1.ogg"
    play fon "sounds/fon/wind.ogg" fadein 2.0
    "Оставшиеся занятия пролетели незаметно, и я, наконец, покинул школу."

    "По пришкольной территории юлой носились крошечные смерчи."
    "Крупными хлопьями падал белый снег."
    "Переливались фонари. Их свет словно кристаллизировался на морозе, становясь твёрдым и остроконечным."

    play sound "sounds/sfx_dog_bark_distant.ogg"

    "Где-то тявкнула собака, заставляя вспомнить бедную Жульку."
    scene bg school_day:
        yalign 0.8 xalign 0.5
        pause .25
        linear .7 xalign 0.7
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Polina 3_4 m_day_winter 01 norm ahead 011:
        xpos 800
        pause .25
        linear .7 xpos 200

    with Dissolve(.25)
    "Полина стояла на крыльце. Ветер теребил её волосы."
    scene bg school_day:
        yalign 0.8 xalign 0.7
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Polina 3_4 m_day_winter 01 norm ahead 01:
        xpos 200
    with Dissolve(.25)
    voice "voice/anton/4day/24. Ya.ogg"
    Ant "Я уже отвык от городского шума. Здесь всегда так тихо."
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina 3_4 m_day_winter 01 norm ahead 04 with Dissolve(.25)
    voice "voice/Polina/4day/20 O.ogg"
    Pol "О, а я мечтаю о какофонии!"
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    voice "voice/anton/4day/25. O.ogg"
    Ant "О како... чём?"
    show Polina Front m_day_winter 00 smile2 ahead 014 with Dissolve(.25):
        linear .2 yoffset 20
        linear .2 yoffset 0
        repeat 3
    play test_three "voice/Polina/4day/112 Hah.ogg"
    "Моя спутница засмеялась."
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina 3_4 m_day_winter 01 norm ahead 04 with Dissolve(.25)
    stop test_three fadeout 0.5
    voice "voice/Polina/4day/21 Kak.ogg"
    Pol "Какофония – это случайное сочетание звуков."
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina 3_4 m_day_winter 01 norm ahead 04 with Dissolve(.25)
    voice "voice/Polina/4day/22 De.ogg"
    Pol "Дедушка учит находить мелодию во всём."
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    voice "voice/anton/4day/26. On.ogg"
    Ant "Он, наверное, классный."
    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Front m_day_winter 00 norm ahead 08 with Dissolve(.25)
    voice "voice/Polina/4day/23 Ne.ogg"
    Pol "Не то слово! Скоро я вас познакомлю."
    show Polina Front m_day_winter 00 norm ahead 01 with Dissolve(.25)
    voice "voice/anton/4day/27. Ti.ogg"
    Ant "Ты меня в гости приглашаешь?"
    show Polina Front m_day_winter 00 norm ahead 01 with Dissolve(.25)
    show Polina Front m_day_winter 00 norm ahead 08 with Dissolve(.25)
    voice "voice/Polina/4day/24 A.ogg"
    Pol "А ты против?"
    show Polina Front m_day_winter 00 norm aside 01
    scene bg school_day:
        yalign 0.8 xalign 0.7
        linear 1.7 xalign 0.2
    show blizzard_d4_day_far zorder 1
    show blizzard_d4_day_near zorder 5
    show Polina Front m_day_winter 00 norm aside 01 zorder 2:
        xpos 200
        linear 1.7 xpos 1500
    show twain_rb_far:
        ypos 300
        xalign 0.7
        linear 1.7 xalign 0.2
    show fence2:
        yalign 0.8 xalign 0.7
        linear 1.7 xalign 0.2

    stop music fadeout 0.5
    play music2 "music/34_Nikita Kryukov - the Sabbath.ogg" fadein 0.5

    play sound "sounds/sfx_whistle_loud.ogg"

    $ story_manager.MarkEvent(("day4", "scene_p2"))

    "Не давая ответить, противный свист пронёсся по двору."
    "Из снегопада материализовались две фигуры: руки в карманах, головы низко опущены."
    "Суровая походка этой парочки сулила мне большие неприятности."
    scene bg school_day:
        yalign 0.8 xalign 0.2
        linear 1.7 xalign 0.53
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show twain_rb_far:
        ypos 300
        xalign 0.2
        linear 1.7 xalign 0.53
        linear .2 alpha 0
    show fence2:
        yalign 0.8 xalign 0.2
        linear 1.7 xalign 0.53
    show Byasha Normal m_day_winter 01 evil ahead 01 zorder 1:
        xzoom -1
        xpos -550
        yoffset 75
        alpha 0
        pause 1.85
        linear .2 alpha 1
    show Romka Angry m_day_winter 01 angry ahead 01 zorder 1:
        xpos 200
        yoffset 75
        alpha 0
        pause 1.85
        linear .2 alpha 1
    show Anton_back_day_4 zorder 1:
        xpos 1350
        linear 1.7 xpos -150
    show Polina_back_day_4 zorder 1:
        xpos 2200
        linear 1.7 xpos 600

    $ renpy.music.set_pan(0, delay=0, channel="test_two")


    show Romka Angry m_day_winter 01 angry ahead 02 with Dissolve(.25)
    queue sound [ "<silence 1.8>", "<from 0 to 5>sounds/steps/snow_stepF02.ogg"]
    $ music_during_lines = 0.75
    voice "voice/romka/4day/214Anu.ogg"
    Rom "А ну руки убрал от неё! Живо!"

    show Romka Angry m_day_winter 01 angry ahead 01 with Dissolve(.25)

    show Romka Angry m_day_winter 01 angry ahead 02 with Dissolve(.25)
    voice "voice/romka/4day/215Polin.ogg"
    Rom "Полин, ты как? Он тебя не тронул?"
    show Romka Angry m_day_winter 01 angry ahead 01 with Dissolve(.25)

    show Byasha Normal m_day_winter 01 evil ahead 02 with Dissolve(.25)

    voice "voice/byasha/4day/01 M.ogg"
    Bya "Мы всё видели, на!"
    show Byasha Normal m_day_winter 01 evil ahead 01 with Dissolve(.25)

    voice "voice/anton/4day/64. Vid.ogg"
    Ant "Видели что?"

    show Romka Angry m_day_winter 01 angry ahead 02 with Dissolve(.25)
    voice "voice/romka/4day/216Chto.ogg"
    Rom "Что ты её в лес вести собрался, психопат! Как Катьку."
    show Romka Angry m_day_winter 01 angry ahead 01 with Dissolve(.25)

    show Byasha Normal m_day_winter 01 evil ahead 02 with Dissolve(.25)
    voice "voice/byasha/4day/02V .ogg"
    Bya "В последний момент успели, на."
    show Byasha Normal m_day_winter 01 evil ahead 01 with Dissolve(.25)

    "Возмущённый голос Полины птицей вспорхнул над двором:"
    voice "voice/Polina/4day/25 Da.ogg"
    Pol "Да что вы мелете?"
    scene bg school_day:
        xalign 0.53
        yalign 0.8
        zoom 1.3
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Byasha Normal b_day_winter 01 evil ahead 01:
        xzoom -1
        xpos -480
        yoffset 0
    show Romka Angry b_day_winter 01 angry ahead 01:
        xpos 400
        yoffset 0
    with Dissolve(.25)

    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/217Ati.ogg"
    Rom "А ты не в курсе?"
    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(.2)

    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/219Kak.ogg"
    Rom "Как только этот чепушило сюда переехал, сразу народ стал пропадать."
    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(.2)

    show Byasha Normal b_day_winter 01 evil ahead 02 with Dissolve(.2)
    voice "voice/byasha/4day/03 Ag.ogg"
    Bya "Ага, я вот сам видел, как он вчера Катю провожать вызвался и в лес уволок!"
    show Byasha Normal b_day_winter 01 evil ahead 01 with Dissolve(.2)

    "Я попытался сопротивляться:"
    voice "voice/anton/4day/Vresh.ogg"
    Ant "Врёшь! Я эту Катьку терпеть не мог!"

    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/220vot.ogg"
    Rom "Ха! Вот потому её и грохнул."
    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(.2)

    show Byasha Normal b_day_winter 01 evil ahead 02 with Dissolve(.2)
    voice "voice/byasha/4day/04 V.ogg"
    Bya "Всё сходится, на."
    show Byasha Normal b_day_winter 01 evil ahead 01 with Dissolve(.2)

    "От такой несправедливости я оторопел."
    "Единственным плюсом оказалось то, что актёры из Ромки и Бяши никудышные. И врали они на тройку с минусом."

    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/221pov.ogg"
    Rom "Повезло тебе, что мы с ментами не якшаемся."
    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(.2)

    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/222ato.ogg"
    Rom "А то бы с радостью тебя, маньяка, сдали."
    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(.2)

    show Byasha Normal b_day_winter 01 evil ahead 02 with Dissolve(.2)
    voice "voice/byasha/4day/05 N.ogg"
    Bya "Ничего-ничего! Ща проведём с ним воспитательную беседу, на."
    show Byasha Normal b_day_winter 01 evil ahead 01 with Dissolve(.2)

    show Byasha Normal b_day_winter 01 evil ahead 02 with Dissolve(.2)
    voice "voice/byasha/4day/06 D.ogg"
    Bya "Держи его!"

    play sound "sounds/sfx_footsteps_snow_slow.ogg"

    show Byasha Normal b_day_winter 01 evil ahead 01 with Dissolve(.2)


    show Romka Angry b_day_winter 01 angry ahead 03 zorder 1:
        yalign .5
        parallel:
            linear .30 xoffset -175 zoom 1.1
        parallel:
            linear .15 yoffset -20
            linear .15 yoffset 0
    "Ромка двинулся на меня, ухмыляясь."

    show Romka Angry b_day_winter 01 angry ahead 04 with Dissolve(.2)
    voice "voice/romka/4day/223zna.ogg"
    Rom "Значит, Катя тебе не нравилась, да?"
    show Romka Angry b_day_winter 01 angry ahead 03 with Dissolve(.2)

    show Romka Angry b_day_winter 01 angry ahead 04 with Dissolve(.2)
    voice "voice/romka/4day/224kone.ogg"
    Rom "Конечно! Кто ещё мог её порешить?"
    show Romka Angry b_day_winter 01 angry ahead 03 with Dissolve(.2)

    scene day3_cornermeet_bg_fence_far:
        xalign .0
        yalign 1.

    show day3_cornermeet_bg_fence_near:
        xalign .0
        yalign 1.
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show day3_cornermeet_fence_anton:
        xpos 600
    show Polina Scream b_day_winter 01 norm ahead 01:
        xpos -400
        zoom 1.2
    with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    stop music2 fadeout 1.5
    play music "music/will go away.ogg" volume 0.8 fadein 1.5

    voice "voice/Polina/4day/26 Ti.ogg"
    Pol "Ты, например."
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show day4_fence_anton_eyes_aside zorder 1 with Dissolve(.25):
        xpos 600

    hide day3_cornermeet_fence_anton
    show day3_cornermeet_fence_anton_02:
        xpos 600
    with Dissolve(.25)
    "Я изумлённо посмотрел на Полину."
    "Ромка застыл с поднятыми кулаками."

    hide day3_cornermeet_fence_anton_02
    hide day4_fence_anton_eyes_aside
    show day3_cornermeet_fence_anton:
        xpos 600
    show day4_fence_anton_eyes_ahead:
        xpos 600
    with Dissolve(.25)

    voice "voice/romka/4day/225vsm.ogg"
    Rom "В см-смысле?"
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/27 Ka.ogg"
    Pol "Катя, при всём уважении, никого не любила."
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/28 Du.ogg"
    Pol "Думаешь, Рома, она про тебя сплетни не распускала?"
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/29 Chto.ogg"
    Pol "Что твой отец в тюрьме сидел? Что он тебя бьёт?"
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)

    scene bg school_day:
        yalign 0.8 xalign 0.53
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Byasha Normal m_day_winter 01 shock aside 01:
        xzoom -1
        xpos -550
        yoffset 75
    show Romka Worry m_day_winter 01 worry ahead 01:
        xpos 200
        yoffset 75
    show Anton_back_day_4:
        xpos -150
    show Polina_back_day_4:
        xpos 600
    with Dissolve(.25)

    show Romka Worry fish with Dissolve(.25)
    play test_one "voice/romka/4day/108 A.ogg"
    "Ромка покраснел и захлопал губами, точно выброшенная на берег рыба."
    "Полина продолжала звенящим от гнева голосом:"

    scene day3_cornermeet_bg_fence_far:
        xalign .0
        yalign 1.
    show day3_cornermeet_bg_fence_near:
        xalign .0
        yalign 1.
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show day3_cornermeet_fence_anton:
        xpos 600
    show Polina Scream b_day_winter 01 norm ahead 01:
        xpos -400
        zoom 1.2
    with Dissolve(.25)

    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/30 A.ogg"
    Pol "А ты, Бяша? Сам-то где вчера вечером пропадал?"
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/31 Ka.ogg"
    Pol "Катя говорила, что ты с приветом стал, как на Чёрный Гараж наткнулся."

    play test_one ["<silence .3>","sounds/sfx_footstep_snow_1.ogg"] 
    play test_two ["<silence 1.1>","sounds/sfx_footstep_snow_2.ogg"]

    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)

    scene bg school_day:
        xalign 0.53
        yalign 0.8
        zoom 1.3
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Romka Worry b_day_winter 01 worry ahead 01:
        xpos 400
        yoffset 20
    show Byasha Scared b_day_winter 01 shock ahead 02:
        xzoom -1
        xpos -480
        yoffset 20
        .25
        parallel:
            linear .30 xoffset -50
            .5
            linear .30 xoffset -100
        parallel:
            easein .15 yoffset 0
            easeout .15 yoffset 20
            .5
            easein .15 yoffset 0
            easeout .15 yoffset 20
    with Dissolve(.25)
    play test_six "voice/byasha/69 Ya vzglyanul.ogg"
    "Бяша попятился, а его лицо в норке капюшона стало белым, как у покойника."

    scene day3_cornermeet_bg_fence_far:
        xalign .0
        yalign 1.
    show day3_cornermeet_bg_fence_near:
        xalign .0
        yalign 1.
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show day3_cornermeet_fence_anton:
        xpos 600
    show Polina Scream b_day_winter 01 norm ahead 01:
        xpos -400
        zoom 1.2
    with Dissolve(.25)

    show layer master:
        align (.4, .5)
        .15
        linear .15 zoom 1.10
        parallel:
            linear .15 zoom 1.00
        parallel:
            block:
                linear .02 xoffset 3
                linear .02 xoffset -3
                repeat 5
            block:
                linear .02 xoffset 2
                linear .02 xoffset -2
                repeat 5
            block:
                linear .02 xoffset 1
                linear .02 xoffset -1
                repeat 10
            linear .02 xoffset 0
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)

    voice "voice/Polina/4day/32 Ta.ogg"
    Pol "Так может, это ты тот психопат, что Катю украл?"
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)

    scene bg school_day:
        yalign 0.8 xalign 0.53
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Byasha Scared m_day_winter 01 shock ahead 01:
        xzoom -1
        xpos -550
        yoffset 75
    show Romka Worry m_day_winter 01 worry ahead 01:
        xpos 200
        yoffset 75
    show Anton_back_day_4:
        xpos -150
    show Polina_back_day_4:
        xpos 600
    with Dissolve(.25)
    show Byasha Scared m_day_winter 01 shock ahead 02:
        xzoom -1
        xpos -550
        yoffset 75
        linear .1 yoffset 50
        linear .1 yoffset 75
    stop test_six fadeout 0.2
    voice "voice/byasha/4day/07 N.ogg"
    Bya "Нет!"
    show Byasha Scared m_day_winter 01 shock ahead 01 with Dissolve(.25)
    "Бяша почти срывался на визг."

    play test_two "sounds/loop_footsteps_snow_fast.ogg"
    $ renpy.music.set_pan(-0.6, delay=4, channel="test_two")

    show Romka Worry m_day_winter 01 worry ahead 01:
        .25
        "Romka Worry m_day_winter 01 worry aside 01" with Dissolve(.25)
    show Byasha Scared m_day_winter 01 shock ahead 01:
        xzoom 1
        xpos -550
        yoffset 75
        parallel:
            linear 1.7 xoffset -960
        parallel:
            linear .1 yoffset 50
            linear .1 yoffset 75
            repeat 20

    stop test_two fadeout 3

    "Он повернулся и шаткой походкой побрёл к воротам, на ходу мотая головой."
    "Ого, - подумал я, - как она ловко справилась с Бяшей."

    $ renpy.music.set_pan(0, delay=4, channel="test_two")

    voice "voice/Polina/4day/33 Ch.ogg"
    Pol "Что, один остался, Ромео недоделанный?"
    voice "voice/Polina/4day/34 Ka.ogg"
    Pol "Какую ещё гнусность выдумаешь, чтобы меня удивить, м?"

    play test_two"voice/romka/4day/226roma.ogg"
    show Romka Worry m_day_winter 01 worry ahead 02 with Dissolve(.25):
        1.5
        "Romka Worry m_day_winter 01 worry ahead 01" with Dissolve(.25)
    "Рома затравленно сглотнул."

    scene day3_cornermeet_bg_fence_far:
        xalign .0
        yalign 1.
    show day3_cornermeet_bg_fence_near:
        xalign .0
        yalign 1.
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show day3_cornermeet_fence_anton:
        xpos 600
    show Polina Scream b_day_winter 01 norm ahead 01:
        xpos -400
        zoom 1.2
    with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/35 Ci.ogg"
    Pol "Цирк устроить хотел? Героем представиться?"
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/36 To.ogg"
    Pol "Только вот не ведут себя так герои."
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)
    show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(.25)
    voice "voice/Polina/4day/37 E.ogg"
    Pol "И актёр ты, Рома, липовый."
    show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(.25)

    scene bg school_day:
        yalign 0.8 xalign 0.53
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    show Romka Worry m_day_winter 01 worry ahead 01:
        xpos 200
        yoffset 75
    show Anton_back_day_4:
        xpos -150
    show Polina_back_day_4:
        xpos 600
    with Dissolve(.25)

    show Romka Worry m_day_winter 01 worry ahead 02 with Dissolve(.25)
    voice "voice/romka/4day/227da.ogg"
    Rom "Да этот очкарик..."
    show Romka Worry m_day_winter 01 worry ahead 01

    voice "voice/Polina/4day/38 V.ogg"
    Pol "...во всём лучше тебя." id d4_school_polina_fc04b1f0
    "Затем она сделала что-то совсем фантастическое — взяла меня за руку."

    play sound "sounds/sfx_rustle_clothes_light_3.ogg" volume 0.6

    hide Anton_back_day_4
    hide Polina_back_day_4
    with Dissolve(0.5)
    show Romka Worry m_day_winter 01 worry ahead 02:
        xpos 200
        yoffset 75
    show ant_and_pol_left:
        yoffset 110
        xpos 820
    with Dissolve(0.5)
    voice "voice/Polina/4day/39 Po.ogg"
    Pol "Пойдём, Антон."
    $ music_during_lines = 1.0


    play test_three "sounds/loop_footsteps_two.ogg" fadein 0.6
    $ renpy.music.set_pan(-0.6, delay=4, channel="test_three")

    show Romka Worry m_day_winter 01 worry ahead 02:
        2.0
        "Romka Worry m_day_winter 01 worry aside 02" with Dissolve(.5)
    show ant_and_pol_left:
        parallel:
            linear 4 xoffset -960
        parallel:
            easein .25 yoffset 100
            easeout .25 yoffset 110
            repeat
        parallel:
            3.5
            linear .5 alpha 0
    "Мы прошли мимо онемевшего Ромки."
    "Было даже жаль его, но — чего скрывать — я ликовал."
    "Он не остановил нас."

    stop music fadeout 6

    "Стоял и таращился в набирающую силу метель."

    $ story_manager.MarkEvent(("day4", "scene_p3"))
    $ renpy.music.set_pan(0, delay=4, channel="test_three")

    scene bg_white
    $ SetParSpeed(120)
    show walking_fox_11_day
    show walking_fox_12_day
    show walking_fox_21_day
    show walking_fox_22_day
    show walking_fox_31_day
    show walking_fox_32_day
    show blizzard_d4_day_far:
        block:
            xpan 0
            linear 80 xpan -360
            repeat
    show blizzard_d4_day_near zorder 5:
        block:
            xpan 0
            linear 60 xpan -360
            repeat
    show pol_walk_day_left
    show ant_walk_day_left
    stop test_one fadeout 0.5
    $ polina_face_state = 5
    with Dissolve(0.2)
    play music2 "music/Lucky.ogg" volume 0.8 fadein 2.5
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop
    "За воротами я воскликнул, подпрыгнув:"
    $ anton_face_polwalk_state = 2
    $ music_during_lines = 0.7
    voice "voice/anton/4day/66. Kak.ogg"
    Ant "Как ты его!"
    $ anton_face_polwalk_state = 0
    $ polina_face_state = 0
    "Полина скромно улыбнулась."
    voice "voice/Polina/4day/40 Nu.ogg"
    Pol "Ну знаешь... Как дедушка говорит, с волками жить — по-волчьи выть."
    voice "voice/anton/4day/67. On.ogg"
    Ant "Он у тебя философ."
    voice "voice/Polina/4day/41 Kra.ogg"
    Pol "Краевед... Был раньше."
    voice "voice/Polina/4day/42 On.ogg"
    Pol "Он уже давно на пенсии, а в последнее время ему серьёзно нездоровится."
    "Я понимающе кивнул."
    "Тайком я рассматривал Полину."
    "Она казалась драгоценным камнем, чьи грани переливаются, мерцают, неуловимо меняясь."
    "«Что?» – спрашивали невинно её смеющиеся глаза."
    "«То!» – молча отвечал я."
    voice "voice/Polina/4day/43 Ti.ogg"
    Pol "Ты храбрый. Мне нравится."

    $ anton_face_polwalk_state = 1
    voice "voice/anton/4day/68. Hr.ogg"
    Ant "Храбрый? Стоял там, язык проглотив."
    voice "voice/Polina/4day/44 No.ogg"
    Pol "Но стоял же! Не сбежал."
    voice "voice/Polina/4day/45 Ya.ogg"
    Pol "Я до сих пор поражаюсь, как ты нашёл в себе смелость послать, а тем более ударить Бабурина."

    $ anton_face_polwalk_state = 0
    play test_two "voice/anton/4day/Rady.ogg"
    Ant "Ради тебя я готов на многое."
    voice "voice/Polina/4day/46 Vot.ogg"
    Pol "Вот! Я же говорю!"
    voice "voice/Polina/4day/47 Ez.ogg"
    Pol "Изъясняешься словами из романов."
    voice "voice/Polina/4day/48 Ra.ogg"
    Pol "«Ради тебя, моя госпожа!»"
    $ music_during_lines = 1.0
    play test_six "voice/Polina/4day/49 Hih.ogg" 
    "Полина захихикала."
    $ anton_face_polwalk_state = 2
    play test_three "voice/anton/4day/32. Hehe.ogg"
    "Я надулся притворно, но не сумел удержаться и тоже улыбнулся." id d4_school_polina_b665ff3b
    stop music2 fadeout 2.5
    stop test_seven fadeout 6
    stop fon fadeout 5

    jump d4_polhouse_begin


label d4_school_solo:
    $ story_manager.MarkEvent(("day4", "scene_s"))
    "Бяша выпрыгнул, как чёртик из табакерки, и резко гаркнул мне в ухо:"
    scene day3_end_class_bg:
        xalign .5
        linear .1 xalign .35

    show Polina Front b_day 01 sadly ahead 03:
        xoffset -500
        zoom 0.95
        yoffset 54
        linear .1 xoffset -350

    show Byasha Normal b_day 01 vicious ahead 08:
        pos (.5,.5)
        anchor (.5,.5)
        xoffset 350
        yoffset 200
        zoom 2.
        linear .1 xoffset 0 zoom 3.

    show focus_lines:
        .15
        linear .5 alpha 0
    stop music2 fadeout 0.5
    play test_six "music/Phrases_01.ogg"
    voice "voice/byasha/4day/171 Op.ogg"
    Bya "Опачки!"
    play music2 "music/Morning Tensions_02.ogg" fadein 2
    scene day3_end_class_bg:
        xalign .35

        linear .5 xalign .5
    show Polina Front b_day 01 sadly ahead 03:
        xoffset -350
        zoom 0.95
        yoffset 54

        linear .5 xoffset -500
    show Byasha Normal b_day 01 vicious ahead 08:
        pos (.5,.5)
        anchor (.5,.5)
        xoffset 0
        yoffset 200
        zoom 3.
        parallel:
            "Byasha Normal b_day 01 vicious ahead 07" with Dissolve(.15)
            .35
            "Byasha Normal b_day 01 vicious ahead 08" with Dissolve(.15)
        parallel:
            linear .5 xoffset 350 zoom 1. yoffset 0

    voice "voice/byasha/4day/172 Ach.ogg"
    Bya "А чё это у вас за шуры-муры, на?"
    show Byasha Normal b_day 01 vicious ahead 07 with Dissolve(.25)
    show Romka Normal m_day 00 what ahead 04 behind Polina with Dissolve(.25):
        xoffset -250
        yoffset 50
        xzoom -1
        linear .25 xoffset -200
    voice "voice/romka/4day/247ti.ogg"
    Rom "Ты чего, очкарик, Полиночку охмуряешь?"
    show Romka Normal m_day 00 what ahead 01 with Dissolve(.25)
    "Полина пришла на помощь, хотя я и не просил."
    "Или всё-таки просил – всем своим видом?"

    show Polina Front b_day 01 sadly ahead 03 with Dissolve(.25)
    show Polina Front b_day 01 sadly ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/174 Ch.ogg"
    Pol "Что за глупости? Мы просто друзья."
    show Polina Front b_day 01 sadly ahead 03 with Dissolve(.25)

    show Romka Normal m_day 00 what ahead 01 with Dissolve(.25)
    show Romka Normal m_day 00 what ahead 04 with Dissolve(.25)
    voice "voice/romka/4day/248Tvo.ogg"
    Rom "Твоя подружка, значит? Ходишь вместе за платьями? С этим педиком?"
    show Romka Normal m_day 00 what ahead 01 with Dissolve(.25)

    show Polina Front b_day 01 sadly ahead 03 with Dissolve(.25)
    show Polina Front b_day 01 sadly ahead 02
    show Byasha Normal b_day 01 vicious aside 07
    with Dissolve(.25)
    voice "voice/Polina/4day/175 N.ogg"
    Pol "Никакой он не педик! И вообще отвянь от Петрова!"

    show Polina Front b_day 01 sadly ahead 03 with Dissolve(.25)
    "Я обязан был что-то предпринять. Но вместо этого сидел, вцепившись в край парты."
    "Ромка хмыкнул презрительно."

    show Romka Normal m_day 00 what ahead 04
    show Byasha Normal b_day 01 vicious ahead 07
    with Dissolve(.25)
    voice "voice/romka/4day/249baba.ogg"
    Rom "Баба тебя спасла, уродец. Живи пока."
    play test_one "sounds/sfx_footsteps_fat_boy_2.ogg"
    show Romka Normal m_day 00 what ahead 01 with Dissolve(.25)

    show Romka Normal m_day 00 what aside 01 with Dissolve(.25)
    show Romka Normal m_day 00 what aside 01:
        xoffset -200
        yoffset 50
        xzoom -1
        parallel:
            linear .25 yoffset 40
            linear .25 yoffset 50
            repeat 2
        parallel:
            linear .5 xoffset -150
    show day3_end_class_bg as bg2 behind Polina with Dissolve(.5):
        xalign .5

    play test_one "voice/romka/4day/250Hohocha.ogg"
    "Хохоча, мои враги удалились из класса."
    stop music2 fadeout 1.5


    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    show Byasha Normal b_day 01 vicious ahead 07 behind Polina
    show day3_end_class_bg as bg3 behind Polina with Dissolve(.5):
        xalign .5
    "Полина грустно улыбнулась мне."
    play music2 "music/loss.ogg" fadein 2

    show Polina Front b_day 01 sadly ahead 04 with Dissolve(.25)

    show Polina Front b_day 01 sadly ahead 09 with Dissolve(.25)
    voice "voice/Polina/4day/176 Bu.ogg"
    Pol "Будь сильным."
    show Polina Front b_day 01 sadly ahead 04 with Dissolve(.25)

    "Подмывало закричать: «Я не могу!»"
    "Не могу быть сильным и дать отпор этим мерзавцам."

    show Polina Front b_day 01 sadly ahead 03 with Dissolve(.25)
    play test_two "voice/anton/2day/130. Vidoh.ogg"
    "Не могу защитить себя, тебя... да хоть кого-нибудь."

    show Polina Front b_day 01 norm aside 03 with Dissolve(.25)
    "Я жалок."
    "Хочу сгинуть в лесу, зарыться в снег. Хочу домой, под одеяло, подальше от людей."
    play test_one "sounds/steps/Polina_step_02.ogg" 

    scene day3_end_class_bg with Dissolve(.5):
        xalign .5
    "Полина ушла, и терзавшие меня мысли окончательно довели до горьких слёз."
    "..."
    play test_two "sounds/steps/steps_shool.ogg"

    scene bg_koridorchic_day_02 with Dissolve(.5):
        xalign .0
    "Я снова задержался после уроков, боясь расправы Ромки за дерзость — разговор с Полиной."

    scene bg school_day:
        yalign 0.7 xalign 0.7
        zoom 1.5
    show blizzard_d4_day_far onlayer master1
    show blizzard_d4_day_near onlayer master1
    with Dissolve(0.5)
    play test_seven "sounds/school_door-close-2.ogg"
    play fon "sounds/fon/crow_wind.ogg" fadein 1.0
    "И брёл из школы в предзакатном свете."

    play test_five "sounds/loop_ice_scraping.ogg" fadein 1 loop
    play sound ["<silence 2.0>","sounds/sfx_boys_laugh_distant.ogg"]

    "Скучающий дворник скоблил лопатой асфальт, а старшеклассники выдували сигаретный дым, похожий на диалоговые облака из комиксов."
    "Хотелось наполнить эти пустые окошки дружескими словами, но не было ничего дружелюбного в ледяных взглядах ребят."

    scene bg school_day:
        yalign 0.7 xalign 0.7
        zoom 1.5
        linear 2 zoom 1.02
    play sound "sounds/sfx_company.ogg"
    play test_one "sounds/steps/steps_snow001.ogg"
    "Я покидал неприятный мир чёрствых булочек и гадких насмешек."
    play test_two "sounds/pushed.ogg"   

    with vpunch
    "Кто-то толкнул меня на пороге. Разве не учили извиняться?"

    stop test_five fadeout 2

    scene d4_bridge
    $ renpy.scene("master1")
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near
    with Dissolve(0.5)
    play test_one "sounds/bridge-steps-in-1.ogg"
    "Я пересёк посёлок и замедлился у моста. Покрутился, выискивая рыжую подругу, но на дороге не было лисиц или других моих новых друзей."
    "Встретивший меня лес был тих и покладист, будто притворившийся спящим зверь."

    $ par_spd = 120

    scene d4_darkroad_01:
        xpan 0
        linear par_spd * 1.00 xpan -360
        repeat
    show d4_darkroad_02:
        xpan 40
        linear par_spd * 0.81 xpan -360+40
        repeat
    show d4_darkroad_03:
        xpan 80
        linear par_spd * 0.72 xpan -360+80
        repeat
    show d4_darkroad_04:
        xpan 120
        linear par_spd * 0.64 xpan -360+120
        repeat

    show blizzard_d4_evening2_far:
        parallel:
            xpan 0
            linear 48 xpan -360
            repeat
        parallel:
            ypan 0
            linear 20 ypan -360
            repeat


    show d4_darkroad_05:
        xpan 160
        linear par_spd * 0.40 xpan -360+160
        repeat

    show blizzard_d4_evening2_near:
        parallel:
            xpan 0
            linear 24 xpan -360
            repeat
        parallel:
            ypan 0
            linear 10 ypan -360
            repeat

    with Dissolve(0.5)
    play test_seven "sounds/steps/loop_footsteps_one.ogg" loop
    "Он всё же следил за мной одним глазком, из-под прикрытых век, а я шагал, сунув пальцы за ремни рюкзака, и смотрел под ноги сквозь очки."

    voice "voice/Child/4day/Katya.ogg"
    Noname "Ка-а-а-а-тя! Ка-а-а-а-тя!"
    "Вновь чёрные тени маячили меж голых деревьев, неустанно повторяя имя, скорее всего, уже мёртвой девочки."
    "Закат затухал над соснами, как пламя повёрнутой к минимуму газовой конфорки."
    "Я пошёл дальше, втянув голову в плечи, не глядя на искорежённые деревья."
    stop test_seven fadeout 2.5
    stop music2 fadeout 3
    stop sound fadeout 2

    jump d4_home






label d4_school_fox_betray:
    $ story_manager.MarkEvent(("day4", "scene_t"))
    scene ant_clas_fon:
        xpos -300
    show ant_clas_1 ul:
        align (.5,.5)
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)

    show ant_clas_1 rot with Dissolve(.25)
    voice "voice/anton/4day/18. K.ogg"
    Ant "Конечно."
    show ant_clas_1 1 with Dissolve(.25)
    show ant_clas_1 rot with Dissolve(.25)
    voice "voice/anton/4day/19. To.ogg"
    Ant "Только давай пойдём через запасной выход. Ну тот, возле спортзала."
    show ant_clas_1 1 with Dissolve(.25)

    scene day3_end_class_bg:
        xalign 1.

    show Polina Front b_day 01 norm ahead 01:
        xzoom -1
        xoffset -100
        yoffset 10

    with Dissolve(.25)
    show Polina Front b_day 01 norm ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/136 Pr.ogg"
    Pol "Прячешься от кого-то?"
    scene day3_end_class_bg:
        xalign 1.
        linear .5 xoffset 500
    show Polina Front b_day 01 norm ahead 01:
        xzoom -1
        xoffset -100
        yoffset 10
        linear .5 xoffset 500

    "Я покосился на парту впереди."
    "Мои товарищи оставили нас вдвоём. Дали время, чтобы я мог их спокойно предать."
    "Совесть впилась в душу крошечными зубами."
    scene day3_end_class_bg:
        xpos -374
        linear .5 xpos -874
    show Polina Front b_day 01 norm ahead 01:
        xzoom -1
        xoffset 500
        yoffset 10
        linear .5 xoffset -100
    show Polina Front b_day 01 norm ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/137 Tak.ogg"
    Pol "Так это из-за Ромки?"
    show Polina Front b_day 01 norm ahead 01 with Dissolve(.25)
    show Polina Front b_day 01 norm ahead 02 with Dissolve(.25)
    voice "voice/Polina/4day/138 Ne.ogg"
    Pol "Не хочешь, чтобы он узнал?"
    show Polina Front b_day 01 norm ahead 01 with Dissolve(.25)
    voice "voice/anton/4day/21. T.ogg"
    Ant "Ты ему нравишься."
    show Polina 3_4 b_day 02 worry ahead 01 with Dissolve(.25)
    show Polina 3_4 b_day 02 worry ahead 04 with Dissolve(.25)
    voice "voice/Polina/4day/139 Slo.ogg"
    Pol "Сложно не заметить."
    show Polina 3_4 b_day 02 worry ahead 01 with Dissolve(.25)
    show Polina 3_4 b_day 02 worry ahead 04 with Dissolve(.25)
    voice "voice/Polina/4day/140 No.ogg"
    Pol "Но парни всегда забывают о главном: сначала надо спросить мнение девушки."
    play test_one "sounds/steps/Polina_step_02.ogg" 

    show Polina 3_4 b_day 01 norm ahead 01:
        xzoom -1
        xoffset -100
        yoffset 10
        parallel:
            linear 6 xoffset -1500

        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 15
    show Polina 3_4 b_day 01 norm ahead 04 with Dissolve(.25)
    show Polina 3_4 b_day 01 norm ahead 01 with Dissolve(.25)
    voice "voice/Polina/4day/141 Ade.ogg"
    Pol "А девушка говорит: после уроков у запасного выхода."
    stop music2 fadeout 3

    scene ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        align (.5,.5)
    with Dissolve(.5)
    show ant_clas_1 ul with Dissolve(.25):
        align (.5,.5)

    "Я улыбнулся облегчённо."
    queue test_one [ "<silence 0>", "<from 0 to 0.5>sounds/steps/Podoshe_2.ogg"] 
    show day3_ant_clas_romka with Dissolve(.25):
        xalign 1.
        yalign 1
    pause .25
    scene day3_end_class_bg:
        xpos 0

    show Romka Angry m_day 001 happy ahead 05:
        zoom 1.25
        xoffset -370
        yoffset -130
    show stone_pie 1:
        subpixel True
        ypos 100
        parallel:
            ease 1 xoffset 5 yoffset 5
            ease 1 xoffset -5 yoffset 5
            ease 1 xoffset 0 yoffset 10
            ease 1 xoffset 5 yoffset 5
            ease 1 xoffset -5 yoffset 0
            repeat
        parallel:
            easein .15 xpos 10 ypos 250
            ease .25 xpos 0 ypos 0


    play sound "sounds/sfx_grab_pie.ogg"

    "Совесть снова принялась поедать душу, когда вернувшийся Ромка бросил мне пирожок с брусникой и подмигнул."
    show Romka Angry m_day 001 happy ahead 05 with Dissolve(.25)
    show stone_pie blur:
        linear 1 yoffset 1000
    show Romka Angry m_day 001 happy ahead 04 with Dissolve(.25)
    voice "voice/romka/4day/Esh.ogg"
    Rom "Ешь, набирайся сил для нашего спектакля!"
    show Romka Angry m_day 001 happy ahead 05 with Dissolve(.25)
    "Но актёр, играющий отрицательную роль – то есть я – на спектакль не пришёл."
    scene bg_black
    with Dissolve(.5)
    play music2 "music/Buried In The Sands.ogg" fadein 1
    "Я отпросился у учительницы за двадцать минут до конца алгебры. Соврал, что болит зуб."


    scene bg school_day:
        yalign 0.8 xalign 0.5
    show blizzard_d4_day_far onlayer master1
    show blizzard_d4_day_near onlayer master1
    with Dissolve(0.5)
    play test_two "sounds/school_door-open-1.ogg"
    $ renpy.pause(0.2)
    play test_two "sounds/school_door-close-1.ogg"

    scene bg school_corner_day_onshow_2
    stop test_one fadeout 6

    "Спрятался за школьными кустами, как преступник."
    "Вскоре появилась Полина."
    queue test_two [ "<silence 0.1>", "<from 0 to 6.5>sounds/steps/sfx_girl_leaves_on_snow.ogg"]
    $ renpy.scene("master1")
    scene bg school_corner_day1_no_squirrel:
        xoffset 0
        yalign 0.5
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    with Dissolve(.25)
    show Polina Front m_day_winter 00 norm aside 01:
        xzoom -1
        xoffset 1200
        yoffset 10
        parallel:
            linear 6. xoffset 0
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 12
    window hide
    pause
    show Polina Front m_day_winter 00 norm ahead 01

    voice "voice/anton/4day/22. Ei.ogg"
    Ant "Эй, я тут!"
    show Polina Front m_day_winter 00 norm ahead 02 with Dissolve(0.2)
    voice "voice/Polina/4day/142 Tib.ogg"
    Pol "Ты б ещё в сугроб зарылся!"
    show Polina Front m_day_winter 00 norm ahead 01 with Dissolve(0.2)
    "Я понимал, что подло пытаюсь усидеть на двух стульях: не лишиться поддержки Ромы и тайно завоевать Полину."
    "Интересно, какой из стульев хрустнет подо мной первым?"
    voice "voice/anton/4day/23. Poi.ogg"
    Ant "Пойдём скорее."
    stop music2 fadeout 2.5
    show Polina Front m_day_winter 00 norm aside 02 with Dissolve(0.2)
    voice "voice/Polina/4day/143 Nu.ogg"
    Pol "Ну пойдём."
    play test_two "sounds/steps/sfx_girl_leaves_on_snow.ogg"
    show Polina Front m_day_winter 00 norm aside 01 with Dissolve(0.2)
    show Polina Front m_day_winter 00 norm aside 01:
        xoffset 0
        parallel:
            linear 1.2 xoffset -240
        parallel:
            linear .2 yoffset 12
            linear .2 yoffset 0
            linear .2 yoffset 12
            linear .2 yoffset 0
            linear .2 yoffset 12
            linear .2 yoffset 0
    pause .8
    stop test_two fadeout 1
    $ story_manager.MarkEvent(("day4", "scene_t2"))
    scene bg_white with dissolve
    $ polina_face_state = 5
    $ anton_face_polwalk_state = 0
    $ SetParSpeed(120)
    show walking_fox_11_day
    show walking_fox_12_day
    show walking_fox_21_day
    show walking_fox_22_day
    show walking_fox_31_day
    show walking_fox_32_day
    show blizzard_d4_day_far:
        block:
            xpan 0
            linear 80 xpan -360
            repeat
    show blizzard_d4_day_near zorder 5:
        block:
            xpan 0
            linear 60 xpan -360
            repeat
    show pol_walk_day_left
    show ant_walk_day_left
    stop test_one fadeout 0.5
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop
    play music2 "music/Lucky.ogg" volume 0.8 fadein 2.5
    "Мы зашагали вдоль стадиона."
    "Солнце светило ярко, но не согревало промёрзшую землю."
    "Сумерки затаились в чаще, ожидая нетерпеливо, когда можно будет выползти и поглотить посёлок."
    voice "voice/anton/4day/24. Ya.ogg"
    Ant "Я уже отвык от городского шума. Здесь всегда так тихо."
    $ polina_face_state = 0
    voice "voice/Polina/4day/20 O.ogg"
    Pol "О, а я мечтаю о какофонии!"
    voice "voice/anton/4day/25. O.ogg"
    Ant "О како... чём?"
    play test_three "voice/Polina/4day/112 Hah.ogg"
    "Моя спутница засмеялась."
    voice "voice/Polina/4day/21 Kak.ogg"
    Pol "Какофония – это случайное сочетание звуков."
    voice "voice/Polina/4day/22 De.ogg"
    Pol "Дедушка учит находить мелодию во всём."
    voice "voice/anton/4day/67. On.ogg"
    Ant "Он у тебя философ."
    voice "voice/Polina/4day/41 Kra.ogg"
    Pol "Краевед... Был раньше."
    voice "voice/anton/4day/26. On.ogg"
    Ant "Он, наверное, классный."
    voice "voice/Polina/4day/23 Ne.ogg"
    Pol "Не то слово! Скоро я вас познакомлю."
    voice "voice/anton/4day/27. Ti.ogg"
    Ant "Ты меня в гости приглашаешь?"
    voice "voice/Polina/4day/24 A.ogg"
    Pol "А ты против?"
    voice "voice/anton/4day/28. Net.ogg"
    Ant "Нет! Конечно, нет!"
    "Тайком я рассматривал Полину."
    "Она казалась драгоценным камнем, чьи грани переливаются, мерцают, неуловимо меняясь."
    "«Что?» – спрашивали невинно её смеющиеся глаза."
    "«То!» – молча отвечал я."
    voice "voice/Polina/4day/TiS.ogg"
    Pol "Ты смелый. Мне это нравится."
    voice "voice/anton/4day/Smel.ogg"
    Ant "Смелый?"
    voice "voice/Polina/4day/144 Ya.ogg"
    Pol "Я до сих пор вспоминаю, как ты Бабурина осадил!"
    voice "voice/anton/4day/30. Pu.ogg"
    Ant "Пустяки."
    voice "voice/Polina/4day/145 Zna.ogg"
    Pol "Знаешь, как для девочек важно, чтобы их защищали!"
    voice "voice/anton/4day/31. Za.ogg"
    Ant "Заступиться за тебя — честь."
    voice "voice/Polina/4day/146 Vot.ogg"
    Pol "Вот! Я же говорю!"
    voice "voice/Polina/4day/147 Ez.ogg"
    Pol "Изъясняешься словами из романов."
    voice "voice/Polina/4day/148 Eto.ogg"
    Pol "Это честь для меня, моя госпожа!"
    play test_two "voice/Polina/4day/177 Hiha.ogg"
    "Полина захихикала."
    play test_three "voice/anton/4day/32. Hehe.ogg"
    "Я надулся притворно, но не сумел удержаться и тоже улыбнулся." id d4_school_fox_betray_b665ff3b
    stop test_seven fadeout 6
    stop music2 fadeout 4

    jump d4_polhouse_begin



label d4_school_fox_voltron:
    $ story_manager.MarkEvent(("day4", "scene_v"))
    scene ant_clas_fon:
        xpos -300
    show Ant Normal b_day 01 norm ahead 01
    show day3_ant_clas_polina:
        align (1., 1.)
    with Dissolve(.25)

    show Ant Normal b_day 01 norm ahead 11 with Dissolve(.15)

    voice "voice/anton/4day/33. Poch.ogg"
    Ant "Почему бы и нет... Давай."

    show Ant Normal b_day 01 norm ahead 01 with Dissolve(.15)

    voice "voice/Polina/4day/149 Togda.ogg"
    Pol "Тогда после алгебры на заднем дворе."

    scene day3_end_class_bg:
        xalign 1.

    show Polina Front b_day 01 norm ahead 03:
        xzoom -1
        xoffset -100
        yoffset 10

    with Dissolve(.25)
    play sound "sounds/sfx_girl_comes3.ogg"

    "Она привстала и снова посмотрела на меня своими пронзительными глазами."
    "Пробормотала, гадая:"

    show Polina Front b_day 01 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/18 Ch.ogg"
    Pol "Что-то из Мусоргского?"
    show Polina Front b_day 01 norm ahead 03 with Dissolve(.15)
    show Polina Front b_day 01 norm aside 02 with Dissolve(.15)
    voice "voice/Polina/4day/19 Ne.ogg"
    Pol "Нет, пожалуй."
    play test_two "sounds/steps/Polina_step_01.ogg"
    stop music2 fadeout 3
    show Polina Front b_day 01 norm aside 03 with Dissolve(.15)

    play sound "sounds/loop_footsteps_class_light.ogg" fadein 0.3
    $ renpy.music.set_pan(-0.8, delay=3, channel="sound")
    $ renpy.music.set_volume(0.2, delay=3, channel="sound")

    show Polina Front b_day 01 norm aside 03:
        xzoom -1
        xoffset -100
        yoffset 10
        parallel:
            linear 1. xoffset -250
        parallel:
            linear .20 yoffset 0
            linear .20 yoffset 10
            repeat 3

    show day3_end_class_bg as overlay_bg:
        xalign 1.
        alpha 0
        .75
        linear .25 alpha 1

    $ renpy.pause(1.5)
    stop sound fadeout 1

    scene day3_end_class_bg:
        xalign 1.

    show Romka Normal b_day 01 norm aside 01:
        xoffset -200
        yoffset 20

        parallel:
            linear 1 xoffset -400
            "Romka Normal b_day 01 norm ahead 01"
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 2
    with Dissolve(.25)

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    $ renpy.music.set_volume(1, delay=0, channel="sound")

    play music "music/42_Talk.ogg" volume 0.7 fadein 1.5
    queue sound ["<silence 0.1>", "<from 0 to 8>sounds/sfx_footsteps_sit.ogg"] 

    "И ушла, а вместо неё в проходе вырос Ромка. Он плюхнулся ко мне за парту и зашептал на ухо:"

    show Romka Normal b_day 01 norm ahead 03 with Dissolve (.15)
    voice "voice/romka/4day/79 Ti.ogg"
    Rom "Ты с ней говорил?"
    show Romka Normal b_day 01 norm ahead 01 with Dissolve (.15)

    $ renpy.music.set_pan(0.4, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_class_normal.ogg" fadein 0.4
    $ renpy.music.set_pan(0, delay=2, channel="sound")

    show Byasha Normal b_day 01 normal ahead 07 behind Romka:
        xoffset 500
        yoffset 20
        alpha 0

        parallel:
            linear 1 xoffset 300
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 2
        parallel:
            linear .25 alpha 1

    $ renpy.pause(1)
    stop sound fadeout 1

    play test_six "voice/byasha/4day/51 ha.ogg"
    "Бяша проковылял к нам, но Рома осадил его сердитым взором:"

    play sound "sounds/sfx_chair_squeak.ogg"

    show Romka Normal b_day 01 what aside 03:
        xzoom -1
    with Dissolve (.15)
    voice "voice/romka/4day/80 Bya.ogg"
    Rom "Бяш, отвали на пару минут."
    show Romka Normal b_day 01 what aside 01

    show Byasha Doubt b_day 01 normal ahead 02:
        xzoom -1
        xoffset 300
        yoffset 20

        1.

        parallel:
            linear 1 xoffset 500
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 2
        parallel:
            .75
            linear .25 alpha 0

    with Dissolve (.15)
    play test_six "voice/byasha/4day/35 oh.ogg"
    play sound ["<silence .8>", "<from 0 to 2>sounds/loop_footsteps_class_normal.ogg"]
    $ renpy.music.set_pan(0.5, delay=2, channel="sound")
    "Тот обиженно поджал губы и скрылся из класса."

    show Romka Normal b_day 01 norm ahead 01 with Dissolve(.15)
    "Рома опять повернулся ко мне:"
    show Romka Normal b_day 01 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/81 Nu.ogg"
    Rom "Ну? Говорил или нет?"
    show Romka Normal b_day 01 norm ahead 01 with Dissolve(.15)
    show Romka Normal b_day 01 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/82 Ona.ogg"
    Rom "Она что-то сказала про меня?"
    show Romka Normal b_day 01 norm ahead 01 with Dissolve(.15)

    scene ant_clas_fon:
        xpos -300
    show Ant Normal b_day 00 norm ahead 12
    show day3_ant_clas_romka:
        align (1., 1.)
    with Dissolve(.25)

    "Мне хотелось улыбаться печально и обречённо."
    "Ромка, капитан команды Вольтрона, был влюблён, действительно влюблён!"
    "В его взгляде кипела надежда, мольба, тревога."
    "И это делало его совсем наивным мальчиком, который оградился от мира спортом, резкими движениями и холодностью."

    show Ant Normal b_day 01 norm ahead 01 with Dissolve(.5)

    "Мог ли я предать его сейчас, когда он так уязвим?"
    "Мог ли сделать правильный выбор в ситуации, где нет ничего правильного?"
    play test_three "voice/anton/4day/34. Khm.ogg"
    "Я проговорил, откашлявшись:"
    show Ant Normal b_day 01 norm ahead 11 with Dissolve(.15)
    $ music_during_lines = 0.8
    voice "voice/anton/4day/35. Ona.ogg"
    Ant "Она спрашивала, где ты будешь после уроков."
    show Ant Normal b_day 01 norm ahead 01 with Dissolve(.15)

    scene day3_end_class_bg:
        xalign 1.
    show Romka Normal b_day 01 norm ahead 01:
        xzoom -1
        xoffset -400
        yoffset 20
    with Dissolve(.5)

    show Romka Angry b_day 01 happy ahead 03 with Dissolve(.5)

    "Лицо его стоило того, чтоб соврать, — оно буквально засветилось от счастья."
    show Romka Angry b_day 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/83 A.ogg"
    Rom "А ты что?"
    show Romka Angry b_day 01 happy ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/36. Sk.ogg"
    Ant "Сказал, что ты будешь на заднем дворе."
    play test_six "voice/romka/4day/84 M.ogg"
    "Ромка взволнованно облизнул губы. Вцепился мне в запястье – я испугался, что сломает."
    $ music_during_lines = 1.0
    show Romka Angry b_day 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/85 Nut.ogg"
    Rom "Ну Тоха! Ну спасибо, друг!"
    show Romka Angry b_day 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry b_day 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/86 Po.ogg"
    Rom "Погнали скорее готовиться!"
    show Romka Angry b_day 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry b_day 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/87 Sh.ogg"
    Rom "Ща мы ей закатим такую шоу-программу, что прям ого-го!"
    show Romka Angry b_day 01 happy ahead 03 with Dissolve(.15)

    show Romka Angry b_day 01 happy ahead 03:
        xzoom -1
        xoffset -400
        yoffset 20

        parallel:
            linear 1. xoffset -200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 4
        parallel:
            .75
            linear .25 alpha 0

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound ["<silence .1>", "<from 0 to 2>sounds/loop_footsteps_class_normal.ogg"]
    $ renpy.music.set_pan(0.5, delay=2, channel="sound")

    stop music fadeout 4
    "Он ушёл к ворчащему в коридоре Бяше, а я, оцепенев, уставился на пустой стул Полины. "
    play music2 "music/Buried In The Sands.ogg" fadein 1
    "Только что я променял одну дружбу на другую."
    "Оставалось лишь надеяться, что я не прогадал."

    stop fon fadeout 9

    scene bg_koridorchic_day:
        xalign 0.
        easein 8 xalign .35
    with Dissolve(.5)

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound "sounds/sfx_school_bell_hall.ogg" fadein 1.5
    play test_one "sounds/steps/loop_footsteps_school_one.ogg" fadein 1.5 loop

    "Эхо звонка металось по мрачным закоулкам школы."
    window hide

    scene bg_black
    with Dissolve(.5)

    scene bg school_day:
        yalign 0.8 xalign 0.5
    show blizzard_d4_day_far onlayer master1
    show blizzard_d4_day2_near onlayer master1
    with Dissolve(0.5)

    stop sound fadeout 4
    stop test_one fadeout 1.5

    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 2.5
    play test_two "sounds/school_door-open-1.ogg"
    $ renpy.pause(1.5)
    play test_two "sounds/school_door-close-1.ogg"

    play sound "sounds/sfx_zip.ogg" 
    window show
    "Наспех застёгивая куртку, я выпорхнул во двор."



    "Синоптики не соврали, пророча метель."
    "С севера наползало свинцовое облако. В нём клокотал могучий рёв."

    scene bg school_day as bg_pre:
        yalign 0.8 xalign 0.5
        parallel:
            easeout 5.0 xalign 0.
            alpha 0

    show bg school_corner_day1_no_squirrel as bg_after:
        alpha 0
        xalign 1.

        4.5

        parallel:
            easein 2.0 xalign 0.5
        parallel:
            linear .5 alpha 1



    play test_one "sounds/sfx_kids_laugh_distant.ogg"
    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 1
    "Дети вставали спиной к ветру и смеялись, когда порывы толкали их по катку."
    "Вьюга уносила смех в фиолетовую даль."
    stop music2 fadeout 4


    $ story_manager.MarkEvent(("day4", "scene_v2"))

    $ renpy.pause(0.5)

    scene bg school_corner_day1_no_squirrel
    hide blizzard_d4_day_far onlayer master1
    hide blizzard_d4_day2_near onlayer master1
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Angry m_day_winter 02 angry ahead 03 zorder 1:
        xoffset 500
        yoffset 20

    with Dissolve(.5)

    stop sound fadeout 1.6
    play music "music/Dvar - Uku Uki.ogg" volume 0.9 fadein 2
    "Ромка бросился ко мне, как только заметил на привычно пустом пятачке за школой."
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    $ music_during_lines = 0.6
    voice "voice/romka/4day/88 G.ogg"
    Rom "Готов? Точно не сдрейфишь?"
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/89 V.ogg"
    Rom "Второго шанса не будет."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    "Я не был готов. Абсолютно."
    "Живот покалывал, требовал убираться, не ввязываться в заранее проигрышное дело."
    "Но бросить Ромку на полпути я уже не мог из принципа."
    "Тот тем временем, загибая испачканные в чернилах пальцы, судорожно пересчитывал реквизит."
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/90 B.ogg"
    Rom "Букет есть."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/91 M.ogg"
    Rom "Маньяк присутствует."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/92 Ch.ogg"
    Rom "Чё там ещё?"
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/37.A.ogg"
    Ant "А что с моим образом?"
    voice "voice/anton/4day/37.Gde.ogg"
    Ant "Где мой топор или там..."
    voice "voice/anton/4day/37.M.ogg"
    Ant "...маска." id d4_school_fox_voltron_ccd9a42e
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/93 Da.ogg"
    Rom "Да не гони, Тоха!"
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/94 Na.ogg"
    Rom "Надень ту заячью, что с собой по жизни таскаешь."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/95 To.ogg"
    Rom "Только резче! Нельзя, чтобы Полина нас видела вместе."
    $ music_during_lines = 1.0
    show Romka Angry m_day_winter 02 angry ahead 03
    with Dissolve(.15)

    play sound "sounds/sfx_schoolbag_open.ogg" fadein 0.3

    scene d4_bg_backpack with Dissolve(.5):
        yzoom -1
    stop music fadeout 3
    "Я с недоверием поглядел на Ромку, но пальцы уже нащупали бегунок на молнии рюкзака и потянули за него в предвкушении."

    play sound "sounds/sfx_schoolbag_mask.ogg"
    play music "music/class.ogg" volume 0.75 fadein 1

    play test_five ["<silence .4>","sounds/sfx_mask_rustle.ogg"]

    "Вместо того чтобы удивиться, я испытал лишь облегчение, вытащив наружу моё настоящее «лицо»."

    scene bg school_corner_day1_no_squirrel
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Angry m_day_winter 02 angry ahead 03 zorder 1:
        xoffset 500
        yoffset 20

    show mask_01_up zorder 2
    with Dissolve(1.0)

    "Вместе с ним пришло спокойствие — и колики улеглись."
    "Я вспомнил ощущение полёта, невесомости, счастья."
    "Тут же проблемы Ромки показались до зевоты мелочными и несущественными."
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/96 Da.ogg"
    Rom "Давай, как репетировали."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/97 To.ogg"
    Rom "Только она появится..."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)

    voice "voice/anton/4day/38. Ya.ogg"
    Ant "Я прегражу ей дорогу."

    show Romka Angry m_day_winter 02 angry ahead 04:
        linear .15 yoffset 0
        linear .15 yoffset 20
    voice "voice/romka/4day/98 A.ogg"
    Rom "Ага, а я из-за тех кустов такой – бац! – и на выручку!"
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/99 T.ogg"
    Rom "Только веди себя посмелее, Тошик."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 02 angry ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/100 Ch.ogg"
    Rom "Чтоб как взаправду."
    show Romka Angry m_day_winter 02 angry ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/39. Y.ogg"
    Ant "Я постараюсь себя не сдерживать."
    "Простой кусочек картона и шерсти нёс в себе энергию, которая могла соперничать с яростью метели."

    window hide
    play sound "sounds/sfx_wear_mask.ogg"

    show mask_02_hand zorder 10
    hide mask_01_up
    with Dissolve(0.5)

    pause .5

    hide mask_02_hand
    show mask_03_face zorder 10
    with Dissolve(0.7)

    pause .5


    hide mask_03_face
    show mask_03_hide zorder 10
    with Dissolve(0.3)

    window show

    "И я не без удовольствия натянул настоящее лицо поверх очков."

    $ renpy.music.set_pan(0.4, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 1
    $ renpy.music.set_pan(-0.2, delay=1.5, channel="sound")
    $ renpy.pause(0.2)
    stop sound fadeout 2

    show Romka Angry m_day_winter 02 angry ahead 03:
        xoffset 500
        yoffset 20
        parallel:
            linear .5 xoffset 400
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 1
        parallel:
            .25
            linear .25 alpha 0
    "Поправил его, чтобы глаза смотрели точно в прорези."
    "Ромка исчез."

    hide Romka Angry m_day_winter 02 angry ahead 03

    $ renpy.music.set_pan(0.7, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_slow_light.ogg" fadein 1 loop
    $ renpy.music.set_pan(0.2, delay=2, channel="sound")
    $ renpy.pause(0.2)

    show Polina Front m_day_winter 00 norm aside 01 zorder 1:
        xzoom -1
        xoffset 1200
        yoffset 10
        parallel:
            linear 6. xoffset 0
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 12

    "А из-за школы вышла, оглядываясь, Полина."
    "Футляр из-под скрипки был неизменно с ней. Сапожки скрипели на свежем снегу."

    stop sound fadeout 1.4

    "Тучи проглотили солнце, и темнота обратила меня в длинноухий силуэт."
    show Polina Front m_day_winter 00 norm ahead 03 with Dissolve(.15)
    "С сомнением посмотрев в мою сторону, Полина начала огибать площадку."

    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.1
        rotate 2
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show d4_masked_anton zorder 1:
        align (.5, 1.)
        xzoom -1
        zoom .85
        transform_anchor True
        rotate 2
        yoffset 55


    with Dissolve(.5)

    "Хе-хе! Значит, не узнала."

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound "sounds/sfx_footsteps_snow_slow.ogg"

    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.1
        rotate 2
        linear .5 zoom 1.2 rotate 5
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show d4_masked_anton zorder 1:
        align (.5, 1.)
        transform_anchor True
        zoom .85
        xzoom -1
        rotate 2
        yoffset 55


        parallel:
            linear .5 zoom 1.
        parallel:
            linear .5 rotate 5



    "Я шагнул наперерез, совершенно не заботясь, что мой рост или одежда могли подсказать Полине, кто перед ней."
    voice "voice/anton/4day/40. Ti.ogg"
    Ant "{i}Ты, случаем, не потерялась, деточка?{/i} "

    scene bg school_corner_day1_no_squirrel
    hide blizzard_d4_day_far onlayer master1
    hide blizzard_d4_day2_near onlayer master1
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    $ renpy.music.set_volume(0.6, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 1 loop
    $ renpy.music.set_pan(0.6, delay=2, channel="sound")

    show Polina Front m_day_winter 01 norm ahead 03 zorder 1:
        xzoom -1
        xoffset 0
        yoffset 10
        parallel:
            linear 1. xoffset 200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
    with Dissolve(.5)

    $ renpy.pause(0.5)
    stop sound fadeout 1.6

    play test_six "voice/Polina/2day/Oh.ogg" 
    "Хмурясь, она потеснилась к кустам."

    $ renpy.music.set_pan(-0.8, delay=0, channel="sound")
    $ renpy.music.set_volume(1, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(-0.25, delay=4, channel="sound")

    show Romka Evil m_day_winter 02 normal alter 01 zorder 1:

        xoffset -1300
        yoffset 20
        parallel:
            linear 3. xoffset -700
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 6

    pause 3.

    stop sound fadeout 2

    play test_six "voice/romka/4day/101 Ch.ogg"
    "Из-за них тут же показался чертыхающийся Ромка."

    $ renpy.music.set_pan(-0.25, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(0, delay=4, channel="sound")

    show Romka Evil m_day_winter 02 normal ahead 01:

        xoffset -700
        yoffset 20
        parallel:
            linear 2. xoffset -300
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 4
    $ renpy.pause(0.6)
    stop sound fadeout 2
    stop music fadeout 35
    play music2 "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 35
    play test_six "voice/romka/4day/101 e.ogg"
    "Он неуклюже двигался боком, словно краб, и всё так же прятал руку с цветами за спиной."
    show Romka Evil m_day_winter 02 normal ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/102E.ogg"
    Rom "Эй, садист проклятый!"
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.15)
    show Romka Evil m_day_winter 02 normal ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/103 P.ogg"
    Rom "Пока я здесь, никто не обидит эту д-девушку."
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.15)
    show Romka Evil m_day_winter 02 normal ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/104 Po.ogg"
    Rom "Понял... ты?"
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.15)
    "Под маской я страдальчески вскинул брови."
    "Интонация Ромки была фальшивой и откровенно идиотской. На репетиции он отыгрывал во сто крат уверенней."

    play sound "sounds/sfx_grab_Polina.ogg"

    show Polina Front b_day_winter 01 sad ahead 03 zorder 2:
        xzoom -1
        yalign 1.
        zoom 1.02
        xoffset 100
        yoffset 20
    with Dissolve(.5)

    "Но я не подал виду, и, нагло схватив Полину за воротник, подтянул к себе."
    "Пальцы пробежали по её шелковистым локонам."

    show Polina Front b_day_winter 01 sad ahead 02:
        xzoom -1
        yalign 1.
        zoom 1.02
        xoffset 100
        yoffset 20
        linear .15 yoffset 0
        linear .15 yoffset 20

    play test_six "voice/Polina/4day/150 O.ogg"
    "Полина возмущённо ойкнула, но я только ухмыльнулся."

    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.5
        rotate 15
    show blizzard_d4_day_far
    show Polina Bunnied b_day_winter 01 afraid aside 01:
        align (.5, 1.)
        transform_anchor True
        rotate 5
        zoom 1.1
        yoffset 50
    show anton_zay_02:
        align (.0, 1.)
        xoffset -100
        transform_anchor True
        rotate 5
        zoom 1.1

    show blizzard_d4_day2_near
    with Dissolve(.5)

    play test_three "voice/anton/4day/41. Zlo.ogg"
    "Чувства вседозволенности и безнаказанности захлестнули меня."
    "Я намерился завалить Полинку на землю и тискать до синяков, пока несущий околёсицу Ромка не научится актёрствовать как надо."

    scene bg school_corner_day1_no_squirrel:
        align (.5, .5)
        transform_anchor True
        zoom 1.3
        rotate -10
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Evil m_day_winter 02 normal ahead 01 zorder 1:
        align (.5, .5)
        transform_anchor True
        zoom 1.0
        rotate -10
        yoffset 30
    with Dissolve(.5)

    show Romka Evil m_day_winter 02 normal ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/106 G.ogg"
    Rom "Говорю, не тронь!"
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.15)
    play test_six "voice/romka/4day/101K.ogg"
    "Но я не послушал и продолжил, пьянея от собственной власти, от того, что растерявшийся Ромка мямлил себе под нос."
    "А я мог делать что угодно под покровом заячьей личины."

    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.5
        rotate 15
    show blizzard_d4_day_far
    show Polina Bunnied b_day_winter 01 afraid aside 01:
        align (.5, 1.)
        transform_anchor True
        rotate 5
        zoom 1.1
        yoffset 50
    show anton_zay_02:
        align (.0, 1.)
        xoffset -100
        transform_anchor True
        rotate 5
        zoom 1.1
    show blizzard_d4_day2_near zorder 1
    with Dissolve(.5)

    hide anton_zay_02
    show anton_zay_03:
        align (.0, 1.)
        xoffset -100
        transform_anchor True
        rotate 5
        zoom 1.1
    with Dissolve(.35)
    voice "voice/anton/4day/41. Pro.ogg"
    Bunny "Прояви терпение, рохля! "
    voice "voice/anton/4day/42. S.ogg"
    Bunny "Сейчас закончу с девчонкой и обязательно возьмусь за тебя."

    scene bg school_corner_day1_no_squirrel:
        align (.5, .5)
        transform_anchor True
        zoom 1.3
        rotate -10
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Worry b_day_winter 01 norm ahead 02 zorder 1:
        align (.5, 1.)
        transform_anchor True
        zoom 1.0
        rotate -10
        yoffset 150
    with Dissolve(.5)

    play test_six "voice/romka/4day/107o.ogg"
    "У Ромки даже округлились глаза от удивления, и было видно, что он какое-то время пытался сохранить самообладание, чтобы не выйти из роли."
    "Но, прежде чем новоиспечённый герой хоть что-то предпринял, его опередила Полина."

    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.5
        rotate 15
    show blizzard_d4_day_far
    show Polina Bunnied b_day_winter 01 afraid aside 01:
        align (.5, 1.)
        transform_anchor True
        rotate 5
        zoom 1.1
        yoffset 50
    show anton_zay_02:
        align (.0, 1.)
        xoffset -100
        transform_anchor True
        rotate 5
        zoom 1.1
    show blizzard_d4_day2_near zorder 5
    with Dissolve(.5)

    show Polina Bunnied b_day_winter 01 hm ahead 01 with Dissolve(.5)
    pause .5
    show Polina Bunnied b_day_winter 01 hm ahead 02 with Dissolve(.25)
    $ music_during_lines = 0.6
    voice "voice/Polina/4day/152 Tak.ogg"
    Pol "Так, что тут происходит? "
    show Polina Bunnied b_day_winter 01 hm ahead 01 with Dissolve(.15)
    show Polina Bunnied b_day_winter 01 hm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/153 P.ogg"
    Pol "Пятифан, ты уберёшь своего дружка?"
    $ music_during_lines = 1.0

    window hide

    show Polina Bunnied b_day_winter 01 hm ahead 01 with Dissolve(.15)
    hide Polina
    hide anton_zay_02

    stop music2 fadeout 0.5
    play sound "sounds/sfx_blow_heavy.ogg"

    show d4_polina_strike:
        align (.5, .5)
        transform_anchor True
        zoom 1.1
        rotate 5
        xoffset 50
    pause .4
    hide d4_polina_strike
    with None
    scene day3_cornermeet_bg_fence_default:
        align (.5, .5)
        transform_anchor True
        zoom 1.5
        rotate 15
        linear .05 xoffset -25
        linear .05 xoffset 0
        linear .05 xoffset -20
        linear .05 xoffset 0
        linear .05 xoffset -20
        linear .05 xoffset 0
    show blizzard_d4_day_far
    show d4_polina_strike_last:
        align (.5, .5)
        transform_anchor True
        zoom 1.1
        rotate 5
        linear .05 xoffset -25
        linear .05 xoffset 0
        linear .05 xoffset -20
        linear .05 xoffset 0
        linear .05 xoffset -20
        linear .05 xoffset 0
    show blizzard_d4_day2_near
    pause .3

    show bg_white zorder 10:
        alpha 0
        linear .75 alpha 1
    play test_three "voice/anton/4day/43. A.ogg"
    "Полина наотмашь стукнула меня футляром так, что я мигом протрезвел."

    window show

    scene bg school_corner_day1_no_squirrel
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Worry b_day_winter 01 norm ahead 02 zorder 1
    show bg_white zorder 10:
        alpha 1
        linear .5 alpha 0

    play music "music/Byasha.ogg" volume 0.8 fadein 3
    voice "voice/romka/4day/108 Ya.ogg"
    Rom "Я же... Он мне..."

    scene day3_cornermeet_bg_fence_default
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Polina Front b_day_winter 01 angry ahead 03 zorder 1

    with Dissolve(.5)

    show Polina Front b_day_winter 01 angry ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/155 D.ogg"
    Pol "Думаете, я вчера на свет появилась?"
    show Polina Front b_day_winter 01 angry ahead 03 with Dissolve(.15)
    show Polina Front b_day_winter 01 angry ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/156 B.ogg"
    Pol "Бяша, небось? Или..."
    show Polina Front b_day_winter 01 angry ahead 03 with Dissolve(.15)
    "Она внимательно посмотрела на меня, словно могла видеть сквозь картонную маску."
    "И даже в тусклом освещении я видел, как порозовело её негодующее личико."
    show Polina Front b_day_winter 01 sad ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/157 An.ogg"
    Pol "Антон?"
    show Polina Front b_day_winter 01 angry ahead 03 with Dissolve(.15)
    show Polina Front b_day_winter 01 angry ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/158 Vot.ogg"
    Pol "Вот не думала, что ты такой."

    scene bg school_corner_day1_no_squirrel
    show blizzard_d4_day_far
    show Romka Worry b_day_winter 01 norm ahead 02:
        align (.5, 1.)
        zoom .85
        xoffset 200
    show d4_masked_anton:
        align (.5, 1.)
        xoffset -200
        zoom 1.
        xzoom -1
    show blizzard_d4_day2_near
    with Dissolve(.5)

    play test_three "voice/anton/4day/44.M.ogg"
    "Я замычал, ища оправдание, втайне надеясь, что Ромка опередит меня и всё объяснит."
    "Но фиговейший из актёров пялился на сугробы и краснел от стыда."
    "Спланировать такое шоу и так облажаться!"
    "Полина смотрела на нас, сжав кулаки, и вдруг выкрикнула:"

    scene day3_cornermeet_bg_fence_default
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Polina Scream b_day_winter 01 norm ahead 01 zorder 1
    with Dissolve(.5)

    $ poldt = .1
    scene day3_cornermeet_bg_fence_default:
        zoom 1.0
        poldt
        linear .15 zoom 1.05
        linear .35 zoom 1.00
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Polina Scream b_day_winter 01 norm ahead 01 zorder 1:
        pos (.5, .5)
        anchor (.5, .5)
        poldt
        "Polina Scream b_day_winter 01 norm ahead 03"
        linear .15 zoom 1.20
        linear .35 zoom 1.00

    show focus_lines_bright onlayer master1:
        align (.5,.5)
        alpha 0
        poldt
        linear .2 alpha 1

    show layer master:
        poldt
        block:
            linear .05 xoffset 10
            linear .05 xoffset -10
            repeat 5
        linear .1 xoffset 0

    play test_seven "music/caricature03.ogg" 
    voice "voice/Polina/4day/159 K.ogg"
    Pol "Клоуны!"

    hide focus_lines_bright onlayer master1
    show Polina Scream b_day_winter 01 norm ahead 01
    with Dissolve(.25)
    pause .25

    hide Polina
    show d4_polina_03 zorder 1:
        yoffset -134
    with Dissolve(.25)
    pause .25

    show d4_polina_03 zorder 1:
        xzoom -1
        yoffset -134
    with Dissolve(.25)
    pause .25

    $ renpy.music.set_pan(0.1, delay=0, channel="sound")
    $ renpy.music.set_volume(1, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_slow_light.ogg" fadein 1 loop
    $ renpy.music.set_pan(-1, delay=4, channel="sound")
    $ renpy.music.set_volume(0, delay=4, channel="sound")

    show d4_polina_03 zorder 1:
        yoffset -134
        xzoom -1
        parallel:
            linear 7. xoffset -1400
        parallel:
            linear .25 yoffset -144
            linear .25 yoffset -134
            repeat 14

    "Крик-вердикт ещё бился о школьные стены, как попавший в ловушку голубь, а Полина кинулась прочь от нас по заснеженному асфальту."

    stop sound fadeout 2

    "Она плеснула тенью, словно шлейфом платья, и скрылась за углом."
    stop music fadeout 3.5

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    $ renpy.music.set_volume(1, delay=0, channel="sound")
    play test_one "sounds/sfx_bouquet_drop.ogg"
    scene d4_flowers_on_snow
    show incar_snow_up
    with Dissolve(.5)

    play music2 "music/loss.ogg" fadein 1
    "Голова Ромки обречённо упала на грудь. Облезлый букет шлёпнулся в серую кашу мокрого снега."
    voice "voice/romka/4day/109 E.ogg"
    Rom "Это фиаско, братан!"


    scene bg school_corner_day1_no_squirrel
    show blizzard_d4_day_far onlayer master1 zorder 5
    show blizzard_d4_day2_near onlayer master1 zorder 15
    show Romka Sad b_day_winter 01 sad aside 06 onlayer master1 zorder 10

    with Dissolve(.5)

    play sound "sounds/sfx_mask_take_off.ogg"
    $ renpy.pause(0.4)

    show d4_mask_in_hands_day onlayer master1 zorder 10:
        alpha 0
        zoom 1.5
        align (.5,.5)
        linear .5 alpha 1. zoom 1
    play test_three "voice/anton/4day/45.A.ogg"
    "Я снял маску со вспотевшего лица. Ветер остудил кожу."
    "С маской я словно стащил слепок посторонних мыслей и эмоций."
    play test_six "voice/romka/4day/110 M.ogg"
    "Ромка скрипел зубами, таращась под ноги."
    play test_six "voice/romka/4day/110H.ogg"
    "Потерянный и подавленный, не умеющий, как и я, встречать контратакой удары судьбы."
    "Я видел, насколько ему плохо."
    play test_six "voice/romka/4day/110E.ogg"
    "Он готов был крушить всё вокруг, биться лбом о бетон."
    "Что угодно, но только не попросить Полину вернуться."
    "Он был сильным и смелым, но так боялся показаться слабым, что это мешало ему жить."

    play sound "sounds/sfx_put_hand.ogg"

    "Решение пришло молниеносно. Я положил ладонь Ромке на плечо."
    voice "voice/anton/4day/45. Z.ogg"
    Ant "Жди."

    window hide

    show Romka Sad b_day_winter 01 sad ahead 06 onlayer master1
    with Dissolve(.5)

    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 1.0 loop
    scene bg school_corner_day_onshow_3_bg
    show bg school_corner_day_onshow_3_fg as fg

    show Romka Sad b_day_winter 01 sad ahead 01 onlayer master1:
        ease 3.5 xoffset -506 - 1000

    pause 5
    hide Romka onlayer master1
    scene bg school_day:
        yalign .8
        xalign .5
    show Polina Back small onlayer master1 zorder 10:
        xzoom -1
    with Dissolve(.5)

    stop sound fadeout 1.2
    play test_five "sounds/loop_footsteps_asphalt.ogg" volume 0.65 fadein 2 loop
    pause .6

    window show
    $ story_manager.MarkEvent(("day4", "scene_v3"))

    "И кинулся по пришкольной территории, пытаясь догнать Полину."
    "Эхо повторяло стук подошв."
    "Скрипичный футляр девочки покачивался, как хвост раздражённого животного."
    voice "voice/anton/4day/46. Pol.ogg"
    Ant "Полин!"
    scene bg school_day:
        yalign .8
        xalign .5
        zoom 1.10
    $ renpy.scene("master1")
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Polina Back big zorder 1:
        xzoom -1

    with Dissolve(1.5)
    "Она сбавила шаг, но не обернулась."
    voice "voice/anton/4day/47. Nu.ogg"
    Ant "Ну Полин!"
    "Показался её хорошенький профиль."
    stop music2 fadeout 3

    stop test_five fadeout 0.9

    show Polina 3_4 b_day_winter 01 alert ahead 012 with Dissolve(.5):
        xzoom 1
        align (.5, .5)
        zoom 1.02
    voice "voice/Polina/4day/160 Ch.ogg"
    Pol "Чего?"
    play music "music/Cinematic Piano.ogg" volume 0.7 fadein 2
    show Polina 3_4 b_day_winter 01 alert ahead 09 with Dissolve(.15)

    play sound "sounds/sfx_clothes_rustle_light.ogg"

    "Я поравнялся с ней, осторожно взял за локоть. Она не отдёрнулась – хороший знак."
    voice "voice/anton/4day/48. Ti.ogg"
    Ant "Ты всё неправильно поняла."
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)

    "Полина убрала с лица прядь."
    "Я подумал, что этот жест она могла подсмотреть в каком-нибудь фильме с Шэрон Стоун."
    "Голос её оставался строгим."
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/161 Ct.ogg"
    Pol "Что тут понимать-то?!"
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/162 R.ogg"
    Pol "Ромка спланировал геройский поступок – в кавычках, конечно."
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/163 At.ogg"
    Pol "А ты вызвался быть шутом, от которого он меня защитит."
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/164 Es.ogg"
    Pol "Ещё и маску где-то нашёл гадкую такую!"
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    "Я вспыхнул: {i}«Ничего она не гадкая!{/i}», но вслух сказал:"
    voice "voice/anton/4day/49. Avot.ogg"
    Ant "А вот и не поняла!"
    voice "voice/anton/4day/50 T.ogg"
    Ant "Ты Ромке очень нравишься."
    "В её взгляде проскользнуло любопытство."
    "Мне так отчаянно захотелось обнять Полину, украсть, увести в лес."
    "Познакомить с моими новыми друзьями."
    "Чтобы флейта играла – Полине бы понравилась её мелодия."
    "Чтобы мы прыгали до небес, выше облаков."
    "И там, под приколоченными к небосводу звёздами, я бы рассказал Полине, как нуждаюсь в ней."
    "Что она – вода, а я умираю от жажды."
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/166 Ya.ogg"
    Pol "Я думала, я тебе нравлюсь."
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    "Я притворился дурачком."
    voice "voice/anton/4day/50. Mne.ogg"
    Ant "Мне?"
    play test_six "voice/Polina/4day/167 V.ogg" 
    "Полина обиженно вырвалась."
    show Polina 3_4 b_day_winter 02 worry ahead 012:
        xzoom 1
        xoffset 0
        yoffset 0
        parallel:
            linear .3 xoffset -100
        parallel:
            linear .15 yoffset -10
            linear .15 yoffset 0
            repeat 1

    play sound "sounds/steps/step_snow2.ogg"

    voice "voice/Polina/4day/168 Vs.ogg"
    Pol "Всё ясно!"
    show Polina 3_4 b_day_winter 02 worry ahead 09 with Dissolve(.15)
    voice "voice/anton/4day/51.Da.ogg"
    Ant "Да постой же! Нравишься!"
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    voice "voice/anton/4day/51.T.ogg"
    Ant "Ты всем нравишься."
    voice "voice/anton/4day/51.No.ogg"
    Ant "Но Ромка – он особенный."
    show Polina 3_4 b_day_winter 02 alert ahead 012 with Dissolve(.15)
    voice "voice/Polina/4day/169 Os.ogg"
    Pol "Особенный лжец."
    show Polina 3_4 b_day_winter 02 alert ahead 09 with Dissolve(.15)
    voice "voice/anton/4day/52. On.ogg"
    Ant "Он целеустремлённый и на самом деле серьёзнее, чем кажется."
    voice "voice/anton/4day/52.Po.ogg"
    Ant "Помнишь, ты говорила о побеге? С ним бы ты точно сбежала."
    voice "voice/anton/4day/52.V.ogg"
    Ant "В какой-нибудь большой сверкающий город."
    voice "voice/anton/4day/52.Da.ogg"
    Ant "Да куда угодно!"
    voice "voice/anton/4day/52.On.ogg"
    Ant "Он обещал защищать тебя."
    show Polina Front b_day_winter 02 norm aside 03 with Dissolve(.15)
    "Полина смотрела в темноту за чертогами школы. Там выл ветер и клубился снег."
    show Polina Front b_day_winter 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/170 E.ogg"
    Pol "И что теперь прикажешь?"
    show Polina Front b_day_winter 02 norm ahead 03 with Dissolve(.15)
    show Polina Front b_day_winter 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/171 Ot.ogg"
    Pol "От его обещаний детей рожать?"
    show Polina Front b_day_winter 02 norm ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/52.Dl.ogg"
    Ant "Для начала узнать поближе, дать ему шанс."
    voice "voice/anton/4day/53.Sh.ogg"
    Ant "Шутки шутками, а настоящий маньяк ещё на свободе."
    voice "voice/anton/4day/53.Po.ogg"
    Ant "Позволь Ромке проводить тебя сегодня."
    "Я говорил, а губы мои немели и деревенело лицо."
    "Я боялся, что голос выдаст истинные чувства."
    "Слова были бритвами, которые резали мне грудь и гортань, высыпаясь наружу."
    "Полина молчала бесконечно долго, а потом ещё дольше."

    play sound "sounds/sfx_fingers_drumming_case.ogg"
    play test_five "sounds/loop_sniffing.ogg" fadein 0.6 loop

    "Она возмущённо сопела и барабанила пальцами по чёрному футляру."

    stop test_five fadeout 0.15

    show Polina Front b_day_winter 01 norm ahead 03 with Dissolve(.15)
    play test_three "voice/Polina/4day/02 Vzdoh.ogg"
    "Наконец она сказала, вздохнув:"
    show Polina Front b_day_winter 01 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/172 Pe.ogg"
    Pol "Передай своему Ромке, что я жду у школьных ворот."
    show Polina Front b_day_winter 01 norm ahead 03 with Dissolve(.15)
    show Polina Front b_day_winter 01 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/173 no.ogg"
    Pol "Но чтоб не думал себе всякое!"
    show Polina Front b_day_winter 01 norm ahead 03 with Dissolve(.15)
    "Я изобразил радость: когда надо, я мог притворяться."
    voice "voice/anton/4day/54. T.ogg"
    Ant "Ты не пожалеешь."

    hide blizzard_d4_day_far
    hide blizzard_d4_day2_near
    show blizzard_d4_day_far onlayer master1 zorder 5
    show blizzard_d4_day2_near onlayer master1 zorder 15
    show Polina Front b_day_winter 01 norm ahead 03 onlayer master1 zorder 10:
        xzoom 1
        align (.5, .5)
        zoom 1.02
        yoffset 0
        xoffset -100
    with Dissolve(.5)

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop

    scene bg school_corner_day_onshow_4_bg:
        zoom 1.10
    show Polina Front b_day_winter 01 norm ahead 03 onlayer master1 zorder 10:
        xzoom 1
        align (.5, .5)
        zoom 1.02
        yoffset 0
        xoffset -100
        parallel:
            ease 5.0 xoffset 1500
        parallel:
            1.5
            "Polina Front b_day_winter 01 norm aside 03"
    show bg school_corner_day_onshow_4_fg as fg zorder 1
    show d4_roma_sad_mono onlayer master1 zorder 10:
        yoffset 350
        parallel:
            xoffset -500
            ease 5.0 xoffset 0
        parallel:
            alpha 0
            1.5
            linear 1.5 alpha 1

    "Я брёл обратно за угол, вслепую шаркая по снегу, потому что веки мои были плотно зажмурены, а сердце билось, как молот, вгоняя в душу гвозди."
    scene bg school_corner_day1_no_squirrel:
        xalign 0.5
        yalign 0.5
    $ renpy.scene("master1")
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Sad m_day_winter 01 sad aside 01 zorder 1:
        yoffset 350
    with Dissolve(.5)

    stop sound fadeout 1.5

    "Ромка сидел на корточках, взъерошивая короткие волосы."
    show Romka Sad m_day_winter 01 sad ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/55. Ona.ogg"
    Ant "Она ждёт тебя у ворот."
    stop music fadeout 2.0
    show Romka Angry m_day_winter 01 happy ahead 03 with Dissolve(.15)

    "Наградой мне было изумление на лице товарища."
    show Romka Angry m_day_winter 01 happy ahead 03 with Dissolve(.15):
        linear .5 yoffset 0

    play sound "sounds/sfx_Romka_get_up.ogg"

    "Он вскочил, захлёбываясь словами."
    "Совсем не тот замкнутый лидер-молчун, с которым я познакомился на прошлой неделе."
    scene bg school_corner_day1_no_squirrel:
        xalign 0.5
        yalign 0.5
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    play sound "sounds/steps/step_snow2.ogg"
    show Romka Angry b_day_winter 01 happy ahead 04 zorder 1 with Dissolve(.35)
    voice "voice/romka/4day/111 T.ogg"
    Rom "Тош, ты спас меня!"
    show Romka Angry b_day_winter 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry b_day_winter 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/112 B.ogg"
    Rom "Братан, да я теперь твой должник на века."
    show Romka Angry b_day_winter 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry b_day_winter 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/113H.ogg"
    Rom "Хошь, я тебе тетрис подгоню? А хошь, научу рукопашным приёмам?"
    show Romka Angry b_day_winter 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry b_day_winter 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/114 E.ogg"
    Rom "Или..."
    show Romka Angry b_day_winter 01 happy ahead 03 with Dissolve(.15)

    scene day3_cornermeet_bg_fence_default
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show d4_anton zorder 1

    with Dissolve(.5)
    play test_six "voice/anton/2day/181. Ya tazelo vdohnul.ogg"
    "Я мечтал об одном: чтоб меня оставили в покое."
    "Чтобы я мог стоять в тишине и смотреть, как колышется на ветру лес."
    "Вдыхать морозный запах хвои сквозь старую маску."
    show d4_anton rot as rot zorder 1 with Dissolve(.15)
    voice "voice/anton/4day/56. Ed.ogg"
    Ant "Иди уже."
    hide rot with Dissolve(.15)
    "Хотелось верить, что в случае с Алисой мне не придётся выбирать между чувствами и дружбой."
    stop music2 fadeout 2.5
    "Кроме неё у меня уже никого не осталось..."
    play music "music/25_Olya.ogg" fadein 1

    $ renpy.music.set_volume(0, delay=2, channel="fon")

    window hide
    scene bg_white with Dissolve(1.0)
    pause 0.5
    scene bg kitchen1_0
    show kitchen ol3_0_1
    show ramka1
    with Dissolve(0.7)
    window show
    "...разве что Оля." id d4_school_fox_voltron_2d5d93dd
    "Ну конечно, мой лучик света в этой кромешной чёрной тайге."
    "Как я мог забыть о своей маленькой сестрёнке?"


    $ renpy.music.set_volume(1, delay=2, channel="fon")

    scene bg_white with Dissolve(.15)
    scene bg school_corner_day1_no_squirrel:
        xalign 0.5
        yalign 0.5
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Angry m_day_winter 01 happy aside 03 zorder 1:
        yoffset 20
        parallel:
            linear 1. xoffset -200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 2
        time 1.
        "Romka Angry m_day_winter 01 happy ahead 03"

    with Dissolve(.5)
    play test_three "sounds/steps/snow_stepS03.ogg"
    $ music_during_lines = 0.6
    voice "voice/anton/4day/57. Ya.ogg"
    Ant "Я знаю, чего я хочу."
    "Ромка, успевший сделать несколько шагов, остановился и посмотрел на меня."
    voice "voice/anton/4day/58. Y.ogg"
    Ant "Я хочу оказаться вместе с сестрой в «Диснейленде»."
    $ music_during_lines = 1.0
    stop music fadeout 3.5

    play sound "sounds/sfx_hat_adjust.ogg"

    play test_six "voice/romka/4day/115 Ha.ogg"
    "Мой приятель ухмыльнулся, сдвинув шапку на затылок."
    show Romka Angry m_day_winter 01 happy ahead 04 with Dissolve(.15)
    play music2 "music/Beautiful mystery.ogg" volume 0.75 fadein 1
    $ music_during_lines = 0.7
    voice "voice/romka/4day/116 E.ogg"
    Rom "И что ты предлагаешь?"
    show Romka Angry m_day_winter 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/117 S.ogg"
    Rom "Сберкассу обнести?"
    show Romka Angry m_day_winter 01 happy ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/59.Ne.ogg"
    Ant "Нет, надо просто поймать маньяка."
    voice "voice/anton/4day/60.To.ogg"
    Ant "Того, кто в ответе за все эти похищения."
    voice "voice/anton/4day/60.E.ogg"
    Ant "И получить обещанную награду в милиции."

    play sound "sounds/sfx_pocket_hand.ogg" volume 0.5
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.5)

    "Ромка скривился, спрятал руки в карманы штанов."
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/118 D.ogg"
    Rom "Думаешь, тебе этот лейтенант что-то за сотрудничество отстегнёт?"
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/119 Po.ogg"
    Rom "Подарит максимум часы командирские — и будь здоров!"
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    "Меня утомило пререкаться с Ромкой."
    voice "voice/anton/4day/60. Ti.ogg"
    Ant "Ты поможешь мне? Да или нет?"
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/120 Ya.ogg"
    Rom "Я сказал уже: мы команда."
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/121 K.ogg"
    Rom "Куда ты — туда и я."
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    voice "voice/anton/4day/60.Ho.ogg"
    Ant "Хорошо."
    voice "voice/anton/4day/60.Te.ogg"
    Ant "Теперь понять бы, с чего начинать."
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/122 S.ogg"
    Rom "Слушай!"
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/123 By.ogg"
    Rom "Бяша говорил, что слышал плач в буреломе за кладбищем."
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/124 G.ogg"
    Rom "Готов поспорить, это была Катька."
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)

    scene day3_cornermeet_bg_fence_default
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show d4_anton zorder 1
    with Dissolve(.5)
    "Я весь собрался, превратился в нерв."
    "Катя – это шажок к Семёну, а от него – к Вове."
    "Поможем милиции арестовать убийцу — и проклятый маньяк перестанет держать наш посёлок в страхе."
    "А с ним уйдут взрослые запреты, что не разрешают Оле выходить на улицу."

    show d4_anton 2 with Dissolve(.5)

    "И я, наконец, научу её прыгать до небес вместе с новыми друзьями."

    show d4_anton rot as rot zorder 1
    with Dissolve(.15)
    voice "voice/anton/4day/61.Ka.ogg"
    Ant "Как тогда будем действовать?"
    hide rot with Dissolve(.15)

    scene bg school_corner_day1_no_squirrel:
        xalign 0.5
        yalign 0.5
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Romka Normal m_day_winter 00 what ahead 02 zorder 1:
        yoffset 20
        xzoom -1
    with Dissolve(.5)

    show Romka Normal m_day_winter 00 what aside 03 with Dissolve(.25)
    voice "voice/romka/4day/125 T.ogg"
    Rom "Так сразу не скажу, да и время поджимает."
    show Romka Normal m_day_winter 00 what aside 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/126 Da.ogg"
    Rom "Давай пересечёмся у дома Полины через час."
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/127 N.ogg"
    Rom "Нет, лучше через полтора!"
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_day_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/128 Z.ogg"
    Rom "Знаешь, где она живет?"
    show Romka Normal m_day_winter 00 what ahead 02 with Dissolve(.15)
    "Я вспомнил номер дома, тайком подсмотренный в анкете Полины."
    voice "voice/anton/4day/63. Du.ogg"
    Ant "Думаю, найду."
    show Romka Angry m_day_winter 01 happy ahead 04 with Dissolve(.15)
    voice "voice/romka/4day/129 O.ogg"
    Rom "Отлично! Мне пора."
    $ music_during_lines = 1.0

    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 1
    $ renpy.music.set_pan(-0.5, delay=3, channel="sound")

    show Romka Angry m_day_winter 01 happy ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 01 happy aside 03:
        parallel:
            linear 2. xoffset 500
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 4
        parallel:
            1.
            linear .5 alpha 0

    pause 2
    stop sound fadeout 1.2

    "И Ромка умчал, а я остался усмирять галоп в грудной клетке."
    stop music2 fadeout 3.5

    window hide

    $ renpy.music.set_pan(0, delay=0.2, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1
    scene bg school_corner_day_onshow_3_bg
    show bg school_corner_day_onshow_3_fg as fg
    show blizzard_d4_day_far onlayer master1
    show blizzard_d4_day2_near onlayer master1
    pause 5

    scene bg school_day:
        yalign .8
        xalign .5
    hide blizzard_d4_day_far onlayer master1
    hide blizzard_d4_day2_near onlayer master1
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Byasha Normal m_day_winter 01 normal aside 03 zorder 1
    with Dissolve(.5)
    stop sound fadeout 1.3
    window show
    "Быть может, теперь, с Ромкиной поддержкой, весь этот ужас, наконец, прекратится."
    stop music2 fadeout 3.5

    $ story_manager.MarkEvent(("day4", "scene_v4"))
    scene bg school_day:
        yalign .8
        xalign .5
        zoom 1.10
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5
    show Byasha Normal b_day_winter 01 normal aside 03 zorder 1:
        xoffset -400
        yoffset 10
    with Dissolve(1.5)

    play sound "sounds/sfx_two_footsteps_snow.ogg"

    show Byasha Normal b_day_winter 01 normal ahead 03 with Dissolve(.5)
    pause .25
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.5)

    play music "music/Byasha.ogg" volume 0.8 fadein 2
    play test_six "voice/byasha/4day/177 Hek.ogg"
    "Лузгающий семечки Бяша скривился, как только я подошёл к нему."

    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/178 S.ogg"
    Bya "Смотрите-ка... тьфу! Явился не запылился, на!"
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)
    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/179 Br.ogg"
    Bya "Бросили меня тут, на… тьфу… и срулили вдвоём… Тьфу, голубки."
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)
    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/180 Aes.ogg"
    Bya "А ещё, на, команда Вольтрона называется. Тьфу!"

    play sound "sounds/sfx_coat_rustle_1.ogg"

    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)

    show Byasha Doubt b_day_winter 01 normal aside 01 with Dissolve(.5)
    play test_six "voice/byasha/4day/182 Shmig.ogg"
    "Бяша нахохлился и демонстративно отвернулся."
    "На минуту я задумался, взвешивая про себя, а пригодится ли нам помощь Бяши в поисках Кати? Или этот Ромкин прихвостень только всё испортит?"

    label dev_byasha hide:

    $ story_manager.MarkEvent(("day4", "byasha"))

    scene bg school_day:
        yalign .8
        xalign .5
        zoom 1.10
    show blizzard_d4_day_far
    show blizzard_d4_day2_near onlayer screens zorder 1
    show blizzard_d4_day2_near zorder 5:
        alpha 0
    show Byasha Doubt b_day_winter 01 normal aside 01:
        xoffset -400
        yoffset 10

    with Dissolve(.5)


    $ renpy.start_predict("d4_byasha_call_img_hover")

    window hide
    call screen day4_byasha_call_or_dismiss()



label d4_byash_choice_dismiss:
    $ story_manager.MarkEvent(("day4", "byasha", "dismiss"))
    show blizzard_d4_day2_near zorder 5:
        alpha 1
    hide blizzard_d4_day2_near onlayer screens
    with Dissolve(.5)
    $ renpy.stop_predict("d4_byasha_call_img_hover")
    "И если я ещё мог поверить в Ромкину дружбу, то его подхалим и прислужник Бяша всегда вызывал у меня отвращение."

    voice "voice/anton/4day/81. Che.ogg"
    Ant "Чего ты сразу, как девчонка, обижаешься?"
    voice "voice/anton/4day/82.Vot.ogg"
    Ant "Вот уж не подумал, что ты так в роль вживёшься."

    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.5)

    play test_six "voice/byasha/4day/177 Sk.ogg"
    "Он ядовито прыснул."

    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/183 Da.ogg"
    Bya "Да пошли вы, на! Тоже мне друзья."
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)
    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/184 Es.ogg"
    Bya "Если сгинете — я по вам скучать не буду, на."
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)
    show Byasha Doubt b_day_winter 01 normal ahead 02 with Dissolve(.15)
    voice "voice/byasha/4day/185 V.ogg"
    Bya "Вы..."
    show Byasha Doubt b_day_winter 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/70. Da.ogg"
    Ant "Да иди уже."

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.4
    $ renpy.music.set_pan(-0.6, delay=2, channel="sound")

    show Byasha Doubt b_day_winter 01 normal aside 01:
        parallel:
            linear 2. xoffset -800
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 4
    with None


    $ achievement_grant("ach_no")

    scene bg school_day:
        yalign .8
        xalign .5
        zoom 1.10
    show blizzard_d4_day_far onlayer master1 zorder 1
    show blizzard_d4_day_near onlayer master1 zorder 5
    with Dissolve(.5)
    pause 2
    stop sound fadeout 1

    "И он демонстративно удалился, бросив кулёк с семечками у моих ног."
    "Я ждал невыносимо долго."



    scene bg school_day_animation
    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop

    window show
    play music "music/Kaite1.ogg" fadein 1
    "Самые длинные полтора часа жизни, словно миксер, размололи мой мозг до жидкой кашицы."
    "Одни тревожные мысли нахлёстывались на другие."

    show d4_road:
        alpha 0
        zoom 1.
        align (.5, 1.)
        parallel:
            linear 3 alpha 1
        parallel:
            linear 4 zoom .7
    with None
    show blizzard_d4_day_far onlayer master1 zorder 1:
        matrixcolor BrightnessMatrix(0.2)
    show blizzard_d4_day_near onlayer master1 zorder 5:
        matrixcolor BrightnessMatrix(0.2)
    with Dissolve(3.)
    "Пропавшая Катя."
    "Лес."
    "Маньяк."

    scene d4_polina_home_clouds:
        align (.5, .5)
        zoom 1.02
    show d4_polina_home_house:
        align (.5, .5)
        zoom 1.02
    show blizzard_d4_day_far:
        matrixcolor BrightnessMatrix(0.2)
    show blizzard_d4_day_near zorder 5:
        matrixcolor BrightnessMatrix(0.2)
    $ renpy.scene("master1")
    with Dissolve(1.)

    stop sound fadeout 1

    "И склепы, могилы, кресты..."

    $ renpy.music.set_pan(-0.5, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(-0.1, delay=2, channel="sound")
    stop music fadeout 2

    show Romka Normal m_day_winter 00 norm ahead 03 zorder 1:
        alpha 0
        xoffset -600
        yoffset 10
        xzoom -1
        parallel:
            linear 1 xoffset -400
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 1

    pause 1
    stop sound fadeout 1

    voice "voice/romka/4day/130 A.ogg"
    Rom "А Бяша где? Зассал поди?"
    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.35)
    "Необязательно было спрашивать Ромку о свидании. По улыбке до ушей становилось ясно, что прошло оно великолепно."
    show Romka Angry m_day_winter 01 happy ahead 05:
        align (.5, 1.)
        xoffset -400
        linear .2 xoffset -350 zoom 1.05
        linear .2 xoffset -400 zoom 1.00

    pause 0.2
    play sound "sounds/sfx_punch_side.ogg" volume 0.35
    with hpunch
    "Ромка шутливо боднул меня в бок."
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.15)
    voice "voice/romka/4day/131 Nu.ogg"
    Rom "Ну ходу, кент!"
    stop music2 fadeout 12

    play sound "sounds/loop_footsteps_two.ogg" fadein 1.2 loop

    show Romka Angry m_day_winter 01 happy ahead 05:
        xoffset -400
        alpha 1
        parallel:
            linear 1 xoffset -200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 0

    show d4_road behind blizzard_d4_day_far:
        alpha 0
        zoom 1.
        align (.0, 1.)
        parallel:
            linear 1 alpha 1


        parallel:
            linear 8 xalign 1.

    window hide
    pause 1
    window show

    play test_one "sounds/loop_well_handle_squeak.ogg" fadein 2 loop volume 0.17
    "В это время люди в домах стряпали, смотрели телевизор, переругивались."
    play music "music/39_Dvar - Oramah Elahar.ogg" fadein 3
    "На крыльце курили хмурые мужчины. Скрипел колодезный ворот."
    "Метель обошла посёлок по дуге."

    stop test_one fadeout 2

    scene bg_white with Dissolve(0.3)
    $ SetParSpeed(30)
    show d4_forest_walk_day_1_0
    show d4_forest_walk_day_1_1
    show d4_forest_walk_day_2_0
    show d4_forest_walk_day_2_1
    show d4_forest_walk_day_3_0
    show d4_forest_walk_day_3_1
    show blizzard_d4_day_far:
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 0
            linear 30 xpan 360
            repeat
    show d4_forest_walk_day_4_0
    show d4_forest_walk_day_4_1

    show blizzard_d4_day_near zorder 5:
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 0
            linear 30 xpan 360
            repeat
    with Dissolve(0.5)
    "Но не она заботила меня и пугала."
    "Лес вырос на нашем пути, и то ли мы вошли в него, то ли он проглотил нас зубастой пастью."
    "Сосны скрипели, а из тайги тянулись зыбкие тени."
    "Они выгибались по обе стороны от дороги."
    "Никто из нас не проронил ни слова, ступая на просеку."
    "Сизая дымка струилась над оврагами, её хвосты завивались в призрачном танце."
    "В лесу тошнотворно пахло воском церковных свечей, мутило рассудок."
    "Снег чавкал, проседая под подошвами."
    "Кочки напоминали насыпи на могилах, а кресты заменяли перекрученные хилые деревья." id d4_byash_choice_dismiss_e8613c9a
    "Из заледеневших болот стенала и булькала тьма. Злобно завыл ветер."
    "Время перестало иметь значение."

    $ story_manager.MarkEvent(("day4", "scene_v5"))

    scene dark_forest_day3_1:
        subpixel True
        zoom 0.5
    show blizzard_d4_evening_far:
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    show blizzard_d4_evening_near zorder 5:
        block:
            ypan 0
            linear 20 ypan -360
            repeat
    with Dissolve(1.)
    stop sound fadeout 1

    play test_seven "sounds/fon/owls-1.ogg" fadein 2 loop

    "В какой-то момент мы упёрлись в бурелом."

    show Romka Normal m_day_winter 00 norm ahead 03 zorder 1 with Dissolve(.5):
        xoffset -100
        yoffset 20

    show bg_black behind Romka:
        alpha 0
        linear 2 alpha .05
    voice "voice/romka/4day/132 Z.ogg"
    Rom "Значит, так..."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/133 P.ogg"
    Rom "Поисковая операция начинается."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/134 D.ogg"
    Rom "Далеко не разбредаемся, ищем любые следы Кати или похитителя."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/135 E.ogg"
    Rom "И желательно, Тоха, поживее."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/136 U.ogg"
    Rom "Уже через час станет темно хоть глаз выколи."
    stop test_seven fadeout 5.5
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)

    play test_three "sounds/loop_footsteps_two.ogg" fadein 0.8 loop



    scene bg_black with Dissolve(.5)

    scene d4_gorelnik_bg:
        xalign 0.
        linear 12 xalign 1.

    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5

    show d4_gorelnik_fg zorder 1:
        xpos 1260
        ypos 1080
        anchor (.0, 1.)
        linear 12 xpos -350

    with Dissolve(.5)

    stop test_seven fadeout 4
    stop music fadeout 3
    "Наши поиски не дали никаких результатов. Проклятый лес умел хоронить секреты."

    stop test_three fadeout 1
    play sound "sounds/sfx_branch_crows.ogg"

    scene d4_gorelnik_bg:
        xalign 1.
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gorelnik_fg:
        xpos -350
        ypos 1080
        anchor (.0, 1.)
    with Dissolve(.25)
    play test_one "sounds/hit-chord-3.ogg"
    "Мы уже собирались идти домой, как хрустнула ветка в овраге позади нас, и в небо взметнулась стая испуганных ворон."


    play test_three "sounds/sfx_butterfly_knife_open_fast.ogg" noloop

    scene bad_mask_bg
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_rom_knife
    show bg_black as dark:
        alpha .5
    with Dissolve(.25)
    "Ромка с завидной проворностью выхватил нож, ткнул им в подступающую темноту."

    scene d4_gorelnik_bg:
        xalign 1.
    show blizzard_d4_evening2_far zorder 1
    show blizzard_d4_evening2_near zorder 1
    show blizzard_d4_evening2_big zorder 5
    show d4_gorelnik_fg zorder 2:
        xpos -350
        ypos 1080
        anchor (.0, 1.)
    with Dissolve(.25)
    voice "voice/romka/4day/138 S.ogg"
    Rom "Слышал? Там кто-то бродит."
    voice "voice/romka/4day/139 V.ogg"
    Rom "Возможно, наш маньяк."

    play music "music/43_Kontakt.ogg"
    show d4_gor_tih 0 with Dissolve(.5)
    "Словно сама ночь услышала его слова, соткав из сумрака и копоти высокий грозный силуэт."

    play test_three "sounds/loop_footsteps_snow_heavy_distant_slow.ogg" fadein 7 volume 0.6 loop

    "Существо некоторое время возвышалось над тающими во мгле пнями и корягами, а потом быстро зашагало к нам."
    show d4_gor_tih 1 with Dissolve(.5)
    play test_four "sounds/loop_branches_cracking.ogg" fadein 8 loop

    "Это явно был не призрак — приближающийся треск сучьев говорил, что оно материально."

    scene d4_gor_fon3
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gor_rom 2:
        xoffset 25
    show d4_gor_ant 2:
        xoffset -300
    with Dissolve(.5)
    voice "voice/anton/4day/74. Cht.ogg"
    Ant "Что дальше, Ром?"

    show d4_gor_rom 5 with Dissolve(.2)
    voice "voice/romka/4day/140 A.ogg"
    Rom "А я почём знаю? Ты же хотел его выцепить!"

    stop test_three fadeout 3
    play test_five "sounds/loop_footsteps_snow_heavy_distant_run.ogg" volume 0.95 fadein 20 loop

    scene d4_gorelnik_bg:
        xalign 1.
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 1
    show blizzard_d4_evening2_big zorder 5
    show d4_gorelnik_fg zorder 2:
        xpos -350
        ypos 1080
        anchor (.0, 1.)
    show d4_gor_tih 2
    with Dissolve(.5)
    "Нечто уже бежало в нашу сторону, лихо перепрыгивая поваленное дерево."

    scene d4_gor_fon3
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gor_rom:
        xoffset 25
    show d4_gor_ant:
        xoffset -300
    with Dissolve(.5)

    pause .2

    show d4_gor_rom 1
    show d4_gor_ant 3
    with Dissolve(.5)

    voice "voice/romka/4day/141 N.ogg"
    Rom "Не стой столбом – хватай дрын какой-нибудь!"
    show d4_gor_rom with Dissolve(.2)

    show d4_gor_ant 2
    show d4_gor_ant_3:
        align (.5, 1.)
        yoffset 200
        alpha 0
        parallel:
            linear .5 yoffset 10
            block:
                linear .05 yoffset 6
                linear .05 yoffset 10
                repeat 6
            2.55
            repeat

        parallel:
            linear .25 alpha 1
    with Dissolve(.5)

    play sound "sounds/sfx_branch_grab.ogg"
    $ add_text_to_dictionary(39)
    "Я с трудом выкорчевал из земли палку размером с биту для {u}лапты{/u}. Вымазанные в саже руки тряслись."
    show d4_gor_rom 1 with Dissolve(.2)
    voice "voice/romka/4day/142 Ne.ogg"
    Rom "Не ссы, я уже махался со взрослыми."
    show d4_gor_rom with Dissolve(.2)
    show d4_gor_rom 2 with Dissolve(.2)
    voice "voice/romka/4day/143 G.ogg"
    Rom "Главное..."
    show d4_gor_rom 4 with Dissolve(.2)
    stop test_five fadeout 5
    "Ромка пытался храбриться, но голос его дрожал."
    show d4_gor_rom with Dissolve(.2)
    show d4_gor_rom 1 with Dissolve(.2)
    voice "voice/romka/4day/144 Ne.ogg"
    Rom "Не вздумай меня тут кинуть одного! Ясно?!"
    show d4_gor_rom with Dissolve(.2)
    "Я молча кивнул и увидел, как запыхавшийся мужчина выхватывает что-то из-за пазухи."

    show d4_gor_rom 2 with Dissolve(.2):
        .2
        "d4_gor_rom 2" with Dissolve(.2)
        .2
        "d4_gor_rom 3" with Dissolve(.2)
        .2
        "d4_gor_rom wtf" with Dissolve(.2)


    "Мой боевой товарищ яростно закричал и бросился в атаку."
    play test_six "sounds/loop_footsteps_snow_two_run.ogg" fadein 1 loop

    show d4_gor_rom wtf2 with Dissolve(.2):
        align (.5, 1.)
        "d4_gor_rom wtf3" with Dissolve(.2)
        .1
        block:
            linear .03 xoffset 22
            linear .03 xoffset 28
            repeat 5
        linear .03 xoffset 25
        .3
        parallel:
            easein .5 xoffset 325
        parallel:
            .25
            linear .25 alpha 0
    voice "voice/romka/4day/145 A.ogg"
    Rom "А-а-а-а-а-а-а!" id d4_byash_choice_dismiss_dd364f5a

    play wtf "voice/anton/2day/Vshlip.ogg"
    show d4_gor_ant wtf with Dissolve(.2)
    "Я последовал за ним, крича скорее от ужаса."

    show d4_gor_ant wtf:
        align (.5, 1.)
        parallel:
            linear .5 xoffset 100
        parallel:
            .25
            linear .25 alpha 0
    show d4_gor_ant_3:
        align (.5, 1.)
        parallel:
            linear .5 xoffset 300
        parallel:
            .25
            linear .25 alpha 0
    voice "voice/anton/4day/75. AAA.ogg"
    Ant "А-а-а-а-а-а-а!" id d4_byash_choice_dismiss_655f972b

    stop test_four fadeout 0.8
    stop test_six fadeout 1.2
    stop test_five fadeout 1

    scene d4_gor_bg
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gor_hnd:
        block:
            linear .5 xoffset -5 yoffset 0
            linear .5 xoffset 0 yoffset -5
            linear .5 xoffset -5 yoffset 5
            linear .5 xoffset 5 yoffset 5
            linear .5 xoffset 0 yoffset 0
            repeat
    show d4_gor_drin:
        linear 12 yoffset 1000
    with Dissolve(.5)

    play sound "sounds/sfx_branch_drop_snow.ogg"
    play test_six "music/finger(Riser).ogg"
    "И тут мы оба встали, как вкопанные. Импровизированная дубина выпала из моих рук."

    scene d4_gorelnik_bg:
        xalign 1.
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gorelnik_fg zorder 1:
        xpos -350
        ypos 1080
        anchor (.0, 1.)
    show d4_gor_tih 3:
        align (.5, 1.)
        zoom .85
    with Dissolve(.5)
    play test_three "voice/anton/4day/71.Eh.ogg"
    "В нашу сторону смотрело нарезное дуло пистолета Макарова, вынуждая нас в страхе попятиться."
    voice "voice/tihonov/4day/01 P.ogg"
    Noname "Пятифанов! А ну брось нож! Чтоб вас!"
    stop music fadeout 2

    play sound "sounds/sfx_footstep_snow_step_down.ogg"

    show d4_gor_tih 3:
        parallel:
            easein .5 zoom 1.02
            ease .2 zoom 1.0
        parallel:
            "d4_gor_tih 4" with ImageDissolve("effect/imagedissolve/shadow/02.jpg", .5, ramplen=128)

    play test_two "sounds/Fail9.ogg"
    "Неизвестный вышел на лунный свет, и только сейчас я узнал старлея Тихонова."

    hide d4_gor_tih
    show d4_gor_tih 4
    with Dissolve(.15)

    show d4_gor_tih 5 with Dissolve(.5)
    show d4_gor_tih 6 as tih_face with Dissolve(.5)
    play test_one "sounds/Fail4.ogg" volume 0.6
    "Он хмуро оглядел нас, затем смачно харкнул в сторону."

    play sound "sounds/sfx_coat_rustle.ogg"

    show d4_gor_tih 7
    hide tih_face
    show d4_gor_tih_rot
    with Dissolve(.5)
    voice "voice/tihonov/4day/02 T.ogg"
    Tikhonov "Тьфу! Провалиться мне на месте."
    hide d4_gor_tih_rot with Dissolve(.25)

    show d4_gor_tih_rot with Dissolve(.25)
    play test_one "sounds/Fail1.ogg" volume 0.5
    voice "voice/tihonov/4day/03 To.ogg"
    Tikhonov "Только вас двоих мне здесь и не хватало."
    hide d4_gor_tih_rot with Dissolve(.25)

    scene d4_gor_fon3
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gor_rom 6:
        xoffset 25
    show d4_gor_ant:
        xoffset -300
    with Dissolve(.5)
    "Ромка злобно ухмыльнулся."

    show d4_gor_rom 8 with Dissolve(.2)
    play test_one "sounds/Fail3.ogg" volume 0.5
    voice "voice/romka/4day/146 T.ogg"
    Rom "Так я и думал, что это ты, легавый, тот самый маньячелло."
    show d4_gor_rom 6 with Dissolve(.2)

    show d4_gor_ant 1:
        linear .03 xoffset -3-300 yoffset 3
        linear .03 xoffset 0-300 yoffset 0
        repeat
    show d4_gor_rom 7
    with Dissolve(.2)
    voice "voice/anton/4day/76.Po.ogg"
    Ant "Пожалуйста, отпустите! Мы ничего не скажем!"

    show d4_gor_ant 3:
        xoffset -300
    show d4_gor_rom 6
    with Dissolve(.2)
    voice "voice/tihonov/4day/05 Da.ogg"
    Tikhonov "Да заткнитесь вы оба!"

    scene d4_gorelnik_bg:
        xalign 1.
        yalign 1.
        zoom 1.1
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show d4_gorelnik_fg_1 zorder 1:
        align (.5, 1.)
        xoffset -800
    show d4_gorelnik_fg_2 zorder 1:
        align (.5, 1.)
        xoffset 800
    show d4_gor_tih 9:
        xalign .5
        block:
            1.
            block:
                linear .03 xoffset 5 yoffset 5
                linear .03 xoffset -5 yoffset -5
                repeat 12
            linear .05 xoffset 0 yoffset 0
            repeat
    with Dissolve(.5)

    play test_one "sounds/Fail2.ogg" volume 0.5
    voice "voice/tihonov/4day/06 Ya.ogg"
    Tikhonov "Я вшивых четыре часа на морозе провёл, а вы мне всю засаду испортили, паразиты."

    play test_three "voice/anton/3day/16 Vzd.ogg"
    "Мы отуплено опустили руки."
    play test_six "music/Fail7.ogg"

    voice "voice/tihonov/4day/07 P.ogg"
    Tikhonov "Полезай-ка в бобик."

    stop test_seven fadeout 3
    play sound "sounds/sfx_car_door_ignition_leave.ogg"

    show bg_black zorder 2:
        alpha 0
        linear .5 alpha 1
    voice "voice/tihonov/4day/08 V.ogg"
    Tikhonov "В участке расскажете, что вы тут забыли."

    window hide

    pause 4
    stop fon fadeout 5

    play test_one "sounds/sfx_car_stop_door.ogg"



    call d4_police_entry from _call_d4_police_entry

    jump d4_police_forced



label d4_byash_choice_call:
    $ story_manager.MarkEvent(("day4", "byasha", "call"))
    show blizzard_d4_day_near zorder 5:
        alpha 1
    hide blizzard_d4_day2_near onlayer screens
    with Dissolve(.5)
    $ renpy.stop_predict("d4_byasha_call_img_hover")

    show Byasha Doubt b_day_winter 01 normal aside 01:
        .2
        "Byasha Doubt b_day_winter 01 normal ahead 01" with Dissolve(.5)
    stop music fadeout 1.5
    play music2 "music/Lucky.ogg" volume 0.8 fadein 2
    voice "voice/anton/4day/63. Nu.ogg"
    Ant "Ну Бяш, не обижайся..."
    voice "voice/anton/4day/64. Ro.ogg"
    Ant "Ромка голову совсем потерял, ты уж не злись на него сильно."
    voice "voice/anton/4day/65. A.ogg"
    Ant "А про тебя я помню. Вот, держи от меня подарок."

    play sound "sounds/sfx_drawing_Voltron_1.ogg"

    show d4_voltron_art zorder 2:
        ypos 200
        xpos 200
        alpha 0
        subpixel True
        parallel:
            linear .5 ypos 5 alpha 1
        parallel:
            animation
            linear 1.5 xoffset -5 yoffset 0
            linear 1.5 xoffset 0 yoffset -5
            linear 1.5 xoffset -5 yoffset 5
            linear 1.5 xoffset 5 yoffset 0
            repeat

    "Я передал Бяше доработанный набросок Вольтрона — огромного трансформера, собранного из пятёрки роботов-львов."

    play sound "sounds/sfx_drawing_Voltron_2.ogg"

    show Byasha Normal b_day_winter 01 normal ahead 07 with Dissolve(.25)
    pause .25
    show d4_voltron_art:
        subpixel True
        parallel:
            animation
            linear 1.5 xoffset -5 yoffset 0
            linear 1.5 xoffset 0 yoffset -5
            linear 1.5 xoffset -5 yoffset 5
            linear 1.5 xoffset 5 yoffset 0
            repeat
        parallel:
            "d4_voltron_empty" with Dissolve(.5)
            1.
            linear .5 ypos 200 alpha 0

    pause .25

    show Byasha Normal b_day_winter 01 normal ahead 08 with Dissolve(.15)
    voice "voice/byasha/4day/186 Ni.ogg"
    Bya "Ничёсе! Это мне, на?"
    show Byasha Normal b_day_winter 01 normal ahead 07 with Dissolve(.15)
    show Byasha Normal b_day_winter 01 normal ahead 08 with Dissolve(.15)
    voice "voice/byasha/4day/187 Sp.ogg"
    Bya "Спасибо, Антоха, уважил!"
    show Byasha Normal b_day_winter 01 normal ahead 07 with Dissolve(.15)
    voice "voice/anton/4day/66. Ch.ogg"
    Ant "Да чего уж там."
    voice "voice/anton/4day/67. Che.ogg"
    Ant "Через полтора часа встречаемся у Полининого дома."
    voice "voice/anton/4day/68.Na .ogg"
    Ant "Намечается срочное дело."
    "Бяша аж порозовел на радостях."
    show Byasha Normal b_day_winter 01 normal ahead 08 with Dissolve(.15)
    voice "voice/byasha/4day/188 Ch.ogg"
    Bya "Чем будем заниматься?"
    show Byasha Normal b_day_winter 01 normal ahead 07 with Dissolve(.15)
    "Я грустно улыбнулся, оценивая наши шансы."
    stop music2 fadeout 5
    voice "voice/anton/4day/69. Po.ogg"
    Ant "Постараемся не пропасть без вести."

    window hide
    hide Byasha

    play sound "sounds/sfx_coat_rustle_2.ogg"

    show d4_byasha_doubt:
        xoffset -400
        yoffset 10
    with Dissolve(.5)

    pause .25

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(-0.5, delay=2, channel="sound")

    show d4_byasha_doubt:
        xoffset -400
        yoffset 10
        parallel:
            linear 2. xoffset -750
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat
        parallel:
            1.
            linear 1. alpha 0
    with Dissolve(.15)


    $ achievement_grant("ach_musketeers")

    hide blizzard_d4_day_far
    hide blizzard_d4_day_near
    hide blizzard_d4_day2_near
    show blizzard_d4_day_far onlayer master1
    show blizzard_d4_day2_near onlayer master1
    with Dissolve(2.0)

    stop sound fadeout 1.2

    scene bg school_day_animation

    window show
    play music "music/Kaite1.ogg" fadein 1
    "Самые длинные полтора часа жизни, словно миксер, размололи мой мозг до жидкой кашицы."
    "Одни тревожные мысли нахлёстывались на другие."

    show d4_road:
        alpha 0
        zoom 1.
        align (.5, 1.)
        parallel:
            linear 3 alpha 1
        parallel:
            linear 4 zoom .7

    "Пропавшая Катя."
    "Лес."
    "Маньяк."

    scene d4_polina_home_clouds:
        align (.5, .5)
        zoom 1.02
    show d4_polina_home_house:
        align (.5, .5)
        zoom 1.02
    $ renpy.scene("master1")
    show blizzard_d4_day_far
    show blizzard_d4_day2_near zorder 5

    with Dissolve(1.)

    "И склепы, могилы, кресты..."

    $ renpy.music.set_pan(0.4, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(0.1, delay=2, channel="sound")

    show Byasha Normal m_day_winter 01 normal aside 03:
        alpha 0
        xoffset 600
        yoffset 10
        parallel:
            linear 1 xoffset 400
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 1

    $ renpy.pause(1.2)
    stop sound fadeout 1

    "Бяша выполз из ранних сумерек в квартале от назначенного места."
    stop music fadeout 2

    play music2 "music/Byasha.ogg" volume 0.8 fadein 3
    show Byasha Normal m_day_winter 01 normal ahead 04
    voice "voice/byasha/4day/189 Ch.ogg"
    Bya "Чего унылый такой, на? Свежих анекдотов нет?"
    show Byasha Normal m_day_winter 01 normal ahead 03
    "Я был рад видеть даже его физиономию."

    $ renpy.music.set_pan(-0.5, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop
    $ renpy.music.set_pan(-0.1, delay=2, channel="sound")

    show Romka Normal m_day_winter 00 norm ahead 01:
        alpha 0
        xoffset -600
        yoffset 10
        xzoom -1
        parallel:
            linear 1 xoffset -400
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 1
    pause 1.

    show Byasha Normal m_day_winter 01 normal ahead 03:
        yoffset 10
        xoffset 400
        alpha 1
    show Romka Normal m_day_winter 00 norm ahead 03:
        yoffset 10
        xoffset -400
        alpha 1

    stop sound fadeout 1

    voice "voice/romka/4day/157 V.ogg"
    Rom "Вся банда в сборе?"
    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.35)
    "Необязательно было спрашивать Ромку о свидании. По улыбке до ушей становилось ясно, что прошло оно великолепно."
    show Romka Angry m_day_winter 01 happy ahead 05:
        align (.5, 1.)
        xoffset -400
        linear .2 xoffset -350 zoom 1.05
        linear .2 xoffset -400 zoom 1.00

    $ story_manager.MarkEvent(("day4", "scene_v6"))

    pause 0.2
    play sound "sounds/sfx_punch_side.ogg" volume 0.35
    with hpunch
    "Ромка шутливо боднул меня в бок."
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.15)
    voice "voice/romka/4day/158 N.ogg"
    Rom "Ну айда, джентльмены!"
    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.15)
    show Byasha Normal m_day_winter 01 normal aside 04 with Dissolve(.15):
        .5
        "Byasha Normal m_day_winter 01 normal ahead 04" with Dissolve(.15)
    voice "voice/byasha/4day/190 Eto.ogg"
    Bya "Этот – счастливый, тот – несчастный."
    show Byasha Normal m_day_winter 01 normal ahead 03 with Dissolve(.15)
    show Byasha Normal m_day_winter 01 normal ahead 04 with Dissolve(.15)
    voice "voice/byasha/4day/191Fig.ogg"
    Bya "Фиг вас поймёшь, на."
    show Byasha Normal m_day_winter 01 normal ahead 03 with Dissolve(.15)
    show Romka Angry m_day_winter 01 happy aside 06 with Dissolve(.25)
    voice "voice/romka/4day/159 A.ogg"
    Rom "А ты лишний раз, Бяш, не думай."
    show Romka Angry m_day_winter 01 happy aside 05 with Dissolve(.15)
    show Romka Angry m_day_winter 01 happy aside 06 with Dissolve(.15)
    voice "voice/romka/4day/160 At.ogg"
    Rom "А то, глядишь, последняя извилина узлом закрутится."
    stop music2 fadeout 12

    play sound "sounds/loop_footsteps_three.ogg" fadein 1.2 loop

    show Romka Angry m_day_winter 01 happy ahead 05:
        xoffset -400
        alpha 1
        parallel:
            linear 1 xoffset -200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 0
    show Byasha Normal m_day_winter 01 normal ahead 03:
        xoffset 400
        alpha 1
        .1
        xzoom -1
        parallel:
            linear 1 xoffset 600
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1 alpha 0

    show d4_road behind blizzard_d4_day_far:
        alpha 0
        zoom 1.
        align (.0, 1.)
        parallel:
            linear 1 alpha 1


        parallel:
            linear 8 xalign 1.

    window hide
    pause 1
    window show

    play test_one "sounds/loop_well_handle_squeak.ogg" fadein 2 loop volume 0.17

    "В это время люди в домах стряпали, смотрели телевизор, переругивались."
    play music "music/39_Dvar - Oramah Elahar.ogg" fadein 3
    "На крыльце курили хмурые мужчины. Скрипел колодезный ворот."
    "Метель обошла посёлок по дуге."

    stop test_one fadeout 6


    $ SetParSpeed(30)
    scene d4_forest_walk_day_1_0
    $ renpy.scene("master1")
    show d4_forest_walk_day_1_1
    show d4_forest_walk_day_2_0
    show d4_forest_walk_day_2_1
    show d4_forest_walk_day_3_0
    show d4_forest_walk_day_3_1
    show blizzard_d4_day_far:
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 0
            linear 30 xpan 360
            repeat
    show d4_forest_walk_day_4_0
    show d4_forest_walk_day_4_1

    show blizzard_d4_day_near zorder 5:
        matrixcolor BrightnessMatrix(0.2)
        block:
            xpan 0
            linear 30 xpan 360
            repeat
    with Dissolve(0.5)

    "Но не она заботила меня и пугала."
    "Лес вырос на нашем пути, и то ли мы вошли в него, то ли он проглотил нас зубастой пастью."
    "Сосны скрипели, а из тайги тянулись зыбкие тени."
    "Они выгибались по обе стороны от дороги."
    "Никто из нас не проронил ни слова, ступая на просеку."
    "Сизая дымка струилась над оврагами, её хвосты завивались в призрачном танце."
    "В лесу тошнотворно пахло воском церковных свечей, мутило рассудок."
    "Снег чавкал, проседая под подошвами."
    "Кочки напоминали насыпи на могилах, а кресты заменяли перекрученные хилые деревья." id d4_byash_choice_call_e8613c9a
    "Из заледеневших болот стенала и булькала тьма. Злобно завыл ветер."
    "Время перестало иметь значение."

    scene dark_forest_day3_1:
        subpixel True
        zoom 0.5
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 5
    show blizzard_d4_evening_face zorder 5
    with Dissolve(1.)
    stop sound fadeout 1

    play test_seven "sounds/fon/owls-1.ogg" fadein 2 loop

    "В какой-то момент мы упёрлись в бурелом."

    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.5):
        yoffset 20

    show bg_black behind Romka:
        alpha 0
        linear 2 alpha .05
    voice "voice/romka/4day/132 Z.ogg"
    Rom "Значит, так..."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/133 P.ogg"
    Rom "Поисковая операция начинается."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/134 D.ogg"
    Rom "Далеко не разбредаемся, ищем любые следы Кати или похитителя."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/164 E.ogg"
    Rom "И желательно, пацаны, поживее."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/136 U.ogg"
    Rom "Уже через час станет темно хоть глаз выколи."
    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.15)

    hide Romka with Dissolve(.5)

    play sound "sounds/loop_footsteps_two.ogg" fadein 1 loop

    "Мы осторожно стали пробираться через поваленные деревья в слабой надежде найти хоть что-то."


    scene d4_forest_1
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 5
    show blizzard_d4_evening_face zorder 5
    show Byasha Doubt m_day_winter 01 normal ahead 02:
        yoffset 10
    with Dissolve(.5)

    stop sound fadeout 1.2

    voice "voice/byasha/4day/192 Hr.ogg"
    Bya "Хрена лысого мы в таких потёмках найдем, на."

    scene d4_forest_purse_on_snow:
        yalign 1.
        linear 6. yalign 0.
    show incar_snow_up onlayer master1:
        matrixcolor BrightnessMatrix(.2)
    with Dissolve(.5)

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop

    voice "voice/byasha/4day/193 Da.ogg"
    Bya "Давайте уж лучше по домам."
    stop music fadeout 3

    show d4_forest_purse_on_snow:
        linear .5 yalign 0.0

    stop sound fadeout 1.5
    play test_five "music/caricature11.ogg"
    voice "voice/byasha/4day/194 Opa.ogg"
    Bya "Опачки! Чё тут у нас?"



    voice "voice/byasha/4day/195 A.ogg"
    Bya "А мне сегодня фартит!"
    play sound ["sounds/sfx_snow_hand.ogg","sounds/sfx_purse_take.ogg"]


    scene d4_forest_snow:
        align (0, 0)
    with Dissolve(.5)

    show d4_forest_purse_in_hand:
        ypos 200
        xpos 200
        alpha 0
        subpixel True
        parallel:
            linear .5 ypos 5 alpha 1
        parallel:
            animation
            linear 1.5 xoffset -5 yoffset 0
            linear 1.5 xoffset 0 yoffset -5
            linear 1.5 xoffset -5 yoffset 5
            linear 1.5 xoffset 5 yoffset 0
            repeat


    play test_two "sounds/Victory2.ogg"
    voice "voice/byasha/4day/196 Br.ogg"
    Bya "Братва! Я, кажись, нашёл."

    voice "voice/byasha/4day/197 Eto.ogg"
    Bya "Это ж Катькин кошелёк!{w=2.}{nw}"
    stop test_seven fadeout 0.5
    play test_five "music/Phrases_03.ogg"
    show kk_shadow behind d4_forest_purse_in_hand:
        align (.5, .5)
        transform_anchor True
        subpixel True
        rotate -90
        zoom 4.
        xoffset 800
        yoffset -400
        linear .25 xoffset 0 yoffset 0

    call screen forced_timer(.25)

    play sound "sounds/sfx_branch_crows.ogg"
    hide incar_snow_up onlayer master1
    scene dark_forest_day3_1:
        subpixel True
        zoom 0.5
        matrixcolor BrightnessMatrix(-.10)
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show Romka Normal m_night_winter 00 norm aside 01:
        align (.5, 1.)
        xoffset 50
        yoffset 50
        matrixcolor BrightnessMatrix(-.05)
    show d4_anton_back:
        align (.5, 1.)
        zoom 1.10
        xoffset -400
        yoffset 100
        matrixcolor BrightnessMatrix(-.05)

    pause .15

    show Romka Normal m_night_winter 00 norm ahead 01 with Dissolve(.25)

    pause .25

    show Romka Worry m_night_winter 01 worry ahead 02 with Dissolve(.25)

    pause .25

    hide d4_anton_back
    show d4_anton_shock:
        align (.5, 1.)
        zoom .95
        xoffset -250
        matrixcolor BrightnessMatrix(-.05)
    with Dissolve(.25)


    play test_six "voice/anton/4day/Ah.ogg"
    play test_two "voice/byasha/4day/198 AAA.ogg"
    "А потом я услышал сдавленный вскрик и не понял, кто кричал: Ромка, Бяша или я сам."
    play test_three "voice/anton/1day/Ah.ogg"
    "Наконец, я всё увидел воочию и всё равно не поверил своим глазам."
    play music2 "music/Evil Alice.ogg" fadein 1

    scene d4_forest_1 dark2
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show Byasha Scared b_night_winter 02 shock aside 02 drop:
        xoffset 200
        yoffset 10
        matrixcolor BrightnessMatrix(-.05)
        block:
            linear .05 yoffset 6
            linear .05 yoffset 10
            repeat 6

        2.55
        repeat

    with Dissolve(.5)

    play sound "sounds/sfx_Byashya_fall_snow.ogg" fadein 0.3 volume 0.7

    stop test_two fadeout 0.5
    play test_six "voice/byasha/4day/199 ee.ogg"
    "Абсолютно седой Бяша в ужасе пятился, спотыкаясь, пока, наконец, не рухнул в сугроб."
    play test_six "voice/byasha/4day/199 mm.ogg"
    "Он протянул руку, и я увидел, как дрожат его пальцы, указывающие в пустоту."
    stop test_six fadeout 0.5
    voice "voice/byasha/4day/199 Be.ogg"
    Bya "Бе... Бе-бе..."

    scene d4_forest_1 dark2:
        align (.5, .5)
        zoom 1.0
        linear .15 zoom 1.2
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show Byasha Scared b_night_winter 02 shock ahead 02 drop:
        xoffset 200
        yoffset 10
        matrixcolor BrightnessMatrix(-.05)
        align (.5, .5)
        zoom 1.0
        parallel:
            block:
                linear .05 yoffset 6
                linear .05 yoffset 10
                repeat 6
            2.55
            repeat

        parallel:
            linear .15 zoom 1.3

    voice "voice/byasha/4day/199 Beee.ogg"
    Bya "Бе-е-е-е-е-е-е!"

    play sound "sounds/sfx_snow_footsteps_away.ogg"
    $ renpy.music.set_pan(-0.5, delay=3, channel="sound")

    show Byasha Scared b_night_winter 02 shock ahead 02:
        xoffset 200
        yoffset 10
        matrixcolor BrightnessMatrix(-.05)
        align (.5, .5)
        zoom 1.3
        parallel:
            linear .1 yoffset 0
            linear .1 yoffset 30
            repeat
        parallel:
            linear 1. xoffset -1920


    "Бяша взвился, словно ужаленный, и побежал прочь."
    "Ромка не посмотрел на него."

    scene dark_forest:
        align (.5, .40)
        subpixel True
        matrixcolor BrightnessMatrix(-.15)
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show Romka Worry m_night_winter 01 worry ahead 02:
        align (.5, 1.)
        xoffset 50
        yoffset 50
        matrixcolor BrightnessMatrix(-.10)
    show d4_anton_shock:
        align (.5, 1.)
        zoom 1.10
        xoffset -400
        yoffset 100
        matrixcolor BrightnessMatrix(-.10)

    with Dissolve(.5)

    "Он продолжал глядеть вперёд. Не моргая. Не дыша."

    $ renpy.music.set_pan(0, delay=0, channel="sound")


    "Я не заметил, как зашагал навстречу чему-то неописуемо страшному."
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop

    scene dark_forest:
        align (.5, .40)
        subpixel True
        matrixcolor BrightnessMatrix(-.15)
        linear 24 xalign 1.
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show Romka Worry m_night_winter 01 worry ahead 02:
        xoffset 50
        yoffset 50
        matrixcolor BrightnessMatrix(-.10)
        xpos 960
        ypos 1080
        anchor (.5, 1.)
        linear 24 xpos -100

    show d4_anton_shock:
        zoom 1.10
        xoffset -400
        yoffset 100
        matrixcolor BrightnessMatrix(-.10)
        xpos 960
        ypos 1080
        anchor (.5, 1.)
        linear 24 xpos -100

    show d4_gorelnik_wide:
        xalign 0.
        alpha 0
        .5
        parallel:
            linear 12 xalign 1.
        parallel:
            linear 1.5 alpha 1

    show d4_gorelnik_fg zorder 1:
        alpha 0
        xpos 1260
        ypos 1080
        anchor (.0, 1.)
        .5
        parallel:
            linear 12 xpos -350
        parallel:
            linear 1.5 alpha 1


    play test_one "sounds/sfx_branch_rustle.ogg"

    "Нерешительно отодвинул завесу из мохнатой хвои."
    "За елями показалась небольшая опушка, некогда выжженная точным попаданием молнии."
    "Почерневшие пни ограждали круг."
    stop sound fadeout 2

    window show
    scene d4_gorelnik_wide_blink:
        xalign 1.
    show blizzard_d4_evening2_far onlayer master1
    show blizzard_d4_evening2_near onlayer master1
    show blizzard_d4_evening2_big onlayer master1
    show d4_gorelnik_fg zorder 1:
        xpos -350
    with Dissolve(.5)

    "Посередине стоял Чёрный гараж."
    "Его гладкие стены были выкрашены чёрной краской."
    "Казалось, они впитали в себя сам мрак."
    "Я подумал, что Гараж – это не просто металлический короб, который легко можно перевозить с места на место."
    "Он нечто живое."
    window hide
    pause .5
    play sound "sounds/loop_footsteps_two.ogg" fadein 1 loop

    scene d4_gorelnik_slim:
        align (.5, .5)
        zoom 1
        linear 4. zoom 1.2
    show d4_gorelnik_fg_slim zorder 1:
        align (.5, .5)
        zoom 1
        linear 4. zoom 1.4

    pause 2.

    stop test_seven fadeout 6
    play test_one "sounds/loop_lamp_blinking.ogg" fadein 1 loop volume 0.55

    $ renpy.scene("master1")
    scene garage_near_blinking_noblur:
        align (.5, .5)
        zoom 1
        linear 1. zoom 1.05
    show garage_smoke_1 onlayer master1 zorder 1:
        xanchor 0.0
    show garage_smoke_2 onlayer master1 zorder 1:
        xanchor 0.0

    show blizzard_d4_evening2_near onlayer master1
    show blizzard_d4_evening2_big onlayer master1
    with Dissolve(1.)

    window show
    stop sound fadeout 1
    play test_three "sounds/loop_Black_garage_generator_outside.ogg" volume 1.5 fadein 1 loop

    $ story_manager.MarkEvent(("day4", "scene_v7"))

    "Насекомое с чёрным лоснящимся хитином. Прожорливый падальщик."
    "Мы таращились на него, а он внимательно следил за нами красным мерцающим глазом."
    "Я сказал себе, что это просто лампочка."
    scene garage_near_blinking_noblur:
        align (.5, .5)
        zoom 1.05
        linear 1. zoom 1.1

    pause .5

    scene garage_near_blinking_1_noblur:
        align (.5, .5)
        linear .5 zoom 1.05

    hide blizzard_d4_evening2_near onlayer master1



    with Dissolve(.5)
    stop music2 fadeout 3.5
    "Генератор жужжал тихонько, но в этом звуке слышалась угроза."

    play sound "sounds/sfx_Black_garage_open_1.ogg"

    window hide
    scene d4_garage_knok_open_animation
    pause 2.5

    scene garage_opened
    hide blizzard_d4_evening2_big onlayer master1
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5:
        matrixcolor BrightnessMatrix(.1)
    show Romka Normal m_night_winter 00 what ahead 02:
        xoffset 400
        yoffset 75
    show garage_over_blink zorder 10
    with Dissolve(.5)

    window show

    play music "music/Garazh_part1.ogg" fadein 1
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15):
        yoffset 75
    voice "voice/romka/4day/166 ot.ogg"
    Rom "Открыто."

    play sound "sounds/sfx_gulp.ogg"

    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    "Я попытался сглотнуть. Рот был сухой, как пустыня."
    "Ворота гаража были распахнуты. Внутри клубилась чернота."

    play sound "sounds/sfx_hand_pat_shoulder.ogg"

    "Я почувствовал прикосновение – Ромка положил ладонь на моё плечо."
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    $ music_during_lines = 0.75
    voice "voice/romka/4day/167 po.ogg"
    Rom "Пойдём?"
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    "Он выглядел сейчас старше своих лет. Да что там — он выглядел дряхлым стариком."
    voice "voice/anton/4day/Kuda.ogg"
    Ant "Куда? Ты что, сбрендил?!"
    voice "voice/anton/4day/Davai.ogg"
    Ant "Давай предупредим лейтенанта Тихонова."
    show Romka Normal m_night_winter 00 what aside 02 with Dissolve(.15)
    play test_six "voice/romka/4day/168 p.ogg"
    "Ромка сплюнул себе под ноги."
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/169 Ne.ogg"
    Rom "Не будь ты таким наивным, Тоха."
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/170 T.ogg"
    Rom "Твой Тихонов, вон, даже варежку в лесу отыскать не смог, ха-ха."
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/171Da.ogg"
    Rom "Да и западло с ментом сотрудничать, особенно когда я у него на учёте состою..."
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)

    scene bad_mask_bg

    play sound "sounds/sfx_butterfly_knife_open_fast.ogg"

    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5

    show d4_rom_knife
    show bg_black as dark:
        alpha .5
    show garage_over_blink zorder 10
    with Dissolve(.5)
    "Хулиган выхватил визитный ножик и серьёзно посмотрел на меня."
    voice "voice/romka/4day/172 m.ogg"
    Rom "Маньяк наверняка вернулся туда, в своё логово."
    voice "voice/romka/4day/173 E.ogg"
    Rom "Если получится — возьмём его тёпленьким, пока он не ждёт."
    voice "voice/romka/4day/174 En.ogg"
    Rom "Иначе в следующий раз подкараулит уже он."

    scene garage_opened
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big zorder 5
    show Romka Normal m_night_winter 00 what ahead 02:
        xoffset 400
        yoffset 75
    show garage_over_blink zorder 10
    with Dissolve(.5)
    "Зверята говорили, что он всего лишь человек из посёлка..."
    "Но справимся ли мы без взрослых?"
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/175 V.ogg"
    Rom "Второго шанса может не быть, брат."
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)
    show Romka Normal m_night_winter 00 what ahead 03 with Dissolve(.15)
    voice "voice/romka/4day/176 T.ogg"
    Rom "Так что решайся!"
    $ music_during_lines = 1.0
    show Romka Normal m_night_winter 00 what ahead 02 with Dissolve(.15)

    label d4_byash_choice_call.choice:

    $ story_manager.MarkEvent(("day4", "garage"))

    window hide
    scene d4_choice_bg_blink
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big
    with Dissolve(.5)

    call screen day4_garage_enter_or_police()


label d4_garage_choice_police:
    $ story_manager.MarkEvent(("day4", "garage", "police"))

    play sound "sounds/sfx_laughter_creepy_door_squeak.ogg"

    "Со стороны гаража раздался хриплый смех, от которого волосы на голове тут же встали дыбом."
    scene d4_gar_bg
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5:
        matrixcolor BrightnessMatrix(.15)
    show blizzard_d4_evening2_big zorder 5:
        matrixcolor BrightnessMatrix(.15)
    show d4_gar_Ant:
        yoffset 10
        xoffset -200
    with Dissolve(.5)

    "Но это всего лишь скрипела массивная чёрная дверь на холодном ветру."
    voice "voice/anton/4day/Eto.ogg"
    Ant "Это точно какая-то ловушка."
    scene garage_opened
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    show garage_over_blink zorder 10

    show Romka Normal m_night_winter 00 what ahead 03:
        xzoom -1
        xoffset 400
        yoffset 75
    with Dissolve(.15)
    voice "voice/anton/4day/Net.ogg"
    Ant "Нет, Ром, без милиции мы туда не сунемся."
    "И без того кислое лицо товарища сморщилось, словно он откусил лимон."
    play test_five "sounds/steps/steps_snow001.ogg"

    stop test_one fadeout 1
    stop test_three fadeout 1

    show Romka Normal m_night_winter 00 what aside 03 with Dissolve(0.01):
        parallel:
            linear 2 xoffset 1200
        parallel:
            linear .2 yoffset 65
            linear .2 yoffset 75
            linear .2 yoffset 65
            linear .2 yoffset 75
            linear .2 yoffset 65
            linear .2 yoffset 75
            linear .2 yoffset 65
            linear .2 yoffset 75
            linear .2 yoffset 65
            linear .2 yoffset 75
    hide garage_smoke_1 onlayer master1
    hide garage_smoke_2 onlayer master1
    stop music fadeout 3.5
    scene bg_black
    with Dissolve(1.)
    voice "voice/romka/4day/177 x.ogg"
    Rom "Хрен с тобой!"

    scene police_station
    show police_01
    show police_roma
    show police_anton
    show blizzard_d4_evening_far:
        parallel:
            ypan 0
            linear 20 ypan -360
            repeat
        parallel:
            xpan 0
            linear 20 xpan -360
            repeat
    show blizzard_d4_evening_near:
        parallel:
            ypan 0
            linear 20 ypan -360
            repeat
        parallel:
            xpan 0
            linear 20 xpan -360
            repeat
    show blizzard_d4_evening_face
    with Dissolve(.5)
    voice "voice/romka/4day/178 To.ogg"
    Rom "Только попомни мои слова: менты хуже душегубов."

    call d4_police_entry from _call_d4_police_entry_1

    jump d4_police_voluntary



label d4_garage_choice_enter:
    $ story_manager.MarkEvent(("day4", "garage", "enter"))

    label mold_test2:
    $ Flags.Raise("katya")

    scene d4_gar_bg
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big
    show d4_gar_Ant:
        yoffset 10
    show d4_gar_Roma:
        xoffset 50
        yoffset 10
    show d4_gar_door 0
    show d4_gar_fg zorder 1
    with Dissolve(.5)

    play sound "sounds/sfx_footsteps_snow_two.ogg" 
    stop test_three fadeout 1.5
    play test_six "sounds/loop_Black_garage_generator_inside.ogg" volume 0.4 fadein 1.5 loop


    "Мы приблизились к постройке."

    show d4_gar_door 1 with Dissolve(.5)

    "Из короба не доносилось ни звука - только гудел генератор."

    play sound "sounds/sfx_Black_garage_knock.ogg"
    show d4_gar_door 1_2

    "Ромка постучал костяшками по воротам, убеждаясь, что они не собираются превращаться в хищные челюсти."

    play sound "sounds/sfx_Black_garage_open_2.ogg"


    show d4_gar_door 3:
        pause .5
        "d4_gar_door 4" with Dissolve(.5)
    play test_three "sounds/loop_footsteps_metal_normal_one.ogg" 
    show d4_gar_Roma behind d4_gar_fg:
        align (.5, 1.)
        xoffset 50
        yoffset 10
        pause 1.5
        parallel:
            linear .35 xoffset 250 zoom 1.1
        parallel:
            linear .20 yoffset 0
            linear .15 yoffset 50
        parallel:
            pause .2
            linear .5 alpha 0

    pause 1.5
    stop test_three fadeout 4

    "Осмелев, он распахнул двери пошире и принялся ощупывать проём в поисках выключателя."
    voice "voice/romka/4day/182 Toh.ogg"
    Rom "Тоха, помоги-ка мне."


    play test_five "sounds/sfx_Black_garage_open_3.ogg"
    $ renpy.music.set_volume(0.25, delay=1, channel="fon")

    show d4_gar_door 5

    play test_four "sounds/sfx_footsteps_metal.ogg"
    $ renpy.music.set_volume(0.25, delay=1, channel="test_one")


    window hide
    scene d4_garage_lookin_dark
    show blizzard_d4_evening2_big onlayer master1
    with Dissolve(.5)
    call screen day4_garage_lighton


    play test_three "sounds/sfx_Black_garage_light_switch.ogg" 

    scene d4_garage_in 3:
        align (.5, .5)
        zoom 0.92
    show d4_garage_gate
    with Dissolve(.5)
    stop music fadeout 3.5
    "..."
    "Гараж оказался самым обыкновенным."
    "Полки с инструментами по бокам, какие-то канистры и тряпки да накрытая чехлом машина."
    "Ни маньяков, ни их жертв."
    "Я даже усмехнулся от облегчения. И прочёл те же эмоции на лице товарища."

    scene d4_garage_lookin_light r2:
        align (.5, .5)
        zoom 0.92
    show d4_garage_gate
    with Dissolve(.5)

    play test_three "sounds/sfx_footsteps_metal_away.ogg" 

    "Ромка вошёл в гараж и обогнул по часовой стрелке автомобиль."

    show d4_garage_lookin_light r1 with Dissolve(.5)

    "Пошарил среди пыльных полок. Посмотрел на меня."

    scene d4_garage_lookin_light r1:
        align (.5, .5)
        zoom .91
        linear .5 zoom .95
    show d4_garage_gate:
        align (.5, .5)
        linear .5 xoffset -50 zoom 1.1

    play sound "sounds/sfx_footsteps_metal.ogg"

    pause .25
    hide garage_smoke_1 onlayer master1
    hide garage_smoke_2 onlayer master1

    scene d4_garage_lookin_light r1:
        align (1., 1.)
    hide blizzard_d4_evening2_big onlayer master1
    show garage_over_slow_blink zorder 1
    show d4_dust_norm
    with Dissolve(.25)

    "Я расхрабрился настолько, что перешагнул порог."
    "В углах, как паутина, налипла тьма. Паук, если он и был, давно покинул гнездо."
    jump d4_garage_lookaround




label d4_garage_lookaround:
    $ story_manager.MarkEvent(("day4", "la garage"))
    $ SceneFlags.Reset()
    label d4_garage_lookaround.main:
        window hide
        call screen day4_garagein_observe
        window show

    label d4_garage_lookaround.tools:
        $ story_manager.MarkEvent(("day4", "la garage", "tools"))
        if SceneFlags.Seen("tools"):
            "Инструменты."
        else:
            play sound "sounds/sfx_metal_tools.ogg"
            "Ржавые железяки, похожие на стальные клыки в пасти этого мёрзлого места или на пыточные инструменты средневекового палача."
            "К таким прикоснёшься, и на пальце сразу расцветёт рана, а в порез просочится инфекция от ржавчины и засохшего жира, и ты сгниёшь заживо."
            "Там на щипцах что-то багровое. Надо подойти и проверить… краска. Это просто краска."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main

    label d4_garage_lookaround.junk:
        $ story_manager.MarkEvent(("day4", "la garage", "junk"))
        if SceneFlags.Seen("junk"):
            "Хлам."
        else:
            play sound "sounds/sfx_match_lit.ogg"
            "Почему мне это так напоминает алтарь? Точно Гараж – это церковь, а здесь – атрибуты нечеловеческой таёжной религии..."
            "Я не хочу видеть иконы этой звериной веры! Древние письмена и железные реликвии."
            "Да нет же, просто хлам!"
            "Никому тут не молятся, не бывает таких храмов! А воск на столешнице потому, что электричество часто отключают, и хозяин работает при свечах."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main

    label d4_garage_lookaround.boxes:
        $ story_manager.MarkEvent(("day4", "la garage", "boxes"))
        if SceneFlags.Seen("boxes"):
            "Ящики."
        else:
            play sound "sounds/sfx_box_drag.ogg" 
            "Отсечённые конечности, груды фарша и головы, облепленные мясными мухами. Вот, что я увижу, заглянув в ящик."
            "Как в ночном кошмаре: страшная версия «Поля чудес», в которой ведущий, хохоча и пуская слюну, вынимает из коробки истекающие гноем призы."
            "Но наяву ящик пуст. Если что там и было, это убрали с глаз долой."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main

    label d4_garage_lookaround.car:
        $ story_manager.MarkEvent(("day4", "la garage", "car"))
        if SceneFlags.Seen("car"):
            "Автомобиль."
        else:
            play sound "sounds/sfx_engine_ignition.ogg"
            "Это машина. Что же ещё? Просто автомобиль, накрытый тканью. Внутри никого нет, ни живых, ни мёртвых. Вонь застарелой крови, она..."
            "Она только у меня в голове. То, что находится под мешковиной, пахнет машинным маслом, не более."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main

    label d4_garage_lookaround.tiski:
        $ story_manager.MarkEvent(("day4", "la garage", "tiski"))
        if SceneFlags.Seen("tiski"):
            "Тиски."
        else:
            play sound "sounds/sfx_bench_vise.ogg" 
            "Что ими сжимали? Что хрустело между металлическими челюстями? Что лилось на верстак из рвущейся плоти? Чугун от длительного использования совсем раскрошился."
            "Но это обыкновенные слесарские тиски, такие же стоят в кабинете труда. Тиски для деталей, а не для жертв. Капли масла, а не крови."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main

    label d4_garage_lookaround.shelf:
        $ story_manager.MarkEvent(("day4", "la garage", "shelf"))
        if SceneFlags.Seen("shelf"):
            "Верхняя полка."
        else:
            play sound "sounds/sfx_pot_shards.ogg" 
            "Тусклый свет не проникает туда. В темноте может быть что угодно. Вдруг, оно смотрит на меня в упор, прячась за кружевом паутины? А если встать на цыпочки…"
            "Пыль и рухлядь."
            $ true_detective_count4 += 1
        jump d4_garage_lookaround.main


label d4_garage_followup:
    $ story_manager.MarkEvent(("day4", "scene_garage"))

    voice "voice/romka/4day/183 r.ogg"
    Rom "Аргх, ржавый хлам!"
    voice "voice/romka/4day/184 ok.ogg"
    Rom "Оказывается, это место капец какое унылое."
    voice "voice/romka/4day/185 K.ogg"
    Rom "Какому такому мудаку пришла в голову идея перевозить гараж с места на место?"
    voice "voice/romka/4day/186 Po.ogg"
    Rom "Пошли отсюда."
    voice "voice/anton/4day/10 Aga.ogg"
    Ant "Ага!"
    voice "voice/anton/4day/10 Da.ogg"
    Ant "Давай догоним Бяшу, ему крепко досталось."

    scene d4_garage_lookin_light r1:
        align (.5, .5)
        zoom 0.92
        blur 4.0

    play sound "sounds/loop_footsteps_metal_normal_one.ogg" fadein 1

    show bg_black:
        alpha 0
        block:
            8
            function play_lamp_blink_4
            alpha .3
            .05
            alpha 0
            repeat 2
    show d4_garage_gate
    show Ant Normal b_evening 00 norm ahead 01:
        xoffset -200
    show blizzard_d4_evening2_big onlayer master1
    show blizzard_d4_evening_face onlayer master1
    with Dissolve(.5)

    pause 1.5
    stop sound fadeout 1.6

    "Я вышел под снегопад."
    show d4_garage_lookin_light r2 with Dissolve(.5)
    "Ромка уже топал к выходу, когда вдруг остановился и задумчиво поглядел на автомобиль."
    scene d4_garage_lookin_light r1:
        align (.5, .5)
        zoom 0.92
    show bg_black:
        alpha 0
        block:
            4
            function play_lamp_blink_4
            alpha .3
            .05
            alpha 0
            4
            repeat 2
    show d4_garage_gate:
        blur 8.0
    show Ant Normal b_evening 00 norm ahead 01:
        xoffset -200
        blur 4.0

    show layer master1:
        linear .5 blur 8
    with Dissolve(.5)
    voice "voice/romka/4day/187 S.ogg"
    Rom "Слушай, а что это мы с пустыми руками будем возвращаться?"
    voice "voice/romka/4day/188 D.ogg"
    Rom "Дай-ка я хоть магнитолу скручу."
    voice "voice/romka/4day/189 O.ogg"
    Rom "Обожди минуту, я мигом."
    play test_two "voice/kate/110 Vsh.ogg"
    scene d4_garage_lookin_light r3:
        align (.5, .5)
        zoom 0.92
        blur 4
    show bg_black:
        alpha 0
        block:
            1.

            block:
                function play_lamp_blink_4

                alpha .3
                .05
                alpha 0
                .05
                repeat 3
            2.
            repeat
    show d4_garage_gate
    show Ant Normal b_evening 00 norm ahead 05:
        xoffset -200
    show layer master1:
        linear .5 blur 0
    with Dissolve(.5)

    "Из-под чехла раздался всхлип."

    play sound "sounds/sfx_footsteps_snow_very_fast.ogg"

    scene d4_garage_lookin_light r3:
        align (.5, .5)
        zoom 0.92
        blur 4
    show bg_black:
        alpha 0
        block:
            1.

            block:
                function play_lamp_blink_4

                alpha .3
                .05
                alpha 0
                .05
                repeat 3
            2.
            repeat
    show d4_garage_gate
    show d4_anton_back_night:
        align (.5, .5)
        xoffset -200
        yoffset 100
        zoom 1.5

    with Dissolve(.5)

    play test_one "sounds/Tension Suspense Risers_01.ogg"
    "От неожиданности я чуть не плюхнулся в сугроб."
    scene d4_garage_lookin_light r4:
        align (.5, .5)
        zoom 0.92
    show bg_black:
        alpha 0
        block:
            1.

            block:
                function play_lamp_blink_4

                alpha .3
                .05
                alpha 0
                .05
                repeat 3
            2.
            repeat
    show d4_garage_gate:
        blur 8
    show d4_anton_back_night:
        align (.5, .5)
        xoffset -200
        yoffset 100
        zoom 1.5
        blur 4
    show layer master1:
        linear .5 blur 8
    with Dissolve(.5)
    voice "voice/romka/4day/190 T.ogg"
    Rom "Ты слышал? Она там!"

    scene d4_gar_bg
    hide blizzard_d4_evening2_big onlayer master1
    hide blizzard_d4_evening_face onlayer master1
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening2_big
    show d4_gar_Ant:
        yoffset 10
    show d4_gar_door 4
    show d4_gar_fg zorder 1

    show bg_black zorder 1:
        alpha 0
        block:
            3.

            block:
                function play_lamp_blink_4

                .05
                alpha .3
                .05
                alpha 0

                repeat 2
            3.

            block:
                function play_lamp_blink_4

                .05
                alpha .3
                .05
                alpha 0

                repeat 3
            repeat
    with Dissolve(.5)

    play sound "sounds/sfx_cover_pluck.ogg"


    "Я смотрел, как друг дёргает за ткань. Но подбежать помочь не хватало сил."
    "Ноги словно примёрзли к земле."

    play sound "sounds/sfx_cover_cut_throw.ogg"

    "Но Ромка справился без меня. Вспоротый с помощью ножа чехол полетел в сторону."
    play test_six "music/Anton Zoom.ogg"
    "Под ним не было автомобиля."

    scene d4_garage_lookin_meat r3:
        align (.5, .5)
        zoom .91
    show d4_garage_canvas
    show bg_black:
        alpha 0
        block:
            1.

            block:
                function play_lamp_blink_4
                alpha .7
                .05
                alpha 0
                .05
                repeat 3

            .2

            block:
                function play_lamp_blink_4
                alpha .7
                .05
                alpha 0
                .05
                repeat 2

            2.
            repeat
    show d4_garage_gate
    show blizzard_d4_evening2_big
    with Dissolve(.5)

    "Там, вырастая из пола, блестела машинным маслом огромная мясорубка."
    $ add_text_to_dictionary(42)
    "Я видел такую в одной передаче «{u}До шестнадцати и старше{/u}»."
    "Промышленная махина, которой на фабриках перемалывали коровьи туши для колбасы."

    scene d4_garage_katya:
        yalign 1.
        linear 5 yalign 0.
    show bg_black:
        alpha 0
        block:
            1.

            function play_lamp_blink_1


            block:
                alpha .7
                .05
                alpha 0
                .05
                repeat 3

            .2

            block:
                function play_lamp_blink_4
                alpha .7
                .05
                alpha 0
                .05
                repeat 2

            2.
            repeat
    play test_two "voice/kate/110 Vsh2.ogg"
    play test_six "music/Tension Suspense Risers_002.ogg"
    "В раструбе, напоминающем зёв кровожадного цветка венериной мухоловки, находилась связанная Катя."
    "Она очнулась словно от сна и её глаза округлились от страха. Кляп позволял лишь хныкать и мычать."
    voice "voice/romka/4day/191 S.ogg"
    Rom "Скорее сюда!"

    play sound "sounds/sfx_footsteps_metal_fast_one_close.ogg" fadein 0.5

    scene d4_garage_in 5:
        align (1., 1.)
    show d4_garage_canvas zorder 3:
        align (1., 1.)

    show d4_garage_romka 3 zorder 3:
        align (1., 1.)
    show d4_garage_grinder_katya 1 zorder 1:
        align (1., 1.)
    show d4_garage_grinder zorder 2:
        align (1., 1.)
    show bg_black zorder 3:
        alpha 0
        block:
            1.

            function play_lamp_blink_1


            block:
                alpha .7
                .05
                alpha 0
                .05
                repeat 3

            .4

            block:
                function play_lamp_blink_4
                alpha .7
                .05
                alpha 0
                .05
                repeat 2

            2.
            repeat
    show d4_dust_norm zorder 2
    with Dissolve(.15)
    "Я сбросил с себя оторопь, как тяжёлый чехол, и рванул в гараж."

    play test_four "sounds/sfx_footsteps_metal_fast_one_distant.ogg" fadein 1.5 volume 0.6

    hide d4_garage_romka
    show d4_garage_grinder_romka:
        align (1., 1.)
    with Dissolve(.5)


    "Тем временем Ромка почти взобрался на стальную душегубку, он взял Катю подмышки и..."

    play sound "sounds/sfx_lever_switch.ogg" 
    $ renpy.music.set_volume(0.1, delay=0, channel="test_five")
    play test_four "sounds/loop_meat_grinder_idle.ogg" fadein 5 loop
    play test_five "sounds/loop_meat_grinder_grind.ogg" loop


    "Вероятно, коленом Ромка зацепил какую-то кнопку."
    play test_two "voice/kate/110 Vsh0.ogg"

    show d4_garage_grinder_katya 2 with Dissolve(.5)
    "Загудел механизм. Звук напоминал ворчание голодного желудка."
    "Ромка закричал испуганно, явно осознавая, что он наделал:"

    show d4_garage_grinder_romka:
        linear .15 yoffset 10
        linear .15 yoffset 0
        .5
        repeat 2
    voice "voice/romka/4day/192 Ch.ogg"
    Rom "Чёрт! Выключи! Выключи её!"

    play sound "sounds/sfx_footsteps_metal_fast_one_close.ogg" fadein 1

    show d4_garage_grinder_ant 1 with Dissolve(.5):
        align (1., 1.)
    voice "voice/anton/4day/11 Yas.ogg"
    Ant "Я сейчас! Держись!"

    show d4_garage_grinder_ant 1:
        linear .15 yoffset 10
        linear .15 yoffset 0
    "Ничего!"

    scene d5_katya_lever_bg:
        subpixel True
        align (.25, .5)
        blur 4
        zoom 1.15
    show d5_katya_lever_fg:
        subpixel True
        align (.25, .5)
        zoom 1.30
        block:
            linear 0.08 xoffset 2 yoffset 2
            linear 0.08 xoffset -2 yoffset -2
            repeat
    show d4_garage_antonback:
        anchor (.5, 1.)
        pos (.25, 1.)
        zoom 2.0
        yoffset 200
        xoffset -300
        transform_anchor True
        rotate 25
        block:
            block:
                linear .15 yoffset 200 + 15 xoffset -300 -10
                linear .15 yoffset 200 xoffset -300
                .5
                repeat 2
            1.0
            repeat
    with Dissolve(.25)
    "Ни одна чёртова кнопка, ни один тумблер не могли остановить этот жуткий скрежет жерновов."

    scene d4_garage_in 5:
        align (1., 1.)
    show d4_garage_canvas zorder 3:
        align (1., 1.)

    show d4_garage_grinder_katya 2 zorder 1:
        align (1., 1.)
    show d4_garage_grinder zorder 2:
        align (1., 1.)
    show d4_garage_grinder_romka:
        align (1., 1.)
    show d4_garage_grinder_ant 1:
        align (1., 1.)
        linear .15 yoffset 10
        linear .15 yoffset 0
        .5
        repeat 2
    show bg_black zorder 3:
        alpha 0
        block:
            1.

            function play_lamp_blink_1


            block:
                alpha .7
                .05
                alpha 0
                .05
                repeat 3

            .4

            block:
                function play_lamp_blink_4
                alpha .7
                .05
                alpha 0
                .05
                repeat 2

            2.
            repeat
    show d4_dust_norm zorder 2
    with Dissolve(.15)
    voice "voice/anton/4day/12 Nera.ogg"
    Ant "Не работает! Ни хрена не помогает!"

    show d4_garage_grinder_romka:
        linear .15 yoffset 10
        linear .15 yoffset 0
    voice "voice/romka/4day/193 Ta.ogg"
    Rom "Так помоги мне!"
    stop test_four fadeout 5

    show d4_garage_grinder_ant 2 with Dissolve(.5)
    "Мы согнулись над Катей и рванули её за локоть."

    $ renpy.music.set_volume(0.0, delay=6, channel="test_four")
    $ renpy.music.set_volume(1.0, delay=6, channel="test_five")

    "Внизу заработали спирали. Сначала медленно, но с каждым витком они набирали скорость."


    "Раздался хруст. Так костёр поедает хворост."
    play test_two "voice/kate/110 Vsh3.ogg"
    play music "music/Garazh_part2.ogg" fadein 0.5

label d4_save_katya:

    $ story_manager.MarkEvent(("day4", "game katya"))

    $ SK_easy_mode = SK_easy_mode_true
    $ SK_hard_mode = SK_hard_mode_true
    jump settings_end

    label dev_d4_save_katya hide:
        menu:
            "POLAROID YES":
                $ Flags.Raise("polaroid")
            "POLAROID NO":
                pass


        scene black
        menu:
            "press SPACE to win":
                $ SK_easy_mode = SK_easy_mode_debug
                $ SK_hard_mode = SK_hard_mode_debug
                jump settings_end
            "true difficulty":
                $ SK_easy_mode = SK_easy_mode_true
                $ SK_hard_mode = SK_hard_mode_true
                jump settings_end
            "configure":
                python:
                    SK_spd_easy_custom = (-25, 25)
                    SK_spd_hard_custom = (-25, 25)
                    SK_sps_easy_custom = -50.0/.3
                    SK_sps_hard_custom = -205.0
                    SK_boost_easy_custom = 35
                    SK_boost_hard_custom = 35
                    SK_decmod_easy_custom = 0.0
                    SK_decmod_hard_custom = 0.7
                    SK_trigrange_easy_custom = (5, 5)
                    SK_trigrange_hard_custom = (180, 5)
                    SK_windel_easy_custom = 3.0
                    SK_windel_hard_custom = 10.0
                jump settings_main

        label settings_main:
            menu:
                "round 1":
                    jump settings_round1
                "round 2":
                    jump settings_round2
                "finish":
                    $ SK_easy_mode_custom = puzKatyaSettings(
                        speed = SK_spd_easy_custom,
                        speed_per_second = SK_sps_easy_custom,
                        speed_boost = SK_boost_easy_custom,
                        decay_mod = SK_decmod_easy_custom,
                        trigger_range = SK_trigrange_easy_custom,
                        win_delay = SK_windel_easy_custom,
                        disp = SK_disp_easy)
                    $ SK_hard_mode_custom = puzKatyaSettings(
                        speed = SK_spd_hard_custom,
                        speed_per_second = SK_sps_hard_custom,
                        speed_boost = SK_boost_hard_custom,
                        decay_mod = SK_decmod_hard_custom,
                        trigger_range = SK_trigrange_hard_custom,
                        win_delay = SK_windel_hard_custom,
                        disp = SK_disp_hard)

                    $ SK_easy_mode = SK_easy_mode_custom
                    $ SK_hard_mode = SK_hard_mode_custom

                    jump settings_end









        label settings_round1:
            menu:
                "Speed: [SK_spd_easy_custom] Per Sec: [SK_sps_easy_custom]\nBoost: [SK_boost_easy_custom] Decay: [SK_decmod_easy_custom]\nTrigger: [SK_trigrange_easy_custom] Win delay: [SK_trigrange_easy_custom]"
                "back":
                    jump settings_main
                "speed limit":
                    jump settings_round1.speed
                "speed per second":
                    jump settings_round1.sps
                "boost power":
                    jump settings_round1.boost
                "decay modifier":
                    jump settings_round1.decay
                "trigger range":
                    jump settings_round1.trigger
                "win delay":
                    jump settings_round1.win

            label settings_round1.speed:
                menu:
                    "SPEED LIMIT, нижний и верхний пределы скорости Кати. Нижний предел - максимальная скорость затягивания, верхний предел - максимальная скорость вытягивания.\nТекущее значение: [SK_spd_easy_custom]"
                    "back":
                        jump settings_round1
                    "bottom: -1":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0] -1, SK_spd_easy_custom[1])
                        jump settings_round1.speed
                    "bottom: -5":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0] -5, SK_spd_easy_custom[1])
                        jump settings_round1.speed
                    "bottom: +1":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0] +1, SK_spd_easy_custom[1])
                        jump settings_round1.speed
                    "bottom: +5":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0] +5, SK_spd_easy_custom[1])
                        jump settings_round1.speed
                    "top: -1":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0], SK_spd_easy_custom[1] -1)
                        jump settings_round1.speed
                    "top: -5":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0], SK_spd_easy_custom[1] -5)
                        jump settings_round1.speed
                    "top: +1":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0], SK_spd_easy_custom[1] +1)
                        jump settings_round1.speed
                    "top: +5":
                        $ SK_spd_easy_custom = (SK_spd_easy_custom[0], SK_spd_easy_custom[1] +5)
                        jump settings_round1.speed

            label settings_round1.sps:
                menu:
                    "SPEED PER SECOND, изменение скорости каждую секунду.\nТекущее значение: [SK_sps_easy_custom]"
                    "back":
                        jump settings_round1
                    "-0.1":
                        $ SK_sps_easy_custom = SK_sps_easy_custom - 0.1
                        jump settings_round1.sps
                    "-1.0":
                        $ SK_sps_easy_custom = SK_sps_easy_custom - 1.0
                        jump settings_round1.sps
                    "-10.0":
                        $ SK_sps_easy_custom = SK_sps_easy_custom - 10.0
                        jump settings_round1.sps
                    "+0.1":
                        $ SK_sps_easy_custom = SK_sps_easy_custom + 0.1
                        jump settings_round1.sps
                    "+1.0":
                        $ SK_sps_easy_custom = SK_sps_easy_custom + 1.0
                        jump settings_round1.sps
                    "+10.0":
                        $ SK_sps_easy_custom = SK_sps_easy_custom + 10.0
                        jump settings_round1.sps

            label settings_round1.boost:
                menu:
                    "BOOST POWER, изменение скорости за каждый клик.\nТекущее значение: [SK_boost_easy_custom]"
                    "back":
                        jump settings_round1
                    "-1":
                        $ SK_boost_easy_custom = SK_boost_easy_custom - 1
                        jump settings_round1.boost
                    "-10":
                        $ SK_boost_easy_custom = SK_boost_easy_custom - 10
                        jump settings_round1.boost
                    "+1.0":

                        $ SK_boost_easy_custom = SK_boost_easy_custom + 1
                        jump settings_round1.boost
                    "+10.0":
                        $ SK_boost_easy_custom = SK_boost_easy_custom + 10
                        jump settings_round1.boost

            label settings_round1.decay:
                if SK_decmod_easy_custom < 0.0:
                    $ SK_decmod_easy_custom = 0.0
                if SK_decmod_easy_custom > 1.0:
                    $ SK_decmod_easy_custom = 1.0
                menu:
                    "DECAY MODIFIER, изменение силы буста в зависимости от прогресса: чем выше Катя, тем сложнее её поднять. Допустимый диапазон от 0.0 до 1.0. \nТекущее значение: [SK_decmod_easy_custom]"
                    "back":
                        jump settings_round1
                    "info":

                        "Модификатор уменьшает силу буста в зависимости от того, где сейчас находится Катя. Катин прогресс пересчитывается в число от 0 до 1, где 0 - нижний край, а 1 - верхний край."
                        "Пересчитанный катин прогресс умножается на Decay-модификатор, и полученная доля вычитывается из буста."
                        "К примеру, буст 100, decay 0.5, Катя на 150 пикселях. Катин прогресс = 150/200 = 0.75, итоговый буст = 100 - (1.0 - 0.5 * 0.75) = 75"
                        "Второй раунд настроен так, что в нём высокий decay, но и зона победы - 180 пикселей. Поднять Катю до самого верха невозможно, но это и не надо - достаточно не дать ей упать несколько секунд."
                        jump settings_round1.decay
                    "-0.1":

                        $ SK_decmod_easy_custom = SK_decmod_easy_custom - 0.1
                        jump settings_round1.decay
                    "+0.1":

                        $ SK_decmod_easy_custom = SK_decmod_easy_custom + 0.1
                        jump settings_round1.decay

            label settings_round1.trigger:
                if SK_trigrange_easy_custom[0] < 0:
                    $ SK_trigrange_easy_custom = (0, SK_trigrange_easy_custom[1])
                if SK_trigrange_easy_custom[0] > 200:
                    $ SK_trigrange_easy_custom = (200, SK_trigrange_easy_custom[1])
                if SK_trigrange_easy_custom[1] < 0:
                    $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], 0)
                if SK_trigrange_easy_custom[1] > 200:
                    $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], 200)
                menu:
                    "TRIGGER RANGE, зоны срабатывания победы и поражения.\nТекущее значение (WIN, LOSE): [SK_trigrange_easy_custom]"
                    "back":
                        jump settings_round1
                    "info":

                        "Всего у Кати 200 пикселей для перемещения, начинает она посередине, на 100."
                        "WIN: в скольки пикселях от верхнего края начинает отсчитываться таймер победы. К примеру, 5 - это в диапазоне от 195 до 200. 160 - от 40 до 200."
                        "LOSE: аналогично, только от нижнего края. 5 - от 0 до 5. 40 - от 0 до 40."
                        "Для победы Катю надо удержать в зоне поражения какое-то время, поражение же засчитывает мгновенно, как Катя попала в зону LOSE."
                        jump settings_round1.trigger
                    "WIN: -1":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0] -1, SK_trigrange_easy_custom[1])
                        jump settings_round1.trigger
                    "WIN: -10":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0] -10, SK_trigrange_easy_custom[1])
                        jump settings_round1.trigger
                    "WIN: +1":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0] +1, SK_trigrange_easy_custom[1])
                        jump settings_round1.trigger
                    "WIN: +10":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0] +10, SK_trigrange_easy_custom[1])
                        jump settings_round1.trigger
                    "LOSE: -1":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], SK_trigrange_easy_custom[1] -1)
                        jump settings_round1.trigger
                    "LOSE: -10":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], SK_trigrange_easy_custom[1] -10)
                        jump settings_round1.trigger
                    "LOSE: +1":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], SK_trigrange_easy_custom[1] +1)
                        jump settings_round1.trigger
                    "LOSE: +10":

                        $ SK_trigrange_easy_custom = (SK_trigrange_easy_custom[0], SK_trigrange_easy_custom[1] +10)
                        jump settings_round1.trigger

            label settings_round1.win:
                if SK_windel_easy_custom < 0:
                    $ SK_windel_easy_custom = SK_windel_easy_custom = 0.01
                menu:
                    "WIN DELAY, задержка победы. Для засчитывания победы игрок должен удержать Катю в победной зоне в течение этого времени.\nТекущее значение: [SK_windel_easy_custom]"
                    "back":
                        jump settings_round1
                    "info":

                        "Для засчитывания победы игрок должен удержать Катю в победной зоне в течение заданного времени. Если за время отсчёта таймера Катя покинула зону победы - таймер сбрасывается."
                        "Для засчитывания поражения игрок должен довести Катю до зоны, поражение засчитывается сразу же."
                        jump settings_round1.win
                    "-0.1":

                        $ SK_windel_easy_custom = SK_windel_easy_custom - 0.1
                        jump settings_round1.win
                    "-1.0":
                        $ SK_windel_easy_custom = SK_windel_easy_custom - 1.0
                        jump settings_round1.win
                    "-10.0":
                        $ SK_windel_easy_custom = SK_windel_easy_custom - 10.0
                        jump settings_round1.win
                    "+0.1":
                        $ SK_windel_easy_custom = SK_windel_easy_custom + 0.1
                        jump settings_round1.win
                    "+1.0":
                        $ SK_windel_easy_custom = SK_windel_easy_custom + 1.0
                        jump settings_round1.win
                    "+10.0":
                        $ SK_windel_easy_custom = SK_windel_easy_custom + 10.0
                        jump settings_round1.win

        label settings_round2:
            menu:
                "Speed: [SK_spd_hard_custom] Per Sec: [SK_sps_hard_custom]\nBoost: [SK_boost_hard_custom] Decay: [SK_decmod_hard_custom]\nTrigger: [SK_trigrange_hard_custom] Win delay: [SK_windel_hard_custom]"
                "back":
                    jump settings_main
                "speed limit":
                    jump settings_round2.speed
                "speed per second":
                    jump settings_round2.sps
                "boost power":
                    jump settings_round2.boost
                "decay modifier":
                    jump settings_round2.decay
                "trigger range":
                    jump settings_round2.trigger
                "win delay":
                    jump settings_round2.win

            label settings_round2.speed:
                menu:
                    "SPEED LIMIT, нижний и верхний пределы скорости Кати. Нижний предел - максимальная скорость затягивания, верхний предел - максимальная скорость вытягивания.\nТекущее значение: [SK_spd_hard_custom]"
                    "back":
                        jump settings_round2
                    "bottom: -1":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0] -1, SK_spd_hard_custom[1])
                        jump settings_round2.speed
                    "bottom: -5":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0] -5, SK_spd_hard_custom[1])
                        jump settings_round2.speed
                    "bottom: +1":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0] +1, SK_spd_hard_custom[1])
                        jump settings_round2.speed
                    "bottom: +5":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0] +5, SK_spd_hard_custom[1])
                        jump settings_round2.speed
                    "top: -1":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0], SK_spd_hard_custom[1] -1)
                        jump settings_round2.speed
                    "top: -5":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0], SK_spd_hard_custom[1] -5)
                        jump settings_round2.speed
                    "top: +1":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0], SK_spd_hard_custom[1] +1)
                        jump settings_round2.speed
                    "top: +5":
                        $ SK_spd_hard_custom = (SK_spd_hard_custom[0], SK_spd_hard_custom[1] +5)
                        jump settings_round2.speed

            label settings_round2.sps:
                menu:
                    "SPEED PER SECOND, изменение скорости каждую секунду.\nТекущее значение: [SK_sps_hard_custom]"
                    "back":
                        jump settings_round2
                    "-0.1":
                        $ SK_sps_hard_custom = SK_sps_hard_custom - 0.1
                        jump settings_round2.sps
                    "-1.0":
                        $ SK_sps_hard_custom = SK_sps_hard_custom - 1.0
                        jump settings_round2.sps
                    "-10.0":
                        $ SK_sps_hard_custom = SK_sps_hard_custom - 10.0
                        jump settings_round2.sps
                    "+0.1":
                        $ SK_sps_hard_custom = SK_sps_hard_custom + 0.1
                        jump settings_round2.sps
                    "+1.0":
                        $ SK_sps_hard_custom = SK_sps_hard_custom + 1.0
                        jump settings_round2.sps
                    "+10.0":
                        $ SK_sps_hard_custom = SK_sps_hard_custom + 10.0
                        jump settings_round2.sps

            label settings_round2.boost:
                menu:
                    "BOOST POWER, изменение скорости за каждый клик.\nТекущее значение: [SK_boost_hard_custom]"
                    "back":
                        jump settings_round2
                    "-1":
                        $ SK_boost_hard_custom = SK_boost_hard_custom - 1
                        jump settings_round2.boost
                    "-10":
                        $ SK_boost_hard_custom = SK_boost_hard_custom - 10
                        jump settings_round2.boost
                    "+1.0":

                        $ SK_boost_hard_custom = SK_boost_hard_custom + 1
                        jump settings_round2.boost
                    "+10.0":
                        $ SK_boost_hard_custom = SK_boost_hard_custom + 10
                        jump settings_round2.boost

            label settings_round2.decay:
                if SK_decmod_hard_custom < 0.0:
                    $ SK_decmod_hard_custom = 0.0
                if SK_decmod_hard_custom > 1.0:
                    $ SK_decmod_hard_custom = 1.0
                menu:
                    "DECAY MODIFIER, изменение силы буста в зависимости от прогресса: чем выше Катя, тем сложнее её поднять. Допустимый диапазон от 0.0 до 1.0. \nТекущее значение: [SK_decmod_hard_custom]"
                    "back":
                        jump settings_round2
                    "info":

                        "Модификатор уменьшает силу буста в зависимости от того, где сейчас находится Катя. Катин прогресс пересчитывается в число от 0 до 1, где 0 - нижний край, а 1 - верхний край."
                        "Пересчитанный катин прогресс умножается на Decay-модификатор, и полученная доля вычитывается из буста."
                        "К примеру, буст 100, decay 0.5, Катя на 150 пикселях. Катин прогресс = 150/200 = 0.75, итоговый буст = 100 - (1.0 - 0.5 * 0.75) = 75"
                        "Второй раунд настроен так, что в нём высокий decay, но и зона победы - 180 пикселей. Поднять Катю до самого верха невозможно, но это и не надо - достаточно не дать ей упать несколько секунд."
                        jump settings_round2.decay
                    "-0.1":

                        $ SK_decmod_hard_custom = SK_decmod_hard_custom - 0.1
                        jump settings_round2.decay
                    "+0.1":

                        $ SK_decmod_hard_custom = SK_decmod_hard_custom + 0.1
                        jump settings_round2.decay

            label settings_round2.trigger:
                if SK_trigrange_hard_custom[0] < 0:
                    $ SK_trigrange_hard_custom = (0, SK_trigrange_hard_custom[1])
                if SK_trigrange_hard_custom[0] > 200:
                    $ SK_trigrange_hard_custom = (200, SK_trigrange_hard_custom[1])
                if SK_trigrange_hard_custom[1] < 0:
                    $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], 0)
                if SK_trigrange_hard_custom[1] > 200:
                    $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], 200)
                menu:
                    "TRIGGER RANGE, зоны срабатывания победы и поражения.\nТекущее значение (WIN, LOSE): [SK_trigrange_hard_custom]"
                    "back":
                        jump settings_round2
                    "info":

                        "Всего у Кати 200 пикселей для перемещения, начинает она посередине, на 100."
                        "WIN: в скольки пикселях от верхнего края начинает отсчитываться таймер победы. К примеру, 5 - это в диапазоне от 195 до 200. 160 - от 40 до 200."
                        "LOSE: аналогично, только от нижнего края. 5 - от 0 до 5. 40 - от 0 до 40."
                        "Для победы Катю надо удержать в зоне поражения какое-то время, поражение же засчитывает мгновенно, как Катя попала в зону LOSE."
                        jump settings_round2.trigger
                    "WIN: -1":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0] -1, SK_trigrange_hard_custom[1])
                        jump settings_round2.trigger
                    "WIN: -10":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0] -10, SK_trigrange_hard_custom[1])
                        jump settings_round2.trigger
                    "WIN: +1":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0] +1, SK_trigrange_hard_custom[1])
                        jump settings_round2.trigger
                    "WIN: +10":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0] +10, SK_trigrange_hard_custom[1])
                        jump settings_round2.trigger
                    "LOSE: -1":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], SK_trigrange_hard_custom[1] -1)
                        jump settings_round2.trigger
                    "LOSE: -10":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], SK_trigrange_hard_custom[1] -10)
                        jump settings_round2.trigger
                    "LOSE: +1":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], SK_trigrange_hard_custom[1] +1)
                        jump settings_round2.trigger
                    "LOSE: +10":

                        $ SK_trigrange_hard_custom = (SK_trigrange_hard_custom[0], SK_trigrange_hard_custom[1] +10)
                        jump settings_round2.trigger

            label settings_round2.win:
                if SK_windel_hard_custom < 0:
                    $ SK_windel_hard_custom = SK_windel_hard_custom = 0.01
                menu:
                    "WIN DELAY, задержка победы.\nТекущее значение: [SK_windel_hard_custom]"
                    "back":
                        jump settings_round2
                    "info":

                        "Для засчитывания победы игрок должен удержать Катю в победной зоне в течение заданного времени. Если за время отсчёта таймера Катя покинула зону победы - таймер сбрасывается."
                        "Для засчитывания поражения игрок должен довести Катю до зоны, поражение засчитывается сразу же."
                        jump settings_round2.win
                    "-0.1":

                        $ SK_windel_hard_custom = SK_windel_hard_custom - 0.1
                        jump settings_round2.win
                    "-1.0":
                        $ SK_windel_hard_custom = SK_windel_hard_custom - 1.0
                        jump settings_round2.win
                    "-10.0":
                        $ SK_windel_hard_custom = SK_windel_hard_custom - 10.0
                        jump settings_round2.win
                    "+0.1":
                        $ SK_windel_hard_custom = SK_windel_hard_custom + 0.1
                        jump settings_round2.win
                    "+1.0":
                        $ SK_windel_hard_custom = SK_windel_hard_custom + 1.0
                        jump settings_round2.win
                    "+10.0":
                        $ SK_windel_hard_custom = SK_windel_hard_custom + 10.0
                        jump settings_round2.win

        label settings_end:


    $ SceneFlags.Reset()

    scene d4_sk_bg
    show d4_sk_katya 0:
        xpos 1000
        ypos 600
        anchor (.5, .5)
    show d4_sk_fg
    with Dissolve(.5)

    call screen btn_save_katya()
    play sound "sounds/loop_bones_grinding.ogg" fadein 4 loop

    show d4_sk_fg:
        linear .03 xoffset 5
        linear .03 xoffset -5
        repeat

    show d4_sk_katya 0
    pause .5
    show d4_sk_katya 00

    pause 1.0

    hide d4_sk_katya 0
    hide d4_sk_fg

    $ puz = puzKatya(win_lbl = "sK1_good", lose_lbl = "sK1_bad", settings = SK_easy_mode)
    call screen saveKatya(puz)
    jump expression _return


label sK1_good:
    window hide
    scene bg_black
    $ renpy.pause(1., hard=True)


    $ panic_mod = .75
    $ base_zoom = 1.1
    scene d4_sk_katya_fail:
        align (.5, 1.)
        zoom base_zoom
        parallel:
            linear .05 xoffset 5
            linear .05 xoffset -5
            repeat
        parallel:
            blur 8
            .5
            linear .5 yalign .0 blur 0
            block:
                parallel:
                    ease 1.0*panic_mod xalign 0.3
                    ease 1.0*panic_mod xalign 0.9
                    ease 1.0*panic_mod xalign 0.5
                    ease 0.2*panic_mod xalign 0.7
                    ease 0.2*panic_mod xalign 0.3
                    ease 1.0*panic_mod xalign 0.9
                    ease 1.0*panic_mod xalign 0.5
                    ease 1.0*panic_mod xalign 0.7
                    repeat
                parallel:
                    ease 0.8*panic_mod yoffset -0
                    ease 0.8*panic_mod yoffset -75
                    ease 0.8*panic_mod yoffset -25
                    ease 0.8*panic_mod yoffset -125
                    ease 0.2*panic_mod yoffset -75
                    ease 0.8*panic_mod yoffset -0
                    repeat
                parallel:
                    pause 2.0*panic_mod
                    ease 0.2 blur 8
                    ease 0.2 blur 0
                    repeat

                parallel:
                    ease 0.8*panic_mod zoom base_zoom + .05
                    ease 0.8*panic_mod zoom base_zoom + .15
                    ease 0.8*panic_mod zoom base_zoom + .07
                    ease 0.4*panic_mod zoom base_zoom + .12
                    ease 0.4*panic_mod zoom base_zoom + .05
                    ease 0.8*panic_mod zoom base_zoom + .15
                    ease 0.8*panic_mod zoom base_zoom + .07
                    ease 0.8*panic_mod zoom base_zoom + .12
                    repeat

    play test_seven "sounds/sfx_blood_splatter.ogg"

    show d4_sk_katya_blood_animation:
        align (.5, 1.)
        zoom 1.2

    show d4_blood_blink

    pause 1.5
    window show
    $ renpy.music.set_volume(0.25, 5, channel="test_five")
    play test_two "voice/kate/110 Vsh4.ogg"
    "Катя взвыла сквозь кляп."
    play test_four "sounds/loop_meat_grinder_idle.ogg" fadein 5 loop
    "Но мясорубка не отпускала — мясорубка питалась."

    scene d4_blood_bg:
        align (.5, .5)
        zoom 1.5
        parallel:
            linear 15 zoom 1.01
        parallel:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat

    show d4_blood_body:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            linear 15 zoom 1.1
        parallel:
            ease .25 yoffset 3
            ease .25 yoffset -3
            repeat

    show d4_blood_head:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            linear 15 zoom 1.1
        parallel:
            ease .25 yoffset -10
            ease .25 yoffset 10
            repeat

    show d4_blood_blink

    play test_six "sounds/sfx_meat_grinder_intense_1.ogg"

    with Dissolve(.5)

    play test_three "voice/anton/4day/13 Pih.ogg"
    "Я закричал, увидев, как лезвия наматывают на себя лохмотья сплюснутых ног."
    play test_three "voice/anton/4day/13 Pih2.ogg"
    "Ноги Кати теперь напоминали измочаленные колготы."
    play test_three "voice/anton/4day/13 Pih3.ogg"
    "Кости проткнули кожу и торчали, словно сучки."
    play test_three "voice/anton/4day/13 Pih4.ogg"
    "В багровом сиропе плавала белая коленная чашечка."

    $ panic_mod = .75
    $ base_zoom = 1.1
    scene d4_sk_katya_fail:
        align (.5, 0.)
        zoom base_zoom
        parallel:
            linear .05 xoffset 5
            linear .05 xoffset -5
            repeat
        parallel:
            parallel:
                ease 1.0*panic_mod xalign 0.3
                ease 1.0*panic_mod xalign 0.9
                ease 1.0*panic_mod xalign 0.5
                ease 0.2*panic_mod xalign 0.7
                ease 0.2*panic_mod xalign 0.3
                ease 1.0*panic_mod xalign 0.9
                ease 1.0*panic_mod xalign 0.5
                ease 1.0*panic_mod xalign 0.7
                repeat
            parallel:
                ease 0.8*panic_mod yoffset -0
                ease 0.8*panic_mod yoffset -75
                ease 0.8*panic_mod yoffset -25
                ease 0.8*panic_mod yoffset -125
                ease 0.2*panic_mod yoffset -75
                ease 0.8*panic_mod yoffset -0
                repeat
            parallel:
                pause 2.0*panic_mod
                ease 0.2 blur 8
                ease 0.2 blur 0
                repeat

            parallel:
                ease 0.8*panic_mod zoom base_zoom + .05
                ease 0.8*panic_mod zoom base_zoom + .15
                ease 0.8*panic_mod zoom base_zoom + .07
                ease 0.4*panic_mod zoom base_zoom + .12
                ease 0.4*panic_mod zoom base_zoom + .05
                ease 0.8*panic_mod zoom base_zoom + .15
                ease 0.8*panic_mod zoom base_zoom + .07
                ease 0.8*panic_mod zoom base_zoom + .12
                repeat

    show d4_sk_katya_blood_animation:
        align (.5, 1.)
        zoom 1.2

    show d4_blood_blink

    with Dissolve(.5)

    play test_three "voice/anton/4day/13 Pih5.ogg"
    "Я тянул Катю на себя и чувствовал, что проигрываю."

    window hide
    scene d4_sk_katya_fail:
        align (.5, 0.)
        zoom 1.1

        parallel:
            linear .5 yalign 1. blur 16
        parallel:
            linear .05 xoffset 5
            linear .05 xoffset -5
            repeat

    pause .5

    scene d4_sk_bg
    $ puz = puzKatya(win_lbl = "sK2_good", lose_lbl = "sK2_bad", settings = SK_hard_mode)
    call screen saveKatya(puz)
    jump expression _return



label sK2_good:
    $ Flags.Raise("help")
    jump d4_save_katya_after

label sK1_bad:
    $ sk_fail_disp = "d4_sk_katya_struggle_2"
    $ SceneFlags.Raise("fail on first")
    jump sK_fail_end

label sK2_bad:
    $ sk_fail_disp = "d4_sk_katya_struggle_4"
    jump sK_fail_end

label sK_fail_end:

    scene d4_sk_bg
    show d4_sk_fg:
        linear .03 xoffset 5
        linear .03 xoffset -5
        repeat

    show d4_sk_blink

    show expression sk_fail_disp behind d4_sk_fg:
        anchor (.5, .5)
        xpos 1000
        ypos 695

        .5
        easeout_quad 2. ypos 1000

    $ renpy.pause(2.5, hard=True)

    show d4_sk_katya_fail_blood_animation behind d4_sk_fg:
        anchor (.5, .5)
        xpos 1000
        ypos 595

    $ renpy.pause(3., hard=True)

    jump d4_save_katya_after



label d4_save_katya_after:
    $ story_manager.MarkEvent(("day4", "scene_garage2"))
    scene bg_black
    $ renpy.pause(1., hard=True)

    window hide
    scene bg_black
    $ renpy.pause(1., hard=True)

    $ panic_mod = .75
    $ base_zoom = 1.1
    $ xal_mod = -0.2

    if not SceneFlags.Has("fail on first"):
        scene d4_sk_katya_fail2:
            align (.5, 1.)
            zoom base_zoom
            parallel:
                linear .05 xoffset 5
                linear .05 xoffset -5
                repeat
            parallel:
                blur 8
                .5
                linear .5 yalign .3 blur 0
                block:
                    parallel:
                        ease 1.0*panic_mod xalign 0.3 + xal_mod
                        ease 1.0*panic_mod xalign 0.9 + xal_mod
                        ease 1.0*panic_mod xalign 0.5 + xal_mod
                        ease 0.2*panic_mod xalign 0.7 + xal_mod
                        ease 0.2*panic_mod xalign 0.3 + xal_mod
                        ease 1.0*panic_mod xalign 0.9 + xal_mod
                        ease 1.0*panic_mod xalign 0.5 + xal_mod
                        ease 1.0*panic_mod xalign 0.7 + xal_mod
                        repeat
                    parallel:
                        ease 0.8*panic_mod yoffset -0
                        ease 0.8*panic_mod yoffset -75
                        ease 0.8*panic_mod yoffset -25
                        ease 0.8*panic_mod yoffset -125
                        ease 0.2*panic_mod yoffset -75
                        ease 0.8*panic_mod yoffset -0
                        repeat
                    parallel:
                        pause 2.0*panic_mod
                        ease 0.2 blur 8
                        ease 0.2 blur 0
                        repeat

                    parallel:
                        ease 0.8*panic_mod zoom base_zoom + .05
                        ease 0.8*panic_mod zoom base_zoom + .15
                        ease 0.8*panic_mod zoom base_zoom + .07
                        ease 0.4*panic_mod zoom base_zoom + .12
                        ease 0.4*panic_mod zoom base_zoom + .05
                        ease 0.8*panic_mod zoom base_zoom + .15
                        ease 0.8*panic_mod zoom base_zoom + .07
                        ease 0.8*panic_mod zoom base_zoom + .12
                        repeat

        play test_six "sounds/sfx_meat_grinder_intense_2.ogg"

        show d4_sk_katya_blood_animation:
            subpixel True
            align (.5, 1.)
            zoom 2.
    else:

        scene d4_sk_katya_fail_first_bg
        show d4_sk_katya_fail_first_machine zorder 2:
            align (.0, .5)
            zoom 1.01
            block:
                linear .03 xoffset 5 yoffset 5
                linear .03 xoffset -5 yoffset -5
                repeat
        show d4_sk_katya_fail_first_kate:
            parallel:
                linear .03 xoffset 5 yoffset 5
                linear .03 xoffset -5 yoffset -5
                repeat
            parallel:
                linear 120 xpos -1000 ypos 1000

        show d4_sk_katya_blood_animation:
            subpixel True
            transform_anchor True
            anchor (.5, 1.)
            pos (.5, 1.)
            rotate 45
            zoom 2.


    show d4_blood_blink zorder 10

    pause 1.5
    window show

    play test_two "voice/kate/110 Vsh5.ogg"
    "Лезвия раздробили таз. Запенилась кровавая каша."
    "Катя выла на одной безумной ноте."
    play test_three "voice/anton/4day/13 Pih0.ogg"
    "Глаза вылезли из орбит и белки стали красными от лопнувших сосудов. Лезвия дошли до живота."

    play test_six "sounds/sfx_meat_grinder_intense_1.ogg"

    "Легко выгребли из плоти сизые трубки кишечника."
    "Так Оля наматывала спагетти на вилку. Вонь внутренностей распространилась по гаражу."
    play test_two "voice/kate/110 Vsh6.ogg"
    "Я больше не пытался помочь Кате – в этом не было ни малейшего смысла."
    "Голова одноклассницы свободно болталась. Мутные глаза смотрели в пустоту." id d4_save_katya_after_dd0bd106
    "Мясорубка перегрызла рёбра и поглотила грудь девочки." id d4_save_katya_after_c94714f8
    "От кровяного давления лицо Кати потемнело. Алые струйки сочились из глаз и ушей."

    if not SceneFlags.Has("fail on first"):
        scene d4_blood_bg:
            align (.5, .5)
            zoom 1.5
            parallel:
                linear 15 zoom 1.01
            parallel:
                linear .03 xoffset 5
                linear .03 xoffset -5
                repeat

        show d4_blood_body:
            xalign .5
            yalign 1.
            xoffset 300
            ypos 1080 + 10 + 300
            parallel:
                linear 15 zoom 1.1
            parallel:
                ease .25 yoffset 3
                ease .25 yoffset -3
                repeat

        show d4_blood_head:
            xalign .5
            yalign 1.
            xoffset 300
            ypos 1080 + 10 + 300
            parallel:
                linear 15 zoom 1.1
            parallel:
                ease .25 yoffset -10
                ease .25 yoffset 10
                repeat

        show d4_blood_blink

        with Dissolve(.5)
    "Катя умерла, но механизм продолжал работу."

    play test_six "sounds/sfx_meat_grinder_intense_1.ogg"

    "Волосы попали в лезвия, и скальп с сочным хлюпаньем отделился от черепа."

    play test_seven "sounds/sfx_blood_splatter.ogg"

    "Кожа лица съехала вниз, гримаса смерти заставила меня отшатнуться."

    $ renpy.music.set_volume(0.3, delay=3.5, channel="sound")

    "Я ощутил руки на своём теле и решил, что сейчас меня швырнут в раструб в качестве десерта."
    "Что я смешаюсь в единый фарш с Катей."
    "Но это Рома тащил меня прочь."

    scene d4_poddon 1:
        align (.5, .5)
        zoom 1.02

        linear .04 yoffset 3
        linear .04 yoffset -3
        repeat

    show d4_poddon_blink
    with Dissolve(.5)



    play test_four "sounds/loop_meat_grinder_idle.ogg" fadein 9 loop
    play test_five "sounds/loop_meat_grinder_grind.ogg" fadein 15 loop
    "Из металлического хобота механизма шлёпалась в поддон толстая колбаса-кровянка с застрявшими волосами и костями."


    if Flags.Has("help"):
        $ story_manager.MarkEvent(("day4", "game katya", "save"))
        $ music_during_lines = 0.7
        voice "voice/romka/4day/250 Mi.ogg"
        Rom "Мы сделали всё, что могли..."


        $ achievement_grant("ach_strawberry")

        voice "voice/romka/4day/197 N.ogg"
        Rom "Надо убираться отсюда."

        stop sound fadeout 5
        $ renpy.music.set_volume(1.0, delay=3.5, channel="test_four")
        stop test_five fadeout 3.5 


        if Flags.Has("polaroid"):
            $ story_manager.MarkEvent(("day4", "game katya", "photo"))
            $ Flags.Raise("photo")
            scene bad_mask_bg
            show d4_sk_blink zorder 1
            with Dissolve(.5)
            "Ледяными пальцами я расстегнул молнию на рюкзаке."
            voice "voice/romka/4day/198 Ti.ogg"
            Rom "Ты свихнулся?"
            show d4_blood_polaroid 1:
                alpha 0
                align (.5, 1.)
                yoffset 50
                linear .5 yoffset 0 alpha 1
                block:
                    ease 2. xoffset -10 yoffset 0
                    ease 2. xoffset 0 yoffset 10
                    ease 2. xoffset 10 yoffset -10
                    repeat

            "Я поднял «Полароид». Рукавом вытер слёзы."
            $ music_during_lines = 0.5
            voice "voice/anton/4day/14 Nam.ogg"
            Ant "Нам нужны доказательства."
            show d4_blood_polaroid 2 with Dissolve(.5)
            "Лезвия дожёвывали кости."
            "На одном из стальных зубов повисла отхваченная косичка."
            "Я прицелился, поймал в объектив резинку с пластмассовой клубничкой."

            window hide
            $ data = PhotoData(child = "d4_help_bg", next_label = "d4_garage_photo")
            $ photo = PhotoEngine(data, (750, 800))

            call screen d4_make_photo(photo)

            label d4_garage_photo:


            play sound "sounds/curtain-3.ogg"

            scene bg_white onlayer overlay
            with None
            hide screen d4_make_photo
            scene d4_help_after_bg:
                align (.5, .5)
                zoom 1.01
                block:
                    linear .03 xoffset 3
                    linear .03 xoffset -3
                    repeat
            show d4_help_after_skalp:
                align (.5, .5)
                zoom 1.01
                block:
                    linear .03 xoffset 3
                    linear .03 xoffset -3
                    repeat
            with Dissolve(1.5)
            window show                    

            "Клац."
            hide d4_help_after_skalp
            with Dissolve(.5)
            pause .5
            scene d4_help_after_bg:
                align (.5, .5)
                zoom 1.01
            with Dissolve(.5)


            $ achievement_grant("ach_secret")

            show d4_photo:
                subpixel True
                ypos 100
                xpos 550
                parallel:
                    linear .5 xpos 500 ypos 0
                parallel:
                    ease 1 xoffset -5*2 yoffset 0
                    ease 1 xoffset 5*2 yoffset -5*2
                    ease 1 xoffset 0 yoffset 5*2
                    ease 1 xoffset 5*2 yoffset 0
                    repeat
            with Dissolve(.5)

            "Коса отправилась в нутро мясорубки. И махина замерла, булькнув напоследок."

            stop test_four fadeout 3
    else:


        $ story_manager.MarkEvent(("day4", "game katya", "fail"))
        $ music_during_lines = 0.7
        voice "voice/romka/4day/194 Ka.ogg"
        Rom "Какого хрена ты стоял, как вкопанный?!"
        voice "voice/romka/4day/195 m.ogg"
        Rom "Мы же могли успеть её спасти..."
        voice "voice/romka/4day/196 V.ogg"
        Rom "Вот уж не думал, что ты её так сильно ненавидел."


        $ achievement_grant("ach_meat")

        voice "voice/romka/4day/197 N.ogg"
        Rom "Надо убираться отсюда."
        $ music_during_lines = 1.0

        stop sound fadeout 5
        stop test_four fadeout 5
        stop test_five fadeout 5 

    scene d4_garage_in 5:
        align (.5, .5)
        zoom 1.05
        linear 1. zoom 1.0
    show d4_garage_canvas zorder 3:
        align (.5, .5)
        zoom 1.05
        linear 1. zoom 1.0

    if Flags.Has("photo"):
        show d4_garage_grinder zorder 2:
            align (.5, .5)
            zoom 1.05
            linear 1. zoom 1.0
    else:
        show d4_garage_grinder zorder 2:
            align (.5, .5)
            zoom 1.05
            parallel:
                linear 1. zoom 1.0
            parallel:
                linear .03 xoffset 2
                linear .03 xoffset -2
                repeat
    show d4_poddon_blink_nosfx zorder 3

    show d4_garage_gate zorder 4:
        alpha 0
        align (.5, .5)
        zoom 1.5
        linear 1. zoom 1. alpha 1
    show blizzard_d4_evening2_big zorder 5:
        alpha 0
        linear 1. alpha 1
    show blizzard_d4_evening_face zorder 5:
        alpha 0
        linear 1. alpha 1
    with Dissolve(.5)


    stop music fadeout 3.5

    "Мы вывалились из гаража."

    scene d4_forest_snow:
        yalign 1.
    show half_shadow
    show incar_snow_up onlayer master1
    with Dissolve(.5)

    stop test_four fadeout 6
    $ renpy.music.set_volume(1.0, delay=4, channel="test_one")
    $ renpy.music.set_volume(1.0, delay=4, channel="fon")
    play sound "sounds/sfx_snow_dig_eat.ogg"

    play test_two "voice/anton/4day/15 Zr.ogg"
    "Я взял горсть снега и запихнул себе в рот. Прожевал рыхлую субстанцию."
    play test_six "voice/romka/4day/199 B.ogg"
    "Рома стоял на коленях, утирая лицо снежком."

    play test_three "sounds/loop_snow_crawl_Anton.ogg" fadein 0.8 loop

    $ step_in = .2
    $ step_in_t = .5
    $ step_back = .03
    $ step_back_t = .25
    scene d4_forest_snow:
        yalign 1.
        ease step_in_t yalign 1. - step_in * 1
        ease step_back_t yalign 1. - step_in * 1 + step_back
        .5
        ease step_in_t yalign 1. - step_in * 2
        ease step_back_t yalign 1. - step_in * 2 + step_back
        .5
        ease step_in_t yalign 1. - step_in * 3
        ease step_back_t yalign 1. - step_in * 3 + step_back
        .5
        ease step_in_t yalign 1. - step_in * 4
        ease step_back_t yalign 1. - step_in * 4 + step_back
        .5
        ease step_in_t yalign 1. - step_in * 5
        ease step_back_t yalign 1. - step_in * 5 + step_back
        .5
    show half_shadow

    stop test_one fadeout 12

    $ renpy.start_predict("d4_poddon animation_memory")
    $ story_manager.MarkEvent(("day4", "scene_v8"))
    play test_two "voice/anton/4day/16 Polz.ogg"
    "Я отползал от чудовищной мясорубки, цепляясь ногтями за лёд."
    "Кашлял, точно пытался отхаркнуть воспоминания об увиденном."

    stop test_three fadeout 1.5

    scene d4_gorelnik_wide_blink:
        xalign 1.
    show d4_gorelnik_fg zorder 1:
        xpos -350

    if Flags.Has("myth4"):
        show d4_myth:
            xalign 1.

    hide incar_snow_up onlayer master1
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    with Dissolve(.5)
    play music "music/Broken Thoughts.ogg" volume 0.8 fadein 0.5
    "Но я знал, что никогда не забуду ни запаха, ни звука ломающихся костей, ни предсмертной агонии Кати."

    play sound "sounds/sfx_crawl_snow.ogg"

    show Romka Blood m_night_winter 00 with Dissolve(.5):
        align (.5, 1.)
        xoffset 250
        yoffset 50
        zoom .80
        .5
        ease .5 zoom .92 yoffset 40 xoffset 225
        ease .25 zoom .90 yoffset 50
        .5
        ease .5 zoom 1.02 yoffset 40 xoffset 200
        ease .25 zoom 1.00 yoffset 50
    "Рома пополз ко мне на четвереньках, и на секунду я решил, что он потерял рассудок от ужаса."
    "И теперь, как дикий зверёныш, перегрызёт мне глотку."

    stop sound fadeout 1
    play test_one "sounds/sfx_grab_hand.ogg"

    show Romka Blood m_night_winter 00:
        ease .1 xoffset 205
        ease .1 xoffset 195
        repeat 2
    pause .5

    play sound "sounds/sfx_coat_snow_rub.ogg"

    show Romka Blood m_night_winter 01 norm ahead 01 zorder 2 with Dissolve(.5)
    "Но он взял меня за куртку и принялся снегом оттирать красные капли с рукава."
    $ music_during_lines = 1.0
    voice "voice/anton/4day/17 Chto.ogg"
    Ant "Что ты делаешь?"
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/200 N.ogg"
    Rom "Никто не должен узнать."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    voice "voice/anton/4day/Ochem.ogg"
    Ant "О чём ты?"
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/201 N.ogg"
    Rom "Никакой милиции, слышишь?"
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/202 Ka.ogg"
    Rom "Катю по частям мы не соберём."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/203 A.ogg"
    Rom "А я не хочу сесть в тюрьму, как мой батя."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    voice "voice/anton/4day/18 no.ogg"
    Ant "Но ты говорил..."
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/204 G.ogg"
    Rom "Говорил-говорил."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    "Он метнул ненавидящий взгляд в Гараж."
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/205 Ya.ogg"
    Rom "Я включил мясорубку."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    voice "voice/anton/4day/19 Nech.ogg"
    Ant "Нечаянно!"
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/206 Pop.ogg"
    Rom "Попробуй докажи."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/207Em.ogg"
    Rom "Им только и надо, чтоб на кого-то повесить убийства."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/208Ya.ogg"
    Rom "Я за решётку пойду, а маньяк будет разгуливать на свободе."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/209 Bl.ogg"
    Rom "Блядь! А жизнь ведь только начала налаживаться!.."
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    voice "voice/anton/4day/20 No.ogg"
    Ant "Но мы не можем просто так..."
    show Romka Blood m_night_winter 01 norm ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/210 M.ogg"
    Rom "Можем! Поклянись, что никому не скажешь!"
    show Romka Blood m_night_winter 01 norm ahead 01 with Dissolve(.2)
    "«А иначе» он не произнёс, но это читалось в его тоне."

    show bg_black as flashback zorder 10 with Dissolve(.5):
        1.
        "d4_poddon animation_memory"
    show Romka Evil m_night_winter 04 normal ahead 03:
        xoffset 300
        yoffset 50
        align (.5, .5)
        zoom 1.5
        xzoom -1
    play test_six "music/Phrases_03.ogg"
    "Я молчал минуту, думая о кровавом бульоне, льющемся из махины."
    "Рома был прав."
    "Даже если Тихонов поверит нам, Гараж к тому времени может исчезнуть."
    "Чудесным образом перенестись на другую поляну в другую часть этого чёртового леса."
    hide flashback
    $ renpy.stop_predict("d4_poddon animation_memory")
    show Romka Evil m_night_winter 04 normal ahead 04
    with Dissolve(.2)
    voice "voice/romka/4day/212 Po.ogg"
    Rom "Пожалуйста."
    show Romka Evil m_night_winter 04 normal ahead 03 with Dissolve(.2)
    show Romka Evil m_night_winter 04 normal ahead 04 with Dissolve(.2)
    voice "voice/romka/4day/213 Kt.ogg"
    Rom "Кто-то должен защищать Полину."
    show Romka Evil m_night_winter 04 normal ahead 03 with Dissolve(.2)
    "«И Олю», - подумал я, медленно кивая."
    voice "voice/anton/4day/21 Horo.ogg"
    Ant "Хорошо."
    "Я боялся, что не сдержу слово."

    $ renpy.music.set_volume(1.0, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 0.2
    $ renpy.music.set_pan(0.5, delay=2, channel="sound")

    scene d4_gorelnik_wide_blink as bg1:
        xalign 1.
    if Flags.Has("myth4"):
        show d4_myth as mmyth1:
            xalign 1.
    show d4_gorelnik_fg as fg1 zorder 1:
        xpos -350
    show Romka Evil m_night_winter 04 normal ahead 03:
        xoffset 300
        yoffset 50
        xzoom -1

        pause .75

        "Romka Evil m_night_winter 04 normal aside 03"

        parallel:
            linear 1. xoffset 500
        parallel:
            easein .25 yoffset 30
            easeout .25 yoffset 50
            repeat 4

    show d4_gorelnik_wide_blink as bg2:
        xalign 1.
        alpha 0
        1.5
        linear .25 alpha 1

    if Flags.Has("myth4"):
        show d4_myth as mmyth2:
            xalign 1.
            alpha 0
            1.5
            linear .25 alpha 1

    show d4_gorelnik_fg as fg2 zorder 1:
        xpos -350
        alpha 0
        1.5
        linear .25 alpha 1

    show layer master1:
        blur 0

    show blizzard_d4_evening2_far onlayer master1
    show blizzard_d4_evening2_near onlayer master1
    show blizzard_d4_evening2_big onlayer master1

    with Dissolve(.5)

    stop sound fadeout 1.5
    "Что мама прочтёт всё на моём лице, увидит нестёртые капли крови, унюхает запах."
    "И я расколюсь, просто упаду перед ней на пол и буду рыдать от страха за себя и за родных."
    "Я ещё не знал, что ждёт меня в месте, которое я по ошибке называл домом."

    $ renpy.music.set_pan(0.0, delay=0, channel="sound")
    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.4

    jump d4_garage_home_transition

label d4_garage_home_transition:
    window hide    
    scene d4_gorelnik_wide:
        xalign 1.
        linear 6 xalign 0.

    if Flags.Has("myth4"):
        show d4_myth:
            xalign 1.
            linear 6 xalign 0.

    show d4_gorelnik_fg:
        xpos -350
        ypos 1080
        anchor (.0, 1.)
        linear 6 xpos 1260

    pause 1.
    show d4_bg_house_night_4:
        alpha 0
        .25
        alpha 1
    show snow_day_4:
        alpha 0
        .25
        alpha 1

    show perehod zorder 10:
        yalign 1.
        alpha 1
        xalign 1.5
        linear .25 xalign .5
        linear .25 xalign -1.
        alpha 0.

    hide blizzard_d4_evening2_far onlayer master1
    hide blizzard_d4_evening2_near onlayer master1
    hide blizzard_d4_evening2_big onlayer master1

    stop sound fadeout 2
    stop music fadeout 3
    jump d4_home



label show_d4_dep_board:
    scene d4_dep_board
    if Flags.Has("witness"):
        show d4_dep_board_witness
    show layer master:
        align (.5, .5)
        zoom 1.05
    return
label dev_d4_police hide:
    scene bg_black














    menu:
        "ДОБРОВОЛЬНАЯ ЯВКА":
            call d4_police_entry from _call_d4_police_entry_2
            jump d4_police_voluntary
        "ПОД ДУЛОМ ПИСТОЛЕТА":
            call d4_police_entry from _call_d4_police_entry_3
            jump d4_police_forced


label d4_police_entry:

    $ Flags.Raise("police")

    window hide

    pause 1


    play sound "sounds/sfx_door_police_station_open_1.ogg"
    play music2 "music/9_Nikita Kryukov - the Obscurity.ogg" fadein 2 

    play fon "sounds/ambience_police_station.ogg" fadein 2 loop
    play test_six "sounds/loop_clock_room.ogg" fadein 2 loop

    scene police_station
    show police_01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near
    show blizzard_d4_evening_big
    with Dissolve(1.)
    pause 1.5
    scene d4_dep_bg
    show d4_dep_door
    with Dissolve(.5)

    play sound "sounds/sfx_door_police_station_close.ogg"

    hide d4_dep_door
    with Dissolve(.5)
    window show


    $ achievement_grant("ach_cops")

    $ add_text_to_dictionary(40)
    "В дежурной части почему-то пахло {u}чебуреками{/u} вперемешку с сигаретным дымом."
    "Из глубин участка приглушённо и тоскливо пела Татьяна Буланова."
    "Казалось, под такие слезливые песни невозможно работать — только отпевать покойников у разрытой могилы."


label d4_police_lookaround:
    $ story_manager.MarkEvent(("day4", "la police"))
    $ SceneFlags.Reset()
    label d4_police_lookaround.main:
        window hide
        call screen day4_police_observe

    label d4_police_lookaround.cage:
        $ story_manager.MarkEvent(("day4", "la police", "cage"))
        if SceneFlags.Seen("cage"):
            "«Обезьянник»."
        else:
            play sound "sounds/sfx_cell_lock.ogg"
            "Как-то раз папа упоминал при мне «обезьянник» — камеру, где держат только что пойманных преступников."
            "Толстые прутья решётки выглядели устрашающе, прямо как в кино. Мне даже захотелось нарисовать это место. На секунду я представил, кого бы мог изобразить внутри клетки. "
            "На ум сразу пришёл Ромка. Надо сказать, он отлично бы сюда вписался!"

            $ true_detective_count4 += 1
        jump d4_police_lookaround.main

    label d4_police_lookaround.mask:
        $ story_manager.MarkEvent(("day4", "la police", "mask"))
        if SceneFlags.Seen("mask"):
            "Противогаз."
        else:
            play sound "sounds/sfx_gas_mask.ogg"
            "На спинке стула висел старый противогаз с хоботом. Здорово, что в милиции не забывают про тренировки! Только вот почему фильтра не видно?"
            "Или противогаз здесь используют для чего-то другого?.."

            $ true_detective_count4 += 1
        jump d4_police_lookaround.main


label d4_police_followup:
    show bg_black

    hide bg_black

    call show_d4_dep_board from _call_show_d4_dep_board
    with Dissolve(.5)

    "Я мотнул головой, отгоняя мрачные мысли. Стянул шапку и провёл пятернёй по взъерошенным волосам."
    "Снег оттаивал с подошв, оставляя на плитке мокрые следы."

    "Громко тикали часы, а со стенда «Внимание! Розыск» на нас глядели сгинувшие в ночи дети."
    if Flags.Has("witness"):
        "Среди ксерокопий преступников был нарисованный мной фоторобот."
    elif not Flags.Has("silent"):
        "Среди ксерокопий преступников не было нарисованного мной фоторобота."
    return


label d4_police_voluntary:
    $ story_manager.MarkEvent(("day4", "scene_police_a"))
    play sound "sounds/sfx_footsteps_Tihonov_2.ogg"
    pause .8

    scene d4_dep_bg
    show Romka Normal m_day_winter 00 norm ahead 01:
        xoffset 400
        yoffset 10
        zoom .85
        align (.5, 1.)
    show Tihonov Norm m_day_winter 00 good ahead 00:
        xoffset -500
        yoffset 15
    with Dissolve(.5)

    window show
    show Tihonov Norm m_day_winter 01 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/68 Ba.ogg"
    Tikhonov "Ба, какие люди!"
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/69 Chto.ogg"
    Tikhonov "Что, Пятифанов, сдаваться пришёл? С повинной?"
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)

    show Romka Normal m_day_winter 00 norm aside 03 with Dissolve(.15)
    voice "voice/romka/4day/179 o.ogg"
    Rom "Обхохочешься..."
    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/70 Da.ogg"
    Tikhonov "Да уж, смешного мало."
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    "Милиционер перевёл тяжёлый взгляд на меня."
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/13 T.ogg"
    Tikhonov "Ты бы, Петров, друзей осторожнее выбирал, а то, считай, знакомы всего ничего, а ты уже дров наломал."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/14 Na.ogg"
    Tikhonov "На учёт поставлю, как некоторых..."
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.5)

    voice "voice/romka/4day/148 O.ogg"
    Rom "Ой, знаем мы ваши учёты: лишь бы отчётность закрыть."
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)
    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/149 A.ogg"
    Rom "А настоящие преступники до сих пор на свободе!"
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)

    show Tihonov Norm m_day_winter 00 gloomy aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/15 No.ogg"
    Tikhonov "Но-но!"
    show Tihonov Norm m_day_winter 00 gloomy aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 gloomy aside 02 with Dissolve(.15)
    voice "voice/tihonov/4day/16 Sm.ogg"
    Tikhonov "Смотри! Не образумишься — как папаша твой, по малолетке загремишь." id d4_police_voluntary_e62dc1ec
    show Tihonov Norm m_day_winter 00 gloomy aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 angry aside 04 with Dissolve(.5)
    voice "voice/romka/4day/150 A.ogg"
    Rom "Я вас ещё удивлю!"
    show Romka Angry m_day_winter 01 angry aside 03 with Dissolve(.15)

    "Я понял, что пора вмешаться в разговор, пока Тихонов не потерял терпение."

    show Tihonov Norm m_day_winter 00 gloomy ahead 00 with Dissolve(.15)
    voice "voice/anton/4day/05 Ko.ogg"
    Ant "Константин Владимирович, вы должны поехать с нами!"

    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.5)
    voice "voice/anton/4day/06 M.ogg"
    Ant "Мы гараж нашли."
    "Я заранее догадался, какой будет ответная реакция."
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/75 Von.ogg"
    Tikhonov "Вон как! Гараж, значит."
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    $ add_text_to_dictionary(41)
    voice "voice/tihonov/4day/76 Da.ogg"
    Tikhonov "Дай угадаю: а в нём сокровища {u}Стеньки Разина{/u} спрятаны?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    voice "voice/anton/4day/78. Net.ogg"
    Ant "Нет, но..."
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/22 Pe.ogg"
    Tikhonov "Петров-Петров... Признавайся, ведь не сам ты это придумал?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/23 P.ogg"
    Tikhonov "Пятифанов подговорил, да? Всё хиханьки да хаханьки."
    show Tihonov Norm m_day_winter 01 gloomy aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.5)
    play test_six "voice/romka/4day/151 O.ogg"
    "Ромка закатил глаза."
    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/180 Ya.ogg"
    Rom "Я предупреждал..."
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)

    voice "voice/anton/4day/79. Nek.ogg"
    Ant "Никто меня не подговаривал!"
    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.5)
    voice "voice/anton/4day/Yasam.ogg"
    Ant "Я сам видел! Как вас вижу! В лесу, среди пней..."

    show Tihonov Norm m_day_winter 01 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/79 Vr.ogg"
    Tikhonov "Времянка это была, Антон."
    show Tihonov Norm m_day_winter 01 good ahead 00 with Dissolve(.15)
    voice "voice/anton/4day/07 Ne.ogg"
    Ant "Нет! Гараж!"
    "Старлей примирительно поднял руки."
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/80 Ti.ogg"
    Tikhonov "Ты хоть знаешь, что такое времянка?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)

    voice "voice/anton/4day/08 Nu.ogg"
    Ant "Ну... Это..."

    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/81 Ne.ogg"
    Tikhonov "Не знаешь! Как же ты их тогда отличишь?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/82 Oh.ogg"
    Tikhonov "Охотники хибару сколотили для припасов."
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/83 Mi.ogg"
    Tikhonov "Мы этих построек штук десять проверили, пока лес обыскивали."
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/84 E.ogg"
    Tikhonov "И вашу, наверное, тоже шмонали... Проверяли то есть."
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)

    voice "voice/anton/4day/09 Hi.ogg"
    Ant "Хибары не едят детей! А Чёрный Гараж ест!"
    play test_one "sounds/Garage.ogg"
    stop music2 fadeout 3.5

    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/85 Ch.ogg"

    Tikhonov "Чёрный?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    play sound "sounds/sfx_footsteps_Tihonov_2.ogg"

    show Tihonov Norm b_day_winter 00 good aside 00 with Dissolve(.5):
        xoffset -200
    play test_four "sounds/sfx_fingers_drumming.ogg"
    "Он крепко задумался, барабаня пальцами по столешнице с кипой бумаг."
    "У меня появилась слабая надежда, что лейтенант прислушается к моим словам."

    show Tihonov Norm b_day_winter 00 good aside 01 with Dissolve(.15)
    play test_four "music/Tension Suspense Risers_06.ogg" fadein 1 volume 0.5
    voice "voice/tihonov/4day/86 Na.ogg"
    Tikhonov "На чёрной-чёрной улице... В чёрной-чёрной подворотне..."

    show Tihonov Norm b_day_winter 00 good aside 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/87 Che.ogg"
    Tikhonov "Чёрный-пречёрный гараж..."
    show Tihonov Norm b_day_winter 00 good aside 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    pause .25

    show Tihonov Norm b_day_winter 00 good ahead 02

    show layer master:
        align (.35, .5)
        zoom 1.1
        linear .15 zoom 1.0
    play test_two "sounds/Fail9.ogg"
    voice "voice/tihonov/4day/88 Hv.ogg"
    Tikhonov "Хвать тебя за шкирку!"
    show Tihonov Norm b_day_winter 00 good ahead 04 with Dissolve(.15)
    play test_five "sounds/Fail2.ogg" volume 0.5
    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.15)
    play test_six "voice/tihonov/4day/88 Heh.ogg" 
    voice "voice/romka/4day/181P.ogg"
    Rom "Приехали..."
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)

    show Tihonov Norm b_day_winter 00 good ahead 04:
        linear .2 yoffset 35
        linear .2 yoffset 15
        linear .2 yoffset 35
        linear .2 yoffset 15
        "Tihonov Norm b_day_winter 00 good ahead 05" with Dissolve(.15)
    voice "voice/tihonov/4day/89 He.ogg"
    Tikhonov "Хе-хе, видите? Не забыл я ещё детскую страшилку."
    show Tihonov Norm b_day_winter 00 good ahead 04 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 05 with Dissolve(.15)
    play test_six "sounds/Fail3.ogg" volume 0.5
    voice "voice/tihonov/4day/90 Po.ogg"
    Tikhonov "Помню, малым так сестрёнку напугал, гаражом этим. Три дня уснуть не могла, дурёха."
    play sound "sounds/sfx_footsteps_Tihonov_2.ogg"
    show Tihonov Norm b_day_winter 00 good ahead 04 with Dissolve(.15)

    show Tihonov Norm m_day_winter 00 good ahead 03 with Dissolve(.15):
        xoffset -500
    "Тихонов улыбнулся, блеснув крепкими зубами, а я подумал о своей Оле."

    show Tihonov Norm m_day_winter 00 good ahead 04 with Dissolve(.15)
    voice "voice/tihonov/4day/91 Ba.ogg"
    Tikhonov "Байка это, ребята. Ей сто лет в обед."
    show Tihonov Norm m_day_winter 00 good ahead 03 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good ahead 04 with Dissolve(.15)
    play test_six "music/Fail7.ogg" volume 0.5
    voice "voice/tihonov/4day/92 V.ogg"
    Tikhonov "Вы ещё своим детям рассказывать её будете, а те – своим."
    show Tihonov Norm m_day_winter 00 good ahead 03 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/93 Ne.ogg"
    Tikhonov "Некоторые истории... Особенно дурные... Они, увы, вечны."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)

    jump d4_police_common


label d4_police_forced:
    $ story_manager.MarkEvent(("day4", "scene_police_b"))
    scene d4_dep_bg
    play sound "<from 0 to 1>sounds/sfx_footsteps_Tihonov_2.ogg"
    show Romka Normal m_day_winter 00 norm ahead 01:
        xoffset 400
        yoffset 10
        zoom .85
        align (.5, 1.)
    show Tihonov Norm m_day_winter 00 good ahead 00:
        xoffset -500
        yoffset 15
    with Dissolve(.5)

    window show

    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/09 R.ogg"
    Tikhonov "Располагайтесь."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/10 Ati.ogg"
    Tikhonov "А ты куда, Пятифанов, присел? Тебя вон, персональное место в обезьяннике дожидается."
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)

    pause .25

    show Romka Normal m_day_winter 00 norm aside 03 with Dissolve(.25)
    voice "voice/romka/4day/147 A.ogg"
    Rom "А чё я сделал-то?"
    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.15)

    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/11 Na.ogg"
    Tikhonov "На офицера при исполнении с ножом напал."
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/12 Teb.ogg"
    Tikhonov "Тебе мало?"
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)

    pause .25

    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    "Милиционер перевёл тяжёлый взгляд на меня."
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/13 T.ogg"
    Tikhonov "Ты бы, Петров, друзей осторожнее выбирал, а то, считай, знакомы всего ничего, а ты уже дров наломал."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/14 Na.ogg"
    Tikhonov "На учёт поставлю, как некоторых..."
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.5)

    voice "voice/romka/4day/148 O.ogg"
    Rom "Ой, знаем мы ваши учёты: лишь бы отчётность закрыть."
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)
    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/149 A.ogg"
    Rom "А настоящие преступники до сих пор на свободе!"
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)

    show Tihonov Norm m_day_winter 00 gloomy aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/15 No.ogg"
    Tikhonov "Но-но!"
    show Tihonov Norm m_day_winter 00 gloomy aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 gloomy aside 02 with Dissolve(.15)
    voice "voice/tihonov/4day/16 Sm.ogg"
    Tikhonov "Смотри! Не образумишься — как папаша твой, по малолетке загремишь." id d4_police_forced_e62dc1ec
    show Tihonov Norm m_day_winter 00 gloomy aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 angry aside 04 with Dissolve(.5)
    voice "voice/romka/4day/150 A.ogg"
    Rom "Я вас ещё удивлю!"
    show Romka Angry m_day_winter 01 angry aside 03 with Dissolve(.15)

    show Tihonov Norm m_day_winter 01 somber aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/17 Pa.ogg"
    Tikhonov "Пасть закрой!"
    show Tihonov Norm m_day_winter 01 somber aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 somber aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/18 Ot.ogg"
    Tikhonov "Отвечайте, что в лесу делали в комендантский час?"
    show Tihonov Norm m_day_winter 01 somber aside 00 with Dissolve(.15)
    voice "voice/anton/4day/77. Ko.ogg"
    Ant "Константин Владимирович, мы Катю искали..."
    show Tihonov Norm m_day_winter 01 somber ahead 00 with Dissolve(.15)
    "Я заранее догадался, какой будет ответная реакция."
    show Tihonov Norm m_day_winter 01 gloomy ahead 04 with Dissolve(.15)
    voice "voice/tihonov/4day/19 Pom.ogg"
    Tikhonov "Помощнички выискались!"
    show Tihonov Norm m_day_winter 01 gloomy ahead 03 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 04 with Dissolve(.15)
    voice "voice/tihonov/4day/20 ta.ogg"
    Tikhonov "Такими темпами вас самих искать придётся!"
    show Tihonov Norm m_day_winter 01 gloomy ahead 03 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/21 V.ogg"
    Tikhonov "В газету захотели попасть? В рубрику «Помним, любим, скорбим»?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    voice "voice/anton/4day/78. Net.ogg"
    Ant "Нет, но..."
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/22 Pe.ogg"
    Tikhonov "Петров-Петров... Признавайся, ведь не сам ты это придумал?"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy aside 01 with Dissolve(.15)
    voice "voice/tihonov/4day/23 P.ogg"
    Tikhonov "Пятифанов подговорил, да? Всё хиханьки да хаханьки."
    show Tihonov Norm m_day_winter 01 gloomy aside 00 with Dissolve(.15)

    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.5)
    play test_six "voice/romka/4day/151 O.ogg"
    "Ромка закатил глаза."
    show Romka Angry m_day_winter 01 mad ahead 02 with Dissolve(.15)
    voice "voice/romka/4day/151Z.ogg"
    Rom "Завёл старую песню..."
    show Romka Angry m_day_winter 01 mad ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/79. Nek.ogg"
    Ant "Никто меня не подговаривал!"
    voice "voice/anton/4day/80. Yasam.ogg"
    Ant "Я сам хотел маньяка поймать."
    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.5)

    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/24 Eto.ogg"
    Tikhonov "Это вам повезло, что вы на меня наткнулись."
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 01 gloomy ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/25 A.ogg"
    Tikhonov "А я ведь предупреждал по-хорошему, чтобы ты дома сидел!"
    show Tihonov Norm m_day_winter 01 gloomy ahead 00 with Dissolve(.15)

    show Tihonov Norm m_day_winter 01 somber ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/26 Na.ogg"
    Tikhonov "На кой лад тебе этот маньяк вообще сдался?"
    show Tihonov Norm m_day_winter 01 somber ahead 00 with Dissolve(.15)
    "Я виновато опустил голову."
    voice "voice/anton/4day/80. Nag.ogg"
    Ant "Награду хочу."
    play sound "<from 0 to 1>sounds/sfx_footsteps_Tihonov_2.ogg"

    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15):
        xoffset -200

    play test_six "voice/tihonov/4day/27 Oi.ogg" 
    "Старлей скрестил руки на груди, тяжело вздохнув."
    show Tihonov Norm b_day_winter 00 good ahead 01
    show Romka Normal m_day_winter 00 norm ahead 01
    with Dissolve(.15)
    voice "voice/tihonov/4day/28 De.ogg"
    Tikhonov "Денег, значит. И куда тебе столько денег?"
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    voice "voice/anton/4day/81. U.ogg"
    Ant "У родителей долги..."
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/29 Da.ogg"
    Tikhonov "Да вся страна у нас в долгах как в шелках! И дальше что?"
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/30 Du.ogg"
    Tikhonov "Думаешь, твоя пропажа им поможет?"
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    queue sound [ "<silence 0.0>", "<from 0 to 1>voice/anton/2day/137. Ot zlosti i.ogg"]
    "Я хныкнул от обиды."
    voice "voice/anton/4day/01 Da.ogg"
    Ant "Да им уже ничего не поможет! Они дня без скандала прожить не могут!"
    voice "voice/anton/4day/02 Pro.ogg"
    Ant "Просто хочу, чтобы мы с Олей были счастливы."
    show Tihonov Norm b_day_winter 00 good aside 00 with Dissolve(.15)
    "Тихонов призадумался, барабаня пальцами по столешнице с кипой бумаг."
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/31 Ne.ogg"
    Tikhonov "Не плачь, пацан. Всё образуется."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/32 E.ogg"
    Tikhonov "И родители помирится, и маньяка найдём..."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Romka Angry m_day_winter 01 angry aside 04 with Dissolve(.5)
    queue sound [ "<silence 1.8>", "<from 0 to 2>music/caricature08.ogg"] volume 0.6 
    voice "voice/romka/4day/152 A.ogg"
    Rom "Ага, и страну поднимем."
    show Romka Angry m_day_winter 01 angry aside 03 with Dissolve(.15)
    play sound "<from 0 to 0.7>sounds/sfx_footsteps_Tihonov_2.ogg"

    show Tihonov Norm m_day_winter 00 somber aside 02 with Dissolve(.15):
        xoffset -500
    voice "voice/tihonov/4day/33 P.ogg"
    Tikhonov "Пятифанов, договоришься у меня!"
    show Tihonov Norm m_day_winter 00 somber aside 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.15)
    "Тихонов оскалился, блеснув крепкими зубами, а я подумал, что всё равно не отступлю. Ради своей Оли."
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/34 A.ogg"
    Tikhonov "Ай, чёрт с вами!"
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/35 W.ogg"
    Tikhonov "В этот раз устное предупреждение вам."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm m_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/36 No.ogg"
    Tikhonov "Но в следующий раз — пеняйте на себя."
    show Tihonov Norm m_day_winter 00 good ahead 00 with Dissolve(.15)

    show Tihonov Norm m_day_winter 00 somber ahead 00 with Dissolve(.15)
    "Он погрозил пальцем."
    show Tihonov Norm m_day_winter 00 somber ahead 02
    show Romka Angry m_day_winter 01 angry aside 01
    with Dissolve(.15)
    voice "voice/tihonov/4day/37U .ogg"
    Tikhonov "Увижу ещё раз, что в потёмках шароёбитесь, – уши откручу!"
    show Tihonov Norm m_day_winter 00 somber ahead 00 with Dissolve(.15)

    jump d4_police_common


label d4_police_common:
    $ story_manager.MarkEvent(("day4", "scene_police_2"))
    "В последний раз всхлипнула и замолчала Буланова. Наступила гробовая тишина."

    "Будто на автопилоте, я побрёл к стенду, оставляя за собой мокрые следы."
    play sound "<from 0 to 1>sounds/loop_footsteps_police_normal_one.ogg"

    call show_d4_dep_board from _call_show_d4_dep_board_1
    with Dissolve(.5)

    stop music2 fadeout 3
    "Я теперь стоял в упор, разглядывая фотографии Сенечки, Вовы, Семёна и Кати, а они в ответ таращились на меня."

    show layer master:
        align (.5, .5)
        zoom 1.05
        linear .05 yoffset 20
        linear .05 yoffset 0

    play sound "sounds/sfx_hand_shoulder_ment.ogg"
    "Когда рука Тихонова легла мне на плечо, я невольно вздрогнул."
    play sound "<from 0 to 1>sounds/sfx_footsteps_Tihonov_2.ogg"

    show d4_tihonov with Dissolve(.25)

    play music "music/Militsioner.ogg" volume 0.35 fadein 2
    voice "voice/tihonov/4day/38 Eh.ogg"
    Tikhonov "Эх, Антон. Знал бы ты, как часто я на них смотрю."

    scene d4_dep_bg
    show Romka Normal m_day_winter 00 norm aside 03:
        xoffset 400
        yoffset 10
        zoom .85
        align (.5, 1.)
    with Dissolve(.5)
    voice "voice/romka/4day/153 L.ogg"
    Rom "Лучше бы преступника ловили, а не на фотки пялились."
    "Я думал, Тихонов обозлится, но он проглотил колкость наглеца."

    call show_d4_dep_board from _call_show_d4_dep_board_2
    show d4_guard
    with Dissolve(.5)

    voice "voice/tihonov/4day/39 Po.ogg"
    Tikhonov "По-вашему, я не хочу на этого козла браслеты надеть?"
    voice "voice/tihonov/4day/40 Vz.ogg"
    Tikhonov "Взять под белы рученьки да к стенке поставить?"
    voice "voice/tihonov/4day/41 Da.ogg"
    Tikhonov "Да я с этой мыслью и спать ложусь, и просыпаюсь!"
    voice "voice/tihonov/4day/42 Zn.ogg"
    Tikhonov "Знаете, что мне снится ночами? Вам лучше и не знать."


    scene d4_dep_bg
    show Romka Normal m_day_winter 00 norm aside 01:
        xoffset 400
        yoffset 10
        zoom .85
        align (.5, 1.)
    with Dissolve(.5)

    play test_seven "sounds/sfx_footsteps_Tihonov_2.ogg"
    show Tihonov Norm m_day_winter 00 good aside 00 with Dissolve(.25):
        align (.5, 1.)
        xoffset -800
        yoffset 20

        parallel:
            linear 1 xoffset -500
        parallel:
            easein .25 yoffset 0
            easeout .25 yoffset 20
            repeat 2


    play test_six "voice/tihonov/4day/Vdoh.ogg" 
    stop test_five fadeout 0.6
    "Словно сгорбившись под весом тяжёлых мыслей, он медленно пошёл к столу и вздохнул."
    "Мы слушали молча."

    play sound "<from 0 to 1>sounds/sfx_footsteps_Tihonov_2.ogg"
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.5):
        xoffset -200
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)

    voice "voice/tihonov/4day/43 De.ogg"
    Tikhonov "Дело это – глухарь!"
    $ renpy.music.set_pause(True, channel=u'music')
    play music2 "music/44_Kontakt_2.ogg" fadein 2.5
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    play test_three "sounds/hit-chord-3.ogg"
    scene bg_white with Dissolve(.15)

    scene d4_station_memory
    show ramka zorder 5
    with Dissolve(.5)

    voice "voice/tihonov/4day/44 Na.ogg"
    Tikhonov "Нашли мы детские следы, ведущие в лес метров на пятьдесят. Да только там они и обрываются."

    show koshmar:
        alpha 0
        linear .5 alpha 1

    voice "voice/tihonov/4day/45 A.ogg"
    Tikhonov "А дальше сплошная чертовщина..."

    play sound "sounds/sfx_dogs_whining.ogg"

    voice "voice/tihonov/4day/46 Pr.ogg"
    Tikhonov "Привлекли кинологов. Но собаки след не берут — скулят только жалобно."

    show bg_lisa001:
        alpha 0
        linear .5 alpha 1
    voice "voice/tihonov/4day/47 S.ogg"
    Tikhonov "С добровольцами весь лес прочесали — ни единой зацепки."
    voice "voice/tihonov/4day/48 D.ogg"
    Tikhonov "Двадцать пять квадратных километров истоптали... Маньяк этот в норах звериных прячется, что ли?"

    show bg_lisa001:
        alpha 1
        linear .5 alpha 0
    voice "voice/tihonov/4day/49 A.ogg"

    play sound "sounds/sfx_laughter_kids_creepy.ogg"

    Tikhonov "А на днях кто-то из местных заявил, что слышит детский смех по ночам."
    voice "voice/tihonov/4day/50 M.ogg"
    Tikhonov "Мол, это пропавшие дети к нему с того света являются и в окошко заглядывают."
    voice "voice/tihonov/4day/51 S.ogg"
    Tikhonov "С ума все посходили, ну что тут взять!"
    stop music2 fadeout 2.5
    $ renpy.music.set_pause(False, channel=u'music')

    scene d4_dep_bg
    show Romka Normal m_day_winter 00 norm aside 01:
        xoffset 400
        yoffset 10
        zoom .85
        align (.5, 1.)
    show Tihonov Norm b_day_winter 00 good aside 00:
        align (.5, 1.)
        xoffset -200
        yoffset 20
    with Dissolve(.5)

    if Flags.Has("finger"):
        show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
        voice "voice/tihonov/4day/52 Es.ogg"
        Tikhonov "Ещё и улики таинственным образом пропадать стали."
        show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)

    "Лейтенант помассировал переносицу."
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/53 A.ogg"
    Tikhonov "А ведь такое в нашем посёлке не впервой..."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/54 Po.ogg"
    Tikhonov "Помню, лет тридцать назад был похожий случай: так же исчезали ребятишки."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/55 Ho.ogg"
    Tikhonov "Хоть на похитителя и не вышли, но всё же тогда следствие лучше сработало: двоих детей удалось спасти."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)
    show Tihonov Norm b_day_winter 00 good ahead 01 with Dissolve(.15)
    voice "voice/tihonov/4day/56 V.ogg"
    Tikhonov "Вот, сохранил на память с той поры."
    show Tihonov Norm b_day_winter 00 good ahead 00 with Dissolve(.15)

    play sound "sounds/sfx_note_1.ogg"

    "Милиционер бережно протянул мне пожелтевшее от времени объявление."
    call show_d4_dep_board from _call_show_d4_dep_board_3

    play test_six "sounds/sfx_turning_pages_1.ogg"
    show d4_guard
    show d4_dep_mail:
        subpixel True
        ypos 1000
        xpos -100
        linear 1 ypos 0

        block:
            linear 2. xoffset 5 yoffset 5
            linear 2. xoffset 0 yoffset 0
            linear 2. xoffset -5 yoffset 10
            linear 2. xoffset 0 yoffset 10
            repeat
    with Dissolve(.5)

    voice "voice/romka/4day/154 V.ogg"
    Rom "В смысле?"
    voice "voice/anton/4day/03 Ta.ogg"
    Ant "Так это были вы?"

    play sound "sounds/sfx_note_2.ogg"


    show d4_dep_mail:
        subpixel True
        xpos -100
        linear 1.5 ypos 100 alpha 0

    with Dissolve(.25)

    voice "voice/tihonov/4day/57 T.ogg"
    Tikhonov "Так точно."
    voice "voice/tihonov/4day/58 ya.ogg"
    Tikhonov "Я ведь в этот участок в первый раз в вашем возрасте попал."
    voice "voice/tihonov/4day/59 P.ogg"
    Tikhonov "Помню, зима была, метель..."
    voice "voice/tihonov/4day/61 No.ogg"
    Tikhonov "Но – вот дела – что со мной было, хоть убейте, не помню."
    voice "voice/tihonov/4day/61 Na.ogg"
    Tikhonov "Нашёл меня в тайге тогдашний участковый."
    voice "voice/tihonov/4day/62 Go.ogg"
    Tikhonov "Говорит, лежал я в отключке, весь в сосновых иголках..."

    play test_three "sounds/sfx_coat_rustle_1.ogg"
    hide d4_guard
    show d4_tihonov
    with Dissolve(.25)

    "Тихонов качнул головой, пребывая в тумане обрывочных воспоминаний."
    play test_three "sounds/sfx_coat_rustle_2.ogg"

    hide d4_tihonov
    show d4_guard
    with Dissolve(.25)

    voice "voice/tihonov/4day/63 Eto.ogg"
    Tikhonov "Это благодаря ему я это гиблое дело не бросаю."
    voice "voice/tihonov/4day/64 Do.ogg"
    Tikhonov "Долг мой — до правды докопаться."
    voice "voice/anton/4day/04 Viska.ogg"
    Ant "Вы сказали, что двоих спасли. А второй кто?"
    voice "voice/tihonov/4day/65 da.ogg"
    Tikhonov "Да в жизни не догадаешься! Второй, точнее, вторая..."
    play test_three "sounds/sfx_coat_rustle_1.ogg"

    hide d4_guard
    show d4_tihonov
    with Dissolve(.25)
    stop music fadeout 4
    "Тихонов не успел договорить."
    window hide

    scene d4_dep_bg:
        align (.5, .5)
        zoom 1.2
    show Tihonov Norm m_day_winter 02 good ahead 00:
        align (.5, 1.)
        yoffset 20
        zoom .95
        xzoom -1
    show Romka Normal m_day_winter 00 norm aside 01:
        align (.5, 1.)
        xoffset 600
        zoom .92
        yoffset 100
    with Dissolve(.5)

    show d4_dep_door:
        align (.5, .5)
        zoom 1.2
    with Dissolve(.5)

    $ renpy.music.set_pan(-0.35, delay=0, channel="sound")
    play test_two "sounds/steps/loop_footsteps_school_one.ogg" fadein 1

    show d4_pavlovna 1:
        xoffset -600
        yoffset 20
        parallel:
            linear 1 xoffset -500
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
    show Tihonov Norm m_day_winter 02 good aside 00
    with Dissolve(.5)

    hide d4_dep_door
    with Dissolve(.5)

    stop test_two fadeout 1.2

    window show
    play test_six "voice/lydia/4day/20 Pih.ogg"
    play music2 "music/3_trouble.ogg" fadein 1.5
    "Распахнулась дверь, и вместе с ветром в участок ввалилась запыхавшаяся Лилия Павловна."
    play test_six "voice/lydia/4day/21 Pih2.ogg"
    "Я подобрался от неожиданности, встал по стойке смирно, однако учительница вовсе нас не замечала."
    voice "voice/lydia/4day/22 Net.ogg"
    Lilia_P "Нет её! Не пришла!"

    show d4_pavlovna 2 with Dissolve(.25)

    voice "voice/lydia/4day/23 Vi.ogg"
    Lilia_P "Вы сказали, придёт, сказали, она у подружек, а её нет!"
    voice "voice/lydia/4day/24 Net.ogg"
    Lilia_P "Нет моей Катеньки..."

    show d4_pavlovna 3 with Dissolve(.25):
        block:
            linear .05 yoffset 6
            linear .05 yoffset 10
            repeat 6

        2.55
        repeat


    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.35)
    play test_six "voice/lydia/4day/25 Za.ogg"
    "Лилия Павловна заплакала навзрыд, прикрыв лицо руками. Мы с Ромкой быстро переглянулись."
    show Romka Normal m_day_winter 00 norm aside 01 with Dissolve(.35)

    show Tihonov Norm m_day_winter 02 good aside 01 with Dissolve(.25)
    voice "voice/tihonov/4day/66 Us.ogg"
    Tikhonov "Успокойтесь! Тише!"
    show Tihonov Norm m_day_winter 02 good aside 00 with Dissolve(.25)

    show d4_pavlovna 2 with Dissolve(.25)
    stop test_six
    voice "voice/lydia/4day/26 Da.ogg"
    Lilia_P "Да как же мне успокоиться?! Кровиночка моя..."

    play sound "sounds/sfx_hug_ment.ogg"

    show Tihonov Norm m_day_winter 02 good aside 00:
        xoffset 0
        yoffset 20
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
        parallel:
            linear .50 xoffset -100
    play test_six "voice/lydia/4day/25 Ri.ogg"
    "Лейтенант обнял Лилию Павловну за плечи и коротко мотнул головой в нашу сторону:"

    show Tihonov Norm m_day_winter 02 good ahead 00 with Dissolve(.25)
    show Tihonov Norm m_day_winter 02 good ahead 01 with Dissolve(.25)
    voice "voice/tihonov/4day/67 Br.ogg"
    Tikhonov "Брысь!"
    play test_six "voice/lydia/4day/25 Rid.ogg"
    show Tihonov Norm m_day_winter 02 good ahead 00 with Dissolve(.25)
    play test_three "sounds/sfx_footsteps_fat_boy_2.ogg"

    show Romka Normal m_day_winter 00 norm aside 01:
        parallel:
            linear 1. xoffset 400
        parallel:
            linear .25 yoffset 90
            linear .25 yoffset 100
            repeat 2
    pause .5
    scene bg_black with Dissolve(.5)

    stop fon fadeout 2
    stop test_six fadeout 2

    "Пятясь, мы выбрались на порог под немилосердные удары ветра."

    scene police_station
    show blizzard_d4_evening_far zorder 1
    show blizzard_d4_evening_near zorder 1
    show blizzard_d4_evening_big zorder 1
    play sound "sounds/Door_close.ogg"

    show police_roma
    show police_anton
    with Dissolve(.5)

    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 1 loop

    $ music_during_lines = 0.75
    voice "voice/romka/4day/155 D.ogg"
    Rom "Дохлый номер! Не помогут нам мусора."
    voice "voice/romka/4day/156 O.ogg"
    Rom "Одна надежда на нас самих."
    $ music_during_lines = 1.0
    "В эту минуту мне казалось, что в мире нет ничего, кроме ветра и долговязых теней, блуждающих в потёмках."
    "И что нам самим суждено стать такими же тенями."

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound "sounds/sfx_shake_hands.ogg"

    "Ромка протянул мне руку, прощаясь."
    "Я подумал, что как только разожму его ладонь, то сам очнусь в лесу без памяти. Если только меня не сожрут заживо."

    play sound "sounds/loop_footsteps_snow_fast.ogg" fadein 0.6

    hide police_roma with Dissolve(.5)
    stop sound fadeout 3
    "Он отпустил руку и ушёл."

    show bg_black zorder 10:
        alpha 0
        linear 2 alpha 1
    "А я ёжился на морозе, долго не решаясь покинуть освещённый пятачок перед милицейским участком."
    stop music2 fadeout 4
    jump d4_home






label d4_polhouse_begin:
    $ story_manager.MarkEvent(("day4", "scene_ph1"))
    jump d4_polhouse_begin.devend
    label d4_polhouse_begin.dev hide:
        scene bg_black
        menu:
            "Полина, амулет":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
                $ Flags.Raise("amulet")
            "Полина, без амулета":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
            "Предатель Лисы":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 fox")
                $ Flags.Raise("betray")
    label d4_polhouse_begin.devend:

    $ Flags.Raise("polhouse")
    scene d4_road:
        zoom .678

    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    with Dissolve(0.5)
    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 2
    play test_two "sounds/loop_dogs_barking_chains.ogg" fadein 2 volume 0.35 loop

    play music "music/Beautiful mystery.ogg" volume 0.75 fadein 1
    "Посёлок выглядел покинутым и каким-то усопшим."
    "Покосившийся штакетник, замусоренные овраги..."
    "Летом, наверное, тут зелено и оттого симпатично. Но зимой, под коркой льда, под одеялом снега..."
    if ROUTE_FOX:
        "Я озирался изредка, чтобы убедиться, не идут ли следом мои в обоих смыслах преданные друзья."
    "Псы лаяли и гремели цепями за заборами, но резко смолкали, когда мы доходили до следующего дома."
    $ music_during_lines = 0.8
    voice "voice/anton/4day/22 Pre.ogg"
    Ant "Представь, что это призраки цепями звенят."
    voice "voice/Polina/4day/50 O.ogg"
    Pol "О, я обожаю сказки про призраков. Дедушка часто мне их рассказывает..."

    stop test_two fadeout 6

    scene d4_polina_home_clouds
    show d4_polina_home_house
    show blizzard_d4_day_far
    show blizzard_d4_day_near zorder 5
    with Dissolve(0.5)

    stop test_three fadeout 1.2

    "Она остановилась у небольшого, но уютного дома с заснеженной крышей. Положила руку на калитку."
    play sound "sounds/steps/step_snow1.ogg"
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.5):
        xoffset -330
    "Вгляделась в меня, словно хотела залезть в душу."
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    show Polina Front b_day_winter 01 serious ahead 011 with Dissolve(0.3)
    voice "voice/Polina/4day/51 Vo.ogg"
    Pol "Вот я всё вспоминаю дедушку, говорю, какой он хороший, заботливый, умный, но это только половина правды."
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    show Polina Front b_day_winter 01 serious ahead 011 with Dissolve(0.3)
    voice "voice/Polina/4day/52 V.ogg"
    Pol "В последнее время он немного..."
    show Polina Front b_day_winter 01 serious aside 04 with Dissolve(0.3)
    "Она сделала паузу, подбирая формулировку."
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    show Polina Front b_day_winter 01 serious ahead 011 with Dissolve(0.3)
    voice "voice/Polina/4day/53 Chu.ogg"
    Pol "...чудной? Да, пожалуй." id d4_polhouse_begin_devend_33730028
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    show Polina Front b_day_winter 01 serious ahead 011 with Dissolve(0.3)
    voice "voice/Polina/4day/54 Sta.ogg"
    Pol "Стал таким с годами. Так что ничему не удивляйся."
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    voice "voice/anton/4day/23 Tak.ogg"
    Ant "Так точно! Ничему не удивляться!"
    show Polina Front b_day_winter 01 serious ahead 04 with Dissolve(0.3)
    show Polina Front b_day_winter 01 smile2 ahead 014 with Dissolve(0.3):
        linear .2 yoffset 10
        linear .2 yoffset 0
        repeat 2
    voice "voice/Polina/4day/55 Ha.ogg"
    Pol "Ха-ха! Вольно!"
    $ music_during_lines = 1.0
    window hide


    play test_three "sounds/loop_footsteps_two.ogg" fadein 1.5 loop

    hide Polina with Dissolve(0.3)

    show d4_polina_home_house:
        align (.5, .5)
        zoom 1.
        subpixel True
        linear 1.5 zoom 1.05
    show d4_poldoor_1:
        alpha 0
        1.
        linear .5 alpha 1

    pause 1
    stop test_three fadeout 1.6

    window show
    "Мы прошли по расчищенной дорожке к дому."

    play sound "sounds/sfx_door_lock_open.ogg"

    "Полина отперла замок."

    play sound "sounds/sfx_door_wooden_open.ogg"

    scene d4_poldoor_2
    show blizzard_d4_day_near zorder 5
    with Dissolve(0.5)
    "Длинный коридор был полон теней."

    window hide

    play test_one "sounds/loop_footsteps_home_normal_two.ogg" fadein 0.6
    pause 0.5
    stop fon fadeout 0.6
    play sound "sounds/sfx_door_wooden_close_fast.ogg"

    show d4_poldoor_2:
        align (.5, .5)
        zoom 1.
        subpixel True
        linear 1. zoom 1.08
    show bg_black zorder 100:
        alpha 0
        .5
        linear .5 alpha 1

    pause 1.5
    stop test_one fadeout 1.6

    window show
    stop music fadeout 6
    "Дверь, хлопнув, отрезала нас от шума ветра и остальных уличных звуков."
    play test_six "sounds/loop_heartbeat_reverb.ogg" fadein 0.8 loop
    "Наступила такая тишина, что я услышал, как стучит сердце Полины."
    stop test_six fadeout 5
    $ add_text_to_dictionary(52)
    "Хотелось накрыть его рукой и ощущать биение ладонью, линиями жизни."

    play sound ["sounds/sfx_door_open_home.ogg","<silence .4>","sounds/sfx_door_wooden_close_fast.ogg"]

    window hide
    play test_three "<from 0 to 3>sounds/steps/steps_shool.ogg"
    play test_four "<from 0 to 3>sounds/steps/Polina_step_02.ogg"
    scene polina_home_day_04 with Dissolve(2.0)
    pause 1.0
    window show
    voice "voice/Polina/4day/56 Ti.ogg"
    Pol "Ты всегда так застываешь?"
    voice "voice/Polina/4day/57 Ka.ogg"
    Pol "Как будто у тебя в голове стоп-кран нажали."
    voice "voice/anton/4day/24 Fa.ogg"
    Ant "Фантазия рисует всякие картинки."
    voice "voice/Polina/4day/58 A.ogg"
    Pol "А, понимаю."

    play sound "sounds/sfx_coat_on_rack.ogg"

    "Она сняла курточку и повесила на крючок."

    play sound "sounds/loop_footsteps_home_light_one.ogg" fadein 0.1

    show sprite_polina_d3:
        alpha 0
        xoffset -80
        parallel:
            linear .5 alpha 1
        parallel:
            linear .8 xoffset 0
        parallel:
            linear .2 yoffset 15
            linear .2 yoffset 0
            linear .2 yoffset 15
            linear .2 yoffset 0
    pause .8
    hide sprite_polina_d3
    show Polina Front m_day 02 norm ahead 04
    with Dissolve(0.5)

    stop sound fadeout 0.3

    window show

    show Polina Front m_day 02 norm ahead 02 with Dissolve(0.15)
    voice "voice/Polina/4day/59 Ra.ogg"
    Pol "Раздевайся-разувайся."
    show Polina Front m_day 02 norm ahead 04 with Dissolve(0.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(0.15)
    voice "voice/Polina/4day/60 Ya.ogg"
    Pol "Я пока в комнате приберусь."
    show Polina Front m_day 02 norm ahead 04 with Dissolve(0.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(0.15)
    voice "voice/Polina/4day/61 De.ogg"
    Pol "Дедушка, бывает, вещи свои оставляет где попало."
    show Polina Front m_day 02 norm ahead 04 with Dissolve(0.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(0.15)
    voice "voice/Polina/4day/62 Ya.ogg"
    Pol "Я быстро."

    window hide

    play test_one "sounds/loop_footsteps_home_light_one.ogg" fadein 0.15
    hide Polina with Dissolve(0.5)
    pause 1.2

    stop test_one fadeout 1
    play sound "sounds/Door_open_2.ogg" volume 0.5
    show Polina_home_door with Dissolve(0.5)
    pause 1

    play test_three "sounds/close-door.ogg"
    hide Polina_home_door with Dissolve(0.5)

    window show
    "Лёгкая, как бабочка, она упорхнула."
    "Такая же, только стальная, могла порхать у меня в животе уже в обозримом будущем."
    "Я стащил куртку. Расшнуровал ботинки."

    play sound "sounds/sfx_wheelchair_squeak_3.ogg" volume 0.35

    "Тонкий скрип достиг уха."

    jump d4_polhouse_lookaround


label d4_polhouse_lookaround:
    $ story_manager.MarkEvent(("day4", "la polhouse1"))
    $ SceneFlags.Reset()
    label d4_polhouse_lookaround.main:
        window hide
        call screen day4_polhouse_observe

    label d4_polhouse_lookaround.ski:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "ski"))
        if SceneFlags.Seen("ski"):
            "Лыжи."
        else:

            play sound "sounds/sfx_ski.ogg"

            "Лыжи «Турист». Папа рассказывал, что в детстве сам делал лыжи и палки, и даже лыжную мазь сам изготавливал из пчелиного воска, канифоли и хвойной смолы."
            "Для здешних суровых зим – то что надо. Но эти лыжи стоит отремонтировать. Скобы крепления совсем истлели. На них какие-то красные пятна. Это просто ржавчина."
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround.main

    label d4_polhouse_lookaround.telephone:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "telephone"))
        if SceneFlags.Seen("telephone"):
            "Телефон."
        else:

            play sound "sounds/sfx_phone_rattle.ogg"

            "Если встать напротив телефона, кажется, что узор на обоях – это внимательные глаза. Отсюда, значит, мне звонит Полина!"
            "Стоит тут под счётчиком, в сумерках, среди теней, накручивает на палец шнур. Может, выключателем балуется, то зажигает свет, то гасит, и говорит со мной из темноты."
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround.main

    label d4_polhouse_lookaround.horns:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "horns"))
        if SceneFlags.Seen("horns"):
            "Рога."
        else:

            play sound "sounds/sfx_deer_roar.ogg"

            "Не понимаю, зачем взрослые такое вешают в доме. Кривые острые отростки. Я читал в «Юном натуралисте», что животным не больно, если спиливают уже отвердевшие рога."
            "И всё равно это как срезанными ногтями стену заклеить. Тоже что-то ороговевшее, когда-то бывшее частью живого организма."
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround.main

    label d4_polhouse_lookaround.portrait:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "portrait"))
        if SceneFlags.Seen("portrait"):
            "Портрет Паганини."
        else:

            play sound "sounds/sfx_violin_Paganini.ogg"

            "А эту картину я знаю. Паганини. Тот, который так круто играл на скрипке, что люди решили, будто он продал душу дьяволу."
            "Портрет нарисовал Николай Фешин — он был известным художником в России, а после революции уехал в Америку и там тоже прославился. Какие длинные у Паганини пальцы."
            "И взгляд такой пронзительный. Куда он смотрит? Может, и правда — продал душу? А Полина, интересно, продала бы?"
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround.main

    label d4_polhouse_lookaround.mirror:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "mirror"))
        if SceneFlags.Seen("mirror"):
            "Зеркало."
        else:

            play test_four "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.35 loop

            $ renpy.start_predict("d4_polmirror_bg idle")
            $ renpy.start_predict("d4_polmirror_bg statterloop")
            $ renpy.start_predict("d4_polmirror_ant down")
            $ renpy.start_predict("d4_polmirror_ant straight")
            $ renpy.start_predict("d4_polmirror_ant scared")
            $ renpy.start_predict("d4_polmirror_dust")
            $ renpy.start_predict("d4_boar_fall")
            $ renpy.start_predict("d4_boar scream")
            $ renpy.start_predict("d4_boar_bg")
            $ renpy.start_predict("d4_boar_hand")


            scene d4_polmirror_bg idle:
                blur 8
            show d4_polmirror_ant down
            show d4_polmirror_fg
            show layer master:
                align (.5, .5)
                zoom 1.00
                easein .5 zoom 1.05
            with Dissolve(.5)

            pause .5
            stop test_four fadeout 0.5

            window show
            "В этом зеркале всё такое резкое и глубокое, взгляд проваливается."

            play sound "sounds/sfx_dust_fall_mirror.ogg"

            show d4_polmirror_dust
            "Будто не зеркало, а дверной проём, за которым такая же комната с лыжами, липкими на ощупь обоями."

            play sound "sounds/sfx_door_rattle.ogg"

            "И счётчиком, который к концу месяца почти ничего не накрутил, словно Полина с дедом вечерами сидят в кромешной темноте."


            show d4_polmirror_fg:
                .7
                linear .5 blur 8
            show d4_polmirror_bg statter1:
                blur 8
                .7
                linear .5 blur 0
            show d4_polmirror_ant straight:
                .5
                .05
                linear .1 alpha 0
            show d4_polmirror_ant scared as _new_ant behind d4_polmirror_fg:
                alpha 0
                .5
                linear .1 alpha 1
                .1
                linear .5 blur 8

            "А ещё..."

            hide d4_polmirror_dust

            show Null ():
                alpha 0
                .5
                "d4_polmirror_dust"
                alpha 1
            show d4_polmirror_bg idle:
                .3
                "d4_polmirror_bg statter1"
            play sound "sounds/sfx_dust_fall_mirror.ogg" volume 0.32
            "А?! Там кто-то есть или это фабричный дефект зеркала искривляет двери?{w=.7}{nw}"

            play wtf "sounds/sfx_hog_screamer.ogg"

            call screen forced_timer(0.2)

            scene d4_polmirror_bg idle
            show d4_polmirror_ant scared
            show d4_polmirror_fg
            show d4_boar_fall
            show layer master:
                align (.5, .5)
                zoom 1.05
            window hide

            scene d4_boar scream
            call screen forced_timer(0.4)

            scene d4_boar_bg
            show d4_boar_hand
            call screen forced_timer(1.0)
            "Всего лишь охотничий трофей."

            play test_four "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.35 loop

            play sound "sounds/sfx_boar_put.ogg"

            show d4_boar_hand:
                linear 4 yoffset 1000

            pause .5

            stop test_four fadeout 0.6

            scene polina_home_day_04 with Dissolve(.5)

            $ renpy.stop_predict("d4_polmirror_bg idle")
            $ renpy.stop_predict("d4_polmirror_bg statterloop")
            $ renpy.stop_predict("d4_polmirror_ant down")
            $ renpy.stop_predict("d4_polmirror_ant straight")
            $ renpy.stop_predict("d4_polmirror_ant scared")
            $ renpy.stop_predict("d4_polmirror_dust")
            $ renpy.stop_predict("d4_boar_fall")
            $ renpy.stop_predict("d4_boar scream")
            $ renpy.stop_predict("d4_boar_bg")
            $ renpy.stop_predict("d4_boar_hand")

            $ SceneFlags.Raise("boarhead")


            $ achievement_grant("ach_pig")

            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround.main

    label d4_polhouse_lookaround.grandfather:
        $ story_manager.MarkEvent(("day4", "la polhouse1", "grandfather"))
        if SceneFlags.Seen("grandfather"):
            "Комната Деда."
        else:

            window hide
            play test_three "<from 0 to 1.2>sounds/loop_footsteps_home_normal_one.ogg"
            scene d4_deddoor 1 with Dissolve(.5)
            call screen day4_ded_door
            scene bg_black
            show d4_deddoor_inside2

            play sound "sounds/sfx_door_close_slow.ogg"
            play test_four "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.3

            show d4_deddoor open:
                subpixel True
                align (.5, .5)
                zoom 1.0
                ease 3 zoom 1.15
            show layer master:
                subpixel True
                align (.5, .5)
                zoom 1.0
                ease 3 zoom 1.05
            pause 2.5
            window show

            stop test_four fadeout 0.5
            play test_five "sounds/loop_fly_buzzing.ogg" volume 0.11 fadein 1 loop

            "Ого, сколько всякого хлама, как в барахолке старьёвщика!"
            "Или как на свалке у посёлкового кладбища, куда сбрасывают искусственные цветы, щепки сгнивших крестов и грязные ленты с золотистыми словами соболезнований."
            "Почему мне кажется, что дед Полины приволок всё это с кладбищенской помойки? Там ведь не бывает детских игрушек… или бубна, как в книжке про северных шаманов."
            "А это… как же оно называется? Ловец снов вроде. Но поймал ловец не сны, а паука-сенокосца."
            "И запашок… Не мудрено, что тут даже среди зимы жужжат мухи. Пахнет топлёным салом и сырой землёй. Если долго здесь находиться, наверное, можно привыкнуть."
            $ true_detective_count4 += 1

            stop test_five fadeout 0.8
            play sound "sounds/sfx_door_home_close.ogg"
            play test_four "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.3

            pause .4

            stop test_four fadeout 0.5

            scene polina_home_day_04 with Dissolve(.5)
        jump d4_polhouse_lookaround.main


label d4_polhouse_followup:
    $ story_manager.MarkEvent(("day4", "scene_ph2"))
    play sound "sounds/sfx_shoes_take_off.ogg"

    window show
    "Снимая обувь, я посмотрел вглубь дома."
    play music2 "music/13_Disaster_pt1.ogg" fadein 0.2
    "Полумрак маскировал поворот в конце коридора. Что-то двигалось ко мне, волочась по рассохшимся доскам."

    play sound "sounds/sfx_wheelchair_coming_1.ogg"

    show shadow_pol_gf 0 with Dissolve(0.5)
    "Кыр-кыр!"

    play sound "sounds/sfx_wheelchair_coming_2.ogg"

    show shadow_pol_gf 1 with Dissolve(0.5)
    "Кыр-кыр!"

    play sound "sounds/sfx_wheelchair_coming_3.ogg"

    show shadow_pol_gf 2 with Dissolve(0.5)
    "Скрип нарастал."

    play sound "sounds/sfx_wheelchair_coming_4.ogg"

    show shadow_pol_gf 3 with Dissolve(0.5)
    "Я поймал себя на том, что отступаю к дверям."
    voice "voice/anton/4day/25 Pol.ogg"
    Ant "Полина?"

    play sound "sounds/sfx_wheelchair_coming_normal.ogg"

    hide shadow_pol_gf
    show pol_grandpa
    with Dissolve(0.5)
    stop music2 fadeout 3
    "Из-за угла выкатилось инвалидное кресло. Кряжистый старик выплыл из темноты."
    hide pol_grandpa

    play sound "sounds/sfx_wheelchair_coming_close_1.ogg"

    show Ded Normal m_day 01 normal ahead 01:
        xoffset 200
        yoffset 10
    with Dissolve(.5)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/01. Ti.ogg"
    Ded "Ты, должно быть, одноклассник моей Поли?"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    play music "music/Mystic Of Hariton.ogg" volume 0.8 fadein 2.5
    $ music_during_lines = 0.88
    voice "voice/anton/4day/26 Da.ogg"
    Ant "Да. Антон Петров."

    play sound "sounds/sfx_shake_hands.ogg"

    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.5)
    "Рукопожатие было на удивление крепким."
    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/02. Ochen.ogg"
    Ded "Очень приятно! Очень."
    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/03. A.ogg"
    Ded "А я Харитон. Греческое имя, значит «щедрый»."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/04.At.ogg"
    Ded "А твоё имя, знаешь, что обозначает?"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/27 Ni.ogg"
    Ant "Никогда не задумывался."
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/05. Ot.ogg"
    Ded "От латинского «антео» — тот, кто вступает в бой!"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    play test_three "voice/anton/4day/Hm.ogg"
    "Я одобрительно хмыкнул."
    "Оказывается, у моего имени «смелые» корни."
    voice "voice/anton/4day/28 APo.ogg"
    Ant "А Полина?"
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/05.pol.ogg"
    Ded "Полина – французского происхождения."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/06.Esli.ogg" 
    Ded "Если не ошибаюсь... «Солнечная»."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    "Ну конечно. Солнце, манящая Франция, небо над Парижем, – всё это про Полину."
    voice "voice/anton/4day/29 Vi.ogg"
    Ant "Вы так много знаете об именах."
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/06.Ya.ogg"
    Ded "Я каждой своей кукле особенное имя давал."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/113. Kuk.ogg"
    Ant "Кукле?"
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/07. Pol.ogg"
    Ded "Полина не рассказывала? Я же кукловодом работал при театре."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/08.Pot.ogg"
    Ded "Потом сторож с сигаретой тлеющей уснул, сам погиб, и театр сгорел до основания."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Worry m_day 01 worry ahead 02 with Dissolve(.15)
    voice "voice/Hariton/09.Ku.ogg"
    Ded "Куклы мои сгорели."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/114. Za.ogg"
    Ant "Жаль."
    "А про себя подумал: вроде Полина рассказывала, что её дедушка был краеведом..."
    show Ded Happy m_day 01 normal ahead 01
    show ded_eyes 4:
        xoffset 200
        yoffset 10
    with Dissolve(.5)
    show ded_eyes 5 with Dissolve(.15)
    pause .5
    show ded_eyes 4 zorder 1 with Dissolve(.15)
    "Он прищурился хитро."
    show Ded Normal m_day 01 normal ahead 01
    hide ded_eyes
    with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/07. Az.ogg"
    Ded "А знаешь ли ты, Петров Антон, что в старину у людей два имени было: настоящее и то, что они называли незнакомцам?"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/08.Sh.ogg"
    Ded "Считалось, что подлинное имя, попав к нехорошим людям, могло обернуться против человека."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/09.Po.ogg"
    Ded "По имени насылали хвори и даже смерть."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/115. Ogo.ogg"
    Ant "Ого!"
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)

    voice "voice/Hariton/10.V.ogg"
    Ded "Вот тебе и ого!"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/11.Iz.ogg"
    Ded "И зверям имена придумывали не просто так."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    $ add_text_to_dictionary(49)
    voice "voice/Hariton/12.Za.ogg"
    Ded "Заяц – от литовского «зайсти» — прыгун, то есть. А волк – старославянское «влек» — тот, кто таскает."

    play sound "sounds/sfx_wheelchair_coming_close_2.ogg"

    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 01:
        align (.5, 1.)
        xoffset 130
        yoffset 40
        zoom 1.1
    with Dissolve(.5)
    "Харитон подъехал ближе. Скрестил руки на груди."
    "Я задумался: дома ли Полинины родители?"
    "Она ни разу не говорила о маме — только о дедушке."
    "Чтобы поддержать беседу, я спросил:"
    voice "voice/anton/4day/116. A.ogg"
    Ant "А медведь?"
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/13.O.ogg"
    Ded "О! Имя медведя неизвестно."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/14.N.ogg"
    Ded "Наши предки так боялись этого зверя, что предпочли забыть слово, которым его величали."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/15.Ono.ogg"
    Ded "Оно просто сгинуло из языка."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    $ add_text_to_dictionary(50)
    voice "voice/Hariton/16. Vm.ogg"
    Ded "Вместо него осталось более позднее прозвище — «ведающий мёдом»."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/117. En.ogg"
    Ant "Интересно."
    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.5)
    "Улыбка старика стала шире. Обнажился частокол металлических коронок."
    stop music fadeout 5.5
    "Он поднял руку и поводил ею в воздухе, как граблями, расчёсывая пальцами пустоту."

    $ renpy.start_predict("koshmar")
    $ renpy.start_predict("koshmar ded 0")
    $ renpy.start_predict("koshmar ded 1")
    $ renpy.start_predict("koshmar ded 2")
    $ renpy.start_predict("koshmar ded 3")
    $ renpy.start_predict("koshmar ded 4")
    $ renpy.start_predict("koshmar ded 5")
    $ renpy.start_predict("koshmar ded 6")
    $ renpy.start_predict("koshmar ded 7")
    $ renpy.start_predict("koshmar ded 8")
    $ renpy.start_predict("koshmar ded 9")


    show Ded Angry m_day 01 angry ahead 01 with Dissolve(.5)
    show Ded Angry m_day 01 angry ahead 02 with Dissolve(.15)
    voice "voice/Hariton/18.Sk.ogg"
    Ded "Скырлы-скырлы-скырлы..."
    show Ded Angry m_day 01 angry ahead 01 with Dissolve(.15)
    play music2 "music/39_Dvar - Oramah Elahar.ogg" fadein 3
    "От скрипучего звука я весь сжался."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.5)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    $ add_text_to_dictionary(51)
    voice "voice/Hariton/19.To.ogg"
    Ded "То я медведь на липовой ноге, на берёзовой клюке."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/19.Vse.ogg"
    Ded "Все по сёлам спят, по деревням спят."
    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/19.Odn.ogg"
    Ded "Одна баба не спит — на моей коже сидит."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/19.Mo.ogg"
    Ded "Мою шерстку прядёт, моё мяско жрёт."
    $ music_during_lines = 1.0
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    "Если об этом предупреждала Полина, то я не сдержал слово."
    "Не то чтобы я удивился — скорей не на шутку встревожился."
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)

    play test_five "sounds/loop_underwater.ogg" volume 0.25 fadein 2 loop

    stop music2 fadeout 4
    play music "music/Magic Orchestral Bells.ogg" volume 0.65 fadein 5

    $ story_manager.MarkEvent(("day4", "scene_ph3"))

    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/20.Po.ogg"
    Ded "По легенде, именно в нашей деревне приключилась эта страшная сказка... Как и многие другие."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)

    show koshmar:
        alpha 0.0
        linear 2. alpha 1.0

    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/21Vot.ogg"
    Ded "Вот, к примеру."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)

    voice "voice/Hariton/21.Vpro.ogg"
    Ded "В прошлом веке простому люду тяжко пришлось."
    voice "voice/Hariton/21.Den.ogg"
    Ded "Денег у них тогда мало было, а еды и того меньше. Точь-в-точь как сейчас."
    show koshmar ded 0 with Dissolve(1.)

    play test_one "sounds/loop_forest_cries.ogg" fadein 2

    voice "voice/Hariton/22. Po.ogg"
    Ded "Подались тогда крестьяне разбойничать – тайгу обворовывать. Кто карася ухватит, а кто и гуся."



    show koshmar with Dissolve(1.)
    voice "voice/Hariton/23.A.ogg"
    Ded "А главный егерь мало того что не препятствовал, так ещё в первых рядах браконьерствовал."
    voice "voice/Hariton/24.S.ogg"
    Ded "Самым зажиточным стал на селе. Погреб того и гляди лопнет."
    show koshmar ded 1 with Dissolve(1.)
    voice "voice/Hariton/25.Tak.ogg"
    Ded "Так и кричал егерь на всю округу: «Я в лесу хозяин!»"

    stop test_one fadeout 5

    show koshmar with Dissolve(.5)
    show koshmar ded 2 with Dissolve(.5)

    play test_six "sounds/loop_banquet_story.ogg" fadein 1 loop

    voice "voice/Hariton/26.Ob.ogg"
    Ded "Обзавёлся он, значится, семьёй, слугами да каким-никаким имением."
    show koshmar with Dissolve(1.)

    play test_one "sounds/loop_dogs_barking_outdoors.ogg" fadein 1 loop

    stop music fadeout 16
    voice "voice/Hariton/27.E.ogg"
    Ded "И на радостях пир закатил горой аж до самой ночи. А как двенадцать пробило, собаки залаяли."
    show koshmar ded 3 with Dissolve(1.)
    voice "voice/Hariton/29. Ed.ogg"
    Ded "«Идите, — кричит егерь слугам, — собакам кости бросьте»."
    show koshmar with Dissolve(1.)

    stop test_one fadeout 1.5
    play sound "sounds/sfx_door_heavy_knock.ogg"

    voice "voice/Hariton/30.Ch.ogg"
    Ded "Через время в ворота застучали."
    show koshmar ded 3 with Dissolve(1.)
    voice "voice/Hariton/31. Ede.ogg"
    Ded "«Идите, — кричит семье, — гостей прогоните»."

    stop test_six fadeout 3

    show koshmar with Dissolve(1.)
    voice "voice/Hariton/32.O.ogg"
    Ded "Остался он за столом один. Никто воротиться не спешит."

    play sound "sounds/sfx_dogs_howling.ogg"

    voice "voice/Hariton/33.Sl.ogg"
    Ded "Слышит, собаки завыли и смолкли."

    play test_one "sounds/sfx_door_banging_hard.ogg" volume 0.75

    voice "voice/Hariton/34.E.ogg"
    Ded "И тут со страшной силой в дверь забарабанили!"
    voice "voice/Hariton/34.B.ogg"
    Ded "Бах-бах-бах!"
    "Я облизал сухие губы и невольно поглядел за плечо старика, про себя умоляя Полину поскорее прийти и прервать этот странный монолог."
    "Но лишь тени копошились за спиной Харитона."

    play sound "sounds/sfx_footsteps_wooden_floor_tale.ogg"

    voice "voice/Hariton/35.E.ogg"
    Ded "Егерь от страха едва живой в погреб помчался."

    stop sound fadeout 0.6
    play test_one "sounds/sfx_door_lock_heavy.ogg"

    voice "voice/Hariton/35.Z.ogg"
    Ded "Замком «щёлк». Вдруг голос из-за двери:"
    show koshmar ded 4 with Dissolve(1.)
    voice "voice/Hariton/36. M.ogg"
    Ded "Милый, это я, жена твоя. Отвори."
    show koshmar with Dissolve(.5)
    show koshmar ded 6 with Dissolve(.5)
    voice "voice/Hariton/37.V.ogg"
    Ded "В жизнь не открою."
    show koshmar with Dissolve(1.)
    voice "voice/Hariton/38. G.ogg"
    Ded "Голос стал грубее, напористее:"
    show koshmar ded 4 with Dissolve(1.)
    voice "voice/Hariton/39. Ez.ogg"
    Ded "Изголодалась я, любимый, дай хоть чего-то из закромов."
    show koshmar with Dissolve(.5)
    show koshmar ded 6 with Dissolve(.5)
    voice "voice/Hariton/40.U.ogg"
    Ded "«Уйди, уйди! Христом заклинаю!» — закричал егерь и упал молиться."
    show koshmar with Dissolve(1.)
    voice "voice/Hariton/41.T.ogg"
    Ded "Тогда голос, как гром, грянул:"
    show koshmar ded 4 with Dissolve(1.)
    show koshmar ded 5 with Dissolve(.1)

    show layer master:
        align (.5, .5)
        zoom 1.01
        block:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            0.05
            repeat

    voice "voice/Hariton/42.C.ogg"
    Ded "Целиком не выйдешь — хоть кусок мне отрежь!"
    show koshmar
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(1.)
    voice "voice/Hariton/43.Eg.ogg"
    Ded "Егерь вне себя от ужаса просидел в подвале до первых петухов."
    voice "voice/Hariton/44. A.ogg"
    Ded "А как показаться отважился, то нашёл своих слуг и родных..."

    window hide
    play test_one "sounds/loop_hanged.ogg" fadein 1 loop
    show koshmar ded 8
    show layer master:
        align (.5, .5)
        zoom 1.01
        block:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            0.05
            repeat
    with Dissolve(1.)

    pause 1.

    voice "voice/Hariton/45.P.ogg"
    Ded "...повешенными на собственных кишках вдоль тракта." id d4_polhouse_followup_9cc6d6f2

    window show

    stop test_one fadeout 3
    play test_two "sounds/loop_sound_house.ogg" fadein 1 loop

    show koshmar with Dissolve(.5)
    show koshmar ded 7 with Dissolve(.5)
    voice "voice/Hariton/46. G.ogg"
    Ded "Глядь — а в имении уже дикие звери хозяйничают."

    play music "music/Hor.ogg"
    show koshmar with Dissolve(.5)

    stop test_two fadeout 3
    play test_four "sounds/sfx_crows_creepy.ogg"

    show koshmar ded 9
    show layer master:
        align (.5, .5)
        block:
            linear .02 zoom 1.02
            linear .02 zoom 1.00
            repeat
    with Dissolve(.5)

    $ music_during_lines = 0.7

    voice "voice/Hariton/47.P.ogg"
    Ded "Потому что нет у тайги границ: она частично в нашем мире, а отчасти там, где ночь никогда не кончается."
    show koshmar
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(1.)

    play test_one "sounds/loop_footsteps_snow_heavy_distant_run.ogg" fadein 1 loop
    pause 1.5

    voice "voice/Hariton/49. E.ogg"
    Ded "Егерь пытался сломя голову бежать из проклятой деревни, но истинный Хозяин леса настиг его в пути." id d4_polhouse_followup_39bc5074

    stop test_one fadeout 0.2
    play sound "sounds/piano-hit-3.ogg"



    stop test_five fadeout 3

    show Ded Normal m_day 01 normal ahead 01 behind koshmar
    hide koshmar with Dissolve(1.)

    $ renpy.stop_predict("koshmar")
    $ renpy.stop_predict("koshmar ded 0")
    $ renpy.stop_predict("koshmar ded 1")
    $ renpy.stop_predict("koshmar ded 2")
    $ renpy.stop_predict("koshmar ded 3")
    $ renpy.stop_predict("koshmar ded 4")
    $ renpy.stop_predict("koshmar ded 5")
    $ renpy.stop_predict("koshmar ded 6")
    $ renpy.stop_predict("koshmar ded 7")
    $ renpy.stop_predict("koshmar ded 8")
    $ renpy.stop_predict("koshmar ded 9")

    stop music fadeout 3.5
    "Мой голос зазвучал неуверенно:"
    voice "voice/anton/4day/118. E.ogg"
    Ant "И что же с ним сделал этот Хозяин леса?"

    $ music_during_lines = 1.0

    play test_seven "sounds/Tension Suspense Risers_05.ogg" volume 0.80
    play test_three "sounds/sfx_wheelchair_squeak_1.ogg"

    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.15):
        align (.5, 1.)
        xoffset 130
        yoffset 40
        zoom 1.1
        block:
            linear .15 yoffset 50
            linear .15 yoffset 40
            linear .15 yoffset 60
            linear .15 yoffset 40
            repeat

    play test_six "voice/Hariton/51. He.ogg"
    "Старик громко расхохотался, склонив голову набок."
    show Ded Happy m_day 01 normal ahead 02:
        align (.5, 1.)
        xoffset 130
        yoffset 40
        zoom 1.1
    show ded_eyes 4:
        align (.5, 1.)
        xoffset 130
        yoffset 40
        zoom 1.1
    with Dissolve(.15)

    voice "voice/Hariton/51.S.ogg"
    Ded "Спроси лучше, чего он не сделал."
    show Ded Normal m_day 01 normal ahead 01
    hide ded_eyes
    with Dissolve(.15)

    $ renpy.music.set_volume(0.5, 0.5, "test_seven")
    voice "voice/Polina/4day/63 An.ogg"
    Pol "Антон!"
    $ renpy.music.set_volume(1.0, 2.5, "test_seven")
    "Глаза старика пригвоздили меня к дверному полотну."

    play sound "sounds/sfx_door_open_slow.ogg"

    show Polina_home_door behind Ded with Dissolve(0.5)
    show Ded Normal m_day 01 normal aside 01 with Dissolve(0.5)
    voice "voice/Polina/4day/64 A.ogg"
    Pol "Антон, проходи в комнату!"
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(0.25)

    "Несколько секунд старик молчал."

    play sound "sounds/sfx_wheelchair_coming_close_1.ogg"
    hide Ded
    show pol_grandpa:
        xzoom -1
        xoffset 400
    with Dissolve(.5)
    "Потом улыбнулся как ни в чём не бывало и откатил коляску."

    voice "voice/Hariton/52. N.ogg"
    Ded "Ну, заболтал я тебя. Ступай."

    play test_one "sounds/loop_footsteps_home_normal_one.ogg" fadein 1 loop

    scene pol_home_zoom:
        align (.5, .5)
        linear .6 zoom 1.1 align (.5, .5)

    scene bg_black with Dissolve(0.7)

    "Я стряхнул оцепенение и засеменил по коридору."

    voice "voice/anton/4day/119. Pr.ogg"
    Ant "Приятно было познакомиться."
    voice "voice/Hariton/53.E.ogg"
    Ded "И мне, Петров Антон, и мне..."

    stop test_one fadeout 1.5
    play sound "sounds/sfx_door_home_close.ogg"


    scene d4_polroom_bg
    show d4_polroom_piano
    show d4_polroom_cat
    show d4_polroom_poster
    with Dissolve(.5)

    play music "music/Romantic Piano Story.ogg" volume 0.9 fadein 1
    "Я с облегчением проскользнул в комнату Полины." id d4_polhouse_followup_52ef9ebd
    "Она была под стать хозяйке – милая и аккуратная." id d4_polhouse_followup_6760dbf0
    "Сразу бросились в глаза огромная коллекция виниловых пластинок и проигрыватель. Стены украшали фотографии в рамках." id d4_polhouse_followup_b8342ba5
    play sound "sounds/sfx_footsteps_two_carpet.ogg"
    show Polina Front m_day 03 norm ahead 02 with Dissolve(.5):
        xoffset -150
        yoffset 30
    stop test_four fadeout 0.6
    voice "voice/Polina/4day/65 De.ogg"
    Pol "Дедушка тебя не сильно донимал?" id d4_polhouse_followup_2132c864
    show Polina Front m_day 03 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/120. Net.ogg"
    Ant "Нет. Он очень... интересный." id d4_polhouse_followup_a3b1b66c
    show Polina Front m_day 03 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/66 Ne.ogg"
    Pol "Небось ты теперь знаешь всё о своём имени." id d4_polhouse_followup_b9f3e5ba
    show Polina Front m_day 03 norm ahead 01 with Dissolve(.15)
    play test_three "voice/anton/4day/121. Na.ogg"
    "Я натянуто засмеялся. Поводил взглядом по фотографиям." id d4_polhouse_followup_2493dc0f
    stop music fadeout 5
    hide Polina with Dissolve(.5)


label d4_polhouse_lookaround2:
    $ story_manager.MarkEvent(("day4", "la polhouse2"))
    label d4_polhouse_lookaround2.main:
        window hide
        call screen day4_polhouse_observe2
        window show

    label d4_polhouse_lookaround2.player:
        $ story_manager.MarkEvent(("day4", "la polhouse2", "player"))
        if SceneFlags.Seen("player"):
            "Проигрыватель."
        else:

            play sound "sounds/sfx_player_noise.ogg"

            "Немного старомодно, но мне нравится! Посмотрим, что у Полины в коллекции. Грампластинки фирмы «Мелодия» и редкий, югославский, винил фирмы Jugoton."
            "Рахманинов, Свиридов, арии Верди в исполнении Хиблы Герзмавы. Одна классика — ни ансамбля «Песняры», ни группы «Секрет»."
            $ add_text_to_dictionary(53)
            "У неё даже музыка на костях есть – записанная электрорекордером поверх рентгеновских снимков. Игла скользит по фотографии чьих-то рёбер, и играет скрипач Ойстрах."
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround2.main

    label d4_polhouse_lookaround2.piano:
        $ story_manager.MarkEvent(("day4", "la polhouse2", "piano"))
        if SceneFlags.Seen("piano"):
            "Пианино «Кузбасс»."
        else:

            play sound "sounds/sfx_winter_wind_piano.ogg"

            "Пианино «Кузбасс». Ни пылинки на крышке! Здесь она репетирует. Почитаем, что за произведение в нотной тетради."
            "Гендель, «Каприччио соль минор». Похоже на название пиццы, которую едят черепашки-ниндзя. А я и «Собачий вальс» не сыграю."
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround2.main

    label d4_polhouse_lookaround2.poster:
        $ story_manager.MarkEvent(("day4", "la polhouse2", "poster"))
        if SceneFlags.Seen("poster"):
            "Плакат «Сейлор Мун»."
        else:

            play sound "sounds/sfx_poster.ogg"

            "Плакат «Сейлор Мун». Девчачий мультик! «Трансформеры» намного лучше, и рисовать их интереснее, особенно в момент перевоплощения, когда одно становится другим."
            "Хотя если у Полины ловит канал «2х2», и она предложит посмотреть, я не откажусь. Возмездие во имя Луны!"
            $ true_detective_count4 += 1
        jump d4_polhouse_lookaround2.main


label d4_polhouse_followup2:
    $ story_manager.MarkEvent(("day4", "scene_ph4"))
    window show

    stop music fadeout 4


    $ renpy.start_predict("d4_dj_cat")
    $ renpy.start_predict("d4_dj_cat_0")
    $ renpy.start_predict("d4_piano")
    $ renpy.start_predict("d4_piano 1")
    $ renpy.start_predict("d4_poster_close")
    $ renpy.start_predict("d4_poster_buster")


    voice "voice/anton/4day/121. A.ogg"
    Ant "А это твои родители?"

    play test_four "sounds/loop_footsteps_home_light_one.ogg" fadein 0.3

    show Polina Front m_day 02 sadly_down aside 01 with Dissolve(.5):
        xoffset -150
        yoffset 30
    stop test_four fadeout 0.6
    "Полина потупилась."

    play music2 "music/loss.ogg" fadein 1
    show Polina Front m_day 02 sadly ahead 02 with Dissolve(.35)
    voice "voice/Polina/4day/67 Da.ogg"
    Pol "Да."
    show Polina Front m_day 02 sadly ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 sadly ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/68 Oni.ogg"
    Pol "Они погибли много лет назад... Я их практически не помню."
    show Polina Front m_day 02 sadly ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/122. O.ogg"
    Ant "О!"
    "Я чувствовал себя ослом. Ведь мог и догадаться, что Полина сирота."
    voice "voice/anton/4day/123. Mne.ogg"
    Ant "Мне очень жаль."
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.35)
    voice "voice/Polina/4day/69 Sp.ogg"
    Pol "Спасибо."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/70 De.ogg"
    Pol "Дедушка воспитывал меня, как родную дочь. Никогда не устану благодарить его."
    show Polina Front m_day 02 norm ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/124. Pr.ogg"
    Ant "Представляю, каково тебе пришлось."
    show Polina Front m_day 02 sad ahead 04 with Dissolve(.35)
    "Полина улыбнулась печально, смахнула с лица непослушные локоны."
    show Polina 3_4 m_day 04 norm ahead 02 with Dissolve(.5)
    stop music2 fadeout 3
    voice "voice/Polina/4day/71 Da.ogg"
    Pol "Давай не будем о грустном."

    show Polina 3_4 m_day 04 norm ahead 01 with Dissolve(.15)
    show Polina 3_4 m_day 04 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/72 Po.ogg"
    Pol "Познакомься с Джоанной."
    play test_two "sounds/steps/Anton-steps-steal-1.ogg"

    show Polina 3_4 m_day 04 norm ahead 01 with Dissolve(.15)

    scene d4_dj_cat_0 with Dissolve(.5)
    stop test_two fadeout 0.5
    "Я наклонился, чтобы получше рассмотреть свернувшуюся у батареи кошку."
    voice "voice/anton/4day/125. Pr.ogg"
    Ant "Привет, Джоанна."

    play sound "sounds/sfx_cat_hiss.ogg"

    scene d4_dj_cat with Dissolve(.5)
    "Кошка ударила хвостом по ребристой батарее. Зашипела, показав клыки."
    play test_two "sounds/steps/Anton-steps-steal-1.ogg" 

    scene d4_polroom_bg
    show d4_polroom_piano
    show d4_polroom_cat
    show d4_polroom_poster
    show Polina 3_4 m_day 08 worry ahead 01:
        yoffset 30
    with Dissolve(.5)

    show Polina 3_4 m_day 08 worry ahead 02 with Dissolve(.15)
    stop test_two fadeout 0.9
    play music "music/29_Polina.ogg" volume 0.7 fadein 2
    voice "voice/Polina/4day/73 Pro.ogg"
    Pol "Прости, она не особо дружелюбна."

    scene d4_polroom_magic_bg:
        yalign 0.
    show Polina Large b_day 01 norm ahead 03
    with Dissolve(.5)

    voice "voice/anton/4day/125.K.ogg"
    Ant "К такой реакции я привык."
    voice "voice/anton/4day/126.Ch.ogg"
    Ant "Что за имя — Джоанна?"
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/74 Te.ogg"
    Pol "Тебе не надоело говорить про имена?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    $ add_text_to_dictionary(44)
    voice "voice/Polina/4day/75 D.ogg"
    Pol "Джоанна — из сериала «{u}Элен и ребята{/u}». Смотрел?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    play test_three "voice/anton/4day/127.Fir.ogg"
    "Я фыркнул."
    voice "voice/anton/4day/128. Et.ogg"
    Ant "Это для девочек!"
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/76 Oi.ogg"
    Pol "Ой, подумаешь. Я вот и «Трансформеров» смотрю."
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/129.Da .ogg"
    Ant "Да ладно! Кто твой любимчик?"
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/77 T.ogg"
    Pol "Ты меня проверяешь? Допустим, Мегатрон."
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/130. A.ogg"
    Ant "Ага! А говорила, что не любишь плохих парней."
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/78 Da.ogg"
    Pol "Да, но вот ему удалось растопить моё сердечко!"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    "Она комично схватилась за грудь."

    if Flags.Has("betray"):
        voice "voice/anton/4day/131. tiz.ogg" 
        Ant "Ты знала, что Оптимус и Мегатрон были друзьями и боролись вместе против руководства Кибертрона?"
        voice "voice/anton/4day/131.No .ogg"
        Ant "Но после того, как лидером избрали Оптимуса, Мегатрон перешёл на тёмную сторону."
        show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
        voice "voice/Polina/4day/80 Bo.ogg"
        Pol "Боюсь, что у тебя с Пятифановым повторится та же история."
        show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
        "Я удивлённо вскинул брови."
        voice "voice/anton/4day/132. Nu.ogg"
        Ant "Ну лидером меня никто не выбирал."
        show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
        voice "voice/Polina/4day/81 Do.ogg"
        Pol "Допустим, я выбрала."
        show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
        "Я, кажется, снова покраснел."

    play sound "sounds/sfx_coach_fall_on.ogg" volume 0.6
    hide Polina with Dissolve(.5)
    "Полина села на диван, болтая изящной ножкой, и поправила покрывало."

    scene d4_polroom_bg
    show d4_polroom_piano
    show d4_polroom_cat
    show d4_polroom_poster
    show Polina Front m_day 02 norm ahead 01:
        xoffset -150
        yoffset 30
    with Dissolve(.5)

    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)

    voice "voice/Polina/4day/02 Chem.ogg"
    Pol "Чем займёмся?"

    "Её поза и игривый взгляд как будто загипнотизировали меня."
    "Вдобавок приглушённый свет создавал в комнате особую, волнительную атмосферу."
    play test_four "voice/anton/2day/Vdoh.ogg"
    "В воздухе чувствовался лёгкий аромат ежевики и чего-то ещё более неуловимого и пленительного."

    scene d4_polroom_magic_bg:
        yalign 0.
    show Ant b_day
    show ant_clas_m4
    with Dissolve(.5)

    "Неожиданно моё привычное смущение сменилось каким-то необычайным задором."
    "Хотелось красоваться и хвастаться, в общем, делать что угодно, лишь бы Полина смотрела на меня как можно дольше."
    "Я ощущал себя этаким агентом 007, готовым вот-вот соблазнить роковую красотку одним лишь своим видом."
    "Будто подражая герою шпионских фильмов, я скрестил руки на груди и, таинственно улыбаясь, решил опереться о стену."
    "В этот миг я сам себе казался обворожительным."

    scene d4_polroom_magic_bg:
        yalign 0.
    show day3_ant_clas_anton 3:
        .25
        linear .25 yoffset 20
    with Dissolve(.25)

    play sound "sounds/sfx_piano_sit.ogg"
    stop music fadeout 0.5
    "Вот только застыть в изящной позе мне помешало бряцанье клавиш: оказывается, я не заметил открытое пианино и уселся на него."
    play test_three "voice/anton/4day/39 Ai.ogg"

    scene d4_piano 1 with Dissolve(.5):
        zoom 1.01

    play test_five "sounds/caricature14.ogg"
    "Подпрыгнув от испуга чуть ли не до потолка, я растерял всё своё обаяние."

    play test_three "sounds/sfx_piano_lid_slam.ogg"

    scene d4_piano:
        zoom 1.01
    "Следом с грохотом захлопнулась крышка инструмента."

    play sound "sounds/sfx_stand_up_quick.ogg"
    play test_six "voice/Polina/4day/03Vz.ogg"
    play sound "sounds/sfx_cat_jump.ogg"
    "Тут же со стула сиганула перепуганная Джоанна."

    play test_one "sounds/sfx_cat_running_1.ogg"
    scene d4_poster_close with Dissolve(.5)

    "Кошка рванула вверх по шторе, а затем, сдирая когтями стружку обоев, метнулась по стене в укрытие на шифоньере."

    window hide
    play sound "sounds/sfx_cat_running_2_tearing.ogg"
    scene d4_poster_buster
    pause 1.1
    window show
    play music "music/Buried In The Sands.ogg" 
    "К моим ногам полетели клочки изорванного постера с «Сейлор Мун», так некстати оказавшегося на пути испуганного животного."
    play test_six "voice/Polina/4day/04 Ah.ogg"
    "И судя по взгляду Полины, плакат ей очень нравился."

    scene d4_polfon
    show Ant ouch 2
    with Dissolve(.5)

    voice "voice/anton/4day/40 Pro.ogg"
    Ant "П-прости. Я не хотел."

    $ story_manager.MarkEvent(("day4", "scene_ph5"))

    scene d4_polroom_magic_bg:
        yalign 0
    show Polina Large b_day 01 sad ahead 05
    with Dissolve(.5)

    show Polina_sad close
    play test_six "voice/Polina/4day/04 Eh.ogg"
    "Она закрыла глаза, губы её скривились, а лоб сморщился."
    "Казалось, сейчас Полина начнёт кричать или заплачет, но она просто выдохнула и совершенно спокойно сказала:"

    show Polina_sad open
    pause .3
    show Polina Large b_day 01 sad ahead 06 with Dissolve(.5)
    voice "voice/Polina/4day/05Ne.ogg"
    Pol "Не беда."
    show Polina Large b_day 01 sad ahead 05 with Dissolve(.5)
    show Polina Large b_day 01 sad ahead 06 with Dissolve(.5)
    voice "voice/Polina/4day/06 Net.ogg"
    Pol "Нет такой поломки, которую нельзя починить с помощью изоленты."
    show Polina Large b_day 01 sad ahead 05 with Dissolve(.5)
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.5)
    voice "voice/Polina/4day/07 Nu.ogg"
    Pol "Ну, в этом случае с помощью скотча."
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.5)
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.5)
    voice "voice/Polina/4day/08Dav.ogg"
    Pol "Давай помогай."
    stop music fadeout 3.5
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.5)


    play music2 "music/46_Romantic piano melody.ogg" fadein 0.5
    window hide
    call zigzag_prepare from _call_zigzag_prepare

    $ renpy.stop_predict("d4_dj_cat")
    $ renpy.stop_predict("d4_dj_cat_0")
    $ renpy.stop_predict("d4_piano")
    $ renpy.stop_predict("d4_piano 1")
    $ renpy.stop_predict("d4_poster_close")
    $ renpy.stop_predict("d4_poster_buster")
    show screen puzzle_cipher(puzzle, debug=False)
    with Dissolve(.5)

    call screen puzzle_cipher(puzzle, debug=False)

    label d4_polhouse_followup2.solved:


    play sound "sounds/curtain-3.ogg"
    $ story_manager.MarkEvent(("day4", "game poster"))
    $ story_manager.MarkEvent(("day4", "game poster", "solve"))
    show screen puzzle_static(puzzle)
    with None

    $ renpy.start_predict("d4_polroom_magic_bg")
    $ renpy.start_predict("d4_polroom_magic_polina_norm")
    $ renpy.start_predict("d4_polroom_magic_polina_light")
    $ renpy.start_predict("showB1")
    $ renpy.start_predict("showB2")
    $ renpy.start_predict("showB3")
    $ renpy.start_predict("d4_dj_bg")
    $ renpy.start_predict("d4_dj_scream")
    $ renpy.start_predict("d4_dj 1")
    $ renpy.start_predict("d4_dj 2")
    $ renpy.start_predict("d4_dj 3")
    $ renpy.start_predict("d4_dj 4")
    $ renpy.start_predict("d4_cat_stani")


    scene d4_polroom_bg
    show Polina Front m_day 02 norm ahead 01:
        xoffset -150
        yoffset 30

    window show
    "Последний кусочек плаката лёг на своё место, и показалось, что вместе с ним в комнате воцарилась утраченная гармония."

    $ music_during_lines = 0.5
    voice "voice/anton/4day/42 Eto.ogg"
    Ant "Это же персонаж из «Сейлор Мун»? Сейлор Юпитер, или как там её?" id d4_polhouse_followup2_solved_5449d1a1
    voice "voice/Polina/4day/09 Da.ogg"
    Pol "Да нет же! Это Сейлор Сатурн!"
    voice "voice/Polina/4day/10 EE.ogg"
    Pol "Её зовут Хотару, она воин разрушения, который, вместо того, чтобы уничтожить мир, спасла его."
    voice "voice/Polina/4day/11 Mne.ogg"
    Pol "Мне она всегда больше всех нравилась!"
    voice "voice/Polina/4day/12 Vot.ogg"
    Pol "Во-о-от... А ещё у неё раздвоение личности, представляешь?"
    voice "voice/Polina/4day/13 Po.ogg"
    Pol "По крайней мере, было. Джоанна порвала её на дюжину личностей, не меньше!"

    $ Hide("puzzle_static", transition=Dissolve(.5))()

    "Я посмотрел на Полину и осторожно спросил:"
    voice "voice/anton/4day/133. Ra.ogg"
    Ant "Расскажи, как проходят твои вечера?" id d4_polhouse_followup2_solved_c7771044

    "Полина пожала плечами, приняв скучающий вид."
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/83 Sm.ogg"
    Pol "Смотрю телевизор или играю дедушке на скрипке."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    $ add_text_to_dictionary(45)
    voice "voice/Polina/4day/84 On.ogg"
    Pol "Он планирует сделать из меня {u}Давида Ойстраха{/u}."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/134. Ko.ogg"
    Ant "Кого?"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/85 Sk.ogg"
    Pol "Скрипач был такой великий."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/135. Ati.ogg"
    Ant "А ты что же, сама не хочешь играть?"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/86 Po.ogg"
    Pol "Почему? Хочу."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/87 Eto.ogg"
    Pol "Это мой шанс уехать в город и начать нормальную жизнь."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/88 Ga.ogg"
    Pol "Гастролировать по странам, знакомиться с новыми людьми."
    $ music_during_lines = 1.0
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    "От её слов я ощутил укол дурацкой ревности."
    stop music2 fadeout 3.5
    voice "voice/anton/4day/136. Po.ogg"
    Ant "Поиграешь для меня?"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    play music "music/11 Empty Road.ogg" fadein 1.5
    voice "voice/Polina/4day/89 Ti.ogg"
    Pol "Ты точно этого хочешь?"
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/137. Oche.ogg"
    Ant "Очень!"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/90 Hor.ogg"
    Pol "Хорошо... Только учти: я сегодня не в форме."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)

    play sound "sounds/sfx_violin_case.ogg"

    "Она извлекла скрипку из футляра. Лак переливался в свете лампы."
    $ music_during_lines = 0.8
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/91 Et.ogg"
    Pol "Это не обычная скрипка."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/92 Ee.ogg"
    Pol "Её смастерил в семнадцатом веке скрипичных дел мастер Гварнери, а сам Ойстрах дал на ней первый концерт."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/138. Ona.ogg"
    Ant "Она дорогая?"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/93 Nu.ogg"
    Pol "Ну, пару миллионов долларов стоит."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    "У меня отвисла челюсть. Полина рассмеялась."
    show Polina Front m_day 02 norm ahead 05 with Dissolve(.15):
        .25
        parallel:
            "Polina Front m_day 02 smile ahead 014" with Dissolve(.15)
        parallel:
            linear .2 yoffset 20 +30
            linear .2 yoffset 0 +30
            repeat 2
        "Polina Front m_day 02 norm ahead 05" with Dissolve(.15)
        .25
        "Polina Front m_day 02 smile ahead 014" with Dissolve(.15)

    voice "voice/Polina/4day/94 Vi.ogg"
    Pol "Видел бы ты своё лицо!"
    show Polina Front m_day 02 smile ahead 05 with Dissolve(.15)
    show Polina Front m_day 02 smile ahead 014 with Dissolve(.15)
    voice "voice/Polina/4day/95 Ya.ogg"
    Pol "Я шучу! Копейки она стоит."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/96 E.ogg"
    Pol "Если бы у меня была скрипка Гварнери, я бы жила в Москве."
    show Polina Front m_day 02 norm ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/139. A.ogg"
    Ant "А я и не повёлся!"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/97 Ko.ogg"
    Pol "Конечно-конечно."
    $ music_during_lines = 1.0
    stop music fadeout 3.5

    show d4_polroom_polina_play
    with Dissolve(.5)

    "Полина приняла нужную позу, зажала скрипку между плечом и скулой. Поднесла смычок."
    voice "voice/Polina/4day/98 Fa.ogg"
    Pol "Фа диез минор."
    play music "music/Schumann - Sonata_No.1_Polina_violin&piano.ogg"

    scene d4_polroom_magic_bg:
        yalign 1.
        matrixcolor BrightnessMatrix(0.)
        parallel:
            linear 12 yalign 0.
        parallel:
            easeout 12. matrixcolor BrightnessMatrix(1.)
    show d4_polroom_magic_polina_norm:
        yalign 1.
        parallel:
            linear 12 yalign 0.
        parallel:
            "d4_polroom_magic_polina_light" with Dissolve(12)
    show showB1
    show showB2
    show showB3
    with Dissolve(.5)

    $ story_manager.MarkEvent(("day4", "scene_ph6"))

    "Смычок скользнул по струнам — и музыка наполнила комнату, насытила собой воздух."
    "Я присел на подоконник, восторгаясь силой мелодии."
    "Как грациозно играла Полина!"
    "Смычок буквально летал, разрезая пространство и время."
    "Длинные пальцы перемещались с невероятной скоростью. Призрачная улыбка теплилась на губах скрипачки."
    "Казалось, музыка, этот таинственный фа диез минор, – ветер, ворвавшийся в дом, принёсший запах моря и далёких городов."
    "И при его порывах я задыхался от восторга."
    "Мелодия подняла меня до небес, заставив вспомнить ночные прыжки над лесом."
    window hide

    scene d4_polroom_magic_bg:
        yalign 0.
        matrixcolor BrightnessMatrix(1.)
        linear 3. matrixcolor BrightnessMatrix(0.)
    show d4_polroom_magic_polina_light:
        yalign 0.
        "d4_polroom_magic_polina_norm" with Dissolve(3.)
    with Dissolve(1.5)

    window show
    "Но, как и всё хорошее, она закончилась слишком быстро."
    stop music fadeout 3.5
    "Полина замерла, опустила руку и поклонилась. Качнулся водопад благоухающих волос."

    scene d4_polvata_floor
    show d4_ant_feet 1
    show d4_dj 4
    with Dissolve(.5)

    play sound "sounds/sfx_footstep_carpet_1.ogg"


    show d4_ant_feet 2
    with Dissolve(.5)

    "Я вскочил, захлопав в ладоши."

    scene d4_polroom_bg
    show Polina Front m_day 02 norm ahead 01:
        xoffset -150
        yoffset 30
    with Dissolve(.5)

    voice "voice/anton/4day/140. Br.ogg"
    Ant "Браво! Кто это сочинил?"
    show Polina Front m_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/100 Rob.ogg"
    Pol "Роберт Шуман."

    scene d4_polfon
    show Ant b_day
    show ant_clas_m4
    with Dissolve(.5)

    hide ant_clas_m4
    show ant_clas_m7
    with Dissolve(.25)

    play test_one "sounds/Victory1.ogg"
    voice "voice/anton/4day/141. Vot.ogg"
    Ant "Вот кто теперь мой любимый композитор! Бра..."

    hide ant_clas_m7
    show Ant ouch 1:
        zoom .85
    with Dissolve(.15)

    play test_six "sounds/Fail2.ogg"
    play test_three "voice/anton/4day/Vo.ogg"
    "Слог «во» стал возгласом изумления, когда что-то яростно взвыло под моей ногой."
    play test_six "sounds/FaiL_su.ogg"


    show d4_dj_bg:
        yalign 0.
        linear .35 yalign 1.

        pause .25
        yalign 0.
        xalign .5
        linear .35 yalign 1.

        pause .25
        yalign 0.
        xalign .5
        linear .35 yalign 1.

    show d4_dj_scream:
        ypos 1.
        yanchor .5
        xalign .5
        linear .35 yanchor 1.

        pause .25
        yanchor .5
        xalign .5
        linear .35 yanchor 1.

        pause .25
        yanchor .5
        xalign .5
        linear .35 yanchor 1.

    play test_three "sounds/sfx_cat_cry.ogg"

    "Джоанна!"

    window hide
    scene d4_polvata_floor
    show d4_dj 3

    show layer master:
        align (1., .0)
        zoom 2.0
        .5
        linear .25 align (.5, 1.)
    with Dissolve(.15)

    pause .5
    play test_two"sounds/Fail9.ogg"
    "В порыве восхищения я позабыл про кошку и нечаянно наступил ей на хвост."


    show d4_dj 2
    show layer master:
        align (.5, 1.)
        zoom 2.0
        .25
        linear .25 zoom 1.0

    "Я не успел озвучить слова извинений."

    play test_three "sounds/sfx_cat_attack_2.ogg"
    play test_one "sounds/Fail8.ogg"
    scene d4_cat_stani
    with Dissolve(.15)
    pause .5
    window show

    "Джоанна взвилась по моей ноге и вцепилась в бедро. Сквозь штанины острые когти пронзили кожу."

    scene d4_polfon:
        align (.5, .5)
        zoom 1.02
    show Ant ouch 1:
        yoffset 30
    with Dissolve(.15)

    voice "voice/anton/4day/142. Ai.ogg"
    Ant "Ай-ай!"

    play sound "sounds/sfx_cat_kick.ogg"

    scene d4_polfon:
        align (.5, .5)
        zoom 1.02
    show Ant ouch 1:
        yoffset 30
    with vpunch

    "Полина кинулась на помощь, шлёпнула кошку по загривку."

    scene d4_polroom_magic_bg:
        yalign 0
    show Polina Scream b_day 01 norm ahead 03
    with Dissolve(.5)

    play test_one "sounds/Fail4.ogg"
    voice "voice/Polina/4day/101 D.ogg"
    Pol "Джоанна, гадость какая, брысь!"

    play sound "sounds/sfx_cat_running_3_away.ogg"

    show Polina Scream b_day 01 norm ahead 01 with Dissolve(.5)
    "Кошка сиганула на ковёр и ретировалась из комнаты, лапой отворив дверь."

    scene d4_polfon
    show Ant ouch 2
    with Dissolve(.5)
    play test_three "voice/anton/4day/142. Ai2.ogg"
    "Я морщился, трогая бедро, явно хорошенько расцарапанное."

    play music "music/11_Poryadok.ogg" volume 0.65 fadein 0.5
    "Полина сочувственно приобняла меня."

    play sound "sounds/sfx_hugs.ogg"

    scene d4_polroom_magic_bg:
        yalign 0
    show Polina Large b_day 01 sad aside 01
    show d4_polant
    with Dissolve(.5)
    show d4_polhand with Dissolve(1.)

    show Polina Large b_day 01 sad aside 02 with Dissolve(.15)
    voice "voice/Polina/4day/Bolno.ogg"
    Pol "Больно?"
    show Polina Large b_day 01 sad aside 01 with Dissolve(.15)
    voice "voice/anton/4day/143. Da.ogg"
    Ant "Да так... Я сам виноват."
    show Polina Large b_day 01 angry ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/102 Ya.ogg"
    Pol "Ой, я ей покажу, как бросаться на моих гостей!"

    play sound "sounds/sfx_coach_fall_on.ogg"

    scene d4_polstani
    with Dissolve(.5)

    "Меня волновала не столько боль, сколько ущерб, нанесённый одежде. Мелкие дырочки испещрили штаны."
    "М-да. Мама будет счастлива."
    "Но внимание Полины мне польстило."
    voice "voice/anton/4day/144.Tv .ogg"
    Ant "Твоя Джоанна – дама с характером."

    scene d4_polroom_bg
    show Polina Front b_day 02 norm ahead 01:
        yoffset 10
    with Dissolve(.5)

    show Polina Front b_day 02 norm ahead 02 with Dissolve(.35)
    voice "voice/Polina/4day/103 Vi.ogg"
    Pol "Вы поладите."
    show Polina Front b_day 02 norm ahead 01 with Dissolve(.15)
    show Polina Front b_day 02 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/104 Es.ogg"
    Pol "Если ты не умрёшь от потери крови, конечно."
    show Polina Front b_day 02 norm aside 01 with Dissolve(.15)
    "Она повертелась, осматривая комнату."

    play test_three "sounds/loop_footsteps_home_light_one.ogg" fadein 0.3
    $ renpy.music.set_pan(0.3, delay=2, channel="test_three")

    show Polina Front b_day 02 norm ahead 02:
        align (.5, 1.)
        yoffset 10
        parallel:
            linear 1 xoffset 200
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat
    show d4_polroom_bg as hider:
        alpha 0
        .25
        linear .5 alpha 1

    pause 1
    stop test_three fadeout 1.2

    voice "voice/Polina/4day/105 Gd.ogg"
    Pol "Где-то тут был йод."
    voice "voice/anton/4day/145. Ne.ogg"
    Ant "Необязательно..."
    voice "voice/Polina/4day/106 Ch.ogg"
    Pol "Что значит «необязательно»?"
    stop music fadeout 3.5
    voice "voice/Polina/4day/107 Esh.ogg"
    Pol "Ещё никто не умирал в моей спальне. И я хочу, чтобы так продолжалось впредь."
    play music2 "music/30_(Tiny_Bunny).ogg" fadein 0.5
    voice "voice/Polina/4day/108 Sn.ogg"
    Pol "Снимай пока штаны."


    $ renpy.stop_predict("d4_polroom_magic_polina_norm")
    $ renpy.stop_predict("d4_polroom_magic_polina_light")
    $ renpy.stop_predict("showB1")
    $ renpy.stop_predict("showB2")
    $ renpy.stop_predict("showB3")
    $ renpy.stop_predict("d4_dj_bg")
    $ renpy.stop_predict("d4_dj_scream")
    $ renpy.stop_predict("d4_dj 1")
    $ renpy.stop_predict("d4_dj 2")
    $ renpy.stop_predict("d4_dj 3")
    $ renpy.stop_predict("d4_dj 4")
    $ renpy.stop_predict("d4_cat_stani")

    scene d4_polfon
    show ant_clas_1 1
    with Dissolve(.5)

    pause .25

    hide ant_clas_1
    show day3_ant_clas_anton 3:
        xoffset 50
    with Dissolve(.5)
    "Я вообразил себя перед Полиной в одних трусах."
    "Как она, нагнувшись, обрабатывает рану. Образ окатил горячим паром."
    play test_three "sounds/sfx_footsteps_two_carpet.ogg"

    scene d4_polroom_magic_bg:
        yalign 0
    show Polina Large b_day 01 norm ahead 03
    with Dissolve(.5)
    $ music_during_lines = 0.75
    voice "voice/anton/4day/145. Nen.ogg"
    Ant "Не надо, Полин. Ну правда."

    play sound "sounds/sfx_flask_open.ogg"

    show Polina Large b_day 01 angry ahead 03 with Dissolve(.5)
    "Не слушая меня, она смочила вату коричневатой жидкостью из пахучего флакончика."

    play sound "sounds/sfx_rustle_clothes_light_2.ogg"

    show d4_polvata with Dissolve(.5)
    show Polina Large b_day 01 angry ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/109 Pa.ogg"
    Pol "Пациент, я готова. Спускайте."
    show Polina Large b_day 01 angry ahead 03 with Dissolve(.15)
    voice "voice/anton/4day/146. Se.ogg"
    Ant "С-серьёзно. Дома промою..."

    show Polina Large b_day 01 angry2 ahead 01 with Dissolve(.15)
    "Улыбка стёрлась с её красивых губ. Вертикальная морщинка рассекла переносицу. В голосе появились капризные нотки."
    show Polina Large b_day 01 angry2 ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/110 P.ogg"
    Pol "Перестань сопротивляться. Дай я тебе помогу."
    show Polina Large b_day 01 angry2 ahead 01 with Dissolve(.15)
    "Она погладила меня значительно ниже раны."
    show Polina Large b_day 01 angry2 ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/111 De.ogg"
    Pol "Девочкам нельзя отказывать."
    show Polina Large b_day 01 angry2 ahead 01 with Dissolve(.15)

    scene d4_polvata_floor:
        zoom 1.02
        align (.5, 1.)
    show d4_ant_feet 1
    with Dissolve(.5)

    pause .5

    play sound "sounds/sfx_footstep_carpet_2.ogg"

    show d4_pol_feet 1 with Dissolve(.5)
    $ story_manager.MarkEvent(("day4", "scene_ph7"))
    "Полина решительно шагнула вперёд и схватилась за пряжку ремня."

    show d4_ant_feet 1:
        xzoom -1
        xoffset 500
    with Dissolve(.5)

    play sound "sounds/sfx_footstep_carpet_3.ogg"

    play test_three "voice/anton/4day/147. Ah2.ogg"
    "Я увернулся, но не тут-то было."

    play sound "sounds/sfx_belt_clothes.ogg"
    play test_five "sounds/sfx_footstep_carpet_4.ogg"


    show d4_pol_feet 2 behind d4_ant_feet
    with Dissolve(.5)

    play test_six "voice/Polina/4day/112 eh.ogg" 
    play test_three "voice/anton/4day/147. Ah3.ogg"
    "Девочка очутилась сзади. Поддела ремень пальцами, попробовала стащить штаны."

    play sound "sounds/sfx_footstep_carpet_5.ogg"

    show d4_ant_feet 5:
        xzoom 1
        xoffset 0

    with hpunch

    show d4_ant_feet 1:
        xzoom -1
        xoffset 500
    with Dissolve(.5)

    play test_six "voice/Polina/4day/112 Nu.ogg" 
    voice "voice/anton/4day/147. Ah.ogg"
    Ant "Ах ты ж!"
    play test_six "voice/Polina/4day/112 Ha.ogg"
    "Она захихикала."

    play sound "sounds/sfx_footstep_carpet_6.ogg"

    show d4_ant_feet 1 behind d4_pol_feet:
        xzoom 1
        xoffset -300
    show d4_pol_feet 3
    with Dissolve(.5)
    play test_six "voice/Polina/4day/112 Hi.ogg" 
    play test_three "voice/anton/4day/147. Ah4.ogg"
    "Я крутанулся, и Полина прижалась ко мне, заливаясь смехом."

    scene d4_polvata_floor:
        zoom 1.02
        align (.5, 1.)
    show d4_ant_feet 1:
        xzoom 1
        xoffset -300
    show d4_pol_feet 3
    with hpunch

    play sound "sounds/sfx_footstep_carpet_7.ogg"

    play test_six "voice/Polina/4day/112 Ag.ogg"
    play test_three "voice/anton/4day/147. Ah5.ogg"
    "Легонько прикусила мою руку, дёрнула за ремень."


    show d4_ant_feet 5:
        xzoom -1
        xoffset 250
        yoffset 20
        easein 3. xoffset 50
    show d4_pol_feet 1:
        xoffset -250
        easein 4. xoffset -400
    with Dissolve(.5)
    show bg_black:
        alpha 0
        1.
        linear .5 alpha 1
    play test_six "voice/Polina/4day/112 Haa.ogg" 
    play test_three "voice/anton/4day/147. Ah6.ogg"


    play test_two "sounds/sfx_fall.ogg"

    "Отступая, я врезался в диван и упал плашмя на его мягкую поверхность. Полина приземлилась сверху."
    play sound "sounds/sfx_coat_rustle_1.ogg"

    play test_five "sounds/sfx_rustle_clothes_light_3.ogg"

    scene d4_polup:
        xzoom -1
    show Polina Up b_day 01 norm ahead 01:
        xzoom -1
        ypos 1.
        xpos .0
        xanchor 0.5
        yanchor 0.75
        linear 1 yanchor 1. xanchor .0
    with Dissolve(.5)

    play test_three "voice/anton/4day/147. Ah7.ogg"
    "Волосы накрыли моё лицо, защекотали ноздри."

    show Polina Up b_day 03 norm ahead 03 with Dissolve(.25)

    play test_six "voice/Polina/4day/112 Haha.ogg"
    "Я ощущал, как вибрирует грудная клетка смеющейся Полины."
    play test_three "voice/anton/4day/148. Ti2.ogg"
    "А ещё я чувствовал сквозняк голой кожей бёдер."
    play test_six "voice/Polina/4day/112 H.ogg" 
    $ music_during_lines = 1.0
    "Ей таки удалось стянуть с меня штаны: я лежал под ней частично нагим и сгорал от смущения."

    play sound "sounds/sfx_bed_rustle_loud.ogg"

    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    show Polina Up b_day 03 norm aside 01:
        ypos 1.
        xpos .0
        xanchor .0
        yanchor 1.
        linear 1 yanchor .9375 xanchor (1. - .8750)

    stop music2 fadeout 2
    "Полина отстранилась. Смех затих."

    play sound "sounds/sfx_mouth_blow.ogg" volume 0.5 

    play music "music/Love theme.ogg" volume 0.85
    "Она сдула прядь волос и заглянула в мои глаза."
    "Уперев кулачок в щёку, прошла задумчивым взглядом по моему лицу."
    voice "voice/anton/4day/148. Ti.ogg"
    Ant "Ты чего?"

    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/113 Ni.ogg" 
    Pol "Ничего. Красивый ты."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    voice "voice/anton/4day/149. Sk.ogg"
    Ant "Скажешь тоже."
    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/114 Che.ogg" 
    Pol "Честно-честно."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/115 E.ogg" 
    Pol "И знаешь, мне кажется, что я все эти годы ждала, когда ты в посёлок приедешь."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)

    play test_six "sounds/loop_heartbeat_fast_light.ogg" fadein 0.8 loop

    "Моё сердце выстукивало бешеный ритм: под рёбрами, в висках, по всему телу."
    "Я забыл, что лежу под ней без штанов и трусь голым бедром об её ногу."
    stop test_six fadeout 5
    voice "voice/anton/4day/150. Mne.ogg"
    Ant "Мне хорошо с тобой."
    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/116 Em.ogg" 
    Pol "И мне."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/117 Ya.ogg"
    Pol "Я встретила человека, который меня понимает."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    show Polina Up b_day 03 norm aside 02 with Dissolve(.25)
    voice "voice/Polina/4day/118 Eto.ogg"
    Pol "Это дороже скрипки Гварнери."
    show Polina Up b_day 03 norm aside 01 with Dissolve(.25)
    "Я переместил взгляд на её рот."
    "Он был так близко, что я видел каждую крошечную морщинку на пересохших, как и у меня, губах."


    window hide
    call screen day4_polina_kiss



label d4_polhouse_choice_kiss:
    $ story_manager.MarkEvent(("day4", "scene_ph8"))
    stop music fadeout 1.5
    play music2 "music/Romantic Piano Story.ogg" fadein 0.5
    play sound "sounds/sfx_bed_rustle_loud.ogg"

    window show
    scene d4_polup:
        xzoom -1
    show d4_polina_kiss_full:
        xzoom -1
        pos (.0, 1.)
        yanchor .9375
        xanchor (1. - .8750)
        linear 1. xanchor .0 yanchor 1.
    show bg_black:
        alpha 0
        .5
        linear 1. alpha 1
    "Полина опустила веки. Затрепетали ресницы."

    show d4_polina_kiss_kiss:
        xzoom -1
        xalign .0
        alpha 0
        linear 2.5 alpha 1

    play test_six "voice/Polina/4day/119 ACMP1.ogg"
    play test_three "voice/anton/4day/151. Kiss.ogg"
    "Наши губы соприкоснулись."

    play sound "sounds/sfx_bed_rustle_quiet.ogg"

    show d4_polina_kiss_kiss:
        xzoom -1
        subpixel True
        xalign 0.
        parallel:
            linear 8 xalign 1.
        parallel:
            linear .5 alpha 1

    show d4_polina_kiss_eyes 0:
        xzoom -1
        subpixel True
        xalign 0.
        alpha 0
        parallel:
            linear 8 xalign 1.
        parallel:
            linear .5 alpha 1

    play test_six "voice/Polina/4day/119 ACMP2.ogg"   
    "Голова закружилась. Померещилось, что я падаю в пропасть."

    show d4_polina_kiss_eyes 1 with Dissolve(1.)

    play test_six "voice/Polina/4day/119 ACMP3.ogg"
    "Каждая клеточка моего тела пела от восторга, словно я пробовал на вкус прекраснейшую музыку, но дегустировал нечто более совершенное, чем мелодия Шумана."

    scene d4_polina_kiss_kiss:
        xalign 1.
        xzoom -1
    show d4_polina_kiss_eyes 2:
        xalign 1.
        xzoom -1
    with Dissolve(.15)
    "И тут я увидел зеркало на дверцах платяного шкафа."
    stop music2 fadeout 0.5

    scene d4_polina_kiss_kiss_crop:
        xzoom -1
        xalign 1-.285
        yalign .48
        zoom 1.2
    show d4_polina_kiss_eyes 3:
        xzoom -1
        xalign 1-.285
        yalign .48
        zoom 1.2
    show focus_line:
        align (.5,.5)
        alpha 0
        .35
        alpha 1
        .25
        linear .25 alpha 0
    with Dissolve(.15)

    jump d4_polhouse_after



label d4_polhouse_after:
    $ story_manager.MarkEvent(("day4", "scene_ph9"))
    play test_one "sounds/sub-drum-4.ogg"
    "Там отражалась приоткрытая дверь, нутро коридора."
    play music "music/Phrases_06(loop).ogg" fadein 1


    scene d4_polhar_witness 2
    stop test_three fadeout 1
    "Из щели за нами следил Харитон."
    "Хмурое лицо будто плавало в чёрных водах темноты. Глаза впились в меня – глубже и злее, чем кошачьи когти."
    stop test_six fadeout 3
    "Рассекреченный старик дал задний ход, отъехал от двери и канул в варево теней."
    stop music fadeout 4
    window hide

    play sound "sounds/sfx_wheelchair_going_away.ogg"

    scene d4_polhar_witness 1 with Dissolve(.5)
    scene d4_polhar_witness 3 with Dissolve(.5)
    scene d4_polhar_bg with Dissolve(.5)

    window show
    "Поражённый, я оторвался от Полининых губ. Прервал сладкий поцелуй."
    play test_three "sounds/sfx_bed_rustle_loud.ogg"

    scene d4_polup:
        xzoom -1
    show Polina Up b_day 01 norm ahead 01:
        xzoom -1
        ypos 1.
        xpos .0
        xanchor 1-.9375
        yanchor .96875
        linear .5 yanchor .9375 xanchor 1-.8750
    with Dissolve(.5)

    play test_six "voice/Polina/4day/121 A.ogg"
    "Полина посмотрела на меня непонимающе и раздосадованно спросила:"

    show Polina Up b_day 01 norm ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/120 V.ogg"
    Pol "В чём дело?"

    play sound "sounds/sfx_bed_Anton_up.ogg"

    scene d4_polvata_floor
    show d4_ant_feet 1:
        alpha 0
        pause 1.
        linear .5 alpha 1
    with Dissolve(.5)
    play music2 "music/9_Nikita Kryukov - the Obscurity.ogg" fadein 1
    play test_six "voice/Polina/4day/121 Vid.ogg"   
    play sound "sounds/sfx_get_up_dressing.ogg"
    "Я выпутался из-под неё, встал, натягивая штаны, с третьего раза застегнул ремень."

    voice "voice/anton/4day/152. Ni.ogg"
    Ant "Ни в чём."
    voice "voice/anton/4day/152. Ya.ogg"
    Ant "Я вспомнил просто... Пообещал маме вернуться к ужину."

    scene d4_polroom_magic_bg:
        yalign 0.
    show Polina 3_4 b_day 01 worry ahead 012
    with Dissolve(.5)
    voice "voice/Polina/4day/122 Ni.ogg"
    Pol "Не уходи."
    show Polina 3_4 b_day 01 worry ahead 011 with Dissolve(.15)
    voice "voice/anton/4day/153. Po.ogg"
    Ant "Полин, послушай..."
    show Polina Cry b_day 01 fine ahead 02 with Dissolve(.5)
    voice "voice/Polina/4day/123 Ne.ogg"
    Pol "Не уходи, Тош!"

    show Polina Cry b_day 01 cry ahead 01 with Dissolve(.5):
        block:
            linear .07 yoffset 5 xoffset 5
            linear .07 yoffset 0 xoffset 0
            repeat 4
        1.5
        repeat
    stop music2 fadeout 3.5
    play music "music/SilentWhispering.ogg" fadein 3.5
    play test_six "voice/Polina/4day/124 kh.ogg"
    "Голос задрожал. Слёзы потекли по щекам серебристыми ручейками."
    "Я оцепенел от неожиданности."
    play test_six "voice/Polina/4day/126 Hnik3.ogg"
    "Настроение Полины сменилось моментально — так же, как и тема в монологе её деда."
    "Но ведь дед был старым и чудным..."
    show Polina Cry b_day 01 cry ahead 02 with Dissolve(.15)
    $ music_during_lines = 0.75
    voice "voice/Polina/4day/124 Za.ogg"
    Pol "Забери меня с собой!"
    show Polina Cry b_day 01 cry ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/154. T.ogg"
    Ant "Ты чего, Полин? Ну перестань!"
    play test_six "voice/Polina/4day/126 Hnik4.ogg"
    "Я обеспокоенно склонился к ней."
    voice "voice/anton/4day/155. Nu.ogg"
    Ant "Ну хватит, правда. Всё же хорошо."
    show Polina Cry b_day 01 cry ahead 02 with Dissolve(.15)
    voice "voice/Polina/4day/125 Ya.ogg"
    Pol "Я здесь с ума сойду! Не знаю... Руки на себя наложу!"
    show Polina Cry b_day 01 cry ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/156. Ne.ogg"
    Ant "Не говори так!"

    play sound "sounds/sfx_couch_fall_on_Polina.ogg"

    hide Polina with Dissolve(.5)
    play test_six "voice/Polina/4day/126 Hnik.ogg"
    "Она повалилась на кровать, ладонями прикрыла лицо. Всхлипы превратились в сдавленное рыдание."

    scene d4_hysteria with Dissolve(.5)
    play test_six "voice/Polina/4day/127 Hnuk.ogg" 
    "Я растерянно топтался на месте, не зная, что предпринять."
    stop test_six fadeout 0.5
    voice "voice/Polina/4day/128 Da.ogg"
    Pol "Давай сбежим! Завтра же соберём вещи и уедем в город!"
    voice "voice/anton/4day/157.Na .ogg"
    Ant "Нам по двенадцать лет..."
    voice "voice/Polina/4day/129 E.ogg"
    Pol "И что?"
    scene d4_hysteria2 with Dissolve(.5):
        align (.5, .5)
        zoom 1.01






    voice "voice/Polina/4day/130 Te.ogg"
    Pol "Тебе нравится жить в хибаре у леса?"
    voice "voice/Polina/4day/131 A.ogg"
    Pol "А мне, думаешь, по нраву гнить, заточённой в четырёх стенах?"

    play sound "sounds/sfx_couch_punching.ogg"

    play test_six "voice/Polina/4day/127 Hnuk2.ogg"
    "Её кулачки били по дивану, тело выгибалось."
    stop test_six fadeout 1
    voice "voice/Polina/4day/132 Es.ogg"
    Pol "Если ты мужчина, уведи меня из этого места!"

    scene d4_polroom_bg with Dissolve(.5)

    play test_six "voice/Polina/4day/127 Hnuk3.ogg"
    "«{i}Пора уходить{/i}», - отчеканил внутренний голос, и я был с ним солидарен."
    voice "voice/anton/4day/158. Pr.ogg"
    Ant "Прости. Тебе надо отдохнуть. Поговорим позже."
    $ music_during_lines = 1.0
    stop test_six fadeout 3
    stop music fadeout 3.5

    play test_one "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.6 loop

    pause 1

    stop test_two fadeout 1.5
    scene bg_black with Dissolve(.25)

    play sound "sounds/sfx_door_open_slow.ogg"

    scene polina_home_day_04
    show Polina_home_door:
        1.
        linear .5 alpha 0
    with Dissolve(.25)

    $ renpy.music.set_pan(0, delay=0, channel="test_three")
    stop test_one fadeout 0.7
    play test_three ["<silence .5>", "sounds/sfx_door_home_close.ogg"]

    "Я вышел в коридор, бурча. Возможно, поступил, как трус, но я не мог больше выносить её истерику."
    play music2 "music/Evil Alice.ogg" volume 0.83 fadein 8

    play sound "sounds/sfx_dressing.ogg"

    "Надел куртку, сунул ноги в ботинки."

    play sound "sounds/sfx_wheelchair_coming_1.ogg"

    show shadow_pol_gf 0 with Dissolve(0.5)
    voice "voice/Hariton/18. Skir.ogg"
    Ded "Скырлы-скырлы."
    play sound "sounds/sfx_wheelchair_coming_1.ogg"
    show shadow_pol_gf 1 with Dissolve(0.5)
    "Я уставился в темноту, думая о медведе-людоеде."

    play sound "sounds/sfx_wheelchair_coming_1.ogg"

    show shadow_pol_gf 2 with Dissolve(0.5)
    play test_five "voice/Polina/4day/tears.ogg" 
    "Плач Полины раздавался за стеной. А на меня надвигалось нечто скрипящее."
    stop test_five fadeout 2

    play sound "sounds/sfx_wheelchair_coming_2.ogg"

    show shadow_pol_gf 3 with Dissolve(0.5)
    "Коляска старика притормозила в двух метрах, на границе света и мрака."

    play sound "sounds/sfx_wheelchair_coming_3.ogg"

    hide shadow_pol_gf
    show pol_grandpa
    with Dissolve(0.5)
    $ music_during_lines = 0.72
    voice "voice/Hariton/54.Uho.ogg"
    Ded "Уходишь? Так быстро?"

    play test_three "sounds/sfx_shoes_tying.ogg"

    "Я промямлил, шнуруя обувь:"
    voice "voice/anton/4day/159. Pro.ogg"
    Ant "Простите, мама будет беспокоиться."
    voice "voice/Hariton/55.Ti.ogg"
    Ded "Ты знаешь настоящее имя своей матери, Петров Антон?"
    "Тени клубились, двигаясь за плечами Харитона. Я жаждал покинуть это странное место как можно скорее."
    voice "voice/anton/4day/160. Ne.ogg"
    Ant "Нет, простите."
    play test_five "voice/Polina/4day/tears.ogg"
    "Взволнованный, я извинялся направо и налево."

    hide pol_grandpa

    play sound "sounds/sfx_wheelchair_coming_normal.ogg"

    show Ded Worry m_day 01 worry ahead 01:
        xoffset 200
        yoffset 10
    with Dissolve(.5)

    show Ded Worry m_day 01 worry aside 01 with Dissolve(.25)
    pause .75
    show Ded Worry m_day 01 worry ahead 02 with Dissolve(.15)
    voice "voice/Hariton/56.Poch.ogg"
    Ded "Почему плачет Полина? Что случилось?"

    show Ded Angry m_day 01 angry ahead 01 with Dissolve(.5)
    "Блеснули железные зубы."

    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.5)
    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/57.Po.ogg"
    Ded "Пойдём на кухню, чай пить будем."
    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Happy m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/58.Ya.ogg"
    Ded "Я тортик разрезал."
    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.15)
    voice "voice/anton/4day/161. Men.ogg"
    Ant "Меня ждут."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.5)
    show Ded Normal m_day 01 normal ahead 02 with Dissolve(.15)
    voice "voice/Hariton/59.Pod.ogg"
    Ded "Подождут и перестанут. Ну, пойдём, пойдём."
    show Ded Normal m_day 01 normal ahead 01 with Dissolve(.15)
    show Ded Worry m_day 01 worry ahead 01 with Dissolve(.5)
    play test_six "voice/Hariton/60.He.ogg"
    "Он хныкнул капризно."

    show Ded Happy m_day 01 normal ahead 01 with Dissolve(.5)
    "Наконец справившись со шнурками, я вскочил на ноги. Старик улыбался надсадно."

    play sound "sounds/sfx_door_lock_rattle.ogg"

    "Я повернулся к нему спиной. Пальцы сражались с замком."


    show Ded Angry m_day 01 angry ahead 01 with Dissolve(.5):
        align (.5, 1.)
        xoffset 00
        yoffset 90
        zoom 1.2
        .5
        linear .5 yoffset 110
        linear .5 yoffset 90
        linear .5 yoffset 110
        linear .5 yoffset 90
    play wtf "sounds/sfx_wheelchair_squeak_1.ogg"
    $ music_during_lines = 1.0
    voice "voice/Hariton/Skirl.ogg"
    Ded "Скырлы-скырлы."
    "Мне не позволят уйти. Наедут сзади коляской, утащат."

    play test_two "sounds/sfx_wheelchair_coming_close_1.ogg"

    show d4_skirli:
        align (.5, .5)
        linear .05 zoom 1.3
        block:
            linear .01 zoom 1.305
            linear .01 zoom 1.300
            repeat
    show d4_polina_am_5 as saliva1:
        pos (.5, .5)
        anchor (.50, .65)
        yoffset 300
        zoom .5
        parallel:
            linear .35 zoom 1.0
        parallel:
            .10
            linear .25 alpha 0
        parallel:
            easeout .35 yoffset 900
    show d4_polina_am_5 as saliva2:
        pos (.5, .5)
        anchor (.50, .65)
        xzoom -1
        zoom .5
        yoffset 300
        parallel:
            linear .35 zoom 1.0
        parallel:
            .10
            linear .25 alpha 0
        parallel:
            easeout .35 yoffset 600
    voice "voice/Hariton/Skirl2.ogg"
    Ded "Скырлы-скырлы."

    hide d4_skirli with Dissolve(.25)
    show Ded Angry m_day 01 angry ahead 01:
        align (.5, 1.)
        xoffset -50
        yoffset 180
        zoom 1.35
    with Dissolve(.25)
    play sound "sounds/sfx_door_wooden_open.ogg"
    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 2

    play wtf "sounds/sfx_wheelchair_coming_normal.ogg"
    "Дверь отворилась, впустив в душный коридор зимний мороз."

    show d4_skirli:
        align (.5, .5)
        linear .05 zoom 1.3
        block:
            linear .01 zoom 1.305
            linear .01 zoom 1.300
            repeat
    voice "voice/Hariton/62.Kak.ogg"
    Ded "Как твоё настоящее имя?"

    play sound "sounds/sfx_door_wooden_close_fast.ogg"

    $ renpy.stop_predict("d4_polroom_magic_bg")
    scene bg_black with Dissolve(.5)
    stop music2 fadeout 2.5
    stop test_five fadeout 0.5
    voice "voice/anton/4day/162. D.ogg"
    Ant "До свидания!"

    window hide

    play test_one "sounds/loop_footsteps_snow_fast.ogg" fadein 0.6 loop

    scene d4_polhouse_night
    show blizzard_d4_evening
    with Dissolve(1.)

    pause 1.2
    stop test_one fadeout 1

    window show

    play music "music/2_Anxiety.ogg" fadein 2.5
    "Я вылетел на крыльцо, на дорожку, петляющую между домов."
    "Пока я гостил у Полины, мрак вороньими крылами объял посёлок."
    "Из-за ветра он казался живым и мыслящим существом. Слабо горели вмурованные в ночь фонари."

    play sound "sounds/sfx_wipe_face.ogg"

    "Я утёр лоб."
    "Ну и ну! Что за концерт устроила Полина?"
    "А старик, подглядывавший за нами? Не мудрено, что она так отчаянно хотела сбежать."

    jump d4_polhouse_after.devend
    label d4_polhouse_after.dev hide:
        scene bg_black
        menu:
            "Амулет":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
                $ Flags.Raise("amulet")
            "Без амулета":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 polina")
            "Предатель Лисы":
                $ Flags.Raise("fight")
                $ Flags.Raise("day2 fox")
                $ Flags.Raise("betray")
    label d4_polhouse_after.devend:

    play test_one "sounds/loop_footsteps_snow_normal.ogg" fadein 0.6 loop

    scene bg road_night snowless
    show blizzard_d4_evening zorder 1
    with Dissolve(.5)
    "Едва я вспомнил металлические зубы Харитона, как мурашки зарыскали по моей коже."
    stop music fadeout 3.5

    stop test_one fadeout 1.2

    show d4_rom_dark 0 with Dissolve(.5)
    voice "voice/romka/4day/228ei.ogg"
    Noname "Эй!"
    "Я встрепенулся и окинул взором улицу. У забора маячил неясный силуэт."
    voice "voice/anton/4day/163. Kto.ogg"
    Ant "Кто здесь?"

    play sound "sounds/loop_footsteps_snow_heavy_distant_slow.ogg" fadein 0.2
    pause 1

    show d4_rom_dark 1 with Dissolve(.5)

    stop sound fadeout 1.6

    play music2 "music/34_Nikita Kryukov - the Sabbath.ogg" volume 1.35 fadein 1
    "Человек шагнул ко мне, встал в кольце фонарного света. Душа, кувыркнувшись, ухнула в пятки."
    "Я узнал Ромку."

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.2
    pause 1

    show d4_rom_dark 2 with Dissolve(.5)
    play test_two"voice/romka/4day/245she.ogg"

    stop sound fadeout 1.6

    "Щёки одноклассника были мокрыми, а глаза покраснели."
    play test_two"voice/romka/4day/245on.ogg"
    "Он плакал, прячась в темноте."
    stop test_two fadeout 0.5

    $ music_during_lines = 0.65
    voice "voice/romka/4day/229nu.ogg"
    Rom "Ну, привет."
    play test_seven "sounds/loop_footsteps_snow_normal.ogg" fadein 0.2

    if Flags.Has("mask") or Flags.Has("day2 polina"):
        jump d4_madrom_notfox

    jump d4_madrom_fox




label d4_madrom_fox:
    $ story_manager.MarkEvent(("day4", "scene_ra"))
    stop test_seven fadeout 0.5
    scene bg road_night2
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Ant Cho b_night 00 norm ahead 01
    with Dissolve(0.5)
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.3)
    voice "voice/anton/4day/164. Chto.ogg"
    Ant "Что ты тут делаешь?"
    voice "voice/romka/4day/230 Da.ogg"
    Rom "Да вот... Ты не пришёл на наш спектакль, и я волновался, что с тобой что-то случилось."

    scene bg road_night
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Romka Evil m_night_winter 01 cry ahead 02
    with Dissolve(.5)
    voice "voice/romka/4day/231 Kak.ogg"
    Rom "Как с Семёном и Катей."

    window hide
    play sound ["sounds/sfx_coat_rustle.ogg","sounds/sfx_butterfly_knife.ogg"]

    show Romka Evil m_night_winter 02 cry ahead 01 with Dissolve(.25)
    pause .25
    show Romka Evil m_night_winter 03 cry ahead 01 with Dissolve(.5)
    pause .5
    window show
    "Раздался щелчок, сверкнул нож-бабочка."

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1

    play sound ["sounds/sfx_coat_rustle.ogg","sounds/sfx_butterfly_knife.ogg"]
    show Romka Dark concise stable silent
    with Dissolve(.5)



    show d4_rom_dark_knife:
        align (.0,.0)
        ypos 200
        yoffset 500
        linear .35 yoffset 0


    play test_five "sounds/sfx_coat_rustle.ogg"
    "Обескровленные губы Ромы растянулись в страшной гримасе. Зрачки сверкали, словно две монеты."

    scene bg road_night2
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Ant Cho b_night 00 norm ahead 01
    with Dissolve(0.5)
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.3)
    voice "voice/anton/4day/165. Rom.ogg"
    Ant "Ром, убери нож."

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Romka Dark concise stable silent
    show d4_rom_dark_knife:
        align (.0,.0)
        ypos 200
    with Dissolve(.5)
    show Romka Dark concise stable say with Dissolve(.15)
    voice "voice/romka/4day/232 Za.ogg"
    Rom "Зачем?"
    show Romka Dark concise stable silent with Dissolve(.15)
    show Romka Dark concise shake say with Dissolve(.15)
    voice "voice/romka/4day/233 Kak.ogg"
    Rom "Как без ножа я смогу разрезать тебя от пупка до глотки и проверить, что внутри у предателей?"
    show Romka Dark concise shake silent with Dissolve(.15)
    voice "voice/anton/4day/166. Roma.ogg"
    Ant "Рома!"

    play test_one "sounds/loop_footsteps_snow_normal.ogg" fadein 0.6 loop

    "Я отступал, боясь повернуться к нему беззащитными лопатками. Рома шёл на меня, скалясь."
    show Romka Dark concise shake say with Dissolve(.15)
    stop test_one fadeout 3.5
    voice "voice/romka/4day/234 Bil.ogg"
    Rom "Был у неё дома, да?"
    show Romka Dark concise shake silent with Dissolve(.15)
    show Romka Dark concise shake say with Dissolve(.15)
    voice "voice/romka/4day/235 Prav.ogg"
    Rom "Правая рука Вольтрона, говорит центр управления! Как слышно?.."
    show Romka Dark concise shake silent with Dissolve(.15)
    show Romka Dark concise shake say with Dissolve(.15)
    voice "voice/romka/4day/236 Ti.ogg"
    Rom "Ты был у моей Полины?"
    show Romka Dark concise shake silent with Dissolve(.15)
    show Romka Dark concise shake say with Dissolve(.15)
    voice "voice/romka/4day/237 Ris.ogg"
    Rom "Рисовал её? Трогал?"
    show Romka Dark concise shake silent with Dissolve(.15)

    scene bg road_night2
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Ant Cho b_night 00 norm ahead 01
    with Dissolve(0.5)
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.3)
    voice "voice/anton/4day/167. Vse.ogg"
    Ant "Всё не так!"
    "Я врал, конечно. Всё было именно так и даже больше."

    stop test_one fadeout 1.2

    jump d4_madrom_common


label d4_madrom_notfox:
    $ story_manager.MarkEvent(("day4", "scene_rb"))
    scene bg road_night
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Romka Evil m_night_winter 01 cry ahead 01
    with Dissolve(.5)

    show Romka Evil m_night_winter 01 cry ahead 02 with Dissolve(.2)
    stop test_seven fadeout 0.5
    voice "voice/romka/4day/239Razve.ogg"
    Rom "Разве я не предупреждал тебя, а?"
    show Romka Evil m_night_winter 01 cry ahead 01 with Dissolve(.2)
    show Romka Evil m_night_winter 01 cry ahead 02 with Dissolve(.2)
    voice "voice/romka/4day/240raz.ogg"
    Rom "Разве не говорил, что убью, если увижу рядом с ней?"
    show Romka Evil m_night_winter 01 cry ahead 01 with Dissolve(.2)

    window hide
    play sound ["sounds/sfx_coat_rustle.ogg","sounds/sfx_butterfly_knife.ogg"]

    show Romka Evil m_night_winter 02 cry ahead 01 with Dissolve(.25)
    pause .25
    show Romka Evil m_night_winter 03 cry ahead 01 with Dissolve(.5)
    pause .5
    window show

    "Раздался щелчок, сверкнул нож-бабочка."

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1



    show Romka Dark concise stable silent
    with Dissolve(.5)

    show d4_rom_dark_knife:
        align (.0,.0)
        ypos 200
        yoffset 500
        linear .35 yoffset 0

    play test_five "sounds/sfx_coat_rustle.ogg"
    "Обескровленные губы Ромы растянулись в страшной гримасе. Зрачки сверкали, словно две монеты."

    scene bg road_night2
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Ant Cho b_night 00 norm ahead 01
    with Dissolve(0.5)
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.3)
    voice "voice/anton/4day/165. Rom.ogg"
    Ant "Ром, убери нож."

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Romka Dark concise stable silent
    show d4_rom_dark_knife:
        align (.0,.0)
        ypos 200
    with Dissolve(.5)

    show Romka Dark concise stable say with Dissolve(.15)
    voice "voice/romka/4day/241dum.ogg"
    Rom "Думаешь, я псих? Я покажу тебе, что делают психи!"
    voice "voice/anton/4day/166. Roma.ogg"
    show Romka Dark concise shake silent with Dissolve(.15)

    Ant "Рома!"

    "Я отступал, боясь повернуться к нему беззащитными лопатками."

    play test_one "sounds/loop_footsteps_snow_normal.ogg" fadein 0.6 loop

    "Ромка шёл на меня, скалясь."

    stop test_one fadeout 1.2

    jump d4_madrom_common


label d4_madrom_common:
    $ story_manager.MarkEvent(("day4", "scene_r2"))

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Romka Dark concise shake silent

    play sound "sounds/sfx_knife_clink.ogg"

    show d4_rom_dark_knife:
        align (.0,.0)
        ypos 200
    with Dissolve(.5)
    show Romka Dark concise shake say with Dissolve(.15)
    voice "voice/romka/4day/244zalkii_pr.ogg"
    Rom "Жалкий ублюдок!"

    play sound "sounds/sfx_saliva_gurgle.ogg"

    show Romka Dark concise shake pena with Dissolve(.5)
    "В уголках его рта выступила пена."

    play sound "sounds/sfx_coat_rustle.ogg"

    show Romka Dark concise shake silent with Dissolve(.5)
    "Он судорожно утёр лицо рукавом, ещё сильнее размазав слёзы по щекам."
    show Romka Dark veil shake silent with Dissolve(.15)
    "Остекленевшие глаза заволокло туманом ненависти."

    if Flags.Has("amulet"):
        jump d4_madrom_amulet

    jump d4_madrom_no_amulet


label d4_madrom_amulet:
    $ story_manager.MarkEvent(("day4", "scene_r4"))
    show bg_white onlayer master1 zorder 100 with Dissolve(.25)
    play test_one "sounds/flashback.ogg"

    show bunny_nightmare_bg onlayer master1 zorder 90

    show tupichok_amulet onlayer master1 zorder 90:
        subpixel True
        parallel:
            linear 1.0 xpos -10 ypos 2
            linear 1.0 xpos -8 ypos 2
            linear 1.0 xpos -6 ypos 0
            linear 1.0 xpos -4 ypos 4
            linear 1.0 xpos -2 ypos 2
            linear 1.0 xpos 0 ypos 0
            repeat
        parallel:
            ease .25 matrixcolor BrightnessMatrix(-0.05)
            ease .25 matrixcolor BrightnessMatrix(0.00)
            repeat
    show old_movie_intense onlayer master1 zorder 90:
        matrixcolor BrightnessMatrix(1.0)

    hide bg_white onlayer master1 with Dissolve(.25)


    "Амулет-коготь, который мне дала Полина, снова пришёл на выручку."
    "Время словно замедлилось, стало как янтарь, в котором застыл не только я, но и Ромка с его опасным ножом."
    play test_one "sounds/hit-chord-2.ogg"

    show bg_white onlayer master1 zorder 100 with Dissolve(.25)

    hide bunny_nightmare_bg onlayer master1
    hide tupichok_amulet onlayer master1
    hide old_movie_intense onlayer master1

    hide bg_white onlayer master1 with Dissolve(.25)

    "«{i}Беги!{/i} — просигналил внутренний голос. — {i}Спасай свою шкуру!{/i}»"
    show Romka Dark veil shake say with Dissolve(.15)
    voice "voice/romka/4day/244 zalkiigrya.ogg"
    Rom "Жалкий грязный ублюдок!"
    show Romka Dark veil shake silent with Dissolve(.15)
    show Romka Dark veil shake scream with Dissolve(.5)
    play test_five "voice/romka/4day/245on.ogg"
    "Вдруг он завыл. Горестный вой взвился к звёздам."

    play sound "sounds/sfx_knife_teeth.ogg"

    show Romka Dark veil shake knife
    hide d4_rom_dark_knife
    with Dissolve(.5)
    "Ромка сунул себе в рот рукоять ножа, как сигару, зажал зубами. Лезвие торчало наружу стальным клыком."

    play sound "sounds/sfx_Romka_fall_snow.ogg" volume 0.6

    $ renpy.start_predict("walking_fox_11_dark")
    $ renpy.start_predict("walking_fox_12_dark")
    $ renpy.start_predict("walking_fox_21_dark")
    $ renpy.start_predict("walking_fox_22_dark")
    $ renpy.start_predict("walking_fox_31_dark")
    $ renpy.start_predict("walking_fox_32_dark")
    $ renpy.start_predict("snow_night_4")

    scene d4_rom_dark_road
    show blizzard_d4_evening_far zorder 1
    show blizzard_d4_evening_near zorder 1
    with Dissolve(.5)
    play test_two"voice/romka/4day/326 Cry.ogg"
    "А затем он упал на четвереньки."
    "Его тень по-звериному нахохлилась."
    "Слюна капала на снег."
    play test_three "sounds/sfx_coat_rustle_1.ogg"
    hide d4_rom_dark_road
    show romka_road_bg behind snow_night_1
    show roma_day4_bezumie 03 behind snow_night_1
    with Dissolve(.5)
    stop music2 fadeout 2
    play test_six "voice/romka/4day/246 Rik.ogg"


    "Обезумевший Ромка зарычал и бросился ко мне, отталкиваясь всеми четырьмя конечностями."
    "{i}Беги!{/i}"
    play test_two "sounds/loop_footsteps_snow_run_creepy.ogg" loop
    play music "music/14_Disaster_pt3-loop.ogg" fadein 2.2

    hide roma_day4_bezumie 03
    show roma_road_anim
    window hide
    pause .15

    play test_three "sounds/loop_footsteps_snow_heavy_distant_run.ogg" fadein 1 loop

    $ renpy.start_predict("road_night")
    $ renpy.start_predict("traktor_02")
    $ renpy.start_predict("d4_traktor_anton")
    $ renpy.start_predict("d4_traktor_shadow")
    $ renpy.start_predict("d4_traktor_eyes")

    scene black
    $ SetParSpeed(10)
    show walking_fox_11_dark
    show walking_fox_12_dark
    show walking_fox_21_dark
    show walking_fox_22_dark
    show walking_fox_31_dark
    show walking_fox_32_dark
    show blizzard_d4_evening_far_run
    show blizzard_d4_evening_near_run

    play sound "voice/anton/1day/029.Beg i o.ogg"
    "Я побежал, не разбирая дороги."
    "Ботинки вязли в сугробах. Мелькал штакетник."
    "Шум поднялся такой, словно за мной гнался не ровесник, а какой-то зверь. Большой до ужаса."
    "Ветер бил по лицу, обжигал, будто листья крапивы."
    "Я задыхался."
    scene road_night:
        align (.5, .5)
        zoom 1.06
        rotate -3
        yoffset -160
    show blizzard_d4_evening2_far
    show traktor_02 zorder 3:
        align (.5, .5)
        zoom 1.02
    show blizzard_d4_evening2_near zorder 5
    show blizzard_d4_evening2_big zorder 5
    with Dissolve(.5)

    $ renpy.stop_predict("walking_fox_11_dark")
    $ renpy.stop_predict("walking_fox_12_dark")
    $ renpy.stop_predict("walking_fox_21_dark")
    $ renpy.stop_predict("walking_fox_22_dark")
    $ renpy.stop_predict("walking_fox_31_dark")
    $ renpy.stop_predict("walking_fox_32_dark")
    $ renpy.stop_predict("snow_night_4")

    pause .5

    stop test_three fadeout 0.8
    stop test_two fadeout 0.9

    show d4_traktor_anton:
        align (.5, .5)
        xoffset -100
        yoffset 50
        zoom 0.55
        rotate -3
    show d4_traktor_anton_silhuete 5 zorder 1:
        align (.5, .5)
        xoffset -100
        yoffset 50
        zoom 0.55
        rotate -3
    with Dissolve(.5)

    stop sound fadeout 3
    "На повороте стоял припаркованный трактор, но водителя я не увидел."

    $ renpy.start_predict("d4_fonari_blink")
    $ renpy.start_predict("d4_selmag_close_fon")
    $ renpy.start_predict("d4_selmag_close_mag")
    $ renpy.start_predict("d4_selmag_shadow")
    $ renpy.start_predict("d4_selmag_reflect_anton")

    play sound "sounds/sfx_Romka_fall_snow.ogg" volume 0.5

    show d4_traktor_shadow with vpunch
    show d4_traktor_eyes with Dissolve(.15):
        align (.5, .5)
        zoom 0.55
        xoffset -100
        yoffset 50
        rotate -3
    pause .25
    hide d4_traktor_eyes with Dissolve(.15)
    "Что-то юркое перепрыгнуло тропинку. Приземлилось в паре метров от меня."

    play sound "sounds/sfx_snow_body_jump_roll.ogg"

    pause .8    

    play test_three "sounds/loop_footsteps_snow_heavy_distant_run.ogg" fadein 1 
    play test_two "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 1 

    hide d4_traktor_anton
    hide d4_traktor_anton_silhuete
    with Dissolve(.5)
    stop test_two fadeout 3
    stop test_three fadeout 2
    "Снежная баррикада перекрыла путь. Я вскарабкался на неё, скатился, ринулся в переулок."
    show d4_traktor_anton zorder 4:
        align (.5, .5)

        rotate -3
    show d4_traktor_anton_silhuete 4 zorder 4:
        align (.5, .5)

        rotate -3
    with Dissolve(.5)

    show d4_fonari_blink zorder 10
    $ lamp_volume = 1.0
    "Фонари мигали панически."

    scene d4_selmag_full:
        align (.75, .5)
        zoom .60

        parallel:
            linear 10. zoom .85
        parallel:
            linear .15 yoffset 25 xoffset -10
            linear .15 yoffset 0
            linear .15 yoffset 25 xoffset 10
            linear .15 yoffset 0
            repeat

    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near
    show blizzard_d4_evening_face

    with Dissolve(.5)
    $ renpy.stop_predict("road_night")
    $ renpy.stop_predict("traktor_02")
    $ renpy.stop_predict("d4_traktor_anton")
    $ renpy.stop_predict("d4_traktor_shadow")
    $ renpy.stop_predict("d4_traktor_eyes")
    play sound "voice/anton/1day/029.Beg i o.ogg"
    play test_three "sounds/loop_footsteps_snow_heavy_distant_run.ogg" fadein 1 loop
    "Я заметил сельмаг и кинулся к нему."

    stop test_three fadeout 1
    stop test_two fadeout 1

    scene d4_selmag_close_fon:
        align (.0, .5)
    show d4_selmag_close_mag:
        align (.0, .5)

    show blizzard_d4_evening2_near onlayer master1
    with Dissolve(.25)

    show d4_selmag_shadow:
        yalign 1.
    with Dissolve(.25)

    stop test_three fadeout 1.5
    play sound "sounds/sfx_door_latch_rattle.ogg"

    scene d4_selmag_close_fon:
        align (.0, .5)
        linear .15 zoom 1.1
        linear .15 zoom 1.
    show d4_selmag_close_mag:
        align (.0, .5)
        linear .15 zoom 1.1
        linear .15 zoom 1.
    show d4_selmag_shadow:
        align (.0, 1.)
        linear .15 zoom 1.1
        linear .15 zoom 1.
    "Дёрнул ручку — заперто!"
    play test_four "sounds/steps/snow_stepS02.ogg"

    hide d4_selmag_shadow with Dissolve(.25)

    $ renpy.start_predict("d4_roadwood")
    $ renpy.start_predict("d4_forest_wolf 1")
    $ renpy.start_predict("d4_forest_wolf 2")

    hide blizzard_d4_evening2_near onlayer master1
    scene d4_selmag_close_fon:
        align (0., .5)
        linear .35 xpos -1296

    show blizzard_d4_evening_far:
        matrixcolor BrightnessMatrix(-.40)
        parallel:
            xpan 0
            linear .35 xpan 360

            block:
                xpan 0
                linear 60 xpan -360
                repeat
        parallel:
            ypan 0
            linear 30 ypan -360
            repeat
    show d4_selmag_close_mag:
        align (0., .5)
        linear .35 xpos -1296
    show d4_selmag_reflect_anton:
        alpha 0
        linear .35 xpos -1296 alpha 1

    show blizzard_d4_evening2_near:

        parallel:
            xpan 0
            linear .35 xpan 360

            block:
                xpan 0
                linear 60 xpan -360
                repeat
        parallel:
            ypan 0
            linear 30 ypan -360
            repeat
    "В стекле отразился переулок. Что-то огромное и жуткое двигалось оттуда, окутанное метелью, точно похоронным саваном."
    window hide

    play test_three "sounds/loop_footsteps_snow_heavy_distant_run.ogg" fadein 1 loop
    play test_two "sounds/loop_footsteps_snow_run_creepy.ogg" volume 0.6 fadein 1 loop
    play test_four "sounds/loop_dogs_whining.ogg" fadein 2 loop
    play sound "voice/anton/1day/029.Beg i o.ogg"

    show d4_selmag_phantom behind d4_selmag_close_mag:
        xalign .45
        yalign .5
        yoffset 300
        zoom .6
        linear .5 xalign .55
        linear .5 zoom 1. yoffset 100
    show d4_selmag_phantom_shadow:
        xalign .55
        ypos 1.
        yanchor 0.
        .5
        linear .5 yanchor .5
    with Dissolve(.5)

    pause .5

    scene d4_selmag_full:
        align (.95, .5)
        zoom 1.

        parallel:
            linear 1. xalign .5
        parallel:
            linear .15 yoffset -15
            linear .15 yoffset 0
            repeat
    show blizzard_d4_evening_far zorder 10
    show blizzard_d4_evening_near zorder 10
    show blizzard_d4_evening_face zorder 10
    scene bg_black with Dissolve(.5)

    window show
    "Я метнулся на расчищенную полоску асфальта."
    "Собаки во дворах не лаяли, а жалобно скулили."

    stop test_two fadeout 2

    scene d4_runaway_night_noglow:
        animation
        align (.5, .5)
    show runaway_snow1:
        zoom 1.1
        matrixcolor BrightnessMatrix(-.6)
    show runaway_snow2:
        zoom 1.1
        matrixcolor BrightnessMatrix(-.6)
    show blizzard_big:
        matrixcolor BrightnessMatrix(-.2)
        parallel:
            xpan 0
            linear .33 xpan 360
            repeat
        parallel:
            ypan 0
            linear .33 ypan -360
            repeat
    show bg_black:
        linear 1.5 alpha 0

    $ renpy.stop_predict("d4_fonari_blink")
    $ renpy.stop_predict("d4_selmag_close_fon")
    $ renpy.stop_predict("d4_selmag_close_mag")
    $ renpy.stop_predict("d4_selmag_shadow")
    $ renpy.stop_predict("d4_selmag_reflect_anton")

    stop test_four fadeout 12

    "Я обогнул крайний дом и выбежал за посёлок. Лес нависал чёрной монолитной глыбой."
    "У меня был выбор: просека, на которой я был бы как на ладони, или прямой маршрут через лес, через рвы и бурелом."
    "И я предпочёл второй вариант."
    stop music fadeout 5.5

    stop test_three fadeout 1
    play sound "sounds/sfx_Romka_fall_snow.ogg"

    scene d4_roadwood:
        align (.5, .5)
        linear .05 xalign 0.55
        linear .05 xalign 0.45
        repeat 4
    show blizzard_d4_evening2_far onlayer master1
    show blizzard_d4_evening2_near onlayer master1
    show blizzard_d4_evening_face onlayer master1:
        matrixcolor BrightnessMatrix(-.2)

    play music "music/Hor.ogg" fadein 0.5
    "Прыгнул вбок, – нога скользнула по льду, — рухнул в овраг."


    play sound "sounds/loop_snow_crawl_Anton.ogg" fadeout 0.6 

    play test_five "voice/anton/2day/fear3.ogg"
    "Брыкаясь, перевернулся на спину и стал отползать, ожидая, что Ромка вот-вот появится сверху."

    scene d4_roadwood:
        align (.45, .5)
        linear .15 xalign 0.

    play sound "sounds/sfx_Wolf_Romka.ogg"

    "Нечеловеческий вопль пронёсся дворами, ввинтился в уши."

    stop sound fadeout 2

    $ renpy.start_predict("d4_pol_drom_0")
    $ renpy.start_predict("d4_dr_wolf_body")
    $ renpy.start_predict("d4_dr_wolf_knife")
    $ renpy.start_predict("d4_dr_wolf_hand 1")
    $ renpy.start_predict("d4_dr_wolf_hand 2")
    $ renpy.start_predict("d4_dr_wolf_shadow")
    $ renpy.start_predict("d4_dr_wolf_eyes static")
    $ renpy.start_predict("d4_dr_wolf_eyes animation")

    scene d4_roadwood:
        align (.0, .5)
        linear 1 xalign .5

    "Прошла минута. Вторая."

    scene d4_roadwood:
        align (.5, .5)
    show d4_forest_wolf 1:
        xalign .5
        alpha 0
        .25
        linear .5 alpha 1
    play test_one "sounds/loop_footsteps_snow_heavy_distant_slow.ogg" fadein 3 loop
    "Я трясся, всматриваясь в край оврага, в чернильные мазки сосен."


    scene d4_roadwood:
        align (.5, .5)
    show d4_forest_wolf 1:
        xalign .5
    with None

    show d4_forest_wolf 2:
        xalign .5
    with Dissolve(.5)
    "В приближающуюся тень."

    hide d4_forest_wolf
    hide blizzard_d4_evening2_far onlayer master1
    hide blizzard_d4_evening2_near onlayer master1
    hide blizzard_d4_evening_face onlayer master1
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 1
    show blizzard_d4_evening_face zorder 1:
        matrixcolor BrightnessMatrix(-.2)
    show Wolf Normal m 01:
        xpos .6
        xanchor .5
        matrixcolor BrightnessMatrix(-.05)
    show d4_dr_wolf_eyes static:
        xpos .6
        xanchor .5
    with Dissolve(.5)

    show d4_dr_wolf_eyes animation

    $ renpy.stop_predict("d4_roadwood")
    $ renpy.stop_predict("d4_forest_wolf 1")
    $ renpy.stop_predict("d4_forest_wolf 2")

    stop test_one fadeout 1

    play test_two "voice/Wolf/307R.ogg"
    "Мальчик в маске волка вышел из леса и остановился передо мной."
    scene d4_pol_drom_0:
        yzoom -1
        blur 8
    show d4_dr_wolf_body:
        blur 8
    show d4_dr_wolf_knife:
        ypos -100
        linear .5 ypos 0
    show d4_dr_wolf_hand 1:
        ypos -100
        linear .5 ypos 0
    show incar_snow_up zorder 1:
        matrixcolor BrightnessMatrix(-0.3)
    show bg_black:
        alpha .5
    with Dissolve(.5)

    $ music_during_lines = 0.8
    voice "voice/Wolf/341 Drr.ogg"
    Wolf "Др-р-руг."

    $ is_slowmo = False
    window hide
    show d4_dr_wolf_hand 2:
        ease 1. + 3*is_slowmo yoffset -30

    play sound ["<silence 0.72>","sounds/sfx_snow_knife_drop.ogg"]


    show d4_dr_wolf_knife:
        subpixel True
        transform_anchor True
        align (.5, .5)
        linear .75 + 3.25*is_slowmo xoffset 50 yoffset 300 zoom 0.7 rotate 15 blur 8
        linear .02 xoffset 55
        linear .02 xoffset 45
        linear .02 xoffset 50

    show d4_dr_wolf_shadow behind d4_dr_wolf_knife:
        subpixel True
        transform_anchor True
        align (.5, .5)
        xoffset 50
        yoffset 305
        zoom 0.2
        alpha 0
        blur 8
        parallel:
            linear .75 + 3.25*is_slowmo rotate 15 zoom .7
        parallel:
            .25 + 1.*is_slowmo
            linear 0.5 + 2.25*is_slowmo alpha .5

    pause 1.5 + 3*is_slowmo

    window show
    "Он разжал кулак – нож-бабочка упал на снег."
    $ story_manager.MarkEvent(("day4", "scene_r5"))

    scene d4_pol_drom_0:
        yzoom -1
        blur 8
        linear .25 blur 100
    show d4_dr_wolf_body:
        blur 8
        linear .25 blur 100
    show d4_dr_wolf_shadow:
        xoffset 50 yoffset 305 zoom 0.7 rotate 15 blur 8
        linear .25 blur 100
    show d4_dr_wolf_knife:
        xoffset 50 yoffset 300 zoom 0.7 rotate 15 blur 8
        linear .25 blur 100
    show d4_dr_wolf_hand 2:
        yoffset -30
        linear .25 blur 100
    show incar_snow_up zorder 1:
        matrixcolor BrightnessMatrix(-0.3)
        linear .25 blur 100
    show bg_black:
        alpha .5
    pause .25

    scene d4_pol_drom_0:
        yzoom -1
        zoom 2.
        align (.5, 1.)
        blur 100
        linear .25 blur 0
    show d4_dr_wolf_knife:
        blur 100
        align (.5, .5)
        rotate 15
        zoom 1.4
        yoffset -30
        linear .25 blur 0
    show d4_dr_wolf_shadow behind d4_dr_wolf_knife:
        blur 100
        align (.5, .5)
        yoffset 5 -30
        rotate 15
        zoom 1.4
        linear .25 blur 0
    show incar_snow_up zorder 1:
        blur 100
        matrixcolor BrightnessMatrix(-0.3)
        linear .25 blur 0
    show bg_black:
        alpha .5
    with Dissolve(.25)
    voice "voice/Wolf/337 Te.ogg"
    Wolf "Тебе ничего не угр-р-рожает. Мы же говор-р-рили."

    scene d4_roadwood:
        align (.5, .5)
    show blizzard_d4_evening2_far
    show blizzard_d4_evening2_near zorder 1
    show blizzard_d4_evening_face zorder 1:
        matrixcolor BrightnessMatrix(-.2)
    show Wolf Normal m 01:
        xpos .6
        xanchor .5
        matrixcolor BrightnessMatrix(-.05)
    show d4_dr_wolf_eyes static:
        xpos .6
        xanchor .5
    with Dissolve(.5)
    show d4_dr_wolf_eyes animation
    "Не веря своим глазам, я поднялся на ноги."
    "Волчонок махнул рукой в сторону просеки."


    voice "voice/Wolf/338 Vs.ogg"
    Wolf "Всё в пор-р-рядке. Иди."
    $ music_during_lines = 1.0

    play test_one "sounds/loop_footsteps_snow_normal.ogg" fadeout 0.6 loop

    scene dark_forest_day3_1 dark1:
        zoom .5
        xzoom -1
    show bg_black:
        alpha .75

    show blizzard_d4_evening2_far:
        matrixcolor BrightnessMatrix(-.2)
    show blizzard_d4_evening2_near:
        matrixcolor BrightnessMatrix(-.2)
    show blizzard_d4_evening_big zorder 1:
        matrixcolor BrightnessMatrix(-.1)

    show d4_dr_scary_base
    show d4_dr_scary_eyes:
        xpos -100+20
        block:
            linear .03 xoffset 2
            linear .03 xoffset -2
            repeat



    with Dissolve(.5)

    play test_three "voice/anton/2day/fear2.ogg"
    "Я был слишком испуган, чтобы задавать вопросы."
    stop music fadeout 2.5

    $ renpy.stop_predict("d4_pol_drom_0")
    $ renpy.stop_predict("d4_dr_wolf_body")
    $ renpy.stop_predict("d4_dr_wolf_knife")
    $ renpy.stop_predict("d4_dr_wolf_hand 1")
    $ renpy.stop_predict("d4_dr_wolf_hand 2")
    $ renpy.stop_predict("d4_dr_wolf_shadow")
    $ renpy.stop_predict("d4_dr_wolf_eyes static")
    $ renpy.stop_predict("d4_dr_wolf_eyes animation")

    scene bg_black with Dissolve(1.5)
    stop test_one fadeout 1.3
    stop test_three fadeout 1

    "Потому я молча ушёл, хромая вдоль колышущихся деревьев, и постарался не думать о сгустках тьмы, что провожали меня, хоронясь за кустами."


    $ achievement_grant("ach_dicaprio")

    "Я ещё не знал, что ждёт меня в месте, которое я по ошибке называл домом."

    jump d4_home


label d4_madrom_no_amulet:
    $ story_manager.MarkEvent(("day4", "scene_r3"))

    $ renpy.start_predict("d4_pol_drom_fonsnow")
    $ renpy.start_predict("d4_pol_drom_boy1")
    $ renpy.start_predict("d4_pol_drom_hand 1")
    $ renpy.start_predict("d4_pol_drom_boy2")
    $ renpy.start_predict("d4_pierce")
    $ renpy.start_predict("d4_pol_drom_hand 2")



    show d4_rom_dark_knife:
        subpixel True
        align (.5,1.)
        yoffset 200
        easein 1. xoffset -400 zoom 0.7

    play test_four "sounds/sfx_coat_rustle.ogg"
    "Железная бабочка начала своё медленное движение вверх и вдруг, как на ускоренной плёнке, нырнула вперёд: это Ромка резко качнулся ко мне."
    window hide
    show bg Fox_give_candy0:
        zoom 1.01
        align (.5,.5)
        .1
        block:
            linear .05 xoffset 5
            linear .05 xoffset -5
            repeat 4

    play sound "sounds/sfx_knife_stab_first.ogg"

    show Romka Dark veil shake silent:
        linear .08 xoffset 100

        linear .15 xoffset 0
    show d4_rom_dark_knife:
        subpixel True
        align (.5,1.)
        xoffset -400
        yoffset 200
        zoom 0.7

        linear .3 xoffset 600 zoom 1 yoffset 1080

    show bg_black:
        alpha 0
        .2
        linear .15 alpha 1
        linear .15 alpha 0
    pause .5
    window show
    "Его лицо приобрело цвет воска, а глаза пылали, как фосфорные."
    "Я ощутил толчок и опустил взор."

    $ renpy.start_predict("d4_murder 1")
    $ renpy.start_predict("d4_murder 2")
    $ renpy.start_predict("d4_murder loop")

    scene d4_pol_drom_fonsnow
    show d4_pol_drom_boy1
    show d4_pol_drom_hand 1:
        align (.5, .5)
        ypos 500
        block:
            linear .1 xoffset 2
            linear .1 xoffset -2
            repeat
    show d4_pol_drom_boy2
    show incar_snow_up
    with Dissolve(.5)
    "Бабочка была не настоящей."
    "Из магазина приколов, игрушка, в которой лезвие погружается в рукоять."
    "Затем я понял, что ошибся, что не вижу лезвие потому, что оно погрузилось в мою грудь."
    "Что оно сейчас внутри."
    "Между рёбер."
    "Холодное."
    "Острое."

    $ renpy.start_predict("d4_murder_spots")
    $ renpy.start_predict("d4_murder_baby_bg")
    $ renpy.start_predict("d4_murder_baby_noise")

    show d4_pierce behind d4_pol_drom_boy2:
        align (.5, .5)
        alpha .5
        zoom 1.
        linear 2. zoom 1.4 alpha 0
    show d4_pol_drom_boy2 as dd:
        align (.5, .5)
        alpha .5
        zoom 1.
        linear 2. zoom 1.4 alpha 0
    show bg_black zorder 1:
        alpha 0
        linear .2 alpha .4
        block:
            linear .05 alpha .5
            linear .05 alpha .4
            repeat 3
        linear 1. alpha 0
    "Как звук, запоздавший за светом, пришла боль."
    "Удивительно, но она не была очень сильной, зато была ужасно неприятной, сосущей, и отдавала куда-то в затылок."

    play sound "sounds/sfx_grab_hand.ogg"

    show d4_pol_drom_hand 2
    with Dissolve(.5)
    "Я схватил Ромку за предплечье."

    show d4_pol_drom_hand 2:
        parallel:
            linear .1 yoffset 3
            linear .1 yoffset -3
            repeat 4

        parallel:
            easeout 1.5 ypos 400
            linear 1. ypos -200
        parallel:
            1.3
            "d4_pol_drom_hand 1" with Dissolve(.5)
            pause .7
            linear .5 alpha 0

    play sound "sounds/sfx_knife_pull_out.ogg"

    "Он вырвал нож: как в замедленной съёмке, за лезвием взлетел пунктир алых капель." id d4_madrom_no_amulet_7192edba

    $ renpy.start_predict("bg kitchen_dark1")
    $ renpy.start_predict("d4_father_old")
    $ renpy.start_predict("d4_mutter_old")

    scene bg Fox_give_candy0:
        align (.5,.5)
        zoom 1.01
        block:
            linear 2. blur 16
            linear 2. blur 0
            repeat
    show blizzard_d4_evening_far:
        block:
            linear 2. blur 12
            linear 2. blur 0
            repeat
    show blizzard_d4_evening_near zorder 1:
        block:
            linear 2. blur 12
            linear 2. blur 0
            repeat
    show Romka Dark veil shake scream:
        block:
            linear 2. blur 8
            linear 2. blur 0
            repeat

    with Dissolve(.5)

    $ renpy.stop_predict("d4_pol_drom_fonsnow")
    $ renpy.stop_predict("d4_pol_drom_boy1")
    $ renpy.stop_predict("d4_pol_drom_hand 1")
    $ renpy.stop_predict("d4_pol_drom_boy2")
    $ renpy.stop_predict("d4_pierce")
    $ renpy.stop_predict("d4_pol_drom_hand 2")

    play test_six "voice/romka/4day/245on.ogg"
    "Кожа на костяном каркасе Ромкиного лица гротескно растянулась, рот распахнулся, между передними зубами натянулись нити слюны."
    "Я хотел сказать, чтобы он прекратил, но слова застряли в горле."
    "Мир пошатнулся."

    play sound "sounds/sfx_Anton_fall_snow.ogg"

    scene d4_pol_drom_0:
        align (.5, .5)
        linear 0.1 zoom 1.1
        linear 0.1 zoom 1.3
        linear 0.2 zoom 1.6
        linear 0.1 zoom 1.3
        linear 0.1 zoom 1.25
        linear 0.1 zoom 1.35
        linear 0.1 zoom 1.3
        linear 0.1 zoom 1.2
        linear 0.1 zoom 1.15
        linear 0.1 zoom 1.0
    show incar_snow_up
    play test_two "voice/anton/4day/197. Davkrov.ogg"
    "Я упал на колени."
    "Стало сложно дышать."
    "Словно воздух в лёгком превратился в вязкое тесто."
    "Рот наполнился кровью."

    play sound ["<silence 4.5>", "sounds/sfx_blood_mouth.ogg"]


    scene d4_pol_drom_blood
    show incar_snow_up
    $ renpy.movie_cutscene("video/blood.webm")


    "Она выплеснулась на снег."

    $ renpy.start_predict("d4_murder_gallery1")
    $ renpy.start_predict("d4_murder_gallery2")
    $ renpy.start_predict("d4_murder_moscow")

    scene bg road_night2
    show blizzard_d4_evening_far
    show blizzard_d4_evening_near zorder 1
    show Ant Dead b_night 00 norm ahead
    with Dissolve(.5)
    play test_two "voice/anton/4day/230. Ah.ogg"
    "Неспособный держать голову ровно, я смотрел в эту красную лужицу." id d4_madrom_no_amulet_2e470940

    play sound "sounds/sfx_Romka_fall_snow.ogg"

    scene d4_pol_drom_blood:
        align (.5, .5)
        linear 0.1 zoom 1.1
        linear 0.1 zoom 1.3
        linear 0.2 zoom 1.6
        linear 0.1 zoom 1.5
    show incar_snow_up
    show bg_black:
        alpha 0
        linear .5 alpha 1
    "Потом я упал в неё лицом."
    "Кровь согрела щёку."
    "Я полежу, и всё пройдёт."
    "Ничего страшного, зашьют врачи..."
    stop music2 fadeout 3.5

    play sound "sounds/sfx_snow_body_roll.ogg"

    play test_four "sounds/loop_breathing_rage.ogg" fadein 1 loop

    "Ромка схватил меня сзади и резко перевернул на спину."
    play music "sounds/Anton's nightmare(without).ogg" fadein 2.5
    "Я увидел его перекошенное лицо и глаза фанатика."

    stop test_four fadeout 2

    scene d4_murder 2:
        yalign 1.
        linear .25 yalign 0.
        "d4_murder 1"
    show blizzard_d4_evening onlayer master1
    play sound "sounds/sfx_knife_pull_out.ogg"

    play test_two"voice/romka/4day/24vzya.ogg"
    "Взяв бабочку обеими руками, зарычав, Рома обрушил оружие вниз."

    play sound "sounds/sfx_knife_stab_3.ogg"

    scene d4_murder 2:
        yalign 0.
        linear .1 yalign 0.7
        linear .1 yalign 0.65
        linear .1 yalign 0.7
    show bg_black:
        alpha 0
        .1
        alpha 0.1
        .05
        alpha 0
    play test_one "sounds/Anton's nightmare(with).ogg"
    "В мой живот."

    show d4_murder 2 as echo:
        yalign .7
        xalign .5
        zoom 1
        alpha .5
        linear 1.5 zoom 1.15 alpha 0
    "Боль поглотила разум."
    "Я не мог пошевелиться."
    "Не мог даже зажмуриться, хотя на зрачках осели горячие росинки."
    scene d4_murder 1:
        yalign 0.7
        linear .25 yalign 0.

    "Нож взмыл вверх."

    play sound "sounds/sfx_knife_stab_2.ogg"

    scene d4_murder 2:
        yalign 0.
        linear .1 yalign 0.7
        linear .1 yalign 0.65
        linear .1 yalign 0.7
    show d4_murder 2 as echo:
        yalign .7
        xalign .5
        zoom 1
        alpha .5
        .1
        linear .5 zoom 1.1 alpha 0
    show bg_black:
        alpha 0
        .1
        alpha 0.1
        .05
        alpha 0
    "Пронзил какой-то пузырь внутри меня."
    scene d4_murder 1:
        yalign 0.7
        linear .25 yalign 0.
    "Взмыл."

    play sound "sounds/sfx_knife_stab_4.ogg"

    scene d4_murder 2:
        yalign 0.
        linear .1 yalign 0.7
        linear .1 yalign 0.65
        linear .1 yalign 0.7
    show bg_black:
        alpha 0
        .1
        alpha 0.1
        .05
        alpha 0
    show d4_murder 2 as echo:
        yalign .7
        xalign .5
        zoom 1
        alpha .5
        .1
        linear .5 zoom 1.1 alpha 0
    "Опустился."
    "Взмыл."
    scene d4_murder loop
    show d4_murder_loop_sfx


    play test_two"voice/romka/4day/246krichal.ogg"
    "Ромка кричал и колол."
    "Кричал и резал."
    show d4_murder loop:
        animation
        blur 3
    show bg_black:
        alpha 0
        linear .5 alpha 0.1
    "Кровь плескалась мне в лицо, взлетала широкими багровыми лентами."
    show d4_murder loop:
        animation
        blur 12
    show bg_black:
        linear .5 alpha 0.2
    "В голове словно вспыхнули десятки огоньков, но сразу же начали гаснуть один за другим."
    show d4_murder loop:
        animation
        blur 30
    show bg_black:
        linear .5 alpha 0.4
    "И те области мозга, в которых погибали эти странные светлячки, погружались во мрак."
    show d4_murder loop:
        animation
        blur 50
    show bg_black:
        linear .5 alpha 0.6
    "Фигура Ромки размывалась."

    hide blizzard_d4_evening onlayer master1
    scene bg_black
    with Dissolve(.5)
    "Я перестал следить за ножом."

    $ renpy.stop_predict("d4_murder 1")
    $ renpy.stop_predict("d4_murder 2")
    $ renpy.stop_predict("d4_murder loop")

    scene bg road_night:
        subpixel True
        align (.0, 1.)
        zoom 2.
        parallel:
            linear 10 yalign 0.
        parallel:
            linear 1. blur 8
            1.
            linear 1. blur 0
            1.
            repeat
    show blizzard_sml:
        parallel:
            xpan 0
            linear 60 xpan -360
            repeat
        parallel:
            ypan 0
            linear 5 ypan -360
            repeat
        parallel:
            linear 1. blur 8
            1.
            linear 1. blur 0
            1.
            repeat
    show blizzard_mid zorder 1:
        parallel:
            xpan 0
            linear 30 xpan -360
            repeat
        parallel:
            ypan 0
            linear 3 ypan -360
            repeat
        parallel:
            linear 1. blur 8
            1.
            linear 1. blur 0
            1.
            repeat
    show romka_dark_plain:
        yalign 1.
        parallel:
            linear 8. yanchor 0.
        parallel:
            linear 1. blur 8
            1.
            linear 1. blur 0
            1.
            repeat
    with Dissolve(.5)
    "Я поднял взгляд – по залитому кровью лицу своего убийцы, вверх, в темнеющее небо."

    scene bg_black
    with Dissolve(1.)
    "За долю секунды я увидел жизнь, которую не проживу."
    show d4_murder_spots onlayer master1:
        alpha 0
        linear 5 alpha .5
    "Миллион упущенных возможностей."
    "Как зритель в пустом кинозале, я смотрел на экран." id d4_madrom_no_amulet_9e2db832
    show d4_murder_baby_bg:
        align (.5, .5)
        zoom 1.
        subpixel True
        linear 20 zoom 1.2
    show d4_murder_baby_noise:
        align (.5, .5)
        zoom 1.
        subpixel True
        linear 20 zoom 1.2
    with Dissolve(.5)
    "Я видел Олю, которая повзрослеет, но я не узнаю об этом."
    "Я видел её детей, которых не подержу на руках."

    scene bg_black
    show bg kitchen_dark1:
        subpixel True
        align (.5, .5)
        alpha .75
        linear 20 zoom 1.2
    show d4_father_old:
        subpixel True
        align (.5, 1.)
        xzoom -1
        xoffset -200
        zoom 1.1
        easein 20 zoom 0.9
    show d4_mutter_old:
        subpixel True
        align (.5, 1.)
        xzoom -1
        xoffset 300
        yoffset 40
        zoom 1.1
        easein 20 zoom 0.9

    with Dissolve(1.)

    $ renpy.stop_predict("d4_murder_baby_bg")
    $ renpy.stop_predict("d4_murder_baby_noise")
    "Стареющих родителей в доме на краю леса."

    show d4_murder_gallery2:
        align (.5, .5)
        zoom 1.
        subpixel True
        linear 20 zoom 0.68
    show d4_murder_gallery1:
        align (.5, .5)
        zoom .68
        subpixel True
        linear 20 zoom 1.
    with Dissolve(.5)
    "Я видел яркий свет в галереях и выставочных залах, чьи стены не украсят мои картины."

    $ renpy.stop_predict("bg kitchen_dark1")
    $ renpy.stop_predict("d4_father_old")
    $ renpy.stop_predict("d4_mutter_old")

    scene d4_murder_moscow:
        subpixel True
        align (.5, .5)
        zoom .67
        easein 30 zoom 1.
    with Dissolve(.5)
    "Мостовые городов, по которым не прошагаю."
    "Двадцать первый век, который настанет не для меня."

    show bg_black:
        alpha 0
        easein 5 alpha .75
    "И просто целую вселенную, состоящую из людей и вещей, навсегда мной утраченных."
    show bg_white:
        alpha 0
        linear .5 alpha 1
    hide bg_black
    show bg_black:
        alpha 0
        1.
        linear 3 alpha 1
    "Ослепительно запылало: то ли в небе, то ли под опускающимися веками."
    "Нож колол и колол, но боль прошла."
    "Тело больше не имело значения."
    hide d4_murder_spots onlayer master1
    with Dissolve(1.)
    $ renpy.stop_predict("d4_murder_gallery1")
    $ renpy.stop_predict("d4_murder_gallery2")
    $ renpy.stop_predict("d4_murder_moscow")
    "Фильм закончился."
    "Я растворился в бесконечной темноте."
    stop music fadeout 3.5

    window hide
    show bg_black:
        linear 3 alpha 1

    jump d4_ending_bad_needle






label d4_home:
    $ story_manager.MarkEvent(("day4", "scene3"))
    jump d4_home.devend
    label d4_home.dev hide:
        scene bg_black
        menu:
            "Маска":
                $ Flags.Raise("mask")
            "Катя, без фото":
                $ Flags.Raise("katya")
            "Катя, с фото":
                $ Flags.Raise("katya")
                $ Flags.Raise("polaroid")
            "Дом Полины":
                $ Flags.Raise("polhouse")
    label d4_home.devend:


    window show

    scene d4_bg_house_night_4
    show blizzard_d4_evening2_far
    show d4_bg_house_tree
    show blizzard_d4_evening2_near
    with Dissolve(0.5)

    if Flags.Has("mask"):
        "Дом темнел на фоне белого поля."

    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 1.2
    play test_one "sounds/sfx_door_home_squeak_distant.ogg" volume 0.2

    "Входная дверь была открыта и чуть покачивалась от ветра."
    play music "music/16_strings0.2-1.ogg" fadein 2
    "Мне показалось, что иней покрывает мою кожу."
    "Я стиснул кулаки."

    stop fon fadeout 2

    if Flags.Has("photo") and Flags.Has("polaroid"):
        "В ладонь впились острые уголки фотографии с останками Кати."

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.3

    show layer master:
        align (.5, .5)
        linear 1. zoom 1.1
    pause .5

    scene d4_home_door_open_dark_bg
    show blizzard_d4_evening2_far:
        xzoom -1
        matrixcolor BrightnessMatrix(-.2)
    show blizzard_d4_evening2_near:
        xzoom -1
        matrixcolor BrightnessMatrix(-.2)
    show d4_home_door_open_dark
    with Dissolve(0.5)

    stop sound fadeout 0.5

    "Мрак просачивался в прихожую, а с ним, медленно планируя на ковёр, влетали снежинки."
    "Будто стая падальщиков, почуявших добычу."
    play test_two "sounds/steps/Anton-steps-steal-1.ogg"

    if Flags.Has("katya"):
        "Я вообразил три мясорубки в разных частях дома и трёх близких людей, перемалываемых лезвиями."

    stop fon fadeout 1
    play sound "sounds/sfx_door_home_close.ogg"

    play test_five "sounds/loop_radio_bg.ogg" fadein 3 loop
    scene d4_home_door_dark with Dissolve(.5)
    "Я осторожно перешагнул порог."
    stop test_two fadeout 1.5

    play sound "sounds/sfx_light_switch.ogg"


    show d4_home_door_evening:
        alpha .5
        .1
        alpha 0
        .05
        alpha 1

    "Вдруг услышал, как кто-то говорит на кухне, но это был всего лишь радиоприёмник."

    stop test_five fadeout 1

    play test_two "sounds/steps/Anton-steps-steal-1.ogg"

    scene d4_house_radio with Dissolve(.5)
    play test_three "sounds/02 MCHS Rossii.ogg"
    stop test_two fadeout 1
    Radio "...циклон, о котором мы предупреждали, движется к региону. Завтра синоптики обещают ветер с порывами до пятнадцати метров." id d4_home_devend_6a300ca5

    scene bg kitchen_dark1 with Dissolve(.5)
    play test_three "sounds/03 MCHS Rossii.ogg"
    Radio "МЧС призвало жителей соблюдать меры предосторожности. Дороги перекрыты, холодная воздушная масса арктического происхождения несёт с собой буран..."
    play test_two "sounds/steps/Anton-steps-steal-1.ogg"

    scene d4_home_door_evening with Dissolve(.5)
    stop test_two fadeout 1
    stop music fadeout 3.5
    stop test_three fadeout 2
    play test_six "voice/karina/4day/207 Sv.ogg"  
    "Сверху тоже доносились голоса."

    if Flags.Has("katya"):
        "Впервые звуки ссоры подействовали успокаивающе."

    play sound "sounds/sfx_footsteps_ladder_creaky.ogg"
    pause .8

    scene d4_hall_walkup 0 with Dissolve(.5)
    "Заскрипели протяжно ступеньки."
    play test_two "sounds/loop_heartbeat_fast_light.ogg" fadein 0.8 loop

    show d4_hall_walkup 1

    stop sound fadeout 0.4
    play test_one "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.8 loop

    play test_seven "voice/father/day4/74ne.ogg"
    play music "music/BlurryMind.ogg" fadein 0.5 
    play test_four"sounds/serdtse.ogg"
    "Я делал шаг, а сердце за это время успевало ударить пять-шесть раз."

    play test_six "voice/karina/4day/208 Sk1.ogg"
    "Дверь родительской комнаты была отворена."

    $ story_manager.MarkEvent(("day4", "scene4"))

    play test_six "voice/karina/4day/209 Sk2.ogg" 
    stop test_four fadeout 5
    "В пятне света выступал театр теней. Чёрные силуэты исполняли танец ненависти."
    play test_six "voice/karina/4day/213 Sk4.ogg"
    "Мамины кисти взметались к потолку, когда она шипела на отца, а он нависал, скрестив руки на широкой груди."
    stop test_two fadeout 2

    stop test_one fadeout 1

    scene d4_home_arguing_bg with Dissolve(.5)

    voice "voice/karina/4day/125 Me.ogg"
    Mam "Мы все в опасности. И всё из-за тебя!"

    play sound "sounds/sfx_put_hand.ogg"

    show d4_home_arguing_ant with Dissolve(.5)
    voice "voice/karina/4day/126 E.ogg"
    Mam "И не ври! Ты видел его в посёлке!"
    voice "voice/karina/4day/127 On.ogg"
    Mam "Он вычислил, где мы живём!"
    voice "voice/father/day4/74 Eto.ogg"
    Pap "Это был не он."
    voice "voice/karina/4day/128 Ya.ogg"
    Mam "Я читала в газетах, на что способны твои дружки."

    hide d4_home_arguing_ant with Dissolve(.5)

    play test_one "sounds/loop_footsteps_home_fast_one.ogg" fadein 0.7 

    if Flags.Has("photo"):
        "Я сунул фотографию в карман и пробежал к спальне."
    else:
        "Я пробежал к спальне."

    stop test_one fadeout 4

    "Родители снова ссорились, выясняли отношения, сыпали взаимными обвинениями."

    scene d4_home_arguing_bg:
        align (.5, .5)
        zoom 1.
        block:
            linear .03 zoom 1.01
            linear .03 zoom 1.00
            repeat

    play test_seven "voice/father/day4/75 Ka.ogg"
    "Отец низко, по-звериному, зарычал."

    scene d4_hall_corridor d1:
        xalign 0
    show Olya Suffer m_evening 01 good ahead 01 dark 50:
        align (.5, 1.)
        xoffset 750
        yoffset 20
        zoom .8
    with Dissolve(.5)

    show Olya Suffer m_evening 01 good ahead 04 dark 50 with Dissolve(.2)
    voice "voice/olya/4day/01 P.ogg"
    Oly "Пусть они прекратят."
    show Olya Suffer m_evening 01 good ahead 01 dark 50 with Dissolve(.2)

    "Оля стояла в коридоре, прижав ладошки к ушам."

    if Flags.Has("katya"):
        "Я отогнал видение, в котором сестру поглощали лезвия мясорубки."
    if Flags.Has("polhouse"):
        "Я отогнал видение, в котором сестру за мои грехи убивал ножом Ромка."

    play test_one "sounds/steps/Olya-steps-4.ogg"
    scene d4_hall_corridor d1:
        xalign 0
    show Olya Weeps m_evening 01 good ahead 00 dark 30:
        xoffset 250
        xzoom -1
    with Dissolve(.5)
    "Опухшее от слёз личико заставило меня похолодеть."

    if Flags.Has("katya"):
        "И почти вытолкнуло из мыслей кровавый образ Кати."
    if Flags.Has("polhouse"):
        "И почти вытолкнуло из мыслей образ скалящегося деда Харитона и скачущего на четвереньках Пятифана."

    voice "voice/anton/4day/168. Chto.ogg"
    Ant "Что случилось?"

    show Olya Prof m_evening 01 good aside 01 dark 30
    with Dissolve(.5)

    show Olya Prof m_evening 01 good aside 06 dark 30 with Dissolve(.2)
    voice "voice/olya/4day/02 O.ogg"
    Oly "Они разведутся."
    play test_one "sounds/steps/Olya-steps-4.ogg"
    show Olya Prof m_evening 01 good aside 01 dark 30 with Dissolve(.2)

    play sound "sounds/sfx_hugs.ogg"

    hide Olya
    hide d4_olya_darkness
    show d4_hall_hug
    with Dissolve(.5)
    "Я обнял сестру и прижал к себе."
    "Язык отказывался повиноваться, искать утешение."
    play test_six "voice/karina/4day/215 M.ogg"
    "Крики будто звучали сразу отовсюду: справа и слева, снизу и сверху. Били по макушке."

    scene d4_room with Dissolve(.5)
    play test_one "sounds/steps/Olya-steps-5.ogg"
    play test_five "voice/karina/4day/216 Ch.ogg"
    stop music fadeout 4.5
    play music2 "music/TremblingMind.ogg" volume 1.3 fadein 2.5
    "Ругань падала нам на головы, и мы прикрыли их руками, как спасающиеся от бомбёжки беженцы."
    show d4_room_2 with Dissolve(.15)
    $ music_during_lines = 0.6
    voice "voice/olya/4day/03 Ya.ogg"
    Oly "Я хочу уйти!"
    hide d4_room_2 with Dissolve(.15)
    voice "voice/anton/4day/169. V.ogg"
    Ant "В свою комнату?"
    show d4_room_2 with Dissolve(.15)
    voice "voice/olya/4day/04 Ne.ogg"
    Oly "Нет! Дальше!"
    hide d4_room_2 with Dissolve(.15)
    show d4_room_2 with Dissolve(.15)
    voice "voice/olya/4day/05 O.ogg"
    Oly "Отведи меня в Небыляндию! Ты обещал!"
    hide d4_room_2 with Dissolve(.15)

    scene d4_hall_corridor d1:
        xalign 0
    show Olya Suffer b_evening 01 good ahead 01 dark 50:
        xoffset 250
        1.
        "Olya Weeps b_evening 01 good ahead 01 dark 50" with Dissolve(.5)
    with Dissolve(.5)



    "Я осторожно отнял её руки от ушей и повёл мимо вибрирующей яростью спальни родителей."

    scene d4_home_arguing_bg with Dissolve(.5):
        align (.5, .5)
        zoom 1.
        block:
            linear .03 zoom 1.005
            linear .03 zoom 1.000
            repeat
    $ music_during_lines = 1.0
    voice "voice/karina/4day/129 Ez.ogg"
    Mam "Из-за тебя!"

    scene d4_home_arguing_bg:
        align (.5, .5)
        zoom 1.
        block:
            linear .03 zoom 1.02
            linear .03 zoom 1.00
            repeat
    voice "voice/father/day4/79 Ra.ogg"
    Pap "Ради кого..."
    scene d4_hall_corridor d1 with Dissolve(.5):
        subpixel True
        xalign 0
        linear 3 xalign 1.

    play test_one "sounds/loop_footsteps_home_normal_two.ogg" fadein 0.8 
    voice "voice/karina/4day/130 To.ogg"
    Mam "Только себя!"

    play sound "sounds/sfx_door_open_slow.ogg" volume 0.6

    show d4_hall_corridor d1 d2 with Dissolve(.5)
    voice "voice/father/day4/80 Ni.ogg"
    Pap "Никогда в жизни!"

    "В эти минуты я презирал их сильнее, чем они презирали друг друга."

    scene bg_room_night1
    show d4_antroom_door
    show Olya Serious m_dark 00 good ahead 01
    with Dissolve(.5)

    stop test_one fadeout 2
    play sound "sounds/sfx_door_room_close_lock.ogg"

    hide d4_antroom_door
    with Dissolve(.5)
    stop music2 fadeout 3
    "В комнате я заперся на шпингалет и прислонился к дверям. Колени подгибались."

    if Flags.Has("mask"):
        play music "music/28_Dejection.ogg" fadein 2.5
        voice "voice/anton/4day/170. Pos.ogg"
        Ant "Послушай, Оля. Мне тоже здесь плохо."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/06 Ti.ogg"
        Oly "Ты хотя бы в школу ходишь!"
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

        play test_three "voice/anton/4day/172. eh.ogg"
        "Я невесело хохотнул."
        voice "voice/anton/4day/171. Eta.ogg"
        Ant "Эта школа — кошмар! Меня там все ненавидят!"
        voice "voice/anton/4day/173. To.ogg"
        Ant "Только одна девочка надо мной не смеётся. Зато жалеет, как побитого пса."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/07Tine.ogg"
        Oly "Ты не пёс! Ты..."
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

        voice "voice/anton/4day/174. Ya.ogg"
        Ant "Я не понимаю, кто я."
        voice "voice/anton/4day/175.No.ogg"
        Ant "Но там, снаружи, ничем не лучше, чем в доме."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/08 Gd.ogg"
        Oly "Где же лучше? Давай пойдём туда! Полетим, поплывём!"
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

        voice "voice/anton/4day/173. Es.ogg"
        Ant "Если б можно было... я бы всё на свете отдал, чтобы уйти и забрать тебя с собой."
        "Верхняя губа Оли дрогнула."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/09K.ogg"
        Oly "Клянёшься?"
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

        "Я горько улыбнулся и сказал:"
        voice "voice/anton/4day/174. Chto.ogg"
        Ant "Чтоб мне умереть!"

        jump d4_beasts

    play music "music/17_Flow.ogg" volume 0.75 fadein 2.5
    show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
    voice "voice/olya/4day/10 Po.ogg"
    Oly "Почему тебя не было так долго?"
    show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

    if Flags.Has("polhouse"):
        voice "voice/anton/4day/176. ya.ogg"
        Ant "Я был в гостях... у одних странных людей."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/12 oni.ogg"
        Oly "Они тоже разводятся?"
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)
    else:

        voice "voice/anton/4day/175.  Y.ogg"
        Ant "Я пытался помочь одной девочке."

        show Olya Serious m_dark 00 good ahead 03 with Dissolve(.2)
        voice "voice/olya/4day/11 T.ogg"
        Oly "Ты помог ей?" id d4_home_devend_f5818d1d
        show Olya Serious m_dark 00 good ahead 01 with Dissolve(.2)

    voice "voice/anton/4day/177. Ne.ogg"
    Ant "Не думаю."

    if Flags.Has("photo"):
        scene d4_table_bg_closed
        show black zorder 1:
            alpha .5
        with Dissolve(.5)
        scene d4_table_bg
        if Flags.Has("number"):
            show d4_table_number
        if Flags.Has("glove"):
            show d4_table_glove
        if Flags.Has("record"):
            show d4_table_record
        if Flags.Has("finger"):
            show d4_table_finger
        show black zorder 1:
            alpha .5
        play test_one "sounds/desk-open-00.ogg"

        with Dissolve(.5)
        show d4_table_photo with Dissolve(.5)
        play test_three "sounds/sfx_listing_photos_2.ogg"
        "Заслонив письменный стол, я осторожно выдвинул ящик и бросил туда фотографию с окровавленной Катиной косой."

        play test_one "sounds/desk-close-00.ogg"
        scene d4_table_bg_closed
        show black zorder 1:
            alpha .5
        with Dissolve(.5)

        scene bg_room_night1
        show Olya Serious m_dark 00 good ahead 01
        with Dissolve(.5)

        "Оля попыталась заглянуть мне за спину, но я резко закрыл его."

    jump d4_beasts


label d4_beasts:
    $ story_manager.MarkEvent(("day4", "scene5"))
    stop music fadeout 1
    play test_two "sounds/hit-chord-3.ogg"
    play sound "sounds/sfx_snowball_window_hit_1.ogg"

    show Olya Serious m_dark 00 good ahead:
        linear .05 yoffset 10
        linear .05 yoffset 0
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.3)

    if Flags.Has("photo"):
        play test_six "voice/olya/4day/13 A.ogg"
        "И одновременно с этим что-то стукнуло о карниз снаружи."
    else:
        play test_six "voice/olya/4day/13 A.ogg"
        "Что-то стукнуло о карниз снаружи."
        play fon "sounds/hum-1.1.ogg" fadein 1.5

    show Olya Weeps m_dark 00 good aside 04 with Dissolve(.15)
    "Оля вздрогнула и бросила взгляд на окно."

    play sound "sounds/sfx_snowball_window_hit_2.ogg"

    show Olya Weeps m_dark 00 good aside 04:
        linear .05 yoffset 10
        linear .05 yoffset 0
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.25)
    play test_six "voice/olya/4day/15 Ah.ogg"
    "«Бам!» — снежок повторно шлёпнулся в раму."
    show Olya Weeps m_dark 00 good aside 04 with Dissolve(.25)
    show Olya Weeps m_dark 00 good ahead 01 with Dissolve(.25)
    voice "voice/olya/4day/14 Ti.ogg"
    Oly "Ты ждёшь кого-то?"
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.25)
    "Я не ответил."
    show Olya Weeps m_dark 00 good ahead 03 with Dissolve(.15)
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.25)

    play sound "sounds/sfx_put_hand.ogg" 

    play test_six "voice/olya/4day/15 Aw.ogg"
    "Отпустил её запястье – она всхлипнула испуганно."

    play test_one "sounds/loop_footsteps_home_normal_one.ogg" fadein 0.7 
    play sound ["sounds/sfx_plates_break.ogg","<silence .5>","sounds/sfx_footsteps_home_parents.ogg"]

    "Я прошёл по комнате, морщась от каждого родительского вскрика. Билась посуда – папа с мамой переместились на кухню."
    window hide

    stop test_one fadeout 0.8

    call screen day4_open_stora

    play test_one "sounds/Phrases_02.ogg"
    stop fon fadeout 1.5
    play sound "sounds/sfx_curtain_move_window_open.ogg"
    play test_five "sounds/loop_wind_window.ogg" fadein 1.6 loop

    scene d4_window_bg_base:
        xalign .7
        linear .15 xalign .5
    show d4_window_bg_owl idle zorder 1:
        xalign .7
        linear .15 xalign .5
    show d4_window_bg_fox idle zorder 2:
        xalign .7
        linear .15 xalign .5
    show d4_window_bg_bear idle zorder 4:
        xalign .7
        linear .15 xalign .5
    show d4_window_bg_wolf idle zorder 3:
        xalign .7
        linear .15 xalign .5

    show snow_night_1 zorder 5
    show blizzard_d4_evening_face zorder 5:
        matrixcolor BrightnessMatrix(-.2)

    show layer master:
        blur 8

    show d4_window_frame onlayer master1:
        xalign 0.5
        linear .15 xalign .0
        .25
        "d4_window_frame2" with Dissolve(.25)
    show day3_window_anton onlayer master1:
        xanchor .5
        ypos 1080
        xpos 1950
        yanchor 1.
        linear .15 xpos 1650

    show layer master1:
        blur 0
    "Я отдёрнул штору и рывком распахнул окно."
    play music "music/Flute 2(reverb).ogg" volume 0.6 fadein 0.5


    show layer master:
        blur 0
    show layer master1:
        blur 8

    with Dissolve(1.00)

    pause .5

    show d4_window_bg_owl wave
    show d4_window_bg_fox wave
    show d4_window_bg_bear wave
    show d4_window_bg_wolf wave
    "Совушка, Медвежутка, Волчик и, конечно, пленительная Алиса, – все были в сборе и махали нам снизу."

    show d4_window_bg_owl waveoff
    show d4_window_bg_fox waveoff
    show d4_window_bg_bear waveoff
    show d4_window_bg_wolf waveoff
    play test_six "voice/olya/4day/15 Oi.ogg"
    "Оля ойкнула, завидев девочку-птицу."

    voice "voice/olya/4day/16 Ya.ogg"
    Oly "Я же говорила."
    voice "voice/anton/4day/178. Da.ogg"
    Ant "Да, знаю. Я тебе всегда верил."
    voice "voice/olya/4day/17 K.ogg"
    Oly "Кто они?"
    "Помимо страха, в голосе звучало любопытство."

    $ music_during_lines = 0.85
    show d4_window_bg_fox wave
    voice "voice/Alisa/4day/05Chob.ogg"
    Alis "Чтобы в такую погоду дома сидеть, надо быть очень скучными детьми!"
    show d4_window_bg_fox waveoff
    show d4_window_bg_owl wave
    voice "voice/Owl/4day/06 U.ogg"
    Owl "У нас столько игр неигранных – ух-ух-ух!"
    show d4_window_bg_owl waveoff
    show d4_window_bg_bear wave
    voice "voice/Bear/4day/22 Dav.ogg"
    Bear "Давайте только не во все игры играть, а то у меня лапка болит."
    voice "voice/Bear/4day/23 Po.ogg"
    Bear "По чуть-чуть — и потом отдохнём."
    show d4_window_bg_bear waveoff
    show d4_window_bg_wolf wave
    voice "voice/Wolf/317 Dr.ogg"
    Wolf "Др-р-р-рузья!"
    show d4_window_bg_bear wave
    show d4_window_bg_fox wave
    show d4_window_bg_owl wave
    voice "voice/Alisa/4day/05Vihod.ogg"
    Animals "Выходите скорее играть и танцевать!"
    show d4_window_bg_owl waveoff
    show d4_window_bg_fox waveoff
    show d4_window_bg_bear waveoff
    show d4_window_bg_wolf waveoff
    "При виде Алисы сердце забилось сильнее, а внутренний голос буквально кричал: {i}«Наконец-то! Она здесь!»{i}"
    $ music_during_lines = 1.0
    voice "voice/olya/4day/18 A.ogg"
    Oly "А они знают, как попасть в Небыляндию?"
    "Я прикидывал, глядя на зверят."
    play test_two "sounds/sfx_window_close.ogg"

    stop test_five fadeout 2

    $ renpy.scene("master1")
    scene n02
    show Olya Serious m_evening 01 good ahead 01 zorder 1
    with Dissolve(.5)

    show n03
    with Dissolve(.5)
    voice "voice/anton/4day/179. Mo.ogg"
    Ant "Может быть. Пойдём и узнаем!"

    play test_two "sounds/steps/Olya-steps-5.ogg"

    play test_one "sounds/loop_footsteps_home_normal_two.ogg" fadein 0.8 

    hide Olya Serious m_evening 01 good ahead A_01
    with Dissolve(.5)

    play sound "sounds/Door_open_2.ogg" volume 0.5

    scene n04
    with Dissolve(.5)
    pause .5

    scene d4_hall_corridor d2:
        xalign 1.
    with Dissolve(.5)
    scene d4_hall_corridor:
        xalign 1.
    with Dissolve(.5)
    scene d4_hall_corridor:
        xalign 1.
        linear 2 xalign 0.

    play test_three "sounds/close-door.ogg"

    "Фигурки лесных друзей обещали избавление от горя, гнева и ужасов ночи."
    stop music fadeout 2.5
    play music2 "music/Kaite1.ogg" fadein 2.5

    stop test_one fadeout 1.6

    scene bg door_night
    with Dissolve(.5)

    play test_one "sounds/steps/Olya-steps-3.ogg"
    show Olya Serious m_evening_winter 02 good ahead 01
    with Dissolve(.5)

    play test_seven "voice/father/day4/78 Tiv.ogg"
    "Я проследил, чтобы Оля закуталась потеплее."

    play sound "sounds/sfx_hat_adjust.ogg"

    show Olya Serious m_evening_winter 00 good ahead 01
    with Dissolve(.5)

    scene bg door_open_night
    show Olya Serious m_evening_winter 00 good ahead 01
    with Dissolve(.5)
    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 1.2
    play sound "sounds/Door_open.ogg"
    $ add_text_to_dictionary(43)
    play test_six "voice/karina/4day/218 Nu.ogg"
    "Мама лаяла на отца отрывисто, как дикое животное из передачи {u}Николая Дроздова.{/u}"

    play test_one "<from 0 to 2>sounds/loop_footsteps_home_normal_two.ogg"

    hide Olya with Dissolve(.5)
    play test_one "sounds/Door_close.ogg"
    scene bg door_night with Dissolve(.5)


    scene d4_bg_house_night_7
    show snow_night_1
    with Dissolve(.5)


    play test_six "voice/karina/4day/217 Bu.ogg"
    stop music2 fadeout 3.5
    "Мы просеменили мимо гремящей кухни и выскользнули под снегопад."

    play test_one "sounds/loop_footsteps_two.ogg" fadein 0.4 loop

    scene d3_outside_guys_bg
    show Fox Normal m_night 00 dark 70:
        align (.5, 1.)
        xoffset -100
        yoffset 30
        zoom .8
    show d4_fence
    show d4_snow_night
    with Dissolve(.5)

    pause .5

    show Fox Normal m_night 00 dark 70:
        align (.5, 1.)
        xoffset -100
        yoffset 30
        zoom .8
        linear .5 xoffset -75 alpha 0

    stop test_one fadeout 1.5
    pause .5

    play test_two "sounds/loop_footsteps_snow_fast.ogg" fadein 2

    hide Fox
    show Fox Normal m_night 00:
        zoom 1.
        xoffset -25
        yoffset 50
        alpha 0
        matrixcolor BrightnessMatrix(0.0)
        linear .5 xoffset 0 alpha 1
    pause .9

    show Fox Normal m_night 00:
        zoom 1.
        xoffset 0
        yoffset 50
        alpha 1
        matrixcolor BrightnessMatrix(0.0)

    play sound "sounds/sfx_hugs_strike.ogg"
    pause .25
    stop test_two fadeout 0.35
    stop test_six fadeout 0.5
    play music "music/18_Olya_(piano&strings).ogg" volume 0.8 fadein 0.5
    "Ко мне тут же подбежала Алиса и обняла меня, уткнувшись холодным носом в шею."

    show Fox Normal m_night 00 good ahead
    voice "voice/Alisa/4day/55 Kak.ogg"
    Alis "Как же долго-о-о!"
    voice "voice/Alisa/4day/56 Poka.ogg"
    Alis "Пока мы вас, домоседов, ждали, то чуть не состарились."


    play test_two "sounds/sfx_footsteps_snow_slow.ogg"

    show Fox Normal b_night 00 good ahead with Dissolve(.5):
        yoffset 0
        align (.5, 1.)
    play sound "sounds/sfx_hugs.ogg"
    "Она прижалась ещё сильнее."


    $ renpy.music.set_pan(-0.6, delay=0, channel="test_three")
    play test_three "sounds/sfx_footsteps_snow_slow.ogg"

    show Bear Normal m 00 dark 50 behind d4_fence with Dissolve(.5):
        xoffset -800
        yoffset 30
        align (.5, 1.)
        zoom .8
        linear .5 xoffset -750
    show Bear Normal m 01 dark 50 with Dissolve(.2)
    voice "voice/Bear/4day/25 Okaz.ogg"
    Bear "Оказывается, ждать так утомительно."
    voice "voice/Bear/4day/26 Fuh.ogg"
    Bear "Фух! Дайте хоть минуточку в себя прийти."
    show Bear Normal m 00 dark 50 with Dissolve(.2)

    $ renpy.music.set_pan(0.45, delay=0, channel="test_two")
    play test_two "sounds/sfx_footsteps_snow_slow.ogg"

    show Owl Normal m 00 dark 50 behind d4_fence with Dissolve(.5):
        xoffset 800
        yoffset 30
        align (.5, 1.)
        zoom .8
        linear .5 xoffset 750
    show Owl Normal m 01 dark 50 with Dissolve(.2)
    voice "voice/Owl/4day/06 Od.ogg"
    Owl "Однажды я тоже долго собиралась – уху, – а когда закончила, то и вовсе забыла куда."
    show Owl Normal m 00 dark 50 with Dissolve(.2)

    scene d4_hfence_bg
    show d4_snow_night2
    show d4_hfence_fence as fleft zorder 1:
        yalign 1.
        xpos .0
        xanchor .90
    show d4_hfence_fence as fright zorder 1:
        yalign 1.
        xpos 1.
        xanchor .12
    show Olya Serious b_evening_winter 01 good ahead 01:
        xpos 200
    show bg_black:
        alpha .3
    with Dissolve(.5)
    "Оля смотрела на Сову с подозрением."

    play sound "sounds/sfx_snow_roll.ogg"

    play test_three "voice/Owl/4day/23 Sm.ogg" 
    play test_six "sounds/sfx_owl_lands_snow.ogg"
    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.1):
        linear .1 yoffset 20
        linear .1 yoffset 0
        "Olya Happy b_evening_winter 01 good ahead 01" with Dissolve(.2)
    play test_two "voice/olya/4day/19 S.ogg"

    "Но хихикнула, когда та вдруг перекувыркнулась через себя и лихо встала на снег, даже не пошатнувшись."

    scene d3_outside_guys_bg
    show d4_fence
    show d4_snow_night2

    show Bear Normal m 00 dark 50 behind d4_fence:
        xoffset -750
        yoffset 30
        align (.5, 1.)
        zoom .8
    show Owl Normal m 00 dark 50 behind d4_fence:
        xoffset 750
        yoffset 30
        align (.5, 1.)
        zoom .8
    show Fox Normal b_night 00 good ahead:
        align (.5, 1.)
    with Dissolve(.5)
    "Остальные звери, как по команде, перестали дурачиться и тоже заворожённо посмотрели на Олю."
    show Owl Normal m 01 dark 50 with Dissolve(.2)
    voice "voice/Owl/4day/04 Eto.ogg"
    Owl "Это же та девочка, что не хотела со мной дружить!"
    show Owl Normal m 00 dark 50 with Dissolve(.2)

    scene d4_hfence_bg
    show d4_snow_night2
    show d4_hfence_fence as fleft zorder 1:
        yalign 1.
        xpos .0
        xanchor .90
    show d4_hfence_fence as fright zorder 1:
        yalign 1.
        xpos 1.
        xanchor .12
    show Olya Happy b_evening_winter 01 good ahead 01:
        xpos 200
    show bg_black:
        alpha .3
    with Dissolve(.5)

    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.2)
    $ music_during_lines = 0.8
    voice "voice/olya/4day/20 M.ogg"
    Oly "Меня зовут Оля."
    show Olya Happy b_evening_winter 01 good ahead 01 with Dissolve(.2)
    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.2)
    voice "voice/olya/4day/21 R.ogg"
    Oly "Раньше я... Ну... Я просто тебя боялась."
    show Olya Happy b_evening_winter 01 good ahead 01 with Dissolve(.2)

    scene d3_outside_guys_bg
    show d4_fence
    show d4_snow_night2
    show Bear Normal m 00 dark 50 behind d4_fence:
        xoffset -750
        yoffset 30
        align (.5, 1.)
        zoom .8
    show Owl Normal m 00 dark 50 behind d4_fence:
        xoffset 750
        yoffset 30
        align (.5, 1.)
        zoom .8
    show Fox Normal b_night 00 good ahead:
        align (.5, 1.)
    with Dissolve(.5)

    show Fox Flirt b_night 01 good ahead with Dissolve(.2):
        align (.5, 1.)
        linear .1 yoffset 20
        linear .1 yoffset 0
    $ music_during_lines = 1.0
    voice "voice/Alisa/4day/57 Teb.ogg"
    Alis "Тебя испугала наша Совушка?"
    show Fox Normal b_night 00 good ahead
    show Bear Normal m 01 dark 50
    with Dissolve(.2)
    voice "voice/Bear/4day/27 Moz.ogg"
    Bear "Может быть, у неё совофобия?"
    show Owl Normal m 01 dark 50
    show Bear Normal m 00 dark 50
    with Dissolve(.2)
    voice "voice/Owl/4day/05 A.ogg"
    Owl "А это лечится?"
    show Owl Normal m 00 dark 50
    show Fox Flirt b_night 01 good ahead:
        align (.5, 1.)
        linear .1 yoffset 20
        linear .1 yoffset 0
    with Dissolve(.2)
    voice "voice/Alisa/4day/58 Glavn.ogg"
    Alis "Главное, чтобы ребёнок не боялся веселиться."
    show Fox Oh b_night 02 good ahead with Dissolve(.2):
        align (.5, 1.)
        linear .1 yoffset 20
        linear .1 yoffset 0
        3.
        block:
            linear .1 yoffset 20
            linear .1 yoffset 0
            repeat 9
    voice "voice/Alisa/4day/59 Inach.ogg"
    Alis "Иначе с нами можно умереть от страха. Аха-ха-ха-ха!"
    show Fox Normal b_night 00 good ahead with Dissolve(.2)
    show Fox Fullface b_night 00 good ahead with Dissolve(.2):
        align (.5, 1.)
    "Я поразился, поняв, что губы мои складываются в улыбку."

    if Flags.Has("polhouse"):
        "И это после всего, что я видел в гостях у Полины!"
    if Flags.Has("katya"):
        "И это после всего, что я видел в Гараже!"

    "Встречаясь с Алисой, я будто переходил через реку, журчание которой глушило все дурные мысли."

    scene d4_hfence_bg
    show d4_snow_night2
    show d4_hfence_fence as fleft zorder 1:
        yalign 1.
        xpos .0
        xanchor .90
    show d4_hfence_fence as fright zorder 1:
        yalign 1.
        xpos 1.
        xanchor .12
    show Olya Amaze b_evening_winter 01 good ahead 01:
        xpos 200
    show bg_black:
        alpha .3
    with Dissolve(.5)

    stop music fadeout 1.5
    play music2 "music/Sweet Bunny.ogg" volume 0.9 fadein 3.5
    show Olya Amaze b_evening_winter 01 good ahead 05 with Dissolve(.2)
    voice "voice/olya/4day/22 Ka.ogg"
    Oly "Какие у вас красивые костюмы!"

    play sound "sounds/sfx_footstep_snow_step_down.ogg"

    show Olya Amaze b_evening_winter 01 good ahead 01 with Dissolve(.2)

    show Fox Back zorder 1:
        xpos -100
        alpha 0
        linear .5 xpos 0 alpha 1
    show Olya Amaze b_evening_winter 01 good aside 01 with Dissolve(.5)
    "Девочка-лисичка разжала свои объятия и присела рядом с Олей."
    voice "voice/Alisa/4day/60 Oo.ogg"
    Alis "О, какая очаровашка!"
    voice "voice/Alisa/4day/61 Anto.ogg"
    Alis "Антоша, почему ты прятал от нас это милое создание раньше?"

    scene d4_house_night_snowless with Dissolve(.5)
    "Я покосился на дом, опасаясь, что родители могли заметить нас и как всегда испортить всё веселье."
    "И сказал, обняв сестру:"
    voice "voice/anton/4day/180.Da.ogg"
    Ant "Давайте отойдём подальше."
    voice "voice/Alisa/4day/62 Zapr.ogg"
    Alis "Запросто!"
    $ renpy.music.set_pan(0, delay=0, channel="test_three")
    play test_three "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 1 

    scene day3_night_sky_rnd with Dissolve(.5)
    pause .5
    show Fox Normal m_night 00 good ahead with Dissolve(.5):
        xpos -300
        yoffset 20
        xoffset 75
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
        parallel:
            linear .5 xoffset 0
    stop test_three fadeout 2
    $ add_text_to_dictionary(46)
    voice "voice/Alisa/4day/63 Ol.ogg"
    Alis "Оля, а ты знаешь, как найти в нашем лесу Деда Мороза?"
    play test_three "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 1

    show Olya Serious m_evening_winter 01 good ahead 01 with Dissolve(.5):
        xzoom -1
        xpos 300
        yoffset 15
        xoffset 75
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 15
        parallel:
            linear .5 xoffset 0
    stop test_three fadeout 2
    "Глаза сестрёнки округлились."

    stop test_three fadeout 1.5

    show Olya Amaze m_evening_winter 01 good ahead 01 with Dissolve(.5)
    show Olya Amaze m_evening_winter 01 good ahead 02 with Dissolve(.2)
    voice "voice/olya/4day/23 K.ogg"
    Oly "Как?"
    show Olya Amaze m_evening_winter 01 good ahead 01 with Dissolve(.2)
    show Fox Nice m_night 00 good ahead with Dissolve(.2)
    voice "voice/Alisa/4day/64 Nu.ogg"
    Alis "Нужно идти по сладкой тропинке."
    show Fox Normal m_night 00 good ahead with Dissolve(.2)

    play sound "sounds/sfx_snow_grab_candy.ogg"

    show Fox Normal m_night 00 good ahead:
        xpos -300
        linear .5 xoffset 75 yoffset 500
        .25
        linear .5 yoffset 0

    show d4_fox_give_bg:
        alpha 0
        pause 1.
        linear .5 alpha 1
    show d4_fox_give_3:
        alpha 0
        pause 1.
        linear .5 alpha 1
    show d4_fox_give_5:
        alpha 0
        pause 1.
        linear .5 alpha 1
    "Алиса наклонилась и вынула из снега конфету."
    play test_six "voice/olya/4day/24 A.ogg"
    "Оля всплеснула ладошками."
    "Посмотрела на меня вопросительно — я кивнул."
    play test_one "sounds/sfx_candies.ogg"

    scene d4_fox_give_bg
    show d4_fox_give_3 zorder 1
    with Dissolve(.5)
    play test_four "sounds/sfx_candy_crunch.ogg"
    "Сестра захрустела конфетой."

    play sound "sounds/sfx_footstep_snow_step_down.ogg"

    show d4_fox_give_owl 1 with Dissolve(.5)
    voice "voice/Owl/4day/10 Un.ogg"
    Owl "У нас что – уху – в лесу завёлся Дед Мороз?"
    voice "voice/Owl/4day/11 Po.ogg"
    Owl "Почему — ух-ху — ты мне не рассказывала?"
    voice "voice/Alisa/4day/65 ya.ogg"
    Alis "Я рассказывала. Сегодня днём."

    show d4_fox_give_owl 2 with Dissolve(.5)
    voice "voice/Owl/4day/23 No.ogg"
    Owl "Но ведь днём я сплю."
    voice "voice/Alisa/4day/66 Aga.ogg"
    Alis "Ага. Вот я и рассказывала, пока ты спала."

    if Flags.Has("polhouse"):
        scene day3_night_sky_rnd
        show Ant Cho b_night 00 norm ahead 01
        with Dissolve(.5)
        "Слушая их ребяческую болтовню, я почему-то вспомнил Ромку."
        "Как во время погони тот истошно закричал всего за пару минут до появления Волчка."
        show Ant Cho b_night 00 norm ahead 02 with Dissolve(.2)
        voice "voice/anton/4day/181. Chto.ogg"
        Ant "Что случилось с Ромкой?"
        show Ant Cho b_night 00 norm ahead 01 with Dissolve(.2)

        scene bg_forest0_long_dark:
            xpos -1160


        show Owl Normal m 00 at owl_pos
        show Fox Normal m_night 00 at fox_pos

        with Dissolve(.5)
        play sound "sounds/sfx_footsteps_snow_slow.ogg"

        pause .25        
        python:
            wolf_zoom_cur = step_in
            wolf_sprite_cur = wolf_Normal

        show Wolf Normal m 00 at wolf_pos:
            alpha 0
            zoom step_in
            xoffset -100
            linear .5 xoffset 0 alpha 1

        voice "voice/Wolf/319 Pov.ogg"
        Wolf "Повер-р-рь, он в пор-р-рядке!"
        call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_13

        call fox_upd (fox_Flirt, step_in) from _call_fox_upd_40
        voice "voice/Alisa/4day/67 Ziv.ogg"
        Alis "Жив-здоров твой Ромка."
        voice "voice/Alisa/4day/68 Tol.ogg"
        Alis "Только такой вредина, как он, вряд ли получит от Деда Мороза подарок."
        voice "voice/Alisa/4day/69 mak.ogg"
        Alis "Максимум — горсть угля."
        call fox_upd (fox_Normal, step_out) from _call_fox_upd_41

        python:
            bear_zoom_cur = step_in
            bear_sprite_cur = bear_Normal

        play sound "sounds/sfx_footsteps_snow_slow.ogg"
        show Bear Normal m 00 at bear_pos:
            alpha 0
            zoom step_in
            xoffset -100
            linear .5 xoffset 0 alpha 1
        voice "voice/Bear/4day/48Nu.ogg"
        Bear "Ну или по шапке."
        $ bear_sprite_cur = bear_Normal

        play test_three "voice/Bear/4day/50.ogg"
        play test_two "voice/Wolf/340 Smeh.ogg"

        call bear_upd (bear_Paw, step_out) from _call_bear_upd_23

        pause .5

        $ laugh_amt = 12
        call bear_upd (bear_Paw, step_out, jump_amt=11, jump_offset=25, jump_speed=0.17) from _call_bear_upd_24
        call wolf_upd (wolf_Normal, step_out, jump_amt=18, jump_offset=15, jump_speed=0.10) from _call_wolf_upd_14
        call fox_upd (fox_Normal, step_out, jump_amt=12, jump_offset=25, jump_speed=0.15) from _call_fox_upd_42
        pause 1.
        call owl_upd (owl_Alter) from _call_owl_upd_22
        pause 1.5
        play test_six "voice/Owl/4day/13 Hihi.ogg"
        call owl_upd (owl_Normal, step_out, jump_amt=11, jump_offset=20, jump_speed=0.16) from _call_owl_upd_23
        "Медвежутка комично погрозил перебинтованной лапой, и зверята дружно расхохотались."

        hide bear_sprite_cur
        hide wolf_sprite_cur
        show Bear Normal m 00 at bear_pos:
            xoffset 0
        show Wolf Normal m 00 at wolf_pos:
            xoffset 0
        with Dissolve(.5)
        play sound "sounds/steps/steps_snow001.ogg"
        show Bear Normal m 00 at bear_pos:
            linear .5 xoffset 100 alpha 0
        pause .1
        show Wolf Normal m 00 at wolf_pos:
            linear .5 xoffset 100 alpha 0
        pause .15

        "Моя едва проснувшаяся тревога тут же забылась, улеглась."
        play test_three "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 0.5


    $ renpy.music.set_pan(0.4, delay=0, channel="test_three")
    $ renpy.music.set_volume(0.35, delay=0, channel="test_three")
    stop music2 fadeout 1.5
    play test_three "sounds/loop_footsteps_snow_normal.ogg"

    scene bg_forest0_long_dark:
        xpos -1160

    show Owl Normal m 00 at owl_pos:
        xoffset 0
    show Fox Normal m_night 00 at fox_pos:
        xoffset 0

    show Owl Normal m 00 at owl_pos:
        linear .5 xoffset 100 alpha 0

    pause .5

    stop test_three fadeout 1.2
    play sound "sounds/sfx_footsteps_snow_slow.ogg"
    play test_seven "sounds/sfx_sparks.ogg"

    show Fox Normal m_night 00 at fox_pos:
        linear .5 zoom 1.65 yalign .5 yoffset 150

    pause .75

    show Fox Normal m_night 00 good dark with Dissolve(.25)
    play music "music/Snowballs.ogg" fadein 1.5
    pause .25

    play sound ["<silence 1.2>", "sounds/loop_footsteps_snow_fast.ogg"]
    $ renpy.music.set_pan(0.5, delay=4, channel="sound")

    hide Fox
    show d4_fox_tail_animation:
        align (.5, 1.)
        xoffset -100
        yoffset 20
        1.2
        parallel:
            linear 2 xoffset 900
        parallel:
            linear .2 yoffset 0
            linear .2 yoffset 20
            repeat

    with Dissolve(.35)

    pause 4.
    stop sound fadeout 1.4



    "Алиса кинулась прочь, вильнув рыжим хвостом, точно факелом."

    $ renpy.music.set_pan(0, delay=0, channel="test_three")
    $ renpy.music.set_volume(1, delay=0, channel="test_three")
    play test_three "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 0.7 volume 0.65 loop

    $ story_manager.MarkEvent(("day4", "scene6"))

    scene d4_procession_bg:
        align (.5, .8)
        easein 60 zoom 1.6
    show d4_procession_fox:
        linear .43 yoffset 14
        linear .43 yoffset 0
        repeat
    show d4_procession_wolf:
        linear .35 yoffset 10
        linear .35 yoffset 0
        repeat
    show d4_procession_owl:
        linear .42 yoffset 13
        linear .45 yoffset 0
        repeat
    show d4_procession_bear:
        linear .50 yoffset 21
        linear .50 yoffset 0
        repeat
    show d4_procession_anton:
        linear .38 yoffset 35
        linear .48 yoffset 0
        repeat
    show d4_procession_olya:
        linear .38 yoffset 20
        linear .48 yoffset 0
        repeat
    show d4_procession_fg:
        align (.5, 1.)
        linear 8 zoom 1.2 xoffset -305

    with Dissolve(.5)
    play test_six "voice/olya/4day/25 Ha.ogg"
    "Оля инстинктивно двинулась за ней и засмеялась, вынув из сугроба вторую конфету."

    show d4_procession_bear alter with Dissolve(.25)
    voice "voice/Bear/4day/30 Vi.ogg"
    Bear "Вы такие бодрые, на вас аж смотреть противно."
    voice "voice/olya/4day/26 Ati.ogg"
    Oly "А ты давай не зевай."

    stop test_three fadeout 1.2

    scene d4_procession_talkback_bg_1:
        xalign .5
    show d4_procession_talkback_bg_2:
        xalign .5
    show d4_procession_talkback_bg_3:
        xalign .5

    $ renpy.music.set_pan(0, delay=0, channel="sound")
    play sound ["<silence 0.5>", "sounds/sfx_candy_rustle.ogg"]

    show Ant Dark 2:
        align (.5, 1.)
        zoom 1.2
        xoffset -250
        1.
        "Ant Dark 1" with Dissolve(.5)
    show Olya Happy b_dark 00 good ahead 02:
        align (.5, 1.)
        zoom 0.8
        yoffset 50
        xoffset 250
    show d4_procession_olya_hand:
        align (.5, 1.)
        zoom 0.8
        xoffset 250
        yoffset 150
        linear .75 yoffset 50
    with Dissolve(.5)

    show Olya Happy b_dark 00 good ahead 04 with Dissolve(.2)
    voice "voice/olya/4day/26 Lu.ogg"
    Oly "Лучше беги с нами к Деду Морозу, пока все подарки не разобрали."
    show Olya Happy b_dark 00 good ahead 02 with Dissolve(.2)

    voice "voice/Bear/4day/31 Ska.ogg"
    Bear "Скажешь тоже!"

    scene d4_candy_shower_0 with Dissolve(.5)
    voice "voice/Bear/4day/32 Skoree.ogg"
    Bear "Скорее уж мне на голову свалится три кило конфет, чем я поверю в байки лисицы."

    scene d4_candy_shower_1 with Dissolve(.5)
    pause .5

    play test_two "sounds/loop_candy_shower.ogg" loop

    scene d4_candy_shower_animation
    pause .5
    play test_six "voice/olya/4day/25 Haha.ogg"
    play test_three "voice/Bear/4day/33 Oi.ogg" 
    "Когда сладости стали падать на макушку медведя, я сам не удержался от смеха – так забавно он ойкал и втягивал шею."

    stop test_six fadeout 1.2
    stop test_two fadeout 1

    scene d4_candy2_bg
    show d4_zefir_spark_animation
    with Dissolve(.5)
    pause .5
    show d4_zefir_bear
    with Dissolve(.5)
    stop test_three fadeout 1
    play test_two "sounds/sfx_footsteps_snow_slow.ogg"
    play test_three "voice/Bear/4day/36 Chih.ogg"
    "Угощения переливались на снегу. Медведь чихнул и достал из уха «Мишки на севере»."
    voice "voice/Bear/4day/34 Yab.ogg"
    Bear "Я бы вздремнул часок, а уж потом пересчитал все эти шоколадки."
    voice "voice/Bear/4day/35Umen.ogg"
    Bear "У меня такое подозрение, что тут не больше килограмма."

    scene d4_procession_talkback_bg_1:
        xalign .5
    show d4_procession_talkback_bg_2:
        xalign .5
    show d4_procession_talkback_bg_3:
        xalign .5

    show Ant Dark 1:
        align (.5, 1.)
        zoom 1.2
        xoffset -250
        yoffset 30
    show Olya Happy b_dark 00 good ahead 02:
        align (.5, 1.)
        zoom 0.8
        yoffset 50
        xoffset 250
    show d4_procession_olya_hand:
        align (.5, 1.)
        zoom 0.8
        xoffset 250
        yoffset 50
    with Dissolve(.5)
    "Со стороны леса донёсся крик Алисы:"

    show Ant Dark 5
    show Olya Happy b_dark 00 good aside 02
    with Dissolve(.5)

    voice "voice/Alisa/4day/70 Ne.ogg"
    Alis "Не в этой жизни!"
    voice "voice/Alisa/4day/71 Dav.ogg"
    Alis "Давайте скорее, Дед Мороз уже заждался нас во дворце!"

    play sound ["<silence 0.4>","sounds/loop_footsteps_snow_fast.ogg"] fadein 0.5 loop

    show Ant Dark 5:
        .5
        parallel:
            linear .5 xoffset -50
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 30
        parallel:
            .25
            linear .25 alpha 0

    show d4_procession_talkback_bg:
        "empty"
        1.5
        xalign .5
        "d4_procession_talkback_bg_crop" with Dissolve(.5)

    "Я пожал плечами. И побежал, потому что от бега злые тиски страха ослабевали."

    $ renpy.music.set_pan(0, delay=0, channel="test_two")

    stop sound fadeout 1
    play test_two ["sounds/sfx_marshmallow_fly.ogg", "sounds/sfx_marshmallow_fall.ogg"]

    scene d4_zefir_animation
    "Что-то круглое пролетело возле моего виска. Я решил, что это снежок, но Оля воскликнула:"

    play sound "sounds/sfx_footstep_snow_light.ogg"

    scene d4_zefir_bg
    show d4_zefir_olya
    show d4_zefir_spark_animation zorder 1
    with Dissolve(.5)
    $ add_text_to_dictionary(47)
    voice "voice/olya/4day/29Z.ogg"
    Oly "Зефир!"

    play sound "sounds/sfx_footstep_snow_normal.ogg"

    show d4_zefir_anton with Dissolve(.5)
    voice "voice/anton/4day/182. Ne.ogg"
    Ant "Не подбирай, он испачкался."

    play sound "sounds/sfx_footsteps_snow_slow.ogg"

    hide d4_zefir_olya
    hide d4_zefir_anton
    show d4_zefir_fox
    with Dissolve(.5)
    voice "voice/Alisa/4day/72 Ti.ogg"
    Alis "Ты что, веришь в микробов?"

    scene d4_procession_bg
    show Fox Flirt b_night 00 good ahead
    with Dissolve(.5)
    show Fox Fullface b_night 00 good ahead with Dissolve(.25)
    voice "voice/anton/4day/184.  A.ogg"
    Ant "А ты нет?"
    voice "voice/Alisa/4day/73 Ra.ogg"
    Alis "Раньше верила."

    show snow_night_1 onlayer master1:
        yzoom -1
        alpha 0
        linear 3 alpha 1
    show blizzard_d4_evening_face onlayer master1 zorder 5:
        yzoom -1
        alpha 0
        linear 3 alpha 1

    play test_three "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 0.7 volume 0.65 loop

    scene d4_procession_bg:
        align (.5, .5)
        .5
        linear 10 zoom 1.4
    with Dissolve(.5)
    "Стройные сосны-великаны встречали нас шорохом своих лап."

    "Снег снова валил снизу вверх, в бескрайнее чёрное небо."
    "Сугробы полыхали, точно расплавленное серебро."

    scene d4_night_forest_moon1:
        xalign 0.5
        yalign 1.0
        ease 10.0 yalign 0.0
    with Dissolve(.5)

    voice "voice/olya/4day/30 Ka.ogg"
    Oly "Как же красиво! А я думала, в лесу страшно."
    $ music_during_lines = 0.5
    voice "voice/Alisa/4day/01Nas.ogg"
    Alis "Нас родители пугали лесом, снегом и совой..."
    voice "voice/Alisa/4day/02Nu.ogg"
    Alis "...ну а мы с совой играли в снежной чаще под луной." id d4_beasts_5dab2bff
    $ music_during_lines = 1.0
    "Я старался не упускать из виду Олю, но это было довольно сложно: сестра то кидалась за кусты, подбирая всё новые конфеты, то, смеясь, выпрыгивала на тропинку."

    stop test_three fadeout 1.2
    play sound "sounds/sfx_whoosh_owl.ogg"

    scene d4_night_forest_moon1:
        align (.5, .0)

    show d4_night_forest_moon2:
        yalign .0
        alpha 0
        1.0
        alpha 1

    show d4_road_dark_shadow:
        anchor (0., 0.)
        pos (1., 1.)
        .5
        linear 1. pos (.0, .0) anchor (1., 1.)

    with Dissolve(.5)
    play test_six "voice/Owl/4day/13 Uh.ogg"    
    "Совушка пронеслась над нами, села на ветку и заухала, мотая головой."

    play sound "sounds/sfx_snow_dig.ogg"

    scene d4_night_forest_moon2:
        ypos 0
        ease 5 ypos -444
    show Olya Amaze b_evening_winter 01 good ahead 01:
        xanchor .5
        xpos .4
        yanchor 1.0
        ypos 2200
        zoom .5
        ease 5 ypos 1080
    show d4_wolf_candy 1:
        anchor (.5, 1.)
        xpos .75
        yanchor 1.0
        ypos 2200
        ease 5 ypos 1080

    play test_two "voice/Wolf/320 Gl.ogg"
    "Волчик вскопал мордой снег, вытянул горсть жвачек и проглотил, не снимая обёртки."

    show Olya Amaze b_evening_winter 01 good ahead 05 with Dissolve(.2)
    $ music_during_lines = 0.85
    voice "voice/olya/4day/32 U.ogg"
    Oly "У тебя будет несварение!"
    show Olya Amaze b_evening_winter 01 good ahead 01 with Dissolve(.2)


    scene d4_night_forest_moon2:
        yalign 1.
    show Olya Amaze b_evening_winter 01 good ahead 01:
        xanchor .5
        xpos .4
        yalign 1.
        zoom .5
    show d4_wolf_candy 1:
        xanchor .5
        xpos .75
        yalign 1.
    with Dissolve(.25)


    play test_two "voice/Wolf/321 Pl.ogg"
    show d4_wolf_candy anim
    "Волк испугался и выплюнул жвачный ком."
    play sound "sounds/sfx_footstep_snow_normal.ogg"

    show Fox Nice m_night 00 good ahead with Dissolve(.5):
        xanchor .5
        xpos .20
        yalign 1.
        xoffset -50
        yoffset 30

        parallel:
            linear .5 xoffset 0
        parallel:
            ease .25 yoffset 0
            ease .25 yoffset 30

    voice "voice/Alisa/4day/75 Vra.ogg"
    Alis "Враки-враки — злые собаки!"

    show Olya Amaze b_evening_winter 01 good aside 01 with Dissolve(.25)
    voice "voice/Alisa/4day/76 Net.ogg"
    Alis "Нет никаких несварений."
    voice "voice/Alisa/4day/76 Vs.ogg"
    Alis "Вся эта чушь случается только со взрослыми."


    show Fox Fullface m_night 00 good ahead with Dissolve(.25):
        .25
        "Fox Fullface m_night 00 good dark" with Dissolve(.5)

    pause .5

    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.25)
    play sound "sounds/sfx_branch_rustle_long.ogg"
    "Алиса встала как вкопанная и важно отодвинула полог переплетённых веток — так в театре открывают занавес."
    stop music fadeout 2.5
    label d4_palace_dev:

    play test_five "sounds/loop_castle_sparkling.ogg" fadein 2 volume 0.5 loop

    scene d4_palace_bg:
        align (.5, .5)
        subpixel True
        zoom .8
        easein 10 zoom (.8 + .85)*.5

    show d4_palace_mid:
        align (.5, .5)
        subpixel True
        zoom .8
        easein 10 zoom (.8 + 1.0)*.5

    show d4_palace_fg behind blizzard_d4_evening_face onlayer master1:
        subpixel True
        align (.5, .5)
        zoom .675
        linear 30 zoom (.675 + 12.35)*.5

    with Dissolve(.5)

    "За преградой была поляна, а на ней серебрился дворец изо льда."
    $ music_during_lines = 1.0
    voice "voice/olya/4day/33 O.ogg"
    Oly "О! Это всё взаправду?"

    hide d4_palace_fg onlayer master1
    scene d4_procession_talkback_bg_1:
        xalign .25
    show d4_procession_talkback_bg_2:
        xalign .75
    show d4_procession_talkback_bg_3:
        xalign .25
    show Bear Normal m 03 dark 30:
        align (.5, 1.)
        xoffset -600
        yoffset 150
        zoom 1.5
        subpixel True
    show Olya Amaze b_evening_winter 01 good ahead 01 dark 30:
        align (.5, 1.)
        zoom 0.75
    show Olya Amaze b_evening_winter 01 good aside 01 dark 30 with Dissolve(.2)
    voice "voice/Bear/4day/37 Ush.ogg"
    Bear "Ущипнуть тебя?"

    show Bear Normal m 04 dark 30
    show Olya Amaze b_evening_winter 01 good ahead 01 dark 30
    play sound "sounds/sfx_footsteps_snow_slow.ogg"
    show d4_anton_back_night:
        align (.5, .5)
        zoom 2.
        xoffset 450
    with Dissolve(.5)
    voice "voice/anton/4day/185. Ne.ogg"
    Ant "Не надо её щипать."

    scene d4_palace_bg:
        align (.5, .5)
        zoom (.8 + .85)*.5

    show d4_palace_mid:
        align (.5, .5)
        zoom (.8 + 1.0)*.5

    show d4_palace_fox:
        align (.5, .5)
        zoom (.8 + 1.0)*.5

    with Dissolve(.5)
    "Мы смотрели на сверкающее чудо: башенки и стены были выложены из снежного и ледяного мрамора."

    play sound "sounds/sfx_bells_distant.ogg" volume 0.2

    "Где-то ласково звенели колокольчики. Отчётливо пахло шоколадом и жжёным сахаром."
    voice "voice/Alisa/4day/78 Mi.ogg"
    Alis "Милости прошу к нашему шалашу!"
    play test_one "sounds/sfx_snow_footsteps_0.ogg"

    hide d4_palace_fox with Dissolve(.5)

    "Дважды приглашать не пришлось. Мы вошли в замок, вертясь и жмурясь от слепящих искр."

    window hide
    play sound "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 1.2 loop
    stop fon fadeout 5

    pause .2

    scene d4_palace_bg:
        align (.5, .5)
        zoom (.8 + .85)*.5
        linear 1. zoom .85

    show d4_palace_mid:
        align (.5, .5)
        zoom (.8 + 1.0)*.5
        linear 1. zoom 1.0

    pause .5

    $ renpy.scene("master1")
    scene d4_palace_room
    show d4_palace_moroz 1
    show layer master:
        align (.5, .5)
        easein .5 zoom 1.05
    with Dissolve(.5)


    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)

    stop sound fadeout 1

    window show
    play test_six "sounds/loop_bells_close.ogg" fadein 2 loop
    stop test_five fadeout 20

    "Дед Мороз сидел на сверкающем троне."

    scene d4_palace_ded_moroz:
        yalign 1.
        linear 6 yalign 0.
    with Dissolve(.5)

    show d4_palace_stars as topst:
        yalign 0.
    pause .1
    show d4_palace_stars as leftst:
        rotate 90
        xpos -800
    pause .15
    show d4_palace_stars as rightst:
        rotate 90
        xpos 700

    $ story_manager.MarkEvent(("day4", "scene7"))
    "Пушистые помпоны покачивались на раздвоенной шапке. Белоснежная борода скрывала спокойную улыбку."
    "Он был таким, как я его себе воображал давным-давно, когда ещё верил в мамины сказки: высоким, сильным и косматым, излучающим одновременно мороз и тепло."
    "И голос его, густой и глубокий, окутал меня, словно дым праздничного костра:"

    scene d4_palace_room
    show d4_palace_moroz 1
    with Dissolve(.5)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    voice "voice/kozel/4day/68.A.ogg"
    Frost "Антон и Ольга!"
    voice "voice/kozel/4day/OH.ogg"
    Frost "Ох и намучались же вы, ребятки, пока сюда добирались!"

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 04:
        xoffset 150
    show Olya Serious b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300
        yoffset 200
    with Dissolve(.5)

    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.2)
    voice "voice/olya/4day/34 Cho.ogg"
    Oly "Что ты, дедушка, мы быстро дошли."
    show Olya Happy b_evening_winter 01 good ahead 01 with Dissolve(.2)

    "Сестра говорила с хозяином замка иначе, чем с другими взрослыми: звонко, беззаботно. Словно он был её ровесник."
    stop test_six fadeout 5

    scene d4_palace_room
    show d4_palace_moroz 1
    with Dissolve(.5)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    play music "music/Christmas_(Tiny_Bunny)_Bells.ogg" fadein 2
    voice "voice/kozel/4day/69.Z.ogg"
    Frost "Знаю, всё знаю!"
    voice "voice/kozel/4day/70.Mne.ogg"
    Frost "Мне мои друзья докладывают..."
    voice "voice/kozel/4day/71.Kto.ogg"
    Frost "Кто был покладистым весь год, того подарок утром ждёт."
    voice "voice/kozel/4day/73.A.ogg"
    Frost "А кто ленился и грустил, пускай он дедушку простит."
    voice "voice/kozel/4day/75.Len.ogg"
    Frost "Лентяям и грустяям конфет не запасаем."

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 04:
        xoffset 150
    show Olya Happy b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300

        yoffset 200
    with Dissolve(.5)

    show Olya Happy b_evening_winter 01 good ahead 03 with Dissolve(.2)
    $ music_during_lines = 0.85
    voice "voice/olya/4day/35 A.ogg"
    Oly "А я не ленилась!"
    show Olya Happy b_evening_winter 01 good ahead 01 with Dissolve(.2)

    $ music_during_lines = 1.0
    voice "voice/kozel/4day/76.Eo.ogg"
    Frost "И о том знаю."

    scene d4_palace_ded_moroz:
        yalign 0.
    show d4_palace_stars as topst:
        yalign 0.
    with Dissolve(.5)
    pause .1
    show d4_palace_stars as leftst:
        rotate 90
        xpos -800
    pause .15
    show d4_palace_stars as rightst:
        rotate 90
        xpos 700

    "Он обвёл нас пристальным взором."
    "Маска Деда Мороза скрывала настоящее лицо."
    "Всё это время я молчал и смотрел, мой взгляд будто примёрз к старику."

    scene d4_palace_room
    show d4_palace_moroz 1
    with Dissolve(1.)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    "Я мог принять живущих в лесу детей и фантастические прыжки до луны, но Дед Мороз в ледяном замке ошарашил настолько, что я лишился дара речи."
    voice "voice/kozel/4day/77.Est.ogg"
    Frost "Есть у меня для вас кое-что особенное."

    play sound "sounds/sfx_bag_big_rustle.ogg"

    show d4_palace_moroz 2
    with Dissolve(.5)
    $ add_text_to_dictionary(48)
    "В его огромной руке появился мешок. В нос ударил запах какао, халвы и мандаринов."

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 04:
        xoffset 150
    show Olya Happy b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300

        yoffset 200
    with Dissolve(.5)

    show Ant High b_evening 00 norm ahead 06 with Dissolve(.2)
    $ music_during_lines = 0.6
    voice "voice/anton/4day/186. Spa.ogg"
    Ant "Спасибо, но мы уже ели конфеты."
    show Ant High b_evening 00 norm ahead 04 with Dissolve(.2)

    scene d4_palace_ded_moroz:
        xalign .5
        yalign 0.15
        zoom 2.0
    "Дед Мороз поглядел на меня внимательно."

    scene d4_palace_ded_moroz:
        subpixel True
        xalign .5
        yalign 0.15
        zoom 2.0
        linear 30. zoom 1.
    $ music_during_lines = 1.0
    voice "voice/kozel/4day/78.Raz.ogg"
    Frost "Ха-ха-ха! Разве то конфеты были? Так, одно название."
    voice "voice/kozel/4day/79.Vot.ogg"
    Frost "Вот у меня конфеты волшебные, прямиком из Небыляндии привезённые. Ха-ха-ха!"


    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 04:
        xoffset 150
    show Olya Happy b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300

        yoffset 200
    with Dissolve(.5)

    show Olya Happy b_evening_winter 01 good ahead 01:
        linear .1 yoffset 220
        "Olya Amaze b_evening_winter 01 good ahead 05"
        linear .1 yoffset 200

    play sound "sounds/sfx_coat_rustle_1.ogg"

    voice "voice/olya/4day/36 Ez.ogg"
    Oly "Из Небыляндии?!"
    show Olya Amaze b_evening_winter 01 good ahead 02 with Dissolve(.2)

    voice "voice/kozel/4day/80.Sra.ogg"
    Frost "Сразу бы вам их дал – заслужили."

    scene d4_palace_room
    show d4_palace_moroz 2
    with Dissolve(1.)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    voice "voice/kozel/4day/81.No.ogg"
    Frost "Но есть правила, ха-ха-ха."
    voice "voice/kozel/4day/82.Nad.ogg"
    Frost "Надобно вам три дедушкины загадки отгадать. Попробуете?"

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 04:
        xoffset 150
    show Olya Amaze b_evening_winter 01 good ahead 02:
        align (.5, 1.)
        xoffset -300

        yoffset 200
    with Dissolve(.5)
    "Я не успел разлепить пересохшие губы:"

    show Olya Amaze b_evening_winter 01 good ahead 03:
        linear .1 yoffset 220
        "Olya Amaze b_evening_winter 01 good ahead 05"
        linear .1 yoffset 200
    voice "voice/olya/4day/37 Da.ogg"
    Oly "Да!"
    show Olya Amaze b_evening_winter 01 good ahead 03 with Dissolve(.2)

    scene d4_palace_ded_moroz:
        xalign .5
        yalign 0.15
        zoom 2.0
    with Dissolve(.5)
    stop music fadeout 14
    voice "voice/kozel/4day/83.To.ogg"
    Frost "Тогда слушайте первую..."

    play music2 "music/Morning Tensions_02.ogg" fadein 3
    voice "voice/kozel/4day/84.Vn.ogg"
    Frost "В нём живут машины и хранятся шины."

    play test_seven "sounds/loop_rumble_background.ogg" fadein 4 volume 0.5 loop

    scene d4_palace_shadows
    with Dissolve(.5)
    "Я посмотрел по сторонам, на детей в масках."

    show d4_palace_shadows_0
    with Dissolve(.5)
    "Они замерли в углах, но их тени плясали на стенах."

    hide d4_palace_shadows_0
    show d4_palace_shadows_00
    with Dissolve(.5)

    play sound "sounds/sfx_stomach_growl_low.ogg"
    "Что-то тихо гудело, и я подумал, робея: это ворчат их желудки."

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 01:
        xoffset 150
    show Olya Amaze b_evening_winter 01 good ahead 02:
        align (.5, 1.)
        xoffset -300

        yoffset 200
    with Dissolve(.5)

    show Olya Amaze b_evening_winter 01 good ahead 03:
        linear .1 yoffset 220
        "Olya Amaze b_evening_winter 01 good ahead 05"
        linear .1 yoffset 200
    voice "voice/olya/4day/38 G.ogg"
    Oly "Гараж!"
    show Olya Amaze b_evening_winter 01 good ahead 02 with Dissolve(.2)
    voice "voice/kozel/4day/85.Ver.ogg"
    Frost "Верно, хе-хей!"

    scene d4_palace_room
    show d4_palace_moroz 2
    with Dissolve(1.)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    voice "voice/kozel/4day/85.Tep.ogg"
    Frost "Теперь вторая загадка. Подключайся, Антон."
    voice "voice/kozel/4day/85.Ves.ogg"
    Frost "Весь день ходит, как тень, посудой гремит, на всех шипит."


    $ renpy.start_predict("d4_palace_horovod_bg")
    $ renpy.start_predict("d4_palace_horovod_fg")

    scene d4_palace_children
    show Ant High b_evening 00 angry ahead 01:
        xoffset 150
    show Olya Amaze b_evening_winter 01 good ahead 02:
        align (.5, 1.)
        xoffset -300
        yoffset 200
    with Dissolve(.5)
    "Я вопросительно вскинул бровь:"
    show Ant High b_evening 00 angry ahead 07 with Dissolve(.2)
    voice "voice/anton/4day/187. Ma.ogg"
    Ant "Мама?"
    show Ant High b_evening 00 angry ahead 01 with Dissolve(.2)
    "Оля потянула руку:"
    show Olya Amaze b_evening_winter 01 good ahead 05 with Dissolve(.2):
        easein .1 yoffset 180
        easeout .1 yoffset 200
        repeat 5
    voice "voice/olya/4day/39M.ogg"
    Oly "Можно я?! Можно я?!"
    show Olya Amaze b_evening_winter 01 good ahead 02 with Dissolve(.2)
    show Olya Amaze b_evening_winter 01 good ahead 07 with Dissolve(.2):
        easein .1 yoffset 180
        easeout .1 yoffset 200
    voice "voice/olya/4day/40 Eto.ogg"
    Oly "Это кошка!"
    show Olya Amaze b_evening_winter 01 good ahead 02 with Dissolve(.2)

    scene d4_palace_room
    show d4_palace_moroz 2
    with Dissolve(.5)

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    stop music2 fadeout 6
    play music "music/Christmas_(Tiny_Bunny)_Bells.ogg" fadein 6
    voice "voice/kozel/4day/87.Verno.ogg"
    Frost "Верно, хо-хо! Осталась последняя загадка — и подарки ваши."
    voice "voice/kozel/4day/88.Tol.ogg"
    Frost "Только вот незадача, ребятушки..." id d4_palace_dev_4da636f1
    voice "voice/kozel/4day/89.Zapa.ogg"
    Frost "Запамятовал я, о чём же была эта загадка."
    voice "voice/kozel/4day/90.Moz.ogg"
    Frost "А может, наши друзья-зверята нам подскажут?"


    play test_seven "sounds/loop_circle_pit.ogg" fadein 1 loop

    scene d4_palace_children
    show d4_palace_horovod_bg
    show Ant High b_evening 00 norm ahead 01:
        xoffset 150
    show Olya Happy b_evening_winter 01 good ahead 02:
        align (.5, 1.)
        xoffset -300
        yoffset 200
    show d4_palace_horovod_fg
    with Dissolve(.5)


    "Ряженые дети с гоготом и топотом окружили нас со всех сторон, чтобы через мгновение закружиться в бешеном хороводе, смутно напоминающем пляску у моего окна в ту злополучную ночь."
    voice "voice/Alisa/4day/04Ded.ogg"
    Animals "Дед Мороз сидит на троне, пряча в бороду смешок."
    voice "voice/Alisa/4day/04Netomy.ogg"
    Animals "Не томи нас слишком долго, развяжи скорей..."


    show Olya Happy b_evening_winter 01 good ahead 07:
        linear .1 yoffset 220
        linear .2 yoffset 200
    voice "voice/olya/4day/41 M.ogg"
    Oly "...мешок!" id d4_palace_dev_b5c9c21d
    show Olya Happy b_evening_winter 01 good ahead 02 with Dissolve(.2)

    stop test_seven fadeout 2

    scene d4_palace_room
    show d4_palace_moroz 2:
        yoffset 10
        1.
        block:
            ease 0.1 yoffset 5
            ease 0.1 yoffset 10
            ease 0.1 yoffset 0
            ease 0.1 yoffset 10
            repeat 5
    with Dissolve(.5)

    $ renpy.stop_predict("d4_palace_horovod_bg")
    $ renpy.stop_predict("d4_palace_horovod_fg")

    show d4_palace_stars as topst zorder 1:
        yalign 0.
    with Dissolve(.10)
    show d4_palace_stars as leftst zorder 1:
        rotate 90
        xpos -800
    with Dissolve(.15)
    show d4_palace_stars as rightst zorder 1:
        rotate 90
        xpos 700
    with Dissolve(.20)
    play test_six "voice/kozel/4day/92.La.ogg"
    "Дед Мороз засмеялся, довольный."
    stop test_six fadeout 0.3
    voice "voice/kozel/4day/91.Ub.ogg"
    Frost "Убедили старика! Получайте!"

    scene d4_palace_candy_bg with Dissolve(.5)
    "И он высыпал из багрового мешка гору угощений, каких я не видел даже в рекламе."

    show d4_palace_candy 1 with Dissolve(.1):
        block:
            linear .03 yoffset -5
            linear .03 yoffset 5
            repeat 2
            linear .03 yoffset 0

    play test_one "sounds/sfx_candies_pour_1.ogg"

    "Жвачки самых разных форм и расцветок, вкусно пахнущие, с торчащими вкладышами."


    show d4_palace_candy 2 with Dissolve(.1):
        block:
            linear .03 yoffset -5
            linear .03 yoffset 5
            repeat 2
            linear .03 yoffset 0
    show d4_palace_glitter:
        alpha 0
        linear 1. alpha 1

    play sound "sounds/sfx_candies_pour_2.ogg"

    "Леденцы размером с кулак и мандарины размером с Олину голову."
    "А ещё «Сникерсы», «Марсы», «Баунти» и «Киндер-сюрпризы», которые мы так давно не пробовали."
    voice "voice/olya/4day/42 Oi.ogg"
    Oly "Ой, спасибо!"

    show layer master:
        blur 0
        easein .5 blur 4
        ease .5 blur 2
        ease .5 blur 6
        .25
        blur 16
        .75
        blur 0
    show Veko_01:
        xpos 0
        ypos -1510
        alpha 0.0
        1.5
        linear 0.25 xpos 0 ypos -500 alpha 1.0
        linear 0.25 xpos 0 ypos -1500 alpha .0
        .25
        linear 0.25 xpos 0 ypos -500 alpha 1.0
        linear 0.25 xpos 0 ypos -1500 alpha .0
    show Veko_02:
        xpos 0
        ypos 1010
        alpha 0.0
        1.5
        linear 0.25 xpos 0 ypos 0 alpha 1.0
        linear 0.25 xpos 0 ypos 1000 alpha .0
        .25
        linear 0.25 xpos 0 ypos 0 alpha 1.0
        linear 0.25 xpos 0 ypos 1000 alpha .0

    "Я вытер рукавом выступившие слёзы радости, когда мой внутренний голос убедил меня отбросить все сомнения."
    "Именно этого я хотел для себя и сестры."
    "Настоящая Небыляндия... Без унижений и запретов."
    "Наконец-то мы будем счастливы."

    play sound ["<silence 0.52>","sounds/sfx_DeadMorose_get_up.ogg"]
    play test_three ["<silence 0.52>","sounds/sfx_coat_rustle.ogg"]

    scene d4_palace_room
    show d4_palace_moroz 3
    with Dissolve(.5)
    pause .5
    show d4_palace_moroz 4
    with Dissolve(.5)

    "Дед Мороз распрямился, покидая трон, и воздел руки над угощениями."
    play test_two "voice/Wolf/306 Hlup.ogg"

    window hide

    scene d4_palace_beasts_bg:
        subpixel True
        align (.5, .5)
        easein 60 zoom .67
    show d4_palace_beasts
    with Dissolve(.5)
    pause 1.5
    window show
    "Звери по бокам тоже подняли лапы."
    "Их глаза блестели ярче драгоценных камней. Пасть волка была мокрой от слюны."

    scene d4_palace_room:
        align (.5, .5)
        zoom 1.2
    show d4_palace_moroz 4:
        align (.5, .5)
        zoom 1.2
    with Dissolve(.5)
    voice "voice/kozel/4day/92.Da.ogg"
    Frost "Да будет пир на весь мир!"

    label d4_palace_dev.choice:

    stop test_six fadeout 5
    play test_two "voice/Wolf/324 Zv.ogg"
    play test_three "voice/Owl/4day/12 Nyam.ogg"
    play test_four "voice/Bear/4day/Nyam.ogg"
    play test_seven "sounds/loop_candies_rustle_eat.ogg" fadein 1  loop 

    scene d4_palace_choice_bg
    show d4_palace_choice_beasts 1
    show d4_anton_treat_choice
    with Dissolve(.5)
    "Звери, толкаясь и рыча, бросились поедать конфеты, одну за другой. Рты у них были вымазаны чем-то тёмным." id d4_palace_dev_469db1f3


    show d4_palace_choice_olya 1
    with Dissolve(.5)
    "Сестра схватила первую попавшуюся конфету и содрала фантик." id d4_palace_dev_fc8c3b8f

    if not Flags.Has("mask"):
        "При виде этого я почувствовал, что внутри меня будто качнулся маятник."

    stop music fadeout 10
    stop test_seven fadeout 15
    window hide

    $ story_manager.MarkEvent(("day4", "treat1"))

    hide d4_palace_choice_olya
    call screen day4_treat_take_or_refuse()




label d4_beasts_choice_refuse:
    $ story_manager.MarkEvent(("day4", "treat1", "refuse"))
    $ Flags.Raise("refuse")

    scene d4_palace_choice_bg
    show d4_palace_choice_beasts 1
    show d4_palace_moroz 3:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -600
        yoffset 200
        zoom 1.6
    with Dissolve(.5)
    window show
    play test_one "voice/olya/4day/43 Ai.ogg"
    "Я вцепился в Олино запястье так, что она пискнула то ли от боли, то ли от неожиданности."
    play test_two "voice/Wolf/Hah.ogg"

    stop test_seven fadeout 1
    play sound "sounds/sfx_rustle_creepy_1.ogg"

    show d4_palace_choice_beasts 2
    voice "voice/anton/4day/188. Ne.ogg"
    Ant "Не ешь."

    play sound "sounds/sfx_whispers_distant.ogg" volume 0.25

    "По залу прошёлся настороженный шёпот. Шевельнулись ушки масок."

    play test_five "sounds/sfx_footstep_massive_1.ogg"
    play sound "sounds/sfx_rustle_creepy_2.ogg"    
    pause .2

    show d4_palace_choice_beasts 3
    hide d4_palace_moroz 3
    show d4_palace_choice_moroz zorder 1:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 200
        yoffset 200
        zoom .95
    with Dissolve(.5)

    "Тени перебежали с места на место."

    play test_five "sounds/loop_footsteps_three.ogg" fadein 0.2

    hide d4_palace_choice_beasts
    show d4_palace_choice_candy
    with Dissolve(.5)

    show Owl Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -650
        yoffset 200
        zoom .95
    with Dissolve(.5)

    pause .4
    stop test_five fadeout 0.8

    voice "voice/Owl/4day/13 Chto.ogg"
    Owl "Что такое? Что случилось?"

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.2

    show Fox Nice m_night 00 good ahead zorder 2:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 625
        yoffset 200
        zoom 1.2
    with Dissolve(.5)

    stop sound fadeout 0.6
    voice "voice/Alisa/4day/80 Niche.ogg"
    Alis "Ничего страшного!"
    voice "voice/Alisa/4day/81 Prosto.ogg"
    Alis "Просто Тоша верит в несуществующий диабет."
    play music2 "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 1.5

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.2
    pause .4

    show Wolf Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 850
        yoffset 100
        zoom 0.95
    with Dissolve(.5)
    stop sound fadeout 0.6

    voice "voice/Wolf/325 Ro.ogg"
    Wolf "Р-р-росказни р-р-родителей!"

    play sound "sounds/loop_footsteps_snow_normal.ogg" fadein 0.1
    pause .25

    show Bear Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -400
        yoffset 100
        zoom .95
    with Dissolve(.5)

    stop sound fadeout 0.6

    voice "voice/Bear/4day/41Raz.ogg"
    Bear "Разбудите меня, когда он перестанет валять дурака."

    play sound "sounds/sfx_footstep_massive_2.ogg"

    show d4_palace_choice_moroz zorder 3:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 150
        yoffset 400
        zoom 1.25
    with Dissolve(.5)
    "Дед Мороз склонился надо мной."
    "От него пахло карамелью и совсем чуть-чуть сыростью."
    $ music_during_lines = 0.65
    voice "voice/kozel/4day/93.Dav.ogg"
    Frost "Давайте не будем портить праздник, друзья!"
    voice "voice/kozel/4day/94.Se.ogg"
    Frost "Сегодня каждый должен веселиться! Ешьте и пляшите!"


    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 01:
        xoffset 150
    show Olya Serious b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300
        yoffset 200
        block:
            .5
            linear .15 xoffset -320
            linear .15 xoffset -300
            repeat 2
    with Dissolve(.5)

    pause .2
    play sound "sounds/sfx_Olya_rustle.ogg"

    play test_six "voice/olya/4day/46 Mn.ogg"
    "Оля попыталась отнять руку, но я не разжал хватки."

    scene d4_palace_candy_bg
    show d4_palace_candy 2

    show old_movie_intense:
        alpha 0
        1.
        linear 1 alpha 1
    show layer master:
        matrixcolor BrightnessMatrix(0.0)
        easein 4 matrixcolor BrightnessMatrix(-0.1)
    with Dissolve(.5)
    "Я смотрел на сладости, на высокого старика, и принюхивался к просачивающемуся запашку."
    "Гниль, маскированная приторным ароматом. Вонь дикого зверя."
    "Казалось, какое-то сильное наваждение перестало действовать. Вернулся холод, усталость и страх."

    $ renpy.start_predict("d4_treat_choice2_refuse_full")

    scene d4_palace_children
    show Ant High b_evening 00 norm ahead 02 zorder 2:
        xoffset 150
    show Olya Serious b_evening_winter 01 good ahead 01 zorder 2:
        align (.5, 1.)
        xoffset -300
        yoffset 200
    with Dissolve(.5)

    show Ant High b_evening 00 norm ahead 03 with Dissolve(.2)
    voice "voice/anton/4day/189. Spa.ogg"
    Ant "Спасибо, но мы сыты."
    show Ant High b_evening 00 norm ahead 02 with Dissolve(.2)

    play test_five "sounds/sfx_footstep_snow_normal.ogg"

    window hide
    hide Ant
    show d4_procession_anton zorder 1:
        yoffset 100
        zoom 1.5
        align (.5, 1.)
    with Dissolve(.5)

    pause 1.0

    play test_six "sounds/sfx_footstep_snow_light.ogg"

    hide Olya
    show d4_procession_olya_bright zorder 1:
        yoffset 100
        zoom 1.5
        align (.5, 1.)

    with Dissolve(.5)

    window show
    voice "voice/anton/4day/190Emi.ogg"
    Ant "И... мы пойдём, наверное. Мама с папой переживают уже."

    play test_four "sounds/loop_footsteps_snow_fast.ogg" fadein 0.2

    show Fox Fullface m_night 00 good ahead:
        xoffset 100
        easein .5 xoffset 0
    with Dissolve(.5)

    pause .8
    stop test_four fadeout 0.8

    "Я потянул сестру к выходу, но Алиса встала наперерез."

    play sound "sounds/sfx_rustle_clothes_light_1.ogg"
    play test_seven "sounds/sfx_rustle_clothes_light_2.ogg"

    scene d4_treat_choice2_bg nocolor:
        yalign 1.
    show d4_treat_choice2_alice_body nocolor:
        yalign 1.
    show d4_treat_choice2_alice_hands nocolor:
        animation
        subpixel True
        yalign 1.
        xalign .5
        parallel:
            handshake(*hs_prm)
        parallel:
            ypos 1080 - 100
            easein .5 ypos 1080
    with Dissolve(.5)
    "В руках она держала фарфоровую тарелку."
    stop music2 fadeout 2.5
    show d4_treat_choice2_refuse_full
    play test_six "music/maggots_loop.ogg" loop
    play test_seven "music/Tension Suspense Risers_04(diminuendo).ogg" 

    window hide
    pause 1.
    window show
    "Мне померещилось, что блюдо наполнено опарышами, но, как только взгляд метнулся к подношению, вместо тошнотворно-шевелящейся массы там оказались мармеладные змейки."
    stop test_six fadeout 3
    scene d4_treat_choice2_bg nocolor:
        yalign 1.
        linear .25 yalign .0
    show d4_treat_choice2_alice_body nocolor:
        yalign 1.
        linear .25 yalign .0
    show d4_treat_choice2_alice_hands nocolor:
        animation
        subpixel True
        yalign 1.
        xalign .5
        parallel:
            handshake(*hs_prm)
        parallel:
            linear .25 yalign .0

    show d4_palace_children:
        align (.5, 1.)
        zoom 1.2
        blur 8
        alpha 0
        .25
        parallel:
            linear .25 alpha 1
        parallel:
            linear .5 yalign .5
    show Fox Fullface b_night 00 good ahead:
        alpha 0
        zoom 1.1
        xalign .5
        .25
        parallel:
            linear .25 alpha 1
        parallel:
            yalign 1.
            linear .5 yalign .5

    $ renpy.stop_predict("d4_treat_choice2_refuse_full")

    $ music_during_lines = 1.0
    voice "voice/Alisa/4day/82 Pro.ogg"
    Alis "Прошу, Антон. Мы же друзья, правда?"
    play music "music/24_Fox.ogg" fadein 1.5
    voice "voice/Alisa/4day/83 Me.ogg"
    Alis "Мы даже больше чем друзья."
    voice "voice/Alisa/4day/84 Vs.ogg"
    Alis "Вспомни, что я обещала?"
    voice "voice/Alisa/4day/85 Ni.ogg"
    Alis "Никто не причинит тебе зла, пока я рядом." id d4_beasts_choice_refuse_1168c6fe
    voice "voice/Alisa/4day/86 Nite.ogg"
    Alis "Ни тебе, ни Оле."
    voice "voice/Alisa/4day/87 Tak.ogg"
    Alis "Так что съешь, пожалуйста, всего одну."
    voice "voice/Alisa/4day/88  S.ogg"
    Alis "Съешь, а?"

    play sound ["<silence 0.35>","sounds/sfx_Olya_rustle.ogg"]

    scene d4_palace_room
    show Ant High b_evening 00 norm ahead 02:
        xoffset 150
    show Olya Weeps b_evening_winter 01 good aside 01:
        align (.5, 1.)
        xoffset -300
        yoffset 200
        block:
            .5
            linear .15 xoffset -320
            linear .15 xoffset -300
            repeat 2
    with Dissolve(.5)
    show Olya Weeps b_evening_winter 01 good aside 05 with Dissolve(.2)
    voice "voice/olya/4day/44 An.ogg"
    Oly "Антон, пусти! Ну пусти!"
    show Olya Weeps b_evening_winter 01 good aside 01 with Dissolve(.2)
    show Olya Weeps b_evening_winter 01 good aside 05 with Dissolve(.2)
    voice "voice/olya/4day/45 T.ogg"
    stop music fadeout 5.5
    Oly "Теперь и ты всё мне запрещаешь, прям как мама!"
    show Olya Weeps b_evening_winter 01 good aside 01 with Dissolve(.2)
    "Оля билась в истерике, силясь разжать мою хватку."

    scene d4_palace_choice_bg2:
        xalign 1.
    show d4_palace_choice_head
    show d4_palace_choice_head_ 1:
        alpha 0
        2.
        alpha 1
        .1
        "d4_palace_choice_head_ 2"
        .1
        "d4_palace_choice_head_ 1"
        .1
        alpha 0
        3.
        repeat
    with Dissolve(.5)
    play music "music/Tanets_Zverey-Symphonic_Orchestra_choir.ogg" volume 0.45
    voice "voice/anton/4day/190Eto.ogg"
    Ant "Это неправильно..."
    $ music_during_lines = 0.75
    voice "voice/anton/4day/191 V.ogg"
    Ant "Всё здесь какое-то неправильное."

    scene d4_palace_children:
        align (.5, .25)
        zoom 1.2
    show Fox Fullface m_night 00 good ahead
    show d4_procession_olya_bright:
        yoffset 100
        zoom 1.5
        xzoom -1
        align (.5, 1.)
    show d4_procession_anton:
        xoffset -800
        yoffset 100
        zoom 1.5
        align (.5, 1.)
    with Dissolve(.5)
    voice "voice/Alisa/4day/89 Vot.ogg"
    Alis "Вот как?"
    voice "voice/Alisa/4day/90 At.ogg"
    Alis "А ты не задумывался, что из неправильного тут только твоё мировоззрение?"
    voice "voice/Alisa/4day/91 Kak.ogg"
    Alis "Как ты думаешь, что делают те таблетки, которые ты глотаешь круглые сутки, м?"
    voice "voice/Alisa/4day/92 Oni.ogg"
    Alis "Они искажают реальность, путают мысли, уводят тебя со снежной тропинки."


    scene d4_palace_children:
        subpixel True
        align (.5, .25)
        zoom 1.2
        easeout 2. zoom 1.00

    show Fox Fullface m_night 00 good ahead

    show d4_procession_olya_bright:
        subpixel True
        yoffset 100
        zoom 1.5
        xzoom -1
        align (.5, 1.)
        easeout 2. xoffset 50 yoffset 150 alpha 0 zoom 1.7
    show d4_procession_anton:
        subpixel True
        xoffset -800
        yoffset 100
        zoom 1.5
        align (.5, 1.)
        easeout 2. xoffset -900 yoffset 150 alpha 0 zoom 1.7

    show layer master:
        subpixel True
        align (.5, .25)
        easeout 2. zoom 1.3

    pause 2.


    scene d4_palace_children:
        align (.5, .25)
        zoom 1.4
    show Fox Fullface b_night 00 good ahead:
        align (.5, 1.)
        xoffset -50

    "Я с подозрением посмотрел на Алису, пытаясь найти, чем ей возразить..."
    "...но не смог." id d4_beasts_choice_refuse_69587d6b
    if Flags.Has("glove") and not Flags.Has("finger"):
        window hide
        play test_one "sounds/Varezka.ogg"
        show bg_white with Dissolve(0.1)
        show memory_scrimer2
        $ renpy.pause(1.2, hard=True)
        hide memory_scrimer2
        hide bg_white with Dissolve(0.1)
        window show
        "Вспомнилась окровавленная варежка Вовы."
        "Это было лишь иллюзией."


    if Flags.Has("finger") and not Flags.Has("glove"):
        window hide
        play test_one "sounds/Varezka.ogg"
        show bg_white zorder 1 with Dissolve(0.1)
        show bunny_nightmare_bg
        show ant_hand 2:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                ease .25 matrixcolor BrightnessMatrix(-0.05)
                ease .25 matrixcolor BrightnessMatrix(0.00)
                repeat
        show ant_hand 2 as gh1:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                alpha .0
                xoffset -200
                easein .6 xoffset 0 alpha 1
                easeout .6 xoffset 200 alpha 0
        show ant_hand 2 as gh2:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                alpha .0
                xoffset 200
                easein .6 xoffset 0 alpha 1
                easeout .6 xoffset -200 alpha 0
        show old_movie_intense:
            matrixcolor BrightnessMatrix(1.0)

        play test_three "sounds/hit-chord-2.ogg"
        hide bg_white with Dissolve(0.1)
        $ renpy.pause(1.2, hard=True)
        show bg_white with Dissolve(0.1)
        hide bunny_nightmare_bg
        hide ant_hand
        hide gh1
        hide gh2
        hide old_movie_intense
        hide bg_white with Dissolve(0.1)
        window show

        "Вспомнился обрубленный палец Семёна в пакете."
        "Это было лишь иллюзией."

    if Flags.Has("finger") and Flags.Has("glove"):
        window hide
        play test_one "sounds/Varezka.ogg"
        show bg_white zorder 1 with Dissolve(0.1)
        show memory_scrimer2 zorder 1
        $ renpy.pause(1.2, hard=True)
        hide memory_scrimer2

        play test_three "sounds/hit-chord-2.ogg"
        show bunny_nightmare_bg
        show ant_hand 2:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                ease .25 matrixcolor BrightnessMatrix(-0.05)
                ease .25 matrixcolor BrightnessMatrix(0.00)
                repeat
        show ant_hand 2 as gh1:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                alpha .0
                xoffset -200
                easein .6 xoffset 0 alpha 1
                easeout .6 xoffset 200 alpha 0
        show ant_hand 2 as gh2:
            parallel:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
            parallel:
                alpha .0
                xoffset 200
                easein .6 xoffset 0 alpha 1
                easeout .6 xoffset -200 alpha 0
        show old_movie_intense:
            matrixcolor BrightnessMatrix(1.0)

        hide bg_white with Dissolve(0.1)
        $ renpy.pause(.8, hard=True)
        show bg_white with Dissolve(0.1)
        hide bunny_nightmare_bg
        hide ant_hand
        hide gh1
        hide gh2
        hide old_movie_intense
        hide bg_white with Dissolve(0.1)
        window show
        "Вспомнились окровавленная варежка Вовы, обрубленный палец Семёна в пакете."
        "Всё это было лишь иллюзией."

    scene d4_palace_choice_bg2:
        xalign 1.
    show d4_palace_choice_head
    show d4_palace_choice_head_ 1:
        alpha 0
        2.
        alpha 1
        .1
        "d4_palace_choice_head_ 2"
        .1
        "d4_palace_choice_head_ 1"
        .1
        alpha 0
        3.
        repeat

    voice "voice/anton/4day/191. Kto.ogg"
    Ant "К-кто вы?"

    scene d4_palace_choice_bg
    show d4_palace_choice_candy
    show Owl Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -650
        yoffset 200
        zoom .95
    show Wolf Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 850
        yoffset 100
        zoom 0.95
    show Bear Normal m 00:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset -400
        yoffset 100
        zoom .95
    show d4_palace_choice_moroz zorder 3:
        align (.5, 1.)
        transform_anchor True
        rotate -12
        xoffset 150
        yoffset 400
        zoom 1.25
    with Dissolve(.5)
    voice "voice/kozel/4day/96.Ana.ogg"
    Frost "А на кого мы похожи?"
    "На кошмары, терзающие мой больной рассудок."

    scene d4_treat_ceiling_bg:
        subpixel True
        align (.5, .5)
        zoom .5
        easein 60 zoom 1.00
    show d4_treat_ceiling_ded

    show layer master:
        subpixel True
        align (.5, .5)
        easein 60 zoom 1.75

    with Dissolve(.5)
    voice "voice/kozel/4day/97.Sname.ogg"
    Frost "С нами вас никто больше не накажет, не запрёт в комнате, не бросит в одиночестве."
    voice "voice/kozel/4day/98.Ot.ogg"
    Frost "Отныне никто не заставит вас делать то, что вам не хочется."

    scene d4_palace_choice_bg2:
        xalign 1.
    show d4_palace_choice_head
    show d4_palace_choice_head_ 1:
        alpha 0
        2.
        alpha 1
        .1
        "d4_palace_choice_head_ 2"
        .1
        "d4_palace_choice_head_ 1"
        .1
        alpha 0
        3.
        repeat
    with Dissolve(.5)

    voice "voice/anton/4day/otkuda.ogg"
    Ant "Откуда вы знаете, чего нам не хочется?"

    play sound "sounds/sfx_scratch_Wolf.ogg"

    "Старик потрепал за ушком громко чавкающего Волчика."

    scene d4_palace_room:
        subpixel True
        align (.5, .5)
        zoom 1.5
        easein 60 zoom 1.0

    show d4_treat_ded_close
    with Dissolve(.5)
    $ music_during_lines = 0.75
    voice "voice/kozel/4day/99.Ya.ogg"
    Frost "Я знаю."
    voice "voice/kozel/4day/100.Mne.ogg"
    Frost "Мне шепчут ветра и тени, холодные звёзды и безграничные небеса."
    voice "voice/kozel/4day/102.On.ogg"
    Frost "Они говорят, что дети не хотят взрослеть."
    voice "voice/kozel/4day/103.Pre.ogg"
    Frost "Превращаться в тех, кто живёт запретами, угрозами, наказаниями."
    "Каждое следующее слово он говорил всё громче."
    $ music_during_lines = 0.8
    voice "voice/kozel/4day/104.Oz.ogg"
    Frost "Ожиданием старости и смерти."
    voice "voice/kozel/4day/105.De.ogg"
    $ music_during_lines = 0.85
    Frost "Дети живут мечтами."
    voice "voice/kozel/4day/106.O.ogg"
    Frost "О, я отлично знаю детские мечты о счастливой и беззаботной жизни."
    $ music_during_lines = 0.95
    voice "voice/kozel/4day/107.Toi.ogg"
    Frost "Той, в которой есть чудеса и дикая свобода."
    "Голос его был громом, от которого волосы на голове вставали дыбом."
    voice "voice/kozel/4day/108.Sto.ogg"
    $ music_during_lines = 1.0
    Frost "Всё это будет вашим — стоит только захотеть."
    voice "voice/kozel/4day/110.S.ogg"
    Frost "Стоит только попросить."
    "И совсем шёпотом:"
    $ music_during_lines = 0.9
    voice "voice/kozel/4day/111.St.ogg"
    Frost "Стоит только согласиться..."

    scene d4_palace_children:
        subpixel True
        align (.5, .5)
    show Ant High b_evening 00 norm ahead 02:
        subpixel True
        xoffset 150 +600
    show Olya Amaze b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset 0
        yoffset 200
    with Dissolve(.5)

    scene d4_palace_children:
        subpixel True
        align (.5, .5)
        .25
        easein 5. zoom 1.15
    show Ant High b_evening 00 norm ahead 02:
        subpixel True
        xoffset 150 +600
        .25
        easein 5. xoffset 150 +600 + 300
    show Olya Amaze b_evening_winter 01 good ahead 02:
        align (.5, 1.)
        xoffset 0
        yoffset 200
        "Olya Amaze b_evening_winter 01 good ahead 05" with Dissolve(.25)
        .75
        "Olya Amaze b_evening_winter 02 good ahead 08" with Dissolve(1.5)

    with Dissolve(.25)

    show layer master:
        subpixel True
        align (.5, .85)
        easein 5. zoom 1.5

    stop music fadeout 3.5
    voice "voice/olya/4day/47 So.ogg"
    Oly "Согласиться..."
    $ music_during_lines = 1.0
    "Словно эхо, повторила зачарованная Оля."

    scene d4_palace_room:
        subpixel True
        align (.5, .5)
        zoom 1.

        easein 60 zoom 1.5

    show d4_treat_ded_close
    with Dissolve(.5)

    voice "voice/kozel/4day/112.Da.ogg"
    Frost "Да, моя дорогая."
    voice "voice/kozel/4day/113.Vk.ogg"
    Frost "Вкусить это."

    scene d4_palace_children:
        align (.0, .5)
        zoom 1.2
        blur 8
        easein 1. xalign .5
    show Fox Normal b_night 00 good ahead:
        xalign .5
        yalign 1.
        xoffset 300
        easein 1. xoffset 0
    with Dissolve(.25)

    show Fox Fullface b_night 00 good ahead with Dissolve(.25)

    "Старец ткнул перстом в сторону лисицы."
    voice "voice/Alisa/4day/93 ya.ogg"
    Alis "Я прошу тебя ради всех нас, ради меня, ради сестры..."

    label d4_beasts_choice_refuse.choice:
    $ hs_prm = (5, 2)

    scene d4_treat_choice2_bg nocolor:
        yalign 1.
    show d4_treat_choice2_alice_body nocolor:
        yalign 1.
    show d4_treat_choice2_alice_hands nocolor:
        animation
        subpixel True
        yalign 1.
        xalign .5
        handshake(*hs_prm)
    with Dissolve(.5)
    voice "voice/Alisa/4day/94 Zai.ogg"
    Alis "Зайчик, отведай хотя бы кусочек." id d4_beasts_choice_refuse_549bd4a5
    voice "voice/Alisa/4day/95 E.ogg"
    Alis "И тогда ты всё поймешь." id d4_beasts_choice_refuse_57e9bc3a
    window hide


label d4_beasts_choice2:
    $ story_manager.MarkEvent(("day4", "treat2"))
    label d4_beasts_choice2.start:
    call screen day4_treat_take_or_refuse_2

    label d4_beasts_choice2.take_hover:
    show d4_treat_choice2_bg nocolor:
        yalign 1.
        "d4_treat_choice2_bg color" with Dissolve(1.)
    show d4_treat_choice2_alice_body nocolor:
        yalign 1.
        "d4_treat_choice2_alice_body color" with Dissolve(1.)
    show d4_treat_choice2_alice_hands nocolor:
        animation
        subpixel True
        yalign 1.
        xalign .5
        parallel:
            handshake(*hs_prm)
        parallel:
            "d4_treat_choice2_alice_hands color" with Dissolve(1.)

    call screen day4_treat_take_or_refuse_2

    label d4_beasts_choice2.take_unhover:
    show d4_treat_choice2_bg color:
        yalign 1.
        "d4_treat_choice2_bg nocolor" with Dissolve(.1)
    show d4_treat_choice2_alice_body color:
        yalign 1.
        "d4_treat_choice2_alice_body nocolor" with Dissolve(.1)
    show d4_treat_choice2_alice_hands color:
        animation
        subpixel True
        yalign 1.
        xalign .5
        parallel:
            handshake(*hs_prm)
        parallel:
            "d4_treat_choice2_alice_hands nocolor" with Dissolve(.1)

    call screen day4_treat_take_or_refuse_2


label d4_beasts_choice2_refuse:
    $ story_manager.MarkEvent(("day4", "treat2", "refuse"))
    scene d4_palace_beasts_bg:
        subpixel True
        align (.5, .5)
        easein 60 zoom .67
    show d4_palace_beasts
    show d4_palace_beasts_faces_dark
    with Dissolve(.5)
    pause 1.0
    window show
    play test_six "sounds/hum-1.1.ogg" fadein 3 loop
    play test_two "voice/Wolf/306 Hlup.ogg"
    "У меня возникло чувство, что ледяной ветер дует из дыр её глаз, из тёмных глазных провалов других зверей и долговязого старика."
    play test_three "<from 0 to 1>voice/Owl/4day/13 Uh2.ogg"
    "Морда совы нервно подёргивалась."
    "Пасть волка истекала слюной."
    play test_two "voice/Bear/4day/00.ogg"
    "Медведь переминался с лапы на лапу, враз избавившись от сонливости."

    $ renpy.music.set_volume(0.15, 0.5, channel="test_four")
    play test_four "sounds/loop_breathing_mask_heavy.ogg" fadein 1 loop

    scene d4_treat_ceiling_bg:
        subpixel True
        align (.5, .5)
        zoom .5
        easein 600 zoom 1.00
    show d4_treat_ceiling_ded

    show layer master:
        subpixel True
        align (.5, .5)
        easein 600 zoom 1.75

    with Dissolve(.5)
    "А сзади нависал тот, кто всё это время притворялся Дедом Морозом."

    stop test_four fadeout 4.5 
    $ renpy.music.set_volume(1.0, 9.5, channel="test_four")

    scene d4_palace_room
    show Ant High b_evening 00 angry ahead 02:
        xoffset 150
    show Olya Serious b_evening_winter 01 good ahead 01:
        align (.5, 1.)
        xoffset -300
        yoffset 200
    with Dissolve(.5)


    $ achievement_grant("ach_Djakel")

    show Ant High b_evening 00 angry ahead 03 with Dissolve(.2)
    voice "voice/anton/4day/192. Yaska.ogg"
    Ant "Я сказал: мы уходим."
    show Ant High b_evening 00 angry ahead 02 with Dissolve(.2)

    play sound "sounds/sfx_hand_creak.ogg"

    "Я покрепче стиснул руку сестры. Конфета выпала из её пальцев, шмякнувшись о пол."

    show Olya Weeps b_evening_winter 01 good ahead 01 with Dissolve(.2):
        .25
        "Olya Weeps b_evening_winter 01 good aside 01" with Dissolve(.2)
        .45
        "Olya Weeps b_evening_winter 01 good ahead 01" with Dissolve(.2)
        3
        repeat
    "Теперь и Оля испуганно озиралась."

    scene d4_palace_children:
        align (.5, .5)
        zoom 1.2
        blur 8
    show Fox Fullface b_night 00 good ahead
    with Dissolve(.25)

    voice "voice/Alisa/4day/YaSkazal.ogg"
    Alis "Я сказал: мы уходим!"
    "Алиса передразнивала меня, и вопреки всему я испытал острую обиду."

    show Fox Normal b_night 00 good ahead with Dissolve(.25)
    voice "voice/Alisa/4day/96 oh.ogg"
    Alis "Ох, ну какой же ты всё-таки..."
    show Fox Normal b_night 00 good ahead:
        "d4_lisa 5" with Dissolve(0.5)
        .75
        "d4_lisa 4" with Dissolve(0.5)
    voice "voice/Alisa/4day/96 Du.ogg"
    Alis "...дурачок." id d4_beasts_choice2_refuse_11fd4757
    stop test_six fadeout 2
    play music "music/Master of the forest.ogg" fadein 0.5
    $ music_during_lines = 0.65

    scene d4_palace_choice_bg2:
        subpixel True
        xalign .75
        linear 30 xalign 0.25
    show d4_flute_olya:
        xalign .5
        xoffset 150
    show d4_flute_anton:
        subpixel True
        xalign 1.
        xoffset 600
        linear 30 xalign .5 xoffset -200
    with Dissolve(.5)
    "Я услышал мелодию флейты, но теперь она напоминала свист хлыста или агонию рыбы, выброшенной на лёд."
    play test_two "voice/anton/2day/fear3.ogg"
    "Музыка трепыхалась и била по ушам."

    play sound "sounds/sfx_transform_beasts.ogg"

    play test_six "voice/olya/4day/48 AAA.ogg"
    "А затем ледяной терем заполнил детский плач, перерастающий в звериный лай, хруст костей и звук лопающихся шкур."

    scene d4_treat_choice2_bg nocolor:
        align (.5, 1.)
        zoom 1.05
    show d4_palace_worms:
        block:
            linear .03 yoffset -5
            linear .03 yoffset 5
            repeat 2
            linear .03 yoffset 0
    show layer master:
        .15
        align (.5, .5)
        zoom 1.1

    play sound "sounds/sfx_plate_break.ogg"
    play test_six "sounds/loop_maggots.ogg" loop
    play test_one "voice/Alisa/4day/97 Sckream.ogg"
    "Вдребезги разбилась фарфоровая тарелка, до краёв наполненная опарышами."

    play test_six ["<silence .83>","sounds/sfx_transform_Alisa.ogg"]

    play test_one "voice/Alisa/4day/97 Sckream2.ogg"
    window hide
    scene d4_pal_fox_transit_beast_bg:
        xalign 1.
        easein 0.3 * 16 xalign 0.

    show d4_pal_fox_transit_beast:
        yalign 1.
        xpos .0
        xanchor .5
        easein 0.3 * 16 xpos 1. xanchor 1.0

    show d4_garage_smoke:
        align (.5, 1.)
        alpha 0
        zoom 1.1
        0.5
        parallel:
            linear 1. alpha 1
        parallel:
            linear 45 xpan 360
            xpan 0
            repeat

    pause 0.3 * 16
    window show
    "Рыжая шуба Алисы лопнула по швам, выпустив смердящий пар."

    scene d4_pal_fox_transit_beast_bg:
        xalign .0
        zoom 1.5
    show d4_palace_monster_fox
    with Dissolve(.5)

    play test_one "voice/Alisa/4day/97 Sckream0.ogg"
    "Её искорёженная морда оскалилась — и вонь шибанула мне в ноздри."


    play test_six "sounds/loop_tail_Alisa.ogg" loop

    scene d4_whiplash:
        align (.5, .5)
        zoom 1.01
        block:
            block:
                linear .03 xoffset 20
                linear .03 xoffset -20
                repeat 3
                linear .03 xoffset 0
            1.5
            repeat

    play test_one "voice/Alisa/4day/97 Sckream3.ogg"
    "Лиса кричала, а кровь текла по её щекам, будто слёзы, заставляя шерсть слипаться. Облысевший хвост бил позвонками о стены."

    scene d4_palace_beasts_bg:
        subpixel True
        align (.5, .85)
        zoom 1.0
        easein 30 zoom 1.2
    show d4_palace_ant_ol:
        subpixel True
        align (.5, 1.)
        zoom .40
        yoffset 200
        easein 30 zoom .40 * 0.95
    with Dissolve(.5)
    play test_two "voice/anton/2day/fear2.ogg"
    stop test_six fadeout 3
    "Я заслонил собой плачущую сестру."
    "Ужас ввинчивался в живот, бежал по кишкам, подступал к горлу."
    "Хотелось сорвать очки, чтобы всего этого не видеть, выдавить глаза, чтобы навсегда ослепнуть."

    play test_five "sounds/loop_maggots_owl.ogg" fadein 1 loop

    scene d4_pal_fox_transit_beast_bg:
        yalign .5
        xalign 1.
        zoom 1.1
        easein .5 xalign .0

    show d4_palace_monster_owl:
        subpixel True
        align (.5, 1.)
        yoffset 400
        zoom 1.5
        xoffset -960
        easein .5 xoffset 0
        .5
        "d4_palace_monster_owl_2"
        ease .75 yoffset 350
        "d4_palace_monster_owl"

    with Dissolve(.15)

    queue sound [ "<silence 1.8>", "<from 0 to 3>sounds/sfx_teeth_clack_1.ogg"]

    "Обернувшись к Сове, я скривился от отвращения."
    play test_three "voice/Owl/4day/Uhy.ogg"
    "Черви копошились в перьях её маски. Сгнивший клюв щёлкал, как садовые ножницы."

    stop test_five fadeout 1

    scene d4_palace_monster_owl_bg:
        yalign .5
        xalign .0
        zoom 1.1
        easein .5 xalign 1.

    show d4_palace_monster_wolf:
        subpixel True
        align (.5, 1.)
        yoffset 400
        zoom 1.5
        xoffset 960
        easein .5 xoffset 0
    with Dissolve(.15)
    play test_six "voice/Wolf/Ar.ogg"
    "Я отшатнулся, едва не врезавшись в волка."
    "Его морда вытягивалась, кости хрустели."
    "Зубы торчали из гноящихся дёсен, словно осколки стекла, а разбухший язык неустанно их облизывал."



    scene d4_palace_choice_bg2:
        xalign 1.
    show d4_palace_choice_head

    pause .2

    play sound ["<silence .2>", "sounds/sfx_footstep_massive_3.ogg"]

    show d4_palace_choice_head_ 3

    show d4_palace_monster_owl_bg:
        yalign .5
        xalign 1.
        zoom 1.1
        xzoom -1.0
        alpha 0
        .5
        parallel:
            easein .5 xalign .0
        parallel:
            linear .15 alpha 1

    show d4_palace_monster_bear:
        subpixel True
        align (.5, 1.)
        yoffset 400
        zoom 1.5
        xoffset -960
        alpha 0
        .5
        parallel:
            easein .5 xoffset 0
        parallel:
            linear .15 alpha 1

    play test_two "voice/anton/2day/Yavzdrognuliostanovils.ogg"
    play test_five "sounds/sfx_footstep_massive_garage_3.ogg"
    queue sound [ "<silence 0.5>", "<from 0 to 5>voice/Bear/4day/Va.ogg"]  
    "Краем глаза я заметил, как медведь загородил проход. Каждый миллиметр его плоти сочился алой сукровицей. Личинки заклеили слезящиеся глаза."

    scene d4_palace_children:
        align (.5, .5)
        zoom 1.01
        matrixcolor BrightnessMatrix(-.05)
        2.0
        block:
            linear .03 yoffset 5
            linear .03 yoffset -5
            repeat 5
        linear .03 yoffset 0
        repeat
    show d4_palace_ant_ol:
        subpixel True
        align (.5, 1.)
        zoom .40
        yoffset 125
        matrixcolor BrightnessMatrix(-.1)

    show palace_dust:
        Null()
        xoffset 200
        2.1
        "d4_polmirror_dust"
        2.36
        xoffset -800
        "d4_polmirror_dust"

    stop test_six fadeout 5

    with Dissolve(.5)
    play test_two "voice/olya/4day/49 Mama.ogg"
    "Я притянул шокированную Олю к себе, в панике ища выход."

    play sound "sounds/sfx_footstep_gore.ogg"

    scene d4_palace_candy_full 1
    show layer master:
        subpixel True
        align (.5, .5)
        easein .15 zoom 1.05
        ease .15 zoom 1.00
    "Нога угодила в груду сладостей, но это были уже не конфеты."
    play test_seven "sounds/Phrases_11.ogg"

    scene d4_palace_candy_full anim
    "На полу лежали человеческие останки."

    scene d4_palace_candy_full 8
    "Рёбра в лохмотьях мяса и выкорчеванные челюсти."
    "Бисер зубов и заплесневелые кости таза."

    scene d4_palace_children:
        align (.5, .5)
        zoom 1.01
        matrixcolor BrightnessMatrix(-.05)
        2.0
        block:
            linear .03 yoffset 5
            linear .03 yoffset -5
            repeat 5
        linear .03 yoffset 0
        repeat
    show d4_palace_ant_ol:
        subpixel True
        align (.5, 1.)
        zoom .40
        yoffset 125
        matrixcolor BrightnessMatrix(-.1)
    with Dissolve(.5)
    play test_two "voice/anton/2day/Vtyanul.ogg" volume 1.5
    "Крошечные черепа и плавающие в реках крови скальпы."
    voice "voice/kozel/4day/114.Esh.ogg"
    Noname "Ешь!"
    window hide
    play wtf "voice/kozel/4day/henshin.ogg"
    play movie "video/henshin_kozel.webm"

    call screen forced_timer(12)

    scene d4_pal_fox_transit_beast_bg:
        subpixel True
        xalign 1.
        linear 10 xalign 0.
    show d4_gor_ant 2:
        subpixel True
        xoffset 200
        align (.5, 1.)
        zoom 1.1
        linear 10 xoffset -400
    show Olya Weeps b_evening_winter 01 good ahead 01 dark 40:
        subpixel True
        align (.5, 1.)
        zoom 1.5
        yoffset 1200
        xoffset -200

        linear 10 xoffset -550-200

    stop movie
    play test_two "voice/anton/2day/Ah.ogg"
    "Надо мной возвышалась рогатая уродина, сжимая в длинных когтистых руках костяную флейту."
    stop wtf

    $ story_manager.MarkEvent(("day4", "scene8"))

    scene d4_big_master:
        subpixel True
        align (.5, 1.)
        easein 5 yalign .0
    with Dissolve(.5)

    show layer master:
        subpixel True
        .5
        align (.5, .5)
        linear 5 zoom 1.1
    "Гигантский, сбросивший обличие старца, Козёл."
    play test_six "voice/kozel/4day/124.Dih.ogg"
    "Чёрный, источающий ненависть и злобу, он испепелял раскалёнными углями глазищ."

    show layer master:
        subpixel True
        align (.5, .5)
        zoom 1.1
    "Его рога царапали потолок."

    play test_five "sounds/sfx_garage_melt.ogg"

    show layer master:
        subpixel True
        zoom 1.1
        align (.5, .5)
        linear 0.1 zoom 1.0
    pause .01

    scene d4_palace_room:
        align (.5, 1.)
        zoom 1.15
        linear .1 zoom 1.1
    show d4_small_master onlayer master1:
        matrixcolor BrightnessMatrix(.05)
        align (.5, 1.)
        zoom 1.05
        linear .1 zoom 1.
    show d4_garage_smoke onlayer master1:
        align (.5, 1.)
        parallel:
            xpan 0
            linear 45 xpan 360
            repeat
    with Dissolve(.1)

    pause .5

    scene d4_palace_room:
        align (.5, 1.)
        zoom 1.1
    with hpunch
    show d4_icicle_3 as ice1:
        subpixel True
        xanchor .5
        xpos 1400
        ypos 0.
        yanchor 1.
        zoom .15
        linear .25 ypos 1. yanchor 0.

    show d4_polmirror_dust:
        xoffset -300
    pause .5
    show d4_icicle_1 as ice2:
        subpixel True
        xanchor .5
        xpos 700
        ypos 0.
        yanchor 1.
        zoom .15
        .5
        linear .25 ypos 1. yanchor 0.
    show d4_polmirror_dust as dust1 onlayer master1:
        xoffset 100
    pause .2
    show d4_polmirror_dust as dust2:
        xoffset 300

    show delayed_dust as dust3 onlayer master1:
        Null()
        xoffset -700
        zoom 1.5
        align (.5, .5)
        1.5
        "d4_polmirror_dust"

    show d4_palace_room:
        align (.5, 1.)
        zoom 1.1
        linear 2.5 yoffset 100

    show d4_small_master onlayer master1:
        linear 2.5 matrixcolor BrightnessMatrix(.0)
    pause .01

    scene d4_palace_dark_blink

    with ImageDissolve("effect/imagedissolve/vfx_garage/01.jpg", 2.5, ramplen=128)

    hide d4_small_master onlayer master1
    hide dust1 onlayer master1
    hide dust2 onlayer master1
    hide dust3 onlayer master1

    show d4_small_master zorder 5
    "Лёд откалывался и таял, стекая в грязные лужи, а под ним обнажались металлические стены."
    "Я понял, что мы обречены в тесном чреве темницы, оцеплённые воющими чудовищами."
    "И оставалось лишь крепче прижимать к себе сестру и смотреть, как сужается круг, как мерзкие лапы тянутся из кровавого марева."

    window show

    play sound ["<silence .27>","sounds/sfx_footstep_massive_garage_1.ogg"]

    show d4_small_wolf zorder 10:
        xanchor .5
        ypos 1080
        xpos wpos[0]
        yanchor wyanc[0]
        zoom wzoom[0]
    with Dissolve(.5)
    show d4_small_wolf:
        ease .25 xpos wpos[1] yanchor wyanc[1] zoom wzoom[1]
        ease .10 xpos wpos[2] yanchor wyanc[2] zoom wzoom[2]
    voice "voice/Wolf/327 Poz.ogg"
    Wolf "Позволь, Хозяин, я разор-р-рву их на части!"

    play sound "sounds/sfx_footstep_massive_garage_2.ogg"

    show d4_small_wolf:
        ease .25 xpos wpos[3] yanchor wyanc[3] zoom wzoom[3]
        ease .10 xpos wpos[4] yanchor wyanc[4] zoom wzoom[4]
    voice "voice/Wolf/328 Ya.ogg"
    Wolf "Я выр-р-рву их глазные яблоки и тр-р-рахну их в сочащиеся р-р-раны!"

    play sound "sounds/sfx_footstep_massive_garage_3.ogg"

    show d4_small_wolf:
        ease .25 xpos wpos[5] yanchor wyanc[5] zoom wzoom[5]
        ease .10 xpos wpos[6] yanchor wyanc[6] zoom wzoom[6]
    voice "voice/Wolf/329 Y.ogg"
    Wolf "Я... Я..."
    show d4_small_wolf:
        ease .10 yanchor wyanc[6] - 0.05
        ease .10 yanchor wyanc[6]
    play test_two "voice/Wolf/342 hi.ogg"
    play test_seven "sounds/sfx_teeth_clack_2.ogg"

    "Пасть рычащего волка клацнула, словно капкан, — и густая белая пена брызнула в нашу сторону."

    play sound "sounds/sfx_footstep_massive_garage_4.ogg"

    play test_five "sounds/sfx_push_stomp_1.ogg"

    show d4_small_bear zorder 10:
        anchor (.5, .9)
        ypos 1080
        xpos .30
        zoom 1.5
        easein .25 xpos .355
        ease .10 xpos .35
    show d4_small_wolf:
        easein .5 xpos wpos[6] + 0.2 alpha 0
    with Dissolve(.15)

    "Тут же заживо гниющий медведь грубо оттолкнул бешеного собрата."

    play sound "sounds/sfx_footstep_massive_garage_2.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .335
            ease .10 xpos .34
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    voice "voice/Bear/4day/45 Dudki.ogg"
    Bear "Дудки! Мой черёд веселиться."

    play sound "sounds/sfx_footstep_massive_garage_1.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .355
            ease .10 xpos .35
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    voice "voice/Bear/4day/46 Kak.ogg"
    Bear "Как же я утомился слушать их сраный гундёж!"

    play sound "sounds/sfx_footstep_massive_garage_4.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .335
            ease .10 xpos .34
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    voice "voice/Bear/4day/47 YaZiv.ogg"
    Bear "О, я живьём сорву кожу с этой грёбаной козявки прямо на глазах её братца."

    play sound "sounds/sfx_footstep_massive_garage_2.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .355
            ease .10 xpos .35
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    voice "voice/Bear/4day/48 Ya.ogg"
    Bear "Я заставлю его съесть собственную сестру. Накормлю его досыта её потрохами."

    play sound "sounds/sfx_footstep_massive_garage_3.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .335
            ease .10 xpos .34
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    voice "voice/Bear/4day/49 Po.ogg"
    Bear "Пожалуйста, Хозяин..."

    play sound "sounds/sfx_footstep_massive_garage_1.ogg"

    show d4_small_bear:
        parallel:
            easein .25 xpos .355
            ease .10 xpos .35
        parallel:
            ease .25 yoffset -10
            ease .10 yoffset 0
    "Казалось, сейчас его морда треснет, расколется, как яйцо, из которого проклюнется что-то ещё более мерзкое, страшное..."

    play sound "sounds/sfx_footstep_massive_garage_3.ogg"
    play test_six "sounds/sfx_push_stomp_2.ogg"

    show d4_small_owl zorder 10:
        anchor (.5, .9)
        ypos 1080
        xpos .55
        zoom 1.5
        easein .25 xpos .495
        ease .10 xpos .50
    show d4_small_bear:
        easein .5 xpos .20 alpha 0
    with Dissolve(.5)
    "В оскалившегося медведя вцепились совиные когти-крючья, не давая тому приблизиться."

    play sound ["<silence .1>","sounds/sfx_footstep_massive_garage_2.ogg"]


    show d4_small_owl:
        parallel:
            easein .25 yoffset -50 zoom 1.75
        parallel:
            linear .25 alpha 0
    show d4_palace_monster_owl_big idle onlayer master1:
        alpha 0
        align (.5, 1.)
        .25
        easein .15 yoffset 35 alpha 1
        easein .05 yoffset 0
    pause .45

    show d4_palace_monster_owl_big scream onlayer master1:
        alpha 1
        align (.5, 1.)

    show layer master:
        align (.5, .5)
        block:
            linear .02 zoom 1.02
            linear .02 zoom 1.00
            repeat 125
    with Dissolve(.1)
    voice "voice/Owl/4day/Ona.ogg"
    Owl "Она моя! Моя, выблядки!"

    show d4_palace_monster_owl_big idle onlayer master1
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(.2)

    show d4_palace_monster_owl_big scream onlayer master1
    show layer master:
        align (.5, .5)
        block:
            linear .02 zoom 1.02
            linear .02 zoom 1.00
            repeat 130
    with Dissolve(.1)
    voice "voice/Owl/4day/Lapi.ogg"
    Owl "Лапы прочь от девчонки!"

    play test_four "sounds/loop_skirmish_beasts.ogg" fadein 0.6 loop

    show d4_palace_monster_owl_big idle onlayer master1
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(.2)

    hide d4_palace_monster_owl_big onlayer master1
    scene d4_palgar_bg2:
        align (.5, 1.)
        zoom 1.05
    show d4_palgar_master_hand:
        align (.5, 1.)
        zoom 1.1
    show d4_palgar_shadow_blink onlayer master1

    show layer master:
        align (.5, .5)
        zoom 1.00
        block:
            block:
                choice:
                    linear .05 xoffset 20
                    linear .05 xoffset -20
                    easein .10 xoffset 0
                choice:
                    linear .05 xoffset -20
                    linear .05 xoffset 20
                    easein .10 xoffset 0
            choice:
                .2
            choice:
                .5
            choice:
                1.
            repeat

    with Dissolve(.5)
    play test_two "voice/Wolf/330 RRR.ogg"
    "Клокочущий зверинец свалился в кучу, барахтаясь в кишках и талом жире."
    play test_six "voice/Bear/4day/Arrr.ogg"
    "Они выли, дрались, кусались, вырывали друг дружке клочки шерсти и горсти перьев, готовые растерзать друг друга, как свора голодных псов из-за объедков."

    stop test_four fadeout 1.2

    hide d4_garage_smoke onlayer master1
    hide d4_palgar_shadow_blink onlayer master1
    scene d4_master_bg:
        subpixel True
        align (.65, .35)
        block:
            ease .05 zoom 1.05
            ease .05 zoom 1.00
            repeat
    show d4_big_master_flute:
        subpixel True
        align (.65, .35)
        block:
            linear .01 zoom 1.01
            linear .01 zoom 1.00
            repeat

    stop test_two fadeout 0.5
    stop music2 fadeout 0.5
    $ music_general_volume = 0.5
    $ renpy.music.set_volume(0.5, 1.0, channel="music")
    play test_one "sounds/kozel_flute_whistle.ogg"
    "Вдруг визг флейты отдёрнул их, словно поводок."

    scene d4_palace_dark_blink
    show d4_small_master_flute onlayer master1
    show d4_small_wolf zorder 1:
        align (.5, 1.)
        xpos .68
    show d4_small_owl:
        align (.5, 1.)
        xpos .82
    show d4_small_bear zorder 1:
        align (.5, 1.)
        xpos .17
    show d4_small_fox:
        align (.5, 1.)
        xpos .32
        yoffset -75

    show d4_garage_smoke onlayer master1:
        xpan 0
        linear 45 xpan 360
        repeat

    show layer master:
        subpixel True
        align (.50, .15)
        block:
            ease .05 zoom 1.01
            ease .05 zoom 1.00
            repeat

    "Хозяин стаи околдовал страшил своей душераздирающей музыкой, вновь обратив их в неподвижные молчащие марионетки, верно ждущие команды «фас»."
    stop test_one fadeout 1.0
    $ music_general_volume = 1.0
    $ renpy.music.set_volume(1.0, 1.8, channel="music")

    show layer master:
        subpixel True
        align (.50, .50)
        zoom 1.0
    hide d4_small_master_flute onlayer master1
    show d4_small_master zorder 1
    with Dissolve(.5)

    "Козёл перестал обгладывать флейту из берцовой кости."

    "В последний раз смолкла дьявольская мелодия — хор вопящих младенцев, угодивших под каток."

    hide d4_garage_smoke onlayer master1
    scene d4_dark_floor:
        align (.5, .5)
        zoom 1.01
    with Dissolve(.5)
    "Кусок сырого человеческого мяса шлёпнулся у моих дрожащих ног."

    play sound "sounds/sfx_meat_slap.ogg"

    show d4_dark_meat with Dissolve(.1):
        align (.5, .5)
        zoom 1.01
        block:
            linear .03 yoffset -10
            linear .03 yoffset 10
            repeat 2
        linear .03 yoffset 0

    pause .3

    show d4_dark_floor:
        align (.5, .5)
        zoom 1.01
        block:
            linear .03 yoffset -5
            linear .03 yoffset 5
            repeat 2
        linear .03 yoffset 0
    voice "voice/kozel/4day/115.EshEli.ogg"
    Master "Ешь. Или будешь съеденным."
    play test_five "sounds/sfx_Olya_fall.ogg"
    pause .3

    scene d4_darkgar_olya_out_1
    with Dissolve(.25)
    "Вне себя от ужаса, я обернулся на Олю: та лежала в стороне, присыпанная снегом."
    "Совсем как мёртвая Белоснежка в мультфильме."
    "Возможно, она потеряла сознание от душераздирающего зрелища."

    scene d4_dark_fonback:
        align (.5, .5)
        zoom 1.5
        parallel:
            linear 15 zoom 1.05

    show d4_blood_body:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            linear 15 zoom .85
        parallel:
            ease 2.50 yoffset 5
            easein .50 yoffset -3
            ease .15 yoffset -2
            easein .25 yoffset -5
            repeat

    show d4_blood_head2:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            linear 15 zoom .85
        parallel:
            ease 2.50 yoffset 10
            easein .50 yoffset -5
            ease .15 yoffset -3
            easein .25 yoffset -10
            repeat




    with Dissolve(.5)
    play test_six "voice/anton/2day/Vshlip.ogg"
    "Мне хотелось разрыдаться в истерике, сойти с ума, умереть быстро и безболезненно прямо здесь и сейчас..."
    "Но, увы, я не мог."
    "Я по-прежнему оставался в камере пыток, выбирая между ужасным исходом в желудках чудовищ и каннибализмом."

    jump d4_beasts_choice3_refuse


label d4_beasts_choice3_refuse:
    $ story_manager.MarkEvent(("day4", "scene9"))

    scene d4_palace_dark_blink
    show d4_small_master zorder 2
    show d4_small_wolf zorder 1:
        align (.5, 1.)
        xpos .68
    show d4_small_owl:
        align (.5, 1.)
        xpos .82
    show d4_small_bear zorder 1:
        align (.5, 1.)
        xpos .17
    show d4_small_fox:
        align (.5, 1.)
        xpos .32
        yoffset -75

    show d4_garage_smoke zorder 5:
        xpan 270
        linear 45 xpan 360+270
    with Dissolve(.5)

    "Шерстяные мясорубки не сводили с меня свои алчные, вечно голодные глазёнки, готовые обглодать и перемолоть все мои кости, если я посмею отказаться от предложения их Хозяина."
    "Но стоит мне согласиться — я так же, как и они, навсегда утрачу свою волю и разум."
    "Превращусь в вечно голодную тварь, пляшущую под дудку кровожадного безумца."
    "И наверняка погублю Олю и всех, кого я так люблю..."

    scene d4_dark_fonback
    show d4_paw_anton_b norm:
        align (.5, 1.)
        xoffset -300
    with Dissolve(.5)
    "Губы мои тряслись, тошнота выворачивала наизнанку, но я нашёл в себе силы закричать:"

    show d4_paw_anton_b angry with Dissolve(.5)
    show d4_paw_anton_b shout with Dissolve(.2):
        linear .1 yoffset 10
        linear .1 yoffset 0
    voice "voice/anton/4day/193. Niko.ogg"
    Ant "Никогда и ни за что! Я человек!"
    show d4_paw_anton_b angry with Dissolve(.2)
    "Эти слова могли бы стать моей эпитафией, но я понимал, что никому уже не суждено найти мои останки."
    "Настала гробовая тишина."

    scene d4_master_bg:
        subpixel True
        align (.5, .5)
        zoom 1.1
        linear 10 zoom 1.2
    show d4_master idle:
        xalign .5
        yalign 1.0
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(.25)

    show d4_master_bg:
        subpixel True
        align (.5, .5)
        linear 10 zoom 1.0
    show d4_master scream
    show layer master:
        align (.5, .5)
        zoom 1.00
        block:
            linear .01 zoom 1.005
            linear .01 zoom 1.000
            repeat
    with Dissolve(.25)

    voice "voice/kozel/4day/116.Este.ogg"
    Master "Ешьте их! Бе-е-е-ейте их! Рвите на части!"

    play test_six ["<silence .67>","sounds/sfx_stomp_goat.ogg"]
    play test_seven ["<silence 2.1>","sounds/sfx_stomp_hard_snow.ogg"]

    show d4_master_bg:
        subpixel True
        align (.5, .5)
        linear 10 zoom 1.2
    show d4_master idle:
        xalign .5
    show layer master:
        align (.5, .5)
        zoom 1.00
    with Dissolve(.25)

    scene d4_domination_bg
    show d4_domination_anton
    show d4_garage_smoke zorder 5:
        xpan 180
        linear 45 xpan 360+180
    show d4_domination_master onlayer master1:
        subpixel True
        align (.5, .5)
        xoffset 0
        yoffset 500
        easein .75 xoffset 100 yoffset 250
        .5
        ease .75 xoffset 200 yoffset 0

    show layer master:
        align (.5, .5)
        zoom 1.05
        .65
        block:
            linear .03 xoffset 3
            linear .03 xoffset -3
            repeat 3
            linear .03 xoffset 0
        1.25
        block:
            linear .03 xoffset 3
            linear .03 xoffset -3
            repeat 3
            linear .03 xoffset 0

    with Dissolve(.25)

    play test_two "voice/anton/2day/fear4.ogg"
    "Рогатая тень накрыла нас."
    voice "voice/kozel/4day/119.Sl.ogg"
    Master "Сладкое мясо!"

    pause .4

    scene d4_protect_bg
    hide d4_domination_master onlayer master1
    show d4_garage_smoke:
        align (.5, 1.)
        transform_anchor True
        rotate 30
        xoffset -500
        yoffset 300
        zoom 2.
        block:
            xpan 0
            linear 45 xpan 360
            repeat
    show d4_protect_fox:
        alpha 0
        xoffset -25
        yoffset -25
        .5
        easein .25 xoffset 0 yoffset 0 alpha 1
    with Dissolve(.25)
    play test_four "sounds/sfx_footstep_massive_garage_2.ogg"

    pause .8

    "Внезапно Алиса метнулась к козлищу и встала между нами, крошечная на фоне огромного монстра."
    "Хвост волочился за лисой, рисуя алый след. Блохи скакали по её спине и проступившим костям."
    $ music_during_lines = 0.4
    voice "voice/Alisa/4day/98 podo.ogg"
    Alis "Подожди! Не спеши так, не стоит."
    voice "voice/Alisa/4day/99 Zai.ogg"
    Alis "Зайчик нам ещё пригодится. Зайчик нас покормит вкусненько."
    voice "voice/Alisa/4day/101 Dlya.ogg"
    Alis "Для медведя и лисы..."
    $ music_during_lines = 0.55
    voice "voice/kozel/4day/120.Za.ogg"
    Master "...Зайчик, кушать принеси." id d4_beasts_choice3_refuse_11cb0e52
    "Пламя в его глазницах замерцало."
    "Замершие истуканы недовольно оскалились."
    window hide
    $ dpos_bg = 1900
    $ dpos_beast = 1600
    $ dpos_master = 1200

    scene d4_palace_dark_blink:
        subpixel True
        align (.5, .25)
        zoom 2.00
        xoffset dpos_bg//2
        matrixcolor BrightnessMatrix(0.05)
        easein 20 xoffset -dpos_bg//2
    show d4_garage_smoke zorder 1:
        align (.5, 1.)
        subpixel True
        xpan 0
        linear 15 xpan 360
        repeat
    show d4_master dark zorder 2:
        subpixel True
        xalign .5
        yalign 1.0
        zoom .85
        blur 16
        xoffset 300
        easein 20 xoffset -900
    show d4_darkgar_bear_mid:
        subpixel True
        align (.5, 1.)
        xoffset -700
        easein 20 xoffset -700 -dpos_beast
    show d4_darkgar_wolf_mid:
        subpixel True
        align (.5, 1.)
        xoffset -100 +dpos_beast
        easein 20 xoffset -100
    show d4_palace_monster_owl_big idle:
        subpixel True
        align (.5, 1.)
        xoffset 500 +(dpos_beast + dpos_master) * .5
        easein 20 xoffset 500
    with Dissolve(.25)

    window show
    $ music_during_lines = 0.7

    voice "voice/Bear/4day/51 Da.ogg"
    Bear "Да разве это Зайчик?"
    pause 1.
    voice "voice/Wolf/332 Raz.ogg"
    Wolf "Разор-р-рвать и сожр-р-рать!"
    pause 1.
    voice "voice/Owl/4day/Samozv.ogg"
    Owl "Самозванец! Уху-уху!"
    pause 1.
    voice "voice/Owl/4day/Kozan.ogg"
    Owl "Кожаный мешок с требухой."

    hide d4_garage_smoke
    scene d4_dark_fonback
    show d4_anton_shock:
        align (.5, 1.)
        zoom .60
        xoffset -200
        matrixcolor BrightnessMatrix(-0.10)
    show d4_garage_smoke:
        align (.5, 1.)
        xpan 0
        linear 45 xpan 360
        repeat

    show d4_darkgar_empty_garage_bg_blink
    show d4_darkgar_alice_beast:
        align (.5, 1.)
        xoffset 400
        zoom 1.1
    with Dissolve(.25)
    $ music_during_lines = 0.6

    voice "voice/Alisa/4day/102 Zat.ogg"
    Alis "Заткнитесь, пустомели!"
    voice "voice/Alisa/4day/103 Razv.ogg"
    Alis "Разве вы не чуете? Разве вы не помните?"
    voice "voice/Alisa/4day/104 Kogda.ogg"
    Alis "Когда он чуть не укусил луну на снежной поляне."
    "Людоеды замолкли, разочарованно сглатывая слюну."
    stop music fadeout 2.5
    "Алиса тем временем крутанулась и..."
    queue music2 "<from 199>music/Sweet Bunny.ogg" volume 1.7 noloop fadein 3.5
    queue music2 "music/Sweet Bunny.ogg" volume 1.3
    $ music_during_lines = 1.0
    window hide

    play sound "sounds/sfx_coat_rustle.ogg"

    scene bg_black
    show d4_garage_smoke:
        align (.5, 1.)
        zoom 1.5

        block:
            xpan 0
            linear 30 xpan 360
            repeat
    show d4_domination_fox beast:
        xoffset -600
    with Dissolve(.25)

    $ dpan = 120
    show d4_garage_smoke as smokefg with Dissolve(.25):
        align (.5, 1.)
        zoom 1.5
        parallel:
            xpan dpan
            linear 5 xpan 360+dpan
            repeat
        parallel:
            2.
            linear 5 alpha 0

    show d4_domination_fox turned with Dissolve(.35)

    show d4_domination_fox cute with Dissolve(.35)

    window show
    "...вновь предстала милым ребёнком в маске лисицы, которую я впервые повстречал январским утром." id d4_beasts_choice3_refuse_990b8d86

    play test_three "sounds/sfx_footstep_massive_garage_2.ogg" 
    hide d4_domination_fox
    show d4_domination_fox bright
    show d4_domination_fox_bg behind d4_garage_smoke:
        alpha 0
        linear 2 alpha 1
    with Dissolve(.5)

    "Она двинулась ко мне скользящей походкой, растворяя весь ужас вокруг запахом апельсинов, порохом петард и волшебством."

    stop test_three fadeout 1

    "Её ласковые лапки нежно коснулись моей щеки, убрали слипшуюся прядь с моего лица."

    play sound "sounds/sfx_hugs.ogg"

    scene d4_dark_fonback:
        align (1., 1.)
        zoom 1.1
    show d4_darkgar_alice_hug_1

    with Dissolve(.5)
    "И, заключив меня в объятия, Алиса сладко зашептала:"
    voice "voice/Alisa/4day/105 Tosha.ogg"
    Alis "Тоша, ты хочешь спастись?"
    play test_two "voice/anton/4day/Uk.ogg"
    "Я молчал, стиснув зубы, боясь отвести взгляд, чтобы не разрушить мимолётное видение."
    voice "voice/Alisa/4day/106 Moi.ogg"
    Alis "Мой милый, скажи, ты хочешь спасти свою сестру?"


    scene d4_dark_fonback:
        align (.5, .5)
        zoom 1.5
        parallel:
            easein 15 zoom 1.05

    show d4_blood_body:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            ease 2.50 yoffset 5
            easein .50 yoffset -3
            ease .15 yoffset -2
            easein .25 yoffset -5
            repeat

    show d4_blood_head 3:
        animation
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        parallel:
            ease 2.50 yoffset 10
            easein .50 yoffset -5
            ease .15 yoffset -3
            easein .25 yoffset -10
            repeat

    show layer master:
        align (.5, 0)
        easein 15 zoom 1.5

    with Dissolve(.5)
    play test_two "voice/anton/4day/Hnik.ogg"
    "Слёзы брызнули из глаз, и я заревел."
    stop test_two fadeout 0.5
    voice "voice/anton/4day/195. Da.ogg"
    Ant "Д-да..."
    play test_two "voice/anton/4day/Hnik2.ogg"
    "Хватая лисичку за подол шубки, я продолжал всхлипывать и дрожать."
    $ music_during_lines = 0.9
    voice "voice/Alisa/4day/107 Ska.ogg"
    Alis "Скажи громче, чтобы все слышали."

    show d4_blood_head 4
    show layer master:
        align (.48, 0)
        zoom 1.75
        easein 30 zoom 1.85
    with Dissolve(.5)
    play test_two "voice/anton/4day/Hnik3.ogg"
    "Не помня себя от горя, я закричал, умываясь слезами:"
    stop test_two fadeout 0.5
    voice "voice/anton/4day/196.Daa.ogg"
    Ant "ДА!"

    play sound "sounds/sfx_choke_meat_Anton.ogg"
    stop music2 fadeout 0.5
    show d4_blood_head 5:
        xalign .5
        yalign 1.
        xoffset 300
        ypos 1080 + 10 + 300
        block:
            "d4_blood_head 3"
            .15
            "d4_blood_head 5"
            .15
            repeat
    show layer master:
        align (.48, 0)
        matrixcolor InvertMatrix(1.0)
        zoom 1.80
        parallel:
            linear .5 matrixcolor InvertMatrix(0.0)
        parallel:
            linear .10 zoom 1.70
            linear .10 zoom 1.80

    play test_two "voice/anton/4day/Uk.ogg"
    "Тут же мой рот наполнил металлический привкус крови."
    play test_one "music/Phrases_03.ogg"
    scene d4_dark_fonback:
        align (1., 1.)
        zoom 1.1
    show d4_darkgar_alice_hug_2:
        yoffset 10
        1.
        block:
            block:
                linear .05 xoffset 10 yoffset 0
                linear .05 xoffset 0 yoffset 10
                1.
                repeat 2
            3.
            repeat

    with Dissolve(.1)

    play music "music/some_ambient.ogg" fadein 4
    $ music_during_lines = 1.0
    play test_two "voice/anton/4day/Ukk.ogg"
    "Чёрные пальцы лисицы пропихивали кусок человечины глубже в мою глотку."

    play sound "sounds/sfx_Romka_fall_snow.ogg"

    scene d4_protect_bg
    show d4_garage_smoke:
        align (.5, 1.)
        transform_anchor True
        rotate 30
        xoffset -500
        yoffset 300
        zoom 2.
        block:
            xpan 180
            linear 45 xpan 360+180
            repeat
    show d4_protect_antfox
    with Dissolve(.25)
    stop test_two fadeout 0.5
    play test_three "voice/anton/4day/197. Davkrov.ogg"
    "Я упал на четвереньки, давясь и кашляя кровью, не в силах срыгнуть ставший в горле кусок плоти."
    "Меня вновь обступали со всех сторон разлагающиеся твари."

    scene d4_palace_dark_blink:
        align (1., 0.)
        zoom 1.3
    show d4_darkgar_owl_master
    show d4_garage_smoke:
        block:
            xpan 180
            linear 45 xpan 360+180
            repeat
    show d4_palace_monster_owl_big idle:
        align (.5, 1.)
        zoom 1.1
    with Dissolve(.25)

    show d4_palace_monster_owl_big scream:
        4.
        "d4_palace_monster_owl_big idle" with Dissolve(.2)
    with Dissolve(.2)
    voice "voice/Owl/4day/Kakoe.ogg"
    Owl "Какое посмешище."

    scene d4_darkgar_olya_out_1
    with Dissolve(.25)

    pause .25

    scene d4_darkgar_olya_out_2
    play test_four "sounds/sfx_footstep_massive_garage_1.ogg"
    with ImageDissolve("effect/ImageDissolve/shadow/01.jpg", .5)

    stop test_three fadeout 1
    voice "voice/Owl/4day/Pozvol.ogg"
    Owl "Позволь, Хозяин, я откушу от девчонки самую малость."

    scene d4_darkgar_olya_out_2:
        subpixel True
        .4

        align (.5, .5)
        transform_anchor True
        block:
            linear .03 zoom 1.01
            linear .03 zoom 1.00
            repeat
    stop test_three fadeout 1

    show d4_darkgar_olya_out_3:
        alpha 0.0
        align (.5, .5)
        ease 0.4 zoom 1.5 alpha 1.0
        parallel:
            ease 1.8 zoom 1.0 alpha 0.0
        parallel:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat 29
            linear .03 xoffset 0
    play test_one "sounds/piano-hit-1.ogg"
    "Бурлящая злоба утопила моё сознание, и что-то чужеродное и первобытное вырвалось из меня свирепым рыком:"
    play test_two "sounds/sfx_wrap_shirt.ogg"

    window hide

    scene d4_antonmad
    with Dissolve(.25)
    pause 1.0
    voice "voice/anton/4day/198. Tolko.ogg"
    Bunny "Только попробуй — и я вырву твой поганый язык и засуну глубоко в клоаку, ты, безмозглая курица! "
    play test_one "sounds/sfx_whoosh.ogg"

    scene d4_palace_dark_bg_1:
        align (1., 0.)
        zoom 1.3
    show d4_palace_monster_owl_big idle as backowl:
        align (.5, 1.)
        zoom 0.95
        alpha 0
        .75
        linear .25 alpha 1
    show d4_darkgar_owl_master
    show d4_garage_smoke:
        block:
            xpan 120
            linear 45 xpan 360+120
            repeat
    show d4_palace_monster_owl_big idle as frontowl:
        align (.5, 1.)
        zoom 1.1
        alpha 1
        .5
        linear .25 alpha 0


    window show

    play sound "sounds/sfx_footstep_massive_garage_2.ogg"
    play test_five "voice/Alisa/4day/Ululu.ogg"
    "Зловещая сова ошеломлённо отпрыгнула под улюлюканье лисы."

    scene d4_dark_floor
    show d4_dark_meat2
    with Dissolve(.25)
    "Мой голос смолк, а затем меня сложило пополам."

    play sound "sounds/sfx_Anton_vomit.ogg"

    hide d4_dark_meat2
    show d4_dark_meat3
    with Dissolve(.25)
    play test_three "voice/anton/4day/199. Rvota.ogg"
    "Изо рта брызнула рвотная каша с непережёванным «угощением»."
    voice "voice/kozel/4day/122.Ti.ogg"
    Master "Ты права. Зайчик..."
    stop music fadeout 4
    play music2 "music/Kripota.ogg" fadein 2
    $ music_during_lines = 0.65

    scene d4_darkgar_prava
    with Dissolve(.25)
    show delayed_dust as dust1:
        Null()
        xoffset -900
        zoom 1.5
        align (.5, .5)
        0.5
        "d4_polmirror_dust"
    show delayed_dust as dust2:
        Null()
        xoffset -100
        zoom 1.5
        align (.5, .5)
        0.75
        "d4_polmirror_dust"
    voice "voice/kozel/4day/124.Dih2.ogg"
    play test_two "voice/anton/4day/Dihanie.ogg"

    play sound "sounds/sfx_finger_poke_Goat.ogg"

    "Палец ткнулся в меня. Казалось, что это нож вонзился в солнечное сплетение по самую рукоять."
    voice "voice/kozel/4day/123.Tv.ogg"
    Master "Твой черёд угощать нас."

    scene d4_master_bg:
        subpixel True
        align (.5, .5)
        zoom 1.1
        ease 5 zoom 1.0
        ease 5 zoom 1.1
        repeat
    show d4_master idle:
        align (.5, .5)
    with Dissolve(.25)

    show d4_master scream:
        align (.5, .5)
        linear .05 zoom 1.01
        linear .05 zoom 1.00
        repeat
    with Dissolve(.25)
    voice "voice/kozel/4day/Dob.ogg"
    Master "Добудь к следующей ночи мяса, а иначе..."

    play sound ["<silence .6>","sounds/sfx_footstep_massive_garage_1.ogg"]

    show d4_master idle:
        align (.5, .5)
        linear .05 zoom 1.00
    with Dissolve(.25)

    $ renpy.start_predict("d4_runaway_night_bg")
    $ renpy.start_predict("d4_night_run_anton_glow")
    $ renpy.start_predict("runaway_snow1")
    $ renpy.start_predict("runaway_snow2")

    scene d4_palace_dark_blink:
        align (.5, .0)
        zoom 1.4
    show d4_small_owl:
        align (.5, 1.)
        xoffset -300
        yoffset 100
    show d4_small_wolf:
        xalign .5
        xoffset 50
        ypos 1.
        yanchor .60
        zoom 1.8
    with Dissolve(.5)
    show d4_small_wolf zorder 2:
        ease .25 xoffset 310+50 zoom 2.55
        ease .10 xoffset 300+50 zoom 2.5
    voice "voice/Wolf/342 Inche.ogg"
    Wolf "Иначе..."

    play sound "sounds/sfx_footstep_massive_garage_4.ogg"

    show d4_palace_monster_bear zorder 4:
        subpixel True
        yalign 1.
        xpos .65
        xanchor 1.
        alpha 0
        parallel:
            easein .25 xpos .76
            ease .10 xpos .75
        parallel:
            linear .25 alpha 1

    voice "voice/Bear/4day/59 Enache.ogg"
    Bear "Иначе..."
    window hide

    show d4_polmirror_dust as dust1 zorder 3:
        xanchor .5
        xpos -.35
    pause .15
    show d4_polmirror_dust as dust2 zorder 5:
        xanchor .5
        xpos -.10
    pause .05
    show d4_polmirror_dust as dust3 zorder 1:
        xanchor .5
        xpos .10
    pause .10
    show d4_polmirror_dust as dust4 zorder 3:
        xanchor .5
        xpos .45

    pause 1.0

    scene d4_master_bg:
        subpixel True
        align (.5, .5)
        zoom 1.0
        ease 5 zoom 1.1
        ease 5 zoom 1.0
        repeat
    show d4_master idle:
        subpixel True
        align (.5, .75)

    $ story_manager.MarkEvent(("day4", "scene10"))

    window show
    "Алиса молча отступила в тень, а Козёл приблизил ко мне зловонную пасть и прорычал:"
    show d4_master scream:
        align (.5, .75)
        linear .05 zoom 1.21
        linear .05 zoom 1.20
        repeat
    show d4_polina_am_5 as saliva1:
        pos (.5, .5)
        anchor (.50, .65)
        yoffset 300
        zoom .5
        parallel:
            linear .35 zoom 1.0
        parallel:
            .10
            linear .25 alpha 0
        parallel:
            easeout .35 yoffset 900
    show d4_polina_am_5 as saliva2:
        pos (.5, .5)
        anchor (.50, .65)
        xzoom -1
        zoom .5
        yoffset 300
        parallel:
            linear .35 zoom 1.0
        parallel:
            .10
            linear .25 alpha 0
        parallel:
            easeout .35 yoffset 600
    with Dissolve(.25)
    $ music_during_lines = 0.85
    voice "voice/kozel/4day/125.ME.ogg"
    Master "Иначе... мы съедим всю твою семью."

    play sound "sounds/sfx_stomp_goat.ogg"

    show d4_master idle:
        align (.5, .75)
        linear .05 zoom 1.20
    with Dissolve(.25)
    "Он рубанул копытом в пол, и я побежал прочь, как ошпаренный, забыв про всё."

    play test_five "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 0.6 loop

    scene d4_runaway_night_bg:
        animation
        align (.5, .5)
    show black:
        alpha .5
    show d4_night_run_anton_glow zorder 1:
        animation
        align (.5, .5)
    show runaway_snow1 zorder 1:
        zoom 1.1
        matrixcolor BrightnessMatrix(-.6)
    show runaway_snow2 zorder 1:
        zoom 1.1
        matrixcolor BrightnessMatrix(-.6)
    with Dissolve(.25)
    play test_six "voice/kozel/4day/126.Se.ogg"
    play test_four "voice/Wolf/334 Siedim.ogg"
    play test_two "voice/anton/1day/029.Beg i o.ogg"
    play test_three "voice/Bear/4day/54 Sozrem.ogg"
    "В спину неслось многоголосое: «Съедим! Сожрём! Живьём!»"

    show d4_icicle_1_dark zorder 2:
        subpixel True
        transform_anchor True
        rotate 30
        xzoom -1
        offset (-500, 0)
        block:
            pos (1., 0.)
            anchor (.0, 1.)
            1.25
            linear .5 pos (0., 1.) anchor (1., 0.)
            .75
            repeat
    show d4_icicle_2_dark zorder 2:
        subpixel True
        transform_anchor True
        rotate 30
        xzoom -1
        offset (200, 0)
        block:
            pos (1., 0.)
            anchor (.0, 1.)
            linear .75 pos (0., 1.) anchor (1., 0.)
            1.75
            repeat
    show d4_icicle_3_dark zorder 0:
        subpixel True
        transform_anchor True
        rotate 30
        xzoom -1
        offset (600, 0)
        block:
            pos (1., 0.)
            anchor (.0, 1.)
            2.0
            linear .5 pos (0., 1.) anchor (1., 0.)
            repeat
    "Лёд падал мне на плечи кусками, в них вмёрзли дохлые грызуны."

    "Я вырвался на волю, туда, где сосны шевелили ветками и сыпали снегом, словно кашевары, сдабривающие солью яства."
    "Ветер драл мои волосы."
    stop test_two fadeout 2.5
    "Я повернулся и похолодел."

    stop test_five fadeout 0.6



    play sound ["<silence .15>","sounds/sfx_castle_fall.ogg"]

    window hide
    show d4_snow_night_full onlayer master1
    scene d4_palace_garage_1:
        align (.5, .5)
        zoom 1.05
    with Dissolve(.5)

    scene d4_palace_garage_break:
        align (.5, .5)
        zoom 1.05

    pause 2.5

    scene d4_palace_garage_blink:
        align (.5, .5)
        zoom 1.05

    pause 1.5

    play test_two "voice/anton/2day/fear5.ogg"

    hide d4_snow_night_full onlayer master1
    scene dark_forest_day3_1 dark1:
        zoom .5
        xzoom -1
    show bg_black:
        alpha .75
    show snow_night_1
    show d4_dr_scary_base
    show d4_scary_eyes_glow:
        xpos -100+20
        block:
            linear .03 xoffset 2
            linear .03 xoffset -2
            repeat

    show blizzard_d4_evening_face
    with Dissolve(.5)

    pause 1.


    scene d4_palace_garage_g1:
        align (.5, .5)
        zoom 1.05
        .5
        "d4_palace_garage_g2" with Dissolve(5.0)
    show d4_snow_night_full onlayer master1
    with Dissolve(.5)

    pause 1.

    window show

    $ renpy.stop_predict("d4_runaway_night_bg")
    $ renpy.stop_predict("d4_night_run_anton_glow")
    $ renpy.stop_predict("runaway_snow1")
    $ renpy.stop_predict("runaway_snow2")

    "На моих глазах Гараж исчезал, растворялся слоями, тускнел и становился прозрачным, а потом порыв ветра смёл фантом чёрных стен."
    stop music2 fadeout 4
    "И только сейчас я понял, что давно выпустил руку сестры, и она осталась в логове чудищ."
    play music "music/27_Cry.ogg" fadein 3
    $ music_during_lines = 1.0
    "На месте, где минуту назад стоял дворец, рос сугроб."
    play test_three "voice/anton/2day/Ah.ogg"
    "Из его верхушки торчала девчачья кисть, как крест из могильной насыпи."
    "Вне себя от ужаса, я бросился к сугробу и принялся расчищать снег."

    play test_five "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 0.4 loop

    window hide

    scene d4_palace_garage_g2:
        align (.5, .5)
        zoom 1.05
    show layer master:
        align (.55, .65)
        parallel:
            easeout_quad 1.0 zoom 1.4
        parallel:
            linear .1 xoffset -5 yoffset -10
            linear .1 xoffset 0 yoffset 0
            linear .1 xoffset 5 yoffset -10
            linear .1 xoffset 0 yoffset 0
            repeat

    pause 0.5

    stop test_five fadeout 0.8
    play sound "sounds/sfx_snow_digging_1.ogg"

    scene d4_episode_end_olya_death_nokidding_trustme_she_died_0

    with Dissolve(.5)
    scene d4_episode_end_olya_death_nokidding_trustme_she_died_0:
        "d4_episode_end_olya_death_nokidding_trustme_she_died_1" with ImageDissolve("effect/imagedissolve/vfx_garage/5.png", 1.5)
    show d4_episode_end_olya_death_nokidding_trustme_she_died_1:
        alpha 0.0
        linear 1.5 alpha 1

    window show
    "Под белой массой оголялось плечо и бледное Олино личико."
    play test_six "voice/olya/4day/72 H.ogg"
    "Её посиневшие губы дрогнули."
    "Жива!"
    voice "voice/anton/4day/200. Ya.ogg"
    Ant "Я сейчас!"

    if Flags.Has("katya"):
        "При мысли, что то же самое я говорил Кате, у меня пересохло в горле."

    play sound "sounds/sfx_snow_digging_2.ogg"

    scene d4_episode_end_olya_death_nokidding_trustme_she_died_2 with Dissolve(.5)
    play test_six "voice/olya/4day/70 H.ogg"
    play test_three "voice/anton/4day/203.Mf.ogg"
    "Я копал и умолял её держаться."
    "Уже дошёл до живота."

    play sound "sounds/sfx_snow_digging_3.ogg"

    scene d4_episode_end_olya_death_nokidding_trustme_she_died with Dissolve(.5):
        yalign 0.0
    voice "voice/olya/4day/69Hol.ogg"
    Oly "Холодно..."
    "Голосок был слабым."
    voice "voice/anton/4day/201. Niche.ogg"
    Ant "Ничего."
    voice "voice/anton/4day/201. Otn.ogg"
    Ant "Отнесу тебя домой, согрею, шоколадом напою, — ты только не засыпай, слышишь?"
    voice "voice/anton/4day/202. Tito.ogg"
    Ant "Ты только..."

    play sound "sounds/sfx_gore_touch.ogg"

    "Мои пальцы напоролись на что-то липкое и горячее."
    "Я разгрёб снег – он сделался красным и рыхлым."

    $ renpy.scene("master1")
    scene d4_episode_end_olya_base
    show d4_episode_end_olya_overlay5
    show blizzard_d4_evening_face
    with Dissolve(.5)
    voice "voice/olya/4day/50 Cho.ogg"
    Oly "Что это? Что это там?"

    hide d4_episode_end_olya_overlay5 with Dissolve(.2)
    play test_three "voice/anton/4day/202. Sgl.ogg"
    "Я сглотнул."
    voice "voice/olya/4day/51Poch.ogg"
    Oly "Почему ты не отвечаешь?"

    scene d4_episode_end_olya_death_nokidding_trustme_she_died:
        yalign 0.
    show d4_snow_night_full onlayer master1
    with Dissolve(.5)
    play test_six "voice/olya/4day/71 H.ogg"
    "А что я мог ответить?"
    play test_six "sounds/screamer-2.ogg"

    stop music fadeout 1
    play test_three "sounds/hum-1.1.ogg" loop

    window hide

    scene d4_episode_end_olya_death_nokidding_trustme_she_died:
        yalign 0.
        linear .5 yalign 1.

    pause 1.

    window show
    "Ниже пояса тело Оли обрывалось. Из туловища вывалились кольца кишечника."

    hide d4_snow_night_full onlayer master1
    scene d4_episode_end_olya_base
    show blizzard_d4_evening_face onlayer master1
    show d4_episode_end_olya_overlay3 with Dissolve(.25):
        block:
            .4
            "d4_episode_end_olya_overlay2" with Dissolve(.2)
            .2
            "d4_episode_end_olya_overlay3" with Dissolve(.2)
            repeat

    show layer master:
        align (.55, .40)
        zoom 1.01
        block:
            linear .15 zoom 1.2
    show focus_lines_bright onlayer master1:
        .15
        linear .25 alpha 0
    play test_six "voice/olya/4day/52EE.ogg"
    "Оля склонила голову и уставилась на безобразные обрубки."

    scene d4_episode_end_olya_base
    show d4_episode_end_olya_overlay7
    show layer master:
        align (.55, .40)
        zoom 1.2
    with Dissolve(.5)

    pause .10

    show d4_episode_end_olya_overlay4
    show layer master:
        align (.55, .40)
        zoom 1.2
        parallel:
            linear 2. zoom 1.35
        parallel:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat
    with Dissolve(.25)

    show black onlayer master1 zorder 100:
        alpha 0
        linear 2. alpha 1

    stop test_three fadeout 3.5
    play test_seven "sounds/piano-hit-3.ogg"
    play test_five "voice/olya/4day/52 Aaa.ogg"
    "Она истошно завопила."


    window hide


    scene black
    $ renpy.scene("master1")
    with Dissolve(.5)

    call d4_true_detective_calculate from _call_d4_true_detective_calculate

    call d4_flowchart

    jump day_5




label d4_beasts_choice_take_1:
    $ story_manager.MarkEvent(("day4", "treat1", "accept"))
    jump d4_beasts_choice_take
label d4_beasts_choice_take_2:
    $ story_manager.MarkEvent(("day4", "treat2", "accept"))
    jump d4_beasts_choice_take
label d4_beasts_choice_take:

    jump d4_beasts_choice_take.devend
    label d4_beasts_choice_take.dev hide:
        scene black
        menu:
            "Сразу согласился":
                pass
            "Согласился со 2го раза":
                $ Flags.Raise("refuse")
        menu:
            "Сватал Полину и Ромку":
                $ Flags.Raise("day2 fox")
            "Не занимался ничем таким":
                pass
        menu:
            "Был в гостях у Полины":
                $ Flags.Raise("polhouse")
            "Занимался другими делами":
                pass
    label d4_beasts_choice_take.devend:

    $ Flags.Raise("agree")

    window hide
    scene d4_agree_bg
    show d4_agree_candyhand 2:
        subpixel True
        ypos 100
        alpha 0
        .5
        parallel:
            ease 5 xoffset -5*2 yoffset 0
            ease 5 xoffset 5*2 yoffset -5*2
            ease 5 xoffset 0 yoffset 5*2
            ease 5 xoffset 5*2 yoffset 0
            repeat
        parallel:
            linear .5 alpha 1 ypos 0


    show layer master:
        matrixcolor SaturationMatrix(0.0)
    with Dissolve(.5)

    play sound "sounds/sfx_snow_grab_candy.ogg"

    "Я вынул из груды сладостей на полу самую аппетитную конфету."

    play sound "sounds/sfx_chew_crunch.ogg"

    show d4_agree_candyhand 1 with Dissolve(.5)
    play music2 "music/FoxSong_Instumental+back_vocal.ogg" volume 0.65 fadein 2

    pause .5
    show layer master:
        matrixcolor SaturationMatrix(0.0)
        linear 1.0 matrixcolor SaturationMatrix(1.0)
    pause .5

    Narr_color "Надкусил — молочный шоколад таял во рту."

    scene d4_color1_bg:
        xalign 1.
    show d4_color1_moroz
    show d4_color1_moroz_hand:
        align (.5, 1.)
        subpixel True
        transform_anchor True
        yoffset 510
        rotate -15
        easein 1.0 yoffset 10 rotate 0
        ease .1 yoffset 15
        block:
            ease 5 xoffset -5*3 yoffset 0
            ease 5 xoffset 5*3 yoffset -5*3
            ease 5 xoffset 0 yoffset 5*3
            ease 5 xoffset 5*3 yoffset 0
            repeat
    with Dissolve(.5)
    $ music_during_lines = 0.6
    voice "voice/kozel/4day/127.S.ogg"
    Frost_Color "С выбором вас поздравляю, веселитесь в этот час!"


    play test_seven "sounds/sfx_sparks.ogg"    
    $ d4_startype = False
    show screen starrise()
    call screen forced_timer (1.85)
    hide screen starrise
    call d4_starfall from _call_d4_starfall


    voice "voice/kozel/4day/127Ya.ogg"
    Frost_Color "Я желанья исполняю сокровенные для вас!"

    show d4_color1_bg:
        xalign 1.
        ease 1. xalign 0. xoffset -10

    show d4_color1_moroz:
        xanchor 0.
        yalign 1.
        xpos 0
        ease 1. xpos int(1602*1.5)
    show d4_color1_moroz_hand:
        xanchor 0.
        yalign 1.
        xpos 0
        ease 1. xpos int(1602*1.5)

    show Olya Color default 00 good ahead 04:
        xpos int(-1602*1.5)
        ease 1. xpos 0

    pause 1.

    show Olya Color default 00 good ahead 06 with Dissolve(.2)
    voice "voice/olya/4day/53 A.ogg"
    Olya_Color "Антон, смотри!"
    show Olya Color default 00 good ahead 05 with Dissolve(.2)

    Narr_color "Личико сестры было перемазано шоколадом, и я уже собирался сделать ей замечание."

    show layer master:
        linear .02 xoffset 5
        linear .02 xoffset 10
        repeat
    Narr_color "Но слова застряли в горле."

    play test_five "sounds/loop_pine_growing.ogg" fadein 3 loop
    stop test_seven fadeout 6

    show d4_color1_elka:
        xpos 1820
        xanchor .5
        yanchor 0.
        ypos 1.
        zoom .75
        easein 10 zoom 1. yanchor 1.

    pause 5.

    show Olya Color default 00 good aside 05 with Dissolve(.2)
    show layer master:
        block:
            linear .02 xoffset 5
            linear .02 xoffset 10
            repeat
        time 5
        linear .02 xoffset 0

    stop test_five fadeout 8

    Narr_color "Гигантская ель устремлялась к звёздам и исчезала где-то в космосе – её венчала круглая Луна."
    Narr_color "Огромные шары сияли на ветвях, гирлянды переливались всеми цветами радуги."



    scene d4_color1_roof
    show d4_color1_elka2
    with Dissolve(.5)
    Narr_color "Крыша исчезла, и над нами раскинулись мириады созвездий."
    play sound "sounds/sfx_roof_gone.ogg"

    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)
    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .6
        matrixcolor SaturationMatrix(1.5)
    show day3_jump_sky_forest:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)
    show d4_color1_elka2
    with ImageDissolve("effect/imagedissolve/elkaroof/elka_roof.jpg", 2.5, ramplen=128)

    show snow_up_d4_trip:
        alpha 0
        linear 1. alpha 1
    play test_six "voice/Alisa/4day/Wahaha.ogg"
    Narr_color "Музыка, смех, аромат хвои и сладостей!"
    play test_four "voice/Bear/4day/hah.ogg"
    play test_three "voice/Owl/4day/10 Hihihi.ogg"
    Narr_color "А рядом плясали Медвежутка, Волчик и Совушка!"
    play test_five "voice/Wolf/314 Happy.ogg"
    Narr_color "И снежинки падали задом наперёд!"

    play sound "sounds/sfx_tinsel_rustle.ogg"
    play test_one "voice/anton/4day/Heh.ogg"
    Narr_color "Я засмеялся. Потрогал пышную позолоченную мишуру."
    Narr_color "Всё по-настоящему!"

    scene d4_color_bg3:
        xalign .0
    show blizzard_d4_trip
    show Olya Color default 00 good aside 02:
        align (.5, 1.)
        zoom .75
    show d4_color1_elka:
        xpos 1820
        xanchor .5
        yalign 1.

    show snow1_slow onlayer master1:
        matrixcolor TintMatrix("#9bd7ff") * BrightnessMatrix(.4)
        yzoom -1
    show snow2_slow onlayer master1:
        matrixcolor TintMatrix("#9bd7ff") * BrightnessMatrix(.4)
        yzoom -1
    show snow3_slow onlayer master1:
        matrixcolor TintMatrix("#9bd7ff") * BrightnessMatrix(.4)
        yzoom -1

    with Dissolve(.5)

    pause .5

    show Olya Color default 00 good ahead 03 with Dissolve(.2)
    voice "voice/olya/4day/54 E.ogg"
    Olya_Color "Это что, это она?"
    show Olya Color default 00 good ahead 02 with Dissolve(.2)

    show d4_color_alice:
        align (.5, 1.)
        xoffset -700
        easein .5 xoffset -600
    with Dissolve(.5)

    voice "voice/Alisa/4day/109 Vi.ogg"
    Alis_Color "Вы тут не про Небыляндию, случайно, говорите?"

    show Olya Color default 00 good ahead 03 with Dissolve(.2)
    voice "voice/olya/4day/55 Et.ogg"
    Olya_Color "Это и есть Небыляндия?"
    show Olya Color default 00 good ahead 02 with Dissolve(.2)


    show d4_color_alice:
        align (.5, 1.)
        xoffset -600
        linear .25 yoffset 90
        linear .25 yoffset 0
    Narr_color "Алиса манерно поклонилась."

    show d4_color_bg3:
        ease 1.5 xalign .9

    show d4_color_alice:
        ease 1.5 xoffset -700 -1600*1.1

    show Olya Color default 00 good ahead 02:
        ease 1.5 xoffset -1600*0.9

    show d4_color1_elka:
        yalign 1.
        ease 1.5 xpos 150
    Narr_color "Шары переливались и мерцали, и моя душа мерцала им в унисон."
    Narr_color "Я становился зимним волшебным лесом, мягкой ласковой хвоей, всеми созвездиями сразу."

    window show

    scene d4_color_bg3:
        subpixel True
        xalign 0.9
        block:
            1.
            easein 1.25 xalign 1.0



    show d4_color1_elka:
        subpixel True
        xanchor .5
        yalign 1.
        xpos 150
        block:
            1.
            easein 1.25 xpos -75



    show d4_color_alice:
        yalign 1.0
        xpos -0.25
        xanchor .5
        zoom 1.2
        alpha 1
        easein 3. xpos .75 zoom 1.
        alpha 0
    show d4_color_alice as alice2 behind d4_color1_elka:
        yalign 1.0
        xpos .75
        xanchor .5
        zoom 1.
        alpha 0
        3.
        alpha 1
        easeout 3. xpos -.25 zoom .8

    show blizzard_d4_trip behind alice2
    with Dissolve(.55)

    voice "voice/Alisa/4day/110 Dobro.ogg"
    Alis_Color "Добро пожаловать домой!"
    Narr_color "Вот где всегда был мой дом."
    Narr_color "Снег искрился и слепил."

    show d4_color_olya_dance:
        yalign 1.0
        xpos -0.25
        xanchor .5
        zoom 1.
        alpha 1
        easein 3. xpos .75 zoom .82
        alpha 0
    show d4_color_olya_dance as olya2 behind d4_color1_elka:
        yalign 1.0
        xpos .75
        xanchor .5
        zoom .82
        alpha 0
        3.
        alpha 1
        easeout 3. xpos -.25 zoom .65
    Narr_color "Оля закружилась в танце. Схватила по конфете в каждую руку."

    pause 1.0

    show d4_color_wolf:
        yalign 1.0
        xpos -0.25
        xanchor .5
        zoom 1.2
        alpha 1
        easein 3. xpos .75 zoom 1.
        alpha 0
    show d4_color_wolf as wolf2 behind d4_color1_elka:
        yalign 1.0
        xpos .75
        xanchor .5
        zoom 1.
        alpha 0
        3.
        alpha 1
        easeout 3. xpos -.25 zoom .8
    play test_two "voice/Wolf/311 R.ogg"
    Narr_color "Волчонок жонглировал «Киндер-сюрпризами»."

    scene d4_color_polyana:
        align (.5, 1.)
        zoom 0.75
    show blizzard_d4_trip zorder 1
    with Dissolve(.5)
    voice "voice/olya/4day/56 T.ogg"
    Olya_Color "Ты видел?"
    show d4_color_polyana:
        subpixel True
        align (.5, 1.)
        zoom 0.75
        ease 1 zoom 0.85
    Narr_color "Приставки, «Тетрисы», куклы и трансформеры лежали под елью, словно их грузовиками свозили сюда."
    voice "voice/olya/4day/57 Et.ogg"
    Olya_Color "О! Это всё наше?"

    play test_four "sounds/loop_dancing.ogg" fadein 1 loop

    show d4_color_polyana:
        subpixel True
        align (.5, 1.)
        zoom 0.85
        block:
            ease .35 yoffset 30
            ease .35 yoffset 0
            repeat 2
        block:
            parallel:
                ease .35 xoffset -40 yoffset 30
                ease .35 xoffset 0 yoffset 0
                ease .35 xoffset 40 yoffset 30
                ease .35 xoffset 0 yoffset 0
                repeat
            parallel:
                ease 3 xpos .45
                ease 3 xpos .55
                repeat
    Narr_color "Я понял, что тоже танцую, и ответил, не прерывая движений:"
    voice "voice/anton/4day/204.Mn.ogg"
    Ant_Color "Многовато для нас одних. Я бы поделился с кем-нибудь. А ты?"
    voice "voice/olya/4day/58 Nu.ogg"
    Olya_Color "Хм... Ну-у-у, если с кем-то хорошим."
    Narr_color "Какие-то дети стояли у кромки опушки, зачарованно глазея на праздник."

    stop test_four fadeout 1.2

    show d4_color_polyana:
        easeout .15 xoffset 0 xpos .5 yoffset 0
    voice "voice/anton/4day/204. Ei.ogg"
    Ant_Color "Эй!"

    play test_six "<from 0 to 1>sounds/loop_footsteps_monster_snow.ogg"
    play sound ["<silence 1.3>","sounds/sfx_owl_lands_snow.ogg"]

    show d4_color_polyana:
        parallel:
            easein_quad .5 zoom .55
            .5
            easeout_quad .5 zoom 1.35 + 0.02
            ease .15 zoom 1.35
        parallel:
            .25
            ease 1.0 yalign .0

    Narr_color "Я прыгнул через всю поляну и плавно приземлился возле них."
    voice "voice/anton/4day/205. Ho.ogg"
    Ant_Color "Хотите с нами?"

    scene d4_color_bg3:
        xalign .5
        xzoom -1
    show blizzard_d4_trip
    show d4_color_children
    with Dissolve(.5)

    voice "voice/Child/4day/Amozno.ogg"
    Children_Color "А можно?"
    voice "voice/anton/4day/206. Spr.ogg"
    Ant_Color "Спрашиваете!"
    play test_three "voice/Child/4day/Zdorovo.ogg"

    play sound "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 1 loop

    Narr_color "Дети взялись за руки. Я повёл их цепочку к подаркам."

    scene d4_color_polyana:
        xalign .5
        yalign .0
        zoom 1.35
    show blizzard_d4_trip
    with Dissolve(.5)

    Narr_color "Не было ничего лучше, чем вести кого-то по тропинке к мечте."

    stop sound fadeout 1.5

    scene d4_color_bg3:
        xalign .0
    show blizzard_d4_trip
    show Olya Color default 00 good ahead 02 zorder 2:
        align (.5, 1.)
        zoom .85
        xoffset -600
    show d4_color1_elka zorder 3:
        xpos 1820
        xanchor .5
        yalign 1.
    with Dissolve(.5)
    Narr_color "Праздник наступил по-настоящему."

    play sound "sounds/steps/loop_five_kids_footsteps_snow.ogg" fadein 1.2

    pause .6

    show d4_color_children behind blizzard_d4_trip:
        align (.5, 1.)
        zoom .80
        xoffset 250
    with Dissolve(.5)
    play test_three "voice/Child/4day/Ha.ogg"
    stop sound fadeout 1
    Narr_color "В каждом празднике, как в красивом яблоке, была червоточинка – его скоротечность."

    show d4_color_alice zorder 1:
        align (.5, 1.)
        xoffset -500
        zoom .95
    with Dissolve(.5)
    play test_seven "voice/olya/4day/Ahahaha.ogg"
    Narr_color "Но здесь, под лапами величественной ели, праздник не кончался."
    voice "voice/Alisa/4day/111 TiS.ogg"
    Alis_Color "Ты счастлив, Тоша?"
    voice "voice/anton/4day/207. Ya.ogg"
    Ant_Color "Я счастлив!"

    play test_five "sounds/loop_fireworks.ogg" loop

    $ d4_startype = True

    scene d4_color_bg3:
        xalign .0
        block:
            linear 0.15 matrixcolor TintMatrix("#bfb") * BrightnessMatrix(0.10 * -0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#fbb") * BrightnessMatrix(0.10 * -0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#fbf") * BrightnessMatrix(0.10 * -0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#ffb") * BrightnessMatrix(0.10 * -0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            repeat
    show d4_color_children:
        align (.5, 1.)
        zoom .80
        xoffset 250
        block:
            linear 0.15 matrixcolor TintMatrix("#7f7") * BrightnessMatrix(0.10 * 0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f77") * BrightnessMatrix(0.10 * 0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f7f") * BrightnessMatrix(0.10 * 0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#ff7") * BrightnessMatrix(0.10 * 0.20)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            repeat
    show blizzard_d4_trip
    show d4_color_alice zorder 1:
        align (.5, 1.)
        xoffset -500
        zoom .95
        block:
            linear 0.15 matrixcolor TintMatrix("#9f9") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f99") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f9f") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#ff9") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            repeat
    show Olya Color default 00 good ahead 02 zorder 2:
        align (.5, 1.)
        zoom .85
        xoffset -600
        block:
            linear 0.15 matrixcolor TintMatrix("#9f9") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f99") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f9f") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#ff9") * BrightnessMatrix(0.10 * 0.70)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            repeat
    show d4_color1_elka zorder 3:
        xpos 1820
        xanchor .5
        yalign 1.
        block:
            linear 0.15 matrixcolor TintMatrix("#0f0") * BrightnessMatrix(0.10 * 1.00)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f44") * BrightnessMatrix(0.10 * 1.00)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#f4f") * BrightnessMatrix(0.10 * 1.00)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            linear 0.15 matrixcolor TintMatrix("#ff0") * BrightnessMatrix(0.10 * 1.00)
            linear 2.00 matrixcolor TintMatrix("#fff") * BrightnessMatrix(.0)
            1.00
            repeat

    play test_three "voice/Child/4day/Haha.ogg"
    Narr_color "В небе взрывались грандиозные фейерверки, озаряя танцующих."
    Narr_color "Глаза увлажнились. Напружинились мышцы."

    window hide
    $ d4_startype = False
    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)

    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .6
        matrixcolor SaturationMatrix(1.5)
    show day3_jump_sky_forest:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)

    hide snow1_slow onlayer master1
    hide snow2_slow onlayer master1
    hide snow3_slow onlayer master1

    show snow_up_d4_trip onlayer master1

    with Dissolve(.5)

    stop test_five fadeout 6

    play test_two "voice/anton/3day/155 Sm.ogg"
    Narr_color "Я запрокинул голову к луне и закричал от переполняющих меня эмоций."
    voice "voice/Alisa/4day/112 TiScha.ogg"
    Alis_Color "Ты счастлив, Зайчик?"

    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)
        easein 2. zoom .85
    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .6
        matrixcolor SaturationMatrix(1.5)
        easein 2. zoom .9
    show day3_jump_sky_forest:
        align (.5,.5)
        zoom .8
        matrixcolor SaturationMatrix(1.5)
        easein 2. zoom 1.

    pause 1.5
    Narr_color "Я прыгнул до звёзд и кувыркнулся."

    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .85
        matrixcolor SaturationMatrix(1.5)
        block:
            rotate 0
            linear 25 rotate 360
            repeat

    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .9
        matrixcolor SaturationMatrix(1.5)

    show day3_jump_sky_forest:
        align (.5,.5)
        zoom 1.
        matrixcolor SaturationMatrix(1.5)
        block:
            rotate 0
            linear 25 rotate -360
            repeat

    Narr_color "Мой крик слышала вся Небыляндия:"

    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .9
        matrixcolor SaturationMatrix(1.5)
        block:
            ease 4 rotate -180
            ease 4 rotate 0
            repeat

    $ music_during_lines = 1.0
    stop test_two fadeout 0.5
    voice "voice/anton/4day/210. Sha.ogg"
    Ant_Color "Счастлив!"
    stop music2 fadeout 5.5
    play test_seven "sounds/sfx_sparks.ogg"

    show black zorder 100:
        alpha 0.0
        linear 3 alpha 1
    show snow_up_d4_trip onlayer master1:
        alpha 1.0
        pause 1.5
        linear 2.0 alpha 0
    pause 3.
    scene black onlayer master1 with Dissolve(2.0)

    pause 1.




    $ story_manager.MarkEvent(("day4", "scene11"))

    $ renpy.scene("master1")
    scene bg_room_day_close_door_blur
    show Veko_01:
        xpos 0
        ypos -510
        alpha 1.0
        linear 0.8 xpos 0 ypos -1500 alpha 0.0
    show Veko_02:
        xpos 0
        ypos 0
        alpha 1.0
        linear 0.8 xpos 0 ypos 1010 alpha 0.0
    show bg_black:
        alpha 1.0
        linear 0.6 alpha 0.0
    $ renpy.pause(0.7)
    show Veko_01:
        xpos 0
        ypos -1080
        alpha 0.0
        linear 0.2 xpos 0 ypos -140 alpha 1.0
    show Veko_02:
        xpos 0
        ypos 1080
        alpha 0.0
        linear 0.2 xpos 0 ypos -400 alpha 1.0
    show bg_black:
        alpha 0.0
        linear 0.2 alpha 0.9
    $ renpy.pause(0.2)
    show bg room_day_close_door:
        alpha 0.0
        linear 2.5 alpha 1.0
    show Veko_01:
        xpos 0
        ypos -510
        alpha 1.0
        linear 0.3 xpos 0 ypos -1500 alpha 0.0
    show Veko_02:
        xpos 0
        ypos 0
        alpha 1.0
        linear 0.3 xpos 0 ypos 1010 alpha 0.0
    show bg_black:
        alpha 0.9
        linear 0.2 alpha 0.0

    play music "music/11 Empty Road.ogg"

    stop test_four fadeout 5
    play fon "sounds/loop_birds_singing.ogg" fadein 2 volume 0.08 loop

    "Я проснулся с улыбкой впервые за долгие дни, проведённые в новом доме."
    "В этот раз счастье не отпускало. И, наслаждаясь им всем телом, я сладостно потянулся."
    "За окном, радуясь яркому январскому солнцу, весело пели красногрудые красавцы-снегири."
    "Их чириканье дарило мне надежду, что однажды лысый лес за окном вновь обратится в райскую кущу, на радость родителям и сестрёнке."

    play test_four "sounds/loop_dog_next_door.ogg" fadein 1 loop

    voice "voice/olya/4day/Hahaha.ogg"
    "Детский топот ног и собачий лай наполнили коридор."
    stop music fadeout 3.5
    window hide

    stop test_four fadeout 1
    play test_one "sounds/knobs_open.ogg"
    play test_three "sounds/sfx_dog_breathing_2.ogg" fadein 1 loop

    show ant_room_door_open_day
    pause 0.5
    scene bg room_day_open_empty with Dissolve(0.5)
    pause 1
    play music2 "music/25_Olya.ogg" volume 0.7
    "Дверь в мою спальню широко распахнулась, обдав меня тёплым ветерком и ароматом свежезаваренного кофе."
    play test_two "sounds/close-door.ogg"   

    play test_one "sounds/loop_footsteps_home_light_one.ogg" fadein 0.4

    scene bg room_day_close_door
    show Olya Zulka m_day 00 good ahead 01
    with Dissolve(0.5)
    show Olya Zulka m_day 00 good ahead 02 with Dissolve(0.25)

    pause .5
    stop test_one fadeout 1

    play test_three "sounds/sfx_dog_breathing_2.ogg" fadein 1 loop
    "На пороге стояла светящаяся от счастья Оля, а в её руках непрерывно ёрзала, виляя хвостом, умилительная Жулька."


    voice "voice/olya/4day/60 To.ogg"
    Oly "Тоша, гляди, гляди! Папа разрешил ей остаться!"
    show Olya Zulka m_day 00 good ahead 01 with Dissolve(0.25)
    "На глазах сестры выступили слёзы радости."
    show Olya Zulka m_day 00 good ahead 01 with Dissolve(0.25)
    show Olya Zulka m_day 00 good ahead 02 with Dissolve(0.25):
        pause .25
        linear .1 yoffset 10
        linear .1 yoffset 0

    stop test_three fadeout 2 
    voice "voice/olya/4day/61Um.ogg"
    Oly "У меня теперь есть собака!"
    show Olya Zulka m_day 00 good ahead 01 with Dissolve(0.25)

    play sound "sounds/sfx_bed_get_up.ogg"

    "От столь потрясающей новости я даже подскочил с кровати."
    play test_one "sounds/steps/Olya-steps-3.ogg"
    show Olya Zulka b_day 00 good ahead 01 with Dissolve(0.5)
    play test_three "sounds/sfx_dog_breathing_2.ogg" fadein 1 loop
    voice "voice/anton/4day/211. Da.ogg"
    Ant "Да ведь это же Жулька!"
    show Olya Zulka b_day 00 good ahead 01 with Dissolve(0.25)
    show Olya Zulka b_day 00 anger ahead 04 with Dissolve(0.25)
    voice "voice/olya/4day/62 S.ogg"
    Oly "Сам ты Жулька! Её зовут Принцесса."
    show Olya Zulka b_day 00 anger ahead 03 with Dissolve(0.25)
    show Olya Zulka b_day 00 good ahead 02 with Dissolve(0.25)
    voice "voice/olya/4day/63 Da.ogg"
    Oly "Да, Ваше высочество?"
    play test_one "sounds/steps/Olya-steps-5.ogg"
    show Olya Zulka m_day 00 good ahead 01 with Dissolve(0.25):
        yoffset 30
        xoffset 500

    play sound "sounds/sfx_dog_bark_light.ogg"

    "Собака одобрительно тявкнула."

    window hide
    play test_one "sounds/knobs_open.ogg"
    show ant_room_door_open_day
    pause 0.5
    scene bg room_day_open_empty
    show Olya Zulka m_day 00 good ahead 01:
        yoffset 30
        xoffset 500
    with Dissolve(0.5)
    window show

    stop test_three fadeout 4

    voice "voice/father/day4/81Tuk.ogg"
    Pap "Тук-тук! Можно к вам?"

    $ renpy.music.set_pan(-0.3, delay=0, channel="test_two")
    play test_two "sounds/loop_footsteps_home_normal_two.ogg" fadein 0.3 loop

    show Dad Happy m_day 00 norm ahead:
        xpos 550
        yoffset 75
    show Mom Normal m_day 04 norm ahead:
        yoffset 75
    with Dissolve(0.25)
    pause 1.2

    stop test_two fadeout 0.5

    "К моей полной неожиданности, улыбающийся папа переступил порог и, что более удивительно, в обнимку с мамой."
    voice "voice/father/day4/82 Kak.ogg"
    Pap "Как тебе пополнение?"
    voice "voice/father/day4/83 Mn.ogg"
    Pap "Мне эта дурёха под колёса бросилась, еле вырулил."
    voice "voice/father/day4/84M.ogg"
    Pap "Машину поцарапал. Думал, голыми руками удавлю."
    voice "voice/father/day4/84 A.ogg"
    Pap "А заглянул ей в глаза... Они такие... Как бы сказать..."
    voice "voice/karina/4day/131 Um.ogg"
    Mam "...умные." id d4_beasts_choice_take_devend_abab32c6
    voice "voice/father/day4/85 Vo.ogg"
    Pap "Во! А сама дрожит вся."

    show Olya Zulka m_day 00 anger ahead 03 with Dissolve(.25)
    voice "voice/father/day4/85 Nu.ogg" 
    Pap "Ну, говорю, ладно: доедешь со мной до дома и сиденье не обгадишь — тогда оставайся."

    show Olya Zulka m_day 00 anger ahead 04 with Dissolve(.25)
    voice "voice/olya/4day/64 Pr.ogg"
    Oly "Принцессы не гадют!"
    show Olya Zulka m_day 00 anger ahead 03 with Dissolve(.25)

    show Dad Happy m_day 00 norm ahead:
        xpos 550
        yoffset 75
        block:
            linear .3 yoffset 85
            linear .3 yoffset 75
            linear .3 yoffset 90
            linear .3 yoffset 75
            repeat
    show Mom Normal m_day 04 norm ahead:
        yoffset 75
        block:
            linear .21 yoffset 85
            linear .22 yoffset 75
            linear .21 yoffset 90
            linear .22 yoffset 75
            repeat
    show Olya Zulka m_day 00 anger ahead 03:
        parallel:
            "Olya Zulka m_day 00 good ahead 01" with Dissolve(.25)
        parallel:
            linear .16 yoffset 35
            linear .16 yoffset 30
            linear .16 yoffset 45
            linear .16 yoffset 30
            repeat
    play test_six "voice/olya/4day/Wahaha.ogg"
    "Мы дружно засмеялись, точно как раньше, когда любая незначительная мелочь могла рассмешить в два счёта."

    show Dad Happy m_day 00 norm ahead:
        xpos 550
        linear .1 yoffset 75
    show Mom Normal m_day 04 norm ahead:
        linear .1 yoffset 75
    show Olya Zulka m_day 00 good ahead 01:
        xoffset 500
        linear .1 yoffset 30

    voice "voice/karina/4day/133 Che.ogg"
    Mam "Чего замолчал? Давай, продолжай."
    show Mom Normal m_day 04 norm aside with Dissolve(0.25)
    "Мама хитро посмотрела на папу. Тот, покраснев, отвёл взгляд. Словно дети, ей-богу."
    voice "voice/father/day4/87 A.ogg"
    Pap "А ещё из хороших новостей: ваш папа получил повышение."
    show Dad Normal m_day 01 norm aside with Dissolve(0.25)
    voice "voice/father/day4/88 Gre.ogg"
    Pap "Грешно, конечно, радоваться, ведь старший бухгалтер пропал всё-таки."
    show Dad Happy m_day 00 norm ahead with Dissolve(0.25)
    voice "voice/father/day4/88 No.ogg"
    Pap "Но, как говорится, нет худа без добра."
    voice "voice/anton/4day/213. Eto.ogg"
    Ant "Это значит, тебя чаще не будет дома?"
    show Mom Normal m_day 04 norm ahead with Dissolve(0.25)
    voice "voice/karina/4day/134 Eto.ogg"
    Mam "Это значит двойную надбавку плюс премии."
    voice "voice/father/day4/89 Pra.ogg"
    Pap "Правильно, Карина!"
    voice "voice/father/day4/89 Ta.ogg"
    Pap "Так что готовьтесь: на следующей неделе нас всех ждёт семейное путешествие."
    "От этих слов моё сердце забилось сильнее."
    voice "voice/anton/4day/214. Kuda.ogg"
    Ant "К-куда?"
    show Olya Amaze m_day 00 good 01 ahead with Dissolve(0.25):
        yoffset 30
        xoffset 500

    play sound "sounds/sfx_dog_land.ogg"

    "Оля даже выпустила дворняжку из крепких объятий."
    show Olya Amaze m_day 00 good ahead 01
    with Dissolve(0.25)
    show Olya Amaze m_day 00 good ahead 06 with Dissolve(0.25)
    show Mom Normal m_day 04 norm aside with Dissolve(0.25)
    voice "voice/olya/4day/66 Neu.ogg"
    Oly "Ах! Неужели в «Макдоналдс»?"
    show Olya Amaze m_day 00 good ahead 01 with Dissolve(0.25)
    show Dad Normal m_day 01 norm aside with Dissolve(0.25)
    voice "voice/father/day4/90 S.ogg"
    Pap "Скажешь тоже, Оль."

    show Dad Happy m_day 00 norm ahead with Dissolve(0.25)
    voice "voice/father/day4/90 Mi.ogg"
    Pap "Бери выше! Мы давно уже планировали эту поездку, да всё не получалось."
    voice "voice/karina/4day/135 Ve.ogg"
    Mam "Вы уж простите нас, ребятки."
    "Мама кулачком смахнула слезу."
    show Dad Normal m_day 01 norm aside with Dissolve(0.25)
    stop music2 fadeout 3.5
    voice "voice/father/day4/90Da.ogg"
    Pap "Да ладно тебе, Карин. Всё в прошлом."
    show Mom Normal m_day 04 norm ahead with Dissolve(0.25)
    play music "music/This Is The End.ogg" fadein 2

    show layer master:
        align (.5, .2)
        linear .5 zoom 1.05
    show Dad Happy m_day 00 norm ahead with Dissolve(0.25)
    voice "voice/father/day4/91 V.ogg" 
    Pap "В общем, собирайте чемоданы, — летим в «Диснейленд»!"

    play test_six "sounds/loop_dog_small_barking.ogg" fadein 1 loop
    "От радости мы с сестрой запрыгали до потолка. К нам присоединилась раззадоренная громкими речами собачонка."

    show Olya Happy m_day 00 good ahead 07:
        yoffset 20
        xoffset 500
        linear .15 yoffset 0
        linear .15 yoffset 30
    play test_six "voice/olya/4day/67 Ura.ogg"
    AntOly "Ура!"
    play test_five "sounds/loop_jumping_carpet_two.ogg" fadein 1 loop

    show Olya Happy m_day 00 good ahead 08 with Dissolve(.15)
    show Olya Happy m_day 00 good ahead 07 with Dissolve(.15)

    show layer master:
        align (.5, .2)
        zoom 1.05
        block:
            linear .20 yalign 0.0
            linear .20 yalign 1.0
            .25
            repeat
    show Olya Happy m_day 00 good ahead 07:
        yoffset 20
        xoffset 500
        block:
            linear .15 yoffset 0
            linear .15 yoffset 30
            .25
            repeat
    play test_six "voice/olya/4day/68 Dis.ogg"
    AntOly "«Диснейленд»! «Диснейленд»!"

    stop test_five fadeout 1.2
    stop test_six fadeout 1.2
    pause .6

    scene bg house_day_no_voron with Dissolve(0.75)

    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 2

    play test_six "voice/olya/4day/Wahaha.ogg"
    "Наш восторженный визг целиком заполнил дом, пронёсся по чердаку и водосточной трубе, облетел двор и скрылся в сверкающем белизной лесу."
    "А вместе с ним ушло и страшное слово на букву «р»."
    show bg_house_night:
        alpha 0
        linear 2 alpha 1
    "Я поклялся, что навсегда запомню этот день, когда с родителей наконец-то спали маски пренебрежения, а под ними оказались лица людей, которых мы всегда знали и любили."
    stop music fadeout 3.5 



    scene bg_black with Dissolve(1)
    pause .7
    scene bg_road_wood with Dissolve(.5):
        xpos 0
        subpixel True
        linear 10 xpos -520

    play test_one "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop


    play music2 "music/Waltz.ogg" fadein 2.5
    $ renpy.music.set_volume(1.5, 2.5, channel="music2")
    "Лилия Павловна всё ещё не вернулась в школу из-за пропажи Кати, поэтому сегодня я выспался и шёл засветло только к третьему уроку."

    scene road_day with Dissolve(.5):
        xalign .5
        yalign .5
        zoom 1.10
    "Проложенная тропинка вела к чернеющим домикам на фоне белоснежной равнины, где из дымоходов уже валил сизый дым, пахнущий берёзовыми и сосновыми поленьями."
    "Крепкий ночной мороз окончательно спал, задремав под солнечными лучами, и на белых шапках крыш заиграли ледяные искры."

    stop test_one fadeout 1

    "Я остановился, уверенный, что сегодня никто не в силах испортить моё настроение."

    if ROUTE_SOLO or ROUTE_POLINA:
        "Ни мой персональный мучитель Пятифанов, ни его гадкий прихвостень Бяша."
        "Ни сверкающий нож, грозивший вспороть мне брюхо, как дохлой рыбе."

    if ROUTE_SOLO:
        "Даже пренебрежение и жалость, с которыми на меня порой смотрела Полина, словно остались в прошлом. Забылись, как дурной сон."

    if ROUTE_FOX:
        "Ни грусти, ни жалости к себе из-за Полины, которая наверняка уже вовсю делилась с Ромкой грандиозными планами покорения Вены."

    "Всё кануло в небытие."

    play sound "sounds/sfx_moo_distant.ogg"

    "Откуда-то протяжно замычала корова."
    "Я выпал из секундной неги и двинулся дальше, хрустя снежной периной под подошвами."
    play test_one "sounds/loop_footsteps_snow_normal.ogg"
    "Высоко над головой плыли косматые облака, в чьих очертаниях угадывались милые сердцу силуэты зверят."
    stop test_one fadeout 0.5

    play sound "sounds/sfx_snowball_head_hit.ogg"

    scene snowball_corner_Polina with hpunch

    play test_six "voice/Polina/4day/177 Hiha.ogg"
    "Внезапно мне на голову приземлился пушистый снежок, и девичий смех, напоминающий звон колокольчика на весеннем ветру, коснулся моих ушей."
    play test_six "voice/Polina/4day/177 Hiha2.ogg"
    "Я обернулся в ожидании увидеть её, мою дорогую проводницу в сказочный мир грёз — горячо любимую и обожаемую Алису."
    play test_one "sounds/sfx_coat_rustle_1.ogg"

    window show
    scene d4_road:
        xalign .5
        yalign .75
    show mini_Polina
    with Dissolve(0.3)
    $ renpy.music.set_volume(1.0, 3.0, channel="music2")
    "Но вместо девочки-лисицы на протоптанной дорожке позади стояла Полина с неизменным скрипичным футляром в руке."

    play test_one "sounds/loop_footsteps_snow_slow_light.ogg" fadein 0.2 loop

    pause .6
    hide mini_Polina
    show Polina 3_4 m_day_winter 01 norm ahead 01:
        xpos 100
        yoffset 75
    with Dissolve(.5)
    show Polina 3_4 m_day_winter 01 norm ahead 03 with Dissolve(.25)

    stop test_one fadeout 0.6

    $ story_manager.MarkEvent(("day4", "scene12"))

    voice "voice/Polina/4day/178 Op.ogg"
    Pol "Опять, Петров, ворон считаешь."

    play test_one "sounds/loop_footsteps_snow_fast.ogg" fadein 0.2 loop

    show Polina Front b_day_winter 01 smile ahead 014 with Dissolve(.25):
        xpos 0
        ypos -75
    show Polina Front b_day_winter 01 smile2 ahead 014 with Dissolve(.25)
    show Polina Front b_day_winter 01 smile ahead 04 with Dissolve(.25)

    stop test_one fadeout 0.6
    play sound "sounds/sfx_hugs_strike.ogg"

    play test_six "voice/Polina/4day/177 Hiha3.ogg" 
    "Она заразительно засмеялась и, подбежав, вдруг бросилась мне на шею. Я опешил, утонув в сладком аромате её духов."

    play sound "sounds/sfx_hugs.ogg"

    show Polina hugs b_day 01 norm aside 00 with Dissolve(.5):
        xalign .5
        yalign .8
        zoom 1.1

    if Flags.Has("polhouse"):
        "Только вчера я был потрясён её внезапной истерикой, и мне казалось, что лучше держаться от Полины подальше."
        "От её резких, как качели, перепадов настроения, от чудаковатого деда..."
        "Но стоило ей обнять меня, как я сразу позабыл весь кошмар и уже не хотел, чтоб скрипачка меня отпускала."

    voice "voice/anton/4day/216. Chto.ogg"
    Ant "Ч-что с тобой?"
    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    "Она смущённо улыбнулась. Я увидел блеск в её васильковых глазах."
    show Polina hugs b_day 01 happy aside 03 with Dissolve(.25)
    voice "voice/Polina/4day/179 De.ogg"
    Pol "Дедушка мой, он..."
    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    show Polina hugs b_day 01 happy aside 03 with Dissolve(.25)
    voice "voice/Polina/4day/180 On.ogg"
    Pol "Он снова может ходить, представляешь?"
    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    show Polina hugs b_day 01 happy aside 03 with Dissolve(.25)
    voice "voice/Polina/4day/181 V.ogg"
    Pol "В это даже сельский врач не верил, а он будто назло ему встал и пошёл."
    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    show Polina hugs b_day 01 happy aside 03 with Dissolve(.25)
    voice "voice/Polina/4day/182 O.ogg"
    Pol "О, это самый счастливый день в моей жизни, Антон!"

    play sound "sounds/sfx_coat_rustle_1.ogg"

    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    "Она зарылась лицом в мою грудь, сцепила руки на шее, словно я был для неё больше, чем просто друг."
    "Я взволнованно начал озираться."
    voice "voice/anton/4day/217. Pol.ogg"
    Ant "Полин, э-э-э... Нас могут увидеть."
    show Polina hugs b_day 01 happy aside 02 with Dissolve(.25)
    show Polina hugs b_day 01 happy aside 03 with Dissolve(.25)
    voice "voice/Polina/4day/183 Iz.ogg"
    Pol "Из-за Пятифанова беспокоишься?"
    show Polina hugs b_day 01 norm aside 00 with Dissolve(.25)
    show Polina hugs b_day 01 norm aside 01 with Dissolve(.25)
    voice "voice/Polina/4day/184 B.ogg"
    Pol "Брось ты это дело — его и след простыл."

    play sound "sounds/sfx_coat_rustle.ogg"

    scene d4_road:
        xalign .5
        yalign .75
    show Polina Front b_day_winter 01 norm ahead 04
    with Dissolve(.5)
    "Я недоверчиво отодвинул Полину, пытаясь понять, розыгрыш это или правда."
    show Polina Front b_day_winter 01 sad ahead 04 with Dissolve(.25)
    show Polina Front b_day_winter 01 sad ahead 011 with Dissolve(.25)
    voice "voice/Polina/4day/185 Nu.ogg"
    Pol "Ну ты чего, не веришь, что ли?"
    show Polina Front b_day_winter 01 sad ahead 04 with Dissolve(.25)
    show Polina Front b_day_winter 01 sad ahead 011 with Dissolve(.25)
    voice "voice/Polina/4day/186 K.ogg"
    Pol "К нам вчера буквально ночью старший лейтенант Тихонов приезжал."
    show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)
    show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(.25)
    voice "voice/Polina/4day/187 T.ogg"
    Pol "Так и так, Бяша потерялся, а вместе с ним и дружок его Ромка."

    play sound "sounds/sfx_skiing_by.ogg"

    show Polina Front b_day_winter 01 norm aside 04 with Dissolve(.25)
    "Мимо нас прямиком в зимний лес прокатили лыжники."
    show Polina Front b_day_winter 02 norm aside 04 with Dissolve(.25)
    play test_one "sounds/steps/step_snow1.ogg" 
    show Polina Front b_day_winter 02 norm aside 04:
        yalign .5
        parallel:
            linear .25 zoom 1.1 xoffset 50
        parallel:
            linear .15 yoffset -10
            linear .10 yoffset 0
    "Полина склонилась ко мне поделиться шепотком, не выпуская спортсменов из виду."
    show Polina Front b_day_winter 02 norm aside 04 with Dissolve(.25)
    show Polina Front b_day_winter 02 norm aside 011 with Dissolve(.25)
    $ music_general_volume = 0.5
    $ renpy.music.set_volume(0.5, 1.0, channel="music2")
    voice "voice/Polina/4day/188 K.ogg"
    Pol "Как я поняла, во всех этих исчезновениях Тихонов подозревает Пятифанова."
    show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)

    scene road_day
    show day3_cornermeet_fence_anton
    with Dissolve(.5)

    show d4_anton_rot with Dissolve(.25)
    voice "voice/anton/4day/218. Da.ogg"
    Ant "Да ладно!"
    hide d4_anton_rot with Dissolve(.25)

    hide day3_cornermeet_fence_anton
    show d4_anton_serious
    with Dissolve(.5)

    voice "voice/Polina/4day/189 Ya.ogg"
    Pol "Я сама в шоке."
    voice "voice/Polina/4day/190 po.ogg"
    Pol "По слухам, у Ромки того, совсем шарики за ролики заехали."
    voice "voice/Polina/4day/191 Da.ogg"
    Pol "Да я, в принципе, и не удивлена..."
    show d4_anton_rot with Dissolve(.25)
    voice "voice/anton/4day/219. Cto.ogg"
    Ant "Что ты имеешь в виду?"
    hide d4_anton_rot with Dissolve(.25)
    voice "voice/Polina/4day/192 A.ogg"
    Pol "А ты не знал? Он из проблемной семьи."
    voice "voice/Polina/4day/193 D.ogg"
    Pol "Даже думать не хочу, что творилось у них дома."
    $ music_general_volume = 1.0
    $ renpy.music.set_volume(1.0, 4.5, channel="music2")
    "Ромка всегда казался мне чрезмерно жестоким, без повода озлобленным на всех подряд."
    "Теперь чернота, что была у него внутри, выплеснулась через край и загубила множество невинных детских душ, даже его собственную."
    "В это было сложно поверить, но, глядя на Ромку, я чувствовал, что приблизительно так всё и кончится."

    scene d4_road:
        xalign .5
        yalign .75
    show Polina Front b_day_winter 01 norm ahead 04
    with Dissolve(.5)

    if not Flags.Has("mask") and Flags.Has("day2 fox") and not Flags.Has("betray"):

        show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(.25)
        voice "voice/Polina/4day/194 V.ogg"
        Pol "Вот, а ты ещё мне его сватал."
        show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)
        show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(.25)
        voice "voice/Polina/4day/195 K.ogg"
        Pol "Как вспомню... Бр-р-р!"
        show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)
        voice "voice/anton/4day/220. Proste.ogg"
        Ant "Прости, пожалуйста."
        "Она махнула рукой и улыбнулась."
        show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(.25)
        voice "voice/Polina/4day/196 K.ogg"
        Pol "Кто старое помянет..."
        show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)

        show Polina Front b_day_winter 01 norm ahead 05
        show doggy_pol 02
        with Dissolve(.15)

        show Polina Front b_day_winter 01 norm ahead 06
        show doggy_pol 03
        with Dissolve(.15)

        show Polina Front b_day_winter 01 norm ahead 07
        show doggy_pol 04
        with Dissolve(.15)

        pause .25

        show Polina Front b_day_winter 01 norm ahead 014 with Dissolve(.25)
        voice "voice/Polina/4day/197 Vo.ogg"
        Pol "Вот бы ещё и бездомные дворняги тоже исчезли."
        show Polina Front b_day_winter 01 norm ahead 07 with Dissolve(.25)
        show Polina Front b_day_winter 01 norm ahead 014 with Dissolve(.25)
        voice "voice/Polina/4day/198 Ne.ogg"
        Pol "Не жизнь была б, а песня."
        show Polina Front b_day_winter 01 norm ahead 07 with Dissolve(.25)

        scene road_day
        show Ant Cho b_day 00 norm ahead 01
        with Dissolve(.5)

        show Ant Cho b_day 00 what ahead 01 with Dissolve(.25)
        "Я с подозрением взглянул на Полину."

        scene d4_road:
            xalign .5
            yalign .75
        show Polina Front b_day_winter 01 smile2 ahead 04:
            align (.5, .5)
            zoom 1.05
        with Dissolve(.5)

        show Polina Front b_day_winter 01 smile2 ahead 014 with Dissolve(.25)
        show Polina Front b_day_winter 01 smile2 ahead 014:
            block:
                linear .2 yoffset 10
                linear .2 yoffset 0
                linear .2 yoffset 15
                linear .2 yoffset 0
                repeat
        voice "voice/Polina/4day/199 Da.ogg"
        Pol "Ха-ха! Да шучу я!"
        show Polina Front b_day_winter 01 smile2 ahead 04 with Dissolve(.25)


    show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(.25):
        linear .2 yoffset 0
    voice "voice/Polina/4day/200 Po.ogg"
    Pol "Пойдём скорее, а то опоздаем."
    $ renpy.music.set_volume(1.8, 4.0, channel="music2")
    show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(.25)
    show Polina Back big
    with Dissolve(.25)

    play test_three "sounds/sfx_coat_rustle_1.ogg"  
    play test_six "voice/Polina/4day/177 Hiha4.ogg" 
    "Полина схватила мою ладонь и, весело смеясь, побежала по просёлочной дороге."
    play test_one "sounds/loop_footsteps_snow_fast.ogg" fadein 0.6 loop

    play test_four "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 0.6 volume 0.4 loop

    hide Polina Back big
    show Polina_back_day_4:
        align (.5, 1.)
        xoffset -100
        zoom 1.1
        linear .5 zoom 1.
    show anton_sp_05:
        align (.5, 1.)
        xoffset 300
        zoom 1.1
        linear .5 zoom 1.
    show d4_road:
        xalign .5
        yalign .75
        linear .5 yoffset 10 zoom 1.1
    with Dissolve(.5)
    "И с каждым шагом, с каждым смешком и шуткой позабытое тепло обволакивало моё сердце."

    scene bg school_day:
        yalign 0.8 xalign 0.5
        easein 1.5 zoom 1.1
    with Dissolve(.5)
    "Всеобъемлющая влюблённость вернулась ко мне, и казалось, что уже никогда меня не покинет."

    stop fon fadeout 2
    stop test_one fadeout 1
    stop test_four fadeout 1
    play sound "sounds/school_door-open-1.ogg"

    pause .5

    play test_one "sounds/loop_footsteps_class_normal.ogg" fadein 1 loop
    play test_two "sounds/loop_footsteps_home_normal_one.ogg" fadein 1 loop

    scene bg_koridorchic_day_02:
        xalign 0.05
        easein 1.5 xalign .0
    with Dissolve(.5)
    "Перед входом в класс я попытался отпустить руку Полины, стесняясь, что одноклассники будут дразнить нас женихом и невестой."

    play sound "sounds/Door_open_2.ogg"

    scene bg_koridorchic_day_02:
        xalign .0
    show d4_hall_door:
        xalign .0
    with Dissolve(.5)
    "Но Полине было словно всё равно, и она только сильнее сжала мою ладонь, отворяя дверь."

    stop test_one fadeout 1.2
    stop test_two fadeout 1.2


    scene classroom_day_bg
    show d4_class_classmates_1
    with Dissolve(.5)
    "И действительно: избавившись от коварной Катьки, бессердечного Ромки и ехидного Бяши, наш класс словно бы излечился от паразитов, стал дружелюбнее и отзывчивее."
    "Никто больше не смотрел на меня залитыми злобой глазами, некому было харкнуть в меня кусочком жёваной бумажки через полый корпус шариковой ручки."

    scene ant_clas_fon:
        align (.5,.5)
    with Dissolve(.5)

    play sound "sounds/sfx_Anton_sit.ogg"

    show anton_class:
        xoffset -400
        xzoom -1
        zoom .9
        align (.5, 1.)
    with Dissolve(.5)

    "Я сел за свою одинокую парту, когда рядом уселась Полина. Меня это нисколько не удивило."
    play sound "sounds/sfx_Polina_sit.ogg"

    show Polina Front b_day 00 norm ahead 01:
        xoffset 400
        yoffset 100
        xzoom -1
    with Dissolve(.5)

    show ant_clas_blink_1:
        xoffset -400
        xzoom -1
        zoom .9
        align (.5, 1.)
    show ant_clas_m6:
        xoffset -400
        xzoom -1
        zoom .9
        align (.5, 1.)
    with Dissolve(.5)
    "Она была такой очаровательной, что я мог бы назвать её своей музой."

    play sound "sounds/sfx_bag_take_notebook.ogg"
    pause .6

    scene bg parta
    with Dissolve(.5)
    show d4_album_bg

    show d4_album 2
    with Dissolve(.5)
    "Подхваченный волной вдохновения, я вытащил из рюкзака альбом для рисования."
    play test_three "sounds/sfx_coat_rustle_1.ogg"   

    scene d4_model_fon:
        xalign 1.
        linear 1 xalign 0.
    show Polina Large b_day 01 norm ahead 01:
        xoffset -1920
        linear 1 xoffset -300
    with Dissolve(.5)
    "Облизнул грифель карандаша, не выпуская из поля зрения свою модель."

    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    $ renpy.music.set_volume(1.0, 2.0, channel="music2")
    "Она вновь улыбнулась мне."
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/201 Ch.ogg"
    Pol "Что ты задумал?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)

    scene d4_model_fon:
        xalign 0.
        linear 1. xalign 1.
    show Polina Large b_day 01 norm ahead 03:
        xoffset -300
        linear 1 xoffset -1920
    pause .5
    scene bg parta
    show d4_album_bg
    with Dissolve(.5)
    voice "voice/anton/4day/221. Spok.ogg"
    Ant "Спокойствие! Работает профессионал."

    play sound "sounds/sfx_drawing_Polina_1.ogg"

    $ story_manager.MarkEvent(("day4", "scene13"))

    show d4_album 3 with tetrad_dissolve
    "Я наметил будущие контуры обворожительного силуэта."

    play sound "sounds/sfx_drawing_Polina_2.ogg"

    show d4_album 4 with tetrad_dissolve
    voice "voice/anton/4day/222. Znae.ogg"
    Ant "Знаешь, я часто наблюдал за тобой отсюда."
    play test_three "sounds/sfx_coat_rustle_1.ogg"   

    scene d4_model_fon:
        xalign .5
        linear .5 xalign 0.
    show Polina Large b_day 01 norm ahead 03:
        xoffset -1110
        linear .5 xoffset -300
    with Dissolve(.25)
    "Она бросила взгляд на свою бывшую парту. Смущённо убрала за ушко локон."

    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/202 P.ogg"
    Pol "Правда?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)

    scene d4_model_fon:
        xalign .0
        linear .5 xalign .5
    show Polina Large b_day 01 norm ahead 03:
        xoffset -300
        linear .5 xoffset -1110
    pause .25
    scene bg parta
    show d4_album_bg
    show d4_album 4
    with Dissolve(.25)
    "Несколькими широкими линиями я обозначил миленькие скулы."

    play sound "sounds/sfx_drawing_Polina_3.ogg"

    show d4_album 5 with tetrad_dissolve
    "Мне никогда ещё не удавалось с такой точностью взять пропорции чьего-либо лица."
    voice "voice/anton/4day/223. Po.ogg"
    Ant "Полина..."

    scene d4_model_fon:
        xalign .0
    show Polina Large b_day 01 norm ahead 03:
        xoffset -300
    with Dissolve(.25)
    show Polina Large b_day 01 norm ahead 04 with Dissolve(.15)
    voice "voice/Polina/4day/203 Cht.ogg"
    Pol "Что, Антон?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.15)
    "Она замерла, боясь неверным движением помешать мне, развеять волшебство."

    scene bg parta
    show d4_album_bg
    show d4_album 5
    with Dissolve(.25)

    play sound "sounds/sfx_drawing_stroking_1.ogg"

    show d4_album 6 with tetrad_dissolve
    voice "voice/anton/4day/244.Na.ogg"
    Ant "Наклонись, пожалуйста, сюда."
    voice "voice/anton/4day/244.Vot.ogg"
    Ant "Вот так, да. Хорошо."

    scene d4_model_fon:
        xalign .0
    show Polina Large b_day 01 norm ahead 03:
        xoffset -300
    with Dissolve(.25)

    play sound "sounds/sfx_shirt_unbutton.ogg"

    show Polina Large b_day 06 norm ahead 03 with Dissolve(.5)
    show Polina Large b_day 07 norm ahead 03 with Dissolve(.5)
    play test_six "voice/Polina/4day/204 Za.ogg" 
    "Задыхаясь от волнения, Полина расслабила узелок шейного платка."
    voice "voice/anton/4day/225. Yav.ogg"
    Ant "Я всегда хотел тебя... нарисовать."
    "Наши глаза встретились."

    scene bg parta
    show d4_album_bg
    show d4_album 6
    with Dissolve(.25)

    play sound "sounds/sfx_drawing_Polina_1.ogg"

    show d4_album 7 with tetrad_dissolve
    voice "voice/Polina/4day/205 O.ogg"
    Pol "О, Антон."

    play sound "sounds/sfx_drawing_stroking_1.ogg"

    show d4_album 8 with tetrad_dissolve
    "Карандаш носился над бумагой, яростно штрихуя тени на её груди."
    voice "voice/anton/4day/226. Ska.ogg"
    Ant "Скажи, ты согласна стать героиней моего комикса?"

    scene d4_model_fon:
        xalign .0
    show Polina Large b_day 07 norm ahead 03:
        xoffset -300
    with Dissolve(.25)
    show Polina Large b_day 07 soulful ahead 10 with Dissolve(.5)
    show Polina Large b_day 07 soulful ahead 10:
        subpixel True
        linear .03 xoffset 1-300
        linear .03 xoffset -1-300
        repeat 4
        linear .03 xoffset 0-300
    "Сладкая дрожь пробежала по её телу. Она томно закатила глаза от удовольствия."
    show Polina Large b_day 07 soulful ahead 09 with Dissolve(.15)
    voice "voice/Polina/4day/206 Da.ogg"
    Pol "Да! Да!"
    show Polina Large b_day 07 soulful ahead 08 with Dissolve(.15)
    show Polina Large b_day 07 soulful ahead 09 with Dissolve(.15)
    voice "voice/Polina/4day/207 K.ogg"
    Pol "Как долго я ждала этих слов, милый!"


label d4_wake_up:
    $ story_manager.MarkEvent(("day4", "scene14"))
    jump d4_wake_up.devend
    label d4_wake_up.dev hide:
    label d4_wake_up.devend:


    scene d4_grafit_bg
    show d4_grafit_hand:
        align (.65, .0)
        yoffset -25
    show d4_grafit_grafit_ok:
        yoffset -25
    with Dissolve(.25)

    stop music2 fadeout 2.5
    "От напряжения грифель карандаша не выдержал и, щёлкнув, разлетелся на мелкие осколки."


    $ achievement_grant("ach_Haide")

    scene d4_grafit_bg
    show d4_grafit_hand:
        align (.65, .0)
        yoffset -25
        transform_anchor True
        rotate -2.0
        subpixel True
        easein 10 yoffset -20 xoffset 20
    show d4_grafit_spot
    show d4_grafit_grafit_broken:
        subpixel True
        easein 10 xoffset -50 yoffset -75
    show d4_grafit_fragments:
        align (.35, .65)
        subpixel True
        easein 10 zoom 1.2
    show layer master:
        align (.5, .5)
        zoom 1.01
        block:
            linear .03 yoffset -5
            linear .03 yoffset 5
            repeat 2
        linear .03 yoffset 0

    stop fon fadeout 2
    play sound "sounds/sfx_break_pencil.ogg"
    play test_one "sounds/roll-hit-1.ogg"
    "Я не мог поверить, глядя на рисунок."
    stop music2 fadeout 2.5
    stop music fadeout 2.5

    scene d4_mess_def:
        align (.5, .5)
        .5
        parallel:
            linear 6.54 zoom 1.3
        parallel:
            1.
            block:
                linear .03 xoffset 5 yoffset 5
                linear .03 xoffset -5 yoffset -5
                repeat 3
            repeat 5

    show bg_black:
        alpha 0

        2.
        block:
            alpha .5
            .1
            alpha .0
            .1
            repeat 2

        1.5
        block:
            alpha .5
            .07
            alpha .0
            .07
            repeat 6

        1.
        block:
            alpha .5
            .04
            alpha .0
            .04
            repeat 10

        alpha .7

    with Dissolve(.1)

    play test_six "music/Phrases_05.ogg" 
    play music2 "music/some_ambient.ogg"
    $ music_during_lines = 1.0
    "Ужасная мазня смотрела на меня. Там, где секунду назад было лицо Полины, сейчас красовалось бесформенное месиво."
    "..."

    play test_one "sounds/loop_nightmare_ambience.ogg" fadein 2 loop

    scene d4_classroom_night_bg:
        xalign 0.
        linear 15 xalign 1.
    show d4_classroom_night_word:
        xalign 0.
        linear 15 xalign 1.


    show d4_dust_wide:
        xpos 0
        alpha .5
        linear 15 xpos -3911+1920
    with Dissolve(.5)
    play test_two "voice/anton/4day/227. A.ogg"
    "Я не сразу понял, что сижу за партой в пустом классе."
    play test_two "voice/anton/4day/227.aa.ogg"
    "Пылинки летали в лунном свете."
    "За окном была ночь, и куда-то подевались одноклассники, Полина, ощущение эйфории."
    "На доске кто-то написал мелом считалочку, но стёр часть слов, и читалось лишь:"
    "раз-два..."
    "...Зайчик..." id d4_wake_up_devend_fa6b925e
    "...мясо..." id d4_wake_up_devend_61ff1306
    "Дурацкая ухмылка сползла с моих губ."
    "Я встал, ущипнув себя за запястье. Тишина была оглушительной."
    "Во рту стоял привкус блевоты, а в ушах звенело, как от нескончаемого вопля, полного отчаянья и ужаса."
    play test_three "sounds/steps/Podoshe_2.ogg"

    play test_two "sounds/loop_lamp_blinking.ogg" fadein 2 loop

    scene d4_khoridor_night_bg:
        xalign 0.
    show d4_khoridor_night_door:
        xalign 0.
    show d4_dust_wide2:
        xpos 0
        alpha .7

    with Dissolve(1.)
    show d4_fonari_blink
    voice "voice/anton/4day/228. Ei.ogg"
    Ant "Эй? Кто-нибудь?"

    hide d4_khoridor_night_door with Dissolve(.5)
    "В коридоре роились тени."

    play test_three "sounds/loop_footsteps_class_normal.ogg" fadein 1 loop

    show d4_khoridor_night_bg:
        linear 15 xalign 1.
    show d4_dust_wide2:
        xpos 0
        alpha .7
        linear 15 xpos -4239+1920
    "Я шёл мимо заколоченных классов, мимо пятен гнили на стенах и серебристой паутины."
    "Пауки быстро перемещались под потолком."
    "Лампы тревожно мерцали."
    stop test_three fadeout 1.2

    show d4_khoridor_night_bg:
        xalign 1.
    with Dissolve(.5)
    "Ошеломлённый, я встал напротив доски объявлений."
    "К портретам Семёна и Кати добавились сотни других фотографий."
    "Чёрно-белые распечатки клеили одну поверх другой. Жуткий коллаж из детских лиц глядел провалами глаз."

    stop test_two fadeout 2



    show bg_black with Dissolve(.5)
    "Не в силах выносить пытку этих внимательных дыр, я выбежал из школы."
    play test_two "sounds/Anton-school-run-1.ogg"

    window hide

    pause .8
    stop test_three fadeout 1

    scene d4_school_night
    show snow_day_4 onlayer master1:
        xzoom -1

        alpha .5
    with Dissolve(.5)
    show d4_fonari_blink_slow

    play fon "sounds/fon/loop_wind_strong_outside.ogg" fadein 1 
    stop music2 fadeout 2
    play music "music/7_nq-mid-amb-4.ogg" fadein 4
    stop test_one fadeout 3.5
    play test_two "sounds/school_door-close-2.ogg"

    pause 2.

    window show

    "По двору – на дорогу, где шуршала пороша."

    window hide

    play test_three "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 1 

    pause .8
    stop test_three fadeout 1

    scene d4_road_night with Dissolve(.5):
        align (.5, 1.)
        zoom .68
        linear 60 zoom 1.

    play test_four "sounds/loop_footsteps_snow_normal.ogg" fadein 1 loop

    pause 2.

    window show


    "Ни людей, ни машин, ни птиц..."
    "Низкие облака задевали дымоходы."
    "Окна словно закрасили чернилами."
    "Фотографии пропавших облепили столбы и заборы бумажной шкурой. Не только детей, но и взрослых."
    "Кажется, все жители посёлка стали чёрно-белыми призраками на снимках с пометкой «РАЗЫСКИВАЕТСЯ»."
    "Я брёл в тишине по умершей улице."
    "В некоторых домах были выбиты стёкла. Ветер хозяйничал, рыская по комнатам."
    "Входные двери качались от его порывов."
    "На штакетинах висели детские курточки, их рукава шевелились, тянулись ко мне."
    "Пустой посёлок. Пустая оболочка."
    "Что здесь случилось?"

    stop test_four fadeout 1.6

    scene d4_selmag_fon_dark:
        xalign 1.
    show d4_selmag_mag_dark:
        xalign 1.
    hide snow_day_4 onlayer master1
    with Dissolve(.5)

    show d4_selmag_shadow:
        xanchor .5
        xpos .35
        yalign 1.
    show d4_selmag_reflect_anton:
        xalign 1.

    with Dissolve(.5)

    play sound "sounds/sfx_dumpster_fall.ogg"

    "В переулке затарахтел, опрокидываясь, мусорный бак."
    play test_seven "voice/anton/2day/fear4.ogg"

    show lv6 chel2 behind d4_selmag_mag_dark:
        xpos 300
        ypos 600
        alpha 1.0
        zoom 0.9
        linear 1. xpos 1920
    "Что-то промелькнуло в оконных проёмах обугленного сельмага."
    play sound "voice/anton/1day/029.Beg i o.ogg"

    play test_four "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 1 loop

    scene d4_selmag_fon_dark:
        xalign 1.
        linear .5 xalign 0.
    show d4_selmag_mag_dark:
        xalign 1.
        linear .5 xalign 0.

    show d4_selmag_shadow:
        xanchor .5
        xpos .35
        yalign 1.
    show d4_selmag_reflect_anton:
        xalign 1.
        alpha 1
        linear .15 alpha 0

    pause .25
    scene d4_road_dark with Dissolve(.25)

    "Я побежал прочь от закопчённого фасада."

    play sound "sounds/sfx_growl_distant.ogg"

    "За колодцем утробно зарычало."
    "Я ускорился, стараясь не замечать тьмы во дворах, в кровавых собачьих будках, в покосившихся сараях."
    "Луна показалась из-за облаков."
    "В изнуряющей тишине что-то пронеслось над головой."

    play sound "sounds/sfx_whoosh.ogg"

    show d4_road_dark_shadow:
        anchor (0., 0.)
        pos (1., 1.)
        linear 1 pos (0., 0.) anchor (1., 1.)
    "Словно кукурузник перелетел с кровли на кровлю. Меня накрыла огромная тень."
    "Я рванул направо в надежде, что меня не заметили."

    scene d4_polhouse_dark with Dissolve(.5)
    "Небольшой зелёный дом впереди — моё убежище."

    play sound "sounds/sfx_gate_slam.ogg"

    if Flags.Has("polhouse"):
        "Сходя с ума от страха, я рванул к ближайшей избе. Вот где я найду убежище!"
        "В глаза не сразу бросилось, что это был дом Полины, где сегодня днём она молила меня в истерике остаться."
    elif not Flags.Has("mask"):
        "Сходя с ума от страха, я рванул к ближайшей избе."

    window hide

    stop test_four fadeout 1.5

    scene d4_polhouse_dark:
        align (.5, .5)
        zoom 1.
        linear 1.0 zoom 1.2
    with None
    pause .25
    show d4_polhouse_door_dark with Dissolve(.5)

    play test_seven "voice/anton/1day/Ah.ogg"
    "Я толкнул калитку и пригнувшись, засеменил к крыльцу."
    stop music fadeout 5.5
    play music2 "music/WF.ogg" fadein 4.5 
    $ music_during_lines = 0.65
    play sound "sounds/sfx_door_Polina_open_fast.ogg"

    scene d4_polhouse_door_dark_bg
    show d4_polhouse_door_dark with None

    pause .6
    play test_five "sounds/loop_wheelchair_next_door.ogg" fadein 3 loop

    hide d4_polhouse_door_dark
    show d4_polhouse_door_dark_anim
    with Dissolve(.25)
    "Дёрнул за ручку. Двери оказались не заперты."

    stop test_five fadeout 1.5
    play sound "sounds/sfx_wheelchair_floor_to_snow.ogg" fadein 2.3

    scene d4_polhouse_door_dark_bg
    show d4_polhouse_door_r
    show d4_polhouse_chair:
        xpos .15
        xanchor .85
        ypos 1.
        yanchor .8
        zoom .75
        parallel:
            linear 5 xpos 1. xanchor .0 yanchor .2 zoom 1.5
        parallel:
            block:
                choice:
                    linear .05 yoffset 5
                    linear .05 yoffset -5
                    linear .05 yoffset 0
                    repeat 2
                choice:
                    linear .05 yoffset 5
                    linear .05 yoffset -5
                    linear .05 yoffset 0
                    repeat 4
                choice:
                    linear .05 yoffset 5
                    linear .05 yoffset -5
                    linear .05 yoffset 0
                    repeat 6

            .1
            repeat
    show d4_polhouse_door_l
    pause 5

    $ story_manager.MarkEvent(("day4", "scene15"))

    window show
    "Инвалидное кресло выехало из темноты, едва не задев меня, покатилось, стуча колёсами по ступенькам, и застыло у яблони."
    "Я проводил его округлившимися глазами. Снова посмотрел в дом."
    "Коридор терялся во мраке. Пустые рамы на стенах. Стекло на полу."
    voice "voice/anton/4day/229. Est.ogg"
    Ant "Есть тут кто?"


    window hide
    hide d4_polhouse_chair with Dissolve(.5)

    scene d4_polhouse_door_dark_bg:
        align (.5, .5)
        linear 1.5 zoom 1.05
    show d4_polhouse_door_dark_002:
        align (.5, .5)
        linear 1.5 zoom 1.2

    pause 1.

    scene d4_polhouse_dark_floor_1 with Dissolve(.5):
        align (.5, .5)
        zoom 1.05

    play sound "sounds/sfx_growl_monster_low_1.ogg"

    "Ответом было рычание."

    play wtf "sounds/sfx_monster_stomp.ogg"

    scene d4_polhouse_dark_floor_2 with vpunch:
        align (.5, .5)
        zoom 1.05
    "Из-за угла в конце коридора высунулась косматая лапа, а следом — страшная морда с горящими глазами."

    scene d4_polhouse_wolf_bg
    show d4_polhouse_wolf:
        anchor (0., .5)
        pos (1., 1.)
        subpixel True
        easein 8 anchor (1., 1.)

        block:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    show d4_polhouse_wolf_fg
    with Dissolve(.5)

    play wtf "sounds/sfx_monster_crawl_heavy.ogg"

    "Огромный разожравшийся зверь выполз на брюхе, извиваясь, как гадюка. Он едва вмещался в коридорное жерло."
    "Протискивался, скобля когтями половицы."

    play test_three ["<silence 0.7>","sounds/sfx_monster_bite_empty.ogg"] noloop

    scene d4_polina_am_clack
    "Челюсти клацнули капканом в сантиметре от моего лица."
    "Чудовище застряло в проходе."

    play test_two "sounds/loop_monster_house_noise.ogg" fadein 1 loop

    scene d4_polyard_full_animation with Dissolve(.5)
    play test_three "voice/Wolf/335 RR.ogg"
    "Лапы били по стенам, слюна брызгала из пасти."

    play test_three "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 0.2 

    scene d4_polyard_bg:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_wolf_animation:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_anton 1:
        align (.5, .5)
        zoom 1.05
        1.
        "d4_polyard_anton 2" with Dissolve(.5)
    with Dissolve(.5)

    pause .8
    stop test_three fadeout 0.5

    "Я развернулся — уносить ноги из кошмара!"

    $ renpy.music.set_volume(0.5, delay=3, channel="test_two")

    play sound "sounds/sfx_owl_monster_land.ogg"
    pause .2

    scene d4_polyard_bg:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_wolf_animation:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_anton 2:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_owl:
        align (.5, .5)
        zoom 1.05
    show d4_polyard_owl_animation:
        align (.5, .5)
        zoom 1.05
    with vpunch

    pause .5


    play test_five "voice/Owl/4day/Uhy.ogg"
    queue sound [ "<silence 1.5>", "<from 0 to 3>sounds/sfx_teeth_clack_3.ogg"]
    "Горбатый филин — крупнее взрослого человека — приземлился у калитки, закрывая дорогу. Клюв щёлкал неустанно."
    stop test_four fadeout 1.5

    play sound "sounds/sfx_burrow.ogg"

    show d4_polyard_snow_animation:
        align (.5, .5)
        zoom 1.05
    pause .5
    show d4_polyard_anton 3 with Dissolve(.5)
    pause 1
    "Сбоку вспучился сугроб, и нечто, похожее на гигантскую землеройку, полезло наружу."

    play sound "sounds/sfx_Romka_fall_snow.ogg"

    play test_three "voice/anton/4day/230. Ah.ogg"
    show d4_polyard_anton 4 with Dissolve(.5)
    "Я упал на колени, словно молился этим древним созданиям."

    stop test_two fadeout 6
    play test_four "sounds/loop_footsteps_monster_snow.ogg" fadein 4 loop

    "Из тёмной норы выползла скалящаяся в улыбке тварь, драпированная грязным лисьим мехом."

    pause 1

    stop test_four fadeout 1.2

    scene d4_polyard_alisa_animation
    with Dissolve(.5)
    play test_seven "voice/Alisa/4day/Ha.ogg"
    "Её хвост — лишь позвоночник в ошмётках сухожилий — волочился сзади."

    $ renpy.music.set_pan(0.5, delay=0, channel="test_one")
    $ renpy.music.set_pan(0.4, delay=0, channel="test_two")
    $ renpy.music.set_volume(1.0, delay=0, channel="test_one")
    $ renpy.music.set_volume(1.0, delay=0, channel="test_two")

    play test_one ["<silence 1.1>","sounds/sfx_footstep_monster_snow_1.ogg"]
    play test_two ["<silence 3.2>","sounds/sfx_footstep_monster_snow_2.ogg"]

    scene d4_monster_sky:
        subpixel True
        align (.5, .5)
        zoom .5
        block:
            ease 120 zoom 1.
            ease 120 zoom .5
            repeat



    show d4_monster_bear_0:
        xpos 642
        ypos -532

        parallel:
            .5
            ease 1 ypos -266 xpos 321
            block:
                linear .02 xoffset 3
                linear .02 xoffset -3
                repeat 2
            1.
            ease 1 ypos 0 xpos 0
            block:
                linear .02 xoffset 3
                linear .02 xoffset -3
                repeat 2

        parallel:
            function WaveShader(amp=4, period=2, speed=.3, direction="both", double="both", melt="both")

    show d4_monster_owl:
        function WaveShader(amp=3, period=3, speed=.3, direction="both", double="both",  melt="both")
    show d4_monster_fox:
        function WaveShader(amp=4, period=2, speed=.4, direction="both", double="both",  melt="both")

    with Dissolve(.5)
    "Тела существ ужасно исказились, и я решил, что схожу с ума."

    $ renpy.music.set_pan(0.0, delay=5, channel="test_one")
    $ renpy.music.set_pan(0.0, delay=5, channel="test_two")




    show d4_monster_bear_0:
        align (.0, .0)
        function WaveShader(amp=4, period=2, speed=.3, direction="both", melt="both")
    show d4_monster_owl:
        align (.0, .0)
        function WaveShader(amp=3, period=3, speed=.3, direction="both", melt="both")
    show d4_monster_fox:
        align (.0, .0)
        function WaveShader(amp=4, period=2, speed=.4, direction="both", melt="both")

    with Dissolve(1.5)
    "Они то казались мне маленькими, размером с ребёнка, то вытягивались выше любой опустевшей избы."
    "Людоеды нависли надо мной, а в их чревах непрерывно что-то копошилось, как будто искало выход наружу."
    "И чем дольше они взирали на меня, тем шире становились их перекошенные улыбки, их лики смерти."

    scene bg_black
    show d4_beast_fox:
        subpixel True
        ypos .7
        yanchor .2
        xalign .5
        parallel:
            linear 5 ypos .3 yanchor .45
        parallel:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    show d4_noise onlayer master1
    with Dissolve(.5)
    voice "voice/Alisa/4day/113 Kak.ogg"
    Alis "Как же славно мы пировали!"

    "Изуродованное чучело лисы облизнулось."
    show d4_beast_fox alter with Dissolve(.5)

    play sound "sounds/sfx_scolopendra.ogg"

    "Язык показался мне чёрной сколопендрой, длиннее моего предплечья."

    play test_one "sounds/sfx_scolopendra_2.ogg"

    show d4_beast_fox with Dissolve(.5)
    show bg_black as fg:
        alpha 0
        linear 1. alpha 1
    "Мерзкое насекомое пробежало между бритвенно-острыми зубами и провалилось в бездонную пасть, способную проглотить весь мир."

    scene bg_black
    show d4_beast_owl:
        subpixel True
        ypos .3
        yanchor .45
        xalign .5
        zoom .85
        matrixcolor BrightnessMatrix(-1.0)
        parallel:
            linear .5 zoom 1.
        parallel:
            easein_quad .25 matrixcolor BrightnessMatrix(0.0)
        parallel:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    voice "voice/Owl/4day/Sladkoe.ogg"
    Owl "Ух-ху-ху, сладкое мясо, сочное мясо."

    scene bg_black with Dissolve(1.5)
    show d4_beast_bear:
        subpixel True
        ypos 1.
        yanchor 1.
        xalign .5
        zoom .9
        matrixcolor BrightnessMatrix(-1.0)
        parallel:
            linear 5 ypos .4 yanchor .5 matrixcolor BrightnessMatrix(0.0)
        parallel:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    with Dissolve(.5)
    $ renpy.pause(4, hard=True)
    voice "voice/Bear/4day/55kak.ogg"
    Bear "Как пожирали, так и будем впредь."

    show d4_beast_bear:
        subpixel True
        ypos .4
        yanchor .5
        xalign .5
        zoom .9
        matrixcolor BrightnessMatrix(0.0)
        parallel:
            linear 3 zoom 1.
            linear 3 zoom .9
            repeat
        parallel:
            ease .15 ypos .3
            ease .15 ypos .4
            repeat
        parallel:
            animation
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    show bg_black as fg:
        alpha 0
        3.
        block:
            linear 3 alpha .6
            linear 3 alpha .0
            repeat
    voice "voice/Bear/4day/56 Vahaha.ogg" 
    Bear "Ба-ха-ха-ха!"
    play test_two "voice/Bear/4day/56 Vahaha.ogg" 
    "В их речи не было ничего человеческого — лишь звериный рык да птичий свист."
    play test_two "voice/Bear/4day/56 Vahaha.ogg"
    "Но я понимал каждое слово, как если бы мы говорили на одном языке."


    scene bg_black with Dissolve(.5)
    hide d4_noise onlayer master1
    show d4_beast_fox_face with Dissolve(.5)
    voice "voice/Alisa/4day/114 Kakzal.ogg"
    Alis "Как жаль, что ты не поспел за нами, Зайчик."
    voice "voice/Alisa/4day/115 Nesm.ogg"
    Alis "Не смог укусить Луну."

    hide d4_beast_fox_face
    show d4_polbeast_talkback_bg
    show d4_polbeast_talkback_anton 1
    with Dissolve(.5)
    voice "voice/anton/4day/Viobedale.ogg"
    Bunny "Вы объедали меня! Предатели! "

    hide d4_polbeast_talkback_bg
    hide d4_polbeast_talkback_anton
    show d4_polyard_alisa_animation
    with Dissolve(.5)
    voice "voice/Alisa/4day/26 T.ogg"
    Alis "Ты сам не захотел есть свою семью."


    hide d4_polyard_alisa_animation
    show d4_polbeast_talkback_bg
    show d4_polbeast_talkback_anton 2
    with Dissolve(.5)

    voice "voice/anton/4day/No.ogg"
    Bunny "Но..."
    show d4_polbeast_talkback_anton 0 with Dissolve(.5)
    pause 1.

    hide d4_polbeast_talkback_bg
    hide d4_polbeast_talkback_anton
    show d4_beast_owl_face
    with Dissolve(.5)
    voice "voice/Owl/4day/Zalk.ogg"
    Owl "Ух-ху-ху, жалкое мясо! Никчёмное мясо!"

    hide d4_beast_owl_face with Dissolve(.5)
    show d4_beast_bear_face with Dissolve(.5)
    voice "voice/Bear/4day/57 Kak.ogg"
    Bear "Как ты ничтожен, братец."
    voice "voice/Bear/4day/58 Men.ogg"
    Bear "Меня от тебя тошнит."

    hide d4_beast_bear_face with Dissolve(.5)
    show d4_beast_wolf_face:
        .05
        zoom 1.1
        .1
        zoom 1.
        block:
            linear .03 xoffset 5
            linear .03 xoffset -5


            repeat 16

        linear .03 xoffset 0


        0.65

        zoom 1.1
        .1
        zoom 1.
        block:
            linear .03 xoffset 5
            linear .03 xoffset -5


            repeat 24

        linear .03 xoffset 0
    voice "voice/Wolf/339 Pzorr.ogg"
    Wolf "Позор-р-р! Позор-р-р!"
    hide d4_beast_wolf_face with Dissolve(.5)

    scene d4_paw_bg
    show d4_paw_fog:
        xpan 0
        alpha .5
        linear 120 xpan 360
        repeat
    show d4_paw_owl_body
    show d4_paw_owl_claw:
        ypos -800
        xpos 400
        subpixel True
        parallel:
            easein_quad 4 ypos -100 xpos 100
        parallel:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat

    show d4_paw_anton_m:
        2.5
        "d4_paw_anton_m_shadow" with ImageDissolve("effect/imagedissolve/shadow/anton02.png", 10, ramplen=128)

    show d4_paw_wolf_claw:
        ypos -800
        xpos -1200
        subpixel True
        1.5
        parallel:
            easein_quad 10 ypos -100 xpos 0
        parallel:
            ease 2. xoffset -10 yoffset 0
            ease 2. xoffset 0 yoffset 10
            ease 2. xoffset 10 yoffset -10
            repeat
    show d4_paw_wolf_body:
        xpos -150
    with Dissolve(.5)
    play test_three "voice/anton/2day/fear3.ogg"
    play test_five "voice/Alisa/sfx_beasts_laugh.ogg"

    "Неописуемый ужас объял меня, когда хохочущие звери потянули ко мне свои когтистые лапы."
    play test_three "voice/anton/2day/fear2.ogg"
    "Как вдруг нечто, притворяющееся лисой, громко залаяло:"

    scene bg_black
    show d4_polyard_alisa_animation
    with Dissolve(.25)
    voice "voice/Alisa/4day/116 Glup.ogg"
    Alis "Глупцы! Его черёд нести угощения."
    hide d4_polyard_alisa_animation with Dissolve(.5)

    show d4_beast_wolf_face with Dissolve(.5):
        .5
        block:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat 8
    voice "voice/Wolf/341 Darmo.ogg"
    Wolf "Дар-р-рмоед!"
    hide d4_beast_wolf_face with Dissolve(.5)

    show d4_beast_owl_face with Dissolve(.5)
    voice "voice/Owl/4day/Espolnit.ogg"
    Owl "Ух-ху-ху, пусть исполнит предназначение!"
    hide d4_beast_owl_face with Dissolve(.5)

    show d4_beast_fox_face with Dissolve(.5)
    voice "voice/Alisa/4day/117 KZ.ogg"
    Alis "К завтрашней ночи ждём мясца, а иначе..."
    hide d4_beast_fox_face with Dissolve(.5)

    show d4_beast_owl_face with Dissolve(.5)
    voice "voice/Owl/4day/Enache.ogg"
    Owl "...иначе..." id d4_wake_up_devend_16fcb524
    hide d4_beast_owl_face with Dissolve(.5)

    show d4_beast_bear_face with Dissolve(.5)
    voice "voice/Bear/4day/59 Enache.ogg"
    Bear "...иначе..." id d4_wake_up_devend_d3234aa7
    hide d4_beast_bear_face with Dissolve(.5)

    show d4_beast_wolf_face with Dissolve(.5):
        .5
        block:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat 8
        linear .03 xoffset 0
    voice "voice/Wolf/342 Enache.ogg"
    Wolf "...иначе..." id d4_wake_up_devend_858b4f79
    hide d4_beast_wolf_face with Dissolve(.5)

    $ story_manager.MarkEvent(("day4", "scene16"))

    show d4_polyard_alisa_animation with Dissolve(1.5)
    show layer master:
        align (0.5, 0.5)
        block:
            linear .03 zoom 1.02
            linear .03 zoom 1.00
            repeat
        time 4.
        linear .05 zoom 1.00
    voice "voice/Alisa/4day/118 Ena.ogg"
    Alis "...иначе мы съедим всю твою семью!" id d4_wake_up_devend_567d2de3
    hide d4_polyard_alisa_animation with Dissolve(.5)
    stop music2 fadeout 4.5
    play music "music/Dvar - Taai Liira.ogg" volume 0.9 fadein 4.5
    $ music_during_lines = 1.0

    play test_five "sounds/loop_circle_pit_monsters.ogg" fadein 1.5 loop

    scene d4_monster_sky:
        subpixel True
        align (.5, .5)
        zoom .5
        block:
            ease 120 zoom 1.
            ease 120 zoom .5
            repeat

    show d4_monster_beast_0:
        subpixel True
        align (.5, .5)
        transform_anchor True
        block:
            rotate 0
            linear 10 rotate 360
            repeat
    with Dissolve(.5)
    "Монстры образовали вокруг меня кольцо и завертелись в хороводе."

    show d4_monster_beast_0:
        subpixel True
        align (.5, .5)
        transform_anchor True
        block:
            rotate 0
            linear 5 rotate 360
            repeat
    with Dissolve(.5)
    play test_three "voice/anton/4day/230. AAA.ogg"
    "Я закричал."


    hide d4_monster_beast_0
    show d4_monster_beast
    with Dissolve(.2)
    "Мелькали глазища, клыки, когти, сливались в вереницу пятен и клякс."
    voice  "voice/Alisa/4day/HorRaz.ogg"
    Chorus "Раз-два, прилети сова."
    voice "voice/Alisa/4day/HorTri.ogg"
    Chorus "Три-четыре-пять, время поиграть."
    voice "voice/Alisa/4day/HorShest.ogg"
    Chorus "Шесть да шесть, дыбом волчья шерсть."
    voice "voice/Alisa/4day/HorSem.ogg"
    Chorus "Семь-восемь, бьём копытом оземь."
    show d4_monster_beast_4:
        xalign .5
        yanchor .5
        alpha 0
        parallel:
            linear .5 yanchor .1 alpha 1

        parallel:
            block:
                linear .02 xoffset 5
                linear .02 xoffset -5
                repeat
    "Морда лисы вылезла из мельтешащих пятен, в которые превратились туши зверей:"
    voice "voice/Alisa/4day/119 Dlya.ogg"
    Alis "Для медведя, для лисы..."
    voice "voice/Alisa/4day/119 Zaich.ogg"
    Alis "Зайчик, кушать принеси!"

    scene d4_paw_bg
    show d4_paw_fog:
        xpan 0
        alpha .5
        linear 120 xpan 360
        repeat
    show d4_paw_anton_scream
    with Dissolve(.5)
    play test_three "voice/anton/4day/231.Aa.ogg"
    "Вопль отчаянья — мой вопль — загудел по закоулкам вымершего посёлка:"
    voice "voice/anton/4day/231.Prinesu.ogg"
    Ant "Принесу, принесу, принесу!"

    stop test_five fadeout 1.2

    hide d4_paw_anton_scream
    show d4_paw_anton_b
    with Dissolve(.5)

    "Круг разомкнулся — и я бросился наутёк."
    play test_two "voice/anton/1day/029.Beg i o.ogg"

    play test_three "sounds/loop_footsteps_snow_run_creepy.ogg" fadein 1 loop

    show d4_paw_anton_b:
        parallel:
            linear .35 xoffset 300
        parallel:
            linear .35 alpha 0

    pause .5

    scene d4_road_dark
    show snow_night_1:
        matrixcolor BrightnessMatrix(-.5)
        blur 2
        block:
            xpan 0
            linear 10 xpan -360
            repeat
    show blizzard_d4_evening_face:
        matrixcolor BrightnessMatrix(-.5)
        block:
            xpan 0
            linear 10 xpan -360
            repeat
    with Dissolve(.5)
    "{sc=1}Будто нёсся в охотничьи силки. Моя голова трещала, в ней танцевали, врезаясь друг в друга, падая,\nподнимаясь, снова пускаясь в пляс уродливые образы.{/sc}"

    show d4_monster_hooty:
        alpha 0
        align (.5, .5)
        transform_anchor True
        subpixel True
        rotate -135
        xoffset int(1920*1./3.)
        zoom .8

        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            easeout_quad 5 zoom 2. xoffset 2000 yoffset -2000
    play test_six "voice/Owl/4day/12.ogg"
    "{sc=10}Раз-два...{/sc}"
    "{sc=3}Взмахивали крыльями, лезли мне в лицо клювами и слюнявыми пастями.{/sc}"

    show d4_monster_alice:
        alpha 0
        align (.5, .5)
        transform_anchor True
        subpixel True
        rotate 60
        xoffset -500


        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            easeout_quad 5 zoom 3. xoffset -2500 yoffset 2000
    play test_five "voice/Alisa/4day/Tri.ogg"
    "{sc=10}Три-четыре...{/sc}"
    "{sc=3}Орали и прыгали, так, что кровь вот-вот пойдёт из ушей: от грохота и криков или от внутреннего\nдавления, раскалывающего череп.{/sc}"
    stop test_three fadeout 20

    show d4_monster_wolfy:
        alpha 0
        align (.5, .5)
        transform_anchor True
        subpixel True
        rotate -60
        xoffset int(1920*1./4.)

        zoom .8
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            easeout_quad 5 zoom 3. xoffset 3000 yoffset 3000
    play test_five "voice/Wolf/Pyat_Shest_B.ogg"
    "{sc=10}Пять-шесть...{/sc}"
    "{sc=3}Шапка сбилась на глаза, отчего казалось, что небо скособочилось, будто готовая рухнуть крыша.{/sc}"

    show d4_monster_teddy:
        alpha 0
        align (.5, .5)
        transform_anchor True
        subpixel True
        rotate 135
        xoffset -int(1920*1./4.)
        yoffset -200
        zoom .8
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            easeout_quad 5 zoom 3. xoffset -2000 yoffset -2000
    play test_six "voice/Bear/4day/Sem8.ogg"
    "{sc=10}Семь-восемь...{/sc}"
    "{sc=3}Снег, как побелка, сыпался сверху.{/sc}"

    show d4_monster_hooty_side as hooty2:
        alpha .6
        subpixel True
        ypos 800
        yanchor .5
        xpos 1920
        xanchor 0.
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 xanchor 1.
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3. blur 32 matrixcolor TintMatrix("#fff0")
    show d4_monster_alice_side as alice2:
        alpha .6
        subpixel True
        ypos 300
        yanchor .5
        xpos 0
        xanchor 1.
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 xanchor 0.
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3. blur 32 matrixcolor TintMatrix("#fff0")
    "{sc=5}Преследуемый стаей, я бежал по пустым улицам, по окоченевшему миру.{/sc}"
    "{sc=3}Оглядывался и никого не видел за спиной.{/sc}"

    show d4_monster_wolfy as wolfy2:
        alpha .6
        transform_anchor True
        subpixel True
        yalign .5
        xpos 1320
        xanchor .5
        yoffset 1080
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom 1. yoffset 0
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")
    show d4_monster_teddy as teddy2:
        alpha .6
        transform_anchor True
        subpixel True
        rotate 180
        yalign .5
        xpos 600
        xanchor .5
        yoffset -1080
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom 1. yoffset 0
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")
    "{sc=5}Зажмуривался и шарахался от их ритуальных плясок в моём пылающем сознании.{/sc}"

    show bg_black:
        alpha 0
        linear 1 alpha 1
    show d4_monster_hooty as hooty3:
        alpha .6
        transform_anchor True
        subpixel True

        rotate 60
        ypos 1.
        xpos 0.
        yanchor .0
        xanchor .5
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom .8 yanchor 1. yzoom 1.5
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")
    show d4_monster_teddy as teddy3:
        alpha .6
        transform_anchor True
        subpixel True

        rotate 30+90
        ypos 0.
        xpos 0.
        yanchor .0
        xanchor .5
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom .8 yanchor .8 yzoom 1.5
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")
    show d4_monster_alice as alice3:
        alpha .6
        transform_anchor True
        subpixel True

        rotate 60+90+90
        ypos 0.
        xpos 1.
        yanchor .0
        xanchor .5
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom .8 yanchor .8 yzoom 1.5
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")
    show d4_monster_wolfy as wolfy3:
        alpha .6
        transform_anchor True
        subpixel True

        rotate 30+90+90+90
        ypos 1.
        xpos 1.
        yanchor .0
        xanchor .5
        zoom 1.
        parallel:
            .05
            alpha 0
            .05
            alpha .6
            repeat
        parallel:
            linear 5 zoom .8 yanchor .8 yzoom 1.5
        parallel:
            2.
            matrixcolor TintMatrix("#ffff")
            easeout_quad 3 blur 32 matrixcolor TintMatrix("#fff0")

    play test_six "voice/Bear/4day/56 Vahaha.ogg"
    "{sc=5}Прижал ладони к ушам, чтобы заглушить шум.{/sc}"
    show bg_black as black2:
        alpha 0
        linear 1 alpha 1
    "{sc=3}Чтобы голова не развалилась.{/sc}"
    play test_seven "voice/anton/2day/Begi2.ogg" fadein 3 
    stop music fadeout 4.5

    stop test_three fadeout 1.5
    stop test_one fadeout 5
    pause 1

    scene bg_forest0_long_dark:
        xalign .0
    with Dissolve(2)
    play fon "sounds/loop_birds_singing.ogg" fadein 2.5 volume 0.08 loop
    "Рассвет я встретил в дебрях леса."
    scene bg forest0_long:
        xalign .0
    with Dissolve(5)

    scene bg_black with Dissolve(2.5)

    call d4_true_detective_calculate from _call_d4_true_detective_calculate_1

    call d4_flowchart

    jump day_5



label d4_true_detective_calculate:
    if Flags.Has("polhouse") and true_detective_count4 == 9:


        $ achievement_grant("ach_true4")
        $ persistent.has_d4_detective_rootA = True
        return

    if Flags.Has("katya") and true_detective_count4 == 6:


        $ achievement_grant("ach_true4")
        $ persistent.has_d4_detective_rootB = True

        return

    if Flags.Has("police") and true_detective_count4 == 2:


        $ achievement_grant("ach_true4")
        $ persistent.has_d4_detective_rootC = True

        return

    return





label d4_ending_bad_needle:
    if not story_manager.IsMarkedPersistStrict(("day4", "ending", "needle")):
        $ new_ending = ("day4", "ending", "needle")
    $ story_manager.MarkEvent(("day4", "ending", "needle"))

    scene bg_black


    $ achievement_grant("ach_end1")

    stop music fadeout 3.0
    stop music2 fadeout 3.0

    $ renpy.start_predict("d4e_scene3_bg")
    $ renpy.start_predict("snow_night_1")
    $ renpy.start_predict("d4e_scene3_fg")
    $ renpy.start_predict("d4_snow_night")
    $ renpy.start_predict("blizzard_d4_evening_face")
    $ renpy.start_predict("d4e_scene4_bg")
    $ renpy.start_predict("d4e_scene4_fg")


    scene expression "images/end/end.png" with Dissolve(1.)

    $ gazeta_text = _("ШКОЛЯР-УБИЙЦА\nМилиция арестовала подростка, зарезавшего сверстника во время ссоры. Между учениками шестого класса средней школы возник конфликт, в результате которого один из учащихся нанёс другому более десятка ран выкидным ножом. Мальчика доставили  в больницу, где он скончался от потери крови. Школьник, убивший сверстника, во время допроса в милиции признал вину. По факту инцидента заведено уголовное дело по статье 105 УК РФ. Также уголовное дело по статье о халатности может грозить директору школы, чей ученик свободно разгуливал с ножом, и заму по воспитательной работе. На месте происшествия работают следователи и криминалисты.")
    show screen gazeta(message = gazeta_text, caption = BTN_CONTINUE) with Dissolve(1.)
    $ ui.interact()
    hide screen gazeta with Dissolve(1.)

    scene bg_black
    with Dissolve(1.)

    play music2 "music/last breath.ogg" 

    $ yadj = ui.adjustment()
    $ title_mover = TitleMover(yadj)

    $ title_mover.x_center = 0.5
    $ title_mover.sect_size = (660, 600)



    $ title_mover.add_section(0.01, "d4_ending_bad_needle.title1")
    $ title_mover.add_section(0.15, "d4_ending_bad_needle.title2")
    $ title_mover.add_section(0.35, "d4_ending_bad_needle.title3")
    $ title_mover.add_section(0.65, "d4_ending_bad_needle.title4")
    $ title_mover.add_section(None, "d4_ending_bad_needle.endtitle")

    show screen endtitles_main(title_mover)
    $ ui.interact()
    return

    label d4_ending_bad_needle.title1:

        show d4e_scene1_bg:
            subpixel True
            xalign .25
            yalign .25
            zoom 2.5
            easein 30 xalign .0
        show d4e_scene1_olya:
            subpixel True
            xalign .5
            xoffset -200
            easein 30 xoffset -300
        show bg_black as dark2:
            alpha 1
            linear 1.0 alpha .2
        $ ui.interact()
        return

    label d4_ending_bad_needle.title2:
        show d4e_scene2:
            alpha 0
            linear 1. alpha 1

        $ ui.interact()
        return

    label d4_ending_bad_needle.title3:

        show d4e_scene3_bg:
            alpha 0
            linear 1.0 alpha 1
        show snow_night_1:
            alpha 0
            linear 1.0 alpha 1
        show d4e_scene3_fg:
            alpha 0
            linear 1.0 alpha 1
        show d4_snow_night:
            alpha 0
            linear 1.0 alpha 1
        show blizzard_d4_evening_face:
            alpha 0
            linear 1.0 alpha 1

        $ ui.interact()
        return

    label d4_ending_bad_needle.title4:

        show d4e_scene4_bg:
            alpha 0
            linear 1.0 alpha 1
        show snow_night_1 as snow2_1:
            alpha 0
            linear 1.0 alpha 1
        show d4e_scene4_fg:
            alpha 0
            linear 1.0 alpha 1
        show d4_snow_night as snow2_2:
            alpha 0
            linear 1.0 alpha 1
        show blizzard_d4_evening_face as snow2_3:
            alpha 0
            linear 1.0 alpha 1

        $ ui.interact()
        return

    label d4_ending_bad_needle.endtitle:
        hide screen endtitles_main with Dissolve(1.0)
        $ renpy.stop_predict("d4e_scene3_bg")
        $ renpy.stop_predict("snow_night_1")
        $ renpy.stop_predict("d4e_scene3_fg")
        $ renpy.stop_predict("d4_snow_night")
        $ renpy.stop_predict("blizzard_d4_evening_face")
        $ renpy.stop_predict("d4e_scene4_bg")
        $ renpy.stop_predict("d4e_scene4_fg")

        call d4_true_detective_calculate from _call_d4_true_detective_calculate_2

        show screen d5_end(pos = (1673, 821)) with Dissolve(.5)
        $ ui.interact()
        hide screen d5_end with Dissolve(.5)

        scene bg_black
        with Dissolve(1)

        stop music2 fadeout 2.0

    call d4_flowchart
    return

label d4_flowchart:
    scene bg_black with Dissolve(.5)

    if not story_manager.IsMarkedLocal(("day1", "scene0")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day1",))
            story_manager.Extend( events )

    if not story_manager.IsMarkedLocal(("day2", "scene0")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day2",))
            story_manager.Extend( events )

    if not story_manager.IsMarkedLocal(("day3", "scene1")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day3",))
            story_manager.Extend( events )

    if not (story_manager.IsMarkedLocal(("day4", "scene1a")) or story_manager.IsMarkedLocal(("day4", "scene1b"))):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day4",))
            story_manager.Extend( events )

    python:
        story_manager.width = 1920*2
        story_manager.height = 8295 +600
        story_manager.day_code = "day4"


    show screen StoryExplainerDCut_Day4(story_manager) with Dissolve(1.5)
    $ ui.interact()

    show screen StoryExplainerDCut_Hider
    with Dissolve(1.5)

    if new_ending is not None:
        call screen gallery()

    return

screen StoryExplainerDCut_Day4(story_manager):
    tag flowchart

    $ story_manager.story_db = story_so_far_dcut

    $ y_val = IncrementalInt(300)
    $ yp_val = IncrementalInt(0)
    $ yf_val = IncrementalInt(0)

    default view_x = ui.adjustment(value = (story_manager.width - 1920)*0.35, range=story_manager.width)
    default view_y = ui.adjustment(value = 0, range=story_manager.height)
    default sub_view_x = ui.adjustment(value = (story_manager.width - 1920)*0.35, range=story_manager.width)
    default sub_view_y = ui.adjustment(value = 0, range=story_manager.height*flowchart_bg_ratio)
    default sub_view_x2 = ui.adjustment(value = (story_manager.width - 1920)*0.35, range=story_manager.width)
    default sub_view_y2 = ui.adjustment(value = 0, range=story_manager.height*flowchart_dust_ratio)

    default xmid = 960+480+240
    default xpmid = 960-240
    default xfmid = 1920+480+240


    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (story_manager.width, story_manager.height*flowchart_bg_ratio)

        yadjustment sub_view_y

        add Widespan_Dependant(None, sub_view_y, None, view_y)
        add "story_bg_1"


    add "story_bg_3"


    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (story_manager.width, story_manager.height)
        draggable True
        pagekeys True

        xadjustment view_x
        yadjustment view_y


        if True:
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene1a", (xmid+250, y_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene1b", (xmid-250, y_val(0)))

            $ y_val(75)

            add "flowchart_arrow_left" anchor (1., .0) pos (xmid+250, y_val(0)) xzoom 0.55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene1a")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xmid-250, y_val(0)) xzoom 0.55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene1b")):
                    at arrow_valid
                else:
                    at arrow_invalid

            $ y_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene2", (xmid, y_val(75)))

            add "flowchart_arrow_left" anchor (1., .0) pos (xmid, y_val(0)) xzoom 3.00:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_t")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (1., .0) pos (xmid, y_val(0)) xzoom 1.75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_p")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, y_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_s")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xmid, y_val(0)) xzoom 1.75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v")):
                    at arrow_valid
                else:
                    at arrow_invalid

            $ y_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_t", (xpmid-250, y_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_p", (xpmid+250, y_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_s", (xmid, y_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v", (xfmid, y_val(0)))

            $ y_val(75)

            add "flowchart_arrow_down_long" anchor (.5, .0) pos (xmid, y_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_s")):
                    at arrow_valid
                else:
                    at arrow_invalid


        if True:
            $ yp_val(y_val(0))

            add "flowchart_arrow_right" anchor (1., .0) pos (xpmid, yp_val(0)) xzoom .55 yzoom 1.5:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_t")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (0., .0) pos (xpmid, yp_val(0)) xzoom .55 yzoom 1.5:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_p")):
                    at arrow_valid
                else:
                    at arrow_invalid

            $ yp_val(175+75)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph1", (xpmid, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la polhouse1", (xpmid - (75*2 + 400*2 + 40)//2, yp_val(175+85*2+75+25)), (75*2 + 400*2 + 40, 175+85*2+75+25), ("ski", "telephone", "horns", "portrait", "mirror", "grandfather"))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph2", (xpmid, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la polhouse2", (xpmid - (75*2 + 400)//2, yp_val(175+85*2+75+25)), (75*2 + 400, 175+85*2+75+25), ("player", "piano", "poster"))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph5", (xpmid, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game poster", (xpmid - (75*2+400)//2, yp_val(175+85*0+75+25)), (75*2 + 400, 175+85*0+75+25), ("solve",))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph6", (xpmid, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph7", (xpmid, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ph1")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ph9", (xpmid, yp_val(75)))

            add "flowchart_arrow_right" anchor (0., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_rb")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (1., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ra")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yp_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_ra", (xpmid-250, yp_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_rb", (xpmid+250, yp_val(0)))

            $ yp_val(75)

            add "flowchart_arrow_right" anchor (1., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_ra")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (0., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_rb")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yp_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_r2", (xpmid, yp_val(75)))

            add "flowchart_arrow_right" anchor (0., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_r4")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (1., .0) pos (xpmid, yp_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "ending", "needle")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yp_val(175)

            use StoryExplainer_EndingSegment(story_manager, story_manager.day_code, "ending", "needle", (xpmid-250, yp_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_r4", (xpmid+250, yp_val(0)))
            $ yp_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid+250, yp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_r4")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_r5", (xpmid+250, yp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xpmid+250, yp_val(int(121*4.25))) yzoom 4.25:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_r5")):
                    at arrow_valid
                else:
                    at arrow_invalid

            add "flowchart_arrow_right" anchor (0., .0) pos (xpmid+250, yp_val(0)) xzoom 1.15:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_r5")):
                    at arrow_valid
                else:
                    at arrow_invalid


        if True:
            $ yf_val(y_val(0))


            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid, yf_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v2")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v2", (xfmid, yf_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid, yf_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v2")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v4", (xfmid, yf_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid, yf_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v4")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "byasha", (xfmid, yf_val(75)))

            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid, yf_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "byasha", "dismiss")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xfmid, yf_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "byasha", "call")):
                    at arrow_valid
                else:
                    at arrow_invalid

            $ yf_val(175)

            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "byasha", (xfmid, yf_val(0)), "dismiss")
            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "byasha", (xfmid, yf_val(0)), "call")
            $ yf_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid-350, yf_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "byasha", "dismiss")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+350, yf_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "byasha", "call")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yf_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v5", (xfmid-350, yf_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v6", (xfmid+350, yf_val(0)))
            $ yf_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid-350, yf_val(0)) yzoom 7.0:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v5")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+350, yf_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v6")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yf_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v7", (xfmid+350, yf_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+350, yf_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v6")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "garage", (xfmid+350, yf_val(75)))

            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid+350, yf_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "police")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xfmid+350, yf_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "enter")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yf_val(175)

            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "garage", (xfmid+350, yf_val(0)), "police")
            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "garage", (xfmid+350, yf_val(0)), "enter")

            $ yf_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+100, yf_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "police")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+600, yf_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "enter")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yf_val(175)

            $ yfp_val = IncrementalInt(yf_val(0))
            $ yfg_val = IncrementalInt(yf_val(0))












            use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la police", (xfmid -125 - (75*2 + 400)//2, yfp_val(175+85*1+75+25)), (75*2 + 400, 175+85*1+75+25), ("cage", "mask"))
            use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la garage", (xfmid +600 - (75*2 + 400)//2, yfg_val(175+85*5+75+25)), (75*2 + 400, 175+85*5+75+25), ("tools", "junk", "boxes", "car", "tiski", "shelf"))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid-125, yfp_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "police")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_police_2", (xfmid-125, yfp_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid-125, yfp_val(0)) yzoom 16.0:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_police_2")):
                    at arrow_valid
                else:
                    at arrow_invalid


            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+600, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "garage", "enter")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_garage", (xfmid+600, yfg_val(0)))
            $ yfg_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+600, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)


            use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game katya", (xfmid + 600 - (75*2+400)//2, yfg_val(175+85*2+75+25)), (75*2 + 400, 175+85*2+75+25), ("fail", "save", "photo"))

            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid+600, yfg_val(175)) xzoom 0.75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_garage2", (xfmid+150, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+150, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "fail")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xfmid+150, yfg_val(0)) xzoom 1.25:
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "save")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_NarrativeSegment_Extended(story_manager, story_manager.day_code, "game katya", "fail", (xfmid+150, yfg_val(0)))
            use StoryExplainer_NarrativeSegment_Extended(story_manager, story_manager.day_code, "game katya", "save", (xfmid+700, yfg_val(0)))
            $ yfg_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+150, yfg_val(0)) yzoom 1.5:
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "fail")):
                    at arrow_valid
                else:
                    at arrow_invalid

            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+700, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "save")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid+700, yfg_val(0)) xzoom 1.25 yzoom 1.5:
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "save")) and not story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "photo")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_NarrativeSegment_Extended(story_manager, story_manager.day_code, "game katya", "photo", (xfmid+700, yfg_val(0)))
            add "flowchart_arrow_down" anchor (.5, .0) pos (xfmid+150, yfg_val(0)) yzoom 1.5:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_garage2")) and not story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "photo")):
                    at arrow_valid
                else:
                    at arrow_invalid

            $ yfg_val(75)

            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid+700, yfg_val(0)) xzoom 1.25:
                if story_manager.IsMarkedLocal((story_manager.day_code, "game katya", "photo")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid-125, yfg_val(0)) xzoom 1.5 yzoom 1.75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_police_2")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_v8", (xfmid+150, yfg_val(75)))
            add "flowchart_arrow_left" anchor (1., .0) pos (xfmid+150, yfg_val(0)) xzoom 1.90:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene_v8")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)



        if True:
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene3", (xmid, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene3")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene4", (xmid, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene4")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene5", (xmid, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene5")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene6", (xmid, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene7")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene7", (xmid, yfg_val(75)))

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid, yfg_val(175)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene7")):
                    at arrow_valid
                else:
                    at arrow_invalid

            use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "treat1", (xmid, yfg_val(75)))

            add "flowchart_arrow_left" anchor (1., .0) pos (xmid, yfg_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat1", "refuse")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xmid, yfg_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat1", "accept")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "treat1", (xmid, yfg_val(0)), "refuse")
            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "treat1", (xmid, yfg_val(0)), "accept")
            $ yfg_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid+350, yfg_val(0)) yzoom 5.0:
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene11")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid-350, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat2")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "treat2", (xmid-350, yfg_val(75)))

            add "flowchart_arrow_left" anchor (1., .0) pos (xmid-350, yfg_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat2", "refuse")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xmid-350, yfg_val(0)) xzoom .75:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat2", "accept")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "treat2", (xmid-350, yfg_val(0)), "refuse")
            use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "treat2", (xmid-350, yfg_val(0)), "accept")
            $ yfg_val(75)

            add "flowchart_arrow_right" anchor (0., .0) pos (xmid-700, yfg_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat2", "refuse")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_right" anchor (0., .0) pos (xmid-0, yfg_val(0)) xzoom .55:
                if story_manager.IsMarkedLocal((story_manager.day_code, "treat2", "accept")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)


            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene8", (xmid-350, yfg_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene11", (xmid+350, yfg_val(0)))
            $ yfg_val(75)

            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid-350, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene8")):
                    at arrow_valid
                else:
                    at arrow_invalid
            add "flowchart_arrow_down" anchor (.5, .0) pos (xmid+350, yfg_val(0)):
                if story_manager.IsMarkedLocal((story_manager.day_code, "scene11")):
                    at arrow_valid
                else:
                    at arrow_invalid
            $ yfg_val(175)

            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene10", (xmid-350, yfg_val(0)))
            use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene16", (xmid+350, yfg_val(0)))







    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (story_manager.width, story_manager.height*flowchart_dust_ratio)

        yadjustment sub_view_y2

        add Widespan_Dependant(None, sub_view_y2, None, view_y)
        add "story_bg_2"


    use StoryExplainer_UI(story_manager)

    use StoryExplainer_Selector(story_manager)


    if config.developer:
        frame:
            align (0., 0.)
            text "y_val: " + str(yfg_val(0)) color "#000"
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
