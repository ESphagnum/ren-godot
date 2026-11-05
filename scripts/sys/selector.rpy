init:
    if persistent.story_unlocks is None:
        $ persistent.story_unlocks = set()

















init python:

    choices_structure = {
    "day1": {
        "choices": ("number", "glove", "tv"),
        "number": {
            "_pos": (1, 0),
            "_start": "bunny_hall_day1_prepare",
            "caption": _("Номер Тихонова"),
            "options": ("take", "ignore"),
            "take": ("bunny_day1_open_door", _("Взять")),
            "ignore": ("bunny_day1_open_door", _("Не трогать")),
            },
        "glove": {
            "_pos": (2, 0),
            "_start": "main_choose2",
            "caption": _("Варежка на ветке"),
            "options": ("take", "run"),
            "take": ("take_anton", _("Взять")),
            "run": ("run_anton", _("Убежать")),
            },
        "tv": {
            "_pos": (3, 0),
            "_start": "bunny_day1_olya_room_photon.choice",
            "caption": _("Репортаж среди помех"),
            "options": ("record", "peter"),
            "record": ("bunny1_pref1", _("Записать")),
            "peter": ("bunny1_find1", _("Игнорировать")),
            },
        },
    "day2": {
        "choices": ("candy", "semen", "waifu", "witness_polina", "mask", "witness_fox"),
        "candy": {
            "_pos": (4, 0),
            "_start": "bunny2_night_meet_fox1",
            "caption": _("Конфета Алисы"),
            "options": ("take", "refuse"),
            "take": ("bunny2_take1", _("Взять")),
            "refuse": ("bunny2_cancel1", _("Отказаться")),
            },
        "semen": {
            "_pos": (5, 0),
            "_start": "bunny_day2_semen",
            "caption": _("Задирание Семёна"),
            "options": ("fight", "submit"),
            "fight": ("bunny2_semen_fight", _("Дать отпор")),
            "submit": ("bunny2_semen_lose", _("Стерпеть")),
            },
        "waifu": {
            "_pos": (6, 1),
            "_start": "bunny_day2_polina_or_fox",
            "caption": _("С кем идти домой"),
            "options": ("polina", "fox"),
            "polina": ("bunny2_polina_win", _("С Полиной")),
            "fox": ("bunny2_fox_win", _("С Алисой")),
            },
        "witness_polina": {
            "_pos": (7, 2),
            "_start": "polwit",
            "caption": _("Мужик в кустах"),
            "options": ("tapped", "ignored"),
            "tapped": ("bunny_day2_gop_stop", _("Заметить")),
            "ignored": ("bunny_day2_gop_stop", _("Не заметить")),
            },
        "mask": {
            "_pos": (8, 0),
            "_start": "bunny_day2_mask_or_not",
            "caption": _("Встреча с хулиганами"),
            "options": ("resist", "mask"),
            "resist": ("bunny2_skip_mask", _("Послать")),
            "mask": ("bunny2_take_mask", _("Надеть маску")),
            },
        "witness_fox": {
            "_pos": (9, 2),
            "_start": "bunny2_skip_mask",
            "caption": _("Мужик в лесу"),
            "options": ("tapped", "ignored"),
            "tapped": ("bunny2_home_evening", _("Заметить")),
            "ignored": ("bunny2_home_evening", _("Не заметить")),
            },
        },
    "day3": {
        "choices": ("minigame_case", "photorobot", "minigame_photorobot", "minigame_suefa", "amulet", "phonecall"),
        "minigame_case": {
            "_pos": (10, 0),
            "_start": "day_3_continue.minigame_start",
            "caption": _("Досье Тихонова"),
            "options": ("no_success", "success1", "success2"),
            "no_success": ("minigame_after", _("Не открывать")),
            "success1": ("minigame_after", _("Открыть 1 раз")),
            "success2": ("minigame_after", _("Открыть 2 раза")),
            },
        "photorobot": {
            "_pos": (12, 0),
            "_start": "minigame_after.choice",
            "caption": _("Подозрительный человек"),
            "options": ("silent", "tell"),
            "silent": ("silent", _("Промолчать")),
            "tell": ("tell_or_silent", _("Рассказать")),
            },
        "minigame_photorobot": {
            "_pos": (13, 0),
            "_start": "tell_or_silent.minigame_photorobot",
            "caption": _("Фоторобот"),
            "options": ("witness", "wrong"),
            "witness": ("minigame_after", _("Подозрительный мужик")),
            "wrong": ("minigame_after", _("Кто-то другой")),
            },
        "minigame_suefa": {
            "_pos": (14, 0),
            "_start": "dev_suefa",
            "caption": _("Суефа"),
            "options": ("win", "lose"),
            "win": ("suefa_win", _("Выиграть")),
            "lose": ("suefa_lose", _("Проиграть")),
            },
        "amulet": {
            "_pos": (15, 1),
            "_start": "day3_amulet_before",
            "caption": _("Амулет Полины"),
            "options": ("yes", "no"),
            "yes": ("day3_amulet_yes", _("Принять")),
            "no": ("day3_amulet_no", _("Отказаться")),
            },
        "phonecall": {
            "_pos": (16, -1),
            "_start": "day3_polinacall_notsolo.choice",
            "caption": _("Звонок Полины"),
            "options": ("betray", "voltron"),
            "betray": ("bunny3_betray_true", _("Полина")),
            "voltron": ("bunny3_betray_false", _("Вольтрон")),
            },
        },
    "day4": {
        "choices": ("byasha", "garage", "katya", "treat"),
        "byasha": {
            "_pos": (17, -1),
            "_start": "dev_byasha",
            "caption": _("Бяша"),
            "options": ("call", "dismiss"),
            "call": ("d4_byash_choice_call", _("Позвать")),
            "dismiss": ("d4_byash_choice_dismiss", _("Не звать")),
            },
        "garage": {
            "_pos": (18, -1),
            "_start": "d4_byash_choice_call.choice",
            "caption": _("Гараж в тайге"),
            "options": ("enter", "police"),
            "enter": ("d4_garage_choice_enter", _("Войти")),
            "police": ("d4_garage_choice_police", _("В полицию")),
            },
        "katya": {
            "_pos": (19, -1),
            "_start": "d4_save_katya",
            "caption": _("Спасение Кати"),
            "options": ("save", "kill"),
            "save": ("sK2_good", _("Спасти")),
            "kill": ("sK_fail_end", _("Дать умереть")),
            },
        "treat": {
            "_pos": (20, 0),
            "_start": "d4_beasts",
            "caption": _("Угощение Деда Мороза"),
            "options": ("accept", "refuse1", "refuse2"),
            "accept": ("d4_beasts_choice_take", _("Принять")),
            "refuse1": ("d4_beasts_choice_refuse", _("Отказаться 1 раз")),
            "refuse2": ("d4_beasts_choice2_refuse", _("Отказаться 2 раза")),
            },
        },
    "day5": {
        "choices": ("zhulka", "polkatya", "drug_polina", "drug_katya", "guests", "faith", "sacrifice_refuse", "sacrifice_accept", "cross1", "cross2", "cross3", "amulet", "pololya", "carmask_olya", "carmask_solo", "final_mask", "sigma_simp"),
        "zhulka": {
            "_pos": (22, 0),
            "_start": "d5_choice_zhulka",
            "caption": _("Жулька"),
            "options": ("kill", "spare"),
            "kill": ("zhulka_kill", _("Убить")),
            "spare": ("zhulka_mercy", _("Помиловать")),
            },
        "polkatya": {
            "_pos": (23, 0),
            "_start": "d5_polkatya_dev",
            "caption": _("Уход из школы"),
            "options": ("polina", "katya"),
            "polina": ("event_m_polina", _("Полина")),
            "katya": ("event_m_katya", _("Катя")),
            },
        "drug_polina": {
            "_pos": (24, -2),
            "_start": "event_m_polina_followup.afterdev",
            "caption": _("Лекарство у Полины"),
            "options": ("take", "refuse"),
            "take": ("event_m_polina_accept", _("Принять")),
            "refuse": ("event_m_polina_refuse", _("Отказаться")),
            },
        "drug_katya": {
            "_pos": (24, 2),
            "_start": "event_m_katya_after_game.afterdev",
            "caption": _("Лекарство у Кати"),
            "options": ("take", "refuse"),
            "take": ("event_m_katya_accept", _("Принять")),
            "refuse": ("event_m_katya_refuse", _("Отказаться")),
            },
        "guests": {
            "_pos": (25, 0),
            "_start": "phase4_guests.choice",
            "caption": _("Приход гостей"),
            "options": ("invite", "hodor"),
            "invite": ("event_invited", _("Впустить")),
            "hodor": ("event_closed_door", _("Не впускать")),
            },
        "faith": {
            "_pos": (26, 0),
            "_start": "event_monsters_came.faith",
            "caption": _("Вопрос веры"),
            "options": ("cross", "amulet"),
            "cross": ("event_monsters_faith_cross", _("Крест")),
            "amulet": ("event_monsters_faith_amulet", _("Амулет")),
            },
        "sacrifice_refuse": {
            "_pos": (28, -2),
            "_start": "d5_choice_monsters_refuse",
            "caption": _("Выбор жертвы"),
            "options": ("anton", "olya", "roma", "polina", "dogmeat"),
            "anton": ("event_monsters_anton_refuse", _("Антон")),
            "olya": ("event_monsters_olya_choice", _("Оля")),
            "roma": ("event_monsters_roma", _("Рома")),
            "polina": ("event_monsters_polina_choice", _("Полина")),
            "dogmeat": ("event_monsters_dog_refuse", _("Собачатина")),
            },
        "sacrifice_accept": {
            "_pos": (28, 3),
            "_start": "d5_choice_monsters_accept",
            "caption": _("Время жертвы"),
            "options": ("anton", "olya"),
            "anton": ("event_monsters_anton_accept", _("Антон")),
            "olya": ("event_monsters_olya_choice", _("Оля")),
            },
        "cross1": {
            "_pos": (30, -3),
            "_start": "event_monsters_polina_cross.choice",
            "caption": _("Крест в первый раз"),
            "options": ("pray", "run"),
            "pray": ("event_monsters_polina_cross_2", _("Молится")),
            "run": ("d5_ending_pack_of", _("Бежать")),
            },
        "cross2": {
            "_pos": (31, -3),
            "_start": "event_monsters_polina_cross_choice_2",
            "caption": _("Крест во второй раз"),
            "options": ("pray", "run"),
            "pray": ("event_monsters_polina_cross_3", _("Молится")),
            "run": ("d5_ending_pack_of", _("Бежать")),
            },
        "cross3": {
            "_pos": (32, -3),
            "_start": "event_monsters_polina_cross_3.choice",
            "caption": _("Крест в третий раз"),
            "options": ("pray", "run"),
            "pray": ("d5_ending_still_water", _("Молится")),
            "run": ("d5_ending_rage", _("Бежать")),
            },
        "amulet": {
            "_pos": (31, 1),
            "_start": "event_monsters_polina_amulet.choice",
            "caption": _("Что делать с амулетом"),
            "options": ("olya", "self", "run"),
            "olya": ("d5_ending_bloody_claw", _("Отдать Оле")),
            "self": ("d5_ending_among_us", _("Оставить себе")),
            "run": ("d5_ending_pack_of", _("Бежать")),
            },
        "pololya": {
            "_pos": (33, 0),
            "_start": "event_monsters_dog_roma",
            "caption": _("Сугроб"),
            "options": ("olya", "polina"),
            "olya": ("event_runaway_girlstrapped_roma_olya", _("Спасти Олю")),
            "polina": ("event_runaway_girlstrapped_roma_polina", _("Спасти Полину")),
            },
        "carmask_olya": {
            "_pos": (34, -2),
            "_start": "event_final_battle_olyayes.choice",
            "caption": _("В машине с Олей"),
            "options": ("mask", "face"),
            "mask": ("event_final_battle_yes_mask", _("Надеть маску")),
            "face": ("event_final_battle_yes_mom", _("Не надевать маску")),
            },
        "carmask_solo": {
            "_pos": (34, 2),
            "_start": "event_final_battle_olyano.choice",
            "caption": _("В машине сам"),
            "options": ("mask", "face"),
            "mask": ("d5_ending_nightmare", _("Надеть маску")),
            "face": ("event_final_battle_no_face", _("Не надевать маску")),
            },
        "final_mask": {
            "_pos": (35, -1),
            "_start": "event_slaughter.choice",
            "caption": _("Финальное решение"),
            "options": ("wear", "break"),
            "wear": ("d5_ending_recipe", _("Надеть")),
            "break": ("event_final_break", _("Разбить")),
            },
        "sigma_simp": {
            "_pos": (36, -1),
            "_start": "d5_choice_simp_sigma",
            "caption": _("Полина"),
            "options": ("polina", "solo"),
            "polina": ("d5_ending_genius", _("Взять за руку")),
            "solo": ("d5_ending_contract", _("Отстраниться")),
            },
        }
    }


