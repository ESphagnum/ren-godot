



label day_1:
    $ story_manager = StoryManager()
    $ story_manager.MarkEvent(("day1", "scene0"))
    play fon "sounds/fon/001wind.ogg" fadein 15.0
    $ renpy.pause(4.5)
    show bg_win_f_0_1
    $ renpy.pause(12.5)
    scene bg_win_f_0
    window show
    "Всю ночь ветер скрёбся в окно когтями."
    "Он бродил по полям и завывал голодным зверем."
    "Бесконечная песнь вилась, словно верёвка, сплетённая из самых разных — тонких, вкрадчивых, насмешливых — голосов."
    "Казалось, они кричат и смеются..."
    "...и спорят о чём-то."

    show bg_win_f_50_1

    "Кто-то носился по снегу, отбрасывая длинные тени. Они то подходили к кровати, то отступали."
    "Дом жил своей жизнью — скрипучей жизнью старых зданий, которые помнят столько всего и будто пытаются рассказать."
    "Одинокий дом глядел на лес, а чащоба смотрела в ответ своими глазищами-дуплами и шуршала, шумела, кивала..."
    "Можно выйти и постоять у кромки леса, просто чтобы убедиться — там, за кривыми деревьями, никого нет."
    "Смутные, мотающиеся на ветру силуэты не причинят вреда."
    "Это же игра света и тени..."
    "Просто такая игра."
    "Я понимаю, что это лишь моё воображение, — мне ведь уже двенадцать."
    "Но всё же..."

    window hide
    stop fon fadeout 3.0
    show bg_win_f_100_1
    $ renpy.pause(2.0, hard = True)
    play fon "sounds/fon/kitchen001.ogg" fadein 5.0
    queue fon "sounds/fon/kitchen002.ogg" loop
    play music "music/1_Melancholy(Tiny_Bunny).ogg" volume 0.7 fadein 6.0

    scene bg_white with Dissolve(1.0)

    scene bg_logo3:
        matrixcolor InvertMatrix(1)
    with Dissolve(1.0)

    show screen center_text(_("Эпизод I: Прилети, сова"), invert=True) with Dissolve(.5)

    pause 1.

    show screen day5_continue_button(d5_logo_begin, invert=True)
    with Dissolve(.5)
    $ ui.interact()

    hide screen day5_continue_button
    with Dissolve(.5)

    pause 1.

    hide screen center_text with Dissolve(.5)

    scene bg_white with Dissolve(1.0)

    $ story_manager.MarkEvent(("day1", "scene1"))


    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant2_book
    with Dissolve(3.0)
    play test_one "sounds/steps/mam_in.ogg"
    show Mom Normal m_day 01 norm aside at mom_income
    window show

    voice "voice/karina/10 K.ogg"
    Mam "Убери книгу немедленно!"

    show kitchen ol1 with Dissolve(0.3)

    voice "voice/karina/01 K.ogg"
    Mam "Сколько раз говорила — не читай за столом! Вредно! Сидишь, ссутулился весь!"

    window hide
    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1_book
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.3)

    hide kitchen_ant1_book
    call screen day1_choice_book()

    show kitchen_ant2_book
    with None

    hide kitchen_ant2_book
    show kitchen_ant1
    with Dissolve(0.5)
    $ renpy.pause(1.5)
    window show

    "Я послушно отложил книгу о похождениях Конана-варвара."

    show kitchen ol1
    with Dissolve(0.3)

    "Всё равно я прочитал одну и ту же строчку три раза и ничего не понял."

    show kitchen ol2
    with Dissolve(0.3)

    "Оля уже позавтракала и взялась за печенье. Хрустела с аппетитом, как девочки из рекламы."

    voice "voice/karina/12 K.ogg"
    Mam "Пока не съешь — из-за стола не встанешь!"

    "А я всё буравил взглядом манку, словно надеялся, что она рассосётся сама по себе."
    "Смутная тревога распирала. Всё из-за бессонной ночи, чёрного леса, огибающего двор, и угрюмого ветра..."

    show kitchen ol1
    with Dissolve(0.3)

    "Чем дольше я тянул, тем холоднее становилась комковатая белая масса."

    show kitchen ol2
    with Dissolve(0.3)

    "Будто медуза из «Подводной одиссеи Кусто». Обожаю эту передачу."
    "Интересно, на дне океана очень жутко?"
    "А ночью в холодном чёрном лесу?"

    window hide
    hide kitchen_ant1
    show kitchen_ant3
    with Dissolve(0.5)
    play test_one "sounds/spoon-2.ogg"
    $ renpy.pause(0.3)
    window show

    "Ложка выпала из руки."
    "Мама плеснула студёным взглядом зелёных глаз."

    voice "voice/karina/13 K.ogg"
    Mam "Что я говорила?"

    voice "voice/anton/1day/001. YA dost.ogg"
    Ant "Я достану!"

    play test_one "<from 0.0 to 0.40>sounds/steps/Olya-stand-up-1.ogg"
    hide kitchen_ant3
    show kitchen_ant0
    with Dissolve(0.5)

    "Десятисекундная передышка перед новым сражением с гадкой кашей."
    "Я нащупал ложку."

    play test_one "sounds/steps/mam_out.ogg"
    show Mom Normal m_day 01 norm aside at mom_reverse_and_out1
    show kitchen ol1 with Dissolve(0.3)

    "А что это такое нацарапано снизу на столешнице?"

    show under_table with Dissolve(0.5)

    "«Ка-ри-на»."

    play test_two "sounds/nadpis-fix.ogg"

    "Ха-х, это же мамино имя!"
    "Видимо, это она в детстве накарябала чем-то острым."
    "Оказывается, хулиганкой была — мебель портила."
    "Ох, меня бы она за такое неделю ругала."
    "Напомнить ей о шалости?"
    "Нет. Что-то она не в духе в последнее время."
    "Я вообразил, как она, моя ровесница, сидела здесь, под столом."

    stop music fadeout 6.0

    "Интересно, в детстве мама боялась темноты?"
    "А шороха на чердаке?"
    "А лесных дебрей?.."

    play music2 "music/2_Anxiety.ogg" fadein 2.0
    stop fon fadeout 3.0
    scene bg_black with Dissolve(1)
    show screen memory_ramka
    scene grand_mather:
        zoom 1.15
        linear 50.0 zoom 1.0
    show bg_black:
        alpha 1.0
        linear 1.5 alpha 0.0

    "Я представил, как бабушка заходит в спальню к моей маленькой маме, садится на край кроватки, где теперь спит Оля, и рассказывает мягким вкрадчивым голосом:"
    voice "voice/grandmother/1. Taiga.ogg"
    Gra "Тайга – особое место, дитятко."
    voice "voice/grandmother/2. Ona.ogg"
    Gra "Она к тебе присматривается, принюхивается."
    voice "voice/grandmother/3. Slovno.ogg"
    Gra "Словно хочет понять, что ты за зверь такой."
    voice "voice/grandmother/4.Ponrav.ogg"
    Gra "Понравишься – в беде не бросит."
    voice "voice/grandmother/5.A bud.ogg"
    Gra "А будешь проказничать – схватит за бочок и утащит с собой под землю."
    voice "voice/grandmother/6.Tut.ogg"
    Gra "Тут и дело с концом."
    "Бабушка была ласковой, никогда ни с кем не ссорилась, не ругалась..."
    "Тогда не было этих сводящих с ума криков до глубокой ночи, разбитой посуды и взаимных обвинений."
    "В то время наши родители ещё любили друг друга."
    "Помню, я случайно подслушал родительский разговор и узнал, что бабушка заранее побеспокоилась о своих похоронах."
    "Купила себе гроб."
    "И называла его ласково «гробиком»."
    "Он стоял в чулане, словно терпеливо ждал."
    "Чёрный, с обивкой цвета мяса – это я увидел потом, когда бабушку хоронили."

    show bg_black:
        alpha 0.0
        linear 3.0 alpha 1.0

    "Дом остался таким же, каким и был при бабуле. Только фотографии все убрали куда-то."

    stop music2 fadeout 6.0
    scene bg_black

    "Застеклённые снимки с серыми лицами моих предков. У всех плоские, но зоркие неживые глаза."

    play music "music/1_Melancholy(Tiny_Bunny).ogg" volume 0.7 fadein 6.0
    hide screen memory_ramka
    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    show bg_black:
        alpha 1.0
        linear 2.0 alpha 0.0

    "Я выбрался из-под стола."
    "Оля расправилась с печеньем и, как хитрый зверёк, поглядывала на мою порцию."
    "Я бросил взгляд на заиндевевшее окно."
    "Снаружи темнели сосны, но не они привлекли моё внимание."
    "Январский узор складывался в картинку."

    scene bg_win_f_100 with Dissolve(1.0)

    voice "voice/anton/1day/002. Olja gl.ogg"
    Ant "Оля, гляди, лиса!"
    voice "voice/olya/02 O.ogg"
    Oly "Где?"
    "Похоже на оптические иллюзии на задних обложках тетрадок."
    "Вроде мешанина из чёрточек, но если расфокусировать взгляд..."
    "...и посмотреть под определённым углом..."

    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    with Dissolve(0.5)

    voice "voice/anton/1day/003. Da ne.ogg"
    Ant "Да не на улице! На стекле!"

    scene bg kitchen1_1
    show kitchen ol3
    show kitchen_ant1
    with Dissolve(0.5)

    voice "voice/anton/1day/004. Smotri.ogg"
    Ant "Смотри, вот нос. Вот..."

    play test_one "sounds/steps/mam_in.ogg"
    show Mom Normal m_day 01 norm aside at mom_income

    voice "voice/karina/14 K.ogg"
    Mam "Ну-ка, доедай!"
    voice "voice/anton/1day/005. Da da.ogg"
    Ant "Да, да... сейчас."

    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.5)

    voice "voice/olya/03 O.ogg"
    Oly "Я ничего не вижу."
    voice "voice/karina/15 K.ogg"
    Mam "Живо, совсем немного осталось!"

    scene bg kitchen1_1
    show kitchen ol3
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.5)

    voice "voice/olya/04 O.ogg"
    Oly "А-а-а-а! Вот... Но всё равно не похоже."
    voice "voice/anton/1day/006.A ja gov.ogg"
    Ant "А я говорю — похоже."

    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.5)

    voice "voice/olya/05 O.ogg"
    Oly "Не-а!"
    voice "voice/anton/1day/007.Pohozhe_.ogg"
    Ant "Похоже!"
    voice "voice/karina/16 K.ogg"
    Mam "Прекратите! Ну что за дети..."

    scene bg_win_f_0 with Dissolve(0.5)

    "Теперь и я не мог отыскать лису."
    "Она исчезла."
    "Ушла."
    "Лишь узоры ползли по стеклу, похожие на вытянутые листья крапивы."

    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    play test_one "sounds/steps/pap_in.ogg"
    show Dad Normal m_day 01 norm aside at dad_income
    with Dissolve(0.5)

    "На кухню вошёл папа, большой и неторопливый."
    "Хочу, когда вырасту, стать как он — бородачом!"
    "Мама, шутя, всё просила папу: «Ну сбрей, колется же!»"

    stop music fadeout 10.0
    play music2 "music/3_trouble.ogg" volume 0.9 fadein 15.0
    $ music_during_lines = 0.7

    "Как давно это было..."
    "А теперь каждый день грохот дверей и мстительные колкости."
    "Оля зажимала уши, когда за стеной раздавались голоса: «Ради чего это всё?»"

    scene bg kitchen1_1
    show kitchen ol1
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    show Dad Normal m_day 01 norm aside at dad_left
    with Dissolve(0.5)

    "\"Ради вас! – отвечал папа, — Ради семьи!\""
    "Я ловил каждый звук и боялся услышать самое страшное, самое убийственное слово на букву «р»."

    show kitchen ol2
    with Dissolve(0.3)

    "Р-а-з-в..."
    "Не хочу даже продолжать."
    "Боюсь представить, что нас с сестрёнкой разлучат и разведут по разным семьям."
    voice "voice/olya/06 O.ogg"
    Oly "Да что твоя лиса. Вот у меня на окне сова!"

    voice "voice/father/01 F.ogg"
    Pap "Опять ты со своей совой!"

    voice "voice/olya/07 O.ogg"
    Oly "Так ты же вчера мне верил!"

    voice "voice/father/02 F.ogg"
    Pap "Никто ключи от машины не видел?"

    voice "voice/father/03 F.ogg"
    Pap "Вроде оставлял на подоконнике..."

    voice "voice/karina/17 K.ogg"
    Mam "Вроде..."

    voice "voice/karina/18 K.ogg"
    Mam "Вроде оставлял, вроде нет."

    voice "voice/karina/19 K.ogg"
    Mam "Вроде взрослый мужчина, отец двоих детей, а вроде..."

    voice "voice/father/04 F.ogg"
    Pap "Перестань, пожалуйста, Карина."

    voice "voice/father/06 F.ogg"
    Pap "Дай мне спокойно собраться."

    voice "voice/karina/20 K.ogg"
    Mam "В корзине твои ключи, возле телефона."

    voice "voice/father/07 F.ogg"
    Pap "Огромное тебе человеческое спасибо."

    show kitchen ol1
    with Dissolve(0.3)

    voice "voice/father/08 F.ogg"
    Pap "Антон, ешь быстрее, а то как мученик сидишь..."
    voice "voice/olya/07A O.ogg"
    Oly "А сова..."

    voice "voice/father/09 F.ogg"
    Pap "Не было там никакой совы."

    scene bg kitchen1_1
    show kitchen ol2
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    show Dad Normal m_day 01 norm aside at dad_left
    with Dissolve(0.5)

    voice "voice/olya/08 O.ogg"
    Oly "Была!"
    voice "voice/olya/09 O.ogg"
    Oly "Глазюки огромные — во! И светятся."

    scene bg kitchen1_1
    show kitchen ol0
    play test_one "sounds/steps/Olya-stand-up-1.ogg"
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    show Dad Normal m_day 01 norm aside at dad_left
    show Olya Serious m_day 00 good ahead 01
    with Dissolve(0.5)

    "Оля вскочила со стула и приставила руки к личику, показывая пальцами глаза, каждый величиной с яблоко."

    $ add_text_to_dictionary(1)

    voice "voice/father/10 F.ogg"

    Pap "В прошлом году — {u}Бабай{/u} в шкафу, сейчас — сова?"
    voice "voice/olya/10 O.ogg"

    Oly "Ну-у я же видела..."
    "Оля переводила взгляд с отца на маму, потом на меня, но нигде не находила поддержки."

    voice "voice/father/11 F.ogg"
    Pap "А ты не думала подружиться с ней, нет?"
    voice "voice/father/12 F.ogg"
    Pap "Вымышленными мышами покормить, например?"

    voice "voice/karina/21 K.ogg"
    Mam "Не подначивай ребёнка."
    voice "voice/karina/22 K.ogg"
    Mam "Просто мала ещё и спать одна боится."

    $ music_during_lines = 1.0

    hide Olya
    with Dissolve(0.3)
    play test_two "sounds/steps/Olya-ladder-steps-1.ogg"

    "Оля капризно надула губы и опрометью вылетела в коридор."
    "Заскрипела лестница, ведущая на второй этаж."

    hide Mom
    show Mom Angry m_day 01 norm aside at mom_right
    with Dissolve(0.3)

    "Мама строго посмотрела на отца."

    stop music2 fadeout 10.0

    "Ох, этот взгляд! Как же неуютно под его прицелом."

    play test_one "sounds/steps/pap_out.ogg"
    hide Dad
    show Dad Normal m_day 01 norm aside at dad_out
    play test_two "sounds/Key.ogg"

    voice "voice/father/13 F.ogg"

    "Папа лишь фыркнул и ушёл, звеня связкой найденных ключей."

    play test_two "sounds/steps/Olya-ladde.ogg"

    "Спустя минуту на весь дом раздалась мелодия из «Русалочки»."
    "Это была затёртая до дыр кассетная плёнка, которую папа уже склеивал однажды."
    "С вещами всё просто — их можно починить или вот, склеить."
    "А как быть с отношениями?"

    play test_one "sounds/steps/mam_out.ogg"
    hide Mom
    show Mom Normal m_day 01 norm aside at mom_reverse_and_out1

    "Мама ушла в гостиную, и я остался один, обеспокоенно поглядывая в окно."

    window hide
    stop fon
    stop test_one
    play music "music/4_Olya's nightmare.ogg" fadein 6.0
    scene bg_black with Dissolve(1.0)
    scene bg Olya_and_Owl0
    show bg_black:
        alpha 1.0
        linear 1.0 alpha 0.0
    show screen memory_ramka
    $ renpy.pause(0.2)
    show old_movie_003_004
    $ renpy.pause(0.2)
    hide old_movie_003_004
    $ renpy.pause(0.5)
    $ persistent.animal_unlock[0] = True
    window show

    "С тех пор как мы переехали в этот старый дом, Оля плохо спала."
    "Ворочалась в постели или съёживалась клубочком под одеялом."
    "Порой вскакивала среди ночи, чтобы включить видеомагнитофон."
    "Мультфильмы помогали отвлечься от переживаний из-за переезда, родителей..."

    window hide
    play wtf "sounds/skrimer01.ogg"
    show owl_screem_effect at clear_owl
    show old_movie_001_002
    $ renpy.pause(0.2)
    hide old_movie_001_002
    show bg Olya_and_Owl with Dissolve(1.5)
    window show

    "А потом Оле привиделось это огромное крылатое чудовище за окном."
    "Она стала одержима совой."
    "Чего только родители ни делали, на какие ухищрения ни шли, чтобы искоренить её страхи."
    "Оля напрочь отказывалась спать одна и не верила, что сова была всего лишь дурным сном."
    "После сегодняшней ночи я не знал, что думать, как теперь относиться к словам сестры..."
    "Могут ли кошмары быть заразными?"

    scene bg_black
    with Dissolve(0.7)
    play fon "sounds/fon/skrip1.ogg"
    scene bg_pole0
    show dancing animal_on:
        xpos 286 ypos 233
    show over_dancing
    show bg_room_night1
    hide bg_black
    show bg_black:
        alpha 1.0
        linear 2.0 alpha 0.0

    $ story_manager.MarkEvent(("day1", "scene2"))

    "Прошлой ночью я лежал без сна и думал о том, что ждёт меня в новой школе."
    "До занятий оставалось несколько дней."
    "Воображение рисовало длинные извилистые коридоры. Они приводили к классу, заполненному детьми."
    "Но ученики за партами были тёмными силуэтами, словно вырезанными по трафарету контурами."

    scene nightmare_klass0 onlayer master1:
        xpan 0
        linear 30 xpan 360
        repeat
    show children_in_class_rem onlayer master1:
        xpan 0
        linear 20 xpan 360
        repeat
    show children_in_class_rem2 onlayer master1:
        xpan 0
        linear 15 xpan 360
        repeat
    show old_movie_intense onlayer master1
    show bg_black onlayer master1:
        alpha .3
    show d4_noise onlayer master1
    show layer master1:
        alpha 0
        linear 5 alpha 1
    "Посреди их чёрных лиц зияли круглые дыры, а в дырах моргали глаза, будто бы совсем другие существа смотрели на меня из-за плоских чёрных фигур."
    "И столько жестокости было в этих взглядах, столько ледяной насмешки, что я дрожал с головы до ног."
    "Выживу ли я здесь?"
    "Не забьют ли меня до смерти толпой быстрые топчущие ноги, вымазанные кровью ботинки..."
    "Пусть бы она сгорела, эта чёртова школа."
    "Пусть бы хоть что-то случилось - неважно что. Лишь бы не идти на уроки."
    "Не видеть людей, которые только и мечтают дать оплеуху, поставить подножку, придумать очередное прозвище — ещё оскорбительнее, чем предыдущее."

    show layer master1:
        alpha 1
        linear 1 alpha 0
    "Будто мои очки делают меня чужаком, каким-то монстром."

    hide bg_black

    "Взор мазнул по рисункам, развешанным на стенах."
    "Я не считал себя великим художником, но Оля упросила повесить. Только рисование меня хоть немного радовало в последнее время..."
    "Моим немногочисленным друзьям тоже нравилось, как я рисую. А ведь они, кстати, обещали звонить..."

    scene d5_phone_bg onlayer master1
    show d5_phone_off onlayer master1
    show d4_noise onlayer master1 zorder 1
    with Dissolve(.5)
    show polina_call_pickedup onlayer master1
    with Dissolve(.5)
    "Иногда воображаю, как мама снимает трубку и говорит холодно: «Вы не туда попали»."
    "Или: «Антона нет»."

    scene d5_phone_bg onlayer master1
    show d5_phone_off onlayer master1
    show d4_noise onlayer master1 zorder 1
    with Dissolve(.5)
    "Антона нет..."

    scene onlayer master1
    with Dissolve(.5)
    "Я представлял своих будущих одноклассников и одноклассниц, которые, как и я, лежали в эту минуту в кроватях, слушая вой невидимых оборотней за окном."

    scene day1_kovai_0
    with Dissolve(.5)
    "Быть может, я всё-таки понравлюсь новому классу?"
    "Кому вообще нравятся ребята в очках с толстенными линзами?"
    "Папа вот в детстве носил очки. А теперь он женат на самой красивой женщине в мире – моей маме."

    stop music fadeout 6.0
    scene bg_room_night1
    with Dissolve(.5)
    "Дом заскрипел под напором ветра."
    "Наш прежний дом — бетонный, девятиэтажный — жужжал соседским перфоратором, бубнил телевизором за стеной, плакал навзрыд из квартиры многодетного семейства."
    "Теперешний дом – язык не поворачивается назвать его новым – был совсем другим."
    "Днём тихий и покладистый - тени отдыхают в углах, в паутине чуланов, под лестницей."

    play music "music/5_Shadow_Dance.ogg" fadein 45.0

    "Но ночью они просыпаются."
    "Что-то смотрит на меня из углов. Будто фотографии мёртвых родственников с земляными глазами снова повесили на стену вместо моих рисунков."
    "Кряхтят половицы, стонут ржавые водостоки, чердак населяют гулкие сквозняки."
    "Словно дом играет какую-то дьявольскую мелодию."

    scene day1_kovai_0
    with Dissolve(.5)
    "Вдруг я понял, что действительно слышу музыку, причём, играет она уже давно."
    "Где-то далеко, на самой границе восприятия, пела флейта."
    "Она словно бы сливалась с воем ветра, с поскрипыванием старого дома, с моими мыслями, наконец."

    play test_one "sounds/steps/Anton-stairs-out-2.ogg"

    scene bg_room_night1
    with Dissolve(.5)
    "Я встал и поторопился к окну. Хотел убедить себя, что нет никакой музыки, что это лишь моё воображение."
    "Что никто не может играть там, в холодной заснеженной ночи."

    window hide
    call screen room_night_1
    play test_one "sounds/curtain.ogg"
    hide bg_room_night1
    show bg_room_night2
    with Dissolve(0.2)
    stop fon
    $ renpy.pause(2.0)

    scene bg_pole0
    show dancing animal_on:
        xpos 286 ypos 233
    show over_dancing
    with Dissolve(0.5)

    window show

    "Там, в поле, кто-то танцевал."
    "Чёрные фигуры, едва различимые на фоне тёмного леса."
    "Залитые лунным светом, они резко подпрыгивали и припадали к сугробам, катались в снегу и ползали на четвереньках."
    "Мне вспомнились истории о волках, играющих под луной. Но это были не волки."
    "Они вставали на ноги, водили хоровод, вздымая вихри снега, растворялись во мраке и появлялись вновь."
    "Творилось что-то странное."
    "Пляска теней в беззвёздной тьме распаляла воображение и одновременно нагоняла тревогу..."

    play test_one "sounds/tydydym.ogg"
    stop music fadeout 0.5
    show dancing animal_off:
        xpos 286 ypos 233
    with Dissolve(0.1)

    $ renpy.start_predict("dancing2 animal_wolf2")

    "Вдруг музыка стихла."
    "Танцующие застыли и — я готов был поклясться — уставились на меня."
    "Внезапно одна из фигур отделилась от странного карнавала теней и ринулась по полю, мощными прыжками преодолевая расстояние."

    play test_one "sounds/snow-steps-breath-1.ogg"
    window hide
    show dancing animal_wolf1:
        xpos 0 ypos 0
    show dancing2 animal_wolf2
    $ renpy.pause(1.5, hard=True)
    hide dancing2 animal_wolf2
    window show

    $ renpy.stop_predict("dancing2 animal_wolf2")
    "Она скользила, не оставляя вмятин на хрустком насте, пока угольная тень дома не поглотила ночное существо, став ещё гуще и чернее."

    play music "music/Garazh_part1.ogg" fadein 6.0

    scene day3_window_bg_blur_0:
        xalign .0
    show over_dancing2
    show day3_window_frame:
        xalign .0
    with Dissolve(.25)
    "Сердце заметалось птицей в клетке."

    play test_one "sounds/curtain.ogg"
    scene shtora_5:
        subpixel True
        align (.5, .5)
        zoom 1.25
        easein .25 zoom 1.0

    "Я отпрянул к кровати, успев рывком задёрнуть шторы."
    "Меня видели!"
    "Страх окатил ледяным потоком."
    "Стоя в тёмной комнате, я слышал, как снаружи возится и скребётся незваный гость, как он мечется по двору, выискивая вход."
    "Звук ушёл вправо."
    "Обогнул дом..."
    "Сейчас гость окажется на пороге..."

    scene bg_room_night1
    with Dissolve(.5)
    "Я кинулся в постель и укрылся с головой, словно одеяло могло меня защитить."

    scene bg_black
    with Dissolve(.5)
    "Страх сковал мышцы."

    scene day1_corpse
    show d4_noise zorder 10:
        alpha .3
    show ramka zorder 100
    with Dissolve(.5)
    "Я вдруг снова вспомнил о похоронах: как бабушка лежала, скрестив руки, с заострившимися чертами лица, похожая на восковую куклу..."

    show day1_ants
    with Dissolve(.5)
    "А по ножкам стульев, на которые водрузили гроб, ползли муравьи."

    show day1_nightmare:
        align (.4, .15)
        zoom 1.05
        .1
        zoom 1.0
    "Я представлял тогда, что они взберутся на голову бабушке и лапками поднимут ей веки."
    "Тогда бы сморщенные глазные яблоки шевельнулись в гнёздах, и бабуля вновь бы увидела внуков."

    show bg_black zorder 200:
        alpha 0
        linear 15 alpha 1
    "Там, на похоронах, я повторял мысленно слова заговора, которому она меня научила."
    "И, лёжа под одеялом, прислушиваясь к скрипу и вою, я шептал эти слова:"

    $ music_during_lines = 0.7
    voice "voice/anton/1day/008. Na ost.ogg"
    Ant "На острове Буяне, в синем океане, стоит домовина, в ней — сало и глина, волосы седые - чертям еда, а раба Божьего Антона не тронут никогда."
    voice "voice/anton/1day/008_1. Besy.ogg"
    Ant "Бесы забудут дорогу к дому."
    voice "voice/anton/1day/008_2. Mertvoe.ogg"
    Ant "Мёртвое — к мёртвому, живое — к живому."
    $ music_during_lines = 1.0

    stop music fadeout 5.0

    scene bg_black
    with Dissolve(.5)
    "Непонятные шумы утихли."

    scene day1_kovai_1 with Dissolve(0.5)
    "Я осторожно высунулся из-под одеяла, чтобы увидеть, как под потолком, словно висельник, колышется штора."

    play music "music/7_nq-mid-amb-4.ogg" fadein 15.0

    "И тут ночь ошпарила меня новой порцией кипящего ужаса."

    play test_one "sounds/claws.ogg"
    scene bg Anton_kovai with Dissolve(0.5)

    "Звук резанул по ушам."

    scene bg_room_night1 with Dissolve(0.15):
        align (.0, .5)
        easein 0.25 zoom 1.15
    "Что-то царапало входную дверь. Быстро-быстро скоблило когтями полотно, требуя впустить его."
    "Дверь заперта."

    play test_two "sounds/claws.ogg"
    scene bg house_day
    show Dad Normal m_day_winter 02 norm2 ahead:
        xzoom -1
        yoffset 50
        xoffset 500
    show d4_noise
    with Dissolve(.5)
    "Папа стал осторожным и вкрутил надёжный замок."
    "Помню, как он долго и напряжённо вглядывался в лес, словно выискивал в нём кого-то."

    scene bg_room_night1
    with Dissolve(.5)
    voice "voice/anton/1day/008_3. Mertvoe.ogg"
    Ant "Мёртвое — к мёртвому!"

    play test_one "sounds/door-kick-glass-1.ogg"
    $ renpy.pause(0.2)

    voice "voice/anton/1day/008_4. Zhivoe.ogg"
    Ant "Живое — к живому!"

    scene day1_kovai_1
    with Dissolve(0.5)
    "Я поджал колени, уткнулся в них подбородком и засверлил взглядом межкомнатную дверь, такую хлипкую и слабую перед мощью темноты."
    "И вдруг..."

    window hide
    scene bg room_night_ZOOM with Dissolve(0.4)
    $ renpy.pause(0.5)
    play test_one "sounds/1.knob-slow.ogg"
    show door open_door1_1
    $ renpy.pause(1.0)
    window show

    "Дверная ручка робко повернулась."

    window hide
    hide door open_door1_1
    play test_one "sounds/2.knobs-mid.ogg"
    show door open_door1_2
    $ renpy.pause(0.5)
    window show

    "Затем дёрнулась раз, другой. Будто у того, кто пытался открыть дверь, не было рук."


    window hide
    hide door open_door1_2
    play test_one "sounds/2.knobs-mid.ogg"
    show door open_door1_2
    $ renpy.pause(0.5)
    window show

    "Ручка вновь кивнула и неожиданно..."

    scene bg room_night_ZOOM_2
    play test_one "sounds/Risers_01.ogg" loop
    play test_two "sounds/4.fast-mad-2-3.ogg" loop

    "...защёлкала бешено."
    "От страха у меня свело челюсть. Мокрые пальцы комкали одеяло."

    play test_one "sounds/creaks.ogg"
    stop test_two fadeout 0.5
    scene bg room_night_ZOOM
    show door open_door1 with Dissolve(0.4)

    "Дверь заскрипела и отворилась."
    "Дом издевательски стонал ветром в жестяных водостоках."
    "Сейчас..."
    "Сейчас ты увидишь..."

    play test_one "sounds/creaks-2.ogg"
    show door open_door2 with Dissolve(0.4)

    "Дверь распахнулась."
    "Тьма кишела в прожорливой пасти проёма."
    voice "voice/olya/11A O.ogg"
    Noname "То-о-о..."
    voice "voice/olya/11B O.ogg"
    Noname "...ша-а-а..."
    "Словно сама ночь обращалась ко мне, то хлопая чёрными крыльями, то скрипя несмазанными петлями."
    "Мрак был паутиной, облепившей углы комнаты, я дрожал в его коконе и ждал, когда из чёрного провала выступит тот, кто соткал паутину."
    voice "voice/olya/12A O.ogg"
    Noname "То-о-о..."
    voice "voice/olya/12B O.ogg"
    Noname "...ша-а-а..."
    "Мышцы живота заныли, грудная клетка расправилась, готовая выпустить отчаянный вопль."

    stop music fadeout 10.0

    $ music_during_lines = 0.8
    "Но прежде чем я закричал, темнота спросила:"
    voice "voice/olya/13 O.ogg"
    Noname "Ты спишь, Тоша?"

    $ renpy.pause(0.5)
    show door open_door3 with Dissolve(0.3)

    "Бледное лицо сестры выплыло из густой тени."

    play music2 "music/8_Peredyshka.ogg" volume 0.8 fadein 3.0
    $ music_during_lines = 1.0

    "Я готов был вскрикнуть от облегчения."

    voice "voice/anton/1day/011. Olja_ja_.ogg"
    Ant "Оля? Я... Я не сплю... Что случилось?"
    "Носик Оли сморщился, а нижняя губа оттопырилась — верный признак, что с секунды на секунду сестра расплачется."

    show door open_door2
    show Olya Weeps m_dark 00 good ahead 04
    with Dissolve(0.5)

    show Olya Weeps m_dark 00 good ahead 01 with Dissolve(.2)
    voice "voice/olya/14 O.ogg"
    Oly "Она опять прилетела и пялится на меня..."
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.2)

    show Olya Weeps m_dark 00 good ahead 02 with Dissolve(0.2)
    voice "voice/olya/15 O.ogg"
    Oly "Прогони её, Тоша! Прогони, пожалуйста."
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.2)

    show Olya Weeps m_dark 00 good ahead 02 at sprite_fear with Dissolve(0.2)
    voice "voice/olya/16 O.ogg"
    Oly "Я так боюсь!"
    show Olya Weeps m_dark 00 good ahead 04 with Dissolve(.2)

    "Страх, только что терзавший меня, уполз и притаился где-то в животе. Я обязан был успокоить Олю."

    voice "voice/anton/1day/012. Eto by.ogg"
    Ant "Это был сон, глупая, не пугайся — сны не кусаются. Никто тебя не обидит."
    "Оля всхлипнула."
    "Она изо всех сил пыталась мне верить."
    "Но верил ли я сам?"

    voice "voice/anton/1day/013. U menja.ogg"
    Ant "У меня есть идея!"
    voice "voice/anton/1day/013. A poidem.ogg"
    Ant "А пойдём к тебе в комнату, видик посмотрим. «Спящую красавицу», например."

    voice "voice/anton/1day/014. Tebe zh.ogg"
    Ant "Тебе же нравится этот мультик?"

    hide Olya
    show Olya Serious m_dark 00 good ahead 01
    with Dissolve(0.5)

    show Olya Serious m_dark 00 good ahead 02 with Dissolve(0.2)
    voice "voice/olya/17 O.ogg"
    Oly "Почему у Спящей красавицы принц, а у меня – эта страшная птица?"
    show Olya Serious m_dark 00 good ahead 01 with Dissolve(0.2)

    "Вопрос застал врасплох."

    voice "voice/anton/1day/014. Ladno.ogg"
    Ant "Ладно, давай посмотрим «Золушку»."
    "Мысли путались, расплывались."
    "Что это было?"

    hide Olya
    with Dissolve(0.3)
    stop music2 fadeout 5.0

    $ renpy.start_predict("wolf_scrimer")
    $ renpy.start_predict("Ant_wakeup2")

    "Что высматривало меня, лихорадочно танцуя под луной?"
    "К оконному стеклу прижималась тьма, и её не обманешь старыми бабушкиными заговорами."
    "Не проведёшь, предложив вместо себя ящик с салом и глиной, с обрезанными седыми косами."
    voice "voice/olya/18 O.ogg"
    Oly "Тоша, ты идёшь?"

    voice "voice/anton/1day/015. Da da.ogg"
    Ant "Да-да. Сейчас."

    play test_one "sounds/wolf-steps-breath-2.ogg"
    window hide
    show door open_door4 with Dissolve(0.1)
    $ renpy.pause(0.2)
    scene bg room_night_opendoor
    show door open_door5
    with Dissolve(0.1)
    hide door open_door5
    show bg_black:
        alpha 0.0
        linear 0.1
        linear 0.3 alpha 0.8
    play wtf "sounds/skrimer05-1.ogg"
    show wolf_scrimer:
        xalign 0.5
        yalign 0.5
        ypos 3000
        alpha 0.9
        zoom 0.2
        linear 0.05 ypos 1500
        linear 0.08 ypos 1000 alpha 0.91 zoom 0.25
        linear 0.1 ypos 600 alpha 0.92 zoom 0.30
        linear 0.15 ypos 600 alpha 0.93 zoom 0.30
        linear 0.1 ypos 1150 alpha 0.99 zoom 1.25
        linear 0.2 ypos 1150 alpha 1.00 zoom 1.25
    $ renpy.pause(0.3, hard=True)
    show bg_black with Dissolve(0.05)
    hide bg_black with Dissolve(0.05)
    show bg_black with Dissolve(0.05)
    hide bg_black with Dissolve(0.05)
    show bg_black with Dissolve(0.025)
    hide bg_black with Dissolve(0.025)
    show bg_black with Dissolve(0.025)
    hide bg_black with Dissolve(0.025)
    show bg_black with Dissolve(0.025)
    hide bg_black with Dissolve(0.025)
    show bg_black with Dissolve(0.025)
    hide wolf_scrimer
    $ renpy.stop_predict("wolf_scrimer")
    $ renpy.pause(0.3, hard=True)
    play test_three "sounds/xrum.ogg" loop
    $ renpy.pause(9.0, hard=True)
    stop test_three fadeout 5.0
    $ renpy.pause(2.0, hard=True)
    play test_three "sounds/sfx_bed_squeaks_2.ogg"
    scene Ant_wakeup2
    $ renpy.pause(2.6, hard=True)
    show old_movie_003_004
    $ renpy.pause(0.2)
    hide old_movie_003_004
    scene bg_black with Dissolve(1.0)
    hide screen memory_ramka
    $ renpy.stop_predict("Ant_wakeup2")

    scene bg kitchen1_1
    show kitchen ol0
    show kitchen_ant1
    show Mom Normal m_day 01 norm aside at mom_right
    show bg_black:
        alpha 1.0
        pause 2.0
        linear 3.0 alpha 0.0
    $ renpy.pause(4.2)
    show old_movie_003_004
    $ renpy.pause(0.2)
    hide old_movie_003_004
    $ renpy.pause(0.5)
    window show

    $ story_manager.MarkEvent(("day1", "scene3"))

    "Вот почему утром мне совсем не хотелось смеяться над Олей и этой её совой."

    window hide
    hide bg_black
    play test_one "sounds/ringe.ogg"
    $ renpy.pause(1.5, hard=True)
    window show
    play music "music/9_Nikita Kryukov - the Obscurity.ogg" volume 0.85 fadein 3.0

    "Кто мог прийти к нам в этой глуши?"

    play test_one "sounds/steps/mam_out.ogg"
    window hide
    hide Mom
    show Mom Normal m_day 01 norm aside at mom_reverse_and_out1
    window show

    "Мы ведь здесь никого не знаем."

    window hide
    play test_one "sounds/ringe.ogg"
    $ renpy.pause(1.5, hard=True)
    window show

    "Настырные какие."
    "От нелепой мысли, что утренние гости пришли прямиком из леса, стало особенно неуютно."
    "В прихожей зазвучали неразборчивые голоса."
    "Подмывало спрятаться."

    scene bg kitchen1_1
    show kitchen ol0
    show kitchen_ant2
    with Dissolve(0.3)

    "В шкаф..."
    "Под стол..."
    "За занавеску, куда любит прятаться Оля."

    scene bg kitchen1_1
    show kitchen ol0
    show kitchen_ant1
    with Dissolve(0.3)

    voice "voice/karina/24 Tosha.ogg"
    Mam "Тоша! Подойди-ка сюда!"
    "К ногам словно гири привязали. Я поплёлся в коридор."

    play test_one "sounds/steps/Anton-stairs-out-2.ogg"

    play fon "sounds/fon/wind.ogg" fadein 2.0 loop
    scene bg door_police with Dissolve(1.5)

    "Два милиционера возвышались на пороге."
    "От них пахло морозом и тревогой."
    "Мама, завидев машины с мигалками, обычно кривилась и ворчала: «Хуже бандитов»."
    "Но сейчас она выглядела несколько растерянно."

    voice "voice/anton/1day/017. Zdravs.ogg"
    Ant "Здравствуйте."

    "Старший по званию мрачно кивнул."

    voice "voice/karina/23 K.ogg"
    Mam "Тут мальчик вчера потерялся. Вовой зовут."
    voice "voice/karina/24 K.ogg"
    Mam "Глянь, пожалуйста. Ты его не видел?"

    "Милиционер протянул мне фотографию."


    window hide
    scene bg fotoboy_man_and with Dissolve(1.5)
    play test_one "sounds/foto.ogg"
    show fotoboy_hand:
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
    window show

    "Рыжий паренёк лет восьми был запечатлён на фоне ковра. Он держал на руках полосатую кошку и широко улыбался."

    voice "voice/anton/1day/018. Net.ogg"
    Ant "Нет."
    voice "voice/tihonov/1day/01 T.ogg"
    Mil "Точно? Посмотри внимательнее."
    voice "voice/anton/1day/019. Gde mn.ogg"
    Ant "Где мне его видеть? Я тут никого не знаю, да и из дома-то почти не выхожу."
    voice "voice/tihonov/1day/02 T.ogg"
    Mil "А может, видел в окно?"
    voice "voice/karina/25 K.ogg"
    Mam "Да! У тебя ведь окна на лес."

    "В окно..."

    window hide
    play test_one "sounds/flashback.ogg"
    show bg_white with Dissolve(0.1)
    show memory_scrimer1
    $ renpy.pause(1.2, hard=True)
    hide memory_scrimer1
    hide bg_white with Dissolve(0.1)
    window show

    voice "voice/anton/1day/020. Net. N.ogg"
    Ant "Нет. Не видел."

    show fotoboy_hand:
        linear 1.5 xpos 800 ypos 500 rotate 50
        linear 0.2 ypos 600

    voice "voice/tihonov/1day/03 T.ogg"
    Mil "Ясно."

    "Голос его был усталым, а вот взгляд..."
    "Долгий, невыносимо тяжёлый. Он смотрел на меня так, будто в чём-то подозревал."
    "Его тень падала на меня, и я невольно ссутулился под весом смутной вины."

    scene bg door_police with Dissolve(1.0)

    "Наконец, оторвав от меня взгляд, милиционер бегло осмотрел прихожую, лестницу и трещины на потолке, которые я почему-то до сих пор не замечал."

    voice "voice/tihonov/1day/04 T.ogg"
    Mil "Вы, кстати, как на новом месте? Попривыкли уже?"
    voice "voice/karina/26 K.ogg"
    Mam "Понемногу. Только вот дочка маленькая по городу скучает..."
    voice "voice/tihonov/1day/05 T.ogg"
    Mil "Скучает, значит... Из местных вас никто не беспокоит?"
    voice "voice/karina/27 K.ogg"
    Mam "Всё хорошо, спасибо."

    scene bg fotoboy_man with Dissolve(1.0)

    "Карие глаза милиционера вновь впились в меня, от чего голова закружилась."

    voice "voice/anton/1day/021.Mozhet.ogg"
    Ant "Может, вам помочь как-то?"

    "Я спросил неуверенно, чтобы показать себя воспитанным мальчиком и просто скорее закончить неприятный разговор."

    voice "voice/tihonov/1day/08 T.ogg"
    Mil "Я вот стою и думаю..."
    voice "voice/tihonov/1day/09 T.ogg"
    Mil "Ты, малец, на племяша моего похож."
    voice "voice/tihonov/1day/10 T.ogg"
    Mil "Шустрый парнишка, твоих лет, с такими же окулярами. Всё книжками зачитывался, детективами..."
    voice "voice/tihonov/1day/11 T.ogg"
    Mil "Когда летом погостить приезжал, говорит, что в школу милиции мечтает поступить."
    voice "voice/tihonov/1day/12 T.ogg"
    Mil "Как я, хотел людям помогать, смекаешь?"

    "Мне стало неловко. Будто передо мной стоял не участковый, а кто-то из дальних родственников."

    voice "voice/tihonov/1day/13 T.ogg"
    Mil "Ох, ребятушки..."
    voice "voice/tihonov/1day/14 T.ogg"
    Mil "Сидите-ка вы лучше дома, не ввязывайтесь ни во что. Жизнь сейчас совсем другая пошла."

    "Мамин голос был холоден:"

    scene bg door_police with Dissolve(1.0)

    voice "voice/karina/28 K.ogg"
    Mam "Мне ли не знать?"
    voice "voice/tihonov/1day/16 T.ogg"
    Mil "Ну да ладно..."
    voice "voice/tihonov/1day/17 T.ogg"
    Mil "Ты, Антон, в каком классе учишься?"
    voice "voice/anton/1day/022.V shesto.ogg"
    Ant "В шестом."
    voice "voice/tihonov/1day/18 T.ogg"
    Mil "Друзей-то на новом месте ещё не завёл?"
    voice "voice/anton/1day/023. Poka n.ogg"
    Ant "Пока нет. Я только после каникул в школу пойду."
    voice "voice/tihonov/1day/20 T.ogg"
    Mil "Тогда вот вам на всякий случай мой номер. Звоните, если... Если узнаете что..."

    scene bg door_open with Dissolve(1.0)

    "Милиционеры ушли, унеся с собой тени, запах дешёвого одеколона и фотографию улыбающегося мальчика."

    stop fon fadeout 0.5
    play test_one "sounds/Door_close.ogg"
    scene bg door with Dissolve(0.5)

    show bunny_nightmare_bg:
        parallel:
            alpha 0
            linear 1 alpha .65
    show vova_foto1:
        subpixel True
        align (.5, .5)
        parallel:
            ease 2.0 xoffset 5 yoffset 0
            ease 2.0 xoffset -5 yoffset -5
            ease 2.0 xoffset 0 yoffset 5
            repeat
        parallel:
            alpha 0
            linear 1 alpha .65
    "Но его лицо всё ещё стояло перед моими глазами."
    "Я думал, каково ему сейчас там, совсем одному."

    show bunny_nightmare_bg:
        linear 1 alpha 0
    show vova_foto1:
        linear 2 alpha 0
    "«Там» – почему-то я представлял лес, качающийся на ветру."
    "Каково его бедным родителям?"

    scene bg kitchen1_2
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.5)

    "И что бы делали мои, если б пропал я?"
    "Плакали? Бились в истерике?"

    stop music fadeout 5.0

    "Или обвиняли бы друг друга, как обычно, а со временем и вовсе забыли."

    voice "voice/anton/1day/024. Mam a.ogg"
    Ant "Мам, а Вова этот в нашем лесу заблудился?"
    voice "voice/karina/29 K.ogg"
    Mam "Выходит, что так. Бедный ребёнок."

    scene bg kitchen_window2 with Dissolve (0.3):
        xalign 0.5
        yalign 0.5
        yoffset 100
        xoffset 100
        zoom 1.0
        linear 8.00 yoffset 0 xoffset 0 zoom 0.67
    play music "music/10_Where Everything Ends.ogg" fadein 3.0

    "Я выглянул в окно на дорогу."

    $ add_text_to_dictionary(2)

    "Милицейский {u}УАЗик{/u} укатил к деревне."
    "Ковыряя расслоившуюся краску подоконника, я почему-то подумал о племяннике участкового."

    $ add_text_to_dictionary(3)

    "Тут же вспомнились детские детективы из серии {u}«Чёрный котёнок»{/u}, которые я сам прочитал за лето."
    "В них обыкновенные школьники расследовали разные таинственные дела."
    "Они искали улики, шпионили за всякими подозрительными людьми."
    "А после захватывающих приключений – бац! - и раскрывали запутанное дело."
    "Становились местными знаменитостями, и, должно быть, родители ими страшно гордились."
    "Я заметил оставленную милиционерами цепочку следов, ведущую к лесу."
    "И тут в голове будто щёлкнуло:"
    "а почему бы не начать собственное расследование?"
    "Может, найду пропавшего мальчика!"
    "А там и награду дадут! Вот Оля обрадуется!"

    scene bg kitchen1_2
    show Mom Normal m_day 01 norm aside at mom_right
    with Dissolve(0.5)

    "И не только Оля. Мама с папой..."
    "Вдруг они на время забудут про свои перепалки?"
    "Может, мне даже удастся спасти нас от слова на букву «р»?"

    scene bg door with Dissolve(0.5)

    "Одеваясь, я фантазировал, как куплю Оле «Тамагочи», а себе — плеер и много-много кассет..."
    "А ещё целую коробку «Киндер Сюрпризов»."
    "Когда в последний раз родители покупали нам игрушки?"

    $ add_text_to_dictionary(4)

    "Осенью, кажется. Тогда папа потерял работу – ту самую, о которой пелось в навязчивой {u}песне{/u}."
    "Я смутно представлял, чем занимаются бухгалтера. Считают деньги вроде."
    "Раньше соседи завидовали нам."
    "Теперь у родителей едва хватало на сладости, и один шоколадный батончик папа делил поровну - мне и Оле."
    "Бывало, я отдавал ей и свою порцию."
    "Как бы сильно мне ни хотелось сладкого, она же малявка."
    "Не терпелось скорее отправиться на поиски улик."

    stop music fadeout 5.0

    voice "voice/anton/1day/025. Poidu.ogg"
    Ant "Пойду погуляю!"

    play test_one "sounds/steps/mam_in.ogg"
    show Mom Angry m_day 01 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    voice "voice/karina/30 K.ogg"
    Mam "Ага, сейчас."
    voice "voice/karina/31 K.ogg"
    Mam "Чтобы потом милиционеры с твоей фотографией по домам ходили?"
    voice "voice/karina/32 K.ogg"
    Mam "Лес вон какой густой..."
    voice "voice/karina/35 K.ogg"
    Mam "А если мальчика звери дикие утащили? Или того хуже?"

    "«Того хуже», - пронеслось эхом по коридору."

    voice "voice/anton/1day/026. Da ja r.ogg"
    Ant "Да я рядом буду. В лес не пойду..."
    voice "voice/karina/33 K.ogg"
    Mam "Что я тебе сказала?! Мне дважды повторять?"

    hide Mom
    show Mom Normal m_day 01 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    voice "voice/karina/37 K.ogg"
    Mam "Лучше портфель собери или с Олей поиграй."

    window hide
    play test_one "sounds/steps/mam_out.ogg"
    hide Mom
    show Mom Normal m_day 01 norm aside:
        xpos -100 ypos 0 xzoom -1.0
        alpha 1.0
        linear 0.5 alpha 1.0 xpos 40-200 ypos 20
        linear 0.5 alpha 1.0 xpos -20-200 ypos 0
        linear 0.5 alpha 0.5 xpos -70-200 ypos 20
        linear 0.5 alpha 0.0 xpos -100-200 ypos 0
    $ renpy.pause(1.0, hard=True)
    window show
    play test_two "sounds/Water-fix-2.ogg"

    "Через секунду на кухне зашумела вода."
    "Это означало, что спор окончен, последнее слово остаётся за мамой."
    play music "music/15_Zaychik_Fon.ogg" fadein 5.0
    $ music_during_lines = 0.5

