init:
    $ generate_img('Liliya', 'Normal', 'm_evening', '00')

    image Liliya Base = "sprite/Liliya/Normal/m_evening/1_body/00.png"


transform liliay_income:
    xzoom -1.0
    alpha 0.0
    ypos 0
    xpos 350 - 1000
    linear 0.5 alpha 0.5 xpos 280 - 1000 ypos 20
    linear 0.5 alpha 1.0 xpos 210 - 1000 ypos 0
    linear 0.5 alpha 1.0 xpos 140 - 1000 ypos 20
    linear 0.5 alpha 1.0 xpos 70 - 1000 ypos 0
    linear 0.5 alpha 1.0 xpos 0 - 1000 ypos 20
    linear 0.5 alpha 1.0 xpos -70 - 1000 ypos 0
    linear 0.5 alpha 1.0 xpos -110 - 1000 ypos 20
    linear 0.5 alpha 1.0 xpos -130 - 1000 ypos 0
    linear 0.5
    linear 0.3 alpha 0.0
    xzoom 1.0 xpos -130 - 1000 + 1420
    linear 0.3 alpha 1.0

transform liliay_out:
    xzoom -1.0
    alpha 1.0
    ypos 0
    xpos -130 - 1000
    linear 0.5 alpha 1.00 xpos -150 - 1000 ypos 20
    linear 0.5 alpha 0.75 xpos -200 - 1000 ypos 0
    linear 0.5 alpha 0.50 xpos -260 - 1000 ypos 20
    linear 0.5 alpha 0.00 xpos -340 - 1000 ypos 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
