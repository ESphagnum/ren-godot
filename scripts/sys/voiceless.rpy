init python:
    
    
    ignored_characters = ["Narr_color"]
    
    def Voiceless():
        characters = dict()
        
        
        f_script = renpy.open_file("script.rpy")
        content = [line.decode("utf-8") for line in f_script]
        fs_path = renpy.config.gamedir + "/"
        
        
        for i in range(len(content)): 
            ln = content[i]
            
            
            char_pos = ln.find("Character")
            if char_pos < 0:
                continue
            
            name_start_idx = 5 + 2
            name_end_idx = 6 + 2
            while ln[name_end_idx] != " ":
                name_end_idx += 1
            
            new_name = ln[name_start_idx : name_end_idx]
            if new_name in ignored_characters:
                continue
            characters[new_name] = []
        
        f_script.close()
        
        
        
        f_scene = renpy.open_file("scripts/scene/scene_day_5.rpy")
        content = [line.decode("utf-8") for line in f_scene]
        f_scene.close()
        
        
        for i in range(len(content)):
            ln = content[i]
            
            for char in characters.keys():
                target_line = " " + char + " \""
                if ln.find(target_line) < 0:
                    continue
                
                ln_prev = content[i-1]
                if ln_prev.find("voice") < 0:
                    characters[char].append((i, ln))
        
        f_out = open(fs_path + "voiceless.txt", "w")
        for char in characters.keys():
            msg = "==>> {} have {} lines:\n".format(char, len(characters[char]))
            
            if len(characters[char]) == 0:
                continue
            
            f_out.write(msg)
            for num, line in characters[char]:
                f_out.write("{}: {}".format(num, line))
        
        f_out.close()
    
    
    def GetPredicts():
        
        result = dict()
        
        f_scene = renpy.open_file("scripts/scene/scene_day_5.rpy")
        content = [line.decode("utf-8") for line in f_scene]
        f_scene.close()
        
        current_label = "day_5"
        
        for i in range(len(content)):
            ln = content[i].strip()
            if not ln:
                continue
            
            if ln[0] == "#":
                continue
            
            if ln.find("label") >= 0 and ln.find(".") < 0:
                current_label = ln.split("label")[1].split(":")[0]
            
            if ln.find("_predict(\"") < 0:
                continue
            
            asset = ln.split("\"")[1]
            if asset not in result:
                result[asset] = []
            
            if ln.find("start_predict") >= 0:
                result[asset].append( (current_label, i, True) )
            if ln.find("stop_predict") >= 0:
                result[asset].append( (current_label, i, False) )
        
        return result
    watchout_predicts = [
        "",
    ]
    def PredictMatches(data):
        keys = list(data.keys())
        result = []
        for asset in keys:
            log = data[asset]
            
            if asset in watchout_predicts:
                print("======", asset, "======")
            
            starts = 0
            stops = 0
            last = None
            for entry in log:
                lbl, line, state = entry
                if asset in watchout_predicts:
                    print(entry)
                last = state
                if state:
                    starts += 1
                else:
                    stops += 1
            
            if starts > stops or last:
                
                result.append((asset, "{}/{}".format(starts, stops), "+" if last else "-"))
        
        f_out = open(renpy.config.gamedir + "/predictless.txt", "w")
        for res in result:
            f_out.write("{}, {}, {}\n".format(res[0], res[1], res[2]))
        
        f_out.close()
    
    
    def ApplyTranslate(episod_number, language_code):
        import openpyxl
        import codecs
        import sys
        
        episods = {
            1: "scene_day_1.rpy",
            2: "scene_day_2.rpy",
            3: "scene_day_3.rpy",
            4: "scene_day_4.rpy",
            5: "scene_day_5.rpy",
        }
        
        languages = {
            0: ("english", 2),
            1: ("chinese", 3),
            2: ("japan", 4),
            3: ("turkish", 5),
            4: ("italiano", 6),
        }
        
        language, target_column = languages[language_code]
        filepath = "tl/" + language + "/scripts/scene/" + episods[episod_number]
        filepath_out = "tl/" + language + "/scripts/scene/_" + episods[episod_number]
        
        russion_column = 1
        
        f_scene = renpy.open_file(filepath)
        content = [line.decode("utf-8") for line in f_scene]
        f_scene.close()
        
        new_content = []
        
        filename_xl = renpy.config.gamedir + "/Tiny_Bunny_TL.xlsx"
        filename_junk = renpy.config.gamedir + "/junk.txt"
        
        junk = []
        
        wb = openpyxl.load_workbook(filename = filename_xl)
        sheet = wb["Sheet1"]
        
        rus = ""
        tl = ""
        
        """
        TODO:

        """
        
        i = 1
        while True:
            i += 1
            
            if i % 100 == 0:
                print(i)
            
            
            rus_val = sheet.cell(row=i, column=russion_column).value
            tl_val = sheet.cell(row=i, column=target_column).value
            
            if rus_val.startswith("47321 слов"):
                break
            
            rus = "    # "
            tl = "    "
            rus += rus_val.strip()
            tl += tl_val.strip()
            rus_old = "    old " + rus_val.strip()
            tl_new = "    new " + tl_val.strip()
            
            found = False
            for j in range(len(content)):
                
                if content[j].find(rus) == 0:
                    found = True
                    
                    splitted = content[j+1].split()
                    
                    if splitted[0] == "voice":
                        content[j+2] = tl + "\n"
                    
                    else:
                        content[j+1] = tl + "\n"
                
                if content[j].find(rus_old) == 0:
                    found = True
                    
                    content[j+1] = tl_new + "\n"
            
            
            if not found:
                
                junk.append(rus + " | " + str(i) + "\n")
                print(i)
                print(rus)
                print(cn)
        
        print("misses:", len(junk))
        
        wb.close()
        
        f_out = open(filepath_out)
        for ln in content:
            f_out.write(content)
        
        f_out.close()
        
        fileObj = codecs.open( filename_junk, "w", "utf_8_sig" )
        fileObj.writelines(junk)
        fileObj.close()

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
