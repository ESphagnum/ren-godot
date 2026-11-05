init -1 python:

    class LipS():
        
        def __init__(self):
            self.frames = [] 
        
        def read_file(self, file):
            
            self.frames = []
            
            f = renpy.file(file)
            frames = f.readlines()  
            
            for line_num in range(len(frames)):
                frames[line_num] = frames[line_num].replace("\r","").replace("\n","").split(',')
                frames[line_num][1] = float(frames[line_num][1])
            
            self.frames = frames

    def LipS_get_Timing(t1,t2, obj, dict):
        
        
        
        
        try:
            stime = 0  
            i = 0
            
            
            while stime <= t1:
                if i == len(obj.frames):
                    
                    return dict['static'], None
                redraw = float(obj.frames[i][1])
                stime += redraw
                i += 1
            
            i -= 1 
            
            if obj.frames[i][0] != '_':
                d = dict[(obj.frames[i][0], int(obj.frames[i][2]))]
            else:
                d = dict['_']
            
            return d, redraw
        except:
            
            
            return dict['static'], None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
