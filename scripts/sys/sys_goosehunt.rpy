define goose_speed_lvl1 = 400
define goose_speed_lvl2 = 600
define goose_speed_lvl3 = 800

define config.mouse["goosehunt_cursor 0"] = [ ("images/interface/empty_cursor.png", 0, 0)]
define config.mouse["goosehunt_cursor 2"] = [ ("images/goosehunt/k2.png", 88, 88)]

default goose_cursor = "goosehunt_cursor 2"

default is_olya_play = False





image goosehunt_splash_1 = "images/goosehunt/alternative/splash/anim1.png"
image goosehunt_splash_2 = "images/goosehunt/alternative/splash/anim2.png"
image goosehunt_splash_3 = "images/goosehunt/alternative/splash/anim3.png"
image goosehunt_splash_4 = "images/goosehunt/alternative/splash/anim4.png"
image goosehunt_splash_5 = "images/goosehunt/alternative/splash/anim5.png"
image goosehunt_splash_6 = "images/goosehunt/alternative/splash/anim6.png"
image goosehunt_splash_7 = "images/goosehunt/alternative/splash/anim7.png"
image goosehunt_splash_8 = "images/goosehunt/alternative/splash/anim8.png"
image goosehunt_splash_9 = "images/goosehunt/alternative/splash/anim9.png"
image goosehunt_splash_10 = "images/goosehunt/alternative/splash/anim10.png"

image goosehunt_splash:
    "goosehunt_splash_1"
    .1
    "goosehunt_splash_2"
    .1
    "goosehunt_splash_3"
    .1
    "goosehunt_splash_4"
    .1
    "goosehunt_splash_5"
    .1
    "goosehunt_splash_6"
    .1
    "goosehunt_splash_7"
    .1
    "goosehunt_splash_8"
    .1
    "goosehunt_splash_9"
    .1
    "goosehunt_splash_10"
    .1
    Null()

image goosehunt_waves_1 = "images/goosehunt/alternative/background/W_1.png"
image goosehunt_waves_2 = "images/goosehunt/alternative/background/W_2.png"

image goosehunt_waves:
    "goosehunt_waves_1"
    .5
    "goosehunt_waves_2"
    .5
    repeat

image goosehunt_waves_1_crop:
    im.Crop("images/goosehunt/alternative/background/W_1.png", (0, goosegame_behind_bush, 1134, 960 - goosegame_behind_bush))

image goosehunt_waves_2_crop:
    im.Crop("images/goosehunt/alternative/background/W_2.png", (0, goosegame_behind_bush, 1134, 960 - goosegame_behind_bush))

image goosehunt_waves_crop:
    "goosehunt_waves_1_crop"
    .5
    "goosehunt_waves_2_crop"
    .5
    repeat


image goosehunt_bg_l1 = "images/goosehunt/alternative/background/L_1.png"
image goosehunt_bg_l2 = "images/goosehunt/alternative/background/L_2.png"

image goosehunt_bg_base:
    contains:
        "goosehunt_bg_l1"
    contains:
        "goosehunt_waves"
    contains:
        "goosehunt_bg_l2"

image goosehunt_bg_l1_crop:
    im.Crop("images/goosehunt/alternative/background/L_1.png", (0, goosegame_behind_bush, 1134, 960 - goosegame_behind_bush))

image goosehunt_bg_l2_crop:
    im.Crop("images/goosehunt/alternative/background/L_2.png", (0, goosegame_behind_bush, 1134, 960 - goosegame_behind_bush))

image goosehunt_bg_base_crop:
    contains:
        "goosehunt_bg_l1_crop"
    contains:
        "goosehunt_waves_crop"
    contains:
        "goosehunt_bg_l2_crop"

image goosehunt_bg:
    "goosehunt_bg_base"
    xpos goosegame_xoffset
    ypos goosegame_yoffset
    anchor (0, 0)

image goosehunt_fg:
    "goosehunt_bg_base_crop"
    xpos goosegame_xoffset
    ypos goosegame_yoffset + goosegame_behind_bush
    anchor (0, 0)

image goosehunt_null:
    "goosehunt/null.png"
    xpos goosegame_xoffset
    ypos goosegame_yoffset
    anchor (0, 0)