label bunny_hall_day1_prepare:
    $ story_manager.MarkEvent(("day1", "la hall"))
    $ SceneFlags.Reset()


label bunny_hall_day1:
    window hide
    scene bg door with Dissolve(0.5)
    call screen hall_day_1
    window show


    $ story_manager.MarkEvent(("day1", "la hall", "door"))
    if not SceneFlags.Seen("door tried"):
        voice "voice/karina/41 K.ogg"
        Mam "Антон!"
        voice "voice/karina/K.ogg"
        Mam "Сейчас ремня получишь! Ни шагу за порог!"
    else:
        "Маму надо как-то отвлечь, иначе заругает и папиного ремня всыпет."

    jump bunny_hall_day1

label bunny_pantry_day1:
    $ story_manager.MarkEvent(("day1", "la hall", "pantry"))
    play test_one "sounds/pantry-door-open-1.ogg"
    show open_pantry with Dissolve(0.2)
    window show
    if SceneFlags.Has("mom talked"):
        "На это нет времени, мама скоро вернётся."
    elif SceneFlags.Seen("kladovka"):
        play test_one "sounds/pantry-door-open-1.ogg"
        show open_pantry with Dissolve(0.2)
        voice "voice/karina/05 K.ogg"
        Mam "Антон! Брысь из кладовки, кому говорю?!"
    else:
        "Тёмная душная кладовка."
        "Мама говорит, внутри пахнет мышами, но откуда ей знать, как они пахнут?"
        "Ей ужасно не нравится, когда я суюсь туда, боится, что порежусь о лезвие недавно заточенного топора."
        "А Олю вообще не заманишь в кладовку. Она считает, что там живёт Бабай."
        "Я как-то пытался побороть её страхи: отворил дверь, включил тусклую лампу, мол, смотри, ничего нет — только паутина, папины инструменты и исцарапанные стены."
        "Не поверила."
        "А мне нравится прятаться в шкафу, слушать, как Оля считает снаружи: «Три, четыре, пять, я иду искать»."
        "И бредёт, скрипя половицами, робко надеясь, что не придётся соваться за мной в тесное логово страшилы."
        $ true_detective_count1 += 1

    play test_one "sounds/pantry-door-close-1.ogg"
    hide open_pantry with Dissolve(0.2)
    jump bunny_hall_day1


