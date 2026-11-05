
init -10:
    $ chinese_font = "font/chinese.ttf"
    $ other_font_interface = "font/razor_k.ttf"
    $ other_font_text = "font/russia.ttf"

translate chinese style default:
    font chinese_font

translate chinese style button_text:
    font chinese_font

translate chinese style gui_text:
    font chinese_font

translate chinese style quick_button_text:
    font chinese_font

translate chinese style quick_text:
    font chinese_font

translate chinese style pref_text:
    font chinese_font

translate chinese style say_dialogue:
    font chinese_font
    size 38

translate chinese style say_label:
    font chinese_font
    size 46
    ypos -25

translate chinese style confirm_prompt_text:
    font chinese_font
    size 46

translate chinese style confirm_textbutton:
    font chinese_font

translate chinese style confirm_button_text:
    font chinese_font

translate chinese style about_text:
    font chinese_font
    size 32

translate chinese style text_font_interface:
    font chinese_font

translate chinese style imagemap_text:
    font chinese_font
    size 46

translate chinese style history_name_text:
    font chinese_font
    size 46

translate chinese style history_text:
    font chinese_font
    size 40

translate chinese style text_dict:
    font chinese_font




translate None style default:
    properties gui.text_properties()
    font other_font_text

translate None style button_text:
    properties gui.text_properties("button")
    yalign 0.5
    font other_font_interface

translate None style gui_text:
    properties gui.text_properties("interface")
    font other_font_interface

translate None style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font other_font_interface

translate None style quick_text:
    properties gui.text_properties("quick_text")
    font other_font_interface

translate None style pref_text:
    font other_font_interface
    color "FFFFFF"
    size 35

translate None style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1
    font other_font_text
    size 60

translate None style say_label:
    font other_font_text
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    size 80

translate None style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    font other_font_text
    size 80

translate None style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    size 40
    color "FFFFFF"
    xoffset -10
    font other_font_interface

translate None style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    size 40
    color "000000"
    xoffset -10
    font other_font_interface

translate None style about_text:
    font other_font_interface
    color "FFFFFF"
    size 36

translate None style text_font_interface:

    font other_font_interface

translate None style imagemap_text:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font other_font_text

    size 60

translate None style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font other_font_text
    size 55

translate None style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font other_font_text
    size 50

translate None style text_dict:
    size 40
    font other_font_text




translate italiano style default:
    properties gui.text_properties()
    font other_font_text

translate italiano style button_text:
    properties gui.text_properties("button")
    yalign 0.5
    font other_font_interface

translate italiano style gui_text:
    properties gui.text_properties("interface")
    font other_font_interface

translate italiano style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font other_font_interface

translate italiano style quick_text:
    properties gui.text_properties("quick_text")
    font other_font_interface

translate italiano style pref_text:
    font other_font_interface
    color "FFFFFF"
    size 35

translate italiano style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1
    font other_font_text
    size 60

translate italiano style say_label:
    font other_font_text
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    size 80

translate italiano style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    font other_font_text
    size 80

translate italiano style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    size 40
    color "FFFFFF"
    xoffset -10
    font other_font_interface

translate italiano style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    size 40
    color "000000"
    xoffset -10
    font other_font_interface

translate italiano style about_text:
    font other_font_interface
    color "FFFFFF"
    size 36

translate italiano style text_font_interface:
    font other_font_text


translate italiano style imagemap_text:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font other_font_text

    size 60

translate italiano style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font other_font_text
    size 55

translate italiano style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font other_font_text
    size 50

translate italiano style text_dict:
    size 40
    font other_font_text


translate turkish style default:
    properties gui.text_properties()
    font other_font_text

translate turkish style button_text:
    properties gui.text_properties("button")
    yalign 0.5
    font other_font_interface

translate turkish style gui_text:
    properties gui.text_properties("interface")
    font other_font_interface

translate turkish style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font other_font_interface

translate turkish style quick_text:
    properties gui.text_properties("quick_text")
    font other_font_interface

translate turkish style pref_text:
    font other_font_interface
    color "FFFFFF"
    size 35

translate turkish style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1
    font other_font_text
    size 60

translate turkish style say_label:
    font other_font_text
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    size 80

translate turkish style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    font other_font_text
    size 80

translate turkish style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    size 40
    color "FFFFFF"
    xoffset -10
    font other_font_interface

translate turkish style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    size 40
    color "000000"
    xoffset -10
    font other_font_interface

translate turkish style about_text:
    font other_font_interface
    color "FFFFFF"
    size 36

translate turkish style text_font_interface:
    font other_font_text


translate turkish style imagemap_text:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font other_font_text

    size 60

translate turkish style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font other_font_text
    size 55

translate turkish style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font other_font_text
    size 50

translate turkish style text_dict:
    size 40
    font other_font_text


translate english style default:
    properties gui.text_properties()
    font other_font_text

translate english style button_text:
    properties gui.text_properties("button")
    yalign 0.5
    font other_font_interface

translate english style gui_text:
    properties gui.text_properties("interface")
    font other_font_interface

translate english style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font other_font_interface

translate english style quick_text:
    properties gui.text_properties("quick_text")
    font other_font_interface

translate english style pref_text:
    font other_font_interface
    color "FFFFFF"
    size 35

translate english style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1
    font other_font_text
    size 60

translate english style say_label:
    font other_font_text
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    size 80

translate english style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    font other_font_text
    size 80

translate english style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    size 40
    color "FFFFFF"
    xoffset -10
    font other_font_interface

translate english style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    size 40
    color "000000"
    xoffset -10
    font other_font_interface

translate english style about_text:
    font other_font_interface
    color "FFFFFF"
    size 36

translate english style text_font_interface:
    font other_font_text


translate english style imagemap_text:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font other_font_text

    size 60

translate english style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font other_font_text
    size 55

translate english style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font other_font_text
    size 50

translate english style text_dict:
    size 40
    font other_font_text



init:
    $ japan_font = "font/GenEiAntiqueNv5-M.ttf"

translate japan style default:
    font japan_font

translate japan style button_text:
    font japan_font

translate japan style gui_text:
    font japan_font

translate japan style quick_button_text:
    font japan_font

translate japan style quick_text:
    font japan_font

translate japan style pref_text:
    font japan_font

translate japan style say_dialogue:
    font japan_font
    size 38

translate japan style say_label:
    font japan_font
    size 46
    ypos -25

translate japan style confirm_prompt_text:
    font japan_font
    size 46

translate japan style confirm_textbutton:
    font japan_font

translate japan style confirm_button_text:
    font japan_font

translate japan style about_text:
    font japan_font
    size 32

translate japan style text_font_interface:
    font japan_font

translate japan style imagemap_text:
    font japan_font
    size 46

translate japan style history_name_text:
    font japan_font
    size 46

translate japan style history_text:
    font japan_font
    size 40

translate japan style text_dict:
    font japan_font
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
