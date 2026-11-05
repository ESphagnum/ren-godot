
label demo4_end:
    stop sound fadeout 5.0
    stop fon fadeout 5.0
    stop music fadeout 5.0
    stop music2 fadeout 5.0



    scene bg_black with Dissolve(.5)

    call screen end4_demo

    return

screen end4_demo():

    if Flags.Has("agree"):
        add "interface/demo_end/death4.png" at mm_elements
    else:
        add "interface/demo_end/death3.png" at mm_elements

    vbox:
        xalign 0.5
        yalign 0.35
        text _("Спасибо, вы прошли четвертый эпизод визуальной новеллы «Зайчик».\nИскренне благодарим вас за то, что приобрели игру на раннем этапе разработки.\nВсе собранные средства будут направлены на продолжение игры."):
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

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at mm_elements

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            at filepic_but3
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
