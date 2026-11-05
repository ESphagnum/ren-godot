

define id_image = "effect/imagedissolve/00.png"


define id_time = 2.0

label image_dissolve_test:


    scene expression "locate/home/in_side/1st_floor/hall/h1/Hall.jpg"


    "Get Ready"


    scene expression "locate/home/in_side/1st_floor/hall/h1/fon_preh.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)

    pause


    scene expression "locate/Death.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)

    pause


    scene expression "locate/grand_mather.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/Death.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/grand_mather.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/Death.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/grand_mather.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/Death.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/grand_mather.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)
    scene expression "locate/Death.jpg"
    with ImageDissolve("effect/imagedissolve/00.png", 1.)



    "Done! Колёсико вверх, чтоб откатиться назад.\nShift+R чтоб применить изменения в коде."

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