label bunny_hall_cross:
    $ story_manager.MarkEvent(("day1", "la hall", "cross"))
    play test_one "sounds/cross-1.ogg"
    window show
    if SceneFlags.Has("mom talked"):
        "На это нет времени, мама скоро вернётся."
    elif SceneFlags.Seen("krest"):
        "Чёрный крест."
    else:
        "Это распятье видело стольких людей, входящих в дом и уходящих из него навсегда."
        "Чёрное, словно впитавшее в себя все людские пороки за долгие годы под этой крышей."
        "После смерти бабушки мама собиралась снять его и повесить над дверью подкову – на счастье. Но поранилась об острый угол креста и чуть не свалилась со стула."
        "Папа назвал это знамением и наказал оставить распятье на его законном месте."
        $ true_detective_count1 += 1

    jump bunny_hall_day1

label bunny_hall_ula:
    $ story_manager.MarkEvent(("day1", "la hall", "ula"))
    play test_one "sounds/yula-3.ogg"
    window show

    if SceneFlags.Has("mom talked"):
        "На это нет времени, мама скоро вернётся."
    elif SceneFlags.Seen("yula"):
        "Олина игрушка."
    else:
        "Мамина юла. Семейная реликвия."
        "Маленькая мама играла с ней, а потом подарила мне."
        "После меня волчка по наследству крутила Оля."
        "Всматривалась в танцующее веретено, словно хотела увидеть там что-то: сказочный сюжет или, может, наше будущее."
        "Теперь и сестрёнка слишком взрослая для старой писклявой юлы."
        $ true_detective_count1 += 1

    jump bunny_hall_day1

label bunny_hall_telephone:
    $ story_manager.MarkEvent(("day1", "la hall", "phone"))
    play test_one "sounds/phone-drop-1.ogg"
    window show
    if SceneFlags.Has("mom talked"):
        "На это нет времени, мама скоро вернётся."
    elif SceneFlags.Seen("phone"):
        voice "voice/karina/Anton otoidi ot tel.ogg"
        Mam "Антон! Отойди от телефона."
    else:
        "Родители запрещают мне звонить по межгороду, а так хочется иногда услышать старых друзей."
        "Бывает, я просто снимаю трубку, слушаю тихое уханье зуммера и далёкий треск, – кажется, будто ветер воет в обледеневших проводах."
        $ true_detective_count1 += 1

    jump bunny_hall_day1



label bunny_day1_kitchen:
    $ story_manager.MarkEvent(("day1", "la kitchen"))
    window hide
    if not Flags.Has("number"):
        scene bg kitchen1_2
    else:
        scene bg kitchen1_3
    if Flags.Has("kalendar"):
        show kalendar_08
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
    with Dissolve(0.5)

    hide Mom
    call screen kitchen_day_1


label bunny_come_fridge:
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    play test_one "sounds/refrigerator-long-2.ogg"
    scene bg fridge0 with Dissolve(0.5)
    jump bunny_kitchen_m

label bunny_kitchen_kalendar:
    $ story_manager.MarkEvent(("day1", "la kitchen", "calendar"))
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    if SceneFlags.Has("mom talked"):
        window show
        "На это нет времени, мама скоро вернётся."
    elif Flags.Seen("kalendar"):
        play test_one "sounds/ka2-fix-1.ogg"
        window show
        "Я к нему больше не притронусь."
    else:
        play test_one "sounds/ka2-fix-1.ogg"
        window show
        "Ветхий, покрытый пятнами календарь когда-то был моим любимым развлечением в доме бабули..."
        "Помню, как просыпался и первым делом бежал на кухню оторвать листок с ушедшей датой, словно от меня зависело, настанет новый день или заплутает где-то в таёжном лесу."
        "На сутки ближе к долгожданному Новому году. На сутки ближе к бабушкиным похоронам..."
        "К этому старому календарю я не прикасался уже много лет."
        "С тех пор как описания на обратной стороне сменились с забавных пословиц и примет на тёмные и мрачные, вгоняющие меня в необъяснимое уныние заговоры на смерть."

        play test_one "sounds/Kal_paper-cut.ogg"
        window hide
        $ renpy.pause(0.2)
        show kalendar_08 with Dissolve(0.3)
        window show

        "Я с осторожностью взял пыльную страницу календаря и без труда сорвал её."
        "К сожалению, жуткие описания из детства так никуда и не пропали:"
        "“Везут бревно на семи лошадях, \n Если семь не повезут — восьмую подпрягут,"

        "Далеко увезут и назад не привезут! \n Это сбудется да не минуется.”"


        play test_one "sounds/Kal_paper-crumpling.ogg"

        "Я скомкал серый лист и швырнул его в мусорное ведро в надежде поскорее избавиться от нахлынувшей на меня тревоги."
        "Она расползалась как чернильное пятно по промокашке..."
        $ true_detective_count1 += 1
    jump bunny_day1_kitchen

label bunny_kitchen_radio:
    $ story_manager.MarkEvent(("day1", "la kitchen", "radio"))
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    $ stop_music()
    if SceneFlags.Has("mom talked"):
        window show
        "На это нет времени, мама скоро вернётся."
    elif not SceneFlags.Seen("radio 0"):
        play test_one "sounds/radio-long-1.ogg"
        window show
        play test_one "sounds/01 MCHS Rossii.ogg"
        "Радио" "...МЧС России объявило экстренное предупреждение из-за неблагоприятных погодных условий."
        play test_one "sounds/02 Po prognozu.ogg"
        "Радио" "По прогнозу синоптиков, к региону приближается циклон, из-за которого ожидается сильный снег, метель, снежные заносы на дорогах."
        play test_one "sounds/03 Budte.ogg"
        "Радио" "Будьте осторожны и берегите себя."
        $ true_detective_count1 += 1
    elif not SceneFlags.Seen("radio 1"):
        play test_one "sounds/00 razdva_radio.ogg"
        $ renpy.pause(27.0)
        stop test_one
    else:
        play test_one "sounds/01 razdva_radio.ogg"
        $ renpy.pause(30.0)
        stop test_one
        $ radio_hidden_message = True
        $ achievement_grant("ach_radio")
    $ play_music()
    jump bunny_day1_kitchen

label bunny_kitchen_gazeta:
    $ story_manager.MarkEvent(("day1", "la kitchen", "crossword"))
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    window show
    if SceneFlags.Has("mom talked"):
        "На это нет времени, мама скоро вернётся."
    elif SceneFlags.Seen("gazeta"):
        play test_one "sounds/gaz-fix-2.ogg"
        "Девять букв по вертикали: так филистимляне называли божество, которое защищало их от укусов ядовитых змей и носило прозвище «Повелитель мух»."
    else:
        play test_one "sounds/gaz-fix-2.ogg"
        "Я тайком заглянул в мамин кроссворд. Она очень сердилась, когда кто-то давал ей подсказки, и мы с папой обожали делать вид, будто знаем правильный ответ и вот-вот назовём его."
        "Я улыбнулся мимолётному воспоминанию..."
        "Девять букв по вертикали: так филистимляне называли божество, которое защищало их от укусов ядовитых змей и носило прозвище «Повелитель мух»."
        "Вторая буква - «е»."
        "Хм..."
        $ true_detective_count1 += 1
    jump bunny_day1_kitchen

label bunny_kitchen_m:
    if not SceneFlags.Has("mom talked"):
        window show
        if not SceneFlags.Seen("number tried"):
            "Боковина старенького холодильника «Океан» была усеяна моими детскими рисунками, мамиными рецептами и разнообразными наклейками от жвачек с динозаврами, которых так любила Оля."
            "Посреди такого натюрморта красовался тетрадный лист в клеточку с номером телефона нашего участкового."
            "«Старший лейтенант Тихонов», - прочитал я про себя, глядя на размашистый почерк милиционера."
            "Лист удерживали два кусочка сломанного магнита из какой-то старой советской игрушки, и словно специально, чтобы подразнить меня, чуть-чуть прикрывали цифры."
            "Я потянулся разрушить эту тайну, забрать листок в надёжный тайник — там номер будет ждать своего часа, когда я, наконец, разыщу Вову и первым позвоню в милицию с радостной вестью."

            voice "voice/karina/38 K.ogg"
            Mam "Антон!"

            "Мама с укором посмотрела на меня."

            voice "voice/karina/42 K.ogg"
            Mam "Зачем тебе? Не трогай — потеряешь же."

            "Меньше всего мне хотелось сейчас злить маму, и я покорно опустил руку."
        else:
            "Так просто не получится."
    else:
        $ renpy.pause(1.0)
        play test_two "sounds/paper-take-6.ogg"
        $ achievement_grant("ach_number")
        jump bunny_come_list
    jump bunny_day1_kitchen

label bunny_come_list:
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    $ Flags.Raise("number")
    $ story_manager.MarkEvent(("day1", "la kitchen", "number"))
    scene bg fridge1 with Dissolve (0.5)
    call screen take_list1
    jump bunny_day1_kitchen

label bunny_hall_day1_transition:
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    jump bunny_hall_day1
label bunny_in_fridge_transition:
    if not SceneFlags.Has("mom talked"):
        show Mom Normal m_day 01 norm aside at mom_left
        with None
    jump bunny_in_fridge1

label bunny_in_fridge1:
    if SceneFlags.Has("mom talked"):
        window show
        "На это нет времени, мама скоро вернётся."
        jump bunny_day1_kitchen
    else:
        $ story_manager.MarkEvent(("day1", "la fridge"))
        scene bg in_fridge1 with Dissolve (0.5)
        call screen in_fridge_screen1

label bunny_in_fridge2:
    $ story_manager.MarkEvent(("day1", "la fridge", "freezer"))
    scene bg in_fridge2 with Dissolve (0.5)
    if SceneFlags.Seen("pelmeni"):
        "Суповой набор и пачка пельменей."
        play test_one "sounds/freezer-close-1.ogg"
    else:
        $ add_text_to_dictionary(5)
        "Когда-то бабушка хранила здесь мороженое для меня и Оли, а теперь тут только суповой набор да слипшиеся {u}пельмени{/u}. Как же они осточертели..."
        play test_one "sounds/freezer-close-1.ogg"
        $ true_detective_count1 += 1
    jump bunny_in_fridge1


label bunny_talk_m_in_kitchen1:
    show Mom Normal m_day 08 norm2 ahead at mom_left
    with None

    window show

    voice "voice/karina/A.ogg"
    "Лгать маме было нелегко, но иначе сбежать из дома не получилось бы." id bunny_talk_m_in_kitchen1_c1237f2d
    voice "voice/anton/1day/027.Mam tam.ogg"
    Ant "Мам, там что-то с телевизором случилось."
    voice "voice/anton/1day/027.Kartink.ogg"
    Ant "Картинка какая-то тусклая и экран весь в полосах..."

    show Mom Normal m_day 09 norm ahead at mom_left
    with Dissolve(.3)
    "Мама резко изменилась в лице."

    voice "voice/karina/45 K.ogg"
    Mam "Без ножа меня режешь! Дострелялся в уток своих?"
    voice "voice/karina/46 K.ogg"
    Mam "Говорила же, посадите мне кинескоп своей приставкой."
    voice "voice/karina/47 K.ogg"
    Mam "Где мы теперь мастера найдём в дыре этой, а?"
    voice "voice/anton/1day/028. Mozhe b.ogg"
    Ant "Может быть, просто настройки сбились?"
    voice "voice/anton/1day/028. Shodi.ogg"
    Ant "Сходи посмотри, пожалуйста."
    voice "voice/karina/48 K.ogg"
    Mam "Хм, нормально же работал с утра."
    voice "voice/anton/1day/029. Izza.ogg"
    Ant "Из-за снегопада, наверное, неполадки."

    "Мама вытерла руки о фартук и, хмурясь, отправилась в комнату Оли."

    $ SceneFlags.Raise("mom talked")
    play test_one "sounds/steps/mam_out.ogg"
    hide Mom with Dissolve(0.5)
    jump bunny_day1_kitchen