image goosehunt_tv:
    "goosehunt/tvframe.png"

image goose1 = "goosehunt/alternative/seagull/1(1)_seagull.png"
image goose2 = "goosehunt/alternative/seagull/1(2)_seagull.png"
image goose3 = "goosehunt/alternative/seagull/1(3)_seagull.png"
image goose4 = "goosehunt/alternative/seagull/2(1)_seagull.png"
image goose5 = "goosehunt/alternative/seagull/2(2)_seagull.png"
image goose6 = "goosehunt/alternative/seagull/2(3)_seagull.png"
image goose7 = "goosehunt/alternative/seagull/3(1)_seagull.png"
image goose8 = "goosehunt/alternative/seagull/3(2)_seagull.png"
image goose9 = "goosehunt/alternative/seagull/3(3)_seagull.png"
image goose10 = "goosehunt/alternative/seagull/4_seagull.png"
image goose11 = "goosehunt/alternative/seagull/5_seagull.png"

define goose_right_1_stock = [
    ("goose1", 4),
    ("goose2", 4),
    ("goose3", 4),
    ]

define goose_right_2_stock = [
    ("goose4", 4),
    ("goose5", 4),
    ("goose6", 4),
    ]

define goose_top_stock = [
    ("goose7", 4),
    ("goose8", 4),
    ("goose9", 4),
    ]

image goose1_left:
    "goose1"
    xzoom -1
image goose2_left:
    "goose2"
    xzoom -1
image goose3_left:
    "goose3"
    xzoom -1
define goose_left_1_stock = [
    ("goose1_left", 4),
    ("goose2_left", 4),
    ("goose3_left", 4),
    ]

image goose4_left:
    "goose4"
    xzoom -1
image goose5_left:
    "goose5"
    xzoom -1
image goose6_left:
    "goose6"
    xzoom -1
define goose_left_2_stock = [
    ("goose4_left", 4),
    ("goose5_left", 4),
    ("goose6_left", 4),
    ]

image goose_strike = "goosehunt/alternative/seagull/4_seagull.png"

image goose_die1:
    "goose11"

image goose_die2:
    "goose11"
    xzoom -1

define goose_die_stock = [
    ("goose_die1", 4),
    ("goose_die2", 4),
    ]


image dog_1 = "goosehunt/alternative/seal/1(1)_seal.png"
image dog_2 = "goosehunt/alternative/seal/1(2)_seal.png"
image dog_3 = "goosehunt/alternative/seal/1(3)_seal.png"
image dog_4 = "goosehunt/alternative/seal/1(4)_seal.png"
image dog_5 = "goosehunt/alternative/seal/2(1)_seal.png"
image dog_6 = "goosehunt/alternative/seal/2(2)_seal.png"
image dog_7 = "goosehunt/alternative/seal/3(1)_seal.png"
image dog_8 = "goosehunt/alternative/seal/3(2)_seal.png"
image dog_9 = "goosehunt/alternative/seal/4(1)_seal.png"
image dog_10 = "goosehunt/alternative/seal/4(2)_seal.png"
image dog_11 = "goosehunt/alternative/seal/5_seal.png"
image dog_12 = "goosehunt/alternative/seal/6_seal.png"

image dog_walk_an:
    "dog_1"
    .3
    "dog_2"
    .3
    "dog_3"
    .3
    "dog_4"
    .3
    repeat

image dog_jump_an:
    "dog_6"
    .6
    "dog_7"
    .3
    "dog_8"

image dog_fall_an:
    "dog_8"


define goosegame_xoffset = 267
define goosegame_yoffset = 35
define goosegame_width = 1134
define goosegame_height = 960
define goosegame_behind_bush = 800

define gh_cen = goosegame_width//2

define gh_baseY = 850
define gh_raiseY = 125

image dog_walk:
    align (.5, .5)


    "dog_walk_an"
    xoffset -171 yoffset gh_baseY
    linear 3.6 xoffset gh_cen - 50 yoffset gh_baseY

    "dog_jump_an"
    anchor (.5, 1.)
    0.9
    linear 0.6 xoffset gh_cen - 0 yoffset gh_baseY - gh_raiseY

