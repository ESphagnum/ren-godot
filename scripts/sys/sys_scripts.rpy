
init -2 python:
















    def Ani_png(img_name, frames, delay=.1, loop=True, reverse=False, effect=None, start=1, ext="png", **properties):
        args = []
        for i in range(start, start + frames):
            args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                args.append(effect)
        if reverse: 
            for i in range(start + frames - 2, start, -1):
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                if loop or (i > start + 1):
                    args.append(delay)
                    args.append(effect)
        return anim.TransitionAnimation(*args, **properties)
    def Ani_jpg(img_name, frames, delay=.1, loop=True, reverse=False, effect=None, start=1, ext="jpg", **properties):
        args = []
        for i in range(start, start + frames):
            args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                args.append(effect)
        if reverse: 
            for i in range(start + frames - 2, start, -1):
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                if loop or (i > start + 1):
                    args.append(delay)
                    args.append(effect)
        return anim.TransitionAnimation(*args, **properties)

    def Ani_jpg2(img_name, frames, delay=0.08, loop=False, reverse=False, effect=None, start=1, ext="jpg", **properties):
        args = []
        for i in range(start, start + frames):
            if i > 9:
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
            else:
                args.append(renpy.display.im.image(img_name + "0" + str(i) + "." + ext))
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                args.append(effect)
        if reverse: 
            for i in range(start + frames - 2, start, -1):
                args.append(renpy.display.im.image(img_name + str(i) + "." + ext))
                if loop or (i > start + 1):
                    args.append(delay)
                    args.append(effect)
        return anim.TransitionAnimation(*args, **properties)

init -2:

    $ dd1 = Dissolve(.5, alpha=True)
    $ dd2 = Dissolve(.1, alpha=True)
    $ dd3 = Dissolve(3.0, alpha=True)
    $ dd4 = Dissolve(0.05, alpha=True)



init 800 python:
    class MouseParallaxX(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<0):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(transX)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                self.xoffset=((float)(x)/(config.screen_width))-0.5
            
            return

    class MouseParallaxY(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<0):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(transY)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                
                self.yoffset=((float)(y)/(config.screen_height))-0.5
            return

    MouseParallaxX([(-1250,"par_bg_x"),(-1600,"par_middle_x"),(-2000,"par_forward_x")]) 
    MouseParallaxY([(-1250,"par_bg_y"),(-1600,"par_middle_y"),(-2000,"par_forward_y")]) 

    def transX(d, st, at, disp=None, m=None):
        d.xoffset = int(round(m*disp.xoffset))
        
        return 0

    def transY(d, st, at, disp=None, m=None):
        
        d.yoffset = int(round(m*disp.yoffset))
        return 0



init -1:
    transform old_eyes:
        alpha 1.0
        linear 2.0
        alpha 0.0
    transform dark_eyes:
        alpha 1.0
        linear 2.0 alpha 0.0