label bunny_day1_open_door:
    $ story_manager.MarkEvent(("day1", "scene4"))

    stop music fadeout 5.0
    play test_one "sounds/Door_open.ogg"
    play fon "sounds/fon/crow_wind.ogg" fadein 1.0 loop
    scene bg door_open with Dissolve (0.5)
    show bg_white with Dissolve(1)
    scene bg house_day with Dissolve(1)
    window show

    play test_two "sounds/steps_snow001.ogg"

    "Я открыл калитку и вышел в поле."
    "Осторожно, чтобы мама не увидела меня из окон."
    "Когда я преодолел половину пути до леса, сугробы доходили до колен."
    "Вспомнились ночные страхи."

    window hide
    play test_one "sounds/flashback.ogg"
    show bg_white with Dissolve(0.1)
    show memory_scrimer1
    $ renpy.pause(1.2, hard=True)
    hide memory_scrimer1
    hide bg_white with Dissolve(0.1)
    window show
    "Примерно здесь я видел те силуэты."
    "Здесь они кувыркались, прыгали, хороводили."

    play music "music/12_Disaster_pt0.ogg" fadein 12.0
    $ music_during_lines = 1.0
    "Музыка заиграла в подсознании, гипнотизирующая и влекущая."
    "При свете дня те далёкие фигуры казались просто сном."
    "Солнце испепелило кошмары, но осталось послевкусие: отдалённый звон в ушах, изломанные тени, ползущие передо мной по снегу."
    "И чуть слышный шепоток в голове. Неясный, почти ласковый."

    scene bg forest0_long:
        xalign 0.0
        yalign 0.5
    show snow_for_forest0
    with Dissolve(1)

    "Было тихо."
    "Так тихо, будто в мире не осталось больше ничего."
    "Ни земли, ни неба, ни родителей, ни Оли."
    "Будто время закончилось, упёрлось в тупик, в частокол из сосен."
    "Тишина порой бывает страшнее криков."
    "Родители кричали друг на друга, и мы с Олей каменели, прислушиваясь к перепалкам."

    scene koshmar onlayer master1:
        matrixcolor InvertMatrix(1.0)
    show layer master1:
        alpha 0.65
    with Dissolve(.5)
    "Но потом наступила оглушающая тишина."
    "Квартира онемела за несколько дней до нашего переезда."


    show d5_killer_p_fin_dad onlayer master1 with Dissolve(.5):
        xpos 950
        yoffset 75
    show d5_killer_p_fin_mom onlayer master1 with Dissolve(.5):
        xpos 200
        yoffset 75
    "И уже вспоминалось с трудом, точно это было в прошлой жизни, что когда-то мама с папой шутили, смеялись, проводили много времени вместе."


    show d5_killer_p_fin_olya onlayer master1 zorder 5 with Dissolve(.5):
        align (.5, .5)
        zoom 1.0
        xoffset 0
        yoffset 150
    "А когда целовались при Оле, она всегда морщилась и забавно фыркала."

    scene onlayer master1
    scene bg_black
    with Dissolve(1.0)
    "В один день всё изменилось."
    "Нечто важное ушло из нашего дома."
    "А что-то страшное заполнило образовавшуюся пустоту."

    scene ramka onlayer master1
    scene d5_mpol_ref_nmare3_poltalk_bg:
        align (.5, 1.)
        zoom 1.0
        xzoom -1
    show bunny_nightmare_bg:
        alpha .25
    show sparks_01:
        contains tr_sparks_halfhigh("sparks_2", stable=1., disap=0.25)
    show sparks_02:
        contains tr_sparks_halfhigh("sparks_2", xal=0.25, delay=0.5, stable=1., disap=0.25)
    show sparks_03:
        contains tr_sparks_halfhigh("sparks_2", xal=0.65, delay=1.5, stable=1., disap=0.25)
    show sparks_04:
        contains tr_sparks_halfhigh("sparks_3", xal=0.25, delay=0.5, stable=1., disap=0.25)
    show sparks_05:
        contains tr_sparks_halfhigh("sparks_3", xal=0.85, delay=2.5, stable=2., disap=0.25)
    show sparks_06:
        contains tr_sparks_halfhigh("sparks_4", xal=0.45, delay=0.25, stable=0.75, disap=0.25)
    show sparks_07:
        contains tr_sparks_halfhigh("sparks_4", xal=0.15, stable=0.75, disap=0.25)
    show sparks_08:
        contains tr_sparks_halfhigh("sparks_3", xal=0.05, stable=0.5, disap=0.75)

    show sparks_1:
        xpos 0
        pause 3.4
        xpos -800
        pause 3.4
        alpha 0
        xpos 500
        pause 3.4
        alpha 1
        repeat

    show sparks_1 as sparks_0_2 zorder 1:
        pause 3.4
        alpha 0
        pause 3.4
        alpha 1
        xpos 500
        pause 3.4
        alpha 0
        repeat

    show layer master:
        align (.5, .85)
        zoom 1.00
        parallel:
            linear .1 matrixcolor BrightnessMatrix(-0.01)
            linear .1 matrixcolor BrightnessMatrix(0.0)
            linear .1 matrixcolor BrightnessMatrix(-0.01)
            linear .1 matrixcolor BrightnessMatrix(0.0)
            linear .1 matrixcolor BrightnessMatrix(-0.02)
            linear .1 matrixcolor BrightnessMatrix(0.0)
            repeat

    with Dissolve(.5)
    "Словно вспыхнул пожар, и родители среди ночи впопыхах собирали вещи, спасая себя и нас."
    "От кого?"
    "Не от тех ли людей, что иногда появлялись в нашем прежнем доме, людей с ледяными, как у мертвецов, глазами?"

    scene day1_worms:
        align (.5, .5)
        zoom 1.05
        block:
            yoffset 0
            .75
            yoffset 10
            .05
            yoffset 0
            .05
            yoffset 10
            .05
            repeat
    show bg_black:
        alpha .15
        .05
        alpha .0
        .05
        repeat
    with Dissolve(.5)
    "Будто они во всём видели лишь клубки червей на чёрной земле."

    scene d5_police_flash_fon
    show d5_police_flash
    show d4_noise
    show bg_black:
        alpha .15
        .05
        alpha .0
        .05
        repeat
    with Dissolve(.5)
    "А где-то далеко, предупреждая о надвигающейся опасности, надрывалась сирена."

    show layer master:
        subpixel True
        align (.5, .5)
        easeout 10 zoom 2.0
    "..."


    scene bg_white onlayer master1
    with Dissolve(.15)

    scene onlayer master1
    scene day1_frostforest_bg
    show day1_frostforest_anton:
        0.1
        linear .1 yoffset 20
        ease .5 yoffset 0
    with Dissolve(0.15)
    "Я вздрогнул, прогоняя наваждение, и осмотрелся."
    "Только я, это белое поле и ветер, что гонял по снегу ледяную пыль и хвосты пороши."
    "Щурясь от солнца, я осмотрел лес, где царил мрак."
    "На фоне ослепительной белизны он был необычайно тёмен."
    "Узловатые корневища змеились под снегом."
    "Прелая листва и хвойные иглы вмёрзли в лёд."

    scene bg forest0 with Dissolve(1)

    "Сухие колючие ветки переплетались, навевая неуютные мысли о решётках."
    "Защищают ли они лес?"
    "Или, наоборот, удерживают нечто внутри?"
    "На одной из острых веток что-то висело."


    $ story_manager.MarkEvent(("day1", "scene5"))
    scene bg forest1_anton
    show mid b000:
        xpos -240
    show snow_for_forest1_anton
    with Dissolve(1)

    "Увязая в сугробах, я пробрался ближе, почти к самой границе леса, и увидел вязаную варежку."
    "Точно раненая птица среди изголодавшихся потёмок."
    "Может, отнести её милиционерам?"

    $ add_text_to_dictionary(6)

    "Их старший, хоть и выглядел угрюмо, напомнил мне капитана Казанову из моего любимого сериала {u}«Улицы разбитых фонарей»{/u}."
    "Такой же полный тревоги, с усталым взглядом, но при этом храбрый и сильный."
    "Поможет ли ему варежка найти пропавшего мальчика?"

    play test_three "sounds/1.vova01-echo.ogg"

    "Во-о-о-ва-а-а!"
    "Послышался далёкий крик. Кажется, у реки."

    play test_four "sounds/2.vova03-echo.ogg"

    "Во-о-о-ва-а-а!"
    "Словно сами деревья звали кого-то."

    scene forest1_A1_bigplan with Dissolve(0.5)
    play test_five "sounds/3.vova02-echo.ogg"

    "«Во-ва!», — подхватили уже ближе."
    "Там, за деревьями, кто-то стоял."
    "Хоронился."

    play test_six "sounds/4.vova04-echo.ogg"

    "Во-ва!"

    scene bg forest0 with Dissolve(1)

    "Я понимал: скорее всего, кто-то ищет пропавшего мальчика, но всё же..."
    "Было что-то странное в той фигуре."
    "В её неподвижности, в том, как она неестественно клонилась к земле."
    "В её черноте."

    scene bg forest1_anton
    show mid b000:
        xpos -240
    show snow_for_forest1_anton
    with Dissolve(1)

    "Там никого нет. Лишь ветки и корни."
    "Просто моё воображение."

    play test_one "sounds/flapping-1.ogg"

    "Где-то громко захлопала крыльями птица."

    window hide
    play test_two "sounds/sub-drum-4.ogg"
    play test_one "sounds/steps_snow001.ogg"
    show mid b001:
        xpos -240
        linear 0.4 xpos -750
    $ renpy.pause(0.5)
    hide mid b001
    window show

    "От дерева отделилась тень и скрылась из виду."
    "Я на секунду отвлёкся, а когда вновь посмотрел на то же место... фигуры уже не было."

    scene forest1_A2_bigplan with Dissolve(0.5)

    "Померещилось."
    "Долго, очень долго стояла тишина."

    window hide
    show bg forest0_long:
        xpos 0 alpha 0.1
        parallel:
            linear 9.5 xpos -1213
        parallel:
            linear 1.0 alpha 1.0
    $ renpy.pause(9.0)
    window show

    "Мускулы мои были напружинены, сердце грохотало в горле."
    "Любой шум, малейший намёк на движения, шепоток из чащобы – и я брошусь бежать."
    "Но ничего не происходило."

label main_choose2:
    scene bg forest1
    show mid ant_for_forest1
    show snow_for_forest1_anton onlayer screens
    with Dissolve(1)
    stop music fadeout 2.0
    stop fon fadeout 3.0
    "Я вновь посмотрел на варежку."
    $ story_manager.MarkEvent(("day1", "glove"))



    window hide
    hide mid ant_for_forest1

    $ renpy.call_screen('forest1_screen', _layer='master')


label run_anton:
    $ story_manager.MarkEvent(("day1", "glove", "run"))

    show mid ant_for_forest1
    window show
    play music "music/14_Disaster_pt3-loop.ogg"

    "Комья снега сорвались с ветвей, и этот звук напомнил мне шорох земли, которая падает в яму, на крышку гроба."
    "У меня закружилась голова, будто я и правда балансировал на краю пропасти."

    play test_one "sounds/snow_step_slow.ogg"

    "Я медленно попятился от находки."

    show mid ant_for_forest2 with Dissolve(1)

    "Казалось, как только я коснусь её, захлопнется капкан."
    "Мышка окажется в мышеловке."
    "Кто-то прошёл по льду в метрах трёх от меня."
    "Внутренний голос прошептал:"

    Ant_m "«Спасайся! Сейчас же!»"

    "Нервы сдали."
    "Я побежал, втянув голову в плечи."
    hide snow_for_forest1_anton onlayer screens
    jump run_to_home


label take_anton:
    $ story_manager.MarkEvent(("day1", "glove", "take"))
    $ Flags.Raise("glove")
    play music "music/14_Disaster_pt3-loop.ogg" fadein 1.0

    show mid ant_for_forest1
    show bg_white with Dissolve(1)
    hide snow_for_forest1_anton onlayer screens
    scene bg wood
    show lv1 wood05
    show lv2 wood
    show lv3 wood04
    show lv4 wood
    show lv5 wood03
    show lv6 wood
    show lv7 wood02
    show lv8 wood
    show lv9 wood01
    show varezka1
    with Dissolve(1)

    "Я принял решение снять одинокую варежку с ветки."


    show lv6 chel2:
        xpos 20
        ypos 500+400
        alpha 1.0
        zoom 0.9
        linear 0.4 xpos 370
        linear 0.01 alpha 0.0
    $ random_f_step_sound()
    $ renpy.pause(2.5)

    show lv6 chel2:
        xpos 1880
        ypos 500+400
        alpha 1.0
        zoom 0.9
        xzoom -1.0
        linear 0.2 xpos 1500
        linear 0.01 alpha 0.0
    $ random_f_step_sound()
    $ renpy.pause(1.0)

    play test_three "sounds/5.vova05-echo-.ogg"
    Noname "Во-ова-а-а!"

    $ renpy.pause(1.6)

    show lv6 chel2:
        xpos 690
        ypos 460+400
        alpha 0.95
        zoom 0.8
        xzoom -1.0
        linear 0.3 xpos 430
        linear 0.01 alpha 0.0
    $ random_f_step_sound()
    $ renpy.pause(1.0)

    show bg_white with Dissolve(0.1)
    show forest1_A2_bigplan with Dissolve(0.1)
    voice "voice/anton/1day/Ah.ogg"
    $ renpy.pause(0.2, hard=True)
    show forest1_A3_bigplan
    hide forest1_A2_bigplan
    hide bg_white
    with Dissolve(0.1)
    $ renpy.pause(0.6, hard=True)
    show bg_white with Dissolve(0.1)
    hide forest1_A3_bigplan
    hide bg_white
    with Dissolve(0.1)

    "Крик прокатился по полю и рассеялся вдали, без эха, без надежды на отклик."

    $ renpy.pause(2.2)
    show lv4 chel2:
        xpos 1250
        ypos 380+400
        alpha 0.9
        zoom 0.8
        xzoom 1.0
        linear 0.2 xpos 1450 zoom 0.8
        linear 0.01 alpha 0.0
    $ random_f_step_sound()
    $ renpy.pause(4.8)
    show lv4 chel1:
        xpos 500
        ypos 650
        alpha 0.9
        zoom 0.85
        linear 0.3 xpos 670
        linear 0.01 alpha 0.0
    $ random_f_step_sound()
    $ renpy.pause(1.0)

    "Шагнув к ощетинившимся деревьям, я попытался снять свою находку."

    play test_two "sounds/steps/steps_snow001.ogg"
    scene bg wood:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv1 wood05:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv2 wood:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv3 wood04:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv4 wood:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv5 wood03:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv6 wood:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv7 wood02:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv8 wood:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show lv9 wood01:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    show varezka1:
        xalign 0.5 yalign 0.5
        ease 0.3 zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.3 zoom 1.1 xalign 0.5 yalign 0.5
    $ renpy.pause(1.0)
    stop test_two fadeout 0.2

    "Она не поддавалась."

    play test_one "sounds/mitten-3.ogg"
    hide varezka1 with Dissolve(0.5)

    "Я потянул сильнее — ветка хрустнула, варежка с чавкающим звуком оторвалась от сучка и осталась у меня в руках."
    "Слишком тяжёлая. Мокрая."
    "Я невольно сжал её, и на снег тонкой струйкой полилось что-то тёмное."
    "Над сугробом заклубился пар."

    scene bg_white with Dissolve(0.5)
    scene bg_handblood
    show handblood_left:
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
    show handblood_right:
        xalign 0.5
        xpos 960
        ypos 1000
        alpha 0.90
        zoom 0.90
        linear 0.5
        linear 0.5 ypos 900 alpha 0.91 zoom 0.91 xpos 965
        linear 0.5 ypos 800 alpha 0.92 zoom 0.92 xpos 960
        linear 0.5 ypos 700 alpha 0.93 zoom 0.93 xpos 965
        linear 0.5 ypos 600 alpha 0.94 zoom 0.94 xpos 960
        linear 0.5 ypos 500 alpha 0.95 zoom 0.95 xpos 965
        linear 0.5 ypos 400 alpha 0.96 zoom 0.96 xpos 960
        linear 0.6 ypos 300 alpha 0.97 zoom 0.97 xpos 965
        linear 0.7 ypos 200 alpha 0.98 zoom 0.98 xpos 960
        linear 0.8 ypos 100 alpha 0.99 zoom 0.99 xpos 965
        linear 0.5 ypos 50 alpha 1.00 zoom 0.995 xpos 962
        linear 0.5 ypos 0 alpha 1.00 zoom 1.00 xpos 960
        block:
            linear 1.0 xpos 965 ypos 10
            linear 1.0 xpos 967 ypos 5
            linear 1.0 xpos 960 ypos 0
            linear 1.0 xpos 958 ypos 5
            linear 1.0 xpos 964 ypos 0
            linear 1.0 xpos 960 ypos 5
            repeat
    with Dissolve(1)

    $ renpy.pause(6.5)

    play test_one "sounds/mitten-4.ogg"

    "Я замер, с отвращением разглядывая ладони."
    "Красные."

    play test_two "sounds/wood-break-1.ogg"

    "Треск веток вторгся в наступившую тишину."

    show bg_white with Dissolve(1)

    scene bg wood
    show lv1 wood05
    show lv2 wood
    show lv3 wood04
    show lv4 wood
    show lv5 wood03
    show lv6 wood
    show lv7 wood02
    show lv8 wood
    show lv9 wood01
    with Dissolve(1)

    "Не раздумывая, я бросился прочь."

    jump run_to_home


