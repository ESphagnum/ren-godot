
define suefa_sfx_hover = "sounds/ka-fix-1.ogg"

define Ant_name = __("Антон{#СУЕФА}")
define Rom_name = __("Рома{#СУЕФА}")
define Bya_name = __("Бяша{#СУЕФА}")

image bg_suefa = "interface/suefa/fon.png"
image plaing_su_e_fa:
    "interface/suefa/H_01.png"
    pause 0.3
    "interface/suefa/H_02.png"
    pause 0.2
    "interface/suefa/H_03.png"
    pause 0.2
    "interface/suefa/H_04.png"
    pause 0.2
    "interface/suefa/H_05.png"
    pause 0.2
    "interface/suefa/H_06.png"
    pause 0.2

screen info_suefa:
    zorder 1
    hbox:
        xalign 0.5
        ypos 20
        spacing 790
        frame:
            xsize 250
            ysize 71
            background "interface/suefa/plaska.png"
            text __("Рома{#СУЕФА}") + ": " + str(r_win):
                align 0.5, 0.5
                color "#000"
        frame:
            xsize 250
            ysize 71
            background "interface/suefa/plaska.png"
            text __("Антон{#СУЕФА}") + ": " + str(a_win):
                align 0.5, 0.5
                color "#000"


        at transform:
            on show:
                alpha .0
                linear .5 alpha 1.0
transform for_left_hand_suefa_1:
    xpos -1920
    easein 2.0 xpos 0
    block:
        ease 0.5 xoffset -2 yoffset 2
        ease 0.5 xoffset -4 yoffset 0
        ease 0.5 xoffset 0 yoffset -2
        ease 0.5 xoffset -1 yoffset 2
        repeat

transform for_right_hand_suefa_1:
    xpos 1920
    easein 2.0 xpos fix_hand_a_on_suefa
    block:
        ease 0.5 xoffset 2 yoffset 0
        ease 0.5 xoffset -2 yoffset 2
        ease 0.5 xoffset -1 yoffset 2
        ease 0.5 xoffset 0 yoffset -2
        repeat

transform for_left_hand_suefa_2:
    xpos 0
    block:
        ease 0.5 xoffset -2 yoffset 2
        ease 0.5 xoffset -4 yoffset 0
        ease 0.5 xoffset 0 yoffset -2
        ease 0.5 xoffset -1 yoffset 2
        repeat

transform for_right_hand_suefa_2:
    xpos fix_hand_a_on_suefa
    block:
        ease 0.5 xoffset 2 yoffset 0
        ease 0.5 xoffset -2 yoffset 2
        ease 0.5 xoffset -1 yoffset 2
        ease 0.5 xoffset 0 yoffset -2
        repeat

transform for_frame_suefa_1:
    alpha 0.0
    pause 1.5
    easein 0.7 alpha 1.0

transform for_frame_suefa_2:
    alpha 0.0
    easein 0.7 alpha 1.0

transform for_button_suefa_1:
    alpha 0.0
    pause 1.5
    pause 0.4
    easein 0.3 alpha 1.0
    on hover:
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos 0 ypos 0

transform for_button_suefa_2:
    alpha 0.0
    pause 0.4
    easein 0.3 alpha 1.0
    on hover:
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos renpy.random.randint(-5,5) ypos renpy.random.randint(-5,5)
        linear 0.01 xpos 0 ypos 0

transform for_plaing_su_e_fa_1:
    alpha 1.0
    pause 1.3
    alpha 0.0

transform for_plaing_su_e_fa_2:
    alpha 0.0
    pause 1.3
    alpha 1.0

transform for_suefa_bg_show:
    alpha 0.0
    easein 0.5 alpha 1.0

transform for_suefa_bg_hide:
    alpha 1.0
    easein 0.5 alpha 0.0

