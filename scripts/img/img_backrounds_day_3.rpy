init python:
    config.layers.insert (-2,"forlayer") 
init:
    image koshmar_round:
        "locate/school/in_side/Sem_gone/f_01.jpg"
        pause .5
        "locate/school/in_side/Sem_gone/f_02.jpg"
        pause .5
        "locate/school/in_side/Sem_gone/f_03.jpg"
        pause .5
        "locate/school/in_side/Sem_gone/f_04.jpg"
        pause .5
        "locate/school/in_side/Sem_gone/f_05.jpg"
        pause .5
        repeat

    image strela:
        alpha 0.0
        "interface/photorobot/strelkaR.png"
        alpha 0.0
    image Sema_F:
        contains:
            alpha 0.0
            "locate/school/in_side/Sem_gone/S_00.png"
            linear 2.5 alpha 1.
    image Sema_F2:
        contains:
            "locate/school/in_side/Sem_gone/S_00.png"
            alpha 0.0
            "locate/school/in_side/Sem_gone/S_01.png"
            linear 2.5 alpha 1.

    image bg_teacher = "locate/school/in_side/teacher/teacer_fon.jpg"

    image bg_teacher 01 08 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        )
    image bg_teacher 01 08_m = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        (50,0), "locate/school/in_side/Ment/T_02.png",
        )

    image bg_teacher 02 08 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/teacer2.png",
        )

    image bg_teacher_02_bg = "locate/school/in_side/teacher/teacer_fon.jpg"
    image bg_teacher_teach 01 = "locate/school/in_side/teacher/teacer1.png"
    image bg_teacher_teach 02 = "locate/school/in_side/teacher/teacer2.png"

    image bg_teacher 03 08 = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/teacher/teacer_fon.jpg",
        (0,0), "locate/school/in_side/teacher/teacer1.png",
        )


    image bg_classroom base 3 1 no_guys = LiveComposite((2299, 1080),
        (0,0), "locate/school/in_side/classroom/classroom005.png",
        (0,0), "chalk_writings_big",
        (0,0), "locate/school/in_side/classroom/Kate_1.png",
        )

    image teach1 = "locate/school/in_side/classroom/classroom002.png"
    image k_fon = "locate/school/in_side/Kaite01/fon_class.jpg"
    image pol 1 = "locate/school/in_side/classroom/Polina_1.png"
    image pol 2 = "locate/school/in_side/classroom/Polina_2.png"
    image kat 1 = "locate/school/in_side/classroom/Kate_1.png"
    image kat 2 = "locate/school/in_side/classroom/Kate_2.png"
    image bysh 1 = "locate/school/in_side/classroom/Bysh_1.png"
    image bysh 2 = "locate/school/in_side/classroom/Bysh_2.png"
    image rom1 = "locate/school/in_side/classroom/Rom_1.png"
    image sem1 = "locate/school/in_side/classroom/classroom006.png"
    image ant1 = "locate/school/in_side/classroom/classroom001.png"
    image bg_cr = "locate/school/in_side/classroom/classroom005.png"
    image ment 0 = "locate/school/in_side/Ment/T_00.png"
    image ment 1 = "locate/school/in_side/Ment/T_01.png"
    image ment 3 = "locate/school/in_side/Ment/T_03.png"
    image t_fon = "locate/school/in_side/teacher/teacer_fon.jpg"
    image teach 002 = "locate/school/in_side/teacher/teacer2.png"
    image teach 001 = "locate/school/in_side/teacher/teacer1.png"
    image teach 03 = "locate/school/in_side/ment/Ticher.png"
    image bg_ment 00 = "locate/school/in_side/ment/fon.jpg"
    image bg_ment 01 = "locate/school/in_side/ment/klassom1.jpg"
    image bg_ment 02 = "locate/school/in_side/ment/klassom2.jpg"
    image bg_ment 03 = "locate/school/in_side/ment/klassom3.jpg"
    image bg_ment 04 = "locate/school/in_side/ment/klassom4.jpg"
    image ment 01 = "locate/school/in_side/ment/ment_01.png"
    image ment 02 = "locate/school/in_side/ment/ment_02.png"
    image ment 03 = "locate/school/in_side/ment/ment_03.png"
    image doc 01 = "locate/school/in_side/ment/Desk/D01.jpg"
    image doc 02 = "locate/school/in_side/ment/Desk/D02.jpg"
    image doc 21 = "locate/school/in_side/ment/Desk/De01.jpg"
    image doc 22 = "locate/school/in_side/ment/Desk/De02.jpg"
    image doc 23 = "locate/school/in_side/ment/Desk/De03.jpg"
    image doc 24 = "locate/school/in_side/ment/Desk/De04.jpg"
    image doc 024 = "locate/school/in_side/ment/Desk/De004.jpg"
    image doc 25 = "locate/school/in_side/ment/Desk/De05.jpg"
    image doc 26 = "locate/school/in_side/ment/Desk/De06.jpg"
    image doc 27 = "locate/school/in_side/ment/Desk/De07.jpg"
    image doc 28 = "locate/school/in_side/ment/Desk/De08.jpg"
    image table 05 = "locate/school/in_side/Ment/Desk2/05.jpg"

    image pack 001 = "locate/school/in_side/Ment/Desk/Pack_001.png"
    image pack 002 = "locate/school/in_side/Ment/Desk/Pack_002.png"

    image doc 3:
        contains:
            "locate/school/in_side/ment/Desk/D01.jpg"
            pause 0.4
            "locate/school/in_side/ment/Desk/D02.jpg"
            parallel:
                yoffset 0
                linear 0.08 yoffset -4
                linear 0.08 yoffset 4
                yoffset 0
                linear 0.09 yoffset -6
                linear 0.09 yoffset 6
                yoffset 0
                linear 0.05
            2.
            alpha 0
        contains:
            pause 1.5
            "locate/school/in_side/ment/Desk/De01.jpg"
            parallel:
                alpha 0
                linear 0.5 alpha 1

    image bg ment 001 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "locate/school/in_side/ment/ment_01.png",
        )
    image bg ment 002 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "teach 03",
        (0,0), "locate/school/in_side/ment/ment_01.png",
        )
    image bg ment 004 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "teach 03",
        (0,0), "locate/school/in_side/ment/ment_04.png",
        )
    image bg ment 005 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "locate/school/in_side/ment/ment_05.png",
        )
    image bg ment 006 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "teach 03",
        (0,0), "locate/school/in_side/ment/ment_06.png",
        )

    image bg ment 021 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "locate/school/in_side/ment/ment_02.png",
        )
    image bg ment 031 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "locate/school/in_side/ment/ment_03.png",
        )
    image bg ment 041 = LiveComposite((1920, 1080),
        (0,0), "locate/school/in_side/ment/fon.jpg",
        (0,0), "locate/school/in_side/ment/ment_04.png",
        )
    image kat_whisper:
        block:
            "locate/school/in_side/Kaite01/001.jpg"
            pause 1.45
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/003.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/001.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/004.jpg"
            pause .17
            "locate/school/in_side/Kaite01/005.jpg"
            pause .17
            "locate/school/in_side/Kaite01/006.jpg"
            pause (renpy.random.randint(4, 9))
        block:
            "locate/school/in_side/Kaite01/001.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/003.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/001.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/003.jpg"
            pause .17
            "locate/school/in_side/Kaite01/002.jpg"
            pause .17
            "locate/school/in_side/Kaite01/001.jpg"
            pause (renpy.random.randint(6, 11))
            repeat (renpy.random.randint(1, 3))
        block:
            "locate/school/in_side/Kaite01/006.jpg"
            pause .17
            "locate/school/in_side/Kaite01/005.jpg"
            pause .17
            "locate/school/in_side/Kaite01/004.jpg"
            pause .5
            "locate/school/in_side/Kaite01/005.jpg"
            pause .17
            "locate/school/in_side/Kaite01/006.jpg"
            pause .17
            "locate/school/in_side/Kaite01/005.jpg"
            pause .17
            "locate/school/in_side/Kaite01/004.jpg"
            pause .17
            "locate/school/in_side/Kaite01/005.jpg"
            pause .17
            "locate/school/in_side/Kaite01/006.jpg"
            pause (renpy.random.randint(6, 11))
            repeat (renpy.random.randint(1, 3))
        repeat
    image sem_t:
        zoom 1.01
        yalign .5
        "locate/school/in_side/Sem_gone/Sem_fin/01.jpg"
        0.1,
        "locate/school/in_side/Sem_gone/Sem_fin/02.jpg"
        0.1
        "locate/school/in_side/Sem_gone/Sem_fin/03.jpg"
        0.1
        "locate/school/in_side/Sem_gone/Sem_fin/04.jpg"
        0.1
        "locate/school/in_side/Sem_gone/Sem_fin/01.jpg"
        parallel:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat

    image flback:
        Animation("locate/school/in_side/Sem_gone/memories/01.jpg", 0.1,
            "locate/school/in_side/Sem_gone/memories/02.jpg", 0.1,
            "locate/school/in_side/Sem_gone/memories/03.jpg", 0.1,
            "locate/school/in_side/Sem_gone/memories/04.jpg", 0.1,
            "locate/school/in_side/Sem_gone/memories/05.jpg", 0.1,
            "locate/school/in_side/Sem_gone/memories/06.jpg", 0.1)
        pause 0.3
        "locate/school/in_side/Sem_gone/memories/06.jpg"
        zoom 1.10
        yanchor .99
        parallel:
            yoffset 0
            linear 0.08 yoffset -1
            linear 0.08 yoffset 1
            yoffset 0
            linear 0.09 yoffset -2
            linear 0.09 yoffset 2
            yoffset 0
            linear 0.05
            repeat
    image ment_hand = "locate/school/in_side/ment/Hand.png"
    image bg koridorchic_mor_full2 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_mor",
        (0,0), "bg_koridor_notice_mor",
        (0,0), "locate/school/in_side/school_hall/Sem_list.png",
        (0,0), "st_03",
        (0,0), "st_02",
        )
    image bg_koridorchic_day_02 = LiveComposite((4239, 1080),
        (0,0), "bg_koridorchic_day",
        (0,0), "bg_koridor_notice_day",
        (0,0), "sem_list",
        )

    image sem_list = "locate/school/in_side/school_hall/Sem_list.png"
    image ant_hand 2 = "locate/school/in_side/finger/2.png"
    image ant_hand 1 = "locate/school/in_side/finger/1.png"
    image ant_hand_fon = "locate/school/in_side/finger/fon.jpg"
    image ant_hand anim:
        "locate/school/in_side/finger/02.jpg"
        pause 0.1
        "locate/school/in_side/finger/03.jpg"
        pause 0.1
        "locate/school/in_side/finger/04.jpg"
        pause 0.1
        "locate/school/in_side/finger/05.jpg"
        pause 0.1
        "locate/school/in_side/finger/06.jpg"
        pause 0.1
        "locate/school/in_side/finger/07.jpg"
        pause 0.1
        "locate/school/in_side/finger/08.jpg"
        pause 0.1
        "locate/school/in_side/finger/09.jpg"
        pause 0.1
        "locate/school/in_side/finger/10.jpg"
        pause 0.1
        "locate/school/in_side/finger/1.png"
        parallel:
            linear 1.0 xpos -10 ypos 2
            linear 1.0 xpos -8 ypos 2
            linear 1.0 xpos -6 ypos 0
            linear 1.0 xpos -4 ypos 4
            linear 1.0 xpos -2 ypos 2
            linear 1.0 xpos 0 ypos 0
            repeat

    image sem_memo:
        "locate/school/in_side/Sem_memo/001.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/002.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/003.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/004.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/005.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/006.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/007.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/008.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/009.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/010.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/011.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/012.jpg"
        pause 0.1
        "locate/school/in_side/Sem_memo/013.jpg"
        pause 0.1
        alpha 0


    image desk2 5 = "locate/school/in_side/Ment/Desk2/05.jpg"
    image desk2 6 = "locate/school/in_side/Ment/Desk2/06.jpg"
    image desk2 anim:
        "locate/school/in_side/Ment/Desk2/01.jpg"
        pause 0.15
        "locate/school/in_side/Ment/Desk2/02.jpg"
        pause 0.15
        "locate/school/in_side/Ment/Desk2/03.jpg"
        pause 0.15
        "locate/school/in_side/Ment/Desk2/04.jpg"
        pause 0.15
    image Gar_Photo = "locate/school/in_side/Ment/Desk/Gar_Photo.png"
    image ant_clas_blink_1 = "locate/school/in_side/Anton_class/blink_01.png"
    image ant_clas_blink:
        alpha 0
        choice:
            3.
        choice:
            4.
        choice:
            5.
        alpha 1
        "locate/school/in_side/Anton_class/blink_2.png"
        .1
        "locate/school/in_side/Anton_class/blink_3.png"
        .1
        "locate/school/in_side/Anton_class/blink_2.png"
        .1
        repeat

    image ant_clas_1 1:
        contains:
            "locate/school/in_side/Anton_class/Anton.png"
        contains:
            "ant_clas_blink"
    image ant_clas_1_2:
        contains:
            "locate/school/in_side/Anton_class/Anton.png"
        contains:
            "ant_clas_blink_1"
    image ant_clas_2:
        contains:
            "locate/school/in_side/Anton_class/Anton2.png"
        contains:
            "ant_clas_blink"
    image ant_clas_1 rot:
        contains:
            "locate/school/in_side/Anton_class/Anton2.png"
        contains:
            "locate/school/in_side/Anton_class/M_02.png"
    image ant_clas_1 rot2:
        contains:
            "locate/school/in_side/Anton_class/Anton2.png"
        contains:
            "locate/school/in_side/Anton_class/M_03.png"

    image ant_clas_fon = "locate/school/in_side/Anton_class/Fon.jpg"
    image ant_clas_3 = "locate/school/in_side/Anton_class/1.png"
    image ant_clas_4 = "locate/school/in_side/Anton_class/2.png"
    image ant_clas_4_aside = "locate/school/in_side/Anton_class/blink_01.png"
    image ant_clas_5 = "locate/school/in_side/Anton_class/3.png"
    image ant_clas_m3 = "locate/school/in_side/Anton_class/m_03.png"
    image ant_clas_m4 = "locate/school/in_side/Anton_class/m_04.png"
    image ant_clas_m5 = "locate/school/in_side/Anton_class/m_05.png"
    image ant_clas_m6 = "locate/school/in_side/Anton_class/m_06.png"
    image ruka_pni_menya = "locate/school/in_side/finger/kickme.png"




    image polina_look_bg = "locate/school/in_side/polina_look/Polinalook.jpg"
    image polina_look2_bg = "locate/school/in_side/polina_look/Polina_look2.jpg"
    image polina_look_1:
        block:
            "locate/school/in_side/polina_look/Polina_look01.png"
            pause 0.1
            "locate/school/in_side/polina_look/Polina_look02.png"
            pause 0.1
            "locate/school/in_side/polina_look/Polina_look03.png"
            pause 0.1
            "locate/school/in_side/polina_look/Polina_look02.png"
            pause 0.1
            "locate/school/in_side/polina_look/Polina_look01.png"
            pause 2
            repeat

    image polina_look_kate1:
        contains:
            "locate/school/in_side/polina_look/Kait_look7.jpg"
            1.5
            alpha 0
        contains:
            "locate/school/in_side/polina_look/Kait_look5.jpg"
            alpha 0
            1.
            linear .5 alpha 1

        contains:
            1.
            block:
                1.
                "locate/school/in_side/polina_look/Kait_look01.png"
                .1
                "locate/school/in_side/polina_look/Kait_look02.png"
                .1
                "locate/school/in_side/polina_look/Kait_look03.png"
                .1
                "locate/school/in_side/polina_look/Kait_look02.png"
                .1
                "locate/school/in_side/polina_look/Kait_look01.png"
                .1
                repeat

    image polina_look_kate2:
        "locate/school/in_side/polina_look/Kait_look6.jpg"

    image polina_look_kate3:
        "locate/school/in_side/polina_look/Kait_look0.jpg"
        1.
        "locate/school/in_side/polina_look/Kait_look3.jpg" with Dissolve(.5)
        .25
        "locate/school/in_side/polina_look/Kait_look4.jpg" with Dissolve(.5)

    image bg photor_ron = LiveComposite((1920, 1080),
        (-1091, 0), im.MatrixColor("locate/school/in_side/classroom/Rom_2.png",
            im.matrix.brightness(0.10))
        )
    image bg photor_ment = LiveComposite((1920, 1080),
        (-1091, 0), im.MatrixColor("locate/school/in_side/classroom/ment.png",
            im.matrix.brightness(0.10))
        )

    image lists = "interface/photorobot/P_01.png"
    image Byash ha = "sprite/Byasha/Hee/b_day/1_body/01.png"

    image bg_tupic = "locate/school/in_side/Tupichok/Tupichok.jpg"
    image tupic_01 = "locate/school/in_side/Tupichok/Tupichok01.png"
    image tupic_02 = "locate/school/in_side/Tupichok/Tupichok02.png"
    image tupic_03 = "locate/school/in_side/Tupichok/Tupichok03.png"

    image byash000 = "sprite/B01.png"
    image polor = "locate/school/in_side/Polaroid00.jpg"
    image polor2 = "interface/suefa/Polaroid2.png"
    image polor02 = "interface/suefa/Polaroid02.png"
    image scen_polor = LiveComposite((1920, 1080),
        (0, 0), "locate/school/in_side/choose_sema/Sema_00.jpg",
        (0, 0), "interface/suefa/Polaroid2.png"
        )

    image vkladish00 = "interface/suefa/vkladush_00.png"
    image vkladish0 = "interface/suefa/vkladush_0.png"
    image pol_win_bg = "interface/suefa/Poloroid_hand_2.png"
    image pol_win_h:
        "interface/suefa/Poloroid_hand.png"
        block:
            linear 0.1 yoffset -2
            linear 0.1 yoffset 0
            linear 0.1 yoffset 1
            linear 0.1 yoffset -1
            linear 0.1 yoffset 0
            linear 0.1 yoffset 1
            linear 0.1 yoffset 2
            linear 0.1 yoffset 1
            linear 0.1 yoffset 0
            repeat

    image house_night01 = "locate/home/out_side/hOUSE_night01.jpg"
    image sprite_polina_d3 = "sprite/Polina.png"
    image d3_rasp_move:
        "locate/home/in_side/2st_floor/anton_room/day2_end/rasp.jpg"
        align (.5,.5)
        subpixel True
        linear 16. zoom .675

    image classroom_day_bg = "locate/school/in_side/classroom/classroom_Day.jpg"
    image mail_01 = "locate/school/in_side/classroom/mail.png"
    image mail_hand = "locate/school/in_side/classroom/mail2.png"
    image tupichok_bg = LiveComposite((1920, 1080),
        (0, 0), "locate/school/in_side/Tupichok/fon.jpg",
        (0, 0), "locate/school/in_side/Tupichok/tupik.png",
        )
    image tupichok_fon = "locate/school/in_side/Tupichok/fon.jpg"
    image tupichok_tup = "locate/school/in_side/Tupichok/tupik.png"
    image tupichok_floor = "locate/school/in_side/Tupichok/floor.jpg"
    image tupichok_notebook = "locate/school/in_side/Tupichok/notebook.png"
    image tupichok_notebook2 = "locate/school/in_side/Tupichok/notebook2.png"
    image cover_tup = "locate/school/in_side/Tupichok/cover.png"
    image cover_2 = "locate/home/out_side/cover.png"
    image tetrad 00 = "locate/school/in_side/classroom/00.png"
    image tetrad 01 = "locate/school/in_side/classroom/01.png"
    image tetrad 02 = "locate/school/in_side/classroom/02.png"
    image tetrad 03 = "locate/school/in_side/classroom/03.png"
    image tetrad 04 = "locate/school/in_side/classroom/04.png"
    image tetrad 05 = "locate/school/in_side/classroom/05.png"
    image tetrad 06 = "locate/school/in_side/classroom/06.png"
    image tetrad 07 = "locate/school/in_side/classroom/07.png"
    image tetrad 08 = "locate/school/in_side/classroom/08.png"
    image tetrad 09 = "locate/school/in_side/classroom/09.png"
    image tetrad 10 = "locate/school/in_side/classroom/10.png"
    image tetrad 11 = "locate/school/in_side/classroom/11.png"
    image tetrad 12 = "locate/school/in_side/classroom/12.png"
    image tetrad 13 = "locate/school/in_side/classroom/13.png"
    image tetrad 14 = "locate/school/in_side/classroom/14.png"
    image tetrad 15 = "locate/school/in_side/classroom/15.png"
    image tetrad 16 = "locate/school/in_side/classroom/16.png"
    image tetrad 17 = "locate/school/in_side/classroom/17.png"
    image tetrad 18 = "locate/school/in_side/classroom/18.png"
    image tetrad 19 = "locate/school/in_side/classroom/19.png"
    image tetrad 20 = "locate/school/in_side/classroom/20.png"
    image tupichok_tup = "locate/school/in_side/Tupichok/tupik.png"
    image tupichok_floor = "locate/school/in_side/Tupichok/floor.jpg"
    image tupichok_notebook = "locate/school/in_side/Tupichok/notebook.png"
    image tupichok_book = "locate/school/in_side/Tupichok/book.jpg"

    image tupichok_cg01 = "locate/school/in_side/Tupichok/Polinacg01.png"
    image tupichok_cg02 = "locate/school/in_side/Tupichok/Polinacg02.png"

    image tupichok_cg_animated:
        contains:
            "tupichok_cg01"
        contains:
            "tupichok_cg02"
            alpha 0


            block:
                alpha 0
                .25
                alpha 1
                .25
                repeat

    image tupichok_cg4 = "locate/school/in_side/Tupichok/Polinacg4.jpg"

    image tupichok_amulet = "locate/school/in_side/Tupichok/Amulet.png"

    image prut_bg:
        "locate/school/in_side/Ment/Tihon/F01.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/F02.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/F03.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/F04.jpg"
        .1
        repeat

    image prut_ment:
        "locate/school/in_side/Ment/Tihon/Tihon1.png"
        .1
        "locate/school/in_side/Ment/Tihon/Tihon2.png"
        .1
        "locate/school/in_side/Ment/Tihon/Tihon3.png"
        .1
        "locate/school/in_side/Ment/Tihon/Tihon4.png"
        .1
        repeat

    image prut_batya:
        yzoom 1.01
        parallel:
            "locate/school/in_side/Ment/Tihon/Father1.jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Father2(5-7).jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Father3.jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Father4.jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Father2(5-7).jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Father06.jpg"
            .1
            block:
                "locate/school/in_side/Ment/Tihon/Father2(5-7).jpg"
                .1
                "locate/school/in_side/Ment/Tihon/Father8.jpg"
                .1
                "locate/school/in_side/Ment/Tihon/Father9.jpg"
                .1
                repeat 2
        parallel:
            linear .05 yoffset -6
            linear .05 yoffset 0
            repeat

    image prut_prut:
        "locate/school/in_side/Ment/Tihon/Prut.png"
        xpos 1920
        linear .75 xpos 1920-3016
        linear .05 ypos -15
        linear .05 ypos 10
        linear .05 ypos -12
        linear .05 ypos 8
        linear .05 ypos -3
        linear .05 ypos 1

    image prut_olya:
        "locate/school/in_side/Ment/Tihon/Olya01.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/Olya02.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/Olya03.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/Olya04.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/Olya05_9.jpg"
        .1
        "locate/school/in_side/Ment/Tihon/Olya06.jpg"
        .1
        block:
            "locate/school/in_side/Ment/Tihon/Olya07.jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Olya08.jpg"
            .1
            "locate/school/in_side/Ment/Tihon/Olya05_9.jpg"
            .1
            repeat 2

    image prut_animation:
        contains:
            "prut_bg"
            alpha 0
            .25
            alpha 1
            2.5
            alpha 0
        contains:
            "prut_ment"
            alpha 0
            .25
            alpha 1
            2.5
            alpha 0
        contains:
            "prut_prut"
            alpha 0
            .25
            alpha 1
            2.5
            alpha 0
        contains:
            "#fff"
            alpha 0
            linear .25 alpha 1
            linear .1 alpha 0
            1.4
            linear .25 alpha 1
            time 5.15
            linear .1 alpha 0
        contains:
            "locate/school/in_side/Ment/Tihon/Olya01.jpg"
            alpha 0
            2.
            linear .1 alpha 1
            "prut_olya"
            1.2
            linear .25 alpha 0
            "locate/school/in_side/Ment/Tihon/Father1.jpg"
            linear .1 alpha 1
            "prut_batya"
            1.2
            linear .25 alpha 0

    image polina_call_phone:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/h1/prih_002.png"
            .07
            "locate/home/in_side/1st_floor/hall/h1/prih_003.png"
            .07
            repeat

    image polina_call_pickedup:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/h1/prih_004.png"

    define pca_delay = 2.0
    image polina_call_animation:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 1.
            linear 1.15*pca_delay xalign 0.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign 1.
            linear 1.15*pca_delay xalign -1.

    image polina_call_anton_bg 0:
        "locate/home/in_side/1st_floor/hall/Anton_call/hall0.jpg"
    image polina_call_anton_bg 1:
        "locate/home/in_side/1st_floor/hall/Anton_call/hall1.jpg"
    image polina_call_anton_bg 2:
        "locate/home/in_side/1st_floor/hall/Anton_call/hall2.jpg"
    image polina_call_anton_bg 3:
        "locate/home/in_side/1st_floor/hall/Anton_call/Cll1.jpg"
    image polina_call_anton_fg:
        "locate/home/in_side/1st_floor/hall/Anton_call/Cll01.png"
    image polina_call_anton_blink:
        alpha 0
        choice:
            4.
        choice:
            6.
        choice:
            8.
        alpha 1
        "locate/home/in_side/1st_floor/hall/Anton_call/1.png"
        .1
        "locate/home/in_side/1st_floor/hall/Anton_call/2.png"
        .1
        "locate/home/in_side/1st_floor/hall/Anton_call/3.png"
        .1
        "locate/home/in_side/1st_floor/hall/Anton_call/2.png"
        .1
        "locate/home/in_side/1st_floor/hall/Anton_call/1.png"
        .1
        repeat

    image polina_call_anton anton5:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/5.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton anton6:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/6.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton anton11:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/11.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton anton22:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/22.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton anton33:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/33.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton anton44:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/44.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc1:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call1.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc2:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call2.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc4:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call4.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc5:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call5.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc6:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call6.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc7:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call7.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_anton antonc8:
        contains:
            "locate/home/in_side/1st_floor/hall/Anton_call/call8.png"
        contains:
            "polina_call_anton_blink"
    image polina_call_art 00:
        contains:
            "locate/home/in_side/1st_floor/hall/call_art/02.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/call_art/00.png"
    image polina_call_art 01:
        "locate/home/in_side/1st_floor/hall/call_art/01.jpg"
    image polina_call_art 02:
        "locate/home/in_side/1st_floor/hall/call_art/02.jpg"
    image polina_call_art 03:
        "locate/home/in_side/1st_floor/hall/call_art/03.jpg"
    image polina_call_art_03:
        "locate/home/in_side/1st_floor/hall/call_art/03.jpg"
    image polina_call_art 003:
        contains:
            "polina_call_art 02"
        contains:
            "locate/home/in_side/1st_floor/hall/call_art/003.png"
    image polina_call_art 04:
        "locate/home/in_side/1st_floor/hall/call_art/04.jpg"
    image polina_call_art 05:
        "locate/home/in_side/1st_floor/hall/call_art/05.jpg"
    image polina_call_art 06:
        "locate/home/in_side/1st_floor/hall/call_art/06.jpg"
    image polina_call_art_06:
        "locate/home/in_side/1st_floor/hall/call_art/06.png"
    image polina_call_art 07:
        "locate/home/in_side/1st_floor/hall/call_art/07.jpg"
    image polina_call_art 08:
        "locate/home/in_side/1st_floor/hall/call_art/08.jpg"
    image polina_call_art 008:
        contains:
            "polina_call_art 02"
        contains:
            "locate/home/in_side/1st_floor/hall/call_art/008.png"
    image polina_call_art 09:
        "locate/home/in_side/1st_floor/hall/call_art/09.jpg"
    image polina_call_art 009:
        contains:
            "polina_call_art 02"
        contains:
            "locate/home/in_side/1st_floor/hall/call_art/009.png"
    image polina_call_art 10:
        "locate/home/in_side/1st_floor/hall/call_art/10.jpg"
    image polina_call_art 11:
        "locate/home/in_side/1st_floor/hall/call_art/11.jpg"
    image polina_call_art 12:
        "locate/home/in_side/1st_floor/hall/call_art/12.jpg"

    image polina_call_betray_idle:
        "locate/home/in_side/1st_floor/hall/call_art/P.png"
    image polina_call_betray_hover:
        im.MatrixColor("locate/home/in_side/1st_floor/hall/call_art/P.png",
            im.matrix.brightness(0.10))

    image polina_call_friend_idle:
        "locate/home/in_side/1st_floor/hall/call_art/R.png"
    image polina_call_friend_hover:
        im.MatrixColor("locate/home/in_side/1st_floor/hall/call_art/R.png",
            im.matrix.brightness(0.10))

    image door_peephole_bg:
        "locate/home/in_side/1st_floor/hall/h1/Outside1.jpg"

    image door_peephole_animation:
        contains:
            "door_peephole_bg"
        contains:
            "locate/home/in_side/1st_floor/hall/h1/Outside2.png"
            pos (.5, -.32)
            anchor (.5, .0)
            subpixel True
            transform_anchor True
            linear 1.5 rotate 180

    image door_peephole_static:
        contains:
            "door_peephole_bg"
        contains:
            "locate/home/in_side/1st_floor/hall/h1/Outside2.png"
            pos (.5, -.32)
            anchor (.5, .0)

    image door_peephole_hall = "locate/home/in_side/1st_floor/hall/Hall_big.jpg"

    image d3_outside_guys_bg:
        "locate/home/in_side/1st_floor/hall/h1/Outside0.jpg"
    image d3_outside_guys_r:
        "locate/home/in_side/1st_floor/hall/h1/r.png"
    image d3_outside_guys_bysh:
        "locate/home/in_side/1st_floor/hall/h1/bysh.png"

    image d3_outside_guys_a:
        "locate/home/in_side/1st_floor/hall/h1/a.png"
    image d3_outside_guys_olya:
        "locate/home/in_side/1st_floor/hall/h1/ol.png"

    image d3_outside_bysh_0:
        "locate/home/out_side/Owl/000.jpg"

    image d3_outside_olya_0:
        "locate/home/out_side/Owl/001.jpg"

    $ dt_owl = .03
    image d3_outside_owl_anim:
        "locate/home/out_side/Owl/002.jpg"
        dt_owl
        "locate/home/out_side/Owl/003.jpg"
        dt_owl
        "locate/home/out_side/Owl/004.jpg"
        dt_owl
        "locate/home/out_side/Owl/005.jpg"
        dt_owl
        "locate/home/out_side/Owl/006.jpg"
        dt_owl
        "locate/home/out_side/Owl/007.jpg"
        dt_owl
        "locate/home/out_side/Owl/008.jpg"
        dt_owl
        "locate/home/out_side/Owl/009.jpg"

    $ dt_wolf = .1
    image wolf_animation:
        "locate/home/out_side/Meet_beasts/Volk_01.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_02.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_03.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_04.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_05.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_06.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_07.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_08.jpg"
        dt_wolf
        "locate/home/out_side/Meet_beasts/Volk_09.jpg"
        dt_wolf*1.5
        "locate/home/out_side/Meet_beasts/Volk_10.jpg"
        dt_wolf*1.5
        "locate/home/out_side/Meet_beasts/Volk_11.jpg"
        dt_wolf*1.5
        "locate/home/out_side/Meet_beasts/Volk_12.jpg"
        dt_wolf*1.5
        repeat

    image day3_beasts_scene2_bg:
        block:
            choice:
                "locate/home/out_side/Meet_beasts/meet_b/bg01.jpg" with Dissolve(.2)
            choice:
                "locate/home/out_side/Meet_beasts/meet_b/bg02.jpg" with Dissolve(.2)
            choice:
                "locate/home/out_side/Meet_beasts/meet_b/bg03.jpg" with Dissolve(.2)
            choice:
                "locate/home/out_side/Meet_beasts/meet_b/bg04.jpg" with Dissolve(.2)

        block:
            choice:
                .3
            choice:
                1.2
            choice:
                3.2
        repeat


    image day3_beasts_scene2_snow1:
        SnowBlossom("effect/snow/s014.png", count=500, yspeed=(-20, -30), xspeed=(5, 10), border=1000, start=3, fast=True)
    image day3_beasts_scene2_snow2:
        SnowBlossom("effect/snow/s013.png", count=200, yspeed=(-30, -40), xspeed=(15, 20), border=1000, start=5, fast=True)
    image day3_beasts_scene2_snow3:
        SnowBlossom("effect/snow/s012.png", count=200, yspeed=(-60, -90), xspeed=(15, 20), border=1000, start=5, fast=True)
    image day3_beasts_scene2_snow4:
        SnowBlossom("effect/snow/s008.png", count=50, yspeed=(-80, -100), xspeed=(10, 20), border=1000, start=5, fast=True)
    image day3_beasts_scene2_snow5:
        SnowBlossom("effect/snow/s002.png", count=10, yspeed=(-320, -400), xspeed=(5, 20), border=1000, start=8, fast=True)

    image day3_beasts_scene2_children = "locate/home/out_side/Meet_beasts/meet_b/children.png"
    image day3_beasts_scene2_tree = "locate/home/out_side/Meet_beasts/meet_b/tree.png"
    image day3_beasts_scene2_k = "locate/home/out_side/Meet_beasts/meet_b/k.png"

    image day3_forest_scene2_stars:
        alpha 0
        block:
            choice:
                "locate/home/out_side/Meet_beasts/wood/1.png"
            choice:
                "locate/home/out_side/Meet_beasts/wood/2.png"
            choice:
                "locate/home/out_side/Meet_beasts/wood/3.png"
            choice:
                "locate/home/out_side/Meet_beasts/wood/4.png"

        linear .2 alpha 1
        .1
        linear .2 alpha 0

        block:
            choice:
                .1
            choice:
                1.6
            choice:
                3.2
        repeat

    image day3_forest_scene2:
        contains:
            "locate/home/out_side/Meet_beasts/wood/fon.jpg"

        contains:
            "day3_forest_scene2_stars"


    image day3_night_run_anton:
        "locate/forest/runaway/runaway_night/anton/run_away_004.png"
        xalign 0.5
        yalign 0.5
        parallel:
            linear 0.2 xoffset -22 yoffset -72
            linear 0.2 xoffset -122 yoffset -152
            linear 0.2 xoffset -50 yoffset -130
            linear 0.2 xoffset -122 yoffset -172
            repeat

    image day3_night_run_bg1:
        "locate/forest/runaway/runaway_night/0002.jpg"
        xanchor 1.
        pos (2.0, -0.9)
        linear 1. pos (0.0, -2.9)
        repeat

    image day3_night_run_bg2:
        "locate/forest/runaway/runaway_night/0002.jpg"
        xanchor 1.
        pos (4.0, 1.9)
        linear 1. pos (2.0, -0.9)
        repeat

    image runaway_night:
        contains:
            "locate/forest/runaway/runaway_night/0002.jpg"
        contains:
            "day3_night_run_bg1"
        contains:
            "day3_night_run_bg2"
        contains:
            "day3_night_run_anton"

    image fox_give_pidorka_bg:
        contains:
            "locate/home/out_side/Meet_beasts/fon.jpg"
        contains:
            block:
                choice:
                    "locate/home/out_side/Meet_beasts/fon02.png"
                    .1
                    "locate/home/out_side/Meet_beasts/fon03.png"
                    .1
                    "locate/home/out_side/Meet_beasts/fon02.png"
                    .1
                    Null()
                choice:
                    "locate/home/out_side/Meet_beasts/fon04.png"
                    .1
                    "locate/home/out_side/Meet_beasts/fon05.png"
                    .1
                    "locate/home/out_side/Meet_beasts/fon04.png"
                    .1
                    Null()
            block:
                choice:
                    .1
                choice:
                    .3
                choice:
                    .8
                choice:
                    1.6
            repeat

    image fox_give_pidorka 0:
        "locate/home/out_side/Meet_beasts/Fox_give1.png"

    image fox_give_pidorka 1:
        "locate/home/out_side/Meet_beasts/Fox_give2.png"

    image fox_give_pidorka 2:
        "locate/home/out_side/Meet_beasts/Fox_give3.png"

    image fox_give_mask:
        "locate/home/out_side/Meet_beasts/Fox_give4.png"

    image fox_give_beast:
        "locate/home/out_side/Meet_beasts/beast.png"

    image day3_night_sky 1 = "locate/home/out_side/sky/sky_01.jpg"
    image day3_night_sky 2 = "locate/home/out_side/sky/sky_02.jpg"
    image day3_night_sky 3 = "locate/home/out_side/sky/sky_03.jpg"
    image day3_night_sky 4 = "locate/home/out_side/sky/sky_04.jpg"
    image day3_night_sky 5 = "locate/home/out_side/sky/sky_05.jpg"
    image day3_night_sky_fox = "locate/home/out_side/sky/fox.png"

    image day3_night_sky_loop:
        "day3_night_sky 1"
        2.5
        "day3_night_sky 2"
        .1
        "day3_night_sky 3"
        .1
        "day3_night_sky 1"
        .1
        "day3_night_sky 4"
        .1
        "day3_night_sky 5"
        .1
        repeat

    image day3_night_sky_rnd:
        block:
            choice:
                "day3_night_sky 1"
                .1
            choice:
                "day3_night_sky 2"
                .1
            choice:
                "day3_night_sky 3"
                .1
            choice:
                "day3_night_sky 4"
                .1
            choice:
                "day3_night_sky 5"
                .1
        "day3_night_sky 1"
        block:
            choice:
                pause .1
            choice:
                pause .3
            choice:
                pause 1.7
        repeat

    image day3_jump_bg_bw = "locate/home/out_side/Meet_beasts/jump/fon.png"
    image day3_jump_bg_cl = "locate/home/out_side/Meet_beasts/jump/fon_2.png"
    image day3_jump_ground_beasts_bw = "locate/home/out_side/Meet_beasts/jump/01.png"
    image day3_jump_ground_beasts_cl = "locate/home/out_side/Meet_beasts/jump/0_1.png"
    image day3_jump_ground_fox_bw = "locate/home/out_side/Meet_beasts/jump/02.png"
    image day3_jump_ground_fox_cl = "locate/home/out_side/Meet_beasts/jump/0_2.png"
    image day3_jump_air_fox:
        contains:
            "locate/home/out_side/Meet_beasts/jump/Fox-1.png"
        contains:
            alpha 0
            choice:
                4.
            choice:
                6.
            alpha 1
            "locate/home/out_side/Meet_beasts/jump/Fox-2.png"
            .1
            "locate/home/out_side/Meet_beasts/jump/Fox-3.png"
            .1
            "locate/home/out_side/Meet_beasts/jump/Fox-2.png"
            .1
            repeat
    image day3_jump_air_fox_revert:
        contains:
            align (.5, .5)
            "locate/home/out_side/Meet_beasts/jump/Fox-0.png"
        contains:
            align (.5, .5)
            "day3_jump_air_fox"
            alpha .35

    image day3_jump_first:
        contains:
            align (.5,.5)
            "day3_jump_bg_bw"
        contains:
            align (.5,.5)
            "day3_jump_bg_cl"
            alpha 0
            linear 2 alpha .35
        contains:
            align (.5,.5)
            "day3_jump_ground_beasts_bw"
        contains:
            align (.5,.5)
            "day3_jump_ground_beasts_cl"
            alpha 0
            linear 2 alpha .35
        contains:
            align (.5,.5)
            "day3_jump_ground_fox_bw"
        contains:
            align (.5,.5)
            "day3_jump_ground_fox_cl"
            alpha 0
            linear 2 alpha .35

    image day3_jump_second:
        contains:
            align (.5,.5)
            "day3_jump_bg_cl"
        contains:
            align (.5,.5)
            "day3_jump_ground_beasts_cl"

    image day3_jump_revert:
        contains:
            align (.5,.5)
            "day3_jump_bg_bw"
        contains:
            align (.5,.5)
            "day3_jump_bg_cl"
            alpha .35
        contains:
            align (.5,.5)
            "day3_jump_ground_beasts_bw"
        contains:
            align (.5,.5)
            "day3_jump_ground_beasts_cl"
            alpha .35

    $ dstar = .1
    image day3_jump_sky_stars:
        contains:
            align (.5,.5)
            "locate/home/out_side/Meet_beasts/jump/s_1.png"

        contains:
            align (.5,.5)
            block:
                choice:
                    "locate/home/out_side/Meet_beasts/jump/Sky2.png"
                    dstar
                    "locate/home/out_side/Meet_beasts/jump/Sky3.png"
                    dstar
                    "locate/home/out_side/Meet_beasts/jump/Sky2.png"
                    dstar
                    Null()
                choice:
                    "locate/home/out_side/Meet_beasts/jump/Sky4.png"
                    dstar
                    "locate/home/out_side/Meet_beasts/jump/Sky5.png"
                    dstar
                    "locate/home/out_side/Meet_beasts/jump/Sky4.png"
                    dstar
                    Null()
            block:
                choice:
                    0.1
                choice:
                    0.3
                choice:
                    0.8
                choice:
                    1.6

            repeat

    image day3_jump_sky_forest = "locate/home/out_side/Meet_beasts/jump/s_2.png"
    image day3_jump_sky_moon = "locate/home/out_side/Meet_beasts/jump/moon.png"
    image day3_jump_sky_moon face:
        "locate/home/out_side/Meet_beasts/jump/moon1.png"
        .2
        "locate/home/out_side/Meet_beasts/jump/moon2.png"
        .2
        repeat

    image day3_jump_snow = LiveComposite((1920, 1080),
        (0, 0), SnowBlossom("effect/snow/s011.png", count=80, yspeed=(-20, 60), xspeed=(320, 350), border=0, start=0, fast=False),
        (0, 0), SnowBlossom("interface/main_meny/partikl_001.png", count=20, yspeed=(-20, 40), xspeed=(340, 430), border=1, start=0, fast=False))

    image day3_cornermeet_fence_anton = "images/locate/school/out_side/school_coner/Anton.png"
    image day3_cornermeet_fence_anton_02:
        contains:
            "images/locate/school/out_side/school_coner/Anton.png"
        contains:
            "images/locate/school/out_side/school_coner/Anton02.png"



    image day3_cornermeet_kitchen = Crop((1765, 0, 1920, 1080), "locate/home/in_side/1st_floor/kitchen/kitchen_nm.jpg")

    image day3_cornermeet_anton_transition:

        contains:
            "day3_cornermeet_bg_fence_default"
            pause 1.5
            "day3_cornermeet_kitchen" with Dissolve(1.)


        contains:
            "day3_cornermeet_fence_anton"
            pause 1.5
            "sprite/Ant/Normal/b_day/1_body/00.png" with Dissolve(1.)


        contains:
            "ant_clas_blink"

    image day3_cornermeet_roma = "images/locate/school/out_side/school_coner/R.png"
    image day3_cornermeet_bg = "images/locate/school/out_side/school_coner/Rom_1.jpg"
    image day3_cornermeet_tree = "images/locate/school/out_side/school_coner/Tree.png"

    image day3_cornermeet_bg_fence_near = "images/locate/school/out_side/school_coner/fence_near.png"
    image day3_cornermeet_bg_fence_mid = "images/locate/school/out_side/school_coner/fence_mid.png"
    image day3_cornermeet_bg_fence_far = "images/locate/school/out_side/school_coner/fence_far.jpg"

    image day3_cornermeet_bg_fence_default:
        contains:
            align (.5, 1.)
            "day3_cornermeet_bg_fence_far"
        contains:
            align (.5, 1.)
            xoffset 200
            "day3_cornermeet_bg_fence_mid"
        contains:
            align (.5, 1.)
            "day3_cornermeet_bg_fence_near"

    image day3_cornermeet_eye:
        "locate/school/out_side/school_coner/defense/Anton_eye2.jpg"
        .1
        "locate/school/out_side/school_coner/defense/Anton_eye3.jpg"
        .1
        "locate/school/out_side/school_coner/defense/Anton_eye2.jpg"
        .1
        "locate/school/out_side/school_coner/defense/Anton_eye1.jpg"

        choice:
            4.
        choice:
            5.
        choice:
            6.

        repeat

    image day3_cornermeet_amulet_bg:
        "locate/school/out_side/school_coner/defense/fon.jpg"
    image day3_cornermeet_amulet_anton 1:
        "locate/school/out_side/school_coner/defense/Amulet1.png"
    image day3_cornermeet_amulet_anton 2:
        "locate/school/out_side/school_coner/defense/Amulet2.png"
    image day3_cornermeet_amulet_anton 3:
        "locate/school/out_side/school_coner/defense/Amulet3.png"
    image day3_cornermeet_amulet_anton 4:
        "locate/school/out_side/school_coner/defense/Amulet4.png"

    image day3_cornermeet_flower_base:
        contains:
            "locate/street/anton_battle/scene_02/fon_01.jpg",
        contains:
            "locate/street/rom_knife/R_knife00.png"

    image day3_cornermeet_flower_hand = "locate/street/rom_knife/fl.png"

    image day3_cornermeet_flower_smile = "locate/street/rom_knife/R_knife10.png"

    image day3_cornermeet_hit1:
        contains:
            "Romka Evil b_day_winter 01 normal ahead 01"
        contains:
            "locate/school/out_side/school_coner/Fight/Fight_01.png"

    image day3_cornermeet_hit2:
        contains:
            "Romka Evil b_day_winter 01 normal ahead 01"
        contains:
            "locate/school/out_side/school_coner/Fight/Fight_02.png"

    image day3_cornermeet_hit3:
        contains:
            "Romka Evil b_day_winter 01 normal ahead 01"
        contains:
            "locate/school/out_side/school_coner/Fight/Fight_03.png"

    image day3_cornermeet_hit4:
        "locate/school/out_side/school_coner/Fight/Fight_04.png"

    image day3_cornermeet_hit5:
        "locate/school/out_side/school_coner/Fight/Fight_05.png"

    image day3_cornermeet_hit6:
        "locate/school/out_side/school_coner/Fight/Fight_06.png"

    image day3_cornermeet_hit_anim:
        "day3_cornermeet_hit1"
        .1
        "day3_cornermeet_hit2"
        .1
        "day3_cornermeet_hit3"
        .1
        "day3_cornermeet_hit4"
        .1
        "day3_cornermeet_hit5"
        .1
        "day3_cornermeet_hit6"
        .1
        Null()

    image day3_cornermeet_dragon:
        "locate/school/out_side/Dragon.png"

    image anton_sp_05:
        "locate/street/Anton_battle/scene_03/Anton_05.png"

    image day3_romafall_blink:
        "locate/school/out_side/school_coner/Romka_fell/1.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/2.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/03.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/2.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/1.png"
        .1
        choice:
            4.
        choice:
            6.
        choice:
            8.
        repeat

    image day3_romafall_blink2:
        "locate/school/out_side/school_coner/Romka_fell/01.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/02.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/03.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/02.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/01.png"
        .1
        choice:
            4.
        choice:
            6.
        choice:
            8.
        repeat

    image day3_romafall_closed = "locate/school/out_side/school_coner/Romka_fell/03.png"

    image day3_romafall_opening:
        "locate/school/out_side/school_coner/Romka_fell/03.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/02.png"
        .1
        "locate/school/out_side/school_coner/Romka_fell/01.png"

        pause 1.

        block:
            "locate/school/out_side/school_coner/Romka_fell/01.png"
            .025
            "locate/school/out_side/school_coner/Romka_fell/02.png"
            .025
            "locate/school/out_side/school_coner/Romka_fell/03.png"
            .025
            "locate/school/out_side/school_coner/Romka_fell/02.png"
            .025
            "locate/school/out_side/school_coner/Romka_fell/01.png"
            .25

            repeat 2

        "locate/school/out_side/school_coner/Romka_fell/1.png" with Dissolve(.25)

    image day3_romafall_eyes 0:
        "day3_romafall_closed"
        1.
        "day3_romafall_opening"
        2.5
        "day3_romafall_blink"

    image day3_romafall_eyes 1 = "day3_romafall_blink"
    image day3_romafall_eyes 2 = "day3_romafall_blink2"

    image day3_romafall_bg 0 = "locate/school/out_side/school_coner/Romka_fell/Rom_1.jpg"
    image day3_romafall_bg 1 = "locate/school/out_side/school_coner/Romka_fell/Rom_2.jpg"

    image day3_romafall_anton = "locate/school/out_side/school_coner/Romka_fell/Ant.png"

    image Olya Chat amaze:
        contains:
            "Olya Amaze b_evening 00 good ahead 00"
        contains:
            block:
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/01.png"
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/02.png"
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/04.png"
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/05.png"
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/06.png"
                choice:
                    "sprite/olya/amaze/b_evening/3_mouth/07.png"

            block:
                choice:
                    .10
                choice:
                    .15
                choice:
                    .15
                choice:
                    .20
            repeat

    image Olya Chat happy:
        contains:
            "Olya Happy b_evening 00 good ahead 00"
        contains:
            block:
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/01.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/02.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/03.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/04.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/05.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/06.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/07.png"
                choice:
                    "sprite/olya/happy/b_evening/3_mouth/08.png"

            block:
                choice:
                    .10
                choice:
                    .15
                choice:
                    .15
                choice:
                    .20
            repeat

    image Olya Chat serious:
        "Olya Serious b_evening 01 good ahead 08"

    image bg_Olga_room_n_2_bg = "locate/home/in_side/2st_floor/olga_room/Olga_room_n_2.jpg"

    default day3_preduck_olya_dt = .15
    image day3_preduck_olya_light:
        "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_01.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/Olga_room_Light_02.png" with Dissolve(.1)
        day3_preduck_olya_dt
        repeat
    image day3_preduck_olya_tv:
        "locate/home/in_side/2st_floor/olga_room/Olga_room_tv01.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/Olga_room_tv02.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/Olga_room_tv03.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/Olga_room_tv04.png" with Dissolve(.1)
        day3_preduck_olya_dt
        repeat
    image day3_preduck_olya_vid:
        "locate/home/in_side/2st_floor/olga_room/tv_00/TV_001.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/tv_00/TV_002.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/tv_00/TV_003.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/tv_00/TV_004.png" with Dissolve(.1)
        day3_preduck_olya_dt
        "locate/home/in_side/2st_floor/olga_room/tv_00/TV_005.png" with Dissolve(.1)
        day3_preduck_olya_dt
        repeat

    image day3_preduck_olya_room:
        contains:
            "bg_Olga_room_n_1_bg"
        contains:
            "day3_preduck_olya_light"
        contains:
            "day3_preduck_olya_tv"

    image day3_preduck_olya_room_vid:
        contains:
            "bg_Olga_room_n_1_bg"
        contains:
            "day3_preduck_olya_light"
        contains:
            "day3_preduck_olya_vid"


    image day3_karp:
        "locate/home/in_side/2st_floor/olga_room/Fish/karp/01.jpg"
        3.0
        block:
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/02.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/03.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/04.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/05.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/06.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/07.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/08.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/09.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/10.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp/01.jpg"
            8.0
            repeat

    image day3_karp2:
        "locate/home/in_side/2st_floor/olga_room/Fish/karp2/01.jpg"
        3.0
        block:
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/02.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/03.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/04.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/05.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/06.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/07.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/08.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/09.jpg"
            .1
            "locate/home/in_side/2st_floor/olga_room/Fish/karp2/01.jpg"
            8.0
            repeat

    define karp_ep_delay = .2
    image day3_karp_ep:
        block:
            block:
                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep01.jpg"

                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep02.jpg"

            block:
                choice:
                    pause 1.75
                choice:
                    pause 2.25

            block:
                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep01.jpg"
                    karp_ep_delay
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep02.jpg"
                    karp_ep_delay
                    repeat 3

                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep01.jpg"
                    karp_ep_delay
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep02.jpg"
                    karp_ep_delay
                    repeat 4

                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep01.jpg"
                    karp_ep_delay
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep02.jpg"
                    karp_ep_delay
                    repeat 5

            block:
                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep01.jpg"

                choice:
                    "locate/home/in_side/2st_floor/olga_room/Fish/karp2/Ep02.jpg"

            block:
                choice:
                    pause 0.75
                choice:
                    pause 1.50
                choice:
                    pause 2.25

            repeat

    image day3_karp_dad_bg:
        "locate/home/in_side/2st_floor/olga_room/hah/fon.png"

    image day3_karp_dad_frame:
        "locate/home/in_side/2st_floor/olga_room/hah/frame.png"

    image day3_karp_dad laugh:
        align (1., .5)
        xoffset 50
        "locate/home/in_side/2st_floor/olga_room/hah/hah0.png"
        block:
            linear .1 xoffset 30
            linear .1 xoffset 50
            repeat 5
        "locate/home/in_side/2st_floor/olga_room/hah/hah.png"
        block:
            linear .1 xoffset 0
            linear .1 xoffset 50
            linear .1 xoffset 30
            linear .1 xoffset 50
            repeat

    image day3_karp_dad cry:
        xoffset 20
        block:
            "locate/home/in_side/2st_floor/olga_room/hah/cry1.png" with Dissolve(.2)
            .5
            "locate/home/in_side/2st_floor/olga_room/hah/cry2.png" with Dissolve(.1)
            .2
            repeat

    image day3_karp_hug_bg:
        "locate/home/in_side/2st_floor/olga_room/fonOl.png"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/fonOl2.png"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image day3_karp_hug:
        "locate/home/in_side/2st_floor/olga_room/Ol.png"

    image day3_karp_hug_alter:
        "locate/home/in_side/2st_floor/olga_room/Ol2.png"

    image day3_bigwin_1:
        "locate/home/in_side/2st_floor/olga_room/big_win/win_1.png"
    image day3_bigwin_2:
        "locate/home/in_side/2st_floor/olga_room/big_win/win_2.png"
    image day3_bigwin:
        "day3_bigwin_1"
        day3_preduck_olya_dt
        "day3_bigwin_2"
        day3_preduck_olya_dt
        repeat

    image table_home = "locate/home/in_side/1st_floor/kitchen/table_home.jpg"

    image big_fox = "locate/street/walkaway/big_Fox.png"
    image bg_Beast = "locate/forest/pole/Beast.png"
    image ant_day3_evning 1 = LiveComposite((1920, 1080),
        (0, 0), "images/sprite/Ant/Normal/b_evening/1_body/01.png",
        (0, 0), "images/sprite/Ant/Normal/b_evening/3_mouth/01.png",)
    image ant_day3_evning 2 = LiveComposite((1920, 1080),
        (0, 0), "images/sprite/Ant/Normal/b_evening/1_body/01.png",
        (0, 0), "images/sprite/Ant/Normal/b_evening/3_mouth/02.png",)
    image ant_day3_evning cho = LiveComposite((1920, 1080),
        (0, 0), "images/sprite/Ant/Normal/b_evening/1_body/03.png",
        (0, 0), "images/sprite/Ant/Normal/b_evening/3_mouth/05.png",)
    image day3_night_sky_fox_ant:
        pause .5
        block:
            "locate/home/out_side/Sky/A_1.png"
            pause .1
            "locate/home/out_side/Sky/A_2.png"
            pause .1
            "locate/home/out_side/Sky/A_3.png"
            pause .1
            "locate/home/out_side/Sky/A_2.png"
            pause .1
            "locate/home/out_side/Sky/A_1.png"
            pause ((renpy.random.randint(15, 34))/10)
            repeat
    image day3_night_sky_fox_fox:
        block:
            "locate/home/out_side/Sky/Fo_1.png"
            pause .1
            "locate/home/out_side/Sky/Fo_2.png"
            pause .1
            "locate/home/out_side/Sky/Fo_3.png"
            pause .1
            "locate/home/out_side/Sky/Fo_2.png"
            pause .1
            "locate/home/out_side/Sky/Fo_1.png"
            pause ((renpy.random.randint(16, 35))/10)
            repeat
    image day3_night_sky_fox_oko = LiveComposite((1920, 1080),
        (0, 0), "day3_night_sky_fox",
        (0, 0), "day3_night_sky_fox_fox",
        (0, 0), "day3_night_sky_fox_ant",)

    image bg_school_corner_day_onhide2_p1:
        "bg school_corner_day1_no_squirrel"
        xoffset 0
        xalign .5
        yalign 0.8
        easeout 2.0 xalign 1.
    image bg_school_corner_day_onhide2_p2:
        "bg school_day"
        yalign 0.8 xoffset 0+2426-1960
        parallel:
            easein 8.0 xoffset -2000+960
        parallel:
            alpha 0.0
            pause 1.5
            linear 1. alpha 1.0

    image romka_stab_knife blured:
        "locate/school/out_side/school_coner/Romka_stab/K002.png"

    image romka_stab_knife solid:
        "locate/school/out_side/school_coner/Romka_stab/K001.png"

    image romka_stab_1 = "locate/school/out_side/school_coner/Romka_stab/01.jpg"

    image romka_stab_animation:
        "locate/school/out_side/school_coner/Romka_stab/01.jpg"
        .1
        "locate/school/out_side/school_coner/Romka_stab/02.jpg"
        .1
        "locate/school/out_side/school_coner/Romka_stab/03.jpg"
        .1
        "locate/school/out_side/school_coner/Romka_stab/04.jpg"
        .1
        "locate/school/out_side/school_coner/Romka_stab/05.jpg"

    image romka_hit_face_animation:
        "locate/school/out_side/school_coner/Rom_hit/000.png"
        .2
        "locate/school/out_side/school_coner/Rom_hit/001.png" with Dissolve(.2)
        .2
        "locate/school/out_side/school_coner/Rom_hit/002.png" with Dissolve(.2)
        .2
        "locate/school/out_side/school_coner/Rom_hit/003.png" with Dissolve(.2)
        .2
        "locate/school/out_side/school_coner/Rom_hit/004.png" with Dissolve(.2)

    image romka_hit_scene_animation:
        contains:
            "day3_cornermeet_bg_fence_far"
            xalign 1.
            yalign 1.
            easein 15 xalign 0.
        contains:
            "day3_cornermeet_bg_fence_mid"
            xalign 1.
            yalign 1.
            easein 15 xoffset 1000
        contains:
            "day3_cornermeet_bg_fence_near"
            xalign 1.
            yalign 1.
            easein 15 xalign 0.
        contains:
            "romka_hit_face_animation"
            pos (1., 1.)
            anchor (.45, .8)
            easein 15 anchor (1., 1.)

    image flashback_dog_attack:
        contains:
            "locate/street/dog_attack.jpg"
            zoom 0.9
            parallel:
                ease 1.0 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 0.2 xalign 0.7
                ease 0.2 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 1.0 xalign 0.7
                repeat
            parallel:
                ease 0.8 yalign 0.2
                ease 0.8 yalign 0.5
                ease 0.8 yalign 0.3
                ease 0.8 yalign 0.7
                ease 0.2 yalign 0.5
                ease 0.8 yalign 0.2
                repeat
        contains:
            im.Blur("locate/street/dog_attack.jpg", 2.5)
            zoom 0.9
            alpha 0.0
            parallel:
                ease 1.0 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 0.2 xalign 0.7
                ease 0.2 xalign 0.3
                ease 1.0 xalign 0.9
                ease 1.0 xalign 0.5
                ease 1.0 xalign 0.7
                repeat
            parallel:
                ease 0.8 yalign 0.2
                ease 0.8 yalign 0.5
                ease 0.8 yalign 0.3
                ease 0.8 yalign 0.7
                ease 0.2 yalign 0.5
                ease 0.8 yalign 0.2
                repeat
            parallel:
                pause 2.0
                ease 0.2 alpha 0.8
                ease 0.2 alpha 0.0
                repeat

    image day3_dendy_tv_noise:
        "locate/home/in_side/2st_floor/olga_room/TV_01.png"
        .5
        "locate/home/in_side/2st_floor/olga_room/TV_02.png"
        .5
        "locate/home/in_side/2st_floor/olga_room/TV_03.png"
        .5
        "locate/home/in_side/2st_floor/olga_room/TV_04.png"
        .5
        repeat


    define tv_dissolve = Dissolve(.5)

    define tv_fullalpha = .8

    image day3_dendy_tv_frames:
        contains:
            "day3_dendy_tv_noise"

        contains:
            alpha 0

            block:
                "locate/home/in_side/2st_floor/olga_room/TV_05.png"
                linear .5 alpha tv_fullalpha
                1.
                "locate/home/in_side/2st_floor/olga_room/TV_06.png" with tv_dissolve
                1.5
                linear .5 alpha 0

                "locate/home/in_side/2st_floor/olga_room/TV_07.png"
                linear .5 alpha tv_fullalpha
                1.
                "locate/home/in_side/2st_floor/olga_room/TV_08.png" with tv_dissolve
                1.5
                linear .5 alpha 0

                "locate/home/in_side/2st_floor/olga_room/TV_09.png"
                linear .5 alpha tv_fullalpha
                1.
                "locate/home/in_side/2st_floor/olga_room/TV_10.png" with tv_dissolve
                1.5
                linear .5 alpha 0

                repeat

    image day3_dendy_black = "locate/home/in_side/2st_floor/olga_room/TV_12.png"

    image day3_dendy:
        "locate/home/in_side/2st_floor/olga_room/dendy.png"

    image day3_dendy_2:
        "locate/home/in_side/2st_floor/olga_room/dendy02.png"

    image day3_goosedendy_black = "locate/home/in_side/2st_floor/olga_room/TV_16.png"

    image day3_dendy_tv = "locate/home/in_side/2st_floor/olga_room/TV_17.png"

    image day3_dendy_9999:
        contains:
            "locate/home/in_side/2st_floor/olga_room/TV_16.png"

        contains:
            "locate/home/in_side/2st_floor/olga_room/TV_17.png"
            xpos 500

            ypos 0
            yanchor 1.

            yoffset -200

            easeout 2. ypos 850
            easein 1. ypos 550
            easeout 1. ypos 850
            easein .5 ypos 700
            easeout .5 ypos 850
            easein .35 ypos 775
            easeout .35 ypos 850

            .5
            block:
                alpha 0
                .1
                alpha 1
                .1
                repeat 4
            1.
            block:
                alpha 0
                .1
                alpha 1
                .1
                repeat 3

    image day3_dendy_bg noise:
        contains:
            "locate/home/in_side/2st_floor/olga_room/dendy.png"
        contains:
            "day3_dendy_tv_noise"

    image day3_dendy_bg frames:
        contains:
            "locate/home/in_side/2st_floor/olga_room/dendy.png"
        contains:
            "day3_dendy_tv_frames"

    image day3_dendy_anton:
        "locate/home/in_side/2st_floor/olga_room/Athon.png"

    image dendy_tv:
        "locate/home/in_side/2st_floor/olga_room/tvframe.png"

    define gh_bg_dt = 2.
    image goosehunt_select_bg:
        "goosehunt/set/set1.png"
        gh_bg_dt
        "goosehunt/set/set2.png"
        gh_bg_dt
        "goosehunt/set/set3.png"
        gh_bg_dt
        "goosehunt/set/set4.png"
        gh_bg_dt
        "goosehunt/set/set5.png"
        gh_bg_dt
        "goosehunt/set/set6.png"
        gh_bg_dt
        "goosehunt/set/set7.png"
        gh_bg_dt
        "goosehunt/set/set8.png"
        gh_bg_dt
        "goosehunt/set/set9.png"
        gh_bg_dt
        "goosehunt/set/set10.png"
        gh_bg_dt
        repeat

    image goosehunt_select_menu:
        "goosehunt/menu.png"

    image goosehunt_select_noise:
        "locate/home/in_side/2st_floor/olga_room/TV_13.png"
        .05
        "locate/home/in_side/2st_floor/olga_room/TV_14.png"
        .05
        "locate/home/in_side/2st_floor/olga_room/TV_15.png"
        .05
        "locate/home/in_side/2st_floor/olga_room/TV_14.png"
        .05
        "locate/home/in_side/2st_floor/olga_room/TV_13.png"

    image chaika:
        "goosehunt/ch1.png"
        0.5
        "goosehunt/ch2.png"
        0.5
        repeat

    image dendy_controller_1:
        "goosehunt/controller1.png"
    image dendy_controller_2:
        "goosehunt/controller2.png"
    image dendy_controller_3:
        "goosehunt/controller3.png"

    image dendy_controller:
        "dendy_controller_1"
        .25
        block:
            "dendy_controller_1"
            chaika_dt - .25
            "dendy_controller_2"
            .25
            repeat

    image goose_olya_back:
        "goosehunt/Ol.png"

    image goose_olya_gun_ready:
        "goosehunt/Olgun.png"
    image goose_olya_gun_pressed:
        "goosehunt/Olgun2.png"

    image goose_olya_gun:
        ConditionSwitch(
            "renpy.get_screen('flash') is not None", "goose_olya_gun_pressed",
            "True", "goose_olya_gun_ready",
            )

    image goose_olya:
        contains:
            "goose_olya_gun"
            xpos 1450
            xanchor .5
            yanchor 1.
            ypos 1080 + 150
            yoffset 150
            linear .5 yoffset 0
            block:
                ease 1.5 xoffset -5 yoffset 0
                ease 1.5 xoffset 5 yoffset -5
                ease 1.5 xoffset 0 yoffset 5
                ease 1.5 xoffset -5 yoffset 5
                ease 1.5 xoffset 5 yoffset 0
                ease 1.5 xoffset 0 yoffset 0
                repeat
        contains:
            "goose_olya_back"
            xpos 1800
            xanchor .5
            yalign 1.

    image goose_anton_gun_ready:
        "goosehunt/gun1.png"
    image goose_anton_gun_pressed:
        "goosehunt/gun2.png"

    image goose_anton_gun:
        ConditionSwitch(
            "renpy.get_screen('flash') is not None", "goose_anton_gun_pressed",
            "True", "goose_anton_gun_ready",
            )
        block:
            ease 1.5 xoffset -5 yoffset 0
            ease 1.5 xoffset 5 yoffset -5
            ease 1.5 xoffset 0 yoffset 5
            ease 1.5 xoffset -5 yoffset 5
            ease 1.5 xoffset 5 yoffset 0
            ease 1.5 xoffset 0 yoffset 0
            repeat

    image odnoklasnitsa_ant_zerkal:
        xzoom -1
        "locate/school/in_side/Anton_class/2.png"
    image fon_day_03_end = LiveComposite((1920, 1080),
        (0, 0), "locate/school/in_side/Anton_class/fon05.jpg",
        (1250, 0), "odnoklasnitsa_ant_zerkal",
        (455, 0), "locate/school/in_side/Anton_class/1.png",
        )
    image phone_hall2:

        contains:
            "locate/home/in_side/1st_floor/hall/h1/hall.jpg"
            subpixel True
            xalign 1.
            linear 1.15*pca_delay xalign 0.
        contains:
            "locate/home/in_side/1st_floor/hall/H1/Hall2.png"
            subpixel True
            xalign 1.
            linear 1.15*pca_delay xalign 0.
        contains:
            "locate/home/in_side/1st_floor/hall/h1/str.png"
            subpixel True
            xalign 1.
            linear 1.15*pca_delay xalign -1.

    image phone_hall2_02:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/H1/prih_001.png"
    image phone_hall2_down:
        contains:
            "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
        contains:
            "locate/home/in_side/1st_floor/hall/h1/prih_002.png"
            pause .2
            "locate/home/in_side/1st_floor/hall/h1/prih_003.png"
            pause .2
            "locate/home/in_side/1st_floor/hall/h1/prih_002.png"

    image phone_hall_hall:
        "locate/home/in_side/1st_floor/hall/h1/hall.jpg"

    image phone_hall_stair:
        "locate/home/in_side/1st_floor/hall/h1/str.png"

    image phone_hall_anton:
        "sprite/Ant/Anton.png"

    image phone_hall_anton_eyes:
        "sprite/Ant/Anton2.png"

    image day_03_hight_ola_room_01_02:
        "locate/home/in_side/2st_floor/olga_room/VS_01.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/VS_02.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image day_03_hight_ola_room_03_04:
        "locate/home/in_side/2st_floor/olga_room/VS_03.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/VS_04.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image day_03_hight_ola_room_05_06:
        "locate/home/in_side/2st_floor/olga_room/VS_05.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/VS_06.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image day_03_hight_ola_room_07_08:
        "locate/home/in_side/2st_floor/olga_room/VS_07.jpg"
        choice:
            .25




        "locate/home/in_side/2st_floor/olga_room/VS_08.jpg"
        choice:
            .25




        repeat

    image day_03_hight_ola_room_obnim:
        "locate/home/in_side/2st_floor/olga_room/obnim-01.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/obnim-02.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image home_out_side_hight = "locate/home/out_side/hOUSE_night04.jpg"
    image day3_tv_frame = "locate/home/in_side/2st_floor/olga_room/tv/intro_0.png"
    image day3_tv_white = "locate/home/in_side/2st_floor/olga_room/tv/intro_01.jpg"
    image day3_tv_1 = "locate/home/in_side/2st_floor/olga_room/tv/intro_02.jpg"
    image day3_tv_2 = "locate/home/in_side/2st_floor/olga_room/tv/intro_03.jpg"
    image day3_tv_3 = "locate/home/in_side/2st_floor/olga_room/tv/intro_04.jpg"
    image day3_tv_4 = "locate/home/in_side/2st_floor/olga_room/tv/intro_05.jpg"

    image day3_tv_loop:
        "day3_tv_1"
        .05
        "day3_tv_2"
        .05
        "day3_tv_3"
        .05
        "day3_tv_4"
        .05
        repeat

    image day3_candy_meet = "locate/home/out_side/Meet.jpg"

    image day3_candy_frame = "locate/home/out_side/Meet_beasts/frame.png"

    image day3_ant_clas_anton 1 = "locate/school/in_side/Anton_class/Anton_01.png"
    image day3_ant_clas_anton 2 = "locate/school/in_side/Anton_class/Anton_02.png"
    image day3_ant_clas_anton 3 = "locate/school/in_side/Anton_class/Anton_03.png"
    image day3_ant_clas_shadow 1 = "locate/school/in_side/Anton_class/shadow01.png"
    image day3_ant_clas_shadow 2 = "locate/school/in_side/Anton_class/shadow02.png"

    image day3_ant_clas_romka = "locate/school/in_side/Anton_class/Romka_01.png"
    image day3_ant_clas_polina = "locate/school/in_side/Anton_class/Polina_01.png"

    image day3_end_class_bg = "locate/school/in_side/Anton_class/KaitMiss_fon.jpg"
    image day3_end_class_miss = "locate/school/in_side/Anton_class/miss.jpg"
    image Kate_end_start = "locate/school/in_side/Anton_class/Katiamiss.jpg"
    image Kate_end_start_solo = "locate/school/in_side/Anton_class/Katiamiss_solo.jpg"
    image Kate_end = "locate/school/in_side/Anton_class/KaitMiss02.jpg"
    image Kate_end_solo = "locate/school/in_side/Anton_class/KaitMiss02_solo.jpg"

    image day3_ant_room_shtora = "locate/home/in_side/2st_floor/anton_room/shtora/Shtora_04.jpg"

    image day3_window_bg_blur_0 = "locate/home/in_side/2st_floor/anton_room/window_par/00.jpg"
    image day3_window_bg_blur_1 = "locate/home/in_side/2st_floor/anton_room/window_par/0003.png"

    image day3_window_bg_0 = "locate/home/in_side/2st_floor/anton_room/window_par/000.jpg"
    image day3_window_bg_1 = "locate/home/in_side/2st_floor/anton_room/window_par/0004.png"

    image day3_window_frame = "locate/home/in_side/2st_floor/anton_room/window_par/0000.png"
    image day3_window_frame_blur = "locate/home/in_side/2st_floor/anton_room/window_par/0001.png"

    image day3_window_anton = "locate/home/in_side/2st_floor/anton_room/window_par/A01.png"
    image day3_window_anton_blur = "locate/home/in_side/2st_floor/anton_room/window_par/A00.png"

    image mask_01_up:
        "mask_01"
        xalign 0.5
        xpos 960
        ypos 1000+ 1450
        alpha 0.90
        zoom 0.90
        linear 0.1
        parallel:
            linear 2. alpha 1 zoom 1 ypos 0 + 1450
        parallel:
            linear 0.2 xpos 960
            linear 0.2 xpos 960
            linear 0.2 xpos 957
            linear 0.2 xpos 955
            linear 0.2 xpos 955
            linear 0.2 xpos 955
            linear 0.2 xpos 957
            linear 0.2 xpos 957
            linear 0.2 xpos 960
            linear 0.2 xpos 960
        linear 0.2 ypos -100+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -175+ 1450 alpha 1.00 zoom 1.00 xpos 957
        linear 0.2 ypos -250+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -300+ 1450 alpha 1.00 zoom 1.00 xpos 957
        linear 0.2 ypos -325+ 1450 alpha 1.00 zoom 1.00 xpos 955
        linear 0.2 ypos -350+ 1450 alpha 1.00 zoom 1.00 xpos 955
        block:
            linear 1.0 xpos 955 yoffset 10
            linear 1.0 xpos 957 yoffset 5
            linear 1.0 xpos 960 yoffset 0
            linear 1.0 xpos 962 yoffset 5
            linear 1.0 xpos 954 yoffset 0
            linear 1.0 xpos 960 yoffset 5
            repeat

    image hand_zero = "locate/school/in_side/classroom/Zero.png"

    image d3_shadow_bunny:
        "locate/home/in_side/2st_floor/olga_room/OvsA1.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        "locate/home/in_side/2st_floor/olga_room/OvsA2.jpg"
        choice:
            .5
        choice:
            .8
        choice:
            1.
        repeat

    image bg_storage_in_table_day_3_evn_01 = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table6.jpg"
    image bg_storage_in_table_day_3_evn_02 = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table5.jpg"
    image pechatka_day_3_evn = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table00.png"
    image item_in_table_glove_day_3_evn = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table07.png"
    image item_in_table_number_day_3_evn = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table06.png"
    image item_in_table_record_day_3_evn = "locate/home/in_side/2st_floor/anton_room/table_evn/slot/table08.png"
    image anim_byash_oko:
        "sprite/Byasha/Doubt/m_day_winter/2_eyes/normal/ahead/01.png"
        pause 1.1
        "sprite/Byasha/Doubt/m_day_winter/2_eyes/normal/ahead/02.png"
        pause .1
        "sprite/Byasha/Doubt/m_day_winter/2_eyes/normal/ahead/03.png"
        pause .1
        "sprite/Byasha/Doubt/m_day_winter/2_eyes/normal/ahead/02.png"
        pause .1
        "sprite/Byasha/Doubt/m_day_winter/2_eyes/normal/ahead/01.png"
        pause 7
        repeat
    image byasha_rot_07_fg = LiveComposite((2299, 1080),
        (0,0), "sprite/Byasha/Doubt/m_day_winter/1_body/01.png",
        (0,0), "anim_byash_oko",
        (0,0), "sprite/Byasha/Doubt/m_day_winter/3_mouth/01.png",
        )
    image empty_desk_sem = "locate/school/in_side/classroom/desk2.png"
    image empty_desk_sem2 = "locate/school/in_side/classroom/desk1.png"
    image korsar_box = "locate/school/in_side/classroom/Korsar.png"
    image classroom_chair = "locate/school/in_side/classroom/chair .png"

    image bg_classroom base 3 1 box:
        contains:
            "bg_classroom base 3 1"
        contains:
            "korsar_box"

    define owl_dt = 0.1
    image owl_jump:
        "owl_jump/001.png"
        owl_dt * 2
        "owl_jump/002.png"
        owl_dt
        "owl_jump/003.png"
        owl_dt
        "owl_jump/004.png"
        owl_dt
        "owl_jump/005.png"
        owl_dt
        "owl_jump/006.png"
        owl_dt
        "owl_jump/007.png"
        owl_dt
        "owl_jump/008.png"

    image owl_land:
        "owl_jump/001.png"
        owl_dt * 2
        owl_Normal
        1.
        parallel:
            linear .5 xoffset 50
        parallel:
            .25
            linear .25 alpha 0
        xoffset owl_xoffset -50
        linear .5 xoffset owl_xoffset alpha 1

    image doc_no_open = LiveComposite((1920, 1080),
        (0,0), "minigame/case/guard_alert_bg.jpg",
        (0,0), "minigame/case/Tihonov.png",
        )
    image banda_mini = "locate/school/in_side/school_hall/RB.png"

    image scare_bg = "locate/home/out_side/Meet_beasts/FonH.jpg"
    image scare_fence = "locate/home/out_side/Meet_beasts/HH.png"

    image scare_bg_fence:
        contains:
            "scare_bg"
            subpixel True
            xalign 0.
            linear 1.5 xalign 1.
        contains:
            "scare_fence"
            subpixel True
            xalign 0.
            linear 1.5 xalign 1.

    image scare_runaway:
        "scare_bg_fence"
        pause 1.5
        Solid("#000")
        "runaway_night" with Dissolve(.5)
    image teacher_OR:
        "locate/school/out_side/school_coner/Help.jpg"

    image d3_myth = "locate/school/out_side/school_coner/bear.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