label run_to_home:
    $ story_manager.MarkEvent(("day1", "scene6"))
    play test_five "sounds/snow-human-run-2.ogg" loop
    scene bg_white2
    show bg_runaway1:
        zoom 0.9
    show bg_runaway2:
        zoom 0.9
    if Flags.Has("glove"):
        show anton_run_full_speed1
    else:
        show anton_run_full_speed2
    show runaway_snow1:
        zoom 1.1
    show runaway_snow2:
        zoom 1.1
    with Dissolve(1)

    play test_four "sounds/snow-animals-run-1.ogg"
    play sound "voice/anton/1day/029.Beg i o.ogg"

    "Кто-то мчался из темноты, ломая осинник, стремительно сокращая расстояние."
    "Ноги вязли в снегу. В голове метались безумные мысли:"
    "сейчас схватят."
    "Сцапают."
    "Утащат в чащу. Навсегда."
    "Но был другой голос, наверное, голос разума. Он придавал сил, ускорял бег:"
    Ant_m "«Ты сможешь! Не останавливайся!»"

    play test_one "sounds/growl-solo-1.ogg"

    "Позади раздался звериный рык."

    play test_two "sounds/growl-multi-1.ogg"

    "Такой громкий, что уши заложило."
    "Казалось, рычит не одна голодная тварь, а целая стая."
    "Тянет ноздрями морозный воздух и чует мой страх."

    play test_one "sounds/owl-flapping-2.ogg"

    "Сверху захлопали два гигантских крыла."

    play sound "sounds/sfx_whoosh.ogg"

    show d4_road_dark_shadow:
        anchor (0., 0.)
        pos (1., 1.)
        alpha .5
        linear 1 pos (0., 0.) anchor (1., 1.)
    "Огромная тень пронеслась над поляной. Что-то заухало, захрипело."

    play test_two "sounds/roar-mix-1.ogg"

    "Теперь уже рычали со всех сторон."
    "Из сухого малинника. Из-за перекрученных елей. Из-под бурелома."
    Ant_m "«Быстрее, беги! Не оглядывайся!»"
    "Словно в дурном сновидении, снежная поляна стала вязкой, как зыбучие пески."

    stop test_five fadeout 2.0
    scene day1_threshold loop
    show layer master:
        align (.5, .5)
        .25
        block:
            linear 0.1 zoom 1.1
            ease 0.1 zoom 1.
            0.3
            linear 0.1 zoom 1.1
            ease 0.1 zoom 1.
            0.3
            linear 0.1 zoom 1.1
            ease 1.0 zoom 1.
            .4
            repeat

    with Dissolve(.25)
    "Я топтался на одном месте."

    play test_one "sounds/snow-snd-1.ogg"
    "Вырывал ногу из рыхлой ловушки, чтобы попасть в следующую, ещё более глубокую."
    "Я продолжал тонуть, погружался глубже с каждым отчаянным рывком."

    show day1_threshold 4
    show focus_lines onlayer master1:
        align (.5, .5)
        zoom 1.1
        alpha 0
        .25
        alpha 1
        matrixcolor BrightnessMatrix(-1.0)
        parallel:
            .25
            linear .5 alpha 0
        parallel:
            easein .75 zoom 1.0
    with Dissolve(.25)
    "Разве снег умеет так держать?"
    "Я завопил от ужаса, сообразив, что это не снег."
    "Что кто-то в сугробе схватил меня за штанину."

    show layer master:
        align (.5, .5)
        easein .5 zoom 1.2
        easeout .25 zoom 1.
    pause 0.5

    show fox_snowball onlayer master1:
        matrixcolor BrightnessMatrix(-0.05)

    scene day1_threshold 5
    with Dissolve(.25)
    "Собрав все силы в кулак, я ринулся вперёд."

    $ renpy.scene("master1")
    play test_two "sounds/snow-snd-2.ogg"

    "Давление исчезло, и ботинок выскользнул из ямы, подошва оттолкнулась от твёрдой поверхности."

    play test_five "sounds/snow-human-run-2.ogg" loop
    scene bg_white2
    show bg_runaway1:
        zoom 0.9
    show bg_runaway2:
        zoom 0.9
    if Flags.Has("glove"):
        show anton_run_full_speed1
    else:
        show anton_run_full_speed2
    show runaway_snow1:
        zoom 1.1
    show runaway_snow2:
        zoom 1.1
    with Dissolve(0.25)
    "Одним прыжком я достиг расчищенной тропинки и оттуда помчался к дому."

    play fon "sounds/fon/crow_wind.ogg" fadein 1.0
    scene bg house_day:
        align (.5, .5)
        zoom 1.05
        parallel:
            linear .15 yoffset 25 xoffset -10
            linear .15 yoffset 0
            linear .15 yoffset 25 xoffset 10
            linear .15 yoffset 0
            repeat
        parallel:
            easein 10 zoom 1.45
    with Dissolve(1)

    "Его угрюмый фасад уже не казался враждебным."

    play test_seven "sounds/sfx-fast-heartbeat-2.ogg" fadein 3 loop

    "Дом был моей защитой от хлопающих крыльями теней, от ползущих под снегом существ."
    "Я споткнулся о порог и врезался в дверь."

    scene day1_threshold:
        align (.5, .15)
        zoom 0.85
        parallel:
            linear .15 yoffset 25 xoffset -10
            linear .15 yoffset 0
            linear .15 yoffset 25 xoffset 10
            linear .15 yoffset 0
            repeat
        parallel:
            easein 15 zoom 1.25
    with Dissolve(.25)
    "Впопыхах различил на ней царапины."
    "Словно пёс бил лапами по дереву, требуя, чтобы его впустили погреться."
    "Уходя на прогулку, я не заметил этих глубоких рытвин."
    "Стук сердца в ушах заглушал прочие звуки — я не слышал, идёт ли кто за мной."
    "Что, если оно... они уже во дворе, а мама заперла дверь?"
    "Захлёбываясь страхом, я дёрнул ручку — та покорно поддалась."

    window hide

    show layer master:
        align (.5, .5)
        linear 1. align (.5, .0) zoom 1.35

    scene bg_white with Dissolve(1.0)
    stop music fadeout 5.0
    stop test_five fadeout 0.5
    stop fon fadeout 0.5
    stop test_seven fadeout 0.5
    play test_one "sounds/Door_open.ogg"
    scene bg door_open
    show layer master:
        subpixel True
        align (.8, .5)
        zoom 1.3
        parallel:
            easein 1.0 zoom 1.0
        parallel:
            linear .15 align (.8, .5 +0.1)
            linear .15 align (.8, .5)
            linear .15 align (.8, .5 +0.1)
            linear .15 align (.8, .5)
            repeat
    with Dissolve(1.0)

    play test_one "sounds/Door_close.ogg"
    scene bg door with Dissolve(0.25)
    $ renpy.pause(0.3, hard=True)
    play test_five "sounds/run_stop.ogg"
    play test_two "sounds/breathing.ogg" loop
    window show
    stop sound fadeout 1


    voice "voice/anton/1day/016. Otdyshk.ogg"
    "Я ввалился в коридор и тут же захлопнул дверь."

    play test_three "sounds/steps-creak-1.ogg"

    "Доски крыльца тихонько запищали — то преследователи поднялись по ступенькам."
    "У меня соскальзывали пальцы, никак не получалось защёлкнуть замок."

    play test_one "sounds/Door_lock.ogg"

    "Стиснув зубы, я дёрнул железный набалдашник, загоняя запор в проёмы планки."
    "Я таращился на дверь."
    "За преградой, тонкой и жалкой, бесполезнее одеяла, кто-то стоял."
    "Хриплое дыхание проникало в дом и накатывало волнами."
    "Отчётливо пахло хвоей и потом."
    "Мама выглянула из кухни и бесстрастным голосом, каким часто говорила с отцом, отчеканила:"

    voice "voice/karina/50 Chto concr.ogg"
    Mam "Что конкретно тебе не ясно в просьбе «не хлопай дверьми»?"
    voice "voice/anton/1day/030. YA slucz.ogg"
    Ant "Я... Я случайно."

    stop test_two fadeout 5.0
    play music "music/11_Poryadok.ogg" volume 0.8 fadein 5.0

    "Я покосился на дверь — запах исчез, вместе с ним и дыхание. Если там и вправду кто-то дышал."
    "Здесь, в пяти метрах от мамы, страх понемногу ослабевал, таял, как снежок в тепле, а вместе с ним - и остатки сил."

    play test_one "sounds/steps/mam_in.ogg"
    show Mom Normal m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Ноги подогнулись. Я упёрся в стену, чтобы не плюхнуться на пол."

    hide Mom
    show Mom Normal m_day 02 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Вдруг мамино лицо изменилось."
    "Ледяная маска строгости и отстранённости мигом слетела. Мама стала такой же, какой была до всех этих ссор."
    "Она наконец увидела моё состояние, мои облепленные гроздьями снега мокрые штаны."

    voice "voice/karina/51 K.ogg"
    Mam "Ты где был? Я тебе что говорила, а?! Чтобы ты дома сидел!"
    voice "voice/karina/52 K.ogg"
    Mam "Я и для тебя пустое место?"

    "Я испугался, что она расплачется. Потянулся к ней, как в детстве, когда просился на руки."

    hide Mom
    show Mom Normal m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Но мама успокоилась и вновь стала прежней."

    stop music fadeout 10.0

    "Глаза её блеснули сталью. Голос зазвенел."

    voice "voice/karina/53 K.ogg"
    Mam "У отца сигареты пропали."
    voice "voice/karina/54 K.ogg"
    Mam "Признавайся, ты их стащил? Курить бегаешь?"
    voice "voice/anton/1day/031. Tam za.ogg"
    Ant "Там... там з-за мной кто-то гнался, я-я думал, м-меня..."

    "Пытаясь всё объяснить, я начал заикаться."
    "Слёзы подступили к горлу."

    voice "voice/karina/55 K.ogg"

    "Мама склонилась и обнюхала меня по-звериному, выискивая запах табака."

    hide Mom
    show Mom Normal m_day 00 norm aside:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Потом хмуро прищурилась и с недоверием посмотрела во двор."

    show Mom Scared m_day 00 norm aside at sprite_scare:
        xpos -100 ypos 0 xzoom -1.0
    play music "music/3_trouble.ogg" volume 0.8 fadein 5.0
    $ music_during_lines = 0.7

    voice "voice/karina/56 K.ogg"
    "И тут же, изменившись в лице, прикрыла рот ладошкой."
    voice "voice/karina/57 K.ogg"
    Mam "Гляди, вон же они! Прямо у забора!"

    "Сердце лихорадочно забилось, будто я снова был добычей, и загонщики преследовали меня в поле."
    "Я готов был поклясться: снаружи кто-то заскрёбся в дверь. Точь-в-точь как в моём кошмаре."

    show Mom Scared m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Мама поманила пальцем, и я, кое-как набравшись смелости, выглянул в кухонное окно, в лицо своему страху."
    scene bg kitchen_window1:
        xalign 0.5
        yalign 0.5
        yoffset 0
        xoffset 0
        zoom 0.67
        linear 8.00 yoffset 100 xoffset 100 zoom 1.0
    if Flags.Has("myth1"):
        show day1_myth:
            xalign 0.5
            yalign 0.5
            yoffset 0
            xoffset 0
            zoom 0.67
            linear 8.00 yoffset 100 xoffset 100 zoom 1.0
    with Dissolve (0.5)

    play test_one "sounds/dogs_0-fix.ogg"

    "Сквозь зимние узоры на стекле были едва различимы косматые силуэты, барахтавшиеся в снегу."
    "Собаки!"
    "Всего-то мелкая свора дворняг, без имени и хозяина, лишь издалека напоминавшая голодных страшил, живущих у кромки леса."

    scene bg door
    show Mom Normal m_day 04 norm aside:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    voice "voice/karina/59 K.ogg"
    Mam "Божечки, ты их испугался? Да они сами тебя перепугаются, Антон."
    voice "voice/anton/1day/032. Oni gn.ogg"
    Ant "Они гнались за мной... словно за зайцем."
    voice "voice/anton/1day/033. A vdru.ogg"
    Ant "А вдруг они бешеные."

    show Mom Normal m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Улыбка медленно исчезла с маминого лица."
    "И теперь мама смотрела по-другому, словно впервые видела этих собак."

    voice "voice/karina/61 K.ogg"
    Mam "Что если они нападут на Олю?"
    voice "voice/anton/1day/034. Mam G.ogg"
    Ant "Мам?"
    voice "voice/karina/62 K.ogg"
    Mam "Вот бы твой отец их всех перестрелял..."
    voice "voice/anton/1day/035. Mama o.ogg"
    Ant "Мама! Они живые!"
    voice "voice/karina/63 K.ogg"
    Mam "А что?"
    voice "voice/karina/64 K.ogg"
    Mam "Ты уж определись, они тебе друзья или враги."
    voice "voice/karina/64 Ne malenk.ogg"
    Mam "Не маленький ведь уже."
    voice "voice/karina/65 K.ogg"

    "Мама хмыкнула, а мне сделалось невыносимо обидно, да так, что я прикусил губу и уставился в затянутый паучьими тенётами угол."
    "М-да, сыщик из меня никудышный."
    "И рисковал я не жизнью перед чудовищными монстрами, а своими брюками перед блохастой шайкой глупых дворняг."

    if Flags.Has("glove"):
        "И ради чего всё? Сдалась мне эта..."
        "Варежка."
        "Ну, конечно!"
        "В руке чавкнула тёмная липкая рукавица пропавшего мальчика, с которой, как оказалось, я не расставался всё это время."
        "Вот мой козырь настоящего детектива!"
        "Я поспешил предъявить улику маме."

        scene var_in_hand0 with Dissolve(0.5)
        play test_one "sounds/Kapli-fix.ogg" loop

        voice "voice/anton/1day/032. Mam sm.ogg"
        Ant "Мам, смотри, это Вовина варежка!"
        voice "voice/anton/1day/032. Nu tog.ogg"
        Ant "Ну того, про которого утром милиция спрашивала!"
        voice "voice/anton/1day/032. Ona vs.ogg"
        Ant "Она вся в крови! На дереве висела! Вон там, могу показать!"
        voice "voice/anton/1day/032. Davai.ogg"
        Ant "Давай в милицию скорее позвоним, как нас участковый просил..."
        voice "voice/anton/1day/032. Mam gl.ogg"
        Ant "Мам, гляди!"
        voice "voice/karina/66 K.ogg"
        Mam "Фу!"

        "На скривившемся мамином лице появилась тень недоверия."

        stop test_one

        "Словно воспоминание о чём-то давно забытом. Так люди пытаются вспомнить сон, но образы ускользают."

        scene bg door
        show Mom Angry m_day 00 norm ahead:
            xpos -100 ypos 0 xzoom -1.0
        with Dissolve(0.5)

        voice "voice/karina/67 K.ogg"
        Mam "А ну-ка, прекрати сейчас же!"
        voice "voice/karina/68 K.ogg"
        Mam "Оля тебя услышит — с ума сойдёт!"
        voice "voice/karina/69 K.ogg"
        Mam "Она и так не спит, на всё подряд жалуется."
        voice "voice/karina/70 K.ogg"
        Mam "Ещё и ты со своими шуточками!"

        scene var_in_hand1 with Dissolve(0.5)

        "Теперь и я видел, что мокрой варежка была от снега."
        "Никакой крови."

    "От стыда хотелось сквозь землю провалиться."

    scene bg door
    show Mom Angry m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)
    play test_one "sounds/tabl-fix.ogg"

    voice "voice/karina/71 K.ogg"
    Mam "Иди сюда, паникёр..."
    voice "voice/karina/72 K.ogg"
    Mam "Да не стой столбом, вот таблетку на, быстро пей!"

    "На мою ладонь упала золотистая пилюля, напоминающая мёртвую осу."

    voice "voice/anton/1day/033. YA uzhe.ogg"
    Ant "Я уже пил сегодня, за завтраком..."
    voice "voice/karina/73 K.ogg"
    Mam "Попререкайся мне ещё."
    voice "voice/karina/74 K.ogg"
    Mam "Сказала, дома сидеть — нет же..."
    voice "voice/karina/75 K.ogg"
    Mam "Был бы отец - выпорол!"
    voice "voice/karina/76 K.ogg"
    Mam "Сейчас же выпей, а то ночью не уснёшь. Тебе ведь в школу завтра."
    $ music_during_lines = 1.0

    stop music fadeout 10.0
    play test_one "sounds/glotok-fix.ogg"

    "Пришлось проглотить горькое лекарство, запив его не менее противной водой с привкусом хлорки."
    "Может, это была и не Вовина рукавичка."
    "Может, и не рукавичка вовсе."
    "Как и чудовища из леса."
    "И Олина сова..."
    "Я схожу с ума?"

    show door_narco
    hide Mom
    show Mom Angry m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    show Mom_Angry_m_day_00_norm_ahead_narco:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    "Что со мной происходит?"

    play music2 "music/9_Nikita Kryukov - the Obscurity.ogg" fadein 5.0

    "То ли таблетка подействовала моментально, то ли перевозбуждённый мозг не подпускал страх."
    "Пришло спокойствие, зевотное безразличие."

    scene bg door
    show Mom Normal m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    voice "voice/karina/77 K.ogg"
    Mam "Антон! Выпил? Можешь, если захочешь."

    show door_narco
    hide Mom
    show Mom Normal m_day 00 norm ahead:
        xpos -100 ypos 0 xzoom -1.0
    show Mom_Normal_m_day_00_norm_ahead_narco:
        xpos -100 ypos 0 xzoom -1.0
    with Dissolve(0.5)

    voice "voice/karina/78 K.ogg"
    Mam "Раздевайся! Уснул, что ли?"
    voice "voice/anton/1day/034. Net ma.ogg"
    Ant "Нет, мам, просто задумался."
    voice "voice/karina/79 K.ogg"
    Mam "Интересно, о чём же?"
    voice "voice/anton/1day/035. Tak gl.ogg"
    Ant "Так... Глупости всякие."

    "Мама смерила меня подозрительным взглядом."
    "Словно сомневалась, что перед ней родной сын, а не какой-то притворщик, явившийся из леса."

    voice "voice/karina/80 K.ogg"
    Mam "Точно всё нормально?"
    voice "voice/karina/81 K.ogg"
    Mam "У тебя такое лицо было, когда милиционер про окно спросил..."
    voice "voice/anton/1day/036. Vse no.ogg"
    Ant "Всё нормально, мам."
    voice "voice/karina/83 K.ogg"
    "Она глубоко вздохнула."
    voice "voice/karina/82 K.ogg"
    Mam "Хорошо."

    scene bg door
    play test_one "sounds/steps/mam_out.ogg"
    show Mom Normal m_day 00 norm aside:
        xpos -100 ypos 0 xzoom -1.0
        alpha 1.0
        linear 0.5 alpha 1.0 xpos 40-200 ypos 20
        linear 0.5 alpha 1.0 xpos -20-200 ypos 0
        linear 0.5 alpha 0.5 xpos -70-200 ypos 20
        linear 0.5 alpha 0.0 xpos -100-200 ypos 0
    $ renpy.pause(1.0, hard=True)
    show door_narco
    if not Flags.Has("glove"):
        $ achievement_grant("ach_escaped")

    "Дом будто изменился."
    "Потускнела диванная обивка."
    "На кафеле в ванной отпечатались следы чьих-то пальцев."
    "Лампочки светили иначе — тускло и жёлто."
    "Даже привкус слюны во рту казался другим."
    "Со второго этажа послышалась мелодия «Аладдина» - Оля пересмотрела свои любимые серии «Русалочки» и переключилась на другие кассеты."
    "Я неспешно разделся, задержался перед умывальником, разглядывая в зеркале своё отражение, словно изучая ребус «найди отличия»."


    play test_one "sounds/steps/Anton-stairs-in-2.ogg"

    scene d4_hall_corridor d1:
        xalign 0.
    with Dissolve(.5)
    "Потом поднялся по лестнице."

    play test_two "sounds/Dja-fix-tuned.ogg"
    scene day1_roomday_nocurtain
    show day1_roomday_nocurtain_ door
    with Dissolve(0.5)
    show day1_roomday_nocurtain_ anton
    with Dissolve(0.5)
    "Умолкли голоса Джафара и Яго."

    play test_one "sounds/steps/Anton-steps-in-1.ogg"
    show day1_roomday_nocurtain_ door
    with Dissolve(0.5)
    "Я прошёл мимо Олиной спальни и юркнул в свою комнату."

label bunny_day1_anton_room_prepare:
    $ SceneFlags.Reset()

label bunny_day1_anton_room:
    if Flags.Has("number") or Flags.Has("glove"):
        $ story_manager.MarkEvent(("day1", "la anton"))
        window hide
        call screen anton_room_day_1
    else:
        jump anton_room_continue1

label bunny_anton_room_circle:
    $ story_manager.MarkEvent(("day1", "la anton", "curtains"))
    play test_one "sounds/curtain-long-2.ogg"
    window show
    if not SceneFlags.Seen("window"):
        "Днём лес не кажется таким мрачным."
        "Перекрученные ветви деревьев вдали и заснеженное поле между домом и лесом нагоняют зевоту."
        "Но иногда я ловлю себя на том, что, забыв про уроки, смотрю в окно на обледенелые кроны."
        $ true_detective_count1 += 1
    else:
        "Как странно: я вроде бы отодвинул штору..."
    jump bunny_day1_anton_room

label bunny_anton_room_toys:
    $ story_manager.MarkEvent(("day1", "la anton", "toys"))
    play test_one "sounds/toy-Long.ogg"
    window show
    if not SceneFlags.Seen("toys"):
        "Моя фигурка трицератопса."
        "Я знаю почти все разновидности динозавров: велоцирапторы, афровенаторы, гипсилофодоны..."
        "Помню, когда мы ещё жили в городе, пошли в кино с родителями на «Парк Юрского периода», и я сфотографировался в фойе возле механического Ти-рекса."
        "Он вертел головой и так оглушительно рычал."
        "Как же было здорово."
        "А рядом — игрушка-трансформер Роботек."
        "Обожаю этот мультик!"
        "Когда в заставке разгоняется истребитель и пищат бластеры, можно быть уверенным, что ближайшие двадцать минут пройдут потрясающе."
        "Космическая фабрика Зентреди захвачена! Рик, приготовься к бою!"
        $ true_detective_count1 += 1
    else:
        "Мои игрушки - трицератопс и Роботек."
    jump bunny_day1_anton_room

label bunny_anton_room_picture:
    $ story_manager.MarkEvent(("day1", "la anton", "pics"))
    play test_one "sounds/wall-pics-long-1.ogg"
    window show
    if not SceneFlags.Seen("picture"):
        "Я мечтаю стать художником с тех пор, как папа купил мне первые комиксы."

        $ add_text_to_dictionary(7)

        "Журнал {u}«Муха»{/u} — самый крутой. Я особенно люблю большой космический выпуск с инопланетными монстрами и смешную серию про жандарма."
        "С тех пор я рисую всё подряд, и, вроде бы, получается неплохо."
        "Когда-то в «Мухе» опубликовали моё письмо. Может, и мой комикс однажды там напечатают?"
        $ true_detective_count1 += 1
    else:
        "Мои лучшие работы."
    jump bunny_day1_anton_room

label bunny_anton_room_book:
    $ story_manager.MarkEvent(("day1", "la anton", "book"))
    play test_one "sounds/book-long-1.ogg"
    window show
    if not SceneFlags.Seen("book"):
        "«Монстры, привидения, НЛО»."
        "Энциклопедия паранормальных явлений издательства «Росмэн». Из неё я узнал про Лох-несское чудовище, Медузу Горгону и бигфута."
        "А Оля от книжки шарахается."
        "Разделы про монстров и пришельцев она ещё кое-как пролистала вместе со мной, но середина энциклопедии, где говорилось про призраков, её напугала."
        "Помню, прочитав книгу, я даже поохотился за привидениями: измерял линейкой расстояние между предметами на столе и утром проверял, не сдвинулись ли они под воздействием призрачных сил."
        "Не сдвинулись."
        "Хотя, на что я надеялся? Что встречу Каспера?"
        $ true_detective_count1 += 1
    else:
        "Я заучил эту книгу от корки до корки."
    jump bunny_day1_anton_room

