init python:
    
    gallery_slot_size = (360, 180)
    gallery_data = [
        {"img": "end/end_mini/end.png", "trigger": ("day4", "ending", "needle"), "caption": _("Школяр-убийца"), "label": ""},
        {"img": "end/end_mini/was_there.png", "trigger": ("day5", "ending", "was_there"), "caption": _("А был ли мальчик"), "label": ""},
        {"img": "end/end_mini/mad_world.png", "trigger": ("day5", "ending", "mad_world"), "caption": _("Безумный Мир"), "label": ""},
        {"img": "end/end_mini/1890.png", "trigger": ("day5", "ending", "apocalypse"), "caption": _("Апокалипсис сегодня"), "label": ""},
        {"img": "end/end_mini/genius.png", "trigger": ("day5", "ending", "genius"), "caption": _("Гений и мрак"), "label": ""},
        {"img": "end/end_mini/recipe.png", "trigger": ("day5", "ending", "recipe"), "caption": _("Рецепт любви"), "label": ""},

        {"img": "end/end_mini/still_water.png", "trigger": ("day5", "ending", "still_water"), "caption": _("В тихом омуте"), "label": ""},
        {"img": "end/end_mini/bloody_claw.png", "trigger": ("day5", "ending", "bloody_claw"), "caption": _("Кровавый коготь"), "label": ""},
        {"img": "end/end_mini/among_us.png", "trigger": ("day5", "ending", "among_us"), "caption": _("Звери среди нас"), "label": ""},
        {"img": "end/end_mini/pack_of.png", "trigger": ("day5", "ending", "pack_of"), "caption": _("Стая убийц"), "label": ""},
        {"img": "end/end_mini/rage.png", "trigger": ("day5", "ending", "rage"), "caption": _("Животная ярость"), "label": ""},
        {"img": "end/end_mini/nightmare.png", "trigger": ("day5", "ending", "nightmare"), "caption": _("Таежный кошмар"), "label": ""},

        {"img": "end/end_mini/past.png", "trigger": ("day5", "ending", "past"), "caption": _("Тени прошлого"), "label": ""},
        {"img": "end/end_mini/hunt.png", "trigger": ("day5", "ending", "hunt"), "caption": _("Сезон охоты"), "label": ""},
        {"img": "end/end_mini/call.png", "trigger": ("day5", "ending", "call"), "caption": _("Зов пропавших"), "label": ""},
        {"img": "end/end_mini/traces.png", "trigger": ("day5", "ending", "traces"), "caption": _("Следы на снегу"), "label": ""},
        {"img": "end/end_mini/in_dark.png", "trigger": ("day5", "ending", "in_dark"), "caption": _("Исчезнувшие в ночи"), "label": ""},
        {"img": "end/end_mini/runaway.png", "trigger": ("day5", "ending", "runaway"), "caption": _("Сбежавший из комы"), "label": ""},

        {"img": "end/end_mini/contract.png", "trigger": ("day5", "ending", "contract"), "caption": _("Контракт с дьяволом"), "label": ""},
        {"img": "end/end_mini/home_violence.png", "trigger": ("day5", "ending", "home_violence"), "caption": _("Домашнее насилие"), "label": ""},
        {"img": Solid("#0ff", xysize = gallery_slot_size), "trigger": None, "caption": "", "label": ""},
        {"img": Solid("#0ff", xysize = gallery_slot_size), "trigger": None, "caption": "", "label": ""},
        {"img": Solid("#0ff", xysize = gallery_slot_size), "trigger": None, "caption": "", "label": ""},
        {"img": Solid("#0ff", xysize = gallery_slot_size), "trigger": None, "caption": "", "label": ""},
    ]
    gallery_by_pages = {
        ("day4", "ending", "needle") : 0,
        ("day5", "ending", "was_there") : 0,
        ("day5", "ending", "mad_world") : 0,
        ("day5", "ending", "apocalypse") : 0,
        ("day5", "ending", "genius") : 0,
        ("day5", "ending", "recipe") : 0,

        ("day5", "ending", "still_water") : 1,
        ("day5", "ending", "bloody_claw") : 1,
        ("day5", "ending", "among_us") : 1,
        ("day5", "ending", "pack_of") : 1,
        ("day5", "ending", "rage") : 1,
        ("day5", "ending", "nightmare") : 1,

        ("day5", "ending", "past") : 2,
        ("day5", "ending", "hunt") : 2,
        ("day5", "ending", "call") : 2,
        ("day5", "ending", "traces") : 2,
        ("day5", "ending", "in_dark") : 2,
        ("day5", "ending", "runaway") : 2,

        ("day5", "ending", "contract") : 3,
        ("day5", "ending", "home_violence") : 3,
    }
    
    def has_endings():
        for event in persistent.story_unlocks:
            for sub in event:
                if sub == "ending":
                    return True
        return False

