
define photorobot_sfx_finish = "sounds/sfx_photorobot_listing_short_3.ogg"


define photorobot_sfx_arrow_list = [
    "sounds/Fotorobot/sfx_photorobot_drawing_short_1.ogg",
    "sounds/Fotorobot/sfx_photorobot_drawing_short_2.ogg",
    "sounds/Fotorobot/sfx_photorobot_drawing_short_3.ogg",
    "sounds/Fotorobot/sfx_photorobot_drawing_short_4.ogg",
    ]

screen photorobot:
    modal True
    zorder 0
    add "interface/photorobot/P_01.png"
    add "interface/photorobot/pices.png"


    add face2
    add face1
    add face4
    add face3


screen photorobot_b5:


    vbox:
        xpos 780
        ypos -40

        imagebutton:
            idle "interface/intercative_button.png"
            focus_mask True
            action [Hide('photorobot_b5'), Return()]

            if photorobot_sfx_finish:
                hover_sound photorobot_sfx_finish


            at transform:
                on hover:
                    alpha .8
                on idle:
                    alpha .0
    vbox:
        xalign 0.5
        ypos 54
        xsize 250
        ysize 50
        text _("ОТДАТЬ"):
            size 50
            style "imagemap_text"
            color "#000000"
            outlines [ (absolute(1), "#FFFFFF", absolute(0), absolute(0)) ]

