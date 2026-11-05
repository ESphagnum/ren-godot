label end_day_03_titr_0():
    menu:
        "{size=+18}Тапнуть на свидетеля{/size}":
            $ is_tapped ="tap"
        "{size=+18}Не тапать{/size}":
            pass
    menu:
        "{size=+18}Записать репортаж{/size}":
            $ Flags.Raise("record")
        "{size=+18}не записывать{/size}":
            pass
    menu:
        "{size=+18}Взять жевачку{/size}":
            $ Flags.Raise("gum")
        "{size=+18}не брать{/size}":
            pass
    menu:
        "{size=+18}Дать отпор (в школе){/size}":
            $ Flags.Raise("fight")
            menu:
                "{size=+18}Алиса{/size}":
                    $ Flags.Raise("day2 fox")
                "{size=+18}Полина{/size}":
                    $ Flags.Raise("day2 polina")
            menu:
                "{size=+18}Послать{/size}" if Flags.Has("fight"):
                    pass
                "{size=+18}Надеть маску{/size}":

                    $ Flags.Raise("mask")
        "{size=+18}Стерпеть{/size}":
            $ Flags.Raise("mask")
    menu:
        "{size=+18}Взять амулет{/size}" if Flags.Has("fight"):
            $ Flags.Raise("amulet")
        "{size=+18}Не брать{/size}":

            pass
    $ ROUTE_SOLO = Flags.Has("mask")
    $ ROUTE_POLINA = not ROUTE_SOLO and Flags.Has("day2 polina")
    $ ROUTE_FOX = not ROUTE_SOLO and Flags.Has("day2 fox")
    jump end_day_03_titr

























default ROUTE_SOLO = True
default ROUTE_POLINA = False
default ROUTE_FOX = False

label d3_0:

    menu:
        "{size=+18}Тапнуть на свидетеля{/size}":
            $ is_tapped ="tap"
        "{size=+18}Не тапать{/size}":
            pass
    menu:
        "{size=+18}Записать репортаж{/size}":
            $ Flags.Raise("record")
        "{size=+18}не записывать{/size}":
            jump lll11

label lll11:
    menu:
        "{size=+18}Взять жевачку{/size}":
            $ Flags.Raise("gum")
        "{size=+18}не брать{/size}":
            jump lll21
label lll21:
    menu:
        "{size=+18}Дать отпор (в школе){/size}":
            $ Flags.Raise("fight")
            menu:
                "{size=+18}Алиса{/size}":
                    $ Flags.Raise("day2 fox")
                "{size=+18}Полина{/size}":
                    $ Flags.Raise("day2 polina")
            menu:
                "{size=+18}Послать{/size}" if Flags.Has("fight"):
                    jump day_3
                "{size=+18}Надеть маску{/size}":

                    $ Flags.Raise("mask")
                    jump day_3
        "{size=+18}Стерпеть{/size}":
            $ Flags.Raise("mask")

default true_detective_count3 = 0
label day_3:
    $ ROUTE_SOLO = Flags.Has("mask")
    $ ROUTE_POLINA = not ROUTE_SOLO and Flags.Has("day2 polina")
    $ ROUTE_FOX = not ROUTE_SOLO and Flags.Has("day2 fox")



    window hide
    scene bg_logo3
    with Dissolve(1.0)

    show screen center_text(_("Эпизод III: Дыбом волчья шерсть")) with Dissolve(.5)

    pause 1.

    show screen day5_continue_button(d5_logo_begin)
    with Dissolve(.5)
    $ ui.interact()

    hide screen day5_continue_button
    with Dissolve(.5)

    pause 1.

    hide screen center_text with Dissolve(.5)

    $ story_manager.MarkEvent(("day3", "scene1"))

    scene black with Dissolve(1.)
    scene d2_end_rasp_zoom
    show men_00:
        anchor (.5, .5)
        ypos 540
        xpos 1000
    show men_02:
        anchor (.5, .5)
        ypos 540
        xpos 960
    show men_03:
        anchor (.5, .5)
        xpos 960
        ypos 540
    show men_04:
        anchor (.5, .5)
        xpos 560
        ypos 540
    show men_05:
        anchor (.5, .5)
        xpos 1100
        ypos 540
    with Dissolve(2.0)
    pause 3
    $ music_during_lines = 0.85
    window show
    play test_one "voice/kate/72 KA.ogg"
    Pupils "Это тот, который Бабурина ненавидел."

    play test_two "voice/Child/3day/01D.ogg"
    Pupils "Думаешь, это он сделал?"
    play test_one "voice/kate/73 KA.ogg"
    Pupils "Я слышала, он со странностями."
    play test_five "sounds/roll-hit-1.ogg"
    $ music_during_lines = 1.0




    if ROUTE_FOX:
        scene bg_white with Dissolve(0.12)
        show flback
        "В ушах звучал крик Ромки, которым он с Бяшей напутствовал удирающего Семёна."
        voice "voice/romka/3day/Gorlo tebe pererezu.ogg"
        Rom "Горло тебе перережу, слышишь!"

        play test_one "voice/romka/3day/69_Svinja.ogg"
        "«Свинья!»"
        scene bg_white with Dissolve(0.12)
        play test_five "sounds/roll-hit-1.ogg"
        scene bg koridorchic_mor_full2:
            xpos -2319
        show men_02:
            subpixel True
            anchor (.5, .5)
            ypos 540
            xpos 960
        "Неужели Ромка грозился всерьёз?"
        "Нагнать бывшего приятеля в чаще и..."
        "... и что?"
        "Убить просто так?"
        "Нет, в голове не укладывается."
    "Я судорожно протёр стёкла очков..."
    "Очки!"
    if ROUTE_FOX:
        "Их сжимал в кулаке Семён, уворачиваясь от затрещин своих дружков."
        "Теперь бывших."


    elif not ROUTE_FOX:
        "Их сжимал в кулаке Семён, когда меня били."

    "А уже через несколько часов пропажа лежала на моём карнизе."
    scene bg koridorchic_mor_full2:
        ypos 0
        xpos -2319
        pause 1.0
        ease 12 xpos -300
    show men_02:
        subpixel True
        anchor (.5, .5)
        ypos 540
        xpos 960
        pause 1.0
        ease 12 xpos 960 + 2019
    with Dissolve(0.7)
    "Сложно представить, что Сёма вдруг засовестился и вернул мне очки таким странным образом."


    play fon "sounds/school_003.ogg" fadein 2.0
    "Шокированный, я шёл к классу под гадкие шепотки."

    "А перед глазами всё стояла фотография."
    show koshmar_round:
        alpha 0.0
        linear 2. alpha 1.0
    play music "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 0.5
    "Сёма пропал. Семёна нет."
    stop fon fadeout 1
    show Sema_F
    "Его толстые пальцы не дотянутся до моего горла, его печатка не врежется в мою скулу, он больше не унизит меня и не оскорбит."
    "Не этого ли я желал?"
    "С другой стороны..."
    show Sema_F2
    "Разве мне и правда хотелось, чтобы Сёма стал мутным пятном на доске объявлений?"
    "Чей-то сын, чей-то внук, над которым измывались так же, как надо мной."
    show bg_black with Dissolve(2)
    "Хотел ли я, чтобы незримый соратник разобрался с ним так жестоко?"
    stop music fadeout 4
    scene bg koridorchic_mor_full2 with Dissolve(2):
        xpos -300
    "Я не знал ответа."
    "Или боялся его."


    show sprite_polina_d3 at mom_income_left with Dissolve(0.5):
        yoffset 120
    play music "music/29_Polina.ogg" volume 0.85 fadein 0.5
    play test_one "sounds/steps/Polina_step_01.ogg"
    "И всё же в школе было и хорошее."
    "Полина — девочка со скрипкой, — она была похожа на горный ручей, на колодезную воду, которую пьёшь, прихватив губами цинковый ободок ведра, и не можешь напиться."

    if ROUTE_POLINA:
        "Воспоминания о вчерашней прогулке слегка остудили мой пыл."
        "Полинина ненависть к собакам, пускай в её случае и была оправданной, всё же настораживала меня."
        "Разве может в сердце такой очаровательной девочки найтись место для столь отвратительной червоточины?"
        "Я тут же вспомнил о неожиданно вскрывшемся тёмном прошлом отца."
        "Человек, которого я считал своим кумиром, стал причиной нашего переезда в эту мрачную глухомань..."
        "…если, конечно, можно верить маминым крикам из-за стены."
        "И всё же Полина пыталась защитить меня от шайки хулиганов, пускай и безуспешно."
        "Она молила Ромку оставить меня в покое, собирала, глотая слёзы, мои разбросанные по лесу учебники и тетради."
        "А когда подонки пытались её уволочь – сопротивлялась что было сил в её хрупком теле."
        "В конце-концов, именно она нашла мой потерянный в таёжном лесу дом и сказала папе, что меня, избитого, бросили одного в потёмках."
        "Возможно, я сужу её слишком строго."

    "Что, если нарисовать историю с её участием? Будто герой спасает её от ужасных чудовищ?"
    play test_one "sounds/steps/shagi.ogg"

    stop music fadeout 2
    show banda_mini behind sprite_polina_d3 with Dissolve(.5):
        xpos -300
    "Едва я подумал про монстров, как парочка одноклассников съехала по перилам, скалясь, словно инопланетяне из фильма «Чужие»."
    play test_one "music/Phrases_05.ogg"

    "Личинки боязни незамедлительно отложились внутри."
    play music2 "music/Morning Tensions_02.ogg" volume 0.85 fadein 1

    "Попадаться на глаза Ромке и Бяше после вчерашнего не было ни малейшего желания. Особенно из-за внезапного исчезновения Семёна."

    show sprite_polina_d3:
        yoffset 120
        alpha 1.0
        parallel:
            linear 2.0 alpha .00
        parallel:
            linear 0.5 yoffset 140
            linear 0.5 yoffset 120
            repeat
        parallel:
            linear 2.0 xoffset 400
    play test_one "sounds/steps/Polina_step_02.ogg"
    if ROUTE_POLINA:
        "Полина хотела было заговорить со мной, но, заметив эту парочку, вдруг помрачнела и прошагала мимо, задержав на мне виноватый взгляд."
    else:
        pause 2
    play sound "sounds/sfx_steps.ogg"

    window hide
    scene bg koridorchic_mor_open_4:
        alpha 1.0
        ypos 0
        xpos -300
        pause 1
        parallel:
            ease 3.0 xpos 0
    show banda_mini:
        xpos -300
        alpha 1
        pause .5
        linear 0.5 alpha 0
    play test_one "sounds/Door_open_2.ogg"
    show bg_classroom base 3 1 box:
        alpha 0.0
        ypos 0
        xpos -3911 + 1920
        parallel:
            pause 2.5
            ease 2.5 xpos -3911 + 1920 + 300
        parallel:
            pause 3
            linear 0.5 alpha 1.0

    $ renpy.pause(1.0)
    play test_one "sounds/steps/steps_shool.ogg"
    $ renpy.pause(3.0)
    play fon "sounds/fon/noise_klass.ogg" fadein 1.0
    play test_two "sounds/steps/steps_shool_02.ogg"
    $ renpy.pause(1.5)

    "Войдя в класс, я прошёл к последней парте."
    stop fon fadeout 0.5
    "В тишине, потому что одноклассники резко притихли."
    "Их взгляды буквально пихали меня, трогали, исследовали."


    if ROUTE_POLINA or ROUTE_SOLO:
        "Они смотрели на меня с убивающей смесью жалости, насмешки и презрения. Так учёный смотрит на гадкого неизвестного науке червяка."

    "Я стиснул кулаки и уставился на свою парту, чуть ли не до потолка заваленную стопками библиотечных учебников."
    "Словно это я пропал в том заснеженном лесу, и теперь моё место наконец сгодилось для чего-то действительно нужного."
    "Впереди стоял пустой стул Семёна. Где-то в другом классе пылился точно такой же стул, покинутый Вовой."
    stop music2 fadeout 4

    $ SceneFlags.Reset()
    $ story_manager.MarkEvent(("day3", "la classroom"))
    label day_3.observe:

    window hide
    scene bg_classroom base 3 1 box:
        xpos -3911 + 1920 + 300
    call screen day3_observe()


label d3_look_projector:
    play test_one "sounds/yula-3.ogg"
    window show
    if SceneFlags.Seen("projector"):
        "Фильмоскоп."
    else:
        $ story_manager.MarkEvent(("day3", "la classroom", "projector"))
        "Старенький и дешёвый проектор для рулонных диафильмов. Я называл такую модель «танчик» — из-за внешнего сходства."

        "Когда-то у меня было много классных сказок, которые мы смотрели с папой в темноте."
        "Помню «Крошку Енота» и того, кто сидит в пруду. «Маугли» Редьярда Киплинга, и многие другие."
        "Тут же меня накрыло воспоминание, как гудел проектор фильмоскопа, как пылал жаром его корпус, а яркий луч бил в стену, превращая её в экран."
        "Жаль, что в школе диафильмы были в основном про полезные минералы и ОБЖ."
        $ true_detective_count3 += 1

    jump day_3.observe


label d3_look_esenin:
    play test_one "sounds/samolet_2.ogg"
    window show
    if SceneFlags.Seen("esenin"):
        "Портреты классиков."
    else:
        $ story_manager.MarkEvent(("day3", "la classroom", "esenin"))
        "Я посмотрел на портреты классиков. Взгляд остановился на фотографии Есенина."
        "В прошлом году мне задали выучить любое стихотворение, и папа предложил про пса Джима, — за авторством Сергея Александровича."
        "Всех четверостиший я уже и не помню, но конец почему-то врезался мне в память:"
        "«Она придёт, даю тебе поруку.\nИ без меня, в её уставясь взгляд,"
        "Ты за меня лизни ей нежно руку\nЗа всё, в чём был и не был виноват»."


        $ true_detective_count3 += 1

    jump day_3.observe


label d3_look_box:
    play test_one "sounds/korsar_2.ogg"
    window show
    if SceneFlags.Seen("box"):
        "Коробка бомбочек «Корсар»."
    else:

        $ story_manager.MarkEvent(("day3", "la classroom", "box"))
        "Такая вещь была у каждого моего знакомого мальчишки. Пороховые петарды, которые оглушительно взрываются."
        "Особенно в закрытой арке. Говорят, их собирают в Китае, и они могут оторвать пальцы, если зажать их в кулаке."
        "Особенно эти чёрные «Корсары». Пластмассовых солдатиков они, конечно, не взорвут, а вот подделки из пластилина — вполне."
        $ true_detective_count3 += 1

    jump day_3.observe


label day_3_continue:
    $ story_manager.MarkEvent(("day3", "scene2"))
    scene bg_classroom base 3 1_no_chair:
        ypos 0
        xpos -3911 + 1920 +300
        pause 0.5
        ease 4.0 xpos -3911 + 1920 + 1300
    show korsar_box:
        ypos 0
        xpos -3911 + 1920 +300
        pause 0.5
        ease 4.0 xpos -3911 + 1920 + 1300
    show classroom_chair:
        xpos -3911 + 1920 + 300 - 20
        ypos 20
    with None

    hide classroom_chair
    with Dissolve(.5)

    pause .5
    "Немного помешкав, я сел за парту Бабурина, куда изначально меня планировала посадить Лилия Павловна."
    play music "music/28_Dejection.ogg" volume 0.8 fadein 0.5
    play fon "sounds/fon/noise_klass.ogg" fadein 1.0
    "Одноклассники вдруг продолжили разговор — будто кто-то снял фильм с паузы."
    scene bg_classroom base 3 2_no_chair:
        xpos -3911 + 1920 + 1300
    with Dissolve(0.5)
    voice "voice/kate/79 KA.ogg"
    Kate "Бабушка Бабурина такой кипиш устроила, когда он домой не явился."
    voice "voice/kate/80 KA.ogg"
    Kate "Сначала в школу прибежала, потом ментов вызвала."
    voice "voice/kate/81 KA.ogg"
    Kate "Да-да-да!"
    scene bg_classroom base 3 1_no_chair:
        xpos -3911 + 1920 + 1300
    with Dissolve(0.5)
    show kat_whisper with Dissolve(1.0):
        alpha 0.0
        linear 1.2 alpha 1.0
    play test_one "voice/kate/82 KA.ogg"
    "Катя с хитрецой посмотрела на меня, а потом склонилась к соседке и зашептала."
    play test_one "voice/kate/86 KA.ogg"
    "Переглянулись девочки со второй парты — она и с ними поделилась — зашушукала, быстро закивала."
    play test_one "voice/kate/85 KA.ogg"
    "Я ловил на себе её взгляд, взгляд её соседки, взгляды других девочек и мальчиков."
    "Каждый из них считал нужным посмотреть на меня, словно они..."
    hide kat_whisper with Dissolve(0.5)

    "... искали следы крови на моих пальцах."
    "Так хотелось оправдаться, закричать: «Вы чего?! Я невиновен!»"


    if ROUTE_FOX:
        scene bg_classroom base 3 3_no_chair with Dissolve(.5):
            xpos -3911 + 1920 + 1300
        "Ромка посмотрел как-то тяжело, тревожно."
        "Похоже, он, как и все, был сбит с толку пропажей Семёна, огорошен случившимся."
        "И вдруг его взгляд упёрся мне в переносицу."
    if ROUTE_POLINA or ROUTE_SOLO:
        scene bg_classroom base 3 3_no_chair with Dissolve(.5):
            xpos -3911 + 1920 + 1300

        scene bg_classroom base 3 4_no_chair with Dissolve(.5):
            xpos -3911 + 1920 + 1300
        "Хулиганы повернулись и молча уставились на меня."
        "Чистая ненависть сочилась из их глаз."
        "Но за что?"
        "Что я такого им сделал? У них пропал друг, а они всё никак не могут забыть обо мне."
        scene bg_classroom base 3 5_no_chair with Dissolve(.5):
            xpos -3911 + 1920 + 1300
        "Вдруг Бяшин взгляд упёрся мне в переносицу."

    "Казалось, он вот-вот ткнёт в меня пальцем и оглушительно закричит:"
    "«Смотрите, эти очки вчера стащил Бабурин! Они вернулись к Антону! Убийца!»"
    "Но он молчал, словно не находил в моих очках ничего примечательного."
    scene bg_classroom base 3 1_no_chair with Dissolve(.5):
        xpos -3911 + 1920 + 1300

    if ROUTE_SOLO or ROUTE_POLINA:
        "Возможно, я схожу с ума, или Бяша что-то знает. Знает и не хочет об этом говорить."

    if ROUTE_FOX:
        "Возможно, я схожу с ума, или Ромка что-то знает. Знает и не хочет об этом говорить."
        "А может, ему просто всё равно. Как и всем прочим."

        show bg_classroom base 3 1_no_chair with Dissolve(.5)
        "Но тут Ромка подозрительно глянул на Катю, как будто сообщая, что ни капли ей не верит."
        "Мне искренне хотелось, чтобы Ромка меня поддержал."
        "Как и Бяша, что развалился неподалёку, уткнувшись в парту подбородком."
        "Но они молчали."
        "Меня настигла пугающая мысль, что эта парочка может легко меня предать, столкнуть в пропасть."
        "Как они уже поступили с Семёном."

    if ROUTE_POLINA:
        show bg_classroom base 3 3_no_chair:
            xpos -3911 + 1920 + 1300
        "Затем Рома тут же посмотрел на меня многозначительно, будто напоминал о своём обещании."
        "Я помнил: ноющий висок не позволял забыть: держись подальше от Полины."
        show bg_classroom base 3 1_no_chair:
            xpos -3911 + 1920 + 1300
        with Dissolve(0.5)

    "Словно в поисках защиты, я до боли сжал линейку."
    show bg_classroom base 3 2_no_chair:
        xpos -3911 + 1920 + 1300
    with Dissolve(0.5)
    $ add_text_to_dictionary(31)
    voice "voice/kate/87 KA.ogg"
    Kate "Не надо быть {u}Коломбо{/u}, чтобы догадаться..."

    voice "voice/kate/88 KA.ogg"
    Kate "Кто на Бабурина зуб имел?"

    if Flags.Has("fight"):
        voice "voice/kate/89 KA.ogg"
        Kate "Кто его вчера ударил? Поиздевался, а после..."

    scene bg_classroom base 3 1_no_chair_2 with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 1300
    play test_one "sounds/sfx_metal_ruler.ogg"
    "Металлическая линейка выпала из моих ослабевших пальцев, и её звон заставил детей встрепенуться."
    show bg_classroom base 3 4_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 1300
    show bg_classroom base 3 5_no_chair with Dissolve(0.3):
        ypos 0
        xpos -3911 + 1920 + 1300
    show bg_classroom base 3 1_no_chair with Dissolve(0.7):
        ypos 0
        xpos -3911 + 1920 + 1300
    "Катя осеклась и как-то боязливо съёжилась."
    "Заскрипели стулья: одноклассники отодвигались от меня поближе к выходу, к учительскому месту."
    "И не я один уловил перемены: Ромка и Бяша тоже заметили и презрительно поморщились."
    stop music fadeout 2
    if ROUTE_POLINA or ROUTE_SOLO:
        "Плохо, что они не боялись меня, как остальные."
    if ROUTE_FOX:
        "Хорошо, что они явно были за меня."

    voice "voice/byasha/3day/71 Da.ogg"
    Bya "Да прикуси ты."
    stop music fadeout 5
    show bg_classroom base 3 5_no_chair:
        ypos 0
        xpos -3911 + 1920 +1300
    with Dissolve(0.5)
    voice "voice/byasha/3day/72 Ba.ogg"
    Bya "Бабурин, небось, с бабкой посрался и сдымил, на."
    voice "voice/byasha/3day/73 Sc.ogg"
    Bya "Скоро найдётся."
    show bg_classroom base 3 2_no_chair with Dissolve(0.5)
    voice "voice/kate/90 KA.ogg"
    Kate "Найдётся, ага."
    voice "voice/kate/91 KA.ogg"
    Kate "В овраге со вспоротым брюхом!"
    show bg_classroom base 3 1_no_chair with Dissolve(0.5)
    play test_one "sounds/glotok-fix.ogg"

    "Я сглотнул."
    play music "music/Phrases_06(loop).ogg" fadein 1
    scene bg_white with Dissolve(0.12)
    show sem_t with Dissolve(0.5)
    stop fon fadeout 1.5
    "Вообразил Сёму на снежной подушке: лицо белое, как рыбье брюхо, расколотое широкой трещиной рта, а падающие хлопья оседают на стеклянных глазах и заполняют гортань."
    "«Видишь, — словно говорит он мне презрительно, — это всё твоя вина!»"
    play fon "sounds/fon/noise_klass.ogg" fadein 1
    if ROUTE_POLINA or ROUTE_SOLO:
        "Но разве только Семён издевался надо мной и получил сполна?"
        Ant_m "Разве не все они должны исчезнуть: Ромка, Бяша, Катька, остальные зубоскалы?"
    show sem_t with Dissolve(0.5)
    scene bg_white with Dissolve(0.12)
    scene bg_classroom base 3 1_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 +1300
    stop music fadeout 1
    "Конечно, Семён услужил мне своим исчезновением. Благодаря ему взоры одноклассников были полны трепета."
    "Но была и обратная сторона медали."
    "Что, если мне вскоре придётся заплатить за услугу?"
    scene bg_classroom base 3 1_no_chair:
        ypos 0
        xpos -3911 + 1920 +1300
        pause 0.2
        ease 1.5 xpos -3911 + 1920 + 1050
    play test_one "sounds/Door_open_2.ogg"
    "Дверь скрипнула — в класс вошла Полина."
    play test_one "sounds/steps/Polina_step_01.ogg"
    scene bg_classroom base 4_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 1050
    "Я весь подобрался, чтобы не выглядеть перед ней затравленным зверьком."

    if ROUTE_SOLO:
        "Полина, не взглянув на меня, села за парту."

    if not ROUTE_SOLO:
        show bg_classroom base 4_2_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 +1050
        "Полина нашла меня взглядом, коротко кивнула и села за парту."
        show bg_classroom base 4_3_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 +1050
        play test_one "voice/kate/92 KA.ogg"
        "Катя вновь ринулась к соседкам, как крыса к угощениям, и зашушукала, косясь то на Полину, то на меня."
        show bg_classroom base 4_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 +1050
        "По классу запрыгали записки."
    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)
    "Задребезжала трель звонка, извещая о начале урока."
    scene bg_teacher:
        xpos 0

    show Liliya Normal m_evening 00:
        xpos 910
        yoffset 200
    with Dissolve(0.5)

    voice "voice/lydia/3day/01 Tak.ogg"
    Teacher "Так, заканчиваем бардак. Дети, встаньте."
    play sound "sounds/sfx_class_stand_up.ogg"
    voice "voice/lydia/3day/02 Pe.ogg"
    Teacher "Петров, тебя это тоже касается!"

    scene bg_teacher:
        xpos 0
        pause 0.5
        ease 3.0 xpos -250
    show ment 1:
        xalign .5
        alpha 0
        pause 3.6
        linear .8 alpha 1
    show Liliya Normal m_evening 00:
        xpos 910
        yoffset 200
        pause 0.5
        linear .5 alpha 0
    show bg_teacher_teach 02:
        xpos -250
        alpha 0
        pause 2.5
        linear .2 alpha 1


    play music2 "music/Militsioner.ogg" volume 0.6 fadein 0.5
    play test_five "sounds/steps/Techer_in.ogg"
    play test_six [ "<silence 0.2>", "<from 0 to 3>sounds/school_door-close-2.ogg"]
    queue sound [ "<silence 0.3>", "<from 0 to 3>sounds/steps/sfx_ment_coming.ogg"]
    "Лилия Павловна прошла к столу, а за ней в кабинет вошёл милиционер при параде."

    "Тот, что приходил недавно в наш дом. Высокий, с пронзительным взглядом, под которым ты гнёшься, как лоза."

    $ story_manager.MarkEvent(("day3", "scene3"))

    scene bg_teacher:
        xpos -250
    show ment 0:
        xalign .5
    show bg_teacher_teach 02:
        xpos -250
    with Dissolve(0.5)

    $ music_during_lines = 0.55
    voice "voice/tihonov/3day/21Z.ogg"
    Mil "Кхм... Здрастье."
    play test_one "sounds/sfx_taking_hat.ogg"
    show ment 3 with Dissolve(0.9)
    voice "voice/Child/3day/02 Zdras.ogg"
    Childs "Здрав-ствуй-те!"
    show bg_teacher_teach 01 with Dissolve(0.5):
        xpos -250
    voice "voice/lydia/3day/03 S.ogg"
    Teacher "Садитесь."
    play sound "sounds/sfx_class_sit_down.ogg"
    voice "voice/lydia/3day/04 P.ogg"
    Teacher "Познакомьтесь — это старший лейтенант Константин Владимирович Тихонов."
    voice "voice/lydia/3day/05 On.ogg"
    Teacher "Он задаст вам несколько вопросов и проведёт небольшую лекцию по безопасности."
    $ music_during_lines = 1.0
    play fon "sounds/fon/noise_klass.ogg"

    scene bg_classroom base 5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 300
    play test_one "voice/Child/3day/04 Luch.ogg"
    "Одноклассники оживились: лучше лекция от милиционера, чем уроки!"
    "А я готов был высидеть сто часов русской литературы, лишь бы не терпеть на себе давящий взор лейтенанта."
    stop music2 fadeout 4
    play sound "music/Phrases_06.ogg"
    "Карие глаза нащупали меня среди учеников. Волосы на моём затылке зашевелились от ужаса, ледяной кол впился в кишки."
    stop fon fadeout 2
    show bg_classroom base 5_3_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 300

    voice "voice/kate/93 KA.ogg"
    Kate "А правда, что Бабурина маньяк убил?"
    show bg_classroom base 5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 300

    voice "voice/lydia/3day/06 E.ogg"
    Teacher "Екатерина, ну-ка цыц! Вопросы здесь взрослые задают."
    play music "music/Morning Tensions_02.ogg" volume 0.85 fadein 0.5
    show polina_look_kate1 with Dissolve(.5)

    voice "voice/kate/94 KA.ogg"
    Kate "Просто нам всем страшно."

    voice "voice/kate/95 KA.ogg"
    Kate "Может, убийца бродит где-то рядом."

    voice "voice/kate/96 KA.ogg"
    Kate "Или сидит у нас за спиной..."
    show polina_look_kate2 with Dissolve(.5)
    "Хитрый лисий взгляд обращался ко мне."
    show bg_ment 02 with Dissolve(1.)
    play test_five "sounds/steps/loop_man_footsteps2.ogg" loop fadein 5
    "Тихонов шагнул в проход между рядами и медленно, невыносимо медленно пошёл, касаясь пальцами спинок стульев."
    "Ученики едва шеи себе не сворачивали, пристально за ним наблюдая."
    "Так в средневековье зеваки предвкушали публичную экзекуцию."
    show bg_ment 03 with Dissolve(0.5)
    "А он шёл, неумолимо приближаясь."
    play test_two "voice/anton/2day/50.2.ogg"
    "Я сжал зубы, удерживая вскрик."
    show doc 01 with Dissolve(0.5)
    stop test_five fadeout 1
    play test_two "voice/anton/2day/Ah.ogg"
    Ant_m "{i}Спокойно! Дыши!{/i}"
    play test_two "voice/anton/2day/Vtyanul.ogg"
    Ant_m "{i}Ты никого не убивал и не похищал.{/i}"
    scene bg ment 001 with Dissolve(0.5)
    "Заранее зная ответ, Тихонов строго спросил:"

    voice "voice/tihonov/3day/22 P.ogg"
    Tikhonov "Петров Антон?"

    voice "voice/anton/3day/001.D.ogg"
    Ant "Да."
    play test_five "sounds/steps/Kait_stop.ogg"
    scene bg ment 002 with Dissolve(0.5)
    voice "voice/lydia/3day/07 V.ogg"
    Teacher "Встань, Петров."
    play test_one "sounds/sfx_stand_up.ogg"
    show ant_clas_fon:
        xpos -300
    show ant_clas_2:
        xpos 0
    show ant_clas_blink
    with Dissolve(0.5)

    "Мышцы окаменели. Я встал, отклеился от стула, почти услышав треск суставов."
    "Хоть бы Полина не оборачивалась, не видела мою застывшую в ужасе гримасу."
    "Очутиться бы сейчас где-нибудь далеко, в лесу, зарыться в сугроб и сжаться комочком."
    "Лейтенант глазел так, словно уже застёгивал наручники на моих запястьях. Они наверняка холодные, эти браслеты."
    "В голове носились мысли о тюрьме, о детской колонии, где десятки Семёнов не оставят на мне живого места."

    hide ant_clas_2
    show ant_clas_1 rot:
        xpos 0
    with Dissolve(0.5)
    voice "voice/anton/3day/002 Ya.ogg"
    Ant "Я ничего не знаю. Я тут ни при чём."
    scene bg ment 002 with Dissolve(0.5)
    voice "voice/tihonov/3day/23 A.ogg"
    Tikhonov "А тебя никто и не обвиняет..."
    voice "voice/tihonov/3day/24 P.ogg"
    Tikhonov "... пока что."

    show doc 3

    play sound "sounds/sfx_slam_folder.ogg"
    stop music fadeout 0.5

    "Только теперь я заметил папку с надписью «ДЕЛО» в его руке, серую, из шершавого картона."
    play music2 "music/31_FearTheMind_final.ogg" volume 0.6 fadein 0.5
    "Она шлёпнулась о стол — словно опустилось лезвие гильотины."
    play sound "sounds/sfx_folder_laces.ogg"
    show doc 22 with Dissolve(0.5)
    pause 0.5
    show doc 024 with Dissolve(0.5)
    "Неторопливо, продолжая меня изучать, Тихонов открыл папку."
    "Краем глаза я видел бумаги и фотографии. На снимках были следы на снегу, кажется, звериные."
    scene bg ment 002 with Dissolve(0.5)
    voice "voice/tihonov/3day/25 T.ogg"
    Tikhonov "Ты с Семёном Бабуриным общался?"
    if Flags.Has("mask"):
        voice "voice/anton/3day/004 N.ogg"
        Ant "Я знал его всего одну неделю."
    if not Flags.Has("mask"):
        voice "voice/anton/3day/003 od.ogg"
        Ant "Я знал его всего один день."
    show k_fon
    show Kate Normal b_day 00 evil ahead 01 with Dissolve(0.2)
    pause .1
    show Kate Normal b_day 00 evil ahead 02 with Dissolve(0.3)
    voice "voice/kate/97 KA.ogg"
    Kate "Все знают: Петров его ненавидел."
    show Kate Normal b_day 00 evil ahead 01 with Dissolve(0.3)
    "Я покраснел."
    Ant_m "{i}Ах ты мерзкая сука.{/i}"
    "{i}Захотелось вцепиться зубами в Катино лицо и выгрызть ей щёку.{/i}"

    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        xpos 0
    show ant_clas_blink_1:
        xpos 0
        alpha 1
        pause .6
        linear .3 alpha 0
    show ant_clas_blink
    with Dissolve(0.5)
    "Но я сказал, совладав с голосом:"


    if not Flags.Has("fight"):
        hide ant_clas_1 1
        show ant_clas_fon:
            xpos -300
        show ant_clas_1 rot:
            xpos 0
        show ant_clas_blink
        with Dissolve(0.5)
        voice "voice/anton/3day/006 Mi.ogg"
        Ant "Мы повздорили не так давно."
        voice "voice/anton/3day/007 On.ogg"
        Ant "Он меня ударил."
        hide ant_clas_1 rot
        show ant_clas_1 1:
            xpos 0
        with Dissolve(0.5)
        "Сбоку донеслось:"
        scene k_fon
        show Romka Normal b_day 01 norm ahead 03
        with Dissolve(0.5)
        voice "voice/romka/3day/03 Xa.ogg"
        Rom "Хана тебе."
        show Romka Normal b_day 01 norm ahead 02
        voice "voice/lydia/3day/08 Ta.ogg"
        Teacher "Так, Пятифанов, а ну рот закрой!"
        scene bg ment 002 with Dissolve(0.7)
        "Я пошатнулся, чудом устояв на ногах."
    else:


        show ant_clas_fon:
            xpos -300
        show ant_clas_1 rot:
            xpos 0
        with Dissolve(0.5)

        voice "voice/anton/3day/005 m.ogg"
        Ant "Мы повздорили вчера."
        show ant_clas_1 1 with Dissolve(0.3):
            xpos 0
        show ant_clas_1 rot with Dissolve(0.3):
            xpos 0

        voice "voice/anton/3day/008 NOon.ogg"
        Ant "Но он первый начал."

        show ant_clas_1 1 with Dissolve(0.3):
            xpos 0
        show ant_clas_1 rot with Dissolve(0.3):
            xpos 0

        voice "voice/anton/3day/009 Ya.ogg"
        Ant "Я его ударил."

        hide ant_clas_1 rot
        show ant_clas_1 1:
            xpos 0
        show ant_clas_blink
        with Dissolve(0.5)

        voice "voice/tihonov/3day/26 S.ogg"
        Tikhonov "Сильно?"

        hide ant_clas_1 1
        show ant_clas_fon:
            xpos -300
        show ant_clas_1 rot:
            xpos 0
        with Dissolve(0.5)

        voice "voice/anton/3day/010 D.ogg"
        Ant "Да нет. Так..."

        hide ant_clas_1 rot

        show ant_clas_fon:
            xpos -300
        show ant_clas_1 1:
            xpos 0
        with Dissolve(0.5)
        play sound "sounds/sfx_wrap_shirt.ogg"
        "Я неопределённо махнул рукой."

        scene bg ment 004 with Dissolve(0.7)
        "Тихонов посмотрел на мой кулак, будто удивляясь, что я способен стукнуть громилу с фотографии."

    scene bg ment 002 with Dissolve(0.7)
    "Лилия Павловна неожиданно пришла мне на помощь."
    scene bg ment 006 with Dissolve(0.5)

    voice "voice/lydia/3day/09 Ba.ogg"
    Teacher "Бабурин — проблемный подросток. С шилом кое-где."

    if not ROUTE_SOLO:
        voice "voice/lydia/3day/10 S.ogg"
        Teacher "Сам ко всем лез."
    show doc 024 with Dissolve(0.7)
    pause .2
    play test_one "sounds/sfx_turning_pages_3.ogg"
    show doc 24 with Dissolve(0.7)
    pause 1
    play test_one "sounds/sfx_turning_pages_1.ogg"
    show doc 25 with Dissolve(0.7)
    "Старлей многозначительно кивнул и вдруг выудил из папки тетрадь."
    queue sound [ "<silence 2.2>", "<from 0 to 4>sounds/sfx_turning_pages_4.ogg"]
    scene bg ment 002 with Dissolve(0.7)
    show ment_hand:
        xpos 800 ypos 500 rotate 50
        linear 3.0 rotate 1 xpos -400 ypos -250
        block:
            linear 1.0 xpos -405 ypos -255
            linear 1.0 xpos -395 ypos -255
            linear 1.0 xpos -405 ypos -245
            linear 1.0 xpos -395 ypos -250
            linear 1.0 xpos -395 ypos -255
            linear 1.0 xpos -400 ypos -245
            repeat
    $ renpy.pause(3)
    pause 1
    window show

    voice "voice/tihonov/3day/27 A.ogg"
    Tikhonov "Это твоё?"

    "Я отвёл взгляд."
    "Это была подписанная мною тетрадь по математике."
    "Взгляды одноклассников жадно впились в меня. Даже писатели на портретах будто бы подозрительно сощурились."
    voice "voice/anton/3day/011M.ogg"
    Ant "М-моё."

    voice "voice/tihonov/3day/28 V.ogg"
    Tikhonov "В лесу нашли."

    voice "voice/tihonov/3day/29 T.ogg"
    Tikhonov "Там же тракторист, что снег убирал, в последний раз видел Бабурина."

    "Я растерянно заморгал."
    "Рюкзак распотрошил Ромка — тетрадь наверняка затерялась где-то под кустом."
    "Лейтенант в курсе насчёт школьной потасовки, но знает ли он про драку на опушке?"
    "У меня были свидетели, которые могли бы подтвердить, что мы с Семёном разошлись по разные стороны баррикад."

    "В надежде я посмотрел на ребят."
    play test_two"voice/romka/3day/94 Ps.ogg"
    scene bg_classroom base 3 33_no_chair_no_teach with Dissolve(0.7):
        ypos 0
        xpos -3911 + 1920 +1150
        easein .75 xpos -3911 + 1920 + 1300

    "За спиной Тихонова Ромка прикоснулся указательным пальцем к губам."
    scene bg_classroom base 2_1_no_chair_no_teach with Dissolve(0.7):
        xpos -3911 + 1920 + 1300
    "И притворился, что ковыряется в носу, когда лейтенант быстро обернулся."
    "Я расшифровал сигнал."
    "Из уст таких ребят, как Ромка, это прозвучало бы как «смотри не мусарнись»."
    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        xpos 0
    with Dissolve(0.5)
    "Я судорожно поправил очки."
    "Но ведь Семён унёс их вчера с собой, а сейчас они..."

    voice "voice/tihonov/3day/31 Tak.ogg"
    Tikhonov "Так что ты делал вчера в лесу, Антон?"

    show ant_clas_1 rot:
        xpos 0

    voice "voice/anton/3day/012Ya.ogg"
    Ant "Я в школу через лес хожу."

    show ant_clas_1 1 with Dissolve(0.3)
    show ant_clas_1 rot with Dissolve(0.3):
        xpos 0

    voice "voice/anton/3day/012M.ogg"
    Ant "Могла выпасть легко."

    hide ant_clas_1 rot
    scene bg ment 002
    show ment_hand:
        linear 2 ypos 1100
    with Dissolve(0.7)
    "Легко – именно так далась мне эта половинчатая правда."
    window hide
    show doc 25 with Dissolve(0.5)
    pause 1
    play test_one "sounds/sfx_folder_close.ogg"
    show doc 28 with Dissolve(0.5)

    voice "voice/tihonov/3day/32 B.ogg"
    Tikhonov "Будь осторожнее."

    stop music2 fadeout 4.5
    scene bg ment 002 with Dissolve(0.5)
    "И прежде чем я понял, угроза это или пожелание, учительница сказала:"

    voice "voice/lydia/3day/11 K.ogg"
    Teacher "Класс, а сейчас лейтенант расскажет о правилах, которые вам необходимо соблюдать."
    play music "music/15_Zaychik_Fon.ogg" volume 0.7 fadein 6

    show k_fon
    show Kate Normal b_day 00 evil ahead 02
    with Dissolve(0.5)

    voice "voice/kate/98 KA.ogg"
    Kate "Так маньяк всё-таки есть!"

    show Kate Normal b_day 00 evil ahead 01 with Dissolve(0.5)

    voice "voice/tihonov/3day/34 P.ogg"
    Tikhonov "Пока мы ничего вам сказать не можем."
    play test_two "voice/Child/3day/06 Kogd.ogg"

    if ROUTE_FOX:
        show bg_classroom base 4_no_chair:
            ypos 0
            xpos -3911 + 1920 +1150
            easein .75 xpos -3911 + 1920 + 1300
        $ renpy.pause(delay=0.7, hard=True)
        show bg_classroom base 5_6_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 + 1300

        "Ромка качнулся на стуле и показал мне большой палец: молоток, мол, держал язык за зубами."
        "Я кивнул, хотя не ощутил ни малейшей гордости от его похвалы."
        show bg_classroom base 4_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 + 1300
        "В конце концов, именно Ромка раскидал мои тетради и учебники по снегу, и он же руководил Семёном, пускай потом и поменял союзников."
        show bg_classroom base 4_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 + 1300
            pause 0.4
            easein .75 xpos -3911 + 1920 +1150

    show bg_ment 04 with Dissolve(0.5):
        pause 0.95
    hide bg_classroom

    voice "voice/tihonov/3day/35 no.ogg"
    Tikhonov "Но есть преступник или нет, вы должны чётко помнить о собственной безопасности."

    voice "voice/tihonov/3day/36 V.ogg"
    Tikhonov "Вас бережёт милиция, вас опекают родители и учителя, но в первую очередь защищать себя должны вы сами."

    show bg_ment 04 with Dissolve(0.5)

    voice "voice/tihonov/3day/37 Ita.ogg"
    Tikhonov "Итак... Кто там что хотел узнать?"

    play fon "sounds/fon/noise_klass.ogg" fadein 2.0
    "Лес рук взвился над партами."
    play test_two "voice/Child/3day/Pokaz.ogg"
    "Дети загалдели, забрасывая милиционера вопросами."
    show doc 22 with Dissolve(0.5)
    "Стараясь усмирить хор, он двинулся к доске."
    play test_one "sounds/steps/sfx_ment_leaving.ogg"
    show doc 23 with Dissolve(0.5)
    "Серая папка осталась лежать передо мной."
    play test_two "voice/anton/2day/fear5.ogg"
    "Я смотрел на неё и дышал как человек, пробежавший стометровку."
    "Под свитером струился пот."

    label day_3_continue.minigame_start:
    show bg_classroom base mini_game
    show case_folder_idle
    with Dissolve(0.5)
    hide doc





















    $ mplay("voice/tihonov/3day/NoPanic.ogg")

    "Я оглядел кабинет." id day_3_continue_0e33c663
    "Все дети внимали лектору." id day_3_continue_c6337233
    play test_five "voice/romka/3day/87 At.ogg"
    "Только Ромка что-то говорил Бяше." id day_3_continue_64b5806a
    stop fon fadeout 3
    "А Лилия Павловна, сражаясь с зевотой, пялилась в окно." id day_3_continue_d8d63774
    play fon "sounds/fon/Hush_klass.ogg"
    stop music fadeout 6

    $ mplay("voice/tihonov/3day/Walk.ogg", chan="test_five")

    $ story_manager.MarkEvent(("day3", "game case"))


    jump minigame_case_start


label minigame_folder_hit1:
    $ story_manager.MarkEvent(("day3", "game case", "hit1"))
    $ mstop(chan = "test_five")
    $ Flags.Raise("doc")
    window hide
    show doc 23
    play sound "sounds/sfx_open_folder.ogg"
    $ renpy.pause(0.2)
    show doc 26 with Dissolve(0.5)

    "Никто не обращал на меня внимания, и я открыл папку одной рукой."
    play music "music/Kontakt_4.ogg"
    "Пальцы заспешили, перебирая бумаги."
    play sound "sounds/sfx_listing_photos_2.ogg"
    show bg_rep_senya behind bg_glich_0
    with Dissolve(.5)
    "Ксения Талалаева, шесть лет. Ушла из дома в конце декабря. Особые приметы, ага..."
    "Сердце подскочило в груди. На фотографии улыбалась круглолицая девочка не старше Оли."
    "Первая жертва маньяка? Первый ребёнок, растворившийся бесследно в ночном лесу?"
    play sound "sounds/sfx_listing_photos_1.ogg"
    hide bg_rep_senya behind bg_glich_0
    with Dissolve(.5)

    "Я перелистнул документы."
    play sound "sounds/sfx_listing_photos_3.ogg"
    show vova_foto1 behind bg_glich_0
    with Dissolve(.5)
    "Владимир Матюхин, 10 лет."
    "Вова был вторым."
    "Его варежка болталась на суку, его имя выкрикивали отчаявшиеся взрослые и повторяло глумливое эхо..."
    play sound "sounds/sfx_listing_photos_5.ogg"
    hide vova_foto1 behind bg_glich_0
    with Dissolve(.5)
    play test_two "voice/lydia/3day/12 ka.ogg"
    "Лилия Павловна кашлянула, призывая к дисциплине расшумевшихся учеников."
    play test_one "sounds/sfx_folder_close.ogg"
    show doc 23 with Dissolve(0.5)
    "Я одёрнул руку. Папка закрылась."
    stop music fadeout 2
    $ mplay("voice/tihonov/3day/Wild.ogg", chan="test_five")


    hide doc










    return


label minigame_folder_hit2:
    $ story_manager.MarkEvent(("day3", "game case", "hit2"))
    $ mpause(channel="test_five")
    stop test_five fadeout 1
    $ Flags.Raise("finger")
    show doc 23
    stop test_one fadeout 1
    "Милиционер встал к классу спиной и заскрёб мелом по доске. Противно заскрежетало."
    voice "voice/tihonov/3day/45 N.ogg"
    Tikhonov "Не-зна-ком-цы."
    voice "voice/tihonov/3day/46 V.ogg"
    Tikhonov "В деревне почти все друг друга знают в лицо, так что чужаков обычно сразу замечают."
    voice "voice/tihonov/3day/47 U.ogg"
    Tikhonov "Увидев незнакомца..."
    play sound "sounds/sfx_open_folder.ogg"
    show doc 26 with Dissolve(0.5)
    play test_two "sounds/sfx_chalk_writing.ogg"
    "Лейтенант снова заскрипел мелом, а я, убедившись, что никто не наблюдает, открыл папку и вынул фотографии, прятавшиеся на дне."
    stop test_two fadeout 3
    play music "music/Kontakt_4.ogg"




    if Flags.Has("record"):
        "Они напоминали стоп-кадры из той странной передачи."
        "Только вместо крестов на белом фоне — корявые рябины."
    "Артерии корневищ. Пни и подрезанные молниями сосенки горельника."
    "Снег, много снега."
    "И вдруг..."
    play sound "sounds/sfx_listing_photos_6.ogg"
    show Gar_Photo with Dissolve(0.5)
    "От чёрной постройки тянуло могильным холодом. Но это был не склеп."
    play test_three "sounds/Garage.ogg"
    "Гараж."
    "Железный, и, судя по деревьям вокруг, установленный прямо в чаще."
    "Чёрные ворота словно засасывали меня внутрь."


    if ROUTE_FOX:
        "Я уже сталкивался раньше с этим скитающимся по округе контейнером."
        "Вчера."
        "Сначала о нём рассказал Ромка. Он говорил, что в пропаже детей виновен Чёрный гараж, словно тот был живым существом."
        "А затем, посреди густого леса, я лично встретился с этой постройкой цвета зияющей бездны."
        "И лисичка сказала, что там прятался Вова."

    hide Gar_Photo with Dissolve(0.5)
    play sound "sounds/sfx_listing_photos_4.ogg"
    "Пальцы дрогнули, и фотография спланировала назад в папку."
    "К счастью, упала изнанкой кверху — смотреть на стальную коробку было физически неприятно."
    play test_five "sounds/sfx_small_bag_opened.ogg"
    show doc 27 with Dissolve(0.5)
    show pack 001 with Dissolve(0.5):
        yalign .4
        xalign .5
    "На дне папки лежал ещё и целлофановый пакет, в каких хранят вещдоки."
    play test_five "sounds/sfx_small_bag_taken.ogg"
    show pack 002 with Dissolve(0.5):
        yalign .4
        xalign .5

    "Я открыл его..."
    stop fon fadeout 3.0

    scene ant_hand_fon with Dissolve(0.5)
    "... а внутри..."
    play music2 "music/finger(Riser).ogg" noloop
    show ant_hand 2:
        ypos 1080
        linear 1.5 ypos 0
        block:
            linear 1.0 xpos -10 ypos 2
            linear 1.0 xpos -8 ypos 2
            linear 1.0 xpos -6 ypos 0
            linear 1.0 xpos -4 ypos 4
            linear 1.0 xpos -2 ypos 2
            linear 1.0 xpos 0 ypos 0
            repeat
    $ renpy.pause(delay=3.0, hard=True)
    "... отрезанный палец!"
    show ant_hand anim
    play music2 "music/Phrases_01.ogg" noloop
    "Моргнул — и мираж тут же рассеялся."
    "Больше не было человеческого обрубка, зато был перстень."
    "Ошпаренный секундной галлюцинацией, я точно перенёсся в лес и услышал слова Семёна:"
    play test_one "sounds/flashback.ogg"
    show sem_memo

    voice "voice/semen/SCHa.ogg"
    Sem "Ща, парашник, я тебе этой печаткой так заряжу!.."
    show ant_hand 1:
        ypos 0
        linear 3 ypos 1080
    "Перстень тускло блестел на ладони."
    stop music fadeout 2
    "Я судорожно сжал улику в кулаке, словно ища подтверждение, что она настоящая."
    play wtf "sounds/sfx_slam_folder.ogg"
    show desk2 anim
    "От неожиданности я клацнул зубами. Вдавился в спинку стула, затравленно моргая."
    play sound "sounds/sfx_grab_folder.ogg"
    show doc 01 with Dissolve(0.5)
    "Милиционер молча сгрёб папку, нахмурился."
    scene bg ment 005 with Dissolve(0.5)
    voice "voice/tihonov/3day/54 B.ogg"
    Tikhonov "Больно ты любопытный, Петров."

    scene ant_clas_fon:
        xpos -300
    show ant_clas_2:
        xpos 0
    with Dissolve(0.5)
    play fon "sounds/fon/Hush_klass.ogg" fadein 4.0
    "Что есть силы я попытался выдавить слова, извиниться, вернуть перстень."
    "Но получилось лишь протянуть сжатый кулак с кольцом и затарахтеть, как двигатель у папиной машины в мороз."
    hide ant_clas_2
    show ant_clas_1 rot:
        xpos 0
        ypos 0
        block:
            linear 0.1 ypos 4
            linear 0.1 ypos 0
            repeat
    voice "voice/anton/3day/013V.ogg"
    Ant "Во-во-во-во..."
    play music2 "music/Fail7.ogg" volume 0.75 noloop
    scene bg ment 001 with Dissolve(0.5)
    voice "voice/tihonov/3day/01 Kak.ogg"
    Tikhonov "Как говорится..."
    voice "voice/tihonov/3day/02 Me.ogg"
    Tikhonov "... меньше знаешь — крепче спишь."
    scene ant_clas_fon:
        xpos -300
    show ant_clas_1 rot:
        xpos 0
        ypos 0
        block:
            linear 0.1 ypos 4
            linear 0.1 ypos 0
            repeat 6
        "ant_clas_2"
    with Dissolve(0.5)

    voice "voice/anton/3day/014 Vo.ogg"
    Ant "Во-во... вот."
    $ achievement_grant("ach_ring")
    play sound "sounds/steps/sfx_ment_leaving.ogg"
    "Он пошёл к доске, не оглядываясь, а я всё сжимал украденную улику и думал о Семёне."
    "Который теперь наверняка уже мёртв."
    jump minigame_after

label minigame_folder_fail1:
    show guard_alert:
        align (.5,.5)
        linear .1 zoom 1.2
        linear .2 zoom 1.
    show focus_lines_bright:
        align (.5,.5)
        alpha 0
        linear .2 alpha 1
    $ mpause(channel="test_five")
    play wtf "sounds/alert.ogg"
    "Как только я коснулся папки, Тихонов хлестнул меня взглядом, словно розгой."
    "Рука непроизвольно отдёрнулась, будто и вправду почувствовала боль."
    "Лейтенант ещё некоторое время молчал, не сводя с меня глаз, и мне было не по себе от этой тишины и насмешливо косящихся одноклассников."
    stop wtf fadeout 1

    if phase < 4:
        "А потом милиционер так же резко заговорил, как ни в чём не бывало."
    $ munpause(channel="test_five")
    hide guard_alert
    hide focus_lines_bright
    return


label minigame_folder_fail2:
    $ story_manager.MarkEvent(("day3", "game case", "fail"))

    $ mstop(chan="test_five")
    play wtf "sounds/sfx_slam_folder.ogg"
    show desk2 anim
    "От неожиданности я клацнул зубами. Вдавился в спинку стула, затравленно моргая."
    show doc 02
    pause 1
    show doc 01 with Dissolve(0.5)
    "Милиционер молча сгрёб папку, нахмурился."
    scene bg ment 005 with Dissolve(0.5)
    voice "voice/tihonov/3day/54 B.ogg"
    Tikhonov "Больно ты любопытный, Петров."
    $ achievement_grant("ach_missed")

    jump minigame_after


label minigame_timeout:
    $ story_manager.MarkEvent(("day3", "game case", "timeout"))
    show doc_no_open with Dissolve(0.5)
    play test_five "sounds/Militsioner-Fin.ogg"
    "Милиционер закончил лекцию и суетливо заозирался."
    show doc 02 with Dissolve(0.5)
    pause 1
    show doc 01 with Dissolve(0.5)
    play sound "sounds/sfx_grab_folder.ogg"
    "Наконец он приметил оставленную на моей парте папку, молча сунул её под мышку и, не оглядываясь, пошёл к доске."
    jump minigame_after

label minigame_after:
    if not (story_manager.IsMarkedLocal(("day3", "game case", "hit1")) or story_manager.IsMarkedLocal(("day3", "game case", "hit2"))):
        $ story_manager.MarkEvent(("day3", "game case", "hit0"))
    $ story_manager.MarkEvent(("day3", "scene4"))

    stop test_two
    stop test_five

    scene bg_classroom base 5_no_chair:
        ypos 0
        xpos -3911 + 1920 + 304
    with Dissolve(0.5)

    voice "voice/tihonov/3day/55 E.ogg"
    Tikhonov "И ещё раз."
    voice "voice/tihonov/3day/56 E.ogg"
    Tikhonov "Если вы заметите в посёлке кого-то подозрительного — неважно, возле школы или на лесной тропинке — сразу сообщайте в милицию."
    voice "voice/tihonov/3day/57 T.ogg"
    Tikhonov "Телефон-то знаете?"
    voice "voice/Child/3day/30 NolDva.ogg"
    Childs "Ноль-два!"
    voice "voice/tihonov/3day/58 S.ogg"
    Tikhonov "Спасибо, ребята."
    voice "voice/tihonov/3day/59 S.ogg"
    Tikhonov "Спасибо, Лилия Павловна."
    voice "voice/tihonov/3day/60 E.ogg"
    Tikhonov "И это, кхм... Одноклассника вашего мы найдём."

    "«Ну да», — подумал я."
    Ant_m "{i}Поройтесь хорошенько в оврагах — может, соберёте...{/i}"
    Ant_m "{i}... как «Лего»{/i}."
    "Мысли были злыми и какими-то неуправляемыми."
    "Я переключился на фразу лейтенанта о подозрительных личностях."
    "Вдруг я видел маньяка? Стоял с ним плечом к плечу?"
    "Подозрительные люди, хм..."
    "Насколько подозрительной была девочка-лиса, разгуливавшая в темноте?"
    "Чудачка из ниоткуда, что растворялась в воздухе со своими загадками и стишками?"
    "Но могла ли она причинить вред здоровенному Семёну?"
    "Сказать ли мне об этом лейтенанту?"
    scene bg_classroom base 5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 304
        pause 0.5
        linear 3.5 xpos -3911 + 1920 + 900
    if Flags.Has("record") or Flags.Has("doc"):
        "Вдруг от моих слов зависят жизни детей: милой девочки Ксении и Вовы?"
    "Или меня поднимут на смех? Снова начнут шептаться за спиной? А может — того ужаснее, — сочтут сумасшедшим?"
    scene bg_classroom base 5_6_Teach_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900
    "Ромка грозно поглядел на меня через плечо. Вряд ли такой, как он, одобрит сотрудничество с милицией."
    "За сидящими впереди хулиганами беспокойно сновала коса Кати."
    "Рука словно прилипла к парте."
    play test_two "voice/lydia/3day/13 Dos.ogg"
    "Тихонов уже прощался с Лилией Павловной."
    "Уйдёт."
    "Опоздаю..."
    label minigame_after.choice:

    $ story_manager.MarkEvent(("day3", "photorobot"))
    call screen day3_photorobot
label silent:
    $ story_manager.MarkEvent(("day3", "photorobot", "silent"))
    $ Flags.Raise("silent")
label tell_or_silent:
    scene bg_classroom base 5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900

    if Flags.Has("silent"):
        "Ну уж нет."
        "Хватит с меня позора."
        play sound "sounds/steps/sfx_ment_leaving.ogg"
        scene bg_classroom base 5_4_2_no_chair with Dissolve(0.5):
            ypos 0
            xpos -3911 + 1920 + 900
        "Тише воды, ниже травы. Как зайчик."
        "Я сцепил замком пальцы и прикусил язык."
        $ achievement_grant("ach_quiet")

        play test_one "sounds/bell.ogg"
        stop fon
        scene bg_bell with Dissolve(0.8)
        "Зазвенел звонок."

        jump day3_draw_wrong_class

    $ story_manager.MarkEvent(("day3", "photorobot", "tell"))
    "Я отклеил ладонь от столешницы."
    "Его надо предупредить. Хотя бы ради Оли, ради её безопасности в доме у скрипучих сосен."
    play test_two "sounds/ruki.ogg"
    "Я поднял руку, тяжёлую, как гиря."
    voice "voice/anton/3day/015 Pr.ogg"
    Ant "Простите..."
    stop fon fadeout 1.0
    play test_five "sounds/sfx_class_turn_1.ogg"
    scene bg_classroom base 5_5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900

    "Два десятка голов повернулись ко мне."
    "Учительница, лейтенант, Полина..."
    play music "music/Morning Tensions_02.ogg" volume 0.85 fadein 2
    "Катя толкнула локтём соседку."
    "Заспанный Бяша вытянул шею."
    "Вопросительно нахмурился Ромка."
    window auto
    voice "voice/tihonov/3day/61 Ya.ogg"
    Tikhonov "Я слушаю."
    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        xpos 0
    with Dissolve(0.5)
    "Меня будто изучали, положив под микроскоп."
    show ant_clas_1 rot2:
        xpos 0
    with Dissolve(0.5)
    voice "voice/anton/3day/016 Vch.ogg"
    Ant "Вчера утром по дороге в школу я видел... гм, незнакомого человека."
    show ant_clas_1 1:
        xpos 0
    with Dissolve(0.5)
    play fon "sounds/fon/Hush_klass.ogg" fadein 2.0
    "Одноклассники зашептались."
    "Тихонов нахмурился, глубокая морщина расчертила его лоб."
    show bg_teacher 01 08_m with Dissolve(0.5):
        xpos -250
    voice "voice/lydia/3day/14 D.ogg"
    Teacher "Да откуда ему знать, чужак это или кто-то из местных."
    voice "voice/lydia/3day/15 On.ogg"
    Teacher "Он же в посёлке без году неделя."
    "Дети захмыкали, злобно ощерилась Катя."
    scene bg_classroom base 5_5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    voice "voice/tihonov/3day/62 S.ogg"
    Tikhonov "Спокойствие!"
    voice "voice/tihonov/3day/63 A.ogg"
    Tikhonov "Антон, а сможешь детальнее описать?"
    show ant_clas_fon:
        xpos -300
    show ant_clas_1 1:
        xpos 0
    with Dissolve(0.5)
    "Меня осенило."
    "Я не только могу описать. А ещё..."
    show ant_clas_1 rot2 with Dissolve(0.5):
        xpos 0
    voice "voice/anton/3day/017 Ya.ogg"
    Ant "Я нарисовать могу!"
    show ant_clas_1 1 with Dissolve(0.5):
        xpos 0
    show ant_clas_1 rot2 with Dissolve(0.5):
        xpos 0
    voice "voice/anton/3day/017Yar.ogg"
    Ant "Я рисую... немного."
    show ant_clas_1 1 with Dissolve(0.5):
        xpos 0
    "Выплюнув это признание, я ожидал, что класс взорвётся гоготом, но никто не засмеялся, даже Катя."
    scene polina_look_bg
    show polina_look_1
    with Dissolve(0.5)
    "Полина заинтересованно смотрела, склонив голову."
    "Внимание одноклассников польстило мне и, осмелев, я спросил:"
    voice "voice/anton/3day/018 .ogg"
    Ant "Нарисовать?"
    scene bg_teacher 01 08_m with Dissolve(0.5):
        xpos -250
    "Тихонов медленно кивнул."
    voice "voice/tihonov/3day/64 L.ogg"
    Tikhonov "Лилия Павловна, мы тут проведём следственный эксперимент?"
    voice "voice/lydia/3day/16 P.ogg"
    Teacher "Пожалуйста, пожалуйста."
    "Я вынул ручку, разгладил альбомный листок."
    play test_two "sounds/pen_bumaga.ogg"
    stop music fadeout 6
    show bg parta with Dissolve(0.5)
    pause 1
    show lists with Dissolve(0.5)
    stop fon fadeout 3
    "Одноклассники вытаращились на меня в предвкушении."
    "Полина улыбнулась, и улыбка эта была мне наградой за проявленную смелость."
    voice "voice/tihonov/3day/65 Na.ogg"
    Tikhonov "Ну что, Ван Гог, рисуй."
    play music2 "music/Militsioner.ogg" volume 0.8 fadein 0.5

    label tell_or_silent.minigame_photorobot:


    $ story_manager.MarkEvent(("day3", "game photorobot"))

    scene photorobot with Dissolve(0.5)
    $ start_photorobot_game()
    call end_photorobot_game from _call_end_photorobot_game








    if get_foto_numbers() == (3, 4, 2, 5):
        $ Flags.Raise("witness")
        jump day3_photo_witness

    if get_foto_numbers() == (6, 2, 4, 3):
        jump day3_photo_fox

    $ Flags.Raise("photo trudovic")

    if config.developer or preferences.language in (None, "english", "italiano", "turkish", "japan"):
        if get_foto_numbers() == (4, 1, 3, 6):
            $ Flags.Raise("photo letov")
            $ Flags.Drop("photo trudovic")
        elif get_foto_numbers() == (5, 3, 1, 4):
            $ Flags.Raise("photo tsoi")
            $ Flags.Drop("photo trudovic")
        elif get_foto_numbers() == (1, 6, 6, 2):
            $ Flags.Raise("photo bodrov")
            $ Flags.Drop("photo trudovic")

    jump day3_photo_trudovic


label day3_photo_fox:
    $ story_manager.MarkEvent(("day3", "game photorobot", "fox"))
    stop music2 fadeout 4
    voice "voice/anton/3day/019 Vo.ogg"
    Ant "Вот, пожалуйста."
    $ achievement_grant("ach_van_gogh")
    scene bg parta with Dissolve(0.5)
    "Я протянул рисунок милиционеру."
    scene bg ment 041 with Dissolve(0.5)
    play test_one "sounds/Fail3.ogg"
    voice "voice/tihonov/3day/67 E.ogg"
    Tikhonov "Это что? Лиса? Смешно, юморист..."
    scene bg ment 031 with Dissolve(0.5)
    voice "voice/tihonov/3day/69 P.ogg"
    Tikhonov "Прикажешь её по лесу с собаками ловить?"
    play test_two "voice/Child/3day/05 HaHaHa.ogg"
    "Казалось, от дружного хохота задребезжали стёкла. Даже Лилия Павловна смеялась."
    voice "voice/anton/3day/020 Vse.ogg"
    Ant "Всё не так..."
    stop test_two fadeout 6
    show k_fon
    show Kate Normal b_day 00 evil ahead 02:
        pause 2
        block:
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 18
            ease 0.1 yoffset 0
            ease 0.1 yoffset 22
            ease 0.1 yoffset 0
            ease 0.1 yoffset 21
            ease 0.1 yoffset 0
            ease 0.1 yoffset 19
            ease 0.1 yoffset 0
            ease 0.1 yoffset 21
            ease 0.1 yoffset 0
            repeat
    with Dissolve(0.5)

    $ add_text_to_dictionary(32)
    voice "voice/kate/100 KA.ogg"
    Kate "Петров, а {u}Чебурашка{/u} тебе не попадался? Ха-ха-ха!"

    show Kate Normal b_day 00 evil ahead 01
    with Dissolve(0.5)
    pause 0.1
    show Kate Normal b_day 00 evil ahead 02:
        pause 2
        block:
            ease 0.1 yoffset 18
            ease 0.1 yoffset 0
            ease 0.1 yoffset 21
            ease 0.1 yoffset 0
            ease 0.1 yoffset 22
            ease 0.1 yoffset 0
            ease 0.1 yoffset 19
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 19
            ease 0.1 yoffset 0
            repeat
    with Dissolve(0.5)
    play test_one "sounds/Fail1.ogg"
    voice "voice/kate/100 KAA.ogg"
    Kate "Вот умора, а-ха-ха-ха-ха!"
    show bg_classroom base 5_5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    "Я сгорал на костре позора."

    show bg_classroom base 5_4_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    voice "voice/tihonov/3day/70 V.ogg"
    Tikhonov "Всё ясно. Что тут ещё скажешь?"

    play test_two "sounds/Kal_paper-crumpling.ogg"
    "Тихонов смял мой рисунок в кулаке."

    voice "voice/tihonov/3day/71 N.ogg"
    Tikhonov "Ну, занимайтесь."
    play sound "sounds/steps/sfx_ment_leaving.ogg"
    show bg_classroom base 5_4_2_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    "Он ушёл."
    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)
    "Зазвенел звонок."
    show polina_look_kate3 with Dissolve(.5)
    voice "voice/kate/101 KA.ogg"
    Kate "Придурочный."
    scene bg_classroom base 5_4_3_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    "Я не двигался. Лишь смотрел в одну точку."

    jump day3_draw_wrong_class


label day3_photo_witness:
    $ story_manager.MarkEvent(("day3", "game photorobot", "witness"))

    "Вот оно, это резкое, холодное, будто высеченное из камня, лицо."
    stop music2 fadeout 4
    "С острым, как бритва, прищуром."
    scene bg parta with Dissolve(0.5)
    play test_six "sounds/paper-take-4.ogg"
    "Я неуверенно протянул готовый рисунок милиционеру."
    scene bg ment 041 with Dissolve(0.5)
    voice "voice/anton/3day/021 Pr.ogg"
    Ant "Вот... примерно так."
    play sound "sounds/sfx_turning_pages_1.ogg"
    $ achievement_grant("ach_van_gogh")
    scene bg ment 021 with Dissolve(0.5)
    play music2 "music/Lucky.ogg" volume 0.8
    voice "voice/tihonov/3day/75 P.ogg"
    Tikhonov "Примерно?"
    voice "voice/tihonov/3day/75 DA.ogg"
    Tikhonov "Да ведь он — один в один тот тип."
    voice "voice/anton/3day/022 Tak.ogg"
    Ant "Так вы его тоже видели?"
    voice "voice/tihonov/3day/76 Z.ogg"
    Tikhonov "Заячью губу? Видел недавно возле посёлка."
    voice "voice/tihonov/3day/77 Du.ogg"
    Tikhonov "Думал, он проездом, давно подался дальше гастролировать."
    voice "voice/tihonov/3day/78 A.ogg"
    Tikhonov "А он, выходит, здесь отирается."
    if ROUTE_FOX:
        voice "voice/anton/3day/023 A.ogg"
        Ant "А ещё он рядом со школой стоял. И в лесу вечером."
    "Тихонов посмотрел на меня так, будто видел впервые."
    voice "voice/tihonov/3day/79 N.ogg"
    Tikhonov "Ну пацан... Ну молодец! Уже хоть какая-то зацепка."

    play sound "sounds/sfx_one_pat.ogg"
    "И, хлопнув меня по плечу, он затопал к дверям."
    play sound "sounds/steps/sfx_ment_leaving.ogg"
    scene bg_classroom base 5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    "Замер, затем окликнул:"
    voice "voice/tihonov/3day/80 T.ogg"
    Tikhonov "Талантливый ты парень."
    voice "voice/tihonov/3day/81 Te.ogg"
    Tikhonov "Тебя в академии художеств с руками оторвут!"
    play sound "sounds/steps/sfx_ment_leaving.ogg"

    scene bg_classroom base 5_4_2_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900

    "Он ушёл."
    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)
    "Зазвенел звонок."

    jump day3_draw_witness_class


label day3_photo_trudovic:
    stop music2 fadeout 3
    voice "voice/anton/3day/019 Vo.ogg"
    Ant "Вот, пожалуйста."
    play test_six "sounds/paper-take-4.ogg"
    $ achievement_grant("ach_van_gogh")
    scene bg parta with Dissolve(0.5)
    "Я протянул рисунок милиционеру."
    play sound "sounds/sfx_turning_pages_1.ogg"
    scene bg ment 004 with Dissolve(0.5)

    if Flags.Has("photo trudovic"):
        $ story_manager.MarkEvent(("day3", "game photorobot", "trudovic"))
        play music2 "music/Fail7.ogg" volume 0.75 noloop
        voice "voice/tihonov/3day/72 H.ogg"
        Tikhonov "Хм, и кто это, по-твоему?"
        scene bg ment 006 with Dissolve(0.3)
        voice "voice/tihonov/3day/02 Lil.ogg"
        Tikhonov "Лилия Павловна, не узнаёте? Случаем, не ваш трудовик?"
        scene bg_teacher 01 08_m with Dissolve(0.5)
        play sound "sounds/sfx_turning_pages_2.ogg"
        "Учительница прищурилась, силясь разглядеть мою работу."
        voice "voice/lydia/3day/18 Ka.ogg"
        Teacher "Какая отвратительная рожа."
        show k_fon:
            zoom 1.2
        show Byash ha:
            pause 2.5
            block:
                ease 0.1 yoffset 20
                ease 0.1 yoffset 0
                ease 0.1 yoffset 18
                ease 0.1 yoffset 0
                ease 0.1 yoffset 22
                ease 0.1 yoffset 0
                ease 0.1 yoffset 21
                ease 0.1 yoffset 0
                ease 0.1 yoffset 19
                ease 0.1 yoffset 0
                ease 0.1 yoffset 21
                ease 0.1 yoffset 0
                repeat
        with Dissolve(0.5)
        play test_one "sounds/Fail2.ogg"
        voice "voice/byasha/3day/75 Da.ogg"
        Bya "Да это батя Петрова! А-ха-ха-ха-ха!"
        play test_two "voice/Child/3day/05 HaHaHa.ogg"
        play test_three "voice/byasha/3day/HaHaHa.ogg"
        if ROUTE_FOX:
            scene k_fon:
                yoffset -5
                zoom 1.2
                parallel:
                    ease 0.06 yoffset 0
                    ease 0.12 yoffset -10
                    ease 0.06 yoffset -5
            show Byasha Scared b_day 01 shock ahead 01:
                xoffset 0
                yoffset 5
                ease 0.24 xoffset -80
                parallel:
                    ease 0.06 yoffset 10
                    ease 0.12 yoffset 0
                    ease 0.06 yoffset 5
            play sound "sounds/sfx_punch.ogg"
            stop test_three
            pause .5
            show Byasha Doubt b_day 01 normal ahead 01:
                xoffset -80
                yoffset 5
                ease 0.24 xoffset 0

            "Ромка звонким подзатыльником осёк Бяшу, заливающегося смехом, и тот наконец прикусил язык."

    if config.developer or preferences.language in (None, "english", "italiano", "turkish", "japan"):
        if Flags.Has("photo letov"):
            $ story_manager.MarkEvent(("day3", "game photorobot", "letov"))

            voice "voice/tihonov/3day/02 Eto.ogg"
            Tikhonov "Это что за мечта парикмахера такая?"

            $ achievement_grant("ach_letov")

            voice "voice/tihonov/3day/02 Sa.ogg"
            Tikhonov "Сам Джон Леннон не иначе. Хотя стой! Была у нас в отделе листовка по неформальным коллективам... Летов это, братец."
            voice "voice/tihonov/3day/02 U.ogg"
            Tikhonov "У него-то может всё идёт по плану, а у меня чёрт знает что."

        if Flags.Has("photo tsoi"):
            $ story_manager.MarkEvent(("day3", "game photorobot", "tsoi"))
            voice "voice/tihonov/3day/01 Ko.ogg"
            Tikhonov "Кого это ты нам намалевал? Неужто товарища Ким Чен Ира?"

            $ achievement_grant("ach_last_hero")

            voice "voice/tihonov/3day/01 Tu.ogg"
            Tikhonov "Тю, да это ж Цой! Мда, Виктор Робертович - не признал, богатым будешь."
            voice "voice/tihonov/3day/01 Bud.ogg"
            Tikhonov "Тут только и остаётся что спеть: Будь осторожен, следи за собой, Антон..."

        if Flags.Has("photo bodrov"):
            $ story_manager.MarkEvent(("day3", "game photorobot", "bodrov"))

            $ achievement_grant("ach_bodrov")

            voice "voice/tihonov/3day/03 k.ogg"
            Tikhonov "Кого это ты мне подсунуть решил? Бодрова?"
            voice "voice/tihonov/3day/03 e.ogg"
            Tikhonov "Или думаешь я в видеосалоны не хожу и совсем про современное кино ни сном, ни духом?"
            voice "voice/tihonov/3day/03 v.ogg"
            Tikhonov "Вот что я тебе скажу: Поживешь подольше - увидишь побольше."

    play test_two "voice/Child/3day/05 HaHaHa.ogg"
    "Казалось, от дружного хохота задребезжали стёкла."
    scene bg_classroom base 5_5_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    pause 2.5
    scene bg_classroom base 5_4_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    stop test_one fadeout 2
    stop test_two fadeout 2
    stop test_three fadeout 2
    voice "voice/lydia/3day/19 A.ogg"
    "Лилия Павловна шикнула на класс, и смех приумолк, но я сгорал на костре позора."
    voice "voice/tihonov/3day/70 V.ogg"
    Tikhonov "Всё ясно. Что тут ещё скажешь?"
    play sound "sounds/sfx_turning_pages_1.ogg"
    "Тихонов небрежно сложил мой рисунок и кинул в папку."
    voice "voice/tihonov/3day/71 N.ogg"
    Tikhonov "Ну, занимайтесь."
    play sound "sounds/steps/sfx_ment_leaving.ogg"
    show bg_classroom base 5_4_2_no_chair with Dissolve(0.5)
    "Он ушёл."
    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)
    "Зазвенел звонок."
    show polina_look_kate3 with Dissolve(.5)
    voice "voice/kate/101 KA.ogg"
    Kate "Придурочный."
    show bg_classroom base 5_4_3_no_chair with Dissolve(0.5):
        ypos 0
        xpos -3911 + 1920 + 900
    "Я не двигался. Лишь смотрел в одну точку."

    jump day3_draw_wrong_class

label day3_draw_wrong_class:
    $ story_manager.MarkEvent(("day3", "scene_wrong"))
    scene bg_classroom base 5_4_3_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900

    play sound "sounds/steps/Techer_out.ogg"
    "Лилия Павловна прошагала, не посмотрев в мою сторону. За ней вышла Полина."
    play test_one "sounds/steps/Techer_out.ogg"
    scene bg_classroom base 4_00_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900
    scene bg_classroom base 4_01_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900
    "Ученики притихли разом, словно на пульте убавили звук."
    "Они следили, как я иду по проходу."
    "Прокурорские взгляды. Прицелы снайперских винтовок."



    if ROUTE_FOX:
        jump day3_transit_wrong_fox


    jump day3_transit_wrong_notfox

label day3_draw_witness_class:
    $ story_manager.MarkEvent(("day3", "scene_witness"))
    scene bg_classroom base 5_4_3_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900

    "Лилия Павловна прошагала, смерив меня заинтересованным взглядом."
    play test_one "sounds/steps/Techer_out.ogg"
    scene bg_classroom base 4_00_no_chair with Dissolve(0.5):
        xpos -3911 + 1920 + 900
    "Ученики притихли разом, словно на пульте убавили звук."
    scene bg_classroom base 4_00_no_chair:
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900
        parallel:
            ease 5.0 xpos -3911 + 1920 +600
    show bg koridorchic_mor_open_5 with Dissolve(0.5):
        alpha 0.0
        ypos 0
        xpos 0
        parallel:
            pause 1.8
            ease 6.0 xpos -300
        parallel:
            pause 1.9
            linear 1.0 alpha 1.0

    play test_two "sounds/steps/steps_shool.ogg"
    "Они следили, как я иду по проходу, и что-то менялось в их взглядах."
    "Даже в Катином произошли перемены."

    show bg_black:
        alpha 0.0
        linear 1.5 alpha 1.0
    play test_one "sounds/sfx_toilet.ogg"
    "Я отчётливо вспомнил, как однажды папа заступился за ветерана в автобусе, приструнив пьяных хулиганов."
    "Пассажиры смотрели на него так же."
    play test_two "sounds/steps/steps_shool.ogg"
    "С уважением."
    play test_one "sounds/sfx_sit_down.ogg"

    scene ant_clas_fon
    show ant_clas_1 1
    with Dissolve(0.5)
    "Сходив в туалет и умывшись ледяной водой, я вернулся в класс."
    play test_two "voice/Child/3day/03 Anton.ogg"
    "Но не успел переступить порог, как кто-то радостно окликнул меня по имени."
    play test_three "sounds/sfx_girl_comes1.ogg"

    show ant_clas_4_aside
    show ant_clas_4:
        xpos -230
    with Dissolve(0.5)
    play test_one "voice/Child/3day/07 Na.ogg"
    "Это была Катина соседка по парте."
    "Улыбнувшись, она угостила меня конфетой «Скитлс»."
    play test_two"voice/anton/3day/01 S.ogg"
    "Я пробурчал слова благодарности и машинально проглотил драже, точно это была мамина таблетка."
    "Сбоку раздался радостный возглас."
    play test_one "sounds/sfx_girl_comes3.ogg"
    hide ant_clas_4_aside
    show ant_clas_3:
        xpos 1150
    with Dissolve(0.5)
    show ant_clas_m4 with Dissolve(.5)
    voice "voice/Child/3day/08 Ant.ogg"
    Classmate "Антон, а меня нарисуешь?"
    play test_two "sounds/sfx_footsteps_fat_boy_3.ogg"
    show ant_clas_5:
        xpos -177
    show ant_clas_4_aside
    with Dissolve(0.5)
    voice "voice/Child/3day/09 E.ogg"
    Classmate "И меня! Можно я, можно я?"
    play test_two "voice/Child/3day/12 Nar.ogg"
    "Кричали уже со всех сторон, и от неловкости я прижался к стенке с атласом."
    voice "voice/Child/3day/10 A.ogg"
    Classmate "А ты сам научился?"
    hide ant_clas_4_aside with Dissolve(0.5)
    voice "voice/Child/3day/11 Mo.ogg"
    Classmate "Можешь Ван Дамма нарисовать? Я дома как плакат повешу!"
    stop music2 fadeout 2.5
    show k_fon
    show Kate Hee b_day 00 angry ahead 04
    with Dissolve(0.5)

    voice "voice/kate/102 KA.ogg"
    Kate "Эй, я вообще-то первая спросила!"
    play music "music/28_Dejection.ogg" volume 0.8

    show Kate Hee b_day 00 angry ahead 01
    with Dissolve(0.5)
    "Катя подползла словно гадюка, незаметно вклинившись между мной и одноклассниками."

    show Kate Hee b_day 00 evil ahead 03
    with Dissolve(0.5)
    voice "voice/kate/103 KA.ogg"
    Kate "Антон меня уже обещал нарисовать. По дружбе..."
    show Kate Hee b_day 00 evil ahead 01 with Dissolve(.3)
    pause .3
    show Kate Hee b_day 00 evil ahead 03 with Dissolve(.3):
        yoffset 0
        linear 0.15 yoffset 30
        linear 0.15 yoffset 0
        repeat 3
    voice "voice/kate/104 KA.ogg"
    Kate "Да-да-да!"
    show Kate Hee b_day 00 evil ahead 01 with Dissolve(.3)
    pause .3
    show Kate Hee b_day 00 evil ahead 03 with Dissolve(.3)
    voice "voice/kate/105 KA.ogg"
    Kate "Правда же, Антон?"

    show Kate Hee b_day 00 evil ahead 01
    with Dissolve(.5)
    "«Как же!» — пронеслось у меня в голове."
    show ant_clas_m5 behind Kate
    hide k_fon
    hide Kate
    with Dissolve(0.5)
    "Только я на что-то сгодился, так сразу ушлая Катя стала набиваться ко мне в друзья."
    show ant_clas_m3 with Dissolve(0.5)
    voice "voice/anton/3day/027 Pr.ogg"
    Ant "Прости, но я уже обещал другой."

    show k_fon
    show Kate Block b_day 00 evil aside 01
    with Dissolve(.5)
    play test_one "voice/kate/114 KA.ogg"
    "Было видно, как дрогнуло Катино лицо, но она молча проглотила мой ответ."
    show Kate Block b_day 00 evil ahead 01
    with Dissolve(.5)
    play test_one "voice/kate/115 KA.ogg"
    stop music fadeout 3


    if ROUTE_FOX:
        jump day3_transit_witness_fox


    jump day3_transit_witness_notfox

label day3_transit_wrong_fox:
    scene bg_classroom base 3 1 no_guys with Dissolve(.5):
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900

    scene bg_classroom base 3 1 no_guys:
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900
        ease 3.0 xpos -3911 + 1920 +600

    show bg koridorchic_mor_full2:
        alpha 0.0
        ypos 0
        xpos -2319 + 300
        parallel:
            pause 2.0
            ease 1.5 xpos -2319
        parallel:
            pause 2.0
            linear 1.0 alpha 1.0

    window hide
    $ renpy.pause(delay=2.0, hard=True)
    window show

    play test_one "sounds/steps/steps_shool.ogg"
    "Я протиснулся сквозь баррикады парт, ища Полину…"


    $ chalk_state_1 = False
    $ chalk_state_2 = False
    $ chalk_state_3 = False

    jump day3_draw_fox

label day3_transit_witness_fox:

    scene bg_classroom base 3 1 no_guys with Dissolve(.5):
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900

    scene bg_classroom base 3 1 no_guys:
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900
        ease 3.0 xpos -3911 + 1920 +600

    show bg koridorchic_mor_full2:
        alpha 0.0
        ypos 0
        xpos -2319 + 300
        parallel:
            pause 2.0
            ease 1.5 xpos -2319
        parallel:
            pause 2.0
            linear 1.0 alpha 1.0

    window hide
    $ renpy.pause(delay=2.0, hard=True)
    window show


    play test_one "sounds/steps/steps_shool.ogg"
    "Я поспешил протиснуться сквозь радостно галдящих ребят, ища Полину…"

    $ chalk_state_1 = False
    $ chalk_state_2 = False
    $ chalk_state_3 = False

    jump day3_draw_fox

label day3_transit_wrong_notfox:

    scene bg_classroom base 3 1 no_guys with Dissolve(.5):
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900

    scene bg_classroom base 3 1 no_guys:
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900
        ease 3.0 xpos -3911 + 1920 +600

    show bg koridorchic_mor_full2:
        alpha 0.0
        ypos 0
        xpos 0
        parallel:
            pause 2.0
            ease 1.5 xpos -300
        parallel:
            pause 2.0
            linear 1.0 alpha 1.0

    window hide
    $ renpy.pause(delay=2.0, hard=True)
    window show


    play test_one "sounds/steps/steps_shool.ogg"
    "Я протиснулся сквозь баррикады парт, ища Полину…"

    $ chalk_state_1 = False
    $ chalk_state_2 = False
    $ chalk_state_3 = False

    jump day3_draw_notfox

label day3_transit_witness_notfox:

    scene bg_classroom base 3 1 no_guys with Dissolve(.5):
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900

    scene bg_classroom base 3 1 no_guys:
        alpha 1.0
        ypos 0
        xpos -3911 + 1920 + 900
        ease 3.0 xpos -3911 + 1920 +600

    show bg koridorchic_mor_full2:
        alpha 0.0
        ypos 0
        xpos 0
        parallel:
            pause 2.0
            ease 1.5 xpos -300
        parallel:
            pause 2.0
            linear 1.0 alpha 1.0

    window hide
    $ renpy.pause(delay=2.0, hard=True)
    window show


    play test_one "sounds/steps/steps_shool.ogg"
    "Я поспешил протиснуться сквозь радостно галдящих ребят, ища Полину…"

    $ chalk_state_1 = False
    $ chalk_state_2 = False
    $ chalk_state_3 = False

    jump day3_draw_notfox

label day3_draw_notfox:
    $ story_manager.MarkEvent(("day3", "scene5a"))
    show Byasha Normal m_day 01 normal ahead 01:
        xoffset -290
        yoffset 75
    show Romka Angry m_day 001 angry ahead 01:
        xoffset 310
        yoffset 75
    with Dissolve(0.5)
    play music "music/40_Imminence.ogg" volume 0.85
    "... а наткнулся на своих новых «товарищей»."
    play test_one "sounds/steps/Podoshe_2.ogg"

    show Romka Angry b_day 01 angry ahead 01:
        xoffset 310
        yoffset 75
    with Dissolve(0.5)

    "Ромка приблизился вразвалку."
    show Romka Angry b_day 01 angry ahead 02:
        xoffset 310
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/04 Re.ogg"
    Rom "Решил сдать нас ментам?"
    show Romka Angry b_day 01 angry ahead 01:
        xoffset 310
        yoffset 75
    with Dissolve(0.3)
    voice "voice/anton/3day/025 No.ogg"
    Ant "Но я ничего не сказал."
    show Romka Angry b_day 01 angry ahead 01:
        xoffset 310
        yoffset 75
    show Byasha Normal m_day 01 normal ahead 02
    with Dissolve(0.3)
    voice "voice/byasha/3day/77 Zato.ogg"
    Bya "Зато подумал, на."

    show Romka Angry b_day 01 angry ahead 01:
        xoffset 310
        yoffset 75
    show Byasha Normal m_day 01 normal ahead 01
    with Dissolve(0.3)
    "Ромка навис надо мной, дыша сигаретным душком."
    show Romka Angry b_day 01 angry ahead 02:
        xoffset 310
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/05 Ti.ogg"
    Rom "Ты сильно ошибаешься, думая, что без Сёмы у тебя настанут весёлые деньки."
    show Romka Angry b_day 01 angry ahead 01 with Dissolve(0.3)
    show Romka Angry b_day 01 angry ahead 02 with Dissolve(0.3)


    if not Flags.Has("silent"):
        voice "voice/romka/3day/06 M.ogg"
        Rom "Можешь не притворяться дурачком, пытаясь удивить Полину своей мазнёй, или корчить из себя психа."

    show Romka Angry b_day 01 angry ahead 01 with Dissolve(0.3)
    show Romka Angry b_day 01 angry ahead 02 with Dissolve(0.3)
    voice "voice/romka/3day/07 mi.ogg"
    Rom "Мы тебя со свету сживём, понял?"
    queue test_three [ "<silence 2>", "<from 0 to 8>sounds/sfx_footsteps_fat_boy_2.ogg"]
    show Romka Angry b_day 01 angry ahead 01 with Dissolve(0.3):
        xoffset 310
        yoffset 75
    pause 1
    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)
    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3):
        xoffset 310
        yoffset 75
        pause .4
        parallel:
            linear 4 xoffset -200
            linear .5 alpha 0 xoffset -250
        parallel:
            linear .5 yoffset 60
            linear .5 yoffset 75
            repeat 5
    voice "voice/romka/3day/08 Do.ogg"
    Rom "До скорого, очкарик!"
    play test_two "sounds/pushed.ogg"


    scene tupichok_floor:
        xalign .5
        yalign .5
        linear 0.1 xalign .5 yalign .5 zoom 1.1
        linear 0.1 xalign .5 yalign .5 zoom 1.3
        linear 0.2 xalign .5 yalign .5 zoom 1.6
        linear 0.1 xalign .5 yalign .5 zoom 1.3
        linear 0.1 xalign .5 yalign .5 zoom 1.25
        linear 0.1 xalign .5 yalign .5 zoom 1.35
        linear 0.1 xalign .5 yalign .5 zoom 1.3
        linear 0.1 xalign .5 yalign .5 zoom 1.2
        linear 0.1 xalign .5 yalign .5 zoom 1.15
        linear 0.1 xalign .5 yalign .5 zoom 1.0
    with Dissolve(0.3)

    "От подзатыльника моя голова резко качнулась вперёд."
    play test_seven "voice/anton/3day/026 Au.ogg"
    show bg koridorchic_mor_open_5:
        xpos -300
    show Byasha Normal m_day 01 normal ahead 02:
        xoffset -290
        yoffset 75
        pause .4
        parallel:
            linear 2 xoffset -400
            linear .5 alpha 0 xoffset -450
        parallel:
            linear .5 yoffset 60
            linear .5 yoffset 75
            repeat 3
    with Dissolve(0.3)
    play test_one "sounds/sfx_footsteps_fat_boy_2.ogg"
    voice "voice/byasha/3day/78 Vot.ogg"
    Bya "Вот же лох, на!"
    play test_one "sounds/wall-pics-long-1.ogg"
    scene tupichok_floor
    show ruka_pni_menya:
        pause .5
        block:
            linear 1.0 xpos 0 ypos 10
            linear 1.0 xpos 2 ypos 5
            linear 1.0 xpos 5 ypos 0
            linear 1.0 xpos 7 ypos 5
            linear 1.0 xpos -1 ypos 0
            linear 1.0 xpos 5 ypos 5
            repeat
    with Dissolve(0.5)

    "Я не удивился, обнаружив записку на моей спине:"
    "ПНИ МЕНЯ!"
    hide ruka_pni_menya with Dissolve(0.5)
    "Кошмар завёлся по новой."

    jump day3_week_later

label day3_draw_fox:
    $ story_manager.MarkEvent(("day3", "scene5b"))

    show Byasha Normal m_day 01 normal ahead 01:
        xoffset -300
        yoffset 75
    show Romka Normal m_day 00 norm ahead 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    play test_one "sounds/steps/Otoshel.ogg"
    "... а наткнулся на своих новых товарищей."
    play music2 "music/Byasha.ogg" volume 0.7 fadein 2
    "Ромка и Бяша караулили у расписания."

    show Romka Angry m_day 001 happy ahead 06 with Dissolve(0.3)

    voice "voice/romka/3day/09 Ya.ogg"
    Rom "Я в тебе не ошибся, Тошик."

    show Romka Angry m_day 001 happy ahead 03 with Dissolve(0.3)
    show Romka Angry m_day 001 happy ahead 06 with Dissolve(0.3)

    voice "voice/romka/3day/10 Pa.ogg"
    Rom "Пацан! Не спалил, как мы чуть было Свинью не забили."

    show Romka Angry m_day 001 happy ahead 03 with Dissolve(0.3)

    voice "voice/anton/3day/028 Eto.ogg"
    Ant "Это повело бы милицию по ложному следу."

    voice "voice/anton/3day/028 Na.ogg"
    Ant "Наверное..."
    voice "voice/anton/3day/029 A.ogg"
    Ant "А вы точно не имеете отношения к исчезновению Свин... Семёна?"

    show Romka Angry m_day 001 happy ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/11 M.ogg"
    Rom "Мы-то нет, а вот ты?"

    show Romka Angry m_day 001 happy ahead 01 with Dissolve(0.3)
    show Romka Angry m_day 001 happy ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/12 Po.ogg"
    Rom "Помнишь, как срулил от нас в потёмках?"

    show Romka Angry m_day 001 happy ahead 01 with Dissolve(0.3)
    pause 0.4
    show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

    voice "voice/byasha/3day/79 A.ogg"
    Bya "Ага! Я такой говорю: очкарик – зверь."

    show Byasha Normal m_day 01 normal ahead 07 with Dissolve(0.3)
    show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

    voice "voice/byasha/3day/80 Sh.ogg"
    Bya "Ща жирного нагонит и кокнет, на!"

    show Byasha Normal m_day 01 normal ahead 01 with Dissolve(0.3)
    pause 0.4
    show Romka Angry m_day 001 happy aside 06 with Dissolve(0.3)

    voice "voice/romka/3day/13 baz.ogg"
    Rom "Базаришь!"

    show Romka Angry m_day 001 happy aside 03 with Dissolve(0.3)
    pause 0.4
    show Romka Angry m_day 001 happy ahead 06 with Dissolve(0.3)

    voice "voice/romka/3day/14 Od.ogg"
    Rom "Однако мы тебе верим. А ты нам?"

    show Romka Angry m_day 001 happy ahead 03 with Dissolve(0.3)

    "Ромка серьёзно взглянул мне в глаза так, что стало неловко, и я закивал."

    show Romka Normal m_day 00 norm ahead 04 with Dissolve(0.3)

    voice "voice/romka/3day/15 Vo.ogg"
    Rom "Вот и славно."

    show Romka Normal m_day 00 norm ahead 01 with Dissolve(0.3)


    if Flags.Has("witness"):

        show Romka Normal m_day 00 norm ahead 01 with Dissolve(0.3)
        show Byasha Normal m_day 01 normal ahead 04 with Dissolve(0.3)

        voice "voice/byasha/3day/81 Et.ogg"
        Bya "Это... Антош, а где ты так классно рисовать научился?"

        show Byasha Normal m_day 01 normal ahead 01 with Dissolve(0.3)

        "Я смутился, но виду не подал. Ковырнул носком ботинка пол."
        voice "voice/anton/3day/030 Da.ogg"
        Ant "Да так. У меня с детства хорошо получалось."
        show Romka Normal m_day 00 norm 01 with Dissolve(0.3)
        show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

        voice "voice/byasha/3day/82 K.ogg"
        Bya "Круто! Я вот тоже... художник."

        show Byasha Normal m_day 01 normal ahead 07 with Dissolve(0.3)
        pause 0.4
        show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

        voice "voice/byasha/3day/84 Pa.ogg"
        Bya "Паяльником по дереву выжигаю, на."

        show Byasha Normal m_day 01 normal ahead 07 with Dissolve(0.3)
        show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

        voice "voice/byasha/3day/85 Von.ogg"
        Bya "Вон, мамке на день рождения тюльпан замутил на разделочной доске."

        show Byasha Normal m_day 01 normal ahead 07 with Dissolve(0.3)
        show Byasha Normal m_day 01 normal ahead 08 with Dissolve(0.3)

        voice "voice/byasha/3day/86 V.ogg"
        Bya "В общем, здорово, что мы с тобой познакомились."

        show Byasha Normal m_day 01 normal ahead 03 with Dissolve(0.3)
        pause 0.4
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/16 T.ogg"
        Rom "Только давайте не будем обниматься на радостях."

        show Romka Normal m_day 00 what aside 01 with Dissolve(0.3)

    stop music2 fadeout 5
    "Ромка понизил тон и с подозрением оглядел коридор."
    play music "music/Kaite1.ogg" volume 0.7 fadein 2
    "Дети поглядывали на нас, шёпотом переговаривались."

    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/17 Sh.ogg"
    Rom "Что ж, Сёма пропал, это правда."

    show Romka Angry m_day 001 angry aside 01 with Dissolve(0.3)
    show Romka Angry m_day 001 angry aside 02 with Dissolve(0.3)

    voice "voice/romka/3day/18 K.ogg"
    Rom "Как и факт, что не просто пропал, а, скорей всего, уже сдох."

    show Romka Angry m_day 001 angry aside 01
    show Byasha Scared m_day 01 shock ahead 01:
        pause .3
        linear .1 yoffset 92
        linear .1 yoffset 75
    with Dissolve(0.3)

    voice "voice/byasha/64 Otshat.ogg"
    "Бяша нервно передёрнулся."

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)

    voice "voice/anton/3day/031 A.ogg"
    Ant "А ты почём знаешь?"

    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/19 D.ogg"
    Rom "Дык!"

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)
    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/29 M.ogg"
    Rom "Мы за это уже тёрли: здесь такие случаи не впервой."

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)
    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)
    show Byasha Scared m_day 01 shock ahead 01 at sprite_fear_speed:
        xoffset -300
        yoffset 75
        parallel:
            pause .6
            linear 1 xoffset -500
            pause .6
            linear 1 xoffset -700
            pause .6
            linear 1 xoffset -900
        parallel:
            pause .6
            linear .5 yoffset 55
            linear .5 yoffset 75
            repeat 3

    voice "voice/romka/3day/30 D.ogg"
    Rom "Думаешь, Сенечка, Вова этот и Сёма в Нарнию попали?"

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)
    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/31 P.ogg"
    Rom "Посидят в лесу с карамелькой за щекой и назад пришлёпают?"

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)
    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)

    voice "voice/romka/3day/32 Ya.ogg"
    Rom "Ясно же, кто их к себе прибрал."

    show Romka Angry m_day 001 angry ahead 01

    voice "voice/anton/3day/032 N.ogg"
    Ant "Неужели Чёрный..."
    play test_one "sounds/steps/Podoshe_2.ogg"
    hide Byasha
    show Byasha Normal b_day 01 shock ahead 09:
        xoffset 0
        xzoom -1
        linear .1 yoffset 10
        linear .1 yoffset 0
        repeat 2
    with Dissolve(0.1)
    voice "voice/byasha/3day/87 Ma.ogg"
    Bya "Маньячелло!"

    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(0.3)
    show Byasha Normal b_day 01 shock ahead 09 with Dissolve(0.3)

    $ add_text_to_dictionary(36)
    voice "voice/byasha/3day/88 BL.ogg"
    Bya "Бля буду, пацаны! Это всё местный {u}Чикатило{/u}, на."

    show Byasha Normal b_day 01 shock ahead 01 with Dissolve(0.3)

    if Flags.Has("witness"):
        show Byasha Normal b_day 01 shock ahead 09 with Dissolve(0.3)

        voice "voice/byasha/3day/89 Mne.ogg"
        Bya "Мне дядька с маминой работы рассказывал: он тоже Зайчью губу в посёлке видел."

        show Byasha Normal b_day 01 shock ahead 01 with Dissolve(0.3)

    voice "voice/anton/3day/033 V.ogg"
    Ant "Вычислить бы ещё, кто он такой."
    play test_one "sounds/steps/Otoshel.ogg"

    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)
    show Byasha Normal m_day 01 shock aside 01 with Dissolve(0.3):
        xoffset -300
        yoffset 75

    voice "voice/romka/3day/33 Nu.ogg"
    Rom "Ну, если этот убийца Бабурина завалил – он и по нашу душу явится, отвечаю."


    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)


    if Flags.Has("finger"):

        show Byasha Normal m_day 01 normal ahead 01:
            xoffset -300
            yoffset 75
        show Romka Normal m_day 00 norm ahead 01:
            xoffset 300
            yoffset 75
        with Dissolve(0.7)
        voice "voice/anton/3day/034 S.ogg"
        Ant "Слушайте, пока Тихонов лекцию читал, я в его папку тайком заглянул."

        show Byasha Normal m_day 01 normal ahead 02 with Dissolve(0.3)
        show Byasha Normal m_day 01 normal ahead 01 with Dissolve(0.3)

        play sound "sounds/sfx_whistle 2.ogg"
        "Бяша присвистнул."
        voice "voice/anton/3day/035 T.ogg"
        Ant "Там лежало кое-что... печатка."

        voice "voice/anton/3day/036 S.ogg"
        Ant "Сёмина печатка. И я её того... прихватил."
        show Byasha Normal m_day 01 vicious ahead 02 with Dissolve(0.3)
        voice "voice/byasha/3day/90 Da.ogg"
        Bya "Да ладно! А ну закежь!"
        show Byasha Normal m_day 01 vicious ahead 01 with Dissolve(0.3)
        play test_two "sounds/ruki.ogg"


        show tupichok_floor
        show ant_hand 1:
            subpixel True
            yoffset 50
            linear .5 yoffset 0
            block:
                linear 1.0 xpos -10 ypos 2
                linear 1.0 xpos -8 ypos 2
                linear 1.0 xpos -6 ypos 0
                linear 1.0 xpos -4 ypos 4
                linear 1.0 xpos -2 ypos 2
                linear 1.0 xpos 0 ypos 0
                repeat
        with Dissolve(.5)

        "Я воровато огляделся, а затем аккуратно показал украденный перстень."

        hide tupichok_floor
        hide ant_hand 1
        with Dissolve(.5)

        show Byasha Normal m_day 01 shock ahead 02 with Dissolve(0.3)

        voice "voice/byasha/3day/92 T.ogg"
        Bya "Так я и думал, на! Маньячелло."

        show Byasha Normal m_day 01 shock aside 01 with Dissolve(0.3)
        show Byasha Normal m_day 01 shock aside 02 with Dissolve(0.3)
        show Byasha Normal m_day 01 shock ahead 01 with Dissolve(0.3)

        voice "voice/byasha/3day/93 Na.ogg"
        Bya "На части нас разрежет."

        show Byasha Normal m_day 01 shock aside 01 with Dissolve(0.3)

        "Рому информация не впечатлила. Он лишь мрачно кивнул."

        show Byasha Normal m_day 01 shock ahead 01 with Dissolve(0.3)

        voice "voice/anton/3day/037 A.ogg"
        Ant "А ещё там фотография была... с гаражом. Чёрным."

        show Byasha Scared m_day 01 shock ahead 01:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)

        "Бяшу словно ударили под дых. Он отшатнулся, рукой заслонил лицо."

        show Romka Angry m_day 001 mad ahead 01 with Dissolve(0.3)

        play test_one "voice/byasha/3day/80 BL.ogg"
        "Ромка закатил глаза и выругался."

        show Romka Angry m_day 001 mad ahead 02 with Dissolve(0.3)

        voice "voice/romka/3day/34 O.ogg"
        Rom "Опять двадцать пять."

        show Romka Angry m_day 001 angry aside 01 with Dissolve(0.3)
        show Romka Angry m_day 001 angry aside 02 with Dissolve(0.3)

        voice "voice/romka/3day/35 Nu.ogg"
        Rom "Ну, спокойно, братан, спокойно."

        show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)

        voice "voice/anton/3day/038 B.ogg"
        Ant "Бяша, ты же встречал Чёрный Гараж раньше, так?"
        voice "voice/anton/3day/038 R.ogg"
        Ant "Рома говорил, что ты даже заглянул в него."
        show Byasha Scared m_day 01 shock ahead 01 at sprite_fear:
            xoffset -300
            yoffset 75
        "Бурятика била крупная дрожь, словно его нагим выбросили на стужу, и каждый мой последующий вопрос окатывал его как из ведра." id day3_draw_fox_49010965
        voice "voice/anton/3day/039 Ch.ogg"
        Ant "Что ты там видел?"

        show Byasha Scared m_day 01 shock ahead 02 at sprite_fear:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)

        voice "voice/byasha/3day/97 Bee A.ogg"
        Bya "Бе-бе-бе-е-е..." id day3_draw_fox_76608aac
        play test_one "sounds/steps/Podoshe_2.ogg"

        show Byasha Scared m_day 01 shock ahead 01 at sprite_fear:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)

        pause 0.5

        hide Romka
        show Romka Worry b_day 01 worry ahead 01:
            xoffset -250
            yoffset 75
        with Dissolve(0.3)

        "Ромка заслонил приятеля грудью, явно недовольный моим допросом."

        show Romka Worry b_day 01 worry ahead 02 with Dissolve(0.3)

        voice "voice/romka/3day/36 Za.ogg"
        Rom "Забудь! Ничё он тебе толком не скажет."

        show Romka Worry b_day 01 worry ahead 01 with Dissolve(0.3)
        show Romka Worry b_day 01 worry ahead 02 with Dissolve(0.3)

        voice "voice/romka/3day/37 B.ogg"
        Rom "Бяше каждый раз мозг набекрень сворачивает, только коснись этой темы."


        show Romka Worry b_day 01 worry ahead 01 with Dissolve(0.3)
        show Romka Worry b_day 01 worry ahead 02 with Dissolve(0.3)

        voice "voice/romka/3day/38 K.ogg"
        Rom "Коль ты теперь с нами, я тебе в первый и последний раз рассказываю..."
        stop music fadeout 4

        show Romka Worry b_day 01 worry aside 01 with Dissolve(0.3)

        "Ромка заговорщицки склонился ко мне, брезгливо сморщился и, словно нехотя возвращаясь к воспоминаниям, зашептал:"
        play music2 "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 2
        show koshmar:
            alpha 0.0
            linear 2. alpha 1.0
        voice "voice/romka/3day/39 O.ogg"
        Rom "Осенью мы с пацанами от нефиг делать чёрной магией баловались: хотели, как обычно, призвать Пиковую даму там, или над духом Пушкина постебаться... то да сё."
        voice "voice/romka/3day/40 A.ogg"
        Rom "А вышло, брат, совсем не весело."
        voice "voice/romka/3day/41 O.ogg"
        Rom "Один старый чудила рассказал, что мы можем призвать настоящего духа, если нарушим один строжайший запрет предков."
        voice "voice/romka/3day/42 Ch.ogg"
        Rom "Чёрт, а я ведь сразу просёк, что он ёбнутый..."
        voice "voice/romka/3day/43 V.ogg"
        Rom "Всего-то надо было пойти за гаражи глубокой ночью..."
        play test_one "sounds/sfx_garage_door_knock.ogg"
        voice "voice/romka/3day/44 E.ogg"
        Rom "... и постучать в самый-самый чёрный, мать его. "
        voice "voice/romka/3day/45 Ta.ogg"
        Rom "Так, мол, явится эта чёрная параша и всех детей заберёт в лучший из миров. Охереть — не встать!"
        voice "voice/romka/3day/46 Vo.ogg"
        Rom "Вот мы по приколу и клюнули."
        stop music2 fadeout 4
        play test_two "sounds/steps/Otoshel.ogg"

        show Romka Normal m_day 00 norm ahead 02:
            xoffset 300
            yoffset 75
        hide koshmar with Dissolve(0.5)

        "Бяша обхватил голову руками и протяжно замычал."
        play music "music/42_Talk.ogg" volume 0.65 fadein 2

        show Byasha Scared m_day 01 shock ahead 02 at sprite_fear:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)

        voice "voice/byasha/3day/97 be.ogg"
        Bya "Бе-бе-е-бе."

        show Byasha Scared m_day 01 shock ahead 01 at sprite_fear:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)

        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/48 A.ogg"
        Rom "А когда Бяша тест на пацана проходил, то должен был в этот Гараж постучать, но эта хитрая морда просто туда заглянул."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/50 E.ogg"
        Rom "И правильно сделал."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/51 On.ogg"
        Rom "Он от ужаса тогда так заорал, что слезы брызнули."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/52 Ot.ogg"
        Rom "Отвечаю, я такой истерики отродясь не видел."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/53 Ya.ogg"
        Rom "Явно там не обещанная райская куща была."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
        show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

        voice "voice/romka/3day/54 S.ogg"
        Rom "С тех пор Чёрный Гараж по нашим закоулкам шарится и нормальных пацанов жрёт."

        show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)

    jump day3_suefa



label day3_suefa:
    $ story_manager.MarkEvent(("day3", "scene6"))
    window auto
    show Byasha Normal m_day 01 shock ahead 01 with Dissolve(0.3)
    voice "voice/anton/3day/040 Chto.ogg"
    Ant "Что же делать?"

    show Romka Angry m_day 001 angry ahead 02 with Dissolve(0.3)
    show Byasha Normal m_day 01 shock aside 01 with Dissolve(0.3)
    $ add_text_to_dictionary(33)
    voice "voice/romka/3day/55 V.ogg"
    Rom "Вместе держаться, вот что. Втроём мы как {u}Вольтрон{/u}."

    show Romka Angry m_day 001 angry ahead 01 with Dissolve(0.3)

    show Byasha Normal m_day 01 normal ahead 04:
        xoffset -300
        yoffset 75
    with Dissolve(0.3)
    if Flags.Has("finger"):
        "Неожиданно отошедший от шока Бяша промямлил:"

    show Romka Angry m_day 001 happy aside 01 with Dissolve(0.3)
    voice "voice/byasha/3day/98 Eto.ogg"
    Bya "Это..."

    show Byasha Normal m_day 01 normal ahead 03 with Dissolve(0.3)
    show Byasha Normal m_day 01 normal ahead 04 with Dissolve(0.3)

    voice "voice/byasha/3day/99 V.ogg"
    Bya "В Вольтроне их пятеро было, на."

    show Byasha Normal m_day 01 normal ahead 03 with Dissolve(0.3)
    pause 0.4
    show Romka Angry m_day 001 happy aside 06 with Dissolve(0.3)

    voice "voice/romka/3day/56 Nu.ogg"
    Rom "Ну, считай, мы покалеченный Вольтрон."
    stop music fadeout 5

    show Romka Angry m_day 001 happy ahead 01 with Dissolve(0.3)
    show Byasha Normal m_day 01 normal ahead 03 with Dissolve(0.3)

    "Он кивнул мне совсем по-взрослому, а его глаза были полными тревоги и грусти."

    show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)
    show Byasha Normal m_day 01 normal aside 03 with Dissolve(0.3)
    play music2 "music/class.ogg" volume 0.75 fadein 4
    voice "voice/romka/3day/57 La.ogg"
    Rom "Ладно, раз Сёмы больше нет... Айда с нами!"
    play test_two "sounds/steps/steps_shool.ogg"
    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    show Byasha Normal m_day 01 normal aside 01 with Dissolve(0.3):
        xzoom -1
        xoffset -300
        linear 0.15 alpha 1 xoffset -300
        linear 0.45 alpha 1 xoffset -250 yoffset 20+75
        linear 0.45 alpha 1.0 xoffset -200 yoffset 0+75
        linear 0.45 alpha 1.0 xoffset -150 yoffset 20+75
        linear 0.45 alpha 1.0 xoffset -100 yoffset 0+75
        linear 0.45 alpha 1.0 xoffset -50 yoffset 20+75
        linear 0.45 alpha 1.0 xoffset 0 yoffset 0+75
        linear 0.45 alpha 1.0 xoffset 50 yoffset 20+75
        linear 0.45 alpha 1.0 xoffset 100 yoffset 0+75
        linear 0.45 alpha 0.5 xoffset 150 yoffset 20+75
        linear 0.45 alpha 0.0 xoffset 200 yoffset 0+75
    show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3):
        xzoom -1
        xoffset 300
        yoffset 75
        linear 0.4 alpha 1 xoffset 350 yoffset 20+75
        linear 0.4 alpha 1.0 xoffset 400 yoffset 0+75
        linear 0.4 alpha 1.0 xoffset 450 yoffset 20+75
        linear 0.4 alpha 1.0 xoffset 500 yoffset 0+75
        linear 0.4 alpha 0.5 xoffset 550 yoffset 20+75
        linear 0.4 alpha 0.0 xoffset 600 yoffset 0+75

    voice "voice/romka/3day/58 D.ogg"
    Rom "Дело одно есть: постоишь для вида, покараулишь. Тебя, кажется, уже боятся все."
    $ renpy.music.set_volume(1.5, 2.5, channel="music2")
    "Меня? Боятся?"
    "И хотя это не укладывалось в голове, меня раздобрило их отношение, и я тут же согласился."

    scene bg_black with Dissolve(.5)
    play test_one "sounds/steps/steps_shool.ogg" loop
    "Я шёл за Ромкой и Бяшей по сумрачным туннелям школы, дегустируя совершенно новое чувство вседозволенности."
    "Мы шагали картинно, будто герои какого-то криминального фильма."

    "Словно только мы втроём обладали некой информацией, недоступной всем прочим."

    stop test_one fadeout 2
    "Не знаю, пошёл бы я с ними, если б мне сразу объяснили цель кампании."
    scene bg_tupic
    show Byasha Normal m_day 01 normal ahead 01:
        xpos -300
        yoffset 75
    show Romka Normal m_day 00 norm ahead 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.7)
    "Мы затаились в темноте у спортзала, а ребята начали потирать костяшки, глядя на выходящих из раздевалки мальчиков."
    show tupic_01 with Dissolve(0.7)
    show Byasha Normal m_day 01 normal aside 01 with Dissolve(0.3):
        xpos -300
        yoffset 75
    "Наконец Бяша ткнул пальцем в кого-то из толпы."
    show Romka Angry m_day 001 angry aside 03:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    show Byasha Normal m_day 01 evil aside 08 with Dissolve(0.3)

    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    voice "voice/byasha/3day/100 Vo.ogg"
    Bya "Вон этот лох!"

    show Byasha Normal m_day 01 evil aside 07 with Dissolve(0.3)

    "Ромка опасно заулыбался и кинул прокуренным голосом:"
    show Romka Angry m_day 001 angry ahead 04:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/59 S.ogg"
    Rom "Стой на стрёме. Если кто из училок объявится — дай знать."
    play test_one "sounds/sfx_steps.ogg"
    hide Romka with Dissolve(0.6)
    show tupic_03 with Dissolve(0.7)

    $ renpy.pause(delay=1.0, hard=True)

    show Byasha Normal m_day 01 evil ahead 08 with Dissolve(0.3)
    voice "voice/byasha/3day/101 G.ogg"
    Bya "Гляди в четыре глаза, на."
    play test_one "sounds/sfx_footsteps_fat_boy_2.ogg"
    hide Byasha
    show tupic_02
    with Dissolve(0.7)
    stop music2 fadeout 5
    voice "voice/romka/3day/60 Davai.ogg"
    "Я встал на углу, переполненный самыми разными мыслями и чувствами."
    voice "voice/romka/3day/60 Nono.ogg"
    "В закутке позади Ромка переговаривался с пятиклассником."
    voice "voice/romka/3day/60 Schet.ogg"
    "Мальчик едва не хныкал, что-то доказывая, но Ромка гнул свою линию, забористо бранясь, а Бяша лишь изредка подгавкивал."
    voice "voice/romka/3day/30 Cry.ogg"
    "Похвалил бы меня папа за то, что я связался с ними?"
    hide tupic_01 with Dissolve(0.5)
    voice "voice/romka/3day/61 v.ogg"
    Rom "Всё, вали давай."
    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    play test_two "sounds/steps/shagi.ogg"
    hide tupic_02
    hide tupic_03
    with Dissolve(0.5)
    show Byasha Normal m_day 01 normal ahead 01:
        xoffset -300
        yoffset 75
    show Romka Normal m_day 00 norm aside 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    play music2 "music/Byasha.ogg" volume 0.7 fadein 4
    $ renpy.music.set_volume(1.5, 2.5, channel="music2")
    "Товарищи вышли из закутка."
    show polor with Dissolve(0.5)
    "Лампочка озарила фотоаппарат в руке Ромки."
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    voice "voice/anton/3day/041 Og.ogg"
    Ant "Ого! «Полароид»... Он твой?"
    "Ромка безразлично тряхнул чёрным чудом техники с раскладной вспышкой."
    voice "voice/romka/3day/62 Te.ogg"
    Rom "Терь мой."
    hide polor
    show Romka Normal m_day 00 norm ahead 03:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    voice "voice/romka/3day/63 M.ogg"
    Rom "Мне тут один должник велик торчал за свой гнилой базар."

    show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
    show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

    voice "voice/romka/3day/64 N.ogg"
    Rom "Но, грит, нет у него велосипеда."

    show Romka Normal m_day 00 norm ahead 02 with Dissolve(0.3)
    show Romka Normal m_day 00 norm ahead 03 with Dissolve(0.3)

    voice "voice/romka/3day/65 V.ogg"
    Rom "Вот и расплатился фотиком."
    show Romka Normal m_day 00 norm aside 04:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    voice "voice/romka/3day/66 A.ogg"
    Rom "А мне он, честно говоря, и в хер не впился."
    play test_two "sounds/steps/steps_shool.ogg"
    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    hide Byasha
    show byash000:
        alpha 1
        xoffset -300
        yoffset 75
        linear 0.4 alpha 1 xoffset -350 yoffset 20+75
        linear 0.4 alpha 1.0 xoffset -400 yoffset 0+75
        linear 0.4 alpha 1.0 xoffset -450 yoffset 20+75
        linear 0.4 alpha 1.0 xoffset -500 yoffset 0+75
        linear 0.4 alpha 1.0 xoffset -550 yoffset 20+75
        linear 0.4 alpha 0.5 xoffset -600 yoffset 0+75
        linear 0.38 alpha 0.0 xoffset -650 yoffset 20+75
    show Romka Normal m_day 00 norm ahead 02:
        xoffset 300
        linear 0.42 alpha 1 xoffset 250 yoffset 20+75
        linear 0.42 alpha 1.0 xoffset 200 yoffset 0+75
        linear 0.42 alpha 1.0 xoffset 150 yoffset 20+75
        linear 0.42 alpha 1.0 xoffset 100 yoffset 0+75
        linear 0.42 alpha 1.0 xoffset 50 yoffset 20+75
        linear 0.42 alpha 1.0 xoffset 0 yoffset 0+75
        linear 0.4 alpha 0.5 xoffset -50 yoffset 20+75
        linear 0.39 alpha 0.0 xoffset -100 yoffset 0+75
    "Парня было жалко, но все плохие мысли растворялись при взгляде на желанную камеру."
    play test_one "sounds/steps/steps_shool.ogg"
    scene bg_black with Dissolve(0.7)
    play sound "sounds/sfx_Polaroid_shot1.ogg"
    "Я живо представил, как понравился бы Оле «Полароид», как я фотографировал бы сестру, маму, отца."
    show bg_koridorchic_day_02 with Dissolve(0.7):
        xpos -520
        linear 1.9 xpos -300
    pause 1.2
    show Byasha Normal m_day 01 normal aside 01:
        xoffset -300
        yoffset 75
    show Romka Normal m_day 00 norm aside 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    "Образы неспешно проступают на твёрдой карточке, будто из тумана выплывают родные лица."
    "И Полину тоже щёлкнул бы – тогда у меня была бы её фотография."
    "Хранилась бы в ящике, под замком."
    stop music2 fadeout 3
    voice "voice/anton/3day/042.Ra.ogg"
    Ant "Раз он тебе не нужен, можешь мне его отдать?"

    show Romka Normal m_day 00 norm ahead 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    play music "music/class.ogg" volume 0.75 fadein 4
    "Рома смерил меня взглядом, и снова стал тем Ромкой, с которым я столкнулся вчера."
    "Коварным и насмешливым вожаком хищной стаи."
    show Romka Angry m_day 001 happy ahead 04:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/67 T.ogg"
    Rom "Ты извини, братан, но я вещами просто так не разбрасываюсь."

    show Romka Angry m_day 001 happy ahead 03 with Dissolve(0.3)
    show Romka Angry m_day 001 happy ahead 04 with Dissolve(0.3)

    voice "voice/romka/3day/68 M.ogg"
    Rom "Могу в ломбард загнать, ну или разыграть во что-нибудь."

    show Romka Angry m_day 001 happy ahead 03 with Dissolve(0.3)

    "Только он сказал об игре, как мне почему-то вспомнилась Алиса."
    show scen_polor with Dissolve(0.5)
    "Я посмотрел на «Полароид»."
    voice "voice/anton/3day/043 Nu.ogg"
    Ant "Ну давай я с тобой на него сыграю. Только во что?"
    play test_one "voice/byasha/3day/107 Pr.ogg"
    "Бяша прыснул в кулак."
    hide scen_polor
    show Byasha Hee m_day 01:
        xoffset -300
        yoffset 75
    show Romka Normal m_day 00 norm aside 01:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    stop test_one fadeout 0.5
    voice "voice/byasha/3day/108 Che.ogg"
    Bya "Чё, Ром, снимем с нашего Антошки последние штаны?"
    show Romka Normal m_day 00 what ahead 03:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 07 normal aside 01:
        xoffset -300
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/69 Ya.ogg"
    Rom "Я те чё, пидор, с пацанов штаны снимать?"

    show Romka Normal m_day 00 what ahead 02 with Dissolve(0.3)

    "Рома посмотрел на меня сверху вниз."
    show Romka Normal m_day 00 norm ahead 04:
        xoffset 300
        yoffset 75
    with Dissolve(0.3)
    voice "voice/romka/3day/70 N.ogg"
    Rom "На что играть собрался?"

    show Romka Normal m_day 00 norm ahead 01 with Dissolve(0.3)
    show Romka Normal m_day 00 norm ahead 04 with Dissolve(0.3)

    voice "voice/romka/3day/71 U.ogg"
    Rom "У тебя хоть бабки есть?"

    show Romka Normal m_day 00 norm ahead 01:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 vicious ahead 07:
        xoffset -300
        yoffset 75
    with Dissolve(0.3)

    voice "voice/byasha/3day/110 Vo.ogg"
    Bya "Во-во! Свети карманы, Тошик."
    scene bg_handblood with Dissolve(0.5)
    "Я медленно вывернул содержимое брюк в слабой надежде наскрести хотя бы какой-то мелочи на завтрак..."


    if not Flags.Has("gum"):
        show hand_zero:
            ypos 1080
            linear 1.6 ypos 0
        "Посреди карманной пыли разместилась пара медяков в компании с пуговицей и наполовину стёртой резинкой."
        voice "voice/byasha/3day/112 Da.ogg"
        Bya "Да ты ж на мели, на!"
        voice "voice/romka/3day/72 P.ogg"
        Rom "Прости, кент."
        voice "voice/romka/3day/73 N.ogg"
        Rom "На такие несметные богатства я меняться не готов."
        show hand_zero:
            ypos 0
            linear 1.6 ypos 1080
        voice "voice/romka/3day/74 A.ogg"
        Rom "А на интерес с тобой играть мы не будем."
        show bg_koridorchic_day_02 with Dissolve(0.7):
            xpos -520
            linear 1.9 xpos -300
        show Romka Normal m_day 00 norm ahead 01:
            xoffset 300
            yoffset 75
        show Byasha Normal m_day 01 vicious ahead 07:
            xoffset -300
            yoffset 75
        with Dissolve(0.3)
        voice "voice/romka/3day/75 D.ogg"
        Rom "Давай-ка в следующий раз."
        "Ромка надел «Полароид» себе на шею, а затем подмигнул нам с Бяшей."
        voice "voice/romka/3day/76 N.ogg"
        Rom "Ну чё, пацаны, пойдём тёлок снимать?"

        jump day3_week_later


    play test_one "sounds/sfx_insert_unfold.ogg"
    "В кармане что-то зашуршало."
    show vkladish00:
        xalign 0.5
        xpos 960
        ypos 1000
        alpha 0.90
        zoom 0.90
        linear 0.5
        linear 0.5 ypos 900 alpha 0.91 zoom 0.91 xpos 960
        linear 0.5 ypos 800 alpha 0.92 zoom 0.92 xpos 955
        linear 0.5 ypos 700 alpha 0.93 zoom 0.93 xpos 960
        linear 0.5 ypos 600 alpha 0.94 zoom 0.94 xpos 955
        linear 0.5 ypos 500 alpha 0.95 zoom 0.95 xpos 960
        linear 0.5 ypos 400 alpha 0.96 zoom 0.96 xpos 955
        linear 0.6 ypos 300 alpha 0.97 zoom 0.97 xpos 960
        linear 0.7 ypos 200 alpha 0.98 zoom 0.98 xpos 955
        linear 0.8 ypos 100 alpha 0.99 zoom 0.99 xpos 960
        linear 0.5 ypos 50 alpha 1.00 zoom 0.995 xpos 957
        linear 0.5 ypos 0 alpha 1.00 zoom 1.00 xpos 955
        block:
            linear 1.0 xpos 955 ypos 10
            linear 1.0 xpos 957 ypos 5
            linear 1.0 xpos 960 ypos 0
            linear 1.0 xpos 962 ypos 5
            linear 1.0 xpos 954 ypos 0
            linear 1.0 xpos 960 ypos 5
            repeat
    "Я выудил из штанов тот самый вкладыш с мерседесом, что получил благодаря Алисе."
    "Видимо я машинально сунул его туда, когда он вылетел из рюкзака со всеми тетрадями."
    voice "voice/anton/3day/044.Ana.ogg"
    Ant "А на вкладыши играете?"
    "У Бяши округлились глаза, стоило поднести картинку с машиной поближе, а вот Ромка даже бровью не повёл."
    voice "voice/romka/3day/77 H.ogg"
    Rom "Хочешь, чтобы я целый фотик за какой-то там фантик отдал?"

    voice "voice/byasha/3day/114 E.ogg"
    Bya "Это же..."
    show bg_koridorchic_day_02:
        xpos -300
    show Romka Worry m_day 01 norm ahead 02:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 shock ahead 07:
        xoffset -300
        yoffset 75
    with Dissolve(0.7)
    voice "voice/romka/3day/78 Da.ogg"
    Rom "Да жвачке этой рубль цена, а в «Полароиде» кассета ещё целая."
    show Romka Worry m_day 01 norm ahead 01:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 vicious ahead 07:
        xoffset -300
        yoffset 75
        linear .17 yoffset 65
        linear .17 yoffset 75
        linear .17 yoffset 65
        linear .17 yoffset 75
    with Dissolve(0.3)
    voice "voice/byasha/3day/114 Et.ogg"
    Bya "Да это же..."
    show Romka Worry m_day 01 norm ahead 02:
        xoffset 300
        yoffset 75
    voice "voice/romka/3day/79 O.ogg"
    Rom "Ой, у меня таких вкладышей жопой жуй. На кой мне ещё..."
    play test_one "sounds/steps/Podoshe_2.ogg"
    show Byasha Normal b_day 01 vicious ahead 08:
        xoffset -300
        yoffset 75
    voice "voice/byasha/3day/115 M.ogg"
    Bya "Мерседес-Бенц, на! Его-то нам и не хватало, Ромыч!"
    scene bg_koridorchic_day_02:
        xpos -300
        linear 0.1 yoffset 10
        linear 0.1 yoffset 0
        linear 0.1 yoffset 10
        linear 0.1 yoffset 0
        linear 0.1 yoffset 10
        linear 0.1 yoffset 0
    show Romka Angry m_day 001 angry aside 01:
        xoffset 300
        yoffset 75
        linear 0.3 xoffset 100
        linear 0.3 xoffset 300
    show Byasha Scared m_day 01 shock ahead 01:
        xoffset -300
        yoffset 75
        pause 0.3
        linear 0.1 yoffset 75
        linear 0.1 yoffset 65
        linear 0.1 yoffset 75
        linear 0.1 yoffset 65
        linear 0.1 yoffset 75
        linear 0.1 yoffset 65
        linear 0.1 yoffset 75
    with Dissolve(0.3)
    play test_one "voice/byasha/3day/116 O.ogg"
    play test_two"voice/romka/3day/80 Tf.ogg"
    play sound "sounds/sfx_punch.ogg"
    "Ромка сплюнул под ноги и отвесил Бяше подзатыльник."
    show Romka Angry m_day 001 angry aside 02:
        xoffset 300
        yoffset 75
    voice "voice/romka/3day/81 Nu.ogg"
    Rom "Ну ты и трепло, братка. Теперь он за него цену до небес взвинтит."
    show Byasha Normal m_day 01 normal aside 01:
        xoffset -300
        yoffset 75
    show Romka Normal m_day 00 norm aside 02:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    "Как я и подозревал, такой автомобиль был ценным пополнением любого коллекционера жвачки Turbo."
    voice "voice/anton/3day/045.Aga.ogg"
    Ant "Ага, значит, появился интерес?"
    voice "voice/anton/3day/046.Ta.ogg"
    Ant "Так во что будем играть?"
    play test_one "sounds/steps/Podoshe_2.ogg"
    show Byasha Normal b_day 01 vicious ahead 08:
        xoffset -300
        yoffset 75
    with Dissolve(0.5)
    voice "voice/byasha/3day/117 V.ogg"
    Bya "В подкидного?"
    play test_two "sounds/steps/Otoshel.ogg"
    show Romka Angry b_day 01 angry ahead 04:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    show Byasha Normal b_day 01 vicious ahead 07:
        xoffset -300
        yoffset 75
    with Dissolve(0.5)
    voice "voice/romka/3day/82 V.ogg"
    Rom "В ножички?"
    show Romka Angry b_day 01 angry ahead 03:
        xoffset 300
        yoffset 75
    with Dissolve(0.5)
    "Я не заметил, как в руках Бяши появилась засаленная и наверняка краплёная колода карт, а Ромка прямо перед носом мастерски крутанул бабочкой."
    "Играть по их правилам совершенно не хотелось."
    voice "voice/anton/3day/047 A.ogg"
    Ant "А давайте в «камень-ножницы»."
    play test_two "sounds/steps/Otoshel.ogg"
    show Romka Angry m_day 001 angry ahead 04:
        xoffset 300
        yoffset 75
    voice "voice/romka/3day/83 O.ogg"
    Rom "Ого, а ты у нас любишь рисковать."
    voice "voice/romka/3day/84 Nu.ogg"
    Rom "Ну что, мой «Полароид» против твоего мерса?"
    stop music fadeout 3
    play test_one "sounds/steps/Podoshe_2.ogg"

    show Romka Angry m_day 001 angry ahead 01:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 vicious ahead 01:
        xoffset -300
        yoffset 75
    voice "voice/anton/3day/048 Po.ogg"
    Ant "По рукам."

    window hide

    label dev_suefa:

    $ story_manager.MarkEvent(("day3", "game suefa"))


    play music "music/Dvar - Uku Uki.ogg" fadein 2
    $ start_suefa_game()
    hide bg_koridorchic_day_02
    hide Romka
    hide Byasha


    if r_win==3:
        jump suefa_lose


    if a_win==3:
        jump suefa_win



label suefa_lose:
    $ story_manager.MarkEvent(("day3", "game suefa", "lose"))

    stop music fadeout 2
    scene bg_koridorchic_day_02:
        xpos -300
    show Romka Angry m_day 001 angry ahead 01:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 vicious ahead 07:
        xoffset -300
        yoffset 75
    play music "music/Beautiful mystery.ogg" volume 0.8 fadein 1
    "Бяша, ликуя, захлопал в ладоши так, что идущие по коридору дети покосились на нас."
    "Я был полностью разгромлен."
    show vkladish00:
        yoffset 50
        alpha 0
        parallel:
            linear .5 alpha 1
        parallel:
            linear .5 yoffset 0
    voice "voice/byasha/3day/122 F.ogg"
    Bya "Фени коля комедия, Тошик! Гони мерс, на."

    hide vkladish00
    show vkladish0
    with Dissolve(.5)
    "Через руки Бяши к Ромке перекочевало моё единственное подтверждение, что Алиса существует."
    $ achievement_grant("ach_defeat")

    hide vkladish0
    show vkladish0:
        parallel:
            linear .5 alpha 0
        parallel:
            easein .5 yoffset 50

    show Romka Angry m_day 001 angry ahead 04
    voice "voice/romka/3day/92 A.ogg"
    Rom "Хе-хе! А вот и вишенка моей коллекции подоспела."

    voice "voice/romka/3day/93 S.ogg"
    Rom "Спасибо, Антош, было приятно иметь с тобой дело."
    window hide
    show Romka Angry m_day 001 angry ahead 01:
        xoffset 300
        yoffset 75
        parallel:
            linear 3.0 xoffset -300
        parallel:
            linear .3 yoffset 60
            linear .3 yoffset 75
            repeat 3
        parallel:
            .5
            linear .5 alpha 0
    show Byasha Normal m_day 01 vicious ahead 01:
        xoffset -300
        yoffset 75
        .25
        parallel:
            linear 3.0 xoffset -900
        parallel:
            linear .25 yoffset 65
            linear .25 yoffset 75
            repeat 3
        parallel:
            .5
            linear .5 alpha 0

    jump day3_week_later



label suefa_win:
    $ story_manager.MarkEvent(("day3", "game suefa", "win"))
    $ Flags.Raise("polaroid")
    stop music fadeout 2
    scene bg_koridorchic_day_02:
        xpos -300
    show Romka Angry m_day 001 angry ahead 01:
        xoffset 300
        yoffset 75
    show Byasha Normal m_day 01 vicious ahead 01:
        xoffset -300
        yoffset 75
    voice "voice/anton/3day/052.Viig.ogg"
    Ant "Ну, я выиграл? Или теперь мне нужно ещё и Бяшу обыграть?"
    play music "music/Beautiful mystery.ogg" volume 0.8 fadein 1
    "Ромка что-то буркнул под нос."
    "Мне показалось, что он откажется выполнять условие и пошлёт меня куда подальше."
    show Byasha Normal m_day 02 vicious ahead 01:
        xoffset -300
        yoffset 75
    voice "voice/byasha/3day/124 E.ogg"
    Bya "Эй, Ромыч, всё по чесноку, на."
    $ achievement_grant("ach_victory")
    show bg_shcool_hall_down
    show polor2
    with Dissolve(0.5)
    play test_one "voice/romka/3day/94  M.ogg"
    "Ромка неохотно сдался."
    play sound "sounds/sfx_take_Polaroid.ogg"
    hide polor2
    show polor02
    with Dissolve(0.5)
    voice "voice/romka/3day/95 V.ogg"
    Rom "Везучий ты, сука. Держи!"

    hide polor02
    with Dissolve(0.5)
    voice "voice/romka/3day/96 T.ogg"
    Rom "Только писюн свой не фоткай."
    play test_two "sounds/steps/steps_shool.ogg"
    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    show pol_win_bg
    show pol_win_h
    with Dissolve(1.5)
    play test_one "voice/anton/3day/053 Hah.ogg"
    "Я взвесил на ладони «Полароид» и понял, что усмехаюсь, как настоящий победитель."

    jump day3_week_later



label day3_week_later:
    $ story_manager.MarkEvent(("day3", "scene7"))
    $ renpy.music.set_volume(1.5, 2.5, channel="music")
    jump dev_day3_week.end
    label dev_day3_week:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Выбери рут"
            "Полина":
                $ ROUTE_POLINA = True
                $ Flags.Raise("day2 polina")
            "Лиса":
                $ ROUTE_FOX = True
                $ Flags.Raise("day2 fox")
            "Маска":
                $ ROUTE_SOLO = True
                $ Flags.Raise("mask")
        label dev_day3_week.end:
    window hide

    show bg_black with Dissolve(5)
    "Семь дней миновало с того дня, как лейтенант навещал класс."
    "На первый взгляд, всё осталось так же."
    scene house_night01:
        zoom 1.4 xalign 0.5 yalign 0.5
        ease 16 zoom 1 xoffset 0 yalign 0
    with Dissolve(4)
    "Лес по-прежнему протягивал к посёлку свои крючковатые лапы, а ветер ночами взметал белые флаги пороши."
    "Родители приглушённо спорили в спальне, а я включал мультики погромче и подсаживался к Оле."
    scene d3_rasp_move
    with Dissolve(1)
    if Flags.Has("record") or Flags.Has("doc"):
        "Фотографии Вовы и Семёна чернели на доске. Да и круглолицая Сенечка не вернулась домой."
    else:
        "Фотографии Вовы и Семёна чернели на доске."
    "Но что-то всё же поменялось. На лицах одноклассников читались перемены."

    if ROUTE_POLINA or ROUTE_SOLO:
        "Они встретили меня новыми порциями тычков и оскорблений. Презрение, издёвки и одиночество стали моими постоянными спутниками."

    if ROUTE_FOX:
        scene classroom_day_bg with Dissolve(0.7)
        "Они оттягивали карман подаренным яблоком. Испарилась враждебность. Школа больше не пугала меня."
    scene table 05 with Dissolve(0.5)
    "А главное..."
    play test_one "sounds/samolet_1.ogg"
    show mail_01 with Dissolve(0.5)
    "Чья-то тень проскользнула по столу, оставив таинственную записку."
    stop music fadeout 4
    scene classroom_day_bg with Dissolve(0.5)
    "Я бросил взгляд в проём между партами, но посыльного и след простыл."
    scene table 05
    show mail_01
    with Dissolve(0.5)
    "От кого эта записка? Что мог скрывать в себе этот аккуратно вырванный и сложенный листок?"
    "Очередные угрозы и унижения, или всё-таки..."
    play test_one "sounds/Page.ogg"
    hide mail_01 with Dissolve(0.5)
    "Я взял листочек и осторожно вдохнул льющийся аромат."
    show mail_hand:
        ypos 980
        linear 2 ypos 0
        block:
            linear 0.7 xpos 0 ypos 1
            linear 0.7 xpos 3 ypos 5
            linear 0.7 xpos 1 ypos 2
            linear 0.7 xpos 4 ypos 4
            linear 0.7 xpos 3 ypos 0
            linear 0.7 xpos 6 ypos 3
            linear 0.7 xpos 2 ypos 1
            linear 0.7 xpos 5 ypos 4
            linear 0.7 xpos 2 ypos 2
            linear 0.7 xpos 4 ypos 5
            linear 0.7 xpos 0 ypos 3
            linear 0.7 xpos 3 ypos 4
            repeat
    play music "music/30_(Tiny_Bunny).ogg" fadein 0.5
    "Ежевика."
    "Внутри красивым почерком было выведено: «Жду тебя в тупичке у раздевалки. Приходи один»."
    hide mail_hand
    scene classroom_day_bg
    with Dissolve(0.5)
    scene classroom_day_bg:
        xpos -995
        pause 0.5
        linear 3.5 xpos -1750
    show bg_koridorchic_day_02:
        xpos 0
        alpha 0
        pause 3.8
        linear 1 xpos -150 alpha 1

        linear 7 xpos -2319

    play test_one "sounds/sfx_stand_up.ogg"
    "Опьянённый призывом, я тут же сорвался с места, то и дело оглядываясь, не увязался ли кто за мной."
    play test_two "sounds/steps/loop_boy_runs_school.ogg" fadein 4 loop
    if not ROUTE_FOX:
        "Мысль, что это была очередная ловушка, подстроенная Ромкой и Бяшей, хоть и зудила в моём возбужденном сознании, всё же быстро оставила в покое."
        "Им бы не хватило смекалки так мастерски подделать записку Полины."
    "Задумавшись, я не заметил, что уже почти бегу, заскакивая за поворот."
    scene bg_koridorchic_day_02:
        xpos -2319
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset -5
    show bg_black with Dissolve(0.3):
        pause .18

    play test_one "sounds/sfx_girl_hit.ogg"
    play test_two "voice/anton/3day/55 Natknul.ogg"
    "И тут же наткнулся на кого-то в тёмном закутке."
    scene tupichok_fon
    show tupichok_tup
    show Polina Front m_day 02 norm ahead 02:
        xpos 400
        ypos 100
    show cover_tup
    with Dissolve(0.7)

    voice "voice/Polina/3day/01 O.ogg"
    Pol "Ой!"
    play sound "sounds/sfx_falling_notebook.ogg"
    scene tupichok_floor
    show tupichok_notebook
    with Dissolve(0.5)
    window auto
    "Как диковинная птица, полетела к моим ногам зелёная тетрадка."
    "Полина преувеличенно возмутилась."
    $ music_general_volume = 0.6
    $ renpy.music.set_volume(0.6, 1.0, channel="music")
    voice "voice/Polina/3day/02 P.ogg"
    Pol "Петров, да ты совсем зрение потерял!"
    "Я поправил очки – собственная близорукость словно бы перестала смущать."
    play sound "sounds/sfx_turning_pages_3.ogg"
    hide tupichok_notebook
    with Dissolve(0.7)

    "Наклонился и подобрал тетрадку."
    scene tupichok_fon
    show tupichok_tup

    show Polina Large b_day 01 angry2 ahead 01:
        xpos 300
    show cover_tup
    with Dissolve(0.5)

    voice "voice/anton/3day/054 Pr.ogg"
    Ant "Прости, я так торопился. Ты меня ждала? Что случилось?"
    $ music_general_volume = 1.0
    $ renpy.music.set_volume(1.0, 4.5, channel="music2")
    stop music fadeout 4.7

    if ROUTE_POLINA:
        jump day3_amulet_before
    else:

        jump day3_amulet_after

label day3_amulet_before:
    $ story_manager.MarkEvent(("day3", "scene8"))
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.5)

    play test_two "voice/Polina/3day/01 S.ogg"
    "Полина сменила наигранный гнев на милость, замялась, явно подбирая правильные слова."

    show Polina Large b_day 01 sad ahead 03 with Dissolve(.5)
    play music2 "music/Broken Thoughts.ogg" volume 0.8 fadein 1
    "При этом смотрела на меня так взволнованно и грустно, словно надеялась, что я продолжу разговор, не дав нам окончательно увязнуть в неловкой тишине."

    show Polina Large b_day 01 sad ahead 01 with Dissolve(.5)

    "Но я хранил молчание, всматриваясь в её дрожащие губы."
    play test_two "voice/Polina/3day/02 Vz.ogg"
    "Наконец Полина глубоко вздохнула и, несколько робея, заговорила:"



    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)

    voice "voice/Polina/3day/04 A.ogg"
    Pol "Антон, скажи, ты на меня сильно злишься?"

    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)

    "Она не дала мне ответить."

    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/05 Oh.ogg"
    Pol "Ох, ну конечно сильно. Что за дурацкий вопрос такой?"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/06 P.ogg"
    Pol "Прости, пожалуйста, я не хотела, чтобы так вышло, честно!"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/07 Ko.ogg"
    Pol "Когда Пятифанов… Этот изверг пнул ту собачку…"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)

    voice "voice/Polina/3day/08 Et.ogg"
    Pol "Это словно и не я была, понимаешь?"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)

    play test_two "voice/Polina/3day/05 Ona.ogg"
    "Она тихонько шмыгнула носом, и даже в полумраке я заметил, как заблестели её глаза цвета океана."
    stop test_two fadeout 1
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/09 Da.ogg"
    Pol "Да, так нельзя…"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/10 Ne.ogg"
    Pol "Нельзя смеяться над тем, как издеваются над животными."
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/11 Nez.ogg"
    Pol "Не знаю даже, что ты обо мне подумал…"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/12 No.ogg"
    Pol "Но я ничего не могу с собой поделать, Антон."
    window hide
    play sound "sounds/loop_dogs_attack_on_man.ogg" fadein 3 loop
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)

    hide bg_white
    show bg_white:
        alpha 0
        linear .25 alpha 1
    show flashback_dog_attack:
        alpha 0
        .25
        linear .5 alpha 1
    show old_movie_001_002:
        alpha 0.0
        .25
        alpha 1.0
        .5
        linear 0.5 alpha 0.0
    pause 2.5
    window auto


    voice "voice/Polina/3day/13 S.ogg"
    Pol "Стоит мне подумать о дедушке, что он пережил в тот день, когда на него напала эта стая бродячих псов, как…"
    play test_six "voice/Hariton/A-001.ogg"
    voice "voice/Polina/3day/14 K.ogg"
    Pol "... как мой разум словно затуманивается."
    stop sound fadeout 1

    window hide
    hide old_movie_001_002
    show old_movie_001_002:
        .15
        linear 0.25 alpha 0.0
    hide flashback_dog_attack with Dissolve(.15)
    show tupichok_book with Dissolve(.25)
    hide bg_white
    window auto
    "Полинина тетрадка в моей руке всё ещё ждала, чтобы вернуться к хозяйке, но я никак не мог найти подходящего момента."


    voice "voice/Polina/3day/15 T.ogg"
    Pol "Ты, наверное, считаешь, что я чокнутая, да?"

    hide tupichok_book with Dissolve(.5)
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)

    "Она смотрела на меня с надеждой, пока я в смятении перебирал в голове все те безумства, что выкидывало моё подсознание в последнее время раз за разом."
    "Я был точно не тем человеком, кто мог судить о нормальности."

    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/16 M.ogg"
    Pol "Мне не всегда удаётся себя контролировать."
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/17 No.ogg"
    Pol "Но я точно не причинила бы кому-то вреда, слышишь?!"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/18 N.ogg"
    Pol "Не то, что этот садист Ромка."
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/19 A.ogg"
    Pol "Антон, прошу, держись от него подальше!"
    show Polina Large b_day 01 sad ahead 01 with Dissolve(.2)

    "В голове будто щёлкнуло. Я недоверчиво покосился на Полину."

    voice "voice/anton/3day/58 V.ogg"
    Ant "Неделю назад во время драки ты называла его по-другому."
    voice "voice/anton/3day/58 R.ogg"
    Ant "Ромочкой."
    voice "voice/anton/3day/59 Sk.ogg"
    Ant "Скажи, вы что, встречаетесь?"

    show Polina Large b_day 01 angry ahead 07 with Dissolve(.5)
    show Polina Large b_day 01 angry2 ahead 07 with Dissolve(.1)
    play test_two "voice/Polina/2day/Oh.ogg"
    "Полину словно током ударило."

    show Polina Large b_day 01 angry ahead 06 with Dissolve(.2)
    voice "voice/Polina/3day/20 E.ogg"
    Pol "Ещё чего! Этот урод ко мне приклеился как банный лист."
    show Polina Large b_day 01 angry ahead 05 with Dissolve(.2)
    show Polina Large b_day 01 angry ahead 06 with Dissolve(.2)
    voice "voice/Polina/3day/22 T.ogg"
    Pol "Такие, как он, не то что намёков, грубых слов не понимают."
    show Polina Large b_day 01 angry ahead 05 with Dissolve(.2)

    show Polina Large b_day 01 norm ahead 01 with Dissolve(.5)
    "Она несколько смягчилась, разглядывая ссадины на моём лице."

    show Polina Large b_day 01 norm ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/23 P.ogg"
    Pol "Прости ещё раз, что так вышло."
    show Polina Large b_day 01 norm ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 norm ahead 02 with Dissolve(.2)
    voice "voice/Polina/3day/24 Ya.ogg"
    Pol "Я… Ну, я правда надеялась, что смогу помочь тебе."
    show Polina Large b_day 01 norm ahead 01 with Dissolve(.2)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.5)
    stop music2 fadeout 4
    voice "voice/Polina/3day/25 Z.ogg"
    Pol "Зря я поверила, что у таких подонков может быть какой-то там кодекс чести."

    show Polina Large b_day 01 norm ahead 03 with Dissolve(.5)
    voice "voice/Polina/3day/26 V.ogg"
    Pol "Вот, у меня есть для тебя подарок."
    play test_one "sounds/sfx_P.ogg"

    show Polina Large b_day 02 norm ahead 03 with Dissolve(.5)
    show expression "sprite/Polina/Large/b_day/1_body/03.png" as polblush with Dissolve(1.5):
        xpos 300
    play test_two "voice/Polina/3day/27 Vz.ogg"
    "Неожиданно она расстегнула верхнюю пуговицу жилетки и тут же засмущалась, заметив мой ошеломлённый взгляд."
    play test_two "sounds/sfx_wrap_shirt.ogg"
    play test_one "sounds/sfx_pull_charm.ogg"

    window hide

    hide polblush
    show Polina Large b_day 04 norm ahead 01
    with Dissolve(.5)

    play music2 "music/Khoomey Tale, intro.ogg" fadeout 1.5
    queue music2 "music/Khoomey Tale, looped.ogg"
    pause 2.5
    window show
    "Затем сняла с шеи амулет на прочном кожаном шнурке, с примотанным к нему крупным звериным когтем, и протянула мне."

    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/28 E.ogg"
    Pol "Этот оберег подарил мне дедушка."
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/29 G.ogg"
    Pol "Говорит, он помогает от всяких бесноватых и одержимых."
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/30 On.ogg"
    Pol "Он ему от одного шамана достался..."
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/31M.ogg"
    Pol "Можешь не верить, но когда дедушка забыл его надеть, с ним и случилось то несчастье."
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)

    "Я вновь покосился на испещрённое царапинами когтище невиданного зверя."

    voice "voice/anton/3day/60 A.ogg"
    Ant "А чей он? Ну, в смысле коготь."

    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/32 D.ogg"
    Pol "Даже не знаю…"
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)

    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/33 M.ogg"
    Pol "Может быть медведя, а может и тигра."
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/34 K.ogg"
    Pol "Кого только не встретишь в нашем лесу."

    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 04 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/35 V.ogg"
    Pol "В любом случае, пожалуйста, прими вместе с моими извинениями."
    stop music2 fadeout 6
    show Polina Large b_day 04 norm ahead 01 with Dissolve(.3)

    window hide
    show Polina Large b_day 05 sad ahead 01:
        align (0,0)
        xoffset 300
    with Dissolve(.5)

    $ story_manager.MarkEvent(("day3", "amulet"))

    call screen day3_choice_amulet()


label day3_amulet_yes:

    $ story_manager.MarkEvent(("day3", "amulet", "yes"))

    $ Flags.Raise("amulet")

    show Polina Large b_day 04 sad ahead 01:
        align (0,0)
        xoffset 300
    play music "music/Romantic Piano Story.ogg" volume 0.9
    voice "voice/anton/3day/61 E.ogg"
    Ant "Если для тебя это так важно..."

    voice "voice/anton/3day/156 Horosh.ogg"
    Ant "Хорошо, давай попробуем начать всё с чистого листа."
    play test_one "sounds/sfx_pull_charm.ogg"


    scene tupichok_floor
    show tupichok_amulet:
        block:
            linear 1. xpos -10 ypos 10
            linear 1. xpos 0 ypos 0
            linear 1.5 xpos 10 ypos 20
            linear 1. xpos 0 ypos 20
            repeat
    with Dissolve(.5)

    "Я осторожно взял амулет свободной рукой — тот источал тепло Полининого тела и пленяющий аромат ежевики."
    "Затем аккуратно повесил его на шею, спрятав под воротник рубашки."
    $ achievement_grant("ach_amulet")

    hide tupichok_amulet
    show tupichok_amulet:
        linear 2. yoffset 1080

    play test_one "sounds/sfx_P.ogg"
    "Вместе с подарком пришла какая-то странная уверенность: этот оберег сможет изменить мою жизнь."

    scene tupichok_fon
    show tupichok_tup
    show Polina Front b_day 01 smile2 ahead 07:
        xoffset 300
    with Dissolve(1.5)
    play test_one "voice/Polina/2day/heh.ogg"
    "Мы с Полиной синхронно улыбнулись, чувствуя, как между нами тает ледяная стена."

    show Polina Front b_day 01 smile ahead 10
    show Polina Front b_day 01 smile ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/36 S.ogg"
    Pol "Спасибо, Антон."
    show Polina Front b_day 01 smile ahead 10 with Dissolve(.3)
    show Polina Front b_day 01 smile ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/37 D.ogg"
    Pol "Для меня это действительно много значит."
    stop music fadeout 3
    show Polina Front b_day 01 smile ahead 10 with Dissolve(.3)

    jump day3_amulet_after


label day3_amulet_no:

    $ story_manager.MarkEvent(("day3", "amulet", "no"))

    play music "music/Romantic Piano Story.ogg" volume 0.7
    voice "voice/anton/3day/62 Da.ogg"
    Ant "Давай он побудет у тебя."


    voice "voice/anton/3day/63 Eto.ogg"
    Ant "Это всё таки ваша семейная реликвия..."

    voice "voice/anton/3day/64 Da.ogg"
    Ant "Да и мне будет спокойнее, если ты будешь под защитой."
    $ achievement_grant("ach_sceptic")

    show Polina Large b_day 01 norm ahead 01 with Dissolve(.5)
    show Polina Large b_day 01 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/38 V.ogg"
    Pol "Всегда думаешь о других..."

    show Polina Large b_day 01 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 01 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/39 Z.ogg"
    Pol "Знаешь, мне казалось, что благородство бывает лишь в книжках."

    show Polina Large b_day 01 norm ahead 01 with Dissolve(.3)
    show Polina Large b_day 01 norm ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/40 P.ogg"
    Pol "Пока не встретила тебя."
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.3)

    "Мне было немного неловко, и я смущенно зашаркал носком ботинка:"

    voice "voice/anton/3day/65 S.ogg"
    Ant "Скажешь тоже."

    show Polina Large b_day 01 sad ahead 01 with Dissolve(.3)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/41 Ya.ogg"
    Pol "Я серьезно!"

    show Polina Large b_day 01 sad ahead 01 with Dissolve(.3)
    show Polina Large b_day 01 sad ahead 02 with Dissolve(.3)
    voice "voice/Polina/3day/42 A.ogg"
    Pol "А что на счёт моих извинений? Их ты примешь?"
    show Polina Large b_day 01 norm ahead 03 with Dissolve(.3)
    play test_one "voice/Polina/2day/heh.ogg"
    "Полина пленительно улыбнулась, заглядывая в мои глаза и я покраснел еще больше."

    voice "voice/anton/3day/66 Da.ogg"
    Ant "Да я и не думал на тебя обижаться."


    voice "voice/anton/3day/156 Bilo.ogg"
    Ant "Было бы на что."
    stop music fadeout 3

    window show
    jump day3_amulet_after

label day3_amulet_after:
    $ story_manager.MarkEvent(("day3", "scene9"))
    play test_two "voice/Polina/3day/Csik.ogg"
    "Полина внимательно меня осмотрела и пощёлкала языком."
    play sound "sounds/sfx_girl_comes3.ogg"
    play music2 "music/11_Poryadok.ogg" volume 0.65 fadein 0

    show Polina Front m_day 03 smile ahead 02:
        xoffset 0
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/Polina/3day/03 A.ogg"
    Pol "А знаешь, на что ты похож, Антоша?"

    show Polina Front m_day 03 smile ahead 03:
        xpos 400
        ypos 100
    with Dissolve(0.5)
    "..."

    show Polina Front m_day 01 norm aside 09:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/Polina/3day/04 Na.ogg"
    Pol "На блюзовую импровизацию."

    show Polina Front m_day 01 norm aside 04:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    "Я заморгал озадаченно."

    show Polina Front m_day 01 norm ahead 04:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/anton/3day/055 Eto.ogg"
    Ant "Это как?"

    show Polina Front m_day 02 norm ahead 09:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/Polina/3day/05 D.ogg"
    Pol "Для меня все люди с чем-то ассоциируются."

    show Polina Front m_day 02 norm ahead 04:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/anton/3day/056..ogg"
    Ant "И для меня. Но не с музыкой же."

    show Polina 3_4 m_day 02 norm ahead 03:
        xpos 400
        ypos 100
    with Dissolve(0.5)

    voice "voice/Polina/3day/06 Vo.ogg"
    Pol "Вот как раз с музыкой!"

    show Polina 3_4 m_day 07 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 07 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/3day/07 B.ogg"
    Pol "Бывают люди-гитарные соло. Или барабанный бой. Или военный марш, как наша Лилия Павловна."

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 02 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/3day/08 A.ogg"
    Pol "А ты такой задумчивый, таинственный. Иногда немного печальный."

    show Polina Front m_day 01 norm aside 09 with Dissolve(0.5)

    voice "voice/Polina/3day/09 T.ogg"
    Pol "Ты точно блюз."

    show Polina Front m_day 01 norm aside 01 with Dissolve(0.5)

    voice "voice/anton/3day/057 A.ogg"
    Ant "А почему импровизация?"

    show Polina Front m_day 01 ahead 09 with Dissolve(0.5)

    voice "voice/Polina/3day/10 A.ogg"
    Pol "А это когда слушатель не догадывается, куда свернёт мелодия, какой темп возьмёт."

    show Polina 3_4 m_day 07 norm ahead 01 with Dissolve(0.3)

    "Конечно, не всё сказанное Полиной дошло до меня."


    "Но я не мог оторваться от её улыбки, лёгкой, как дуновенье майского ветерка, и от глаз, голубых и глубоких."

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 02 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/3day/11 Ch.ogg"
    Pol "Чтобы распознать в тебе музыку, нужен опыт и вкус."

    show Polina 3_4 m_day 00 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 00 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/3day/12 E.ogg"
    Pol "Это не какая-то там эстрада."

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)

    voice "voice/anton/3day/058.Ya.ogg"
    Ant "Я, наверное, вообще не знаю, что такое этот блюз."

    show Polina Front m_day 01 serious ahead 03 with Dissolve(0.5)

    play test_two "voice/Polina/3day/13 Ohn.ogg"
    "Полина охнула, нахмурилась, от чего стала ещё красивее."

    show Polina Front m_day 02 serious ahead 02 with Dissolve(0.5)

    voice "voice/Polina/3day/13 Ne.ogg"
    Pol "Не произноси при мне такие слова! Я тебе обязательно дам кассету."

    show Polina Front m_day 01 serious ahead 03 with Dissolve(0.3)
    show Polina Front m_day 01 serious ahead 02 with Dissolve(0.3)

    voice "voice/Polina/3day/14 R.ogg"
    Pol "Раньше мне дедушка из города столько музыки привозил! И джаз, и свинг, и классику."

    show Polina Front m_day 01 serious aside 03 with Dissolve(0.3)
    show Polina Front m_day 01 serious aside 02 with Dissolve(0.3)

    voice "voice/Polina/3day/15 E.ogg"
    Pol "Это он подметил, что у меня склад ума, как у музыканта."

    show Polina Front m_day 01 serious aside 03 with Dissolve(0.3)
    show Polina Front m_day 01 serious aside 02 with Dissolve(0.3)

    voice "voice/Polina/3day/16 Ya.ogg"
    Pol "Я ещё совсем маленькой пыталась на бумаге записать звуки природы: пение дождя, леса..."

    show Polina Front m_day 01 serious aside 01 with Dissolve(0.3)

    voice "voice/anton/3day/059 Eh.ogg"
    Ant "Эх, мне бы твои уши."

    show Polina 3_4 m_day 02 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/3day/17 A.ogg"
    Pol "А мне бы твои глаза!"

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)

    "Я напрягся, тревожась, что она подтрунивает. Но Полина качнула головой."


    pause .3

    show Polina Front m_day 00 serious ahead 01 with Dissolve(0.5):
        xzoom -1

    pause .3
    play test_two "sounds/steps/Polina_step_01.ogg"

    show Polina Front m_day 00 serious ahead 01:
        linear 0.35 xoffset -20 yoffset 20
        linear 0.35 xoffset -40 yoffset 0 alpha 0

    pause .3

    show Polina Front b_day 01 norm ahead 02:
        xzoom -1
        xpos -450
        ypos 75
        xanchor .0
        linear .5 xpos -500 yoffset 0
    show cover_tup
    with Dissolve(0.5)

    pause .3

    voice "voice/Polina/3day/18 Da.ogg"
    Pol "Да-да, я серьёзно. У тебя глаза художника."

    show Polina Front b_day 01 serious ahead 01 with Dissolve(0.5)
    show Polina Front b_day 01 serious ahead 02 with Dissolve(0.5)

    voice "voice/Polina/3day/19 S.ogg"
    Pol "Смотришь на вещи и фиксируешь их. Я так не умею."

    show Kate Hee m_day 00 evil aside 01 behind tupichok_tup:
        xzoom -1
        xpos 200
        ypos 360
        zoom 0.7
        parallel:
            linear 6 xpos 660
        parallel:
            linear .5 yoffset -10
            linear .5 yoffset 0
            repeat 6

    with Dissolve(0.5)
    stop music2 fadeout 2
    play music "music/Kaite1.ogg" volume 0.7 fadein 0
    show Polina Front b_day 01 serious ahead 01 with Dissolve(0.5)
    play test_one "sounds/steps/sfx_girl_comes.ogg"
    "Мимо прошагала Катя со своим фирменным морозным взглядом."
    "Мы нырнули в тень, стараясь его избежать."

    show Polina Front b_day 01 norm aside 02
    with Dissolve(0.5)

    voice "voice/Polina/3day/21 t.ogg"
    Pol "Теперь понимаешь, почему мы тут прячемся? Вот из-за таких, как она."

    show Polina Front b_day 01 norm ahead 03:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    voice "voice/anton/3day/060 AKat.ogg"
    Ant "А Катька какая мелодия?"

    show Polina Front b_day 01 serious ahead 05:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    play test_two "voice/Polina/3day/22 Hee.ogg"
    "Полина хитро улыбнулась."

    show Polina Front b_day 01 serious ahead 09:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    voice "voice/Polina/3day/22 Sk.ogg"
    Pol "Скрип несмазанных дверных петель."

    show Polina Front b_day 01 serious ahead 04:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)
    show Polina Front b_day 01 serious ahead 09:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    voice "voice/Polina/3day/23 Z.ogg"
    Pol "Знаешь, такой мерзкий дискант."

    show Polina Front b_day 01 serious aside 04:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    play test_two "voice/anton/3day/060.Sme.ogg"
    "Я захихикал, прикрыв рот."
    show Kate Hee m_day 00 evil ahead 02 with Dissolve(0.5)
    play test_one "voice/kate/112 KA.ogg"
    "Катя, конечно, не слышала нашего перешёптывания, но вдруг неодобрительно покосилась через плечо. А потом лишь хмыкнула и ушла восвояси."
    play test_one "sounds/sfx_girl_walks_away.ogg"
    window hide
    stop music fadeout 4

    show Kate Hee m_day 00 evil aside 01:
        xzoom -1
        xpos 660
        ypos 360
        zoom 0.7
        parallel:
            linear 6 xpos 1080
        parallel:
            linear .5 yoffset -10
            linear .5 yoffset 0
            repeat 6
    $ renpy.pause(delay=3.4, hard=True)

    scene tupichok_floor
    show tupichok_notebook2:
        block:
            linear 0.7 xpos 0 ypos 1
            linear 0.7 xpos 3 ypos 5
            linear 0.7 xpos 1 ypos 2
            linear 0.7 xpos 4 ypos 4
            linear 0.7 xpos 3 ypos 0
            linear 0.7 xpos 6 ypos 3
            linear 0.7 xpos 2 ypos 1
            linear 0.7 xpos 5 ypos 4
            linear 0.7 xpos 2 ypos 2
            linear 0.7 xpos 4 ypos 5
            linear 0.7 xpos 0 ypos 3
            linear 0.7 xpos 3 ypos 4
            repeat
    with Dissolve(0.3)
    play music "music/29_Polina.ogg" volume 0.75
    play test_two "sounds/paper-take-4.ogg"
    "Я же вспомнил про тетрадь, которую так и сжимал в руке. Повертел её."
    "Вместо названия предмета на обложке были выведены имя и фамилия хозяйки и слова «только для друзей»."
    voice "voice/Polina/3day/24 L.ogg"
    Pol "Любопытной Варваре кое-что оторвали."
    voice "voice/anton/3day/062 Pr.ogg"
    Ant "Прости. Это анкета?"
    scene tupichok_fon
    show tupichok_tup
    show Polina Front b_day 01 norm ahead 03:
        xzoom -1
        xpos -500
        ypos 75
    show cover_tup
    with Dissolve(0.5)

    show Polina Front b_day 02 norm ahead 08:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    voice "voice/Polina/3day/25 Za.ogg"
    Pol "Заполнял когда-нибудь?"

    show Polina Front b_day 02 norm ahead 04:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    play test_two "voice/anton/3day/063 Ugu.ogg"
    "Я соврал, что да."
    "На деле же одноклассницы из моей старой школы никогда не просили меня заполнить анкету. Это было довольно обидно."
    "Развлечение, конечно, девчачье: просто список стандартных вопросов про любимых актёров и любимые цвета, но доверить кому-то такую тетрадку считалось показателем дружбы."


    "И иногда чего-то большего, о чём раньше я имел смутные представления."

    show Polina 3_4 b_day 02 norm ahead 06:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    voice "voice/Polina/3day/26 Ho.ogg"
    Pol "Хочешь — заполни и мою."

    show Polina 3_4 b_day 02 norm ahead 01:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.5)

    "Сердце участило свой бег."

    voice "voice/anton/3day/064 Ho.ogg"
    Ant "Хочу, спасибо."

    play test_two "voice/Polina/3day/01 HeHe.ogg"
    "Полина хитро хихикнула."


    jump day3_polinahall_amuletfox


label day3_polinahall_amuletfox:
    $ story_manager.MarkEvent(("day3", "scene10"))
    show Polina 3_4 b_day 02 norm ahead 06:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.3)

    voice "voice/Polina/3day/27 A.ogg"
    Pol "А хотя... там же столько секретов!"

    show Polina 3_4 b_day 02 norm ahead 01:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.3)
    show Polina 3_4 b_day 02 norm ahead 06:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.3)

    voice "voice/Polina/3day/28 Na.ogg"
    Pol "Наверное, лучше тебе и не знать, о чём мы, девочки, думаем."

    show Polina 3_4 b_day 02 norm ahead 01:
        xzoom -1
        xpos -500
        ypos 75
    with Dissolve(0.3)

    "Она потянулась к тетрадке, играя со мной. Я перебросил находку в другую руку. Полина попыталась пресечь мой манёвр."

    scene tupichok_cg4:
        xalign 0.
        easein 7. xalign 1.

    show tupichok_cg_animated:
        xpos 1820
        easein 7. xpos 0
    with Dissolve(0.5)

    "Её волосы на миг коснулись моего лица — шелковистая прядь защекотала нос."
    "Я ощутил запах, и весь мир стал этим ароматом: душистым, манящим, живым..."
    "Запомнить бы его, украсть!"
    "Голова пошла кругом, но я собрался и сказал, подражая интонациям лейтенанта Тихонова:"
    play sound "sounds/sfx_girl_comes3.ogg"

    window hide

    scene tupichok_fon
    show tupichok_tup
    show Polina Front m_day 02 serious ahead 04:

        ypos 100
    with Dissolve(1.5)

    voice "voice/anton/3day/065 Va.ogg"
    Ant "Ваша анкета является важнейшей уликой, и я вынужден временно изъять её для изучения."

    show Polina Front m_day 02 sadly ahead 013 with Dissolve(0.5)

    "Полина прикрыла округлившийся в притворном ужасе рот."

    show Polina Front m_day 03 sadly ahead 09 with Dissolve(0.5)

    voice "voice/Polina/3day/29 E.ogg"
    Pol "И что мне грозит за сокрытие улик?"

    show Polina Front m_day 03 sadly ahead 04 with Dissolve(0.5)

    voice "voice/anton/3day/066.S.ogg"
    Ant "Следствие покажет."

    show Polina 3_4 m_day 08 norm ahead 02 with Dissolve(0.5)

    voice "voice/Polina/3day/30 S.ogg"
    Pol "Сдаюсь, товарищ милиционер."

    show Polina 3_4 m_day 08 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 08 norm ahead 02 with Dissolve(0.3)

    voice "voice/Polina/3day/31 T.ogg"
    Pol "Только обещайте ничего не читать."

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day 02 norm ahead 02 with Dissolve(0.3)

    voice "voice/Polina/3day/32 Z.ogg"
    Pol "Здесь содержатся секретные сведения."

    show Polina 3_4 m_day 02 norm ahead 01 with Dissolve(0.3)

    voice "voice/anton/3day/067 B.ogg"
    Ant "Боюсь, что мне всё-таки придётся выяснить, не влюблён ли кто в гражданина Петрова."
    play sound "sounds/steps/Kait_stop.ogg"

    show Polina Front b_day 02 smile2 ahead 014 with Dissolve(0.3)

    play test_two "voice/Polina/2day/ha-ha_pol.ogg"
    "Полина засмеялась и неожиданно притиснулась к моей груди, вновь обдав ароматом волос и кожи, такой сливочной, почти прозрачной, с тоненькими ниточками вен под ней."

    show Polina Front b_day 02 serious ahead 04 with Dissolve(0.3)
    stop test_two fadeout 1
    "Её шёпот был горячим, как расплавленное на сковородке масло."

    show Polina Front b_day 02 serious ahead 09 with Dissolve(0.3)

    voice "voice/Polina/3day/33 T.ogg"
    Pol "Тогда поклянитесь, что не станете разглашать информацию."

    show Polina Front b_day 02 serious ahead 04 with Dissolve(0.3)

    voice "voice/anton/3day/068 Ch.ogg"
    Ant "Честное милицейское!"
    play test_one "sounds/bell.ogg"

    jump day3_polinahall_ring


label day3_polinahall_ring:
    $ story_manager.MarkEvent(("day3", "scene11"))
    show Polina Front b_day 02 serious ahead 09 with Dissolve(0.3)

    show bg_black:
        alpha 0.0
        linear 1.5 alpha 1

    voice "voice/Polina/3day/34 At.ogg"
    Pol "А теперь, Антоша, самое время поторопиться."
    play sound "sounds/steps/Polina_step_02.ogg"
    $ renpy.pause(1.5, hard=True)


    stop music fadeout 2

    pause 3.0

    jump dev_day3_anketa.after
    label dev_day3_anketa:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Solo":
                $ ROUTE_SOLO = True
            "Alice":

                $ ROUTE_FOX = True
            "Polina":

                $ ROUTE_POLINA = True

                menu:
                    "Amulet":
                        $ Flags.Raise("amulet")
                    "No amulet":
                        pass
        label dev_day3_anketa.after:

    scene bg parta
    show tetrad 00
    with Dissolve(0.5)
    window show
    play test_two "sounds/paper-take-4.ogg"
    "На уроке я достал тетрадь."
    play test_one "sounds/sfx_turning_pages_1.ogg"

    play music2 "music/33_Symphony Of Extinct Lights.ogg" fadein 0.5

    show tetrad 01
    with Dissolve(0.5)

    if Flags.Has("amulet") or ROUTE_FOX:
        "С величайшей осторожностью, будто она была хрупким сокровищем."

    "Полистал, вчитываясь в чужие предпочтения."
    play test_two "sounds/sfx_turning_pages_2.ogg"

    show tetrad 16
    "Изрядно удивился, обнаружив кривоватый почерк Ромки."
    "Буквы вылезали за рамки клеточек, словно стеснялись своей бесформенности."
    "Грозный Ромка нашёл время заниматься такой ерундой?"
    "Я улыбнулся в кулак, узнав, что любимый мультфильм Ромы – даже не «Чёрный плащ», а «Утиные истории»."
    "Где-то далеко учитель декламировал отрывки из рассказа Андреева «Кусака». Мне было не до него."
    play test_two "sounds/sfx_turning_pages_3.ogg"

    show tetrad 03
    with Dissolve(0.5)
    "Страницу с ответами Полины украшали цветы и вырезки из журнала «Cool girl»."
    "Любимая музыка – Шуберт."
    "Лучший друг – дедушка."
    "Хобби – не скрипка, как я предполагал, а куда более загадочное – «слушать»."

    show polina_look2_bg with dissolve

    "Неужели такой банальный процесс может быть увлечением?"
    "Я посмотрел через головы одноклассников на Полину. Она сосредоточенно записывала за учителем."
    play test_two "sounds/sfx_turning_pages_4.ogg"
    hide polina_look2_bg
    show tetrad 02
    with Dissolve(0.5)
    play test_one "sounds/pen_bumaga.ogg"
    "Я пролистал тетрадь до чистой страницы и вооружился ручкой."

    $ tetrad_dissolve = ImageDissolve("effect/imagedissolve/anketa/04.png", 1.5)

    "Петров Антон. 6 «В»."
    play test_two "sounds/sfx_writing_words_3.ogg"
    show tetrad 04 with tetrad_dissolve

    $ add_text_to_dictionary(37)

    "Я долго вспоминал любимого музыканта, пока на ум не пришла модная группа «{u}Кар-мэн{/u}» с крутыми танцорами в клипах."
    play test_two "sounds/sfx_writing_words_0.ogg"
    show tetrad 05 with tetrad_dissolve

    "Любимый праздник – это просто. Новый год, естественно."
    play test_two "sounds/sfx_writing_words_00.ogg"
    show tetrad 06 with tetrad_dissolve

    "Хобби – рисование."
    play test_two "sounds/sfx_writing_words_0.ogg"
    show tetrad 07 with tetrad_dissolve

    "Мечта... Пускай будет посетить Диснейленд."
    play test_two "sounds/sfx_writing_words_4.ogg"
    show tetrad 08 with tetrad_dissolve

    "Мой герой."
    "Я не раздумывая начал: «па...»"
    play test_two "sounds/sfx_writing_words_1.ogg"
    show tetrad 09 with tetrad_dissolve

    "Остановился на первом слоге из двух. Вдруг тем, кто будет читать анкеты, мой выбор покажется смешным и глупым?"
    "Обмозговав, я решил, что далеко не всё стоит доверять бумаге."
    "«Паук», — закончил я, сверху присобачил «человек». Человек-паук. Почему бы и нет?"
    play test_two "sounds/sfx_writing_words_0.ogg"
    show tetrad 10 with tetrad_dissolve

    "Чего ты боишься больше всего?"
    "Я написал незамедлительно: потерять дорогого мне человека."
    play test_two "sounds/sfx_writing_words_4.ogg"
    show tetrad 11 with tetrad_dissolve

    "Твой номер телефона."
    "Никакого секрета: 3-03-95."
    play test_two "sounds/sfx_writing_words_3.ogg"
    show tetrad 12 with tetrad_dissolve
    "Любимый мультфильм?"
    "Трансформеры"
    play test_two "sounds/sfx_writing_words_0.ogg"

    show tetrad 13 with tetrad_dissolve

    "Лучший друг..."
    "Я замешкался, прикусив колпачок ручки."


    if ROUTE_FOX:
        "Вспомнил Алису, скользящую за стволами деревьев, задорно смеющуюся в темноте."

        "В конце концов, именно она не дала меня на растерзание тому исполинскому монстру, что бродит по лесу в ночи."
        "Как-то упомянул при Ромке и Бяше «девочку в маске», но они лишь странно на меня посмотрели."
        "Интересно, чем она сейчас занимается?"

    "«Лучший друг», — перечитал я анкетный вопрос. Такой лёгкий и такой важный."


    if ROUTE_POLINA or ROUTE_FOX:
        "Ответом были две буквы, и я аккуратно вписал их в клеточки:"
        "«Ты»."
        play test_two "sounds/sfx_writing_words_0.ogg"
        window hide
        show tetrad 14 with tetrad_dissolve

        scene black with Dissolve(1.0)
        window show
        "«Ты», — повторил я, выныривая из школы."
        pause 1
        scene bg school_day:
            yalign 0.8 xalign 0.5
        with Dissolve(0.5)
        play test_two "sounds/school_door-open-1.ogg"
        $ renpy.pause(1.5)
        play test_two "sounds/school_door-close-1.ogg"

        "Морозный бодрящий воздух обдал мои щёки румянцем."
        "Солнце, похожее на целый яичный желток, ярко светило."
        "Дорогу словно отлили серебром: снег искрился, преломляя солнечные лучи, и я, зажмурившись, улыбался ослепительной белизне."
        "И от чего-то волшебного и зовущего в груди."
        "Потому что в дружбе может таиться нечто большее."
        stop music2 fadeout 6
    else:


        "Ответом было имя сестры, и я аккуратно вписал его в клеточки:"
        play test_two "sounds/sfx_writing_words_0.ogg"

        show tetrad 15 with tetrad_dissolve
        "«Оля»."
        window hide

        scene bg school_day:
            yalign 0.8 xalign 0.5
        with Dissolve(0.5)

        window show
        "«Оля», — повторил я, выныривая из школы."
        play test_two "sounds/school_door-open-1.ogg"
        $ renpy.pause(1.5)
        play test_two "sounds/school_door-close-1.ogg"

        show day3_cornermeet_dragon with Dissolve(.5):
            align (.5,.5)

        play test_one "sounds/sfx_turning_pages_4.ogg"
        "В моей тетрадке красовался свежий рисунок дракончика, которого я сделал специально для моей любимой сестрёнки."
        "В этом царстве мрака и обмана только её поддержка вдохновляла меня продолжать творить и не терять веру в людей."
        "Морозный бодрящий воздух обдал мои щёки румянцем."
        play test_one "sounds/sfx_turning_pages_3.ogg"
        hide day3_cornermeet_dragon with Dissolve(.5)
        "Солнце, похожее на целый яичный желток, ярко светило."
        "Дорогу словно отлили серебром: снег искрился, преломляя солнечные лучи, и я, зажмурившись, улыбался ослепительной белизне."
        "Плевать, что у меня больше нет настоящих друзей."
        "У меня есть нечто большее — тот, кто нуждается в моей защите; тот, кто никогда не предаст и не обидит."
        "Потому что семья — это самое главное. Так всегда говорил мой папа."
        stop music2 fadeout 2.5

    jump dev_day3_cornermeet.after
    label dev_day3_cornermeet:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Solo":
                $ ROUTE_SOLO = True
            "Alice":

                $ ROUTE_FOX = True
            "Polina":

                $ ROUTE_POLINA = True

                menu:
                    "Amulet":
                        $ Flags.Raise("amulet")
                    "No amulet":
                        pass
        label dev_day3_cornermeet.after:


    if ROUTE_FOX:
        jump day3_corner_fox


    jump day3_corner_notfox


label day3_corner_fox:
    $ story_manager.MarkEvent(("day3", "scene12"))
    show Byasha Normal m_day_winter 01 normal ahead 08:
        yoffset 75
    with Dissolve(0.5)

    voice "voice/byasha/125 Tosh.ogg"
    Bya "Тош, ты чё лыбишься?"
    play music "music/Byasha.ogg" volume 0.7 fadein 2.5

    show Byasha Normal m_day_winter 01 normal ahead 07:
        yoffset 75
    with Dissolve(0.5)

    "Я сжевал улыбку и покраснел, как рак."
    voice "voice/anton/3day/070 Aneg.ogg"
    Ant "Да так, анекдот вспомнил."
    "Бяша топтался в центре двора, ботинки нетерпеливо елозили по льду."

    show Byasha Normal m_day_winter 01 normal ahead 08 with Dissolve(0.5)

    voice "voice/byasha/126 Nu.ogg"
    Bya "Ну делись тогда, на."

    show Byasha Normal m_day_winter 01 normal ahead 07 with Dissolve(0.5)

    "Я прошерстил память и выдал первый попавшийся анекдот, услышанный утром в столовой."

    voice "voice/anton/3day/069 Ko.ogg"
    Ant "Кощей вышел на крыльцо, почесать себе сундук, зайца, утку и яйцо."
    stop music fadeout 2
    play test_one "sounds/BaDumTss-1.ogg"
    window hide
    show Byasha Normal m_day_winter 01 normal ahead 07 with Dissolve(0.5)
    pause 1
    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.5)
    pause 1
    show byasha_rot_07_fg:
        yoffset 75
    hide Byasha
    with Dissolve(0.3)
    play test_one "sounds/Fail1.ogg"
    show Byasha Doubt m_day_winter 01 normal ahead 02:
        yoffset 75
    with Dissolve(0.3)
    $ add_text_to_dictionary(28)

    voice "voice/byasha/127 Yasno.ogg"
    Bya "Ясно, {u}Петросян{/u}."
    hide byasha_rot_07_fg
    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    show Byasha Normal m_day_winter 01 normal ahead 02 with Dissolve(0.3)

    voice "voice/byasha/128 NuIdem.ogg"
    Bya "Ну, идём, на."
    play music "music/31_FearTheMind_final.ogg" volume 0.6
    play test_one "sounds/steps/snow_step01.ogg"

    show Byasha x00:
        parallel:
            linear 1. xoffset -200
        parallel:
            linear .25 yoffset 65
            linear .25 yoffset 75
            repeat
        parallel:
            linear 1. alpha 0

    "И не дожидаясь, он последовал к углу школы. Я неуверенно двинулся за ним."
    play test_two "sounds/steps/asphalt-walk-2.ogg"

    window hide
    scene bg school_day:
        yalign 0.8 xpos -2000+960
        linear 4 xpos 0
    show Byasha Normal m_day_winter 01 normal ahead 01:
        yoffset 75
        xoffset -2000+960-600-100
        linear 4 xoffset -600

    voice "voice/anton/3day/071 A.ogg"
    Ant "А куда?"
    stop test_two fadeout 3


    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)

    voice "voice/byasha/129 Idem A.ogg"
    Bya "Идём-идём, на." id day3_corner_fox_a711250f

    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)

    voice "voice/byasha/130 mi.ogg"
    Bya "Мы теперь в одной связке и действуем заодно."

    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)

    voice "voice/byasha/131 Po.ogg"
    Bya "Помощь твоя нужна в кое-каком дельце."
    play test_one "sounds/steps/snow_step01.ogg"

    show Byasha x00:
        xoffset -600
        parallel:
            linear 1. xoffset -800
        parallel:
            linear .25 yoffset 65
            linear .25 yoffset 75
            repeat
        parallel:
            linear 1. alpha 0

    $ renpy.pause(delay=1.0, hard=True)

    "Я почувствовал холодок за пазухой. Больно не понравилось слово «дельце»."
    "За этим словом, произнесённым вот так, через плевок, обычно скрывались разные тёмные штуки."
    "Так говорили незнакомцы, звоня нам в старую квартиру по телефону: «Батю позови, дельце есть»."
    "Бяша обернулся: в облегающем капюшоне он был похож на космонавта."
    "Если бы он был звуком, то, скорее всего, пронзительным свистом, сигналом того, кто сторожит на шухере."
    "От мысли, что меня сейчас втянут во что-то преступное, ноги предательски затряслись."
    play test_one "music/Risers_03.ogg"

    window hide
    show prut_animation
    $ renpy.pause(delay=5.25, hard=True)
    play test_five "sounds/roll-hit-1.ogg"
    window show
    play fon "sounds/fon/wind.ogg" fadein 6
    stop music fadeout 3
    "Череда образов проскочила перед глазами: строгий Тихонов захлопывает дверь камеры, отец гневно бьёт по тюремным прутьям, а мама и Оля тихо плачут рядом..."
    "На заднем дворе, как назло, никого не было."

    scene day3_cornermeet_bg:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.2 rotate -5

    show day3_cornermeet_roma:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.4 rotate -5

    show day3_cornermeet_tree:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.5 rotate -5

    with Dissolve(.5)

    play music2 "music/34_Nikita Kryukov - the Sabbath.ogg"
    "Никого, кроме мрачного Ромки."
    "Он стоял, широко раздвинув ноги, правая рука была спрятана за спину."
    "Наверняка там нож – стальная бабочка смерти, летящая на стук сердца."
    "Ромка плотно сжал сухие губы, стреляя взглядом то в меня, то по сторонам."
    "Что происходит?"
    "Ромка будто прочёл и озвучил мои мысли:"

    $ music_during_lines = 0.75
    voice "voice/romka/3day/01 Ct.ogg"
    Rom "Что происходит?"

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5

    show Byasha Normal m_day_winter 01 normal aside 02:
        xoffset 0
        xpos 1400
        xanchor .5
    show Romka Evil m_day_winter 02 normal alter 01:
        xoffset 0
        xpos 500
        xanchor .5

    with Dissolve(.5)

    voice "voice/byasha/132 Niche.ogg"
    Bya "Ничего. Проветриваемся, на."
    show Byasha Normal m_day_winter 01 normal aside 01 with Dissolve(.2)
    "Голос Бяши был противным, насмешливым."
    show Romka Evil m_day_winter 02 normal alter 02 with Dissolve(.2)
    voice "voice/romka/3day/02 Pr.ogg"
    Rom "Проветривайся в другом месте."
    show Romka Evil m_day_winter 02 normal alter 01
    show Byasha Normal m_day_winter 01 normal ahead 07
    with Dissolve(.2)

    voice "voice/byasha/134 A mne.ogg"
    Bya "А мне и здесь нормально. Да, куколка?"
    scene day3_cornermeet_bg_fence_default
    show Ant Cho b_day 00 what ahead 02
    with Dissolve(.5)

    stop music2 fadeout 2.5
    play music "music/Byasha.ogg" volume 0.7 fadein 2.5
    "Куколка? Это он мне?"
    "От изумления я не мог выдавить из себя ни звука."
    "Только таращился на весь этот цирк, разыгрываемый моими неоднозначными товарищами."

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5
    show Byasha Normal m_day_winter 01 normal ahead 01:
        xoffset 0
        xpos 1380
        xanchor .5
    show Romka Evil m_day_winter 02 normal ahead 02:
        xoffset 0
        xpos 680
        xanchor .5
        yoffset 10
    show anton_sp_05
    with Dissolve(.5)

    $ music_during_lines = 1.0
    voice "voice/romka/3day/03 Vi.ogg"
    Rom "Видишь, ты её напугал."
    stop fon fadeout 8

    show Romka Evil m_day_winter 02 normal alter 01
    show Byasha Normal m_day_winter 01 normal aside 02
    with Dissolve(.3)

    voice "voice/byasha/3day/136 Atebe.ogg"
    Bya "А тебе какая забота, говнюк? Вали пока цел, на."

    show Romka Evil m_day_winter 02 normal alter 01
    show Byasha Normal m_day_winter 01 normal aside 01
    with Dissolve(.3)

    "Я переваривал услышанное: Бяша назвал Рому говнюком? Он свихнулся?"
    voice "voice/anton/3day/072 Pa.ogg"
    Ant "Пацаны..."
    play test_six "voice/romka/3day/04 XA.ogg"

    show Byasha Normal m_day_winter 01 normal aside 01:
        xoffset 0
        xpos 1380
        xanchor .5
        pause .2
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    show Romka Evil m_day_winter 02 normal alter 01:
        xoffset 0
        xpos 680
        xanchor .5
        linear 0.3 xoffset 200
        linear 0.3 xoffset 00
    with Dissolve(.3)

    "Не обращая внимание на мой робкий протест, Бяша шагнул к Роме, замахнулся как-то чудно и комично."


    show Byasha Normal m_day_winter 01 normal aside 01:
        xoffset 0
        xpos 1380
        xanchor .5
        linear 0.3 xoffset -200
        linear 0.3 xoffset 00
    show Romka Evil m_day_winter 02 normal alter 01:
        xoffset 0
        xpos 680
        xanchor .5
        pause .2
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    with Dissolve(.3)

    play sound "voice/byasha/137 Nevin.ogg"
    "Не вынимая правой руки, Рома свободной кистью заблокировал удар."
    play test_six "voice/romka/3day/04 KI.ogg"
    "Актёры в индийских фильмах, которые любит мама, и то дрались убедительнее."
    play sound "voice/byasha/139 Voi.ogg"
    "Бяша заскулил, хоть я и не видел, чтобы Рома стукнул его."

    show Byasha Normal m_day_winter 01 normal ahead 02:
        xoffset 0
        xpos 1380
        xanchor .5
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
    with Dissolve(.3)

    stop sound fadeout 0.5
    voice "voice/byasha/138 Ai.ogg"
    Bya "Ай-ай-ай, больно как, у меня сотрясение мозга!"
    play sound "voice/romka/3day/04 Di.ogg"

    show Romka Evil m_day_winter 02 normal alter 01:
        xoffset 0
        xpos 680
        xanchor .5
        yoffset 10
        linear .3 xoffset 200
        linear .3 xoffset 0
    show Byasha Normal m_day_winter 01 normal ahead 01:
        xoffset 0
        xpos 1400
        xanchor .5
        pause .2
        linear .5 xpos 1600
        linear .5 yoffset 100 alpha 0
        yoffset 0
        ypos 600
        xpos 1900
        linear .5 ypos 700 alpha 1
    with Dissolve(.3)

    play sound "voice/byasha/140 skulit.ogg"
    "Рома пнул куда-то в коленку, Бяша припал на четвереньки, охая и ахая."
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.5)
    "А я смотрел, не моргая, как приближается Ромка."
    play test_three "sounds/steps/step_snow1.ogg"

    show Romka Evil m_day_winter 02 normal ahead 01:
        xoffset 0
        xpos 680
        xanchor .5
        yalign .5
        yoffset 10
        linear .3 xpos 720 zoom 1.1
    "Локоть его подёргивался, рука выползала из-за спины. Я врос в асфальт."
    play test_three "sounds/steps/step_snow2.ogg"

    show Romka Evil m_day_winter 02 normal ahead 01:
        linear .3 xpos 760 zoom 1.2

    "Сейчас заблестит лезвие."
    play test_three "sounds/steps/step_snow1.ogg"

    show Romka Evil m_day_winter 02 normal ahead 01:
        linear .3 xpos 800 zoom 1.3

    stop sound fadeout 0.5
    "Вот сейчас!"
    "Ромка резко выкинул руку, и я щёлкнул зубами от испуга."
    play test_one "sounds/caricature01.ogg"
    window auto

    scene day3_cornermeet_flower_base
    show day3_cornermeet_flower_hand:
        align (.5,.5)
        rotate 30
        yoffset 1000
        linear .5 rotate 0 yoffset 0

        block:
            linear 1. xoffset -5 yoffset -5
            linear 1. xoffset 5 yoffset -5
            linear 1. xoffset 0 yoffset 5
            linear 1. xoffset 5 yoffset -5
            repeat
    show focus_lines_bright:
        .5
        linear 1.0 alpha 0
    with Dissolve(.25)

    pause 1.
    show day3_cornermeet_flower_smile behind day3_cornermeet_flower_hand with Dissolve(.5)

    play test_two "voice/romka/2day/Hah.ogg"
    "Букет подснежников, не пойми откуда взявшийся в такой мороз, качнулся у моего лица."
    "Это что? Цветы?!"
    voice "voice/romka/3day/05 Poz.ogg"
    Rom "Позволь проводить тебя."
    voice "voice/romka/3day/06 Ato.ogg"
    Rom "А то сама знаешь: шастают тут всякие... маньяки."

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5

    show Byasha Normal m_day_winter 01 normal ahead 02:
        xoffset 0
        xpos 1900
        xanchor .5
        ypos 700
    show Romka Angry m_day_winter 02 angry ahead 01:
        xoffset 0
        xpos 500
        xanchor .5

    with Dissolve(.5)

    voice "voice/byasha/3day/141 N.ogg"
    Bya "Ну а чё, на? Бедным маньякам уже и пошастать нельзя?"

    show Byasha Normal m_day_winter 01 normal ahead 01
    show Romka Angry m_day_winter 02 angry aside 02:
        xzoom -1
        xoffset 0
        xpos 500
        xanchor .5
    with Dissolve(.3)
    voice "voice/romka/3day/07 Xr.ogg"
    Rom "Эх, хреновый из тебя маньяк, Бяшка, даже Тоха не повёлся."

    show Romka Angry m_day_winter 02 angry aside 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry aside 02 with Dissolve(.2)
    voice "voice/romka/3day/08 A ona.ogg"
    Rom "А она нас в два счёта раскусит."
    show Romka Angry m_day_winter 02 angry ahead 01:
        xoffset 0
        xpos 500
        xanchor .5
    with Dissolve(.3)
    "Наконец ко мне вернулся дар речи."
    voice "voice/anton/3day/073 Ona.ogg"
    Ant "Она? Кто «она»? Что тут творится?"

    scene day3_cornermeet_flower_base
    show day3_cornermeet_flower_smile
    show day3_cornermeet_flower_hand:
        linear 1. xoffset -5 yoffset -5
        linear 1. xoffset 5 yoffset -5
        linear 1. xoffset 0 yoffset 5
        linear 1. xoffset 5 yoffset -5
        repeat
    with Dissolve(.5)

    play test_two "voice/romka/3day/H.ogg"
    "Рома хмыкнул, сдувая с цветов снежинки."
    voice "voice/romka/3day/09 Da.ogg"
    Rom "Да, маленькая репетиция, братан."
    voice "voice/romka/3day/10 Ho.ogg"
    Rom "Хотели на твою реакцию посмотреть."
    play test_one "sounds/stryahivanie_3.ogg"

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5

    show Byasha Normal m_day_winter 01 normal ahead 07:
        xoffset 0
        xpos 1700
        xanchor .5
        ypos 700
        linear .5 ypos 600 alpha 0
        ypos 100
        yoffset 10
        linear .5 ypos 0 alpha 1
        1.5
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1. xpos 1400
    show Romka Angry m_day_winter 02 angry ahead 01:
        xoffset 0
        xpos 500
        xanchor .5
        yoffset 10
        xzoom -1

    with Dissolve(.5)

    "Бяша встал, отряхиваясь."
    play sound "sounds/steps_snow001.ogg"
    show Byasha Normal m_day_winter 01 normal ahead 08 with Dissolve(.2)
    voice "voice/byasha/3day/142 Da.ogg"
    Bya "Да Ромыч в тёлку одну втюрился."
    show Byasha Normal m_day_winter 01 normal ahead 07 with Dissolve(.2)
    show Byasha Normal m_day_winter 01 normal ahead 08 with Dissolve(.2)
    voice "voice/byasha/3day/143 V.ogg"
    Bya "Вон, откуда-то цветы нарыл, на."
    show Byasha Normal m_day_winter 01 normal ahead 07 with Dissolve(.2)

    show Romka Angry m_day_winter 02 angry aside 02 with Dissolve(.2)
    voice "voice/romka/3day/11 Pa.ogg"
    Rom "Пасть заткни!"

    show Romka Angry m_day_winter 02 angry aside 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/12Ya.ogg"
    Rom "Я так... планирую подкатить слегка."

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/13 Ra.ogg"
    Rom "Разыграть представление, а то она неприступная, мать её за ногу."

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)

    voice "voice/romka/3day/14 Ti.ogg"
    Rom "Типа гуляет девочка себе, а к ней докапывается такое вот говно."

    show Romka Angry m_day_winter 02 angry ahead 01
    show Byasha Doubt m_day_winter 01 normal ahead 01
    with Dissolve(.2)
    "Бяша обиженно заворчал."

    show Byasha Doubt m_day_winter 01 normal aside 02 with Dissolve(.2)
    voice "voice/byasha/3day/144 S.ogg"
    Bya "Сам ты говно!"
    show Byasha Doubt m_day_winter 01 normal ahead 01 with Dissolve(.2)

    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/15 Nu.ogg"
    Rom "Ну и я такой её – раз! – и спасаю!"

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02
    show Byasha Normal m_day_winter 01 normal ahead 07
    with Dissolve(.2)
    voice "voice/romka/3day/16 No.ogg"
    Rom "Но чёт Бяша совсем бездарный актёр."

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/17 Da.ogg"
    Rom "Давай-ка ты маньяком будешь."

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)

    voice "voice/anton/3day/074 Ya.ogg"
    Ant "Я?"

    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/18 Nu.ogg"
    Rom "Ну а чё."

    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/19 Kak.ogg"
    Rom "Как по телеку показывали: маньяки вообще всегда тихие, скромные люди."

    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/20 Vot.ogg"
    Rom "Вот прям как ты."

    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/21 A.ogg"
    Rom "А благодаря Катькиным сплетням все в школе думают, что именно ты Бабурина кокнул."

    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/22 Da.ogg"
    Rom "Давай, соглашайся, Тох."
    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)

    "От сердца отлегло. Никакого криминала — обычный театр, ещё и ради девочки."
    voice "voice/anton/3day/075 A.ogg"
    Ant "А что делать-то надо?"

    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/23 T.ogg"
    Rom "Ты ж видел Бяшины кривляния?"

    show Romka Angry m_day_winter 02 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 02 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/24 Tip.ogg"
    Rom "Тип, идёшь ко мне, борзый такой. Можешь разок в печень заехать."
    play sound "sounds/sfx_wrap_shirt.ogg"
    show Romka Evil m_day_winter 02 normal ahead 02:
        xoffset 0
        xpos 680
        xanchor .5
        yoffset 10
        xzoom 1
        linear .1 yoffset 0
        linear .1 yoffset 10


    voice "voice/romka/3day/25 A.ogg"
    Rom "А я тебя, тип, херак, — и в сугроб."

    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.2)
    voice "voice/anton/3day/076.Nu.ogg"
    Ant "Ну давайте попробуем."
    "Рома оживился."
    play sound "sounds/steps_snow001.ogg"

    show Romka Angry m_day_winter 02 angry ahead 02:
        xoffset 0
        xpos 500
        xanchor .5

        parallel:
            linear 2. xpos 200
            .25
            linear .1 alpha 0 xzoom .75
            xzoom -.75
            linear .1 alpha 1 xzoom -1.

        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 4

    voice "voice/romka/3day/26 O.ogg"
    Rom "Отлично!"

    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry aside 02 with Dissolve(.2)

    voice "voice/romka/3day/27 B.ogg"
    Rom "Бяша, меняешь пол. Ты теперь тёлочка."
    play sound "music/caricature008.ogg"

    show Byasha Baby m_day_winter 01 normal ahead 03 with Dissolve(.5)
    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry aside 02 with Dissolve(.2)
    voice "voice/romka/3day/28 G.ogg"
    Rom "Гуляй!"

    show Romka Angry m_day_winter 02 angry aside 01 with Dissolve(.2)
    "Бяша зашаркал по двору, закривлялся."
    play sound "sounds/steps_snow001.ogg" loop

    show Byasha Baby m_day_winter 01 normal ahead 04:
        parallel:
            linear 3. xpos 700
            linear .1 alpha 0 xzoom .75
            xzoom -.75
            linear .15 alpha 1 xzoom -1.

        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 6
            .25
        1.5

        block:
            parallel:
                linear 4. xpos 1750
                linear .1 alpha 0 xzoom -.75
                xzoom .75
                linear .15 alpha 1 xzoom 1.

            parallel:
                linear .25 yoffset 0
                linear .25 yoffset 10
                repeat 8
                .25

            block:
                choice:
                    1.5
                choice:
                    2.5
                choice:
                    3.5
            parallel:
                linear 4. xpos 700
                linear .1 alpha 0 xzoom .75
                xzoom -.75
                linear .15 alpha 1 xzoom -1.

            parallel:
                linear .25 yoffset 0
                linear .25 yoffset 10
                repeat 8
                .25
            block:
                choice:
                    1.5
                choice:
                    2.5
                choice:
                    3.5
            repeat

    voice "voice/byasha/3day/145 Ya.ogg"
    Bya "Я тёлочка, красивая тёлочка, я гуляю! Ля-ля-ля."
    stop sound fadeout 5

    show Byasha Baby m_day_winter 01 normal ahead 03 with Dissolve(.2)
    show Romka Angry m_day_winter 02 angry ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/29 To.ogg"
    Rom "Тоха, действуй."
    show Romka Angry m_day_winter 02 angry ahead 01 with Dissolve(.2)
    play sound "sounds/steps/step_snow2.ogg"

    hide Romka
    hide Byasha
    with Dissolve(.1)

    show bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5
        linear .5 zoom 1.15 xoffset 300

    show Byasha Baby m_day_winter 01 normal ahead 01:
        xzoom 1.
        align (.5, 1.)
        yoffset 10
        xoffset 500
        alpha 0
        zoom .9
        parallel:
            linear .5 xoffset 700 zoom 1.
        parallel:
            linear .25 alpha 1

    show Romka Evil b_day_winter 01 normal ahead 01:
        xzoom 1.
        align (.5, 1.)
        yoffset 10
        xoffset -200
        zoom .9
        alpha 0
        parallel:
            linear .5 xoffset 0 zoom 1.
        parallel:
            linear .25 alpha 1

    with Dissolve(.5)

    "Я, борясь с улыбкой, направился к Ромке."
    "Он опять спрятал руку и смотрел сурово. Актёрствовал на пять баллов."
    voice "voice/anton/3day/077 Ona.ogg"
    Ant "Она моя!"

    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.2)
    voice "voice/romka/3day/30 Ris.ogg"
    Rom "Рискни!"
    queue sound [ "<silence 0.5>", "<from 0 to 2>voice/romka/3day/31 Fol.ogg"]
    queue test_one [ "<silence 0.4>", "<from 0 to 2>sounds/sfx_punch.ogg"]
    window hide
    hide Romka
    show day3_cornermeet_hit_anim:
        yoffset 10
        xoffset 0
    pause .8
    show Byasha Scared m_day_winter 01 shock aside 01
    with Dissolve(.5)

    window show
    "Я рискнул — махнул в сторону друга. Костяшки кулака лишь скользнули по кожаной куртке, как Ромка внезапно упал."
    "Не от шутливого тычка, конечно, а поскользнувшись на льду."
    play sound "sounds/steps/snow_stepF02.ogg"

    show Byasha Scared m_day_winter 01 shock aside 01:
        parallel:
            linear .1 yoffset 0
            linear .1 yoffset 10
            repeat 5
        parallel:
            linear 1. xoffset 0

    pause 1.
    show Byasha Scared m_day_winter 01 shock aside 03

    play test_one "voice/byasha/70 Byasha ost.ogg"
    "Хлопнулся всем весом, так и не убрав руку из-под тела."

    show Byasha Scared m_day_winter 01 shock ahead 01 with Dissolve(.2)

    "Лепестки примятых бутонов остались на снегу."
    "Я кинулся на помощь."
    play test_three "sounds/steps/step_snow2.ogg"

    scene day3_romafall_bg 0
    show day3_romafall_eyes 0
    show day3_romafall_anton:
        xpos -700
        ypos 1080
        linear 1. xpos 0 ypos 1080 - 1453

    pause 3.

    show day3_romafall_bg 1 with Dissolve(.2)

    voice "voice/romka/3day/32 Oi.ogg"
    Rom "Ой, бля... Да погоди ты, не дёргай."

    show day3_romafall_bg 0 with Dissolve(.2)

    voice "voice/anton/3day/078 N.ogg"
    Ant "Не сломал?"
    play test_one "voice/romka/3day/32 R.ogg"
    "Рома осторожно разминал запястье."

    show day3_romafall_bg 1 with Dissolve(.2)
    voice "voice/romka/3day/33 Ta.ogg"
    Rom "Та не. Ушиб вроде."
    show day3_romafall_bg 0 with Dissolve(.2)

    voice "voice/byasha/3day/146 L.ogg"
    Bya "Лёд приложить нужно, на."

    show day3_romafall_eyes 2
    show day3_romafall_bg 1 with Dissolve(.2)

    voice "voice/romka/3day/34 Te.ogg"
    Rom "Тебя, мудака, приложить нужно..."

    show day3_romafall_bg 0 with Dissolve(.2)
    show day3_romafall_bg 1 with Dissolve(.2)
    voice "voice/romka/3day/35 O.ogg"
    Rom "О стенку башкой."
    play test_one "sounds/UP.ogg"

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5

    show Byasha Normal m_day_winter 01 normal ahead 01:
        anchor (.5,1.)
        ypos 1080
        xpos 1400
        yoffset 10

    show Romka Sad m_day_winter 01 sad aside 06:
        xzoom -1
        xpos -500
        yoffset 10
        ypos 200
        alpha .3
        parallel:
            linear .5 ypos 0
        parallel:
            linear .5 alpha 1

    with Dissolve(.5)

    play test_one "voice/romka/3day/36 Xe.ogg"
    "Ромка встал, уже посмеиваясь, собрал цветы."

    show Romka Sad m_day_winter 01 sad aside 02 with Dissolve(.2)

    voice "voice/romka/3day/37 d.ogg"
    Rom "М-да, если я так при подруге навернусь — можно будет про неё забыть."

    show Romka Sad m_day_winter 01 sad aside 01 with Dissolve(.2)

    voice "voice/anton/3day/079 Da.ogg"
    Ant "Давай ещё раз отрепетируем."
    "Рома мотнул головой."

    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.2)
    voice "voice/romka/3day/38 V.ogg"
    Rom "Вечером, как рука пройдёт."

    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.2)
    show Romka Normal m_day_winter 00 norm ahead 03 with Dissolve(.2)
    voice "voice/romka/3day/39 N.ogg"
    Rom "Не хочу опозориться перед первой скрипкой школы."
    stop music fadeout 2

    show Romka Normal m_day_winter 00 norm ahead 01 with Dissolve(.2)
    voice "voice/anton/3day/080 Dog.ogg"
    Ant "Догово..."
    play music "music/Cinematic Piano.ogg" volume 0.72
    "Я осёкся на полуслове."
    "В голове щёлкнул рубильник, и всё встало на свои места."
    "Я вспомнил беглые взоры, которые Ромка посылал Полине."
    "Вспомнил его каракули в анкете: и почему я не удосужился как следует изучить их?"
    "Меня будто молотом огрели, вколотили в землю."
    "Полина. Вот главный герой спектакля, срежиссированного Ромкой."
    "А мне в нём досталась роль третьего лишнего."
    "Я рассеяно брякнул:"
    voice "voice/anton/3day/081D.ogg"
    Ant "Договорились."

    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.5)
    voice "voice/romka/3day/40 V.ogg"
    Rom "Вот это я понимаю – команда Вольтрона!"

    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.2)

    voice "voice/romka/3day/41 Od.ogg"
    Rom "Один за всех..."

    show Romka Angry m_day_winter 01 happy ahead 05
    show Byasha Normal m_day_winter 01 vicious ahead 08
    with Dissolve(.2)
    voice "voice/byasha/3day/147 I.ogg"
    Bya "... и все на одного!"

    show Romka Angry m_day_winter 01 angry aside 02
    show Byasha Normal m_day_winter 01 normal aside 03
    with Dissolve(.2)
    voice "voice/romka/3day/42 Z.ogg"
    Rom "Захлопни!"

    show Byasha Normal m_day_winter 01 normal ahead 03
    show Romka Angry m_day_winter 01 happy ahead 05
    with Dissolve(.2)
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.2)

    voice "voice/romka/3day/43 E.ogg"
    Rom "Если вдруг тебе понадобится помощь, Антоха, — можешь рассчитывать на меня."

    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.2)
    show Byasha Normal m_day_winter 01 normal ahead 03:
        linear .1 alpha 0 xzoom .75
        xzoom -.75
        linear .15 alpha 1 xzoom -1.
    voice "voice/romka/3day/44 A.ogg"
    Rom "А теперь бывай!"

    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.2)
    show Romka Angry m_day_winter 01 happy ahead 06 with Dissolve(.2)
    voice "voice/romka/3day/45 V.ogg"
    Rom "Вечером мы к тебе заглянем."
    play test_two "sounds/steps/footsteps_two2.ogg"

    window hide

    show Romka Angry m_day_winter 01 happy ahead 05 with Dissolve(.2)

    show Romka Angry m_day_winter 01 happy aside 05:
        parallel:
            linear 1. xoffset 150
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1. alpha 0

    stop test_two fadeout 2
    show Byasha Normal m_day_winter 01 normal aside 03:
        .2
        parallel:
            linear 1. xoffset 150
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 2
        parallel:
            linear 1. alpha 0

    pause 2

    scene day3_cornermeet_anton_transition
    with Dissolve(.5)
    $ renpy.pause(delay=2.5, hard=True)
    stop music fadeout 5
    jump day3_olyatalk



label day3_corner_notfox:

    play test_two"sounds/steps/Stop.ogg"
    show Byasha Normal m_day_winter 01 normal ahead 09:
        yoffset 75
    with Dissolve(0.5)
    voice "voice/byasha/3day/148 S.ogg"
    Bya "Слыш, хорош лыбу тянуть!"
    play music "music/31_FearTheMind_final.ogg" volume 0.9
    show Byasha Normal m_day_winter 01 normal ahead 01:
        yoffset 75
    with Dissolve(0.3)
    "Улыбка скукожилась на задеревеневших губах."
    play fon "sounds/fon/сrow_wind.ogg" fadein 5.0
    "Бяша топтался в центре двора, ботинки нетерпеливо елозили по льду."
    voice "voice/anton/3day/082 Ya.ogg"
    Ant "Я не тяну."
    play test_one "sounds/steps/snow_stepS02.ogg"

    show bg school_day:
        yalign 0.8 xalign 0.5
        linear .5 xoffset -100
    show Byasha Normal m_day_winter 01 normal ahead 01:
        linear .25 xoffset -100
        linear .25 xoffset 0

    "Попробовал обойти его — как же!"
    "Фортуна помахала ручкой, сгинув в ранних сумерках."
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)
    voice "voice/byasha/3day/149 To.ogg"
    Bya "Торопишься, на?"
    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    voice "voice/anton/3day/083 N.ogg"
    Ant "Немного. Меня папа ждёт."
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)
    $ add_text_to_dictionary(35)
    voice "voice/byasha/3day/150 Ya.ogg"
    Bya "Я ему чиркну на {u}пейджер{/u}, что ты не придёшь, на."
    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    "Глаз непроизвольно дёрнулся. Взмокла кожа."
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)
    voice "voice/byasha/3day/151 Ed.ogg"
    Bya "Идём, на. К тебе дельце есть."
    play test_two "sounds/steps/snow_step01.ogg"
    show Byasha x00:
        parallel:
            linear 1. xoffset -200
        parallel:
            linear .25 yoffset 65
            linear .25 yoffset 75
            repeat
        parallel:
            linear 1. alpha 0
    play test_one "sounds/steps/asphalt-walk-2.ogg" loop
    "Я почувствовал холодок за пазухой."


    window hide
    scene bg school_day:
        yalign 0.8 xpos -2000+960-100
        linear 4 xpos 0
    show Byasha Normal m_day_winter 01 normal ahead 01:
        yoffset 75
        xoffset -2000+960-600-200
        linear 4 xoffset -600
    stop test_one fadeout 4

    "Больно не понравилось слово «дельце»."
    "За этим словом, произнесённым вот так, через плевок, обычно скрывались разные тёмные штуки."
    "Так говорили незнакомцы, звоня нам в старую квартиру по телефону: «Батю позови, дельце есть»."
    play test_one "sounds/steps/snow_step01.ogg"

    show Byasha x00:
        xoffset -600
        parallel:
            linear 1. xoffset -800
        parallel:
            linear .25 yoffset 65
            linear .25 yoffset 75
            repeat
        parallel:
            linear 1. alpha 0

    "Бяша обернулся: в облегающем капюшоне он был похож на космонавта."
    "Если бы он был бы звуком, то, скорее всего, пронзительным свистом, сигналом того, кто сторожит на шухере."
    stop music fadeout 2.5
    "На заднем дворе, как назло, никого не было."
    play test_one "sounds/steps/asphalt-walk-2.ogg"

    scene day3_cornermeet_bg:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.2 rotate -5

    show day3_cornermeet_roma:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.4 rotate -5

    show day3_cornermeet_tree:
        align (.5,.5)
        zoom .91
        subpixel True
        ease 20 zoom 1.5 rotate -5

    with Dissolve(.5)

    play music2 "music/34_Nikita Kryukov - the Sabbath.ogg"
    "Никого, кроме мрачного Ромки."
    "Он стоял, широко раздвинув ноги ,правая рука была спрятана за спину."
    "Сухие губы плотно сжаты, глаза стреляют то в меня, то по сторонам."

    if ROUTE_POLINA:
        "Я всей душой надеялся, что Ромка не видел нас с Полиной вместе."

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5

    show Byasha Normal m_day_winter 01 normal ahead 02:
        xoffset 0
        xpos 1400
        xanchor .5
    show Romka Evil m_day_winter 02 normal alter 01:
        xoffset 0
        xpos 500
        xanchor .5

    with Dissolve(.5)

    $ music_during_lines = 0.75
    voice "voice/byasha/3day/152 Pri.ogg"
    Bya "Привёл, на."

    show Byasha Normal m_day_winter 01 normal ahead 01
    show Romka Evil m_day_winter 02 normal ahead 02
    with Dissolve(.3)

    voice "voice/romka/3day/46 Vi.ogg"
    Rom "Вижу."
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.3)

    show Byasha Normal m_day_winter 01 normal aside 01
    show Romka Evil m_day_winter 02 normal ahead 03
    with Dissolve(.3)

    voice "voice/romka/3day/47 Nu.ogg"
    Rom "Ну здорово, Антоша!"
    show Romka Evil m_day_winter 02 normal ahead 01 with Dissolve(.3)
    scene day3_cornermeet_bg_fence_default
    show day3_cornermeet_fence_anton
    with Dissolve(.5)
    show day3_cornermeet_fence_anton_02 with Dissolve(.5)

    voice "voice/anton/3day/084 Ch.ogg"
    Ant "Что тебе нужно?"

    window hide
    scene rom_knife_00
    with Dissolve(0.3)
    show rom_knife_03
    play sound "sounds/sfx_butterfly_knife.ogg"
    $ renpy.pause(1.0)
    scene rom_knife_01
    window show
    "Он медленно извлёк из-за спины узкое, хищно блестящее лезвие."
    "Нож – стальная бабочка смерти, летящая на стук сердца."

    scene bg school_corner_day1_no_squirrel:
        yalign 0.8 xalign 0.5
    show Byasha Normal m_day_winter 01 normal ahead 01:
        xoffset 0
        xpos 1400
        xanchor .5
    show Romka Evil m_day_winter 03 normal ahead 01:
        xoffset 0
        xpos 500
        xanchor .5
    play sound "sounds/bax.ogg"
    with vpunch

    "Я инстинктивно отпрянул и врезался в Бяшу. Ромкина шестёрка подтолкнула меня обратно."

    show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
    voice "voice/romka/3day/48 Am.ogg"
    Rom "А мы с Бяшей хотели узнать..."
    show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
    show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
    voice "voice/romka/3day/49 T.ogg"
    Rom "Ты не держишь на нас обиду?" id day3_corner_notfox_76a38d7a
    stop fon fadeout 9
    show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
    "Ромка принялся ковырять жёлтый ноготь, с коварной усмешкой уставившись на меня."
    show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
    voice "voice/romka/3day/50 Nu.ogg"
    Rom "Ну, там, в лесу... мы были немного грубы с тобой."
    show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
    show Byasha Normal m_day_winter 01 vicious ahead 08 with Dissolve(.3):
        xoffset 0
        xpos 1400
        xanchor .5
    voice "voice/byasha/3day/153 Sa A.ogg"
    Bya "Сам понимаешь, такое у нас воспитание, на." id day3_corner_notfox_b07911b6
    show Byasha Normal m_day_winter 01 vicious ahead 07 with Dissolve(.3)
    show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
    voice "voice/romka/3day/51 D.ogg"
    Rom "Да, до вас, городских, далеко."
    show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
    show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
    voice "voice/romka/3day/52 V.ogg"
    Rom "Вот порой нас и заносит."
    show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
    "Я кивнул, глядя на нож."

    if ROUTE_POLINA:
        show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
        voice "voice/romka/3day/53 Sk.ogg"
        Rom "Скажи, Антоша..."
        show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
        show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
        voice "voice/romka/3day/54 Y.ogg"
        Rom "Я тебя в последний раз не сильно огрел?"
        show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
        voice "voice/anton/3day/085 Da.ogg"
        Ant "Да нет..."
        show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
        voice "voice/romka/3day/55 Nu.ogg"
        Rom "Ну и славно!"
        show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
        show Romka Evil m_day_winter 03 normal ahead 03 with Dissolve(.3)
        voice "voice/romka/3day/55 A.ogg"
        Rom "А то я затревожился, что память тебе отбил. И ты запамятовал, о чём тебе втолковывали."
        show Romka Evil m_day_winter 03 normal ahead 01 with Dissolve(.3)
        voice "voice/anton/3day/086 Ya.ogg"
        Ant "Я помню."

    "Лезвие переливалось в закатном свете. И так же зло переливались зрачки Ромки."
    play test_one "sounds/steps/snow_stepS02.ogg"

    window hide
    show Romka Evil m_day_winter 03 normal ahead 01:
        xoffset 0
        xpos 500
        xanchor .5
        yalign .5
        linear .3 zoom 1.2 xpos 550
    pause .1
    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3):
        xpos 650

    show romka_stab_knife blured:
        anchor (.5,.5)
        xpos 300 + 50
        ypos 1080 - 470 + 225
        yoffset 500
        linear .35 yoffset 0

        block:
            linear 1. xoffset -5 yoffset -5
            linear 1. xoffset 5 yoffset -5
            linear 1. xoffset 0 yoffset 5
            linear 1. xoffset 5 yoffset -5
            repeat

    pause 2.
    window show
    "Он шагнул ко мне."

    show bg school_corner_day1_no_squirrel:
        blur 10.
    show Byasha Normal m_day_winter 01 normal ahead 01:
        blur 8.
    show Romka Evil b_day_winter 01 normal ahead 01:
        blur 6.
    show romka_stab_knife solid
    with Dissolve(.5)

    "Поводил ножом в сантиметре от куртки."
    "Одно движение — и сталь вспорет ткань. А если надавить глубже..."

    show bg school_corner_day1_no_squirrel:
        blur 0.
    show Byasha Normal m_day_winter 01 normal ahead 01:
        blur 0.
    show Romka Evil b_day_winter 01 normal ahead 02:
        blur 0.
    show romka_stab_knife blured
    with Dissolve(.3)

    voice "voice/romka/3day/56 Na.ogg"
    Rom "Нам одна птичка напела, что ты опять возле Полины отирался."
    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)
    "Страшно было так, что я не сразу понял, кто такая Полина."
    "Мозг сбоил. Колени тряслись."
    play test_two "sounds/steps/sfx_girl_comes_on_snow.ogg"

    show Kate Kawai m_day_winter 00 evil ahead 01 behind Byasha with Dissolve(.3):
        xzoom -1
        xpos -1200
        yoffset 10
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 4
        parallel:
            linear 2.0 xpos -700

    "Вдруг позади Ромки неспешной походкой прошла наша староста."
    show Kate Normal m_day_winter 00 evil ahead 02 with Dissolve(.3)
    voice "voice/kate/106 KA.ogg"
    Kate "О, смотрю, мальчики, вы нашли общий язык."
    show Kate Normal m_day_winter 00 evil ahead 01
    show Romka Evil b_day_winter 01 normal aside 02
    with Dissolve(.3)
    voice "voice/romka/3day/57 Z.ogg"
    Rom "За мной должок, Катька."
    show Kate Normal m_day_winter 00 evil aside 02
    show Romka Evil b_day_winter 01 normal aside 01
    with Dissolve(.3)
    voice "voice/kate/107 KA.ogg"
    Kate "Ой, не благодари, Ромочка. Я всегда на страже настоящей любви!"
    show Kate Normal m_day_winter 00 evil ahead 01 with Dissolve(.3)
    show Romka Evil b_day_winter 01 normal ahead 01
    show Kate Normal m_day_winter 00 evil ahead 02:
        yoffset 0
        linear 0.15 yoffset 30
        linear 0.15 yoffset 0
        repeat 3
    with Dissolve(.3)

    voice "voice/kate/108 KA.ogg"
    Kate "Да-да-да!"
    play test_two "sounds/steps/sfx_girl_leaves_on_snow.ogg"
    show Kate Kawai m_day_winter 00 evil ahead 01:
        .25
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 10
            repeat 20
        parallel:
            linear 10.0 xpos 1250
        parallel:
            time 6
            "Kate Kawai m_day_winter 00 evil aside 01" with Dissolve(.3)
    with Dissolve(.25)
    play test_one "voice/kate/113 KA.ogg"
    "«{i}Клянусь, я убью тебя!{/i}»"
    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
    voice "voice/romka/3day/58 T.ogg"
    Rom "Так, я не слышу: ты к Полине подходил или нет?"
    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)
    voice "voice/anton/3day/087 M.ogg"
    Ant "Мы... так... болтали."
    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
    voice "voice/romka/3day/59 B.ogg"
    Rom "Болтать будешь кишками, когда я тебе брюхо вскрою."
    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)
    play fon "sounds/fon/wind.ogg" fadein 10
    "Лезвие плашмя прошлось по моему рукаву вверх и достало до воротника."
    "Ветер остужал лицо, но струйка пота стекла по виску."



    if ROUTE_SOLO:
        $ story_manager.MarkEvent(("day3", "scene13a"))
        "Вдруг в голове щёлкнул рубильник, и всё встало на свои места."
        "Я вспомнил беглые взоры, которые Ромка посылал Полине."
        "Вспомнил его каракули в анкете – и почему я не удосужился как следует изучить их?"
        show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
        voice "voice/romka/3day/60 Ese.ogg"
        Rom "Ещё раз замечу рядом с Полинкой – пеняй на себя. Шишкой не отделаешься."
        show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)
        show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
        voice "voice/romka/3day/60 Us.ogg"
        Rom "Усёк?"

        scene day3_cornermeet_bg_fence_default
        show day3_cornermeet_fence_anton
        with Dissolve(.5)
        show day3_cornermeet_fence_anton_02 with Dissolve(.5)


        voice "voice/anton/3day/089 Da_l.ogg"
        Ant "Да."

        hide day3_cornermeet_fence_anton_02 with Dissolve(.5)
        voice "voice/romka/3day/61 P.ogg"
        Rom "Пшёл вон!"
        "Вероятно, я был так загипнотизирован ножом, что Роме пришлось повторить."
        scene bg school_corner_day1_no_squirrel:
            yalign 0.8 xalign 0.5
            linear .15 zoom 1.05
            linear .25 zoom 1.00
        show Byasha Normal m_day_winter 01 normal ahead 01:
            yalign .5
            xpos .5
            xanchor .5
            xoffset -450
            zoom 1.0
            xzoom -1
            linear .15 zoom 1.05
            linear .25 zoom 1.01
        show Romka Evil b_day_winter 01 normal ahead 03:
            yalign .5
            xpos .5
            xanchor .5
            zoom 1.0
            linear .15 zoom 1.2
            linear .25 zoom 1.1
        show focus_lines_bright:
            align (.5,.5)
            alpha 0
            linear .5 alpha 1

        $ music_during_lines = 1.0
        voice "voice/romka/3day/62 Von.ogg"
        Rom "Вон!"

        scene bg_school_corner_day_onhide2_p1
        show Byasha Normal m_day_winter 01 normal ahead 01:

            yalign .5
            xpos .5
            xanchor .5
            xoffset -450
            xzoom -1

            easeout 4.5 xpos -0.5
        show Romka Evil b_day_winter 01 normal ahead 01:
            yalign .5
            xpos .5
            xanchor .5
            zoom 1.1
            easeout 4.5 xpos -0.5
        show bg_school_corner_day_onhide2_p2
        with Dissolve(.5)
        "Ретируясь с площадки, я думал о холодном остро заточенном металле."
        "И спрашивал себя, хватит ли мне духа нарушить данное ублюдкам слово."


    if ROUTE_POLINA:


        if not Flags.Has("amulet"):
            $ story_manager.MarkEvent(("day3", "scene13b"))
            show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
            voice "voice/romka/3day/63Na.ogg"
            Rom "Наверное, мне надо объяснить так, чтобы ты понял..."
            show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)

            scene romka_stab_1 with Dissolve(.5)

            "Рукояти и клинок завертелись в опасной пляске, как лопасти вертолёта, сметающие всё на своём пути."
            play test_two "voice/romka/3day/64 Bax.ogg"

            window hide
            scene romka_stab_animation
            pause 1.
            "Я попытался увернуться, как тут же бритвенно-острый наконечник спикировал в моё плечо."
            play test_one "sounds/sfx_knife_stab_in.ogg"

            scene romka_hit_scene_animation with hpunch
            pause 4
            "Шокированный, я видел, как нож с рвущимся треском погружается в меня, заполняя образовавшуюся канавку кровью."
            "Адреналина уже было недостаточно, и пронзающая боль вырвалась из меня жалобным криком."
            voice "voice/anton/3day/088 AAAAAA.ogg"
            Ant "А-а-а-а-а-а-а-а!"
            play test_one "sounds/sfx_knife_stab_out.ogg"

            scene bg school_corner_day1_no_squirrel:
                yalign 0.8 xalign 0.5
            show Romka Evil m_day_winter 03 normal ahead 01
            with Dissolve(.5)


            play test_two "voice/anton/3day/088 Au.ogg"
            "Ромка грубо вытащил нож и я, зажав кровоточащую рану, бросился прочь без оглядки."
            play sound "sounds/steps/loop_snow_footsteps.ogg"
            scene bg_school_corner_day_onhide2_p1
            show Romka Evil m_day_winter 03 normal ahead 02:
                yalign .5
                xpos .5
                xanchor .5
                easeout 2.5 xpos -0.5
            show bg_school_corner_day_onhide2_p2
            show expression "#000":
                alpha 0
                2.
                linear 3. alpha 1
            pause 2
            voice "voice/romka/3day/65 Po.ogg"
            Rom "Попробуй ещё раз позабудь!"
            stop sound fadeout 3
            voice "voice/romka/3day/66 Ant.ogg"
            Rom "Антоша!"
            stop music2 fadeout 3.5
            window hide
            pause 3
        else:


            $ story_manager.MarkEvent(("day3", "scene13c"))
            show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(.3)
            voice "voice/romka/3day/63Na.ogg"
            Rom "Наверное, мне надо объяснить так, чтобы ты понял..."
            show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(.3)

            window auto
            scene romka_stab_1 with Dissolve(.5)

            "Рукояти и клинок завертелись в опасной пляске, как лопасти вертолёта, сметающие всё на своём пути."
            play test_two "voice/romka/3day/64 Bax.ogg"

            stop music2 fadeout 2

            window hide
            scene romka_stab_animation
            pause 1.
            "Я попытался увернуться, но, сделав шаг назад, поскользнулся и грохнулся на пятую точку."
            play test_one "sounds/fall.ogg"

            scene day3_cornermeet_amulet_bg:
                align (.5,.5)
                zoom 1.01
                .35
                block:
                    linear .05 xoffset 3
                    linear .05 xoffset -3
                    repeat 2
            show day3_cornermeet_amulet_anton 1:
                xpos .1
                ypos 1.
                yanchor 1.
                linear .35 xpos .0 yanchor .9

                block:
                    linear .05 xoffset 5
                    linear .05 xoffset -5
                    repeat 2

            with Dissolve(.5)
            play music2 "music/Khoomey Tale, intro.ogg" volume 3.5 fadeout 1.5
            queue music2 "music/Khoomey Tale, looped.ogg" volume 3.5
            "Амулет Полины будто того и ждал — бросился из-под воротника навстречу острию ножа."

            show day3_cornermeet_amulet_anton 2 with Dissolve(.5)
            pause 1.
            play test_two "sounds/sfx_tissue.ogg"
            show day3_cornermeet_amulet_anton 3 with Dissolve(.5)
            "Подвеска не дала когтю впиться в шею обидчика, и оберег глухо рухнул мне на грудь."

            "Казалось, колотые раны вот-вот посыпятся на меня в таком количестве, что я захлебнусь собственной кровью."

            show day3_cornermeet_amulet_anton 4 with Dissolve(.5)
            "Но почему-то Ромка застыл, словно завороженный."

            scene day3_cornermeet_eye with Dissolve(.5)
            "Он стоял с занесённой для удара рукой и, вытаращившись на побрякушку, рычал что-то злобное и нечленораздельное."
            "Полинин подарок одним свои видом бесил Ромку, но одновременно связывал его руки."

            scene bg school_corner_day1_no_squirrel:
                yalign 0.8 xalign 0.5
            show Byasha Doubt m_day_winter 01 normal aside 01:
                xoffset 0
                xpos 1400
                xanchor .5
            show Romka Worry b_day_winter 01 worry ahead 02:
                xzoom -1
                xoffset 0
                xpos 900
                xanchor .5
            with Dissolve(.5)

            "Это длилось неестественно долгое время, так что Бяша с непониманием нахмурился."

            show Byasha Doubt m_day_winter 01 normal ahead 01:
                .5
                yoffset 10
                "Byasha Scared m_day_winter 01 shock ahead 01" with Dissolve(.5)
                .5
                parallel:
                    .5
                    linear .25 alpha 0

                parallel:
                    linear .75 xoffset -400

                parallel:
                    linear .1 yoffset 0
                    linear .1 yoffset 10
                    repeat 4
            show Romka Worry b_day_winter 01 worry ahead 01
            with Dissolve(.5)
            play test_two "sounds/steps/snow_stepF02.ogg"
            play sound "sounds/sfx_touch_window0.ogg"
            "Где-то наверху скрипнуло открывающееся окно..."
            play test_one "sounds/sfx_open_window.ogg"



            show Romka Worry b_day_winter 01 worry aside 01
            show teacher_OR
            if Flags.Has("myth3"):
                show d3_myth
            with Dissolve(.5)
            voice "voice/lydia/3day/08 Pyatifanov.ogg"
            Teacher "Пятифанов!"
            hide teacher_OR
            with Dissolve(.5)
            "Адреналина уже было предостаточно, и, почти взлетев с места, я бросился прочь."
            "Ромка ожил, когда я был уже далеко, и бросил мне вслед пугающее напоминание:"
            play test_one "sounds/steps/loop_snow_footsteps.ogg" loop

            scene bg_school_corner_day_onhide2_p1
            show Romka Evil b_day_winter 01 normal ahead 01:
                yalign .5
                xpos .5
                xanchor .5

                parallel:
                    easeout 4.5 xpos -0.5
                parallel:
                    2.
                    "Romka Evil b_day_winter 01 normal ahead 02"
            with Dissolve(.5)
            show bg_school_corner_day_onhide2_p2
            show expression "#000":
                alpha 0
                2.
                linear 3. alpha 1
            pause 2
            stop test_one fadeout 4
            voice "voice/romka/3day/65 Po.ogg"
            Rom "Попробуй ещё раз позабудь!"
            stop music2 fadeout 1.5
            voice "voice/romka/3day/66 Ant.ogg"
            Rom "Антоша!"
            window hide
            pause 3


    jump day3_olyatalk


label day3_olyatalk:

    jump dev_d3_olyatalk.end
    label dev_d3_olyatalk:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Выбери рут"
            "Полина":
                $ ROUTE_POLINA = True
                $ Flags.Raise("day2 polina")
            "Лиса":
                $ ROUTE_FOX = True
                $ Flags.Raise("day2 fox")
            "Маска":
                $ ROUTE_SOLO = True
                $ Flags.Raise("mask")
        menu:
            "Добыть печатку":
                $ Flags.Raise("finger")
            "Не брать":
                pass
        menu:
            "Добыть номер":
                $ Flags.Raise("number")
            "Не брать":
                pass
        menu:
            "Добыть кассету":
                $ Flags.Raise("record")
            "Не брать":
                pass
        label dev_d3_olyatalk.end:

    $ story_manager.MarkEvent(("day3", "scene14"))
    scene table_home with Dissolve(.5)
    window show
    stop fon fadeout 1
    play music2 "music/9_Nikita Kryukov - the Obscurity.ogg" volume 0.85 fadein 0.5
    play test_one "sounds/tabl-fix.ogg"
    "Во рту стоял привкус гадкой воды, которой я запил лекарства."
    play test_one "sounds/glotok-fix.ogg"


    if ROUTE_POLINA and not Flags.Has("amulet"):
        "Обработанный йодом порез ныл под бинтом с махристыми краями."
        "Я не сказал родителям правду, как это получилось, сославшись на то, что наткнулся на острый сук в лесу."
        "Всё ждал более удобного случая, когда у вечно занятых мамы с папой появится на меня время."

    "Все мысли занимала только Полина."


    if ROUTE_SOLO:
        "И та угроза Ромки, если я вновь к ней приближусь."


    if ROUTE_FOX:
        "И тот спектакль, где Ромка уготовил мне роль злодея."

    scene day2_siluet_room_bg:
        xalign .0
        block:
            linear 10. xalign 1.
            1.
            linear 10. xalign .0
            1.
            repeat

    show Olya Chat amaze:
        xanchor .5
        xpos .65
        block:
            linear 10. xpos .35
            1.
            linear 10. xpos .65
            1.
            repeat
    with Dissolve(.7)

    play test_two "voice/olya/3day/01 bla.ogg" loop
    play test_one"voice/anton/3day/02 Aha.ogg"
    play sound "sounds/steps/Anton-steps-out-1.ogg"
    "Я бродил по дому, будто пьяный, поддакивал сестре, толком не разбирая, о чём она говорит."

    show Olya Chat happy
    with Dissolve(.5)
    play test_one"voice/anton/3day/02 Ahaa.ogg"
    "Оля же талдычила без перебоя, то и дело вскидывая руки и смеясь, как вдруг так же резко смолкла и уставилась на меня до боли знакомым колючим маминым взглядом."
    show day2_siluet_room_bg:
        linear .5 xalign .5
    show Olya Chat serious:
        linear .5 xpos .5
    stop music2
    stop test_two fadeout 0.2
    play test_two"voice/anton/3day/03 A.ogg"
    "Меня буквально выдернуло из темницы разума, где клокочущие мысли, подобно гарпиям, обрушивались на мой искусанный мозг, не давая вернуться в реальность."
    play music "music/SilentWhispering.ogg" fadein 0.5
    "Я уставился на сестру — сейчас она была миниатюрной копией мамы."
    "Точнее тем, в кого она превратилась с момента переезда сюда: с её грозной позой в виде заглавной буквы «Ф» и вздёрнутыми к потолку бровями."

    $ music_during_lines = 0.75
    show Olya Serious b_evening 01 good ahead 09 with Dissolve(.3)
    voice "voice/olya/3day/02 Ti.ogg"
    Oly "Ты меня не слушал, так?!"
    show Olya Serious b_evening 01 good ahead 08 with Dissolve(.3)

    play test_one "voice/olya/3day/03 Hm.ogg"
    "Она брызнула ядом в мою сторону, копируя мимику и интонации чуть ли не единственного человека, с кем проводила всё своё свободное время."
    "На мгновение мне показалось, что свет, излучаемый Олей все эти годы, стал слабее и опасно затрепыхался на ветру затянувшихся перемен. "
    "Еще немного — и моя прекрасная принцесса станет драконом, который сторожил её в своей башне. А это пугало сильнее подкрадывающихся ко мне ужасов из будущего."

    voice "voice/anton/3day/04 Ol.ogg"
    Ant "Оля, прости..."
    voice "voice/anton/3day/05T.ogg"
    Ant "Ты же не сердишься, правда? Я просто задумался."
    $ music_during_lines = 1.0

    "Взгляд заметался по комнате, как загнанный в ловушку зверь, перескакивая с одного предмета на другой, силясь найти хоть что-нибудь, что могло отвлечь Олю."

    stop music fadeout 8

    voice "voice/anton/3day/06 A.ogg"
    Ant "А давай в приставку поиграем!"

    show Olya Serious b_evening 00 good ahead 01 with Dissolve(.5)

    "Оля нахохлилась, однако искорка интереса вспыхнула в её изумрудных глазках. "
    play music2 "music/25_Olya.ogg" volume 0.7 fadein 2
    "И ледяной осколок, занесённый Снежной королевой, начал потихоньку оттаивать."

    show Olya Serious b_evening 00 good ahead 03 with Dissolve(.3)
    voice "voice/olya/3day/04 A.ogg"
    Oly "А как же второй джойстик? Не работает же."
    show Olya Serious b_evening 00 good ahead 01 with Dissolve(.3)
    show Olya Serious b_evening 00 good ahead 03 with Dissolve(.3)
    voice "voice/olya/3day/05 A.ogg"
    Oly "А папе починить некогда..."
    show Olya Serious b_evening 00 good ahead 01 with Dissolve(.3)

    voice "voice/anton/3day/07 M.ogg"
    Ant "М-м-м... Можем из пистолета пострелять."
    voice "voice/anton/3day/08 V.ogg"
    Ant "В ковбоев или уток, хочешь?"

    show Olya Serious b_evening 00 good ahead 05 with Dissolve(.3)
    voice "voice/olya/3day/06 T.ogg"
    Oly "Ты лучше меня играешь." id dev_d3_olyatalk_end_33067940
    show Olya Serious b_evening 00 good ahead 01 with Dissolve(.3)

    voice "voice/anton/3day/09 Da.ogg"
    Ant "Да ладно тебе."
    voice "voice/anton/3day/10 P.ogg"
    Ant "Поди, целый день тренировалась, пока меня дома не было."

    show Olya Happy b_evening 00 good ahead 07 with Dissolve(.5)

    play test_one "voice/olya/3day/07 Pf.ogg"
    "Оля прыснула со смеха. Ледяное сердце окончательно растаяло."

    show Olya Happy b_evening 00 good ahead 07 with Dissolve(.3)
    voice "voice/olya/3day/08 A.ogg"
    Oly "А как ты догадался?"
    show Olya Happy b_evening 00 good ahead 05 with Dissolve(.5)
    show Olya Happy b_evening 00 good ahead 07 with Dissolve(.5)
    voice "voice/olya/3day/09 Ya.ogg"
    Oly "Я сейчас знаешь какая меткая? Считай, уже проиграл."
    show Olya Happy b_evening 00 good ahead 08 with Dissolve(.3)

    voice "voice/anton/3day/11 Ne.ogg"
    Ant "Не на того напала! Включай скорее!"
    play test_five "sounds/creaks-2.ogg"
    play test_two "sounds/steps/Olya_out.ogg"

    hide Olya with Dissolve(.5)

    if Flags.Has("finger"):
        window hide
        call screen day3_open_box()
label open_box_table:
    if Flags.Has("finger"):
        play test_two "sounds/steps/Anton-steps-steal-0.ogg"
        scene day2_siluet_room_bg:
            xalign .5
            linear .5 zoom 1.1
        show bg_storage_in_table_day_3_evn_01 with Dissolve(0.5):
            alpha 0
            pause .4
            linear .2 alpha 1
        pause 1
        play test_one "sounds/desk-open-00.ogg" 
        show bg_storage_in_table_day_3_evn_02
        if Flags.Has("number"):
            show item_in_table_number_day_3_evn
        if Flags.Has("glove"):
            show item_in_table_glove_day_3_evn
        if Flags.Has("record"):
            show item_in_table_record_day_3_evn

        with Dissolve(0.5)

        "Я спрятал печатку Семёна в ящик письменного стола."
        play test_two "sounds/vhs/Vhs_put.ogg"
        show pechatka_day_3_evn with Dissolve(0.5)
        "Хотя сам до конца так и не понял — поступил ли я правильно украв у милиционера важную улику."
        play test_one "sounds/desk-close-00.ogg"
        scene bg_storage_in_table_day_3_evn_01 with Dissolve(0.5)
        play test_one "sounds/steps/Anton-steps-out-1.ogg"
        "Наконец, я перебрался в комнату сестры."

    play test_one "sounds/close-door.ogg"
    stop music2 fadeout 2

    window auto





    $ story_manager.MarkEvent(("day3", "scene15"))

    scene bg_black with Dissolve(.5)

    play test_five "sounds/steps/Olya_in.ogg"
    play test_two "sounds/steps/Anton-steps-in-1.ogg"
    $ renpy.pause(4.5, hard=True)

    play sound "sounds/sfx_tv_warming_noise.ogg"
    show day3_tv_frame zorder 1 with None
    show day3_tv_loop:
        alpha 0
        easeout 10 alpha 1

    $ renpy.pause(1, hard=True)

    play music "music/18_Olya_(piano&strings).ogg" volume 0.8 fadein 0.5
    play test_one "voice/olya/3day/10 V.ogg"
    play test_seven "sounds/sfx_plug_console.ogg"
    "Малютка подскочила к телевизору и, щёлкнув питанием, начала вслепую шарить по задней стенке «Фотона», явно пытаясь воткнуть кабель от приставки в гнездо антенны."

    scene day3_dendy_bg frames
    show goose_olya_back:
        yalign 1.
        xalign 1.
    show day3_dendy_anton zorder 1
    with Dissolve(.5)
    $ add_text_to_dictionary(34)
    play sound "sounds/vhs/TV.ogg" loop
    "Отрывки из телепередач маячили на ламповом экране, пока Оля листала до канала, где ловила заветная «{u}Денди{/u}»."
    stop test_seven fadeout 2

    voice "voice/anton/3day/12 Ch.ogg"
    Ant "Что дома интересного происходило?"

    "Вопрос был обывательским — я даже и не задумался над его значением."

    hide goose_olya_back
    show Olya Prof b_evening 00 good aside 01:
        xoffset 600
    with Dissolve(.5)

    stop music fadeout 5
    stop test_one fadeout 1
    play test_five "voice/olya/3day/11 V.ogg"
    stop sound fadeout 5
    "Однако Оля внезапно изменилась в лице и растеряла обретённую дорогой ценой детскую невозмутимость."



    voice "voice/anton/3day/13 Ol.ogg"
    Ant "Оль, что-то случилось?"

    play test_one "sounds/Chtoto3.ogg"
    "Сестрёнка вставила кабель на место и, вытащив испачканную ручонку, стала неуклюже отряхивать пыль. "

    show Olya Serious b_evening 00 good ahead 01:
        xzoom -1
        xoffset 500
    with Dissolve(.5)
    "Она явно искала в себе силы, чтобы начать разговор."
    play test_one "sounds/steps/Olya-steps-3.ogg"



    scene day3_dendy_bg noise
    show Olya Serious b_evening 00 good ahead 01:
        xzoom -1
        xoffset -100

    show day3_dendy_anton
    with Dissolve(1.)
    show Olya Serious b_evening 00 good ahead 02:
        xzoom -1
        xoffset -100

    play music "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 0.1
    voice "voice/olya/3day/13 Ma.ogg"
    Oly "Мама..."
    show Olya Serious b_evening 00 good ahead 01:
        xzoom -1
        xoffset -100
    play test_one "voice/olya/3day/15 ona.ogg"
    "Она замолчала, и на секунду показалось, что на её глазах выступили слезы."

    show Olya Weeps b_evening 00 good ahead 05 with Dissolve(.3)

    stop test_one fadeout 0.2
    $ music_during_lines = 0.75
    voice "voice/olya/3day/16 U.ogg"
    Oly "У неё опять был этот страшный..."

    show Olya Weeps b_evening 00 good ahead 01 with Dissolve(.3)

    "Оля взглянула на меня мокрыми глазёнками-блюдцами."

    scene bg_black with Dissolve(1.5)

    voice "voice/anton/3day/14 P.ogg"
    Ant "... приступ."

    show koshmar:
        alpha 0.0
        linear 2. alpha 1.0

    "Такое случалось и раньше, но довольно редко, а когда мы перебрались в этот богом забытый край — мамины приступы пугающе участились."

    scene day3_karp with Dissolve(1.)
    voice "voice/olya/3day/17 Pa.ogg"
    Oly "Папа принёс большую рыбу..."

    show bg_black:
        alpha 0.0
        linear 2. alpha 1.0

    voice "voice/olya/3day/18 Ona.ogg"
    Oly "Она в газету была завёрнута и пахла так... Бэ..."

    scene day3_dendy_bg noise
    show Olya Weeps b_evening 00 good ahead 05:
        xoffset -100
    show day3_dendy_anton
    with Dissolve(1.)

    voice "voice/olya/3day/19 A.ogg"
    Oly "А мама опять начала злиться, потом взяла нож."

    window show

    scene day3_bigwin:
        xalign 1.
    with Dissolve(.5)

    play test_one "voice/olya/3day/14 m.ogg"
    "Оля поёжилась, с опаской выглянув в окно."
    voice "voice/olya/3day/20 O.ogg"
    Oly "Они начали громко ругаться и..."

    scene bg_black with Dissolve(.5)

    scene bunny_nightmare_bg
    show Olya Suffer b_day 00 good ahead 07
    show bg_black:
        linear 2. alpha .0

    play test_one "voice/olya/3day/15 Hnuk2.ogg"
    "Я замер, представляя, как сестрёнка, такая маленькая и незаметная, стояла посреди кухонного проёма."
    play test_one "voice/olya/3day/25 Hnuk1.ogg"
    "Она даже не пыталась спрятаться: родители попросту её не замечали."

    voice "voice/olya/3day/21E.ogg"
    Oly "И потом мама ударила."

    show Olya Suffer b_day 00 good ahead 07:
        linear .10 yoffset 50
        linear .25 yoffset 0

    voice "voice/olya/3day/22 V.ogg"
    Oly "Вот так."

    "Оля едва дёрнула кулачком сверху вниз, имитируя удар."

    scene day3_karp2 with Dissolve(.5)

    play sound "sounds/loop_fish_beating.ogg" loop
    voice "voice/olya/3day/23 R.ogg"
    Oly "Рыбу."
    voice "voice/olya/3day/24 O.ogg"
    Oly "Она была живая, Тош. Ей было больно, а мама... мама..."

    "Мне было легко представить, что было дальше: извивающаяся рыба с воткнутым в жабры клинком брызнула зловонной слизью на мамино лицо."
    show bg_black:
        alpha 0.0
        linear 2. alpha 1.
    stop sound fadeout 2
    "Если смерть приближалась так близко к маме, как в тот день, когда при нас человека сбило автобусом, и кровь размазалась по лобовому стеклу..."
    "Или когда бабушка отрубила голову цыплёнку — мама всегда впадала в странный пугающий до дрожи приступ."
    play test_seven "sounds/sfx_seizure.ogg" loop

    hide bg_black
    show day3_karp_ep:
        align (.5,.5)
        zoom 1.02
        block:
            yoffset 5
            .05
            yoffset 0
            .05
            repeat
    show bg_black:
        alpha .35
        .05
        alpha 0
        .05
        repeat
    with Dissolve(.5)

    "Её глаза закатывались, она падала навзничь, как спиленное дерево, и извивалась, как та самая бившаяся в агонии рыба, переворачивая стулья и выплёвывая обрывки пугающих фраз."

    voice "voice/anton/3day/15 A.ogg"
    Ant "А папа? Он ей помог?"

    play test_one "voice/olya/3day/25 Hnuk.ogg"
    "Оля вздрогнула, как будто бы воспоминания ранили её."

    voice "voice/olya/3day/26 Da.ogg"
    Oly "Да. Но в начале..."


    scene day3_karp_dad_bg
    show day3_karp_dad laugh
    show day3_karp_dad_frame
    with Dissolve(.5)
    voice "voice/olya/3day/27 On.ogg"
    Oly "Он засмеялся, Тоша!"
    play test_three "voice/father/day_2/Haha2.ogg"
    stop test_seven fadeout 3


    voice "voice/olya/3day/28 T.ogg"
    Oly "Так страшно, когда увидел, что маме плохо..."
    show day3_karp_dad cry with Dissolve(.5)
    play test_three "voice/father/day_2/110 hnik.ogg"

    voice "voice/olya/3day/29 A.ogg"
    Oly "А потом вдруг заплакал."
    $ music_during_lines = 1.0

    "От услышанного у меня дёрнулась бровь."

    show koshmar:
        alpha 0.0
        linear 2. alpha 1.0

    "Безумие, источаемое лесом и окончательно завладевшее мамой, перебросилось и на нашего сильного и храброго отца."
    play sound "sounds/vhs/tv_noise.ogg" fadein 3 loop

    scene day3_karp_hug_bg
    show day3_karp_hug
    with Dissolve(.5)
    stop music fadeout 8
    play test_two "sounds/steps/Anton-steps-steal-0.ogg"
    "Я быстро шагнул навстречу Оле, заключив её в крепкие объятия."
    "Она уткнулась мордашкой мне в грудь, и я почувствовал, как рубашка сделалась мокрой."

    voice "voice/olya/3day/30 Z.ogg"
    Oly "Зачем они так издеваются друг над другом, Тош?"

    show day3_karp_hug_alter
    with Dissolve(.5)

    voice "voice/olya/3day/31 Oni.ogg"
    Oly "Они сумасшедшие?"

    scene day3_bigwin:
        xalign 1.
    with Dissolve(.5)
    "Не находя, как оправдать родительское поведение, я запнулся."


    play test_two"voice/anton/3day/16 Vzd.ogg"
    "Слова иссякли, и всё, что я мог, так это покрепче обнять Олю."
    stop test_one fadeout 2.5



    window hide
    queue wtf [ "<silence 1.8>", "<from 0 to 6>sounds/Vid_glich.ogg"]

    scene day3_bigwin:
        xalign 1.
        1.5
        linear .23 xalign 0.0
    $ renpy.pause(delay=1.73, hard=True)

    play movie "video/Vid_Glich3.webm"
    play wtf "sounds/Vid_glich.ogg"
    $ renpy.pause(delay=5, hard=True)
    stop movie

    scene day3_preduck_olya_room_vid:
        align (.5,.5)
        zoom 1.1
        linear .25 zoom 1.

    play test_one "voice/olya/3day/32 Vopit.ogg"
    "Оля в ужасе вскрикнула и спряталась за меня."

    voice "voice/olya/3day/33 Per .ogg"
    Oly "Переключи, переключи скорей!"

    "Сколько бы раз она ни видела эту заставку, всё время реагировала одинаково... как и при виде совы."
    stop sound fadeout 2
    play test_two "sounds/vhs/button_2.ogg"
    play fon "sounds/rep/tv-noise-2.ogg" fadein 1
    scene day3_preduck_olya_room with Dissolve(.5)
    play test_two"voice/anton/3day/17 Espug.ogg"
    $ add_text_to_dictionary(29)
    "У меня самого выступали мурашки при появлении этого {u}призрачного лица{/u}, поэтому я моментально исполнил пожелание сестры."
    stop fon fadeout 2

    jump day3_goosehunt

label day3_goosehunt:

    scene bg_black

    show day3_dendy:
        yalign 1.
    with Dissolve(.5)

    call screen day3_dendy_btn()

    hide day3_dendy
    show day3_dendy:
        ypos -1519
        1.
        linear 2. ypos 0
    play test_one "sounds/sfx_plug_cartridge.ogg"
    show day3_dendy_2:
        1.
        linear 2. ypos 1519

    show day3_dendy_tv_noise:
        ypos -1519
        1.
        linear 2. ypos 0
    show day3_dendy_black:
        alpha .9
        ypos -1519
        1.
        linear 2. ypos 0

    with Dissolve(.5)

    pause 2

    scene day3_dendy_9999
    queue sound [ "<silence 1.8>", "<from 0 to 8>sounds/sfx_dendy.ogg"]
    show goosehunt_tv
    show goosehunt_jack
    with Dissolve(1.)

    "Наконец на экране появился список многоигровки, идущей в комплекте вместе с приставкой."
    stop sound fadeout 1

    scene goosehunt_select_bg
    show goosehunt_select_menu
    show chaika:
        xpos 345
        ypos 165
    show goosehunt_tv
    show goosehunt_jack
    with Dissolve(.5)
    play music2 "audio/huntgoose/game_select_bg.ogg" fadeout 2
    "Досадно, что большинство наименований на этом картридже были просто другими уровнями одной и той же игры."

    $ chaika_dt = 3.0
    show chaika:
        xpos 345
        ypos 165 + 45 *0
        chaika_dt
        ypos 165 + 45 *1
        chaika_dt
        ypos 165 + 45 *2
        chaika_dt
        ypos 165 + 45 *3
        chaika_dt
        ypos 165 + 45 *4
        chaika_dt
        ypos 165 + 45 *5
        chaika_dt
        ypos 165 + 45 *6
        chaika_dt
        ypos 165 + 45 *7
        chaika_dt
        ypos 165 + 45 *8
        chaika_dt
        ypos 165 + 45 *9
        chaika_dt
        ypos 165 + 45 *10
        chaika_dt
        ypos 165 + 45 *11
        chaika_dt
        ypos 165 + 45 *12
        chaika_dt
        ypos 165 + 45 *13
        chaika_dt
        repeat
    show dendy_controller zorder 5:
        xalign .5
        yalign 1.
        yoffset 200
        alpha 0
        linear .5 yoffset 100 alpha 1

    "Я подобрал серый прямоугольный джойстик и стал выискивать в пиксельном многообразии знакомые английские слова про утиную охоту."

    show Olya Happy b_evening 00 good ahead 01 behind dendy_controller:
        xanchor .5
        xpos 1800
        alpha 0
        zoom 1.2
        yalign .5
        linear .25 xpos 1750 alpha 1
        linear .25 xpos 1700

    play test_one "sounds/steps/Olya-steps-5.ogg"

    "Фоновая музыка подействовала на Олю умиротворяюще, и она спокойно поинтересовалась:"

    show Olya Happy b_evening 00 good ahead 02 behind dendy_controller with Dissolve(.2)
    $ music_during_lines = 0.65
    voice "voice/olya/3day/34 Aka.ogg"
    Oly "А как твои дела в школе?"
    show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)

    if ROUTE_POLINA:
        $ story_manager.MarkEvent(("day3", "scene16a"))
        voice "voice/anton/3day/34 Ya.ogg"
        Ant "Я с одной девочкой подружился."

        show Olya Happy b_evening 00 good ahead 02 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/54 A.ogg"
        Oly "А она красивая?"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        "Я смутился."
        voice "voice/anton/3day/35 Nu.ogg"
        Ant "Ну... я не знаю."
        show Olya Happy b_evening 00 good ahead 06 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/55 Xa.ogg"
        Oly "Ха, ты засмущался. Значит очень красивая!"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/36 Pe.ogg"
        Ant "Перестань, Оль."
        show Olya Happy b_evening 00 good ahead 08 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/56 Vl.ogg"
        Oly "Влюбился! Влюбился!"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/37 Ol.ogg"
        Ant "Оля, блин, сейчас не буду с тобой играть."
        show Olya Happy b_evening 00 good ahead 05 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/57 D.ogg"
        Oly "Ха-ха! Да я пошутила!"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        show Olya Happy b_evening 00 good ahead 02 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/58 A.ogg"
        Oly "А ты нас познакомишь?"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/38 Nu.ogg"
        Ant "Ну, может быть."
        show Olya Happy b_evening 00 good ahead 03 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/59 Ak.ogg"
        Oly "А как её зовут?"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/39 P.ogg"
        Ant "П-полина..."
        show Olya Happy b_evening 00 good ahead 05 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/60 Pok.ogg"
        Oly "А ты покраснел!"
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        show Olya Happy b_evening 00 good ahead 04 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/61 A.ogg"
        Oly "А где вы будете жить, когда поженитесь?"
        show Olya Happy b_evening 00 good ahead 08 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/40 M.ogg"
        Ant "Мы будем играть или нет?"

    if ROUTE_FOX:
        $ story_manager.MarkEvent(("day3", "scene16b"))
        voice "voice/anton/3day/41 Da.ogg"
        Ant "Да вот завёл пару друзей... наверное."
        show Olya Happy b_evening 00 good ahead 04 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/63 Og.ogg"
        Oly "Ого! Целых двух. Везёт."
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/42 A.ogg"
        Ant "А ты говоришь, лисичку видела?"
        show Olya Happy b_evening 00 good ahead 06 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/64 Aga.ogg"
        Oly "Ага. Её зовут Алиса."
        show Olya Happy b_evening 00 good ahead 05 behind dendy_controller with Dissolve(.2)
        "Мне резко стало не по себе при упоминании новой знакомой."
        voice "voice/anton/3day/43 Ot.ogg"
        Ant "Откуда ты знаешь? Она так сказала?"
        show Olya Happy b_evening 00 good ahead 07 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/64 da.ogg"
        Oly "Да, когда с мамой мусор ходили выбрасывать. А ещё говорила, что спасла тебя."
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/44 S.ogg"
        Ant "Спасла?.."
        "Тут же вспомнилась перепалка с хулиганами в лесу, а затем таинственный шепоток из чащи."
        "Как улепётывал побитый Семён, и как склонялся надо мной, заслоняя луну, рогатый великан."
        "Всё это время я будто бы ощущал незримое присутствие Алисы. Словно она следила за мной из-за кривых стволов деревьев с застывшей улыбкой на рыжей маске."
        "Я вздрогнул, прогоняя наваждение."
        voice "voice/anton/3day/45 A.ogg"
        Ant "А ещё она что-нибудь говорила?"
        show Olya Happy b_evening 00 good ahead 02 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/65 Nea.ogg"
        Oly "Не-а."
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        show Olya Happy b_evening 00 good ahead 03 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/66 Ma.ogg"
        Oly "Мама так быстро вернулась. Я её хотела с лисичкой познакомить, а та уже убежала."
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)
        voice "voice/anton/3day/46 T.ogg"
        Ant "Ты её не боишься?"
        show Olya Happy b_evening 00 good ahead 05 behind dendy_controller with Dissolve(.2)
        show Olya Happy b_evening 00 good ahead 06 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/67 A.ogg"
        Oly "А почему я должна бояться? Алиса добрая, такая пушистая и красивая..."
        show Olya Serious b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.4)
        show Olya Serious b_evening 00 good ahead 02 behind dendy_controller with Dissolve(.2)
        voice "voice/olya/3day/68 Ne.ogg"
        Oly "Не то что сова."
        show Olya Happy b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)

    if ROUTE_POLINA or ROUTE_FOX:
        show goosehunt_select_noise behind goosehunt_tv
        show chaika behind goosehunt_select_noise:
            xpos 345
            ypos 165 + 45 *10
        pause .25
        hide goosehunt_select_noise

        hide dendy_controller
        show dendy_controller_3 zorder 5:
            xalign .5
            yalign 1.
            yoffset 100
            1.
            linear .5 yoffset 200 alpha 0
        play test_two"voice/olya/47A O.ogg"
        "Я вставил световой пистолет в гнездо от второго джойстика под смешок сестры."


        hide Olya
        show goose_olya zorder 4:
            zoom 1.2
            yalign .5
            xoffset -300
        with Dissolve(.5)

        voice "voice/olya/3day/62 Chu.ogg"
        Oly "Чур, я первая!"
        stop music2 fadeout 2
        window hide

    if ROUTE_SOLO:
        $ story_manager.MarkEvent(("day3", "scene16c"))
        voice "voice/anton/3day/18 Ni.ogg"
        Ant "Ничего хорошего."
        stop music2 fadeout 2

        voice "voice/anton/3day/19 Sh.ogg"
        Ant "Школа новая, а достаётся мне по-прежнему."
        play music "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 2
        show Olya Serious b_evening 00 good ahead 01 behind dendy_controller with Dissolve(.2)

        voice "voice/anton/3day/20 S.ogg"
        Ant "Словно и не переезжали никуда... Задолбало."

        scene d3_shadow_bunny:
            xalign .5
            yalign 1.
            linear 15 yalign .2

        with Dissolve(1.0)

        "И прежде чем безнадёга снова повела меня тоскливой тропинкой в плен гнетущих мыслей, что-то зловещее зашевелилось в недрах черепной коробки."
        "Будоража такие дикие и оттого приятные воспоминания."
        voice "voice/anton/3day/21 H.ogg"
        Ant "{i}Хотя, знаешь... Кое-что хорошее всё же случилось.{/i}"
        "Оля с надеждой посмотрела на мою криво расползающуюся улыбку, отдалённо напоминающую вспоротую рану от канцелярского ножа."
        voice "voice/anton/3day/22 E.ogg"
        Ant "{i}Ещё один мальчик пропал.{/i}"

        voice "voice/olya/3day/35 To.ogg"
        Oly "Тоша, разве это... хорошо? Почему ты так говоришь?"

        "Голос сестры вздрогнул, когда она заглянула мне в глаза сквозь толстые очки."

        show d3_shadow_bunny:
            linear 1 yalign .2

        voice "voice/anton/3day/23 Z.ogg"
        Ant "{i}Знаешь, а может, тот пропавший Вова сам виноват, что с ним это случилось.{/i}"
        voice "voice/anton/3day/24 M.ogg"
        Ant "{i}Может, он совершил нечто настолько плохое... что не заслуживал жить.{/i}"
        scene day_03_hight_ola_room_01_02 with Dissolve(.5)
        voice "voice/olya/3day/36 Ne.ogg"
        Oly "Не будь таким жестоким, пожалуйста!"
        "Оля прижала ноги к подбородку и обхватила их руками, пытаясь сжаться сильнее."
        "Будто она хотела стать ещё меньше, быть может, окончательно исчезнуть."
        "Это всё, что нам оставалось — пропасть без вести. Затеряться среди прочих сломанных игрушек."
        "И больше никогда не попадаться озлобленным родителям и взбешённым одноклассникам."

        scene day_03_hight_ola_room_05_06 with Dissolve(.5)
        "Мы единственные, кто остался друг у друга: те, кто может защитить, выслушать и пожалеть."
        "А значит, она обязана слушать, что я думаю о них всех — этих озверевших тварях, притворяющихся детьми, так жаждущих издеваться над слабыми."
        "Мой черёд говорить."
        voice "voice/anton/3day/25 D.ogg"
        Ant "{i}Думаю, они не последние.{i}"
        play test_two"voice/anton/3day/26 Disht.ogg"
        "Моё дыхание участилось. Пальцы забарабанили по дощатому полу."
        stop test_two fadeout 0.5
        voice "voice/anton/3day/27 Ta.ogg"
        Ant "{i}Такие люди, как они, недостойны жить, ходить с нами в одну школу...{i}"
        voice "voice/anton/3day/28 S.ogg"
        Ant "{i}… смотреть на твой свет.{i}"
        "Мысли путались, ускользали вслед за спокойствием."

        scene day_03_hight_ola_room_01_02 with Dissolve(.5)
        voice "voice/olya/3day/37 To.ogg"
        Oly "Тошенька, хватит! Ты меня пугаешь."
        voice "voice/anton/3day/29 Ne.ogg"
        Ant "{i}Не бойся, я смогу тебя защитить.{i}"

        scene day_03_hight_ola_room_07_08 with Dissolve(.5)
        "И тут я впервые заметил, как Оля смотрит на меня, словно на незнакомца."
        voice "voice/olya/3day/38 Kto.ogg"
        Oly "К-кто ты?"
        $ music_during_lines = 1.0
        play test_one "sounds/snare-noise-1.ogg"
        scene day_03_hight_ola_room_03_04 with Dissolve(0.5)
        stop music fadeout 2
        "Потаённая ярость отступила, спряталась за оболочкой труса, оставив меня один на один с нарастающим чувством стыда за то, что я напугал сестру."
        voice "voice/anton/3day/30 Ol.ogg"
        Ant "Оленька, прости, я... Я не хотел."
        play music "music/Cinematic Piano.ogg" volume 0.72

        voice "voice/anton/3day/31 Vi.ogg"
        Ant "Видимо, я схожу с ума в этой школе."

        scene day_03_hight_ola_room_obnim with Dissolve(0.5)
        "Она бросилась мне на шею, едва сдерживая слёзы."
        voice "voice/olya/3day/39 V.ogg"
        Oly "Всё хорошо, Тоша, только, пожалуйста-пожалуйста, никогда так больше не говори."
        voice "voice/anton/3day/32 K.ogg"
        Ant "Клянусь маминым сердцем."
        "Оля горько улыбнулась."


        voice "voice/olya/3day/40 A.ogg"
        Oly "А сам сказал, что так говорить нехорошо..."
        scene goosehunt_select_bg
        show goosehunt_select_menu
        show goosehunt_tv
        show goosehunt_jack
        show goosehunt_select_noise behind goosehunt_tv
        show chaika behind goosehunt_select_noise:
            xpos 345
            ypos 165 + 45 *10

        show dendy_controller zorder 5:
            xalign .5
            yalign 1.
            yoffset 100
        pause .25
        hide goosehunt_select_noise

        voice "voice/anton/3day/33 T.ogg"
        Ant "Ты права. Давай лучше играть."
        stop music fadeout 4
        hide dendy_controller
        show dendy_controller_3 zorder 5:
            xalign .5
            yalign 1.
            yoffset 100
            1.
            linear .5 yoffset 200 alpha 0

        hide Olya
        show goose_olya zorder 4:
            zoom 1.2
            yalign .5
            xoffset -300
        with Dissolve(.5)
        stop music2 fadeout 2
        voice "voice/olya/3day/41 To.ogg"
        Oly "Только, чур, я первая!"

    $ story_manager.MarkEvent(("day3", "game goosehunt"))
    python:
        goosegame_goosespeed = goose_speed_lvl1

        goosehunt_game = GooseHunt()
        goosehunt_game.round = 1
        goosehunt_game.reward = 500
        goosehunt_game.player = 1












    hide bg_black
    show day3_goosedendy_black behind goosehunt_tv
    play movie "video/goose 1.webm"

    $ renpy.pause(16, hard=True)
    stop movie
    $ goosehunt_game.points[0] = 3000

    label day3_goose_anton_turn:
    $ goose_cursor = "goosehunt_cursor 2"

    hide dendy_controller
    hide dendy_controller_1
    hide dendy_controller_2
    hide dendy_controller_3

    hide goose_olya
    show goose_olya_back zorder 4:
        xpos 1800
        xanchor .5
        zoom 1.2
        yalign .5
    with Dissolve(.5)

    show goose_anton_gun zorder 4:
        ypos 1.
        yanchor .4
        xalign .35
        alpha 0
        xzoom -1.0
        linear .5 yanchor .8 alpha 1
    pause .5

    python:
        goosehunt_game.Reset()
        goosehunt_game.player = 2
        goose_nextlabel = "day3_goose_round_1"

    jump goosehunt


label day3_goose_round_1:
    show goose_anton_gun zorder 4:
        linear .5 yanchor .4 alpha 0

    show day3_goosedendy_black
    play sound "audio/huntgoose/score.ogg"
    show screen goosehunt_msg_points()

    if goosehunt_game.points[1] > goosehunt_game.points[0]:
        hide goose_olya_back
        show Olya Serious b_evening 00 good ahead 09 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
        with Dissolve(.5)
        voice "voice/olya/3day/47 S.ogg"
        Oly "Считай, это я тебе поддалась."
    elif goosehunt_game.points[1] == goosehunt_game.points[0]:
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 02 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)
        voice "voice/olya/3day/50 M.ogg"
        Oly "Метко, ничего не скажешь."
    else:
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 07 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)
        voice "voice/olya/3day/44 Nu.ogg"
        Oly "Ну-ка, от винта!"

    hide day3_goosedendy_black
    hide screen goosehunt_msg_points

    python:
        goosegame_goosespeed = goose_speed_lvl2

        goosehunt_game.Reset()
        goosehunt_game.round = 2
        goosehunt_game.reward = 1000
        goosehunt_game.player = 1

    hide Olya
    show goose_olya zorder 4:
        zoom 1.2
        yalign .5
        xoffset -300
    with Dissolve(.5)









    show day3_goosedendy_black behind goosehunt_tv
    play movie "video/goose 2.webm"

    $ renpy.pause(7, hard=True)
    stop movie
    $ goosehunt_game.points[0] = 7000


    label day3_goose_round_1.anton_turn:
    $ goose_cursor = "goosehunt_cursor 2"

    hide goose_olya
    show goose_olya_back zorder 4:
        xpos 1800
        xanchor .5
        zoom 1.2
        yalign .5
    with Dissolve(.5)
    show goose_anton_gun zorder 4:
        ypos 1.
        yanchor .4
        xalign .35
        alpha 0
        xzoom -1.0
        linear .5 yanchor .8 alpha 1

    python:
        goosehunt_game.Reset()
        goosehunt_game.player = 2
        goose_nextlabel = "day3_goose_round_2"

    jump goosehunt


label day3_goose_round_2:
    show goose_anton_gun zorder 4:
        linear .5 yanchor .4 alpha 0

    show day3_goosedendy_black
    play sound "audio/huntgoose/score.ogg"
    show screen goosehunt_msg_points()

    if goosehunt_game.points[1] > goosehunt_game.points[0]:
        hide goose_olya_back
        show Olya Weeps b_evening 00 good ahead 05 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
        with Dissolve(.5)
        voice "voice/olya/3day/48 bu.ogg"
        Oly "Бу! Это ты виноват, что я промазала."
    elif goosehunt_game.points[1] == goosehunt_game.points[0]:
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 02 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)
        voice "voice/olya/3day/51 Hor.ogg"
        Oly "Хорош! Почти как я."
    else:
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 07 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)
        voice "voice/olya/3day/45 Kto.ogg"
        Oly "Ха! Кто на новенького?"

    hide day3_goosedendy_black
    hide screen goosehunt_msg_points

    python:
        goosegame_goosespeed = goose_speed_lvl3

        goosehunt_game.Reset()
        goosehunt_game.round = 3
        goosehunt_game.reward = 1500
        goosehunt_game.player = 1

    hide Olya
    show goose_olya zorder 4:
        zoom 1.2
        yalign .5
        xoffset -300
    with Dissolve(.5)









    show day3_goosedendy_black behind goosehunt_tv
    play movie "video/goose 3.webm"

    $ renpy.pause(7, hard=True)
    stop movie
    $ goosehunt_game.points[0] = 13000

    label day3_goose_round_2.anton_turn:
    $ goose_cursor = "goosehunt_cursor 2"

    hide goose_olya
    show goose_olya_back zorder 4:
        xpos 1800
        xanchor .5
        zoom 1.2
        yalign .5
    with Dissolve(.5)
    show goose_anton_gun zorder 4:
        ypos 1.
        yanchor .4
        xalign .35
        alpha 0
        xzoom -1.0
        linear .5 yanchor .8 alpha 1

    python:
        goosehunt_game.Reset()
        goosehunt_game.player = 2
        goose_nextlabel = "day3_goose_round_3"

    jump goosehunt


label day3_goose_round_3:
    show goose_anton_gun zorder 4:
        linear .5 yanchor .4 alpha 0

    show day3_goosedendy_black
    play sound "audio/huntgoose/game over.ogg"
    show screen goosehunt_msg_points()

    if goosehunt_game.points[1] > goosehunt_game.points[0]:
        $ story_manager.MarkEvent(("day3", "game goosehunt", "dominate"))
        hide goose_olya_back
        show Olya Weeps b_evening 00 good ahead 06 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
        with Dissolve(.5)

        if goosehunt_game.points[1] == 39000:
            $ achievement_grant("ach_duckinator")
        else:
            $ achievement_grant("ach_meanie")

        voice "voice/olya/3day/43Ne.ogg"
        Oly "Несчитово! Ты ближе к экрану стоял. Я с тобой так больше не играю!"

    elif goosehunt_game.points[1] == goosehunt_game.points[0]:
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 02 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)
        voice "voice/olya/3day/52 Au.ogg"
        Oly "А у нас, Тоша, ничья."
    else:

        $ story_manager.MarkEvent(("day3", "game goosehunt", "comfort"))
        hide goose_olya_back
        show Olya Happy b_evening 00 good ahead 07 zorder 4:
            xanchor .5
            xpos 1650
            zoom 1.2
            yalign .5
            yoffset 30
        with Dissolve(.5)

        $ achievement_grant("ach_bro")

        voice "voice/olya/3day/42 Pif.ogg"
        Oly "Пиф-паф! Ой-ой-ой! Умирает зайчик мой. Ха-ха! Ты проиграл, Тоша."

    jump day3_polinacall

label dendy_jack_turnoff:

    $ default_mouse = "default"
    $ is_save_allowed = True
    $ _game_menu_screen = "quick_menu"

    stop goose_1
    stop goose_2

    hide screen goosehunt_hunting
    hide screen vt_frame
    hide screen goosehunt_ui
    hide screen day3_dendy_turnoff
    hide screen goosehunt_msg_round
    hide screen goosehunt_msg_getready

    scene bg_rep_04

    show dendy_tv

    show goose_anton_gun:
        ypos 1.
        yanchor .8
        xalign .35
        xzoom -1.0
        linear .5 yanchor .4 alpha 0

    show goose_olya_back:
        xpos 1800
        xanchor .5
        zoom 1.2
        yalign .5

    with Dissolve(.5)

    pause 1.

    hide goose_olya_back
    show Olya Serious b_evening 00 good ahead 01:

        xanchor .5
        xpos 1700
        zoom 1.2
        xzoom -1
        yalign .5

    with Dissolve(.3)

    pause .5

    voice "voice/anton/3day/47 Po.ogg"
    Ant "Поиграли и будет."
    play test_three "voice/olya/3day/12 Vshlip.ogg"
    play sound "sounds/steps/Anton-steps-out-1.ogg"

    $ achievement_grant("ach_meanie")
    show Olya Weeps b_evening 00 good ahead 05 with Dissolve(.5)


    jump day3_polinacall

label day3_polinacall:
    $ story_manager.MarkEvent(("day3", "scene17"))
    jump dev_d3_polinacall.end
    label dev_d3_polinacall:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Выбери рут"
            "Полина":
                $ ROUTE_POLINA = True
                $ Flags.Raise("day2 polina")
            "Лиса":
                $ ROUTE_FOX = True
                $ Flags.Raise("day2 fox")
            "Маска":
                $ ROUTE_SOLO = True
                $ Flags.Raise("mask")
        label dev_d3_polinacall.end:

    pause 1.5

    show screen black_scr with Dissolve(1.5)
    hide screen goosehunt_msg_points

    scene bg_black

    hide screen black_scr





    pause .5


    play test_one "voice/karina/3day/121 Ant.ogg"
    "Мама докричалась до меня только с третьего раза."
    stop test_one fadeout 0.3

    voice "voice/karina/3day/122 Teb.ogg"
    Mam "Антон! Тебя к телефону!"

    voice "voice/karina/3day/123 Dev.ogg"
    Mam "Девочка какая-то."
    play test_two "sounds/Anton-school-run-1.ogg"

    window auto
    scene phone_hall2

    "Моментально протрезвев, я метнулся в коридор."


    scene phone_hall2_02 with Dissolve(.5)


    voice "voice/karina/3day/124 Ne.ogg"
    Mam "Не споткнись смотри!"
    play test_one "sounds/sfx_phone_take.ogg"


    window show

    scene polina_call_pickedup with Dissolve(.5)

    "Я схватил трубку, прижал к груди, многозначительно глядя на маму."
    "Она лишь пожала плечами и удалилась в комнату, на ходу собирая разбросанные Олей игрушки."


    scene polina_call_anton_bg 0
    show polina_call_anton antonc5
    with Dissolve(.5)
    voice "voice/anton/3day/090 A.ogg"
    Ant "Алло!"

    show polina_call_anton antonc1 with Dissolve(.5)
    play music "music/29_Polina.ogg" volume 0.7 fadein 0.5
    voice "voice/Polina/3day/35 Utv.ogg"
    Pol "У твоей мамы такой молодой голос."

    show polina_call_anton antonc4 with Dissolve(.5)
    voice "voice/anton/3day/091 Anu.ogg"
    Ant "А... Ну да. Она сама молодая."

    show polina_call_anton antonc2 with Dissolve(.5)
    voice "voice/Polina/3day/36 Ne.ogg"
    Pol "Не мешаю?"

    show polina_call_anton antonc8 with Dissolve(.5)
    voice "voice/anton/3day/092 Net.ogg"
    Ant "Нет, что ты."

    "Знала бы она, как дорого мне может обойтись этот разговор, и чем я рискую, просто отвечая на звонок."

    scene polina_call_art 01 with Dissolve(1.0)
    "На тумбочке лежали карандаш и потрёпанный блокнот."
    play test_one "sounds/pen_bumaga.ogg"

    scene polina_call_art 02 with Dissolve(.5)
    scene polina_call_art 003 with Dissolve(1)
    if ROUTE_SOLO:
        show polina_call_art_03:
            alpha 0
            pause 1.5
            linear .5 alpha 1
    "Я взял их и принялся водить грифелем по бумаге, рисуя хаотичные завитки, так и норовящие соединиться в дурацкие сердечки."
    play test_six "sounds/Karandash_01.ogg"

    if ROUTE_SOLO:
        jump day3_polinacall_solo

    jump day3_polinacall_notsolo

label day3_polinacall_solo:
    $ story_manager.MarkEvent(("day3", "scene18a"))
    scene polina_call_art 02 with Dissolve(.5)
    voice "voice/Polina/3day/90 Ya.ogg"
    Pol "Я тут подумала... Мне надо тебе сказать кое-что."

    "Я застыл."

    scene polina_call_art 04 with Dissolve(.5)
    "Не может быть! Неужели я ей нравлюсь?"
    scene polina_call_art 05 with Dissolve(.5)
    voice "voice/Polina/3day/92 V.ogg"
    Pol "В последнее время у тебя такой потерянный вид."
    voice "voice/Polina/3day/93 A.ogg"
    Pol "А сегодня в школе на тебе буквально лица не было."
    show polina_call_art_06:
        alpha 0
        pause 1.5
        linear .5 alpha 1
    "Я не находил слов. Сердце трепетало в ожидании."

    voice "voice/Polina/3day/94 Ya.ogg"
    Pol "Я хочу сказать..."

    voice "voice/Polina/3day/95 Y.ogg"
    Pol "Я на твоей стороне."
    stop music fadeout 2

    scene polina_call_art 07 with Dissolve(.5)
    "В предвкушении Полининых слов улыбка растеклась по моим губам."
    play sound "music/Tension Suspense Risers_02.ogg"


    voice "voice/Polina/3day/96 E.ogg"
    Pol "И мне тебя очень жаль."



    voice "voice/Polina/3day/97 Ta.ogg"
    Pol "Такие хорошие ребята, как ты, заслуживают большего."


    voice "voice/Polina/3day/98 M.ogg"
    Pol "Мне очень хочется верить, что однажды ты найдёшь в себе силы дать отпор, и другие перестанут тебя задирать."
    play music2 "music/Broken Thoughts.ogg" volume 0.8

    "Карандаш выпал из разжавшихся пальцев."
    "Это всё, что она мне скажет?"

    voice "voice/Polina/3day/99 Mo.ogg"
    Pol "Может, даже девушку найдёшь..."

    "Она будто сомневалась в собственных словах."
    voice "voice/Polina/3day/100 K.ogg"
    Pol "Короче, знай: ты славный парень!"
    "Это был провал."
    "Вместо предложения погулять – сочувствие, будто к какому-то калеке."
    voice "voice/Polina/3day/101 T.ogg"
    Pol "Ты тут?"

    jump day3_polinacall_phase2_notfox

label day3_polinacall_notsolo:
    $ story_manager.MarkEvent(("day3", "scene18b"))
    scene polina_call_art 003 with Dissolve(.5)
    voice "voice/Polina/3day/37 Ya.ogg"
    Pol "Я прочла твои ответы."
    voice "voice/Polina/3day/38 A.ogg"
    Pol "А тебе действительно «Кар-Мэн» нравится?"
    play test_six "sounds/Karandash_02.ogg"
    scene polina_call_art 03 with Dissolve(.5)
    voice "voice/anton/3day/051 Mne.ogg"
    Ant "Мне, если по правде, русский рок больше нравится."
    voice "voice/anton/3day/052 No.ogg"
    Ant "Но я почему-то постеснялся это написать."
    play test_three "sounds/sfx_turning_pages_1.ogg"


    scene polina_call_art 02 with Dissolve(.5)
    voice "voice/Polina/3day/39 A.ogg"
    Pol "А хочешь, Антоша, и я честной буду?"
    voice "voice/anton/3day/094 K.ogg"
    Ant "Конечно."

    scene polina_call_art 04 with Dissolve(.5)
    play test_six "sounds/Karandash_01.ogg"
    "Карандаш вывел женский профиль, глаз, длинные ресницы."

    scene polina_call_art 05 with Dissolve(.5)
    play test_six "sounds/Karandash_02.ogg"
    "Полина сказала полушёпотом, наверное, чтобы дедушка не услышал:"
    voice "voice/Polina/3day/40 Mn.ogg"
    Pol "Мне здесь ужасно тоскливо."
    play test_six "sounds/Karandash_01.ogg"

    scene polina_call_art 06 with Dissolve(.5)
    voice "voice/anton/3day/095 Doma.ogg"
    Ant "Дома?"
    voice "voice/Polina/3day/41 V.ogg"
    Pol "В посёлке."
    play test_six "sounds/Karandash_02.ogg"
    stop music fadeout 6
    scene polina_call_art 07 with Dissolve(.5)
    voice "voice/Polina/3day/42 Z.ogg"
    Pol "Здесь никогда ничего не происходит, а если происходит, то всякая гадость."
    play music2 "music/3_trouble.ogg" volume 0.9 fadein 5
    voice "voice/Polina/3day/43 E.ogg"
    Pol "И дело даже не в пропавших детях."
    voice "voice/Polina/3day/44 Zd.ogg"
    Pol "Здесь музыки мало."

    $ music_during_lines = 0.6
    voice "voice/anton/3day/096 No.ogg"
    Ant "Но у тебя же кассеты есть."
    voice "voice/Polina/3day/45 Ya.ogg"
    Pol "Я не про записи."
    voice "voice/Polina/3day/46 Ya.ogg"
    Pol "Я про... ну, голос этого места."
    play test_three "sounds/sfx_turning_pages_2.ogg"

    scene polina_call_art 02 with Dissolve(.5)
    voice "voice/Polina/3day/47 On.ogg"
    Pol "Он не мелодичный. Всё шуршит, как патефонная игла, скрипит, воет изредка."
    voice "voice/Polina/3day/48 T.ogg"
    Pol "Тут неуютно, тесно очень."
    voice "voice/Polina/3day/49 N.ogg"
    Pol "Не знаю, как объяснить тебе."
    play test_six "sounds/Karandash_02.ogg"

    scene polina_call_art 008 with Dissolve(.5)
    "Грифель набросал дом, окружённый высокими деревьями."
    voice "voice/anton/3day/097 Ka.ogg"
    Ant "Кажется, я тебя понимаю."
    voice "voice/anton/3day/097 M.ogg"
    Ant "Моя сестрёнка говорит, что чувствует себя заточённой в темницу."
    play test_six "sounds/Karandash_01.ogg"
    scene polina_call_art 08 with Dissolve(.5)
    voice "voice/Polina/3day/50 V.ogg"
    Pol "Вот и я... Я очень люблю дедушку. И бросить его боюсь."
    voice "voice/Polina/3day/51 A.ogg"
    Pol "А порой так хочется убежать. Далеко-далеко."
    stop music fadeout 6
    "«{i}В лес,{/i} — подумал я отчуждённо, малюя хвойные лапы; — {i}Убежать в лес, чтобы снежинки падали на шерсть, и ветви закрыли от посторонних глаз{/i}»."
    voice "voice/anton/3day/098 Ya.ogg"
    Ant "Я, когда рисую, будто путешествую."
    play test_three "sounds/sfx_turning_pages_4.ogg"

    scene polina_call_art 02 with Dissolve(.5)
    voice "voice/Polina/3day/52 Um.ogg"
    Pol "У меня так же со скрипкой."
    play test_six "sounds/Karandash_02.ogg"

    scene polina_call_art 009 with Dissolve(.5)
    scene polina_call_art 09 with Dissolve(.5)
    voice "voice/Polina/3day/53 U.ogg"
    Pol "Убегаю по смычку в небо."
    $ music_during_lines = 1.0
    play test_six "sounds/Karandash_01.ogg"

    scene polina_call_art 10 with ImageDissolve("effect/imagedissolve/cross-t.jpg", .5)
    "Я осознал, что рисую нож-бабочку. Зачеркнул."
    "Воспоминания о Ромке испортили настроение."


    if ROUTE_FOX:
        "Сказать ей? Предупредить, что он замыслил?"
        "Сорвать его планы охмурить Полину?"
        "А как же команда Вольтрона? Всё-таки они были какими-никакими, но моими приятелями."
        "И кем бы я стал, предав их?"
        stop music2 fadeout 4

        label day3_polinacall_notsolo.choice:
        $ story_manager.MarkEvent(("day3", "phonecall"))
        window hide
        scene polina_call_art 11 with Dissolve(.5)
        call screen day3_choice_polina_call()

    jump day3_polinacall_phase2_notfox


label bunny3_betray_true:
    $ story_manager.MarkEvent(("day3", "phonecall", "betray"))
    $ Flags.Raise("betray")



    play music2 "music/46_Romantic piano melody.ogg" volume 0.65
    window show
    voice "voice/anton/3day/102 Pol.ogg"
    Ant "Полина?"
    voice "voice/Polina/3day/54 Da.ogg"
    Pol "Да?"
    voice "voice/anton/3day/103YaHo.ogg"
    Ant "Я хочу тебе кое в чём признаться..."
    voice "voice/anton/3day/103Rom.ogg"
    Ant "Ромка... попросил меня об одной услуге."
    "Слова вязли во рту, ускользали."
    "От напряжения я стал накручивать завитой провод на палец."
    voice "voice/Polina/3day/56 A.ogg"
    Pol "Алло, Антош, я тебя плохо слышу."
    play test_two "voice/anton/3day/104 Vzd.ogg"
    "Я громко выдохнул."

    scene polina_call_anton_bg 0
    show polina_call_anton antonc5
    with Dissolve(.5)

    voice "voice/anton/3day/105 Romk.ogg"
    Ant "Ромка сделал из меня маньяка."
    "В трубке повисло гудящее молчание."
    voice "voice/Polina/3day/57 Ha.ogg"
    Pol "Ха! Что?"

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/106 On.ogg"
    Ant "Он попросил меня напасть на тебя..."

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/106 Kak.ogg"
    Ant "Как будто я какой-то монстр."

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/107 Aon.ogg"
    Ant "А он бы тут же объявился и героически тебя спас."

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/107 ALe.ogg"
    Ant "Алё, Полин?"

    show polina_call_anton anton33 with Dissolve(.5)

    play test_two "voice/anton/3day/108Duu.ogg"
    "Она молчала, так что я подул в трубку."
    voice "voice/Polina/3day/58 E.ogg"
    Pol "И? Ты согласился?"
    "Её голос стал серьёзным, более жёстким."

    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/109 Net.ogg"
    Ant "Нет! Как ты могла подумать?"

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton44 with Dissolve(.2)
    voice "voice/anton/3day/109 Ya.ogg"
    Ant "Я ведь сказал тебе правду."

    show polina_call_anton anton33 with Dissolve(.2)
    show polina_call_anton anton5 with Dissolve(.2)
    voice "voice/anton/3day/110 AR.ogg"
    Ant "А Ромка с Бяшей... После такого они мне больше не товарищи!"

    scene polina_call_art 07 with Dissolve(1.)
    voice "voice/Polina/3day/59 Ah.ogg"
    Pol "Ах, Антон! Спасибо!"
    voice "voice/Polina/3day/60 Ya.ogg"
    Pol "Я так рада, что ты со мной."
    "Сердце заколотилось быстрее. Волнение потерять Полину передало эстафету трепету встречи."
    $ achievement_grant("ach_muse")
    voice "voice/Polina/3day/61 P.ogg"
    Pol "Понимаю, как тебе было нелегко рассказать такое."
    voice "voice/Polina/3day/62 S.ogg"
    Pol "Слушай, дедушка всегда говорил, что музыка лечит душу."
    voice "voice/Polina/3day/63 H.ogg"
    Pol "Хочешь, я тебе сыграю?"
    voice "voice/anton/3day/111 Gd.ogg"
    Ant "Где? В школе?"
    voice "voice/Polina/3day/84 N.ogg"
    Pol "Нет же. После школы."
    voice "voice/Polina/3day/85 P.ogg"
    Pol "Придёшь завтра ко мне в гости?"
    play test_one "sounds/sfx_drop_pencil2.ogg"

    "Не веря в услышанное, я обронил карандаш."
    play test_one "sounds/sfx_head_hit.ogg"


    scene polina_call_art 07 with hpunch
    scene bg_black with Dissolve(.5)

    scene polina_call_anton_bg 0
    show polina_call_anton antonc8
    with Dissolve(.2)
    play test_two "voice/anton/3day/112 A.ogg"
    "А когда бросился вытаскивать его из-под тумбочки, что есть силы треснулся о неё лбом."


    show polina_call_anton anton22 with Dissolve(.2)
    voice "voice/anton/3day/113. Ko.ogg"
    Ant "К-конечно... П-почему бы и нет?"

    show polina_call_anton antonc8 with Dissolve(.2)
    voice "voice/Polina/3day/86 T.ogg"
    Pol "Тогда завтра после уроков, хорошо?"
    "На макушке медленно надувалась шишка, но я её почти не чувствовал."

    jump day3_polinacall_phase2_fox


label bunny3_betray_false:
    $ story_manager.MarkEvent(("day3", "phonecall", "voltron"))


    play music2 "music/42_Talk.ogg" volume 0.65
    $ renpy.music.set_volume(1.4, 2.0, channel="music2")
    "Да, порой Ромка вёл себя ужасно, бывал несправедлив к другим и помыкал слабыми."
    "Но что-то мне подсказывало, что дружба для Ромки — не пустое слово."
    $ achievement_grant("ach_voltron")
    "Разве не о друзьях я мечтал всё это время на новом месте?"
    "Пускай здесь они и были так же чудовищны, как вид на древний лес из моего окна."
    "Я сдвинул очки на лоб, потирая глаза."

    scene polina_call_anton_bg 0
    show polina_call_anton antonc5
    with Dissolve(.5)

    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    voice "voice/anton/3day/114 p .ogg"
    Ant "Эх, поскорей бы уже повзрослеть."

    show polina_call_anton anton33 with Dissolve(.2)

    voice "voice/Polina/3day/87 D.ogg"
    Pol "Думаешь, будет проще?"
    jump day3_polinacall_phase2_fox

label day3_polinacall_phase2_fox:
    $ story_manager.MarkEvent(("day3", "scene19"))
    play test_one "sounds/ringe.ogg"
    "Не давая ответить, раздался дверной звонок."
    scene door_peephole_hall with Dissolve(.2)

    "Мой блуждающий взгляд ткнулся в дверь."
    "Это Ромка с Бяшей пришли репетировать, а я должен помочь им увести девочку, которая мне нравится."

    if Flags.Has("betray"):
        "Придётся сделать вид, что я с ними. Ради Полины."
    scene polina_call_anton_bg 0
    show polina_call_anton antonc5
    with Dissolve(.2)
    voice "voice/anton/3day/115 Pol.ogg"
    Ant "Полин, подожди минутку."
    queue sound [ "<silence 1.0>", "<from 0 to 2>sounds/steps/Anton-steps-steal-0.ogg"]

    scene door_peephole_hall:
        align (.5,.5)
        linear 1. zoom 1.3
    with Dissolve(.5)

    scene door_peephole_static
    with Dissolve(.5)
    "Сделав пару шагов, я прижался к дверному полотну."


    call screen day3_door_peephole()

    scene door_peephole_animation
    "Горевшая снаружи лампочка озаряла крыльцо, и в замёрзшем глазке различались два невысоких тёмных силуэта."
    "Явились, не запылились."
    voice "voice/anton/3day/116 Pod.ogg"
    Ant "Подождите, я сейчас."
    scene phone_hall2_02 with Dissolve(.5)
    pause .5
    scene polina_call_pickedup with Dissolve(.5)
    play test_one "sounds/sfx_phone_take.ogg"
    "Вернувшись к телефону, я поднял трубку."

    scene polina_call_anton_bg 0
    show polina_call_anton antonc8
    with Dissolve(.5)
    voice "voice/anton/3day/117P.ogg"
    Ant "Мне надо бежать."
    show polina_call_anton antonc2 with Dissolve(.5)
    voice "voice/Polina/3day/88 Mn.ogg"
    Pol "Мне тоже."
    voice "voice/Polina/3day/89 S.ogg"
    Pol "Спасибо, что выслушал."
    play test_three "sounds/loop_short_beeps.ogg"
    "Гудки завибрировали в ухо."
    stop test_three fadeout 0.5
    scene polina_call_pickedup with Dissolve(.5)
    pause .5
    play test_one "sounds/sfx_phone_put.ogg"
    scene phone_hall2_down with Dissolve(.5)

    "Я опустил трубку на рычаг и покосился на лестницу."
    "Мама, увлечённая сериалами, не заметила трель."
    stop music2 fadeout 3

    scene phone_hall_hall:
        xpos -450
    show phone_hall_anton:
        yalign 1.
        yoffset 20
        xpos 400
    show phone_hall_anton_eyes:
        yalign 1.
        yoffset 20
        xpos 400
    show phone_hall_stair:
        xpos 900
    with Dissolve(.5)
    pause .5
    play test_one "sounds/sfx_put_on_clothes.ogg"
    hide phone_hall_anton_eyes with Dissolve(.5)
    "Никого не предупредив, я натянул обувь и шапку, а затем выскользнул в темноту зимнего вечера."
    play music "music/2_Anxiety.ogg" fadein 2

    scene phone_hall_hall:
        xpos -450
        linear 2. xpos 0
    show phone_hall_anton:
        yalign 1.
        yoffset 20
        xpos 400
        parallel:
            linear 2. xpos 300
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 4
    show phone_hall_stair:
        xpos 900
        linear 2. xpos 900 + 900

    show bg_black:
        alpha 0
        .5
        linear .5 alpha 1
    stop test_one fadeout 1
    play test_two "sounds/Door_open.ogg"
    pause 1.
    play test_one "sounds/Door_close.ogg"
    scene home_out_side_hight with Dissolve(.5)

    pause .5

    play fon "sounds/Real_wind.ogg" fadein 1.0 loop
    "Ветер защипал щёки. Я поморгал, привыкая к сумеркам."
    "От леса тянуло холодом и смолистым запахом хвои, а где-то в поле трещал мороз."
    "Впереди у калитки маячили две тени. Лишь рост позволял распознать в них моих одноклассников."
    play test_one "sounds/steps_snow001.ogg"
    scene d3_outside_guys_bg
    show d3_outside_guys_r
    show d3_outside_guys_bysh
    with Dissolve(.5)

    "Я направился к забору, слушая вой ветра в ушах и монотонный скрип под подошвами."
    window hide
    hide d3_outside_guys_r
    show d3_outside_guys_r behind d3_outside_guys_bysh:
        block:
            linear .05 xpos -3
            linear .05 xpos 3
            repeat 2
        linear 2. xpos 400 alpha .0
    pause 2.0
    window show

    "Одна из фигур шевельнулась и плавно устремилась к чащобе, будто конькобежец по льду."
    "Я замедлил шаг и коснулся очков, тщетно стараясь вычленить из мрака хоть какие-то детали."
    "Тревога опустилась на плечи, как невесомая снежинка."
    "В животе закопошилась проснувшаяся змея. Стало тошно."
    "Я подумал о доме, о хлипкой крепости позади."
    "Мама и Оля сидят в тепле перед телевизором на втором этаже и непринуждённо следят за похождениями героев «Санта-Барбары»."
    "Мне совсем не хотелось участвовать в Ромкиных постановках."
    "И ещё сильнее не хотелось идти туда, где на зимнем ветру колыхалась раздвоенная тень."
    $ renpy.start_predict("d3_outside_owl_anim")
    voice "voice/byasha/3day/154 nu.ogg"
    Bya "Ну что застрял, на?"
    voice "voice/byasha/3day/154 M.ogg"
    Bya "Мы тут замёрзли совсем!"
    "Голос Бяши буквально дрожал, а нетерпеливый Ромка пускал клубы пара у тёмных сосен. Такой влюблённый и задумчивый."
    voice "voice/byasha/3day/155 do.ogg"
    Bya "До костей продрогли, на."
    voice "voice/byasha/3day/156 Sh.ogg"
    Bya "Шевелись..."
    voice "voice/anton/3day/118 E.ogg"
    Ant "Да иду, иду..."
    play test_two "sounds/steps/sfx_girl_leaves_on_snow2.ogg"
    stop music fadeout 15

    scene d3_outside_guys_bg:
        align (.5,.5)
        subpixel True
        linear 3. zoom 1.1
    show d3_outside_guys_bysh:
        align (.5,.5)
        subpixel True
        linear 3. zoom 1.2

    play test_one "voice/anton/3day/119 Pin.ogg"
    "Я глубоко вдохнул и пошёл, пиная сугробы."


    scene d3_outside_bysh_0 with Dissolve(.5)
    "Бяша замер лицом к тайге."
    "До него было рукой подать, и я зачем-то положил озябшую кисть ему на плечо — наверное, убедиться, что это всё не сон."
    play wtf "sounds/sfx_owl_screamer.ogg"
    window hide
    scene d3_outside_owl_anim
    pause 1.
    $ renpy.stop_predict("d3_outside_owl_anim")
    "В мою сторону торчал острый клюв, со всех сторон усеянный мохнатыми перьями, из которых складывалась морда совы."
    play music "music/Master of the forest.ogg" fadein 2

    "Нечто в птичьей маске таращилось на меня."
    voice "voice/Owl/3day/01Do.ogg"
    Owl "У-ху, до самых косточек."
    "Голос был точь-в-точь Бяшин, но за перьями и картоном таился некто иной."

    scene home_out_side_hight with Dissolve(.5):
        align (.5, .5)
        zoom 1.01
        parallel:
            linear 2. zoom 1.15

        parallel:
            yoffset 0
            linear 0.07 yoffset -3
            linear 0.07 yoffset 3
            yoffset 0
            linear 0.05 yoffset -2
            linear 0.05 yoffset 2
            yoffset 0
            linear 0.05
            repeat
    play test_one "voice/anton/1day/029.Beg i o.ogg"
    play test_two "sounds/loop_snow_footsteps.ogg"
    "Я рванул прочь, словно меня стегнули нагайкой."
    "Существо в маске лишь притворялось Бяшей..."
    Ant_m "«{i}Чтобы выманить меня!{/i}»"

    jump day3_night


label day3_polinacall_phase2_notfox:
    $ story_manager.MarkEvent(("day3", "scene20"))
    stop music2 fadeout 2
    "Не давая ответить, Оля спустилась по ступенькам."
    play music2 "music/17_Flow.ogg" volume 0.75 fadein 1
    play test_two "sounds/steps/Olya-steps-1.ogg"
    scene polina_call_anton_bg 3:
        xpos -696
    show Olya Serious m_evening 04 good ahead 01:
        xpos 550
        ypos -162
        xzoom -1.15
        yzoom 1.15
    show polina_call_anton_fg:
        xpos -696
    with Dissolve(.5)
    "В её руке была зажата книжка с розовой обложкой: «Энциклопедия маленьких принцесс»."
    show Olya Serious m_evening 04 good ahead 03 with Dissolve(.2):
        xpos 550
        ypos -162
        xzoom -1.15
        yzoom 1.15
    voice "voice/olya/3day/01 T.ogg"
    Oly "Ты долго ещё?"
    show Olya Serious m_evening 04 good ahead 01 with Dissolve(.2)
    "Я прикрыл ладонью трубку."
    voice "voice/anton/3day/120Ya.ogg"
    Ant "Я разговариваю."
    voice "voice/anton/3day/121Ch.ogg"
    Ant "Что случилось?"
    show Olya Serious m_evening 04 good ahead 03 with Dissolve(.2)
    voice "voice/olya/3day/02 Po.ogg"
    Oly "Почитай мне, пожалуйста."
    show Olya Serious m_evening 04 good ahead 01 with Dissolve(.2)
    show Olya Serious m_evening 04 good ahead 03 with Dissolve(.2)
    voice "voice/olya/3day/03 M.ogg"
    Oly "Мама уснула."
    show Olya Serious m_evening 04 good ahead 01 with Dissolve(.2)
    voice "voice/anton/3day/122 Ed.ogg"
    Ant "Иди к себе. Я сейчас."
    show Olya Serious m_evening 04 good ahead 03 with Dissolve(.2)
    voice "voice/olya/3day/04 To.ogg"
    Oly "Только быстрее, ладно?"
    show Olya Serious m_evening 04 good ahead 01 with Dissolve(.2)
    voice "voice/anton/3day/123La.ogg"
    Ant "Ладно!"
    play test_one "sounds/steps/Olya-ladder-steps-1.ogg"
    play test_two "voice/anton/3day/124Vz.ogg"
    hide Olya with Dissolve(.5)
    "Последнее слово прозвучало излишне раздражённо. Я вздохнул, наблюдая, как сестра семенит по лестнице."

    if ROUTE_POLINA:
        scene polina_call_art 10 with Dissolve(.5)
        voice "voice/anton/3day/125Pr.ogg"
        Ant "Прости, надо бежать."
        voice "voice/Polina/3day/88 Mn.ogg"
        Pol "Мне тоже."
        voice "voice/Polina/3day/89 S.ogg"
        Pol "Спасибо, что выслушал."
        play test_three "sounds/loop_short_beeps.ogg"
        "Гудки завибрировали в ухо.Я опустил трубку на рычаг."
        stop test_three fadeout 0.5
        scene polina_call_pickedup with Dissolve(.5):
            pause 1
            "phone_hall2_down" with Dissolve(.5)
        play test_one ["<silence .5>", "sounds/sfx_phone_put.ogg"]
        "Размышляя о девочке, за которую мне грозит смерть от ножа, я поплёлся на второй этаж."
    if ROUTE_SOLO:
        stop music2 fadeout 2
        scene polina_call_art 07 with Dissolve(.5)
        voice "voice/anton/3day/099 AlePo.ogg"
        Ant "Алё! Полина?"
        voice "voice/Polina/3day/102 Pr.ogg"
        Pol "Прости, мне надо бежать."
        play music2 "music/9_Nikita Kryukov - the Obscurity.ogg" volume 0.85
        voice "voice/Polina/3day/103 Pre.ogg"
        Pol "Представляешь, кое-кто втюрился в меня и теперь отирается у моих окон, требуя сходить с ним на свидание."
        voice "voice/Polina/3day/104 Po.ogg"
        Pol "Пойду прогоню его, пока дедушка не проснулся."
        voice "voice/Polina/3day/105 H.ogg"
        Pol "Хм, или, может, дать ему шанс?"
        "Я прикусил нижнюю губу от обиды."
        voice "voice/Polina/3day/106 Es.ogg"
        Pol "Если интересно — расскажу тебе завтра."
        play sound "sounds/sfx_pencil_hard_swooshes.ogg"
        voice "voice/Polina/3day/107 M.ogg"
        Pol "Мы, в конце концов, друзья."

        show polina_call_art 00 with Dissolve(.5)
        "Друзья. Хорошо хоть не подружки."
        voice "voice/anton/3day/100 Da.ogg"
        Ant "М-да, конечно."
        voice "voice/anton/3day/101Do.ogg"
        Ant "Доброй..."
        play test_three "sounds/loop_short_beeps.ogg"
        "Гудки ударили по мозгам."
        stop test_three fadeout 0.5


        scene polina_call_pickedup with Dissolve(.5):
            pause 1
            "phone_hall2_down" with Dissolve(.5)
        play test_one ["<silence .5>", "sounds/sfx_phone_put.ogg"]
        play test_two "sounds/hit-low-3.ogg"
        "«{i}Потаскуха{/i}», — процедил злой голос в голове."
        "Словно зомби, лишённый покоя и рассудка, я поплёлся по лестнице."

    scene bg_black with Dissolve(.5)
    play test_one "sounds/steps/Anton-steps-steal-1.ogg" loop
    "Рассказать бы отцу. Попросить его мужского совета."
    "Но из-за новой работы его до поздней ночи не бывает дома."
    "Родителям не до меня, если не сказать грубее."
    stop test_one fadeout 1.5

    scene bg_Olga_room_n_2_bg with Dissolve(.5)
    voice "voice/anton/3day/126Nu.ogg"
    Ant "Ну, где твоя книжка?"
    stop music2 fadeout 1.5
    stop music fadeout 1.5

    "Я осёкся. Детская была пуста."
    voice "voice/anton/3day/127Ol.ogg"
    Ant "Оль?"

    scene bg_black with Dissolve(.5)
    "Наверное, пробралась ко мне."
    play test_two "sounds/steps/Anton-steps-out-1.ogg"
    "Я зашагал по коридору."

    scene bg_room_night1 with Dissolve(.5)
    "Тени населяли комнату. Занавеска колыхалась, будто кто-то хоронился за ней."

    scene day3_ant_room_shtora with Dissolve(.5)
    play test_two "sounds/steps/Anton-steps-steal-0.ogg"
    play test_one "music/caricature06.ogg"
    "Я улыбнулся. Тихо прокрался к окну и распахнул штору."
    play test_one "sounds/curtain.ogg"

    window hide
    scene day3_ant_room_shtora:
        align (.5, .5)
        parallel:
            linear .25 yalign .25
            linear .25 yalign .5

        parallel:
            linear .5 zoom 1.1

    pause .5

    scene day3_window_bg_blur_0:
        xalign .5
        linear .5 xalign 0.
    show day3_window_bg_blur_1:
        xalign .5
        linear .5 xalign 0.
    show day3_window_frame:
        xalign 1.
        linear .5 xalign 0.
    show day3_window_anton:
        xpos 1920
        xanchor .5
        ypos 1080
        yanchor .95

        alpha 0
        parallel:
            linear .25 alpha 1
        parallel:
            linear .5 xpos 1650 yanchor 1.
    play test_one "music/caricature08.ogg"

    pause 1.5
    window show
    voice "voice/anton/3day/128 Po.ogg"
    Ant "Попалась!"
    "За тканью никого не было."
    "Окно, как экран телевизора, показывало зимний пейзаж."
    "Фонарь, поле, и в самом его центре – бредущие фигурки."


    scene day3_window_bg_0:
        xalign 0.
    show day3_window_bg_1:
        xalign 0.
    show day3_window_frame_blur:
        xalign 0.
    show day3_window_anton_blur:
        xpos 1650
        xanchor .5
        ypos 1080
        yanchor 1.
    with Dissolve(.5)


    play test_two "sounds/Phrases_03.ogg"
    "Алиса и Оля..."
    play test_one "voice/anton/3day/129 Ah.ogg"
    "Я ахнул, прижав кулак ко рту, впился зубами в кожу."
    play music2 "music/Evil Alice.ogg"

    scene day3_window_bg_0:
        xalign 0.
        yalign .75
        linear .5 zoom 1.1
    show day3_window_bg_1:
        xalign 0.
        yalign .75
        linear .5 zoom 1.1
    show day3_window_frame_blur:
        xalign 0.
        yalign .5
        linear .5 zoom 1.15
    show day3_window_anton_blur:
        xpos 1650
        xanchor .5
        ypos 1080
        yanchor 1.
        linear .5 zoom 1.15 xanchor .25
    "Алиса уводила в чащу мою сестру."
    stop test_one fadeout 1
    play test_two "sounds/Anton-school-run-1.ogg"



    window hide
    scene bg_room_night1 with Dissolve(.5)
    pause .5
    scene phone_hall2 with Dissolve(.5)
    pause .5

    scene phone_hall_hall:
        xpos -450
    show phone_hall_anton:
        yalign 1.
        yoffset 20
        xpos 400




    show phone_hall_stair:
        xpos 900
    with Dissolve(.5)
    window show

    play test_one "sounds/sfx_put_on_clothes.ogg"
    "Понадобилось меньше минуты, чтобы я второпях оделся и вылетел из дому."
    stop test_one fadeout 1
    play test_two "sounds/Door_open.ogg"

    scene phone_hall_hall:
        xpos -450
        linear 2. xpos 0
    show phone_hall_anton:
        yalign 1.
        yoffset 20
        xpos 400
        parallel:
            linear 2. xpos 300
        parallel:
            linear .25 yoffset 0
            linear .25 yoffset 20
            repeat 4
    show phone_hall_stair:
        xpos 900
        linear 2. xpos 900 + 900

    show bg_black:
        alpha 0
        .5
        linear .5 alpha 1

    "Сердце стучало пулемётной очередью."
    play test_one "sounds/Door_close.ogg"
    play fon "sounds/Real_wind.ogg"

    scene home_out_side_hight with Dissolve(.5)

    "От леса тянуло холодом и смолистым запахом хвои, а где-то в поле трещал мороз."

    scene d3_outside_guys_bg
    show d3_outside_guys_a
    show d3_outside_guys_olya
    with Dissolve(.5)

    "Впереди у калитки маячили две тени, лишь рост позволял распознать в них мою сестру и девочку-лисицу."
    play test_two "sounds/steps/sfx_girl_leaves_on_snow2.ogg"
    "Я помчался к забору, слыша вой ветра в ушах и ритмичный скрип под подошвами."

    hide d3_outside_guys_a
    show d3_outside_guys_a behind d3_outside_guys_olya:
        linear 2. xpos 400 alpha .0

    "Фигура повыше шевельнулась и устремилась к чащобе, плавно, будто конькобежец по льду."
    "Я замедлил шаг и коснулся очков, тщетно стараясь вычленить из мрака хоть какие-то детали."
    "Тревога опустилась на плечи, как невесомая снежинка."
    "В животе закопошилась проснувшаяся змея. Стало тошно."
    "Я подумал о доме, о хлипкой крепости позади."

    scene d3_outside_guys_bg:
        align (.5,.5)
        subpixel True
        linear 3. zoom 1.1
    show d3_outside_guys_olya:
        align (.5,.5)
        subpixel True
        linear 3. zoom 1.2

    play test_two "sounds/steps/sfx_girl_leaves_on_snow2.ogg"
    "Наконец я настиг сестрёнку, одетую в одну курточку."
    stop music2 fadeout 15

    voice "voice/anton/3day/130 Ol.ogg"
    Ant "Оля!"
    voice "voice/olya/3day/05 T.ogg"
    Oly "Ты видел лисичку?"
    voice "voice/anton/3day/131 Olya.ogg"
    Ant "Оля, зачем ты вышла на улицу?"
    voice "voice/anton/3day/131 Es.ogg"
    Ant "Если мама узнает..."

    scene d3_outside_olya_0 with Dissolve(.5)
    "Сестра замерла к тайге лицом."
    "До неё было рукой подать, и я зачем-то положил озябшую кисть ей на плечо, наверное, убедиться, что это всё не сон."

    play wtf "sounds/sfx_owl_screamer.ogg"
    window hide
    scene d3_outside_owl_anim
    pause 1.
    $ renpy.stop_predict("d3_outside_owl_anim")
    "В мою сторону торчал острый клюв, со всех сторон усеянный мохнатыми перьями, из которых складывалась морда совы."
    "Нечто в птичьей маске таращилось на меня."
    voice "voice/olya/3day/06 Uxu.ogg"
    Owl "У-ху, не узнает."

    play music "music/Master of the forest.ogg" fadein 2
    "Голос был точь-в-точь Олин, но за перьями и картоном таился некто иной."

    scene home_out_side_hight with Dissolve(.5):
        align (.5, .5)
        zoom 1.01
        parallel:
            linear 2. zoom 1.15

        parallel:
            yoffset 0
            linear 0.07 yoffset -3
            linear 0.07 yoffset 3
            yoffset 0
            linear 0.05 yoffset -2
            linear 0.05 yoffset 2
            yoffset 0
            linear 0.05
            repeat
    play test_one "voice/anton/1day/029.Beg i o.ogg"
    play test_two "sounds/loop_snow_footsteps.ogg"
    "Я рванул прочь, словно меня стегнули нагайкой."
    "Существо в маске лишь притворялось Олей..."
    Ant_m "{i}Чтобы выманить меня!{/i}"



label day3_night:
    $ story_manager.MarkEvent(("day3", "scene21"))
    "Я бежал со всех ног, утопая в снегу."
    "Дом впереди стремительно увеличивался."
    "Жёлтый свет в окнах дарил надежду."
    "Там мама, сестра! Спасение!"
    "За спиной было тихо, как будто никто не гнался за мной."
    "Может, потому что совы умеют летать?"
    stop test_one fadeout 1
    "Я уже карабкался по крыльцу, как вдруг краем глаза заметил ещё одну фигуру."

    $ persistent.animal_unlock[2] = True
    scene wolf_animation

    play test_two "voice/Wolf/305R.ogg"
    "Взъерошенный волчок выполз из угольной тени дома, преградив путь."
    play test_six "sounds/loop_strange_dance.ogg" loop
    "Он двигался дёргано, хаотично, словно приплясывал какой-то жуткий танец..."
    play test_one "voice/Wolf/308 R.ogg"
    "... или корчился в припадке."
    stop test_six fadeout 3
    "И пускай я отчётливо видел, что волчья морда — обыкновенная маска, что-то в судорогах оборотня заставило меня окоченеть."
    play test_one "voice/Wolf/308 RR.ogg"
    "Ряженый потёрся боком о столб крыльца и припал на четвереньки."
    play test_six "sounds/sfx_rustle_sit_down.ogg"
    "Выгнулся так, что позвоночник должен был хрустнуть."
    play test_one "voice/Wolf/307R.ogg"
    "Глаза образины засверкали."
    play test_six "sounds/loop_strange_dance.ogg" loop
    "Но зверь не нападал."
    play test_one "voice/Wolf/306R.ogg"
    "Он то ползал вокруг по-пластунски, то трусил на четырёх конечностях."
    stop test_six fadeout 3
    "С отвисшей челюстью я перебирал ногами, пытаясь удерживать его в поле зрения."
    play test_two "sounds/Kapli-fix.ogg" loop
    "Из-под прорезей маски сочилась жидкость. Тягучие капли падали на доски."
    "«Слюна», — догадался я."
    stop test_two fadeout 3

    $ renpy.start_predict("scare_runaway")

    "Какая-то сила толкнула в спину, шепнула: «{i}Спасайся!{i}»"

    scene scare_bg:
        xalign 0.
    show scare_fence:
        xalign 0.
    with Dissolve(.5)

    "Штакетины забора замельтешили."
    queue wtf [ "<silence 0.3>", "<from 0 to 2>voice/Bear/3day/00.ogg"]
    play test_five "sounds/snow-human-run-2.ogg" loop

    $ persistent.animal_unlock[4] = True
    scene scare_runaway

    play test_one "voice/anton/1day/029.Beg i o.ogg" loop
    "Я снова бежал — в обратную сторону, к зубчатой и пахнущей хвоей кромке леса."
    play test_two "sounds/loop_fast_heartbeat.ogg" fadein 2.5 loop
    "Удары сердца отмеряли время."
    "Волчок позади, будто забыв человеческую речь, рычал:"
    voice "voice/Wolf/308 GR.ogg"
    Noname "Гр-р-р-р... Гр-р-р-р-р..."
    "Правая нога застряла в припорошенной лунке."
    "Я выдернул её, чертыхаясь, и тут же рухнул на землю."
    "Подо мной заструились зыбучие снега, мешая подняться, упереться во что-нибудь."
    "Но дикая жажда жизни буквально вырвала меня из ловушки."
    "Тьма подкрадывалась всё ближе, напоминая едкий дым погребальных костров. И я снова побежал, вдыхая колючий воздух."
    "Волосы развевались на ветру."
    "Падая, я обронил шапку, и уши запекло от лютого мороза, пока сам я весь взмок от пота."
    "Поле наконец закончилось."

    "Понимая, что было не лучшим решением мчаться в лес, я юркнул за деревья."
    "Не останавливаясь, бежал, прикрывая ладонью лицо."
    "Чтобы случайный сук не лишил глаза."
    "Ветки били по одежде, кололи кожу, как мясники, гнавшие скотину прямиком в мясорубку."
    stop test_two fadeout 10
    $ renpy.stop_predict("scare_runaway")

    jump dev_bunny3_candyjumps.end
    label dev_bunny3_candyjumps:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Выбери рут"
            "Полина":
                $ ROUTE_POLINA = True
                $ Flags.Raise("day2 polina")
            "Лиса":
                $ ROUTE_FOX = True
                $ Flags.Raise("day2 fox")
            "Маска":
                $ ROUTE_SOLO = True
                $ Flags.Raise("mask")
        label dev_bunny3_candyjumps.end:


    "Узел выбившихся из почвы корней прихватил за стопу."
    stop music fadeout 3

    show expression "#000":
        alpha 0
        pause .3
        linear 0.2 alpha 1
    stop test_one fadeout 1
    play test_five "sounds/sfx_tree_bump.ogg"
    play test_two "voice/anton/3day/133 O.ogg"
    "Я врезался в шершавый ствол, сполз к самому его основанию и в панике оглянулся."
    play test_one "voice/anton/2day/fear7.ogg"


    scene fox_give_pidorka_bg
    show fox_give_pidorka 0
    show snow_for_forest1_anton
    with Dissolve(1.5)


    voice "voice/Alisa/3day/01 Uh.ogg"
    Alis "Ух, какой ты быстрый!"
    play music2 "music/Mystic Waltz.ogg" volume 0.7 fadein 0.5
    "Первым желанием было кинуться к ней и обнять её."
    "Но я поборол себя и плотнее притиснулся к сосне."
    voice "voice/anton/3day/133.Ti.ogg"
    Ant "Ты... Что ты здесь делаешь?"

    show fox_give_pidorka 1
    with Dissolve(.5)

    voice "voice/Alisa/3day/02 Da.ogg"
    Alis "Да вот."
    "Она протянула мне потерянную шапку."
    voice "voice/Alisa/3day/03 V.ogg"
    Alis "В бюро находок подрабатываю."
    voice "voice/Alisa/3day/04 N.ogg"
    Alis "Надевай, а то уши замёрзнут, а потом, глядишь, и вовсе отвалятся."
    play test_two "voice/Alisa/3day/05 Xa.ogg"
    "Она хихикнула."
    "Я подозрительно смотрел то на неё, то на шапку, будто боялся, что в руке Алисы окажется что-то вроде отрубленной головы — или ещё страшнее."
    "Но шапка была просто шапкой."

    window hide

    call screen day3_fox_pidorka()

    play test_one "sounds/sfx_taking_hat.ogg"
    show fox_give_pidorka 2
    with Dissolve(.5)

    "Я забрал её, натянул по самые брови."
    voice "voice/Alisa/3day/06 T.ogg"
    Alis "Тепло?"
    "Я не ответил."


    scene day3_night_sky_rnd

    show Ant Normal b_evening 00 norm ahead 05
    show snow_for_forest1_anton
    with Dissolve(.5)

    voice "voice/anton/3day/134 Tam.ogg"
    Ant "Там во дворе были какие-то дети."
    show Ant Normal b_evening 00 norm ahead 01 with Dissolve(.3)
    voice "voice/Alisa/3day/07 E.ogg"
    Alis "И что? Покусали тебя, что ли?"
    show Ant Normal b_evening 00 norm ahead 05 with Dissolve(.3)
    voice "voice/anton/3day/135 net.ogg"
    Ant "Нет..."
    show Ant Normal b_evening 00 norm ahead 01 with Dissolve(.3)
    voice "voice/Alisa/3day/08 A.ogg"
    Alis "А чего же ты убежал?"
    "Ответ был очевиден, но, покатав мысль на языке, я лишь пробурчал:"
    show Ant Normal b_evening 00 norm ahead 02 with Dissolve(.3)
    voice "voice/anton/3day/136 Nez.ogg"
    Ant "Не знаю..."
    show Ant Normal b_evening 00 norm ahead 01 with Dissolve(.3)
    voice "voice/Alisa/3day/09 E.ogg"
    Alis "Эх, обещала не обзывать тебя дурачком."
    voice "voice/Alisa/3day/10 A.ogg"
    Alis "А я обещания исполняю."
    play test_one "sounds/sfx_snow_footsteps_0.ogg"
    hide snow_for_forest1_anton
    hide Ant Normal b_evening 00 norm ahead 01
    show big_fox
    show Ant Normal b_evening 00 norm aside 01
    show snow_for_forest1_anton
    with Dissolve(.5)
    "Она подошла вплотную, взяла под локоть."
    show Ant Normal b_evening 00 norm aside 03 with Dissolve(.3)
    "Я почувствовал запах мяты, апельсинов и сгоревших бенгальских огней."
    "Захотелось наклониться к Алисе, чтобы распробовать все тонкости ароматов."
    voice "voice/Alisa/3day/11 S.ogg"
    Alis "Сколько можно повторять: со мной ты в безопасности."
    voice "voice/Alisa/3day/12 Ya.ogg"
    Alis "Я твой друг."
    show Ant Normal b_evening 00 norm aside 01 with Dissolve(.3)
    voice "voice/Alisa/3day/13 E.ogg"
    Alis "И они."
    stop music2 fadeout 2

    scene day3_night_sky_rnd
    show big_fox
    show ant_day3_evning 1
    show snow_for_forest1_anton
    with Dissolve(.5)

    play test_two"voice/anton/3day/137 Aa.ogg"
    "Я быстро обернулся туда, куда показывала лисичка."
    play test_one "sounds/gong-echo-2.ogg"

    scene bg_pole0
    show bg_Beast:
        pos (286, 233)
    show cover_2
    show snow_for_forest1_anton
    with Dissolve(.5)

    "На краю опушки появились дети в масках. По крайней мере все они были небольшого роста."
    play test_six "sounds/Phrases_07.ogg"

    scene day3_candy_meet
    show snow_for_forest1_anton
    with Dissolve(.5)
    "Волчок, сова и медвежонок."
    play test_two "sounds/steps/loop_five_kids_footsteps_snow.ogg"
    play test_three "voice/Bear/3day/0.ogg" fadein 2


    scene bg_forest0_long_dark:
        xpos -1213
    show Bear Normal m 02:
        align (.5, 1.)
        xoffset -400
    show Wolf Normal m 01:
        align (.5, 1.)
    show Owl Normal m 02:
        align (.5, 1.)
        xoffset 400
    show snow_for_forest1_anton
    with Dissolve(.5)
    stop test_two fadeout 2
    "Они фыркали и вздыхали, явно утомившись от бега."
    play test_one "sounds/steps/step_snow2.ogg"

    show Owl Normal m 02:
        align (.5, 1.)
        xoffset 400
        parallel:
            linear .5 xoffset 600 zoom 1.1
        parallel:
            "Owl Normal m 00" with Dissolve(.5)
    pause .5
    stop test_three fadeout 2
    voice "voice/Owl/3day/09 Ya.ogg"
    Noname "Я ду-у-ху-мала, ты в снег провалился."
    play music "music/23_Christmas.ogg" volume 0.8
    voice "voice/Owl/3day/10 S.ogg"
    Noname "Стала снег копать – нет тебя."
    play test_one "sounds/steps/step_snow1.ogg"

    show Owl Normal m 00:
        align (.5, 1.)
        xoffset 600
        zoom 1.1
        linear .5 zoom 1.0

    show Bear Normal m 02 behind Wolf:
        align (.5, 1.)
        xoffset -400
        parallel:
            linear .5 xoffset -600 zoom 1.1
        parallel:
            "Bear Normal m 00" with Dissolve(.5)
    pause .5
    voice "voice/Bear/3day/01 A.ogg"
    Noname "А я не копал. Лень копать было."
    voice "voice/Bear/3day/02 O.ogg"
    Noname "Оно как получается: если дурак, то бегай да копай."
    voice "voice/Bear/3day/03 Ae.ogg"
    Noname "А если умный — подожди, пока другие набегаются, накопаются и устанут."
    voice "voice/Bear/3day/04 E.ogg"
    Noname "И уж тогда заводи разговор."
    play test_one "sounds/steps/step_snow2.ogg"

    hide Bear
    show Bear Normal m 00 behind Wolf:
        align (.5, 1.)
        xoffset -600
        zoom 1.1
        linear .5 zoom 1.0

    show Wolf Normal m 01:
        align (.5, 1.)
        "Wolf Normal m 00" with Dissolve(.5)
        linear .5 zoom 1.1

        .6
        "Wolf Normal m 00"
        .5
        linear .5 zoom 1.0
    pause .5

    voice "voice/Wolf/309 Kak.ogg"
    Noname "Как я р-р-рад!"

    hide Wolf
    show Wolf Normal m 00:
        align (.5, 1.)
        linear .15 zoom 1.1
        "Wolf Normal m 02"
        .9
        "Wolf Normal m 00"
        .5
        linear .5 zoom 1.0

    voice "voice/Wolf/310 D.ogg"
    Noname "Дегенер-р-р-рат!"

    scene day3_night_sky_rnd
    show big_fox
    show Ant Normal b_evening 03 alpha0 ahead 06
    show snow_for_forest1_anton
    with Dissolve(.3)
    window show
    voice "voice/anton/3day/137A.ogg"
    Ant "А?"
    voice "voice/Alisa/3day/12 Neobr.ogg"
    Alis "Не обращай внимания, он со странностями."
    "Я понял, что стою с открытым ртом, с бессильно опущенными руками."


    hide ant_day3_evning
    show Ant Normal b_evening 00 norm ahead 01 behind snow_for_forest1_anton
    with Dissolve(.3)
    "Не зная, как реагировать на слова поздних гостей, я всё-таки выдавил подобие улыбки."

    show Ant Normal b_evening 00 norm ahead 03
    with Dissolve(.3)
    voice "voice/anton/3day/138 V.ogg"
    Ant "Вы просто меня напугали."
    hide big_fox
    show big_fox behind Ant:
        linear 1. xoffset -750
    pause .35


    scene bg_forest0_long_dark:
        xpos -1160
    show Bear Normal m 00 at bear_pos
    show Wolf Normal m 00 at wolf_pos
    show Owl Normal m 00 at owl_pos
    show Fox Normal m_night 00 at fox_pos
    show snow_for_forest1_anton_02
    with Dissolve(.5)

    "Они начали переглядываться, а кто-то даже фыркнул, словно услышал шутку."

    call wolf_upd (wolf_Normal, step_in, jump_amt=3, jump_offset=10, jump_speed=.1) from _call_wolf_upd
    voice "voice/Wolf/310 Da.ogg"
    Noname "Да, да! Лиса права..."
    call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_1

    call bear_upd (bear_Alter, step_in) from _call_bear_upd
    voice "voice/Bear/3day/06 Eto.ogg"
    Noname "Это он!"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_1

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd
    voice "voice/Alisa/3day/15 N.ogg"
    Alis "Нет, это наш..."
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_1
    hide snow_for_forest1_anton_02
    show snow_for_forest1_anton_02
    call owl_upd (owl_Alter, step_in) from _call_owl_upd
    voice "voice/Owl/3day/15 N.ogg"
    Noname "Неужели нашли?"
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_1

    call bear_upd (bear_Alter, step_in) from _call_bear_upd_2
    voice "voice/Bear/3day/07 Na.ogg"
    Noname "Наш Зайчик!"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_3

    call owl_upd (owl_Alter, step_in) from _call_owl_upd_2
    voice "voice/Owl/3day/16 D.ogg"
    Noname "Да, да, похож..."
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_3

    hide snow_for_forest1_anton_02
    show snow_for_forest1_anton_02
    call wolf_upd (wolf_Normal, step_out, jump_amt=5, jump_offset=10, jump_speed=.1) from _call_wolf_upd_2
    play test_two "voice/Wolf/311 R.ogg"
    "Взбесившийся от радости волчок начал махать частью костюма, словно хвостом."

    call wolf_upd (wolf_Normal, step_in, jump_amt=5, jump_offset=10, jump_speed=.1) from _call_wolf_upd_3
    voice "voice/Wolf/312 P.ogg"
    Noname "Пе-е-ер-р-р-рвый!"
    call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_4

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_2
    voice "voice/Alisa/3day/17 Nu.ogg"
    Alis "Ну конечно, ты первый."
    voice "voice/Alisa/3day/18 Et.ogg"
    Alis "Это Волчик раньше всех почуял Зайчика в тебе. И рассказал нам."
    hide snow_for_forest1_anton_02
    show snow_for_forest1_anton_02
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_3
    voice "voice/anton/3day/52 Zd.ogg"
    Ant "Здравствуй."
    voice "voice/Alisa/3day/02 S.ogg"
    Alis "С нашей Совушкой ты знаком не понаслышке. Не такая она уж и страшная, правда?"
    voice "voice/anton/3day/53 Da.ogg"
    Ant "Да, наверное..."
    play test_two "voice/Bear/3day/05Ha.ogg"
    voice "voice/Alisa/3day/04 A.ogg"
    Alis "А этот улыбчивый бугай — Медвежутка."
    voice "voice/Alisa/3day/05 T.ogg"
    Alis "Ты лучше с ним поласковее, а то голову откусит."
    voice "voice/anton/3day/54 Za.ogg"
    Ant "Зачем это?"

    voice "voice/Alisa/3day/06 M.ogg"
    Alis "М-да, смотрю, ты и чувство юмора где-то обронил."

    $ renpy.start_predict("beast_dance_1")
    $ renpy.start_predict("beast_dance_2")









    "Всё ещё сомневаясь в благих намерениях причудливых зверят, я спрятал руки за спину, стараясь при этом не смотреть на зияющие дыры карнавальных масок вместо глаз."

    call fox_upd (fox_Nice, step_in, jump_offset=10, jump_speed=.2) from _call_fox_upd_4
    play sound "voice/Alisa/3day/00 h.ogg"
    "Алиса наигранно подбоченилась и как-то ухитрилась подмигнуть своей рыжей личиной."
    call fox_upd (fox_Normal, step_in) from _call_fox_upd_5



    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_6
    voice "voice/Alisa/3day/19 K.ogg"
    Alis "Когда в следующий раз придём — будем звенеть в колокольчики, чтобы ты не так боялся нашего визита."
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_7

    hide snow_for_forest1_anton_02
    show snow_for_forest1_anton_02
    call owl_upd (owl_Alter, step_in) from _call_owl_upd_4
    voice "voice/Owl/3day/01 A.ogg"
    Owl "А у нас разве есть колокольчики?"
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_5

    call bear_upd (bear_Alter, step_in) from _call_bear_upd_4
    voice "voice/Bear/3day/09 Ch.ogg"
    Bear "Чур, я звенеть не буду."
    voice "voice/Bear/3day/10 U.ogg"
    Bear "У меня лапка болит."
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_5

    play test_two"voice/anton/3day/139 Ul.ogg"
    "Моя улыбка стала настоящей."

    hide snow_for_forest1_anton_02
    show snow_for_forest1_anton_02
    call fox_upd (fox_Flirt, step_in) from _call_fox_upd_8
    voice "voice/Alisa/3day/13 Ozu.ogg"
    Alis "О, зубы показал — это добрый знак."
    voice "voice/Alisa/3day/14 Neo.ogg"
    Alis "Не ожидала, что сможем тебя рассмешить."
    voice "voice/Alisa/3day/15 Ya.ogg"
    Alis "Я думала, это под силу только Диснейленду."

    voice "voice/anton/3day/140 Otk.ogg"
    Ant "Откуда ты знаешь?"

    call fox_upd (fox_Normal, step_in) from _call_fox_upd_9
    voice "voice/Alisa/3day/20 Da.ogg"
    Alis "Да так, прочитала кое-где..."

    voice "voice/anton/3day/141 Pro.ogg"
    Ant "Про меня?"

    call fox_upd (fox_Nice, step_in) from _call_fox_upd_10
    voice "voice/Alisa/3day/24 Pr.ogg"
    Alis "Про клюв от воробья! Про Диснейленд, яхонтовый."
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_11

    call owl_upd (owl_Alter, step_in) from _call_owl_upd_6
    voice "voice/Owl/3day/12 T.ogg"
    Owl "Ты умеешь читать по-человечески?"
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_7

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_12
    voice "voice/Alisa/3day/25 Z.ogg"
    Alis "Зря я, что ли, в школу хожу день ото дня?"
    stop fon fadeout 3
    stop music fadeout 2
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_13

    label dev_d3_dance:

    scene black with Dissolve(1.)

    show bd_snow_behind:
        alpha 0
        linear 3. alpha 1
    show day3_beasts_scene2_snow5 zorder 1:
        alpha 0
        linear 3. alpha 1

    "И она кокетливо запела:"

    $ is_save_allowed = False

    show fox_appear
    pause 2.5

    hide fox_appear
    show Fox Fullface b_night 00
    with Dissolve(.5)

    hide Fox
    show beast_dance_1



    window auto
    play test_one "voice/Alisa/3day/01 Ka.ogg"
    Alis "Как детей не замечать, как мечты их развенчать \nУчат в школе, учат в школе, учат в школе!{w=7.367}{nw}"



    hide beast_dance_1
    show beast_dance_2


    Alis "Крепко-накрепко вломить, с детства слабеньких чморить \nУчат в школе, учат в школе, учат в школе!"
    play test_two"voice/anton/3day/142 Xe.ogg"

    $ renpy.stop_predict("beast_dance_1")
    $ renpy.stop_predict("beast_dance_2")

    $ is_save_allowed = True
    "Я осторожно засмеялся."
    play fon "sounds/Real_wind.ogg" fadein 2.0 loop
    play music "music/11_Poryadok.ogg" volume 0.65

    scene day3_beasts_scene2_bg

    show day3_beasts_scene2_snow1

    show day3_beasts_scene2_children

    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3

    show day3_beasts_scene2_tree

    show day3_beasts_scene2_snow4

    show day3_beasts_scene2_k

    show day3_beasts_scene2_snow5 zorder 1
    with Dissolve(.5)
    "Новые знакомые уже не отпугивали, а, напротив, привлекали."
    "Было в них что-то особенное."
    "И в этой опушке, и в луне, и в снежинках, которые почему-то падали наоборот, с земли в тёмное небо, как на прокрученной задом наперёд плёнке."
    "Дети в масках приблизились, и я ощутил их прикосновения: они хлопали дружески, трогали мою одежду, словно проверяли, что я настоящий."
    "В их прикосновениях не было звериной злости — лишь чистое незамутнённое любопытство ребёнка."
    "И я почему-то сказал про себя:"
    Ant_m "«{i}Им можно доверять{/i}»."
    "Снежинки всё планировали ввысь."

    scene bg_forest0_long_dark:
        xpos -1160

    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4

    show Bear Normal m 00 at bear_pos
    show Wolf Normal m 00 at wolf_pos
    show Owl Normal m 00 at owl_pos
    show Fox Normal m_night 00 at fox_pos

    show day3_beasts_scene2_snow5 zorder 1
    with Dissolve(.5)

    call owl_upd (owl_Alter, step_in) from _call_owl_upd_8
    voice "voice/Owl/3day/14 N.ogg"
    Owl "Никто тебя больше не обидит."
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_9

    call wolf_upd (wolf_Normal, step_in, jump_amt=3, jump_offset=10, jump_speed=.1) from _call_wolf_upd_5
    voice "voice/Wolf/313 D.ogg"
    Wolf "Др-р-руг."
    call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_6

    call bear_upd (bear_Alter, step_in) from _call_bear_upd_6
    voice "voice/Bear/3day/12 P.ogg"
    Bear "Пусть только попробуют!"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_7

    pause .3

    scene bg_forest0_long_dark:
        xpos -1160
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4
    show Bear Normal m 00 at bear_pos
    show Wolf Normal m 00 at wolf_pos
    show Owl Normal m 00 at owl_pos
    show Fox Normal m_night 00 at fox_pos
    show day3_beasts_scene2_snow5 zorder 1
    with hpunch
    play test_two "voice/Alisa/3day/08 Tol.ogg"
    play sound "sounds/sfx_one_pat.ogg"
    "Лиса тихонько пихнула меня в плечо и рассмеялась."
    stop test_two fadeout 0.5
    call fox_upd (fox_Flirt, step_in) from _call_fox_upd_14
    voice "voice/Alisa/3day/28 N.ogg"
    Alis "Ну что, Тоша, убежишь с воплями или с нами пойдёшь?"

    voice"voice/anton/3day/143 Ku.ogg"
    Ant "Куда?"
    stop music fadeout 4

    call fox_upd (fox_Oh, step_in, jump_amt=4, jump_offset=20, jump_speed=.15) from _call_fox_upd_15
    voice "voice/Alisa/3day/29 N.ogg"
    Alis "А-ха-ха-ха! На аттракционы!"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_16
    play music2 "music/5_Shadow_Dance.ogg" fadein 1
    "В эту секунду далёкий звук флейты нарушил обманчивую тишину тайги."
    "Прекрасный и таинственный, он вызывал в памяти звон хрусталя и журчание студёного ручья."

label beasts_sky:
    $ story_manager.MarkEvent(("day3", "scene22"))
    scene day3_beasts_scene2_bg
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_children
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_tree
    show day3_beasts_scene2_snow4
    show day3_beasts_scene2_k
    show day3_beasts_scene2_snow5 zorder 1
    with Dissolve(.5)
    "Если какие-то сомнения оставались, то песня флейты развеяла их."
    play test_two "sounds/steps/loop_five_kids_footsteps_snow.ogg"

    hide day3_beasts_scene2_children with Dissolve(1.)
    "Я пошёл за новыми друзьями прежде, чем принял решение."


    hide day3_beasts_scene2_k
    show day3_beasts_scene2_k:
        linear 2. xoffset -1000

    show bg_black:
        alpha 0
        .25
        linear 1. alpha 1

    "Ноги сами переступали, а образованные соснами туннели раздвигались. Кусты кланялись перед нашей процессией."
    "Всё это напоминало сон."

    scene day3_forest_scene2:
        ypos -444
        linear 15 ypos 0
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4
    show day3_beasts_scene2_snow5 zorder 1
    with Dissolve(.5)
    stop test_two fadeout 2
    "Ведь даже поляну, на которую мы выбрались, я видел во сне."
    "Флейта, как чудесная птица, парила где-то высоко, между тёмных крон."
    "Снежинки, взлетая, закручивались спиралью."
    "Луна окрашивала ветви в серебряный цвет."
    play test_two "voice/Alisa/3day/30 Ah.ogg"
    "Алиса зачарованно ахнула. И я разделял её восторг."

    show day3_forest_scene2 behind day3_beasts_scene2_snow1:
        linear 1 ypos 0
    "Задрав голову, я смотрел вверх."

    $ beasts_low = True

    show Owl Normal m 00:
        align (.5, 1.)
        xoffset owl_xoffset
        yoffset 100 + low_yoffset*beasts_low
        alpha 0
        linear .5 yoffset low_yoffset*beasts_low alpha 1
    $ music_during_lines = 0.6
    voice "voice/Owl/3day/15 K.ogg"
    Owl "У-у-ух, красиво как!"

    show Bear Normal m 00:
        align (.5, 1.)
        xoffset bear_xoffset
        yoffset 100 + low_yoffset*beasts_low
        alpha 0
        linear .5 yoffset low_yoffset*beasts_low alpha 1
    play test_two"voice/Bear/3day/11 Heh.ogg"
    voice "voice/anton/3day/144 Och.ogg"
    Ant "Очень красиво."

    show Wolf Normal m 00:
        align (.5, 1.)
        xoffset wolf_xoffset
        yoffset 100 + low_yoffset*beasts_low
        alpha 0
        linear .5 yoffset low_yoffset*beasts_low alpha 1
    play test_one "voice/Wolf/314 R.ogg"
    "Волчок одобрительно завыл."

    show Fox Normal m_night 00:
        align (.5, 1.)
        xoffset fox_xoffset
        yoffset 100 + low_yoffset*beasts_low
        alpha 0
        linear .5 yoffset low_yoffset*beasts_low alpha 1
    stop test_one fadeout 0.5
    voice "voice/Alisa/3day/31 E.ogg"
    Alis "Это мелочи!"

    call fox_upd (fox_Fullface, step_in, is_low=beasts_low) from _call_fox_upd_17
    voice "voice/Alisa/3day/32 Ya.ogg"
    Alis "Я покажу гораздо больше..."
    voice "voice/Alisa/3day/33 E.ogg"
    Alis "Если захочешь."
    call fox_upd (fox_Normal, step_out, is_low=beasts_low) from _call_fox_upd_18

    "А я хотел. Как сильно я хотел увидеть то, что видела лисичка своими спрятанными в полутьме капюшона глазами!"
    "Теперь смущало не то, что дети носили маски, а то, что без маски был я."
    "Точно голый на январском ветру."

    $ beasts_low = False

    show day3_forest_scene2 behind day3_beasts_scene2_snow1:
        ypos 0
        linear 1 ypos -400

    show Owl Normal m 00:
        align (.5, 1.)
        xoffset owl_xoffset
        yoffset low_yoffset
        linear 1 yoffset 0

    show Bear Normal m 00:
        align (.5, 1.)
        xoffset bear_xoffset
        yoffset low_yoffset
        linear 1 yoffset 0

    show Wolf Normal m 00:
        align (.5, 1.)
        xoffset wolf_xoffset
        yoffset low_yoffset
        linear 1 yoffset 0

    show Fox Normal m_night 00:
        align (.5, 1.)
        xoffset fox_xoffset
        yoffset low_yoffset
        linear 1 yoffset 0

    voice"voice/anton/3day/145 S.ogg"
    Ant "Скажите, а зачем вам маски?"
    "Я не боялся, хотя меня и трясло."
    "Дрожь была не от холода, а от странного волнения, предвкушения чего-то невероятного."

    show day3_forest_scene2 behind day3_beasts_scene2_snow1:
        ypos -400

    show Bear Normal m 00 at bear_pos
    show Wolf Normal m 00 at wolf_pos
    show Owl Normal m 00 at owl_pos
    show Fox Normal m_night 00 at fox_pos

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_19
    voice "voice/Alisa/3day/07 At.ogg"
    Alis "А тебе зачем?"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_20

    "Я дотронулся до прохладной щеки."
    voice"voice/anton/3day/146 No.ogg"
    Ant "Но я без маски."

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_21
    voice "voice/Alisa/3day/35 O.ogg"
    Alis "А-ха-ха-ха! Обожаю человеческие сказки!"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_22

    call owl_upd (owl_Alter, step_in) from _call_owl_upd_10
    voice "voice/Owl/3day/16 Ch.ogg"
    Owl "Человеческие ласки?"
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_11

    call bear_upd (bear_Normal, step_in) from _call_bear_upd_8
    voice "voice/Bear/3day/13 Ch.ogg"
    Bear "Человеческие дрязги."
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_9

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_23
    voice "voice/Alisa/3day/36 Ya.ogg"
    Alis "Я же говорила..."
    voice "voice/Alisa/3day/36 V.ogg"
    Alis "Все жители посёлка носят маски."
    voice "voice/Alisa/3day/37 T.ogg"
    Alis "Только скрываются за ними отнюдь не люди."
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_24

    voice"voice/anton/3day/147 E.ogg"
    Ant "И даже я?"

    call bear_upd (bear_Normal, step_in) from _call_bear_upd_10
    voice "voice/Bear/3day/14 T.ogg"
    Bear "Хе-хе, ты такой рассеянный, Антон."
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_11

    call owl_upd (owl_Normal, step_in) from _call_owl_upd_12
    voice "voice/Owl/3day/17 Od.ogg"
    Owl "Однажды мы уже нашли твои очки."
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_13

    call wolf_upd (wolf_Normal, step_in, jump_amt=3, jump_offset=10, jump_speed=.1) from _call_wolf_upd_7
    voice "voice/Wolf/315 E.ogg"
    Wolf "И шапку-у-у-у!"
    call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_8


    scene fox_give_pidorka_bg

    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2

    show fox_give_beast

    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4

    show fox_give_mask
    show snow_for_forest1_anton

    show day3_beasts_scene2_snow5 zorder 1

    with Dissolve(1.5)

    voice "voice/Alisa/3day/38 E.ogg"
    Alis "И твоё настоящее лицо."
    $ music_during_lines = 1.0


    "Я увидел маску, которую лиса мне протягивала."
    "Ту самую маску зайчика, похожую на серебряный слиток в лунном свете."
    "Любопытно стало, как изменится мир, если взглянуть сквозь прорези."

    window hide
    call screen day3_fox_mask()
    hide fox_give_mask
    show fox_give_pidorka 2 behind snow_for_forest1_anton
    with Dissolve(.5)
    window show
    "Но вдруг, с трудом просачиваясь сквозь мелодию флейты, меня посетило озарение: очки, которые они нашли, были у Семёна."
    "Мои новые знакомые наверняка знали, что с ним произошло."
    "Или хуже..."
    stop music2 fadeout 2
    stop music fadeout 2

    scene day3_forest_scene2:
        ypos -400
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4
    show day3_beasts_scene2_snow5 zorder 1

    show Bear Normal m 00 at bear_pos
    show Wolf Normal m 00 at wolf_pos
    show Owl Normal m 00 at owl_pos
    show Fox Normal m_night 00 at fox_pos

    with Dissolve(.5)
    voice"voice/anton/3day/148 A.ogg"
    Ant "А куда подевался Семён? Что с ним стало?"


    voice"voice/anton/3day/148 Es.ogg"
    Ant "И с остальными детьми?"
    call owl_upd (owl_Sad, step_out) from _call_owl_upd_14
    call bear_upd (bear_Sad, step_out) from _call_bear_upd_12
    play music "music/amb new combined.ogg" 
    "Медвежонок и сова переглянулись."
    call fox_upd (fox_Sad, step_out) from _call_fox_upd_25
    call wolf_upd (wolf_Sad, step_out) from _call_wolf_upd_9
    "Волчок сжался комочком, а лисичка чуть опустила острый носик маски."

    $ music_during_lines = 0.65
    call owl_upd (owl_Sad, step_in) from _call_owl_upd_15
    voice "voice/Owl/3day/18 T.ogg"
    Owl "Тот, кого держали в клетке!"
    call owl_upd (owl_Sad, step_out) from _call_owl_upd_16

    call wolf_upd (wolf_Sad, step_in, jump_amt=5, jump_offset=10, jump_speed=.1) from _call_wolf_upd_10
    voice "voice/Wolf/316 T.ogg"
    Wolf "Тот, кто р-р-режет мелко-мелко!"
    call wolf_upd (wolf_Sad, step_out) from _call_wolf_upd_11

    call fox_upd (fox_Sad, step_in) from _call_fox_upd_26
    voice "voice/Alisa/3day/39 T.ogg"
    Alis "Тот, кто носит кожаное лицо, забрал их."
    call fox_upd (fox_Sad, step_out) from _call_fox_upd_27

    call bear_upd (bear_Sad, step_in) from _call_bear_upd_13
    voice "voice/Bear/3day/15 Um.ogg"
    Bear "Умел бы я креститься – перекрестился бы."
    call bear_upd (bear_Sad, step_out) from _call_bear_upd_14

    voice "voice/anton/3day/149 H.ogg"
    Ant "Хотите сказать, это был человек?"

    call fox_upd (fox_Sad2, step_in) from _call_fox_upd_28
    voice "voice/Alisa/3day/16 Chem.ogg"
    Alis "Чем ты только слушал?"
    call fox_upd (fox_Sad, step_in) from _call_fox_upd_29
    voice "voice/Alisa/3day/17 Razv.ogg"
    Alis "Разве можно назвать такого, как он, человеком?"
    call fox_upd (fox_Sad, step_out) from _call_fox_upd_30

    call bear_upd (bear_Sad, step_in) from _call_bear_upd_15
    voice "voice/Bear/3day/16 O.ogg"
    Bear "Одно слово – взрослый."
    call bear_upd (bear_Sad, step_out) from _call_bear_upd_16

    call owl_upd (owl_Sad, step_in) from _call_owl_upd_17
    voice "voice/Owl/3day/19 V.ogg"
    Owl "В мире взрослых так легко потеряться."
    stop music fadeout 10
    call owl_upd (owl_Sad, step_out) from _call_owl_upd_18


    call fox_upd (fox_Sad, step_in) from _call_fox_upd_31
    voice "voice/Alisa/3day/42 U.ogg"
    Alis "Убийцы, жестокие дрессировщики и равнодушные родители..."
    voice "voice/Alisa/3day/43 L.ogg"
    Alis "Эх, лучше об этом вовсе не думать, чтобы не грустить."

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_32
    voice "voice/Alisa/3day/44 A.ogg"
    Alis "Не знаю, как вам, а мне печалиться совсем не хочется."
    play music2 "music/Flute 2(reverb).ogg"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_33

    pause .1
    call bear_upd (bear_Normal, step_in) from _call_bear_upd_17
    pause .05
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_19
    pause .2
    call wolf_upd (wolf_Normal, step_out) from _call_wolf_upd_12
    voice "voice/Bear/3day/17 E.ogg"
    Bear "И я сегодня какой-то не грустный."
    voice "voice/Bear/3day/18 A.ogg"
    Bear "Антон, а ты?"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_18

    voice"voice/anton/3day/150 A.ogg"
    Ant "А?"
    "Я задумался, глядя в лес, пытаясь определить, откуда доносится звук флейты."
    "Я был уверен, что музыкант стоит прямо за частоколом сосен."
    "Очень высокий, перебирающий длинными пальцами дырочки в корпусе флейты."

    call bear_upd (bear_Alter, step_in) from _call_bear_upd_19
    voice "voice/Bear/3day/20 T.ogg"
    Bear "Так что? Сядем тосковать или займёмся отдыхом?"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_20

    voice"voice/anton/3day/151 Al.ogg"
    Ant "Алиса хотела что-то показать..."

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_34
    voice "voice/Alisa/3day/45 D.ogg"
    Alis "Давай начнём с самой сладкой части программы!"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_35


    play test_two "sounds/sfx_pull_candies.ogg"
    "Лисичка извлекла из карманов горсть конфет и вручила по очереди всем детям."
    play test_one "sounds/sfx_unwrap_candies.ogg"
    "Зашуршали фантики. Тут же запахло ананасом, какао и дыней."
    play test_one "sounds/steps/step_snow1.ogg"

    hide Fox
    hide fox_sprite_cur
    show Fox Normal m_night 00:
        align (.5, .5)
        xoffset fox_xoffset
        parallel:
            linear .5 zoom 1.35 xoffset 0
        parallel:
            .25
            linear .25 alpha 0

    pause 1.

    play test_two "voice/Alisa/3day/46 Am.ogg"


    show day3_night_sky_fox_oko
    with Dissolve(.5)
    play test_five"voice/anton/3day/152 Am.ogg"
    "Последнюю конфету, вафельную, мою любимую, Алиса вложила мне прямо в рот."
    "Язык обволокло пряностью."
    play test_one "sounds/steps/step_snow2.ogg"
    hide day3_night_sky_fox_oko with Dissolve(.5)
    hide Fox
    show Fox Fullface m_night 00 at fox_pos with Dissolve(.5)
    $ fox_sprite_cur = fox_Fullface
    $ fox_zoom_cur = step_out
    "Казалось, что моё тело покрылось шерстью, по которой пробегали яркие искорки."
    queue sound [ "<silence 1.0>", "<from 0 to 3>sounds/glotok-fix.ogg"]
    "Замешкав, я прожевал вафли и шоколад, проглотил их, наслаждаясь вкусом."

    play test_two"voice/anton/3day/153 Sp.ogg"
    Ant "Спасибо..."

    window hide
    show mask_01_up zorder 1
    with Dissolve(1.0)
    $ renpy.pause(2.0)
    "Благодарность вышла глуховатой, потому что губы мои уже касались маски."
    play sound "sounds/sfx_wear_mask.ogg"

    show mask_02_hand zorder 1
    hide mask_01_up
    with Dissolve(0.5)

    pause .5

    hide mask_02_hand
    show mask_03_face zorder 1
    with Dissolve(0.7)

    pause .5


    hide mask_03_face
    show mask_03_hide zorder 1
    with Dissolve(0.3)

    "Я не заметил, как поднёс её к лицу."
    "От папье-маше исходило тепло. Маска льнула к коже, и приятно пощипывало."
    "Так я нырял после зимней прогулки в горячую ванну и лежал, мурча от пенной воды."


    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_36
    voice "voice/Alisa/3day/47 G.ogg"
    Alis "Говорила же: это твоё!"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_37

    voice"voice/anton/3day/154 M.ogg"
    Ant "Моё!"

    call bear_upd (bear_Normal, step_in) from _call_bear_upd_21
    voice "voice/Bear/3day/21 Ch.ogg"
    Bear "Чего стоим? За нас веселиться никто не будет!"
    call bear_upd (bear_Normal, step_out) from _call_bear_upd_22

    call owl_upd (owl_Normal, step_in) from _call_owl_upd_20
    voice "voice/Owl/3day/21 E.ogg"
    Owl "И то верно!" id beasts_sky_21310ee3
    $ music_during_lines = 1.0
    call owl_upd (owl_Normal, step_out) from _call_owl_upd_21

    "Мелодия кружилась по поляне, как вихрь."
    stop music2 fadeout 2
    "Не терпелось выпустить ту энергию, тот жар, которыми меня наполняла чарующая музыка."
    play test_two "voice/Owl/3day/22 Uuh.ogg"
    play test_six "sounds/sfx_wings_sweep_2.ogg"


    hide Owl
    hide owl_sprite_cur
    show owl_jump at owl_pos
    pause .5

    scene day3_forest_scene2:
        ypos -400
        linear 1. ypos 0
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4
    show day3_beasts_scene2_snow5 zorder 1

    show Bear Normal m 00 at bear_pos:
        linear 1. yoffset 300
    show Wolf Normal m 00 at wolf_pos:
        linear 1. yoffset 300
    show Fox Normal m_night 00 at fox_pos:
        linear 1. yoffset 300


    play test_one "sounds/flapping-1.ogg"
    "Сова прыгнула и исчезла высоко вверху."
    play test_six "sounds/sfx_owl_lands_snow.ogg"
    stop test_one fadeout 0.5



    scene day3_forest_scene2:
        ypos 0
        linear .25 ypos -400
    show day3_beasts_scene2_snow1
    show day3_beasts_scene2_snow2
    show day3_beasts_scene2_snow3
    show day3_beasts_scene2_snow4
    show day3_beasts_scene2_snow5 zorder 1

    show Bear Normal m 00 at bear_pos:
        yoffset 300
        linear .25 yoffset 0
    show Wolf Normal m 00 at wolf_pos:
        yoffset 300
        linear .25 yoffset 0
    show Fox Normal m_night 00 at fox_pos:
        yoffset 300
        linear .25 yoffset 0
    pause .25
    show owl_land
    with vpunch

    play test_one "voice/Owl/3day/24 UF.ogg"
    "Над головой раздался её смех, а потом она приземлилась обратно, фырча и отдуваясь."

    call fox_upd (fox_Fullface, step_in) from _call_fox_upd_38
    voice "voice/Alisa/3day/48 E.ogg"
    Alis "И ты так можешь! Попробуй!"
    call fox_upd (fox_Normal, step_out) from _call_fox_upd_39
    "Я попробовал."
    play sound "sounds/sfx_girl_hit.ogg"
    play test_two"voice/anton/3day/155Wow.ogg"
    play music "music/FoxSong_Instumental+back_vocal.ogg" volume 0.85 fadein 0.5

    window hide

    $ dz = .015
    scene day3_jump_first:
        subpixel True
        align (.5,.5)
        zoom 1.
        easein_quad 2. zoom (.55 - dz)
        block:
            ease 3. zoom .55 + dz
            ease 3. zoom .55 - dz
            repeat

    show day3_jump_snow:
        alpha 0
        2.
        linear 1.5 alpha 1

    pause 2.
    window auto


    "Ноги оттолкнулись от земли. Я взлетел ракетой к звёздам и закричал от счастья, увидев своих друзей внизу."
    "Ветер помогал мне лететь. Словно я скакал на громадном батуте."
    stop fon fadeout 2

    window hide
    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .8
        easein 2. zoom .85
    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .6
        easein 2. zoom .9
    show day3_jump_sky_forest:
        align (.5,.5)
        zoom .8
        easein 2. zoom 1.

    pause 2.
    window auto

    $ story_manager.MarkEvent(("day3", "scene23"))

    Narrator_color "Звёзды казались яркими блёстками, до которых можно дотянуться языком, слизнуть."

    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .85
        easeout 2. zoom .8

    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .9
        easeout 2. zoom .6

    show day3_jump_sky_forest:
        align (.5,.5)
        zoom 1
        easeout 2. zoom .8


    Narrator_color "Луна стала ближе... А потом я полетел вниз."
    play sound "sounds/fall.ogg"
    Narrator_color "Лишь на мгновение испугался, что сломаю ноги, но подошвы твёрдо встали на снег."

    $ music_during_lines = 0.65
    voice "voice/Alisa/3day/49 S.ogg"
    Alis_Color "С нами ты в безопасности!"
    voice "voice/Alisa/3day/50 E.ogg"
    Alis_Color "И все твои мечты станут явью!"
    voice "voice/Alisa/3day/51 Ya.ogg"
    Alis_Color "Я так счастлива наконец обрести тебя..."
    voice "voice/Alisa/3day/52 Z.ogg"
    Alis_Color "Зайчик."
    play test_two"voice/anton/3day/155 Sm.ogg"
    Narrator_color "Смеясь от восторга, я понял главное: эти четверо не причинят мне вреда."
    Narrator_color "А настоящие враги – я чувствовал это каждой шерстинкой своей маски – те, кто далёк от волшебства."
    Narrator_color "Люди из посёлка."

    window hide
    scene day3_jump_sky_stars:
        align (.5,.5)
        zoom .85
        linear 15*100000 rotate 360*100000

    show day3_jump_sky_moon:
        align (.5,.5)
        zoom .6

    show day3_jump_sky_forest:
        align (.5,.5)
        zoom 0.8
        linear 25*100000 rotate -360*100000

    pause 2.
    window auto

    Narrator_color "Ещё я понял, что всё вокруг по-настоящему живое."
    Narrator_color "Услышал, как стонет под снегом сухая трава; увидел, что у деревьев и звёзд есть лица. Деревья ухмылялись, а звёзды корчились в страхе."

    window hide
    show day3_jump_sky_moon face with Dissolve(1.5)
    window auto

    Narrator_color "«{i}Правильно! Бойтесь! Я допрыгну до вас и…{/i}»"
    Narrator_color "Я щёлкнул зубами. Затем закричал ликующе и прыгнул одновременно с лисой."
    play test_two"voice/anton/3day/155 Ha.ogg"
    window hide
    play sound "sounds/sfx_girl_hit.ogg"

    scene day3_jump_second:
        subpixel True
        align (.5,.5)
        zoom 1.
        easein_quad 2. zoom (.55 - .015)
        block:
            ease 3. zoom .55 + .015
            ease 3. zoom .55 - .015
            repeat

    show day3_jump_snow:
        alpha 0
        2.
        linear 1.5 alpha 1

    show day3_jump_air_fox:
        animation
        subpixel True
        align (.75, 1.)
        xoffset 200
        zoom .80
        easein_quad 2.8 zoom .98
        block:
            ease 2.1 zoom .98
            ease 2.1 zoom 1.01
            repeat

    pause 2.
    window auto


    Narrator_color "Мы полетели выше самых высоких сосен, и застыли в воздухе."
    Narrator_color "Я закружился, Алиса закружилась в такт."
    Narrator_color "Я знал, что она улыбается, и улыбался сам."
    Narrator_color "А флейта всё играла и играла, унося нас ввысь."
    stop music fadeout 8

label end_day_03_titr():


    jump dev_day3_end_titr.end
    label dev_day3_end_titr:
        $ ROUTE_FOX = False
        $ ROUTE_POLINA = False
        $ ROUTE_SOLO = False
        menu:
            "Выбери рут"
            "Полина":
                $ ROUTE_POLINA = True
                $ Flags.Raise("day2 polina")
            "Лиса":
                $ ROUTE_FOX = True
                $ Flags.Raise("day2 fox")
            "Маска":
                $ ROUTE_SOLO = True
                $ Flags.Raise("mask")
        label dev_day3_end_titr.end:


    show Veko_01:
        xpos 0
        ypos -1080
        alpha 0.0
        linear 1.0 xpos 0 ypos -540 alpha 1.0
    show Veko_02:
        xpos 0
        ypos 1080
        alpha 0.0
        linear 1.0 xpos 0 ypos 0 alpha 1.0
    show bg_black:
        alpha 0.0
        pause 0.5
        linear 0.5 alpha 1.0

    pause 1.

    show day3_jump_revert behind day3_jump_snow:
        subpixel True
        align (.5,.5)
        zoom (.55 - .015)
        block:
            ease 3. zoom .55 + .015
            ease 3. zoom .55 - .015
            repeat

    show day3_jump_air_fox_revert behind Veko_01:
        subpixel True
        align (.75, 1.)
        xoffset 200
        zoom .98
        block:
            ease 2.1 zoom .98
            ease 2.1 zoom 1.01
            repeat

    hide Veko_01
    hide Veko_02
    hide bg_black
    show day3_jump_air_fox:
        animation
        alpha 0
    show Veko_01:
        xpos 0
        ypos -540
        linear 1.0 xpos 0 ypos -1500 alpha 0.0
    show Veko_02:
        xpos 0
        ypos 0
        linear 1.0 xpos 0 ypos 1010 alpha 0.0

    show bg_black:
        .25
        linear 0.5 alpha 0.0

    if ROUTE_FOX:
        $ story_manager.MarkEvent(("day3", "scene24a"))
        voice "voice/romka/3day/67 Ti.ogg"
        Rom "Ты чё, опять в облаках витаешь?"
        $ music_during_lines = 1.0
        stop test_two fadeout 2
    else:


        $ story_manager.MarkEvent(("day3", "scene24b"))
        voice "voice/Polina/3day/108 E.ogg"
        Pol "Эй, тебя что, заколдовали?"
        $ music_during_lines = 1.0
        stop test_two fadeout 3

    hide Veko_01
    hide Veko_02
    hide bg_black
    show Veko_01:
        xpos 0
        ypos -1080
        alpha 0.0
        linear 1.0 xpos 0 ypos -540 alpha 1.0
    show Veko_02:
        xpos 0
        ypos 1080
        alpha 0.0
        linear 1.0 xpos 0 ypos 0 alpha 1.0
    show bg_black:
        alpha 0.0
        pause 0.5
        linear 0.5 alpha 1.0

    pause 1.

    scene day3_end_class_bg:
        xalign 1.

    if ROUTE_FOX:
        show Romka Angry b_day 001 happy ahead 01:
            xzoom -1
            xoffset -100
    else:
        show Polina Front b_day 01 norm ahead 03:
            xzoom -1
            xoffset -100
            yoffset 10

    show Veko_01:
        xpos 0
        ypos -540
        linear 1.0 xpos 0 ypos -1500 alpha 0.0
    show Veko_02:
        xpos 0
        ypos 0
        linear 1.0 xpos 0 ypos 1010 alpha 0.0

    show bg_black:
        .25
        linear 0.5 alpha 0.0
    play music2 "music/33_Symphony Of Extinct Lights.ogg" fadein 1

    if ROUTE_FOX:
        "«С вами полетаешь», — сонно подумал я, отклеивая подбородок от парты."
    else:

        "«Расколдовали», — сонно подумал я, отклеивая подбородок от парты."

    scene ant_clas_fon:
        align (.5,.5)
        zoom 1.3
    show day3_ant_clas_shadow 1:
        align (.5,.5)
    show day3_ant_clas_anton 1:
        align (.5,.5)

    if ROUTE_FOX:
        show day3_ant_clas_romka:
            align (1., 1.)
    else:
        show day3_ant_clas_polina:
            align (1., 1.)

    with Dissolve(.5)
    "Мышцы слегка ныли, но это было приятное чувство."

    scene fon_day_03_end with Dissolve(0.12)
    "Все отчего-то вновь слонялись по классу, передавали друг другу записки, шушукались."
    "Их физиономии казались выцветшими масками, блёклыми и скучными."

    scene ant_clas_fon:
        align (.5,.5)
        zoom 1.3
    show day3_ant_clas_shadow 1:
        align (.5,.5)
    show day3_ant_clas_anton 2:
        align (.5,.5)

    if ROUTE_FOX:
        show day3_ant_clas_romka:
            align (1., 1.)
    else:
        show day3_ant_clas_polina:
            align (1., 1.)

    with Dissolve(.5)

    play test_one "voice/anton/3day/1Zev.ogg"
    "Я зевнул, вспоминая, как парил высоко над лесом, а рядом смеялась Алиса и крепко сжимала мою ладонь."
    "Возможно, — и почти наверняка, — это был сон."
    "Потому что из лесу я не возвращался, а проснулся дома в кровати обыкновенным утром с чаем и таблетками."

    scene day3_end_class_miss with Dissolve(.5)
    "Но меня мало тревожило разумное объяснение ночным танцам."
    "Куда важнее было чувство полёта."

    scene day3_end_class_bg:
        xalign 1.

    if ROUTE_FOX:
        show Romka Angry b_day 01 happy ahead 01:
            xzoom -1
            xoffset -100
    else:

        show Polina Front b_day 01 norm ahead 01:
            xzoom -1
            xoffset -100
            yoffset 10

    with Dissolve(.5)

    "Знание о том, каково висеть над пиками величественных сосен и скалиться на луну."
    stop music2 fadeout 2.5

    if ROUTE_FOX:
        voice "voice/anton/3day/2. Nu.ogg"
        Ant "Ну чего?"

        show Romka Angry b_day 01 happy ahead 02 with Dissolve(.2)
        voice "voice/romka/3day/68 Cho.ogg"
        Rom "Чего-чего... Пока ты носом клевал, Катька пропала."
        play test_one "sounds/hit-chord-3.ogg"

        window hide
        scene day3_end_class_bg:
            xalign 1.
            1.
            linear .5 xalign 0.

        show Romka Angry b_day 001 happy ahead 01:
            xzoom -1
            xoffset -100
            1.
            linear .5 xoffset 700
        with Dissolve(.2)

        pause 2.
        window show
        "Сон как рукой сняло. Я недоверчиво нахмурился."
    else:

        voice "voice/anton/3day/7. Pr.ogg"
        Ant "Прости, задумался."
        show Polina Front b_day 01 sad ahead 02 with Dissolve(.2)
        voice "voice/Polina/3day/109 S.ogg"
        Pol "Слышал уже про Катю?"
        show Polina Front b_day 01 sad ahead 03 with Dissolve(.2)
        voice "voice/anton/3day/6. A.ogg"
        Ant "А?"
        play test_one "sounds/hit-chord-3.ogg"

        window hide
        scene day3_end_class_bg:
            xalign 1.
            1.
            linear .5 xalign 0.

        show Polina Front b_day 01 sad ahead 03:
            xzoom -1
            xoffset -100
            yoffset 10
            1.
            linear .5 xoffset 700
        with Dissolve(.2)

        pause 2.
        window show

        "Я бросил взгляд на пустующее место впереди."
        play sound "sounds/steps/Kait_stop.ogg"

        scene day3_end_class_bg:
            xalign 0.
        show Polina Front b_day 01 sad ahead 02:
            xzoom -1
            xoffset 700
            parallel:
                linear .25 xoffset 575
            parallel:
                linear .1 yoffset 0
                linear .15 yoffset 10
        voice "voice/Polina/3day/110.ogg"
        Pol "Катя пропала."
        show Polina Front b_day 01 sad ahead 03 with Dissolve(.2)
        "Сон как рукой сняло. Я недоверчиво нахмурился."

    $ delay_dt = .5
    scene ant_clas_fon:
        subpixel True
        align (.5,.5)
        zoom 1.3
        .5
        easeout delay_dt zoom 1.0
    show day3_ant_clas_shadow 2:
        subpixel True
        align (.5,.5)
        .5
        easeout delay_dt zoom .85
    show day3_ant_clas_anton 3:
        subpixel True
        align (.5,.5)
        .5
        easeout delay_dt zoom 1.3
    play test_five "music/Anton Zoom.ogg"
    voice "voice/anton/3day/3 Kak.ogg"

    Ant "Как пропала? Быть не может!"
    stop test_five fadeout 1
    play test_six "music/Kate Zoom.ogg"




    window hide
    if ROUTE_SOLO:
        scene Kate_end_start_solo with Dissolve(.5)
        pause 1
        scene Kate_end_solo
        with Dissolve(.5)
        pause 3
    else:
        scene Kate_end_start with Dissolve(.5)
        pause 1
        scene Kate_end
        with Dissolve(.5)
        pause 3

    if true_detective_count3 == 3:
        $ achievement_grant("ach_detective_3")
        $ persistent.has_d3_detective = True

    scene black with Dissolve(1.5)


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

    python:
        story_manager.width = 1920
        story_manager.height = 10935 +600
        story_manager.day_code = "day3"

    show screen StoryExplainerDCut_Day3(story_manager) with Dissolve(1.5)
    $ ui.interact()

    show screen StoryExplainerDCut_Hider
    with Dissolve(1.5)
    jump d4_begin



screen StoryExplainerDCut_Day3(story_manager):
    tag flowchart

    $ story_manager.story_db = story_so_far_dcut

    $ y_val = IncrementalInt(300)

    default view_x = ui.adjustment(value = 0, range=1920)
    default view_y = ui.adjustment(value = 0, range=story_manager.height)
    default sub_view_x = ui.adjustment(value = 0, range=1920)
    default sub_view_y = ui.adjustment(value = 0, range=story_manager.height*flowchart_bg_ratio)
    default sub_view_x2 = ui.adjustment(value = 0, range=1920)
    default sub_view_y2 = ui.adjustment(value = 0, range=story_manager.height*flowchart_dust_ratio)


    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (1920, story_manager.height*flowchart_bg_ratio)

        yadjustment sub_view_y

        add Widespan_Dependant(None, sub_view_y, None, view_y)
        add "story_bg_1"


    add "story_bg_3"


    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (1920, story_manager.height)
        draggable True
        pagekeys True

        xadjustment view_x
        yadjustment view_y


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene1", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175)) at arrow_valid


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la classroom", (960 - (75+200), y_val(175+85*2+75+25)), (75*2 + 400, 175+85*2+75+25), ("projector", "esenin", "box"))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175)) at arrow_valid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene2", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175)) at arrow_valid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene3", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175)) at arrow_valid


        use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game case", (960 - (75+200), y_val(175+85*2+75+25)), (75*2 + 400, 175+85*2+75+25), ("hit0", "hit1", "hit2"))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175)) at arrow_valid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene4", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "photorobot", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "photorobot", "silent")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "photorobot", "tell")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "photorobot", (960, y_val(0)), "silent")

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "photorobot", (960, y_val(0)), "tell")

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960+250, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "photorobot", "tell")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960-250, y_val(0)) yzoom 6.5:
            if story_manager.IsMarkedLocal((story_manager.day_code, "photorobot", "silent")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game photorobot", (960 - (75+200) +250, y_val(175+85*5+75+25)), (75*2 + 400, 175+85*5+75+25), ("fox", "witness", "trudovic", "letov", "tsoi", "bodrov"))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960+250, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "game photorobot", "witness")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (1., .0) pos (960+250, y_val(0)) xzoom 1.25:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "game photorobot", "witness")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_wrong", (960-250, y_val(0)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene_witness", (960+250, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960-250, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene_wrong")) and story_manager.IsMarkedLocal((story_manager.day_code, "scene5a")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960+250, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene_witness")) and story_manager.IsMarkedLocal((story_manager.day_code, "scene5b")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (1., .0) pos (960+250, y_val(0)) xzoom 1.25:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene_witness")) and story_manager.IsMarkedLocal((story_manager.day_code, "scene5a")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960-250, y_val(0)) xzoom 1.25:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene_wrong")) and story_manager.IsMarkedLocal((story_manager.day_code, "scene5b")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene5a", (960-250, y_val(0)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene5b", (960+250, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960+250, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene5b")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960-250, y_val(0)) yzoom 6.5:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene5a")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene6", (960+250, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_left" anchor (1., .0) pos (960+250, y_val(0)) xzoom 0.60:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "game suefa")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960+250, y_val(0)) xzoom 0.65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "game suefa")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(125)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(0)) yzoom 3.5:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "game suefa")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(50)


        use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game suefa", (960 - (75+200) +250 +250, y_val(175+85*1+75+25)), (75*2 + 400, 175+85*1+75+25), ("lose", "win"))



        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom 0.65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene5a")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom 1.25:
            if story_manager.IsMarkedLocal((story_manager.day_code, "game suefa")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene7", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(0)) yzoom 7.0:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "scene8")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom 0.75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene8")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene8", (960-300, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960-300, y_val(175)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene8")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "amulet", (960-300, y_val(125)))


        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "amulet", (960-300, y_val(100)), "yes")

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "amulet", (960-300, y_val(100)), "no")

        add "flowchart_arrow_right" anchor (0., .0) pos (960-300, y_val(175)) xzoom 0.75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene8")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene9", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene10", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene11", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene12", (960-225, y_val(75)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene13a", (960-75, y_val(75)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene13b", (960+75, y_val(75)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene13c", (960+225, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene14", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene15", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene16a", (960-150, y_val(75)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene16b", (960, y_val(75)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene16c", (960+150, y_val(75)))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_GameSegment(story_manager, story_manager.day_code, "game goosehunt", (960 - (75+200), y_val(175+85*1+75+25)), (75*2 + 400, 175+85*1+75+25), ("dominate", "comfort"))

        add "flowchart_arrow_down" anchor (0., .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene17", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene18a")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene18b")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene18a", (960-250, y_val(0)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene18b", (960+250, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960-250, y_val(0)) yzoom 4.5:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene18a")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960+250, y_val(0)) yzoom 4.5:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "phonecall")) and story_manager.IsMarkedLocal((story_manager.day_code, "scene18b")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960+250, y_val(0)) xzoom 0.65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "phonecall")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "phonecall", (960+525, y_val(125)))


        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "phonecall", (960+525, y_val(100)), "betray")

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "phonecall", (960+525, y_val(100)), "voltron")

        add "flowchart_arrow_left" anchor (1., .0) pos (960+525, y_val(0)) xzoom 0.65

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene19", (960+250, y_val(0)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene20", (960-250, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene19")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene20")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene21", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene22", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene23", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene24b")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene24a")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene24a", (960+250, y_val(0)))

        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene24b", (960-250, y_val(0)))

        $ y_val(75)


    viewport:
        align (.0, .5)
        xysize (1960, 1080)
        child_size (1920, story_manager.height*flowchart_dust_ratio)

        yadjustment sub_view_y2

        add Widespan_Dependant(None, sub_view_y2, None, view_y)
        add "story_bg_2"


    use StoryExplainer_UI(story_manager)

    use StoryExplainer_Selector(story_manager)


    if config.developer:
        frame:
            align (0., 0.)
            text "y_val: " + str(y_val(0)) color "#000"
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