image gallery_slots = "interface/save_load_menu/015.png"
image gallery_slots_2 = "interface/save_load_menu/016.png"
image gallery_btn_left = "interface/save_load_menu/btn_left.png"
image gallery_btn_right = "interface/save_load_menu/btn_right.png"
image gallery_btn_back = "interface/save_load_menu/btn_back.png"
screen gallery_slot(idx, data):
    if idx == 0:
        $ target_pos = (258, 180)
    if idx == 1:
        $ target_pos = (762, 180)
    if idx == 2:
        $ target_pos = (1257, 180)
    if idx == 3:
        $ target_pos = (258, 515)
    if idx == 4:
        $ target_pos = (762, 515)
    if idx == 5:
        $ target_pos = (1257, 515)

    $ trigger = data.get("trigger")

    if trigger is not None:
        if trigger and trigger in persistent.story_unlocks:


            if new_ending == trigger:
                add Solid("#000", xysize=gallery_slot_size):

                    at transform:
                        pos target_pos
                        1.25
                        data["img"] with ImageDissolve("effect/imagedissolve/vfx_garage/01.jpg", 2.5, ramplen=128)
                text "???":
                    anchor (.5, 1.)
                    pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65)
                    size 40
                    if preferences.language == "japan":
                        font other_font_interface
                    font other_font_interface

                    at transform:
                        alpha 1
                        1.25
                        linear 1.25 alpha 0
                text data["caption"]:
                    anchor (.5, 1.)
                    pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65)
                    size 40
                    if preferences.language == "japan":
                        font other_font_interface
                    font other_font_interface

                    at transform:
                        alpha 0
                        2.5
                        linear 1.25 alpha 1

            else:
                add data["img"] pos target_pos
                text data["caption"]:
                    anchor (.5, 1.)
                    pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65)
                    size 40
                    if preferences.language == "japan":
                        font other_font_interface
                    font other_font_interface


        else:
            add Solid("#000", xysize=gallery_slot_size) pos target_pos

            text "???":
                anchor (.5, 1.)
                pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65)
                size 40
                if preferences.language == "japan":
                    font other_font_interface
                font other_font_interface

transform gallery_but_trn:
    alpha 1.0 yoffset 0 xoffset 0
    on hover:
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

default new_ending = None
screen gallery():
    tag menu
    on "show" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-save_load-1.ogg")

    default current_page = 0 if new_ending is None else gallery_by_pages[new_ending]

    add "bg_menu_save_load" at conf_fon

    fixed:
        at for_show_save_load

        showif current_page == 3:
            add "gallery_slots_2"
        else:
            add "gallery_slots"

        label _("ГАЛЕРЕЯ КОНЦОВОК"):
            xalign .5
            ypos 50
            text_size 70

        use gallery_slot(0, gallery_data[0 + current_page*6])
        use gallery_slot(1, gallery_data[1 + current_page*6])
        use gallery_slot(2, gallery_data[2 + current_page*6])
        use gallery_slot(3, gallery_data[3 + current_page*6])
        use gallery_slot(4, gallery_data[4 + current_page*6])
        use gallery_slot(5, gallery_data[5 + current_page*6])

        if current_page > 0:
            imagebutton:
                idle "gallery_btn_left"
                pos (960-40, 900)
                anchor (1., .5)
                at gallery_but_trn
                action SetScreenVariable("current_page", current_page -1), SetVariable("new_ending", None)

        text str(current_page+1):
            xpos 960
            ypos 900
            anchor (.5, .5)
            size 55


        if current_page < 3:
            imagebutton:
                idle "gallery_btn_right"
                pos (960+40, 900)
                anchor (0., .5)
                at gallery_but_trn
                action SetScreenVariable("current_page", current_page +1), SetVariable("new_ending", None)

        imagebutton:
            idle "gallery_btn_back"
            pos (1676+45, 832 + 40)
            anchor (.5, .5)
            at gallery_but_trn
            action SetVariable("new_ending", None), Return()

    key "game_menu" action [SetVariable("new_ending", None), Return()]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
