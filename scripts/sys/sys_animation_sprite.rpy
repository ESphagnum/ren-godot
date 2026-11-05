transform sprite_scare:
    yoffset 0
    linear 0.1 yoffset 20
    linear 0.1 yoffset 0

transform sprite_happy:
    yoffset 0
    linear 0.2 yoffset 30
    linear 0.2 yoffset 0

transform sprite_ha:
    yoffset 0
    linear 0.1 yoffset 30
    linear 0.1 yoffset 0

transform sprite_happy_2times:
    yoffset 0
    linear 0.2 yoffset 30
    linear 0.2 yoffset 0
    linear 0.2
    linear 0.2 yoffset 30
    linear 0.2 yoffset 0

transform sprite_happy_alltimes:
    yoffset 0
    block:
        linear 0.1 yoffset 15
        linear 0.1 yoffset 0
        linear 0.1
        repeat

transform sprite_fear:
    yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 2.55
    repeat
transform sprite_fear_speed:
    yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.05 yoffset 2 xoffset 2
    linear 0.05 yoffset 0 xoffset 0
    linear 0.55
    repeat


transform for_tv_1:
    parallel:
        xoffset 0
        linear 0.9
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0
        linear 3.3
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0
        linear 5.9
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0
        linear 2.3
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0
        linear 7.3
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0
        repeat
    parallel:
        yoffset 0
        linear 1.0
        linear 0.05 yoffset -5
        linear 0.05 yoffset 2
        linear 0.05 yoffset 0
        linear 0.05 yoffset -2
        linear 0.05 yoffset 5
        linear 0.05 yoffset 0
        linear 5.0
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