screen photorobot_b1_1:
    button:
        background "interface/photorobot/strelkaL.png"
        xsize 100
        ysize 151
        xpos 100
        ypos 200
        action [Hide('photorobot_b1_1'), Show('photorobot_b1_1'), Function(change_face_img,1,"prev"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b1_2:
    button:
        background "interface/photorobot/strelkaR.png"
        xsize 100
        ysize 151
        xpos 535
        ypos 200
        action [Hide('photorobot_b1_2'), Show('photorobot_b1_2'), Function(change_face_img,1,"next"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b2_1:
    button:
        background "interface/photorobot/strelkaL.png"
        xsize 100
        ysize 151
        xpos 100
        ypos 595
        action [Hide('photorobot_b2_1'), Show('photorobot_b2_1'), Function(change_face_img,2,"prev"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b2_2:
    button:
        background "interface/photorobot/strelkaR.png"
        xsize 100
        ysize 151
        xpos 535
        ypos 595
        action [Hide('photorobot_b2_2'), Show('photorobot_b2_2'), Function(change_face_img,2,"next"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b3_1:
    button:
        background "interface/photorobot/strelkaL.png"
        xsize 100
        ysize 151
        xpos 100 + 1240
        ypos 200
        action [Hide('photorobot_b3_1'), Show('photorobot_b3_1'), Function(change_face_img,0,"prev"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b3_2:
    button:
        background "interface/photorobot/strelkaR.png"
        xsize 100
        ysize 151
        xpos 535 + 1240
        ypos 200
        action [Hide('photorobot_b3_2'), Show('photorobot_b3_2'), Function(change_face_img,0,"next"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b4_1:
    button:
        background "interface/photorobot/strelkaL.png"
        xsize 100
        ysize 151
        xpos 100 + 1240
        ypos 595
        action [Hide('photorobot_b4_1'), Show('photorobot_b4_1'), Function(change_face_img,3,"prev"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

screen photorobot_b4_2:
    button:
        background "interface/photorobot/strelkaR.png"
        xsize 100
        ysize 151
        xpos 535 + 1240
        ypos 595
        action [Hide('photorobot_b4_2'), Show('photorobot_b4_2'), Function(change_face_img,3,"next"), Function(random_list_sound, photorobot_sfx_arrow_list)]
        at button_for_photorobot

init python:
    max_face_img = 7
    photorobot_face = []
    t_face1 = []
    t_face2 = []
    t_face3 = []
    t_face4 = []
    for i in range(max_face_img):
        t_face1.append("interface/photorobot/faces/face1_" + str(i) + ".png")
        t_face2.append("interface/photorobot/faces/face2_" + str(i) + ".png")
        t_face3.append("interface/photorobot/faces/face3_" + str(i) + ".png")
        t_face4.append("interface/photorobot/faces/face4_" + str(i) + ".png")
    photorobot_face.append(t_face1)
    photorobot_face.append(t_face2)
    photorobot_face.append(t_face3)
    photorobot_face.append(t_face4)

    face1 = photorobot_face[0][0]
    face2 = photorobot_face[1][0]
    face3 = photorobot_face[2][0]
    face4 = photorobot_face[3][0]

    def change_face_img(n1,face_act):
        global face1
        global face2
        global face3
        global face4
        global photorobot_face
        n2 = 0
        img = photorobot_face[n1][n2]
        
        if n1 == 0:
            while img != face1:
                n2 += 1
                img = photorobot_face[n1][n2]
        
        elif n1 == 1:
            while img != face2:
                n2 += 1
                img = photorobot_face[n1][n2]
        
        elif n1 == 2:
            while img != face3:
                n2 += 1
                img = photorobot_face[n1][n2]
        
        elif n1 == 3:
            while img != face4:
                n2 += 1
                img = photorobot_face[n1][n2]
        
        if face_act == "next":
            
            if (n1==0 and n2==2) or (n1==1 and n2==3) or (n1==2 and n2==1) or (n1==3 and n2==4):
                
                if is_tapped == "tap" or Flags.Has("witness tapped"):
                    n2 += 1
                    if n2 >= max_face_img:
                        n2 = 1
                else:
                    n2 += 2
                    if n2 >= max_face_img:
                        n2 = 1
            else:
                n2 += 1
                if n2 >= max_face_img:
                    n2 = 1
        
        if face_act == "prev":
            if (n1==0 and n2==4) or (n1==1 and n2==5) or (n1==2 and n2==3) or (n1==3 and n2==6):
                if is_tapped == "tap" or Flags.Has("witness tapped"):
                    n2 -= 1
                    if n2 == 0:
                        n2 = max_face_img - 1
                else:
                    n2 -= 2
                    if n2 == 0:
                        n2 = max_face_img - 2
            else:
                n2 -= 1
                if n2 == 0:
                    n2 = max_face_img - 1
        
        if n1 == 0:
            face1 = photorobot_face[n1][n2]
        elif n1 == 1:
            face2 = photorobot_face[n1][n2]
        elif n1 == 2:
            face3 = photorobot_face[n1][n2]
        elif n1 == 3:
            face4 = photorobot_face[n1][n2]
        
        if "0" not in face1 and "0" not in face2 and "0" not in face3 and "0" not in face4:
            renpy.show_screen('photorobot_b5')

    def start_photorobot_game():
        renpy.show_screen('photorobot')
        renpy.show_screen('photorobot_b1_1')
        renpy.show_screen('photorobot_b1_2')
        renpy.show_screen('photorobot_b2_1')
        renpy.show_screen('photorobot_b2_2')
        renpy.show_screen('photorobot_b3_1')
        renpy.show_screen('photorobot_b3_2')
        renpy.show_screen('photorobot_b4_1')
        renpy.call_screen('photorobot_b4_2')


    def get_foto_numbers():
        return (int(face1[-5]), int(face2[-5]), int(face3[-5]), int(face4[-5]))

init:
    image photorobot = LiveComposite((1920, 1080),
        (0, 0), "bg parta",
        (0, 0), "interface/photorobot/P_01.png")

label end_photorobot_game:
    hide screen photorobot
    hide screen photorobot_b1_1
    hide screen photorobot_b1_2
    hide screen photorobot_b2_1
    hide screen photorobot_b2_2
    hide screen photorobot_b3_1
    hide screen photorobot_b3_2
    hide screen photorobot_b4_1
    hide screen photorobot_b4_2
    scene photorobot
    show expression face1
    show expression face2
    show expression face4
    show expression face3
    $ renpy.pause(0.5, hard=True)
    scene photorobot:
        xoffset 0
        yoffset 0
        linear 1.55 zoom 1.5 xoffset -510 yoffset -180
    show expression face1:
        xoffset 0
        yoffset 0
        linear 1.55 zoom 1.5 xoffset -510 yoffset -180
    show expression face2:
        xoffset 0
        yoffset 0
        linear 1.55 zoom 1.5 xoffset -510 yoffset -180
    show expression face4:
        xoffset 0
        yoffset 0
        linear 1.55 zoom 1.5 xoffset -510 yoffset -180
    show expression face3:
        xoffset 0
        yoffset 0
        linear 1.55 zoom 1.5 xoffset -510 yoffset -180
    $ renpy.pause(1.5)


    return

transform button_for_photorobot:
    alpha 0.0
    linear 0.55 alpha 1.0
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
