













transform AnimatedAberate:
    shader "MakeVisualNovels.AnimatedAberration"
    u_aberrationAmount (10.0)

transform StillAberate:
    shader "MakeVisualNovels.StillAberration"
    u_aberrationAmount (10.0)

transform IntenseAberate:
    shader "MakeVisualNovels.StillAberration"
    u_aberrationAmount (50.0)

transform bits16:
    shader "MakeVisualNovels.256colors"

transform bits8:
    shader "MakeVisualNovels.16colors"

transform VHS:
    shader "MakeVisualNovels.VHS"





    u_color (1.0, 1.0, 1.0, 1.0)

transform WhiteNoise:
    shader "MakeVisualNovels.Static"

    u_color (1.0, 1.0, 1.0, 1.0)
    u_intensity (3)




    u_mode (0)

transform WhiteNoise2:
    shader "MakeVisualNovels.Static"

    u_color (1.0, 1.0, 1.0, 1.0)
    u_intensity (1)




    u_mode (0)

transform Static:
    shader "MakeVisualNovels.Static"

    u_color (1.0, 1.0, 1.0, 1.0)
    u_intensity (1)




    u_mode (1)






transform TransRights:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 1.0, 1.0)
    u_key_light_color (0, 0, 1.0)
    u_fill_light_color (0, 0.25, 0.2)
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.0, -0.5)
    u_key_light_position (0.45, 0.2)
    u_key_light_radius (0.5)
    u_fill_light_direction (-1.0, 0.0)
    u_back_light_intensity (2)
    u_key_light_intensity (1)
    u_fill_light_intensity (-0.7)





transform Bisexuality:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 0.0, 1.0)
    u_key_light_color (0.7, 0.7, 1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.0, -0.5)
    u_key_light_position (0.2, 0.2)
    u_key_light_radius (1.0)
    u_fill_light_direction (-1.0, 0.0)
    u_back_light_intensity (1)
    u_key_light_intensity (0.7)
    u_fill_light_intensity (-0.5)



transform SunsetLighting:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (0.9, 0.7, 0.4)
    u_key_light_color (0.0, 0.0, 0.5)
    u_fill_light_color (0.4, 0.9, 0.9)
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.25, -0.5)
    u_key_light_position (0.45, 0.2)
    u_key_light_radius (0.8)
    u_fill_light_direction (-1.0, 0.0)
    u_back_light_intensity (4)
    u_key_light_intensity (0.4)
    u_fill_light_intensity (-0.5)



transform SimulatedLighting:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 1.0, 1.0)
    u_key_light_color (1.0, 1.0, 1.0)
    u_fill_light_color (1, 1, 1)
    u_back_light_direction (1.5, -0.5)

    u_back_light_position (0.25, -0.5)


    u_key_light_position (0.45, 0.2)
    u_key_light_radius (0.8)
    u_fill_light_direction (-1.0, 0.0)
    u_back_light_intensity (1)
    u_key_light_intensity (0.5)

    u_fill_light_intensity (-0.5)


transform Regicide:
    shader "MakeVisualNovels.PerlinWarp"


    u_fps (6.0)


    u_minSmooth (0.0)
    u_maxSmooth (0.5)
    u_warpIntensity (2.0)
    u_speed (1.15)
    u_scale (10)


    u_flipIntensity (5.0)
    u_flipSpeed (2.0)
    u_flipScale (100)






transform VirtualBoy:

    shader "MakeVisualNovels.Manga"
    u_color (0.7, 0.1, 0.1, 1.0)

    u_intensity (0.6)

transform Manga:
    shader "MakeVisualNovels.Manga"

    u_color (0.0,0.0,0.0,0.0)

    u_intensity (0.6)

transform TakeOnMe:
    shader "MakeVisualNovels.TakeOnMe"

    u_color (1.0,1.0,1.0,1.0)
    u_intensity (0.6)


    u_fps (6.0)


    u_minSmooth (0.0)
    u_maxSmooth (0.5)
    u_warpIntensity (2.0)
    u_speed (1.15)
    u_scale (5)


    u_flipIntensity (5.0)
    u_flipSpeed (0.15)
    u_flipScale (10)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