label anton_room_continue1:
    $ story_manager.MarkEvent(("day1", "scene7"))

    if not Flags.Has("glove"):
        if Flags.Has("number"):
            scene bg storage_in_table0 with Dissolve(0.5)
            "Один из ящиков стола пустовал. Туда я спрятал номер телефона участкового."

            play test_one "sounds/desk-open-00.ogg"
            window hide
            scene bg storage_in_table1 with Dissolve(0.5)
            $ renpy.pause(1.0, hard=True)
            play test_one "sounds/paper-take-4.ogg"
            show item_in_table_number with Dissolve(0.5)
            window show

        "Такое простое действие отняло у меня последние силы."

        if Flags.Has("number"):
            play test_one "sounds/desk-close-00.ogg"
            window hide
            scene bg storage_in_table0 with Dissolve(0.5)
            $ renpy.pause(1.0, hard=True)
            scene bg room_day_open_curtain with Dissolve(0.5)
            window show

        stop music2 fadeout 5.0
        play test_one "sounds/bed.ogg"

        "Я сел на постель."

        scene daykovai with Dissolve (0.5):
            xalign 0.5
            yalign 0.5
            yoffset 0
            xoffset 0
            zoom 0.67
        play music "music/16_strings0.2-1.ogg" fadein 7.0

        "И только тут увидел: за шторкой кто-то стоял."
        "Моя рука обессилено упала."
        "Лекарства тому виной или пережитый стресс, но комната колебалась, словно ветер надувал стены, как парусину."
        "Углы плыли и изгибались."
        "Только силуэт между подоконником и гардиной оставался недвижимым. Ткань облепила притаившегося гостя."

        scene daykovai:
            xalign 0.5
            yalign 0.5
            yoffset 0
            xoffset 0
            zoom 0.67
            linear 12.00 yoffset 100 xoffset 0 zoom 1.0

        "«Точно саван», — подумал я."

        voice "voice/anton/1day/037. Olja.ogg"
        Ant "Оля?"

        "Кому же ещё там стоять?"
        "Я встал с кровати, облизал пересохшие губы."

        voice "voice/anton/1day/038. Olja ocz.ogg"
        Ant "Оля, очень смешно."

        play test_seven "sounds/sfx-slow-heartbeat.ogg" fadein 5 loop

        "Силуэт не шевелился."
        "Штора мягко обтекала контуры. Будто не человек, а уплотнение мрака."
        "Я потянулся к шторке."
        "«Тук-тук, тук-тук», – стучало отрегулированное таблетками сердце."
        "Ветер в поле пел многоголосым хором."
        "На секунду захотелось вернуться на кровать, лечь и просто смотреть на человека за шторкой, зная, что он смотрит в ответ."
        "Смотрит, не моргая, и ждёт, когда я усну."

        stop music fadeout 3.0
        play test_three "sounds/trumpet-1.ogg"
        play test_one "sounds/curtain.ogg"
        show bg_white with Dissolve (0.15)
        play test_two "sounds/steps/Olya_top.ogg"
        scene bg room_day_open_empty
        show Olya Happy b_day 00 good ahead 03 at sprite_happy
        stop test_seven fadeout 0.2
        show bg_white:
            alpha 1.0
            linear 0.35 alpha 0.0

        voice "voice/olya/19 O.ogg"
        Oly "Попался!"

        play music2 "music/17_Flow.ogg" volume 0.7 fadein 5.0

        voice "voice/anton/1day/039. Da ja s.ogg"
        Ant "Да я сразу понял, что это ты."

        play test_one "sounds/steps/Olya-steps-5.ogg"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.3)

        "На фоне предзакатного солнца над Олиной головой вспыхнул ослепительный нимб."
        "Словно моя сестра сияла."
        "Когда Оля была совсем крошкой, папа частенько говорил, что она светится от радости."
        "Я возражал: она же не фонарик, чтобы светиться!"
        "Но однажды поднес её к окну, и солнечные лучи попали на улыбающееся личико."
        "Казалось, я держу на руках ребёнка, сотканного из света."

        show Olya Serious m_day 00 good ahead 02 with Dissolve (0.2)
        voice "voice/olya/20 O.ogg"
        Oly "А почему к нам милиция приходила? Ты что-то натворил?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        voice "voice/anton/1day/040. Net ko.ogg"
        Ant "Нет, конечно. Скажешь тоже."

        show Olya Serious m_day 00 good ahead 02 with Dissolve (0.2)
        voice "voice/olya/21 O.ogg"
        Oly "Это из-за совы, да?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        "Я улыбнулся невесело и потрепал сестрёнку по волосам."

        voice "voice/anton/1day/041. Odin m.ogg"
        Ant "Один мальчик потерялся в лесу."

        show Olya Serious m_day 00 good ahead 02 with Dissolve (0.2)
        voice "voice/olya/22 O.ogg"
        Oly "О, ему, наверное, там очень холодно."
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)
        show Olya Serious m_day 00 good ahead 02 with Dissolve (0.2)
        voice "voice/olya/23 O.ogg"
        Oly "А его найдут?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        voice "voice/anton/1day/042. Objazat.ogg"
        Ant "Обязательно."
        voice "voice/anton/1day/042.Uczastko.ogg"
        Ant "Участковый по домам ходит, всем фотографию его показывает."

        play test_one "sounds/steps/Olya-steps-3.ogg"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2):
            xpos 500

        "Оля с опаской прошла по комнате и впечатала в оконное стекло ладошки."

        show Olya Prof m_day 00 good aside 07 with Dissolve(0.2)
        voice "voice/olya/24 O.ogg"
        Oly "А почему он по домам ходит, а не по лесу?"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)
        show Olya Prof m_day 00 good aside 07 with Dissolve(0.2)
        voice "voice/olya/38 O.ogg"
        Oly "Боится?"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)

        "Вопрос застал меня врасплох."

        voice "voice/anton/1day/043. Milici.ogg"
        Ant "Милиционеры ничего не боятся."
        voice "voice/anton/1day/043. I les.ogg"
        Ant "И лес они прочесали..."
        "Я сменил тему."
        "Словно попытался отвести Олю подальше от чащи."

        voice "voice/anton/1day/044. Esli ja.ogg"
        Ant "Если я сам найду пропавшего мальчика, нам, может, награду дадут."

        $ add_text_to_dictionary(8)

        voice "voice/anton/1day/044. Kuczu v.ogg"
        Ant "Кучу всякого, как в {u}«Поле чудес»{/u}."
        voice "voice/anton/1day/044. Klevo.ogg"
        Ant "Клёво же?"

        scene d5_br_window_bg:
            matrixcolor BrightnessMatrix(.2)
        show d5_br_window_frame
        show bg_in_fridge_olya:
            align (.5, 1.)
            xoffset 200
            yoffset 300
        with Dissolve(.5)
        "Оля словно не слышала меня."
        "Она тихо спросила, буравя лес взглядом внимательных, каких-то удивительно взрослых глаз:"

        voice "voice/olya/26 O.ogg"
        Oly "А что, если это сова его утащила?.."
        voice "voice/anton/1day/045. Erunda.ogg"
        Ant "Ерунда!"
        voice "voice/anton/1day/045. Ne mozh.ogg"
        Ant "Не может сова поднять человека."
        voice "voice/anton/1day/045. No vot.ogg"
        Ant "Но вот что..."

        "Я тщательно подбирал слова."
        "Вытаскивал их силком из переутомлённого мозга."

        scene bg room_day_open_empty
        show Olya Prof m_day 00 good aside 01:
            xoffset 600
        with Dissolve (0.5)
        voice "voice/anton/1day/046.Ty v le.ogg"
        Ant "Ты в лес не суйся. Мне кажется, он какой-то..."
        voice "voice/anton/1day/046.Kak by.ogg"
        Ant "Как бы сказать... Проклятый, что ли."

        show Olya Serious m_day 00 good ahead 03 with Dissolve(0.2)
        voice "voice/olya/27 O.ogg"
        Oly "Как в сказке?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve(0.2)

        voice "voice/anton/1day/047. Net. S.ogg"
        Ant "Нет. Скорее как на той страшной кассете, что родители прячут."

        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)

        "Оля поёжилась и украдкой выглянула в окно."

        scene d5_br_window_bg:
            matrixcolor BrightnessMatrix(.2)
        show d5_br_window_frame
        show bg_in_fridge_olya:
            align (.5, 1.)
            xoffset 200
            yoffset 300
        with Dissolve(.5)
        "Я смотрел на сестру, и сердце обливалось кровью."
        "До чего же она хрупкая! Как легко погасить этот свет!"

        scene bg room_day_open_empty
        show Olya Prof m_day 00 good aside 01:
            xoffset 600
        with Dissolve (0.5)
        "Подует ветер — и затушит лампадку."
    else:



        scene bg storage_in_table0 with Dissolve(0.5)

        if Flags.Has("number"):
            "Один из ящиков стола пустовал. Туда я спрятал варежку вместе с номером телефона участкового."
        else:
            "Один из ящиков стола пустовал. Туда я спрятал варежку."

        $ achievement_grant("ach_Vova")

        play test_one "sounds/desk-open-00.ogg"
        window hide
        scene bg storage_in_table1 with Dissolve(0.5)
        $ renpy.pause(1.0, hard=True)
        if Flags.Has("number"):
            play test_one "sounds/paper-take-4.ogg"
            show item_in_table_number
        play test_two "sounds/mitten-drop-2.ogg"
        show item_in_table_glove
        with Dissolve(0.5)
        window show

        "Такое простое действие отняло у меня последние силы."

        play test_one "sounds/desk-close-00.ogg"
        window hide
        scene bg storage_in_table0 with Dissolve(0.5)
        $ renpy.pause(1.0, hard=True)
        scene bg room_day_open_curtain with Dissolve(0.5)
        window show

        stop music2 fadeout 5.0
        play test_one "sounds/bed.ogg"

        "Я сел на кровать."

        scene daykovai with Dissolve (0.5):
            xalign 0.5
            yalign 0.5
            yoffset 0
            xoffset 0
            zoom 0.67
        play music "music/16_strings0.2-1.ogg" fadein 7.0

        "И только тут увидел: за шторкой кто-то стоял."
        "Моя рука обессилено упала."
        "Лекарства тому виной или пережитый стресс, но комната колебалась, словно ветер надувал стены, как парусину."
        "Углы плыли и изгибались."
        "Только силуэт между подоконником и гардиной оставался недвижимым."

        scene daykovai:
            xalign 0.5
            yalign 0.5
            yoffset 0
            xoffset 0
            zoom 0.67
            linear 12.00 yoffset 100 xoffset 0 zoom 1.0

        "Ткань облепила притаившегося гостя."
        "«Точно саван», - подумал я."

        voice "voice/anton/1day/037. Olja.ogg"
        Ant "Оля?"

        "Кому же ещё там стоять?"
        "Я встал с кровати, облизал пересохшие губы."

        voice "voice/anton/1day/038. Olja ocz.ogg"
        Ant "Оля, очень смешно."

        play test_seven "sounds/sfx-slow-heartbeat.ogg" fadein 5 loop
        "Силуэт не шевелился."
        "Штора мягко обтекала контуры."
        "Будто не человек, а уплотнение мрака."
        "Я потянулся к шторке."
        "Тук-тук-тук – стучало отрегулированное таблетками сердце."
        "Ветер в поле пел стоголосым хором."
        "На секунду захотелось вернуться на кровать, лечь и просто смотреть на человека за шторкой, зная, что он смотрит в ответ."
        "Смотрит, не моргая, и ждёт, когда ты уснёшь."
        "Пластмассовые кольца зашуршали о карниз, когда я рывком отдёрнул шторку."

        window hide
        pause 2
        play test_one "sounds/curtain.ogg"
        show bg_white with Dissolve (0.15)
        play test_three "sounds/trumpet-1.ogg"
        play test_two "sounds/steps/Olya_top.ogg"
        stop test_seven fadeout 0.2
        stop music fadeout 3.0
        scene bg room_day_open_empty
        show Olya Happy b_day 00 good ahead 03 at sprite_happy
        show bg_white:
            alpha 1.0
            linear 0.35 alpha 0.0
        window show

        voice "voice/olya/19 O.ogg"
        Oly "Попался!"

        play music2 "music/17_Flow.ogg" volume 0.7 fadein 5.0

        voice "voice/anton/1day/039. Da ja s.ogg"
        Ant "Да я сразу понял, что это ты."

        play test_one "sounds/steps/Olya-steps-5.ogg"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.3)

        "На фоне предзакатного солнца над Олиной головой вспыхнул ослепительный нимб."
        "Словно моя сестра светилась."
        "Когда Оля была совсем крошкой, папа частенько говорил, что она светится от радости."
        "Я возражал: она же не фонарик, чтобы светиться!"
        "Но однажды поднёс её к окну, и солнечные лучи попали на улыбающееся личико."
        "Казалось, я держу на руках ребёнка, сотканного из света."

        show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
        voice "voice/olya/29 O.ogg"
        Oly "А я всё видела!"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        voice "voice/anton/1day/048. Da nu_.ogg"
        Ant "Да ну!"

        show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
        voice "voice/olya/30 O.ogg"
        Oly "Что ты спрятал?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        "Вылитая маленькая мама, ещё до того, как она нацепила эту маску тоскливой усталости и перешла на приказной тон."

        voice "voice/anton/1day/049. Niczego.ogg"
        Ant "Ничего, просто..."
        "Оля подбежала к столу, спросила, округлив глаза:"

        show Olya Amaze m_day 00 good ahead 05 with Dissolve (0.2)
        voice "voice/olya/31 O.ogg"
        Oly "Ты что-то украл и теперь прячешь?"
        show Olya Amaze m_day 00 good ahead 01 with Dissolve (0.2)
        show Olya Amaze m_day 00 good ahead 05 with Dissolve (0.2)
        voice "voice/olya/31A O.ogg"
        Oly "Ты — вор?"
        show Olya Amaze m_day 00 good ahead 01 with Dissolve (0.2)

        voice "voice/anton/1day/Chto glup.ogg"
        Ant "Что? Глупая!"
        voice "voice/anton/1day/Nichego ya ne kral.ogg"
        Ant "Ничего я не крал..."

        "Всплыл чёткий образ: варежка, висящая на суку."

        window hide
        play test_one "sounds/Varezka.ogg"
        show bg_white with Dissolve(0.1)
        show memory_scrimer2
        $ renpy.pause(1.2, hard=True)
        hide memory_scrimer2
        hide bg_white with Dissolve(0.1)
        window show

        "А вдруг я её украл?"
        "У леса, у склонившегося силуэта за деревьями?"
        "Оля, когда хотела, могла быть капризной и напористой."

        show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
        voice "voice/olya/32 O.ogg"
        Oly "Покажи тогда!"
        show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

        voice "voice/anton/1day/Poklyanis.ogg"
        Ant "Поклянись, что никому не скажешь, — тогда покажу."

        show Olya Happy m_day 00 good ahead 08 with Dissolve (0.2)

        "Оля заговорщицки улыбнулась."

        show Olya Happy m_day 00 good ahead 07 with Dissolve (0.2)
        voice "voice/olya/33 O.ogg"
        Oly "Клянусь маминым сердцем!"
        show Olya Happy m_day 00 good ahead 08 with Dissolve (0.2)

        $ add_text_to_dictionary(9)

        "Клятва, услышанная ею в старом фильме про {u}пионеров{/u}, что мы смотрели однажды."

        voice "voice/anton/1day/052. Ne gov.ogg"
        Ant "Не говори так."
        "Оля кивнула и жестом заперла рот на невидимый ключик."

        scene bg storage_in_table0 with Dissolve(0.5)

        "Любопытство переполняло её, плескалось в огромных глазах."

        play test_one "sounds/desk-open-00.ogg"
        window hide

        scene bg storage_in_table1
        if Flags.Has("number"):
            show item_in_table_number
            show item_in_table_glove
            with Dissolve(0.5)
        else:
            show item_in_table_glove
            with Dissolve(0.5)

        "Я выдвинул ящик, и Оля наклонилась, затаив дыхание."
        "Казалось, там лежала не просто рукавица, а какой-то диковинный зверёк."

        voice "voice/olya/34 O.ogg"
        Oly "Это... чья-то варежка?.."
        "Она сказала это с такой интонацией, будто сама не могла понять, что это такое."
        voice "voice/anton/1day/053. Odin m.ogg"
        Ant "Один мальчик потерял... и сам потерялся."
        voice "voice/anton/1day/053.Teper.ogg"
        Ant "Теперь понимаешь, как опасно гулять в лесу, особенно детям?"

        voice "voice/olya/35 O.ogg"
        Oly "Ему, наверное, там очень холодно."

        window hide
        play test_one "sounds/desk-close-00.ogg"
        scene bg storage_in_table0 with Dissolve(0.5)
        window show

        voice "voice/olya/36 O.ogg"
        Oly "Его найдут?"
        voice "voice/anton/1day/Obyazatelno.ogg"
        Ant "Обязательно."

        scene bg room_day_open_empty
        show Olya Serious m_day 00 good ahead 01
        with Dissolve (0.3)

        voice "voice/anton/1day/Uchastkoviy.ogg"
        Ant "Участковый по домам ходит, всем фотографию показывает."

        play test_one "sounds/steps/Olya-steps-3.ogg"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2):
            xpos 1500

        "Оля с опаской прошла по комнате и впечатала в оконное стекло ладошки."

        show Olya Prof m_day 00 good aside 07 with Dissolve(0.2)
        voice "voice/olya/37 O.ogg"
        Oly "А почему он по домам ходит, а не по лесу?"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)
        show Olya Prof m_day 00 good aside 07 with Dissolve(0.2)
        voice "voice/olya/38 O.ogg"
        Oly "Боится?"
        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)

        "Вопрос застал меня врасплох."
        voice "voice/anton/1day/043. Milici.ogg"
        Ant "Милиционеры ничего не боятся."
        voice "voice/anton/1day/043. I les.ogg"
        Ant "И лес они прочесали."
        "«Да как же!» — мелькнуло в затуманенном сознании."

        scene bg_white onlayer master1
        with Dissolve(.15)
        scene bg forest0_long onlayer master1:
            xalign 0.0
            yalign 0.5
        show bg forest0_long as glitch onlayer master1:
            alpha 0
            zoom 1.5
            block:
                alpha .75
                align (.1, .5)
                .2
                align (.5, .4)
                .2
                zoom 2.25
                align (.0, .5)
                .2
                zoom 1.5
                align (.05, .4)
                .2
                alpha 0
                3
                repeat
        show d4_noise onlayer master1
        show ramka onlayer master1
        with Dissolve(.5)
        "Проверяли ли они в самых потаённых уголках, где тьма, холод и шёпот обледенелых ветвей?"

        scene bg_white onlayer master1
        with Dissolve(.15)
        scene onlayer master1
        with Dissolve(.5)
        "Допустим, да, но почему тогда не нашли варежку?"
        "Или она появилась позже... для меня?"
        "Я сменил тему."
        "Словно попытался отвести Олю подальше от чащи."
        voice "voice/anton/1day/044. Esli ja.ogg"
        Ant "Если я сам найду пропавшего мальчика, нам, может, награду дадут."

        $ add_text_to_dictionary(8)

        voice "voice/anton/1day/044. Kuczu v.ogg"
        Ant "Кучу всякого, как в {u}«Поле чудес»{/u}."

        voice "voice/anton/1day/044. Klevo.ogg"
        Ant "Клёво же?"

        scene d5_br_window_bg:
            matrixcolor BrightnessMatrix(.2)
        show d5_br_window_frame
        show bg_in_fridge_olya:
            align (.5, 1.)
            xoffset 200
            yoffset 300
        with Dissolve(.5)
        "Оля словно не слышала меня."
        "Она тихо спросила и буравила лес взглядом внимательных, каких-то удивительно взрослых глаз:"

        voice "voice/olya/26 O.ogg"
        Oly "А что, если это сова его утащила?.."
        voice "voice/anton/1day/045. Erunda.ogg"
        Ant "Ерунда!"
        voice "voice/anton/1day/045. Ne mozh.ogg"
        Ant "Не может сова поднять человека."
        voice "voice/anton/1day/045. No vot.ogg"
        Ant "Но вот что..."
        "Я тщательно подбирал слова. Вытаскивал их силком из переутомлённого мозга."

        scene bg room_day_open_empty
        show Olya Prof m_day 00 good aside 01:
            xoffset 600
        with Dissolve (0.5)
        voice "voice/anton/1day/046.Ty v le.ogg"
        Ant "Ты в лес не суйся. Мне кажется, он какой-то..."
        voice "voice/anton/1day/046.Kak by.ogg"
        Ant "Как бы сказать... Проклятый, что ли."

        show Olya Serious m_day 00 good ahead 03 with Dissolve(0.2)
        voice "voice/olya/27 O.ogg"
        Oly "Как в сказке?"
        show Olya Serious m_day 00 good ahead 01 with Dissolve(0.2)

        voice "voice/anton/1day/047. Net. S.ogg"
        Ant "Нет. Скорее как на той страшной кассете, что родители прячут."

        show Olya Prof m_day 00 good aside 01 with Dissolve(0.2)

        "Оля поёжилась и украдкой выглянула в окно."

        scene d5_br_window_bg:
            matrixcolor BrightnessMatrix(.2)
        show d5_br_window_frame
        show bg_in_fridge_olya:
            align (.5, 1.)
            xoffset 200
            yoffset 300
        with Dissolve(.5)

        voice "voice/olya/39 O.ogg"
        Oly "Я видела, как ты убегал..."

        voice "voice/olya/40 O.ogg"
        Oly "За тобой кто-то гнался?"

        voice "voice/anton/1day/054. Net_ p.ogg"
        Ant "Нет, просто... чтобы мама не волновалась, спешил домой."
        "Я смотрел на сестру, и сердце обливалось кровью."
        "До чего же она хрупкая! Как легко погасить этот свет!"

        scene bg room_day_open_empty
        show Olya Prof m_day 00 good aside 01:
            xoffset 600
        with Dissolve (0.5)
        "Подует ветер и затушит лампадку."


    $ story_manager.MarkEvent(("day1", "scene8"))
    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/41 O.ogg"
    Oly "Хорошо тебе."
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/42 O.ogg"
    Oly "Меня вот мама не пускает даже на крыльцо."
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/43 O.ogg"
    Oly "Как принцесса в башне сижу — никуда не могу выйти."
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/44 O.ogg"
    Oly "Так и умру тут от скуки..."
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/055. Ne pri.ogg"
    Ant "Не придумывай!"
    voice "voice/anton/1day/055. Ot sku.ogg"
    Ant "От скуки ещё никто не умирал."
    voice "voice/anton/1day/055.U tebja.ogg"
    Ant "У тебя же есть я и мультики, а мама с папой скоро помирятся."

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/45 O.ogg"
    Oly "Знаешь, что бы я загадала на следующий день рождения?"
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/46 O.ogg"
    Oly "Чтобы родители тоже в детей превратились, и мы бы все вместе играли как раньше!"
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/056. Aga_a.ogg"
    Ant "Ага, а если бы они стали размером с жука, то мы бы их в спичечный коробок посадили..."

    play test_one "sounds/steps/Olya-steps-4.ogg"
    show Olya Happy b_day 00 good ahead 01:
        align (.5, 1.)
        xoffset 0
        .3
        linear .2 yoffset 25
        linear .2 yoffset 0
        linear .2 yoffset 25
        linear .2 yoffset 0
    with Dissolve (0.3)

    voice "voice/olya/47A O.ogg"
    "Оля хихикнула, потянула меня за рукав."

    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/47 O.ogg"
    Oly "Тоша, пойдём «Аладдина» смотреть."
    show Olya Happy b_day 00 good ahead 01 with Dissolve (0.2)

    "Усталость была сильнее желания побыть с сестрой. Меня одолела какая-то гнусная апатия."

    voice "voice/anton/1day/057. Vymota.ogg"
    Ant "Вымотался я. Что-то не хочется."

    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/48 O.ogg"
    Oly "Ну пойдём!"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)
    show Olya Serious b_day 00 good ahead 02 with Dissolve (0.2)
    voice "voice/olya/49 O.ogg"
    Oly "Мне скучно одной, а мама занята всё время."
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)
    show Olya Serious b_day 00 good ahead 02 with Dissolve (0.2)
    voice "voice/olya/50 O.ogg"
    Oly "Можно выбрать другой мультик, который ты ещё не видел."
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/058. Da ja v.ogg"
    Ant "Да я все наши кассеты наизусть знаю..."

    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/51 O.ogg"
    Oly "А вот и не все! Ты «Питера Пэна» не видел!"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)
    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/52 O.ogg"
    Oly "Помнишь, ты уснул на середине?.."
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)
    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/53 O.ogg"
    Oly "А там потом такое... Ну, пойдём, пойдём!"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/059. Davai.ogg"
    Ant "Давай попозже."

    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/54 O.ogg"
    Oly "Рассказать тебе, чем всё закончилось?"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/060. Utrom rasskazes.ogg"
    Ant "Утром расскажешь."

    show Olya Serious b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/55 O.ogg"
    Oly "Утром не захочу!"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    show Olya Amaze b_day 00 good ahead 01 at sprite_happy
    show Olya Amaze b_day 00 good ahead 04 with Dissolve (0.2)
    voice "voice/olya/56 O.ogg"
    Oly "Придумала! А давай в прятки?"
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/061. Net Ol.ogg"
    Ant "Нет, Оль."

    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/57 O.ogg"
    Oly "Тогда нарисуй мне динозавра."
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/062. Olja bl.ogg"
    Ant "Оля, блин..."

    show Olya Amaze b_day 00 good ahead 04 at sprite_happy_2times with Dissolve (0.2)
    voice "voice/olya/58 O.ogg"
    Oly "Нарисуй! Нарисуй!"
    stop music2 fadeout 2.0
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/063. Da ost.ogg"
    Ant "Да оставь ты меня в покое!!!"

    play test_one "sounds/steps/Olya-steps-5.ogg"
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.3)

    "Слова сами сорвались с губ. Я даже опешил."
    "Прежде я так не прикрикивал на сестру."

    play music "music/8_Peredyshka.ogg" volume 0.8 fadein 3.0

    "Ошеломлённая Оля уставилась на меня."

    show Olya Weeps m_day 00 good ahead with Dissolve (0.2)

    "Губы задрожали, предвещая неминуемые слёзы."

    voice "voice/anton/1day/064. Gadliv.ogg"
    "Гадливость и стыд заклокотали в груди: что со мной происходит?"
    "Я заспешил опередить Олин плач."

    voice "voice/anton/1day/065. Ladno.ogg"
    Ant "Ладно, уболтала, давай смотреть мультики, только недолго."

    voice "voice/olya/59 O.ogg"
    Oly "Уже не хочу."

    show Olya Weeps b_day 00 good ahead 01 with Dissolve (0.2)

    "Я подошёл к ней. Положил ладонь на мягкие волосы."

    voice "voice/anton/1day/066. Poidem.ogg"
    Ant "Пойдём."
    voice "voice/anton/1day/066. Pitera.ogg"
    Ant "«Питера Пэна» посмотрим."

    show Olya Weeps b_day 00 good ahead 05 with Dissolve (0.2)

    voice "voice/olya/60 O.ogg"

    Oly "Ага! Ты опять уснёшь."

    stop music fadeout 2.0
    show Olya Weeps b_day 00 good ahead 01 with Dissolve (0.2)

    "Я улыбнулся, поднял её подбородок. Глаза были мокрыми, бездонными."

    play music "music/25_Olya.ogg" volume 0.7 fadein 5.0
    show Olya Serious b_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/067. Ne usn.ogg"
    Ant "Не усну, обещаю."
    voice "voice/anton/1day/067. A poto.ogg"
    Ant "А потом я тебе целого трицератопса нарисую."

    show Olya Happy b_day 00 good ahead 02 at sprite_happy

    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/61A O.ogg"
    Oly "Ура!"
    show Olya Happy b_day 00 good ahead 02 with Dissolve (0.2)
    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/61 O.ogg"
    Oly "Трипе... цире... пупса!"
    show Olya Happy b_day 00 good ahead 02 with Dissolve (0.2)

    voice "voice/anton/1day/068. Nu pochti.ogg"
    Ant "Ну, почти."

    "Она протёрла рукавом глаза и засияла улыбкой."

    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/63 O.ogg"
    Oly "Давай ты пока кассету перемотаешь, а я у мамы попрошу сгущёнки с хлебом."
    show Olya Happy b_day 00 good ahead 02 with Dissolve (0.2)
    show Olya Happy b_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/64 O.ogg"
    Oly "Только утром свежий привезли, как ты любишь."
    show Olya Happy b_day 00 good ahead 02 with Dissolve (0.2)

    voice "voice/anton/1day/069. Nesi t.ogg"
    Ant "Неси, только аккуратнее, а то разольёшь."
    voice "voice/anton/1day/069.Opjat r.ogg"
    Ant "Опять ругаться будут."

    play test_one "sounds/steps/Olya-steps-5.ogg"

    show Olya Happy m_day 00 good ahead 08 with Dissolve (0.2)
    voice "voice/olya/65 O.ogg"
    Oly "Спорим, не разолью!"
    show Olya Happy m_day 00 good ahead 02 with Dissolve (0.2)

    stop music fadeout 3.0

    show Olya Happy m_day 00 good ahead 03 with Dissolve (0.2)
    voice "voice/olya/66 O.ogg"
    Oly "Кассета где-то в тумбочке, поищи пока."
    show Olya Happy m_day 00 good ahead 02 with Dissolve (0.2)

    play test_one "sounds/steps/Olya_out.ogg"
    hide Olya
    with Dissolve (0.3)

    "Оля исчезла в дверях, а я поплёлся в соседнюю комнату."

    play music2 "music/1_Melancholy(Tiny_Bunny).ogg" fadein 5.0
    stop music fadeout 10.0
    play test_two "sounds/steps/Anton-steps-out-1.ogg"
    scene bg_Olga_room_day
    with Dissolve (0.5)