init python:
    story_node_type_narration = 0
    story_node_type_lookaround = 1
    story_node_type_item = 2
    story_node_type_choice = 3
    story_node_type_option = 4
    story_node_type_minigame = 5

    story_so_far = {
    "rday1":{
        "scene0": {
            "type": story_node_type_narration,
            "caption": "Пролог",
            "pos": (0, 0),
        },
        "scene1": {
            "type": story_node_type_narration,
            "caption": "Завтрак",
            "pos": (0, 1),
        },
        "scene2": {
            "type": story_node_type_narration,
            "caption": "Флешбек",
            "pos": (0, 2),
        },
        "scene3": {
            "type": story_node_type_narration,
            "caption": "Милиция",
            "pos": (0, 3),
        },
        "scene4": {
            "type": story_node_type_narration,
            "caption": "Лес",
            "pos": (0, 7),
        },
        "scene5": {
            "type": story_node_type_narration,
            "caption": "Варежка",
            "pos": (0, 8),
        },
        "scene6": {
            "type": story_node_type_narration,
            "caption": "Бег домой",
            "pos": (0, 11),
        },
        "scene7a": {
            "type": story_node_type_narration,
            "caption": "Комната Антона (вар.А)",
            "pos": (1, 12),
        },
        "scene7b": {
            "type": story_node_type_narration,
            "caption": "Комната Антона (вар.Б)",
            "pos": (-1, 12),
        },
        "scene8": {
            "type": story_node_type_narration,
            "caption": "Разговор с Олей",
            "pos": (0, 16),
        },
        "scene9": {
            "type": story_node_type_narration,
            "caption": "Репортаж среди помех",
            "pos": (0, 21),
        },
        "scene10": {
            "type": story_node_type_narration,
            "caption": "Вечер",
            "pos": (0, 24),
        },
        "la hall": {
            "type": story_node_type_lookaround,
            "caption": "Коридор",
            "pantry":{
                "type": story_node_type_item,
                "caption": "Кладовка",
                "pos": (75+200, 175+0),
            },
            "cross":{
                "type": story_node_type_item,
                "caption": "Крест",
                "pos": (75+200, 175+85),
            },
            "ula":{
                "type": story_node_type_item,
                "caption": "Юла",
                "pos": (75+200, 175+85*2),
            },
            "phone":{
                "type": story_node_type_item,
                "caption": "Телефон",
                "pos": (75+200, 175+85*3),
            },
        },
        "la kitchen": {
            "type": story_node_type_lookaround,
            "caption": "Кухня",
            "number":{
                "type": (story_node_type_item, story_node_type_option),
                "caption": "Номер Тихонова",
                "pos": (75+200, 175+85*0),
            },
            "calendar":{
                "type": (story_node_type_item),
                "caption": "Календарь",
                "pos": (75+200, 175+85*1),
            },
            "radio":{
                "type": (story_node_type_item),
                "caption": "Радио",
                "pos": (75+200+440, 175+85*0),
            },
            "crossword":{
                "type": (story_node_type_item),
                "caption": "Кроссворд",
                "pos": (75+200+440, 175+85*1),
            },
        },
        "la fridge": {
            "type": story_node_type_lookaround,
            "caption": "Холодильник",
            "freezer":{
                "type": story_node_type_item,
                "caption": "Морозилка",
                "pos": (75+200, 175+85*0),
            },
        },
        "la anton": {
            "type": story_node_type_lookaround,
            "caption": "Комната Антона",
            "toys":{
                "type": story_node_type_item,
                "caption": "Игрушки",
                "pos": (75+200, 175+85*0),
            },
            "curtains":{
                "type": story_node_type_item,
                "caption": "Занавески",
                "pos": (75+200, 175+85*1),
            },
            "pics":{
                "type": story_node_type_item,
                "caption": "Рисунки",
                "pos": (75+200+440, 175+85*0),
            },
            "book":{
                "type": story_node_type_item,
                "caption": "Книга",
                "pos": (75+200+440, 175+85*1),
            },
        },
        "la olya": {
            "type": story_node_type_lookaround,
            "caption": "Комната Оли",
            "pig":{
                "type": story_node_type_item,
                "caption": "Копилка",
                "pos": (75+200, 175+85*0),
            },
            "bear":{
                "type": story_node_type_item,
                "caption": "Мишка",
                "pos": (75+200, 175+85*1),
            },
            "curtains":{
                "type": story_node_type_item,
                "caption": "Занавески",
                "pos": (75+200, 175+85*2),
            },
        },
        "glove": {
            "type": story_node_type_choice,
            "caption": "Варежка на ветке",
            "pos": (0, 9),
            "take":{
                "type": story_node_type_option,
                "caption": "Взять",
                "pos": (320, 75),
            },
            "run":{
                "type": story_node_type_option,
                "caption": "Убежать",
                "pos": (-320, 75),
            },
        },
        "tv": {
            "type": story_node_type_choice,
            "caption": "Репортаж",
            "watch":{
                "type": story_node_type_option,
                "caption": "Смотреть",
                "pos": (250, 100),
            },
            "switch":{
                "type": story_node_type_option,
                "caption": "Переключить",
                "pos": (-250, 100),
            },
        },
    }
}

    story_so_far_dcut = {
    "day1":{
        "scene0": {
            "type": story_node_type_narration,
            "caption": _("Пролог{#flowchart_day1}"),
            "pos": (0, 0),
            },
        "scene1": {
            "type": story_node_type_narration,
            "caption": _("Завтрак{#flowchart_day1}"),
            "pos": (0, 1),
            },
        "scene2": {
            "type": story_node_type_narration,
            "caption": _("Флешбек{#flowchart_day1}"),
            "pos": (0, 2),
            },
        "scene3": {
            "type": story_node_type_narration,
            "caption": _("Милиция{#flowchart_day1}"),
            "pos": (0, 3),
            },
        "scene4": {
            "type": story_node_type_narration,
            "caption": _("Лес{#flowchart_day1}"),
            "pos": (0, 7),
            },
        "scene5": {
            "type": story_node_type_narration,
            "caption": _("Варежка{#flowchart_day1}"),
            "pos": (0, 8),
            },
        "scene6": {
            "type": story_node_type_narration,
            "caption": _("Бегство{#flowchart_day1}"),
            "pos": (0, 11),
            },
        "scene7": {
            "type": story_node_type_narration,
            "caption": _("Дома{#flowchart_day1}"),
            "pos": (1, 12),
            },
        "scene8": {
            "type": story_node_type_narration,
            "caption": _("Разговор с Олей{#flowchart_day1}"),
            "pos": (0, 16),
            },
        "scene9": {
            "type": story_node_type_narration,
            "caption": _("Репортаж среди помех{#flowchart_day1}"),
            "pos": (0, 21),
            },
        "scene10": {
            "type": story_node_type_narration,
            "caption": _("Вечер{#flowchart_day1}"),
            "pos": (0, 24),
            },
        "la hall": {
            "type": story_node_type_lookaround,
            "caption": _("Коридор{#flowchart_day1}"),
            "pantry":{
                "type": story_node_type_item,
                "caption": _("Кладовка{#flowchart_day1}"),
                "pos": (75+200, 175+0),
            },
            "cross":{
                "type": story_node_type_item,
                "caption": _("Крест{#flowchart_day1}"),
                "pos": (75+200, 175+85),
            },
            "ula":{
                "type": story_node_type_item,
                "caption": _("Юла{#flowchart_day1}"),
                "pos": (75+200, 175+85*2),
            },
            "phone":{
                "type": story_node_type_item,
                "caption": _("Телефон{#flowchart_day1}"),
                "pos": (75+200, 175+85*3),
            },
            },
        "la kitchen": {
            "type": story_node_type_lookaround,
            "caption": _("Кухня{#flowchart_day1}"),
            "number":{
                "type": (story_node_type_item, story_node_type_option),
                "caption": _("Номер Тихонова{#flowchart_day1}"),
                "pos": (75+200, 175+85*0),
            },
            "calendar":{
                "type": (story_node_type_item),
                "caption": _("Календарь{#flowchart_day1}"),
                "pos": (75+200, 175+85*1),
            },
            "radio":{
                "type": (story_node_type_item),
                "caption": _("Радио{#flowchart_day1}"),
                "pos": (75+200+440, 175+85*0),
            },
            "crossword":{
                "type": (story_node_type_item),
                "caption": _("Кроссворд{#flowchart_day1}"),
                "pos": (75+200+440, 175+85*1),
            },
            },
        "la fridge": {
            "type": story_node_type_lookaround,
            "caption": _("Холодильник{#flowchart_day1}"),
            "freezer":{
                "type": story_node_type_item,
                "caption": _("Морозилка{#flowchart_day1}"),
                "pos": (75+200, 175+85*0),
            },
            },
        "la anton": {
            "type": story_node_type_lookaround,
            "caption": _("Комната Антона{#flowchart_day1}"),
            "toys":{
                "type": story_node_type_item,
                "caption": _("Игрушки{#flowchart_day1}"),
                "pos": (75+200, 175+85*0),
            },
            "curtains":{
                "type": story_node_type_item,
                "caption": _("Занавески{#flowchart_day1}"),
                "pos": (75+200, 175+85*1),
            },
            "pics":{
                "type": story_node_type_item,
                "caption": _("Рисунки{#flowchart_day1}"),
                "pos": (75+200+440, 175+85*0),
            },
            "book":{
                "type": story_node_type_item,
                "caption": _("Книга{#flowchart_day1}"),
                "pos": (75+200+440, 175+85*1),
            },
            },
        "la olya": {
            "type": story_node_type_lookaround,
            "caption": _("Комната Оли{#flowchart_day1}"),
            "pig":{
                "type": story_node_type_item,
                "caption": _("Копилка{#flowchart_day1}"),
                "pos": (75+200, 175+85*0),
            },
            "bear":{
                "type": story_node_type_item,
                "caption": _("Мишка{#flowchart_day1}"),
                "pos": (75+200, 175+85*1),
            },
            "curtains":{
                "type": story_node_type_item,
                "caption": _("Занавески{#flowchart_day1}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "glove": {
            "type": story_node_type_choice,
            "caption": _("Варежка на ветке{#flowchart_day1}"),
            "pos": (0, 9),
            "take":{
                "type": story_node_type_option,
                "caption": _("Взять{#{#flowchart_day1}"),
                "pos": (320, 75),
            },
            "run":{
                "type": story_node_type_option,
                "caption": _("Убежать{#flowchart_day1}"),
                "pos": (-320, 75),
            },
            },
        "tv": {
            "type": story_node_type_choice,
            "caption": _("Телевизор{#flowchart_day1}"),
            "record":{
                "type": story_node_type_option,
                "caption": _("Настроить{#flowchart_day1}"),
                "pos": (250, 100),
            },
            "peter":{
                "type": story_node_type_option,
                "caption": _("Искать{#flowchart_day1}"),
                "pos": (-250, 100),
            },
            },
    },
    "day2":{
        "scene0": {
            "type": story_node_type_narration,
            "caption": _("Вступление{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene1": {
            "type": story_node_type_narration,
            "caption": _("Сборы в школу{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene2": {
            "type": story_node_type_narration,
            "caption": _("Встреча с Алисой{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene3": {
            "type": story_node_type_narration,
            "caption": _("Прогулка до школы{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene4": {
            "type": story_node_type_narration,
            "caption": _("Школа{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene5": {
            "type": story_node_type_narration,
            "caption": _("Класс{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene6": {
            "type": story_node_type_narration,
            "caption": _("Встреча с Полиной{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene7": {
            "type": story_node_type_narration,
            "caption": _("Прогулка с Алисой{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene8": {
            "type": story_node_type_narration,
            "caption": _("Одиночка{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene9": {
            "type": story_node_type_narration,
            "caption": _("Хулиганы{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene10": {
            "type": story_node_type_narration,
            "caption": _("Отец{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene11": {
            "type": story_node_type_narration,
            "caption": _("Дома{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene12a": {
            "type": story_node_type_narration,
            "caption": _("Вечер(вер.А){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene12b": {
            "type": story_node_type_narration,
            "caption": _("Вечер(вер.Б){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene13": {
            "type": story_node_type_narration,
            "caption": _("Кошмар с Катей{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene14": {
            "type": story_node_type_narration,
            "caption": _("Сова{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "scene15": {
            "type": story_node_type_narration,
            "caption": _("Финал{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_fox0": {
            "type": story_node_type_narration,
            "caption": _("Драка (Алиса){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_fox1": {
            "type": story_node_type_narration,
            "caption": _("Страшный лес{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_fox2": {
            "type": story_node_type_narration,
            "caption": _("В машине (Алиса){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_polina0": {
            "type": story_node_type_narration,
            "caption": _("Драка (Полина){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_polina1": {
            "type": story_node_type_narration,
            "caption": _("Счастливая семья{#flowchart_day2}"),
            "pos": (0, 0),
            },
        "s_polina2": {
            "type": story_node_type_narration,
            "caption": _("В машине (Полина){#flowchart_day2}"),
            "pos": (0, 0),
            },
        "la school": {
            "type": story_node_type_narration,
            "caption": _("Двор школы{#flowchart_day2}"),
            "boys":{
                "type": story_node_type_item,
                "caption": _("Парни{#flowchart_day2}"),
                "pos": (75+200, 175+85*0),
            },
            "car":{
                "type": story_node_type_item,
                "caption": _("Машина{#flowchart_day2}"),
                "pos": (75+200, 175+85*1),
            },
            "witness":{
                "type": story_node_type_item,
                "caption": _("Мужик{#flowchart_day2}"),
                "pos": (75+200, 175+85*2),
            },
            "nest":{
                "type": story_node_type_item,
                "caption": _("Гнездо{#flowchart_day2}"),
                "pos": (75+200, 175+85*3),
            },
            },
        "la waifu": {
            "type": story_node_type_narration,
            "caption": _("После уроков{#flowchart_day2}"),
            "bucket":{
                "type": story_node_type_item,
                "caption": _("Ведро{#flowchart_day2}"),
                "pos": (75+200, 175+0),
            },
            "airplane":{
                "type": story_node_type_item,
                "caption": _("Самолётик{#flowchart_day2}"),
                "pos": (75+200, 175+85*1),
            },
            "shoes":{
                "type": story_node_type_item,
                "caption": _("Обувь{#flowchart_day2}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "la corner": {
            "type": story_node_type_narration,
            "caption": _("Двор школы{#flowchart_day2}"),
            "witness":{
                "type": story_node_type_item,
                "caption": _("Мужик{#flowchart_day2}"),
                "pos": (75+200, 175+0),
            },
            "hangman":{
                "type": story_node_type_item,
                "caption": _("Висельник{#flowchart_day2}"),
                "pos": (75+200, 175+0),
            },
            "niddle":{
                "type": story_node_type_item,
                "caption": _("Шприцы{#flowchart_day2}"),
                "pos": (75+200, 175+85*1),
            },
            "squirrel":{
                "type": story_node_type_item,
                "caption": _("Белка{#flowchart_day2}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "candy": {
            "type": story_node_type_choice,
            "caption": _("Угощение{#flowchart_day2}"),
            "take":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day2}"),
                "pos": (250, 100),
            },
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Отказаться{#flowchart_day2}"),
                "pos": (-250, 100),
            },
            },
        "semen": {
            "type": story_node_type_choice,
            "caption": _("Семён{#flowchart_day2}"),
            "fight":{
                "type": story_node_type_option,
                "caption": _("Дать отпор{#flowchart_day2}"),
                "pos": (250, 100),
            },
            "submit":{
                "type": story_node_type_option,
                "caption": _("Стерпеть{#flowchart_day2}"),
                "pos": (-250, 100),
            },
            },
        "waifu": {
            "type": story_node_type_choice,
            "caption": _("С кем идти домой{#flowchart_day2}"),
            "fox":{
                "type": story_node_type_option,
                "caption": _("Алиса{#flowchart_day2}"),
                "pos": (0, 0),
            },
            "polina":{
                "type": story_node_type_option,
                "caption": _("Полина{#flowchart_day2}"),
                "pos": (0, 0),
            },
            },
        "mask": {
            "type": story_node_type_choice,
            "caption": _("Маска{#flowchart_day2}"),
            "take":{
                "type": story_node_type_option,
                "caption": _("Надеть{#flowchart_day2}"),
                "pos": (-350, 100),
            },
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Послать{#flowchart_day2}"),
                "pos": (350, 100),
            },
            },
        "man_polina": {
            "type": story_node_type_choice,
            "caption": "",
            "witness":{
                "type": story_node_type_option,
                "caption": _("Мужик в лесу{#flowchart_day2}"),
                "pos": (0, 0),
            },
            },
        "man_fox": {
            "type": story_node_type_choice,
            "caption": "",
            "witness":{
                "type": story_node_type_option,
                "caption": _("Мужик в лесу{#flowchart_day2}"),
                "pos": (0, 0),
            },
            }
    },
    "day3":{
        "scene1": {
            "type": story_node_type_narration,
            "caption": _("Начало{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene2": {
            "type": story_node_type_narration,
            "caption": _("Класс{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene3": {
            "type": story_node_type_narration,
            "caption": _("Тихонов{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene4": {
            "type": story_node_type_narration,
            "caption": _("Незнакомцы в деревне{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene5a": {
            "type": story_node_type_narration,
            "caption": _("Коридор(травля){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene5b": {
            "type": story_node_type_narration,
            "caption": _("Коридор(друзья){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene6": {
            "type": story_node_type_narration,
            "caption": _("Фотоаппарат{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene7": {
            "type": story_node_type_narration,
            "caption": _("Неделю спустя{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene8": {
            "type": story_node_type_narration,
            "caption": _("Извинения Полины{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene9": {
            "type": story_node_type_narration,
            "caption": _("Разговор с Полиной{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene10": {
            "type": story_node_type_narration,
            "caption": _("Флирт{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene11": {
            "type": story_node_type_narration,
            "caption": _("Анкета{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene12": {
            "type": story_node_type_narration,
            "caption": _("За школой(друзья){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene13a": { 
            "type": story_node_type_narration,
            "caption": _("За школой(травля){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene13b": { 
            "type": story_node_type_narration,
            "caption": _("За школой(буйный){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene13c": { 
            "type": story_node_type_narration,
            "caption": _("За школой(оберег){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene14": {
            "type": story_node_type_narration,
            "caption": _("Дома{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene15": {
            "type": story_node_type_narration,
            "caption": _("Рассказ Оли{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene16a": { 
            "type": story_node_type_narration,
            "caption": _("Перед игрой(девушка){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene16b": { 
            "type": story_node_type_narration,
            "caption": _("Перед игрой(друзья){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene16c": { 
            "type": story_node_type_narration,
            "caption": _("Перед игрой(психоз){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene17": {
            "type": story_node_type_narration,
            "caption": _("Звонок Полины{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene18a": {
            "type": story_node_type_narration,
            "caption": _("Подружки{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene18b": {
            "type": story_node_type_narration,
            "caption": _("Разговор по душам{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene19": {
            "type": story_node_type_narration,
            "caption": _("Время репетиции{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene20": {
            "type": story_node_type_narration,
            "caption": _("Время сказки на ночь{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene21": {
            "type": story_node_type_narration,
            "caption": _("Бегство{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene22": {
            "type": story_node_type_narration,
            "caption": _("Прогулка со зверьми{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene23": {
            "type": story_node_type_narration,
            "caption": _("Прыжки под луной{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene24a": {
            "type": story_node_type_narration,
            "caption": _("Реальность(Рома){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene24b": {
            "type": story_node_type_narration,
            "caption": _("Реальность(Полина){#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene_wrong": {
            "type": story_node_type_narration,
            "caption": _("Нет фоторобота{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "scene_witness": {
            "type": story_node_type_narration,
            "caption": _("Впечатленный Тихонов{#flowchart_day3}"),
            "pos": (0, 0),
            },
        "la classroom": {
            "type": story_node_type_narration,
            "caption": _("Класс{#flowchart_day3}"),
            "projector":{
                "type": story_node_type_item,
                "caption": _("Проектор{#flowchart_day3}"),
                "pos": (75+200, 175+85*0),
            },
            "esenin":{
                "type": story_node_type_item,
                "caption": _("Портреты{#flowchart_day3}"),
                "pos": (75+200, 175+85*1),
            },
            "box":{
                "type": story_node_type_item,
                "caption": _("Коробка{#flowchart_day3}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "game case": {
            "type": story_node_type_choice,
            "caption": _("Досье{#flowchart_day3}"),
            "hit0":{
                "type": story_node_type_option,
                "caption": _("Ни открыл ни разу{#flowchart_day3}"),
                "pos": (75+200, 175+85*0),
            },
            "hit1":{
                "type": story_node_type_option,
                "caption": _("Открыл 1й раз{#flowchart_day3}"),
                "pos": (75+200, 175+85*1),
            },
            "hit2":{
                "type": story_node_type_option,
                "caption": _("Открыл 2й раза{#flowchart_day3}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "photorobot": {
            "type": story_node_type_choice,
            "caption": _("Кое-кто подозрительный{#flowchart_day3}"),
            "silent":{
                "type": story_node_type_option,
                "caption": _("Промолчать{#flowchart_day3}"),
                "pos": (-250, 0),
            },
            "tell":{
                "type": story_node_type_option,
                "caption": _("Рассказать{#flowchart_day3}"),
                "pos": (250, 0),
            },
            },
        "game photorobot": {
            "type": story_node_type_choice,
            "caption": _("Фоторобот{#flowchart_day3}"),
            "fox":{
                "type": story_node_type_option,
                "caption": _("Алиса{#flowchart_day3}"),
                "pos": (75+200, 175+85*0),
            },
            "witness":{
                "type": story_node_type_option,
                "caption": _("Заячья губа{#flowchart_day3}"),
                "pos": (75+200, 175+85*1),
            },
            "trudovic":{
                "type": story_node_type_option,
                "caption": _("Трудовик{#flowchart_day3}"),
                "pos": (75+200, 175+85*2),
            },
            "letov":{
                "type": story_node_type_option,
                "caption": _("Летов{#flowchart_day3}"),
                "pos": (75+200, 175+85*3),
            },
            "tsoi":{
                "type": story_node_type_option,
                "caption": _("Цой{#flowchart_day3}"),
                "pos": (75+200, 175+85*4),
            },
            "bodrov":{
                "type": story_node_type_option,
                "caption": _("Бодров{#flowchart_day3}"),
                "pos": (75+200, 175+85*5),
            },
            },
        "game suefa": {
            "type": story_node_type_choice,
            "caption": _("Суефа{#flowchart_day3}"),
            "lose":{
                "type": story_node_type_option,
                "caption": _("Проиграл{#flowchart_day3}"),
                "pos": (75+200, 175+85*0),
            },
            "win":{
                "type": story_node_type_option,
                "caption": _("Выиграл{#flowchart_day3}"),
                "pos": (75+200, 175+85*1),
            },
            },
        "game goosehunt": {
            "type": story_node_type_choice,
            "caption": _("Утки{#flowchart_day3}"),
            "dominate":{
                "type": story_node_type_option,
                "caption": _("Выграл{#flowchart_day3}"),
                "pos": (75+200, 175+85*0),
            },
            "comfort":{
                "type": story_node_type_option,
                "caption": _("Утешил{#flowchart_day3}"),
                "pos": (75+200, 175+85*1),
            },
            },
        "phonecall": {
            "type": story_node_type_choice,
            "caption": _("Замысел Ромы{#flowchart_day3}"),
            "betray":{
                "type": story_node_type_option,
                "caption": _("Предать{#flowchart_day3}"),
                "pos": (0, 0),
            },
            "voltron":{
                "type": story_node_type_option,
                "caption": _("Хранить секрет{#flowchart_day3}"),
                "pos": (0, 0),
            },
            },
        "amulet": {
            "type": story_node_type_choice,
            "caption": _("Амулет{#flowchart_day3}"),
            "yes":{
                "type": story_node_type_option,
                "caption": _("Взять{#flowchart_day3}"),
                "pos": (0, 0),
            },
            "no":{
                "type": story_node_type_option,
                "caption": _("Оставить Полине{#flowchart_day3}"),
                "pos": (0, 0),
            },
            },
    },
    "day4":{
        "scene1a": {
            "type": story_node_type_narration,
            "caption": _("Начало(Рома){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene1b": {
            "type": story_node_type_narration,
            "caption": _("Начало(Полина){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene2": {
            "type": story_node_type_narration,
            "caption": _("Разговор с Полиной{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_s": {
            "type": story_node_type_narration,
            "caption": _("Школа(Один){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v": {
            "type": story_node_type_narration,
            "caption": _("Школа(Вольтрон){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v2": {
            "type": story_node_type_narration,
            "caption": _("Постановка{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v3": {
            "type": story_node_type_narration,
            "caption": _("Сватовство{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v4": {
            "type": story_node_type_narration,
            "caption": _("Бяша{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v5": {
            "type": story_node_type_narration,
            "caption": _("Бурелом(без Б){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v6": {
            "type": story_node_type_narration,
            "caption": _("Бурелом(с Б){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v7": {
            "type": story_node_type_narration,
            "caption": _("Гараж{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_t": {
            "type": story_node_type_narration,
            "caption": _("Школа(Предатель){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_t2": {
            "type": story_node_type_narration,
            "caption": _("Дорога(вер.Б){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_p": {
            "type": story_node_type_narration,
            "caption": _("Школа(Полина){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_p2": {
            "type": story_node_type_narration,
            "caption": _("Конфронтация{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_p3": {
            "type": story_node_type_narration,
            "caption": _("Дорога(вер.А){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_garage": {
            "type": story_node_type_narration,
            "caption": _("Катя{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_garage2": {
            "type": story_node_type_narration,
            "caption": _("Исход{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_v8": {
            "type": story_node_type_narration,
            "caption": _("Последствия{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_police_a": {
            "type": story_node_type_narration,
            "caption": _("Милиция(добровольно){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_police_b": {
            "type": story_node_type_narration,
            "caption": _("Милиция(принудительно){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_police_2": {
            "type": story_node_type_narration,
            "caption": _("Разговор с Тихоновым{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph1": {
            "type": story_node_type_narration,
            "caption": _("Дом Полины{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph2": {
            "type": story_node_type_narration,
            "caption": _("Знакомство с Харитоном{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph3": {
            "type": story_node_type_narration,
            "caption": _("Сила тайги{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph4": {
            "type": story_node_type_narration,
            "caption": _("Болтовня с Полиной{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph5": {
            "type": story_node_type_narration,
            "caption": _("Смерть плаката{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph6": {
            "type": story_node_type_narration,
            "caption": _("Игра на скрипке{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph7": {
            "type": story_node_type_narration,
            "caption": _("Йод c поцелуем{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph8": {
            "type": story_node_type_narration,
            "caption": _("Поцелуй{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ph9": {
            "type": story_node_type_narration,
            "caption": _("Уход{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_ra": {
            "type": story_node_type_narration,
            "caption": _("Злой Рома(предатель){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_rb": {
            "type": story_node_type_narration,
            "caption": _("Злой Рома(соперник){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_r2": {
            "type": story_node_type_narration,
            "caption": _("Нож{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_r3": {
            "type": story_node_type_narration,
            "caption": _("Месть{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_r4": {
            "type": story_node_type_narration,
            "caption": _("Бегство{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene_r5": {
            "type": story_node_type_narration,
            "caption": _("Спасение{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene3": {
            "type": story_node_type_narration,
            "caption": _("Вечер Дома{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene4": {
            "type": story_node_type_narration,
            "caption": _("Скандал родителей{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene5": {
            "type": story_node_type_narration,
            "caption": _("Встреча со зверьми{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene6": {
            "type": story_node_type_narration,
            "caption": _("Процессия{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene7": {
            "type": story_node_type_narration,
            "caption": _("Снежный дворец{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene8": {
            "type": story_node_type_narration,
            "caption": _("Кошмар наяву{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene9": {
            "type": story_node_type_narration,
            "caption": _("\"Я - человек!\"{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene10": {
            "type": story_node_type_narration,
            "caption": _("Ультиматум(вер.А){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene11": {
            "type": story_node_type_narration,
            "caption": _("Цветные сны{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene12": {
            "type": story_node_type_narration,
            "caption": _("Полина{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene13": {
            "type": story_node_type_narration,
            "caption": _("Портрет{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene14": {
            "type": story_node_type_narration,
            "caption": _("Пробуждение{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene15": {
            "type": story_node_type_narration,
            "caption": _("Пустой посёлок{#flowchart_day4}"),
            "pos": (0, 0),
            },
        "scene16": {
            "type": story_node_type_narration,
            "caption": _("Ультиматум(вер.Б){#flowchart_day4}"),
            "pos": (0, 0),
            },
        "la polhouse1": {
            "type": story_node_type_lookaround,
            "caption": _("Прихожая{#flowchart_day4}"),
            "ski":{
                "type": story_node_type_item,
                "caption": _("Лыжи{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            "telephone":{
                "type": story_node_type_item,
                "caption": _("Телефон{#flowchart_day4}"),
                "pos": (75+200, 175+85*1),
            },
            "horns":{
                "type": story_node_type_item,
                "caption": _("Рога{#flowchart_day4}"),
                "pos": (75+200, 175+85*2),
            },
            "portrait":{
                "type": story_node_type_item,
                "caption": _("Портрет{#flowchart_day4}"),
                "pos": (75+200+440, 175+85*0),
            },
            "mirror":{
                "type": story_node_type_item,
                "caption": _("Зеркало{#flowchart_day4}"),
                "pos": (75+200+440, 175+85*1),
            },
            "grandfather":{
                "type": story_node_type_item,
                "caption": _("Комната дедушки{#flowchart_day4}"),
                "pos": (75+200+440, 175+85*2),
            },
            },
        "la polhouse2": {
            "type": story_node_type_lookaround,
            "caption": _("Комната Полины{#flowchart_day4}"),
            "player":{
                "type": story_node_type_item,
                "caption": _("Проигрыватель{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            "piano":{
                "type": story_node_type_item,
                "caption": _("Пианино{#flowchart_day4}"),
                "pos": (75+200, 175+85*1),
            },
            "poster":{
                "type": story_node_type_item,
                "caption": _("Плакат{#flowchart_day4}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "la garage": {
            "type": story_node_type_lookaround,
            "caption": _("Гараж{#flowchart_day4}"),
            "tools":{
                "type": story_node_type_item,
                "caption": _("Инструменты{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            "junk":{
                "type": story_node_type_item,
                "caption": _("Хлам{#flowchart_day4}"),
                "pos": (75+200, 175+85*1),
            },
            "boxes":{
                "type": story_node_type_item,
                "caption": _("Ящики{#flowchart_day4}"),
                "pos": (75+200, 175+85*2),
            },
            "car":{
                "type": story_node_type_item,
                "caption": _("Автомобиль{#flowchart_day4}"),
                "pos": (75+200, 175+85*3),
            },
            "tiski":{
                "type": story_node_type_item,
                "caption": _("Тиски{#flowchart_day4}"),
                "pos": (75+200, 175+85*4),
            },
            "shelf":{
                "type": story_node_type_item,
                "caption": _("Верхняя полка{#flowchart_day4}"),
                "pos": (75+200, 175+85*5),
            },
            },
        "la police": {
            "type": story_node_type_lookaround,
            "caption": _("Участок{#flowchart_day4}"),
            "cage":{
                "type": story_node_type_item,
                "caption": _("«Обезьянник»{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            "mask":{
                "type": story_node_type_item,
                "caption": _("Противогаз{#flowchart_day4}"),
                "pos": (75+200, 175+85*1),
            },
            },
        "byasha": {
            "type": story_node_type_choice,
            "caption": _("Бяша{#flowchart_day4}"),
            "call":{
                "type": story_node_type_option,
                "caption": _("Звать{#flowchart_day4}"),
                "pos": (350, 0),
            },
            "dismiss":{
                "type": story_node_type_option,
                "caption": _("Не звать{#flowchart_day4}"),
                "pos": (-350, 0),
            },
            },
        "garage": {
            "type": story_node_type_choice,
            "caption": _("Гараж{#flowchart_day4}"),
            "police":{
                "type": story_node_type_option,
                "caption": _("В милицию{#flowchart_day4}"),
                "pos": (-250, 0),
            },
            "enter":{
                "type": story_node_type_option,
                "caption": _("Войти{#flowchart_day4}"),
                "pos": (250, 0),
            },
            },
        "treat1": {
            "type": story_node_type_choice,
            "caption": _("Угощение{#flowchart_day4}"),
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Отказаться{#flowchart_day4}"),
                "pos": (-350, 0),
            },
            "accept":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day4}"),
                "pos": (350, 0),
            },
            },
        "treat2": {
            "type": story_node_type_choice,
            "caption": _("Угощение(2){#flowchart_day4}"),
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Отказаться{#flowchart_day4}"),
                "pos": (-350, 0),
            },
            "accept":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day4}"),
                "pos": (350, 0),
            },
            },
        "treat": {
            "type": story_node_type_choice,
            "caption": "",
            "accept":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day4}"),
                "pos": (0, 0),
            },
            },
        "game katya": {
            "type": story_node_type_choice,
            "caption": _("Катя в мясорубке{#flowchart_day4}"),
            "fail":{
                "type": story_node_type_option,
                "caption": _("Не пытался{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            "save":{
                "type": story_node_type_option,
                "caption": _("Пытался{#flowchart_day4}"),
                "pos": (75+200, 175+85*1),
            },
            "photo":{
                "type": story_node_type_option,
                "caption": _("Фото{#flowchart_day4}"),
                "pos": (75+200, 175+85*2),
            },
            },
        "game poster": {
            "type": story_node_type_choice,
            "caption": _("Плакат{#flowchart_day4}"),
            "solve":{
                "type": story_node_type_option,
                "caption": _("Собрать{#flowchart_day4}"),
                "pos": (75+200, 175+85*0),
            },
            },
        "ending": {
            "type": story_node_type_narration,
            "caption": "",
            "pos": (0, 0),
            "needle":{
                "type": story_node_type_option,
                "caption": _("Школяр-убийца{#flowchart_day4}"),
                "pos": (0, 0),
            },
            },
    },
    "day5":{
        "scene1a": {
            "type": story_node_type_narration,
            "caption": _("Начало(угощение){#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene1b": {
            "type": story_node_type_narration,
            "caption": _("Начало(без угощения){#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene2": {
            "type": story_node_type_narration,
            "caption": _("Жулька{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene3": {
            "type": story_node_type_narration,
            "caption": _("Психоз{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene4": {
            "type": story_node_type_narration,
            "caption": _("Лекарство{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene5a": {
            "type": story_node_type_narration,
            "caption": _("Собака в морозилке{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene5b": {
            "type": story_node_type_narration,
            "caption": _("Собака под столом{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene6": {
            "type": story_node_type_narration,
            "caption": _("Лес{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene7": {
            "type": story_node_type_narration,
            "caption": _("Гараж{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene8": {
            "type": story_node_type_narration,
            "caption": _("Школа{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene9": {
            "type": story_node_type_narration,
            "caption": _("Пробуждение{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene10": {
            "type": story_node_type_narration,
            "caption": _("Зов помощи{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene11a": {
            "type": story_node_type_narration,
            "caption": _("Позвонить в участок{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene11b": {
            "type": story_node_type_narration,
            "caption": _("Позвонить Тихонову{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene12a": {
            "type": story_node_type_narration,
            "caption": _("Заячья Губа взят{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene12b": {
            "type": story_node_type_narration,
            "caption": _("Маньяк на свободе{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene13a": {
            "type": story_node_type_narration,
            "caption": _("Нет улик{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene13b": {
            "type": story_node_type_narration,
            "caption": _("Улики собраны{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene14": {
            "type": story_node_type_narration,
            "caption": _("Гости{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene15a": {
            "type": story_node_type_narration,
            "caption": _("Рома с Полиной{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene15b": {
            "type": story_node_type_narration,
            "caption": _("Полина{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene16": {
            "type": story_node_type_narration,
            "caption": _("Барикады{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene17": {
            "type": story_node_type_narration,
            "caption": _("Монстры пришли{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene18": {
            "type": story_node_type_narration,
            "caption": _("Вера{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene19": {
            "type": story_node_type_narration,
            "caption": _("Время решать{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene20": {
            "type": story_node_type_narration,
            "caption": _("Догнали{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene21": {
            "type": story_node_type_narration,
            "caption": _("Тихонов{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene22": {
            "type": story_node_type_narration,
            "caption": _("Чаепитие{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene23a": {
            "type": story_node_type_narration,
            "caption": _("В машине(Антон и Оля){#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene23b": {
            "type": story_node_type_narration,
            "caption": _("В машине(один Антон){#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene24": {
            "type": story_node_type_narration,
            "caption": _("Зайчиха{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene25a": {
            "type": story_node_type_narration,
            "caption": _("Зайчиха убежала{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene25b": {
            "type": story_node_type_narration,
            "caption": _("Зайчиха бросилась в бой{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene26": {
            "type": story_node_type_narration,
            "caption": _("Выход из машины{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene27": {
            "type": story_node_type_narration,
            "caption": _("Бойня{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene28": {
            "type": story_node_type_narration,
            "caption": _("Конец{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_21": {
            "type": story_node_type_narration,
            "caption": _("Бегство{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_22a": {
            "type": story_node_type_narration,
            "caption": _("Амулет{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_22b": {
            "type": story_node_type_narration,
            "caption": _("Крест{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_p1": {
            "type": story_node_type_narration,
            "caption": _("Пробки выбило{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_p2": {
            "type": story_node_type_narration,
            "caption": _("Мираж{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_k1": {
            "type": story_node_type_narration,
            "caption": _("В гостях у Кати{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "scene_k2": {
            "type": story_node_type_narration,
            "caption": _("Мираж{#flowchart_day5}"),
            "pos": (0, 0),
            },
        "la katya": {
            "type": story_node_type_lookaround,
            "caption": _("Комната Кати{#flowchart_day5}"),
            "aqua":{
                "type": (story_node_type_item, story_node_type_option),
                "caption": _("Аквариум{#flowchart_day5}"),
                "pos": (75+200, 175+85*0),
            },
            "certif":{
                "type": (story_node_type_item),
                "caption": _("Награды{#flowchart_day5}"),
                "pos": (75+200+440, 175+85*0),
            },
            "dollh":{
                "type": (story_node_type_item),
                "caption": _("Домик Барби{#flowchart_day5}"),
                "pos": (75+200+220, 175+85*1),
            },
            "mirror":{
                "type": (story_node_type_item),
                "caption": _("Трельяж{#flowchart_day5}"),
                "pos": (75+200, 175+85*2),
            },
            "musicb":{
                "type": (story_node_type_item),
                "caption": _("Магнитофон{#flowchart_day5}"),
                "pos": (75+200+440, 175+85*2),
            },
            },
        "zhulka": {
            "type": story_node_type_narration,
            "caption": _("Судьба Жульки{#flowchart_day5}"),
            "pos": (0, 0),
            "spare":{
                "type": story_node_type_option,
                "caption": _("Пощадить{#flowchart_day5}"),
                "pos": (-350, 0),
            },
            "kill":{
                "type": story_node_type_option,
                "caption": _("Убить{#flowchart_day5}"),
                "pos": (350, 0),
            },
            },
        "waifu": {
            "type": story_node_type_narration,
            "caption": _("Кого провожать?{#flowchart_day5}"),
            "pos": (0, 0),
            "polina":{
                "type": story_node_type_option,
                "caption": _("Полина{#flowchart_day5}"),
                "pos": (-550, 0),
            },
            "katya":{
                "type": story_node_type_option,
                "caption": _("Катя{#flowchart_day5}"),
                "pos": (550, 0),
            },
            },
        "guests": {
            "type": story_node_type_narration,
            "caption": _("Гости{#flowchart_day5}"),
            "pos": (0, 0),
            "invite":{
                "type": story_node_type_option,
                "caption": _("Впустить{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "hodor":{
                "type": story_node_type_option,
                "caption": _("Не впускать{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "faith": {
            "type": story_node_type_narration,
            "caption": _("Вера{#flowchart_day5}"),
            "pos": (0, 0),
            "amulet":{
                "type": story_node_type_option,
                "caption": _("Амулет{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "cross":{
                "type": story_node_type_option,
                "caption": _("Крест{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "amulet": {
            "type": story_node_type_narration,
            "caption": _("Амулет{#flowchart_day5}"),
            "pos": (0, 0),
            "run":{
                "type": story_node_type_option,
                "caption": _("Убежать{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "self":{
                "type": story_node_type_option,
                "caption": _("Оставить себе{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "olya":{
                "type": story_node_type_option,
                "caption": _("Отдать Оле{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "sacrifice": {
            "type": story_node_type_narration,
            "caption": _("Жертва{#flowchart_day5}"),
            "pos": (0, 0),
            "olya":{
                "type": story_node_type_option,
                "caption": _("Оля{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "polina":{
                "type": story_node_type_option,
                "caption": _("Полина{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "roma":{
                "type": story_node_type_option,
                "caption": _("Рома{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "anton":{
                "type": story_node_type_option,
                "caption": _("Антон{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "dogmeat":{
                "type": story_node_type_option,
                "caption": _("Собачатина{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "cross1": {
            "type": story_node_type_narration,
            "caption": _("Крест 1{#flowchart_day5}"),
            "pos": (0, 0),
            "pray":{
                "type": story_node_type_option,
                "caption": _("Молиться{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "run":{
                "type": story_node_type_option,
                "caption": _("Убежать{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "cross2": {
            "type": story_node_type_narration,
            "caption": _("Крест 2{#flowchart_day5}"),
            "pos": (0, 0),
            "pray":{
                "type": story_node_type_option,
                "caption": _("Молиться{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "run":{
                "type": story_node_type_option,
                "caption": _("Убежать{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "cross3": {
            "type": story_node_type_narration,
            "caption": _("Крест 3{#flowchart_day5}"),
            "pos": (0, 0),
            "pray":{
                "type": story_node_type_option,
                "caption": _("Молиться{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "run":{
                "type": story_node_type_option,
                "caption": _("Убежать{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "snowtrap": {
            "type": story_node_type_narration,
            "caption": _("Сугроб-ловушка{#flowchart_day5}"),
            "pos": (0, 0),
            "olya":{
                "type": story_node_type_option,
                "caption": _("Спасти Олю{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "polina":{
                "type": story_node_type_option,
                "caption": _("Спасти Полину{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "carmask": {
            "type": story_node_type_narration,
            "caption": _("Маска в машине{#flowchart_day5}"),
            "pos": (0, 0),
            "mask":{
                "type": story_node_type_option,
                "caption": _("Надеть маску{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "face":{
                "type": story_node_type_option,
                "caption": _("Не надевать маску{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "final": {
            "type": story_node_type_narration,
            "caption": _("Маска от козла{#flowchart_day5}"),
            "pos": (0, 0),
            "break":{
                "type": story_node_type_option,
                "caption": _("Сломать маску{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "wear":{
                "type": story_node_type_option,
                "caption": _("Надевать маску{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "polina": {
            "type": story_node_type_narration,
            "caption": _("Полина в машине{#flowchart_day5}"),
            "pos": (0, 0),
            "hug":{
                "type": story_node_type_option,
                "caption": _("Обнять{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "solo":{
                "type": story_node_type_option,
                "caption": _("Оставить{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "drug polina": {
            "type": story_node_type_narration,
            "caption": _("Лекарства(у Полины){#flowchart_day5}"),
            "pos": (0, 0),
            "take":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Отказаться{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "drug katya": {
            "type": story_node_type_narration,
            "caption": _("Лекарства(у Кати){#flowchart_day5}"),
            "pos": (0, 0),
            "take":{
                "type": story_node_type_option,
                "caption": _("Принять{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "refuse":{
                "type": story_node_type_option,
                "caption": _("Отказаться{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
        "game phone": {
            "type": story_node_type_narration,
            "caption": _("Телефон Полины{#flowchart_day5}"),
            "pos": (0, 0),
            "call":{
                "type": story_node_type_option,
                "caption": _("Позвонить домой{#flowchart_day5}"),
                "pos": (75+200, 175+85*0),
            },
            },
        "game guitar": {
            "type": story_node_type_narration,
            "caption": _("Игра на гитаре{#flowchart_day5}"),
            "pos": (0, 0),
            "mistake":{
                "type": story_node_type_option,
                "caption": _("Ошибся{#flowchart_day5}"),
                "pos": (75+200, 175+85*0),
            },
            "round1":{
                "type": story_node_type_option,
                "caption": _("1й раунд{#flowchart_day5}"),
                "pos": (75+200, 175+85*1),
            },
            "round2":{
                "type": story_node_type_option,
                "caption": _("2й раунд{#flowchart_day5}"),
                "pos": (75+200, 175+85*2),
            },
            "round3":{
                "type": story_node_type_option,
                "caption": _("3й раунд{#flowchart_day5}"),
                "pos": (75+200, 175+85*3),
            },
            },
        "game stove": {
            "type": story_node_type_narration,
            "caption": _("Ужин{#flowchart_day5}"),
            "pos": (0, 0),
            "bad":{
                "type": story_node_type_option,
                "caption": _("Не вышло{#flowchart_day5}"),
                "pos": (75+200, 175+85*0),
            },
            "good":{
                "type": story_node_type_option,
                "caption": _("Получилось{#flowchart_day5}"),
                "pos": (75+200, 175+85*1),
            },
            },
        "ending": {
            "type": story_node_type_narration,
            "caption": "",
            "pos": (0, 0),
            "was_there":{
                "type": story_node_type_option,
                "caption": _("А был ли мальчик{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "home_violence":{
                "type": story_node_type_option,
                "caption": _("Домашнее насилие{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "mad_world":{
                "type": story_node_type_option,
                "caption": _("Безумный Мир{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "apocalypse":{
                "type": story_node_type_option,
                "caption": _("Апокалипсис сегодня{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "genius":{
                "type": story_node_type_option,
                "caption": _("Гений и мрак{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "recipe":{
                "type": story_node_type_option,
                "caption": _("Рецепт любви{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "still_water":{
                "type": story_node_type_option,
                "caption": _("В тихом омуте{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "bloody_claw":{
                "type": story_node_type_option,
                "caption": _("Кровавый коготь{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "among_us":{
                "type": story_node_type_option,
                "caption": _("Звери среди нас{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "pack_of":{
                "type": story_node_type_option,
                "caption": _("Стая убийц{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "rage":{
                "type": story_node_type_option,
                "caption": _("Животная ярость{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "nightmare":{
                "type": story_node_type_option,
                "caption": _("Таёжный кошмар{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "past":{
                "type": story_node_type_option,
                "caption": _("Тени прошлого{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "hunt":{
                "type": story_node_type_option,
                "caption": _("Сезон охоты{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "call":{
                "type": story_node_type_option,
                "caption": _("Зов пропавших{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "traces":{
                "type": story_node_type_option,
                "caption": _("Следы на снегу{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "in_dark":{
                "type": story_node_type_option,
                "caption": _("Исчезнувшие в ночи{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "runaway":{
                "type": story_node_type_option,
                "caption": _("Сбежавший из комы{#flowchart_day5}"),
                "pos": (0, 0),
            },
            "contract":{
                "type": story_node_type_option,
                "caption": _("Контракт с дьяволом{#flowchart_day5}"),
                "pos": (0, 0),
            },
            },
    },
}


init python:
    def ConvertStoryToFlags(story):
        events = set()
        
        for node in story:
            if node.GetSelectedOption() is not None:
                events.add( node.GetFullSelectedOption() )
        print(events)
        return ConvertEventsToFlags(events)

    def ConvertEventsToFlags(events):
        flags = FlagVault()
        
        
        if ("day1", "glove", "take") in events:
            flags.Raise("glove")
        
        if ("day1", "number", "take") in events:
            flags.Raise("number")
        
        if ("day1", "tv", "record") in events:
            flags.Raise("record")
        
        
        
        if ("day2", "candy", "take") in events:
            flags.Raise("gum")
        
        if ("day2", "semen", "fight") in events:
            flags.Raise("fight")
        
        if ("day2", "waifu", "polina") in events:
            flags.Raise("day2 polina")
        
        if ("day2", "waifu", "fox") in events:
            flags.Raise("day2 fox")
        
        if ("day2", "witness_polina", "tapped") in events:
            flags.Raise("witness tapped")
        
        if ("day2", "witness_fox", "tapped") in events:
            flags.Raise("witness tapped")
        
        if ("day2", "mask", "mask") in events:
            flags.Raise("mask")
        
        
        
        if ("day3", "minigame_case", "success1") in events:
            flags.Raise("doc")
        if ("day3", "minigame_case", "success2") in events:
            flags.Raise("doc")
            flags.Raise("finger")
        
        if ("day3", "photorobot", "silent") in events:
            flags.Raise("silent")
        
        if ("day3", "minigame_photorobot", "witness") in events:
            flags.Raise("witness")
        
        if ("day3", "minigame_suefa", "win") in events:
            flags.Raise("polaroid")
        
        if ("day3", "amulet", "yes") in events:
            flags.Raise("amulet")
        
        if ("day3", "phonecall", "betray") in events:
            flags.Raise("betray")
        
        
        
        if ("day4", "katya", "save") in events:
            if flags.Has("polaroid"):
                flags.Raise("photo")
        
        if ("day4", "treat", "accept") in events:
            flags.Raise("agree")
        
        if ("day4", "treat", "refuse1") in events:
            flags.Raise("agree")
            flags.Raise("refuse")
        
        if ("day4", "treat", "refuse2") in events:
            flags.Raise("refuse")
        
        
        if flags.Has("number") and not flags.Has("agree"):
            if flags.Has("witness"):
                flags.Raise("jailed")
            if flags.Has("glove") and flags.Has("record") and flags.Has("finger") and flags.Has("photo"):
                flags.Raise("savior")
        
        if flags.Has("agree"):
            flags.Raise("guest mom")
        
        if not flags.Has("agree"):
            if flags.Has("day2 polina"):
                flags.Raise("guest polina")
            if flags.Has("day2 fox"):
                flags.Raise("guest roma")
        
        if ("day5", "polkatya", "polina") in events:
            flags.Raise("drug polina")
        if ("day5", "polkatya", "katya") in events:
            flags.Raise("drug katya")
        
        if ("day5", "sacrifice_refuse", "olya") in events:
            flags.Raise("kill olya")
        if ("day5", "sacrifice_refuse", "roma") in events:
            flags.Raise("kill roma")
        if ("day5", "sacrifice_refuse", "polina") in events:
            flags.Raise("kill polina")
        
        if ("day5", "zhulka", "kill") in events:
            flags.Raise("meat")
        
        if ("day5", "guests", "invite") in events:
            flags.Raise("invited")
        
        if ("day5", "faith", "amulet") in events:
            flags.Raise("heresy")
        
        if ("day5", "pololya", "polina") in events:
            flags.Raise("olya died")
        
        if ("day5", "carmask_olya", "mask") in events:
            flags.Raise("day5 mask")
        
        return flags

    def ConvertFlagsToEvents(flags, days):
        story = StoryManager()
        
        
        if "day1" in days:
            story.MarkEvent(("day1", "scene0"))
            story.MarkEvent(("day1", "scene1"))
            story.MarkEvent(("day1", "scene2"))
            story.MarkEvent(("day1", "scene3"))
            story.MarkEvent(("day1", "la hall"))
            story.MarkEvent(("day1", "la hall", "door"))
            story.MarkEvent(("day1", "la kitchen"))
            
            if flags.Has("number"):
                story.MarkEvent(("day1", "la kitchen", "number"))
            
            story.MarkEvent(("day1", "scene4"))
            story.MarkEvent(("day1", "scene5"))
            story.MarkEvent(("day1", "glove"))
            
            if flags.Has("glove"):
                story.MarkEvent(("day1", "glove", "take"))
            else:
                story.MarkEvent(("day1", "glove", "run"))
            
            story.MarkEvent(("day1", "scene6"))
            
            if flags.Has("number") or flags.Has("glove"):
                story.MarkEvent(("day1", "la anton"))
            
            story.MarkEvent(("day1", "scene7"))
            story.MarkEvent(("day1", "scene8"))
            
            story.MarkEvent(("day1", "la olya"))
            
            story.MarkEvent(("day1", "scene9"))
            
            story.MarkEvent(("day1", "tv"))
            
            if flags.Has("record"):
                story.MarkEvent(("day1", "tv", "record"))
            else:
                story.MarkEvent(("day1", "tv", "peter"))
            
            story.MarkEvent(("day1", "scene10"))
        
        
        if "day2" in days:
            story.MarkEvent(("day2", "scene0"))
            story.MarkEvent(("day2", "scene1"))
            story.MarkEvent(("day2", "scene2"))
            
            story.MarkEvent(("day2", "candy"))
            if flags.Has("gum"):
                story.MarkEvent(("day2", "candy", "take"))
            else:
                story.MarkEvent(("day2", "candy", "refuse"))
            
            story.MarkEvent(("day2", "scene3"))
            story.MarkEvent(("day2", "la school"))
            story.MarkEvent(("day2", "scene4"))
            story.MarkEvent(("day2", "scene5"))
            
            story.MarkEvent(("day2", "semen"))
            if flags.Has("fight"):
                story.MarkEvent(("day2", "semen", "fight"))
            else:
                story.MarkEvent(("day2", "semen", "submit"))
                story.MarkEvent(("day2", "scene8"))
            
            story.MarkEvent(("day2", "scene6"))
            
            if flags.Has("fight"):
                story.MarkEvent(("day2", "la waifu"))
                
                if flags.Has("day2 fox"):
                    story.MarkEvent(("day2", "waifu", "fox"))
                if flags.Has("day2 polina"):
                    story.MarkEvent(("day2", "waifu", "polina"))
            
            if flags.Has("day2 fox"):
                story.MarkEvent(("day2", "la corner"))
                story.MarkEvent(("day2", "la corner", "hangman"))
                
                story.MarkEvent(("day2", "scene7"))
                
                if flags.Has("witness tapped"):
                    story.MarkEvent(("day2", "man_fox", "witness"))
            
            if flags.Has("day2 polina") and flags.Has("witness tapped"):
                    story.MarkEvent(("day2", "man_polina", "witness"))
            
            story.MarkEvent(("day2", "scene9"))
            story.MarkEvent(("day2", "mask"))
            if flags.Has("mask"):
                story.MarkEvent(("day2", "mask", "take"))
            else:
                story.MarkEvent(("day2", "mask", "refuse"))
            
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day2", "s_fox0"))
                story.MarkEvent(("day2", "s_fox1"))
                story.MarkEvent(("day2", "s_fox2"))
            
            if flags.Has("day2 polina") and not flags.Has("mask"):
                story.MarkEvent(("day2", "s_polina0"))
                story.MarkEvent(("day2", "s_polina1"))
                story.MarkEvent(("day2", "s_polina2"))
            
            if flags.Has("fight"):
                story.MarkEvent(("day2", "scene10"))
            
            story.MarkEvent(("day2", "scene11"))
            
            if not flags.Has("mask"):
                story.MarkEvent(("day2", "scene12a"))
            else:
                story.MarkEvent(("day2", "scene12b"))
            
            story.MarkEvent(("day2", "scene13"))
            story.MarkEvent(("day2", "scene14"))
            story.MarkEvent(("day2", "scene15"))
        
        
        if "day3" in days:
            story.MarkEvent(("day3", "scene1"))
            story.MarkEvent(("day3", "la classroom"))
            story.MarkEvent(("day3", "scene2"))
            story.MarkEvent(("day3", "scene3"))
            
            if flags.Has("doc"):
                story.MarkEvent(("day3", "game hit1"))
            if flags.Has("finger"):
                story.MarkEvent(("day3", "game hit2"))
            
            story.MarkEvent(("day3", "scene4"))
            story.MarkEvent(("day3", "photorobot"))
            
            if flags.Has("silent"):
                story.MarkEvent(("day3", "photorobot", "silent"))
            else:
                story.MarkEvent(("day3", "photorobot", "tell"))
                story.MarkEvent(("day3", "game photorobot"))
                
                if flags.Has("witness"):
                    story.MarkEvent(("day3", "game photorobot", "witness"))
                
                elif flags.Has("photo letov"):
                    story.MarkEvent(("day3", "game photorobot", "letov"))
                
                elif flags.Has("photo tsoi"):
                    story.MarkEvent(("day3", "game photorobot", "tsoi"))
                
                elif flags.Has("photo bodrov"):
                    story.MarkEvent(("day3", "game photorobot", "bodrov"))
                
                else:
                    story.MarkEvent(("day3", "game photorobot", "trudovic"))
            
            if not flags.Has("witness"):
                story.MarkEvent(("day3", "scene_wrong"))
            else:
                story.MarkEvent(("day3", "scene_witness"))
            
            if not flags.Has("day2 fox") or flags.Has("mask"):
                story.MarkEvent(("day3", "scene5a"))
            
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene5b"))
                story.MarkEvent(("day3", "scene6"))
                
                if flags.Has("gum"):
                    story.MarkEvent(("day3", "game suefa"))
                    
                    if flags.Has("polaroid"):
                        story.MarkEvent(("day3", "game suefa", "win"))
                    else:
                        story.MarkEvent(("day3", "game suefa", "lose"))
            
            story.MarkEvent(("day3", "scene7"))
            
            if flags.Has("day2 polina") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene8"))
                story.MarkEvent(("day3", "amulet"))
                
                if flags.Has("amulet"):
                    story.MarkEvent(("day3", "amulet", "yes"))
                else:
                    story.MarkEvent(("day3", "amulet", "no"))
            
            story.MarkEvent(("day3", "scene9"))
            story.MarkEvent(("day3", "scene10"))
            story.MarkEvent(("day3", "scene11"))
            
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene12"))
            
            if flags.Has("mask"):
                story.MarkEvent(("day3", "scene13a"))
            
            if flags.Has("day2 polina") and not flags.Has("mask"):
                if flags.Has("amulet"):
                    story.MarkEvent(("day3", "scene13c"))
                else:
                    story.MarkEvent(("day3", "scene13b"))
            
            story.MarkEvent(("day3", "scene14"))
            story.MarkEvent(("day3", "scene15"))
            
            if flags.Has("day2 polina") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene16a"))
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene16b"))
            if flags.Has("mask"):
                story.MarkEvent(("day3", "scene16c"))
            
            story.MarkEvent(("day3", "game goosehunt"))
            
            story.MarkEvent(("day3", "scene17"))
            
            if flags.Has("mask"):
                story.MarkEvent(("day3", "scene18a"))
            else:
                story.MarkEvent(("day3", "scene18b"))
                
                if flags.Has("day2 fox"):
                    story.MarkEvent(("day3", "phonecall"))
                    
                    if flags.Has("betray"):
                        story.MarkEvent(("day3", "phonecall", "betray"))
                    else:
                        story.MarkEvent(("day3", "phonecall", "voltron"))
                    
                    story.MarkEvent(("day3", "scene19"))
            
            if flags.Has("day2 polina") or flags.Has("mask"):
                story.MarkEvent(("day3", "scene20"))
            
            story.MarkEvent(("day3", "scene21"))
            story.MarkEvent(("day3", "scene22"))
            story.MarkEvent(("day3", "scene23"))
            
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day3", "scene24a"))
            else:
                story.MarkEvent(("day3", "scene24b"))
        
        
        if "day4" in days:
            
            if flags.Has("day2 fox") and not flags.Has("mask"):
                story.MarkEvent(("day4", "scene1a"))
            else:
                story.MarkEvent(("day4", "scene1b"))
            
            story.MarkEvent(("day4", "scene2"))
            
            route = "solo"
            if flags.Has("mask"):
                story.MarkEvent(("day4", "scene_s"))
            
            elif flags.Has("day2 polina"):
                route = "polina"
                story.MarkEvent(("day4", "scene_p"))
            
            elif flags.Has("day2 fox"):
                route = "fox"
                
                if flags.Has("betray"):
                    route = "traitor"
                    story.MarkEvent(("day4", "scene_t"))
                else:
                    story.MarkEvent(("day4", "scene_v"))
            
            if route in ("polina", "traitor"):
                story.MarkEvent(("day4", "scene_ph1"))
                story.MarkEvent(("day4", "la polhouse1"))
                story.MarkEvent(("day4", "scene_ph2"))
                story.MarkEvent(("day4", "la polhouse2"))
                story.MarkEvent(("day4", "scene_ph5"))
                story.MarkEvent(("day4", "game poster"))
                story.MarkEvent(("day4", "game poster", "solve"))
                story.MarkEvent(("day4", "scene_ph6"))
                story.MarkEvent(("day4", "scene_ph7"))
                story.MarkEvent(("day4", "scene_ph9"))
                
                if route == "polina":
                    story.MarkEvent(("day4", "scene_rb"))
                if route == "traitor":
                    story.MarkEvent(("day4", "scene_ra"))
                
                story.MarkEvent(("day4", "scene_r2"))
                
                if not flags.Has("amulet"):
                    story.MarkEvent(("day4", "ending", "needle"))
                    return story.current
                
                story.MarkEvent(("day4", "scene_r4"))
                story.MarkEvent(("day4", "scene_r5"))
            
            if route in ("fox"):
                story.MarkEvent(("day4", "scene_v2"))
                story.MarkEvent(("day4", "scene_v4"))
                
                story.MarkEvent(("day4", "byasha"))
                
                if flags.Has("katya"):
                    story.MarkEvent(("day4", "byasha", "call"))
                    story.MarkEvent(("day4", "scene_v6"))
                    story.MarkEvent(("day4", "scene_v7"))
                    story.MarkEvent(("day4", "garage"))
                    story.MarkEvent(("day4", "garage", "enter"))
                    story.MarkEvent(("day4", "scene_garage"))
                    story.MarkEvent(("day4", "la garage"))
                    story.MarkEvent(("day4", "game katya"))
                    if flags.Has("help"):
                        story.MarkEvent(("day4", "game katya", "save"))
                        if flags.Has("polaroid"):
                            story.MarkEvent(("day4", "game katya", "photo"))
                    else:
                        story.MarkEvent(("day4", "game katya", "fail"))
                    
                    story.MarkEvent(("day4", "scene_garage2"))
                    story.MarkEvent(("day4", "scene_v8"))
                
                else:
                    story.MarkEvent(("day4", "byasha", "dismiss"))
                    story.MarkEvent(("day4", "scene_v5"))
                    story.MarkEvent(("day4", "la police"))
                    story.MarkEvent(("day4", "scene_police_2"))
                    story.MarkEvent(("day4", "scene_v5"))
            
            story.MarkEvent(("day4", "scene3"))
            story.MarkEvent(("day4", "scene4"))
            story.MarkEvent(("day4", "scene5"))
            story.MarkEvent(("day4", "scene7"))
            story.MarkEvent(("day4", "treat1"))
            
            if flags.Has("refuse"):
                story.MarkEvent(("day4", "treat1", "refuse"))
                story.MarkEvent(("day4", "treat2"))
                
                if flags.Has("agree"):
                    story.MarkEvent(("day4", "treat2", "accept"))
                else:
                    story.MarkEvent(("day4", "treat2", "refuse"))
            
            else:
                story.MarkEvent(("day4", "treat1", "accept"))
            
            if flags.Has("agree"):
                story.MarkEvent(("day4", "scene11"))
                story.MarkEvent(("day4", "scene16"))
            else:
                story.MarkEvent(("day4", "scene8"))
                story.MarkEvent(("day4", "scene10"))
        
        return story.current


init python:
    class EventVault:
        def __init__(self):
            self.vault = list()
            return
        
        def Add(self, day_id, choice_id, option_id):
            if self.Has(day_id, choice_id, option_id):
                return
            self.vault.append((day_id, choice_id, option_id))
            self.vault.sort()
        
        def Remove(self, day_id, choice_id, option_id):
            if not self.Has(day_id, choice_id, option_id):
                return
            self.vault.remove((day_id, choice_id, option_id))
        
        def ClearOf(self, day_id, choice_id, *option_ids):
            for option_id in option_ids:
                self.Remove(day_id, choice_id, option_id)
        
        def Has(self, day_id, choice_id, option_id):
            return (day_id, choice_id, option_id) in self.vault
        
        def ClearAll(self):
            self.vault.clear()

    class StoryManager:
        def __init__(self):
            self.current = set()
            
            if persistent.story_unlocks is None:
                persistent.story_unlocks = set()
            
            self.height = config.screen_height
            self.width = config.screen_width
            self.all_visible = False
        
        def MarkEvent(self, event):
            self.current.add(event)
            persistent.story_unlocks.add(event)
        
        def IsMarkedLocal(self, event):
            return event in self.current
        
        def IsMarkedPersist(self, event):
            if self.all_visible:
                return True
            return event in persistent.story_unlocks
        
        def IsMarkedPersistStrict(self, event):
            return event in persistent.story_unlocks
        
        def Extend(self, events):
            for e in events:
                self.MarkEvent(e)
        
        def ValidDays(self):
            result = set()
            for event in self.current:
                result.add(event[0])
            return result
        
        def IsEnding(self):
            for event in self.current:
                if event[1] == "ending":
                    return True
            return False


    class IncrementalInt:
        def __init__(self, init_val = 0):
            self.value = init_val
        
        def __call__(self, val):
            _value = self.value
            self.value += val
            return _value

screen FlagsSelector(available_days, fvault):
    default current_day = available_days[0]

    $ day_id = "day" + str(current_day)
    $ day = choices_structure[day_id]
    hbox:
        ypos 75
        yanchor .5
        xpos 960
        xanchor .5
        spacing 25

        textbutton "Эпизод 1":
            text_hover_color "#fff"
            selected current_day == 1
            sensitive 1 in available_days
            action SetScreenVariable("current_day", 1)

        textbutton "Эпизод 2":
            text_hover_color "#fff"
            selected current_day == 2
            sensitive 2 in available_days
            action SetScreenVariable("current_day", 2)

        textbutton "Эпизод 3":
            text_hover_color "#fff"
            selected current_day == 3
            sensitive 3 in available_days
            action SetScreenVariable("current_day", 3)

        textbutton "Эпизод 4":
            text_hover_color "#fff"
            selected current_day == 4
            sensitive 4 in available_days
            action SetScreenVariable("current_day", 4)

        textbutton "Эпизод 5":
            text_hover_color "#fff"
            selected current_day == 5
            sensitive 5 in available_days
            action SetScreenVariable("current_day", 5)

    hbox:
        xalign .5
        ypos 100
        yanchor 0.0

        viewport:
            xsize 400
            ysize 900
            mousewheel True
            scrollbars "vertical"

            has vbox
            xfill True

            for choice_id in day["choices"]:
                $ choice = day[choice_id]

                text choice["caption"]:
                    xalign .0
                    size 35

                for option_id in choice["options"]:
                    hbox:
                        xalign 1.
                        $ msg = choice[option_id][1]
                        if fvault.Has(day_id, choice_id, option_id):
                            textbutton msg + "( + )":
                                yalign .5
                                text_size 35
                                selected False
                                text_hover_color "#fff"
                                action SetScreenVariable("selected", None), Function(fvault.Remove, day_id, choice_id, option_id)
                        else:
                            textbutton msg + "(   )":
                                yalign .5
                                text_size 35
                                selected False
                                text_hover_color "#fff"
                                action SetScreenVariable("selected", option_id), Function(fvault.ClearOf, day_id, choice_id, *choice["options"]), Function(fvault.Add, day_id, choice_id, option_id)

        viewport:
            xsize 400
            ysize 900
            mousewheel True
            scrollbars "vertical"

            has vbox
            xfill True
            for entry in fvault.vault:
                text str(entry) size 35

    button:
        xpos 1500
        xanchor 0.
        ypos 100
        xysize (438, 86)
        background "interface/button.png"

        hover_sound "sounds/menu/menu-button-select-3.ogg"

        text "СБРОСИТЬ":
            align (.5, .5)
            size 50
            color "#000"

        action Function(fvault.ClearAll)

    button:
        xpos 1500
        xanchor 0.
        ypos 250
        xysize (438, 86)
        background "interface/button.png"

        hover_sound "sounds/menu/menu-button-select-3.ogg"

        text "ПОДТВЕРДИТЬ":
            align (.5, .5)
            size 50
            color "#000"

        action Return()

define flowchart_selector_data = (
    ("# 1", "day1", "StoryExplainerDCut_Day1", 1920, 5790 +600),
    ("# 2", "day2", "StoryExplainerDCut_Day2", 1920, 8365 +600),
    ("# 3", "day3", "StoryExplainerDCut_Day3", 1920, 10935 +600),
    ("# 4", "day4", "StoryExplainerDCut_Day4", 1920*2, 8295 +600),
    ("# 5", "day5", "StoryExplainerDCut_Day5", 1920*2, 15500 +600),
)

transform flowchart_button:
    on idle:
        linear 0.25 alpha 0.75
    on hover:
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset renpy.random.randint(-5,5) yoffset renpy.random.randint(-5,5)
            linear 0.01 xoffset 0 yoffset 0

screen StoryExplainer_Selector(story_manager):
    $ valid_days = story_manager.ValidDays()

    vbox:
        align (.0, .5)
        xoffset 50
        spacing 25

        for capt, ep_code, scr, width, height in flowchart_selector_data:
            if ep_code in valid_days:
                button:
                    xysize (127, 69)
                    background "interface/05.png"

                    if ep_code in valid_days and story_manager.day_code != ep_code:
                        sensitive True
                        activate_sound "sounds/menu/menu-button-click-1.ogg"
                        hover_sound "sounds/menu/menu-button-select-1.ogg"
                        at flowchart_button

                    elif story_manager.day_code == ep_code:
                        sensitive False

                    text capt align (.5, .5) color "#000"

                    action SetField(story_manager, "day_code", ep_code), SetField(story_manager, "width", width), SetField(story_manager, "height", height), Show(scr, story_manager=story_manager)

screen StoryExplainer_UI(story_manager):

    button:
        align (.98, .95)
        xysize (306, 92)
        add "flowchart_continue_" align (.5, .5)

        if story_manager.IsEnding():
            text _("Меню{#flowchart}") anchor (1., .5) pos (.45, .5) color "#000"
        else:
            text _("Дальше{#flowchart}") anchor (1., .5) pos (.45, .5) color "#000"

        action Return()
        activate_sound "sounds/menu/menu-button-click-1.ogg"
        hover_sound "sounds/menu/menu-button-select-1.ogg"

        at flowchart_button

screen StoryExplainerDCut_Hider():
    tag flowchart

    timer 0.01 action Hide("StoryExplainerDCut_Hider")

define flowchart_dust_ratio = 1.4
define flowchart_bg_ratio = 0.65
image story_bg_1 = Tile("interface/flowchart/texture_bg.jpg")
image story_bg_2 = Tile("interface/flowchart/texture_dust_alpha.png")
image story_bg_3 = "interface/flowchart/vignette.png"

image flowchart_gray = "interface/flowchart/buttons/gray.png"
image flowchart_white = "interface/flowchart/buttons/white.png"
image flowchart_black = "interface/flowchart/buttons/black.png"
image flowchart_dark = "interface/flowchart/buttons/dark.png"
image flowchart_ending = "interface/flowchart/buttons/base02.png"
image flowchart_ending_dim = "interface/flowchart/buttons/base002.png"
image flowchart_frame = "interface/flowchart/buttons/stroke.png"

image flowchart_corner_topleft = "interface/flowchart/frame/up left.png"
image flowchart_corner_topright = "interface/flowchart/frame/up right.png"
image flowchart_corner_bottomleft = "interface/flowchart/frame/down left.png"
image flowchart_corner_bottomright = "interface/flowchart/frame/down right.png"
image flowchart_eye = "interface/flowchart/frame/eye.png"

image flowchart_joystick = "interface/flowchart/buttons/joystick.png"

image flowchart_arrow_down = "interface/flowchart/arrows/down.png"
image flowchart_arrow_down_long = "interface/flowchart/arrows/down_long.png"
image flowchart_arrow_left = "interface/flowchart/arrows/left.png"
image flowchart_arrow_right = "interface/flowchart/arrows/right.png"
image flowchart_arrow_side_left = "interface/flowchart/arrows/side_left.png"
image flowchart_arrow_side_right = "interface/flowchart/arrows/side_right.png"

image flowchart_continue_ = "interface/flowchart/buttons/base04.png"
image flowchart_continue = "interface/flowchart/buttons/base04_arrow.png"

screen StoryExplainer_NarrativeSegment(story_manager, kday, kevent, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent)) or forced:
            $ caption = event["caption"]
        else:
            $ caption = "???"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)) or forced:
            add "flowchart_white" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
        else:
            add "flowchart_gray" align (.5, .5):

                at transform:
                    alpha 0.7
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
screen StoryExplainer_NarrativeSegment_Extended(story_manager, kday, kevent, kopt, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = event["caption"]
        else:
            $ caption = "???"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            add "flowchart_white" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
        else:
            add "flowchart_gray" align (.5, .5):

                at transform:
                    alpha 0.7
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
screen StoryExplainer_EndingSegment(story_manager, kday, kevent, kopt, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize (400, 85)
        xanchor .5
        yanchor .5
        padding (0, 0)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = __("{size=-5}конец:{/size} ") + __(event["caption"])
        else:
            $ caption = __("{size=-5}конец:{/size} ") + "???"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            add "flowchart_ending" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#000000"
        else:
            add "flowchart_ending_dim" align (.5, .5):

                at transform:
                    alpha 0.65
            text caption:
                align (.5, .5)
                size 50
                color "#303030"
screen StoryExplainer_ChoiceSegment(story_manager, kday, kevent, xypos, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)

        background None

        if story_manager.IsMarkedPersist((story_manager.day_code, kevent)) or forced:
            $ caption = event["caption"]
        else:
            $ caption = "???"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)) or forced:
            add "flowchart_black" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#fff"
        else:
            add "flowchart_black" align (.5, .5) alpha 0.65
            text caption:
                align (.5, .5)
                size 50
                color "#ccc"

screen StoryExplainer_OptionSegment(story_manager, kday, kevent, xypos, kopt, forced=False):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    $ option = story_manager.story_db[story_manager.day_code][kevent][kopt]
    $ _x_opt = _x + option["pos"][0]
    $ _y_opt = _y + option["pos"][1]

    frame:
        pos (_x_opt, _y_opt)
        xysize (400, 75)
        xanchor .5
        yanchor .5
        padding (0, 0)

        background None


        if story_manager.IsMarkedPersist((story_manager.day_code, kevent, kopt)) or forced:
            $ caption = option["caption"]
        else:
            $ caption = "???"

        if story_manager.IsMarkedLocal((story_manager.day_code, kevent, kopt)) or forced:
            add "flowchart_black" align (.5, .5)
            add "flowchart_frame" align (.5, .5)
            text caption:
                align (.5, .5)
                size 50
                color "#fff"
        else:
            add "flowchart_dark" align (.5, .5):

                at transform:
                    alpha 0.5
            text caption:
                align (.5, .5)
                size 50
                color "#bdbdbd"
screen StoryExplainer_LookaroundSegment(story_manager, kday, kevent, xypos, xysize, items):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize xysize
        padding (0, 0)
        background None

        add "flowchart_corner_topleft" align (0., 0.)
        add "flowchart_corner_topright" align (1., 0.)
        add "flowchart_corner_bottomleft" align (0., 1.)
        add "flowchart_corner_bottomright" align (1., 1.)

        $ caption = event["caption"]
        if not story_manager.IsMarkedPersist((story_manager.day_code, kevent)):
            $ caption = "???"


        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)):
            add "flowchart_eye" align (.5, 0.)
            text caption ypos 25 xalign .5 color "#fff"

        else:
            add "flowchart_eye" align (.5, 0.):

                at transform:
                    alpha .7
            text caption ypos 25 xalign .5 color "#bdbdbd":
                at transform:
                    alpha .7
    for it in items:
        $ item = story_manager.story_db[story_manager.day_code][kevent][it]
        $ _x_it = _x + item["pos"][0]
        $ _y_it = _y + item["pos"][1]

        frame:
            pos (_x_it, _y_it)
            xysize (400, 75)
            xanchor .5
            yanchor .5
            padding (0, 0)

            background None

            $ caption = item["caption"]

            if not story_manager.IsMarkedPersist((story_manager.day_code, kevent, it)):
                $ caption = "???"

            if story_manager.IsMarkedLocal((story_manager.day_code, kevent, it)):
                add "flowchart_white" align (.5, .5)
                text caption:
                    align (.5, .5)
                    size 50
                    color "#000"
            else:
                add "flowchart_gray" align (.5, .5):

                    at transform:
                        alpha 0.7
                text caption:
                    align (.5, .5)
                    size 50
                    color "#303030"
screen StoryExplainer_GameSegment(story_manager, kday, kevent, xypos, xysize, items):
    $ event = story_manager.story_db[story_manager.day_code][kevent]
    $ _x, _y = xypos

    frame:
        pos (_x, _y)
        xysize xysize
        padding (0, 0)
        background None

        add "flowchart_corner_topleft" align (0., 0.)
        add "flowchart_corner_topright" align (1., 0.)
        add "flowchart_corner_bottomleft" align (0., 1.)
        add "flowchart_corner_bottomright" align (1., 1.)


        $ caption = event["caption"]
        if not story_manager.IsMarkedPersist((story_manager.day_code, kevent)):
            $ caption = "???"


        if story_manager.IsMarkedLocal((story_manager.day_code, kevent)):
            add "flowchart_joystick" align (.5, 0.) matrixcolor BrightnessMatrix(1.0)
            text caption ypos 25 xalign .5 color "#fff"

        else:
            add "flowchart_joystick" align (.5, 0.):
                matrixcolor BrightnessMatrix(1.0)

                at transform:
                    alpha .7
            text caption ypos 25 xalign .5 color "#bdbdbd":
                at transform:
                    alpha .7
    for it in items:
        $ item = story_manager.story_db[story_manager.day_code][kevent][it]
        $ _x_it = _x + item["pos"][0]
        $ _y_it = _y + item["pos"][1]

        frame:
            pos (_x_it, _y_it)
            xysize (400, 75)
            xanchor .5
            yanchor .5
            padding (0, 0)

            background None

            $ caption = item["caption"]

            if not story_manager.IsMarkedPersist((story_manager.day_code, kevent, it)):
                $ caption = "???"

            if story_manager.IsMarkedLocal((story_manager.day_code, kevent, it)):
                add "flowchart_white" align (.5, .5)
                text caption:
                    align (.5, .5)
                    size 50
                    color "#000"
            else:
                add "flowchart_gray" align (.5, .5):

                    at transform:
                        alpha 0.7
                text caption:
                    align (.5, .5)
                    size 50
                    color "#303030"
transform arrow_invalid:
    alpha 0.15
transform arrow_valid:
    alpha 1.00

label story_selector:
    scene black
    menu:
        "story selector":
            jump story_shortcut_selector
        "flags selector":
            $ fvault = EventVault()
            call screen FlagsSelector((1, 2, 3, 4, 5), fvault)
            $ ret = _return

default target_label = None
label flag_shortcut_selector:
    scene black
    $ fvault = EventVault()
    call screen FlagsSelector((1, 2, 3, 4, 5), fvault)
    $ Flags = ConvertEventsToFlags(fvault.vault)

    $ ROUTE_SOLO = Flags.Has("mask")
    $ ROUTE_POLINA = not ROUTE_SOLO and Flags.Has("day2 polina")
    $ ROUTE_FOX = not ROUTE_SOLO and Flags.Has("day2 fox")

    jump expression target_label

label story_shortcut_selector:

    $ algo = StoryStructureAlgo()
    call screen StoryGenerator(algo)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
