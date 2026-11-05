init python:
    
    achievement_list = [
    
        "ach_detective_1",      
        "ach_number",           
        "ach_Vova",             
        "ach_escaped",          
        "ach_tape",             
        "ach_neverland",        
        "ach_radio",            

    
        "ach_accepted_treat",   
        "ach_rejected_treat",   
        "ach_detective_2",      
        "ach_force",            
        "ach_fight",            
        "ach_insulted",         
        "ach_knigh",            
        "ach_adventure",        
        "ach_masquerade",       
        "ach_tough_luck",       

    
        "ach_amulet",           
        "ach_sceptic",          
        "ach_duckinator",       
        "ach_quiet",            
        "ach_van_gogh",         
        "ach_meanie",           
        "ach_bro",              
        "ach_voltron",          
        "ach_muse",             
        "ach_ring",             
        "ach_missed",           
        "ach_victory",          
        "ach_defeat",           
        "ach_detective_3",      

    
        "ach_pig",              
        "ach_Haide",            
        "ach_Djakel",           
        "ach_musketeers",       
        "ach_no",               
        "ach_strawberry",       
        "ach_meat",             
        "ach_end1",             
        "ach_secret",           
        "ach_dicaprio",         
        "ach_cops",             
        "ach_true4",            

    
        "ach_amur",
        "ach_melo",
        "ach_smak",
        "ach_blevan",
        "ach_lapke",
        "ach_fish",
        "ach_bard",
        "ach_punk",
        "ach_bezdar",
        "ach_red",
        "ach_zoh",
        "ach_blue",
        "ach_natur",
        "ach_P_R",
        "ach_P",
        "ach_hodor",
        "ach_gerasim",
        "ach_pavlov",
        "ach_love",
        "ach_family",
        "ach_beast",
        "ach_human",
        "ach_kill_rom",
        "ach_kill_polina",
        "ach_kill_olya",
        "ach_hot",
        "ach_sherlok",
        "ach_stanislavski",
        "ach_yaz",
        "ach_cross",
        "ach_star",
        "ach_ego",
        "ach_altruist",
        "ach_light",
        "ach_dark",
        "ach_norm",
        "ach_sigma",
        "ach_1890",
        "ach_light_off",
        "ach_P_end",
        "ach_grey",
        "ach_reunification",
        "ach_blood",
        "ach_hell",
        "ach_madhouse",
        "ach_alien",
        "ach_ratatouille",
        "ach_canned",
        "ach_solid",
        "ach_last_spurt",
        "ach_abyss",
        "ach_last_hero",
        "ach_bodrov",
        "ach_letov",
        "ach_darkness",
        "ach_Davie504",
        "ach_zulka",
        "ach_detective_5",
        "ach_collector",
    ]
    
    for ach_id in achievement_list:
        achievement.register(ach_id)
    
    achievement.sync()
    
    def achievement_grant(ach_id):
        achievement.grant(ach_id)
        
        all_granted = True
        for ach_id in achievement_list:
            if ach_id == "ach_collector":
                continue
            
            if not achievement.has(ach_id):
                all_granted = False
        
        if all_granted:
            achievement.grant("ach_collector")
            achievement.sync()

default true_detective_count1 = 0
default true_detective_count2 = 0
default radio_hidden_message = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