init -1 python:
    sprites_dir = 'sprite'

    dark_list = [
    ("15", Solid("#0002")),
    ("30", Solid("#0004")),
    ("40", Solid("#0006")),
    ("50", Solid("#0008")),
    ("60", Solid("#000a")),
    ("70", Solid("#000b")),
    ("90", Solid("#000c")),
    ("100", Solid("#000f")),
]
    generate_dark_version = False

    def generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur=None, delay=0.0):
        random_blink_init_delay = renpy.random.random()*8.0
        random_blink_delay = renpy.random.random()*3.0 + 6.0
        if eyes_type == 'ahead_to_aside':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '02.png'
            ani3 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '03.png'
            ani4 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '02.png'
            ani5 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '01.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), 0.0, im.Blur(ani2,1.5), 0.1, im.Blur(ani3,1.5), 0.1, im.Blur(ani4,1.5), 0.1, im.Blur(ani5,1.5), random_blink_delay+delay), old_eyes)
            else:
                return At(Animation(ani1, 0.0, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, random_blink_delay+delay), old_eyes)
        elif eyes_type == 'aside_to_ahead':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '02.png'
            ani3 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '03.png'
            ani4 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '02.png'
            ani5 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '01.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), 0.0, im.Blur(ani2,1.5), 0.1, im.Blur(ani3,1.5), 0.1, im.Blur(ani4,1.5), 0.1, im.Blur(ani5,1.5), random_blink_delay+delay), old_eyes)
            else:
                return At(Animation(ani1, 0.0, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, random_blink_delay+delay), old_eyes)
        if eyes_type == 'ahead_shock':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '04.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), 0.1, im.Blur(ani2,1.5), 0.1), old_eyes)
            else:
                return At(Animation(ani1, 0.1, ani2, 0.1), old_eyes)
        if eyes_type == 'aside_shock':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '04.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), 0.1, im.Blur(ani2,1.5), 0.1), old_eyes)
            else:
                return At(Animation(ani1, 0.1, ani2, 0.1), old_eyes)
        elif eyes_type == 'dark':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '01.png'
            if blur:
                return Image(im.Blur(ani1,1.5))
            else:
                return Image(ani1)
        elif eyes_type == 'dark_to_ahead':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'dark' + '/' + '01.png'
            if blur:
                return At(Image(im.Blur(ani1,1.5)), dark_eyes)
            else:
                return At(Image(ani1), dark_eyes)
        elif eyes_type == 'dark_to_aside':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'dark' + '/' + '01.png'
            if blur:
                return At(Image(im.Blur(ani1,1.5)), dark_eyes)
            else:
                return At(Image(ani1), dark_eyes)
        elif eyes_type == 'aside_to_dark':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '02.png'
            ani3 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '03.png'
            ani4 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '02.png'
            ani5 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'aside' + '/' + '01.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), random_blink_init_delay, im.Blur(ani2,1.5), 0.1, im.Blur(ani3,1.5), 0.1, im.Blur(ani4,1.5), 0.1, im.Blur(ani5,1.5), random_blink_delay+delay), dark_eyes)
            else:
                return At(Animation(ani1, random_blink_init_delay, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, random_blink_delay+delay), dark_eyes)
        elif eyes_type == 'ahead_to_dark':
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '02.png'
            ani3 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '03.png'
            ani4 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '02.png'
            ani5 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + 'ahead' + '/' + '01.png'
            if blur:
                return At(Animation(im.Blur(ani1,1.5), random_blink_init_delay, im.Blur(ani2,1.5), 0.1, im.Blur(ani3,1.5), 0.1, im.Blur(ani4,1.5), 0.1, im.Blur(ani5,1.5), random_blink_delay+delay), dark_eyes)
            else:
                return At(Animation(ani1, random_blink_init_delay, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, random_blink_delay+delay), dark_eyes)
        else:
            ani1 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '01.png'
            ani2 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '02.png'
            ani3 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '03.png'
            ani4 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '02.png'
            ani5 = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '2_eyes' + '/' + view_dir2 + '/' + eyes_type + '/' + '01.png'
            if npc_dir == 'Romka':
                return Animation(ani1, 1.1, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, 7.5+delay)
            elif npc_dir == 'Byasha':
                return Animation(ani1, 0.7, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, 6.0+delay)
            else:
                if blur:
                    return Animation(im.Blur(ani1,1.5), random_blink_init_delay, im.Blur(ani2,1.5), 0.1, im.Blur(ani3,1.5), 0.1, im.Blur(ani4,1.5), 0.1, im.Blur(ani5,1.5), random_blink_delay+delay)
                else:
                    return Animation(ani1, random_blink_init_delay, ani2, 0.1, ani3, 0.1, ani4, 0.1, ani5, random_blink_delay+delay)

    def generate_char(npc_dir, emotion_dir, view_dir, body_type, view_dir2=None, eyes_type=None, mouth_type=None, drop_type=None, blur=None, size=(1920, 1080), eyes_size=(1920, 1080), blink_delay=0.0):
        comp_list = []
        
        comp_list.append((0, 0))
        body_part = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '1_body' + '/' + body_type + '.png'
        if blur:
            comp_list.append(im.Blur(body_part, 1.5))
        else:
            comp_list.append(body_part)
        
        if eyes_type != None:
            if eyes_type == 'ahead_to_aside':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'aside', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            elif eyes_type == 'aside_to_ahead':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'ahead', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            elif eyes_type == 'aside_to_dark':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'dark', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            elif eyes_type == 'ahead_to_dark':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'dark', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            elif eyes_type == 'dark_to_aside':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'aside', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            elif eyes_type == 'dark_to_ahead':
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, 'ahead', blur, delay=blink_delay)
                comp_list.append(eyes_part)
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
            else:
                comp_list.append((0, size[1] - eyes_size[1]))
                eyes_part = generate_eyes(npc_dir, emotion_dir, view_dir, view_dir2, eyes_type, blur, delay=blink_delay)
                comp_list.append(eyes_part)
        
        if mouth_type != None:
            comp_list.append((0, 0))
            mouth_part = sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '3_mouth' + '/' + mouth_type + '.png'
            if blur:
                comp_list.append(im.Blur(mouth_part, 1.5))
            else:
                comp_list.append(mouth_part)
        
        if drop_type != None:
            comp_list.append((0, 0))
            drop_part = Animation(
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '01.png', 1.5,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '02.png', 0.1,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '03.png', 0.1,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '04.png', 0.1,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '05.png', 0.1,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '06.png', 0.1,
            sprites_dir + '/' + npc_dir + '/' + emotion_dir + '/' + view_dir + '/' + '4_drop' + '/' + '01.png', 6.0)
            if blur:
                comp_list.append(im.Blur(drop_part, 1.5))
            else:
                comp_list.append(drop_part)
        
        return Composite(size,
        *comp_list)

    def generate_img(npc_dir, emotion_dir, view_dir, body_type, view_dir2=None, eyes_type=None, mouth_type=None, drop_type=None, blur=None, size=(1920, 1080), eyes_size=(1920, 1080), blink_delay=0.0):
        temp_string = npc_dir + ' ' + emotion_dir + ' ' + view_dir + ' ' + body_type
        if eyes_type:
            temp_string += ' ' + view_dir2 + ' ' + eyes_type
        if mouth_type:
            temp_string += ' ' + mouth_type
        if blur:
            temp_string += ' ' + blur
        
        char = generate_char(npc_dir, emotion_dir, view_dir, body_type, view_dir2, eyes_type, mouth_type, drop_type, blur, size, eyes_size, blink_delay)
        renpy.image(temp_string, char)
        
        if generate_dark_version:
            
            for value, disp in dark_list:
                _temp_string = temp_string + ' dark ' + value
                dark_char = AlphaMask(disp, char)
                renpy.image(_temp_string, Composite(size, (0, 0), char, (0, 0), dark_char))









    def generate_wekup():
        comp_list = []
        
        for i in range(47):
            if i < 9:
                img_part = 'locate/home/in_side/2st_floor/anton_room/wekup/wekup_0' + '0' + str(i + 1) + '.jpg'
            else:
                img_part = 'locate/home/in_side/2st_floor/anton_room/wekup/wekup_0' + str(i + 1) + '.jpg'
            comp_list.append(img_part)
            comp_list.append(0.08)
        
        return Animation(
        *comp_list)

    renpy.image('Ant_wakeup2', generate_wekup())


    def stop_music(channel='music', fadeout=3.0):
        renpy.music.set_volume(0.0, delay=fadeout, channel='music')

    def play_music(channel='music', fadein=3.0):
        renpy.music.set_volume(1.0, delay=fadein, channel='music')


    def parallax_walking(arr):
        renpy.show(Image(At(arr[0][0], parr_walking1)))
        renpy.show(Image(At(arr[0][0], parr_walking2)))





init:
    transform parr_walking1(sp=20, xs=3840):
        block:
            xpos 0
            linear sp xpos (xs-1)//2
            linear sp xpos (xs-1)
            xpos (-xs)
            linear sp xpos (-xs)//2
            linear sp xpos 0
            repeat

    transform parr_walking2(sp=20, xs=3840):
        block:
            xpos (-xs)
            linear sp xpos (-xs)//2
            linear sp xpos 0
            xpos 0
            linear sp xpos (xs-1)//2
            linear sp xpos (xs-1)
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
