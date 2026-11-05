


label day_2:
    $ story_manager.MarkEvent(("day2", "scene0"))

    play fon "sounds/fon/skrip1.ogg" fadein 5.0
    scene black
    window show

    "И всё-таки он настал."
    "Первый учебный день, которого я боялся больше всего."

    play music "music/9_Nikita Kryukov - the Obscurity.ogg"  fadein 5.0

    window hide

    pause 1.

    scene bg_logo3
    with Dissolve(1.0)

    show screen center_text(_("Эпизод II: Время поиграть")) with Dissolve(.5)

    pause 1.

    show screen day5_continue_button(d5_logo_begin)
    with Dissolve(.5)
    $ ui.interact()

    hide screen day5_continue_button
    with Dissolve(.5)

    pause 1.

    hide screen center_text with Dissolve(.5)

    scene black with Dissolve(1.)

    scene day1_kovai_0 with Dissolve(2.0)

    $ story_manager.MarkEvent(("day2", "scene1"))

    window show
    "Новая школа и учителя, а главное — новые одноклассники, с которыми мне всегда было сложно найти общий язык."

    scene bg_room_night1 with Dissolve(0.5)
    "Как и большинству очкариков, наверное."

    scene bg room_night_ZOOM
    with Dissolve(.5)
    "Я пересилил себя и выбрался из тёплой постели."

    show room_night_zoom_door 1
    pause 0.1
    show room_night_zoom_door 2
    pause 0.1
    show room_night_zoom_door 3
    pause 0.5
    hide room_night_zoom_door
    show door open_door1
    pause .1 
    show door open_door2
    "В старую школу меня обычно провожал папа, но этим утром из родительской спальни не доносилось ни звука."

    show layer master:
        subpixel True
        align (.25, .5)
        zoom 1.0
        easeout 1.0 zoom 1.15
    pause 0.5

    scene d4_hall_corridor d2:
        xalign 1.
    show layer master:
        align (.85, .75)
        zoom 2.25
        easein .5 zoom 2.10
    show bg_black:
        alpha .3
    with Dissolve(.5)
    "Неужели проспали?"

    play test_two "sounds/steps/Anton-steps-steal-1.ogg"

    show d4_hall_corridor d2:
        ease 12 xalign .0
    show layer master:
        align (.85, .75)
        zoom 2.10
        ease 12 zoom 1.0
    "Оно и к лучшему – не хотелось в первый же день прослыть папенькиным сынком."
    "Наверное, родители лежат сейчас под одеялом и видят сны, где всё по-прежнему — легко и понятно."
    "Хорошие сны, пусть и лживые."

    scene day2_stairs_1:
        subpixel True
        xalign 1.
        easein 4. xalign 0.
    show day2_stairs_2:
        subpixel True
        xalign 1.
        easein 4. xalign -1.
    with Dissolve(.5)
    "Чтобы никого не разбудить, особенно мирно спящую Олю, я прокрался на первый этаж."

    scene d5_mercy_olyafall_bg with Dissolve(0.5)
    "Старался наступать на середину половицы."

    scene d5_zh_hall_closed with Dissolve(.5)
    "Так я забавлялся ещё в прошлой квартире: если ступня попадёт на щель между досками — считай, сгорел."

    scene bg door_night with Dissolve(0.5)
    "Стрелки часов нарезали время."
    "«{i}Стоит поторопиться. Скорее, скорее!{/i}»"
    "Слишком быстро — я сделал круг по прихожей."

    scene d5_monchoice_bg with Dissolve(.5)
    "Лава кипела в зазорах между половицами."

    show layer master:
        subpixel True
        align (.45, .15)
        zoom 1.0
        ease 1. zoom 1.10
        .5
        ease 1. zoom 1.21
        .5
        ease 1. zoom 1.33
        .5
        ease 1. zoom 1.46
        .5
        ease 1. zoom 1.60
    "Надо идти аккуратно. Выжить любой ценой."
    "Прыг, прыг — словно жаба по кочкам, словно трусливый зайка в роще, кишащей волками."


    play test_two "sounds/steps/Anton-steps-in-1.ogg"





    scene bg kitchen_dark1
    if not Flags.Has("kalendar"):
        show kalendar_07_dark
    with Dissolve(0.5)

    play test_one "sounds/sfx_eating_sandwich.ogg"

    "На кухне я сделал бутерброд, с трудом протолкнул его в желудок и запил холодным чаем."
    "Аппетит был как у человека, идущего на гильотину."
    "Я потупился и увидел, что правая ступня стоит сразу на двух досках."
    "Сгорел."
    "Я переставил ногу."
    "В животе закопошились мерзкие змеёныши — страх перед тычками и гадкими прозвищами."
    "Часы щёлкнули стрелками."
    "Пора..."


    play test_two "sounds/steps/Anton-steps-in-1.ogg"
    scene bg door_night with Dissolve(0.5)

    "Раннее утро было по-зимнему тёмным."
    "Мрак из домов здесь никогда не уходил до конца."

    play test_one "sounds/sfx_put_on_clothes.ogg"

    "Я долго зашнуровывал ботинки, застёгивал пуховик на все пуговицы — до последнего оттягивал неприятный выход в полутьму, в тревожную неизвестность."

    show layer master:
        align (.75, .4)
        zoom 1.5
    with Dissolve(.5)
    "Протёр очки на удачу, хотя и не припомню случая, когда эти толстенные стекляшки принесли бы мне везение."

    window hide
    play test_one "sounds/Door_open.ogg"
    play fon "sounds/fon/crow_wind.ogg" fadein 1.0
    scene bg door_open_night
    show layer master:
        subpixel True
        align (.75, .4)
        zoom 1.5
    with Dissolve(0.5)
    pause 0.5
    show layer master:
        subpixel True
        align (.75, .4)
        zoom 1.5
        easeout 1.5 zoom 2.25
    $ renpy.pause(1.0)
    stop music fadeout 4.0


    play fon "sounds/fon/wind.ogg" fadein 2.0
    play test_one "sounds/Door_close.ogg"
    scene bg house_night1 with Dissolve(0.5)
    window show

    "Небо напоминало огромный кровоподтёк."

    play test_two "sounds/fon/owls-1.ogg"  fadein 5.0 loop

    "На востоке громоздилась и разбухала чёрная туча."
    "Слизывала звёзды и гасила рассветное зарево."
    "Тьма облепила деревья."
    "Осторожные птичьи вскрики путались в зарослях."

    play test_one "sounds/lock-door-1.ogg"
    scene d5_guests_treshold_l1:
        align (.5, .5)
    show d5_guests_treshold_l2:
        align (.5, .5)
    show layer master:
        subpixel True
        align (.5, .5)
        zoom 1.05
    with Dissolve(.5)
    "Я запер входную дверь длинным ключом, который носил на шее."
    "Родители обязали носить меня шнурок-петлю, опасаясь, что я, растяпа, потеряю ключ."

    scene d3_outside_guys_bg
    show d4_fence
    with Dissolve(.5)
    "Ветер свистел за калиткой, приглашал в новую жизнь, навстречу сомнительным приключениям."

    play test_one "sounds/steps_snow001.ogg"

    scene d3_outside_guys_bg:
        subpixel True
        align (.5, .5)
        ease 5 zoom 1.5
    show d4_fence:
        subpixel True
        align (.5, .5)
        ease 5 zoom 2.25
    "И, будто старый приятель, увязался за мной, подталкивая в спину."
    "Тени сосен раскинулись, поглотив треть пустыря."


    play music "music/21_He is near.ogg"  fadein 5.0
    scene bg_forest0_long_dark_full:
        subpixel True
        xalign 0.
        ease 15 xalign 1.
    with Dissolve(.5)
    play test_one "sounds/steps_snow001.ogg"

    "На подходе к лесу я спрятал нос под воротник."
    "Весь нахохлился, ссутулился, вклиниваясь в просеку."
    "Высокие деревья обступили тропинку."
    "Под ногами шуршало снежное покрывало, а сверху ветви сплетались, образуя полог, отрезая меня от жалкого мерцания звёзд."
    "Ночь и не думала убираться из чащобы."
    "В темноте деревья походили на косматых старух и пахли могильной землёй."
    "Стволы превращались в потрескавшиеся морщинистые морды со ртами-дуплами."
    "Зазеваешься — и замшелые ведьмы утащат в лесные дебри."
    "Будут потом родители бродить по лесам, голосить: «Антон! Антон!»"
    "Мёртвые не отвечают живым."

    window hide
    play test_seven "sounds/hit-chord-2.ogg"
    show memory_scrimer_grandmother
    $ renpy.pause(1.0, hard=True)
    hide memory_scrimer_grandmother
    window show

    "Или отвечают?"

    $ SetParSpeed(30)
    window hide
    play test_one "sounds/flashback.ogg"
    show bg_white with Dissolve(0.1)
    show gohome01_dark_reverse
    show gohome01_1_dark_reverse
    show gohome02_dark_reverse
    show gohome02_1_dark_reverse
    show gohome03_dark_reverse
    show gohome03_1_dark_reverse
    show gohome04_dark_reverse
    show gohome04_1_dark_reverse
    show gohome05_dark_reverse
    show gohome05_1_dark_reverse
    show memory_scrimer1
    $ renpy.pause(1.2, hard=True)
    hide memory_scrimer1
    hide bg_white with Dissolve(0.1)
    window show

    "Паника разрасталась в груди."

    stop fon fadeout 3.0
    stop music fadeout 5.0
    stop test_two fadeout 3.0

    play test_one "sounds/loop_footsteps_1.ogg" loop

    "Я готов был явиться в школу хоть у папы на руках, только бы не видеть, как тьма, словно чёрное тесто, поднимается в оврагах."

    play test_three "sounds/Bush_rustle.ogg"
    play test_four "sounds/Special_SFXs.ogg"

    "Я обернулся — показалось, что кто-то нырнул за кусты."















    play test_two "sounds/loop_footsteps_2.ogg" loop

    play fon "sounds/Real_wind.ogg"

    "Стоило мне ускорить шаг, как позади заскрипел снег."

    play test_five "sounds/Trees_SFXs_2.ogg"

    "Лес вздохнул гигантскими лёгкими. Затрещал бурелом."
    "Ветер, птицы — всё осталось в поле, шум леса был единственным спутником."
    "Я шёл, вслушивался и всё сильнее ощущал незримое присутствие."
    "Будто кто-то следовал за мной по пятам, стараясь попадать в такт моих шагов."

    scene gohome_dark_stop
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.1)
    play test_one "sounds/neck crunch-1.ogg"
    stop test_two fadeout 3.5
    play test_four "sounds/cymb-roll-3.ogg"

    "Я оглянулся так резко, что хрустнула шея." with hpunch

    scene scare_00 with Dissolve(0.1)
    window hide
    $ renpy.pause(2.0)
    window show

    "Узкая тропинка позади меня терялась в темноте."

    play test_five "sounds/Trees_SFXs_1.ogg"

    "Сучья перехлёстывались над нерукотворным туннелем."

    voice "voice/anton/2day/Esttzdes.ogg"
    Ant "Есть здесь кто?"

    "Вопрос сорвался с губ и растворился в несмолкаемом скрипе деревянных идолов, этих древних сосен."

    play test_three "sounds/Bush_rustle.ogg"

    "И взбрело мне в голову идти через лес одному!"
    "Наверное, я спятил или..."
    "...кто-то нарочно выманил меня из дома."
    "Даруя слабую надежду, вдали замаячили огни."
    "Просёлочная дорога!"

    $ SetParSpeed(3)
    scene black
    show gohome01_dark_reverse
    show gohome01_1_dark_reverse
    show gohome02_dark_reverse
    show gohome02_1_dark_reverse
    show gohome03_dark_reverse
    show gohome03_1_dark_reverse
    show gohome04_dark_reverse
    show gohome04_1_dark_reverse
    show gohome05_dark_reverse
    show gohome05_1_dark_reverse
    with Dissolve(0.2)
    stop music fadeout 7.0
    play test_one "sounds/steps/loop_snow_footsteps.ogg"

    "Со всех ног я бросился туда, будто боялся, что тропинка сомкнётся, когтистые лапы схватят меня за плечи, повернут и заставят взглянуть в лицо голодным обитателям леса."

    play music2 "music/2_Anxiety.ogg"  fadein 2.0

    stop test_four fadeout 3.0


    "Но никто меня не задержал."
    "Не веря в удачу, я буквально вылетел на трухлявый мост."


    scene bg bridge with Dissolve(0.3)
    show snow_night_0
    play test_one "sounds/bridge-steps-in-1.ogg"

    "Ручей, студёный и чёрный, будто смола, омывал опоры."
    "Я упёрся ладонями в колени и исподлобья глянул на лес."
    "Фыркнул, выравнивая дыхание."
    "Чащоба притворялась спящей. Миролюбивой. Неживой."

    play test_one "sounds/bridge-steps-out-1.ogg"

    "Остальной путь пролегал по заснеженной дороге, освещённой редкими фонарями."


    scene bg road_night with Dissolve(0.3)

    "Я отогнал дурные мысли и постарался как можно быстрее перебегать от одного круга света к другому, под защиту электричества."

    $ add_text_to_dictionary(13)

    "Как в детской {u}забаве{/u}, где первому нужно закричать: «Я в домике!»"

    stop music2 fadeout 3.0

    "Только домики эти были хрупкими, а за их стенами непрерывно двигалась тьма."

    play music "music/Garazh_part1.ogg"  fadein 3.0
    scene bg Fox_road1 with Dissolve(0.3)
    $ persistent.animal_unlock[1] = True

    play sound "sounds/dog-eats-3.ogg" fadein 1.5 loop
    $ renpy.sound.set_volume(0.4, delay=0, channel='sound')

    $ story_manager.MarkEvent(("day2", "scene2"))

    "Вдруг я заметил нечто до жути странное."
    "Там, куда не доставал свет покосившегося фонаря, ожила и утробно зарычала сгорбленная лохматая тень."

    window auto
    scene bg Fox_road2
    show bg_Fox_road3
    with Dissolve(0.3)
    $ renpy.sound.set_volume(1.0, delay=0, channel='sound')
    $ renpy.pause(3.0)

    "Её черты будто отторгали свет, а неестественная поза внушала страх."
    "Я выпучил глаза и заморгал, чтобы прогнать наваждение."

    scene bg road_night
    show Fox Normal m_dark 00
    with Dissolve(0.3)

    stop sound fadeout 0.8

    play test_one "sounds/growl2.ogg" volume 0.5 loop

    "Но тень всё ещё была там и даже приблизилась."
    "Ужас скрутил мои кишки. Я попятился и чуть не упал в сугроб."

    "Чучело же выпрямилось во весь рост и спросило ласковым голосом:"

    $ music_during_lines = 0.5
    voice "voice/Alisa/Alisa2day/01 Chego krad.ogg"
    Noname "Чего крадёшься? Душу мою украсть хочешь?"

    "От удивления я лишился дара речи."
    "Кто может говорить со мной таким шёлковым голоском здесь, между лесом и дремлющим посёлком?"

    voice "voice/Alisa/Alisa2day/02 Chego molch.ogg"
    Noname "Чего молчишь, несмышлёныш?"

    voice "voice/Alisa/Alisa2day/03 Yazik.ogg"
    Noname "Язык вырвали?"

    stop test_one fadeout 4

    voice "voice/Alisa/Alisa2day/04 Slushai.ogg"
    Noname "Слу-у-у-шай, а я тебе ещё и нос откушу!"

    voice "voice/Alisa/Alisa2day/05 Budesh.ogg"
    Noname "Будешь знать, как совать его в чужие дела!"
    $ music_during_lines = 1.0

    stop music fadeout 4.0

    "Судя по голосу и фигуре, это была девочка."
    "Но не успел я одёрнуть себя — «Дурак! Испугался девчонки!» — как различил под капюшоном распахнутый рот и что-то опасно блеснувшее в его широкой щели."

    play music "music/24_Fox.ogg" fadein 5.0

    "Я обомлел."

    stop test_one fadeout 1.5
    window hide
    hide Fox
    show Fox Normal m_night 00 good dark
    with Dissolve(3.5)
    window show

    "Из пещеры капюшона на меня таращилась пугающе живая лисья морда."

    stop fon fadeout 5.0

    "Только вот пасть её не шевелилась, а глаза не моргали."

    show Fox Fullface m_night 00 good dark
    with Dissolve(0.3)

    "Маска!"
    "Обыкновенная девочка! Просто маску лисы напялила."
    "По крайней мере, я хотел так думать."
    "Как это случается после резкого испуга, я нервно заулыбался."

    voice "voice/anton/2day/01 A ya.ogg"
    Ant "А я..."

    voice "voice/anton/2day/01.2 Prosto v shkolu.ogg"
    Ant "Просто в школу иду, а тут... ты."

    voice "voice/Alisa/Alisa2day/06 Chto ya.ogg"
    Fox "Что я?"

    voice "voice/Alisa/Alisa2day/07 Nikogda ne videl.ogg"
    Fox "Никогда не видел, как лиса собаку кормит?"

    scene bg dog_01
    with Dissolve(0.3)
    play test_one "sounds/sfx_dog_breathing_2.ogg" loop

    "Действительно, возле ног девочки-лисицы крутилась маленькая собачонка. Кажется, одна из дворняг, что гнались за мной вчера."

    voice "voice/anton/2day/002. Izvinite.ogg"
    Ant "Извини, я не хотел..."

    play test_two "sounds/sfx_dog_calling_one.ogg"

    "Услышав мой голос, собака тявкнула, прижала уши, затем принюхалась и завиляла хвостом."

    stop test_one fadeout 1.5

    "Наверное, от меня пахло колбасой, что я ел на завтрак."

    scene bg road_night
    show Fox Fullface m_night 00 good dark
    with Dissolve(0.3)

    "Я смотрел то на моську, то на девочку. Она уже не казалась страшной — только странной."

    show Fox Nice m_night 00 good dark
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/08 Znachit.ogg"
    Fox "Значит, не хотел. Ну-ну..."

    voice "voice/Alisa/Alisa2day/09 Kak tebya zovut.ogg"
    Fox "Как тебя зовут?"

    voice "voice/anton/2day/03 Menya Anton.ogg"
    Ant "Меня — Антон..."

    voice "voice/anton/2day/03.2 A tebya.ogg"
    Ant "А тебя?"

    show Fox Nice m_night 00 good dark_to_ahead

    voice "voice/Alisa/Alisa2day/10 A menya net.ogg"
    Fox "А меня — нет!"

    show Fox Nice m_night 00 good ahead:
        yoffset 0
        block:
            linear 0.15 yoffset 5
            linear 0.15 yoffset 0
            repeat

    voice "voice/Alisa/Alisa2day/11 A menya net.ogg"
    Fox "Хи-хи-хи!"

    show Fox Nice m_night 00 good ahead:
        yalign 1.0

    "Чудная какая-то. С приветом."
    "Зато голос приятный."
    "Оторопь сменилась радостью: незнакомка явно была человеком, хоть и со странностями."
    "Ещё я немного злился на себя."
    "Эта лисичка-сестричка гуляет в сумраке как ни в чём не бывало, а я вздрагиваю от малейшего шороха."
    "Можно было идти дальше, но девочка раздразнила любопытство."
    "В следующий раз спросит меня милиционер, завёл ли я знакомства на новом месте, а я ему отвечу: «Ага, с говорящей лисой!»"

    voice "voice/anton/2day/04 Ti zdes.ogg"
    Ant "Ты здесь живёшь?"

    voice "voice/anton/2day/04.2 V poselke.ogg"
    Ant "В посёлке?"

    play sound "voice/Alisa/Alisa2day/11 Lisitsa.ogg"
    play test_three "voice/Alisa/Alisa2day/Ururu.ogg"
    "Лисица хихикнула и заурчала."

    show Fox Fullface m_night 00 good ahead with Dissolve(0.3)

    "Крутанулась вокруг себя так, что подол шубки раздулся."
    stop test_three fadeout 1

    voice "voice/Alisa/Alisa2day/12 Net glupiy.ogg"
    Fox "Нет, глупый."

    voice "voice/Alisa/Alisa2day/13 Foxes ne.ogg"
    Fox "Лисы не живут в посёлках."

    voice "voice/anton/2day/005. Hochesh.ogg"
    Ant "Хочешь сказать, ты живёшь в лесу?"

    show Fox Normal m_night 00 good ahead with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/14 Iz kakoy.ogg"
    Fox "Из какой норы ты вылез?"

    voice "voice/Alisa/Alisa2day/15 Konechno lisam.ogg"
    Fox "Конечно, лисам среди людей не выжить..."

    voice "voice/Alisa/Alisa2day/16 Poka oni.ogg"
    Fox "Пока они лисы."

    "Шутки у неё тоже чудные."
    "Как и карнавальная маска... Всего лишь папье-маше с наклеенным мехом."

    scene bg_dog_02_1
    with Dissolve(0.3)

    play test_one "sounds/sfx_dog_calling_two.ogg"

    "Собака напомнила о себе звонким лаем."

    play test_one "sounds/sfx_open_bag.ogg"

    "Я отстегнул клапан рюкзака."
    "Папа иногда подбрасывал мне в рюкзак что-нибудь вкусное: печенье или яблоко, или даже мои любимые крабовые палочки."

    $ add_text_to_dictionary(12)

    "Говорил, мол, «Это тебе от {u}зайчика»{/u}."
    "Дворняга, просительно облизываясь, засеменила ко мне."
    "Лисичка явно чем-то угощала её, но, видимо, не утолила собачий голод."

    scene bg road_night
    show Fox Fullface m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/anton/2day/06 Zachem ti tak.ogg"
    Ant "Зачем ты так вырядилась с утра пораньше?"

    voice "voice/anton/2day/06.2 Na utrennik.ogg"
    Ant "На утренник идёшь?"

    stop music fadeout 4.0
    show Fox Angry m_night 00
    with Dissolve(0.3)
    play test_seven "sounds/hit-chord-3.ogg"
    play music2 "music/16_strings0.2-1.ogg" fadein 7.0

    "Незнакомка встрепенулась, сбросив с носа серебристые снежинки."
    "И будто стряхнула с себя человеческий облик..."

    "...превратившись в настоящего зверя."
    "Хитрую, быструю и опасную лису."

    play test_seven "sounds/hit-chord-2.ogg"
    show Fox Angry b_night 00
    with Dissolve(0.3)

    "Зазеваешься — полетят клочки по закоулочкам. Разорвёт, съест — и не подавится."
    "Я опешил и встал, словно загипнотизированный."

    stop music2 fadeout 4.0
    show Fox Flirt m_night 00 good dark_to_ahead:
        yoffset 0
        block:
            linear 0.15 yoffset 5
            linear 0.15 yoffset 0
            repeat
    with Dissolve(0.3)
    play music "music/24_Fox.ogg" fadein 5.0

    play test_one "voice/Alisa/Alisa2day/16 Poka ne uslishal.ogg"

    "Пока не услышал её приглушенный мелодичный смех, скрытый за образиной зверя."

    show Fox Flirt m_night 00 good dark_to_ahead:
        yalign 1.0

    voice "voice/Alisa/Alisa2day/17 Videl bi ti.ogg"
    Fox "Видел бы ты свою маску, сладенький."

    "Сла... сладенький, она сказала?"
    "Тут я засмущался. Покраснел до корней волос."
    "Однажды мы с папой видели в зоосаде лису – та была вылинявшей, серой и тощей. "
    "А эта девчонка – огненная лисичка, пушистая, как в сказках."
    "Я до сих пор шарил в рюкзаке."
    "Пальцы, искавшие еду для собаки, нащупали что-то мягкое и скомканное..."

    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/18 Nichego.ogg"
    Fox "Ничего."

    voice "voice/Alisa/Alisa2day/18 Skoro.ogg"
    Fox "Скоро проснутся настоящие звери."

    voice "voice/Alisa/Alisa2day/19 Sprosi-ka.ogg"
    Fox "Спроси-ка лучше у них, где они взяли свои человеческие лица."

    "Тень девочки плясала в свете фонаря."

    scene bg_dog_02_1
    with Dissolve(0.3)

    play test_one "sounds/sfx_dog_calling_one.ogg"

    "Собака, будто соглашаясь, одобрительно тявкнула."

    play test_one "sounds/sfx_glove_falls.ogg"

    "От неожиданности я выронил находку прямо в сугроб, толком и не разглядев её."
    "Холодный ветер тут же засыпал край снежной лунки."

    play test_one "sounds/sfx_dog_breathing.ogg"
    play test_two "sounds/sfx_dog_digging.ogg"

    "Собака, решив, что это лакомство, бросилась на раскопки."

    scene bg road_night
    show Fox Fullface m_night 00 good ahead
    with Dissolve(0.3)
    stop test_one fadeout 1.5
    stop test_two fadeout 1.0

    play sound "voice/Alisa/Alisa2day/Lisa_fir.ogg"
    "Лиса лишь фыркнула."
    "Я так оробел, что не знал куда себя деть."
    "За пределами электрического круга никак не рассветало, тьма напротив, будто бы сделалась гуще."
    "В её чернилах беспробудно дремали окрестные дома."
    "А я постарался продолжить разговор с удивительно странной незнакомкой:"

    voice "voice/anton/2day/008. Tak ti v shkolu.ogg"
    Ant "Так ты в школу идёшь?"

    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/20 Oh nu kakoi.ogg"
    Fox "Ох, ну какой же дурачок!"

    voice "voice/Alisa/Alisa2day/21 Tak nichego.ogg"
    Fox "Так ничего и не понял?"

    scene bg road_night2
    show Ant Normal b_night 00 serious ahead 01
    with Dissolve(0.5)

    "Ну вот. Хотел подружиться, а она лишь зубы скалит."
    "Ещё и обзывается."
    "Всё-таки стоило пройти мимо и не обращать внимания на чудачку с её глупой собакой."

    show Ant Normal b_night 00 serious ahead 04 with Dissolve(0.2)

    voice "voice/anton/2day/09 A chego ti.ogg"
    Ant "А ты чего обзываешься?"

    show Ant Normal b_night 00 serious ahead 02 with Dissolve(0.2)
    show Ant Normal b_night 00 serious ahead 04 with Dissolve(0.2)

    voice "voice/anton/2day/09.2 Ne hocshesh.ogg"
    Ant "Не хочешь отвечать – и пожалуйста."

    show Ant Normal b_night 00 serious ahead 02 with Dissolve(0.2)
    show Ant Normal b_night 00 serious ahead 04 with Dissolve(0.2)

    voice "voice/anton/2day/09.3 Nikto ne.ogg"
    Ant "Никто не требует."

    show Ant Normal b_night 00 serious ahead 02 with Dissolve(0.2)
    scene bg road_night
    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    "Но что-то удерживало, притягивало к тёмной фигурке."
    "Таинственный облик, томный голос с бархатисто-сладострастной ленцой."
    "Я был заинтригован и взбудоражен. Я смотрел на неё, как смотрят на пожар."

    show Fox Flirt m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/22 Da ne duysa.ogg"
    Fox "Ой, да не дуйся."

    voice "voice/Alisa/Alisa2day/23 Glyadika.ogg"
    Fox "Гляди-ка лучше."

    voice "voice/Alisa/Alisa2day/24 Ti nrav.ogg"
    Fox "Ты нравишься Жульке."

    "Собачонка разгребала снег, громко сопя и резво перебирая лапами."
    "Лисица оглянулась на окна ближайшего дома, на бревенчатый фасад в дымке. "
    "Кончик её фальшивого носа блестел в свете фонаря."

    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/25 I ne tolko.ogg"
    Fox "И не только ей."

    scene bg road_night2
    show Ant Smile b_night 00 norm ahead 01
    with Dissolve(0.5)

    "Я снова покраснел, как варёный рак."

    show Ant Smile b_night 00 norm ahead 01 with Dissolve(0.2)

    "Это она про себя или про кого-то другого?"

    hide Ant
    show Ant Smile b_night 00 norm ahead_to_aside 01
    with Dissolve(0.2)

    "Я надеялся, что в полумраке девочка не заметит моё смущение."
    play sound "voice/anton/2day/010. Prezde chem sprosit.ogg"
    "Прежде чем спросить, я откашлялся."

    hide Ant
    show Ant Smile b_night 00 norm aside_to_ahead 07
    with Dissolve(0.2)

    voice "voice/anton/2day/11.2 A komu eshe ya.ogg"
    Ant "А кому ещё я нравлюсь?"

    hide Ant
    show Ant Smile b_night 00 norm ahead_to_aside 05
    with Dissolve(0.2)

    "Я ждал, считая удары сердца."

    scene bg road_night
    show Fox Normal m_night 00 good ahead
    with Dissolve(0.5)

    "Лиса не ответила."
    "Её лукавый взгляд бегал по морозным рисункам чужих окон."
    "Читал их как стеклянную книгу."
    "Интересно, что она видит в январских узорах?"

    scene bg varishka2 with Dissolve(1.0)

    "Дворняга закончила копошиться в снегу."

    play test_one "sounds/sfx_dog_comes.ogg"

    "Засеменила ко мне, сжимая в пасти находку."

    stop music fadeout 2.0
    play music2 "music/Menu_Tiny_Bunny.ogg" volume 0.7 fadein 2.0
    play test_one "sounds/sfx_glove_falls.ogg"

    "Варежка."
    "Неужели та самая, что я нашёл в лесу?"
    "Что она здесь делает?"
    "Но, приглядевшись, я сразу понял, что это всего лишь моя рукавичка."
    "Может, мама подсунула мне их, пока я спал?"
    "Я тут же вспомнил о пропавшем мальчике."

    scene bg road_night
    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    $ music_during_lines = 0.6
    voice "voice/anton/2day/012. Hey ti zhaesh.ogg"
    Ant "Эй, ты знаешь что-нибудь про Вову?"

    "Перед глазами встала картина: пляшущие силуэты на пустыре."

    window hide
    play test_one "sounds/flashback.ogg"
    show bg_white with Dissolve(0.1)
    show memory_scrimer1
    $ renpy.pause(1.2, hard=True)
    hide memory_scrimer1
    hide bg_white with Dissolve(0.1)
    window show

    "Танцы в ночь, когда исчез Вова."
    "Мальчик, чья находка сулит мне большую награду и даже может спасти мою семью."
    "Я вспомнил свой день рождения, когда родители обещали отвезти меня с сестрой в Париж, в Диснейленд..."
    "...но вместо долгожданного подарка родители с нескрываемым смущением преподнесли мне обычный тетрис."
    "Как я тогда плакал и требовал, чтобы меня взяли на обещанные аттракционы!"
    "Именно тогда мама с папой впервые поссорились. Мой каприз надломил их отношения."
    "Если бы только я мог всё исправить... Собрать всех, кого я люблю, и отвезти в Диснейленд."

    show Fox Flirt m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/anton/2day/013. V noch kogda propal vova.ogg"
    Ant "В ночь, когда пропал Вова, я, кажется, видел, как кто-то похожий на тебя плясал под моим окном..."

    show Fox Flirt b_night 00 good ahead
    with Dissolve(0.3)

    "Невероятно, но её маска будто бы стала ещё ехиднее."

    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    "Лиса словно принюхивалась."

    voice "voice/Alisa/Alisa2day/26 A chto.ogg"
    Fox "А что, ты тогда испугался?"

    voice "voice/Alisa/Alisa2day/27 Za sebya.ogg"
    Fox "За себя или кого-то ещё?"

    "«Оля!» — при мысли о сестре грудную клетку сжали тиски, и холодный пот сбежал по позвоночнику."

    stop music2 fadeout 2
    play music "music/16_strings0.2-1.ogg" fadein 1
    show Fox Angry m_night 00
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/28 Nu tak.ogg"
    Fox "Ну так слушай меня внимательно, мальчик по имени Антон."

    voice "voice/Alisa/Alisa2day/29 Eto.ogg"
    Fox "Это большой и страшный лес."

    "Лисичка сделала грозный шаг вперёд."

    play test_one "sounds/sfx_snow_footsteps_0.ogg"
    show Fox Angry b_night 00
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/30 I ya.ogg"
    Fox "И я — не единственный его обитатель."

    voice "voice/Alisa/Alisa2day/31 Drugie zveri.ogg"
    Fox "Другие звери уже знают о тебе."

    voice "voice/Alisa/Alisa2day/32 Beregis nas.ogg"
    Fox "Берегись нас! Этой ночью мы опять придём..."

    "«Всё же не стоило знакомиться с этим злом в детском обличии», — в панике думал я."


    play test_seven "music/Tension Suspense Risers_06.ogg"

    voice "voice/Alisa/Alisa2day/33 Poka ti.ogg"
    Fox "Пока ты со своей семьёй будешь спать, подкрадёмся близко-близко и станцуем..."

    stop music fadeout 0.5

    voice "voice/Alisa/Alisa2day/34 Makarenu.ogg"
    Fox "...макарену!"

    scene bg road_night2
    show Ant Cho b_night 00 norm ahead 01
    with Dissolve(0.5)
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.3)
    voice "voice/anton/2day/013. Che.ogg"

    Ant "Ч-чё?"

    scene bg road_night
    show Fox Angry b_night 00
    with Dissolve(0.3)
    show Fox Angry b_night 00 at sprite_scare

    voice "voice/Alisa/Alisa2day/35 Ei.ogg"
    Fox "Эй! Макарена!"

    window hide
    scene bg road_night2
    show Ant Cho b_night 00 norm ahead 02
    with Dissolve(0.5)
    pause 2
    play music "music/23_Christmas.ogg" volume 0.8 fadein 2.0
    scene bg road_night
    show Fox Flirt m_night 00 good dark_to_ahead:
        yoffset 0
        block:
            linear 0.15 yoffset 5
            linear 0.15 yoffset 0
            repeat
    with Dissolve(0.3)

    $ music_during_lines = 1.0
    voice "voice/Alisa/Alisa2day/36 U tebya pryamo.ogg"
    Fox "Аха-ха-ха-ха! У тебя прямо челюсть отвисла, Антоша!"

    show Fox Flirt m_night 00 good ahead:
        yalign 1.0

    voice "voice/Alisa/Alisa2day/37 Videl on menya.ogg"
    Fox "Видел он меня ночью у своего окна, ага. Как же!"

    voice "voice/Alisa/Alisa2day/38 A ti sluachaem.ogg"
    Fox "А ты, случаем, не местный дурачок, нет?"

    show Fox Normal m_night 00 good ahead with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/39 Menya.ogg"
    Fox "Меня не отпускают гулять так поздно."

    voice "voice/Alisa/Alisa2day/40 Zdes.ogg"
    Fox "Здесь, знаешь ли, дети пропадают."

    "Я потрогал пластиковую дужку очков, озадаченный глупой шуткой."
    "Напугался до чёртиков."

    show Fox Nice m_night 00 good ahead with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/41 Oi da ne.ogg"
    Fox "Ой, да не тереби ты окуляры свои."

    voice "voice/Alisa/Alisa2day/42 Ya ranshe.ogg"
    Fox "Я раньше тоже близорукой была."

    voice "voice/Alisa/Alisa2day/43 Poslush.ogg"
    Fox "Лучше послушай меня — может быть, ума наберёшься."

    voice "voice/Alisa/Alisa2day/44 Lisichku.ogg"
    Fox "Лисичку как обычно называют?"

    voice "voice/anton/2day/014. Plutovka.ogg"
    Ant "П-плутовка?"

    hide Fox
    show Fox Feel m_night 00 good ahead_to_aside
    with Dissolve(0.3)

    "Она вдруг заговорила обиженно:"

    voice "voice/Alisa/Alisa2day/45 Ah ti.ogg"
    Fox "Ах ты ж! Да как ты меня?.."

    hide Fox
    show Fox Feel m_night 00 good aside_to_ahead
    with Dissolve(0.3)

    voice "voice/anton/2day/017. Oi prosti.ogg"
    Ant "Ой, прости."

    show Fox Flirt m_night 00 good ahead:
        yoffset 0
        block:
            linear 0.15 yoffset 5
            linear 0.15 yoffset 0
            repeat
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/46 Devochka.ogg"

    "Девочка засмеялась, словно серебряные колокольчики зазвенели."

    voice "voice/Alisa/Alisa2day/47 Da shuchu.ogg"
    Fox "Да шучу я!"

    show Fox Flirt m_night 00 good ahead:
        yalign 1.0

    voice "voice/Alisa/Alisa2day/48 Konecnho.ogg"
    Fox "Конечно, плутовкой."

    $ music_during_lines = 0.7
    voice "voice/Alisa/Alisa2day/49 Esli ti.ogg"
    Fox "Если ты ловкий и смелый, не боишься с плутовкой водиться, я, так и быть, помогу разыскать этого Вову."

    voice "voice/Alisa/Alisa2day/50 Ti ze.ogg"
    Fox "Ты же неспроста его ищешь, да?"

    "Я неопределённо поводил плечами. Её прозорливость насторожила."

    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/51 I know.ogg"
    Fox "Знаю, почему дети повадились соваться в наш лес."

    voice "voice/Alisa/Alisa2day/52 Poroi tam.ogg"
    Fox "Порой там можно найти много всякого интересного."

    voice "voice/Alisa/Alisa2day/53  Ya vot.ogg"
    Fox "Я вот однажды нашла целый сугроб конфет и купалась в нём, да так, что челюсть слиплась."

    "Сугроб конфет?"
    "По интонации не понять: она сама-то верит в то, что говорит?"
    "Я снова улыбнулся, но на этот раз неискренне."

    voice "voice/Alisa/Alisa2day/54 Posmotrite ka.ogg"
    Fox "Посмотрите-ка, какой недоверчивый!"

    voice "voice/Alisa/Alisa2day/55 Nu nu.ogg"
    Fox "Ну-ну, а что ты на это скажешь?"

    label dev_night_meet_fox:
    scene Fox_give_candy_bg
    show snow_night_1
    show Fox_give_candy_01
    show Fox_give_candy_gum
    with Dissolve(0.5)
    $ renpy.start_predict_screen("day2_choice_candy_or_refuse")
    $ renpy.start_predict("candy_refuse")

    "Она протянула руку в меховой перчатке."
    "В ладони лежала горсть разных сладостей."

    $ add_text_to_dictionary(10)

    "В городе, где я когда-то жил, такие продавали на рынке или в {u}киосках{/u}."
    "Среди вкусных сокровищ я заметил свою любимую жвачку в яркой обёртке."
    $ add_text_to_dictionary(71)
    "Знакомая надпись на фантике гласила: {u}«Turbo»{/u}." id dev_night_meet_fox_8d7fdfd7
    "Треугольная лисья морда ткнула носом в мою сторону."

    play fon "sounds/fon/wind.ogg" volume 0.8 fadein 5.0

    $ music_during_lines = 1.0
    voice "voice/Alisa/Alisa2day/56 Ugosh.ogg"
    Fox "Угощайся."

    voice "voice/Alisa/Alisa2day/56 Y menya ih.ogg"
    Fox "У меня их — полные карманы."


label bunny2_night_meet_fox1:
    stop music fadeout 3.0
    window hide
    scene Fox_give_candy_bg
    show snow_night_1

    $ story_manager.MarkEvent(("day2", "candy"))
    call screen day2_choice_candy_or_refuse()


label bunny2_cancel1:
    $ renpy.stop_predict_screen("day2_choice_candy_or_refuse")
    $ renpy.stop_predict("candy_refuse")

    $ story_manager.MarkEvent(("day2", "candy", "refuse"))

    scene Fox_give_candy_bg
    show snow_night_1
    show Fox_give_candy_04
    with None

    window show

    voice "voice/anton/2day/018. Net spasibo.ogg"
    Ant "Н-нет, спасибо. Я..."

    "Мне не хотелось обижать первую знакомую, которую я завёл на новом месте, но и брать жвачку у странной девочки не было желания."
    "Вдруг она её и правда в сугробе нашла?"
    "Или это конфета с сюрпризом из магазина приколов? Развернёшь её - а она как стрельнёт!"

    voice "voice/anton/2day/019. U menya na sladkoe.ogg"
    Ant "У меня на сладкое аллергия."

    voice "voice/Alisa/Alisa2day/57 Aller.ogg"
    Fox "Ал-лер... что?"

    "Её тон стал озадаченным."

    voice "voice/Alisa/Alisa2day/57 Ti chego.ogg"
    Fox "Ты чего, живёшь в мире таблеток и микстур?"

    voice "voice/anton/2day/020.NuvcelomDa.ogg"
    Ant "Ну... в целом, да."

    play test_one "voice/Alisa/Alisa2day/58 Svist.ogg"

    "Лиса присвистнула."

    scene bg road_night
    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    "Её ладонь опустела — конфеты куда-то подевались — и заплавала в воздухе, задумчиво ловя снежинки."

    voice "voice/Alisa/Alisa2day/59 I noviy god.ogg"
    Fox "И Новый год у вас правда раз в двенадцать месяцев?"

    voice "voice/Alisa/Alisa2day/60 I est eti.ogg"
    Fox "И есть эти... м..."

    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    "Она пощёлкала пальцами, вспоминая."

    voice "voice/Alisa/Alisa2day/61 Mondays.ogg"
    Fox "Понедельники?"

    voice "voice/anton/2day/21.1Aga.ogg"
    Ant "Ага."

    play test_one "voice/anton/2day/21.2Yazaulibalsya.ogg"

    "Я заулыбался."

    voice "voice/Alisa/Alisa2day/62 Uu kak.ogg"
    Fox "У-у-у-у, как всё запущено."

    voice "voice/Alisa/Alisa2day/63 Vam bi.ogg"
    Fox "Вам бы, юноша, кило шоколада съесть против скуки и уныния."
    $ achievement_grant("ach_rejected_treat")

    jump bunny2_cont1


label bunny2_take1:

    $ renpy.stop_predict_screen("day2_choice_candy_or_refuse")
    $ renpy.stop_predict("candy_refuse")

    $ story_manager.MarkEvent(("day2", "candy", "take"))
    $ Flags.Raise("gum")

    scene Fox_give_candy_bg
    show snow_night_1
    show Fox_give_candy_01
    show Fox_give_candy_gum
    with None

    play test_one "sounds/sfx_candies.ogg"

    hide Fox_give_candy_gum
    with Dissolve(0.5)
    window show

    "Я принял угощение, почувствовав, как пахнет девочка: шерстью, дымом фейерверков и петард, цитрусами... Праздником, наконец."

    play music "music/11 Empty Road.ogg"

    play test_one "sounds/sfx_open_gum1.ogg"

    "Пальцы покалывало, когда я осторожно распечатал фантик."

    hide Fox_give_candy_01
    show Fox_give_candy_05
    with Dissolve(.5)
    "Ноздри уловили аромат персика. И чего-то ещё — незнакомого, но приятного."
    "Фруктовый кубик отправился в рот."
    "Я задвигал челюстями, перемалывая резинку."
    "На вкус обычная турецкая жвачка, разве что язык слегка онемел."

    scene bg vkladish with Dissolve(0.3)
    show vkladish2:
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

    play test_one "sounds/sfx_insert_unfold.ogg"

    $ add_text_to_dictionary(11)

    "Развернув {u}вкладыш{/u}, я обомлел от счастья."
    "На нём красовался Мерседес-Бенц — редкий и оттого желанный экземпляр коллекции каждого мальчишки моего прошлого двора."
    "Сердце бухнуло о рёбра. Я с трудом оторвался от вкладыша, не веря в свою удачу."

    $ music_during_lines = 0.8
    voice "voice/anton/2day/022. Eto ze.ogg"
    Ant "Это же... Это..."

    voice "voice/Alisa/Alisa2day/64 Teper ponyal.ogg"
    Fox "Теперь понял, что можно найти в лесу?"

    voice "voice/Alisa/Alisa2day/65 Tolko na tvoem.ogg"
    Fox "Только на твоём месте я бы туда в одиночку не ходила."

    voice "voice/Alisa/Alisa2day/66 Tebe von ot.ogg"
    Fox "Тебе вон от жвачки в зобу дыханье спёрло."

    voice "voice/Alisa/Alisa2day/67 A predst.ogg"
    Fox "А представляешь, что с тобой будет, если найдёшь чемодан таких фантиков?"

    voice "voice/Alisa/Alisa2day/68 Golovu.ogg"
    Fox "Голову напрочь снесёт — и пиши пропало."

    "Необычные угощения."
    "Как и она сама."

    hide vkladish2 with Dissolve(0.3)
    play test_one "sounds/sfx_insert_in_bag.ogg"
    play test_two "voice/Alisa/Alisa2day/69 Pod ee smeh.ogg"

    "Под её смешок я осторожно спрятал вкладыш в портфель, словно посадил бабочку в банку."
    "Здесь всё не так, как должно быть в понедельник утром!"
    $ achievement_grant("ach_accepted_treat")

    jump bunny2_cont1

label bunny2_cont1:
    $ story_manager.MarkEvent(("day2", "scene3"))

    scene bg road_night
    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    "Кто же ты такая?"
    "Спрашивать было глупо — не ответит. Или соврёт."
    "Ужасно хотелось заглянуть под маску."
    "Всё больше казалось, что под ней прячется совсем не маленькая девочка."

    stop music fadeout 5.0
    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    $ music_during_lines = 1.0
    voice "voice/Alisa/Alisa2day/70 Mozet Vova.ogg"
    Fox "Может, Вова тоже нашёл сугроб сладостей и теперь кувыркается в нём?"

    stop music fadeout 3.0
    play music2 "music/24_Fox.ogg" fadein 1.0

    $ music_general_volume = 0.7
    $ renpy.music.set_volume(0.7, 1.0, channel="music2")
    voice "voice/Alisa/Alisa2day/71 Slushai.ogg"
    Fox "Слу-у-ушай, вдруг он решил остаться в лесу?.."

    voice "voice/Alisa/Alisa2day/72 Togda navernoe.ogg"
    Fox "Тогда, наверное, ему очень холодно в одной варежке..."

    "Ветер подхватывал её слова, как дым от костра, и уносил в темноту, в дремучую чащобу."
    "Деревья позади скрипели и скрежетали ветками-костями."

    hide Fox
    show Fox Feel m_night 00 good ahead_to_aside
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/73 Ili s nim.ogg"
    Fox "Или... с ним что-то случилось в пути."

    voice "voice/Alisa/Alisa2day/74 Chto-to scary.ogg"
    Fox "Что-то страшное."

    "Лес словно оживал от её голоса: прислушивался, принюхивался, точно любопытный зверь."
    "Лиса отвечала таким же внимательным взглядом."

    voice "voice/anton/2day/024. Dikie zveri.ogg"
    Ant "Дикие звери?"

    hide Fox
    show Fox Feel m_night 00 good aside_to_ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/75 Eto po tvoemu.ogg"
    Fox "Это, по-твоему, страшно?"

    voice "voice/anton/2day/025. Nu ne znay.ogg"
    Ant "Ну... не знаю."

    show Fox Flirt m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/76 Ne znaet.ogg"
    Fox "Не знает!"

    voice "voice/Alisa/Alisa2day/77 Uz ne s.ogg"
    Fox "Уж не с двоечником ли я подружилась?"

    "Слово «двоечник» мне не понравилось, а вот «подружились» — даже очень."

    voice "voice/anton/2day/026. Ya horoshist.ogg"
    Ant "Я хорошист!"

    voice "voice/Alisa/Alisa2day/78 Bel da pus.ogg"
    Fox "Бел да пушист!"

    show Fox Nice m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/79 Poidesh so mnoi.ogg"
    Fox "Пойдёшь со мной, хорошист Антон?"

    voice "voice/Alisa/Alisa2day/80 Naidesh svoego.ogg"
    Fox "Найдём твоего Вову, и сам его спросишь, что он нашёл в этой пуще."

    voice "voice/Alisa/Alisa2day/81 Ved poka mi vmeste.ogg"
    Fox "Ведь пока мы вместе, никто тебя в лесу не тронет."

    voice "voice/Alisa/Alisa2day/82 Vot uvidish.ogg"
    Fox "Вот увидишь."

    "Внутри что-то тревожно заворочалось."
    "«{i}Лучше уходи{/i}», — посоветовал шепоток."

    voice "voice/anton/2day/027. Ya tebe ne veryu.ogg"
    Ant "Я тебе не верю."

    hide Fox
    show Fox Feel m_night 00 good ahead_to_aside
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/83 Ti dumaesh.ogg"
    Fox "Ты думаешь, я врунья?"

    hide Fox
    show Fox Feel m_night 00 good aside_to_ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/84 Da i poz.ogg"
    Fox "Да и пожалуйста, мне никогда никто не верит!"

    "В голосе незнакомки чувствовалась обида. Пойди пойми, наигранная или нет."

    hide Fox
    show Fox Feel m_night 00 good ahead_to_dark
    with Dissolve(0.3)

    "Лиса отвернулась, будто я мигом перестал её интересовать."

    if Flags.Has("gum"):
        "Жвачка стала горчить."

    "Вспомнилась папина любимая фраза: «Где твои манеры, сын?»"
    "А ведь лиса и вправду была ко мне добра."

    voice "voice/anton/2day/28 Ne obiz.ogg"
    Ant "Не обижайся, пожалуйста."

    voice "voice/anton/2day/28.2 Lisi bivaut.ogg"
    Ant "Лисы бывают и добрыми..."

    voice "voice/anton/2day/29 Nu kak v skazkah.ogg"
    Ant "Ну как в сказках."

    voice "voice/anton/2day/29.2 Mne bi tolko.ogg"
    Ant "Мне бы только понять, что ты за лиса."

    play sound "voice/Alisa/Alisa2day/94 Devochka.ogg"

    "Девочка мелодично хихикнула, прикрыв руками нос маски."

    show Fox Fullface m_night 00 good dark
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/95 Togda.ogg"
    Fox "Тогда пойдём со мной в лес — и ты всё обо мне узнаешь."

    show Fox Fullface m_night 00 good dark_to_ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/96 No ne.ogg"
    Fox "Но не сейчас, а когда рассветёт, а то тебя, бедного, всего аж потряхивает."

    voice "voice/Alisa/Alisa2day/97 Togo i glyadi.ogg"
    Fox "Того и гляди кондрашка хватит."

    voice "voice/Alisa/Alisa2day/98 Aida.ogg"
    Fox "Айда провожу тебя до школы."

    scene bg varishka2 with Dissolve(0.5)

    play test_one "sounds/sfx_dog_calling_one.ogg"

    "Услышав это, собака согласно гавкнула и бросила возиться с варежкой."
    "Я нагнулся, чтобы подобрать чуть было не сбежавшую от меня рукавицу."

    voice "voice/anton/2day/030. Nu esli tebe po puti.ogg"
    Ant "Ну если тебе по пути..."
    $ music_general_volume = 1.0
    $ renpy.music.set_volume(1.0, 4.5, channel="music2")

    play test_one "sounds/steps/loop_footsteps_two.ogg" loop
    $ SetParSpeed(120)
    show walking_fox_11_dark
    show walking_fox_12_dark
    show walking_fox_21_dark
    show walking_fox_22_dark
    show walking_fox_31_dark
    show walking_fox_32_dark
    show snow_night_1_left:
        alpha 1.0
        pause 7.0
        ease 15.0 alpha 0.0
    show ant_walk
    show fox_walk
    with Dissolve(0.5)

    "Мы двинулись навстречу школе и потерявшемуся рассвету."
    "Тут и там в окнах домов загорались огни, словно их обитатели подавали нам неведомые сигналы."
    "За шторами мелькали силуэты, изредка лаяли дворовые псы."
    "Из труб вился серый дымок, на кухнях бубнили телевизоры, звенела посуда."
    "Мы смотрели, как неохотно просыпается посёлок, а сами осторожно шагали по заснеженным колеям."
    "Я шёл по левой, она — по правой, а собака плелась за нами следом."
    "Я ждал, что лиса продолжит свои чудные разговоры, но она всю дорогу молчала, словно играла со мной в какую-то ведомую ей одной игру."
    "Лишь изредка плутовка хихикала, когда собака нелепо чихала от падающих на усы снежинок."

    play test_two "sounds/sfx_dog_sneeze.ogg"

    "Я первым нарушил молчание."

    voice "voice/anton/2day/031. Tak kak tebya.ogg"
    Ant "Так как тебя зовут?"

    voice "voice/Alisa/Alisa2day/100 Nu konechno.ogg"
    Fox "О, ну конечно."

    voice "voice/Alisa/Alisa2day/101 Imena.ogg"
    Fox "Имена, имена, имена!"

    voice "voice/Alisa/Alisa2day/102 Ludyam.ogg"
    Fox "Людям непременно надо вешать ярлыки на всё подряд."

    voice "voice/Alisa/Alisa2day/103 Nu i kak bi.ogg"
    Fox "Ну и как бы ты назвал такую лису, как я?"

    voice "voice/anton/2day/32 Daze ne znay.ogg"
    Ant "Даже не знаю..."

    voice "voice/anton/2day/32.2 No ya chital.ogg"
    Ant "Но я читал про лису по имени Алиса."

    voice "voice/Alisa/Alisa2day/104 A chto.ogg"
    Fox "А что?"

    voice "voice/Alisa/Alisa2day/105 Ya ne.ogg"
    Fox "Я не против."

    voice "voice/Alisa/Alisa2day/106 Pust budet.ogg"
    Alis "Пусть будет Алиса."

    "И не поймёшь, шутит она или серьёзно."
    "Я оглянулся, словно искал подсказки: у собаки, у тёмного неба без проблеска зари."

    stop music2 fadeout 5.0

    "Мои немые вопросы оставались без ответа."


    stop test_one fadeout 2.5
    scene bg school_night_maninblack1 with Dissolve(0.5)

    "Впереди уже вырисовывалась школа."

    play music "music/31_FearTheMind_final.ogg" volume 0.6 fadein 3.0

    "Кирпичная коробка, застрявшая в нескончаемой ночи."
    "Свет её окон не сулил ничего хорошего."
    "Деревья-часовые охраняли пришкольный участок."

    play sound "sounds/sfx_company.ogg"

    "Крик, детский смех и чей-то свист разорвали тишину."
    "Мы ходили сюда с мамой как только приехали в посёлок, и тогда школа казалась уютной: пустые коридоры, пахнущие полиролью, пушистый снег снаружи..."
    "Второй раз я пришёл один, за учебниками, и всё пытался представить ровесников, скатывающихся по перилам, малышей, бегущих в библиотеку и учителей, важно вышагивающих по коридору."
    "На пороге в нахлобученных на затылки шапках и спортивных штанах курили старшеклассники."
    "Их вид развеял мои представления о школьном уюте."
    "Колючие глаза и жёлтые от никотина зубы, кривые усмешки — всё это вгоняло в тоску, равную по мощи хмурому зимнему утру."


    "Погрузившись в мысли, я совсем забыл про попутчицу."

    show Fox Normal m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/107 Posle.ogg"
    Alis "После уроков жду тебя на заднем дворе."

    voice "voice/Alisa/Alisa2day/108 Vozle.ogg"
    Alis "Возле повешенного."

    voice "voice/anton/2day/033. Vozle kogo.ogg"
    Ant "Возле кого?"

    "Она проигнорировала вопрос."

    voice "voice/Alisa/Alisa2day/109 Ne opazd.ogg"
    Alis "Не опаздывай."

    "Я поколебался."
    "«И хочется, и колется», — говорит мама, когда я никак не мог решиться."
    "Мысль о маме помогла ответить:"

    voice "voice/anton/2day/034. Ya posle shkoli.ogg"
    Ant "Я после школы сразу домой."

    show Fox Fullface m_night 00 good ahead
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/110 Eh.ogg"
    Alis "Эх, Антоша-Антоша, это я тебя так просто отпустила."

    voice "voice/Alisa/Alisa2day/111 Drugie ze.ogg"
    Alis "Другие же незаметно подкрадутся со своими улыбочками и вцепятся — клещами не оторвёшь."

    voice "voice/Alisa/Alisa2day/112 Popomni.ogg"
    Alis "Попомни мои слова."

    play sound "voice/Alisa/Alisa2day/112 Zevok.ogg"
    show Fox Am m_night 00
    with Dissolve(0.3)
    pause 0.3
    show Fox Fullface m_night 00 good ahead
    with Dissolve(0.3)

    "Лиса разинула пасть в широком зевке."
    "Что ещё за трюк такой?"

    play test_one "sounds/Antoha_1.ogg"

    "Кто-то из пробегавших вдалеке ребят выкрикнул моё имя."

    scene bg_dog_02
    with Dissolve(0.5)

    "Я машинально обернулся на крик."

    show bg_dog_05
    show bg_dog_04:
        alpha 1.0
        pause 0.30
        linear 0.2 alpha 0.0
    show bg_dog_03:
        alpha 1.0
        linear 0.2 alpha 0.0
    play sound "sounds/snowball_4.ogg"
    play test_two "sounds/sfx_dog_calls_0.ogg"

    "Увесистый снежок пролетел в полуметре от моего плеча и задел собаку."
    "Жалобно тявкнув, дворняжка припустила в сторону ручья, — только хвост мелькнул."

    scene black with Dissolve(0.5)

    "Темнота пожрала её."

    scene bg school_night_maninblack1 with Dissolve(0.5)

    "И лисичка пропала без следа. Растворилась в морозном воздухе."
    "А может, в тень мою спряталась?"

    if Flags.Has("gum"):
        play test_one "sounds/glotok-fix.ogg"
        "Я сглотнул."
        "Жвачку."
        "Вот же не повезло."

    play sound "voice/anton/2day/Vdoh.ogg"

    "Глубоко вздохнув, я двинулся к школе, к запаху котлет в тесте, к льющемуся на снег свету."

    $ story_manager.MarkEvent(("day2", "la school"))
    $ SceneFlags.Reset()

label bunny_school_night1:
    window hide
    if Flags.Has("witness school"):
        scene bg school_night_maninblack0 with Dissolve(0.5)
    else:
        scene bg school_night_maninblack1 with Dissolve(0.5)
    call screen school_night_1
    window show

label bunny_school_night_gopniks:
    $ story_manager.MarkEvent(("day2", "la school", "boys"))

    play test_one "sounds/sfx_boys_laugh_long_street.ogg"
    if SceneFlags.Seen("sempai"):
        "Толпа старшеклассников."
    else:
        "Толпа галдящих старшеклассников с шапками набекрень. Таким лучше на глаза не попадаться."
        $ true_detective_count2 += 1
    jump bunny_school_night1

label bunny_school_night_dog:
    $ story_manager.MarkEvent(("day2", "la school", "car"))

    play test_one "sounds/sfx_car_door.ogg"
    if SceneFlags.Seen("school car"):
        "Чёрная Волга."
    else:
        "Неподалёку, взобравшись передним колесом на затянутый гололедицей бордюр, разместилась новенькая Волга."
        "Чёрная, как сажа. Словно сбежала из папиной страшилки, что он любил рассказывать на чердаке в грозу."
        "Помню, как он грустно улыбнулся, припоминая воронок, похищающий маленьких детей."
        "Отец говорил:"
        "\"У него, словно внутри катафалка, в окошке салона маячат белые шторки.\""
        "\"А в номере стоят буквы ССД. Знаешь, что это значит? Смерть Советским Детям.\""
        "Смешно, я ведь тоже родился в Советском Союзе..."
        $ true_detective_count2 += 1
    jump bunny_school_night1

label bunny_school_night_witness:
    $ story_manager.MarkEvent(("day2", "la school", "witness"))

    $ Flags.Raise("witness school")


    "Высокий мужчина курил, пуская клубы дыма по ветру."
    "На учителя не похож."
    "Или, может, физрук?"

    scene bg school_night_maninblack2 with Dissolve(0.5)

    "Я осторожно осмотрел его лицо, будто высеченное из гранита, заячью губу над тлеющей сигаретой."



    "Мужчина поигрывал брелоками и внимательно смотрел на меня."
    "Огонёк отражался в глубоко посаженных глазах."
    "Я потупился."



    "Взор громилы лениво отклеился от меня и устремился на дорогу."

    play test_one "sounds/sfx_man_walks_away (1).ogg"
    pause 0.4
    stop test_one fadeout 1.5
    $ true_detective_count2 += 1

    jump bunny_school_night1

label bunny_school_night_nest:
    $ story_manager.MarkEvent(("day2", "la school", "nest"))

    if SceneFlags.Seen("school nest"):
        "Воронье гнездо."
    else:
        play test_one "sounds/sfx_nest_noises.ogg"
        "Интересно, чьё это гнездо?"
        "Может, сороки-воровки?"
        "Тогда наверняка в нём полно всякой блестящей всячины."
        "Цветные стекляшки, лимонадные пробки, отполированные монеты... или детские брекеты."
        $ true_detective_count2 += 1
    jump bunny_school_night1

label bunny_school_inside1:
    $ story_manager.MarkEvent(("day2", "scene4"))
    stop music fadeout 3.0
    play test_one "sounds/steps/steps_snow001.ogg"

    if Flags.Has("witness school"):
        scene bg school_night_maninblack0:
            yalign 0.5
            ease 4 zoom 1.5 xoffset -600 yalign 0.8
    else:
        scene bg school_night_maninblack1:
            yalign 0.5
            ease 4 zoom 1.5 xoffset -600 yalign 0.8

    $ renpy.pause(1.0)
    play test_two "sounds/school_door-open-1.ogg"
    stop fon fadeout 2.0
    scene black with Dissolve(1.0)
    play test_three "sounds/school_door-close-1.ogg"
    $ renpy.pause(1.0)
    play test_one "sounds/Anton-stairs-in-2-echo-1.ogg"

    label total_test:

    "За дверями приглушённо звучали голоса. Мигали лампы."
    "Тьма ползла мимо окон, и казалось, что школа плывёт в открытом космосе, как заблудившийся звездолёт."

    play fon "sounds/school_003.ogg" fadein 2.0
    scene bg_raspisanie:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 0.675
        ease 10 zoom 0.83 xalign 0.32 yalign 0.5
    show men_00:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 1.2 xpos 1050 ypos 540
    show men_01:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 1.2 xpos 950 ypos 540
    show men_02:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 1.2 xpos 1100 ypos 540
    show men_03:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 1.2 xpos 1200 ypos 540
    show men_04:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 2.0 xpos 0 ypos 500
    show men_05:
        subpixel True
        yalign 0.5
        xalign 0.5
        xpos 960
        ypos 540
        ease 10 zoom 2.0 xpos 1200 ypos 500
    with Dissolve(2.0)

    "Поднявшись на второй этаж, я заметил толпу у расписания."
    "Все что-то оживлённо обсуждали."
    "Я подошёл поближе и через стену рюкзаков и спин сумел разглядеть то, что вызвало такой живой интерес."
    "Слева от расписания к стеклу было приклеено объявление, отпечатанный на принтере листок."

    scene bg_raspisanie:
        anchor (0.5, 0.5)
        zoom 0.83 xalign 0.32 yalign 0.5
    show men_00:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.2 xpos 1050 ypos 540
    show men_01:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.2 xpos 950 ypos 540
    show men_02:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.2 xpos 1100 ypos 540
    show men_03:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.2 xpos 1200 ypos 540
    show men_04:
        subpixel True
        anchor (0.5, 0.5)
        zoom 2.0 xpos 0 ypos 500
    show men_05:
        subpixel True
        anchor (0.5, 0.5)
        zoom 2.0
        xpos 1200
        ypos 500

    call screen read_attention()

    play sound "voice/kate/02 KA.ogg"

    window hide
    stop fon fadeout 4.0
    play test_one "sounds/steps/Podoshe_2.ogg"
    play music "music/28_Dejection.ogg" volume 0.8 fadein 5.0
    scene bg_propalrebenok1 with Dissolve(0.5)
    $ renpy.pause(10.0)

    play test_two "voice/kate/03 KA.ogg"










    window show

    "«Внимание! Пропал ребёнок!»"
    "Вова Матюхин. Так его звали."
    "Четвёртый класс."
    "На зернистом отпечатке Вова был мертвецом с чёрным ртом и тёмными провалами глаз."
    "Может, это живущий в чащобе мрак впитался в его поры и изувечил лицо?"
    "Пластиковый автомат не защитил от шёпота ветвей и воющего ветра."
    "Пустые глаза исчезнувшего школьника сверлили меня, будто молили о чём-то."

    play test_one "sounds/steps/Otoshel.ogg"

    scene bg koridorchic_mor_full with Dissolve(0.5):
        ypos 0
        xpos -2319
        pause 1.5
        ease 15 xpos 0
    queue fon "sounds/school_004.ogg" loop

    "Не выдержав взгляда, я отвернулся и поспешил к окну. Уселся на подоконник."
    "Этаж постепенно заполнялся детьми, они собирались группками по несколько человек."
    "На меня никто не обратил внимания."
    "В сумерках у туалетов детские голоса чеканили считалочку:"

    play test_six "voice/Child/2day/Child_01.ogg" volume 0.75
    Childs "Для медведя, для лисы, \nЗайчик, кушать принеси!"

    "Я повернул голову в их сторону, приглядываясь к фигурам, но тут моё внимание отвлекло громкое цоканье."

    play test_one "sounds/steps/Techer_in.ogg"
    scene bg koridorchic_mor_full:
        ypos 0
        xpos 0
    show Liliya Normal m_evening 00 at liliay_income:
        yoffset 100
    with Dissolve(0.3)

    "По коридору, гордо задрав подбородок, продефилировала учительница."
    "Каблуки стучали о пол, как копытца."

    play test_one "sounds/sfx_girl_comes1.ogg"
    show Kate Kawai m_day 00 good aside 01 at kate_income:
        yoffset 100
    with Dissolve(0.3)

    "Им вторили шаги девочки, которая держалась рядом."

    hide Kate
    show Kate Kawai m_day 00 good aside_to_ahead 01:
        xpos 150 + 140 ypos 0
        yoffset 100
    with Dissolve(0.3)

    "Очень важная, она остановилась, чтобы шепнуть на ухо однокласснице какой-то секрет."

    hide Kate
    show Kate Kawai m_day 00 good ahead_to_aside 01:
        xpos 150 + 140 ypos 0
        yoffset 100
    with Dissolve(0.3)

    "Староста, наверное, — вон, ей вручают классный журнал."

    show Kate Normal m_day 00 evil aside 01 with Dissolve(0.3)

    voice "voice/lydia/2day/01 Ekaterina.ogg"
    Teacher "Екатерина, возьми, пожалуйста."

    play test_one "sounds/Door_open_2.ogg"
    scene bg koridorchic_mor_full_open:
        ypos 0
        xpos 0
    show Liliya Normal m_evening 00:
        xzoom -1.0 xpos -130 - 1000 ypos 0
        yoffset 100
    show Kate Normal m_day 00 evil aside 01:
        xpos 150 + 140 ypos 0
        yoffset 100
    with Dissolve(0.3)
    pause 0.3
    play test_two "sounds/steps/Techer_in.ogg"
    show Liliya Normal m_evening 00 at liliay_out
    hide Kate
    show Kate Normal m_day 00 evil aside_to_ahead 01:
        xpos 150 + 140 ypos 0
        yoffset 100

    "Учительница открыла кабинетную дверь, и толпа, галдя и толкаясь, повалила внутрь."

    show Semen Normal b_day 00 evil aside 01:
        yoffset 80
    with Dissolve(0.3)

    "Среди всех выделялся высокий рыжий толстяк с прыщавым лицом, до странности напоминавшим гранат."

    hide Semen
    show Semen Normal m_day 00 evil aside_to_ahead 01 onlayer master1:
        xzoom -1.0 yoffset 80
    with Dissolve(0.3)

    "Недоброе предчувствие зашевелило волоски на моём загривке."

    hide Kate
    show Kate Normal m_day 00 evil ahead_to_aside 01:
        xpos 150 + 140 ypos 0 yoffset 100

    "Встречал я уже ребят с такими бегающими глазами и таким каркающим смехом."

    play test_one "sounds/sfx_girl_walks_away1.ogg"

    show Kate Normal m_day 00 evil aside 01 at kate_out
    hide Semen onlayer master1
    show Semen Disgust m_day 00 evil ahead_to_aside 01:
        xzoom 1.0 yoffset 80
    with Dissolve(0.3)

    "Девочка, похожая на учительницу — её уменьшенная копия, — предостерегла толстяка жестом и по расчищенной тропке вошла в кабинет."
    "Какой-то паренёк замешкался в проходе, и рыжий тут же пихнул его:"

    hide Kate
    play test_one "sounds/sfx_push.ogg"
    show Semen Disgust m_day 00 evil aside 02 at sprite_scare:
        yoffset 80

    voice "voice/semen/2day/01 Topa.ogg"
    Noname "Топай резче, мудила!"

    show Semen Disgust m_day 00 evil aside 01
    show bg koridorchic_mor_open_1:
        ypos 0
        xpos 0
    with Dissolve(0.3)
    play test_one "sounds/sfx_steps.ogg"

    "Мальчик полетел, размахивая руками в попытке сохранить равновесие."

    show Semen Happy m_day 00 good ahead at sprite_happy_alltimes:
        yoffset 80
    with Dissolve(0.3)

    play sound "voice/semen/2day/02 Tols.ogg"

    "Толстяк рассмеялся, противный гогот подхватило несколько человек в его окружении."

    hide Semen
    show Semen Normal m_day 00 evil ahead_to_aside 01 at semen_out:
        yoffset 80
    with Dissolve(0.3)

    play test_one "sounds/sfx_footsteps_fat_boy_2.ogg"
    play test_seven "voice/semen/2day/ha.ogg"

    "Они хохотали, словно щёлкали ножницами, — большими страшными садовыми ножницами."

    scene bg koridorchic_mor_open_2:
        ypos 0
        xpos 0
    with Dissolve(0.3)
    stop fon fadeout 3.0
    play test_one "sounds/sfx_footsteps_class.ogg"

    "Кабинет засосал детей. Коридор опустел."

    scene bg koridorchic_mor_open_3:
        ypos 0
        xpos 0
    with Dissolve(0.3)

    "Мне захотелось врасти в подоконник."

    window hide
    play fon "sounds/fon/wind_shooll.ogg" fadein 2.0
    scene bg_transition_01 with Dissolve(1.0)
    stop music fadeout 5.0
    $ renpy.pause(3.5)
    play music2 "music/39_Dvar - Oramah Elahar.ogg"  fadein 5.0
    window show

    "За окнами редкие фонари боролись с темнотой, барахтались, как флуоресцирующие рыбы в чёрном океане."
    "А что, если сейчас убежать?"
    "Выйти туда и раствориться во мраке."
    "Я представил, как бегу по снегу, как он скрипит под моими ногами, и с каждым шагом я всё легче, всё невесомей."

    stop music2
    play test_one "sounds/bell.ogg"
    stop fon
    scene bg_bell with Dissolve(0.8)

    "Трель звонка взорвала видение."

    scene bg koridorchic_mor_open_3:
        ypos 0
        xpos -400
    with Dissolve(0.5)

    "Я с неохотой отлип от окна."

    play test_two "voice/anton/2day/036.Potom neskolko raz.ogg"

    "Потом несколько раз глубоко вздохнул, чтобы хоть немного усмирить разбушевавшийся пульс, и вошёл в класс."

    jump bunny2_school_classroom1

label bunny2_school_classroom1:
    $ story_manager.MarkEvent(("day2", "scene5"))

    window hide
    scene bg koridorchic_mor_open_3:
        alpha 1.0
        ypos 0
        xpos -400
        parallel:
            ease 6.0 xpos 0

    show bg_classroom base2:
        alpha 0.0
        ypos 0
        xpos -3911 + 1920
        parallel:
            pause 3.0
            ease 5.0 xpos -3911 + 1920 + 300
        parallel:
            pause 4.0
            linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    play test_one "sounds/steps/steps_shool.ogg"
    $ renpy.pause(3.0)
    play fon "sounds/fon/noise_klass.ogg" fadein 1.0
    play test_two "sounds/steps/steps_shool_02.ogg"
    $ renpy.pause(1.5)

    "Чопорная учительница смерила меня раздражённым взглядом поверх очков."

    scene bg_teacher 02 01:
        xpos 0
    with Dissolve(0.5)

    voice "voice/anton/2day/37 Ya novenkiy.ogg"
    Ant "Я... новенький."

    voice "voice/anton/2day/37.2 Mne vot skazali.ogg"
    Ant "Мне вот сказали к вам подойти."

    "Заснеженная лесная тропинка вилась перед глазами. Вовсе не хищно, а умиротворённо шуршали сосны."

    scene bg_teacher 01 01:
        xpos 0
    with Dissolve(0.4)
    scene bg_teacher 01 01:
        xpos 0
        ease 4.0 xpos -2299 + 1920

    voice "voice/lydia/2day/02 Hm.ogg"
    Teacher "Хм..."

    play test_one "sounds/perelist_02.ogg"

    "Она уткнулась носом в журнал и пролистала страницы."

    voice "voice/lydia/2day/03 A fam.ogg"
    Teacher "А фамилия-то как?"

    voice "voice/anton/2day/038. P-petrov.ogg"
    Ant "П-п-петров..."

    voice "voice/lydia/2day/04 Gromche.ogg"
    Teacher "Громче говори!"

    voice "voice/lydia/2day/05 Chego.ogg"
    Teacher "Чего мямлишь?"

    play test_one "sounds/steps/Podoshe_2.ogg"
    scene bg_teacher 01 02:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/anton/2day/039. Petrov.ogg"
    Ant "Петров!"

    scene bg_teacher 02 02:
        xpos -2299 + 1920
    with Dissolve(0.4)
    play music "music/28_Dejection.ogg" volume 0.8 fadein 1.0

    voice "voice/lydia/2day/06 Net.ogg"
    Teacher "Хм... Нет такого."

    "Она долго и тяжело смотрела на меня, точно пыталась уличить в обмане."
    "Хотелось просочиться сквозь линолеум."
    "Слева наблюдали размытые лица. Класс дышал, фыркал единым организмом, как опасный зверь."

    voice "voice/lydia/2day/08 Ty ne.ogg"
    Teacher "Ты не ошибся?"

    voice "voice/lydia/2day/09 Net takogo.ogg"
    Teacher "Нет такого в списке."

    "Предательски дрожали колени, кружилась голова."
    "Я сжал кулаки так, что костяшки побелели."

    voice "voice/anton/2day/040. Mne skazali 204.ogg"
    Ant "Мне сказали: 204 кабинет, Лилия Павловна, шестой «В»."

    play sound "sounds/sfx_laugh.ogg"
    "Кажется, класс принял мои слова за подобие шутки и разразился хохотом."

    voice "voice/lydia/2day/10 Chto za.ogg"
    Teacher "Что за бардак?!"

    stop fon fadeout 0.5

    "Шум резко стих."
    "Класс припрятал смешки для более удобного момента."

    scene bg_teacher 01 03:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/lydia/2day/11 Ponaberut.ogg"
    Teacher "Понаберут студентов!"

    voice "voice/lydia/2day/12 Tolko.ogg"
    Teacher "Только знают, что губяки свои малевать, а я — разгребай, значит?"

    scene bg_teacher 01 02:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/lydia/2day/13 A bumagi.ogg"
    Teacher "А бумаги-то кто заполнять будет? Не первый раз ведь уже."

    voice "voice/lydia/2day/14 Podozdi.ogg"
    Teacher "Подожди здесь. Сейчас..."

    scene bg_teacher 00 02:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/lydia/2day/15 Seychas.ogg"
    Teacher "Сейчас я им устрою."

    scene bg_anton_on_board:
        zoom 0.79
        xpos 0
        ypos 0
    with Dissolve(0.5)
    play test_one "sounds/steps/Techer_out.ogg" fadein 1.0

    "Учительница пронеслась мимо, злобно бормоча, а я остался один посреди класса."
    "Будто приговорённый к расстрелу перед строем автоматчиков, я потупился, чувствуя на себе глумливые взгляды."

    stop music fadeout 5.0

    "Они трогали, щипали, скользили по коже лазерными прицелами."

    play fon "sounds/fon/wind_shooll.ogg" fadein 2.0
    scene bg_anton_on_board:
        zoom 0.79
        xpos 0
        ypos 0
        ease 1.0 zoom 11.0 xpos -12300 ypos -6800
    pause 0.6
    scene bg_black with Dissolve(0.4)
    scene transition_01:
        zoom 11.0
        xalign 0.5
        yalign 0.7
        ease 1.0 xalign 0.5 yalign 0.7 zoom 1.0
    show transition_05:
        zoom 9.18
        xalign 0.5
        ypos -28000
        ease 1.0 xalign 0.5 ypos 200 zoom 0.18
    with Dissolve(0.5)
    play music "music/39_Dvar - Oramah Elahar.ogg"  fadein 3.0

    "Вновь представил, как бегу далеко-далеко отсюда, наперекор холодному ветру, взмываю над соснами в прыжке."
    "И никого нет вокруг — только попутный ветер."

    scene transition_01:
        xpos 0
        yalign 0.7
        easeout 4.0 yalign 0.0
    show transition_05:
        zoom 0.18
        xalign 0.5
        ypos 200
        parallel:
            easeout 1.8 ypos 1150
        parallel:
            linear 1.6 alpha 0.0
    show transition_03:
        xpos 0
        ypos -600
        pause 1.6
        linear 2.8 zoom 0.9 xpos -100 ypos 1600
    show transition_04:
        xpos 1000
        ypos -700
        pause 1.7
        linear 2.8 zoom 0.9 xpos 1300 ypos 1100
    show transition_02:
        xpos 0
        ypos -1800
        pause 2.6
        linear 1.5 xpos 0 ypos 0

    "В глазах одноклассников читался немой вопрос: «Этот новенький — он наш или он чужак?»"

    stop fon fadeout 3.0
    play test_one "voice/kate/01 KA.ogg"
    play sound "sounds/sfx_laugh2.ogg"

    "Кто-то что-то еле процедил, и по кабинету прокатился сдавленный смех."

    stop music fadeout 5.0

    play music2 "music/41_Imminence part.ogg" volume 0.8 fadein 1.0 noloop

    voice "voice/semen/2day/03 Dosk.ogg"
    Noname "Доску вытри!"

    "Легко было понять, кто тут главный юморист."

    scene bg_Sem3
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

    voice "voice/semen/2day/04 Ei.ogg"
    Noname "Эй, очкарик!"

    play fon "sounds/fon/noise_klass.ogg" fadein 1.0

    voice "voice/semen/2day/05 Ty cz.ogg"
    Noname "Ты чё, не только слепой, но ещё и глухой?"

    scene bg_classroom ant:
        xpos -3911 + 1980
    with Dissolve(0.5)

    voice "voice/semen/2day/06 Dosk.ogg"
    Noname "Доску вытри, говорю!"

    "Теперь тряслись не только колени."
    "Всё тело било мелкой дрожью, и я молился, чтобы учительница вернулась поскорее."
    "Высшие силы услышали мои просьбы."

    play test_one "sounds/Door_open_2.ogg"
    play test_two "sounds/steps/Techer_in.ogg"
    $ renpy.pause(2.5)
    scene bg_classroom ant_teacher:
        xpos -3911 + 1980
    with Dissolve(0.4)

    voice "voice/lydia/2day/17 Nu chto.ogg"
    Teacher "Ну что мне с тобой делать-то?!"

    voice "voice/lydia/2day/18 Kuda saj.ogg"
    Teacher "Куда сажать, а?"

    voice "voice/lydia/2day/19 Davai-ka.ogg"
    Teacher "Давай-ка сядь, наверное, с Семёном."

    stop music2 fadeout 2.0

    voice "voice/lydia/2day/20 On vse.ogg"
    Teacher "Он всё равно один."

    play music "music/28_Dejection.ogg" volume 0.8

    voice "voice/semen/2day/07 Escze.ogg"
    Sem "Ещё чего!"

    window hide
    play test_one "sounds/Bag.ogg"
    scene bg_classroom ant_teacher_bag:
        xpos -3911 + 1980
        yoffset 0
        linear 0.1 yoffset -3
        linear 0.1 yoffset 2
        linear 0.1 yoffset 0
    with Dissolve(0.1)
    $ renpy.pause(1.0)
    window show
    play test_two "voice/semen/2day/08 Tols.ogg"

    "Толстяк демонстративно водрузил рюкзак на соседний стул, почесал брюхо и ухмыльнулся."

    scene bg_teacher 01 02:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/lydia/2day/21 Ti opyat.ogg"
    Teacher "Ты опять за старое?"

    voice "voice/lydia/2day/22 Snova.ogg"
    Teacher "Снова бабушку в школу вызывать?"

    stop fon fadeout 3.0

    "Класс притих."

    scene bg_Sem3 with Dissolve(0.3)

    voice "voice/semen/2day/09 A cze.ogg"
    Sem "А чё она мне сделает?"

    scene bg_teacher 01 02:
        xpos -2299 + 1920
    with Dissolve(0.4)

    voice "voice/lydia/2day/23 Ne ona.ogg"
    Teacher "Не она — так я тебе сделаю."

    voice "voice/lydia/2day/24 Bag.ogg"
    Teacher "Рюкзак убрал, быстро!"

    "Семён не шелохнулся."
    "Со скучающим видом он принялся рассматривать портреты писателей на стене."
    "Нужно было что-то делать, как-то выкручиваться. Спасать положение."

    voice "voice/anton/2day/41 Ya.ogg"
    Ant "Я..."

    play test_one "voice/anton/2day/41. Ya prochistil.ogg"

    "Я прочистил горло и продолжил сдавленным, не своим, голосом:"

    voice "voice/anton/2day/42.2 Ya mogu za posl.ogg"
    Ant "Я могу за последнюю парту сесть."

    voice "voice/anton/2day/42.3 Tam kazetsa.ogg"
    Ant "Там, кажется, свободно."

    scene bg_teacher 02 02:
        xpos -2299 + 1920
    with Dissolve(0.4)
    play test_one "voice/lydia/2day/25 Teach.ogg"

    "Учительница громко засопела."
    "Посмотрела на меня, на Семёна, затем снова на меня."

    voice "voice/lydia/2day/26 Ladno.ogg"
    Teacher "Ладно. Садись пока туда."

    voice "voice/lydia/2day/27 A s toboy.ogg"
    Teacher "А с тобой, Бабурин, мы ещё поговорим!"

    voice "voice/lydia/2day/28 Chtobi.ogg"
    Teacher "Чтобы подошёл после уроков."

    voice "voice/lydia/2day/29 Budesh.ogg"
    Teacher "Будешь по классу дежурить. Ясно?"

    scene bg_Sem2 with Dissolve(0.3)

    "Семён криво улыбнулся. Сочные прыщи зрели на кончике его носа."

    scene bg_classroom base2:
        xpos -3911 + 1920 + 300
    show ant1:
        xpos -3911 + 1920 + 300
    pause 1.0
    hide ant1 with Dissolve(0.4)

    "Я пошёл, до одури боясь споткнуться и стать причиной нового всплеска веселья."

    play fon "sounds/fon/noise_klass.ogg"
    play sound "sounds/satdown.ogg"

    "Сел сзади, за самую последнюю парту, на которой грудой валялись старые плакаты."

    play sound "sounds/satdown2.ogg"

    "Места для изгоев заняты — можно приступать."

    voice "voice/lydia/2day/30 Vot i.ogg"
    Teacher "Вот и хорошо! Начнём урок!"

    voice "voice/lydia/2day/31 Tema.ogg"
    Teacher "Тема: традиции русской и мировой литературы в рассказе Зощенко «Не надо врать»."

    scene bg_classroom sem_back:
        xpos -3911 + 1920 + 300
    with Dissolve(0.4)

    "Толстяк обернулся ко мне. Взгляд его сулил долгие дни, недели, месяцы издёвок и тычков."

    stop music fadeout 5.0

    "«Я тебя запомнил», — говорили эти водянистые глаза."

    window hide
    $ renpy.pause(0.2)
    scene bg_classroom base2:
        xpos -3911 + 1920 + 300
    with Dissolve(0.4)
    $ renpy.pause(0.5)

    show black:
        alpha 0
        linear 1. alpha 1
    pause 1.5

    $ renpy.pause(delay=1, hard=True)

    scene bg_notebook with Dissolve(1)
    stop fon fadeout 3.0
    window show
    play music "music/40_Imminence.ogg" volume 0.65 fadein 3.0
    play sound "sounds/Page.ogg"

    "Уже пару уроков спустя я увидел в своей тетради растекавшийся амёбой желтоватый плевок."

    $ add_text_to_dictionary(27)

    "Позже в столовой Семён, вроде бы случайно, облил меня {u}компотом{/u}."
    "А выходя из туалета, он так тряхнул мокрыми руками, что морось попала мне в лицо."

    scene bg_koridorchic_day:
        ypos 0
        xpos 0
        ease 6.0 xpos -400
    with Dissolve(0.5)
    play test_one "sounds/steps/steps_shool.ogg" loop

    "Перед последним уроком Семён вдруг толкнул меня в толпу воркующих одноклассниц."

    scene bg_kate_attacked at hpunch2
    show layer master:
        align (.5, .5)
        zoom 1.05
    with hpunch
    play sound "voice/kate/04A KA.ogg"
    stop test_one fadeout 0.5
    play test_two "sounds/pushed.ogg"

    "Они с руганью расступились, а я, не удержавшись, ткнулся лицом в грудь той важной девочке, которую раньше принял за старосту."

    scene bg_koridorchic_day:
        ypos 0
        xpos 0
    with Dissolve(0.5)

    $ music_during_lines = 0.75
    voice "voice/kate/04 KA.ogg"
    Kate "Ай!"

    show Kate Shame m_day 00 norm ahead:
        alpha 0.0
        yoffset 170
        ease 1 yoffset 100 alpha 1.0
    pause 0.5

    play test_one "sounds/steps/Kait_stop.ogg"

    "Я тут же отпрянул, сгорая от стыда."

    voice "voice/anton/2day/043. Prosti ti v.ogg"
    Ant "Прости, ты в порядке?"




    play sound "voice/kate/05 KA.ogg"
    Kate "Я..."

    play test_one "voice/kate/05A KA.ogg"

    show Kate Block m_day 00 evil ahead 01
    with Dissolve(0.3)

    "Неожиданно она подбоченилась."

    show Kate Scream m_day 00 evil ahead
    with Dissolve(0.3)

    voice "voice/kate/06 KA.ogg"
    Kate "Нет, ну вы посмотрите на него!"

    voice "voice/kate/07 KA.ogg"
    Kate "Облапал меня прямо у всех на глазах!"

    voice "voice/kate/08 KA.ogg"
    Kate "Я сейчас всё маме расскажу!"

    show Kate Block m_day 00 evil ahead 02
    with Dissolve(0.3)

    voice "voice/kate/09 KA.ogg"
    Kate "Тебя из школы выгонят, извращенец!"




    "В её глазах было какое-то садистское веселье, словно во взгляде ребёнка, подносящего горящую спичку к беззащитному майскому жуку."

    voice "voice/anton/2day/044. Ya nechayanno.ogg"
    Ant "Я нечаянно! Меня толкнули..."

    show Kate Scream m_day 00 evil ahead
    with Dissolve(0.3)

    voice "voice/kate/10 KA.ogg"
    Kate "Все видели! Слепых среди нас нет!"

    show Kate Hee m_day 00 evil ahead 01
    with Dissolve(0.3)

    "Она уставилась на мои очки и радостно осклабилась."

    play test_one "sounds/sfx_footsteps_fat_boy_3.ogg"
    play test_two "voice/semen/2day/25 Smen.ogg"

    "Ярость вскипела в груди, но гогот Семёна охладил мой пыл."


    show Semen Disgust m_day 00 evil ahead 02:
        xzoom -1.0
        xpos -500
        yoffset 80
    with Dissolve(0.5)

    voice "voice/semen/2day/10 Tolk.ogg"
    Sem "Толкнули? Чё, правда?"

    show Semen Disgust m_day 00 evil ahead 01 with Dissolve(0.3)

    "Он подошёл вальяжно, окутывая запахом семечек и гнилых зубов, а затем резко сбил меня с ног."

    scene bg_koridorchic_day:
        ypos 0
        xpos 0
    show Kate Hee m_day 00 evil ahead 01:
        yoffset 100
    show layer master:
        align (.5, .5)
        zoom 1.05
    with hpunch
    play test_one "sounds/sfx_fall.ogg"

label bunny_day2_semen:
    scene bg_shcool_hall_down
    show layer master:
        align (.5, .5)
        zoom 1.05
    with hpunch
    show sema upper_02:
        xpos -800
        ypos 740
        ease 0.8 xpos 0 ypos 0
    with Dissolve(0.5)
    $ renpy.start_predict_screen("day2_choice_fight_or_submit")
    $ renpy.start_predict("bunny2_fight_sema")
    $ renpy.start_predict("sema fight")
    play test_one "sounds/Semen.ogg"

    voice "voice/semen/2day/11 Vot.ogg"
    Sem "Вот так, да? И чё ты сделаешь?"

    "Хулиган нависал надо мной, всем своим видом как бы говоря:"
    "«Ну же! Давай, ударь меня! Попробуй!»"


    window hide
    call screen forced_pause_delay(.8)
    hide sema upper_02

    $ story_manager.MarkEvent(("day2", "semen"))

    call screen day2_choice_fight_or_submit()


label bunny2_semen_fight:
    $ renpy.stop_predict_screen("day2_choice_fight_or_submit")
    $ renpy.stop_predict("bunny2_fight_sema")

    $ story_manager.MarkEvent(("day2", "semen", "fight"))

    $ Flags.Raise("fight")
    show sema upper_02
    window show

    voice "voice/anton/2day/048. Slushai ti.ogg"
    Ant "Слушай, ты..."

    "В горле пересохло, губы не слушались, и голос мой походил скорее на сдавленный писк."

    show sema upper_04
    with Dissolve(0.3)

    "Семён издевательски улыбнулся."

    voice "voice/semen/2day/12 Dava.ogg"
    Sem "Давай-давай, продолжай, очкарик."

    voice "voice/semen/2day/13 CZo p.ogg"
    Sem "Чё примолк-то?"

    voice "voice/semen/2day/14 Nam.ogg"
    Sem "Нам всем очень интересно."

    voice "voice/anton/2day/049. Esle eshe hot raz.ogg"
    Ant "Если ещё хоть раз меня тронешь..."

    "Семён медленно оттопырил палец и ткнул меня в лоб."

    play test_one "sounds/sfx_clicks_4.ogg"
    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/15 Nu t.ogg"
    Sem "Ну тронул, и чё?"

    voice "voice/anton/2day/50.1Eshohotraz.ogg"
    Ant "Ещё хоть раз..."

    play test_one "sounds/sfx_clicks_1.ogg"
    hide sema upper_04
    play test_six "voice/anton/2day/50.2.ogg"
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/16 Tron.ogg"
    Sem "Тронул."

    play test_one "sounds/sfx_clicks_2.ogg"

    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/17 A vo.ogg"
    Sem "А вот ещё."

    play test_one "sounds/sfx_clicks_3.ogg"
    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/18 I escz.ogg"
    Sem "И ещё!"

    play test_one "sounds/sfx_clicks_4.ogg"
    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/19 I escz.ogg"
    Sem "И ещё!"

    play test_one "sounds/sfx_clicks_2.ogg"
    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04

    voice "voice/semen/2day/20 I escz.ogg"
    Sem "И ещё!"

    "Он тыкал пальцем с такой силой, что моя голова отлетала назад."
    "Только бы не расплакаться."
    "Иначе — труба!"

    play test_one "sounds/sfx_clicks_3.ogg"
    hide sema upper_04
    show sema punch_01
    $ renpy.pause(0.60, hard=True)
    show sema upper_04
    stop music fadeout 3.0

    voice "voice/semen/2day/21 CZe t.ogg"
    Sem "Чё ты мне сделаешь, мямля?"

    "В глазах помутилось."
    "Я рванулся вперёд, так что подошвы отклеились от пола.."
    "И махнул наугад кулаком."

    window hide
    hide sema upper_04
    play test_one "sounds/sfx_punch.ogg"
    play test_two "sounds/piano-hit-3.ogg"
    play test_three "voice/anton/2day/051. Anton kick.ogg"
    show sema fight
    $ renpy.pause(3.0, hard=True)
    hide sema fight
    show sema upper_05
    window show
    $ renpy.stop_predict("sema fight")

    "Картина, открывшаяся моему взору, была прекрасной и ужасающей одновременно."
    $ achievement_grant("ach_force")
    "Семён держался за ушибленное ухо и изумлённо моргал."
    "Неужели я был первым, кто взбунтовался против его абсолютной власти?"

    show sema_friend1 at for_sema_friend1
    show sema_friend2 at for_sema_friend2

    play sound "voice/romka/2day/03 Stope.ogg"
    play test_four "sounds/steps/shagi.ogg"

    "Надо было бежать, но меня обступили его дружки."

    show sema upper_06 with Dissolve(0.3)

    voice "voice/kate/11 KA.ogg"
    Kate "Лилия Павловна!"

    voice "voice/kate/12 KA.ogg"
    Kate "Лилия Павловна, Петров Бабурина ударил!"

    "Щёки Семёна стали ещё краснее, а прыщи побелели, словно головки личинок."
    "Но на губах промелькнула ухмылка, замеченная лишь мною в этом стане врага."

    hide sema upper_06
    show sema upper_07
    with Dissolve(0.3)
    play test_one "sounds/Semen.ogg"
    play music "music/Phrases_06(loop).ogg" fadein 1

    "Он подошёл вплотную. Обдал кариозной вонью."

    voice "voice/semen/2day/23 Tebe.ogg"
    Sem "Тебе..."

    voice "voice/semen/2day/24 Pizd.ogg"
    Sem "...пиздец."

    "Голос у него был злым и опасным, точно кастрюля с бурлящим жиром, с которой сорвало крышку."

    play test_three "sounds/serdtse.ogg" loop

    "Я ждал удара."
    "Считал толчки сердца и гадал, куда угодит кулак."
    "В солнечное сплетение? В челюсть? В нос?"

    play test_one "sounds/sfx_footsteps_fat_boy_2.ogg"
    stop music fadeout 1
    stop test_three fadeout 1

    "А он просто развернулся и ушёл."

    scene bg_shcool_hall_down with Dissolve(0.5)

    "Мысль, холодная, трезвая и удивительно спокойная, вспыхнула в голове:"

    play test_five "sounds/gong-echo-2.ogg"

    "Сегодня меня убьют."

    jump bunny2_meet_pol

label bunny2_meet_pol:
    $ story_manager.MarkEvent(("day2", "scene6"))

    scene bg hall_day_before_choice:
        ypos 0
        xpos -250
    with Dissolve(1.5)

    play test_four "sounds/school_004.ogg" loop

    "После занятий я специально задержался подольше в коридоре, чтобы не идти вместе со всеми."
    "Семён не появился на последнем уроке, и это вселяло надежду: вдруг он решил избежать дежурства и смотался домой, забыв обо мне?"

    if Flags.Has("fight"):
        "Как смертник, узнавший, что казнь откладывается на день, я облегчённо выдохнул."
        "Но не позволил себе забыть его тон, мстительный взгляд и наэлектризованную пугающую ухмылку."
    else:
        "Это радовало: не хватало ещё встретить его в пустом коридоре."
        "Перед глазами перевёрнутыми подковами плыли ухмылки одноклассников."
        "Издевательство надо мной изрядно повеселило класс, и те, кто его прозевал, просили у свидетелей в красках описать произошедшее."
        "Нужно было отправить меня в школу для уродов, где среди горбатых, хромых и трёхногих я бы особо не выделялся."

    "Пока школьники с шумом и смехом расходились по домам, я встал у окна и сделал вид, что перебираю учебники."
    "Я напряжённо всматривался в окно."
    "Во дворе и на участке у школьных ворот Семёна не было."
    "Я не очень-то верил в такое везение, так что решил перестраховаться и немного потоптался в стремительно пустеющем коридоре."

    stop test_four fadeout 1.5
    play fon "sounds/loop_corridor.ogg" fadein 0.5

    "Шум ушёл на первый этаж."
    "Из кабинета биологии выглядывал скелет, которому какой-то шутник натянул на голову кепку с американским кондором."
    "За дверями туалетов журчала вода."
    "Я остался один в целой школе."

    stop fon fadeout 1.0
    play music "music/43_Kontakt.ogg" fadein 1.0

    "«Не один!» — пришла внезапная мысль."

    scene bg hall_day_before_choice:
        ypos 0
        xpos -250
        ease 5 xpos -2319

    "Я вспомнил о пропавшем мальчике — его портрет сейчас висел на доске у расписания."

    label rebenok:
    scene bg_propalrebenok2
    show ef_scrap
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)
    label test_polina:

    "Вспомнил, что он улыбается..."
    "...и что он смотрит на меня..."
    "...и что он, скорее всего, уже мёртв."

    stop music fadeout 1.0

    voice "voice/Polina/2day/1 Privet.ogg"
    Noname "Привет!" with vpunch

    scene bg hall_day_before_choice:
        xpos -400
    show bg_white
    with Dissolve(0.5)

    "Я вздрогнул и обернулся."

    window hide
    play music "music/29_Polina.ogg" volume 0.7 fadein 2.0
    show Polina:
        xalign 0.5
        ypos -2800
        alpha 0.0
        ease 4.6 ypos -1300 alpha 1.0
    $ renpy.pause(5.0, hard=True)
    window show

    "Сначала мой взгляд упёрся в чёрный футляр для скрипки."

    label doehal_1:
    show Polina:
        xalign 0.5
        ypos -1300
        alpha 1.0
        ease 6.0 ypos 140

    "Потом я заметил, что его держит девочка из моего класса."

    window hide

    show Polina:
        ease 0.5 ypos 140

    $ renpy.pause(delay=1, hard=True)

    hide bg_white
    hide Polina
    show Polina1:
        xalign 0.5
        ypos 140
        alpha 1.0
    with Dissolve(0.5)
    window show

    "На уроках она сидела за второй партой второго ряда, несколько раз я ловил на себе её взгляд." id doehal_1_6a66d915

    show Polina Front b_day 02 norm aside 01
    hide Polina1
    with Dissolve(0.3)

    "И сам украдкой смотрел на неё."
    "Просто иногда приятно посмотреть на что-то красивое: на ручей, небо или на девочку, которая не гогочет со всеми хором над шуточками Семёна."
    "Не перешёптывается с Катей, поливая грязью одноклассниц."
    "Все перемены она проводила так же, как и я, — оставалась в классе и либо глядела в окно, либо рисовала что-то в зелёном блокноте."

    hide Polina
    show Polina Front b_day 02 norm aside_to_ahead 01
    with Dissolve(0.3)

    voice "voice/anton/2day/052. Zdravstvui.ogg"
    Ant "Здравствуй!"

    "Я покраснел и притворился, что рассматриваю узор на дощатом полу."

    if Flags.Has("fight"):
        show Polina Front b_day 01 angry ahead 09 with Dissolve(0.3)

        voice "voice/Polina/2day/02 Kruto ti emu.ogg"
        Noname "Круто ты ему врезал!"

        show Polina Front b_day 01 norm ahead 01 with Dissolve(0.3)

        voice "voice/anton/2day/053.Eto vishlo slych.ogg"
        Ant "Это вышло случайно. Почти."

        "Я стал рассеянно складывать учебники в рюкзак, чтобы хоть чем-то себя занять."
    else:

        show Polina Front b_day 02 sadly ahead 02 with Dissolve(0.3)

        voice "voice/Polina/2day/40 Ya videka.ogg"
        Noname "Я видела, как Бабурин тебя толкнул."

        show Polina Front b_day 02 sadly ahead 03 with Dissolve(0.2)
        show Polina Front b_day 01 sad ahead 02 with Dissolve(0.2)

        voice "voice/Polina/2day/41 Ti v poryadke.ogg"
        Noname "Ты в порядке?"

        show Polina Front b_day 01 sad ahead 03 with Dissolve(0.2)

        "Шишка немного побаливала, но не она доставляла мне неприятности."

        show Polina Front b_day 01 norm ahead 01 with Dissolve(0.3)

        voice "voice/anton/2day/Vporyadke.ogg"
        Ant "В порядке."

        show Polina Front b_day 01 norm ahead 03 with Dissolve(0.3)

        voice "voice/anton/2day/Pustyak.ogg"
        Ant "Пустяк."

        show Polina 3_4 b_day 01 alert ahead 012 with Dissolve(0.3)

        voice "voice/Polina/2day/42 Aga.ogg"
        Noname "Ага, пустяк!"

        show Polina 3_4 b_day 01 alert ahead 011 with Dissolve(0.2)
        show Polina 3_4 b_day 01 alert ahead 012 with Dissolve(0.2)

        voice "voice/Polina/2day/43 Etot.ogg"
        Noname "Этот придурок последнее время совсем распоясался."

        show Polina Front b_day 01 angry ahead 03 with Dissolve(0.2)
        show Polina Front b_day 01 angry ahead 08 with Dissolve(0.2)

        voice "voice/Polina/2day/44 Vrezal.ogg"
        Noname "Врезал бы ты ему."

        show Polina Front b_day 02 norm ahead 03 with Dissolve(0.3)

        play sound "voice/anton/2day/054. Ya zamich.ogg"

        "Я замычал."

    hide Polina
    show Polina Front b_day 01 norm ahead_to_aside 02
    with Dissolve(0.2)

    voice "voice/Polina/2day/03 Vrode semen.ogg"
    Noname "Вроде Семён раньше таким не был."

    show Polina Front b_day 01 norm aside 03 with Dissolve(0.2)
    show Polina Front b_day 01 norm aside 02 with Dissolve(0.2)

    voice "voice/Polina/2day/04 On k nam.ogg"
    Noname "Он к нам недавно перевёлся."

    show Polina Front b_day 01 norm aside 03 with Dissolve(0.2)
    hide Polina
    show Polina Front b_day 01 norm aside_to_ahead 02
    with Dissolve(0.2)

    voice "voice/Polina/2day/05 Babushka.ogg"
    Noname "Бабушка его мне по секрету сказала, что он словно взбесился..."

    show Polina Front b_day 01 norm ahead 03 with Dissolve(0.2)
    show Polina Front b_day 01 norm ahead 02 with Dissolve(0.2)

    if Flags.Has("fight"):
        voice "voice/Polina/2day/06 Semena daze.ogg"
        Noname "Семёна даже старшеклассники побаиваются, представляешь?"

        show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
        show Polina 3_4 b_day 00 norm ahead 06 with Dissolve(0.2)

        voice "voice/Polina/2day/07 A ti vot.ogg"
        Noname "А ты вот молодец."

        show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
        show Polina 3_4 b_day 00 norm ahead 06 with Dissolve(0.2)

        voice "voice/Polina/2day/08 Ne strusil.ogg"
        Noname "Не струсил."

        show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.3)

        play test_two "voice/anton/2day/054. Ya zamich.ogg"

        "Я замычал."
        "Ага, конечно, нашла смельчака!"
        "Герой, что уже полчаса торчит у окон, лишь бы ему по шапке не дали."
    else:

        show Polina Front b_day 01 norm ahead 02 with Dissolve(0.2)
        "Я стал рассеянно складывать учебники в рюкзак, чтобы хоть чем-то себя занять."

    "Девочка смотрела на меня чистыми внимательными глазами."

    show Polina Front b_day 01 norm ahead 02 with Dissolve(0.3)

    voice "voice/Polina/2day/09 A ti za rekoi.ogg"
    Noname "А ты за рекой живёшь?"

    show Polina Front b_day 01 norm ahead 01 with Dissolve(0.2)
    show Polina Front b_day 01 norm ahead 02 with Dissolve(0.2)

    voice "voice/Polina/2day/10 V tom dome.ogg"
    Noname "В том деревянном доме?"

    show Polina Front b_day 01 norm ahead 01 with Dissolve(0.2)

    voice "voice/anton/2day/055. Nu da.ogg"
    Ant "Ну да..."

    show Polina Front b_day 01 sad ahead 02 with Dissolve(0.2)

    voice "voice/Polina/2day/11 Tam navernoe.ogg"
    Noname "Там, наверное, страшно."

    show Polina Front b_day 01 sad ahead 01 with Dissolve(0.2)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(0.2)

    voice "voice/Polina/2day/11 Da esche.ogg"
    Noname "Да ещё и через лес идти..."

    show Polina Front b_day 01 sad ahead 01 with Dissolve(0.2)
    show Polina Front b_day 01 sad ahead 02 with Dissolve(0.2)

    voice "voice/Polina/2day/12 Ya bi tak.ogg"
    Noname "Я бы так не смогла."

    hide Polina
    show Polina Front b_day 01 sad ahead_to_aside 03
    with Dissolve(0.3)

    "Упоминание о лесе заставило меня поёжиться."
    "Я подумал о переплетённых ветках, о змеящейся тропинке, о бесконечной темноте, что разрасталась как лишайник среди косых деревьев."
    "И выдал самую настоящую ложь:"

    hide Polina
    show Polina Front b_day 01 sad aside_to_ahead 03
    with Dissolve(0.3)

    voice "voice/anton/2day/56 Da ne tak uzh.ogg"
    Ant "Да не так уж там и страшно."

    show Polina Front b_day 01 sad ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/56.2 A chto tebya.ogg"
    Ant "А что тебя так пугает?"

    "Немного помолчав, она вдруг улыбнулась."

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.3)

    "Словно смахнула наваждение."

    show Polina 3_4 b_day 00 norm ahead 06 with Dissolve(0.2)

    voice "voice/Polina/2day/13 Da tak.ogg"
    Noname "Да так... Ничего."

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
    show Polina 3_4 b_day 00 norm ahead 06 with Dissolve(0.2)

    voice "voice/Polina/2day/14 Menya kstati.ogg"
    Pol "Меня, кстати, Полина зовут."

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/057. A menya Anton.ogg"
    Ant "А меня — Антон."

    show Polina Front b_day 02 norm ahead 08 with Dissolve(0.2)

    voice "voice/Polina/2day/15 Nu eto ya znayu.ogg"
    Pol "Ну это я знаю."

    if Flags.Has("fight"):

        show Polina Front b_day 02 norm ahead 01 with Dissolve(0.2)

        Pol "..."

        hide Polina
        show Polina Front b_day 02 norm ahead_to_aside 02
        with Dissolve(0.3)

        voice "voice/Polina/2day/16 Slushai.ogg"

        Pol "Слушай, Антон..."

        show Polina Front b_day 02 norm aside 04 with Dissolve(0.2)

        play test_two "voice/Polina/3day/01 HeHe.ogg"
        "Полина замялась, будто решая, стоит ли продолжать."

        hide Polina
        show Polina Front b_day 02 norm aside_to_ahead 02
        with Dissolve(0.3)

        voice "voice/Polina/2day/17 A chto ti.ogg"
        Pol "А что ты делаешь после школы?"

        hide Polina
        show Polina Front b_day 02 norm ahead_to_aside 01
        with Dissolve(0.3)

        "От её невинного вопроса кольнуло в груди, но как-то по-особенному приятно."

        show black:
            alpha 0.0
            linear 5.0 alpha 1.0
        show bg_white1:
            alpha 0.0
        hide Polina
        show Polina Front b_day 02 norm aside 01
        stop music fadeout 5.0

        voice "voice/anton/2day/058. Nichego takogo.ogg"
        Ant "Ничего такого..."

        hide Polina
        show Polina Front b_day 01 norm aside_to_ahead 01
        with Dissolve(0.3)

        "Я запнулся, не закончив фразу."

        play music2 "music/24_Fox.ogg" fadein 2.0
        window hide
        hide Polina
        show polina_lisa_02
        with Dissolve(2.0)
        hide polina_lisa_02
        show polina_lisa_03
        with Dissolve(2.0)
        hide polina_lisa_03
        with Dissolve(1.0)
        show showB
        $ renpy.pause(3.0)
        show polina_lisa_04
        with Dissolve(0.5)
        $ renpy.pause(2.0)
        hide polina_lisa_04
        show polina_lisa_05
        with Dissolve(1.0)
        hide polina_lisa_05
        show polina_lisa_06
        with Dissolve(1.0)
        hide polina_lisa_06
        show Fox Normal b_night 00 good ahead
        with Dissolve(1.0)

        "Перед глазами мелькнула хищная улыбка на маске Алисы."
        "Её насмешливые глаза в прорезях маски, которые я, скорее всего, сам себе придумал."
        "Неужели эта девочка-лисица и правда ждёт меня после школы?"
        "Или это была её очередная странная шутка?"
        "Интересно, прячет ли она большой рыжий хвост под своей шубкой?"

        show showC

        "От этой мысли я вдруг покрылся мелкой испариной, как после нормативов по физкультуре."

        show showD
        show showE
        show bg_white1:
            alpha 0.0
            linear 5.0 alpha 1.0

        "Захотелось принять душ, словно сами размышления о лисичке делали меня грязным, пачкали, сбивали с дороги и уводили в объятия леса."

        stop music2 fadeout 3.0
        $ renpy.pause(1.5)
        play music "music/29_Polina.ogg" volume 0.7 fadein 2.0
        scene bg_white with Dissolve(0.5)
        scene bg hall_day_before_choice:
            ypos 0
            xpos -250
        show Polina 3_4 b_day 00 norm ahead 06
        with Dissolve(1.5)
        window show

        voice "voice/Polina/2day/18 Y meanya seychas.ogg"
        Pol "У меня сейчас занятие — скрипка, — а потом я свободна."

        show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
        show Polina 3_4 b_day 00 norm ahead 06 with Dissolve(0.2)

        voice "voice/Polina/2day/19 Ded mne.ogg"
        Pol "Дедушка мне репетитора нанял."

        show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
        show Polina 3_4 b_day 00 norm ahead 03 with Dissolve(0.2)

        voice "voice/Polina/2day/20 Nash uchitel.ogg"
        Pol "Наш учитель музыки — он же скрипач, а здесь, в посёлке, ему некому преподавать... Только мне."

        show Polina 3_4 b_day 03 norm ahead 01 with Dissolve(0.3)

        "Она махнула в воздухе свободной рукой, имитируя движение смычка по скрипичным струнам."

        show Polina 3_4 b_day 02 norm ahead 06 with Dissolve(0.3)

        "Я почти услышал музыку."

        show Polina 3_4 b_day 02 norm ahead 01 with Dissolve(0.3)

        "Алису я выбросил из головы."

        show Polina Front b_day 01 norm ahead 01 with Dissolve(0.3)

        "Смотрел на губы Полины, ловя каждое слово, и замирал от непривычных ощущений."
        "Они были тёплыми, согревающими."

        show Polina Front b_day 01 norm ahead 04 with Dissolve(0.3)

        "А ещё щекотными."
        "И казалось, что я — маленький, а чувства — очень большие, и им тесно внутри."

        hide Polina
        show Polina Front b_day 01 serious ahead_to_aside 02
        with Dissolve(0.3)

        voice "voice/Polina/2day/21 Tut govoryat.ogg"
        Pol "Тут говорят, что у нас в посёлке маньяк завёлся."

        show Polina Front b_day 01 serious aside 03 with Dissolve(0.2)
        hide Polina
        show Polina Front b_day 01 serious aside_to_ahead 02
        with Dissolve(0.3)
        stop music fadeout 2.5

        voice "voice/Polina/2day/22 Ranshe.ogg"
        Pol "Раньше со школы меня всегда дедушка забирал, но в последнее время ему нездоровится."

        show Polina Front b_day 01 sad ahead 03 with Dissolve(0.2)

        "Я бросил беглый взгляд на фотографию Вовы."

        play test_one "sounds/4.vova04-echo.ogg"
        window hide
        scene bg_propalrebenok2 with Dissolve(0.5)
        window show

        "Глаза-колодцы изучали меня, рот был словно бы напомажен чёрным."

        play music "music/43_Kontakt.ogg" fadein 1.0

        "Как портрет на могильной плите."

        stop music fadeout 2.0
        scene bg hall_day_before_choice:
            ypos 0
            xpos -250
        show Polina Front b_day 01 norm aside 02
        with Dissolve(0.5)
        play music2 "music/30_(Tiny_Bunny).ogg" volume 0.6 fadein 2.0

        voice "voice/Polina/2day/24 Ti ne.ogg"
        Pol "Ты не подумай, я не трусишка, просто..."

        show Polina Front b_day 01 norm aside 03 with Dissolve(0.2)
        hide Polina
        show Polina Front b_day 01 norm aside_to_ahead 02
        with Dissolve(0.3)

        voice "voice/Polina/2day/25 Prosto mne.ogg"
        Pol "Просто мне кажется, что с тобой будет безопаснее."

        show Polina Front b_day 01 norm ahead 03 with Dissolve(0.2)
        show Polina Front b_day 01 sad ahead 08
        with Dissolve(0.3)

        voice "voice/Polina/2day/26 Anton ti.ogg"
        Pol "Антон, ты сможешь проводить меня до дома?"

        show Polina Front b_day 01 sad ahead 04
        with Dissolve(0.3)

        "Вот оно!"
        "Наконец всё, о чём я читал этим летом в приключенческих романах, о чём тайно грезил, начинало просачиваться в мою жизнь..."
        "Таинственное преступление, прекрасная незнакомка и героическая дуэль."
        "Дуэль..."

        hide Polina
        show Polina Front b_day 01 norm ahead_to_aside 01
        with Dissolve(0.3)
        stop music2 fadeout 5.0
        play test_one "music/Phrases_06.ogg"
        play music "music/31_FearTheMind_final.ogg" volume 0.6 fadein 7.0

        "Мысли о Семёне моментально отрезвили, вернули на землю, и почва под ногами зашаталась, как палуба корабля."
        "Только бы сейчас не упасть в грязь лицом перед Полиной."
        "Ведь сколько бы я ни храбрился, было очевидно и мне, и ей: выстоять в драке против такого амбала мне не под силу."
        "И если он и нокаутирует меня – это не самое страшное."
        "Страшно, что это увидит Полина."

        show Polina Front b_day 01 norm aside 04 with Dissolve(0.3)

        "Засмеётся со всеми остальными..."
        "Нет, нужно избавить свидетелей от моего позора."

        hide Polina
        show Polina Front b_day 01 norm aside_to_ahead 03
        with Dissolve(0.3)

        voice "voice/anton/2day/59 Segonya vryad li.ogg"
        Ant "Сегодня вряд ли получится."

        show Polina Front b_day 01 serious ahead 03 with Dissolve(0.3)

        voice "voice/anton/2day/59.2 You know.ogg"
        Ant "Ты же знаешь: Семён, скорее всего, караулит на школьном дворе."

        stop music fadeout 2.0

        voice "voice/anton/2day/60. Better mne.ogg"
        Ant "Лучше мне с ним разобраться лично, по-мужски."

        show Polina Front b_day 01 serious ahead 010 with Dissolve(0.3)

        voice "voice/Polina/2day/27 Gluposti kakie.ogg"
        Pol "Глупости какие."

        show Polina Front b_day 01 serious ahead 03 with Dissolve(0.2)
        show Polina 3_4 b_day 02 norm ahead 010 with Dissolve(0.3)
        play music "music/29_Polina.ogg" volume 0.8

        "Полина отбросила чёлку со лба, и до меня донёсся едва уловимый аромат ежевики."

        show Polina 3_4 b_day 02 norm ahead 01 with Dissolve(0.3)

        "Полина была водой, которую хотелось пить, – глотаешь жадно, а жажда всё не утоляется."
        "Я вспомнил летние вечера на даче, едкий дым костра, свисающую из-за ограды соседскую ягоду и мягкий ковёр сосновых иголок под подошвой."

        show Polina Front b_day 01 norm ahead_to_aside 01 with Dissolve(0.3)

        "Редкие безмятежные дни, когда я чувствовал себя в безопасности."

        hide Polina
        show Polina Front b_day 01 norm aside_to_ahead 01
        with Dissolve(0.3)

        "Мама отдыхает в гамаке, отец нанизывает мясо на шампуры."

        show Polina Front b_day 01 smile ahead 01 with Dissolve(0.3)

        "Мог ли я при желании различить в треске углей, в смехе родителей, в запахе скоротечного июля намёк на будущую катастрофу?"

        show Polina Front b_day 01 norm ahead 01 with Dissolve(0.3)

        "Видел ли я, как хрупок и ненадёжен тот мир?"

        show Polina Front b_day 01 angry ahead 011 with Dissolve(0.3)

        voice "voice/Polina/2day/28 Dumaesh.ogg"
        Pol "Думаешь, этот дикарь будет честно драться?"

        show Polina Front b_day 01 angry ahead 03 with Dissolve(0.3)
        $ renpy.pause(0.3)
        show Polina Front b_day 01 angry ahead 011 with Dissolve(0.3)

        voice "voice/Polina/2day/29 So svoimi.ogg"
        Pol "Со своими дружками набросятся всем скопом, опомниться даже не дадут."

        show Polina Front b_day 01 serious ahead 07 with Dissolve(0.3)

        "Полина вдруг хитро улыбнулась."

        show Polina Front b_day 01 serious ahead 09 with Dissolve(0.2)

        voice "voice/Polina/2day/30 No esli mi.ogg"
        Pol "Но если мы пойдем вместе, это их ошарашит."

        show Polina Front b_day 01 serious ahead 01 with Dissolve(0.2)
        show Polina Front b_day 01 serious ahead 012 with Dissolve(0.3)

        voice "voice/Polina/2day/31 Ya ze ne tolko.ogg"
        Pol "Я же не только первая скрипка на деревне — я ведь ещё и девочка!"

        show Polina Front b_day 01 serious ahead 01 with Dissolve(0.2)
        show Polina Front b_day 01 serious ahead 09 with Dissolve(0.2)

        voice "voice/Polina/2day/32 Slishala.ogg"
        Pol "Слышала от знакомого хулигана, что он никогда не нападает на кого-то в присутствии девушки."

        show Polina Front b_day 01 serious ahead 01 with Dissolve(0.2)
        show Polina Front b_day 01 serious ahead 012 with Dissolve(0.2)

        voice "voice/Polina/2day/33 Predstavlyaesh.ogg"
        Pol "Представляешь, у них кодекс чести такой!"

        show Polina Front b_day 01 serious ahead 01 with Dissolve(0.3)

        "«Знакомый хулиган?» – забеспокоился я."
        "Лучше ли он меня? Симпатичнее?"

    play test_one "sounds/bell.ogg"
    show Polina 3_4 b_day 05 worry ahead 06 with Dissolve(0.3)

    voice "voice/Polina/2day/34 Oi mne.ogg"
    Pol "Ой, мне на музыку пора."

    play test_one "sounds/steps/Polina_step_01.ogg"
    show Polina 3_4 m_day 01 norm ahead 010:
        yoffset 120
    with Dissolve(0.3)

    "Она сделала пару шагов и остановилась."
    "Удивительно, Полина совсем не похожа на тех красоток с журнальных постеров или на актрис из кинофильмов."

    show Polina 3_4 m_day 01 norm ahead 01 with Dissolve(0.3)

    "Но в свете потрескивающих ламп она была притягательнее их всех."

    show Polina Front m_day 01 norm ahead 011 with Dissolve(0.3)

    voice "voice/Polina/2day/35 A ti.ogg"
    Pol "А ты играешь на чём-нибудь?"

    show Polina Front m_day 00 norm ahead 01 with Dissolve(0.3)

    "Два года назад мне купили гитару."
    "Я живо вспомнил свои жалкие попытки научиться музицировать."
    "Am-Em... Перемен, мы ждём перемен..."

    $ add_text_to_dictionary(14)

    "Песня {u}Цоя{/u} точно ложилась на мои мысли и на желание изменить хоть что-то."
    "Та гитара запропастилась куда-то, словно напрочь отказалась переезжать в старый дом у леса."
    "Наверное, родители отдали инструмент кому-то, кому он нужнее."

    voice "voice/anton/2day/61. Uvy ne.ogg"
    Ant "Увы, не играю."

    show Polina Front m_day 00 sadly ahead 02 with Dissolve(0.3)

    voice "voice/Polina/2day/36 Eh.ogg"
    Pol "Жалко."

    show Polina 3_4 m_day 06 norm ahead 010 with Dissolve(0.3)
    pause 0.2
    show Polina 3_4 m_day 06 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/2day/37 Nu ladno.ogg"
    Pol "Ну ладно. Я побежала."

    show Polina 3_4 m_day 05 norm ahead 01 with Dissolve(0.2)
    pause 0.2
    show Polina 3_4 m_day 05 norm ahead 07 with Dissolve(0.2)

    voice "voice/Polina/2day/38 Poka.ogg"
    Pol "Пока!"

    window hide

    hide Polina with Dissolve(1.0)

    window show

    "Крик девочки подхватило гулкое эхо."

    play test_one "sounds/steps/Polina_step_02.ogg"

    "Туфли застучали по школьным коридорам."

    stop music fadeout 2.0

    voice "voice/anton/2day/62.Poka.ogg"
    Ant "Пока."

    "Не уверен, услышала ли Полина."
    "Я снова посмотрел в окно."

    if Flags.Has("fight"):
        play music2 "music/33_Symphony Of Extinct Lights.ogg"

        "Школьный двор опустел — только пара ребят из младших классов кидали друг в друга снежки."
        "Никого похожего на грузного Семёна с его компанией не было видно."
        "Это вселяло надежду."
        "Что же делать?"
        "Полина могла бы стать моим другом – первым на новом месте!"
        "И потом ей и впрямь могла угрожать встреча с маньяком, а тут я – защитник, рыцарь..."
        "И пускай последнее внутренний голос подвергал сомнению и шептал о побеге – подальше от убийц, от рыскающих по ночным лесополосам маньяков."
        "Полина стоила риска."
        "Но и рыжая плутовка манила тайной."
        "Обещала помочь найти Вову, а за этим следует награда."
        "Много денег – почти гарантия мира в семье."
        "Подарки для Оли..."

        $ add_text_to_dictionary(15)

        "Я вообразил сестру, счастливую, как те девочки, получающие призы от {u}Супонева{/u} в телепередаче «Звёздный час»."

        $ add_text_to_dictionary(21)

        "Её кружат в танце известные певцы, может, даже эта новая популярная группа, {u}«Иванушки International»{/u}."
        "Мама с папой обнимаются в останкинском павильоне."

        label polfox_test:

        "А потом мы всей семьёй едем в Диснейленд."

        jump bunny_day2_polina_or_fox
    else:
        jump bunny2_solo_win



label bunny_day2_polina_or_fox:
    window hide


    show bg hall_day_before_choice:
        xpos -250
        ypos 0
        xpos -250
        ease 1.8 xpos -400

    $ renpy.pause(delay=1.8, hard=True)

    show bg hall_day_before_choice:
        xpos -400
    show bg_hall_day_choice:
        xpos -400

    $ story_manager.MarkEvent(("day2", "waifu"))
    $ story_manager.MarkEvent(("day2", "la waifu"))

    call screen day2_choice_polina_or_fox

    label bucket_see:
        $ story_manager.MarkEvent(("day2", "la waifu", "bucket"))
        if not SceneFlags.Seen('bucket'):
            play test_one "sounds/vedro_2.ogg"
            "Брошенное кем-то цинковое ведёрко с притаившейся на дне тряпкой было до краёв наполнено мутной канализационной водой."
            "От него исходил какой-то химически-солоноватый смрад, причём с такой страшной силой, что меня затошнило. Я отшатнулся, про себя молясь избежать участи дежурного."
            $ true_detective_count2 += 1
        else:
            "Смердящее ведёрко."
        call screen day2_choice_polina_or_fox
    label airplane_see:
        $ story_manager.MarkEvent(("day2", "la waifu", "airplane"))
        if not SceneFlags.Seen('airplain'):
            play test_one "sounds/samolet_2.ogg"
            "«Хочешь узнать, кто дурак — переверни меня». Готов поспорить, с обратной стороны точно такая же острота."
            "Интересно, долго бы Семён крутил такую бумажку, попадись она ему в руки?"
            $ true_detective_count2 += 1
        else:
            "Самолётик."
        call screen day2_choice_polina_or_fox
    label shoes_see:
        $ story_manager.MarkEvent(("day2", "la waifu", "shoes"))
        if not SceneFlags.Seen('shoes'):
            play test_one "sounds/Sumka_2.ogg"
            "На подоконнике кто-то оставил сменную обувь — пару потёртых «шанхаек». Судя по размеру, они явно принадлежат мальчику моего возраста."
            $ true_detective_count2 += 1
        else:
            "Сменка."
        call screen day2_choice_polina_or_fox


label bunny2_fox_win:
    $ story_manager.MarkEvent(("day2", "waifu", "fox"))
    $ Flags.Raise("day2 fox")

    scene bg hall_day_before_choice:
        xpos -400
    show fox_window:
        xpos -400
    with Dissolve(1.0)
    window show
    play test_one "sounds/sfx_zip.ogg"
    stop music2 fadeout 2.0

    "Застегнув рюкзак, я сбежал вниз по ступенькам."
    $ achievement_grant("ach_adventure")

    window hide
    play test_two "sounds/Anton-school-run-1.ogg"
    scene bg_black with Dissolve(0.5)
    $ renpy.pause(3.0)
    scene bg school_day:
        yalign 0.8 xalign 0.5
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)
    $ renpy.pause(1.0)
    window show

    "Снова оценил обстановку во дворе — уже через окна вестибюля."

    stop music fadeout 3.0
    play music2 "music/26_Mistik.ogg" volume 0.7 fadein 5.0

    "Никого подозрительного."

    play test_two "sounds/school_door-close-2.ogg"

    "Входные двери скрипнули. Звук напомнил музыку из триллера — такая высокая нота, предшествующая напряжённой сцене."
    "Я шустро обогнул школу, стараясь не попасться никому на глаза."
    "Из школьной столовой пахло выпечкой и жжёным сахаром."
    "Я замер, увидев силуэт в окне второго этажа: наверное, это Полина, чуть склонив голову, скользила смычком по скрипке."
    "Жаль, мелодию не слышно, да и Полина – просто тёмный абрис, рисунок на жёлтом листе окна."

    play test_one "sounds/steps/asphalt-walk-2.ogg" loop

    "Нехотя я пошёл дальше."

    window hide
    if Flags.Has("myth2"):
        scene bg school_corner_day_onshow_snowpile_myth
    else:
        scene bg school_corner_day_onshow_snowpile
    show layer master:
        align (.5, .5)
        zoom 1.05
    stop test_one fadeout 6
    $ renpy.pause(8.0, hard = True)
    window show

    "На школьном стадионе верёвочная сетка футбольных ворот вздувалась и опадала."



    "Ветер гонял по полю белые смерчи."
    "Где-то неподалёку шумел невидимый трактор, спугнувший стаю каркающих ворон."


    "Звук мотора напомнил рёв голодных зверей, гнавшихся за мной по снежным пустошам."
    "Вновь вспомнилась эта странная Алиса со своей маской."
    "Сейчас, при свете дня, было очень трудно поверить в её существование."
    "Как она там сказала?"
    "На заднем дворе... возле повешенного..."
    "Что за ерунда? Какого ещё..."

label bunny_nearschool_day2_prepare:
    $ SceneFlags.Reset()
    $ story_manager.MarkEvent(("day2", "la corner"))




label bunny_nearschool_day2:
    if not SceneFlags.Has("witness2 school"):
        scene bg school_corner_day2:
            xpos 0
        show school_coner_01:
            xpos 0
    else:
        scene bg school_corner_day1:
            xpos 0
        show school_coner_01:
            xpos 0

    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05
    window hide
    call screen school2_near

label bunny2_school_near2:
    window show

    $ story_manager.MarkEvent(("day2", "la corner", "witness"))

    voice "voice/anton/2day/Ezvinite.ogg"
    Ant "И-извините?"

    scene bg school_corner_day1:
        xpos 0
    show school_coner_01:
        xpos 0
    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(.3)

    "Силуэт скрылся за углом и зашагал вглубь школьного тупичка."
    "Следом за ним растаял сигаретный дым."
    "Это был кто-то из взрослых. Может, учитель?"

    $ true_detective_count2 += 1
    $ Flags.Raise("witness2 school")
    $ SceneFlags.Raise("witness2 school")
    play test_one "sounds/sfx_man_walks_away.ogg"
    jump bunny_nearschool_day2

label bunny2_school_near4:
    $ story_manager.MarkEvent(("day2", "la corner", "hangman"))

    play test_one "sounds/sfx_chalk_2.ogg"
    window show
    if SceneFlags.Seen("hangman"):
        "Повешенный."
    else:
        if not SceneFlags.Seen("witness2 school"):
            scene bg school_corner_day1:
                xpos 0
            show school_coner_01:
                xpos 0
            if Flags.Has("myth2"):
                show day2_myth:
                    xpos 0
            show layer master:
                align (.5, .5)
                zoom 1.05
            with Dissolve(.3)
        "Я посмотрел на стену: над просмоленной полосой был нарисован пляшущий в петле человечек."
        "Кто-то играл здесь в «Виселицу»."
        "Вокруг человечка каракули: «ПОБЕГ», «СТРАХ», «ПРАВДА»."

        voice "voice/Alisa/Alisa2day/114 Blize.ogg"
        Noname "Ближе, мой сладкий..."

        "Я не сразу понял, откуда звук."
        "Взгляд заметался по безлюдному закутку на задворках школы, по окнам, отражающим солнечный свет, по снегу."

        $ true_detective_count2 += 1

    jump bunny_nearschool_day2

label bunny2_school_near5:
    $ story_manager.MarkEvent(("day2", "la corner", "niddle"))

    play test_one "sounds/sfx_syringe_4.ogg"
    window show
    if SceneFlags.Seen("niddle"):
        "Шприц."
    else:
        "Использованный шприц затесался среди окурков... Надеюсь, кому-то просто понадобился укол инсулина."
        $ true_detective_count2 += 1
    jump bunny_nearschool_day2

label bunny2_school_near6:
    $ story_manager.MarkEvent(("day2", "la corner", "squirrel"))

    play test_one "sounds/sfx_squirrel_eats.ogg"
    window show
    if SceneFlags.Seen("squirrel"):
        "Белка."
    else:
        "Вон лесная белка задорно лузгает семечки. Видать, кто-то из учеников её прикормил. Надо же."
        $ true_detective_count2 += 1
    jump bunny_nearschool_day2


label bunny2_school_near1:
    $ story_manager.MarkEvent(("day2", "scene7"))
    if not SceneFlags.Has("witness2 school"):
        scene bg school_corner_day3:
            xpos 0
    else:
        scene bg school_corner_day1:
            xpos 0
    scene bg school_corner_day1:
        xpos 0
    show school_coner_01:
        xpos 0
    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)
    stop music2 fadeout 3.0
    scene bg school_corner_day:
        xpos 0
    show school_coner_01:
        xpos 0
        linear 0.1 xpos 5
        linear 0.1 xpos -5
        pause 0.1
        linear 0.1 xpos 5
        linear 0.1 xpos -5
        pause 0.4
        linear 0.1 xpos 5
        linear 0.1 xpos -5
        pause 1.0
        linear 0.1 xpos 5
        linear 0.1 xpos -5
        pause 0.1
        linear 0.1 xpos 5
        linear 0.1 xpos -5
        pause .1
        repeat
    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05

    "Один из сугробов задрожал, словно вулкан перед извержением."


    play test_one "sounds/roll-hit-1.ogg"
    play test_two "voice/Alisa/Alisa2day/115 Otdai.ogg"
    show fox_boo
    play sound "sounds/iz_sugroba_1.ogg"
    $ renpy.pause(0.7)
    scene bg school_corner_day:
        xpos 0
    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    show Fox Normal m_day 00 good ahead
    show fox_boo_snow
    show layer master:
        align (.5, .5)
        zoom 1.05
    $ renpy.pause(0.6)
    hide fox_boo_snow
    window show

    Alis "Отдай своё сердце!"

    play music2 "music/23_Christmas.ogg" volume 0.75

    "Не успел я опомниться, как белая корка лопнула, и из-под снега выпрыгнула лиса."
    "Она грациозно поклонилась, наслаждаясь произведённым эффектом."
    "Снежок серебрился на её шубке."
    "Я не представлял, что мысли о хвостатых девочках могут быть такими... Даже не знаю, с чем и сравнить."
    "Заразными? Ядовито-сладкими?"

    voice "voice/Alisa/Alisa2day/116 Otpor.ogg"
    Alis "Отпор не дал — сердце потерял!"

    play sound "voice/Alisa/Alisa2day/117 Hihi.ogg"

    "Она хихикнула так задорно, что я невольно заулыбался."

    voice "voice/anton/2day/63. Da nu tebya.ogg"
    Ant "Да ну тебя!"

    show Fox Oh m_day 00 good ahead with Dissolve(0.5)

    "Резво зачерпнув горсть снега, я скатал снежок и зарядил им в Алису."

    show Fox Oh m_day 00 good ahead:
        ease 0.4 xoffset 95
        ease 0.2 xoffset 0
    pause 0.6
    play test_one "sounds/snowball_4.ogg"
    show Fox Oh m_day 01 good ahead:
        ease 0.1 yoffset 40
        pause 0.05
        ease 0.2 yoffset 0

    play sound "voice/anton/2day/64. Ona popitalas.ogg"

    "Она попыталась увернуться, но было поздно, — снаряд угодил в плечо."

    voice "voice/Alisa/Alisa2day/118 Ah ti.ogg"
    Alis "Ах ты ж! Гадкий мальчишка!"

    voice "voice/anton/2day/66. Da vot takoy ya.ogg"
    Ant "Да, вот такой я!"

    "Лиса плавно отпрянула, вооружаясь."

    hide Fox with Dissolve(0.7)

    voice "voice/Alisa/Alisa2day/119 Ti hiter.ogg"
    Alis "Ты хитёр, да мы хитрей!"

    voice "voice/Alisa/Alisa2day/120 Lovok.ogg"
    Alis "Ловок ты, да мы ловчей!"

    "Ответный снежок прочертил дугу между заснеженным двором и вороньём, реющим над нами."
    play sound "voice/anton/2day/66. Ya hotel prign.ogg"
    "Я хотел пригнуться, но поскользнулся и упал на колени."
    "А пока поднимался, снег прилетел прямо в лицо, опалил холодом щёки."

    play test_one "sounds/snowball_2.ogg"
    show fox_snowball_corner_splash with hpunch

    play sound "voice/anton/2day/67. Ot dosadi ya.ogg"

    "От досады я выругался на всю улицу."

    $ add_text_to_dictionary(16)

    play sound "voice/anton/2day/67. Slovechki.ogg"

    "Словечки из песен {u}«Сектора газа»{/u}, с кассет, что я слушал тайком от родителей."
    "Будь рядом папа, он выкрутил бы мне уши."
    "Чего-чего, а мата он не терпел, изъяснялся исключительно литературным языком."

    show Fox Flirt m_day good ahead 00 with Dissolve(0.5)

    voice "voice/Alisa/Alisa2day/121 Da ladno.ogg"
    Alis "Да ладно тебе."

    scene bg Fox_school with Dissolve(0.5)

    voice "voice/Alisa/Alisa2day/122 Ne bolno.ogg"
    Alis "Не больно же совсем."

    play test_one "sounds/stryahivanie_3.ogg"

    "Она сочувственно отряхнула мой воротник, взяла за локоть и помогла встать."

    scene bg school_corner_day:
        xpos 0
    if Flags.Has("myth2"):
        show day2_myth:
            xpos 0
    with Dissolve(0.5)

    "Аккуратно, с недетской заботливостью, сняла мои очки, сдула с них снежинки, а затем протянула обратно."

    show Fox Nice b_day good ahead 00 with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/123 Vot tak.ogg"
    Alis "Вот так, один-один, Тоша."

    "Тошей меня называли только близкие люди."
    "А я даже настоящего лица её не видел, не знал ни фамилии, ни класса, ни то, есть ли у неё хвост под шубкой."

    show Fox Feel m_day good ahead 00 with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/124 Zelaes.ogg"
    Alis "Желаешь отыграться?"

    voice "voice/anton/2day/68. Mi hoteli poiskat.ogg"
    Ant "Мы хотели поискать Вову, помнишь?"

    show Fox Fullface m_day 00 good ahead with Dissolve(0.3)

    voice "voice/anton/2day/69. Lucshe potorop.ogg"
    Ant "Лучше поторопиться, а то меня родители станут искать."

    play sound "voice/Alisa/Alisa2day/125 Zevok.ogg"

    "Лиса демонстративно зевнула:"

    show Fox Am m_day 00 with Dissolve(0.3)
    pause 0.1
    show Fox Fullface m_day 00 good ahead with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/125 Parents.ogg"
    Alis "Ро-ди-тели!"

    voice "voice/Alisa/Alisa2day/126 Kak skuchno.ogg"
    Alis "Как скучно! Да не будь таким занудой!"

    voice "voice/Alisa/Alisa2day/127 Davai.ogg"
    Alis "Давай чуть-чуть поиграем, всё равно тебе дома тоскливо."

    voice "voice/anton/2day/70. A ti otkuda znaesh.ogg"
    Ant "А ты откуда знаешь?"

    show Fox Normal m_day good ahead 00 with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/128 Toze mne.ogg"
    Alis "Тоже мне тайна."

    voice "voice/Alisa/Alisa2day/129 So vzrosl.ogg"
    Alis "Со взрослыми да в четырёх стенах — тоска смертная! Всегда!"

    voice "voice/Alisa/Alisa2day/130 Y menya.ogg"
    Alis "У меня от стен и взрослых нервный тик. Вот!"

    show Fox Normal m_day good ahead 00:
        ease 0.1 xoffset 15
        ease 0.1 xoffset 0
        ease 0.1 xoffset -30
        ease 0.1 xoffset 0
        ease 0.1 xoffset 15
        ease 0.1 xoffset 0
        ease 0.1 xoffset -30
        ease 0.1 xoffset 0
    pause 0.9

    "Она задёргала мохнатой лисьей бровкой."

    play sound "voice/anton/2day/71. Ya neiskrenne hohotnul.ogg"

    "Я неискренне хохотнул, не решив до конца, смешно ли это — вот так шевелить частями маски."

    show Fox Nice m_day good ahead 00 with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/131 Nu ze.ogg"
    Alis "Ну же, Тоша, решайся."

    voice "voice/Alisa/Alisa2day/132 Ya ze.ogg"
    Alis "Я же вижу, ты хочешь поиграть."

    voice "voice/Alisa/Alisa2day/133 I esli.ogg"
    Alis "И если победишь..."

    show Fox Nice b_day good ahead 00 with Dissolve(0.3)

    "Лисичка приблизилась вплотную и встала на цыпочки, едва не коснувшись шершавым носиком моего лица."
    "В глубине глаз тлели весёлые огоньки."
    "Пахло от неё чем-то приятным, ягодно-приторным."
    "Возможно, так пахнет независимость и настоящая свобода."
    "Когда у тебя всех хлопот — что беситься и уплетать конфеты."
    "Горячий шёпот влился в мои уши:"

    show Fox Flirt b_day good ahead 00 with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/134 Esli.ogg"
    Alis "Если победишь — буду твоим провожатым."

    voice "voice/Alisa/Alisa2day/135 Pover.ogg"
    Alis "Поверь, мне есть, что тебе показать..."

    show Fox Flirt b_day good ahead 00:
        ease 0.1 yoffset -20
        ease 0.1 yoffset 0
        ease 0.1 yoffset -20
        ease 0.1 yoffset 0

    voice "voice/Alisa/Alisa2day/136 Naidem.ogg"
    Alis "Хи-хи! Найдём твоего Вову!"

    "Внутри у меня сжалась пружина."
    "В животе заныло — не сказать, чтобы неприятно."
    "Как же странно: только что я болтал с Полиной, а теперь Алиса тащит куда-то."

    if Flags.Has("record"):
        "Чувство такое, будто я расщепляюсь, раздваиваюсь, как могильные кресты на той жуткой плёнке."

    voice "voice/anton/2day/72. A esli.ogg"
    Ant "А... а если проиграю?"

    show Fox Angry m_day 00 with Dissolve(0.5)

    voice "voice/Alisa/Alisa2day/137 Dushu.ogg"
    Alis "Душу из тебя выцарапаю, неженка!"

    show Fox Oh m_day good ahead 00:
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        repeat
    with Dissolve(0.5)

    voice "voice/Alisa/Alisa2day/138 Ahaha.ogg"
    Alis "А-ха-ха-ха-ха!"

    show Fox Normal m_day good ahead 00:
        yoffset 0
    with Dissolve(0.5)

    voice "voice/Alisa/Alisa2day/139 Skoree.ogg"
    Alis "Давай, скорей!"

    show Fox Normal m_day good ahead 00:
        linear 0.5 alpha 1.00 xoffset 150 + 10 yoffset 25
        linear 0.5 alpha 0.75 xoffset 200 + 80 yoffset 0
        linear 0.5 alpha 0.50 xoffset 260 + 120 yoffset 25
        linear 0.5 alpha 0.00 xoffset 340 + 150 yoffset 0
    stop music2 fadeout 4.0

    play sound "voice/Alisa/Alisa2day/139 Zasm.ogg"

    "Засмеявшись, она махнула подолом и побежала к дороге, по которой мы шли в школу."
    "Её обещание..."

    play music2 "music/33_Symphony Of Extinct Lights.ogg"  fadein 2.0
    "...чуть ли не угроза..."

    "...загипнотизировало меня."

    play test_one "sounds/sfx_snow_footsteps_0.ogg"

    "Я нагнулся и зачерпнул снег."
    "Вот было бы у меня специальное устройство, чтобы распознавать, когда шутит Алиса, а когда говорит всерьёз!"

    if Flags.Has("myth2"):
        scene bg school_corner_day_onhide_myth
    else:
        scene bg school_corner_day_onhide

    play test_two "sounds/steps/asphalt-walk-2.ogg" loop

    "Или у таких, как она, всегда — третий вариант?"

    label ttt:

    "Между шуткой и правдой, смехом и горячим дыханием на ухо..."
    "Я хотел победить."

    stop test_two fadeout 0.5

    "Наказать её за быстроту и свободу, которой слишком много для обычной девочки."
    "Азарт, любопытство и что-то ещё — что-то неясное — завладели моими чувствами, опьянили."

    $ add_text_to_dictionary(18)

    "Как тогда, когда я наелся вишен из маминой {u}наливки{/u}, и лежал, сомкнув веки, а кровать вращалась подо мной, и голова ходила кругом."

    play sound "voice/anton/2day/73. Ya splynul.ogg"

    "Я сплюнул, вытер губы."
    "Поиграть хочешь, лисичка-сестричка?"

    scene bg_white


    show bg school_day:
        zoom 1.0 xoffset -2000+960 yalign 0.8
        ease 4 zoom 0.5 xoffset 0 yalign 0.5
    play test_one "sounds/steps/steps_snow001.ogg"

    "Ну давай поиграем!"
    "Вооружившись снежком, я ринулся за беглянкой."

    play test_one "sounds/steps/loop_snow_footsteps.ogg" loop

    label test_run:
    scene bg_white2
    show bg_runaway1_rev:
        xzoom -1
    show bg_runaway2_rev:
        xzoom -1
    show anton_run_rev_snowball
    show runaway_snow1_rev:
        xzoom -1
    show runaway_snow2_rev:
        xzoom -1
    window hide
    pause 2

    "Вот показалась знакомая улица с деревянными столбами, уже совсем не страшными."
    "Всего-то брёвна, занесённые снегом. Крикнешь — залают цепные псы, люди высунутся в окна."
    "Фигурка Алисы маячила впереди, дразнилась, но швырять в неё снежком с такого расстояния было напрасно — только зря снаряд бы растратил."


    $ SetParSpeed(5)
    scene white
    show gohome01
    show gohome01_1
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    with Dissolve(0.5)


    "Вдоль расчищенной дороги замаячили искалеченные морозом берёзки."
    "У деревьев высился огромный снежный холм."
    "Видимо, сюда трактор свозил снег со всего посёлка. В такой горе спрячется целый выводок лисичек."
    "«{i}Нет{/i}, — подумалось, — {i}лисичка одна, не бывает второй. Её и одной-то слишком много{/i}.»"

    stop test_one fadeout 5.0
    scene bg_dog_06 with Dissolve(0.5)
    play test_one "sounds/sfx_dog_breathing_2.ogg" loop
    play test_two "sounds/sfx_dog_calling_one.ogg"

    "Возле рощицы бегала моя вторая утренняя знакомая — дворняга с озябшими лапками."

    stop music2 fadeout 3.0
    stop test_one fadeout 1

    "Принюхавшись, она пометила голые кусты смородины и шустро засеменила к другим."

    scene gohome_day_stop1 with Dissolve(0.5)
    show Fox Flirt m_day good ahead 00:
        xzoom -1.0
        alpha 0.0
        yoffset 70
        ease 0.5 yoffset 0 alpha 1.0
    pause 0.4
    play music "music/30_(Tiny_Bunny).ogg" volume 0.7 fadein 3.0
    play sound "voice/Alisa/Alisa2day/141 Alisa vin.ogg"

    "Алиса вынырнула из-за холма."

    voice "voice/Alisa/Alisa2day/140 Zulka.ogg"
    Alis "Жулька! За мной, девочка!"

    show Fox Flirt m_day good ahead 00:
        xzoom -1.0
        linear 0.25 alpha 1.00 xoffset -150 - 10 yoffset 25
        linear 0.25 alpha 0.75 xoffset -200 - 80 yoffset 0
        linear 0.25 alpha 0.50 xoffset -260 - 120 yoffset 25
        linear 0.25 alpha 0.00 xoffset -340 - 150 yoffset 0

    play test_one "sounds/sfx_dog_calling_two.ogg"

    "Собачонка подняла уши, одобрительно гавкнула и побежала следом."


    scene bg_white with Dissolve(0.3)
    $ SetParSpeed(10)
    show gohome01
    show gohome01_1
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    with Dissolve(0.5)
    play sound "voice/Alisa/Alisa2day/141 Mchalis.ogg"

    "Мы мчались всё дальше, изредка обмениваясь снежными залпами, хохоча и спотыкаясь."

    scene bg_white with Dissolve(0.3)
    scene gohome_day_stop2
    show Fox Fullface m_day good ahead 00:
        alpha 1.0 xoffset 0
    with Dissolve(0.5)

    "Впереди рос, поднимался до низких облаков зимний лес. Мы достигли его тени — костистой и почти осязаемой."



    show Fox Fullface m_day good ahead 00:
        linear 0.15 alpha 1.00 xoffset -170 - 15 yoffset 35
        linear 0.15 alpha 0.75 xoffset -230 - 85 yoffset 0
        linear 0.15 alpha 0.50 xoffset -290 - 130 yoffset 35
        linear 0.15 alpha 0.00 xoffset -350 - 155 yoffset 0

    "Лиса юркнула за исполинскую сосну, явно намереваясь незаметно подобраться ко мне со спины и насыпать снега за шиворот."

    play sound "sounds/sfx_dog_calling_one.ogg"
    scene bg_dog_07 with Dissolve(0.5)

    "Это был хороший план, но её выдавала Жулька, крутившаяся рядом."
    "Отломив сухую ветку, я решил действовать ещё хитрее."

    scene bg_forest_fox with Dissolve(0.3)

    "Насадил на сучок шапку и поднёс к сосне."
    "Пускай решит, что это моя голова высовывается из-за ствола."
    "Чтобы не рассмеяться, я прикусил губу. Прыгнул с другой стороны, пульнул снежком в упор."

    scene gohome_evning_stop
    show layer master:
        align (.5, .5)
        zoom 1.05
    show Fox Oh m_day good ahead 00
    with Dissolve(0.3)

    play test_one "sounds/snowball_4.ogg"
    show Fox Oh m_day good ahead 01:
        ease 0.1 yoffset 40
        pause 0.05
        ease 0.2 yoffset 0


    play sound "voice/Alisa/Alisa2day/141 Naverno.ogg"

    "Наверное, Алиса сразу раскусила мою уловку, но позволила мне победить со счётом 3-1."
    "Я был ранен в ногу, она же с «простреленным» животом и грудью истекала передо мной выдуманной кровью."

    show Fox Oh m_day good ahead 01 at sprite_happy_alltimes
    play sound "voice/Alisa/Alisa2day/142 I molila.ogg"

    "И молила о пощаде, давясь от смеха."

    voice "voice/Alisa/Alisa2day/142 Molu.ogg"
    Alis "Аха-ха-ха! Молю, сжалься."

    voice "voice/Alisa/Alisa2day/142 Pomirayu.ogg"
    Alis "Ха-ха! Помираю!"

    show Fox Oh m_day good ahead 01 at sprite_happy

    voice "voice/anton/2day/75. Da vse vse.ogg"
    Ant "Да всё-всё, живи!"

    show Fox Feel m_day 01 good ahead with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/143 Spasibo.ogg"
    Alis "Спасибо, добрый рыцарь!"

    show Fox Feel m_day 01 good ahead:
        alpha 1.0
        yoffset 0
        ease 0.5 yoffset 100 alpha 0.0


    "Она притворилась, что кланяется мне, схватила полные горсти снега и, как умирающий воин, в последней отчаянной попытке, метнула их в меня."

    play test_one "sounds/miss_1.ogg"
    show Fox Flirt m_day 001 good ahead:
        alpha 0.0
        yoffset 100
        ease 0.2 yoffset 0 alpha 1.0
    with Dissolve(0.3)
    stop music fadeout 4.0

    play sound "voice/anton/2day/76. Gogocha.ogg"
    play test_seven "voice/Alisa/Alisa2day/144 Ya legko.ogg"

    "Я легко уклонился. Гогоча и возмущаясь одновременно, добил воительницу двумя прицельными выстрелами." with hpunch

    play test_one "sounds/snowball_4.ogg"
    show Fox Flirt m_day 002 good ahead:
        ease 0.1 yoffset 40
        pause 0.05
        ease 0.2 yoffset 0
    pause 0.1
    play test_two "sounds/snowball_3.ogg"
    show Fox Flirt m_day 003 good ahead
    pause 0.2

    voice "voice/Alisa/Alisa2day/145 Zivizivi.ogg"
    Alis "Живи-живи..."

    voice "voice/Alisa/Alisa2day/145 Nauchil.ogg"
    Alis "Научил бы меня жить, раз умный такой."

    voice "voice/anton/2day/77. Molchi ti.ogg"
    Ant "Молчи! Ты умерла уже!"

    play music2 "music/24_Fox.ogg"

    voice "voice/Alisa/Alisa2day/146 Toze mne.ogg"
    Alis "Тоже мне помеха!"

    voice "voice/Alisa/Alisa2day/147 Davai.ogg"
    Alis "Давай сыграем в кое-что поинтереснее."

    show Fox Flirt m_day 003 good ahead:
        ease 0.1 yoffset 30
        pause 0.1
        ease 0.1 yoffset 0
    pause 0.15
    show fox_snowball
    hide Fox
    with Dissolve(0.3)
    play sound "sounds/iz_sugroba_1.ogg"
    play test_two "voice/Alisa/Alisa2day/148 Vistreliv.ogg"

    "Выстрелив вслепую, она кинулась за деревья."



    voice "voice/Alisa/Alisa2day/149 Razdva.ogg"
    Alis "Раз-два, прилети, сова."

    voice "voice/Alisa/Alisa2day/150 Trichetire.ogg"
    Alis "Три-четыре-пять, время поиграть."

    play test_one "sounds/steps/steps_snow001.ogg" fadein 1.0
    $ SetParSpeed(60)
    show gohome01_evning
    show gohome01_1_evning
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1

    "Я неуверенно двинулся к бурелому."

    voice "voice/Alisa/Alisa2day/151 Shest.ogg"
    Alis "Шесть да шесть, дыбом волчья шерсть."

    "Померещилось, что я действительно вижу хвост, скользнувший по кустам."
    "Будто привязанный, я бросился туда, где ветки схлёстывались, помогая Алисе прятаться."
    "Приходилось раздвигать их, рвать, точно паутину."
    "Ветви пружинили в лицо, но не били, а словно гладили по щекам."
    "Я вспотел, но сил оставалось предостаточно."
    "Врёшь, лисичка, поймаю тебя."
    "Голос Алисы плутал за буреломом."

    voice "voice/Alisa/Alisa2day/152 Semvosem.ogg"
    Alis "Семь-восемь, бьём копытом оземь..."

    voice "voice/Alisa/Alisa2day/153 Haha.ogg"
    Alis "Ха-ха-ха-ха-ха!"

    voice "voice/Alisa/Alisa2day/154 A ya tebya.ogg"
    Alis "А я тебя недооценила!"

    voice "voice/Alisa/Alisa2day/155 Dumala.ogg"
    Alis "Думала, ты просто мальчик!"

    scene d5_mwear_children_forest_bg
    show d5_mwear_children_play_10
    show d5_mwear_children_forest_fg zorder 1
    with Dissolve(.5)
    "Уверенный, что она стоит за чахлой осиной, я выскочил наперерез."

    hide d5_mwear_children_play_10
    show d5_mwear_children_play_9
    with Dissolve(.5)
    "Но здешняя акустика обманула — теперь её голос журчал слева:"

    hide d5_mwear_children_play_9
    show d5_mwear_children_play_11
    with Dissolve(.5)
    voice "voice/Alisa/Alisa2day/156 A ti.ogg"
    Alis "А ты – Зайчик!"

    hide d5_mwear_children_play_11
    show d5_mwear_children_play_9
    with Dissolve(.5)
    voice "voice/Alisa/Alisa2day/157 Shustr.ogg"
    Alis "Шустренький, хорошенький! Ха-ха!"

    play test_two "sounds/miss_2.ogg"

    hide d5_mwear_children_play_9
    show d5_mwear_children_play_10
    with Dissolve(.5)
    "Снежок вылетел из тёмного укрытия, просвистел над ухом."

    hide d5_mwear_children_play_10
    show d5_mwear_children_play_9
    with Dissolve(.5)
    voice "voice/anton/2day/77. Ya tebe dam.ogg"
    Ant "Я тебе дам зайчик!"

    hide d5_mwear_children_play_9
    show d5_mwear_children_play_11
    with Dissolve(.5)
    voice "voice/Alisa/Alisa2day/158 Dai mne.ogg"
    Alis "Дай мне зайчика, дай."

    hide d5_mwear_children_play_11
    show d5_mwear_children_play_10
    with Dissolve(.5)

    hide d5_mwear_children_play_10
    with Dissolve(.5)
    "Яркая лисья шуба мелькнула возле трухлявого пня."

    scene bg_white2 with Dissolve(0.2)
    $ SetParSpeed(10)
    show gohome01_evning
    show gohome01_1_evning
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    with Dissolve(0.2)

    "Я устремился туда, перепрыгивая через ров."

    voice "voice/Alisa/Alisa2day/159 Zaichik.ogg"
    Alis "Зайчик, выходи скорей, \nМясом накорми зверей!"

    "Самым важным для меня сейчас был меховой воротник, рыжеющий за очередным деревом."
    "Губа моя задрожала, как у настоящего загонщика, почуявшего добычу."
    "Рывок — и лиса в моих объятиях, такая гладкая и желанная."

    scene gohome_evning_stop
    show Fox Oh m_day good ahead 00
    with Dissolve(0.3)

    voice "voice/Alisa/Alisa2day/160 Vse v.ogg"
    Alis "Всё-всё-всё, ты победил!"

    show Fox Feel m_day 00 good ahead with Dissolve(0.3)

    play sound "voice/Alisa/Alisa2day/162 Zasopela.ogg"

    "Она прислонилась к шершавой коре, засопела:"

    stop sound fadeout 0.5

    voice "voice/Alisa/Alisa2day/163 Poz.ogg"
    Alis "Пожалуйста, давай немного отдохнём."

    voice "voice/Alisa/Alisa2day/164 Ti slishkom.ogg"
    Alis "Ты слишком быстрый, слишком сильный... лакомый слишком."

    show Fox Normal m_day 00 good ahead with Dissolve(0.3)

    "Довольный, я подбоченился в ожидании награды от побеждённой."

    show Fox Normal m_day 00 good ahead:
        ease 0.1 yoffset 30
        pause 0.1
        ease 0.1 yoffset 0
    pause 0.15
    show fox_snowball
    hide Fox
    with Dissolve(0.3)
    play sound "sounds/snowball_4.ogg"

    play test_one "voice/Alisa/Alisa2day/164 No vmesto.ogg"

    "Но вместо приза получил подлый снежок в своё напыщенное лицо."

    scene bg_white2 with Dissolve(0.2)
    $ SetParSpeed(4)
    show gohome01_evning
    show gohome01_1_evning
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    show gohome05
    show gohome05_1
    with Dissolve(0.3)
    play test_one "sounds/steps/loop_snow_footsteps.ogg" loop
    play sound "voice/Alisa/Alisa2day/165 Zal.ogg"

    "Заливаясь хохотом, хитрейшая из хитрейших рванула прочь, а я даже не думал сердиться."
    "Во что бы то ни стало надо догнать Алису, опрокинуть её, оседлать."
    "Сорвать с неё маску и увидеть всё!"

    scene bg_white2
    show bg_runaway1_rev:
        xzoom -1
    show bg_runaway2_rev:
        xzoom -1
    show anton_run_rev
    show runaway_snow1_rev:
        xzoom -1
    show runaway_snow2_rev:
        xzoom -1
    window hide
    pause 2
    stop test_one fadeout 4

    voice "voice/Alisa/Alisa2day/166 Bend.ogg"
    Alis "Бедный зайчик прыгает..."

    voice "voice/Alisa/Alisa2day/166 Vozle.ogg"
    Alis "Возле мокрых сосен..."

    voice "voice/Alisa/Alisa2day/166 Strashno.ogg"
    Alis "Страшно в лапы волку серому попасть..."

    voice "voice/Alisa/Alisa2day/166 Dumaet o lete.ogg"
    Alis "Думает о лете, прижимает уши..."

    voice "voice/Alisa/Alisa2day/166 Na nebo.ogg"
    Alis "На небо косится — неба не видать..."

    "Небо действительно исчезло за навесом крон."
    "Я ориентировался по лаю глупой Жульки, что не отставала от хозяйки."
    "И настигал."
    "А под ногами мелькала та самая тропинка, что я представлял в школе."

    scene bg_white2 with Dissolve(0.2)
    $ SetParSpeed(10)
    show gohome01_evning
    show gohome01_1_evning
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    with Dissolve(0.2)

    "Оказывается, нестись во весь опор так легко."
    "{i}Скорее! Выше! Быстрее!{/i}"
    "Мне казалось, внутри отворился какой-то потаённый ларец с новыми возможностями."
    "Мои мышцы гудели, лёгкие увеличились, а я сам будто стал сильнее."
    "Даже зрение обострилось: я видел каждую оледенелую веточку, каждую зазубрину на коре."
    "У кустов валялось что-то пёстрое – деталь одежды."
    "Ещё одно цветастое пятно справа."
    "Алиса скидывала с себя вещи на бегу. Как шкуру."
    "И я, окрылённый, стащил зубами варежки."
    "Раздеться полностью и отдаться ветру до остатка!"
    "{i}Скорее!!!{/i}"
    "Я потянулся сбросить шапку, махом откинуть всё, что мешает бежать по нескончаемому лесу."

    play sound "sounds/slip_and_fall_2.ogg"

    "Рюкзак тормозил – я швырнул его в снег, вместе со всеми ручками и карандашами в пенале, цветными тетрадями в линейку и клетку, со всеми рисунками на полях и динозавром для Оли..."

    stop music2 fadeout 3.0
    play music "music/25_Olya.ogg" volume 0.8 fadein 3.0

    "Оля!"
    "И вдруг в голове возник отчётливый образ:"

    window hide
    scene bg_white with Dissolve(1.0)
    pause 0.5
    scene bg kitchen1_0
    show kitchen ol3_0_1
    show ramka1
    with Dissolve(0.7)
    window show

    "Сестра, застывшая у окна в предзакатном свете."
    "Маленькие детские ладошки прижались к стеклу и, согрев его, отпечатались."
    "Она бы согрела так целый мир."
    "Оля смотрит на тайгу и повторяет моё имя."

    show kitchen ol3_1_1 with Dissolve(0.3)
    $ renpy.pause(0.35)
    show kitchen ol3_2_1 with Dissolve(0.3)

    voice "voice/olya/2day/01 Tosha.ogg"
    Oly "Тоша!"

    show kitchen ol3_1_1 with Dissolve(0.3)

    "Я остановился, глубоко вдохнув, и понял вдруг, как всё это сумасбродно и глупо – раздеваться в лесу догола в погоне за лисицей..."
    "Я вернулся за рюкзаком, будто за обронённой частью самого себя."
    "И снова вспомнил, как сестра не любила оставаться дома без меня, умоляла вернуться после школы как можно быстрее."
    "Что ж я за брат-то?!"
    "Бегаю по лесу, которым сам же пугал сестру."
    "Веселюсь, когда ей за порог запрещено выходить: сиди в клетке, Оль, и смотри в сотый раз одни и те же мультики."

    show kitchen ol3_2_1 with Dissolve(0.3)

    voice "voice/olya/2day/02 Tosha.ogg"
    Oly "Тоша!"

    show kitchen ol3_1_1 with Dissolve(0.3)

    voice "voice/anton/2day/78. Da olenka.ogg"
    Ant "Да, Оленька?"

    show kitchen ol3_2_1 with Dissolve(0.3)

    voice "voice/olya/2day/03 ToshaA.ogg"
    Oly "Тоша, а куда..."

    stop music
    play test_one "sounds/tydydym.ogg"
    show kitchen ol3_gop1 with Dissolve(0.3)
    $ renpy.pause(0.1)
    show kitchen ol3_gop with Dissolve(0.3)

    voice "voice/olya/2day/03 Kuda A.ogg"
    Oly "Куда так скачешь, чмошник?" id test_run_5e315b1b

    jump bunny_day2_gop_stop


label bunny2_semen_lose:
    $ story_manager.MarkEvent(("day2", "semen", "submit"))

    $ Flags.Raise("mask")
    $ renpy.stop_predict_screen("day2_choice_fight_or_submit")
    $ renpy.stop_predict("bunny2_fight_sema")
    $ renpy.stop_predict("sema punch_01")
    show sema upper_02
    window show
    play sound "voice/anton/2day/Vtyanul.ogg"

    "Я шумно втянул воздух. Встал, массируя затылок."

    show sema upper_04 with Dissolve(0.3)
    play test_two "voice/semen/2day/25 Smen.ogg"

    "Семён гримасничал, словно спрашивал беззвучно: «И что ты хочешь сделать?»"
    "Я посмотрел на его красные кулаки, казавшиеся мне в тот миг огромными, и понял: если скажу хоть слово — он ударит."

    show sema upper_02 with Dissolve(0.3)

    "Он будет бить, пока я не заплачу, пока не попрошу пощады, а может, и тогда не остановится."
    "И никто мне не поможет."

    show sema upper_01 with Dissolve(0.3)

    voice "voice/anton/2day/45 Prostite.ogg"
    Ant "Простите."

    voice "voice/anton/2day/45.2 Ya spotknulsya.ogg"
    Ant "Я споткнулся."

    "Какой жалкий писк."

    show sema upper_02 with Dissolve(0.3)

    "Если б можно было действительно загореться от стыда, я запылал бы сейчас, как головёшка в печи."

    voice "voice/kate/13 KA.ogg"
    Kate "Ходить нормально научись."

    play test_one "sounds/sfx_girl_walks_away1.ogg"
    show sema upper_04 with Dissolve(0.3)

    voice "voice/kate/14 KA.ogg"
    Kate "Слепошара."

    play sound "voice/semen/2day/Heh.ogg"

    "Опустив взгляд, я протиснулся мимо Семёна."

    show sema upper_02 with Dissolve(0.3)

    "Он обдал меня кариозной вонью."

    show sema upper_03 with Dissolve(0.3)

    voice "voice/semen/2day/26 Poka.ogg"
    Sem "Пока-пока, терпила."

    hide sema upper_03 with Dissolve(0.7)
    play test_one "sounds/sfx_nose_blow.ogg"

    "Толстяк смачно сморкнулся у меня за спиной."

    play test_one "sounds/sfx_back_rustle.ogg"
    play test_two "sounds/sfx_footsteps_fat_boy_2.ogg"

    "Мышцы мои одеревенели, и я почувствовал, как напоследок он вытер ладонь о мою спину."
    $ achievement_grant("ach_insulted")

    play test_three "sounds/steps/steps_shool.ogg" loop
    play test_one "sounds/sfx_boys_laugh_long.ogg"


    "Я побрёл дальше под издевательские смешки со всех сторон."
    play sound "sounds/sfx_boys_laugh.ogg"

    stop test_three fadeout 0.5

    "Всё было гораздо хуже, чем я предполагал накануне."
    "..."

    jump bunny2_meet_pol

label bunny2_solo_win:
    $ story_manager.MarkEvent(("day2", "scene8"))
    scene black with Dissolve(1.0)
    play fon "sounds/fon/La_00.ogg" volume 0.8 noloop fadein 3.0
    queue fon "sounds/fon/La_02.ogg" volume 0.8
    $ SetParSpeed(30)
    show bg_class_for_child1
    show bg_class_for_child2
    show children_in_class
    show bg_black:
        alpha 1.0
        ease 9.0 alpha 0.0

    "«Ой, извини!» - говорил Семён, толкая меня на лестнице, да так, что и шею недолго было сломать."
    "Или «Я случайно!», обливая меня компотом в столовой."
    "И так каждый день."
    "Ни на секунду я не мог расслабиться из-за потока «случайностей»."
    "И с ужасом понимал, что это только начало, а дальше будет хуже, но сделать уже ничего не мог."
    "Я ходил по школе, опустив глаза в пол, и считал минуты до конца уроков."

    scene bg_polina_look with Dissolve(0.5)

    "Лишь иногда, поймав на себе взгляд Полины, я задыхался от стыда, и готов был драться, но, как назло, ничего не происходило."

    stop fon fadeout 3.5

    "Потом запал кончался, и всё продолжалось по-старому."

    show bg school_day:
        zoom 1.0 xoffset -2000+960 yalign 0.8
        ease 4 zoom 0.5 xoffset 0 yalign 0.5

    play test_one "sounds/steps/steps_snow001.ogg"

    "Домой я ходил один."


    scene bg_white with Dissolve(0.3)
    $ SetParSpeed(30)
    show gohome01
    show gohome01_1
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1
    show gohome04
    show gohome04_1
    with Dissolve(0.5)

    play music "music/Morning Tensions.ogg" volume 0.75
    play test_seven "sounds/steps/loop_footsteps_one.ogg" loop

    "Сначала через посёлок, потом по мосту через реку и, наконец, через лес."
    "Минут десять дорога ползла между деревьями."
    "Прохожих не было, только иногда, будто боясь завязнуть в снегу, медленно проезжали машины."
    "Я старался идти как можно быстрее, потому что белые от снега ветки и чёрные стволы создавали странную иллюзию: казалось, кто-то бродит по лесу."
    "Кто-то высокий, неуловимый, готовый в любой момент вытянуться деревом или упасть на землю сугробом, а потом, когда внимание к нему ослабнет, вновь продолжить свой путь вдоль дороги."

    voice "voice/semen/2day/28 Nu z.ogg"
    Sem "Ну здорово, Антошка!"

    stop test_seven fadeout 2
    stop music fadeout 2

    "Сердце замерло."

    jump bunny_day2_gop_stop



label bunny2_polina_win:
    $ story_manager.MarkEvent(("day2", "waifu", "polina"))
    $ Flags.Raise("day2 polina")

    scene bg hall_day_before_choice:
        xpos -400
    show polina_door:
        xpos -400
    with Dissolve(1.)

    play music "music/37_Schumann - Sonata_No.1_Polina_00.ogg" volume 0.6 fadein 3.0
    stop music2 fadeout 2.0
    $ renpy.music.set_volume(0.6, channel='music2')

    "За окнами вился снежок, словно плясал в такт зазвучавшей из-за поворота музыке."



    scene bg hall_day_before_choice:
        ypos 0
        xpos -400
        ease 15 xpos -2319
    show polina_door:
        ypos 0
        xpos -400
        ease 15 xpos -2319

    "Я спрыгнул с подоконника и пошёл по коридору, снедаемый любопытством."
    "Полчаса, что я ждал здесь, проползли улиткой. Хотелось скорее увидеть Полину снова."

    $ renpy.music.set_volume(1.0, delay=3.0, channel='music2')

    "Музыка стала громче, она струилась из приоткрытых дверей в дальнем конце коридорного тоннеля."

    $ add_text_to_dictionary(19)

    "Мои музыкальные вкусы ограничивались {u}Летовым{/u} и Шевчуком, «Старыми песнями о главном», шлягерами по телевизору."
    "А также клипами, которые иногда записывали бонусом на видеокассеты для затравки перед фильмом."
    "Но мелодия скрипки пленила меня."

    stop fon fadeout 1.0
    scene bg hall_day_before_choice:
        ypos 0
        xpos -2319
        ease 15 xpos -400



    "Она казалась тончайшей резьбой по дереву ценной породы, хрустальной игрушкой, дуновением тёплого ветерка."
    "Я приник к дверному косяку."
    "Полина пряталась от меня в глубине класса, но её тень – тень девочки со скрипкой – падала на стену."
    "И столько грации было в движениях руки и смычка, что я будто поплыл на волнах музыки."
    "Сердце словно пробило преграду грудной клетки и понеслось вскачь."
    "Быстрее и быстрее по снежным просторам, скользя меж сосен к солнцу, пылающему над валежником."

    stop music2 fadeout 1.5
    play music "music/18_Olya_(piano&strings).ogg" volume 0.72
    scene bg hall_day_before_choice:
        ypos 0
        xpos -400
    show Polina Front b_day 01 smile ahead 08
    with Dissolve(0.5)

    voice "voice/Polina/2day/53 Zaskuchal.ogg"
    Pol "Заскучал?"

    show Polina Front b_day 01 smile ahead 01 with Dissolve(0.3)

    "Я погрузился в мысли с головой и не услышал шагов."
    "Искупавшаяся в музыке, Полина стала ещё волшебнее."

    voice "voice/anton/2day/80 Da net net.ogg"
    Ant "Да нет, нет."

    voice "voice/anton/2day/80.2 Ya mmm.ogg"
    Ant "Я... м-м-м..."

    voice "voice/anton/2day/81. Ya o komikse.ogg"
    Ant "Я о комиксе своём думал."

    "Зачем-то я соврал."

    show Polina Front b_day 02 smile ahead 02 with Dissolve(0.3)

    voice "voice/Polina/2day/54 Ti komiksi.ogg"
    Pol "Ты комиксы рисуешь?"

    show Polina Front b_day 02 smile ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/82 Da nu to est.ogg"
    Ant "Да, ну то есть..."

    voice "voice/anton/2day/82.2 Planiruy.ogg"
    Ant "Планирую рисовать."

    show Polina 3_4 b_day 00 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/2day/55 Aga.ogg"
    Pol "Ага!"

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.2)
    show Polina 3_4 b_day 00 norm ahead 03 with Dissolve(0.2)

    voice "voice/Polina/2day/55 I pro chto.ogg"
    Pol "И про что твой комикс?"

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.3)

    "Про самую очаровательную и добрую скрипачку, чудом оказавшуюся в этой обители страха."

    voice "voice/anton/2day/83. Pro lisu.ogg"
    Ant "Про лису."

    voice "voice/anton/2day/84.Oi.ogg"
    Ant "Ой, точнее про говорящих животных, что живут в лесу и помогают заблудившимся детям вернуться домой."

    voice "voice/anton/2day/85 A potom oni.ogg"
    Ant "А потом они..."

    voice "voice/anton/2day/85.2 Oni plyashut.ogg"
    Ant "...они пляшут в ночи."

    show Polina 3_4 b_day 02 norm ahead 03 with Dissolve(0.3)

    voice "voice/Polina/2day/56 Ogo.ogg"
    Pol "Ого!"

    voice "voice/Polina/2day/56 Kak interesno.ogg"
    Pol "Как интересно."

    voice "voice/Polina/2day/56 Sam pridumal.ogg"
    Pol "Сам придумал?"

    show Polina 3_4 b_day 00 norm ahead 01 with Dissolve(0.3)

    "Я опустил глаза."

    voice "voice/anton/2day/86. Vdohnovilsya.ogg"
    Ant "Вдохновился... глядя в окно."
    $ achievement_grant("ach_knigh")

    window hide
    scene bg_black with Dissolve(0.5)
    play test_one "sounds/sfx_walk_down_stairs.ogg"
    $ renpy.pause(3.0)




    window show

    "Мы спустились на первый этаж."

    play test_two "sounds/school_door-open-1.ogg"
    $ renpy.pause(1.5)
    play test_two "sounds/school_door-close-1.ogg"

    window hide
    scene bg school_day:
        yalign 0.8 xalign 0.5
    with Dissolve(0.5)
    $ renpy.pause(1.0)
    window show

    "Я отворил перед Полиной дверь – папа говорил, как важно быть джентльменом."

    show Polina Front m_day_winter 01 norm ahead 09:
        yoffset 100
    with Dissolve(0.5)

    voice "voice/Polina/2day/57 Znachit.ogg"
    Pol "Значит, творческая личность."

    show Polina Front m_day_winter 01 norm ahead 01 with Dissolve(0.2)
    show Polina Front m_day_winter 01 norm ahead 09 with Dissolve(0.2)

    voice "voice/Polina/2day/57 Ya dogad.ogg"
    Pol "Я догадывалась, что ты не такой, как все."

    show Polina Front m_day_winter 01 norm ahead 01 with Dissolve(0.2)
    show Polina Front m_day_winter 01 norm ahead 09 with Dissolve(0.2)

    voice "voice/Polina/2day/57 Osoben.ogg"
    Pol "Особенный."

    show Polina Front m_day_winter 01 norm ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/88 Shutish.ogg"
    Ant "Шутишь? Я?"

    show Polina Front m_day_winter 00 norm ahead 01 with Dissolve(0.5)

    voice "voice/anton/2day/88.2 Ya samiy.ogg"
    Ant "Я самый обыкновенный."

    show Polina 3_4 m_day_winter 07 norm ahead 012 with Dissolve(0.3)

    voice "voice/Polina/2day/58 Eto Semen.ogg"
    Pol "Это Семён обыкновенный..."

    show Polina 3_4 m_day_winter 07 norm ahead 011 with Dissolve(0.2)
    show Polina 3_4 m_day_winter 07 norm ahead 012 with Dissolve(0.2)

    voice "voice/Polina/2day/58 V smisle.ogg"
    Pol "В смысле, обычный придурок."

    show Polina 3_4 m_day_winter 03 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day_winter 03 norm ahead 06 with Dissolve(0.2)

    voice "voice/Polina/2day/58 A v tebe.ogg"
    Pol "А в тебе живёт нечто доброе и пушистое."

    show Polina 3_4 m_day_winter 01 norm ahead 01 with Dissolve(0.3)
    play test_two "sounds/sfx_dog_calling_one.ogg"

    "Что-то тявкнуло у ног, прерывая Полину, когда мы пересекали школьный двор."

    stop music fadeout 3
    show Polina 3_4 m_day_winter 07 worry ahead 012 at sprite_happy:
        yoffset 100


    voice "voice/Polina/2day/59 Ai.ogg"
    Pol "Ай!"

    show Polina 3_4 m_day_winter 07 worry ahead 011 with Dissolve(0.3)

    voice "voice/anton/2day/89. Ne boyisya.ogg"
    Ant "Не бойся, это Жулька!"

    scene bg_dog_08 with Dissolve(0.5)
    play test_one "sounds/sfx_dog_breathing_2.ogg"

    "Я встал на одно колено, почесал за ухо гавкающую собачонку."

    play music "music/17_Flow.ogg" volume 0.75 fadein 3
    play sound "sounds/sfx_dog_calling_one.ogg"

    "Она бешено виляла хвостом, будто это был пропеллер."

    window hide
    scene bg school_day:
        yalign 0.8 xalign 0.5
    show Polina 3_4 m_day_winter 07 alert ahead 011:
        yoffset 100
    with Dissolve(0.3)
    $ renpy.pause(0.4)
    window show
    scene bg school_day:
        yalign 0.8 xalign 0.5
        ease 1.0 xalign 0.2
        ease 2.0 xalign 0.8
        ease 1.0 xalign 0.5
    show Polina 3_4 m_day_winter 07 alert ahead 011:
        yalign 1.0 xalign 0.5
        yoffset 100
        ease 1.0 xoffset 500
        ease 2.0 xoffset -500
        ease 1.0 xoffset 0
    stop test_one fadeout 2

    "Я оглядел пришкольный участок, ожидая увидеть Алису."
    "Но девочки-лисы не было ни во дворе, ни на дороге."

    show Polina 3_4 m_day_winter 07 alert ahead 012 with Dissolve(0.3)

    voice "voice/Polina/2day/60 Bros.ogg"
    Pol "Брось её."

    show Polina 3_4 m_day_winter 07 alert ahead 011 with Dissolve(0.2)
    show Polina 3_4 m_day_winter 07 alert ahead 012 with Dissolve(0.2)

    voice "voice/Polina/2day/60 Ti chto.ogg"
    Pol "Ты что, она же дикая!"

    show Polina 3_4 m_day_winter 07 alert ahead 011 with Dissolve(0.2)
    show Polina 3_4 m_day_winter 07 alert ahead 012 with Dissolve(0.2)

    voice "voice/Polina/2day/60 Klesh.ogg"
    Pol "Клещей ещё подцепишь."

    show Polina 3_4 m_day_winter 07 alert ahead 011 with Dissolve(0.2)

    voice "voice/anton/2day/90 Net u nee.ogg"
    Ant "Нет, у неё хозяйка есть."

    voice "voice/anton/2day/90.2 Vrode.ogg"
    Ant "Вроде."

    show Polina 3_4 m_day_winter 07 alert ahead 08 with Dissolve(0.3)

    "Полина, поднеся ко рту платок, с неприязнью наблюдала за веселящейся псиной."

    show Polina 3_4 m_day_winter 07 alert ahead 011 with Dissolve(0.3)

    voice "voice/anton/2day/91. U tebya.ogg"
    Ant "У тебя никакой еды не завалялось?"

    show Polina 3_4 m_day_winter 03 alert ahead 06 with Dissolve(0.3)

    voice "voice/Polina/2day/61 Kazetsya.ogg"
    Pol "Кажется, что-то осталось."

    show Polina 3_4 m_day_winter 03 norm ahead 01 with Dissolve(0.3)
    show Polina 3_4 m_day_winter 03 norm ahead 03 with Dissolve(0.2)

    voice "voice/Polina/2day/61 Pokormim.ogg"
    Pol "Покормим и пойдём, ладно?"

    scene bg_dog_08
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)
    play test_one "sounds/sfx_dog_calling_two.ogg"

    "Она вынула из портфеля бутерброд, швырнула Жульке."

    play test_one "sounds/sfx_dog_breathing.ogg"

    "Собачонка накинулась на лакомство."
    "Отбросила носом хлеб и принялась за докторскую колбасу."

    voice "voice/anton/2day/92 kakaya privered.ogg"
    Ant "Какая привереда!"

    voice "voice/anton/2day/92.2 Esh vse.ogg"
    Ant "Ешь всё, давай!"

    play sound "sounds/Derg.ogg"

    "Полина дёрнула меня за рукав, поторапливая." with hpunch

    scene bg school_day:
        yalign 0.8 xalign 0.5
    show Polina Front b_day_winter 01 smile ahead 04
    with Dissolve(0.5)

    voice "voice/anton/2day/93. Ti chego.ogg"
    Ant "Ты чего?"

    show Polina Front b_day_winter 01 smile2 ahead 014 at sprite_happy_alltimes
    play sound "voice/Polina/2day/Hahaha.ogg" volume 0.75

    "Ответом был смех."

    hide Polina
    show Polina Front b_day_winter 01 smile ahead 04
    scene bg school_day_dog:
        yalign 0.8 xalign 0.5
    with Dissolve(0.5)

    "Скрипачка буквально выволокла меня за калитку, прыская в кулак."

    play test_one "sounds/steps/steps_snow001.ogg"
    pause 0.3
    window hide
    scene bg school_day_dog:
        zoom 1.0 xoffset -2000+960 yalign 0.8
        ease 4 zoom 0.5 xoffset 0 yalign 0.5

    pause 3
    window show

    "Я повернулся."

    stop sound fadeout 1
    play test_one "voice/Polina/2day/Ha.ogg" volume 0.75

    "Покинутая Жулька провожала нас обиженным взглядом, такая одинокая на фоне школы."

    scene bg_white
    $ SetParSpeed(120)
    show walking_fox_11_day
    show walking_fox_12_day
    show walking_fox_21_day
    show walking_fox_22_day
    show walking_fox_31_day
    show walking_fox_32_day
    show pol_walk_day_left
    show ant_walk_day_left
    stop test_one fadeout 0.5
    $ polina_face_state = 2
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop

    "И тут Полина перестала смеяться. Шла рядом отстранённая, с пустым взглядом."

    voice "voice/Polina/2day/62 Nechego.ogg"
    Pol "Нечего паразитов плодить!"

    "Замечание вышло достаточно резким."
    "Разве дворняжка виновата, что живёт на улице?"

    voice "voice/Polina/2day/63 Oni potom.ogg"
    Pol "Они потом на людей кидаются."

    $ polina_face_state = 4

    window hide
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
    play sound "sounds/loop_dogs_attack_on_man.ogg" fadein 4 loop
    voice "voice/Polina/2day/63 Proshloy.ogg"
    Pol "Прошлой зимой такая стая чуть дедушку не загрызла."
    play test_six "voice/Hariton/A-001.ogg"

    voice "voice/anton/2day/94. Kakoi.ogg"
    Ant "Какой кошмар!"
    stop sound fadeout 1
    stop test_six fadeout 1


    window hide
    hide old_movie_001_002
    show old_movie_001_002:
        .15
        linear 0.25 alpha 0.0
    hide flashback_dog_attack with Dissolve(.15)
    hide bg_white with Dissolve(.25)
    window auto

    stop test_seven fadeout 75
    voice "voice/anton/2day/94.2 Emu s.ogg"
    Ant "Ему с тех пор не здоровится?"

    $ anton_face_polwalk_state = 1

    voice "voice/Polina/2day/64 Ego.ogg"
    Pol "Его парализовало."

    voice "voice/Polina/2day/64 On.ogg"
    Pol "Он больше никогда не сможет ходить."

    $ polina_face_state = 3

    "Я с ужасом вспомнил стаю диких собак преследовавшую меня накануне."

    voice "voice/anton/2day/95. Mne ochen.ogg"
    Ant "Мне... мне очень жаль."

    $ anton_face_polwalk_state = 0

    voice "voice/Polina/2day/65 Nichego.ogg"
    Pol "Ничего."

    $ polina_face_state = 1

    "Полина вновь пленительно заулыбалась, прикрыв глаза."

    voice "voice/Polina/2day/66 Glavnoe.ogg"
    Pol "Главное, что мы друг друга поняли."

    stop music fadeout 3

    "После её слов я и думать забыл про Жульку."

    play music2 "music/Cinematic Piano.ogg" volume 0.72 fadein 3

    "Около ограды третьеклашки перебрасывались снежками и напевали звонко:"

    play test_two "voice/Child/2day/Child_02.ogg" volume 0.8
    Childs "Раз-два, прилети, сова..."

    "Сова?"

    window hide
    hide bg_white
    play sound "sounds/stick-echo-1.ogg"
    show bg_white with Dissolve(0.2)
    $ renpy.pause(0.3)
    show bg kitchen1_0
    show ramka1
    show kitchen ol3_0_1
    with Dissolve(0.3)
    window show

    "Оля!"
    "Вспыхнул образ сестры, скучающей у окна, высматривающей меня в сумерках."
    "Я пообещал себе, что не задержусь: провожу Полину — и сразу домой."

    hide bg_white
    hide bg kitchen1_0
    hide ramka1
    hide kitchen ol3_0_1
    with Dissolve(0.3)
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop

    voice "voice/anton/2day/96. A chto.ogg"
    Ant "А что это за песенку малые поют?"

    voice "voice/anton/2day/97. Uze.ogg"
    Ant "Уже второй раз за день её слышу."

    play test_three "sounds/fon/crow_wind.ogg" volume 0.75 fadein 1.0 loop

    "Мы шли по главной улице."

    play test_one "sounds/sfx_tractor_pass.ogg"

    "Где-то рядом бурчал, разгребая заносы, трактор."
    "В пепельном небе парили вороны."
    "Целая стая чёрных птиц рыскала над нами, напоминая жуткие кресты, сорвавшиеся с могил."

    voice "voice/Polina/2day/67 Pro sovu.ogg"
    Pol "Про сову?"

    voice "voice/Polina/2day/67 Eto.ogg"
    Pol "Это считалочка местная."

    voice "voice/Polina/2day/67 Mne.ogg"
    Pol "Мне её в детстве дедушка напевал."

    voice "voice/Polina/2day/67 On interes.ogg"
    Pol "Он интересуется историей края, много знает про наш фольклор."

    voice "voice/anton/2day/98. I chto tam za.ogg"
    Ant "И что там за считалочка такая?"

    voice "voice/Polina/2day/69 Slushai.ogg"
    Pol "Слушай!"

    "Она пошла спиной вперёд, смотря на меня и задорно улыбаясь."

    voice "voice/Polina/2day/70 Raz dva.ogg"
    Pol "Раз-два, прилети, сова."

    voice "voice/Polina/2day/70 Three.ogg"
    Pol "Три-четыре-пять, время поиграть."

    voice "voice/Polina/2day/70 Six.ogg"
    Pol "Шесть да шесть, дыбом волчья шерсть."

    voice "voice/Polina/2day/70 Seven.ogg"
    Pol "Семь-восемь, бьём копытом оземь."

    voice "voice/Polina/2day/70 Bear fox.ogg"
    Pol "Для медведя, для лисы..."

    voice "voice/Polina/2day/70 Bunny.ogg"
    Pol "... зайчик, кушать принеси!"

    "Я подумал, что одну лису встретил сегодня утром."
    "Хорошо, что не волка и не медведя."
    "Но, любуясь спутницей и странно смелея, вслух сказал совсем другое:"

    voice "voice/anton/2day/99. U tebya.ogg"
    Ant "У тебя красивый голос."

    "Полина кокетливо поправила чёлку."

    voice "voice/Polina/2day/71 Spasibo.ogg"
    Pol "Спасибо."

    voice "voice/anton/2day/100 I chto ze.ogg"
    Ant "И что же, это конец считалочки?"

    voice "voice/anton/2day/100.2 Prines im zayac.ogg"
    Ant "Принёс им заяц покушать или нет?"

    voice "voice/Polina/2day/72 Podi.ogg"
    Pol "Поди узнай."

    voice "voice/Polina/2day/73 Sprosit.ogg"
    Pol "Спросить не у кого — считалочка очень старая."

    voice "voice/Polina/2day/74 Drevnaya.ogg"
    Pol "Древняя даже."

    voice "voice/Polina/2day/75 S nei.ogg"
    Pol "С ней легенда одна связана."

    voice "voice/Polina/2day/76 Esli tebe.ogg"
    Pol "Если тебе интересно."

    voice "voice/anton/2day/101. Konechno.ogg"
    Ant "Конечно!"

    voice "voice/Polina/2day/77 Tut v taige.ogg"
    Pol "Тут, в тайге, раньше племена жили разные."

    voice "voice/Polina/2day/78 Dedushka.ogg"
    Pol "Дедушка говорит, у них была такая ициниа... исцинианция... короче, — такой ритуал, когда мальчику наступала пора становиться мужчиной."

    "Я навострил уши."
    "Ведь и мне скоро, не за горами... превращаться."

    stop music fadeout 3
    $ polina_face_state = 2
    play music2 "music/Khoomey Tale, intro.ogg" fadeout 1.5
    queue music2 "music/Khoomey Tale, looped.ogg"
    $ polina_face_state = 5

    voice "voice/Polina/2day/79 Young.ogg"
    Pol "Юношу отводили в лес, и он должен был три ночи провести там, охотясь."

    stop test_seven fadeout 35

    voice "voice/Polina/2day/80 Po legende.ogg"
    Pol "По легенде, один такой юноша ушёл в тайгу и пропал."

    voice "voice/Polina/2day/81 A vernulsya.ogg"
    Pol "А вернулся, когда его перестали искать."

    voice "voice/Polina/2day/82 Nagryanul.ogg"
    Pol "Нагрянул в деревню, исцарапанный, грязный, замёрзший."

    window hide
    stop test_three fadeout 1.5
    play fon "sounds/fon/wind_shooll.ogg" fadein 2.0
    scene bg_transition_01 with Dissolve(1.0)
    $ renpy.pause(3.5)
    window show

    "Я представил долгие ночёвки среди сосен и медвежьих берлог."

    voice "voice/Polina/2day/83 Rodnie.ogg"
    Pol "Родные выбежали к нему, а он упал на землю."

    scene bg_white
    $ SetParSpeed(120)
    show walking_fox_11_day
    show walking_fox_12_day
    show walking_fox_21_day
    show walking_fox_22_day
    show walking_fox_31_day
    show walking_fox_32_day
    show pol_walk_day_left
    show ant_walk_day_left
    show bg_shaman1
    show bg_shaman2
    with Dissolve(0.7)

    voice "voice/Polina/2day/84 Priveli.ogg"
    Pol "Привели шамана..."

    voice "voice/Polina/2day/85 Tot.ogg"
    Pol "Тот осмотрел молодого охотника и помрачнел."

    voice "voice/Polina/2day/86 Skazal.ogg"
    Pol "Сказал: плохи дела."

    voice "voice/Polina/2day/87 Du utra.ogg"
    Pol "До утра юноша бился в судорогах и повторял... эту считалочку."

    voice "voice/Polina/2day/88 Snova.ogg"
    Pol "Снова и снова."

    voice "voice/Polina/2day/89 Raz dva.ogg"
    Pol "«Раз-два, прилети, сова...» Будто ему в тайге нашептали."

    voice "voice/Polina/2day/90 A k rassvetu.ogg"
    Pol "А к рассвету он умер."

    voice "voice/Polina/2day/91 Tolko.ogg"
    Pol "Только вот шаман сказал, что он и так был мёртв, что он мёртвым из лесу пришёл и мёртвыми губами шептал считалочку."

    hide bg_shaman1
    hide bg_shaman2
    with Dissolve(0.7)
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop
    $ polina_face_state = 3

    "Я опешил."

    voice "voice/anton/2day/102. Eto tochno.ogg"
    Ant "Это точно не ужастик?"

    stop music fadeout 1.5

    voice "voice/Polina/2day/92 Folklor.ogg"
    Pol "Фольклор бывает пострашнее всякого кино, уж поверь!"

    voice "voice/Polina/2day/93 Dedushka.ogg"
    Pol "Дедушка говорит, что племя то собралось спешно и ушло на юг."

    play music2 "music/05 Color Of Silence.ogg" volume 0.5 fadeout 10

    voice "voice/anton/2day/103 Oni bili.ogg"
    Ant "Они были смелыми."

    voice "voice/anton/2day/103.2 Esli.ogg"
    Ant "Если жили здесь."

    play sound "sounds/snowball_3.ogg"

    "Полина пнула сугроб сапожком."

    voice "voice/Polina/2day/94 Smelimi.ogg"
    Pol "Смелыми и глупыми."

    voice "voice/Polina/2day/94 Neuzeli.ogg"
    Pol "Неужели надо мертвецу явиться из лесу, чтобы до людей дошло?"

    voice "voice/anton/2day/104. Doshlo chto.ogg"
    Ant "Дошло что?"

    voice "voice/Polina/2day/95 Chto nuzno.ogg"
    Pol "Что нужно уезжать отсюда."

    voice "voice/Polina/2day/95 Est.ogg"
    Pol "Есть целый мир."

    $ polina_face_state = 1

    voice "voice/Polina/2day/95 A est.ogg"
    Pol "А есть наш посёлок."

    stop fon fadeout 3

    voice "voice/Polina/2day/96 Mir.ogg"
    Pol "Мир..."

    play sound "sounds/ruki.ogg"

    "Она широко развела руки."

    voice "voice/Polina/2day/97 Poselok.ogg"
    Pol "Посёлок..."

    "Она показала что-то миллиметровое двумя пальцами."

    voice "voice/Polina/2day/98 Ya chasto.ogg"
    Pol "Я часто представляю большие города."

    voice "voice/Polina/2day/98 Mogu.ogg"
    Pol "Могу часами рассматривать глобус."

    voice "voice/Polina/2day/98 Ili zurn.ogg"
    Pol "Или журналы «Вокруг света» из библиотеки."

    voice "voice/Polina/2day/98 Kakie ze tam.ogg"
    Pol "Какие же там прекрасные названия! Только послушай:"

    voice "voice/Polina/2day/98 Reik.ogg"
    Pol "Рейкьявик..."

    voice "voice/Polina/2day/98 Telaviv.ogg"
    Pol "Тель-Авив..."

    voice "voice/Polina/2day/98 Eto ze.ogg"
    Pol "Это же чистейшая музыка, а не слова!"

    "Она закружилась, мечтательно зажмурившись."
    "Впереди вздымался лес, соприкасаясь с низкими облаками."


    window hide
    $ SetParSpeed(60)
    hide walking_fox_11_day
    hide walking_fox_12_day
    hide walking_fox_21_day
    hide walking_fox_22_day
    hide walking_fox_31_day
    hide walking_fox_32_day
    show gohome01 behind pol_walk_day_left
    show gohome01_1 behind pol_walk_day_left
    show gohome02 behind pol_walk_day_left
    show gohome02_1 behind pol_walk_day_left
    show gohome03 behind pol_walk_day_left
    show gohome03_1 behind pol_walk_day_left
    show gohome04 behind pol_walk_day_left
    show gohome04_1 behind pol_walk_day_left

    show gohome05a

    with Dissolve(1.5)
    window show

    "Дорога проваливалась в полутьму меж сосен."

    voice "voice/Polina/2day/99 Ya bi mogla.ogg"
    Pol "Я бы могла покорить сцену!"

    voice "voice/Polina/2day/99 Vistupat.ogg"
    Pol "Выступать перед тысячами зрителей!.."

    voice "voice/anton/2day/105. A ya scene.ogg"
    Ant "А я сцены ужасно боюсь."

    voice "voice/Polina/2day/100 Tak ti.ogg"
    Pol "Так ты другим возьмёшь – живописью!"

    voice "voice/Polina/2day/100 U nas.ogg"
    Pol "У нас-то есть будущее, а что ждёт того же Семёна?"

    voice "voice/Polina/2day/100 Nu stanet on.ogg"
    Pol "Ну станет он ещё толще..."

    voice "voice/Polina/2day/100 Nu.ogg"
    Pol "Ну..."

    voice "voice/anton/2day/106. Cakes.ogg"
    Ant "Будет пирожками торговать!"

    voice "voice/Polina/2day/101 Aga.ogg"
    Pol "Ага, ха-ха-ха, с собачатиной, ха-ха-ха-ха!"

    play sound "voice/anton/2day/107. Mi.ogg"

    "Мы рассмеялись, беспечным весельем изгнали тревогу."

    voice "voice/Polina/2day/102 Esli emu.ogg"
    Pol "Если ему, конечно, доверят пирожки!"

    voice "voice/anton/2day/108 Naverno.ogg"
    Ant "Наверное, ты права!"

    voice "voice/anton/2day/108.2 On ih.ogg"
    Ant "Он их в один присест слопает."

    voice "voice/Polina/2day/103 Ya tak i.ogg"
    Pol "Я так и думала, что вдвоём в лесу не страшно."


    show bg forest0_long:
        subpixel True
        xalign .19
        easein 5 xalign 0.
    show snowman_snow
    with Dissolve(1.0)

    "Я поглядел по сторонам."
    "Снег пускал искры, отражая последние солнечные лучи."
    "При мысли, что мы тут одни, пульс участился."

    stop music2 fadeout 1
    $ polina_face_state = 5

    voice "voice/anton/2day/109. Da ti.ogg"
    Ant "Да, ты была права."

    label polwit:

    $ SceneFlags.Reset()
    window hide
    $ SetParSpeed(30)
    scene bg_black
    show gohome01
    show gohome01_1
    show gohome02
    show gohome02_1
    show gohome03
    show gohome03_1

    show screen witness_walkaway(spr="sprite/Svedetel_01.png", blur = None, timeout = 0.6)

    show gohome04
    show gohome04_1

    show pol_walk_day_left:
        xpos 1920
        easein 20 xpos 900
    show ant_walk_day_left:
        xpos 1920+300
        easein 20 xpos 900+300
    show gohome05a
    with Dissolve(1.5)


    $ is_tapped = ui.interact()

    if is_tapped == "tap":

        $ story_manager.MarkEvent(("day2", "man_polina", "witness"))
        $ Flags.Raise("witness tapped")
        hide bg_black
        show bg_black with Dissolve(.5)
        show gohome01_stop
        show gohome01_1_stop
        show gohome02_stop
        show gohome02_1_stop
        show gohome03_stop
        show gohome03_1_stop

        show man in_black0:
            zoom 0.80
            ypos 200
            xalign .5

        show gohome04_stop:
            xalign .3
        show gohome04_1_stop:
            xalign .3
        with Dissolve(.5)

        hide screen witness_walkaway
        stop test_seven fadeout 2

        "Неожиданно сбоку зашуршали кусты, посыпая белым овраг."

        hide man
        show man in_black1:
            align (.5,1.)
            zoom .8
            alpha .0
            linear 1. zoom 1. alpha 1.
        play sound "sounds/steps/Man in.ogg"

        "Из-за них вышел, застёгивая ширинку, громила."

        if Flags.Has("witness school"):
            "Я узнал его — видел утром у школы."

        show man in_black1_2
        with None
        hide man
        with Dissolve(1.)

        play sound "sounds/steps/Man out.ogg"

        "Он посмотрел на нас без интереса и зашагал прочь."

        show Polina Front b_day_winter 02 hm ahead 02 with Dissolve(0.2)

        voice "voice/Polina/2day/104 Nu i tip.ogg"
        Pol "Ну и тип!"

        show Polina Front b_day_winter 02 hm ahead 03 with Dissolve(0.2)
        show Polina Front b_day_winter 01 norm ahead 011 with Dissolve(0.2)

        voice "voice/Polina/2day/104 Horosho.ogg"
        Pol "Хорошо, что ты со мной, Антон."

        show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(0.2)
        show Polina Front b_day_winter 01 sad ahead 09 with Dissolve(0.2)

        voice "voice/Polina/2day/105 Kto znaet.ogg"
        Pol "Кто знает, чтобы сделал этот бандит, если бы я была одна."

        show Polina Front b_day_winter 01 norm ahead 04 with Dissolve(0.2)

        "Она одарила меня восхищённым взглядом."

        show Polina Front b_day_winter 01 smile2 ahead 014 with Dissolve(0.2)
        play sound "voice/Polina/2day/149 A kogda.ogg"

        "А когда бугай почти скрылся за деревьями, показала ему язык и мелодично рассмеялась."
        "Ей-богу, маленькая проказница."

        hide Polina
        hide bg_black
        hide gohome01_stop
        hide gohome01_1_stop
        hide gohome02_stop
        hide gohome02_1_stop
        hide gohome03_stop
        hide gohome03_1_stop
        hide gohome04_stop
        hide gohome04_1_stop
        show bg_white
        with Dissolve(.5)

        hide bg_white
        with Dissolve(.5)


    play music "music/18_Olya_(piano&strings).ogg" volume 0.75 fadein 3
    stop fon fadeout 2
    play test_seven "sounds/steps/loop_footsteps_two.ogg" loop

    "Полина поспешила по просеке."

    voice "voice/Polina/2day/106 Ne ots.ogg"
    Pol "Не отставай!"

    voice "voice/anton/2day/110. Nikogda.ogg"
    Ant "Никогда в жизни."

    $ polina_face_state = 1

    voice "voice/Polina/2day/107 Ti znaesh.ogg"
    Pol "Ты знаешь, ты так изъясняешься..."

    voice "voice/Polina/2day/107 Kak pers.ogg"
    Pol "Как персонаж из приключенческой книжки."

    "Комплимент это? Или насмешка?"
    "Не хотелось искать подвохов. Только не во время такой чудесной прогулки."

    voice "voice/anton/2day/111. Nu da.ogg"
    Ant "Ну да, я люблю книги."

    voice "voice/Polina/2day/108 Ogo.ogg"
    Pol "Ого, читающий мужчина, хм?"

    voice "voice/Polina/2day/108 Zvuchit.ogg"
    Pol "Звучит интригующе!"

    "Мужчина? Серьёзно?"
    "Я засмущался и покраснел, но тысячу раз поблагодарил судьбу за то, что брожу теперь с Полиной по лесу."

    $ polina_face_state = 2

    "Девочка внезапно замолчала и задумчиво всмотрелась в чернеющие дебри."
    "Словно в ожидании чего-то."
    "И мне сделалось неспокойно."
    "А затем она спросила холодно:"

    $ polina_face_state = 3

    voice "voice/Polina/2day/Te bul.ogg"
    Pol "Ты был там?"

    voice "voice/anton/2day/112. Gde v.ogg"
    Ant "Где, в чаще?"

    play sound "voice/Polina/2day/101 Smeh.ogg"
    $ polina_face_state = True

    "Полина засмеялась, разрушив мои переживания."

    stop sound

    voice "voice/Polina/2day/110 Da net.ogg"
    Pol "Да нет!"

    voice "voice/Polina/2day/110 V bolshom.ogg"
    Pol "В большом мире!"

    voice "voice/Polina/2day/110 V gorodah.ogg"
    Pol "В городах с музыкальными названиями."

    voice "voice/anton/2day/113 A razve.ogg"
    Ant "А разве Москва – музыкальное название?"

    voice "voice/anton/2day/113.2 Bolshe pohoze.ogg"
    Ant "Больше похоже на кваканье лягушки."

    "Полина замерла и недоверчиво осмотрела меня."

    voice "voice/Polina/2day/111 Ti bil.ogg"
    Pol "Ты... был..."

    voice "voice/Polina/2day/111 V moskve.ogg"
    Pol "...в Москве?"

    voice "voice/anton/2day/114 Nu da.ogg"
    Ant "Ну да."

    voice "voice/anton/2day/114 V detstve.ogg"
    Ant "В детстве."

    "Глаза Полины заискрились."

    voice "voice/Polina/2day/112 I kakaya.ogg"
    Pol "И какая она?"

    voice "voice/anton/2day/115 Nu krasivaya.ogg"
    Ant "Ну... красивая."

    voice "voice/anton/2day/115.2 Shumnaya.ogg"
    Ant "Шумная."

    voice "voice/anton/2day/115.3 Neonovaya.ogg"
    Ant "Неоновая."

    voice "voice/Polina/2day/113 Neon.ogg"
    Pol "Неоновая..."

    "Она словно смаковала это слово."

    voice "voice/Polina/2day/114 A na krasn.ogg"
    Pol "А на Красной площади был?"

    voice "voice/anton/2day/116.1Konechno.ogg"
    Ant "Конечно."

    voice "voice/anton/2day/116.2Onatakaya.ogg"
    Ant "Она такая... выпуклая."

    $ add_text_to_dictionary(24)
    $ add_text_to_dictionary(25)

    voice "voice/anton/2day/117 I v TSUMe.ogg"
    Ant "И в {u}ЦУМе{/u} был, и на {u}ВДНХ{/u}."

    voice "voice/anton/2day/117.2 Mne bolshe vsego.ogg"
    Ant "Мне больше всего метро понравилось."

    voice "voice/anton/2day/117.3 Tam tak.ogg"
    Ant "Там так пахнет..."

    voice "voice/Polina/2day/115 Kak.ogg"
    Pol "Как?"

    "Она бросилась ко мне, схватила за рукав, пытливо вглядываясь."

    voice "voice/anton/2day/118. Ne mogu opisat.ogg"
    Ant "Не могу описать."

    voice "voice/Polina/2day/116 A naris.ogg"
    Pol "А нарисовать?"

    voice "voice/anton/2day/119. Chto zapah.ogg"
    Ant "Что? Запах?"

    voice "voice/Polina/2day/117 Velikie.ogg"
    Pol "Великие музыканты могут сыграть запах."

    voice "voice/anton/2day/120. Ne mozet bit.ogg"
    Ant "Не может быть!"

    voice "voice/Polina/2day/118 Ya dam tebe.ogg"
    Pol "Я дам тебе кассеты."

    "Она снова закружилась под снежком."

    voice "voice/Polina/2day/119 ya obyaz.ogg"
    Pol "Я обязательно побываю в Москве."

    voice "voice/Polina/2day/119 A glavnoe.ogg"
    Pol "А главное – в Вене."

    voice "voice/Polina/2day/119 Vena.ogg"
    Pol "Вена - моя мечта."

    voice "voice/Polina/2day/119 eto ze.ogg"
    Pol "Это же столица музыки!"

    voice "voice/Polina/2day/119 mozart.ogg"
    Pol "Моцарт, Бетховен, Штраус!"

    voice "voice/Polina/2day/119 fil.ogg"
    Pol "Филармонический оркестр!"

    voice "voice/Polina/2day/119 gos.ogg"
    Pol "Государственная опера!"

    voice "voice/Polina/2day/119 ya budu.ogg"
    Pol "Я буду выступать, а ты – рисовать!"

    "Восторг передался и мне."
    "Хотелось сделать что-то, прямо сейчас, немедленно!"

    voice "voice/Polina/2day/120 A ti kuda.ogg"
    Pol "А ты куда хочешь попасть?"

    play sound "voice/anton/2day/121.1 Yapriznalsa.ogg"

    "Я признался, вздохнув:"

    voice "voice/anton/2day/121.2Vdisney.ogg"
    Ant "В Диснейленд."

    "Я опять вспомнил «Звёздный час»."
    "Оля, конечно, предпочитала «Зов джунглей», но меня по понедельникам было не оттащить от экрана."
    "Разноцветные столы с цифрами на табличках, обаятельный Супонев у штурвала."
    "А призы!"
    "Шоколадные яйца, видеотехника... и самое будоражащее – путёвка в Диснейленд для победителя."
    "Родители обещали свозить меня туда, в страну Микки Мауса, и поначалу я верил им, а возможно, поначалу они тоже верили."

    stop music fadeout 5
    $ anton_face_polwalk_state = 1

    "Теперь на вопрос о путешествии они лишь отмалчивались, а меня разбирала смертельная обида."
    "Три слова буквально рвались из горла:"
    "Вы! Же! Обещали!"
    "Полина словно угадала мои мысли."

    voice "voice/Polina/2day/121 Dobr.ogg"
    Pol "Добраться туда проще, чем нам кажется."

    $ anton_face_polwalk_state = 0

    voice "voice/Polina/2day/121 Kazd lepit.ogg"
    Pol "Каждый лепит свою судьбу, как хочет."

    play music "music/30_(Tiny_Bunny).ogg" volume 0.7 fadein 2

    "Она набрала полные горсти снега."
    "И вдруг, позабыв обо всем, заговорщицки улыбнулась."

    voice "voice/Polina/2day/122 A davai.ogg"
    Pol "А давай снеговика лепить?"

    voice "voice/anton/2day/122. Davai.ogg"
    Ant "Давай!"

    "Когда вернусь домой, то обязательно слеплю снеговика для Оли – вот она обрадуется!"
    "А пока..."

    stop test_seven fadeout 2.5
    scene snowman 0
    show snowman_snow
    with Dissolve(0.5)

    "Мы уже скатывали первый ком, вместе, плечом к плечу."

    play sound "voice/Polina/2day/Smeh_pol.ogg"

    "Полина смеялась."
    "Локоны падали на её оживлённое лицо."
    "И она так очаровательно сдувала их."

    show snowman 00 behind snowman_snow

    voice "voice/anton/2day/123. Perviy gotov.ogg"
    Ant "Первый готов!"

    voice "voice/Polina/2day/123 Ha-ha.ogg"
    Pol "Ха-ха!"

    voice "voice/Polina/2day/123 Chego u tebya.ogg"
    Pol "Чего у тебя такой маленький шар, Антон?"

    voice "voice/Polina/2day/123 Maksimum.ogg"
    Pol "Максимум – голова снеговичка."

    voice "voice/Polina/2day/123 Bolshe.ogg"
    Pol "Больше надо!"

    voice "voice/Polina/2day/123 Ne lenis.ogg"
    Pol "Не ленись!"

    "Я забыл, когда в последний раз так веселился."
    "Полина вытерла рукавичкой заалевшие губы."

    voice "voice/Polina/2day/124 Ti mechtal.ogg"
    Pol "Ты мечтал когда-нибудь очутиться на другой планете?"

    "Что-то такое промелькнуло в её взгляде... Я не смог разгадать."

    voice "voice/anton/2day/124. I daze v.ogg"
    Ant "И даже в другой вселенной."

    play sound "voice/Polina/2day/Vidoh.ogg"
    "Полина будто бы облегчённо вздохнула."

    voice "voice/Polina/2day/125 Togda.ogg"
    Pol "Тогда ты понимаешь меня."

    play test_six "sounds/sfx_make_snowman.ogg"

    "Ладони скользили по кому, сглаживая шероховатости."
    "Почти идеальный белый шар вырос посреди поляны."
    "За ним появился второй."
    "Мы взяли его с двух сторон и водрузили на основание."

    show snowman 1
    with Dissolve(0.5)

    play sound "sounds/Pom_snow.ogg"
    "Наконец Полина помогла третьему шару оседлать предыдущие."

    voice "voice/Polina/2day/126 Stavit golovu.ogg"
    Pol "Ставить голову на место – мой конёк!"

    voice "voice/Polina/2day/127 U tebya.ogg"
    Pol "У тебя морковка случайно не завалялась?"

    voice "voice/anton/2day/125. Uvi.ogg"
    Ant "Увы!"

    scene dark_forest_day2_3:
        xpos -900
    show snowman_snow
    with Dissolve(0.5)

    "На этой опушке не было ни страха, ни тревоги."
    "Осмелев, я побежал к чаще наломать веток."

    scene dark_forest_day2_4:
        xpos -900
    show snowman_snow
    with Dissolve(0.5)
    play test_one "sounds/steps_snow001.ogg"
    show dark_forest_day2_4:
        subpixel True
        xpos -900
        ease 10 xpos -350

    "Дёрнул за переплетение бурелома, как вдруг голос Полины вытащил меня из забытья."

    voice "voice/Polina/2day/128 Anton.ogg"
    Pol "Антон!.."

    stop music fadeout 5

    voice "voice/Polina/2day/123 Tam kto-to.ogg"
    Pol "Там кто-то есть."

    show dark_forest_day2_4:
        subpixel True
        xpos -350
        ease 5 xpos -900

    "Я повернулся, растерянный."

    play music2 "music/12_Disaster_pt0.ogg" fadein 2

    "Полина смотрела на меня... нет... на что-то за моей спиной."
    "Смотрела и хмурилась."
    "От былого веселья не осталось и следа."

    voice "voice/anton/2day/126. Polin.ogg"
    Ant "Полин?"

    "Она медленно подняла руку, указывая на подступающую тьму за деревьями."

    voice "voice/Polina/2day/129 Vperedi.ogg"
    Pol "Впереди кто-то стоит."

    voice "voice/Polina/2day/130 Temnaya.ogg"
    Pol "Тёмная сгорбленная фигура, видишь?"

    voice "voice/Polina/2day/131 I ruch.ogg"
    Pol "И ручищами сосну гладит..."

    window hide
    show dark_forest_day2_4:
        subpixel True
        xpos -900
        ease 3.0 xpos 0
    show snowman_snow:
        ease 1.0 alpha 0.0
    show dark_forest_day3_1:
        subpixel True
        zoom 0.5
        alpha 0.0
        pause 2.2
        linear 0.9 alpha 1.0
    show snowman_snow_revers:
        alpha 0.0
        pause 2.2
        linear 0.9 alpha 1.0

    $ renpy.pause(delay=3.5, hard=True)
    window show

    "Обернувшись, я проследил за её пальцем."
    "В сухом малиннике было пусто."

    voice "voice/anton/2day/128. Tam nikogo.ogg"
    Ant "Там никого нет."

    show dark_forest_day3_1:
        subpixel True
        zoom 0.5
        linear 20.0 zoom 0.75 xpos -480 ypos -400

    voice "voice/Polina/2day/132 Ono spr.ogg"
    Pol "Оно спряталось..."

    voice "voice/Polina/2day/132 Za derevom.ogg"
    Pol "..за деревом."

    "Стало вдруг душно. Я непроизвольно оттянул воротник."
    "Желудок свело от спазма."

    scene dark_forest_day2_4:
        subpixel True
        xpos -900

    show snowman_snow
    with Dissolve(0.5)

    "Неуверенно улыбнувшись, я поинтересовался с надеждой:"

    voice "voice/anton/2day/129. Eto chto.ogg"
    Ant "Это что, шутка?"

    "Полина словно онемела, она безотрывно вглядывалась в бездну леса."
    "«Проверка на храбрость», - решил я и зашагал к чёрному лоснящемуся стволу, тогда как взгляд Полины подталкивал сзади."







    scene dark_forest_day3_1:
        subpixel True
        zoom 0.75 xpos -480 ypos -400



    show snowman_snow_revers



    with Dissolve(.5)

    "Что есть сил я пытался храбриться, но внутренний голос призывал замереть, сжаться комочком, да хоть прикинуться дохлым, но не идти туда, в сгущающуюся тьму."
    "Лесные сумерки плавали вокруг, сужая кольцо."
    "Опушка была колодцем, в чью горловину с трудом пробивались солнечные лучи."
    "Я слышал, как воздух звенит. Или звенело в моих ушах."

    play test_two "sounds/steps/step_snow1.ogg"
    show dark_forest_day3_1:
        subpixel True
        zoom 0.75 xpos -480 ypos -400
        linear 2.0 zoom 0.80 xpos -480-96 ypos -500
    $ renpy.pause(2, hard=not config.developer)

    "Шаг."

    play test_two "sounds/steps/step_snow2.ogg"
    show dark_forest_day3_1:
        subpixel True
        zoom 0.80 xpos -480-96 ypos -500
        linear 2.0 zoom 0.85 xpos -480-192 ypos -600
    $ renpy.pause(2, hard=not config.developer)

    "Второй."

    show dark_forest_day3_1:
        subpixel True
        zoom 0.85 xpos -480-192 ypos -600
        linear 20.0 zoom 1.0 xpos -960 ypos -800
    pause 2 

    "Я прикусил губу, чтобы в случае чего не завопить."
    "..."
    "За сосной никого не было."

    stop music2 fadeout 5
    play sound "voice/anton/2day/130. Vidoh.ogg"

    "Я выдохнул."

    scene dark_forest_day2_5:
        subpixel True
        xpos -900

    show snowman_snow
    with Dissolve(0.5)

    "И опять повернулся к Полине."

    voice "voice/anton/2day/131. Polina zdes.ogg"
    Ant "Полина, здесь никого..."

    window hide
    play test_one "sounds/steps_snow001.ogg"
    show dark_forest_day2_5:
        subpixel True
        xpos -900
        ease 5.0 zoom 1.2 xpos -1300 ypos -88
    pause 4.5

    pause 0.3
    play test_one "sounds/doom-drum-2.ogg"
    scene bg_white with Dissolve(0.1)
    pause 0.2
    scene bg_road_wood:
        xpos -100
    show Semen Happy m_day_W 00 good ahead 01:
        yoffset 260
        xoffset 420
        zoom 0.86
    show snow_for_forest1_anton
    with Dissolve(0.3)
    pause 0.2
    stop fon fadeout 1
    play music "music/34_Nikita Kryukov - the Sabbath.ogg"  fadein 3.0

    $ music_during_lines = 0.75
    voice "voice/semen/2day/28 Nu z.ogg"
    Sem "Ну здорово, Антошка!"

    window hide
    jump bunny_day2_gop_stop

label bunny_day2_gop_stop:
    $ story_manager.MarkEvent(("day2", "scene9"))

    if not Flags.Has("day2 polina"):
        pause 0.3
        play test_one "sounds/doom-drum-2.ogg"
        scene bg_white with Dissolve(0.1)
        pause 0.2
        scene bg_road_wood:
            xpos -100
        show Semen Happy m_day_W 00 good ahead 01:
            yoffset 260
            xoffset 420
            zoom 0.86
        show snow_for_forest1_anton
        with Dissolve(0.3)
        pause 0.2
        play music "music/34_Nikita Kryukov - the Sabbath.ogg"  fadein 3.0
        window show

    "Из вечной темноты за соснами, как дикари из пещер, вышли ухмыляющийся Семён и его гогочущая шайка."

    show Semen Disgust b_day_W 00 evil ahead 01:
        xalign 0.5
        yalign 1.0
        xoffset 0
        yoffset 0
        zoom 1.0
    show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
        xoffset -540
        yoffset 75
    show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
        xoffset 540
        yoffset 75
    show snow_for_forest1_anton behind Semen
    with Dissolve(0.3)

    if Flags.Has("day2 fox"):
        show Semen Disgust b_day_W 00 evil ahead 02:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            zoom 1.0
        with Dissolve(0.3)

        $ music_during_lines = 0.75
        voice "voice/semen/2day/28 Nu z.ogg"
        Sem "Ну здорово, Антошка!"

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
    else:

        show Romka Angry m_day_winter 01 angry ahead 03 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Romka Angry m_day_winter 01 angry ahead 04 with Dissolve(0.3)

        voice "voice/romka/2day/02 Opaczki.ogg"
        Noname "Опачки, какая встреча!"

    if Flags.Has("day2 fox"):
        show Romka Angry m_day_winter 01 angry ahead 03 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Romka Angry m_day_winter 01 angry ahead 04 with Dissolve(0.3)

        voice "voice/romka/2day/01 Haha.ogg"
        Noname "Хе-хе, не вышло сдрыснуть, да?!"

    show Romka Angry m_day_winter 01 angry ahead 03
    show Byasha Hee m_day_winter 01
    with Dissolve(0.3)

    voice "voice/byasha/01 Ochkarik.ogg"
    Noname "Очкарик-в-жопе-шарик, на! Ха-ха-ха!"

    if Flags.Has("day2 polina"):
        play sound "voice/Polina/2day/Oik.ogg"
        "Полина ойкнула, когда подонки отодвинули её подальше от меня."

    show Byasha Normal m_day_winter 01 vicious ahead 07 with Dissolve(0.3)

    "Словно хищная стая, они окружали меня, вынуждая пятиться."

    if Flags.Has("day2 polina"):
        window hide

        show snowman 1
        show layer master:
            align (.5, .5)
            zoom 1.05
        pause
        play test_one "voice/semen/2day/97 Noga.ogg"
        show fox_snowball onlayer master1:
            align (.5, .5)
            zoom 1.05
        play test_two "sounds/snowball_2.ogg"
        pause 0.1
        show snowman 2 with vpunch
        show snowman_snow_more
        pause 1.0
        window show

        "Нога грузного Семёна протаранила брюхо снеговика."
        "Комья развалились, стали бесформенной кучей, из которой печально торчала сломанная ветка."
        play sound "voice/Polina/2day/Ah.ogg"
        "Полина обиженно ахнула. Гнев ошпарил меня кипятком."

        hide fox_snowball
        hide snowman 2
        hide snowman_snow_more
        show snow_for_forest1_anton
        scene onlayer master1
        with Dissolve(0.3)

    "В нос шибанул запах пота и табака. Во рту стало кисло, словно я лизал батарейку."

    if Flags.Has("day2 polina"):
        voice "voice/anton/2day/132. Polin ne.ogg"
        Ant "Полин, не бойся!"

        "Я вздрогнул, когда услышал свой голос."
        "Он был неестественным, свирепым и пугающим."

        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/Polinketoche.ogg"
        Sem "Полинке-то чего бояться? Ха-ха."

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/Luchshezasebya.ogg"
        Sem "Лучше за себя беспокойся."

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)

        play sound "sounds/bax.ogg"

        "Здоровяк сплюнул сквозь щель в зубах и резко толкнул меня так, что я впечатался спиной в дерево." with vpunch

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/Nukak.ogg"
        Sem "Ну как?"

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/Strashno.ogg"
        Sem "Страшно, мудила?"

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)

        "Позади раздался сердитый возглас Полины:"

        show doggy_fon
        show Polina Scream b_day_winter 01 norm ahead 01
        show snowman_snow_revers
        with Dissolve(0.3)
        show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(0.1)

        voice "voice/Polina/2day/133 Ne trogaite.ogg"
        Pol "Не трогайте его!"

        show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(0.1)

        "Лучше бы Полины здесь не было. Лучше бы она не видела этого позора."

        hide doggy_fon
        hide Polina
        hide snowman_snow_revers
        with Dissolve(0.3)

        show Romka Angry m_day_winter 01 angry ahead 04 with Dissolve(0.3)

        voice "voice/romka/2day/04 Gljadite1.ogg"
        Noname "Глядите-ка, пацаны!"

        show Romka Angry m_day_winter 01 angry ahead 03 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Romka Angry m_day_winter 01 angry ahead 04 with Dissolve(0.3)

        voice "voice/romka/2day/08 Devczonk.ogg"
        Noname "Девчонка за него заступается!"

        show Romka Angry m_day_winter 01 angry ahead 03 with Dissolve(0.3)

        window hide

    if Flags.Has("day2 fox"):
        voice "voice/anton/2day/79. Alisa.ogg"
        Ant "Алиса!"

        "Имя спутницы превратилось в сдавленное сипение."
        "Сосны качались молчаливыми стражами."
        "Взгляд мой заметался."

        scene bg_road_wood:
            xpos -100
            ease 0.3 xpos -462
            ease 0.3 xpos 0
            ease 0.3 xpos -100
        show Semen Disgust b_day_W 00 evil ahead 01:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            ease 0.3 xoffset -362
            ease 0.3 xoffset 100
            ease 0.3 xoffset 0
        show Byasha Normal m_day_winter 01 vicious ahead 07 behind Semen:
            xoffset -540
            yoffset 75
            ease 0.3 xoffset -362-540
            ease 0.3 xoffset 100-540
            ease 0.3 xoffset 0-540
        show Romka Angry m_day_winter 01 angry ahead 03 behind Semen:
            xoffset 540
            yoffset 75
            ease 0.3 xoffset -362+540
            ease 0.3 xoffset 100+540
            ease 0.3 xoffset 0+540
        show snowman_snow

        "Я так мечтал увидеть за деревьями лисичку, ждал, что она придёт на помощь."
        "Но лишь ветер отвечал на мои призывы."

        show Byasha Normal m_day_winter 01 evil ahead 01 with Dissolve(0.3)

        voice "voice/anton/2day/79 Gde Alisa.ogg"
        Ant "Где Алиса?!"

        show Romka Normal m_day_winter 00 what ahead 01 with Dissolve(0.3)

        voice "voice/anton/2day/79.2 Chto vi s nei.ogg"
        Ant "Что вы с ней сделали?!"

        "Я вздрогнул, когда услышал свой голос."
        "Он был неестественным, свирепым и пугающим."

        hide Semen
        show Semen Disgust b_day_W 00 evil ahead_to_aside 02
        with Dissolve(0.3)

        voice "voice/semen/2day/29 Kaka.ogg"
        Sem "Какая ещё Алиса?"

        show Semen Disgust b_day_W 00 evil aside 01 with Dissolve(0.3)
        pause 0.3
        hide Semen
        show Semen Disgust b_day_W 00 evil aside_to_ahead 02
        with Dissolve(0.3)
        pause 0.3

        voice "voice/semen/2day/30 U te.ogg"
        Sem "У тя чё, кукуха поехала?"

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
        $ renpy.pause(0.2)
        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/31 Ne s.ogg"
        Sem "Не ссы, ща вмиг вылечим."

        show Semen Disgust b_day_W 00 evil ahead 01 with Dissolve(0.3)
        play test_one "voice/semen/2day/32 Zdor.ogg"
        play sound "sounds/bax.ogg"

        "Здоровяк сплюнул сквозь щель в зубах и резко толкнул меня так, что я впечатался спиной в дерево." with vpunch

        show Semen Disgust b_day_W 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/semen/2day/33 Nu k.ogg"
        Sem "Ну как? Полегчало?"

        scene bg gop_wood_2:
            xpos 0
        show romka 01 01 01
        show baysha 01 02 01
        show sema 01
        with Dissolve(0.5)

        "Неужели..."
        "Неужели Алиса специально заманила меня в ловушку к этим уродам?"
        "Нет, не верю, не желаю верить!"

        window hide
        scene bg gop_wood_2:
            linear 3 xpos -720
        show romka 01 01 01:
            linear 3 xpos -720
        show baysha 01 02 01:
            linear 3 xpos -720
        show sema 01:
            linear 3 xpos -720
        $ renpy.pause(delay=3.0, hard=True)
        show romka 01 01 04 with Dissolve(0.3)
        window show

        voice "voice/romka/2day/04 Gljadite.ogg"
        Noname "Глядите-ка, пацаны! А здесь он не такой борзый, как в школе."

    if Flags.Has("day2 polina"):
        window hide
        scene bg gop_wood_2:
            linear 3 xpos -720
        show romka 01 01 01:
            linear 3 xpos -720
        show baysha 01 02 03:
            linear 3 xpos -720
        show sema 01:
            linear 3 xpos -720
        $ renpy.pause(delay=3.0, hard=True)

        voice "voice/byasha/07 Aga syk.ogg"
        Noname "Ага, ссыкло, на."

    if Flags.Has("day2 fox"):
        show baysha 01 02 03 at sprite_ha

        voice "voice/byasha/08 Aga vylit.ogg"
        Noname "Ага, вылитый терпила, на."

    if Flags.Has("fight"):
        show baysha 01 02 04
        show sema 02 with Dissolve(0.3)
        show bg_gop_wood_ring_blick:
            xpos -720

        voice "voice/semen/2day/35 Ty.ogg"
        Sem "Ты, сука приезжая, не на того руку поднял."

        "Семён уже двинулся на меня, замахнувшись."

        play test_one "sounds/sfx_whistle.ogg"

        window hide
        show romka 01 01 01
        show sema 14 with Dissolve(0.3)
        scene bg gop_wood_2:
            xpos -720
            linear 1 xpos -980
        show romka 01 01 01:
            xpos -720
            linear 1 xpos -980
        show baysha 01 02 04:
            xpos -720
            linear 1 xpos -980
        show sema 14:
            xpos -720
            linear 1 xpos -980
        $ renpy.pause(1.0)
        window show

        "Внезапно другой хулиган в спортивных штанах оглушительно свистнул, и здоровяк покорно опустил занесённую руку."
        "Это было неожиданно — главный в банде оказался не Бабурин."
        "На деле все слушались этого похожего на хищного зверька парнишку с крепкими и острыми зубами."

    if Flags.Has("day2 polina"):
        "Бить не стали."
        "Видимо, собирались для начала поглумиться на глазах у девочки."
        "Проклятье!"

        show romka 01 01 02 with Dissolve(0.2)

    if Flags.Has("day2 fox"):
        "Бить не стали. Видимо, собирались для начала поглумиться."

        show romka 01 01 02 with Dissolve(0.2)

    if Flags.Has("fight"):
        voice "voice/romka/2day/09 Slysh G.ogg"
        Noname "Слышь, Гандон Батькович!"

    if Flags.Has("day2 polina"):
        voice "voice/romka/2day/11 A eto k.ogg"
        Noname "А это кто? Ещё одна подружка?"

        show romka 01 01 06 with Dissolve(0.2)

        voice "voice/byasha/09 Da y tebya.ogg"
        Noname "Да у тебя тут гарем, на!"

    if Flags.Has("day2 fox"):
        voice "voice/romka/2day/10 Eto czt.ogg"
        Noname "Это, что ли, твоя Алиса?"

    if Flags.Has("fight"):
        scene bg_road_wood_dog1 with Dissolve(0.3)

        "Я только сейчас заметил рядом с собой дрожащую от холода Жульку, на шерсть которой налипли комки снега."

    if Flags.Has("day2 polina"):
        play test_six "sounds/sfx_dog_calling_two.ogg"

        "Видать, бежала от самой школы и нашла нас по запаху."

    if Flags.Has("fight"):
        "Хулиган присел на корточки и жестом поманил собаку."

        scene bg_road_wood_dog2 with Dissolve(0.3)
        play test_six "sounds/sfx_dog_calls_0.ogg"

        voice "voice/romka/2day/12 Oi ty.ogg"
        Noname "Ой ты, батюшки!"

    if Flags.Has("day2 polina"):
        voice "voice/romka/2day/Ko mne.ogg"
        Noname "Ко мне, сучка блохастая!"

    if Flags.Has("day2 fox"):
        voice "voice/romka/2day/13 Alisa.ogg"
        Noname "Алиса! Ко мне, сучка блохастая!"

    if Flags.Has("fight"):
        play sound "voice/semen/2day/ha-ha.ogg"

        "Остальные мерзко захихикали."
        "Собака, навострив уши, облизнулась и стала осторожно приближаться."

        voice "voice/romka/2day/14 Idi sud.ogg"
        Noname "Иди сюда, иди-иди, дам кой-чего..."

        window hide
        play sound "sounds/sfx_kicking_dog.ogg"
        scene bg_dog_bully with Dissolve(0.3)
        $ renpy.pause(3.0)
        window show

        "Не успела собака принюхаться, как живодёр схватил её за ухо и с размаху пнул под хвост так, что она полетела, скуля, в ближайший сугроб."

    if Flags.Has("day2 fox"):
        window hide
        play test_seven "voice/semen/2day/ha-ha-ha.ogg"
        scene bg gop_wood_2:
            xpos -720
        show romka 01 03 04:
            xpos -720
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
        show baysha 01 02 03:
            xpos -720
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
            ease 0.09 yoffset 15
            ease 0.09 yoffset 0
        show sema 10:
            xpos -720
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
            ease 0.11 yoffset 22
            ease 0.11 yoffset 0
        with Dissolve(0.5)
        $ renpy.pause(3.0)
        window show

        "Вся банда взорвалась смехом, а у меня сердце обледенело."

        stop music fadeout 3.0
        play sound "sounds/sfx_crows.ogg"

        "Даже птицы, сидевшие на ветках, отозвались испуганным граем."

        scene bg_lisa001
        show snowman_snow
        with Dissolve(0.5)

    if Flags.Has("day2 polina"):
        play test_one "voice/semen/2day/ha-ha-ha.ogg"
        $ renpy.start_predict("doggy_fly")
        $ renpy.start_predict("Polina Front b_day_winter 01 norm ahead 01")

        "Вся банда взорвалась смехом, а у меня сердце обледенело."

        stop music fadeout 3.0
        play sound "sounds/sfx_crows.ogg"

        "Даже птицы, сидевшие на ветках, отозвались испуганным граем."

        window hide
        show doggy_fly:
            xpos -2500
            ypos 1080
            linear 2.5 xpos -300 ypos -1500
            linear 5.0 xpos 220 ypos -2200
            linear 22.0 xpos 420 ypos -2600
        pause 1.25
        show doggy_fon behind doggy_fly:
            alpha 0.0
            linear 0.25 alpha 1.0
        show Polina Front b_day_winter 01 norm ahead 01 behind doggy_fly:
            alpha 0.0
            linear 0.25 alpha 1.0
        show doggy_pol 01 behind doggy_fly:
            alpha 0.0
            linear 0.25 alpha 1.0
        pause 1.5
        show Polina Front b_day_winter 01 norm ahead 04
        show doggy_pol 02
        with Dissolve(0.2)
        show Polina Front b_day_winter 01 norm ahead 05
        show doggy_pol 03
        with Dissolve(0.2)
        show Polina Front b_day_winter 01 norm ahead 06
        show doggy_pol 04
        with Dissolve(0.2)
        show Polina Front b_day_winter 01 hm ahead 07
        hide doggy_pol 04
        with Dissolve(0.2)
        window show

        $ renpy.stop_predict("doggy_fly")
        $ renpy.stop_predict("Polina Front b_day_winter 01 norm ahead 01")

        "Мельком я заметил кое-что странное."

        play music "music/40_Imminence.ogg"
        play sound "voice/Polina/2day/heh.ogg"

        "Полина с трудом сдерживала улыбку."
        "Неужели она настолько не любит собак, что садистский поступок тощего развеселил её?"

        show Polina Front b_day_winter 01 sad ahead 01
        with Dissolve(0.2)
        show Polina Front b_day_winter 01 sad ahead 03
        with Dissolve(0.2)
        show Polina Front b_day_winter 01 sad ahead 02
        with Dissolve(0.2)
        play sound "voice/Polina/2day/Oh.ogg"

        "Встретившись со мной глазами, Полина сменила торжествующую ухмылку на озабоченную гримасу."
        "«Почему она не убегает?», – ужаснулся я."

        scene bg_lisa001
        show snowman_snow
        with Dissolve(0.5)

        "И будто кто-то прошёл на периферии зрения, в обманчивых сумерках спящего леса."
        "Или просто кусты на ветру шевельнули заиндевелыми шипами веток."

    if Flags.Has("day2 fox"):
        "Боковым зрением я заметил, будто кто-то промелькнул в обманчивых сумерках спящего леса."
        "Или просто кусты на ветру шевельнули заиндевелыми шипами веток."

        play music "music/40_Imminence.ogg"

    if Flags.Has("fight"):
        scene bg gop_wood_2:
            xpos -720
        show romka 01 02 06:
            xpos -720
        show baysha 01 03 04:
            xpos -720
        show sema 11:
            xpos -720
        with Dissolve(0.5)

        voice "voice/semen/2day/37 Romk.ogg"
        Sem "Ромка, она ж больше срать не сможет!"

        voice "voice/semen/2day/38 Dava.ogg"
        Sem "Дай, теперь я."

        voice "voice/semen/2day/39 Vtor.ogg"
        Sem "Второй раз ебану — минус на минус даст плюс."

        scene bg_road_wood_no_dog with Dissolve(0.3)

        "Но дворняги уже и след простыл."

        scene bg gop_wood_2:
            xpos -720
        show romka 01 03 02:
            xpos -720
        show baysha 01 02 01:
            xpos -720
        show sema 14:
            xpos -720
        with Dissolve(0.5)

        voice "voice/romka/2day/16 CZego ty.ogg"
        Rom "Чего ты, баран?"

        voice "voice/romka/2day/17 Vtolkui.ogg"
        Rom "Втолкуй вон очкарику, где его место."

        voice "voice/romka/2day/18 Tolko.ogg"
        Rom "Только так, чтобы он понял."

        show romka 01 03 05
        show baysha 01 02 05
        with Dissolve(0.3)

        voice "voice/byasha/05 Aga.ogg"
        Noname "Ага, за ним косяк, на."

        voice "voice/byasha/06 Etot.ogg"
        Noname "Этот очкарик тебе при всём классе всёк."

        show baysha 01 02 01
        show sema 17
        with Dissolve(0.3)

        voice "voice/semen/2day/40 Da b.ogg"
        Sem "Да без бэ!"
    else:

        voice "voice/romka/2day/05 Gljadite.ogg"
        Noname "Глядите на этого сопляка, пацаны."

        voice "voice/romka/2day/06 V shkole.ogg"
        Noname "В школе так споткнулся, что паркет помял."

        voice "voice/romka/2day/07 A remon.ogg"
        Noname "А ремонтировать кто будет?"

        voice "voice/byasha/02 Skin.ogg"
        Noname "Скинешься на ремонт, терпила?"

        voice "voice/semen/2day/Ne_bzdi.ogg"
        Sem "Не бзди, мы тебя правильно ходить научим!"

    window hide
    scene bg gop_wood_2:
        xpos -720
    show romka 01 03 05:
        xpos -720
    show baysha 01 02 01:
        xpos -720
    show sema 02:
        xpos -720
    with Dissolve(0.3)
    scene bg gop_wood_2:
        xpos -720
        ease 2.0 xpos -300
    show romka 01 03 05:
        xpos -720
        ease 2.0 xpos -300
    show baysha 01 02 01:
        xpos -720
        ease 2.0 xpos -300
    show sema 02:
        xpos -720
        ease 2.0 xpos -300
    $ renpy.pause(2.1)
    window show

    "Семён демонстративно поднёс к моему лицу увесистое кольцо-печатку с каким-то геометрическим символом."

    show bg_gop_wood_ring_blick:
        xpos -300

    voice "voice/semen/2day/41 SCHa.ogg"
    Sem "Ща, парашник, я тебе этой печаткой так заряжу – клеймо на всю жизнь останется!"

    if Flags.Has("fight"):
        "И куда подевались моя потаённая сила и храбрость?"

    play sound "voice/anton/2day/134. Ya prosipel.ogg"

    "Я просипел: «стой», а голова мотнулась, врезавшись в кулак Семёна. Красные искры брызнули из глаз."

    if not Flags.Has("day2 fox"):
        "Сейчас меня забьют толпой..."


    window hide
    play sound "sounds/sfx_punch.ogg"
    play test_one"sounds/fall.ogg"
    scene bg_gop_wood_sema_punch1:
        xpos -300
    show layer master:
        align (.5, .5)
        zoom 1.05
    with hpunch
    $ renpy.pause(0.3)
    scene bg_gop_wood_sema_punch2 with Dissolve(0.2):
        xpos -300
    show bg_gop_wood_ring_blick:
        xpos -300
    window show

    if Flags.Has("day2 polina"):
        show doggy_fon
        show Polina Scream b_day_winter 01 norm ahead 01
        show snowman_snow_revers
        with Dissolve(0.3)
        show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(0.1)

        voice "voice/Polina/2day/134 Roma pust.ogg"
        Pol "Рома! Пусть они прекратят!"

        scene bg gop_wood_1:
            xpos -300
            linear 3.0 xpos -720
        show romka 01 03 04:
            xpos -300
            linear 3.0 xpos -720
        show baysha 01 02 03:
            xpos -300
            linear 3.0 xpos -720
        show sema 10:
            xpos -300
            linear 3.0 xpos -720
        with Dissolve(0.5)

        voice "voice/romka/2day/19 Prosti.ogg"
        Rom "Прости, но пацанам надо по-мужски побазарить."

        voice "voice/romka/2day/20 A tebe.ogg"
        Rom "А тебе – в сторонке постоять."






        show romka 01 03 06 with Dissolve(0.2)

    voice "voice/semen/2day/44 Bjasha.ogg"
    Sem "Бяша, подсоби!"

    play sound "voice/semen/2day/43 Seme.ogg"

    "Семён грубо толкнул меня навстречу подонку с раскосыми глазами, и тот подставил подножку."

    scene bg_gop_noga1
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)
    play test_one "voice/semen/2day/45 YA up.ogg"

    "Я упал на острую корку льда, и толстяк тут же наступил на мою руку, не давая подняться."

    play sound "voice/anton/2day/135. Iz gorla.ogg"

    "Из горла вырвался болезненный стон."

    stop test_one fadeout 0.5

    voice "voice/semen/2day/47 Slyh.ogg"
    Sem "Слыхали, как заныл?"

    voice "voice/semen/2day/48 A ty.ogg"
    Sem "А ты, случаем, не педик?"

    play test_one "voice/anton/2day/137. Ot zlosti i.ogg"

    "От злости и обиды я начал задыхаться."

    play test_one "voice/anton/2day/136. Bol.ogg"

    "Боль нарастала."

    play test_one "voice/anton/2day/137. Uho puls.ogg"

    "Ухо пульсировало и пекло, точно его отрезали, а поверх пришили ком крапивы."

    voice "voice/romka/2day/21 CZo molcz.ogg"
    Rom "Чего молчишь, Антошка?"

    voice "voice/romka/2day/22 Otveczai.ogg"
    Rom "Отвечай! Ты педик?"

    play test_one "sounds/piano-hit-1.ogg"
    show bg_gop_noga_rage

    "И тут я почувствовал чистую, незамутнённую ярость, концентрат моей злобы."

    play test_one "sounds/piano-hit-1.ogg"
    show bg_gop_noga_rage

    "Как чернила спрута, она всплывала из глубин сознания, заполняя все мои мысли."

    voice "voice/anton/2day/138. Tvari.ogg"
    Ant "Твари!!!" with hpunch

    voice "voice/anton/2day/139. Znaete.ogg"
    Ant "Знаете, что мой..."

    voice "voice/anton/2day/139. Moi otec.ogg"
    Ant "Мой отец..."

    voice "voice/byasha/12 Toze.ogg"
    Bya "Тоже педик?"

    play sound "voice/semen/2day/48 Smem.ogg"

    "Семён загоготал."
    "Это стало последней каплей."
    "Страх и злость сцепились внутри меня, словно бешеные собаки."

    voice "voice/anton/2day/140. On aikido.ogg"
    Ant "Он айкидо занимался! Поняли?"

    voice "voice/anton/2day/140. A esche voeval.ogg"
    Ant "А ещё воевал!"

    voice "voice/anton/2day/141. Takih kak vi.ogg"
    Ant "Таких, как вы, с закрытыми глазами убивает!"

    voice "voice/anton/2day/141. Ya tolko slovo.ogg"
    Ant "Я только слово скажу — он..."

    if Flags.Has("fight"):
        "Ромка поднял руку, остановив поток лжи, и сделал пару шагов вперёд."
    else:
        "Мальчишка в спортивном костюме поднял руку, остановив поток лжи, и сделал пару шагов вперёд."

    play sound "voice/anton/2day/142. Semen.ogg"

    "Семён медленно отступил, дав мне возможность встать."

    if not Flags.Has("fight"):
        "Это было неожиданно - главный в банде оказался не Бабурин."
        "На деле все слушались этого похожего на хищного зверька парнишку с крепкими и острыми зубами."

    if not Flags.Has("day2 fox"):
        "Сосны качались молчаливыми стражами."

    scene bg_road_wood:
        xpos -100
    show Byasha Normal m_day_winter 01 vicious ahead 01:
        xoffset -560
        yoffset 75
    show Semen Serious m_day_W 00 evil ahead 01:
        xoffset 540
        yoffset 75
    show snowman_snow
    show Romka Evil b_day_winter 01 normal ahead 01
    with Dissolve(0.5)

    "Неужели поверил?"
    "Или его смутило моё перекошенное от ярости лицо?"

    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(0.2)

    voice "voice/romka/2day/23 Voeval.ogg"
    Rom "Воевал, говоришь?"

    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(0.2)
    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(0.2)

    voice "voice/romka/2day/24 Moi bat.ogg"
    Rom "Мой батя тоже воевал."

    show Romka Evil b_day_winter 01 normal ahead 01 with Dissolve(0.2)
    show Romka Evil b_day_winter 01 normal ahead 02 with Dissolve(0.2)

    voice "voice/romka/2day/25 V Afgan.ogg"
    Rom "В Афгане."

    show Romka Normal b_day_winter 01 what ahead 03 with Dissolve(0.2)

    voice "voice/romka/2day/26 A tvoi.ogg"
    Rom "А твой?"

    show Romka Normal b_day_winter 01 what ahead 02 with Dissolve(0.2)

    voice "voice/anton/2day/143. I moi.ogg"
    Ant "И м-мой..."

    show Romka Normal b_day_winter 01 what ahead 03 with Dissolve(0.3)

    voice "voice/romka/2day/27 Da i v.ogg"
    Rom "Да? И в каких войсках, интересно?"

    show Romka Normal b_day_winter 01 what ahead 02 with Dissolve(0.3)

    "Я замялся — страх вцепился в глотку злости и пустил ей кровь."

    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)

    voice "voice/byasha/13 Da on.ogg"
    Bya "Да он фуфло гонит, Ромка."

    show Byasha Normal m_day_winter 01 normal ahead 01 with Dissolve(0.3)
    pause 0.2
    show Byasha Normal m_day_winter 01 normal ahead 09 with Dissolve(0.3)

    voice "voice/byasha/14 Blya.ogg"
    Bya "Бля буду, на."

    show Byasha Normal m_day_winter 01 normal ahead 01
    show Romka Angry b_day_winter 01 angry ahead 02
    with Dissolve(0.3)

    voice "voice/romka/2day/28 Dumal.ogg"
    Rom "Думал, меня так просто развести?"

    show Romka Angry b_day_winter 01 angry ahead 01 with Dissolve(0.2)
    pause 0.2
    show Romka Angry b_day_winter 01 angry ahead 02 with Dissolve(0.2)

    voice "voice/romka/2day/29 YA tebja.ogg"
    Rom "Я тебя, сучонка, насквозь вижу."

    show Romka Angry b_day_winter 01 angry ahead 03 with Dissolve(0.2)

    "На лице Ромки появилась гадкая улыбка."
    "Ничего хорошего это не предвещало."

    show Romka Angry b_day_winter 01 angry ahead 06 with Dissolve(0.2)

    voice "voice/romka/2day/30 Ty sam.ogg"
    Rom "Ты сам себе приговор подписал."

    show Romka Angry b_day_winter 01 angry ahead 03 with Dissolve(0.2)

    if Flags.Has("fight"):
        show Semen Happy m_day_W 00 good ahead 02
        show Romka Angry b_day_winter 01 angry ahead 03
        with Dissolve(0.2)

        voice "voice/semen/2day/50 V shk.ogg"
        Sem "В школе тебя училка спасла, ну а теперь всё..."

        show Semen Happy m_day_W 00 good ahead 01 with Dissolve(0.2)
        show Semen Happy m_day_W 00 good ahead 02:
            yoffset 75
            linear 0.1 yoffset 95
            linear 0.1 yoffset 75
            linear 0.1
            linear 0.1 yoffset 95
            linear 0.1 yoffset 75

        voice "voice/semen/2day/50 Heh.ogg"
        Sem "Хе-хе."

    show Semen Disgust m_day_W 00 evil ahead 02 with Dissolve(0.2)

    voice "voice/semen/2day/50 Hana.ogg"
    Sem "Хана тебе!"

    show Semen Disgust m_day_W 00 evil ahead 01
    show Byasha Normal m_day_winter vicious 04
    with Dissolve(0.2)

    voice "voice/byasha/15 Vo vo.ogg"
    Bya "Во-во!"

    show Byasha Normal m_day_winter vicious 08 with Dissolve(0.2)

    voice "voice/byasha/16 Davai.ogg"
    Bya "Давай, Антошка, молись, чтобы твой труп по весне нашли, на."

    show Romka Normal b_day_winter 01 what ahead 03
    show Byasha Normal m_day_winter vicious 07
    with Dissolve(0.2)

    voice "voice/romka/2day/31 Sidel b.ogg"
    Rom "Сидел бы ниже травы — был бы целочкой."

    show Romka Normal b_day_winter 01 what ahead 02 with Dissolve(0.2)

    if Flags.Has("fight"):
        show Romka Normal b_day_winter 01 what ahead 03 with Dissolve(0.2)

        voice "voice/romka/2day/32 ZHirnogo.ogg"
        Rom "Жирного стукнул – одно дело."

        show Romka Evil m_day_winter 01 normal ahead 02 behind snowman_snow:
            xpos 950
            yoffset 75
        with Dissolve(0.3)
        $ add_text_to_dictionary(23)

        voice "voice/romka/2day/33 No pro.ogg"
        Rom "Но про Афган пиздеть, где мой батя под пулями... долг Интернациональный... в {u}Дашти-Марго{/u}, блять."
    else:
        $ add_text_to_dictionary(23)
        show Romka Normal b_day_winter 01 what ahead 03 with Dissolve(0.2)

        voice "voice/romka/2day/33 No pro.ogg"
        Rom "Но про Афган пиздеть, где мой батя под пулями... долг Интернациональный... в {u}Дашти-Марго{/u}, блядь."

    show Romka Angry m_day_winter 01 angry ahead 02:
        xoffset 540
        yoffset 75
    hide Semen
    show Semen Disgust b_day_W 00 evil ahead 01
    with Dissolve(0.3)

    voice "voice/romka/2day/34 Sema u.ogg"
    Rom "Сёма, ушатай-ка его!"

    scene bg gop_wood_2:
        xpos -720
    show romka 01 01 01:
        xpos -720
    show baysha 01 02 01:
        xpos -720
    show sema 01:
        xpos -720
    with Dissolve(0.5)

    "Хулиганы вновь сомкнули кольцо, и я оказался напротив Семёна."
    "Кровь стучала в висках."

    if Flags.Has("day2 polina"):
        show doggy_fon
        show Polina Front b_day_winter 01 sadly ahead 03
        show snowman_snow_revers
        with Dissolve(0.3)
        show Polina Front b_day_winter 01 sadly ahead 02 with Dissolve(0.2)

        voice "voice/Polina/2day/135 Nu Romochka.ogg"
        Pol "Ну Ромочка, ну хватит!"

        show Polina Front b_day_winter 01 sadly ahead 03 with Dissolve(0.2)
        show Polina Front b_day_winter 01 sadly ahead 02 with Dissolve(0.2)

        voice "voice/Polina/2day/135 Ti uze.ogg"
        Pol "Ты уже всё доказал."

        show Polina Front b_day_winter 01 sadly ahead 03 with Dissolve(0.2)
        show Polina Front b_day_winter 01 sadly ahead 02 with Dissolve(0.2)

        voice "voice/Polina/2day/135 Dai nam.ogg"
        Pol "Дай нам уйти."

        hide doggy_fon
        hide Polina
        hide snowman_snow_revers
        with Dissolve(0.4)

        show romka 01 01 02 with Dissolve(0.2)

        voice "voice/romka/2day/35 Ty idi.ogg"
        Rom "Ты иди, иди."

        show romka 01 01 01 with Dissolve(0.2)
        show romka 01 01 02 with Dissolve(0.2)

        voice "voice/romka/2day/35 A my po.ogg"
        Rom "А мы пока мусор приберём."

        show romka 01 01 01 with Dissolve(0.2)

        "Меня зацепило даже не это оскорбление, а ласковое «Ромочка» из уст Полины."
        "Уроды оттесняли девочку к соснам."

    "Ветки, качаясь, как будто что-то шептали. Обнадёживали."
    "Стиснув зубы и борясь с мыслью, что выгляжу глупо, я встал в боксёрскую стойку, которую частенько видел в кино."

    show baysha 01 02 05 with Dissolve(0.2)

    voice "voice/byasha/17 Hera ti.ogg"
    Bya "Хера ты — Майк Тайсон, на!"

    show baysha 01 02 01 with Dissolve(0.2)

    "Это была моя первая драка."

    show romka 01 01 01:
        xpos -720
        alpha 1.0
        linear 1.0 alpha 0.0
    play sound "sounds/steps/snow_stepS01.ogg"

    "Запомню на всю жизнь. Если, конечно, не сдохну сейчас."

    window hide
    scene bg_lisa005 with Dissolve(0.2)
    $ renpy.pause(0.2)
    scene bg_lisa006 with Dissolve(0.2)
    scene bg_lisa007 with Dissolve(0.2)
    show snowman_snow
    window show

    "Краем глаза я заметил, что тьма вокруг нас снова зашевелилась, будто в ней кто-то ходил туда-сюда..."
    "Я почувствовал клешни Ромы, схватившие за портфель."

    window hide
    scene bg gop_wood_2:
        xpos -720
    show baysha 01 02 01:
        xpos -720
    show sema 01:
        xpos -720
    with Dissolve(0.5)
    window show

    $ renpy.start_predict("rom_knife_03")

    voice "voice/romka/2day/37 Manatki.ogg"
    Rom "Манатки, Антошка."

    voice "voice/romka/2day/38 Mahatsa mesaet.ogg"
    Rom "Махаться мешает."

    scene rom_knife_00
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.3)

    "Я было упёрся, не желая подчиняться мерзавцу, но он ловким движением выудил из-за пазухи нож-бабочку и, демонстративно крутанув, подставил остриё к моему горлу."

    window hide
    show rom_knife_03
    play sound "sounds/sfx_butterfly_knife.ogg"
    $ renpy.pause(1.0)
    scene rom_knife_01
    show layer master:
        align (.5, .5)
        zoom 1.05
    window show
    $ renpy.stop_predict("rom_knife_03")

    voice "voice/romka/2day/40 Slysh f.ogg"
    Rom "Слышь, фраер, расслабься, а то больно будет."

    play test_one "voice/anton/2day/144. Vmesto slov.ogg"

    "Вместо слов я выдохнул клуб пара."

    play sound "sounds/snimaet_rukzak_2.ogg"
    $ renpy.pause(0.1)
    scene rom_knife_01
    show layer master:
        align (.5, .5)
        zoom 1.05
    with hpunch
    play test_one "voice/romka/2day/36 Romka zh.ogg"

    "Ромка же дёрнул изо всех сил, и рюкзак перекочевал к нему."

    if Flags.Has("day2 polina"):
        play test_one "voice/Polina/2day/Polina vzv.ogg"

        "Полина взвизгнула."
        "Ромка подмигнул ей, мол, без паники."

    "Вальяжный и спокойный."

    scene rom_knife_02
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.3)
    play sound "voice/romka/2day/41 Heh.ogg"

    "Противно скалясь, он заглянул внутрь."

    voice "voice/romka/2day/41 Ty ot n.ogg"
    Rom "Ты от нас что-то скрываешь, да?"

    voice "voice/romka/2day/42 U menja.ogg"
    Rom "У меня в школе какая-то крыса сменку подрезала."

    play test_one "sounds/bag2.ogg"

    voice "voice/romka/2day/43 SCHa pogl.ogg"
    Rom "Ща поглядим, может, это был..."

    voice "voice/romka/2day/44 Opaczki.ogg"
    Rom "Опачки!"

    "Ромка многозначительно ухмыльнулся."

    window hide
    scene bg_backpack_crash with Dissolve(0.5)
    $ renpy.pause(3.5)
    window show
    play test_one "sounds/bag3.ogg"

    voice "voice/romka/2day/45 Taktak.ogg"
    Rom "Так-так, а что это у нас здесь?"

    "Учебники и тетради полетели на снег."
    "Хулиган держал в одной руке портфель, а в другой — что-то странное, напоминающее..."
    queue sound [ "<silence 2.0>", "<from 0 to 2>sounds/UP.ogg"]

    window hide
    scene bg_handblood
    show maska_up
    with Dissolve(1.0)
    $ renpy.pause(2.0)
    window show

    "...маску."
    "Он поднял её высоко, словно показывал кому-то ещё, кроме нас, кому-то в кронах, в сумерках за деревьями."
    "Старая маска зайца."
    "Длинные потрёпанные уши, едва заметно нарисованные нос и усы, облезлый мех на щеках."
    "Откуда ей было взяться? Подбросил кто?"

    play sound "voice/semen/2day/51 Seme.ogg"

    "Семён хохотнул."

    voice "voice/semen/2day/52 Novy.ogg"
    Sem "Новый год уже прошёл, мудила!"

    voice "voice/semen/2day/53 Ili.ogg"
    Sem "Или ты реально поехавший?"

    voice "voice/anton/2day/144. Eto ne moe.ogg"
    Ant "Это не моё!"

    voice "voice/byasha/18 Da kak.ogg"
    Bya "Да как не твоё, э? В твоём портфеле лежала, на!"

    play sound "voice/romka/2day/Hah.ogg"

    "Ромка наблюдал за этой сценой, ехидно улыбаясь."

    if Flags.Has("day2 polina"):
        show doggy_fon
        show Polina Scream b_day_winter 01 norm ahead 01
        show snowman_snow_revers
        with Dissolve(0.3)
        show Polina Scream b_day_winter 01 norm ahead 03 with Dissolve(0.1)

        voice "voice/Polina/2day/136 Dikari.ogg"
        Pol "Дикари! Масок раньше не видели?"

        show Polina Scream b_day_winter 01 norm ahead 01 with Dissolve(0.1)

        voice "voice/romka/2day/49 Takih k.ogg"
        Rom "Таких конченых не видели."

        hide doggy_fon
        hide Polina
        hide snowman_snow_revers
        with Dissolve(0.3)

    voice "voice/romka/2day/47 A znaesh.ogg"
    Rom "А знаешь что?.."

    voice "voice/romka/2day/48 Nadevai.ogg"
    Rom "Надевай."

    voice "voice/anton/2day/145. Zachem.ogg"
    Ant "Зачем?"

    voice "voice/romka/2day/50 Nadevai.ogg"
    Rom "Надевай, говорю."

    voice "voice/romka/2day/51 Popryga.ogg"
    Rom "Попрыгаешь перед нами, зайчик."

    voice "voice/byasha/20 Davai davai.ogg"
    Bya "Давай-давай!"

    voice "voice/byasha/21 Ili bez.ogg"
    Bya "Или без штанов домой пойдёшь, на."

    if Flags.Has("day2 polina"):
        "Только не при Полине."
    else:
        "Только не это!"
        "А если мимо кто-то из нашего класса пойдёт?!"

    if not Flags.Has("fight"):
        "Полина, например?!"

    if not Flags.Has("fight"):
        voice "voice/anton/2day/147. Net.ogg"
        Ant "Нет..."
    else:
        voice "voice/anton/2day/146. Ne nadenu.ogg"
        Ant "Не надену..."

    voice "voice/romka/2day/52 Sema n.ogg"
    Rom "Сёма, надень-ка на него."

    play sound "voice/byasha/22 Byasha us.ogg"

    "Бяша услужливо подскочил к приятелю, взял облупленную маску, отвесил шутовской поклон."

    hide maska_up
    with Dissolve(0.5)

    "Затем передал её Семёну, уже потиравшему руки в нетерпении."

    show bg_lisa001
    show snowman_snow
    with Dissolve(0.2)

    "Я оглянулся на сосны."
    "Словно ждал помощи, ждал, что тени, ползающие вокруг нас, сжалятся и займут мою сторону."
    "Ветви напоминали изломанные под страшными углами руки."
    "Почерневшая кора была обварившейся кожей, а тьма — гарью."
    "Не убегу. Не успею. Догонят."
    "И тогда..."

    if Flags.Has("day2 polina"):
        "Нет, никуда не побегу. Я не брошу Полину."

    if Flags.Has("fight"):
        window hide
        scene bg gop_wood_2:
            xpos -720
        show romka 01 03 02:
            xpos -720
            alpha 0.0
            pause 1.0
            linear 1 alpha 1.0
        show baysha 01 02 04:
            xpos -720
        show sema 14:
            xpos -720
        with Dissolve(0.5)
        window show

        voice "voice/romka/2day/53 Tolko.ogg"
        Rom "Только учти, Cёма!"

        show sema 12
        with Dissolve(0.3)

        voice "voice/romka/2day/54 Esli on.ogg"
        Rom "Если он скакать не станет - ты сам за него поскачешь."

        show romka 01 03 05
        show sema 17:
            xpos -720
        with Dissolve(0.3)

        voice "voice/semen/2day/55 Etot.ogg"
        Sem "Этот чмошник и не станет?"




        voice "voice/semen/2day/56 Da p.ogg"
        Sem "Да погляди на него — он же дурик конченный."

        show romka 01 03 02
        show sema 15
        with Dissolve(0.3)

        voice "voice/romka/2day/55 Etot du.ogg"
        Rom "Этот дурик тебе уже раз в жбан зарядил."

        show romka 01 03 06
        show baysha 01 03 04
        show sema 13
        with Dissolve(0.3)

        voice "voice/byasha/23 Romka prav.ogg"
        Bya "Ромка прав!"

        voice "voice/byasha/24 Davai fat.ogg"
        Bya "Давай, толстый, восстанавливай авторитет, на."

        show romka 01 03 04
        show baysha 01 02 01
        show sema 12
        with Dissolve(0.3)

        voice "voice/romka/2day/56 Ili sam.ogg"
        Rom "Или сам у нас запрыгаешь так, что титяндры отцепятся!"

        show romka 01 03 06
        show baysha 01 02 05
        with Dissolve(0.3)

        "Значит, он и вправду боится Ромку."

        show sema 01
        with Dissolve(0.3)

        if Flags.Has("day2 polina"):
            "Семён выругался под нос, злобно зыркнул на меня, затем на Полину."
        if Flags.Has("day2 fox"):
            "Семён выругался под нос, злобно зыркнул на меня."

    scene bg gop_wood_2:
        xpos -720
    show romka 01 03 06:
        xpos -720
    show baysha 01 02 05:
        xpos -720
    show sema 24:
        xpos -720
    with Dissolve(0.3)

    voice "voice/semen/2day/57 Vot.ogg"
    Sem "Вот."

    voice "voice/semen/2day/57 Eto.ogg"
    Sem "Это чтобы маска хорошо налезла!"

    play test_one "voice/semen/2day/58 On s.ogg"
    pause 1

    show baysha 01 03 02
    show sema 20
    with Dissolve(0.3)

    "Он смачно харкнул в заячью морду и поднёс маску к моему лицу."
    "Плевок был похож на раздавленного паука."
    "Ромка как-то по-звериному дёрнулся, скривился, хотел что-то сказать Семёну... но промолчал."

    if Flags.Has("day2 polina"):
        play sound "voice/Polina/2day/152 Zakrila.ogg"
        "Полина в ужасе закрыла лицо ладонями."

    "Сёма тёрся рядом, омерзительно скалясь и опаляя меня вонью из пасти."

    show sema 21
    with Dissolve(0.3)

    voice "voice/semen/2day/59 Nade.ogg"
    Sem "Надевай, быро!"

    $ renpy.start_predict_screen("day2_choice_mask_or_not")
    $ renpy.start_predict("bunny2_mask_anton")
    $ renpy.start_predict("bunny2_mask_sema")

    voice "voice/semen/2day/60 A to.ogg"
    Sem "А то урою!"

    "Маска словно бы стала ещё отвратительнее, злее, но, вопреки всему, казалось..."
    "..она могла подарить спасение."
    "Стать второй кожей — только примерь, только коснись лицом её твёрдой бугристой поверхности, — и мех засеребрится, уши затрепещут живыми мышцами."
    "Стоит надеть её — и Семёна c компанией не станет."
    "Навсегда."

    jump bunny_day2_mask_or_not

    label bunny_day2_mask_dev:
        $ Flags.Raise("fight")
        $ renpy.start_predict_screen("day2_choice_mask_or_not")
        $ renpy.start_predict("bunny2_mask_anton")
        $ renpy.start_predict("bunny2_mask_sema")
        menu:
            "No Fight":
                $ Flags.Drop("fight")
            "Polina":

                $ Flags.Raise("day2 polina")
            "Fox":

                $ Flags.Raise("day2 fox")


label bunny_day2_mask_or_not:
    window hide
    scene bg_gop_wood_MASK:
        xpos -720
        ease 2.0 xpos 0
    $ renpy.pause(2.1)
    scene bg_gop_wood_MASK_choice:
        xpos 0

    $ story_manager.MarkEvent(("day2", "mask"))

    call screen day2_choice_mask_or_not()


label bunny2_take_mask:
    $ renpy.stop_predict("bunny2_mask_anton")
    $ renpy.stop_predict("bunny2_mask_sema")
    $ renpy.stop_predict_screen("day2_choice_mask_or_not")

    $ story_manager.MarkEvent(("day2", "mask", "take"))

    $ Flags.Raise("mask")
    scene bg_gop_wood_MASK:
        xpos 0
    with None
    "Я протянул руку – она больше не дрожала."

    window hide
    scene bg_road_wood:
        xpos -100
    show Byasha Normal m_day_winter 01 normal ahead 01:
        xoffset -540
        yoffset 75
    show Romka Normal m_day_winter 00 norm ahead 01:
        xoffset 540
        yoffset 75
    show Semen Normal m_day_W 00 evil ahead 01
    with Dissolve(0.3)
    $ renpy.pause(0.2)
    show snowman_snow
    show mask_00_up
    with Dissolve(1.0)
    $ renpy.pause(0.5)
    window show
    play sound "voice/semen/2day/Wahaha.ogg"

    "Семён вручил мне маску и злобно расхохотался."
    "Шерсть была тёплой, как я и подозревал."
    "По коже побежали мурашки. Электричество заструилось по позвоночнику."

    voice "voice/anton/2day/197 Vot ono.ogg"
    Ant "Вот оно."

    stop music fadeout 2

    voice "voice/anton/2day/197.2  Moe spasenie.ogg"
    Ant "Моё спасение."

    "Из колодца моего подсознания шептал голос: «{i}Просто надень её — и никто не причинит тебе вреда{/i}»."
    "Лес застыл, всматриваясь в меня трещинами коры."
    "Я начал действовать не спеша."

    scene bg_road_wood blur:
        xpos -100
    show Byasha Normal m_day_winter 01 normal ahead 01 blur:
        xoffset -540
        yoffset 75
    show Romka Normal m_day_winter 00 norm ahead 01 blur:
        xoffset 540
        yoffset 75
    show Semen Normal m_day_W 00 evil ahead 01 blur
    show snowman_snow
    show mask_00_hand
    hide mask_00_up
    with Dissolve(0.3)

    "Снял очки."

    play test_one "sounds/stryahivanie_3.ogg"
    show mask_01_hand
    hide mask_00_hand
    with Dissolve(0.3)

    "Горстью снега стёр гадкий плевок с папье-маше."

    play music2 "music/Flute 2(reverb).ogg"

    "Внутри заячьего лика что-то шевелилось."
    "Словно пыталось пробиться наружу."
    "Надо ему помочь."

    show mask_02_hand
    hide mask_01_hand
    with Dissolve(0.3)

    "Я поднял маску. И стал подносить её к пылающим щекам."
    "Как в том фильме с Джимом Керри..."
    "Маска — это сила."
    "Маска — это власть."

    stop music2 fadeout 3
    scene bg_road_wood:
        xpos -100
    show Byasha Normal m_day_winter 01 normal ahead 01:
        xoffset -540
        yoffset 75
    show Romka Normal m_day_winter 00 norm ahead 01:
        xoffset 540
        yoffset 75
    show Semen Normal m_day_W 00 evil ahead 01
    show snowman_snow
    show mask_03_face
    with Dissolve(0.7)

    "Картонка коснулась щёк."
    "Повторила линию скул, носа, устроилась поудобнее."

    play sound "voice/anton/2day/Vdoh.ogg"

    "Пахло звериной берлогой и хвоей."

    hide mask_03_face
    show mask_03_hide
    with Dissolve(0.3)
    play music "music/35_tense intro.ogg" fadein 3.0
    queue music "music/36_tense loop.ogg"

    "Губы ткнулись в бугристый материал."
    "Моя броня."
    "Удивительно, но сквозь прорези старой карнавальной маски я видел так же хорошо, как сквозь стёкла очков."
    "Застывшая троица на поляне."
    "Замершие в воздухе пушинки."
    "Деревья, чьи тени струились ко мне чёрными ручейками."
    "И странная фигура в ранних сумерках за буреломом."
    "В тишине Семён неуверенно произнёс:"

    show Semen Amazy m_day_W 00 evil ahead 01
    show Byasha Normal m_day_winter 01 shock ahead 01
    with Dissolve(0.3)
    show Romka Worry m_day_winter 01 norm ahead 02 with Dissolve(0.3)

    voice "voice/semen/2day/101 E.ogg"
    Sem "Э, пацаны, что это с ним?"

    "Я расправил плечи."
    "Мускулы налились сталью."
    "Незримые дымчатые шлейфы отделились от стволов и поплыли ко мне."
    "Сила леса впитывались в мои поры."

    show Byasha Scared m_day_winter 01 shock ahead 01 with Dissolve(0.3)

    "Я улыбнулся под маской. Или оскалился."

    play test_one "sounds/sfx_clench_fist.ogg"

    "Засвербели кулаки."
    "Заурчал желудок."

    show Byasha Scared m_day_winter 01 shock ahead 02 with Dissolve(0.3)

    voice "voice/byasha/27 On prevrashyaetsya.ogg"
    Bya "Он превращается..."

    show Byasha Scared m_day_winter 01 shock ahead 01 with Dissolve(0.3)



    "Сами напросились!"

    play sound "sounds/steps/step_snow2.ogg"

    "Я сделал шаг вперёд."

    show snowman_snow behind Semen
    show Semen Amazy b_day_W 00 evil ahead 01 with Dissolve(0.3)
    play sound "sounds/steps/step_snow1.ogg"

    "Семён осторожно двинулся ко мне, будто ступал по тонкому льду."
    "Передо мной вновь вилась тропинка из моих грёз."
    "Бесконечная, манящая, та, что уводит прочь от всех проблем в новую великолепную страну, волшебную Небыляндию."

    play sound "sounds/Zip.ogg"

    "Я дёрнул молнию, расстегнул и сбросил рывком куртку."

    play test_one "voice/anton/2day/198. Zarichal.ogg"

    "Зарычал."
    "Словно что-то металось под шкурой в поисках выхода."
    "И пошёл прямо на Семёна."

    show Byasha Scared m_day_winter 01 shock ahead 02 with Dissolve(0.3)

    voice "voice/byasha/27 On prevrash.ogg"
    Bya "Он превращается!"

    show Byasha Scared m_day_winter 01 shock ahead 01
    show Semen Amazy b_day_W 00 evil ahead 02
    with Dissolve(0.3)

    voice "voice/semen/2day/102 Tvo.ogg"
    Sem "Твою мать!"

    show Byasha Scared m_day_winter 01 shock ahead 02
    show Semen Amazy b_day_W 00 evil ahead 01
    with Dissolve(0.3)

    voice "voice/byasha/28 Prevrashyaetsya.ogg"
    Bya "Превращается..."

    show Romka Angry m_day_winter 01 angry ahead 06 behind Semen
    show Byasha Normal m_day_winter 01 vicious ahead 07 behind Semen
    show Semen Happy b_day_W 00 good ahead 02
    with Dissolve(0.3)
    play music2 "music/38_tense fail.ogg" noloop
    stop music fadeout 1.0

    voice "voice/romka/2day/147 V koncz.ogg"
    Rom "...в конченого мудака!"

    play test_one "voice/semen/2day/Wahaha2.ogg"

    window hide
    scene bg gop_wood_2:
        xpos -720
    show romka 01 03 04:
        xpos -720
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
        ease 0.1 yoffset 20
        ease 0.1 yoffset 0
    show baysha 01 02 03:
        xpos -720
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
        ease 0.09 yoffset 15
        ease 0.09 yoffset 0
    show sema 10:
        xpos -720
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
        ease 0.11 yoffset 22
        ease 0.11 yoffset 0
    with Dissolve(0.5)

    window show

    "Опушка взорвалась истеричным смехом."

    play test_two "voice/byasha/10 Hahah.ogg"

    "Бяша схватился за живот."

    play test_three "voice/romka/2day/148 Uhmil.ogg"

    "Рома ухмылялся, качая головой."

    scene bg gop_wood_2:
        xpos -720
    show romka 01 03 04:
        xpos -720
    show baysha 01 02 03:
        xpos -720
    show sema 07:
        xpos -720
    with Dissolve(0.2)
    scene bg gop_wood_3:
        xpos -720
        ease 2.0 xpos -300
    show romka 01 03 04:
        xpos -720
        ease 2.0 xpos -300
    show baysha 01 02 03:
        xpos -720
        ease 2.0 xpos -300
    show sema 07:
        xpos -720
        ease 2.0 xpos -300

    play test_four "voice/semen/2day/103 A g.ogg"

    play music "music/34_Nikita Kryukov - the Sabbath.ogg"

    "А гогочущий Семён плюнул себе на костяшки и помахал кулаком как дубинкой."
    stop test_four

    $ music_during_lines = 0.75
    voice "voice/semen/2day/104 Nu.ogg"
    Sem "Ну и дебил же ты, Тошик."

    scene bg gop_wood_1:
        xpos -300
    show anton_zay_02:
        xpos -300
    show romka 01 03 04:
        xpos -300
    show baysha 01 02 03:
        xpos -300
    show sema 18:
        xpos -300
    show layer master:
        align (.5, .5)
        zoom 1.05

    play test_one "sounds/sfx_masked_face_punch.ogg"

    show anton_zay_02 with hpunch:
        xpos -300
        linear 0.2 xpos -1000 ypos 10

    $ renpy.pause(0.3)
    show sema 07:
        xpos -300

    play test_one "voice/anton/2day/199. Kulak vrez.ogg"

    "Кулак врезался в маску."
    "Шерсть не смягчила удар."
    "Не было ни силы, ни волшебного дыма, испускаемого соснами."

    scene bg gop_wood_1:
        xpos -300
        ease 2.0 xpos -720
    show romka 01 03 04:
        xpos -300
        ease 2.0 xpos -720
    show baysha 01 02 03:
        xpos -300
        ease 2.0 xpos -720
    show sema 10:
        xpos -300
        ease 2.0 xpos -720

    play sound "voice/anton/2day/203. Ya otletel.ogg"

    "Я отлетел к кустам и упал на пятую точку."

    scene bg gop_wood_1 blur:
        xpos -720
    show romka byasha blur:
        xpos -720
    show sema 10 blur:
        xpos -720

    if Flags.Has("day2 polina"):
        show doggy_fon
        show Polina Front b_day_winter 01 sadly ahead 03
        show snowman_snow_revers
        with Dissolve(0.3)

        "К моему ужасу за спинами веселящейся стаи стояла бледная Полина."
        "Она смотрела на меня со смесью удивления и непонимания."
        "И, возможно, разочарования."
        "Хотя, чего я ожидал?"
        "Что обращусь супергероем и спасу её, нацепив старый кусок картона на морду?"

        show doggy_fon blur
        show Polina blur
        with Dissolve(1.0)

        "Зрение, обострённое адреналином, снова упало."
        "Напряжённое лицо Полины размывалось."

        hide doggy_fon
        hide Polina
        hide snowman_snow_revers
        with Dissolve(0.3)
    else:

        with Dissolve(1.5)

        "Зрение, обострённое адреналином, снова упало."

    voice "voice/romka/2day/149 Vot et.ogg"
    Rom "Вот это был номер!"

    voice "voice/romka/2day/150 Dumal.ogg"
    Rom "Думал, он на четвереньки встанет и сгрызёт нас всех."

    voice "voice/romka/2day/151 Kak mo.ogg"
    Rom "Как морковку!"

    voice "voice/byasha/30 Ne nu vi videli.ogg"
    Bya "Не, ну вы видели, на?"

    voice "voice/byasha/31 Videli.ogg"
    Bya "Видели?!"

    voice "voice/semen/2day/105 Eto.ogg"
    Sem "Это считается, что он попрыгал?"

    voice "voice/romka/2day/152 Eto da.ogg"
    Rom "Это даже лучше."

    play test_one "voice/anton/2day/Vshlip.ogg"

    "Я всхлипнул."

    scene bg_sema attack_fon blur
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(0.5)

    "У маски всё же был один плюс: если я разревусь, никто этого не увидит."

    voice "voice/semen/2day/106 Nu.ogg"
    Sem "Ну и дурик."

    voice "voice/semen/2day/Datebevpsih.ogg"
    Sem "Да тебе в психбольнице место!"

    voice "voice/byasha/32 V psohbolnice.ogg"
    Bya "В психбольнице для животных, на!"

    "Семён упёрся коленом в сугроб."

    play test_one "voice/semen/2day/107 I v.ogg"

    "И вырвал из моих онемевших пальцев очки." with hpunch

    if Flags.Has("day2 polina"):
        voice "voice/Polina/2day/141 Verni emu.ogg"
        Pol "Верни ему!"

        voice "voice/Polina/2day/142 Verni gad.ogg"
        Pol "Верни, гад!"

    show sema attack_blurred with Dissolve(0.2)

    voice "voice/anton/2day/200 Otdai ochki.ogg"
    Ant "Отдай очки!"

    show bg_sema attack_fon_dark
    show sema attack_blurred_dark

    voice "voice/anton/2day/200.2 Ya domoi.ogg"
    Ant "Я домой не дойду!"

    voice "voice/semen/2day/108 CZush.ogg"
    Sem "Чушь!"

    voice "voice/semen/2day/109 Zna.ogg"
    Sem "Знаешь, какой у зайцев нюх?"

    voice "voice/semen/2day/109 Po.ogg"
    Sem "По запаху доберёшься, не ссы."

    voice "voice/semen/2day/110 Pry.ogg"
    Sem "Прыг-скок! Прыг-скок!"

    scene bg kenti
    show kenti_army
    with Dissolve(0.5)

    $ renpy.start_predict("gohome01_dark_blur")
    $ renpy.start_predict("gohome01_1_dark_blur")
    $ renpy.start_predict("gohome02_dark_blur")
    $ renpy.start_predict("gohome02_1_dark_blur")
    $ renpy.start_predict("gohome03_dark_blur")
    $ renpy.start_predict("gohome03_1_dark_blur")
    $ renpy.start_predict("gohome04_dark_blur")
    $ renpy.start_predict("gohome04_1_dark_blur")

    play sound "voice/semen/2day/08 Tols.ogg"

    "Семён сунул трофей себе в карман и довольно ощерился."

    voice "voice/semen/2day/111 Kro.ogg"
    Sem "Кролики очки не носят."

    voice "voice/romka/2day/153 A tepe.ogg"
    Rom "А теперь вали отсюда, даун!"

    play test_one "voice/anton/2day/142. Semen.ogg"

    "Я, пошатываясь, встал."
    "Деревья размылись в сплошную стену тьмы."

    if Flags.Has("day2 polina"):
        "Вокруг колебались четыре размытых силуэта."
    else:
        "Вокруг колебались три размытых силуэта."

    "Чёрные пятна – глазницы и рты. Только мерещилось, что глаз и ртов больше, чем должно быть."

    if Flags.Has("day2 polina"):
        voice "voice/anton/2day/202. Polina.ogg"
        Ant "Полина!"

        "Я пошарил почти вслепую. Одна из фигур дёрнулась ко мне, но другая преградила дорогу."

        voice "voice/romka/2day/154 Ty ne.ogg"
        Rom "Ты не переживай, ушастый."

        voice "voice/romka/2day/155 My Pol.ogg"
        Rom "Мы Полину сами проводим. В обиду не дадим."

        voice "voice/romka/2day/156 A to t.ogg"
        Rom "А то тут психов по лесу шляется – мама не горюй. Да, Полин?"

        play test_one "voice/Polina/2day/Oi.ogg"

        "Она промолчала. Отступила к кустам."
        "Отчаянье клокотало во мне."

    scene bg_black
    show gohome01_dark_blur_stop:
        xpos -1920
    show gohome02_dark_blur_stop:
        xpos -1920
    show gohome03_dark_blur_stop:
        xpos -1920
    show gohome04_dark_blur_stop:
        xpos -5660+1920-90
    with Dissolve(0.5)

    "Я повернулся к лесу."

    scene bg_black
    show gohome01_dark_blur
    show gohome01_1_dark_blur
    show gohome02_dark_blur
    show gohome02_1_dark_blur
    show gohome03_dark_blur
    show gohome03_1_dark_blur
    show gohome04_dark_blur
    show gohome04_1_dark_blur
    show layer master:
        align (.5, .5)
        zoom 1.02
    with vpunch

    play sound "voice/anton/2day/203. Botinok.ogg"
    play test_one "sounds/sfx_punch.ogg"

    $ renpy.stop_predict("gohome01_dark_blur")
    $ renpy.stop_predict("gohome01_1_dark_blur")
    $ renpy.stop_predict("gohome02_dark_blur")
    $ renpy.stop_predict("gohome02_1_dark_blur")
    $ renpy.stop_predict("gohome03_dark_blur")
    $ renpy.stop_predict("gohome03_1_dark_blur")
    $ renpy.stop_predict("gohome04_dark_blur")
    $ renpy.stop_predict("gohome04_1_dark_blur")

    play test_seven "sounds/steps/loop_footsteps_one.ogg" loop
    "Ботинок Семёна помог, врезавшись мне в зад и ускорив тем самым постыдный побег."

    show bad_mask_bg_blur
    show bad_mask 0_blur
    with Dissolve(0.5)

    voice "voice/byasha/33 Prig skok.ogg"
    Bya "Прыг-скок! Прыг-скок!"

    stop music fadeout 3.0
    show bad_mask 3_blur
    pause 1.0
    play test_one "sounds/sfx_drop_mask.ogg"
    play test_three "voice/anton/2day/41. Ya prochistil.ogg"

    "От обиды я швырнул маску в овраг."
    $ achievement_grant("ach_masquerade")

    hide bad_mask_bg_blur
    hide bad_mask
    with Dissolve(0.5)
    play test_two "sounds/steps/loop_footsteps_1.ogg" loop
    play music "music/Morning Tensions.ogg" volume 0.75

    "А затем пошёл зигзагами по просеке, один-одинёшенек в огромном заснеженном мире."
    "Стволы выгибались, их кроны исчезали во мраке."

    show snow_night_2_left:
        alpha 0.0
        linear 5.0 alpha 1.0

    "Небо будто придавливало к земле."
    "Хотелось плакать, но слёзы иссякли."

    stop test_two fadeout 4.0
    $ renpy.start_predict("bg house_night6_snow_blur")

    "Осталось уныние и тоска, желание зарыться в снег или уйти в Небыляндию, присоединившись к Вове и Сенечке."
    "Куда угодно – лишь бы подальше отсюда."
    "Прочь."

    stop music fadeout 2
    stop test_seven fadeout 2
    jump bunny2_home_evening


label bunny2_skip_mask:
    $ renpy.stop_predict("bunny2_mask_anton")
    $ renpy.stop_predict("bunny2_mask_sema")
    $ renpy.stop_predict_screen("day2_choice_mask_or_not")

    $ story_manager.MarkEvent(("day2", "mask", "refuse"))

    scene bg_gop_wood_MASK:
        xpos 0
    with None
    stop music fadeout 3.0
    play music2 "music/35_tense intro.ogg" fadein 1.0
    queue music2 "music/36_tense loop.ogg"
    scene bg_road_wood:
        xpos -225
        linear 1.0 xpos -75
        linear 5.0 xpos 0
    show anton_battle_romka 1:
        xpos 0 xoffset 1000
        linear 1.0 xoffset 150
        linear 5.0 xoffset 0
    show anton_battle_byasha 1:
        xpos 0 xoffset 1000
        linear 1.0 xoffset 150
        linear 5.0 xoffset 0
    show Semen Serious m_day_W 00 evil ahead 01:
        xpos 0 xoffset 1000
        linear 1.0 xoffset 250
        linear 5.0 xoffset -70
    show snowman_snow
    with Dissolve(0.3)

    "Почему-то Ромкино недовольство Семёном меня расхрабрило."
    "Что-то у них было не так в банде, старые разногласия..."
    "Мне бы расковырять эту рану."


    scene anton_battle_bg_2:
        xpos -225
        linear 1.0 xpos -75
        linear 5.0 xpos 0
    show anton_battle_anton 2:
        xpos 0 xoffset 1000
        linear 1.0 xoffset 150
        linear 5.0 xoffset 0
    show snowman_snow_revers
    show anton_battle_motion_2:
        xpos -2000
        linear 0.5 xpos 2000
    with Dissolve(0.3)

    if Flags.Has("day2 fox"):
        "Пролезть бы в их головы, в их черепа, в их тёплые мозги."

    show anton_battle_anton 2_open with Dissolve(0.3)

    voice "voice/anton/2day/148.Znaesh chto.ogg"
    Ant "Знаешь что, Семён..."


    scene bg_road_wood:
        xpos -225
        linear 1.0 xpos -75
        linear 5.0 xpos 0
    show Romka Angry m_day_winter 01 angry ahead 01:
        zoom 1.1 xpos 0 xoffset 1000 ypos 100
        linear 1.0 xoffset 550
        linear 5.0 xoffset 400
    show Byasha Normal m_day_winter 01 normal ahead 01:
        zoom 1.1 xpos 0 xoffset 1000 ypos 100
        linear 1.0 xoffset -400
        linear 5.0 xoffset -650
    show Semen Serious m_day_W 00 evil ahead 01:
        zoom 1.3 xpos 0 xoffset 1000 ypos -100
        linear 1.0 xoffset -150
        linear 5.0 xoffset -350
    show snowman_snow
    with Dissolve(0.3)

    "Собственный голос – ровный и твёрдый – удивил меня."
    "Я сделал шаг вперёд и тихо, спокойно отчеканил:"


    scene anton_battle_bg_2:
        xpos -225
        linear 1.0 xpos -75
        linear 5.0 xpos 0
    show anton_battle_anton 4:
        xpos 0 xoffset 1000
        linear 1.0 xoffset 150
        linear 5.0 xoffset 0
    show snowman_snow_revers
    show anton_battle_motion_4:
        xpos -2000
        linear 0.5 xpos 2000
    with Dissolve(0.3)
    show anton_battle_anton 4_bad_open with Dissolve(0.3)

    voice "voice/anton/2day/149. Idi nahui.ogg"
    Ant "Иди на хуй."

    show anton_battle_anton 4_bad with Dissolve(0.3)

    "Мир словно поставили на паузу, а через секунду разморозили."

    scene bg_road_wood
    show layer master:
        align (.5, .5)
        zoom 1.05
    show Semen Amazy b_day_W 00 good ahead 01:
        xalign 0.5
        yalign 1.0
        xoffset 0
        yoffset 0
        zoom 1.0
    show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
        xoffset -540
        yoffset 75
    show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
        xoffset 540
        yoffset 75
    show snowman_snow
    with Dissolve(0.3)

    "Зрачки Семёна расширились. Маска выпала из мясистых рук."

    play sound "voice/semen/2day/62 On n.ogg"

    "Он некоторое время отуплено переваривал услышанное, будто тужился решить в уме сложное уравнение, и, судя по пульсирующей на лбу вене, ответ приводил его в бешенство."

    show Semen Amazy b_day_W 00 evil ahead 03 with Dissolve(0.2)
    play test_one "voice/semen/2day/61 Osta.ogg"

    "Остальные молча наблюдали за нами, предвкушая скорую расправу."

    if Flags.Has("day2 polina"):
        "Я заметил, как вытягивается от ужаса лицо Полины."

    show Semen Amazy b_day_W 00 evil ahead 04 with Dissolve(0.2)

    voice "voice/semen/2day/63 Ty.ogg"
    Sem "Ты... Ты!.."

    show Semen Amazy b_day_W 00 evil ahead 03 with Dissolve(0.2)
    $ renpy.pause(0.3)

    hide bg_road_wood
    hide Byasha Normal m_day_winter 01 normal ahead 01
    hide Romka Normal m_day_winter 00 norm ahead 01
    hide Semen
    show bg_road_wood:
        pos (.5,.5)
        anchor (.5,.5)
        linear .2 zoom 1.03
        linear .2 zoom 1.00
    show Byasha Normal m_day_winter 01 normal ahead 01:
        pos (.5,.5)
        anchor (.5,.5)
        xoffset -540
        yoffset 75
        linear .2 zoom 1.05
        linear .2 zoom 1.00
    show Romka Normal m_day_winter 00 norm ahead 01:
        pos (.5,.5)
        anchor (.5,.5)
        xoffset 540
        yoffset 75
        linear .2 zoom 1.05
        linear .2 zoom 1.00

    show Semen Amazy b_day_W 00 evil ahead 04:
        pos (.5,.5)
        anchor (.5,.5)
        linear .2 zoom 1.20


    show focus_lines_bright:
        align (.5,.5)
        alpha 0
        linear .2 alpha 1

    with hpunch

    voice "voice/semen/2day/64 Ty t.ogg"
    Sem "ТЫ ТРУП!!!"

    show Semen Amazy b_day_W 00 evil ahead 03 with Dissolve(0.2)

    if Flags.Has("day2 fox"):
        $ story_manager.MarkEvent(("day2", "s_fox0"))
        hide focus_lines_bright
        with dissolve
        "В дебрях зазвенел ледок, срываясь с ветвей."
        "Звук напоминал мелодичный смех."
        "И тут я услышал шёпот из крон, из нор, из лесных берлог."
        "Будто бы Алиса, притаившись в сугробе, словно суфлёр из будки, старалась достучаться до меня."
        "Не испуганная, а с весёлым гневом в голосе, – так представлялся мне этот тихий гул."

        scene bg_lisa001 with Dissolve(0.5)
        show snowman_snow

        "Я уставился в проём между деревьями."
        play sound "sounds/sfx_drop_mask.ogg"

        window hide
        show bg_lisa_anim behind snowman_snow
        $ renpy.pause(0.6)
        hide bg_lisa_anim
        window show

        "Там мелькнуло рыжее пятно."

        show bg_lisa_stand behind snowman_snow
        with Dissolve(0.3)

        "Лиса – настоящая, обыкновенная лиса – выступила из-за кустарника."

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
        $ renpy.pause(1.1)
        show bg_lisa_smeh behind snowman_snow
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
        pause 0.3
        scene bg_lisa_anim_smeh with Dissolve(0.3)
        show snowman_snow

        "Я моргнул ошарашенно."
        "Животное, припав на живот, буравило меня горящими глазками."

        "Пушистый хвост сновал по снегу, разбрасывая белую пыль."

        voice "voice/semen/2day/66 Na m.ogg"
        Sem "На меня смотри, падла!"

        "Но я смотрел мимо, на лису, которая... улыбалась мне."

        play test_one "sounds/sfx_snow_digging.ogg" loop

        "Оскалившись, она рыла нору в сугробе, двигала лапами так, будто танцевала."

        scene bg_lisa_anim_smeh_reverse with Dissolve(0.3)
        pause 0.1
        scene bg_lisa_anim_smeh1 with Dissolve(0.3)
        pause 0.1
        show bg_lisa_anim_smeh1_1 with Dissolve(0.3)
        stop test_one fadeout 1.0

        play test_two "voice/Alisa/Alisa2day/168 Morda.ogg"

        "Острая морда была в снегу, усики подёргивались. Оскалившись, лиса обнажила частокол желтоватых зубов."








        play test_two "sounds/sfx_fox_breath.ogg"

        "Лиса припала передом ещё ниже к земле. Сверкающие плошки глаз налились расплавленным серебром."
        "Я перевёл взгляд на перекошенное лицо Семёна."

        scene bg_road_wood
        show layer master:
            align (.5, .5)
            zoom 1.05
        show Semen Amazy b_day_W 00 evil ahead 03:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            zoom 1.0
        show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
            xoffset -540
            yoffset 75
        show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
            xoffset 540
            yoffset 75
        show snowman_snow
        with Dissolve(0.3)
        play test_three "voice/semen/2day/67 On cz.ogg"

        "Он что-то рычал – я не понимал, что."
        "Лиса пошла задом наперёд и скрылась в темноте."
        "А из леса на меня дохнуло шёпотом."

        voice "voice/Alisa/Alisa2day/169 Skazi.ogg"
        Noname "СКАЖИ..."

        voice "voice/Alisa/Alisa2day/169 Svinie.ogg"
        Noname "...СВИНЬЕ..."

        voice "voice/Alisa/Alisa2day/169 Zatkn.ogg"
        Noname "...ЗАТКНУТЬСЯ."

        play test_one "voice/anton/2day/150. Ya hlopnul.ogg"

        "Я хлопнул рукой по щеке, прогоняя чужой голос." with hpunch
        "Но смысл послания остался на подкорке."

        play test_one "voice/semen/2day/68 Pods.ogg"

        "Подсказка — мой шанс."

        play test_one "voice/semen/2day/70 YA us.ogg"

        "Я уставился на переносицу хрюкающего от злобы Семёна и проговорил:"

        scene anton_battle_bg_2
        show anton_battle_anton 4_evil
        show snowman_snow_revers
        with Dissolve(0.5)
        show anton_battle_anton 4_evil_open
        with Dissolve(0.3)

        voice "voice/anton/2day/152. Shut up pig.ogg"
        Ant "Заткнись, свинья!"

        scene bg_road_wood
        show Semen Amazy b_day_W 00 good ahead 01:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            zoom 1.0
        show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
            xoffset -540
            yoffset 75
        show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
            xoffset 540
            yoffset 75
        show snowman_snow
        with Dissolve(0.3)
        play test_three "voice/semen/2day/72 Seme.ogg"

        "Семёна будто парализовало."

        $ add_text_to_dictionary(22)

        "Словно экстрасенс {u}Аллан Чумак{/u} загипнотизировал его, лишил воли."

        if Flags.Has("gum"):
            "Во рту возник привкус Алисиной жвачки."
            "Ягодный, терпкий."

        "Я словно вытянул карту из засаленной колоды, и она оказалась козырной."
        "Мозг работал на пределах возможностей."
        "Словно киношные титры, промелькнули слова Полины о том, что после переезда характер Семёна испортился."
        "Пазлы сложились."
        "Козырь полетел в прыщавую физиономию."
        "Я говорил вальяжно, растягивая слоги."


        scene anton_battle_bg_2
        show anton_battle_anton 4_evil
        show snowman_snow_revers
        with Dissolve(0.5)
        show anton_battle_anton 4_evil_grid
        with Dissolve(0.3)

        voice "voice/anton/2day/153. Est y menya.ogg"
        Ant "Есть у меня подозрение: ты не просто так перевёлся в новую школу."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/154. Zbezal.ogg"
        Ant "Сбежал, да? Как крыса сбежал."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/155. Potomu chto sv.ogg"
        Ant "Потому что сверстники бывают жестокими... с теми, кто не такой, как они."

        voice "voice/anton/2day/156. S temi kto.ogg"
        Ant "С теми, кто толще их, например. Слабее."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/157. I ti reshil.ogg"
        Ant "И ты решил издеваться над другими. Как издевались над тобой."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        play sound "voice/semen/2day/73 YA uv.ogg"

        "Я увидел, как дёрнулся кадык Семена – словно перезарядили помповую винтовку."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/158 Ti otigrivaeshsa.ogg"
        Ant "Ты отыгрываешься за старые обиды."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/158.2 Hochesh kazats.ogg"
        Ant "Хочешь казаться тем, кем не являешься."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/159 No zhaesh nichego.ogg"
        Ant "Но, знаешь, ничего не меняется по щелчку пальца."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/159.2 Zhaesh kem ti bil.ogg"
        Ant "Знаешь, кем ты был?"

        show anton_battle_anton 4_evil with Dissolve(0.2)

        "Лес затаил дыхание, слушая, наслаждаясь."

        show anton_battle_anton 4_evil with Dissolve(0.2)
        $ renpy.pause(0.3)
        show anton_battle_anton 4_evil_grid with Dissolve(0.2)

        voice "voice/anton/2day/160. Zhaesh kto ti est.ogg"
        Ant "Знаешь, кто ты есть?"

        scene bg_road_wood
        show Semen Amazy b_day_W 00 good ahead 01:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            zoom 1.0
        show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
            xoffset -540
            yoffset 75
        show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
            xoffset 540
            yoffset 75
        show snowman_snow
        with Dissolve(0.3)

        voice "voice/semen/2day/74 Pap.ogg"
        Sem "П-пацаны..."

        show Byasha Normal m_day_winter 01 evil ahead 01 behind Semen:
            xoffset -1000
            yoffset -75
            zoom 1.5
        show Romka Angry m_day_winter 00 angry aside 01 behind Semen
        with Dissolve(0.3)
        play sound "voice/byasha/34 Byasha shagnul.ogg"

        "Бяша шагнул было к приятелю, но Ромка осадил его, хлеснув властным взглядом."

        show Byasha Normal m_day_winter 01 vicious ahead 03 behind Semen:
            xoffset -540
            yoffset 75
            zoom 1.0
        show Romka Angry m_day_winter 00 angry ahead 01 behind Semen
        with Dissolve(0.3)
        play test_one "voice/byasha/35 Tot retir.ogg"

        "Тот ретировался, сунув руки в карманы."

        show Romka Angry m_day_winter 01 angry ahead 04 with Dissolve(0.3)

        voice "voice/romka/2day/57 Prodolzh.ogg"
        Rom "Продолжай, Тоха."

        show Romka Angry m_day_winter 01 angry ahead 05 with Dissolve(0.3)

        "Слова Ромки рикошетили от шершавых стволов."

        scene bg gop_wood_2
        show bg_gop_wood_1_SemAnx
        with Dissolve(0.2)

        voice "voice/anton/2day/161. Znaesh kem ti budesh.ogg"
        Ant "Знаешь, кем ты будешь всегда?"

        show bg_gop_wood_1_SemAnxAnim
        with Dissolve(0.2)

        "Семён беспомощно озирался."

        voice "voice/anton/2day/162. Vtoroe imya.ogg"
        Ant "Второе имя — настоящее имя, — которое дали тебе одноклассники..."

        show bg_gop_wood_1_SemAnx_Baysha_eyes
        with Dissolve(0.2)

        voice "voice/semen/2day/75 Otku.ogg"
        Sem "Отк-куда... т-ты?.."

        play test_one "voice/byasha/36 Teper Romka.ogg"

        "Теперь Ромка и Бяша смотрели на Семёна, как на добычу."

        play sound "voice/byasha/37 Daze pokazalos.ogg"

        "Даже показалось, что облизывали свои сухие губы."
        "И ветер тоже облизывался, гоняя вдоль дороги мои разбросанные тетради."

        scene anton_battle_bg_2
        show anton_battle_anton 4_evil
        show snowman_snow_revers
        with Dissolve(0.5)
        show anton_battle_anton 4_evil_open
        with Dissolve(0.2)

        voice "voice/anton/2day/163. Pig.ogg"
        Ant "Свинья!!!"

        scene bg_lisa001
        show snowman_snow
        with Dissolve(0.5)

        "Мой громогласный крик эхом полетел по лесу."
        "Деревьям и оврагам он понравился."
        "Эхо повторило, удвоило, утроило возглас."

        scene bg_road_wood
        show Semen Amazy b_day_W 00 good ahead 01:
            xalign 0.5
            yalign 1.0
            xoffset 0
            yoffset 0
            zoom 1.0
        show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
            xoffset -540
            yoffset 75
        show Romka Angry m_day_winter 01 angry ahead 05 behind Semen:
            xoffset 540
            yoffset 75
        show snowman_snow
        with Dissolve(0.3)

        "Рома оскалился, блеснув зубами."

        play test_one "voice/semen/2day/76 Ruki.ogg"

        "Руки Семёна упали по швам, глаза намокли, а я воспользовался преимуществом."

        window hide
        play test_one "sounds/z - v ebalo.ogg"
        $ renpy.pause(2.2)
        stop music2 fadeout 1.0
        queue sound [ "<silence 1.1>", "<from 0 to 2>voice/anton/2day/164. Ruki Semena.ogg"]
        scene bg_anton_punch_semen with Dissolve(0.3)

        queue test_three [ "<silence 1.1>", "<from 0 to 2>voice/semen/2day/77 Udar.ogg"]
        $ renpy.pause(1.3)
        window show

        "Ударил со всего маха."
        $ achievement_grant("ach_fight")

        play music "music/34_Nikita Kryukov - the Sabbath.ogg"

        window hide
        scene semen_down:
            xpos 0
            ypos -345
            ease 1 ypos 0
            linear 0.05 xoffset 4 yoffset 4
            linear 0.05 xoffset -4 yoffset 4
            linear 0.05 xoffset 4 yoffset -4
            linear 0.05 xoffset -4 yoffset -4
            linear 0.05 xoffset 4 yoffset 4
            linear 0.05 xoffset -4 yoffset 4
            linear 0.05 xoffset 4 yoffset -4
            linear 0.05 xoffset -4 yoffset -4
            linear 0.05 xoffset 0 yoffset 0
        with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        play test_one "sounds/sfx_fall_on_snow.ogg"

        window show
        play sound "voice/semen/2day/78 Gora.ogg"

        "Гораздо сильнее, чем в первый раз в школе."
        "До хруста впечатал кулак в его испуганную физиономию."
        "Прыщавая щека заплясала под костяшками, как поверхность киселя."
        "Охнув, Семён плюхнулся на заледеневшую дорогу."

        play sound "voice/semen/2day/79 On d.ogg"

        "Он держался за ушибленное место, не понимая, что происходит и как так вышло."

        scene bg_anton_battle_wood_4_mouth_smile
        show snowman_snow_revers
        with Dissolve(0.3)

        "И, глядя на него, я понял, что улыбаюсь."

        window hide
        play sound "voice/semen/2day/80 Tols.ogg"
        scene bg_sema_battle_appear2
        $ renpy.pause(2.0)
        window show

        "Толстяк наконец очухался, вскочил на ноги и, скорчив яростную гримасу, бросился на меня с кулаками."

        window hide
        scene bg_sema_battle_disappear2 with Dissolve(0.3)
        $ renpy.pause(2.0)
        window show

        "Но я, разгорячённый игрой в снежки, ловко увернулся."

        window hide
        play test_one "sounds/sfx_fall_on_snow.ogg"
        scene bg_sema_kakahi
        show layer master:
            align (.5, .5)
            zoom 1.05
        with hpunch
        $ renpy.pause(3.0)
        window show
        play sound "voice/semen/2day/81 on p.ogg"

        "Он полетел на снег, неудачно приземлился прямо на кучу свежих собачьих какашек и обиженно взвизгнул."

        $ music_during_lines = 0.75
        voice "voice/romka/2day/58 Ai kras.ogg"
        Rom "Ай, красава, Тоха!"

        voice "voice/romka/2day/59 Dumal.ogg"
        Rom "Думал, ты сосунок, а вон как жирдяя уделал!"

        "Семён захныкал, осознав всю гибельность своего положения."

        voice "voice/semen/2day/81 Suka.ogg"
        Sem "С-сука!"

        voice "voice/semen/2day/82 CZo ja.ogg"
        Sem "Чё я бабушке теперь скажу?"

        voice "voice/semen/2day/83 Ona.ogg"
        Sem "Она меня убьёт, когда увидит!"

        scene bg_road_wood_dark
        show Byasha Normal m_day_winter 01 normal ahead 01 behind Semen:
            xoffset -540
            yoffset 75
        show Romka Normal m_day_winter 00 norm ahead 01 behind Semen:
            xoffset 540
            yoffset 75
        show snowman_snow
        with Dissolve(0.3)

        voice "voice/romka/2day/60 CZego ty.ogg"
        Rom "Чего ты там скулишь?"

        voice "voice/romka/2day/61 Tebja s.ogg"
        Rom "Тебя с параши не слышно."

        play test_one "voice/semen/2day/84 Tczet.ogg"

        show Byasha Hee m_day_winter 01:
            xoffset -540
            yoffset 75
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0
            ease 0.1 yoffset 20
            ease 0.1 yoffset 0

        play sound "voice/byasha/37 Tshet.ogg"

        "Тщетные потуги Семёна снегом отчистить дубленку вызвали у Бяши приступ веселья."
        "Я тоже улыбнулся. Криво, зло."

        voice "voice/byasha/38 Mastev.ogg"
        Bya "Ха-ха! Мастёвый, на!"

        show Romka Evil m_day_winter 01 normal ahead 02:
            xoffset 540
            yoffset 75
        with Dissolve(0.3)

        voice "voice/romka/2day/62 A nu vs.ogg"
        Rom "А ну, вставай и скачи, как зайчик."

        voice "voice/romka/2day/63 Tolko.ogg"
        Rom "Только желательно подальше, а то от тебя уже дерьмом несёт."

        voice "voice/romka/2day/64 Fu B.ogg"
        Rom "Фу!"

        voice "voice/semen/2day/85 Hru.ogg"
        Sem "Хрю-у-у-у-у-у..."

        voice "voice/semen/2day/86 Idit.ogg"
        Sem "Идите вы все на хер!"

        play sound "voice/semen/2day/87 Ego.ogg"

        "Его красные зарёванные глаза остановились на мне."

        window hide
        scene bg_sema_battle_revenge
        show layer master:
            align (.5, .5)
            zoom 1.05
        $ renpy.pause(2.0)
        window show
        play sound "voice/semen/2day/88 Ne u.ogg"

        "Не успел я стереть улыбку с губ, как Cемён налетел коршуном, вцепился мне в лицо скрюченными пальцами с обгрызенными ногтями."

    if Flags.Has("day2 polina"):
        $ story_manager.MarkEvent(("day2", "s_polina0"))
        window hide
        scene bg_sema_battle_appear
        show layer master:
            align (.5, .5)
            zoom 1.05
        $ renpy.pause(4.0)
        window show

        "Cемён налетел коршуном, вцепился мне в лицо скрюченными пальцами, обгрызенными ногтями."

    play test_one "sounds/sfx_kick_pull_glasses.ogg"
    play sound "voice/semen/2day/89 YA pn.ogg"

    "Я пнул куда-то в слой жира под дублёнкой." with hpunch

    if Flags.Has("day2 polina"):
        show doggy_fon
        show Polina Front b_day_winter 01 angry ahead 03
        show snowman_snow_revers
        with Dissolve(0.3)
        show Polina Front b_day_winter 01 angry ahead 10 with Dissolve(0.1)

        voice "voice/Polina/2day/137 Da vsip.ogg"
        Pol "Да! Всыпь ему!"

        scene bg_sema attack_fon_day with Dissolve(0.3)

        "И мир лишился чёткости, расплылись контуры чёрных деревьев, затуманились лица одноклассников."

        scene bg_sema_attack_day with Dissolve(0.3)

    if Flags.Has("day2 fox"):
        scene bg_sema attack_fon with Dissolve(0.3)

        "И мир лишился чёткости, расплылись контуры чёрных деревьев, затуманились лица одноклассников."

        scene bg_sema_attack with Dissolve(0.3)

        voice "voice/semen/2day/90 A czo.ogg"
        Sem "А чё на это скажешь, сука?"

        "Он победно поднял руку с моими очками."
        "Но триумф длился недолго."

        scene bg_sema_attack_juctice with Dissolve(0.3)

        "Два расплывчатых силуэта выскочили вперёд."
        "Бывшие Сёмины дружки."

        scene bg_sema_attack_juctice_punish with Dissolve(0.3)

        play sound "sounds/loop_kicking.ogg" loop
        play test_one "voice/semen/2day/91YA usl.ogg"
        play test_seven "voice/romka/2day/64 ja uslysh.ogg"

        "Я услышал знакомый до боли звук: на Семёна посыпались смачные оплеухи."

        $ music_during_lines = 1.0
        voice "voice/romka/2day/65 Ne pop.ogg"
        Rom "Не по-пацански поступаешь, гнида!"

        voice "voice/romka/2day/66 A nu go.ogg"
        Rom "А ну, гони линзы назад!"

        voice "voice/byasha/40 Deris.ogg"
        Bya "Дерись по понятиям, на!"

        play test_two "voice/byasha/Na-na.ogg"

        "Судя по охам и кряхтению Семёна, на уговоры друзей он не поддавался."

        voice "voice/semen/2day/92 Vy cz.ogg"
        Sem "Вы чё творите?.."

        voice "voice/semen/2day/93 Oi b.ogg"
        Sem "Ой, бля!"

        voice "voice/semen/2day/94 Na l.ogg"
        Sem "На лоха позорного меня променяли... Ой-ой!"

        voice "voice/semen/2day/95 Da p.ogg"
        Sem "Да пошли вы в жопу! Тоже мне друзья..."

        voice "voice/semen/2day/96 Hru.ogg"
        Sem "Хрю-у-у-у-у-у-у-у!"

        stop sound fadeout 1.0

        play test_one "voice/romka/2day/Blya.ogg"

        "Крупная фигура, барахтающаяся в снегу, кое-как смогла вырваться из-под града тумаков и бросилась наутёк, быстро растаяв в потёмках."
        stop test_one fadeout 1.0

        scene bg_sema_attack_threat with Dissolve(0.7)

        voice "voice/romka/2day/68 Zavtra.ogg"
        Rom "Завтра в школе тебя выцепим, Хрюндель!"

        voice "voice/byasha/41 Tochno tochno.ogg"
        Bya "Точно-точно!"

        voice "voice/byasha/42 Za bazar.ogg"
        Bya "За базар ответишь, на!"

        voice "voice/romka/2day/157 Gorlo tebe pererezu.ogg"
        Rom "Горло тебе перережу, слышишь!"

        play test_one "sounds/Rom&Byash.ogg"

        "Ромка и Бяша начали швырять глыбы льда вслед убегающему Семёну, а потом вместе страшно закричали, запричитали глумливо:"

        voice "voice/romka/2day/69 Svinja.ogg"
        "«Свинья!»"

        stop music fadeout 5.0
        scene bg_road_wood heavy_dark_blur:
            xpos -100
        with Dissolve(0.5)

        play test_one "sounds/steps/Rom&Byash_step.ogg"

        "Захрустел снег."

        show Byasha Hee m_day_winter 01 heavy_dark_blur:
            xoffset -540
            yoffset 75
        show Romka Normal m_day_winter 00 norm ahead 01 heavy_dark_blur:
            xoffset 540
            yoffset 75
        with Dissolve(0.7)

        "Запыхавшиеся ребята приблизились ко мне, и я наконец смог разглядеть их прибавившие в резкости лица."

        voice "voice/anton/2day/174. Moi ochki (lisa).ogg"
        Ant "Мои очки..."

        voice "voice/romka/2day/69Blyad.ogg"
        "Ромка выругался."

        voice "voice/romka/2day/70 Gondon.ogg"
        Rom "Гандон этот стащил."

        show Byasha Hee m_day_winter 01 dark_blur:
            ease 0.1 yoffset 20+75
            ease 0.1 yoffset 0+75
            repeat

        voice "voice/byasha/44 Zato mi emu.ogg"
        Bya "Зато мы ему всыпали от души, на!"

        voice "voice/byasha/45 Zavtra.ogg"
        Bya "Завтра во-от с таким фуфелом припрётся, отвечаю."

        play test_one "voice/byasha/laugh.ogg"

        "Бяша захохотал гортанно."


        show Byasha Hee m_day_winter 01 dark_blur:
            xoffset -540
            yoffset 75

        "Гиены в «Короле льве» обзавидовались бы этому смеху."

        voice "voice/romka/2day/71 Nu.ogg"
        Rom "Ну и дела."

        voice "voice/romka/2day/72 Toha t.ogg"
        Rom "Тоха, ты без очков хоть что-то видишь?"

        voice "voice/anton/2day/175. N-nemnogo.ogg"
        Ant "Н-немного..."

        scene dark_forest_day2_1 with Dissolve(0.5):
            xpos 0
            subpixel True
            linear 15 xpos -661

        play music2 "music/42_Talk.ogg" volume 0.7 fadein 6.0

        "Из мглы выдвинулась рука с красным прямоугольником — Рома предлагал мне сигарету."

        voice "voice/romka/2day/73 Ugosczais.ogg"
        Rom "Угощайся."

        "Я прищурился, силясь различить марку табака, хотя совсем не разбирался в сигаретах."
        "Я ни разу не курил, да и начинать не хотелось."
        "Интересно, будут ли они со мной общаться, если не перенимать все их привычки?"
        "Поколебавшись, я покачал головой."

        voice "voice/byasha/47 Sportsmen.ogg"
        Bya "Спортсмен, что ли? Ха!"

        voice "voice/romka/2day/74 A ty v.ogg"
        Rom "А ты в глаза долбишься?"

        voice "voice/romka/2day/75 Ne vide.ogg"
        Rom "Не видел, как он Семёну чётко вмазал?"

        voice "voice/byasha/49 Da bazaru.ogg"
        Bya "Да базара ноль. Мортал Комбат, на."

        voice "voice/byasha/50 Toha u nas.ogg"
        Bya "Тоха у нас Рокки Бальбоа."

        voice "voice/romka/2day/76 Togda u.ogg"
        Rom "Тогда уж Иван Драго."

        voice "voice/romka/2day/77 Kurim o.ogg"
        Rom "Курим одну на двоих, гони жигу."

        "Ромка губой подцепил сигарету, а Бяша суетливо шарил по карманам в поисках зажигалки."

        voice "voice/romka/2day/78 Toha cz.ogg"
        Rom "Тоха, чё я сказать хотел..."

        voice "voice/romka/2day/79 Ne derzh.ogg"
        Rom "Не держи зла, брат."

        voice "voice/romka/2day/80 My tebja.ogg"
        Rom "Мы тебя на вшивость проверяли, а то очки эти, ещё и маска..."

        play test_one "sounds/zazhigalka.ogg"
        "Бяша чиркнул здоровенной «Тбилиси», и Ромка смачно затянулся."

        stop test_one fadeout 0.5

        voice "voice/romka/2day/81 Menja k.ogg"
        Rom "Меня, кстати, Ромка зовут."

        play test_one "voice/romka/2day/82 On pozha.ogg"

        "Он пожал мне руку, сильно, до боли сдавив пальцы."
        "Его сорванные сухие мозоли на ладошке говорили, что он носит спортивный костюм не просто так."

        voice "voice/romka/2day/83 Eto vot.ogg"
        Rom "Это вот Бяша."

        voice "voice/romka/2day/84 Ty ne o.ogg"
        Rom "Ты не очкуй. Со Свиньёй мы лично пообщаемся."

        play test_one "voice/romka/2day/86 Kurit B.ogg"
        play sound "voice/anton/2day/176. On vidohnyl.ogg"

        "Он выдохнул в мою сторону клуб дыма, отчего я тут же закашлялся."

        voice "voice/anton/2day/177. Aga.ogg"
        Ant "Ага..."

        play test_one "sounds/steps_snow001.ogg"
        scene dark_forest_day2_2 with Dissolve(0.7):
            xpos -661

        voice "voice/anton/2day/178. Poidu poka.ogg"
        Ant "Пойду пока сумку соберу, а то темнеет."

        "Я нагнулся за выпотрошенным рюкзаком и его содержимым, надеясь, что новые приятели исчезнут, когда я повернусь."
        "Но они так и остались стоять, передавая друг другу сигарету."
        "Два низкорослых силуэта с блуждающим между ними огоньком на фоне сосновых столбов."
        "Они ждали, пока я соберу учебники, и перешёптывались."

        stop music2 fadeout 3.0

        "Говорил в основном Ромка — Бяша лишь шмыгал носом и одобрительно мычал."

        play music "music/44_Kontakt_2.ogg"

        "И тут, среди припорошенных снежком тетрадей, я вновь увидел ту старую, потрёпанную временем заячью морду из папье-маше."

        scene bad_mask_bg
        show bad_mask 0_blur_ne_blur
        with Dissolve(0.5)

        "Пустые дыры глаз, в которых может быть что угодно, любые глаза, но маска..."
        "...будто хотела иметь мои."
        "Откуда она взялась и что забыла в моём портфеле?"
        "Я подобрал её так осторожно, словно опасался, что она цапнет меня за палец."
        "Просто новогодняя маска с заиндевевшим плевком на внутренней стороне."
        "Только что-то в ней было не так. Что-то копошилось внутри, под коркой старых газет..."

        play music2 "music/45_Kontakt_3.ogg" fadein 2.0 noloop
        show ef_scrap

        "Я слышал шуршание тысячи маленьких тел, дрожь, исходящую от меха."
        "Что-то пыталось прогрызться наружу..."

        play music2 "music/Tension Suspense Risers_04(diminuendo).ogg" noloop
        show bad_mask 0
        show bad_mask 1 with Dissolve(0.3)
        window hide
        play test_six "sounds/loop_maggots.ogg" loop
        pause 2

        "ОПАРЫШИ!"

        stop music fadeout 2.0
        show Veko_01:
            xpos 0
            ypos -510
            alpha 1.0
            linear 0.5 xpos 0 ypos -1500 alpha 0.5
            linear 0.15 xpos 0 ypos -200 alpha 1.0
            linear 0.2 xpos 0 ypos -1500 alpha 0.0
        show Veko_02:
            xpos 0
            ypos 0
            alpha 1.0
            linear 0.5 xpos 0 ypos 1010 alpha 0.5
            linear 0.15 xpos 0 ypos -210 alpha 1.0
            linear 0.2 xpos 0 ypos 1100 alpha 0.0
        $ renpy.pause(0.6, hard=True)
        hide ef_scrap
        show bad_mask 0_blur_ne_blur
        play test_one "voice/romka/2day/90 Gotov.ogg"
        stop test_six fadeout 0.25

        Rom "Готов, Тоха?"

        show bad_mask 3
        pause 1.5
        play test_one "sounds/sfx_drop_mask.ogg"

        "Голос Ромки выдернул меня из кошмарного виденья, и я с ужасом отбросил маску прочь, за пределы видимости."
        "Отвращение клокотало внутри, но я собрался и не подал виду."

        play music2 "music/Morning Tensions.ogg" volume 0.65 fadein 2

        "Настоящие это черви или очередной сдвиг по фазе — без разницы."

        scene bg kenti:
            xpos 0
        show kenti1:
            xpos 0
        with Dissolve(0.5)

        "Слишком много всего для одного дня."
        "Хотелось как можно скорее очутиться дома."

        voice "voice/anton/2day/179. Ladno pacani.ogg"
        Ant "Л-ладно, пацаны, мне пора уже..."

        voice "voice/anton/2day/179. Do svidania.ogg"
        Ant "До свиданья."

        "Я протянул руку навстречу двум фигурам, чтобы попрощаться."
        "Тёмные продолговатые пятна подрагивали впереди."

        hide kenti1
        show kenti2:
            xpos 0
        with Dissolve(0.5)

        "Застыли, внимательно меня изучая."

        hide kenti2
        show kenti3:
            xpos 0
        $ renpy.pause(1.4)
        hide kenti3
        show kenti4:
            xpos 0

        voice "voice/romka/2day/91 S kedra.ogg"
        Rom "С кедрами закорешиться решил?"

        voice "voice/romka/2day/92 My zdes.ogg"
        Rom "Мы здесь вообще-то."

        "Голос Ромки прозвучал у меня из-за спины, и я, чувствуя себя неловко, обернулся."

        scene bg kenti:
            xpos 0
            ease 6 xpos -1300
        show kenti5:
            xpos 0
            ease 6 xpos -2300

        voice "voice/romka/2day/93 Derevja.ogg"
        Rom "Деревья — хреновые кенты."

        voice "voice/romka/2day/94 Ty ne s.ogg"
        Rom "Ты не ссы, мы тебя до дома доведём, а то ты как слепой котёнок."

        voice "voice/romka/2day/95 Tak zde.ogg"
        Rom "Ха-ха. Так здесь живьём и сгниёшь."

        play test_one "sounds/sfx_cigarette_butt.ogg"

        "Окурок разбился о пень снопом искр и зашипел в сугробе у моих ног."

        play sound "voice/romka/2day/He-he.ogg"

        "Ребята как-то натянуто засмеялись и взяли меня под локти."

        $ renpy.start_predict("gohome01_dark_lowblur")
        $ renpy.start_predict("gohome01_1_dark_lowblur")
        $ renpy.start_predict("gohome02_dark_lowblur")
        $ renpy.start_predict("gohome02_1_dark_lowblur")
        $ renpy.start_predict("gohome03_dark_lowblur")
        $ renpy.start_predict("gohome03_1_dark_lowblur")
        $ renpy.start_predict("gohome04_dark_lowblur")
        $ renpy.start_predict("gohome04_1_dark_lowblur")
        $ renpy.start_predict("romka_walkaway")
        $ renpy.start_predict("anton_walkaway")
        $ renpy.start_predict("hands_walkaway")
        $ renpy.start_predict("byasha_walkaway")
        $ renpy.start_predict("byasha_walkaway")
        scene Draka_fon4 with Dissolve(0.5)

        "Покидая пустырь, я обернулся в надежде увидеть Алису."
        "Хотя бы рыжее пятно. А вдруг..."

        show traktor with Dissolve(0.5)
        play test_one "sounds/sfx_tractor_pass.ogg"

        "Но увидел лишь грохочущий трактор, который выползал откуда-то из-за поворота."

        window hide
        play test_two "sounds/steps/loop_footsteps_three.ogg" loop

        $ SetParSpeed(30)
        $ SceneFlags.Reset()
        window hide
        scene bg_black

        show gohome01_dark_lowblur
        show gohome01_1_dark_lowblur
        show gohome02_dark_lowblur
        show gohome02_1_dark_lowblur
        show gohome03_dark_lowblur
        show gohome03_1_dark_lowblur

        show screen witness_walkaway(spr="locate/street/walkaway/witness_01.png", blur = lowblur_val, timeout = 0.64)

        show gohome04_dark_lowblur
        show gohome04_1_dark_lowblur

        show romka_walkaway at walkaway(-400, appear = 30.0)
        show anton_walkaway at walkaway(-400, 5, appear = 30.0)
        show hands_walkaway at walkaway(-400, 5, appear = 30.0)
        show byasha_walkaway at walkaway(500, appear = 30.0)

        $ is_tapped = ui.interact()


        if is_tapped == "tap":


            $ story_manager.MarkEvent(("day2", "man_fox", "witness"))
            $ Flags.Raise("witness tapped")
            scene bg_black with Dissolve(.5)
            show gohome01_dark_blur_stop:
                xalign .25
            show gohome02_dark_blur_stop:
                xalign .25
            show gohome03_dark_blur_stop:
                xalign .25
            show gohome04_dark_blur_stop:
                xalign .25

            show man in_black3:
                zoom 0.80
                ypos 200
                xalign .5

            with Dissolve(.5)

            hide screen witness_walkaway
            stop test_two fadeout 1

            "Впереди, на обочине, из тумана возник силуэт."
            "Мы отошли, чтобы пропустить его."

            show man in_black1_heavyblur:
                align (.5,1.)
                zoom .9
                alpha 0.
                linear 1. zoom 1. alpha 1.

            play sound "sounds/steps/Man in.ogg"

            "Из-за упавшего зрения и сумерек казалось, что навстречу нам, не касаясь земли подошвами, скользит призрак."

            show man in_black1 with Dissolve(1.)

            "Но он приблизился, и я рассмотрел взрослого мужчину."


            if Flags.Has("witness school"):
                "Узнал его по кряжистой фигуре. Тот тип, что курил у школы утром."

            "Мужчина одарил нас деловитым взглядом ледяных глаз и пошёл дальше, быстро сгинув в полутьме."
            play sound "sounds/steps/Man out.ogg"
            show man in_black2
            hide man with Dissolve(.5)

            voice "voice/byasha/62 Net gorba.ogg"
            Bya "Нет горба, зато заячья губа."

            "Я испугался, что незнакомец услышит дразнилку, но он был уже далеко."
            "Мы продолжили путь."

            scene bg_black with Dissolve(.5)
            $ SetParSpeed(30)
            scene bg_black
            show gohome01_dark_lowblur
            show gohome01_1_dark_lowblur
            show gohome02_dark_lowblur
            show gohome02_1_dark_lowblur
            show gohome03_dark_lowblur
            show gohome03_1_dark_lowblur
            show gohome04_dark_lowblur
            show gohome04_1_dark_lowblur
            show romka_walkaway at walkaway(-400)
            show anton_walkaway at walkaway(-400, 5)
            show hands_walkaway at walkaway(-400, 5)
            show byasha_walkaway at walkaway(500)
            with Dissolve(.5)

        window hide
        play test_two "sounds/steps/loop_footsteps_three.ogg" loop

        "Молчаливой процессией брели мы вдоль замершей просеки."
        "Тишина и частичная слепота вместе действовали угнетающе, и я заговорил:"

        voice "voice/anton/2day/180. A pochemu tebya Byasha.ogg"
        Ant "А почему тебя Бяша зовут?"

        play test_one "voice/byasha/63 Buryat.ogg"
        "Бурятик криво ухмыльнулся."

        voice "voice/byasha/63 Potomu chto.ogg"
        Bya "Потому что я волк в овечьей шкуре, на."

        $ romka_walkaway_state = 1

        voice "voice/romka/2day/96 Breshesh.ogg"
        Rom "Брешешь!"

        voice "voice/romka/2day/97 Purgu g.ogg"
        Rom "Пургу гнать — это он умеет."

        voice "voice/romka/2day/98 A zvat.ogg"
        Rom "А звать его так потому, что блеет, как овца."

        voice "voice/romka/2day/99  vse po.ogg"
        Rom "Всё после того, как из Чёрного гаража живым выбрался."

        $ byasha_walkaway_state = 1

        play sound "voice/byasha/64 Otshat.ogg"

        "Бяша моментально изменился в лице – я заметил это даже сквозь пелену."
        "Отшатнулся."

        play sound "voice/byasha/65 Zamich.ogg"

        "Замычал что-то нечленораздельно."

        voice "voice/romka/2day/100 Vidish.ogg"
        Rom "Видишь?"

        voice "voice/romka/2day/101 S nim.ogg"
        Rom "С ним так всегда, как об этой херне заговоришь."

        voice "voice/anton/2day/180. Ti seichas o chem.ogg"
        Ant "Ты сейчас о чём?"

        stop music2 fadeout 1.5

        voice "voice/romka/2day/102 Ty ser.ogg"
        Rom "Ты серьёзно про эту страшилку не знаешь?"

        stop test_two fadeout 10

        hide bg_black
        show bg_black:
            alpha 0.0
            linear 2. alpha 1.0

        play music "music/Into The Woods (Intro).ogg" volume 0.8 fadein 2

        voice "voice/romka/2day/103 Na czer.ogg"
        Rom "На чёрной-чёрной улице..."

        show koshmar:
            alpha 0.0
            linear 2. alpha 1.0

        voice "voice/romka/2day/104 V czern.ogg"
        Rom "...в чёрной-чёрной подворотне..."

        voice "voice/romka/2day/105 Stoit.ogg"
        Rom "...стоит чёрный-пречёрный гараж."

        hide bg_black
        show bg_black:
            alpha 0.0
            choice:
                pause .15
            choice:
                pause .5
            choice:
                pause 1.
            linear .05 alpha 1.0
            pause .05
            linear .05 alpha 0.0
            repeat

        voice "voice/romka/2day/106 I on z.ogg"
        Rom "И он знает о тебе всё..."

        voice "voice/romka/2day/107 Gde ty.ogg"
        Rom "Где ты живёшь. Что любишь. С кем дружишь."

        hide bg_black
        show bg_black:
            alpha 0.0
            linear 2. alpha 1.0

        voice "voice/romka/2day/108 Navern.ogg"
        Rom "Наверняка слышал о пропавших детях."

        $ show_snow_1 = False
        $ show_snow_2 = False
        $ show_snow_3 = False

        $ SetParSpeed(30)
        scene bg_black
        show gohome01_dark_blur
        show gohome01_1_dark_blur
        show gohome02_dark_blur
        show gohome02_1_dark_blur
        show gohome03_dark_blur
        show gohome03_1_dark_blur
        show gohome04_dark_blur
        show gohome04_1_dark_blur

        show snow_walkaway_lay3

        show romka_walkaway at walkaway(-400)
        show anton_walkaway at walkaway(-400, 5)
        show hands_walkaway at walkaway(-400, 5)
        show byasha_walkaway at walkaway(500)

        show snow_walkaway_lay2

        show gohome05_dark_blur
        show gohome05_1_dark_blur

        show snow_walkaway_lay1

        with Dissolve(2.)

        $ renpy.stop_predict("gohome01_dark_lowblur")
        $ renpy.stop_predict("gohome01_1_dark_lowblur")
        $ renpy.stop_predict("gohome02_dark_lowblur")
        $ renpy.stop_predict("gohome02_1_dark_lowblur")
        $ renpy.stop_predict("gohome03_dark_lowblur")
        $ renpy.stop_predict("gohome03_1_dark_lowblur")
        $ renpy.stop_predict("gohome04_dark_lowblur")
        $ renpy.stop_predict("gohome04_1_dark_lowblur")
        $ renpy.stop_predict("romka_walkaway")
        $ renpy.stop_predict("anton_walkaway")
        $ renpy.stop_predict("hands_walkaway")
        $ renpy.stop_predict("byasha_walkaway")
        $ renpy.stop_predict("byasha_walkaway")

        voice "voice/romka/2day/109 Eto tu.ogg"
        Rom "Это тут не первый год происходит..."

        voice "voice/romka/2day/110 Vse me.ogg"
        Rom "Все местные знают, кто здесь замешан."

        voice "voice/romka/2day/111 Dazhe v.ogg"
        Rom "Даже взрослые."

        voice "voice/romka/2day/112 Voobscze.ogg"
        Rom "Вообще везёт тебе — ты вон в лесу, считай, живёшь..."

        voice "voice/romka/2day/113 On k t.ogg"
        Rom "Он к тебе так просто не сунется."

        voice "voice/romka/2day/114 Tupo s.ogg"
        Rom "Тупо сечёт, что среди деревьев будет выделяться."

        voice "voice/romka/2day/115 A u na.ogg"
        Rom "А у нас эта хрень может где угодно поджидать: иногда в конце переулка или возле дома."

        voice "voice/romka/2day/116 A escze.ogg"
        Rom "А ещё..."

        voice "voice/romka/2day/117 Idesh.ogg"
        Rom "Идёшь такой себе ночью, и тут — раз..."

        voice "voice/romka/2day/119 On sto.ogg"
        Rom "Он стоит, где совсем недавно пусто было."

        voice "voice/romka/2day/120 Dver.ogg"
        Rom "Дверь открыта, внутри – мрак..."

        voice "voice/romka/2day/121 I tut.ogg"
        Rom "И тут как..."

        $ byasha_walkaway_state = 2
        play sound "voice/byasha/69 Byasha nat.ogg"

        "Бяша натянул капюшон на голову и завыл на высокой трепещущей ноте, стараясь заглушить Ромкину речь."


        $ romka_walkaway_state = 0
        stop music fadeout 1.5

        voice "voice/romka/2day/122 Ladno.ogg"
        Rom "Ладно-ладно, проехали..."

        $ byasha_walkaway_state = 1

        play music2 "music/2_Anxiety.ogg" volume 0.85

        "Я переваривал рассказ Ромки, не понимая, как относиться к услышанному."
        "За недолгое время, проведённое в этом заснеженном глухом посёлке, я уяснил одно – многие здесь столкнулись с тем, чего так и не смогли понять."

        play test_one "voice/byasha/69 Ya vzglyanul.ogg"

        "Я взглянул на мелко трясущегося Бяшу."

        $ romka_walkaway_state = 1

        voice "voice/romka/2day/123 Toha.ogg"
        Rom "Тоха, а вот скажи, нахрена вы-то сюда переехали?"

        play test_one "voice/anton/2day/181. Ya tazelo vdohnul.ogg"

        "Я тяжело вздохнул, глядя под ноги."
        "Далеко внизу ботинки бодали носками туман."
        "Это были вызубренные наизусть слова:"

        voice "voice/anton/2day/182 U otca tut.ogg"
        Ant "У отца тут новая работа."

        voice "voice/anton/2day/182.2 I mama v poselke.ogg"
        Ant "И мама в посёлке раньше жила."

        voice "voice/anton/2day/182.3 Davno eshe.ogg"
        Ant "Давно ещё, при Союзе."

        voice "voice/romka/2day/124 Zdes.ogg"
        Rom "Здесь же нечего делать, только гнить."

        voice "voice/romka/2day/125 Nu ili.ogg"
        Rom "Ну или как Бяша — по лесам шастать."

        play test_one "voice/byasha/70 Byasha ost.ogg"
        $ byasha_walkaway_state = 0

        "Бяша осторожно высунулся из-под капюшона, словно улитка из домика, и прислушался."

        voice "voice/romka/2day/126 On u n.ogg"
        Rom "Он у нас турист."

        voice "voice/romka/2day/127 Letom.ogg"
        Rom "Летом целую неделю в палатке жил."

        voice "voice/romka/2day/128 Zdes.ogg"
        Rom "Здесь, рядом."

        voice "voice/romka/2day/129 Prikin.ogg"
        Rom "Прикинь?"

        Rom "..."

        $ romka_walkaway_state = 0




        $ show_snow_1 = False
        $ show_snow_2 = True
        $ show_snow_3 = True

        voice "voice/romka/2day/130 Hotja o.ogg"
        Rom "Хотя от мамки его звезданутой я бы сам в лес сбежал."

        $ show_snow_1 = True
        $ show_snow_2 = True
        $ show_snow_3 = True

        "Мы шли дальше, но казалось, что это лес плывёт мимо."
        "Сосны — чёрные клавиши, снежные прорехи – белые."
        "И чаща играет свою древнюю скрипучую мелодию — музыку корней, берлог и забытых таёжных скитов."
        "Снежинки создавали будоражащую иллюзию."
        "Казалось, кто-то бродит по лесу..."
        "Кто-то высокий, неуловимый, готовый в любой момент прикинуться деревом или слиться с сугробами..."
        "А потом, когда внимание к нему ослабнет, вновь продолжит свой путь вдоль дороги."
        "Но это была лишь игра света и тени — там никого не было."

        "По крайне мере, мне хотелось так думать."

        $ scare_anim = False
        scene scare_reverted
        show layer master:
            align (.5, .5)
            zoom 1.05
        show screen day2_scare_trees
        play sound "sounds/steps/Stop.ogg"

        "Ромка вдруг резко притормозил и сказал:" with hpunch

        voice "voice/romka/2day/131 Slyshte.ogg"
        Rom "Слышите?"

        voice "voice/romka/2day/132 V lesu.ogg"
        Rom "В лесу кто-то бродит, по ходу..."

        "Кожа под одеждой засвербела, заныло в желудке."
        "Мы посмотрели, куда показывал Ромка."

        voice "voice/romka/2day/133 Vysocze.ogg"
        Rom "Высоченный, причём с нашей скоростью идёт..."

        "Никаких гигантских фигур за мачтами сосен."

        scene scare_reverted:
            xalign .5
            yalign 1.
            linear 5.0 zoom 1.15

        show scare_reverted as scare2:
            xalign .5
            yalign 1.
            parallel:
                linear 4.0 zoom 1.3
            parallel:
                linear 4.0 alpha 0.0

        $ scare_anim = True

        "Только тени, крадущиеся в полумраке."
        "Медленные тени."
        "Быстрые тени."
        "Голодные."
        "Снег бесшумно осыпался с ветки, заставив вздрогнуть, прикусить губу."
        "Будто что-то огромное поднялось с дерева и улетело."
        "Возможно, в нашу сторону..."

        play sound "voice/romka/2day/134 Krjahti.ogg"

        "Ромка поднял с земли шишку и швырнул в чащу."

        voice "voice/romka/2day/135 Ei A.ogg"
        Rom "Эй!"

        "Оклик срикошетил, словно ударил о тугой барабан. Эхо передразнило Ромку. А затем вновь воцарилась тишина."

        voice "voice/romka/2day/136 Ktoni.ogg"
        Rom "Кто-нибудь видел?"

        "Я помотал головой."
        "Что я видел, так это вертикальные мазки деревьев, темноту, снег и своих спутников в дымке."
        "Вспоминались шершавые стволы, губчатый лишайник и ледяное крошево на дне рвов."

        stop music2 fadeout 1

        voice "voice/anton/2day/183. Poiemte skoree.ogg"
        Ant "Пойдёмте скорее, а то вечереет."

        hide screen day2_scare_trees

        scene scare_reverted:
            xalign .5
            yalign 1.
            zoom 1.15
            linear 5.0 zoom 1.0

        show snow_boiz_2

        show rom_walk2_1 at walkaway2(0, 4.0)
        show ant_walk2_1 at walkaway2(5, 4.0)
        show byash_walk2_1 at walkaway2(0, 4.0)
        play music2 "music/21_He is near.ogg"


        show snow_boiz_1
        with Dissolve(1.)

        play test_seven "sounds/steps/loop_footsteps_three.ogg" loop

        "Меня вновь взяли под локти и повели вперёд, понесли к лесу, к торчащим шпилям сучьев."



        show bg_black:
            alpha 0.0
            linear 1.0 alpha 1.

        "Солнце окончательно кануло за зелёные пики."
        "Мрак зашевелился, расправил плечи, пополз, как дым."

        scene scare_reverted
        show scare_reverted_blur:
            alpha 0.0
            linear 6. alpha 1.

        show snow_boiz_2

        show rom_walk2_1 at walkaway2(0)
        show ant_walk2_1 at walkaway2(5)
        show byash_walk2_1 at walkaway2(0)

        show rom_walk2_2 at walkaway2(0):
            alpha 0.0
            linear 3.0 alpha 1.0
        show ant_walk2_2 at walkaway2(5):
            alpha 0.0
            linear 3.0 alpha 1.0
        show byash_walk2_2 at walkaway2(0):
            alpha 0.0
            linear 3.0 alpha 1.0

        show snow_boiz_1

        show bg_black:
            alpha 1.0
            linear 1.0 alpha 0.

        show dark_walk

        "Вдобавок повалил снег — густые липкие хлопья, белые мухи, летящие на запах падали."
        "Моё зрение стало крохотным островком, омываемым тёмными водами."
        "Утренняя тревога вновь начинала овладевать мной."

        show dark_walk as dark2:
            alpha 0.0
            linear 2.0 alpha 1.
        stop music2 fadeout 3
        play music "music/Flute 2(reverb).ogg"

        "Мерещилось, что далеко-далеко, на самой кромке сознания, я слышу вкрадчивое пение флейты."
        "Хрупкое, словно мартовский ледок, под которым дремлет бездонное озеро."

        stop music fadeout 2

        "Я ковырнул пальцем в ухе, прогоняя слуховую галлюцинацию."
        "Лес был тих."
        "Я представил ребёнка, идущего в ночи под надзором дуплистых сосен."

        voice "voice/anton/2day/184 A vi znali Vovu.ogg"
        Ant "А вы знали Вову Матюхина?"

        voice "voice/anton/2day/184.2 Malchika.ogg"
        Ant "Мальчика, который пропал недавно?"

        $ story_manager.MarkEvent(("day2", "s_fox1"))

        hide romka_walkaway
        show fox_walkaway at walkaway2(0)
        hide dark_walk
        hide dark2
        show dark_walk
        show dark_walk as dark2
        hide snow_boiz_1
        with Dissolve(1.0)

        voice "voice/Alisa/Alisa2day/170 A razve mi.ogg"
        Alis "А разве мы не его ищем, сладкий?"

        scene bg_black
        show fox_walkaway
        show ant_walk2_1
        with Dissolve(.25)
        stop music2 fadeout 2

        play test_one "voice/anton/2day/Yavzdrognuliostanovils.ogg"

        stop test_seven fadeout 1
        play sound "sounds/roll-hit-2.ogg"

        "Я вздрогнул и остановился, уставившись на провожатого."

        hide ant_walk2_1
        show ant_walk2_3
        with Dissolve(.5)

        "На Алису в её неизменной маске лисы."
        "Девочка нежно придерживала меня за локоть."

        voice "voice/anton/2day/185 Chto ti zdes.ogg"
        Ant "Что ты здесь?.."

        play music "music/Mystic Waltz.ogg" volume 0.7

        voice "voice/anton/2day/185.2 A ved ya tebya.ogg"
        Ant "А ведь я тебя потерял!"

        voice "voice/Alisa/Alisa2day/171 Poteryal.ogg"
        Alis "Потерял потому, что зазевался."

        show ant_walk2_4

        "Я щурился недоверчиво."

        voice "voice/anton/2day/186. I davno ti.ogg"
        Ant "И давно ты за нами идёшь?"

        voice "voice/Alisa/Alisa2day/172 Chto znachit.ogg"
        Alis "Что значит «давно»? Я всегда была рядом."

        voice "voice/Alisa/Alisa2day/173 Da i za kem.ogg"
        Alis "Да и за кем «за вами»?"

        "Одураченный, я повертелся, но не нашёл ни Рому, ни Бяшу."

        show ant_walk2_5

        "И вдруг почувствовал её прохладные пальцы на своём запястье."

        voice "voice/Alisa/Alisa2day/175 Poidem ze.ogg"
        Alis "Пойдём же!"

        hide ant_walk2_5
        show ant_walk2_3

        voice "voice/Alisa/Alisa2day/176 Mi sobiralis.ogg"
        Alis "Мы собирались искать Вову."

        play test_seven "sounds/steps/snow_step01.ogg"
        $ SetParSpeed(10)
        scene bg_black
        show gohome01_dark_blur
        show gohome01_1_dark_blur
        show gohome02_dark_blur
        show gohome02_1_dark_blur
        show gohome03_dark_blur
        show gohome03_1_dark_blur
        show gohome04_dark_blur
        show gohome04_1_dark_blur



        show foxanton_walkaway at walkaway(-400, loop_mod = .3)



        show gohome05_dark_blur
        show gohome05_1_dark_blur



        with Dissolve(2.)

        "Не дав опомниться, она повела меня через лес."
        "Запах мандаринов, кофе и петард обволакивал."
        "Я ощущал себя маленьким мальчиком, которого ведут в неизвестность."
        "Впереди темнели стволы деревьев. Грозно щетинились ледяные кусты-дикобразы."
        "На пути возникло что-то прямоугольное, вроде большой коробки..."






        "Я окаменел."
        "Коснулся краешка глаза, оттягивая веко, как бы настраивая зрение."

        stop music fadeout 2
        show garage_blinking_blure:
            alpha 0.0
            pause .25
            alpha 1.0

        show perehod:
            xalign 1.5
            linear .25 xalign .5
            linear .25 xalign -1.
            alpha 0.

        play music2 "music/Into The Woods (Intro).ogg" fadein 2

        "Металлический гараж вырастал прямо из валежника."
        "Тяжёлый, громоздкий — такой невозможно без труда перевезти с места на место."
        "Стены окрашены чёрным – чернее окружающей тьмы."

        show Fox Normal m_night 00 blur:
            xpos -350
        with Dissolve(0.5)

        play sound "voice/Alisa/Alisa2day/Lisa_nuh.ogg"
        "Лиса принюхалась, и, показалось, её маска сморщилась от омерзения."

        show Fox Fullface m_night 00 blur with Dissolve(.3)

        voice "voice/Alisa/Alisa2day/178 Eto zdes.ogg"
        Alis "Это здесь."

        "Встревоженный голос спутницы напугал меня даже больше, чем эта жутковатая железная коробка."

        voice "voice/anton/2day/187. Zdes.ogg"
        Ant "Здесь?"

        voice "voice/Alisa/Alisa2day/179 Ya slishu.ogg"
        Alis "Я слышу его запах..."

        show Fox Normal m_night 00 blur with Dissolve(.3)

        voice "voice/Alisa/Alisa2day/180 Mozet Vova.ogg"
        Alis "Может, Вова играет с нами в прятки, и он решил спрятаться..."

        voice "voice/Alisa/Alisa2day/181 Vnutri.ogg"
        Alis "...внутри?"

        hide Fox with Dissolve(.5)

        "Мне казалось, что от постройки отделяются дымчатые щупальца и что-то рыщут в прелой листве."
        "Они стелились по снежному одеялу, подбираясь к нашим ногам."
        "И какой-то жуткий металлический скрежет доносился из-за огромных чёрных ворот."
        "Кто-то или что-то явно ждало нас внутри."




        label bunny2_fox_garage_dev:
            $ Flags.Raise("fight")
            $ Flags.Raise("day2 fox")











        call screen day2_garage_open()

        "Наверное, со стороны моё дёрганье напоминало пластику марионетки, танцующей на нитях кукловода."

        play test_one "sounds/steps_snow001.ogg"

        show garage_blinking_blure:
            xalign 0.5 yalign 1.
            ease 0.6 zoom 1.05
            pause 0.2
            ease 0.6 zoom 1.1

        pause 1.6

        scene garage_near_blinking
        show garage_smoke_1 onlayer master1:
            xanchor 0.0
        show garage_smoke_2 onlayer master1:
            xanchor 0.0
        with Dissolve(.5)








        play test_three "sounds/Trees_SFXs_2.ogg" loop

        "Я приблизился к гаражу, затаив дыхание..."

        play test_seven "sounds/Tension Suspense Risers_05.ogg"



        hide garage_smoke_1 onlayer master1
        hide garage_smoke_2 onlayer master1
        scene kk_bg

        show kk_shadow:
            subpixel True
            pos (0., 1.)
            parallel:
                easein 10 pos (0., 0.)

            parallel:
                linear 2 offset (0,-3)
                linear 2 offset (3,-3)
                linear 2 offset (-3,0)
                linear 2 offset (-3,-3)
                linear 2 offset (0,0)
                repeat

        show kk_hand_1:
            subpixel True
            pos (-1., 1.)
            parallel:
                easein 10 pos (0., 0.)

            parallel:
                linear 2 offset (0,-3)
                linear 2 offset (3,-3)
                linear 2 offset (-3,0)
                linear 2 offset (-3,-3)
                linear 2 offset (0,0)
                repeat

        show garage_blink_black

        with Dissolve(.5)

        $ renpy.pause(delay=9.5, hard=True)
        stop test_four




        "...и постучал костяшками по листовому железу."



        hide kk_shadow
        show kk_shadow

        hide kk_hand_1
        show kk_hand_1:
            alpha 0
            time .15
            alpha 1
            time .5
            alpha 0
            time .65
            alpha 1

        show kk_hand_2:
            alpha 1
            time .15
            alpha 0
            time .5
            alpha 1
            time .65
            alpha 0

        hide garage_blink_black
        show garage_blink_black



        play test_one "sounds/sfx_garage_door_knock.ogg"

        "Тук-тук!"


        scene garage_near_blinking:
            align (.5,.5)
            zoom 1.35
            easein .35 zoom 1.0
        show garage_smoke_1 onlayer master1:
            xanchor 0.0
        show garage_smoke_2 onlayer master1:
            xanchor 0.0


        stop test_five
        play test_six "sounds/Lamp_03.ogg" loop
        play sound "sounds/steps/snow_stepS02.ogg"

        "Тут же опасливо отскочил."
        if Flags.Has("record"):
            play sound "sounds/screamer-1.ogg"
            show bg_white with Dissolve(.25)
            show bg_black with Dissolve(.25)
            show bg_rep_senya_crack:
                dsen*19
                alpha 0
            pause dsen*15
            hide bg_white
            hide bg_black
            show bg_white with Dissolve(.25)
            show bg_black with Dissolve(.25)
            hide bg_white
            hide bg_black

            "На мгновение показалось, как за стенками гаража что-то мучительно завыло."

        play test_one "sounds/steps/step_snow1.ogg"
        scene garage_near_blinking_0
        with dissolve

        "Послышалось, как зазвенели проржавевшие мясные крюки на толстых металлических цепях, и что-то громоздкое, отринув сон, поползло отворить чёрные ворота."

        play sound "sounds/screamer-2.ogg"

        show bg_white with Dissolve(.25)
        show bg_black with Dissolve(.25)
        show bg_gar_vova_crack:
            dvova*19
            alpha 0

        pause dvova*15

        hide bg_white
        hide bg_black
        show bg_white with Dissolve(.25)
        show bg_black with Dissolve(.25)
        hide bg_white
        hide bg_black

        scene garage_near_blinking_1
        with dissolve

        "Ничего не происходило."


        scene kk_wtf_0
        show kk_wtf_2
        show kk_wtf_3
        show kk_wtf_blink
        show garage_blink_black
        with dissolve
        stop test_six
        play test_two "sounds/sfx-heartbeat.ogg" fadein 0.5 loop
        play sound "sounds/Lamp_03.ogg" loop
        show kk_wtf_1 behind kk_wtf_2:
            xoffset -300
            linear 1 xoffset 0
        play test_one "sounds/Bush_rustle2.ogg"

        "Сердце бухало в груди."
        "Ничего."

        play test_one "sounds/Bush_rustle.ogg"
        stop music2 fadeout 0.25

        stop test_three fadeout 0.5
        hide kk_wtf_1
        show kk_wtf_1 behind kk_wtf_2:
            xoffset 0
            linear 1 xoffset -300
        "Тук-тук-тук."
        stop test_two fadeout 0.5
        stop sound


        hide garage_smoke_1 onlayer master1
        hide garage_smoke_2 onlayer master1

        scene garage_near_blinking_static

        "Опасаясь повернуться к гаражу спиной, я очень медленно сделал шаг назад, не в силах оторвать взгляд от сочащей смрадом расщелины, и хотел было позвать Алису...{w=2.5}{nw}"

        window hide

        scene garage_near_blinking_anim


        play music "music/Into The Woods (Opens).ogg"
        play test_one "sounds/sfx_open_garage_door.ogg"
        play wtf "sounds/screamer-3.ogg"

        $ renpy.pause(delay=1.5, hard=True)



        show garage_smoke_1 onlayer master1:
            xanchor 0.0
        show garage_smoke_2 onlayer master1:
            xanchor 0.0
        show garage_near_opened_blur

        show garage_blink_black2


        "«{i}Беги!{/i}» – трусливо проблеял голос в голове."



        scene garage_blinking_blure:
            xalign .5
            yalign 1.
            zoom 1.15

            parallel:
                linear 2. zoom 1.

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

        hide garage_smoke_1 onlayer master1
        hide garage_smoke_2 onlayer master1
        with Dissolve(.15)

        play test_one "sounds/steps/loop_snow_footsteps.ogg" loop
        play test_seven "voice/anton/2day/Begi.ogg" loop

        "Спотыкаясь, я рванул в кишащую тенями ночь."
        "За изломанный ствол лиственницы, уверенный, что Алиса бежит рядом."

        scene fkoz_bg
        show fkoz_beast:
            align (.5,.5)
            zoom .95
        show fkoz_2_2
        show fkoz_2_1
        show fkoz_1_2
        show fkoz_1_1

        stop test_one fadeout 1
        stop test_seven fadeout 0.5
        play test_six "voice/anton/2day/Begi2.ogg"

        "Минуту спустя я обнаружил, что девочка пропала."

        scene fkoz_bg
        show fkoz_beast:
            subpixel True
            align (.5,.5)
            zoom .95
            linear 5 zoom 1.05
        show fkoz_2_2:
            align (.5,1.)
            linear 5 xoffset 300 zoom 1.05
        show fkoz_2_1:
            align (.5,1.)
            linear 5 xoffset -240 zoom 1.05
        show fkoz_1_2:
            align (.5,1.)
            linear 5 xoffset 250 zoom 1.15
        show fkoz_1_1:
            align (.5,1.)
            linear 5 xoffset -250 zoom 1.15

        "Лес бормотал свои древние молитвы."
        "Скрипел, тикал, шуршал."

        stop test_six fadeout 0.5

        "Я замер."

        stop music fadeout 1

        "Не знаю, сколько прошло времени, прежде чем я понял, что стою почти в полной темноте, в кольце взмывающих ввысь стволов."

    if Flags.Has("day2 polina"):
        voice "voice/anton/2day/165. Moi ochki (Polina).ogg"
        Ant "Мои очки..."

        voice "voice/semen/2day/99 CZto.ogg"
        Sem "Что, ничего не видишь без очков, мудила?"

        "Он воздел к небу руку с моими очками, так что я не мог до них дотянуться."

        window hide
        scene bg gop_wood_4:
            xpos -720
            ease 2.0 xpos -300
        show romka 01 03 05:
            xpos -720
            ease 2.0 xpos -300
        show baysha 01 02 01:
            xpos -720
            ease 2.0 xpos -300
        show sema 02:
            xpos -720
            ease 2.0 xpos -300
        with Dissolve(0.3)
        $ renpy.pause(1.7)
        window show

        voice "voice/anton/2day/166. Otdai seychas.ogg"

        Ant "Отдай! Сейчас же вер..."

        window hide
        play test_one "sounds/sfx_heavy_face_punch.ogg"
        scene bg_gop_wood_sema_punch1_2:
            xpos -300
        show layer master:
            align (.5, .5)
            zoom 1.05
        with hpunch
        $ renpy.pause(0.3)
        scene bg_gop_wood_sema_punch2:
            xpos -300
        show layer master:
            align (.5, .5)
            zoom 1.05
        show bg_gop_wood_ring_blick:
            xpos -300
        with Dissolve(0.2)
        window show

        "Меня прервал свинцовый кулак с заостренной печаткой, который с хрустом врезался мне в бровь, опрокинув на промёрзшую землю."

        scene bg_anton_relax_rage with Dissolve(0.2)

        "Хоровод смазанных лиц, давящихся отвратительным смехом, резвился надо мной, доводил до тошноты."

        play sound "sounds/steps/Rom&Byash_step.ogg"

        "И только я успел опомниться, как расплывающаяся фигура стала стремительно приближаться..."
        "...но вместо очередного удара протянула мне руку."
        "В надежде, что это Полина я ухватился за неё, как за соломинку, и тут же понял, как я ошибся, почувствовав укол сорванных сухих мозолей на ладошке."

        scene rom_knife_00_1_blur with Dissolve(0.3)
        play test_one "voice/anton/2day/142. Semen.ogg"

        "Это был Ромка. Он помог мне встать на ноги."

        voice "voice/romka/2day/137 Pravda.ogg"
        Rom "Правда ничего не видишь?"

        "Голос звучал сочувственно, что смутило меня."
        "Я прищурился, ища в тумане Полину. Она собирала мои вещи в рюкзак, распихивала тетрадки."

        voice "voice/romka/2day/138 A slysh.ogg"
        Rom "А слышишь хорошо?"

        voice "voice/anton/2day/167. A.ogg"
        Ant "А?"

        "Он склонился ко мне вплотную и спросил уже без напускного дружелюбия."

        voice "voice/romka/2day/139 Slyshish.ogg"
        Rom "Слышишь ты хорошо, Антошка?"

        voice "voice/anton/2day/168. Da.ogg"
        Ant "Да..."

        "Я озадаченно моргнул."

        voice "voice/romka/2day/140 Nu tak.ogg"
        Rom "Ну так слушай внимательно."

        "Он отряхнул мою куртку."
        "А потом ударил в скулу со всего размаха."

        window hide
        play test_one "voice/romka/2day/141 CZelust.ogg"
        play sound "sounds/sfx_punch.ogg"

        scene roma_figth_anim
        $ renpy.pause(0.3)
        scene roma_figth_4
        show layer master:
            align (.5, .5)
            zoom 1.05
        with hpunch
        show black:
            alpha 0.0
            linear 4.0 alpha 1.0
        play test_two "voice/anton/2day/169. Udar.ogg"
        play test_one "sounds/loop_fast_heartbeat.ogg" fadein 2.0 loop

        "Челюсть моя щёлкнула – попадись между зубов язык, и я бы не только видел плохо, но и изъяснялся бы хуже Бяши."
        "Меня занесло, мир в очередной раз крутанулся юлой. Но Ромка поддержал за локоть, не давая упасть."
        "Где-то далеко вскрикнула Полина."

        voice "voice/Polina/2day/139 Anton (gde-to).ogg"
        Pol "Антон!"

        "Бяша сгрёб её в охапку, не давая подбежать ко мне."

        stop test_one fadeout 10
        scene rom_knife_00_1_blur
        show layer master:
            align (.5, .5)
            zoom 1.05
        show Veko_01:
            xpos 0
            ypos -510
            alpha 1.0
            linear 0.5 xpos 0 ypos -1500 alpha 0.5
            linear 0.15 xpos 0 ypos -200 alpha 1.0
            linear 0.2 xpos 0 ypos -1500 alpha 0.0
        show Veko_02:
            xpos 0
            ypos 0
            alpha 1.0
            linear 0.5 xpos 0 ypos 1010 alpha 0.5
            linear 0.15 xpos 0 ypos -210 alpha 1.0
            linear 0.2 xpos 0 ypos 1100 alpha 0.0

        with Dissolve(0.3)

        voice "voice/romka/2day/142 Eto te.ogg"
        Rom "Это тебе аванс."

        voice "voice/romka/2day/143 Escze ra.ogg"
        Rom "Ещё раз увижу тебя с Полинкой, хотя бы в метре от неё — пеняй на себя."

        voice "voice/romka/2day/144 Ty pon.ogg"
        Rom "Ты понял, а?"

        voice "voice/anton/2day/170. D-da.ogg"
        Ant "Д-да..."

        stop fon fadeout 2

        voice "voice/romka/2day/145 CZisto.ogg"
        Rom "Чисто чтобы закрепить."

        window hide
        play sound "sounds/sfx_punch.ogg"
        play test_two "voice/anton/2day/199. Kulak vrez.ogg"
        scene roma_figth_anim
        show layer master:
            align (.5, .5)
            zoom 1.05
        $ renpy.pause(0.2)
        play test_one "sounds/fast_heartbeat_peep.ogg"
        scene roma_figth_4
        show layer master:
            align (.5, .5)
            zoom 1.05
        show bg_white:
            alpha 0.0
            linear 0.3 alpha 1.0
        with hpunch

        "Кулак прилетел в мой висок."
        "Мир опрокинулся."

        window hide
        scene roma_figth_bg_chao
        show layer master:
            align (.5, .5)
            zoom 1.05
        with Dissolve(1.5)
        window show

        stop test_one fadeout 15

        "Казалось, я падаю в небо цвета разложившегося мяса."
        "Я схватился за корни, чтобы не кувыркнуться вверх."
        "Сознание сдутым шариком болталось на поверхности пучины и тонуло, скользило ко дну."

        scene roma_figth_0
        show layer master:
            align (.5, .5)
            zoom 1.05
        with Dissolve(0.3)

        "Я попытался привстать."

        scene roma_figth_01
        show layer master:
            align (.5, .5)
            zoom 1.05
        with Dissolve(0.3)

        play sound "voice/Polina/2day/140 Razm fugirka.ogg"

        "Размытая фигурка – Полина – отмахивалась, но две другие, взяв её под руки, уводили прочь."

        scene roma_figth_02
        show layer master:
            align (.5, .5)
            zoom 1.05

        voice "voice/byasha/Mi domoi.ogg"
        Bya "Мы домой тебя проводим, не бойся, на."

        voice "voice/semen/2day/100 Mal.ogg"
        Sem "Мало ли какие психи по лесу шастают."

        scene roma_figth_1
        show layer master:
            align (.5, .5)
            zoom 1.05
        with Dissolve(0.3)

        voice "voice/romka/2day/146 A Tosha.ogg"
        Rom "А Тоша пускай отдохнёт..."



        voice "voice/anton/2day/171. Polina (Tosha).ogg"
        Ant "Полина!"

        stop music2 fadeout 5
        "Ботинок Ромки прилетел мне в лоб."
        play sound "sounds/sfx_punch.ogg"

        window hide
        play test_two "voice/anton/2day/172. Botinok priletel.ogg"
        scene roma_figth_2:
            linear 0.03 xoffset 15
            linear 0.03 xoffset -15
            linear 0.04 xoffset 15
        show layer master:
            align (.5, .5)
            zoom 1.05
        with Dissolve(0.1)
        show bg_white with Dissolve(0.05)
        scene roma_figth_3 with Dissolve(0.2)
        $ renpy.pause(0.5)
        show bg_white with Dissolve(0.75)
        scene bg_black with Dissolve(1.25)
        window show
        play test_one "sounds/sfx_fall_on_snow.ogg"

        "Рука подломилась, затылок стукнулся о лёд. Зрачки безвольно закатились."
        "Тьма выпрыгнула, замерла..."
        "...и слопала меня."
        $ achievement_grant("ach_tough_luck")
        "..."

        voice "voice/anton/2day/142. Semen.ogg"
        Ant "Угх... кхр..."

        label bunny2_happy_family_nightmare:

        $ story_manager.MarkEvent(("day2", "s_polina1"))

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

        "Я пошевелился, потёрся носом о наволочку. С трудом разлепил веки."
        "Рисунки на стенах. Книги. Стопка комиксов."
        "Я потрогал челюсть, опасаясь, что она ответит вспышкой боли."
        "Пальцы переползли к виску — ни шишки, ни боли."

        play test_one "sounds/bed.ogg"

        "Я сел в кровати, удивлённо моргая. Поправил очки."
        "Изучил свои руки — чистые, без грязи под ногтями."
        "Рюкзак прикорнул у стола. Отголоски беседы раздавались за дверью."
        "Я дома, в своей спальне."
        "Сам добрёл? А очки? Их мне Семён вернул? Может, Полина? Или неизвестный доброжелатель?"
        "Решив выяснить это позже, я выглянул в окно. У леса было множество тайн, но он не спешил ими делиться."
        "Часы на прикроватной тумбочке показывали десять утра."
        "Солнце светило над полем, но не согревало его."
        "Закряхтела старыми костями чащоба."

        window hide
        call screen day2_nightmare_open()
        pause 0.5
        play test_one "sounds/knobs_open.ogg"
        show ant_room_door_open_day
        pause 0.5
        scene bg room_day_open_empty with Dissolve(0.5)
        play test_two "sounds/steps/Anton-stairs-out-2.ogg"
        pause 1

        stop music fadeout 3
        play music2 "music/This Is The End.ogg" volume 0.8 fadein 4

        scene bg door1 with Dissolve(0.5)
        window show
        play test_one "sounds/steps/Anton-stairs-in-2.ogg"

        play sound "voice/karina/2day/Ya vishel.ogg"
        play test_two "sounds/steps/Anton-steps-steal-1.ogg"

        "Я вышел в коридор, и отзвуки беседы сделались громче. Смех... Как давно я не слышал, чтобы мама смеялась."
        "В тихом доме, среди притаившихся теней."

        play sound "voice/karina/2day/113 Chtoby.ogg"

        "Такой обыденный родной смех."
        "Я прокрался по лестнице, словно боялся спугнуть момент."

        voice "voice/father/day_2/13 A ya emu.ogg"
        Pap "А я ему говорю: комиксы есть? Зайцу своему купить хочу."

        voice "voice/father/day_2/13 A on vash.ogg"
        Pap "А он: ваш заяц комиксы читает?"

        play sound "voice/karina/2day/51 Mama rassmeyalas.ogg"

        "Мама рассмеялась. Ей вторила Оля."

        voice "voice/father/day_2/14 Nu da govoru.ogg"
        Pap "Ну да, говорю! Заяц у меня цирковой!"

        voice "voice/karina/2day/108 Bozhe ty.ogg"
        Mam "Боже, ты лучший!"

        voice "voice/father/day_2/15A ti somnevalas.ogg"
        Pap "А ты сомневалась?"

        voice "voice/karina/2day/109 Ni na.ogg"
        Mam "Ни на секундочку!"

        voice "voice/olya/2day/48 Zenih.ogg"
        Oly "Жених и невеста!"

        scene bg kitchen1_0
        show nightmare_ol_d2
        show nightmare_pen1
        show Dad Happy m_day 00 norm ahead:
            xpos 1300
        show Mom Normal m_day 04 norm ahead
        with Dissolve(0.5)
        play test_two "sounds/steps/Anton-steps-in-1.ogg"
        play test_one "voice/karina/2day/110 Kogda ya.ogg"

        "Когда я вошёл на кухню, мама целовала отца в макушку, а он поглаживал её по плечу."
        "Оля сидела между родителями, вооружённая вилкой."

        show pan 0 with Dissolve(0.5)
        play sound "sounds/fork.ogg"

        "Накрытая крышкой крапчатая кастрюля источала ароматный запах."

        voice "voice/father/day_2/16_a_vot.ogg"
        Pap "А вот и он!"

        voice "voice/karina/2day/111 Privet.ogg"
        Mam "Привет, соня! Весь в отца."

        hide pan
        hide nightmare_ol_d2
        show nightmare_ol_d1 behind nightmare_pen1
        with Dissolve(0.5)

        "Прямоугольник окна возвышался за её спиной, отчего мама казалась нарисованной на белом холсте."

        voice "voice/father/day_2/17_sadis.ogg"
        Pap "Садись, садись, в ногах правды нет!"

        voice "voice/father/day_2/18_zavtrak.ogg"
        Pap "А завтрак – самое важное для здорового человека!"

        "Я сел, очарованно улыбаясь."

        play test_one "sounds/lamp2.ogg"

        show black:
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.1
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.1
            pause 0.05
            alpha 0.0

        "Оля подмигнула мне и одновременно мигнула лампа."

        voice "voice/karina/2day/112 Zaspanny.ogg"
        Mam "Заспанный какой!"

        voice "voice/father/day_2/19_kakoy_yest.ogg"
        Pap "Какой есть – наш, родной! В детдом сдавать поздно!"

        play sound "voice/father/day_2/19_hohotnul.ogg"
        "Папа хохотнул, показывая, что шутит. Мама хлопнула его по плечу."

        hide nightmare_ol_d1
        show nightmare_ol_d3 behind nightmare_pen1

        voice "voice/olya/2day/49 Oi ya.ogg"
        Oly "Ой, я голодная страшно!"

        hide nightmare_ol_d3
        show nightmare_ol_d1 behind nightmare_pen1

        voice "voice/karina/2day/113 A my.ogg"
        Mam "А мы, думаешь, просто так тут слюной капаем?"

        hide nightmare_ol_d1
        show nightmare_ol_d3 behind nightmare_pen1

        voice "voice/olya/2day/50 Bratik.ogg"
        Oly "Братик, ты так кушать будешь?"

        hide nightmare_ol_d3
        show nightmare_ol_d1 behind nightmare_pen1



        show dad_happy_day:
            xpos 1300
        show mom_happy_day

        voice "voice/anton/2day/204. Kak.ogg"
        Ant "Как?"

        "Я поймал на себе искрящиеся от веселья взгляды родителей."
        "Был бы у меня фотоаппарат – запечатлел бы, чтобы они всегда улыбались мне со снимка."

        play sound "voice/karina/2day/113_Chtoby_2.ogg"
        "Чтобы остановить этот прекрасный миг."

        play test_one "sounds/lamp3.ogg"

        hide black
        show black:
            alpha 0.1
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.4
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
        pause 0.3
        scene bg kitchen_window2:
            zoom 2.0/3.0
        show black:
            alpha 1.0
            pause 0.15
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.1
            pause 0.05
            alpha 0.0
        play music "music/amb new combined.ogg" fadein 5
        "Лампочка погасла и вспыхнула. Чуть слышно задребезжало стекло в раме."

        voice "voice/karina/2day/114 Snimy.ogg"
        Mam "Сними маску, сынок, — eсть же неудобно."

        scene bg kitchen_window3
        with Dissolve(2.0)

        voice "voice/anton/2day/205. Kakyu masku.ogg"
        Ant "Какую маску?"

        "Глуповатая улыбка прилипла к губам."












        $ dad_sprite = "Dad Happy b_evening 01"
        $ mom_sprite = "Mom Happy b_evening 01 norm ahead"
        $ olya_sprite = "Olya Happy b_evening 00 good ahead 07"
        call bunny2_happy_family
        with Dissolve(1.5)

        "Папа сказал, показывая крепкие белые зубы, похожие на клавиши пианино:"

        voice "voice/father/day_2/20_snimay.ogg"
        Pap "Снимай-снимай, заяц."

        play test_two "voice/anton/2day/206. Ya provel rukoi.ogg"

        "Я провёл рукой по щекам. Засмеялся."

        stop music2 fadeout 5

        voice "voice/anton/2day/207. Vi o chem.ogg"
        Ant "Вы о чём?"





        $ dad_y = 10
        $ dad_t = .17
        $ mom_y = 8
        $ mom_t = .13
        $ oly_y = 5
        $ oly_t = .15
        $ parallax_t = 5

        scene kitchen_wide as bg1:
            xalign .5
            xoffset camera_xoffset
            linear parallax_t xoffset camera_xoffset + bg_loop
        show layer master:
            align (.5, .5)
            zoom 1.05

        show kitchen_wide as bg2:
            xalign .5
            xoffset camera_xoffset - bg_loop
            linear parallax_t xoffset camera_xoffset

        show Dad Happy b_evening 01 as dad1:
            yalign 1.
            xalign .5
            xoffset dad_pos + camera_xoffset
            parallel:
                linear parallax_t xoffset dad_pos + camera_xoffset + bg_loop
            parallel:
                linear dad_t yoffset dad_y
                linear dad_t yoffset 0
                repeat
        show Dad Happy b_evening 01 as dad2:
            yalign 1.
            xalign .5
            xoffset dad_pos + camera_xoffset - bg_loop
            parallel:
                linear parallax_t xoffset dad_pos + camera_xoffset
            parallel:
                linear dad_t yoffset dad_y
                linear dad_t yoffset 0
                repeat

        show Mom Happy b_evening 01 norm ahead as mom1:
            yalign 1.
            xalign .5
            xoffset mom_pos + camera_xoffset
            parallel:
                linear parallax_t xoffset mom_pos + camera_xoffset + bg_loop
            parallel:
                linear mom_t yoffset mom_y
                linear mom_t yoffset 0
                repeat
        show Mom Happy b_evening 01 norm ahead as mom2:
            yalign 1.
            xalign .5
            xoffset mom_pos + camera_xoffset - bg_loop
            parallel:
                linear parallax_t xoffset mom_pos + camera_xoffset
            parallel:
                linear mom_t yoffset mom_y
                linear mom_t yoffset 0
                repeat

        show Olya Happy b_evening 00 good ahead 07 as olya1:
            yalign 1.
            xalign .5
            yoffset olya_y
            xoffset olya_pos + camera_xoffset
            parallel:
                linear parallax_t xoffset olya_pos + camera_xoffset + bg_loop
            parallel:
                linear oly_t yoffset oly_y + olya_y
                linear oly_t yoffset 0 + olya_y
                repeat
        show Olya Happy b_evening 00 good ahead 07 as olya2:
            yalign 1.
            xalign .5
            yoffset olya_y
            xoffset olya_pos + camera_xoffset - bg_loop
            parallel:
                linear parallax_t xoffset olya_pos + camera_xoffset
            parallel:
                linear oly_t yoffset oly_y + olya_y
                linear oly_t yoffset 0 + olya_y
                repeat


        play sound "voice/karina/2day/115 Uzhe vsya.ogg"
        $ renpy.pause(delay=parallax_t, hard=True)
        "Уже вся семья смеялась, тыча в меня пальцами и хлопая ладонями по коленам и клеёнке."

        window hide

        stop sound fadeout 2
        play test_one "voice/father/day_2/Haha.ogg"

        "Папа сказал, утирая костяшками увлажнившиеся глаза:"




        call bunny2_happy_family

        stop test_one fadeout 1
        voice "voice/father/day_2/21_nasmeshil.ogg"
        Pap "Ух, насмешил ты нас! Ну молодец."


        $ dad_sprite = "Dad Normal b_evening 01 norm ahead"


        call bunny2_happy_family
        with dissolve

        voice "voice/father/day_2/22_a_teper_masky.ogg"
        Pap "А теперь маску сними, будь добр."

        "Я опять потрогал своё лицо. Ощутил, как немеет кожа."


        $ camera_move_to = mom_center
        $ camera_transition_time = 3

        $ mom_sprite = "Mom Normal b_evening 01 norm ahead"
        $ olya_sprite = "Olya Serious b_evening 00 good ahead 01"
        call bunny2_happy_family

        $ renpy.pause(delay=3, hard=True)

        voice "voice/anton/2day/208. No na mne.ogg"
        Ant "Но на мне нет маски..."



        $ mom_sprite = "Mom Angry b_evening 01 norm ahead 01"


        call bunny2_happy_family

        "Мама поёрзала на стуле. Прищурилась, склонив голову."
        "«Холст» окна теперь был серым и всё быстрее чернел."



        $ mom_sprite = "Mom Nightmare1"


        call bunny2_happy_family

        play test_one "sounds/roll-hit-2.ogg"

        voice "voice/karina/2day/117 Poka ne.ogg"
        Mam "Пока не снимешь — не начнём."


        $ camera_move_to = olya_center
        $ camera_transition_time = 1



        call bunny2_happy_family

        voice "voice/olya/2day/52 No ya.ogg"
        Oly "Ну я не могу уже терпеть!"



        $ camera_move_to = dad_center
        $ camera_transition_time = 1



        call bunny2_happy_family

        voice "voice/father/day_2/23_snimi_masky.ogg"
        Pap "Сними маску. Не валяй дурака."

        "Голос был ласковый, но твёрдый."


        $ camera_move_to = olya_center
        $ camera_transition_time = 3


        $ olya_sprite = "Olya Weeps b_evening 00 good ahead 02"
        call bunny2_happy_family

        voice "voice/olya/2day/53 Mam.ogg"
        Oly "Ма-ам... Тоша меня пугает."


        $ olya_special_flag = True
        $ bg_special_flag = True





        call bunny2_happy_family
        play test_one "sounds/chair2.ogg"

        "Заскрипели ножки стула по половицам. Оля отодвинулась от меня."


        $ camera_move_to = dad_center
        $ camera_transition_time = 1



        call bunny2_happy_family

        "Она больше не улыбалась. Никто больше не улыбался — разве что щели облупившихся стен."




        $ dad_sprite = "Dad Angry b_evening 01 norm ahead"


        call bunny2_happy_family

        voice "voice/father/day_2/25_chto_nadelal.ogg"
        Pap "Что ты наделал? Твоя сестра плачет!"


        $ olya_special_xoffset = 0
        $ olya_y = 150
        $ camera_move_to = olya_center
        $ camera_transition_time = 1


        $ olya_sprite = "Olya Suffer b_evening 00 good ahead 04"
        call bunny2_happy_family

        voice "voice/anton/2day/209. No.ogg"
        Ant "Но..."

        play sound "voice/olya/2day/54 Plak1.ogg"

        "Оля хныкала, опустив голову, исподлобья боязливо посматривая на меня."

        play test_one "sounds/amb new fx2.ogg"
        play wtf "sounds/Taible_001.ogg"

        show pan 1
        show pan_1ani with vpunch:
            pause 1.0
            alpha 0.0

        "Мама грохнула кулаком по столешнице – я чуть не повалился на пол вместе со стулом."


        $ camera_xoffset = mom_center



        $ mom_sprite = "Mom Nightmare2"

        call bunny2_happy_family
        with Dissolve(.5)

        play test_one "sounds/roll-hit-1.ogg"

        voice "voice/karina/2day/118 Syn.ogg"
        Mam "Сын называется! Мы веселились, а тут ты пришёл! Испортил всё!"

        "В меня полетели брызги слюны."


        $ camera_move_to = dad_center
        $ camera_transition_time = 2
        $ dad_sprite = "Dad Daun"


        call bunny2_happy_family

        play test_one "voice/father/day_2/27_ya_povernylsya.ogg"
        "Я повернулся к папе, умоляя объяснить, что происходит."

        play sound "voice/father/day_2/28_sirop.ogg"
        "Липкий сироп тёк по подбородку отца и капал на рубашку. Глаза его смотрели в разные стороны."


        $ rotate_t = 5.
        $ mom_evil_mouth = True
        $ mom_sprite = "Mom Evil Nightmare"
        scene kitchen_wide as bg1:
            xalign .5
            block:
                xoffset camera_xoffset
                linear rotate_t xoffset camera_xoffset + bg_loop
                repeat

        show kitchen_wide as bg2:
            xalign .5
            block:
                xoffset camera_xoffset - bg_loop
                linear rotate_t xoffset camera_xoffset
                repeat

        show expression dad_sprite as dad1:
            yalign 1.
            xalign .5
            block:
                xoffset dad_pos + camera_xoffset
                linear rotate_t xoffset dad_pos + camera_xoffset + bg_loop
                repeat
        show expression dad_sprite as dad2:
            yalign 1.
            xalign .5
            block:
                xoffset dad_pos + camera_xoffset - bg_loop
                linear rotate_t xoffset dad_pos + camera_xoffset
                repeat

        show expression mom_sprite as mom1:
            yalign 1.
            xalign .5
            block:
                xoffset mom_pos + camera_xoffset
                linear rotate_t xoffset mom_pos + camera_xoffset + bg_loop
                repeat
        show expression mom_sprite as mom2:
            yalign 1.
            xalign .5
            block:
                xoffset mom_pos + camera_xoffset - bg_loop
                linear rotate_t xoffset mom_pos + camera_xoffset
                repeat

        show expression olya_sprite as olya1:
            yalign 1.
            xalign .5
            yoffset olya_y
            block:
                xoffset olya_pos + camera_xoffset
                linear rotate_t xoffset olya_pos + camera_xoffset + bg_loop
                repeat
        show expression olya_sprite as olya2:
            yalign 1.
            xalign .5
            yoffset olya_y
            block:
                xoffset olya_pos + camera_xoffset - bg_loop
                linear rotate_t xoffset olya_pos + camera_xoffset
                repeat


        play test_one "sounds/amb new fx2.ogg"

        "На чердаке грохнуло. Зашуршало в коридоре. Водопроводные трубы забурчали."

        play sound "sounds/sfx_sounds_house.ogg"

        "Дом ожил."

        play test_two "sounds/loop_sound_house.ogg"

        "В каждой комнате кто-то возился, ползал, дышал."


        $ mom_evil_mouth = False
        show black:
            block:
                alpha 1.0
                pause 0.05
                alpha 0.0
                pause 0.10
                repeat

        "Лампочка заморгала с частотой стробоскопа."

        $ rotate2_t = 0.8
        scene vzih_bg as bg1:
            xoffset 0
            linear rotate2_t xoffset 3794
            repeat
        show vzih_bg as bg2:
            xoffset -3794
            linear rotate2_t xoffset 0
            repeat
        show black:
            alpha 1
            .5
            linear .1 alpha 0
            .1
            block:
                alpha 1.0
                pause 0.05
                alpha 0.0
                pause 0.5
                repeat

        "Лица родителей то ныряли во тьму, то возникали вновь."

        scene vzih_anim1:
            xpos 0 ypos 0
            block:
                linear 8.0 xpos -1080
                linear 8.0 xpos 0
                repeat
        show black:
            block:
                alpha 1.0
                pause 0.05
                alpha 0.0
                pause 0.10
                repeat
        play test_four "sounds/steps/shagi-Koz.ogg"

        "За окнами прошла высокая тень."
        "Я намеревался вскочить, броситься прочь, но тело не повиновалось, руки мёртвым грузом лежали на столе."
        "Я просто смотрел."

        window hide
        $ renpy.pause(0.5)
        scene black:
            alpha 1.0
        $ renpy.pause(2.5)
        window show

        play test_two "sounds/sfx-fast-heartbeat-3.ogg"

        "Свет погас. Во мраке сердце ударило три раза."

        play test_one "sounds/amb new fx2.ogg"
        window hide
        show bg_white:
            alpha 1.0
            ease 3.0 alpha 0.0
        show Mom_mask:
            xoffset 50
        show Olya_mask
        show Dad_mask:
            xoffset 1150
        show bg_white1:
            alpha 1.0
            ease 0.1 alpha 0.0
            alpha 1.0
            ease 0.5 alpha 0.0
        show Mom Mask m_night 00:
            alpha 0.0
            xoffset 50
            ease 3.0 alpha 1.0
        show Olya Mask m_night 00:
            alpha 0.0
            ease 3.0 alpha 1.0
        show Dad Mask m_night 00:
            alpha 0.0
            xoffset 1150
            ease 3.0 alpha 1.0
        $ renpy.pause(3.0)
        show ef_scrap
        window show

        "Лампочка вспыхнула ярко."
        "Три маски уставились на меня дырами-отверстиями."

        scene bg_black with Dissolve(1.0)
        play sound "voice/karina/2day/breath_mask.ogg"
        show Mom Mask b_night 00:
            alpha 0.0
            ease 3.0 alpha 1.0
        show ef_scrap

        "Женщина-лиса там, где секунду назад сидела мама."

        scene bg_black with Dissolve(1.0)

        stop sound fadeout 2
        play test_one "voice/father/day_2/30 Rrrr.ogg"

        show Dad Mask b_night 00:
            alpha 0.0
            ease 3.0 alpha 1.0
        show ef_scrap

        "Мужчина-волк во главе стола."

        scene bg_black with Dissolve(1.0)
        stop test_one fadeout 2
        play sound "voice/olya/2day/Olya_breath_mask_1.ogg"
        show Olya Mask b_night 00:
            alpha 0.0
            ease 3.0 alpha 1.0
        show ef_scrap
        "И девочка-зайчик. Моя Оля."

        scene bg_black with Dissolve(1.0)
        stop sound fadeout 2
        show Mom Mask m_night 00:
            alpha 0.0
            xoffset 50
            ease 3.0 alpha 1.0
        show Olya Mask m_night 00:
            alpha 0.0
            ease 3.0 alpha 1.0
        show Dad Mask m_night 00:
            alpha 0.0
            xoffset 1150
            ease 3.0 alpha 1.0
        show ef_scrap

        "Я не мог даже спросить, зачем они нацепили эти странные и страшные морды."
        "И почему шерсть на них шевелится, словно что-то движется внутри масок, вспучивая папье-маше."
        "Язык отказался реагировать на команды мозга."
        "Лишь взгляд мой перемещался по маскам, по длинным кривым теням за спинами семьи."

        show black:
            alpha 0.1
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.4
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
        pause 0.3
        scene pan 1
        show black:
            alpha 1.0
            pause 0.15
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.1
            pause 0.05
            alpha 0.0

        play test_one "sounds/amb new fx2.ogg"

        voice "voice/karina/2day/119 Kyashat.ogg"
        Mam "Кушать подано!"

        stop music fadeout 2
        show ef_scrap

        "Она сорвала крышку с кастрюли."

        play test_two "sounds/Krizka.ogg"

        play test_one "sounds/Anton's nightmare(with).ogg"

        window hide
        show black:
            alpha 0.1
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.4
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
        pause 0.5
        scene pan 2:
            yzoom 1.01
            align (.5,1.)
            parallel:
                linear .05 yoffset 5
                linear .05 yoffset 0
                repeat
        show black:
            alpha 1.0
            pause 2.15
            alpha 0.0
            pause 0.05
            alpha 0.7
            pause 0.05
            alpha 0.0
            pause 0.05
            alpha 0.1
            pause 0.05
            alpha 0.0
        pause 2.3
        show old_movie_003_004:
            block:
                alpha 1.0
                pause 0.2
                alpha 0.0
                pause 4.2
                repeat
        show ef_scrap
        show bg_black:
            alpha 0.
            block:
                linear .05 alpha 0.35
                linear .05 alpha 0.
                repeat

        window hide

        "В кровавой подливе лежала отрезанная голова."

        play test_two "sounds/Anton's nightmare(without).ogg" loop

        "Остекленевшие глаза буравили меня. Распахнутый рот вопил беззвучно."

        hide black
        show black:
            alpha 0.0
            ease 5.0 alpha 1.0

        "Моя собственная голова на дне кастрюли."

        show Zaichik_01:
            xpos 1984
            ypos -1432
            ease 5.0 xpos 0 ypos 0

        hide bg_black
        show bg_black:
            alpha 0.
            block:
                linear .05 alpha 0.35
                linear .05 alpha 0.
                repeat

        "Кровь заструилась из отсечённой головы по перекошенному лицу."
        "Одновременно горячие струйки потекли из моих ноздрей, марая клеёнку багровым."

        show Zaichik_01 behind bg_black:
            ease 0.1 xpos 10 ypos -10
            ease 0.1 xpos 0 ypos 0

        voice "voice/karina/2day/120 Esh.ogg"
        Mam "Ешь!"


        show Zaichik_01 behind bg_black:
            xpos 0 ypos 0 alpha 0.45
            pause 0.08
            ease 0.1 xpos 10 ypos 10
            ease 0.1 xpos -10 ypos -10
            repeat
        show Zaichik_02 behind bg_black:
            xpos 0 ypos 0
            ease 0.1 xpos -10 ypos -10
            ease 0.1 xpos 10 ypos 10
            repeat
        with Dissolve(0.1)

        play sound "voice/anton/2day/211. Ya zakrichal.ogg"

        "Я закричал."

        window hide
        scene Wecup_00
        show Wecup_00_ani
        with Dissolve(1.3)
        window show

        stop test_two fadeout 2
        stop sound fadeout 1

        "..."
        "Резко выпрямился. Челюсть обдало огнём. Висок саднило."
        play music "music/4_Olya's nightmare.ogg"
        "Кухня, твари в масках и мёртвая голова – всё исчезло."
        "Всё, кроме преследовавшей меня проклятой маски, которую кто-то из хулиганов нацепил на меня ради смеха."

        play test_one "sounds/sfx_drop_mask.ogg"
        scene Wecup_01 with Dissolve(0.5)
        play sound "voice/anton/2day/fear2.ogg"

        "Я оторвал уже примёрзшую к моему лицу заячью морду и понял, что очнулся в лесу, возле поваленного снеговика."

        scene Wecup_02 with Dissolve(0.5)



        "Весь в снегу и хвойных иголках. Без очков и с разбитой физиономией."
        "Обморок... Кошмар..."

        window hide

        scene black
        show sosni 0_blur_ne_blur at truecenter:
            zoom .5

        with Dissolve(1.3)
        window show

        "Пульсирующая боль была подарком по сравнению с привидевшимся ужасом."
        window hide



        scene black
        show batya wood 0_blur_ne_blur
        with Dissolve(1.3)
        window show
        play sound "voice/anton/2day/201. Vstal.ogg"

        "Я поднялся на ноги, отплёвываясь."
        "Лес огородил меня, как прутья решётки. Я не знал, как долго пробыл в отключке."
        "Ноги и руки задубели. Штаны промокли насквозь."

        "Я стоял один почти в полной темноте, в кольце взмывающих ввысь стволов."


    if Flags.Has("fight"):
        play music2 "music/4_Olya's nightmare.ogg"
        "И всё вокруг шевелилось и дрожало, уши закладывало от шороха и шелеста."
        "Кроны таяли в космической черноте."
        "Кусты становились пустыми клетками, чьи обитатели вдруг вышли на волю."




        "Казалось, что вот-вот когтистая лапа выпростается из мрака и схватит моё одеревеневшее лицо."













        "Где-то вдалеке послышался крик."

        voice "voice/father/day_2/Antooon.ogg"
        Noname "Анто-о-о-о-он!"



        if Flags.Has("day2 polina"):
            scene black
            show batya wood2 0_blur_ne_blur
            with Dissolve(1.3)

        "Меня искали. Как того..."
        "..пропавшего мальчика."
        "Глаза защипало выступившими слезами. Тяжёлая капля сорвалась с ресниц."


        if Flags.Has("day2 polina"):
            show batya wood3 0_blur_ne_blur
            with Dissolve(1.3)


        voice "voice/father/day_2/Antooon2.ogg"
        Noname "Анто-о-он!"

        "Крик зазвучал громче, и на мгновенье я даже поверил, что меня спасут."

        if Flags.Has("day2 polina"):

            show batya wood4 0_blur_ne_blur
            with Dissolve(1.3)

        stop music fadeout 4
        stop music2 fadeout 4

        voice "voice/anton/2day/188. Ya zes.ogg"
        Ant "Я зде-е-есь!.."

    if Flags.Has("day2 polina"):

        window hide
        scene black
        show batya wood05 0_blur_ne_blur
        with Dissolve(1.3)








        show Hand_2:
            xpos -.25
            ypos 3.0
            linear .7 ypos -.45
        $ renpy.pause (0.7, hard = True)

        show batya wood_5 0_blur_ne_blur
        window show

        play test_three "sounds/Phrases_08.ogg"

        "Тут же свет ударил мне в лицо. Я заслонился пятернёй."


    if Flags.Has("day2 fox"):

        show fkoz_beast true behind fkoz_2_2:
            align (.5,.5)
            zoom 1.05
        with Dissolve(1.)
        show kozel_eye5:
            align (.5,.5)
            zoom 1.05

        play music "music/Master of the forest.ogg" fadein 3
        play sound "sounds/Phrases_01.ogg"

        "Одно из деревьев двинулось вперёд."
        "Это был не Ромка. И не Бяша."
        "Кто-то взрослый. Высокий, с длинными руками."

        play sound "sounds/Phrases_02.ogg"

        show kozel_eye1:
            xoffset 60
            alpha 0
            linear 0.5 alpha 1
        show kozel_eye2:
            alpha 0
            pause .1
            linear 0.5 alpha 1
        show kozel_eye3:
            alpha 0
            pause .3
            linear 0.5 alpha 1
        show kozel_eye4:
            alpha 0
            pause .4
            linear 0.5 alpha 1

        hide fkoz_1_2
        hide fkoz_1_1

        show fkoz_1_2:
            align (.5,1.)
            xoffset 250
            zoom 1.15
        show fkoz_1_1:
            align (.5,1.)
            xoffset -250
            zoom 1.15

        "А позади него крались тени, напоминавшие собак, но эти существа были намного крупнее Жульки."
        "Лес больше не таился, не прятался за ложными образами."
        "Я замер, будто олень, нашпиленный на лучи приближающегося автомобиля, а чудища уставились на меня."
        "В сумерках без очков я видел слишком мало, но и увиденного хватало с лихвой, чтобы остолбенеть от ужаса."
        "Резкий запах звериной мочи и мокрой шерсти окутал поляну, когда жуткая процессия во главе с гигантом направилась ко мне."

        hide fkoz_beast
        hide fkoz_2_2
        hide fkoz_2_1
        hide kozel_eye1
        hide kozel_eye2
        hide kozel_eye3
        hide kozel_eye4
        hide kozel_eye5
        hide fkoz_1_2
        hide fkoz_1_1

        show fkoz_beast true:
            subpixel True
            align (.5,.5)
            zoom 1.05
            linear 3 zoom 1.15
        show fkoz_2_2:
            align (.5,1.)
            xoffset 300
            zoom 1.05
        show fkoz_2_1:
            align (.5,1.)
            xoffset -240
            zoom 1.05

        show kozel_eye1:
            subpixel True
            xoffset 60
            align (.5,1.)
            linear 3 zoom 1.1
        show kozel_eye2:
            subpixel True
            align (.5,1.)
            linear 3 zoom 1.1
        show kozel_eye3:
            subpixel True
            align (.5,1.)
            linear 3 zoom 1.1
        show kozel_eye4:
            subpixel True
            align (.5,1.)
            linear 3 zoom 1.1
        show kozel_eye5:
            subpixel True
            align (.5,.5)
            zoom 1.05
            linear 3 zoom 1.15

        show fkoz_1_2:
            align (.5,1.)
            xoffset 250
            zoom 1.15
        show fkoz_1_1:
            align (.5,1.)
            xoffset -250
            zoom 1.15

        show bg_black:
            alpha 0
            pause 1
            linear 2 alpha 1.

        stop music2 fadeout 2
        play test_four "sounds/steps/shagi-Koz.ogg"
        play test_two "sounds/snow-snd-2.ogg"

        "От страха подкосились ноги, и я упал на колени в снег, словно бы молясь этой фигуре, деревьям, темноте."

        scene kozel_hoof_1_blur with Dissolve(.5)
        play sound "voice/anton/2day/fear.ogg"

        "Я не смел поднять глаз, и когда он подошёл, накрыв меня смрадом, на миг почудилось, что ноги его поросли серой шерстью."

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

        pause 0.5
        scene bg_black
        with Dissolve(.5)
        play sound "voice/anton/2day/fear2.ogg"

        "Я зажмурился так сильно, что на внутренней стороне век заплясали красные круги."

        play sound "voice/anton/2day/fear3.ogg"

        "Лишь бы не видеть всего этого!"

        play sound "voice/anton/2day/fear4.ogg"

        "Зато я чудесно слышал."
        "Его дыхание наждачной бумагой царапало уши."
        "Хриплое, глубокое. Рычащее."

        voice "voice/kozel/2day/02 Hrr A.ogg"
        Noname "Хр-р... р-р-рых, р-р-рых, р-р-рых..."

        "Я выудил из памяти бабушкин заговор:"

        $ music_during_lines = 0.75
        voice "voice/anton/2day/190. Mertvoe.ogg"
        Ant "Мёртвое — к мёртвому! Живое — к живому! Мёртвое — к..."

        scene kozel_loop with Dissolve(2.0):
            yalign .5
            yzoom 1.01
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat

        play test_one "voice/kozel/2day/02 Otvetom.ogg"

        "Ответом были рычание и вонь."
        "Слова не защищали от когтей и клыков. Я был бессилен."
        "И тут неподалёку послышался знакомый ласковый голосок."

        voice "voice/Alisa/Alisa2day/183 Nu ze.ogg"
        Alis "Ну же, скорей! Попробуй его на вкус."

        window hide

        scene kozel_loop_full with Dissolve(.15):
            yalign .5
            yzoom 1.01
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat
        pause 0.8
        play wtf "voice/kozel/2day/02 Nu ze.ogg"
        play test_six "sounds/snare-noise-1.ogg"

        $ renpy.pause(1.2)

        show Veko_01:
            xpos 0
            ypos -1080
            alpha 0.0
            linear .25 xpos 0 ypos -540 alpha 1.0
        show Veko_02:
            xpos 0
            ypos 1080
            alpha 0.0
            linear 0.25 xpos 0 ypos 0 alpha 1.0
        show bg_black:
            alpha 0.0
            pause 0.15
            linear 0.35 alpha 1.0

        voice "voice/anton/2day/191. Ne nado.ogg"
        Ant "Не надо!"

        play test_two "sounds/sfx_sticky_licking.ogg"

        "Что-то горячее пробежало по горлу, как верёвка, мясистая и липкая."
        "Язык."

        voice "voice/Alisa/Alisa2day/184 Ya ze.ogg"
        Alis "Я же говорила, Хозяин!"

        voice "voice/Alisa/Alisa2day/185 Eto nash.ogg"
        Alis "Это наш Зайчик."

        voice "voice/Alisa/Alisa2day/186 O nem.ogg"
        Alis "Позаботься о нём."

        scene kozel_phase2_2:
            yalign .5
            yzoom 1.01
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat

        show Veko_01:
            ypos -540
            pause .5
            linear .5 ypos -810

        show Veko_02:
            pause .5
            linear 0.5 ypos 270

        show bg_black:
            alpha 1.0
            linear 0.5 alpha 0.0

        play sound "voice/anton/2day/fear7.ogg"

        "В узкой бойнице приподнятых век за дрожащими пальцами я видел грозную фигуру, нависшую надо мной."
        "Вкушал запах псарни, компостных ям и мха."
        "Передо мной величественно и жутко возвышался рогатый зверь."
        "В позе сквозила будоражащая царственность."
        "Рога подпирали тучи, а вытаращенные бельма впивались крючьями в мои готовые лопнуть от ужаса глаза."

        window hide
        hide Veko_01
        hide Veko_02

        show Veko_01:
            ypos -810
            linear .5 ypos -540
        show Veko_02:
            ypos 270
            linear 0.5 ypos 0
        show bg_black:
            alpha 0.0
            pause .5
            linear 0.5 alpha 1.0

        pause 1.0

        scene kozel_hoof_1_blur

        show Veko_01:
            ypos -540
            pause .5
            linear .5 ypos -1080

        show Veko_02:
            pause .5
            linear 0.5 ypos 1080

        show bg_black:
            alpha 1.0
            linear 1.0 alpha 0.0

        show layer master:
            align (.5, .5)
            zoom 1.05

        play sound "voice/anton/2day/fear6.ogg"

        "Руки были полны даров."

        show kozel_hoof_2_blur with vpunch
        play test_one "sounds/sfx_toys_from_bag0.ogg"

        "Конфеты выпадали на снег и переливались пёстрыми фантиками. Серебрились упаковки шоколадных батончиков, «Чупа-чупс» воткнулся в сугроб пластиковой палочкой."

        voice "voice/kozel/2day/03 Tebe.ogg"
        Master "Тебе-е-е-е!"

        "К моим ногам посыпались конфеты."

        show kozel_hoof_3_blur with vpunch

        play test_one "sounds/sfx_plastic_rifle_drop.ogg"
        play sound "voice/anton/2day/fear8.ogg"
        play test_two "sounds/sfx_toys_from_bag.ogg"

        "Стукнулся о лёд игрушечный автомат, и, парализованный страхом, я вспомнил: у пропавшего Вовы был точно такой же."
        "Рядом упала кукла. Посыпались градом: металлическая юла, плюшевый медведь с облезлым носом, рыжий Карлсон без пропеллера, оловянный солдатик-знаменосец, пожарная машина и кукурузник..."

        play sound "voice/anton/2day/fear6.ogg"

        "Игрушки не были перепачканы в крови, но воображение дорисовывало багровые потёки и кляксы."
        "На эти сокровища, принадлежавшие безвестным детям, ложилась рогатая тень чудовища."

        voice "voice/kozel/2day/04 Beri.ogg"
        Master "Бе-е-е-ери."

        window hide
        scene black
        show mask_before
        play sound "voice/anton/2day/192. Kosmatie ruki.ogg"

        "Косматые руки выудили откуда-то из темноты преследовавшую меня образину зайца..."

        show wear_mask with Dissolve (0.2)
        play sound "sounds/sfx_masked_face_punch.ogg"
        $ renpy.pause(2.4, hard=True)
        window hide
        scene black with Dissolve (0.7)

        "...и грубо нацепили мне на лицо."

        $ renpy.start_predict("kozel_light")

        scene kozel_phase2_2b
        with Dissolve(1.)

        voice "voice/kozel/2day/05 Zaichick.ogg"
        Master "Зайчик."
        $ music_during_lines = 1.0

        "Тени зверей вокруг медленно и грациозно встали на задние лапы."

        show kozel_light
        show Hand_2:
            xpos -.25
            ypos 3.0
            pause .0
            linear .7 ypos -.45

        $ renpy.stop_predict("kozel_light")
        stop music fadeout 1.5
        play test_three "sounds/Phrases_08.ogg"

        "Тут же свет ударил мне в лицо, расколов пополам фигуру монстра."





        "Я заслонился пятернёй."

    if Flags.Has("day2 polina"):
        hide batya
        show batya wood6 0_blur_ne_blur

        hide Hand_2
        show Hand_2:
            xpos -.25
            ypos -.45
            linear 4.7 ypos 3.0 xpos .25

    if Flags.Has("day2 fox"):

        show batya_kozel_19_reblur
        hide Hand_2
        show Hand_2:
            xpos -.25
            ypos -.45
            linear 4.7 ypos 3.0 xpos .25

    if Flags.Has("fight"):

        play music2 "music/8_Peredyshka.ogg" volume 0.9 fadein 1
        play fon "sounds/fon/owls-1.ogg"  fadein 5.0 loop
        play sound "voice/anton/2day/130. Vidoh.ogg"

        "Луч фонаря скользнул вниз."


    if Flags.Has("day2 polina"):
        voice "voice/father/day_2/32_anton_vot_ty_gde.ogg"
        Pap "Антон! Вот ты где!"


        hide batya
        show batya wood7 0_blur_ne_blur
        with Dissolve(.7)

        voice "voice/father/day_2/33_sovsem_sdyrel.ogg"
        Pap "Ты совсем сдурел?"

    if Flags.Has("day2 fox"):
        voice "voice/father/day_2/32_Anton_Z.ogg"
        Pap "Антон!"

        voice "voice/father/day_2/32_vot_ty_gde.ogg"
        Pap "Вот ты где!"

        voice "voice/father/day_2/33_sovsem_sdyrel.ogg"
        Pap "Ты совсем сдурел?!"

    if Flags.Has("fight"):
        $ story_manager.MarkEvent(("day2", "scene10"))
        voice "voice/father/day_2/34_eto_voobshe_kak_ponimat.ogg"
        Pap "Это вообще как понимать?!"

    if Flags.Has("day2 polina"):
        "Папа шагнул ко мне из мрака."
        "Я ринулся навстречу, надеясь, что он не растает, оказавшись очередным миражом, проделками свихнувшегося разума."
        "Он был настоящим, тёплым и живым."

    if Flags.Has("day2 fox"):
        "Онемев, я глядел на папу. Туда, где секунду назад громоздилось чудовище."
        "Мрак укутал поляну, но игрушки и конфеты темнели на снегу."
        "А если набраться сил и подойти к кустам, то наверняка там будут и отпечатки лап."

    if Flags.Has("fight"):
        voice "voice/father/day_2/39_yazik_proglotil.ogg"
        Pap "Язык проглотил?!"

    if Flags.Has("day2 polina"):
        window hide

        hide batya
        show batya wood8 0_blur_ne_blur
        with Dissolve(.7)

        voice "voice/father/day_2/39_ya_vstretil_odnoklassnicy.ogg"
        Pap "Я встретил твою одноклассницу на дороге. Она сказала..."

    if Flags.Has("day2 fox"):
        voice "voice/father/day_2/36_ondoklassniki_tvoi.ogg"
        Pap "Одноклассники твои к нам пришли!"

        voice "voice/father/day_2/36_skazali_chto_sbezhal.ogg"
        Pap "Сказали: ты сбежал от них в лес, в самую чащу, и..."

        hide batya_kozel_17_reblur
        show batya_kozel_17_reblur

        voice "voice/father/day_2/36_chto_za_dryan_napyalil.ogg"
        Pap "Что за дрянь ты напялил?.."

        show bad_mask 3:
            alpha 0
            zoom 1.5
            align (.5,.5)
            linear .5 alpha 1. zoom 1

        pause 1.5
        play sound "sounds/sfx_drop_mask.ogg"

        "Я стянул маску с взопревшего лица и бросил её к остальным игрушкам."

    if Flags.Has("fight"):

        if Flags.Has("day2 polina"):

            hide batya
            show batya wood9 0_blur_ne_blur
            with Dissolve(.3)

        if Flags.Has("day2 fox"):
            hide batya_kozel_21_reblur
            show batya_kozel_21_reblur
        play test_one "voice/father/day_2/40_v_debryah.ogg"
        play sound "sounds/wood-break-1.ogg"

        "В дебрях захрустели ветки."
        "Снедаемый ужасом, я прильнул к отцу. А он встрепенулся, изучая чащобу."
        "И сказал совсем другим, напряжённым тоном:"

        if Flags.Has("day2 polina"):

            hide batya
            show batya wood6 0_blur_ne_blur
            with Dissolve(.7)
        if Flags.Has("day2 fox"):
            hide batya_kozel_18_reblur
            show batya_kozel_18_reblur

        voice "voice/father/day_2/41_poydem_otsyda.ogg"
        Pap "Так, пойдём отсюда скорее."

        voice "voice/father/day_2/41_mat_yznaet_kakoy.ogg"
        Pap "Мать узнает — такой нагоняй нам устроит – мало не покажется!"

        "Я потянулся к отцу, всё ещё леденея от ужаса."
        "Схватился за его крепкую ладонь, почувствовал подушечками быстрый пульс."


        if Flags.Has("day2 polina"):

            hide batya
            show batya wood 0_blur_ne_blur
            with Dissolve(1.3)
        if Flags.Has("day2 fox"):
            hide batya_kozel_22_reblur
            show batya_kozel_22_reblur
            with Dissolve(1.3)
        play test_six "sounds/steps/footsteps_two2.ogg"

        "Поднялся и, пошатываясь, побрёл с папой по его едва различимым следам."

        stop test_six fadeout 15

        "Назад, к человеческому жилью, к свету, к дороге, где отец припарковал машину."

        voice "voice/father/day_2/43_doma_ni_slova.ogg"
        Pap "Чтобы дома — ни слова. Ясно?!"

        voice "voice/father/day_2/43_ni_edinogo_nameka.ogg"
        Pap "Ни единого намёка, где я тебя нашёл."

        voice "voice/anton/2day/194. Da pap.ogg"
        Ant "Да, пап."

        window hide
        scene black

        with Dissolve (2.0)
        window auto

        "Он держал меня за руку, словно что-то очень ценное, и всё рассказывал, как боится потерять меня и Олю."


    if Flags.Has("day2 polina"):
        $ story_manager.MarkEvent(("day2", "s_polina2"))
        "Я кивал и послушно перебирал ногами."

        stop fon fadeout 3
        scene black
        stop test_six
        play test_seven "sounds/car-door3.ogg"
        "..."

        window hide
        $ incar_state_bg = 0
        $ incar_state_snow = 0
        $ incar_state_chetki = 0
        $ incar_state_car = 0
        $ incar_state_dad = 0
        $ incar_state_box1 = 0
        $ incar_state_box2 = 0
        $ incar_state_at = 0
        show screen incar_polina()

        "Только в машине отец заметил ссадины."

        voice "voice/father/day_2/45_tebya_bili.ogg"
        Pap "Тебя били?"

        "Я ощупал скулу."

        voice "voice/anton/2day/195. Podralsya.ogg"
        Ant "Подрался..."

        voice "voice/father/day_2/48_iz_za_chego.ogg"
        Pap "Из-за чего?"

        voice "voice/anton/2day/196. Iz-za devushki.ogg"
        Ant "Из-за девушки."

        $ incar_state_dad = 1
        $ renpy.start_predict("incar_polina_bg2")
        $ renpy.start_predict("incar_comp")

        "Отец кивнул вдумчиво."

        $ incar_state_dad = 2
        $ incar_state_car = 1
        $ incar_state_chetki = 1
        $ incar_state_at = 1
        play test_one "sounds/sfx_car_engine_start.ogg"

        "Загудел двигатель."

        play test_two "sounds/loop_car_driving_inside_snow.ogg" loop

        $ incar_state_bg = 1
        $ incar_state_chetki = 2
        $ incar_state_at = 2




        $ dx_bonus = 450
        $ sssnow0.factory.xspeed = (sssnow0.factory.xspeed[0] + dx_bonus, sssnow0.factory.xspeed[1] + dx_bonus)
        $ sssnow1.factory.xspeed = (sssnow1.factory.xspeed[0] + dx_bonus, sssnow1.factory.xspeed[1] + dx_bonus)
        $ sssnow2.factory.xspeed = (sssnow2.factory.xspeed[0] + dx_bonus, sssnow2.factory.xspeed[1] + dx_bonus)
        $ sssnow3.factory.xspeed = (sssnow3.factory.xspeed[0] + dx_bonus, sssnow3.factory.xspeed[1] + dx_bonus)
        $ sssnow4.factory.xspeed = (sssnow4.factory.xspeed[0] + dx_bonus, sssnow4.factory.xspeed[1] + dx_bonus)
        play sound "voice/father/day_2/47_v_vyrazhenii.ogg"

        "В выражении папиного лица я угадал боязнь. Но это был не липкий, парализовавший меня в кошмаре, страх."
        "Его страх был благородным и чистым бриллиантом."

        $ incar_state_box1 = 1
        play test_one "sounds/sfx_glove_box_open.ogg"

        "Он открыл бардачок, достал салфетки."

        $ incar_state_box2 = 1
        $ incar_state_dad = 3

        play test_one "sounds/sfx_tissue.ogg"

        voice "voice/father/day_2/49_mama_by_seychas.ogg"
        Pap "Мама бы меня сейчас не одобрила. Но вот что, сынок."

        voice "voice/father/day_2/49_dratsya_za_devushky.ogg"
        Pap "Драться за девушку – это правильно."

        voice "voice/father/day_2/51_nyzno_reshat.ogg"
        Pap "Да, нужно решать конфликт словами. Но иногда... иногда слова не помогают."

        $ incar_state_dad = 2

        "И папа улыбнулся мне подбадривающе."

        hide screen incar_polina

        scene incar_bord 0_blur_ne_blur at my_shake2 (2):
            zoom 1.01
            xpos -3
            ypos -3

        $ renpy.start_predict("incar_forest")
        $ renpy.start_predict("incar_car")
        $ renpy.start_predict("snow_for_forest0")
        $ renpy.start_predict("incar_snow_up")

        "За секунду до того, как он захлопнул бардачок, я увидел торчащую из-под тряпки рукоять."
        "Он возил с собой оружие. Мой интеллигентный папа держал под рукой пистолет. Как герой боевиков."
        "{i}«Или как обычный бандит»{/i}, - шепнул голосок."

        play test_six "sounds/close_bordachek.ogg"

        show screen incar_polina()
        $ incar_state_bg = 1
        $ incar_state_chetki = 2
        $ incar_state_car = 1
        $ incar_state_dad = 2
        $ incar_state_box1 = 0
        $ incar_state_box2 = 0
        $ incar_state_at = 2

        if not Flags.Has("day2 polina"):
            $ dx_bonus = 450
            $ sssnow0.factory.xspeed = (sssnow0.factory.xspeed[0] + dx_bonus, sssnow0.factory.xspeed[1] + dx_bonus)
            $ sssnow1.factory.xspeed = (sssnow1.factory.xspeed[0] + dx_bonus, sssnow1.factory.xspeed[1] + dx_bonus)
            $ sssnow2.factory.xspeed = (sssnow2.factory.xspeed[0] + dx_bonus, sssnow2.factory.xspeed[1] + dx_bonus)
            $ sssnow3.factory.xspeed = (sssnow3.factory.xspeed[0] + dx_bonus, sssnow3.factory.xspeed[1] + dx_bonus)
            $ sssnow4.factory.xspeed = (sssnow4.factory.xspeed[0] + dx_bonus, sssnow4.factory.xspeed[1] + dx_bonus)

        "За окнами мельтешили сосны. Фары бодались с темнотой."
        pause 1

        $ incar_state_dad = 3

        "Машина везла домой. Папа изучал меня настороженно в зеркало заднего вида."
        "Я думал о пистолете, о снах, о людях в масках зверей, притворявшихся моими родителями."

        stop test_two fadeout 2

    if Flags.Has("day2 fox"):
        $ story_manager.MarkEvent(("day2", "s_fox2"))
        "Но это был не тот липкий, как язык животного, страх."
        "Его страх был благородным и чистым бриллиантом. А я кивал и послушно перебирал ногами."
        "И вдруг где-то из-за спины я вновь услышал знакомый голос:"

        window hide



        show polina_lisa_05:
            alpha 0
            linear .5 alpha 1
            linear .5 alpha 0
        show polina_lisa_06:
            alpha 0
            pause .5
            linear .5 alpha 1
            pause .25
            linear .5 alpha 0
        show Fox Normal b_night 00 as fox1:
            alpha 0
            pause 1
            linear 1. alpha 1
            alpha 0
        show Fox Normal b_night 00 good ahead as fox2:
            alpha 0
            pause 2
            alpha 1


        $ renpy.start_predict("incar_garage_bg")

        voice "voice/Alisa/Alisa2day/187 Pomni.ogg"
        Alis "Помни..."

        stop music2 fadeout 2

        voice "voice/Alisa/Alisa2day/188 Poka.ogg"
        Alis "Пока ты со мной — никто тебя здесь не тронет."



        stop test_six
        play test_seven "sounds/car-door3.ogg"
        show black as forebg:
            alpha 0
            linear 2 alpha 1

        "..."
        play test_one "sounds/sfx_car_engine_start.ogg"
        stop fon fadeout 2

        "Машина двинулась по направлению к дому."

        play test_two "sounds/loop_car_driving_inside_snow.ogg" loop

        $ incar_state_bg = 1
        $ incar_state_chetki = 2
        $ incar_state_car = 1
        $ incar_state_dad = 2
        $ incar_state_box1 = 0
        $ incar_state_box2 = 0
        $ incar_state_at = 2
        show screen incar_polina()

        $ renpy.start_predict("incar_forest")
        $ renpy.start_predict("incar_car")
        $ renpy.start_predict("snow_for_forest0")
        $ renpy.start_predict("incar_snow_up")

        if not Flags.Has("day2 polina"):
            $ dx_bonus = 450
            $ sssnow0.factory.xspeed = (sssnow0.factory.xspeed[0] + dx_bonus, sssnow0.factory.xspeed[1] + dx_bonus)
            $ sssnow1.factory.xspeed = (sssnow1.factory.xspeed[0] + dx_bonus, sssnow1.factory.xspeed[1] + dx_bonus)
            $ sssnow2.factory.xspeed = (sssnow2.factory.xspeed[0] + dx_bonus, sssnow2.factory.xspeed[1] + dx_bonus)
            $ sssnow3.factory.xspeed = (sssnow3.factory.xspeed[0] + dx_bonus, sssnow3.factory.xspeed[1] + dx_bonus)
            $ sssnow4.factory.xspeed = (sssnow4.factory.xspeed[0] + dx_bonus, sssnow4.factory.xspeed[1] + dx_bonus)

        window hide
        $ incar_state_bg = 2
        show screen incar_polina with Dissolve(1.)

        $ renpy.pause(delay=2.0, hard=True)

        play test_three "sounds/Garage.ogg" 
        hide bg_black

        pause 10

        $ renpy.stop_predict("incar_garage_bg")

        play music2 "music/26_Mistik.ogg" volume 0.75 fadein 5.0

        "Припав к стеклу, я различил среди елей приземистую постройку, хибару чернее самой чёрной ночи."
        "Гараж, хоронившийся в чащобе. Металлический склеп."
        "Он словно шёл за нами по пятам."
        "Через миг постройка скрылась за поворотом."

        stop test_two fadeout 2

        "Я сглотнул горечь."

    if Flags.Has("fight"):
        hide screen incar_polina

        $ renpy.stop_predict("incar_polina_bg2")
        $ renpy.stop_predict("incar_comp")

        scene black
        show incar_forest
        show incar_car
        show snow_for_forest0
        show incar_snow_up:
            zoom 3.0
            linear 8.0 zoom 1.0
        with Dissolve (2.0)
        pause 3
        play test_three "sounds/sfx_car_passing_by_snow.ogg"
        pause 10




        $ renpy.stop_predict("incar_forest")
        $ renpy.stop_predict("incar_car")
        $ renpy.stop_predict("snow_for_forest0")
        $ renpy.stop_predict("incar_snow_up")

        "А белые снежинки всё парили в темноте."

        stop music2 fadeout 5
        scene black with dissolve
        $ renpy.pause (1.0, hard= True)
        scene black with dissolve


label bunny2_home_evening:
    $ story_manager.MarkEvent(("day2", "scene11"))
    window hide
    scene bg house_night6_snow_blur with Dissolve(0.5)
    $ renpy.stop_predict("bg house_night6_snow_blur")
    $ renpy.pause(2.5)
    scene bg door_open_night_blur with Dissolve(0.3)
    $ renpy.pause(1.5)
    play test_one "sounds/Door_close.ogg"
    scene bg door_night_blur with Dissolve(0.1)
    $ renpy.pause(1.5)

    if Flags.Has("mask"):

        play music "music/17_Flow.ogg" volume 0.75 fadein 2

        show Mom Normal m_evening 00 norm aside blur at left with Dissolve(0.5)

        window show

        voice "voice/karina/2day/05 Tak ya ne.ogg"
        Mam "Так, я не поняла... Антон, а где очки? Потерял?"

        voice "voice/anton/2day/Danumam.ogg"
        Ant "Да, ну мам."

        voice "voice/karina/2day/06 I kak.ogg"
        Mam "И как можно быть таким рассеянным? Ты думаешь, я деньги печатаю?"

        voice "voice/karina/2day/06 Kakze.ogg"
        Mam "Как же! Будешь до следующего года в старых очках ходить." id bunny2_home_evening_7c826de7

        play test_one "sounds/steps/mam_out.ogg"
        hide Mom with Dissolve(0.5)

        "Ко мне бросилась Оля."
    else:

        stop music2 fadeout 5
        play music "music/17_Flow.ogg" volume 0.75  fadein 2
        show Dad Normal m_night_winter 02 norm aside blur:
            xpos 1100
        with Dissolve(0.5)

        window show

        voice "voice/father/day_2/53_a_vot_i_my.ogg"
        Pap "А вот и мы!"

        voice "voice/karina/2day/Yavilis nezapililis.ogg"
        Mam "Явились — не запылились."

        "Мама спускалась по лестнице, вцепившись в отца фирменным взглядом."

        play sound "sounds/steps/mam_in.ogg"
        show Mom Normal m_evening 00 norm aside blur at mom_income_left with Dissolve(0.5)

        "На её лице застыла грозная эмоция на стыке гнева и презрения."
        "Внезапно её взор упал на меня и опасно долго задержался."

        show Mom Angry m_evening 00 norm ahead blur with Dissolve(0.3)

        voice "voice/karina/2day/05 Tak ya ne.ogg"
        Mam "Так, я не поняла... Антон, а где очки? Потерял?"

        voice "voice/father/day_2/Da v shkole.ogg"
        Pap "Да в школе, поди, забыл, простофиля."

        "Повисла ядовитая пауза."

        voice "voice/karina/2day/04 Ves.ogg"
        Mam "Весь в тебя."

        play sound "voice/father/day_2/53_otec_serdito_smeril.ogg"

        "Отец сердито смерил маму взглядом, а затем заговорщицки подмигнул мне, напоминая о нашем уговоре."

        stop sound

        voice "voice/father/day_2/Nu nichego.ogg"
        Pap "Ну ничего, есть же запасные — проживем как-нибудь."

        "Родители еще некоторое время стояли в тишине, а затем каждый из них молча побрёл по своим делам, подальше друг от друга."

        play sound "sounds/steps/mam_out.ogg"
        play test_one "sounds/steps/pap_out.ogg"
        show Dad Normal m_night_winter 02 norm aside blur:
            xzoom -1.0
            alpha 1.0
            yoffset 0
            parallel:
                linear 2.0 alpha .00
            parallel:
                linear 0.5 yoffset 20
                linear 0.5 yoffset 0
                repeat
            parallel:
                linear 2.0 xoffset 400

        show Mom Normal m_evening 00 norm aside blur:
            xpos 0
            xoffset -1920 + 650
            xanchor .5
            xalign .5
            yalign 1.
            yoffset 0
            xzoom 1
            yzoom 1
            xzoom -1.0

            alpha 1.0
            yoffset 0
            parallel:
                linear 2.0 alpha .0
            parallel:
                linear 0.5 yoffset 20
                linear 0.5 yoffset 0
                repeat 2
            parallel:
                linear 2.0 xoffset -1920 + 650 -300

        pause 2.0

        "Я ещё не успел раздеться, как ко мне бросилась Оля."

    play test_one "sounds/steps/Olya-steps-5.ogg"

    show Olya Amaze m_evening 00 good ahead 01 blur with Dissolve(0.3)
    $ renpy.pause(0.5)
    show Olya Amaze m_evening 00 good ahead 05 blur with Dissolve(0.3)

    window show

    voice "voice/olya/2day/04 A ya.ogg"
    Oly "А я лису видела!"

    show Olya Amaze m_evening 00 good ahead 01 blur with Dissolve(0.3)

    "В меня словно дробью пальнули."

    show Olya Happy m_evening 00 good ahead 01 blur with Dissolve(0.3)

    "Онемев, я лишь зашевелил губами."


    play test_one "sounds/sfx_cup_breaks.ogg"
    show Cup with Dissolve(0.8)

    "Со звоном разбилась вдребезги чашка."
    "Это мама выпустила её из рук."
    "Её лицо было бледным, она растерянно уставилась на осколки."
    "Эта короткая — в доли секунды — пауза длилась вечность."
    "Потом мама с досадой сказала:"

    hide Cup
    show Olya Amaze m_evening 00 good ahead 05 blur
    with Dissolve(0.8)

    voice "voice/karina/2day/88 To sova to lisa.ogg"
    Mam "То сова, то лиса!"

    voice "voice/karina/2day/89 Kogda zh.ogg"
    Mam "Когда ж тебе надоест?"

    show Olya Amaze m_evening 00 good ahead 05 blur:
        linear 0.1 yoffset 10
        linear 0.1 yoffset 0
        pause 0.2
        linear 0.1 yoffset 10
        linear 0.1 yoffset 0

    voice "voice/olya/2day/05 Pravda-pravda.ogg"
    Oly "Правда-правда!"

    show Olya Amaze m_evening 00 good ahead 01 blur with Dissolve(0.3)
    $ renpy.pause(0.2)
    show Olya Amaze m_evening 00 good ahead 05 blur with Dissolve(0.3)

    voice "voice/olya/2day/06 Takaya.ogg"
    Oly "Такая пушистая!"

    show Olya Amaze m_evening 00 good ahead 01 blur with Dissolve(0.3)
    $ renpy.pause(0.2)
    show Olya Amaze m_evening 00 good ahead 05 blur with Dissolve(0.3)

    voice "voice/olya/2day/07 Ona u zabora.ogg"
    Oly "Она у забора стояла на задних лапах, совсем как человек."

    show Olya Amaze m_evening 00 good ahead 01 blur with Dissolve(0.3)
    $ renpy.pause(0.2)
    show Olya Serious m_evening 03 good ahead blur with Dissolve(0.3)

    voice "voice/olya/2day/08 Ona menya.ogg"
    Oly "Она меня позвала, а тут мама вышла — и лиса убежала."

    show Olya Serious m_evening 02 good ahead blur with Dissolve(0.3)

    voice "voice/karina/2day/90 Ne bilo tam.ogg"
    Mam "Не было там никакой лисы."

    voice "voice/karina/2day/91 Ne vid.ogg"
    Mam "Не выдумывай!"

    voice "voice/anton/2day/212. Ne podhodi k nei.ogg"
    Ant "Не подходи к ней!"

    "Если бы понадобилось, я был готов трясти сестру, как тряпичную куклу."

    show Olya Serious m_evening 03 good ahead blur with Dissolve(0.3)

    voice "voice/olya/2day/09 Ti chego.ogg"
    Oly "Ты чего, Тоша?"

    show Olya Serious m_evening 02 good ahead blur with Dissolve(0.3)

    voice "voice/anton/2day/213. Ne podhodi slish.ogg"
    Ant "Не подходи, слышишь?!"

    play test_one "sounds/steps/mam_in.ogg"

    hide Mom
    show Mom Normal m_evening 01 norm ahead blur at mom_income_left with Dissolve(0.5)

    "Мама вышла в коридор и удивлённо посмотрела на меня."
    "Я стушевался."

    voice "voice/anton/2day/214. Nu lisa ved.ogg"
    Ant "Ну лиса ведь укусить может."

    "Мне вспомнились детские сказки, в которых лисы воровали детей."

    if Flags.Has("day2 fox"):
        "Представил свою Алису, вольную, хищную, бегущую быстро-быстро по ночному лесу с дёргающимся мешком в обнимку."
    else:

        "Представил Алису, вольную, хищную, бегущую быстро-быстро по ночному лесу с дёргающимся мешком в обнимку."

    voice "voice/karina/2day/92 Eto ze.ogg"
    Mam "Это ж была ненастоящая лиса."

    voice "voice/karina/2day/93 Rasskazi.ogg"
    Mam "Расскажи ему, Оль."

    show Olya Serious m_evening 03 good ahead blur with Dissolve(0.3)

    voice "voice/olya/2day/10 Ona na.ogg"
    Oly "Она на двух ногах ходила, а ещё была в платье одета."

    show Olya Serious m_evening 02 good ahead blur with Dissolve(0.3)
    $ renpy.pause(0.2)
    show Olya Serious m_evening 03 good ahead blur with Dissolve(0.3)

    voice "voice/olya/2day/11 Tolko ona.ogg"
    Oly "Только она была взаправду."

    show Olya Serious m_evening 02 good ahead blur
    show Mom Normal m_evening 07 norm ahead blur
    with Dissolve(0.3)

    voice "voice/karina/2day/94 Vidish.ogg"
    Mam "Видишь?"

    "Мама устало улыбнулась, словно это всё объясняло."
    "Я тоже выдавил из себя улыбку."

    play test_one "sounds/steps/mam_out.ogg"

    show Mom Normal m_evening 07 norm ahead blur at mom_reverse_and_out_1eft

    "Жалкую, как тонкий кусочек мыла перед тем, как оно окончательно растает в руках."
    "Но, оставшись наедине с сестрой, я шепнул:"

    voice "voice/anton/2day/215. Eshe raz.ogg"
    Ant "Ещё раз увидишь её — беги."

    stop music fadeout 5
    window hide
    pause 1.0
    play test_one "sounds/steps/Olya_out.ogg"
    hide Olya with Dissolve(.5)
    pause 0.5

    scene black
    show old_movie2_gray
    with Dissolve(1.)
    pause 2.0

    window show


    if not Flags.Has("mask"):
        if Flags.Has("day2 polina"):
            "Воспоминания о семье в омерзительных масках атаковали, бомбардировали меня, будто подлые удары одноклассников."
            "Передо мной стояли поросшие шерстью лица моих близких, оскалившиеся клыкастые пасти, полные густой слюны."
            "Что со мной происходит?"
            "Что за фокусы выкидывает мой разум?"
            "Ведь эта маска зайца настоящая. Вот она, не пойми откуда взявшаяся в моём портфеле, словно и не выкидывал её в том жутком лесу."

        if Flags.Has("day2 fox"):
            "Мысли о лесном чудовище атаковали, бомбардировали меня, будто дождь из конфет и игрушек."
            "Передо мной стояла поросшая шерстью фигура, распрямляющаяся на фоне стволов."
            "Кто он? Что случилось в лесу?"
            "Что со мной происходит?"

    play music "music/39_Dvar - Oramah Elahar.ogg"
    play test_one "voice/anton/2day/216. Tabletki.ogg"

    "Я зажмурился и бросил в рот витамины. Запил их водой."

    hide old_movie2_gray
    show old_movie2_gray:
        alpha 1
        linear 4 alpha 0

    "Хватит сходить с ума. Пожалуйста, хватит."

label bunny2_night_room_anton_table:


    if not Flags.Has("mask"):
        $ story_manager.MarkEvent(("day2", "scene12a"))
        scene homework with Dissolve(.3)

        $ renpy.start_predict("bg_black")
        $ renpy.start_predict("bg_raspisanie")
        $ renpy.start_predict("men_00")
        $ renpy.start_predict("men_01")
        $ renpy.start_predict("men_02")
        $ renpy.start_predict("men_03")
        $ renpy.start_predict("men_04")
        $ renpy.start_predict("men_05")
        $ renpy.start_predict("transition_05")

        "Я кое-как уселся за математику, но задачи не желали решаться."
        "Цифры в тетради то кувыркались и перемешивались, то кружились в танце, то прыгали за поля."
        "От всей этой чехарды голова стала тяжёлой и так и норовила упасть в числовую вязь."
        "К векам словно подвесили маленькие гири — те, что кладут на весы в продуктовом магазине."

        window hide

        play sound "sounds/steps/steps_shool.ogg" loop
        show bg_black:
            alpha 0.0
            linear 2.0 alpha 1.

        show bg_raspisanie:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_00:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_01:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_02:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_03:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_04:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_05:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.

        show transition_05:
            align (.5,.0)
            offset (-32, 100+17)
            zoom .2

            parallel:
                pause 1.
                block:
                    linear .5 yoffset 100+17+10
                    linear .5 yoffset 100+17
                    repeat

            parallel:
                alpha 0.
                linear 3. alpha 1.

                parallel:
                    easeout 4. zoom 1.
                parallel:
                    easeout 4. alpha 0.

        $ renpy.pause(6.0, hard=True)
        stop sound fadeout 3
        window show

        "Стоило мне сдаться и захлопнуть тетрадь, как воспоминания о прожитом дне суматошно заскакали перед глазами."

        $ renpy.stop_predict("bg_black")
        $ renpy.stop_predict("bg_raspisanie")
        $ renpy.stop_predict("men_00")
        $ renpy.stop_predict("men_01")
        $ renpy.stop_predict("men_02")
        $ renpy.stop_predict("men_03")
        $ renpy.stop_predict("men_04")
        $ renpy.stop_predict("men_05")
        $ renpy.stop_predict("transition_05")
    else:

        $ story_manager.MarkEvent(("day2", "scene12b"))
        scene table_art_01 with Dissolve(0.5)

        play test_one "sounds/pen_bumaga.ogg"

        "В пятницу вечером я сидел за уроками."
        "Самое сложное я уже сделал."
        "Оставалось только рисование. Любимый предмет."

        window hide

        call screen day2_album_paint()

        play test_six "sounds/Karandash_01.ogg"

        scene table_art_02 with Dissolve(0.3)

        "Нужно было изобразить какое-нибудь сказочное существо."

        play test_six "sounds/Karandash_02.ogg"
        scene table_art_03 with Dissolve(0.3)
        pause 0.75
        play test_six "sounds/Karandash_01.ogg"
        scene table_art_04 with Dissolve(0.3)
        show miganie_t4_t5
        stop music fadeout 3.5
        play music2 "music/Dvar - Ariil Iaat.ogg" volume 0.9 fadein 2.5

        "Сначала я хотел нарисовать динозавра, вот только кисточка сама потянулась к оранжевой краске."

        play test_one "sounds/lamp.ogg"

        window hide
        show miganie_t6_t7
        $ renpy.pause(4.0)
        scene table_art_06 with Dissolve(0.1)
        $ renpy.pause(0.09)
        scene table_art_07 with Dissolve(0.1):
            zoom 0.48
        window show

        "Мазок за мазком — и на бумаге медленно, по частям, появилась лиса."
        "Будто вылезла из белоснежной бумаги."
        "Встала на задние лапы и хитро заулыбалась."
        "Кисть мазнула, рисуя пушистый хвост. И выпала из ослабевших пальцев."

        show table_art_07:
            xalign 0.682
            yalign 0.48
            zoom 0.48
            subpixel True
            easein 15.0 zoom 1.90
            linear 30.0 zoom 2.70

        $ renpy.start_predict("evening_screamer")

        "Закончив рисунок, я долго и с удивлением разглядывал его, точно не мог понять, откуда же взялся этот рыжий зверь."
        "Чем дольше я смотрел, тем страшнее казалась мне лисья улыбка."
        "Хищная, фальшивая, напоминающая улыбки женщин из журналов для взрослых, какие попадались за стёклами газетных киосков в городе."
        "Манящая улыбка, маскирующая откровенную злобу."
        "А вот глаза лисы получились красными, будто налитыми кровью."
        "Выглядели они совсем как дырки от пуль, какими их показывают в боевиках."
        "Не помню, чтобы рисовал такие глаза."
        "Я отодвинулся от стола, и свет лампы отразился на влажной краске."

        stop music2 fadeout 1.5

        "Рисунок лоснился. Мерещилось, будто лиса следит за мной."
        "И ждёт, чтобы..."

        window hide None
        scene evening_screamer
        show focus_lines
        window show
        $ renpy.stop_predict("evening_screamer")

        voice "voice/father/day_2/55_anton.ogg"
        Pap "Антон!"

        scene room_evning
        show Dad Angry m_evening 01 norm ahead:

            xpos 1100
        with Dissolve(0.5)

        voice "voice/father/day_2/56_ty_ogloh_B.ogg"
        Pap "Ты что, оглох?"

        voice "voice/anton/2day/217. Ya zadumals.ogg"
        Ant "Я-я... задумался."

        play music "music/3_trouble.ogg" fadein 2

        voice "voice/father/day_2/57_tebya_sprashivau.ogg"
        Pap "Тебя спрашиваю, ты сестру не видел?"

        voice "voice/father/day_2/58_opyat_ona_gdeto.ogg"
        Pap "Опять она где-то прячется."

        play test_one "sounds/Chtoto.ogg"

        "Что-то мелькнуло под кроватью, и я замер."

        play test_one "sounds/Chtoto2.ogg"

        "На секунду показалось чумазое личико Оли с приложенным к губам пальцем."

        voice "voice/olya/2day/13 Tss.ogg"
        Oly "Тс-с."

        show Dad Normal m_evening 01 norm aside with Dissolve(0.3)

        voice "voice/father/day_2/59_olya_ya_vizhu.ogg"
        Pap "Оля! Я тебя вижу."

        voice "voice/father/day_2/59_vylezhai.ogg"
        Pap "Вылезай. Ты же в пыли вся!"

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.5)

        play test_one "sounds/Chtoto3.ogg"

        "Оля выползла и, понурив голову, принялась отряхивать колготки."

        voice "voice/father/day_2/60_poydem_ol.ogg"
        Pap "Пойдем, Оль."

        voice "voice/father/day_2/60_ya_tebe_skazky_pochitau.ogg"
        Pap "Я тебе сказку почитаю."

        voice "voice/father/day_2/60_posizhu_s_toboy_poka.ogg"
        Pap "Посижу с тобой, пока не уснёшь."

        show Olya Weeps b_evening 00 good ahead 05 with Dissolve(0.2)

        voice "voice/olya/2day/14 Ya s vami.ogg"
        Oly "Я с вами спать хочу. Не в той комнате."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)
        pause 0.2
        show Olya Weeps b_evening 00 good ahead 05 with Dissolve(0.2)

        voice "voice/olya/2day/15 Tam.ogg"
        Oly "Там..."

        play test_two "sounds/steps/mam_in.ogg"
        show Olya Weeps b_evening 00 good ahead 01
        show Mom Normal m_evening 00 norm aside behind Olya:
            xpos 150
        with Dissolve(0.5)

        "В комнату зашла мама."

        voice "voice/karina/2day/102 Chto opyat.ogg"
        Mam "Что, опять сова?"

        voice "voice/father/day_2/61_a_kto_eshe.ogg"
        Pap "А кто ж ещё?"

        voice "voice/father/day_2/61_ol_ona_ne_pridet.ogg"
        Pap "Оль, она не придёт больше."

        voice "voice/father/day_2/61_ya_ee_prognal.ogg"
        Pap "Я её прогнал."

        "Оля упёрто помотала головой."

        show Olya Weeps b_evening 00 good ahead 06 with Dissolve(0.2)

        voice "voice/olya/2day/Neprognal.1.ogg"
        Oly "Не прогнал."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)
        pause 0.2
        show Olya Weeps b_evening 00 good ahead 06 with Dissolve(0.2)

        voice "voice/olya/2day/Onapridet.2.ogg"
        Oly "Она придёт."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)
        pause 0.2
        show Olya Weeps b_evening 00 good ahead 06 with Dissolve(0.2)

        voice "voice/olya/2day/Ona skazala.3.ogg"
        Oly "Она сказала, что будет каждую ночь приходить."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)

        voice "voice/father/day_2/62_o_tak_ona.ogg"
        Pap "О, так она у тебя говорящая?"

        "Оля проигнорировала вопрос, а потом с новой силой начала:"

        show Olya Weeps b_evening 00 good ahead 05 with Dissolve(0.2)

        voice "voice/olya/2day/Moznoyasva.1.ogg"
        Oly "Можно я с вами посплю?"

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)
        pause 0.2
        show Olya Weeps b_evening 00 good ahead 05 with Dissolve(0.2)

        voice "voice/olya/2day/Mozno.2.ogg"
        Oly "Можно?"

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)
        pause 0.2
        show Olya Weeps b_evening 00 good ahead 05 with Dissolve(0.2)

        voice "voice/olya/2day/Vsamiposledni.3.ogg"
        Oly "В самый последний раз."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)

        play sound "voice/father/day_2/64_kryahtit.ogg"
        show Mom Angry m_evening 00 norm ahead with Dissolve(0.3)

        voice "voice/karina/2day/103 Ty ze govorila.ogg"
        Mam "Ты же говорила, что последний раз был вчера?"

        show Dad Normal m_evening 01 norm ahead with Dissolve(0.3)

        voice "voice/father/day_2/63_olga_ty_yzhe_bolshaya.ogg"
        Pap "Ольга, ты уже большая девочка..."

        voice "voice/anton/2day/Apust.ogg"
        Ant "А пусть у меня ложится!"

        "Мне показалось, что это отличная мысль. Но Оля покачала головой."

        show Olya Weeps b_evening 00 good ahead 04 with Dissolve(0.2)

        voice "voice/olya/2day/18 Net u tebya.ogg"
        Oly "Нет. У тебя не хочу. Она и на тебя смотрит."

        show Olya Weeps b_evening 00 good ahead 01 with Dissolve(0.2)

        "По спине у меня побежали мурашки."

        voice "voice/karina/2day/104 Hvatit.ogg"
        Mam "Хватит!"

        voice "voice/karina/2day/105 Net nikakoy.ogg"
        Mam "Нет никакой совы!"

        voice "voice/karina/2day/105 Ty segodnya.ogg"
        Mam "Ты сегодня спишь у себя, ясно?"

        show Olya Suffer b_evening 00 good ahead 04 with Dissolve(0.3)

        voice "voice/olya/2day/Nupozaluistamam.ogg"
        Oly "Ну пожалуйста, мам!"

        show Olya Suffer b_evening 00 good ahead 01 with Dissolve(0.3)
        pause 0.2
        show Olya Suffer b_evening 00 good ahead 04 with Dissolve(0.3)

        voice "voice/olya/2day/Pozaluista.ogg"
        Oly "Пожалуйста!"

        show Olya Suffer b_evening 00 good ahead 01 with Dissolve(0.3)

        "Мама взяла Олю за руку и попробовала вывести из комнаты."

        voice "voice/karina/2day/106 Poydem milaya.ogg"
        Mam "Пойдем, милая, не мешай брату."

        "Оля свободной рукой вцепилась в спинку моей кровати."

        show Olya Suffer b_evening 00 good ahead 01 with Dissolve(0.3)
        pause 0.2
        show Olya Suffer b_evening 00 good ahead 04 with Dissolve(0.3)

        voice "voice/olya/2day/PozaluistaPozaluista.ogg"
        Oly "Пожалуйста! Пожалуйста! Пожалуйста!"

        show Olya Suffer b_evening 00 good ahead 01 with Dissolve(0.3)
        pause 0.2
        show Olya Suffer b_evening 00 good ahead 04 with Dissolve(0.3)

        voice "voice/olya/2day/Nehochyknei.ogg"
        Oly "Не хочу к ней!"

        show Olya Suffer b_evening 00 good ahead 01 with Dissolve(0.3)
        play test_one "sounds/Skrip2.ogg"

        "Мама потянула Олю к себе, но та не поддавалась, и только спинка кровати жалобно скрипела."

        play test_two "sounds/steps/mam_out.ogg"
        hide Mom with Dissolve(0.5)
        play test_three "voice/father/day_2/Nununu.ogg"
        play test_one "sounds/Skrip3.ogg"

        "Тогда подошёл отец, подхватил Олю и понёс, не обращая внимания на протесты и крики."

        play test_one "sounds/steps/pap_out.ogg"
        hide Olya
        hide Dad
        with Dissolve(0.5)

        $ music_during_lines = 1.0
        voice "voice/olya/2day/Nenado.ogg"
        Oly "Не надо!"

        voice "voice/olya/2day/Nenadoknei.ogg"
        Oly "Не надо к ней!"

        voice "voice/olya/2day/Onaopyatsmotret.ogg"
        Oly "Она опять смотреть будет!"

        play sound "voice/olya/2day/Mamochka.ogg"

        "Я ещё долго слушал, как сестрёнку пытаются уложить."

        scene room_night with Dissolve(1.0)

        "В конце концов родители сдались и опять разрешили ей лечь с ними."
        "В самый-самый-самый последний раз."

        stop sound fadeout 1
        stop music fadeout 3

        "Когда всё стихло, я лежал в темноте и думал об Олиных словах:"

        voice "voice/olya/2day/Ona.ogg"
        "«Она и на тебя смотрит»."

        "Было не по себе."
        "Лишь задернув шторы на окне, я сумел успокоиться."
        "Но стоило мне сомкнуть веки, как воспоминания прожитого дня суматошно запрыгали перед глазами."

        window hide

        show bg_black:
            alpha 0.0
            linear 2.0 alpha 1.

        pause 3

        show bg_raspisanie:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_00:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_01:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_02:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_03:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_04:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        show men_05:
            alpha 0.0
            pause 3
            linear 3.0 alpha 1.
        play sound "sounds/steps/steps_shool.ogg" loop
        show transition_05:
            align (.5,.0)
            offset (-32, 100+17)
            zoom .2

            parallel:
                pause 1.
                block:
                    linear .5 yoffset 100+17+10
                    linear .5 yoffset 100+17
                    repeat

            parallel:
                alpha 0.
                linear 3. alpha 1.

                parallel:
                    easeout 4. zoom 1.
                parallel:
                    easeout 4. alpha 0.

        $ renpy.pause(6.0, hard=True)



    label day2_nightmare:
    $ story_manager.MarkEvent(("day2", "scene13"))

    stop music fadeout 3.5
    window show
    stop sound fadeout 3

    "Вот снова я посреди душных школьных коридоров."

    scene bg koridorchic_mor_full:
        xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05
    with Dissolve(2.0)

    play music2 "music/Kaite1.ogg" volume 0.7 fadein 2
    window show

    "Отсюда виден кабинет литературы: лица мёртвых классиков на портретах, строгая и царственная поза классной руководительницы Лилии Павловны."
    "А за тем углом ждёт не дождётся её ненаглядная дочка Катя, ябеда и сплетница."

    play test_one "sounds/steps/Kait_stop.ogg"

    show Kate Kawai m_day 00 good ahead 02:
        yoffset 100
    with Dissolve(0.5)

    $ music_during_lines = 0.75
    voice "voice/kate/15 KA.ogg"
    Kate "Эй, новенький! Новенький!"

    show Kate Kawai m_day good 00 ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/219. Chego tebe.ogg"
    Ant "Чего тебе, Кать?"

    "Она закачалась на носочках, спрятав за спиной руки, и с фальшивой улыбкой поинтересовалась:"

    show Kate Kawai m_day 00 good ahead 02 with Dissolve(0.3)

    voice "voice/kate/16 KA.ogg"
    Kate "Скажи, пожалуйста, а чего это тебя к нам перевели, а?"

    show Kate Kawai m_day good 00 ahead 01 with Dissolve(0.3)

    "Может быть, я сказал бы правду Полине."
    "Но Катька продаст мою правду на рынке за три копейки – то же самое, что распечатать мои мысли на принтере и повесить рядом с фотографией Вовы, чтобы все читали."
    "Я вновь обратился к заученному ответу:"

    voice "voice/anton/2day/220 Eto vse.ogg"
    Ant "Это всё из-за моих родителей..."

    voice "voice/anton/2day/220.2 U papi.ogg"
    Ant "У папы тут новая работа, а мама... мама..."

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.3)

    "Но Катя даже не думала меня слушать, метнулась к навострённым ушам подружек, зашептала, косясь на меня и хихикая."

    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.3)

    voice "voice/kate/17 KA.ogg"
    Kate "Да-да! Конечно-конечно!"

    voice "voice/kate/18 KA.ogg"
    Kate "Он нас тут совсем за дурачков держит."

    voice "voice/kate/19 KA.ogg"
    Kate "Я вот слыхала, что это всё из-за его отца."

    voice "voice/kate/20 KA.ogg"
    Kate "Он недавно какому-то крутому дорогу перешёл, и теперь они всей своей семейкой в нашем захолустье скрываются."

    voice "voice/anton/2day/221. Nepravda.ogg"
    Ant "Неправда! Ты всё врёшь!"

    if Flags.Has("day2 fox"):
        show Kate Block m_day 00 evil ahead 02 with Dissolve(0.3)
        stop music2 fadeout 0.5

        voice "voice/kate/21 KA.ogg"
        Kate "А слышали-слышали, как он Бабурина просто так стукнул?!"

        play music "music/SilentWhispering.ogg" volume 0.7 fadein 2

        voice "voice/kate/22 KA.ogg"
        Kate "Это каким надо быть уродом, чтобы в первый же день так над одноклассником измываться?!"

        voice "voice/anton/2day/222. Prekrati on perviy.ogg"
        Ant "Прекрати! Ты же знаешь — он первый начал!"
    else:

        stop music2 fadeout 0.5
        show Kate Normal m_day 00 evil ahead 02 with Dissolve(0.3)

        voice "voice/kate/23 KA.ogg"
        Kate "А слышали, слышали, как ему Бабурин всыпал?!"

        $ SetParSpeed(30)
        show bg_class_for_child1:
            alpha 0.0
            ease 2.0 alpha 1.0

        show bg_class_for_child2:
            alpha 0.0
            ease 2.0 alpha 1.0

        show children_in_class:
            alpha 0.0
            ease 2.0 alpha 1.0

        play music "music/SilentWhispering.ogg" volume 0.7 fadein 2

        voice "voice/kate/24 KA.ogg"
        Kate "А этот лишь ручки опустил да глазёнки потупил."

        voice "voice/anton/2day/223. Prekrati ne odin.ogg"
        Ant "Прекрати! Ты знаешь - он не один был!"

    voice "voice/kate/25 KA.ogg"
    Kate "И будто этого мало..."



    if Flags.Has("day2 fox"):
        if Flags.Has("mask"):
            voice "voice/kate/32 KA.ogg"
            Kate "Ходят слухи, что этот чудик повсюду таскает с собой заячью маску."

            voice "voice/kate/33 KA.ogg"
            Kate "Ой, девочки, ну кто же в своём уме будет такое делать?"

            voice "voice/kate/34 KA.ogg"
            Kate "Ясно-понятно, со странностями наш Антошка."

            voice "voice/kate/35 KA.ogg"
            Kate "Может слабоумный, а может..."

            voice "voice/kate/36 KA.ogg"
            Kate "...и маньяк!"

            voice "voice/kate/38 KA.ogg"
            Kate "Если в его в портфеле хорошо покопаться, там и топор отыскать можно, а может что и похуже."
        else:

            voice "voice/kate/26 KA.ogg"
            Kate "Ходят слухи, что он спутался с ворюгами из шайки Ромки Пятифана."

            voice "voice/kate/27 KA.ogg"
            Kate "Ой, девочки, сумки проверяйте!"

            voice "voice/kate/28 KA.ogg"
            Kate "Того и гляди в гардеробе вещи начнут пропадать."

            voice "voice/kate/29 KA.ogg"
            Kate "Будем знать — это Петров с дружками постарался."
    else:

        voice "voice/kate/32 KA.ogg"
        Kate "Ходят слухи, что этот чудик повсюду таскает с собой заячью маску."

        voice "voice/kate/33 KA.ogg"
        Kate "Ой, девочки, ну кто же в своём уме будет такое делать?"

        voice "voice/kate/34 KA.ogg"
        Kate "Ясно-понятно, со странностями наш Антошка."

        voice "voice/kate/35 KA.ogg"
        Kate "Может слабоумный, а может..."

        voice "voice/kate/36 KA.ogg"
        Kate "...и маньяк!"

        voice "voice/kate/38 KA.ogg"
        Kate "Если в его в портфеле хорошо покопаться, там и топор отыскать можно, а может что и похуже."

    hide bg koridorchic_mor_full
    scene bg koridorchic_mor_full:
        xpos 0
    show layer master:
        align (.5, .5)
        zoom 1.05
    show Kate Kawai m_day evil 00 ahead 02:
        yoffset 100
        linear 0.2 yoffset 130
        linear 0.2 yoffset 100

        linear 0.2 yoffset 130
        linear 0.2 yoffset 100


    voice "voice/kate/30 KA.ogg"
    Kate "Да-да-да!"

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.3)

    voice "voice/anton/2day/224. Zamolchi.ogg"
    Ant "Замолчи! Заткнись!"


    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)
    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.2)

    voice "voice/kate/39 KA.ogg"
    Kate "Вон как раскричался-то! Будто ужаленный!"

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)
    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.2)

    voice "voice/kate/40 KA.ogg"
    Kate "А зрачки-то, зрачки какие широкие!"

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)
    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.2)

    voice "voice/kate/41 KA.ogg"
    Kate "Опять, чего доброго, с катушек слетит и руки распускать начнёт."

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)
    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.2)

    voice "voice/kate/42 KA.ogg"
    Kate "Не зря же мать его таблетками пичкает."

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)

    "Я замер в смятении, безуспешно пытаясь понять, откуда она знает про лекарство. И что пугало сильнее: вдруг в её болтовне кроется ужасающая правда?"

    show Kate Normal m_day 00 evil ahead 02:
        yoffset 100
        linear 0.2 yoffset 130
        linear 0.2 yoffset 100

        linear 0.2 yoffset 130
        linear 0.2 yoffset 100
    with Dissolve(0.3)

    voice "voice/kate/43 KA.ogg"
    Kate "Да-да!"

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.2)
    show Kate Kawai m_day evil 00 ahead 02 with Dissolve(0.2)

    voice "voice/kate/44 KA.ogg"
    Kate "Он такой же ненормальный, как и его сестрица."

    voice "voice/kate/45 KA.ogg"
    Kate "Представляете, к этой сумасшедшей дурочке каждую ночь прилетает сова ростом с человека!"

    show Kate Kawai m_day evil 00 ahead 02:
        yoffset 100
        linear 0.2 yoffset 130
        linear 0.2 yoffset 100

        linear 0.2 yoffset 130
        linear 0.2 yoffset 100
    with Dissolve(0.3)

    voice "voice/kate/46 KA.ogg"
    Kate "Да-да!"

    voice "voice/kate/47 KA.ogg"
    Kate "Только что-то её никто из здоровых людей не видел."

    voice "voice/kate/48 KA.ogg"
    Kate "А этот наивный простак ей верит."

    voice "voice/kate/49 KA.ogg"
    Kate "Нет, ну вы представляете?!"

    show Kate Kawai m_day evil 00 ahead 01 with Dissolve(0.3)

    "И тут среди ухмыляющейся толпы я поймал единственный сочувствующий взгляд."

    if Flags.Has("day2 fox"):
        show Polina Front m_day 03 sad ahead 02:
            yoffset 100
            xpos -350
        with Dissolve(0.5)

        voice "voice/Polina/2day/45 Pravda.ogg"
        Pol "Это правда, Антон?"
    else:

        show Polina Front m_day 03 sad ahead 02:
            yoffset 100
            xpos -350
        with Dissolve(0.5)

        voice "voice/Polina/2day/50 Kak ze tak.ogg"
        Pol "Как же так, Антон?"

    show Polina Front m_day 03 sad ahead 03 with Dissolve(0.2)
    show Polina Front m_day 03 sad ahead 02 with Dissolve(0.2)

    voice "voice/Polina/2day/46 Neuzeli.ogg"
    Pol "Неужели действительно? Тебе нездоровится?"

    show Polina Front m_day 03 sad ahead 03 with Dissolve(0.3)

    voice "voice/anton/2day/225. Polina poslush.ogg"
    Ant "Полина... Послушай меня!"

    show Kate Block m_day 00 evil ahead 02 with Dissolve(.3)

    voice "voice/kate/50 KA.ogg"
    Kate "Как же, как же!"

    show Polina Front m_day 02 sad ahead 03
    show Kate Block m_day 00 good ahead 02
    with Dissolve(.3)

    voice "voice/kate/51 KA.ogg"
    Kate "Не слушай этого болтуна, Полиночка!"

    if Flags.Has("day2 fox"):
        voice "voice/kate/52 KA.ogg"
        Kate "Ты ещё не знаешь..."

        voice "voice/kate/53 KA.ogg"
        Kate "Он тебя на другую променял! Не из нашей школы."

        voice "voice/kate/54 KA.ogg"
        Kate "На А-ли-су."

    if Flags.Has("day2 polina"):
        voice "voice/kate/61 KA.ogg"
        Kate "Свистит он, что в Москве бывал, как пить дать."

    if not Flags.Has("day2 fox"):
        voice "voice/kate/57 KA.ogg"
        Kate "Это ничтожество даже постоять за себя не может..."

        voice "voice/kate/58 KA.ogg"
        Kate "А при случае и за тебя не заступится."

        stop music2 fadeout 1.5
        stop music fadeout 1.5

        voice "voice/kate/59 KA.ogg"
        Kate "Бросит, думая только как бы самому по шее не схлопотать."

        play music "music/some_ambient.ogg" fadein 4

        $ music_during_lines = 1.0
        voice "voice/kate/60 KA.ogg"
        Kate "Сла-бак."

    show Polina Cry m_day 01 fine ahead 01 with Dissolve(0.3)

    play sound "voice/Polina/2day/152 polina sogn.ogg"

    "Полина согнулась, будто её пнули в живот, а потом залилась слезами и громко, истерично плача, рухнула на грязный пол."

    stop sound fadeout 0.5
    show Polina Cry m_day 01 fine ahead 02 with Dissolve(0.3)

    voice "voice/Polina/2day/153 net.ogg"
    Pol "Не-е-е-е-ет! Нет!!!"

    show Polina Cry m_day 01 fine ahead 01 with Dissolve(0.2)
    show Polina Cry m_day 01 fine ahead 02 with Dissolve(0.2)

    if Flags.Has("day2 fox"):
        voice "voice/Polina/2day/153  pochemu ona.ogg"
        Pol "Почему она, Антон?! Почему-у-у?!"
    else:

        voice "voice/Polina/2day/159 Anton.ogg"
        Pol "Анто-о-он! Почему? За что?!"

    show Polina Cry m_day 01 fine ahead 01 with Dissolve(0.3)

    "Ничего не понимая, я бросился к Полине, но Катя грубо оттолкнула меня."

    show Kate Scream m_day 00 evil ahead with Dissolve(.3)

    voice "voice/kate/62 KA.ogg"
    Kate "Убери от неё свои лапы, чудовище!" with vpunch

    show fist_0 with Dissolve(1.)

    "Под пеленой страха зрела ярость."

    show fist_loop
    play test_one "sounds/sfx_clench_fist.ogg"

    "Медленно всплывала из клубящегося морока."
    "Я почувствовал, как моя верхняя губа ползёт к дёснам, оголяя зубы."

    voice "voice/kate/63 KA.ogg"
    Kate "То, что твой отец бьёт мать, ещё не дает тебе права поднимать руку на девушку!"

    "Кулаки стали кувалдами – не разжать!"

    play test_one "sounds/sfx_clench_fist.ogg"

    "Никто не смеет говорить такое про мою семью!"

    hide bg koridorchic_mor_full
    scene bg koridorchic_mor_full:
        anchor (.25,1.)
        xpos 960
        ypos 1.
        easein .5 zoom 1.1
    show Kate Normal m_day 00 evil ahead 01:
        yoffset 100
        align (.5,1.)
        easein .5 zoom 1.15
    play sound "voice/anton/2day/Yavzdrognuliostanovils.ogg"

    "Я опомнился, когда уже кинулся на злобную Катьку."

    show Kate Normal m_day 00 evil ahead 02 with Dissolve(.3)
    stop music fadeout 1

    voice "voice/kate/64 KA.ogg"
    Kate "Ага! Слетел-таки! Слетел!.."

    show Kate Normal b_day 00 good ahead 02 with Dissolve(.3)

    voice "voice/kate/65 KA.ogg"
    Kate "Спасите! Помогите! Петров с катушек слетел!"

    scene nightmare_klass0
    show nightmare_klass2:
        yalign 0.
    with Dissolve(1.)

    play music2 "sounds/Anton's nightmare(without).ogg"
    stop music fadeout 2

    "Тут же толпа школьников вокруг неё зашумела, разразилась свистом и гневным рыком."

    hide nightmare_klass2
    show nightmare_klass2:
        subpixel True

        parallel:
            linear 12 yalign 1.

        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show ef_scrap:
        alpha 0.
        pause 4.
        alpha 1.

    show bg_black:
        alpha 0.
        pause 4.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat

    play test_one "sounds/sfx_trees_transform.ogg"

    "И стала расти."
    "Субтильные фигурки учеников увеличивались, ширились, тянулись вверх, всё выше и выше, под самый потолок."
    "Превращались в огромный чёрный лес, кишащий оскаленными мордами."

    window hide

    pause 2

    hide nightmare_klass2
    hide ef_scrap
    hide bg_black

    show nightmare_klass2:
        yalign 1.

        block:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat
    show ef_scrap
    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat


    show bg_black as black2:
        alpha 0
        linear 2. alpha 1

    "Я сжался до пушистого комочка, затрясся перед могуществом изрытых язвами стволов – не то людей, не то деревьев."

    show nightmare_kate1:
        alpha 0
        align (.5, 0.)
        zoom .6
        parallel:
            linear 1.5 alpha 1
        parallel:
            linear 1.5 zoom .8
        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    hide bg_black
    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat

    voice "voice/kate/66 KA.ogg"
    Kate "Вот ты и показал своё животное нутро!"

    hide nightmare_kate1
    show nightmare_kate2:
        align (.5,.0)
        block:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat
    hide bg_black
    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat

    voice "voice/kate/67 KA.ogg"
    Kate "Трус!"

    "Катино лицо было обезображено ликованием и восторгом."

    hide nightmare_kate2
    show nightmare_kate2 behind bg_black:
        align (.5,.0)
        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat
        parallel:
            linear 1.5 alpha 0
    show Polina Scream b_day 01 cry ahead 04 behind bg_black:
        align (.5,.0)
        alpha 0
        1.5
        linear 2. alpha 1

    $ music_during_lines = 0.75
    voice "voice/Polina/2day/51 Anton.ogg"
    Pol "Анто-о-он!"

    if Flags.Has("day2 fox"):
        voice "voice/Polina/2day/157  pochemu ona_net.ogg"
        Pol "Почему она? Нет!!!"

        voice "voice/Polina/2day/158 Chem ona.ogg"
        Pol "Чем она лучше меня?!"
    else:

        voice "voice/Polina/2day/155 Pochemu.ogg"
        Pol "Почему? Нет!!!"

        voice "voice/Polina/2day/156 Zachto.ogg"
        Pol "За что?!"

    show bunny_nightmare_bg:
        alpha 0.0
        linear 2 alpha 1.0

    show bunny_nightmare_mask:
        ypos 1.
        yanchor 0.
        xalign .5
        parallel:
            linear 3 yalign .5
        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bunny_nightmare_nose:
        ypos 1.
        yanchor 0.
        xalign .5
        parallel:
            linear 3 yalign .5
        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat
    play sound "voice/Polina/2day/153 Zalivalas.ogg"

    "— заливалась слезами несчастная Полина."

    stop sound fadeout 1

    $ music_during_lines = 1.0
    voice "voice/kate/68 KA.ogg"
    Kate "Он!"

    hide bunny_nightmare_mask
    hide bunny_nightmare_nose
    hide bunny_nightmare_bg
    hide bg_black

    show bunny_nightmare_bg:
        align (.5,.5)

    show bunny_nightmare_mask:
        align (.5,.5)
        block:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bunny_nightmare_nose:
        align (.5,.5)
        block:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat

    voice "voice/kate/69 KA.ogg"
    Kate "Животное!"

    hide bunny_nightmare_mask
    hide bunny_nightmare_nose
    hide bunny_nightmare_bg
    hide bg_black

    show bunny_nightmare_bg:
        align (.5,.5)
        parallel:
            linear .4 zoom 1.0125
            linear .1 zoom 1.01
            linear .2 zoom 1.017
            linear .1 zoom 1.00

        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bunny_nightmare_mask:
        align (.5,.5)
        parallel:
            linear .4 zoom 1.075
            linear .1 zoom 1.06
            linear .2 zoom 1.155
            linear .1 zoom 1.00

        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bunny_nightmare_nose:
        align (.5,.5)
        parallel:
            linear .4 zoom 1.075
            linear .1 zoom 1.06
            linear .2 zoom 1.155
            linear .1 zoom 1.00

        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    show bg_black:
        alpha 0.
        block:
            linear .05 alpha 0.35
            linear .05 alpha 0.
            repeat

    voice "voice/kate/70 KA.ogg"
    Kate "Чужак!"

    window hide

    hide bg_black
    show bg_black:
        alpha 0.
        linear 3 alpha 1

    $ renpy.start_predict("nightmare_animation1")

    $ renpy.pause(delay=3.0, hard=True)

    scene nightmare_animation_0
    with Dissolve(1.5)
    show nightmare_animation

    queue sound [ "<silence 1.8>", "<from 0 to 2>sounds/sfx_bunny_scream.ogg"]
    $ renpy.pause(delay=3, hard=True)

    $ renpy.stop_predict("nightmare_animation1")
    $ renpy.start_predict("Ant_wakeup")

    play wtf "sounds/flapping-1.ogg"

    "Из леса донеслось пугающее хлопанье крыльев."
    "Два огромных белых уха спустились откуда-то сверху, и я с головой зарылся в них."

    $ music_during_lines = 0.75
    voice "voice/Polina/2day/148 Dva ogromnih.ogg"
    Pol "Антон! Антон!"

    voice "voice/kate/71 KA.ogg"
    Kate "Пожалуйста!"

    voice "voice/olya/2day/24 Vstavai.ogg"
    Oly "Вставай!"


    $ story_manager.MarkEvent(("day2", "scene14"))

    play test_three "sounds/sfx_bed_squeaks_2.ogg"
    scene Ant_wakeup
    pause 2
    $ renpy.stop_predict("Ant_wakeup")
    stop music2 fadeout 4

    "Я подскочил, чуть не упав с кровати."

    show bg_black:
        alpha 0
        linear 3 alpha 1

    show shtora_0 blur:
        alpha 0
        pause 3
        linear 3 alpha 1

    play music "music/8_Peredyshka.ogg" fadein 3

    "Оказалось, я несколько часов метался по мокрой от пота постели."
    "Олин крик вырвал, вызволил из щупалец кошмара."

    $ music_during_lines = 0.9
    voice "voice/olya/2day/25 Anton.ogg"
    Oly "Анто-о-о-н!"

    voice "voice/olya/2day/27 Pls.ogg"
    Oly "Пожалуйста..."

    voice "voice/olya/2day/24 Vstavai_vstavai.ogg"
    Oly "Вставай... Вставай!"

    "Я не сразу разглядел её силуэт у окна."
    "Голос Оли был глухим – после драки у меня звенело в голове."
    "Звук искажался. Будто уши закупорили ватой."
    "Всхлипывая, расстроенная, как никогда прежде, сестрёнка повторяла и повторяла:"

    voice "voice/olya/2day/28 Sova.ogg"
    Oly "Сова! Сова!"

    voice "voice/olya/2day/29 Pls2.ogg"
    Oly "Пожалуйста..."

    voice "voice/olya/2day/30 Ya bouys.ogg"
    Oly "Я бою-у-у-ухусь!"

    scene bg_room_night1 with Dissolve(.5)

    "Её слёзы кипятком ошпаривали мне сердце, но, признаться, я почти благодарил сову за визит."
    "За то, что напуганная Оля разбудила меня."

    voice "voice/anton/2day/227. Olya ya.ogg"
    Ant "Оля, я сейчас..."

    $ add_text_to_dictionary(26)

    voice "voice/anton/2day/228. Hochesh Murzilku.ogg"
    Ant "Хочешь, я тебе {u}«Мурзилку»{/u} почитаю?"

    voice "voice/anton/2day/229. Podozdi.ogg"
    Ant "Подожди..."

    play sound "sounds/Posaril.ogg"

    "Я опустил босые пятки на холодный пол."
    "Пошарил в поисках очков."

    play sound "voice/anton/2day/230. Vsdoh.ogg"

    "Вспомнил Семёна, его подлый поступок, и горестно вздохнул."

    show shtora_0 with Dissolve(.5)

    voice "voice/olya/2day/31 Anton.ogg"
    Oly "Антон."

    voice "voice/olya/2day/31 Pls pls.ogg"
    Oly "Пожалуйста... Пожалуйста!"

    voice "voice/olya/2day/32 Posmotri.ogg"
    Oly "Посмотри!"

    "Она не отводила глаз от окна, словно боялась проиграть ему в гляделки."

    play test_one "sounds/sfx_light_switch.ogg"
    show shtora_1

    "Я нащупал переключатель — лампа плеснула ослепляющим светом."

    play test_one "sounds/bed.ogg"

    "Встал с кровати."
    "Зрение обманывало, то приближая ко мне окно, то отдаляя."

    show day2_siluet_room:
        xalign .0
    with Dissolve(.5)

    stop music fadeout 5

    "Сестра была размытым пятном впереди."

    hide day2_siluet_room
    show day2_siluet_room:
        xalign .0
        linear 2 xalign 1.

    queue sound [ "<silence 1.0>", "<from 0 to 2>sounds/steps/Anton-steps-steal-0.ogg"]


    "Я сделал осторожный шаг."

    voice "voice/anton/2day/231 Ol.ogg"
    Ant "Оль..."

    voice "voice/anton/2day/231.2 Chto tam.ogg"
    Ant "Что там?"

    voice "voice/anton/2day/232 Chto-to sluch.ogg"
    Ant "Что-то случилось?"

    voice "voice/anton/2day/232.2 Ti hochshesh.ogg"
    Ant "Ты хочешь, чтобы я открыл шторы?"

    voice "voice/olya/2day/33 Net pls.ogg"
    Oly "Нет! Не надо!"

    voice "voice/olya/2day/34 Tam ze.ogg"
    Oly "Там же сова!"

    play test_six "sounds/hum-1.1.ogg" loop

    "Голос доносился из-за моей спины."

    $ move_back = .60

    hide day2_siluet_room
    show day2_siluet_room:
        xalign 1.
        linear 1. xalign move_back
    show day2_door6_overlay:
        xalign 1.

        parallel:
            linear 1. xalign move_back



    play test_five "sounds/gong-noise-2.ogg"

    "Я обернулся и оцепенел от ужаса."
    "В дверном проёме стояла зарёванная Оля."

    voice "voice/olya/2day/35 S kem.ogg"
    Oly "С кем..."

    play test_one "sounds/steps/Olya-steps-3.ogg"
    hide day2_door6_overlay
    show day2_door5_overlay:
        xalign move_back
    show Olya Weeps m_evening 00 good ahead 01
    with Dissolve(.5)

    voice "voice/olya/2day/36 S kem ti.ogg"
    Oly "С кем ты разговаривал, братик?"

    show Olya Weeps m_evening 00 good ahead 00 with Dissolve(.2)

    "Обхватив плечи, она таращилась на меня красными от слёз глазами, спрашивала, но будто боялась услышать ответ."

    hide day2_siluet_room
    show day2_siluet_room:
        xalign move_back
        linear 1. xalign 1.
    hide day2_door5_overlay
    show day2_door5_overlay:
        xalign move_back
        linear 1. xalign 1.
    hide Olya Weeps m_evening 00 good ahead 00
    show Olya Weeps m_evening 00 good ahead 00:
        xalign .5
        linear 1. xoffset -340

    play test_four "sounds/cymb-roll-3.ogg"

    voice "voice/anton/2day/234. Ya razgovarival.ogg"
    Ant "Я разговаривал с тобой... с тем, кто притворился тобой..."

    hide shtora_1
    show shtora_1
    play test_one "sounds/sfx_wooden_creak.ogg"

    "За окном угрожающе скрипнул карниз, словно на нём сидел кто-то тяжёлый."

    play music2 "music/Hor.ogg" fadein 1
    play test_two "sounds/sfx_Olya_transforms.ogg"
    scene shtora_2 with Dissolve(2.)
    stop test_six fadeout 3

    "А то, что выдавало себя за Олю, начало расползаться, менять свои очертания, увеличиваться в свете ненасытной луны до пугающих размеров."

    $ music_during_lines = 0.7
    voice "voice/Owl/Owl_2day/02 Anton.ogg"
    Noname "Антон!"

    voice "voice/Owl/Owl_2day/04 Pozalsta.ogg"
    Noname "Пожалуйста..."

    voice "voice/Owl/Owl_2day/05 Podoidi.ogg"
    Noname "Подойди ко мне... Подойди-и-и-и-и!"

    "Голос больше не принадлежал сестре."
    "Тому, кто прятался за шторой, надоело притворяться, водить меня за нос."
    "Я больно ущипнул себя в надежде, что силуэт у окна – лишь продолжение ночного кошмара, галлюцинация проклятого дома, ведь они не кусаются."
    "Фигура высилась передо мной в дымке..."
    "Я услышал громкий вскрик Оли, когда по стеклу постучали."

    play test_one "sounds/stuk-v-okno_001.ogg"
    scene shtora_2:
        align (.5,.5)

        zoom 1.1
        .15
        zoom 1.0
    play test_two "voice/olya/2day/37 Tuk1.ogg"

    "Тук-тук!"

    voice "voice/olya/2day/38 Ona prishla.ogg"
    Oly "Она пришла за нами!"

    play test_one "sounds/stuk-v-okno_002.ogg"
    scene shtora_2:
        align (.5,.5)
        0.1
        zoom 1.1
        .3
        zoom 1.0

    "Стук повторился, и я отшатнулся вглубь комнаты."
    "Словно на свете существовали потайные углы, где я мог бы схорониться от этой жути."

    play test_one "sounds/stuk-v-okno_003.ogg"

    scene shtora_2:
        align (.5,.5)
        zoom 1.1
        .1
        zoom 1.0

    "Тук-тук!"
    "Стучали чем-то острым, железным."
    "Замерцала лампа светильника, ярко озарила комнату и погасла, как свеча на яростном ветру, — нить накаливания лопнула со звоном."

    play test_one "sounds/sfx_bulb_burst.ogg"
    scene shtora_3
    show shtora_flash
    pause 0.7
    play sound "voice/olya/2day/37 Mrak.ogg"
    $ renpy.pause(3, hard=True)

    "Мрак, словно только того и ждал, хлынул из углов и сомкнулся."
    "От всей вселенной осталось лишь окно: снаружи светила луна и красила всё в цвет костей, извлечённых из склепа."
    play test_two "voice/olya/2day/37 Tuk3.ogg"
    "В черноте Оля завизжала, ткнулась в мою спину, ища защиты."

    show kovai:
        align (.5,.5)
        zoom .5
        alpha 0
        linear 2. alpha 1
    "И тут на нас уставился горящий прожорливым огнём глаз."

    play test_one "sounds/stuk-v-okno_004.ogg"

    show kovai:
        align (.5,.5)
        zoom .5
        0.1
        zoom .5*1.1
        0.15
        zoom .5*1.0
        0.5
        zoom .5*1.1
        0.25
        zoom .5*1.2
        0.25
        zoom .5*1.0

    "Тук-тук! Тук! Тук-тук!"
    "Нет, оно не пыталось разбить окно. Оно играло."

    "Стучало и стучало, сводя нас с ума."

    play test_one "sounds/stuk-v-okno_005.ogg"
    play sound "voice/olya/2day/37 Tuk2.ogg"

    show kovai:
        align (.5,.5)
        zoom .5
        0.1
        zoom .5*1.1
        0.2
        zoom .5*1.2
        0.25
        zoom .5*1.0
        0.5
        zoom .5*1.1
        0.25
        zoom .5*1.0

    "Тук-тук! Тук! Тук-тук!"

    play test_two "sounds/stuk-v-okno_005.ogg" loop

    show kovai:
        align (.5,.5)
        zoom .5
        block:
            0.05
            zoom .5*1.1
            0.2
            zoom .5*1.2
            0.25
            zoom .5*1.0
            0.5
            zoom .5*1.1
            0.25
            zoom .5*1.0
            0.5
            repeat

    "Будто гигантские часы мерили отведённое нам время, и маятник раскачивался над бездной."

    stop test_two fadeout 0.5
    show kovai:
        align (.5,.5)
        zoom .5

    voice "voice/olya/2day/39 Uhodi.ogg"
    Oly "Уходи! Убирайся! Пошла прочь!"

    "Оля истошно кричала, клещами вцепившись мне в руку."

    voice "voice/Owl/Owl_2day/06 Anton.ogg"
    Noname "Антон! Антон!"

    voice "voice/Owl/Owl_2day/07 Podoidi.ogg"
    Noname "Подойди!"

    hide kovai
    show kovai:
        align (.5,.5)
        zoom .5
        linear 15. zoom .8

    "Я с трудом различил два огромных крыла, раскрывшихся над чёрным пятном."

    voice "voice/olya/2day/40 Skazi.ogg"
    Oly "Скажи ей, Антон!"

    voice "voice/olya/2day/41 Skazi chto.ogg"
    Oly "Скажи, что я больше не буду себя плохо вести!"

    voice "voice/olya/2day/42 Nikogda.ogg"
    Oly "Никогда!"

    voice "voice/olya/2day/43 Tolko pust.ogg"
    Oly "Только пусть она уйдет!"

    voice "voice/olya/2day/44 Pls.ogg"
    Oly "Пожалуйста!.."

    $ music_during_lines = 1.0
    show kovai2:
        align (.5,.5)
        zoom .8
    with Dissolve(1.)

    "Лунный свет вдруг померк, погрузив комнату во тьму, и светящийся глаз скрылся."
    "Я проглотил застрявший в горле ком — будто репейник сглотнул."

    hide kovai2
    play test_two "sounds/steps/Anton-steps-steal-0.ogg"
    show kovai2:
        align (.5,.5)
        parallel:
            zoom .8
            linear 1. zoom .87
            linear .25 zoom .95
        parallel:
            linear 1. yoffset -50
            linear .25 yoffset 0

    "Шагнул к шторам, заворожённый призывом безобразного гостя."

    play sound "voice/olya/2day/45 Ne budu.ogg"

    "Оля бормотала позади: «Не буду, не буду, не буду!»"
    "Блёклое окно наползало на меня. Занавески шуршали."

    stop sound fadeout 2
    hide kovai2
    show kovai2:
        align (.5,.5)
        parallel:
            zoom .95
            linear 1. zoom 1.

    "Я потянулся, чтобы отодвинуть штору, чтобы посмотреть в глаза страху."
    play test_two "sounds/sfx_distant_door_slam.ogg"
    "И в этот момент из родительской спальни донёсся шум."
    "Недолго думая, я рывком отдёрнул штору."

    play test_seven "sounds/cymb-echo-3.ogg"
    play test_one "sounds/curtain.ogg"
    show bg night_window1:
        xalign 1
        linear .15 xalign .5
    stop music2 fadeout 3

    "Никого."
    "Только за стеклом, на карнизе, среди птичьих перьев что-то поблёскивало."

    play test_seven "sounds/window2.ogg" loop
    window hide
    scene window_fon
    show window_plumage
    with Dissolve(1.)
    window show

    "Мои очки."
    "Те, что сорвал с меня Семён."
    "Откуда они здесь?.."
    "Неужели это подарок клокочущей ночи? Неужели их принесла сова?"
    "Я посмотрел во двор, на ту зловещую поляну, на зубчатый гробовой лес."
    "Ни души. Ни намёка на поздних визитёров."
    "Старый столб одиноким часовым дремал посреди снежной пустыни."
    "Рассохшиеся ставни кряхтели."

    play test_two "sounds/sfx_tear_papers.ogg"
    $ add_text_to_dictionary(17)

    "Я отодрал утеплитель и {u}полоски приклеенных газет{/u}."

    play test_two "sounds/sfx_window_open.ogg"
    pause 1
    play test_one "sounds/loop_wind_only.ogg" loop
    stop test_seven fadeout 0.25

    "С трудом открыл окно."
    "Мороз впился мелкими иголочками в кожу. Зашевелились от сквозняка рисунки на стенах."
    "Я дотронулся до очков, уверенный, что они растают в пальцах."
    "Они были настоящими."
    "Мозг искал всему объяснение. Семён и его банда разыграли меня, вот и всё."
    "Вот и..."
    "В кругу света под фонарём блестело гладкое снежное одеяло."
    "Если кто-то ходил у дома, взбирался по трубе к подоконнику, он должен был наследить."
    "Отпечатков не было."

    show window_fon2:
        alpha 0
        linear .5 alpha 1
    hide window_plumage
    show window_plumage
    play test_six "sounds/sfx_pick_up_glasses.ogg"

    "Я осторожно забрал очки."
    "Никто не отхватил мне кисть."
    "Не выдернул в полный тревожного движения сумрак."

    voice "voice/karina/2day/95 Vy pochemy.ogg"
    Mam "Вы почему не спите?!"

    scene n01
    show Mom Angry m_evening 00 norm aside at left
    show Olya Weeps m_evening 00 good ahead 00:
        xzoom -1.0
    with Dissolve(0.5)

    play fon "sounds/loop_windgust.ogg" 
    stop test_one fadeout 1

    "От неожиданности я покачнулся и чуть не вывалился из окна."

    voice "voice/karina/2day/96 Sovsem sdyreli.ogg"
    Mam "Совсем сдурели?!"

    voice "voice/karina/2day/97 Zharko.ogg"
    Mam "Жарко, что ли?!"

    voice "voice/karina/2day/98 Ne boleli.ogg"
    Mam "Не болели давно?!"

    show Olya Weeps m_evening 00 good ahead 01 with Dissolve(0.3)

    voice "voice/olya/2day/46 Tam sova.ogg"
    Oly "Там сова была! Тоша её прогнал..."

    show Olya Weeps m_evening 00 good ahead 00 with Dissolve(0.3)

    voice "voice/karina/2day/99 A nyka.ogg"
    Mam "А ну-ка марш спать к себе в комнату!"

    show Mom Angry m_evening 00 norm ahead with Dissolve(.3)

    voice "voice/karina/2day/100 A s toboi.ogg"
    Mam "А с тобой..."

    voice "voice/karina/2day/101 Mama vyderzhala.ogg"

    "Мама выдержала паузу, прожигая меня взглядом. Подбирала наказание соразмерное проступку."
    "Но, махнув рукой, взяла за плечо Олю и ушла, бросив напоследок угрюмое:"

    voice "voice/karina/2day/101 Zavtra pogovorim.ogg"
    Mam "Завтра поговорим."

    play test_three "sounds/steps/mam_out.ogg"
    hide Mom
    hide Olya
    with Dissolve(.5)
    pause 1
    play test_one "sounds/close-door.ogg"
    scene n02 with Dissolve(.3)

    "Я несколькими ударами вогнал раму обратно в паз, повернул шпингалеты, натрудив пальцы."

    play test_two "sounds/sfx_window_knock_3.ogg"
    pause 0.5

label day_2_f:
    $ story_manager.MarkEvent(("day2", "scene15"))

    scene n03 with Dissolve(.3)
    stop fon fadeout 1

    play music "music/Morning Tensions.ogg" volume 0.75 fadein 5

    "Холод ушёл из комнаты. Но не страх."

    window hide
    show d2_end_glasses
    $ renpy.pause(dt_glass*10, hard=True)
    hide d2_end_glasses
    show d2_end_glasses_blink

    "Водрузив на нос очки, я изучал своё отражение в оконном стекле."
    "Не лицо, а какая-то посмертная маска."
    "Как у мальчика с доски объявлений."
    "А ведь этой ночью я был предельно близок к тому, чтобы оказаться на его месте."

    scene final_animation
    $ renpy.pause(4, hard=True)

    "В просвете между детскими затылками прямо на меня смотрело чёрно-белое лицо."

    if Flags.Has("fight"):
        show semen_ob2
    else:
        show semen_ob
    with Dissolve(1.)

    "И это был не Вова – его фото висело рядом. Я узнал щекастую физиономию, нездоровую кожу."
    "Семён."

    show d2_end_rasp
    show men_00:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1050 ypos 540





    show men_02:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1100 ypos 540
    show men_03:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1200 ypos 540
    show men_04:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 2.0 xpos 0 ypos 500
    show men_05:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 2.0 xpos 1200 ypos 500
    with Dissolve(1.)

    "Фотографию Бабурина распечатали и поместили под стекло, как музейный экспонат."

    scene d2_end_rasp_move
    show men_00:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1050 ypos 540
        ease 3 ypos 540 xpos 1000 zoom 1.






    show men_02:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1100 ypos 540
        ease 3 ypos 540 xpos 960 zoom 1.
    show men_03:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 1.2 xpos 1200 ypos 540
        ease 3 xpos 960 ypos 540 zoom 1.
    show men_04:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 2.0 xpos 0 ypos 500
        ease 3 xpos 560 ypos 540 zoom 1.
    show men_05:
        subpixel True
        yalign 0.5
        xalign 0.5
        zoom 2.0 xpos 1200 ypos 500
        ease 3 xpos 1100 ypos 540 zoom 1.
    pause 3

    show bg_black
    with Dissolve(3)

    if true_detective_count2 == 11:

        $ achievement_grant("ach_detective_2")
        $ persistent.has_d2_detective = True


    if not story_manager.IsMarkedLocal(("day1", "scene0")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day1",))
            story_manager.Extend( events )

    if not story_manager.IsMarkedLocal(("day2", "scene0")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day2",))
            story_manager.Extend( events )

    python:
        story_manager.width = 1920
        story_manager.height = 8365+600
        story_manager.day_code = "day2"

    show screen StoryExplainerDCut_Day2(story_manager) with Dissolve(1.5)
    $ ui.interact()

    show screen StoryExplainerDCut_Hider
    with Dissolve(1.5)
    jump day_3


screen StoryExplainerDCut_Day2(story_manager):
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


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene0", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene1", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene2", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "candy", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "candy", "refuse")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "candy", "take")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(100)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "candy", (960, y_val(0)), "refuse")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "candy", (960, y_val(0)), "take")

        $ y_val(75)
        $ y_val(100)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "candy", "take")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(175)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "candy", "refuse")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene3", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la school", (960 - (75+200), y_val(175+85*3+75+25)), (75*2 + 400, 175+85*3+75+25), ("boys", "car", "witness", "nest"))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene4", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene5", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "semen", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "fight")):
                at arrow_invalid
            else:
                at arrow_valid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "submit")):
                at arrow_invalid
            else:
                at arrow_valid

        $ y_val(100)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "semen", (960, y_val(0)), "fight")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "semen", (960, y_val(0)), "submit")

        $ y_val(75)
        $ y_val(100)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "fight")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(175)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "submit")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene6", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom 1.0:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "submit")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom 0.75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "semen", "fight")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(100)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene8", (960-450-75, y_val(0)+100))

        $ y_val(50)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960-450-75, y_val(0)+100) yzoom 10.0:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "la waifu")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la waifu", (960, y_val(175+85*3)), (75*2 + 400, 175+85*4+75+25), ("bucket", "airplane", "shoes"))

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "waifu", (960+200+75, y_val(85)), "fox")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "waifu", (960+200+75, y_val(0)), "polina")

        $ y_val(175)

        add "flowchart_arrow_left" anchor (1., .0) pos (960+275, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "waifu", "polina")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960+275, y_val(0)) xzoom .65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "waifu", "fox")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la corner", (960 + 200+75, y_val(0)), (75*2 + 400, 175+85*2+75+25), ("witness", "squirrel", "niddle"))

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "man_polina", (960, y_val(0)+50), "witness")

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(0) + 75) yzoom 4.0:
            if story_manager.IsMarkedLocal((story_manager.day_code, "waifu", "polina")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175+85*2+75+25)

        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom 1.2:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "la waifu")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (.0, .0) pos (960, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "waifu", "fox")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene9", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "mask", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "mask", "take")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "mask", "refuse")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(100)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "mask", (960, y_val(0)), "take")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "mask", (960, y_val(0)), "refuse")

        $ y_val(175)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_polina0")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960+350, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_fox0")):
                at arrow_valid
            else:
                at arrow_invalid

        add "flowchart_arrow_down" anchor (.5, .0) pos (960-350, y_val(0)) yzoom 10.0:
            if story_manager.IsMarkedLocal((story_manager.day_code, "mask", "take")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_fox0", (960+650, y_val(0)))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_polina0", (960, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960+650, y_val(0)) yzoom 3.0:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "man_fox", "witness")) and story_manager.IsMarkedLocal((story_manager.day_code, "s_fox0")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960+0, y_val(0)) yzoom 3.0:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_polina0")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (1., .0) pos (960+650, y_val(0)) xzoom 0.65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "man_fox", "witness")) and story_manager.IsMarkedLocal((story_manager.day_code, "s_fox0")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "man_fox", (960+350, y_val(0)), "witness")

        $ y_val(75)

        add "flowchart_arrow_right" anchor (1., .0) pos (960+650, y_val(0)) xzoom 0.65:
            if story_manager.IsMarkedLocal((story_manager.day_code, "man_fox", "witness")) and story_manager.IsMarkedLocal((story_manager.day_code, "s_fox0")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_fox1", (960+650, y_val(0)))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_polina1", (960, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_left" anchor (0., .0) pos (960+350, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_fox1")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960+350, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_polina1")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene10", (960+350, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_left" anchor (1., .0) pos (960+350, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_polina1")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960+350, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_fox1")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_fox2", (960+650, y_val(0)))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "s_polina2", (960, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(0)):
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_polina2")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom 0.85:
            if story_manager.IsMarkedLocal((story_manager.day_code, "mask", "take")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_left" anchor (.0, .0) pos (960, y_val(0)) xzoom 1.5:
            if story_manager.IsMarkedLocal((story_manager.day_code, "s_fox2")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene11", (960, y_val(0)))

        $ y_val(75)

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene12b")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(0)) yzoom 3.0:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene12b")):
                at arrow_invalid
            else:
                at arrow_valid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene12b", (960-250, y_val(75)))

        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "scene12b")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene13", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene14", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene15", (960, y_val(75)))



        $ print("y_val final:", y_val.value)


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