image dog_fall:
    pos (goosegame_xoffset, goosegame_yoffset)
    anchor (.5, 1.)

    "dog_fall_an"
    xoffset gh_cen - 0 yoffset gh_baseY - gh_raiseY
    linear 1.2 xoffset gh_cen + 50 yoffset gh_baseY + gh_raiseY*2

image dog_splash:
    anchor (.5, 1.)
    pos (goosegame_xoffset, goosegame_yoffset)

    "goosehunt_splash"
    xoffset gh_cen +25 yoffset goosegame_behind_bush

image dog_laugh_an:
    "dog_9"
    0.2
    "dog_10"
    0.2
    repeat

image dog_laugh:
    contains:
        "dog_laugh_an"
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 342
        linear .3 yoffset goosegame_behind_bush + 50
        pause 2.0
        linear .3 yoffset goosegame_behind_bush + 342
    contains:
        Null()
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 50

        2.3
        "goosehunt_splash"

image dog_one_goose:
    contains:
        "dog_11"
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 342
        linear .3 yoffset goosegame_behind_bush + 50
        pause 1.0
        linear .3 yoffset goosegame_behind_bush + 342
    contains:
        Null()
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 50

        1.3
        "goosehunt_splash"

image dog_two_gooses:
    contains:
        "dog_12"
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 342
        linear .3 yoffset goosegame_behind_bush + 50
        pause 1.0
        linear .3 yoffset goosegame_behind_bush + 342
    contains:
        Null()
        anchor (.5, 1.)
        pos (goosegame_xoffset, goosegame_yoffset)
        xoffset gh_cen yoffset goosegame_behind_bush + 50

        1.3
        "goosehunt_splash"



init -1 python:
    renpy.music.register_channel("goose_1", "sfx", False)
    renpy.music.register_channel("goose_2", "sfx", False)

