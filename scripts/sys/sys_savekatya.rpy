

init python:
    import pygame 
    import random 
    pygame.init() 

    Width = 553 
    Height = 563 

    error_margin = 5.0 
    win_delay = 5.0 
    spf = 0.04 

    savekatya_text_call_to_action_btn = _("СПАСТИ{#SaveKatyaButton}")
    savekatya_text_call_to_action_alert = _("СПАСТИ{#SaveKatyaInGameAlert}")

    class puzKatyaSettings:
        def __init__(self, progress = (0, 200), speed = (-30, 50), speed_per_second = -200, speed_boost = 80, trigger_range = (5., 5.), win_delay = 5.0, decay_mod = 0.0, disp = None):
            self.min_progress = progress[0]
            self.max_progress = progress[1]
            self.min_spd = speed[0]
            self.max_spd = speed[1]
            self.trigger_range = trigger_range
            self.win_delay = win_delay
            self.decay_mod = decay_mod
            
            self.spd_per_sec = speed_per_second
            self.spd_boost = speed_boost
            
            self.disp = disp

    class puzKatya:
        def __init__(self, settings, win_lbl=None, lose_lbl = None, start_progress_ratio = 0.5):
            self.win_lbl = win_lbl
            self.lose_lbl = lose_lbl
            
            self.settings = settings
            self.speed = settings.min_spd
            self.progress = settings.min_progress * (1. - start_progress_ratio) + settings.max_progress * start_progress_ratio
            self.progress_range = self.settings.max_progress - self.settings.min_progress
            
            self.win_timer = 0.0
            self.init_pos = (0, 100)
            self.pos = (self.init_pos[0], int(self.init_pos[1] - self.progress))
            self.boosted = False
        
        def boost(self):
            self.boosted = True
        
        def update(self, dt, is_boosted = None):
            if is_boosted is None:
                is_boosted = self.boosted
                self.boosted = False
            
            progress_ratio = (self.progress - self.settings.min_progress) / self.progress_range
            boost_value = self.settings.spd_boost * (1. - progress_ratio*self.settings.decay_mod)
            
            self.speed += self.settings.spd_per_sec*dt + boost_value*is_boosted
            self.speed = min(max(self.speed, self.settings.min_spd), self.settings.max_spd)
            
            self.progress += self.speed*dt
            self.progress = min(max(self.progress, self.settings.min_progress), self.settings.max_progress)
            
            self.pos = (self.init_pos[0], int(self.init_pos[1] - self.progress))
            
            if self.win_lbl is not None:
                if self.settings.max_progress - self.progress < self.settings.trigger_range[0]:
                    self.win_timer += dt
                
                if self.win_timer > self.settings.win_delay:
                    return self.win_lbl
            
            if self.lose_lbl is not None:
                if self.progress - self.settings.min_progress < self.settings.trigger_range[1]:
                    return self.lose_lbl
        
        def draw(self, render, st, at):
            img_d = renpy.displayable("d4_puzKatya")
            
            render.blit( img_d.render(0, 0, st, at), self.pos)


transform struggle:
    subpixel True
    linear .1 yoffset 3
    linear .1 yoffset -5
    linear .1 yoffset 5
    linear .1 yoffset -5
    repeat

screen saveKatya(puz):
    fixed:
        xfit True
        yfit True
        pos 1000, 600

        add puz.settings.disp:
            anchor (.5, .5)
            pos puz.pos
            at struggle

    add "d4_sk_fg":

        at transform:
            linear .03 xoffset 5
            linear .03 xoffset -5
            repeat
    add "d4_sk_blink"

    text savekatya_text_call_to_action_alert:
        align (.53, .72)

        at transform:
            linear .1 zoom 1.15
            linear .1 zoom 1.00
            repeat
    button:
        background None
        xfill True
        yfill True
        action Function(puz.boost)
    key "K_SPACE" action Function(puz.boost)

    timer spf:
        action Function(puz.update, spf)
        repeat True

screen btn_save_katya():
    button:
        xysize (360, 280)
        align (.53, .78)
        background "interface/intercative_button.png"
        text savekatya_text_call_to_action_btn:
            align (.5, .5)
            color "#000"
        action Return()

init python:
    SK_disp_easy = "d4_sk_katya_struggle_easy"
    SK_disp_hard = "d4_sk_katya_struggle_hard"
    SK_spd_easy = (-25, 25)
    SK_spd_hard = (-25, 25)
    SK_spd_easy_debug = (-50, 250)
    SK_spd_hard_debug = (-50, 250)
    SK_sps_easy = -35.0/.3
    SK_sps_hard = -35.0/.3
    SK_sps_easy_debug = -50.0/10.
    SK_sps_hard_debug = -50.0/10.
    SK_boost_easy = 35
    SK_boost_hard = 35
    SK_boost_easy_debug = 350
    SK_boost_hard_debug = 350
    SK_decmod_easy = 0.0
    SK_decmod_hard = 0.7
    SK_trigrange_easy = (15, 5)
    SK_trigrange_hard = (180, 5)
    SK_windel_easy = 3.0
    SK_windel_hard = 10.0
    SK_windel_easy_debug = 1.0
    SK_windel_hard_debug = 4.0

    SK_easy_mode_true = puzKatyaSettings(
    speed = SK_spd_easy,
    speed_per_second = SK_sps_easy,
    speed_boost = SK_boost_easy,
    decay_mod = SK_decmod_easy,
    trigger_range = SK_trigrange_easy,
    win_delay = SK_windel_easy,
    disp = SK_disp_easy)
    SK_hard_mode_true = puzKatyaSettings(
    speed = SK_spd_hard,
    speed_per_second = SK_sps_hard,
    speed_boost = SK_boost_hard,
    decay_mod = SK_decmod_hard,
    trigger_range = SK_trigrange_hard,
    win_delay = SK_windel_hard,
    disp = SK_disp_hard)
    SK_easy_mode_debug = puzKatyaSettings(
    speed = SK_spd_easy_debug,
    speed_per_second = SK_sps_easy_debug,
    speed_boost = SK_boost_easy_debug,
    decay_mod = SK_decmod_easy,
    trigger_range = SK_trigrange_easy,
    win_delay = SK_windel_easy_debug,
    disp = SK_disp_easy)
    SK_hard_mode_debug = puzKatyaSettings(
    speed = SK_spd_hard_debug,
    speed_per_second = SK_sps_hard_debug,
    speed_boost = SK_boost_hard_debug,
    decay_mod = SK_decmod_hard,
    trigger_range = SK_trigrange_hard,
    win_delay = SK_windel_hard_debug,
    disp = SK_disp_hard)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