transform r_lose:
    pause 0.4

    parallel:
        easeout 2.0 xoffset -200 yoffset 600
    parallel:
        transform_anchor True
        xanchor 0.0
        ycenter 0.5
        pause 0.2
        easeout 2.0 rotate 40
    parallel:
        pause 1.0
        easeout 1.0 alpha 0.0


transform a_lose:
    xpos fix_hand_a_on_suefa
    pause 0.4
    parallel:
        easeout 2.0 xoffset 200 yoffset 600
    parallel:
        transform_anchor True
        xanchor 1.0
        ycenter 0.5
        xpos 1920 + fix_hand_a_on_suefa
        pause 0.2
        easeout 2.0 rotate -40
    parallel:
        pause 1.0
        easeout 1.0 alpha 0.0

init python:
    suefa_r = 3
    suefa_a = 3
    suefa_r_new = 3
    suefa_a_new = 3
    a_win = 0
    r_win = 0
    suefa_one=True

    fix_hand_a_on_suefa = 86

    def choice_suefa(a):
        global suefa_r_new, suefa_a_new
        suefa_r_new = renpy.random.randint(1,3)
        suefa_a_new = a

    def accept_suefa():
        global suefa_r_new, suefa_a_new, suefa_r, suefa_a
        suefa_r, suefa_a = suefa_r_new, suefa_a_new

    def start_suefa_game():
        global suefa_r_new, suefa_a_new, r_win, a_win, suefa_one
        a_win = 0
        r_win = 0
        
        
        renpy.show("bg_suefa", [for_suefa_bg_show])
        
        renpy.call_screen("start_suefa", first_time = True)
        
        
        while a_win < 3 and r_win < 3:
            if a_win == 1 and r_win == 0 and suefa_one:
                suefa_one=False
                renpy.pause(1.0, hard=True)
                suefa_r_new = 3
                suefa_a_new = 3
                
                voice("voice/anton/3day/049 Es.ogg")
                renpy.say(Ant_name, _("\"Есть!\""))
                
                
                renpy.say(None, _("Я торжествующе вскинул к потолку кулаки."))
                
                voice("voice/romka/3day/85 S.ogg")
                renpy.say(Rom_name, _("\"Стопе, стопе! У нас принято до трёх побед играть.\""))
                
                voice("voice/anton/3day/050 A.ogg")
                renpy.say(Ant_name, _("\"А раньше сказать?\""))
                
                voice("voice/byasha/3day/118 Ti.ogg")
                renpy.say(Bya_name, _("\"Ты думал, всё так просто будет, на?\""))
                
                voice("voice/romka/3day/86 N.ogg")
                renpy.say(Rom_name, _("\"Не пойму я, чё ты хмуришься так? Один раз уже выиграл, преимущество на твоей стороне.\""))
                
                voice("voice/romka/3day/87 D.ogg")
                renpy.say(Rom_name, _("\"Давай-ка продолжим. Раз, два, три!\""))
                
                renpy.show_screen("info_suefa")
            
            elif r_win == 1 and a_win == 0 and suefa_one:
                suefa_one=False
                renpy.pause(1.0, hard=True)
                suefa_r_new = 3
                suefa_a_new = 3
                
                renpy.play("voice/romka/3day/88 Ulu.ogg", channel="sfx")
                renpy.say(None, _("Ромка и Бяша радостно заулюлюкали, когда я проиграл."))
                
                voice("voice/byasha/3day/119 Kr.ogg")
                renpy.say(Bya_name, _("\"Красава, Ромка! Под орех Тошика разделал, на!\""))
                
                
                renpy.say(None, _("Как бы ни было грустно по итогу остаться ни с чем, я протянул вкладыш ребятам."))
                renpy.say(None, _("Папа всегда говорил, что карточный долг — это святое, хоть тут у нас вовсе и не карты."))
                renpy.say(None, _("Ромка сложил руки на груди и с довольной миной осматривал свой приз, а затем, посмотрев на меня, вдруг выдал:"))
                
                voice("voice/romka/3day/89 Ch.ogg")
                renpy.say(Rom_name, _("\"Чего, Тошик, приуныл? Ладно, давай, как другу, дам шанс отыграться.\""))
                
                voice("voice/romka/3day/90 Eg.ogg")
                renpy.say(Rom_name, _("\"Играем, скажем... до трёх побед.\""))
                
                voice("voice/byasha/3day/120 Nuti.ogg")
                renpy.say(Bya_name, _("\"Ну ты, Ромыч, и щедрый тип.\""))
                
                renpy.play("voice/romka/3day/97 Waha.ogg", channel="sfx")
                renpy.say(None, _("Дружки вновь гиенисто засмеялись, но Ромка тут же серьёзно поднял кулак."))
                renpy.say(None, _("Он явно хотел продолжить."))
                
                renpy.show_screen("info_suefa")
            
            renpy.pause(1.0)
            renpy.call_screen("start_suefa")
        
        if a_win == 3:
            renpy.pause(1.0, hard=True)
            renpy.show_screen("win_suefa", winer = "a")
            renpy.pause(3.0, hard=True)
            renpy.play("sounds/Victory2.ogg")
            renpy.say(None, _("Я с подозрением взглянул на оппонента."))
        elif r_win == 3:
            renpy.pause(1.0, hard=True)
            renpy.show_screen("win_suefa", winer = "r")
            renpy.pause(3.0, hard=True)
            
            voice("voice/romka/3day/91 K.ogg")
            renpy.play("sounds/Fail_su2.ogg")
            renpy.say(Rom_name, _("\"Как два пальца...\""))
        
        renpy.pause(0.5, hard=True)
        renpy.hide_screen("info_suefa")
        renpy.hide_screen("win_suefa")
        renpy.hide("bg_suefa")

    def check_win_suefa():
        global suefa_r_new, suefa_a_new, r_win, a_win
        if (suefa_r_new + 1 == suefa_a_new) or (suefa_r_new - 2 == suefa_a_new):
            r_win += 1
        elif (suefa_a_new + 1 == suefa_r_new) or (suefa_a_new - 2 == suefa_r_new):
            a_win += 1
        elif suefa_a_new == suefa_r_new:
            pass