init python:
    spf = .05
    goosegame_goosespeed = 500
    def spd_pf():
        return goosegame_goosespeed * spf
    fall_spd = spd_pf() * .75
    def CalcDxDy(p1, p2):
        
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dist = (dx**2 + dy**2 )**.5
        time = dist / goosegame_goosespeed
        
        r1 = dx / dist * spd_pf()
        r2 = dy / dist * spd_pf()
        
        fr = max( min( int(time / spf), 30), 5)
        r3 = fr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return r1, r2, r3

    goosegame_goosesize = 152

    def random_x():
        return renpy.random.randint(0, goosegame_width - goosegame_goosesize) + goosegame_goosesize // 2

    GOOSE_ACTIVE = 0
    GOOSE_FLYING_AWAY = 1
    GOOSE_FLEW = 2
    GOOSE_FALL = 3
    GOOSE_STRUCK = 4
    GOOSE_FALLEN = 5

    class Goose():
        def __init__(self, index):
            self.index = index
            self._y = 790
            self._x = random_x()
            self.x = int(self._x)
            self.y = int(self._y)
            t_x = random_x()
            t_y = renpy.random.randint(0, 500) + goosegame_goosesize // 2
            self.dx, self.dy, self.fr = CalcDxDy((self.x, self.y), (t_x, t_y))
            self.state = GOOSE_ACTIVE
            self.is_onscreen = True
            self.lifetime = 0
            self.splashed = None
            
            self.img = self.check_img()
            renpy.music.play("audio/huntgoose/duck_flying.ogg", "goose_{}".format(self.index), True)
        
        def update(self, ammo):
            if not self.is_onscreen:
                return
            
            if self.state in (GOOSE_FLEW, GOOSE_FALLEN):
                return
            
            self.fr -= 1
            self.lifetime += 1
            
            self._x += self.dx
            self._y += self.dy
            self.x = int(self._x)
            self.y = int(self._y)
            
            if self.fr == 0:
                if self.state == GOOSE_STRUCK:
                    self.state = GOOSE_FALL
                    self.dy = fall_spd
                    renpy.play("audio/huntgoose/duck_falling.ogg", "goose_{}".format(self.index))
                
                
                if self.state == GOOSE_ACTIVE:
                    if self.lifetime > 80 or ammo == 0:
                        self.state = GOOSE_FLYING_AWAY
                        self.dx = 0
                        self.dy = -spd_pf()
                    
                    else:
                        t_x = random_x()
                        t_y = renpy.random.randint(0, 500) + goosegame_goosesize // 2
                        self.dx, self.dy, self.fr = CalcDxDy((self.x, self.y), (t_x, t_y))
            
            
            if self.state == GOOSE_FLYING_AWAY:
                if self.y < -goosegame_goosesize // 2:
                    self.state = GOOSE_FLEW
                    self.dy = 0
                    self.is_onscreen = False
                    renpy.play("audio/huntgoose/quack.ogg", "goose_{}".format(self.index))
            
            if self.state == GOOSE_FALL:
                if self.y > goosegame_behind_bush + goosegame_goosesize // 2 + 10:
                    self.state = GOOSE_FALLEN
                    self.dy = 0
                    self.is_onscreen = False
                    self.splashed = False
                    renpy.play("audio/huntgoose/duck_fallen.ogg", "goose_{}".format(self.index))
            
            self.img = self.check_img()
        
        
        def strike(self):
            self.state = GOOSE_STRUCK
            self.dx = 0
            self.dy = 0
            self.fr = int(.25 / spf)
            self.img = self.check_img()
        
        def check_img(self):
            if self.state == GOOSE_STRUCK:
                return "goose_strike"
            if self.state == GOOSE_FLYING_AWAY:
                return select_from_stock(goose_top_stock, self.lifetime)
            if self.state == GOOSE_FALL:
                return select_from_stock(goose_die_stock, self.lifetime)
            
            if self.dx > 0:
                if self.dy > -.67 * spd_pf():
                    return select_from_stock(goose_right_1_stock, self.lifetime)
                else:
                    return select_from_stock(goose_right_2_stock, self.lifetime)
            else:
                if self.dy > -.67 * spd_pf():
                    return select_from_stock(goose_left_1_stock, self.lifetime)
                else:
                    return select_from_stock(goose_left_2_stock, self.lifetime)

    def select_from_stock(stock, timestomp):
        pool = 0
        for item in stock:
            pool += item[1]
        
        cur = timestomp % pool
        
        for item in stock:
            cur -= item[1]
            if cur <= 0:
                return item[0]
        
        return Null()


    GOOSEGAME_READY = 0
    GOOSEGAME_ACTIVE = 1
    GOOSEGAME_AFTER = 2
    class GooseHunt:
        def __init__(self):
            self.active_gooses = [None, None]
            self.state = GOOSEGAME_READY 
            self.ammo = 0
            self.goose_statuses = [] 
            self.points = [0, 0]
            self.reward = 0
            self.round = 1
            self.player = 1
        
        
        def Reset(self):
            self.active_gooses = [None, None]
            self.state = GOOSEGAME_READY 
            self.ammo = 0
            self.goose_statuses = [] 
        
        def AddPoints(self):
            self.points[ self.player-1 ] += self.reward
        
        def StartRound(self):
            self.ammo = 3
            self.active_gooses[0] = Goose(1)
            self.active_gooses[1] = Goose(2)
            self.goose_statuses.append( None )
            self.goose_statuses.append( None )
            self.state = GOOSEGAME_ACTIVE
        
        def Update(self):
            g0 = self.active_gooses[0]
            g1 = self.active_gooses[1]
            
            if g0.is_onscreen:
                g0.update(self.ammo)
                
                if g0.splashed == False:
                    renpy.show_screen("goose1_splash", xpos = g0.x)
                    g0.splashed = True
            
            if g1.is_onscreen:
                g1.update(self.ammo)
                
                if g1.splashed == False:
                    renpy.show_screen("goose2_splash", xpos = g1.x)
                    g1.splashed = True
            
            if g0.is_onscreen or g1.is_onscreen:
                return
            
            self.goose_statuses[-2] = g0.state == GOOSE_FALLEN
            self.goose_statuses[-1] = g1.state == GOOSE_FALLEN
            self.state = GOOSEGAME_AFTER
            return True

screen flash:
    layer "master"
    zorder 1
    add "#fff"
    timer 0.1 action Hide("flash")