label bunny_day1_olya_room_prepare:
    $ story_manager.MarkEvent(("day1", "la olya"))
    $ SceneFlags.Reset()
    play test_one "sounds/steps/Anton-steps-in-1.ogg"
label bunny_day1_olya_room:
    window hide
    jump bunny_day1_olya_room.afterdev
    label bunny_day1_olya_room.dev:
        scene bg_black
        menu:
            "Номер (+)" if Flags.Has("number"):
                $ Flags.Drop("number")
            "Номер (-)" if not Flags.Has("number"):
                $ Flags.Raise("number")
            "Варежка (+)" if Flags.Has("glove"):
                $ Flags.Drop("glove")
            "Варежка (-)" if not Flags.Has("glove"):
                $ Flags.Raise("glove")
            "Продолжить":
                jump bunny_day1_olya_room.afterdev
        jump bunny_day1_olya_room.dev
    label bunny_day1_olya_room.afterdev:

    call screen olya_room_day_1

label bunny_olya_room_circle:
    $ story_manager.MarkEvent(("day1", "la olya", "curtains"))
    play test_one "sounds/curtain-long-2.ogg"
    window show
    if not SceneFlags.Seen("window"):
        "То самое жуткое окно, за которым каждую ночь Оля видит проклятую сову, караулящую в темноте."
        "Днём Оля держит шторы раздвинутыми, но в сумерках плотно зашторивает окна, чтобы не видеть глядящих снаружи жадных глаз."
        $ true_detective_count1 += 1
    else:
        "Никакой совы - лишь тёмный лес."
    jump bunny_day1_olya_room

label bunny_olya_room_bear:
    $ story_manager.MarkEvent(("day1", "la olya", "bear"))
    play test_one "sounds/teddybear-long-1.ogg"
    window show
    if not SceneFlags.Seen("toys"):
        "Бессчётные Олины игрушки."
        "Самая главная среди них — старый плюшевый медведь. Оля без него не засыпает."
        "А когда спит, зарывается носиком в его мех."
        $ true_detective_count1 += 1
    else:
        "Плюшевый мишутка."
    jump bunny_day1_olya_room

label bunny_olya_room_pig:
    $ story_manager.MarkEvent(("day1", "la olya", "pig"))
    play test_one "sounds/coins-rotate-02.ogg"
    window show
    if not SceneFlags.Seen("pig"):
        "Свинья-копилка."
        "Оля собирает деньги на настоящего щенка, так как папа говорит, что содержать его будет дорого."
        $ true_detective_count1 += 1
    else:
        "К сожалению, у меня нет с собой монетки."
    jump bunny_day1_olya_room

label bunny_day1_olya_room_photon:
    $ story_manager.MarkEvent(("day1", "scene9"))
    play test_two "sounds/steps/Anton-steps-in-1.ogg"
    stop music2 fadeout 5.0
    scene tv_1_up
    with Dissolve (0.5)
    stop test_two fadeout 0.5
    window show

    "Старый телевизор «Фотон» пылился в углу."
    "Оставалось только щёлкнуть кнопкой на передней панели."

    window hide
    play test_one "sounds/rep/tv-on-click-1.ogg"
    $ renpy.pause(0.2)
    play test_two "sounds/rep/tv-on.-kinescope-1.ogg"
    $ renpy.pause(0.2)
    play fon "sounds/rep/tv-noise-2.ogg" fadein 5.0
    scene tv_1_up_pomehi with Dissolve (2.5)
    window show

    "Кинескоп нагрелся, на чёрном экране привычно заплясал белый шум."

    scene bg_rep_04 with Dissolve (0.5)

    "Я было потянулся включить видеомагнитофон, как вдруг рябь улеглась, и на мгновение вынырнула размытая картинка."

    scene bg_rep_02 with Dissolve (0.5)
    play fon "sounds/rep/strange-voices-1.ogg"

    "Это был мрачный таёжный лес, в точности такой же, как у меня за окном. Искажение разделяло экран прямо посередине."
    "Из динамика доносилось нечто зловещее, едва похожее на человеческую речь."

    scene bg_rep_04 with Dissolve (0.5)
    play fon "sounds/rep/tv-noise-2.ogg"

    "Не прошло и нескольких секунд, как пейзаж снова замело помехами."

    stop fon fadeout 4.0
    play music2 "music/15_Zaychik_Fon.ogg" fadein 3.0

    "Неужели ловит новый сигнал?"
    "На местном телевидении показывают только советские мультфильмы, да и те очень редко."
    "А раньше я всегда смотрел «Роботэк» перед школой."
    "Вот же было здорово..."

    scene tv_1_up_pomehi with Dissolve (0.5)

    "Может, пошевелить антенну? Вдруг поймаю тот самый канал?"
    "Но с другой стороны..."
    "Оля просила найти кассету..."
    "Нехорошо будет опять её расстраивать."
    "И эта сонливость... Сил нет делать всё скопом."


    window hide
    scene tv_1_up_pomehi:
        yalign 0.0
        linear 2.0 yalign 0.5
    $ renpy.pause(2.0)
    scene tv_1_up_pomehi:
        yalign 0.5

    label bunny_day1_olya_room_photon.choice:
    $ story_manager.MarkEvent(("day1", "tv"))

    call screen day1_choice_tv_or_peter


label bunny1_find1:
    $ story_manager.MarkEvent(("day1", "tv", "peter"))
    scene tv_1_up_pomehi:
        yalign 0.5
        linear 2.0 yalign 1.0
    $ renpy.pause(2.0)
    scene tv_1_up_pomehi:
        yalign 1.0
    $ renpy.pause(1.0)
    play test_one "sounds/vhs/Open.ogg"
    scene tv_2_up_pomehi:
        yalign 1.0
    with Dissolve (0.5)
    play test_one "sounds/vhs/resirch.ogg"

    "Я прошерстил полки, заставленные куклами и голубыми бегемотиками из «Киндер Сюрприза»."

    show tv_3 with Dissolve (0.5)

    "Нужная кассета нашлась по стёртому голубому корешку."

    hide tv_3 with Dissolve (0.3)
    $ renpy.pause(0.5)
    play test_one "sounds/vhs/Close.ogg"
    scene tv_1_up_pomehi:
        yalign 1.0
    with Dissolve (0.5)
    $ renpy.pause(0.2)
    window show
    play test_one "sounds/vhs/vhs_1.ogg"

    "Я вытряхнул из коробки чёрный прямоугольник."

    $ achievement_grant("ach_neverland")
    window hide
    scene tv_1_up_pomehi:
        yalign 1.0
        linear 3.0 yalign 0.0
    $ renpy.pause(3.0)
    scene tv_1_up_pomehi:
        yalign 0.0
    play test_one "sounds/vhs/forward.ogg"
    window show

    "Зашуршала плёнка, перекручиваясь к началу. Её шелест убаюкивал."
    "Меня, сидящего на корточках перед экраном, окутало дрёмой."

    scene bg_rep_04 with Dissolve (0.5)

    show transition_01 onlayer master1:
        alpha 0
        yalign 1.
        parallel:
            linear 3. alpha .75
        parallel:
            linear 20 yalign .0
    show old_movie_intense onlayer master1:
        alpha 0
        matrixcolor BrightnessMatrix(1.0)
        linear 1 alpha 1
    "В голове завертелись образы: мы с Олей летим над лесом, кувыркаемся на мягкой перине облаков."
    "Сестра смеётся, и я улыбаюсь, но улыбка с каждой секундой всё натянутей."
    "Я замечаю, что облака раздвинулись под нами, а внизу ощетинились сосны."

    show layer master1:
        alpha 1
        linear 2 alpha 0
    "Меж деревьев хлюпает болотистая тьма. А крылья уже не могут удерживать нас, и Оля..."

    play test_two "sounds/steps/Olay_go.ogg"
    scene onlayer master1
    scene bg_Olga_room_day
    show tv_pomehi
    with Dissolve (0.5)
    stop music2 fadeout 5.0
    play music "music/25_Olya.ogg" volume 0.7 fadein 5.0

    voice "voice/olya/67 O.ogg"
    Oly "Ты не смотришь без меня?"

    show Olya00 with Dissolve (0.5)

    "В руках у сестры был поднос с криво нарезанным хлебом и целой банкой сгущёнки."
    "Я протёр глаза."

    voice "voice/anton/1day/070. Net. S.ogg"
    Ant "Нет. Садись."
    voice "voice/olya/68 O.ogg"
    Oly "Мама с папой опять ругаются."
    voice "voice/anton/1day/071. U nih.ogg"
    Ant "У них сейчас период такой."
    voice "voice/olya/69 O.ogg"
    Oly "Глупый какой-то период."

    "На экране Вэнди убирала в комод тень Питера Пэна. Олю веселила мультяшная собака Нэна."

    scene bg_Olga_room_day
    show tv_multiki
    show Olya Serious m_day 00 good ahead 03
    with Dissolve (0.5)

    voice "voice/olya/70 O.ogg"
    Oly "Может, и нам родители собачку купят?"

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/072. Aga ka.ogg"
    Ant "Ага, как же."

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)

    voice "voice/olya/71 O.ogg"
    Oly "В Небыляндии у меня будет своя собственная собака! И кошка! И попугайчик!"

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    "Оля намазала хлеб толстым слоем сгущёнки и вручила мне бутерброд."

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)

    voice "voice/olya/72 O.ogg"
    Oly "А у тебя все молочные зубы выпали?"

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/072. Koneczn.ogg"
    Ant "Конечно."
    "Оля озабоченно нахмурилась."

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)

    voice "voice/olya/73 O.ogg"
    Oly "У Питера Пэна зубы молочные."
    voice "voice/olya/74 O.ogg"
    Oly "Вдруг со взрослыми зубами тебя не пустят в его страну?"

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/073. My czto.ogg"
    Ant "Мы что-нибудь обязательно придумаем."

    show Olya Amaze m_day 00 good ahead 05 with Dissolve (0.2)

    voice "voice/olya/75 O.ogg"
    Oly "Попросим папу исправить тебе возраст в паспорте."

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/074. S czego.ogg"
    Ant "С чего это папа будет документы подделывать?"
    "Оля куснула бутерброд и сказала с набитым ртом:"

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)

    voice "voice/olya/76 O.ogg"
    Oly "Будет-будет! Мама говорила, что он так делал, а я подслушала."

    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    voice "voice/anton/1day/075. Smotri.ogg"
    Ant "Смотри, уши вырастут, как у Дамбо."
    "Оля всполошилась, потрогала себя за мочку. Я улыбнулся тайком."

    play test_one "sounds/Pen_01-fix-tuned.ogg"

    "Сестра замолчала - теперь она уминала хлеб, наблюдая за похождениями Пэна, феи Динь-Динь и Джеймса Крюка."

    stop music fadeout 5.0

    "Словно действительно переместилась в сказочную Небыляндию."

    show bg_black:
        alpha 0.0
        linear 5.0 alpha 1.0
    "Что греха таить, и я часто представлял себя там, в стране, где не взрослеют, не ссорятся из-за пустяков, не слушают ночами ругань за стеной и звон посуды."

    jump bunny1_continue1


label bunny1_pref1:
    $ story_manager.MarkEvent(("day1", "tv", "record"))
    $ Flags.Raise("record")
    stop music2 fadeout 5.0

    scene tv_1_up_pomehi:
        yalign 0.5
        linear 2.0 yalign 0.0
    $ renpy.pause(2.0)
    scene tv_1_up_pomehi:
        yalign 0.0
    $ renpy.pause(1.0)
    scene bg_rep_04 with Dissolve (0.5)
    $ renpy.pause(1.0)

    stop fon fadeout 1.0
    play test_one "sounds/rep/interference-2.ogg"
    show bg_rep_4_1 at for_tv_1
    show bg_rep_4_2 at for_tv_1
    show bg_rep_3_1 at for_tv_1
    show bg_rep_3_2 at for_tv_1
    show bg_rep_2_1 at for_tv_1
    show bg_rep_2_2 at for_tv_1
    show bg_rep_1_1 at for_tv_1
    show bg_rep_1_2 at for_tv_1
    show bg_rep_0 at for_tv_1
    show bg_glich_0
    with Dissolve (0.2)

    "Наконец-то изображение стало чётче."

    stop music2 fadeout 5.0
    play music "music/19_Reportage.ogg" fadein 5.0
    $ music_during_lines = 0.7

    "Не успел я обрадоваться, что поймал новый сигнал, как вдруг телевизор громко закашлял, и сквозь какофонию звуков прорвался голос."

    voice "voice/dictor/01 D.ogg"
    Dic "Видели его часто..."
    voice "voice/dictor/02 D.ogg"
    Dic "Именно тогда..."

    "На экране вырисовывались заснеженные холмики, поверх которых плясали кривые кресты, а мужской голос заунывно и неторопливо вёл свой рассказ."

    voice "voice/dictor/03 D.ogg"
    Dic "Стояла беспросветная кладбищенская ночь."

    show bg_rep_senya behind bg_glich_0
    with Dissolve(.5)

    voice "voice/dictor/04 D.ogg"
    Dic "В то мрачное время маленькая Сеня встретила свою судьбу в лице чудовищного обитателя дикой чащобы."
    voice "voice/dictor/05 D.ogg"
    Dic "Местные называют его не иначе как Хозяин леса."

    "Я замер, стараясь не шевелиться, словно своим движением мог спугнуть диктора. Внимательно вслушивался в каждое слово."

    voice "voice/dictor/06 D.ogg"
    Dic "Зверь разобрался с беспомощной девочкой по-хозяйски..."

label staruha1:
    scene bg_rep_snow_1 with Dissolve (0.1)
    show bg_glitch_1

    "Камера медленно плыла по заляпанному чем-то чёрным снегу, высматривая разбросанные всюду лохмотья одежды."
    "Мне не хотелось думать, были ли в них завёрнуты останки Cенечки, и я непроизвольно зажмурился."

    window hide
    show bg_rep_snow_2
    $ renpy.pause(2.40, hard = True)
    window show

    "Голос не переставал:"

    voice "voice/dictor/07 D.ogg"
    Dic "Волки здесь редкие гости."

    play test_one "sounds/rep/tv-noise-2.ogg"
    scene bg_rep_04 with Dissolve (0.1)
    scene bg_tamara with Dissolve (0.1)
    stop test_one
    show bg_glitch_1
    with Dissolve (0.5)

    voice "voice/dictor/08 D.ogg"
    Dic "Вот что поведала нам баба Тамара, обитательница одного из местных склепов."
    voice "voice/tamara/00T.ogg"
    "Изувеченное жизнью и алкоголем лицо старой бездомной задребезжало во весь экран."
    voice "voice/tamara/01 T.ogg"
    Tam "Да, да... Бестия страшенная, хуже мертвеца отрытого."
    voice "voice/tamara/03A.T.ogg"
    "Старуха забрызгала слюной прямоугольник микрофона."

    window hide
    show pshhh_forest
    $ renpy.pause(0.35)
    play test_one "sounds/rep/tv-noise-2.ogg"
    $ renpy.pause(0.1)
    stop test_one
    $ renpy.pause(2.25)
    play test_one "sounds/rep/tv-noise-2.ogg"
    $ renpy.pause(0.1)
    stop test_one
    window show

    voice "voice/tamara/02 T.ogg"
    Tam "И смердит ишшо. Как..."
    voice "voice/tamara/02A T.ogg"
    "Гудок проглотил сравнение."
    voice "voice/tamara/03 T.ogg"
    Tam "Не пряпомню я такой вони."
    voice "voice/tamara/04 T.ogg"
    Tam "Стояла энта тварюга тама, где ты, милок, сейчас стоишь, и таращалася на мяня, прям посяредь дня."
    voice "voice/tamara/05 T.ogg"
    Tam "Здоровенна така, глаза стеклянны..."
    voice "voice/tamara/05A T.ogg"
    "Опять пикнуло, скрадывая ругань."
    voice "voice/tamara/06 T.ogg"
    Tam "Говорять, что если тебя энтот диавол заприметить, то сунет в мяшок к сябе — и дело с концом."
    voice "voice/tamara/07 T.ogg"
    Tam "Ха-ха-ха. Но мяня он не трогаеть. Ха-ха!"
    voice "voice/tamara/08 T.ogg"
    Tam "Видать, нравлюсь я ему."
    voice "voice/tamara/09 T.ogg"
    Tam "Вот и зовуть мяня чёртовой нявестой. Ха-ха-ха-ха-ха!"
    voice "voice/dictor/09 D.ogg"
    Dic "Что правда, то правда."
    voice "voice/dictor/10 D.ogg"
    Dic "Опустившимися до звериного образа жизни хищник брезгует, предпочитая детскую невинную кровь."
    voice "voice/dictor/11 D.ogg"
    Dic "Теперь всё чаще Хозяина леса видят в поселениях на периферии нашей родины."
    "Раздираемый сомнениями, вымысел это или правда, я почему-то захотел записать остатки репортажа."
    "Быстро схватив лежавшую на телевизоре кассету и даже не посмотрев, что на ней записано, я сунул её в видик."

    play test_one "sounds/vhs/vhs-in-1.ogg"

    "Включил запись, накрутил звук и стал внимательно следить за ускользающим сигналом."

    play test_one "sounds/rep/tv-noise-2.ogg"
    scene bg_rep_04 with Dissolve (0.1)
    stop test_one
    scene rep_forest_one with Dissolve (0.1)
    show bg_glitch_final
    show bg_glitch_1

    voice "voice/dictor/12 D.ogg"
    Dic "Хозяином леса его прозвали не просто так."
    voice "voice/dictor/13 D.ogg"
    Dic "Ему подчиняются все звери, пернатые и лохматые. Они - предвестники появления самого чудовища."
    voice "voice/dictor/14 D.ogg"
    Dic "Если слышите вой вдалеке, то, скорей всего, он знает, где вы живёте."
    $ music_during_lines = 1.0

    stop music fadeout 2.0

    voice "voice/dictor/15 D.ogg"
    Dic "Если порог дома истоптан звериными следами, а за окном караулят птицы, прячьтесь — он уже идёт за вами."

    show bg_rep_04:
        alpha 0.0
        linear 1.0 alpha 1.0
    show bg_grey:
        alpha 0.0
        linear 1.0 alpha 0.5

    show bg_glitch_final
    show bg_glitch_1


    voice "voice/dictor/16 D.ogg"
    Dic "А если однажды ночью, проснувшись, вы увидите глаза в окне, то скоро..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."
    voice "voice/dictor/17 D.ogg"
    Dic "Cкоро..."
    Dic "..."

    window hide None
    play music "music/skoro_2.ogg"
    scene bg_rep_07 with Dissolve (0.1)
    show bg_glitch_final
    show bg_glitch_1
    $ renpy.pause(2.0, hard=True)
    scene bg_rep_04 with Dissolve (0.1)
    show bg_rep_05
    show bg_rep_0_2
    show bg_glitch_final
    show bg_glitch_1
    $ renpy.pause(4.0, hard=True)
    show bg_rep_glaz with Dissolve (0.1)
    show bg_glitch_final
    show bg_glitch_1
    window show

    "Взбесившийся телевизор закольцевал последнее слово диктора, оно повторялось опять и опять, впивалось в уши."

    window hide
    scene bg_rep_06
    show bg_glitch_final
    show bg_glitch_1
    $ renpy.pause(1.5, hard=True)
    play fon "sounds/rep/tv-noise-2.ogg" fadein 2.0
    stop music fadeout 2.0
    scene bg_rep_04 with Dissolve (0.1)
    $ renpy.pause(0.5, hard=True)
    scene tv_1_up_pomehi:
        yalign 0.0
    window show

    "По спине бежали мурашки."

    stop fon fadeout 2.0
    play test_one "sounds/vhs/Vhs_revers.ogg"

    "Кассета закончилась и теперь перематывалась к началу."
    "Шорох плёнки напоминал шелест листвы на ветру и тихое рычание зверя."
    "Я вышел из ступора, ткнул пальцем в кнопку."

    play test_one "sounds/vhs/vhs-out-1.ogg"

    "Магнитофон выплюнул кассету – на миг почудилось, что она испачкана в слюнях."
    "Но это лишь свет люстры заставлял чёрный пластик переливаться."

    scene VHS with Dissolve (0.5)

    "И тут я заметил обложку."
    "Ёлки! Я же на «Питера Пэна» записал!"
    "Поторопился."
    "Мало того, что испортил Олин мультфильм, так ещё и такой жутью."
    "Нельзя, чтобы сестра это увидела. Слёз будет – океан."

    scene bg_Olga_room_day
    show tv_pomehi
    with Dissolve (0.5)

    "Я украдкой посмотрел на дверь."
    "В коридоре задребезжали стаканы, скрипнули половицы."

    play test_one "sounds/steps/Olay_go.ogg"
    play music2 "music/25_Olya.ogg" volume 0.7 fadein 3.0

    "Оля материализовалась в дверном проёме."

    voice "voice/olya/67 O.ogg"
    Oly "Ты не смотришь без меня?"

    show Olya00 with Dissolve (0.5)

    "В руках у сестры был поднос с неровно нарезанным хлебом и целой банкой сгущёнки."
    voice "voice/anton/1day/076. Em net.ogg"
    Ant "Эм, нет..."
    voice "voice/anton/1day/076. Ya poka.ogg"
    Ant "Я пока кассету ищу."
    voice "voice/anton/1day/077. A ti tochno.ogg"
    Ant "А ты точно хочешь «Питера Пэна» смотреть?"

    scene bg_Olga_room_day
    show tv_pomehi
    show Olya Amaze m_day 00 good ahead 05
    with Dissolve (0.5)

    voice "voice/olya/77 O.ogg"
    Oly "Хочу-хочу!"
    voice "voice/olya/78 O.ogg"
    Oly "Включай скорее, а то мама скоро сядет свой бразильский сериал смотреть."

    show Olya Amaze m_day 00 good ahead 01 with Dissolve (0.3)

    "Ну же, думай, горе-сыщик."

    voice "voice/anton/1day/078. Chestno mne.ogg"
    Ant "Честно, мне как-то «Питер Пэн» совсем не понравился."
    voice "voice/anton/1day/078. Mozet luche.ogg"
    Ant "Может, лучше «Русалочку»?"

    show Olya Serious m_day 00 good ahead 03
    with Dissolve (0.3)

    voice "voice/olya/79 O.ogg"
    Oly "«Русалочку» я уже насмотрелась."

    show Olya Serious m_day 00 good ahead 05
    with Dissolve (0.3)

    voice "voice/olya/80 O.ogg"
    Oly "А ты обещал!"

    show Olya Serious m_day 00 good ahead 01
    with Dissolve (0.3)

    "Вот до чего ж упрямая."
    voice "voice/anton/1day/079. Pridumal davai.ogg"
    Ant "Придумал! Давай сначала пару серий «Черепашек-ниндзя», согласна?"
    "Оля насупила брови, но, похоже, сдалась."
    "Она отставила поднос и демонстративно скрестила руки на груди."

    scene Olya01
    with Dissolve (0.5)

    voice "voice/olya/81 O.ogg"
    Oly "Если так сильно просишь..."
    voice "voice/olya/82 O.ogg"
    Oly "Откроешь сгущёнку? Порезаться боюсь — края острые..."

    show old_movie_001_002:
        alpha 1.0
        linear 0.2
        alpha 0.0

    "Стоило подняться, как перед глазами запрыгали разноцветные точки, а онемевшие ноги закололо иголочками."
    "И только добравшись до дивана, я сообразил, что банка была уже открыта."
    "Оля схитрила, обвела меня вокруг пальца."

    play test_one "sounds/steps/Olya-ladder-steps-1.ogg"

    "Под ложечкой засосало."

    scene bg_Olga_room_day
    show tv_pomehi
    show Olya Serious m_day 00 good ahead 01
    with Dissolve (0.5)

    "Я намеревался рвануть к телевизору, но сестра опередила."
    "Схватив пульт, она победоносно рассмеялась:"

    show Olya Happy m_day 00 good ahead 04 with Dissolve (0.2)

    voice "voice/olya/83 O.ogg"
    Oly "Повёлся, повёлся!"

    stop music2 fadeout 5.0

    voice "voice/olya/84 O.ogg"
    Oly "Владычица пульта приказывает смотреть «Питера Пэна»!"

    scene VHS
    show bg_black:
        alpha 0.0
        linear 1.5
        linear 0.5 alpha 1.0
    with Dissolve (0.5)

    play test_one "sounds/vhs/vhs-in-2.ogg"
    play music2 "music/21_He is near.ogg" fadein 3.0
    $ music_during_lines = 0.5

    "Не успел я и рта раскрыть, как видик послушно съел злосчастную кассету."
    "Сейчас она включит, а там..."
    "Чёрные кресты на безымянных могилах и опустошённые склепы, кровавые ошмётки на снегу и безумная невеста лесной твари."
    "Лучше сказать правду."

    scene bg_Olga_room_day
    show tv_pomehi
    show Olya Serious m_day 00 good ahead 01
    with Dissolve (0.5)

    voice "voice/anton/1day/080. Olja_st.ogg"
    Ant "Оля, стой!"
    voice "voice/anton/1day/080. YA tebe.ogg"
    Ant "Я тебе конец кассеты нечаянно стёр."
    voice "voice/anton/1day/081. Otdai.ogg"
    Ant "Отдай её мне и возьми любые две мои."

    show Olya Serious m_day 00 good ahead 03 with Dissolve (0.2)

    voice "voice/olya/85 O.ogg"
    Oly "Ты чего?"
    voice "voice/olya/86 O.ogg"
    Oly "Не мог ты стереть: мы с папой всем кассетам зубики пластмассовые выломали. Отвёрткой."
    voice "voice/olya/87 O.ogg"
    Oly "Теперь ни на один мой мультфильм ничего записать нельзя."
    $ music_during_lines = 1.0

    stop music2 fadeout 5.0
    show Olya Serious m_day 00 good ahead 01 with Dissolve (0.2)

    "Сестра ловко нажала треугольную кнопку «Play» на пульте."

    show tv_multiki
    hide tv_pomehi
    with Dissolve (0.2)

    "Я внутренне сжался, ожидая услышать потусторонний голос диктора."

    play test_one "sounds/Pen_01-fix-tuned.ogg"

    "Но на экране появилась дуэль Питера Пэна с капитаном Крюком."

    play music2 "music/25_Olya.ogg" fadein 3.0

    voice "voice/anton/1day/082. YA oble.ogg"
    "Я облегчённо выдохнул."
    "Голова опустилась на ладони, тяжёлая, словно чугунный шар."

    show Olya Happy m_day 00 good ahead 04 with Dissolve (0.2)

    "Оля довольно улыбнулась."

    scene Olya00 with Dissolve (0.5)
    play test_one "sounds/vhs/vhs-forward-1.ogg"

    "Отправила кассету мотаться на начало, а сама принялась обильно поливать хлеб сгущёнкой."
    "А когда начался мультфильм, она забыла про всё на свете."

    scene bg_Olga_room_day
    show tv_multiki
    with Dissolve (0.5)

    "Словно и правда переместилась в сказочную Небыляндию, о которой всегда мечтала."
    "Что греха таить, и я часто представлял себя там, в стране, где не взрослеют, не ссорятся из-за пустяков, не слушают ночами ругань за стеной и звон посуды."

    stop music2 fadeout 5.0

    "Но сейчас страна Питера Пэна была особенно далека от меня."

    show bg_black:
        alpha 0.0
        linear 5.0 alpha 1.0

    "Мысли тянулись, натыкались на рогатую тень, подстерегающую среди деревьев, а замогильный голос диктора преследовал, низко скользя над кустами и оврагами."
    "Так крылатый хищник преследует жертву."

    jump bunny1_continue1