screen start_suefa(first_time=False):
    add "interface/suefa/01.png":
        if first_time:
            at for_frame_suefa_1
        else:
            at for_frame_suefa_2

    add "interface/suefa/R_0"+str(suefa_r)+".png":
        if first_time:
            at for_left_hand_suefa_1
        else:
            at for_left_hand_suefa_2
    add "interface/suefa/A_0"+str(suefa_a)+".png":
        if first_time:
            at for_right_hand_suefa_1
        else:
            at for_right_hand_suefa_2

    for i in range(3):
        imagebutton:
            idle "interface/suefa/" + str(i+1) + ".png"
            focus_mask True
            if first_time:
                at for_button_suefa_1
            else:
                at for_button_suefa_2
            action Function(choice_suefa, i+1), Hide("start_suefa"), Show("end_suefa")

            if suefa_sfx_hover:
                hover_sound suefa_sfx_hover

    timer 0.01 action Hide("end_suefa", transition = dissolve)

screen end_suefa:
    add "bg_suefa"
    add "plaing_su_e_fa" at for_plaing_su_e_fa_1
    add "interface/suefa/R_0"+str(suefa_r_new)+".png" at for_plaing_su_e_fa_2
    add "interface/suefa/A_0"+str(suefa_a_new)+".png" at for_plaing_su_e_fa_2:
        xpos fix_hand_a_on_suefa
    timer 1.5 action Function(check_win_suefa), Return()

screen win_suefa(winer):
    add "interface/suefa/R_03.png":
        if winer == "a":
            at r_lose
        else:
            at for_left_hand_suefa_2
    add "interface/suefa/A_03.png":
        if winer == "r":
            at a_lose
        else:
            at for_right_hand_suefa_2

    timer 0.01 action Hide("end_suefa", transition = dissolve)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