screen points_reward_goose1(pos=None):
    layer "master"
    zorder 1

    $ delay = 1.5
    if pos is None:
        $ delay = 0.01

    $ reward = goosehunt_game.reward
    text "[reward]":
        pos pos
        xanchor .5
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    timer delay action Hide("points_reward_goose1")

screen goose1_splash(xpos=-1000):
    layer "master"
    zorder 1

    $ delay = 3.0
    if xpos < 0:
        $ delay = 0.01

    add "goosehunt_splash":
        anchor (.5, 1.)
        xpos xpos + goosegame_xoffset
        ypos goosegame_yoffset + goosegame_behind_bush +50

    timer delay action Hide("goose1_splash")

screen goose2_splash(xpos=-1000):
    layer "master"
    zorder 1

    $ delay = 3.0
    if xpos < 0:
        $ delay = 0.01

    add "goosehunt_splash":
        anchor (.5, 1.)
        xpos xpos + goosegame_xoffset
        ypos goosegame_yoffset + goosegame_behind_bush +50

    timer delay action Hide("goose2_splash")

screen points_reward_goose2(pos=None):
    layer "master"
    zorder 1

    $ delay = 1.5
    if pos is None:
        $ delay = 0.01

    $ reward = goosehunt_game.reward
    text "[reward]":
        pos pos
        xanchor .5
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    timer delay action Hide("points_reward_goose2")

screen vt_frame:
    layer "master"
    zorder 3
    add "goosehunt/tvframe.png"
    add "goosehunt_jack"

screen goosehunt_ui(game):
    layer "master"
    zorder 2


    frame:
        xpos 90 + goosegame_xoffset
        ypos 750 + goosegame_yoffset
        xsize 270
        ysize 60

        background Frame("images/goosehunt/frame1.png", 20, 20)
        has hbox
        align 0.5, 0.5
        spacing 10
        text "SHOT:":
            xalign 0.0
            yalign 0.5
            size 30
            font "font/Retro Gaming.ttf"
        hbox:
            xalign 1.0
            yalign 0.5
            for i in range(3):
                if i < game.ammo:
                    add "goosehunt/01.png"
                else:
                    add Null(40,40)


    frame:
        xpos 620 + goosegame_xoffset
        ypos 750 + goosegame_yoffset
        xsize 450
        ysize 60

        background Frame("images/goosehunt/frame1.png", 20, 20)
        has hbox
        align 0.5, 0.5
        spacing 10
        text "HIT:":
            xalign 0.0
            yalign 0.5
            size 30
            font "font/Retro Gaming.ttf"
        hbox:
            xalign 1.0
            yalign 0.5

            for i in range(8):
                if i < len(game.goose_statuses):
                    $ status = game.goose_statuses[i]

                    if status is None:
                        add "goosehunt/03.png":

                            at transform:
                                alpha 1
                                .5
                                alpha 0
                                .5
                                repeat
                    elif status is True:
                        add "goosehunt/02.png"

                    else:
                        null width 40 height 40

                else:
                    add "goosehunt/03.png"

    $ points = game.points[game.player - 1]
    text f"{points:07}":
        xpos 1070 + goosegame_xoffset
        xalign 1.
        ypos 730 + goosegame_yoffset
        yalign 1.
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

screen goosehunt_hunting(game):
    layer "master"
    zorder 1
    add "goosehunt_bg"

    button:
        if goose_cursor == "goosehunt_cursor 0":
            xsize 1920
            ysize 1080
        else:
            xpos goosegame_xoffset
            ypos goosegame_yoffset
            xsize 1130
            ysize 960
        background Null()
        if game.ammo>0:
            action SetField(game, "ammo", game.ammo-1), Show("flash"), Play("sound", "audio/huntgoose/shot.ogg")
        elif goose_cursor == "goosehunt_cursor 0":
            action NullAction()
        mouse goose_cursor

    $ i = 0
    for goose in game.active_gooses:
        $ i += 1
        button:
            id goose
            xsize goosegame_goosesize
            ysize goosegame_goosesize
            xpos goose.x + goosegame_xoffset
            ypos goose.y + goosegame_yoffset
            xanchor .5
            yanchor .5

            background goose.img

            sensitive game.ammo > 0 and goose.state in (GOOSE_ACTIVE, GOOSE_FLYING_AWAY)
            action [
                Function(goose.strike),
                SetField(game, "ammo", game.ammo-1),
                Show("flash"),
                Play("sound", "audio/huntgoose/shot.ogg"),
                Show("points_reward_goose{}".format(i), pos=(goose.x + goosegame_xoffset, goose.y + goosegame_yoffset - 100)),
                Function(game.AddPoints)
                ]
            mouse goose_cursor

            at transform:
                linear spf xoffset goose.dx yoffset goose.dy

    add "goosehunt_fg"

    timer spf:
        action Function(game.Update)
        repeat True