label bunny1_continue1:
    $ story_manager.MarkEvent(("day1", "scene10"))
    play music "music/27_Cry.ogg" volume 0.95 fadein 5.0
    $ music_during_lines = 0.5

    "Я будто задремал с открытыми глазами."
    "В реальность вернул резкий оклик сестры:"

    scene bg_Olga_room_n_1
    show Olya Weeps b_night 00 good ahead 04:
        xzoom -1.0
    show bg_black:
        alpha 1.0
        linear 0.5 alpha 0.0

    voice "voice/olya/88 O.ogg"
    Oly "Тоша, скорей штору задёрни!"
    voice "voice/anton/1day/083. Zaczem.ogg"
    Ant "Зачем?"
    voice "voice/anton/1day/083.Nikto zh.ogg"
    Ant "Никто же на тебя не смотрит."

    show Olya Weeps b_night 00 good ahead 02:
        xzoom -1.0
    with Dissolve (0.2)

    voice "voice/olya/89 O.ogg"
    Oly "Уже темно, а когда темнеет, прилетает сова..."
    voice "voice/olya/90 O.ogg"
    Oly "Я... Я боюсь."

    hide Olya with Dissolve (0.2)
    play test_one "sounds/steps/Anton-steps-in-1.ogg"

    "Превозмогая усталость, я слез с кровати и задёрнул штору."

    window hide
    call screen olya_room_day_1_close_circle

    show layer master:
        subpixel True
        align (.5, .5)
        zoom 1.0
        ease 1.5 zoom 1.15

    pause 2.

    play test_one "sounds/curtain.ogg"
    scene bg_Olga_room_n_2
    show layer master:
        subpixel True
        align (.5, .5)
        zoom 1.15
        1.
        ease 1.5 zoom 1.0
    with Dissolve (0.2)
    window show

    "Старался при этом не смотреть наружу, на пики сосен, на тайгу, которая в сумерках словно приближалась к дому."
    "Хотя, конечно, это лишь корябающие снег тени создавали впечатление, что сосны двигаются."

    show Olya Serious m_night 01 good ahead:
        xzoom -1.0
    with Dissolve (0.2)

    voice "voice/olya/91 O.ogg"
    Oly "Тоша, мама думает, что я напридумывала про сову."
    voice "voice/olya/92 O.ogg"
    Oly "И папа считает, что раз я маленькая, то, значит, врушка."

    show Olya Weeps m_night 01 good ahead:
        xzoom -1.0
    with Dissolve (0.2)

    voice "voice/olya/93 O.ogg"
    Oly "А сова есть!"
    voice "voice/olya/94 O.ogg"
    Oly "Вот честное-пречестное – есть она!"
    voice "voice/olya/95 O.ogg"
    Oly "Ты же мне веришь?"
    voice "voice/olya/96 O.ogg"
    Oly "Что она там и каждую ночь прилетает, и... и..."

    show layer master:
        subpixel True
        align (.5, 1.)
        zoom 1.0
        ease .5 zoom 1.10
    "Я порывисто взял Олю за руку, посмотрел в глаза."
    "Словно пытался передать ей каплю смелости и уверенности."
    "Но есть ли эти качества во мне самом?"

    scene day_03_hight_ola_room_05_06
    with Dissolve(.5)
    voice "voice/anton/1day/084. YA tebe.ogg"
    Ant "Я тебе верю, слышишь?"
    voice "voice/anton/1day/084.Ty tol.ogg"
    Ant "Ты только родителям больше не рассказывай про сову."
    voice "voice/anton/1day/085. U nih.ogg"
    Ant "У них и так хлопот по горло, они только рассердятся."
    voice "voice/anton/1day/085. Ty mne.ogg"
    Ant "Ты мне говори, если что случится."
    voice "voice/anton/1day/086. I v ok.ogg"
    Ant "И в окно не смотри."

    scene bg_Olga_room_n_2
    show Olya Weeps m_night 01 good ahead:
        xzoom -1.0
    with Dissolve (0.5)
    voice "voice/olya/97 O.ogg"
    Oly "Но она хочет, чтобы я смотрела."

    show Olya Serious m_night 01 good ahead
    with Dissolve (0.2)

    voice "voice/anton/1day/087. Pereho.ogg"
    Ant "Перехочет!"
    voice "voice/anton/1day/088. Pritvo.ogg"
    Ant "Притворись, что её нет и не было никогда, что она выдумка, как родители говорят."
    voice "voice/anton/1day/089. Ei zhda.ogg"
    Ant "Ей ждать надоест — она улетит."
    $ music_during_lines = 1.0

    window hide
    show bg_black:
        alpha 0.0
        linear 4.0 alpha 1.0
    $ renpy.pause(4.0, hard=True)


    if Flags.Has("gloves"):
        window show
        "Безумие, но после всех событий я всё больше верил, что олина сова существует"
        "..."
        window hide


    stop music fadeout 5.0

    scene bg_Olga_room_n_2
    show layer master:
        align (.25, .65)
        zoom 2
    show bg_black:
        alpha 1.0
        linear 5.0 alpha 0.0
    play music "music/26_Mistik.ogg" fadein 3.0
    $ renpy.pause(5.0, hard=True)
    window show

    "Мы следили за приключениями Питера Пэна, будто не было ничего: ни леса, который похищал детей, ни родителей, которые поедали друг друга по кусочку."

    play test_one "sounds/Pen_02-fix-tuned.ogg"

    "Капитан Крюк улепётывал от крокодила, капитан Пэн направлялся в Лондон на золотом паруснике."
    "Чудом я пересидел сестру."
    "Олины веки слиплись, она засопела, опустив подбородок на изголовье кровати."


    if Flags.Has("record"):
        stop music fadeout 2.0
        play music2 "music/19_Reportage.ogg" fadein 2.0

        "Хор пел финальную песенку, в диснеевском мире сияла серебристая луна."

        window hide
        play test_one "sounds/rep/tv-noise-2.ogg"
        $ renpy.pause(0.1)
        stop test_one
        scene pshhh_forest_repeat
        show bg_Olga_room_n_2_evil:
            alpha 0.0
            linear 2.05
            linear 0.2 alpha 1.0
        $ renpy.pause(2.0)
        play test_one "sounds/rep/tv-noise-2.ogg"
        $ renpy.pause(0.1)
        stop test_one
        window show

        "Из-под этой нарисованной луны внезапно выглянула другая."
        "Страшная и мёртвенная, висящая над таёжным бором."
        "Жуткий репортаж записался аккурат на титры мультфильма."
        "Во рту у меня пересохло. Пульс участился."

        scene Olya_sleep with Dissolve (0.4)

        "Я быстро посмотрел на Олю."

        show Olya_sleep_up:
            alpha 0.0
            linear 0.2 alpha 1.0
            linear 0.4
            linear 0.2 alpha 0.0
        $ renpy.pause(0.8, hard = True)

        "Она причмокнула губами во сне."

        stop fon fadeout 1.5
        scene bg_Olga_room_n_2
        show tv_pomehi
        with Dissolve (0.4)
        stop music2 fadeout 3.0

        "Я стиснул пульт, готовый в любой момент нажать кнопку «Stop»."

        play music "music/26_Mistik.ogg" fadein 5.0

        play test_one "sounds/vhs/vhs-forward-1.ogg"
        queue test_one "sounds/vhs/vhs-out-1.ogg"

        "Промотал запись и оценил сохранность репортажа, а затем бережно вытащил кассету."

        scene VHS_dark with Dissolve (0.4)

        "Защитный зубец оказался на месте."
        scene bg_Olga_room_n_2
        show tv_pomehi
        show layer master:
            align (.25, .65)
            zoom 2
        with Dissolve(.5)
        pause 0.5



    scene bg_Olga_room_Evil_full
    show layer master:
        align (.25, .65)
        zoom 2
    show bg_black:
        alpha 0.0
        linear 4.0 alpha 1.0
    with Dissolve(.15)
    pause 0.5

    show layer master:
        align (.25, .65)
        zoom 2
        ease .5 zoom 1.85
        .25
        ease .5 zoom 1.70
        .25
        ease .5 zoom 1.55
        .25
        ease .5 zoom 1.40
        .25
        ease .5 zoom 1.25
        .25
        ease .5 zoom 1.10

    "Я встал осторожно и покинул детскую."
    window hide
    scene bg_black with Dissolve(1.)
    pause 1



    if Flags.Has("record"):
        play test_one "sounds/desk-open-00.ogg"
        window hide
        scene bg storage_in_table1_dark
        if Flags.Has("number"):
            show item_in_table_number_dark
        if Flags.Has("glove"):
            show item_in_table_glove_dark
        with Dissolve(0.5)
        $ renpy.pause(1.0, hard=True)
        play test_two "sounds/vhs/Vhs_put.ogg"
        show item_in_table_record_dark with Dissolve(0.2)
        window show

        if Flags.Has("glove"):
            "Не знаю, провиденье это или проклятье, но кассету я успел спрятать рядом с варежкой как раз перед тем, как заглянула в комнату мама."
        else:
            "Не знаю, провиденье это или проклятье, но кассету я успел спрятать как раз перед тем, как заглянула в комнату мама."
        $ achievement_grant("ach_tape")

        play test_one "sounds/desk-close-00.ogg"
        window hide
        scene bg storage_in_table0_dark with Dissolve(0.5)
        $ renpy.pause(1.0, hard=True)
        play test_two "sounds/steps/mam_in.ogg"
        scene bg room_night_ZOOM
        with Dissolve(0.5)
        $ renpy.pause(0.2, hard=True)
        play test_five "sounds/creaks-2.ogg"
        show door open_door1
        with Dissolve(0.5)
        show Mom Normal m_night 00 norm ahead:
            xpos 600
        with Dissolve(0.5)
        window show
    else:

        window show
        scene day3_window_bg_0:
            xalign 1.0
        show day3_window_frame:
            xalign 1.0
            blur 8
        with Dissolve(.5)
        "Я смотрел в окно, изучая поле, когда мама заглянула ко мне."
        window hide
        play test_two "sounds/steps/mam_in.ogg"
        pause 0.7
        play test_five "sounds/creaks-2.ogg"
        pause 1.0
        window show


    $ music_during_lines = 0.5
    voice "voice/karina/84 K.ogg"
    Mam "Довольно баловства."

    if not Flags.Has("record"):
        scene day3_window_bg_0:
            xalign 1.
            easeout 1. xalign 0.5
        show day3_window_frame:
            xalign 1.0
            blur 8
            easeout 1.0 xalign 0.
        with None
        pause 0.5
        scene bg room_night_ZOOM
        show door open_door1
        show Mom Normal m_night 00 norm ahead:
            xpos 600
        with Dissolve(0.5)

    voice "voice/karina/85 K.ogg"
    Mam "Завтра первый день в школе."
    voice "voice/karina/86 K.ogg"
    Mam "Ложись, тебе надо выспаться."

    hide Mom
    show Mom Normal m_night 00 norm aside:
        xpos 600
    with Dissolve(0.2)

    voice "voice/karina/87 K.ogg"
    Mam "Не хочешь же ты, чтобы тебя все дразнили соней?"
    $ music_during_lines = 1.0

    play test_two "sounds/steps/mam_out.ogg"
    window hide
    hide Mom
    with Dissolve(0.5)
    play test_one "sounds/close-door.ogg"
    $ renpy.pause(0.2, hard=True)
    scene bg room_night_ZOOM
    with Dissolve(0.5)
    window show

    "Как же у взрослых всё просто."

    play fon "sounds/fon/skrip1.ogg" fadein 3.0

    "Словно мой крепкий сон будет залогом того, что я понравлюсь одноклассникам."

    scene day1_kovai_3
    with Dissolve(.5)
    "Натянув одеяло под горло, я слушал, как бормочет дом, как в тёмных углах шуршит кто-то невидимый."

    show bg_black zorder 1:
        alpha 0.0
        linear 15.0 alpha 1.0
    "Внутренний голос задался вопросом: хочу ли я снова услышать ту странную флейту?"
    "Да или нет?"

    show bg_black:
        linear 10.0 alpha 1.0
    "Возможно, я взрослею и не могу до конца понять себя и свои желания."

    show bg room_night_ZOOM
    with Dissolve(.5)
    "Лес стенал за преградой стен."

    show bg_black:
        linear 6.0 alpha 1.0
    "Что-то бесплотное бродило по полям."

    show bg_black:
        linear 2.0 alpha 1.0
    "Шевелились ветви, будто звали."
    "И ветер выл и выл в ночи."
    "Мысли, как назойливые мухи, что лезли в голову, становились вялыми и путанными."

    stop music fadeout 5.0
    stop fon fadeout 5.0

    "Я сам не заметил, как провалился в сон."

    window hide

    if true_detective_count1 == 15:
        $ achievement_grant("ach_detective_1")
        $ persistent.has_d1_detective = True

    scene black with Dissolve(0.5)

    if not story_manager.IsMarkedLocal(("day1", "scene0")):
        python:
            events = ConvertFlagsToEvents(Flags, days=("day1",))
            story_manager.Extend( events )

    python:
        story_manager.width = 1920
        story_manager.height = 5790 +600
        story_manager.day_code = "day1"



    show screen StoryExplainerDCut_Day1(story_manager) with Dissolve(1.5)
    $ ui.interact()

    show screen StoryExplainerDCut_Hider
    with Dissolve(1.5)

    jump day_2


screen StoryExplainerDCut_Day1(story_manager):
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


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene3", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la hall", (960-800, y_val(0)), (75*2 + 400, 175+85*3+75+25), ("pantry", "cross", "ula", "phone"))

        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la kitchen", (960-200, y_val(175+85*1+75+25)), (75*2 + 400*2 + 40, 175+85*1+75+25), ("number", "calendar", "radio", "crossword"))

        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la fridge", (960-200+440, y_val(175+85*0+75+25)), (75*2 + 400, 175+85*0+75+25), ("freezer",))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene4", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene5", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "glove", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "glove", "run")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "glove", "take")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(100)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "glove", (960, y_val(0)), "run")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "glove", (960, y_val(0)), "take")

        $ y_val(75)
        $ y_val(75)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "glove", "take")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(175)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "glove", "run")):
                at arrow_valid
            else:
                at arrow_invalid


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene6", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene7", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "la anton")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "la anton")):
                at arrow_invalid
            else:
                at arrow_valid

        $ y_val(175-75)

        add "flowchart_arrow_down" anchor (.5, .0) pos (960 + 320, y_val(0)) yzoom 3.5:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "la anton")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175-100)


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la anton", (960-900, y_val(175+85*1+75+25)), (75*2 + 400*2 + 40, 175+85*1+75+25), ("toys", "curtains", "pics", "book"))


        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if not story_manager.IsMarkedLocal((story_manager.day_code, "la anton")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "la anton")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene8", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_LookaroundSegment(story_manager, story_manager.day_code, "la olya", (960 - (75+200), y_val(175+85*2+75+25)), (75*2 + 400, 175+85*2+75+25), ("pig", "curtains", "bear"))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene9", (960, y_val(75)))

        add "flowchart_arrow_down" anchor (.5, .0) pos (960, y_val(175))


        use StoryExplainer_ChoiceSegment(story_manager, story_manager.day_code, "tv", (960, y_val(75)))

        add "flowchart_arrow_left" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "tv", "peter")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "tv", "record")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(100)

        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "tv", (960, y_val(0)), "record")
        use StoryExplainer_OptionSegment(story_manager, story_manager.day_code, "tv", (960, y_val(0)), "peter")

        $ y_val(175)

        add "flowchart_arrow_left" anchor (0., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "tv", "record")):
                at arrow_valid
            else:
                at arrow_invalid
        add "flowchart_arrow_right" anchor (1., .0) pos (960, y_val(0)) xzoom .75:
            if story_manager.IsMarkedLocal((story_manager.day_code, "tv", "peter")):
                at arrow_valid
            else:
                at arrow_invalid

        $ y_val(175)


        use StoryExplainer_NarrativeSegment(story_manager, story_manager.day_code, "scene10", (960, y_val(0)))



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
