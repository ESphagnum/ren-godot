label demo_end:
    stop sound fadeout 5.0
    stop fon fadeout 5.0
    stop music fadeout 5.0
    stop music2 fadeout 5.0

    scene bg_black with Dissolve(0.2)

    call screen end_demo

    return

screen end_demo():

    add "interface/demo_end/bye3.png" at mm_elements

    vbox:
        xalign 0.5
        yalign 0.35
        text _("Спасибо, вы прошли третий эпизод визуальной новеллы «Зайчик».\nИскренне благодарим вас за то, что приобрели игру на раннем этапе разработки.\nВсе собранные средства будут направлены на продолжение игры."):
            xalign 0.5
            yalign 0.5
            size 55
            text_align 0.5
        at mm_elements

    use block_screen

    hbox:
        xalign 0.485
        yalign 0.9
        spacing 115
        imagebutton idle "interface/demo_end/icon_01.png":
            action OpenURL('https://bunny-horror.tumblr.com/')
            hover_sound "sounds/menu/menu-button-select-3.ogg"
            activate_sound "sounds/menu/language-sellect-1.ogg"
            at mm_but_lang
        imagebutton idle "interface/demo_end/icon_02.png":
            action OpenURL('https://twitter.com/TinyBunnyVN')
            hover_sound "sounds/menu/menu-button-select-3.ogg"
            activate_sound "sounds/menu/language-sellect-1.ogg"
            at mm_but_lang
        imagebutton idle "interface/demo_end/icon_03.png":
            action OpenURL('https://store.steampowered.com/app/1421250/TINY_BUNNY/')
            hover_sound "sounds/menu/menu-button-select-3.ogg"
            activate_sound "sounds/menu/language-sellect-1.ogg"
            at mm_but_lang
        imagebutton idle "interface/demo_end/icon_04.png":
            action OpenURL('https://vk.com/bunnyhorror')
            hover_sound "sounds/menu/menu-button-select-3.ogg"
            activate_sound "sounds/menu/language-sellect-1.ogg"
            at mm_but_lang
        at mm_elements

    button:
        pos 1673, 621
        xysize (438, 86)
        xanchor 1.
        action Jump("d4_begin")

        background "interface/button.png"

        text _("Начать четвертый эпизод"):
            align (.4, .5)
            size 50
            color "#000"


        at transform:
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
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