screen goosehunt_msg_round():
    frame:
        xpos goosegame_xoffset + goosegame_width // 2
        ypos goosegame_yoffset + (goosegame_height // 4)
        xsize 232
        ysize 96
        xanchor .5

        background "images/goosehunt/frame1.png"

        if goosehunt_game.round < 3:
            text "ROUND  {}".format(goosehunt_game.round):
                xalign 0.5
                yalign 0.5
                size 30
                font "font/Retro Gaming.ttf"
        else:
            text "FINAL ROUND":
                xalign 0.5
                yalign 0.5
                size 30
                font "font/Retro Gaming.ttf"

screen goosehunt_msg_perfect():
    frame:
        xpos goosegame_xoffset + goosegame_width // 2
        ypos goosegame_yoffset + (goosegame_height // 4)
        xsize 232
        ysize 96
        xanchor .5
        background Frame("images/goosehunt/frame1.png", 10, 10)


        has vbox
        xalign 0.5
        yalign 0.5
        text "PERFECT!!":
            xalign 0.5
            size 30
            font "font/Retro Gaming.ttf"
        text "+5000":
            xalign 0.5
            size 30
            font "font/Retro Gaming.ttf"

screen goosehunt_msg_points():

    fixed:
        xpos goosegame_xoffset
        ypos goosegame_yoffset
        xsize goosegame_width
        ysize goosegame_height

        text "SCORE":
            xalign 0.5
            yalign 0.25
            size 30
            font "font/Retro Gaming.ttf"

        vbox:
            xalign .34
            yalign 0.45
            text "PLAYER 1":
                size 30
                font "font/Retro Gaming.ttf"
            text "PLAYER 2":
                size 30
                font "font/Retro Gaming.ttf"

        vbox:
            xalign .70
            yalign 0.45
            text "{}".format(goosehunt_game.points[0]):
                xalign 1.
                size 30
                font "font/Retro Gaming.ttf"
            text "{}".format(goosehunt_game.points[1]):
                xalign 1.
                size 30
                font "font/Retro Gaming.ttf"

screen goosehunt_msg_getready():
    fixed:
        xpos goosegame_xoffset
        ypos goosegame_yoffset
        xsize goosegame_width
        ysize goosegame_height

        vbox:
            xalign 0.5
            yalign 0.35

            text "PLAYER {}".format(goosehunt_game.player):
                xalign 0.5
                size 30
                font "font/Retro Gaming.ttf"

            text "GET READY":
                xalign 0.5
                size 30
                font "font/Retro Gaming.ttf"

default goose_player = 1
default goose_nextlabel = None
image goosehunt_jack = "goosehunt/jack.png"

default cursor_default = config.mouse["default"]

label goosehunt:

    $ is_save_allowed = False
    $ _game_menu_screen = None

    if goose_cursor == "goosehunt_cursor 0":
        $ default_mouse = goose_cursor

    show screen day3_dendy_turnoff()

    label goosehunt.intro:
        window hide
        hide goosehunt_fg
        show goosehunt_tv zorder 3
        show goosehunt_jack zorder 3
        show day3_goosedendy_black
        show screen goosehunt_msg_getready()

        pause 2.0

        hide day3_goosedendy_black
        hide screen goosehunt_msg_getready
        show screen goosehunt_msg_round()
        show goosehunt_bg

        if goosehunt_game.round == 1 and goosehunt_game.player == 1:

            $ renpy.play("audio/huntgoose/game_start.ogg", "sound")

            show dog_walk_an:
                anchor (.5, 1.)
                pos (goosegame_xoffset, goosegame_yoffset)
                xoffset -171 yoffset gh_baseY

                linear 3.6 xoffset gh_cen - 50 yoffset gh_baseY

            pause 3.6

            $ renpy.play("audio/huntgoose/dog_barks.ogg", "sound")
            pause 1.0

            hide dog_walk_an
            show dog_jump_an:
                anchor (.5, 1.)
                pos (goosegame_xoffset, goosegame_yoffset)
                xoffset gh_cen - 50 yoffset gh_baseY

                0.9
                linear 0.6 xoffset gh_cen - 0 yoffset gh_baseY - gh_raiseY

            pause 1.5

            show goosehunt_fg zorder 1

            hide dog_jump_an
            show dog_fall_an:
                anchor (.5, 1.)
                pos (goosegame_xoffset, goosegame_yoffset)
                xoffset gh_cen - 0 yoffset gh_baseY - gh_raiseY

                linear 1.2 xoffset gh_cen + 50 yoffset gh_baseY + gh_raiseY*2

            pause .6

            show goosehunt_splash:
                anchor (.5, 1.)
                pos (goosegame_xoffset, goosegame_yoffset)
                xoffset gh_cen +50 yoffset goosegame_behind_bush + 50

            pause 1.5
        else:

            pause 2.0
            show goosehunt_fg zorder 1

        hide screen goosehunt_msg_round
        hide goosehunt_bg

        hide dog_walk
        hide goosehunt_tv
        hide goosehunt_jack
        hide dog_fall
        hide goosehunt_null



    label goosehunt.loop:
        $ goosehunt_game.StartRound()

        show screen goosehunt_hunting(game = goosehunt_game)
        show screen goosehunt_ui(game = goosehunt_game)
        show screen vt_frame()

        $ ui.interact()

        hide screen goosehunt_hunting
        hide screen vt_frame

    label goosehunt.round_result:

        $ ngoose = 0
        if goosehunt_game.active_gooses[0].state == GOOSE_FALLEN:
            $ ngoose += 1
        if goosehunt_game.active_gooses[1].state == GOOSE_FALLEN:
            $ ngoose += 1

        show goosehunt_bg
        show goosehunt_fg
        show goosehunt_tv zorder 3
        show goosehunt_jack zorder 3

        if ngoose == 2:
            $ renpy.play("audio/huntgoose/dog_with_ducks.ogg", "sound")
            show dog_two_gooses as dog_result

            $ renpy.pause( 2.3, hard=True )

        elif ngoose == 1:
            $ renpy.play("audio/huntgoose/dog_with_ducks.ogg", "sound")
            show dog_one_goose as dog_result

            $ renpy.pause( 2.3, hard=True )
        else:

            $ renpy.play("audio/huntgoose/dog_laughs.ogg", "sound")
            show dog_laugh as dog_result

            $ renpy.pause( 3.3, hard=True )

        hide dog_result

        if len(goosehunt_game.goose_statuses) < 8:

            hide goosehunt_tv
            hide goosehunt_jack
            hide goosehunt_null

            jump goosehunt.loop
        else:

            python:
                goose_hits = 0
                for hit in goosehunt_game.goose_statuses:
                    if hit:
                        goose_hits += 1
            if goose_hits == 8:
                $ goosehunt_game.points[ goosehunt_game.player-1 ] += 5000
                show screen goosehunt_msg_perfect()
                pause 2.0
                hide screen goosehunt_msg_perfect

    hide goosehunt_fg
    hide screen goosehunt_ui
    hide screen day3_dendy_turnoff

    $ default_mouse = "default"

    $ is_save_allowed = True
    $ _game_menu_screen = "quick_menu"

    if goose_nextlabel is not None:
        jump expression goose_nextlabel

    return


label start_goosehunt:
    menu:
        "slow":
            $ goosegame_goosespeed = 400
            $ goose_reward = 500
        "normal":
            $ goosegame_goosespeed = 500
            $ goose_reward = 1000
        "fast":
            $ goosegame_goosespeed = 650
            $ goose_reward = 1500
    show goose_olya zorder 4
    jump goosehunt
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
