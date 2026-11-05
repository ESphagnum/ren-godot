"Wave Shader Ren'Py Module 2022 Daniel Westfall <SoDaRa2595@gmail.com>"
"http://twitter.com/sodara9 I'd appreciate being given credit if you do end up using it! :D Would really make my day to know I helped some people out! Really hope this can help the community create some cool visuals! http://opensource.org/licenses/mit-license.php Github: https://github.com/SoDaRa/RenpyWaveShader itch.io: https://wattson.itch.io/renpy-wave-shader Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=64378"






























"Notes on how to use"





"Important Part"




init -1 python:
    
    from renpy.uguu import GL_CLAMP_TO_EDGE, GL_MIRRORED_REPEAT, GL_REPEAT
    renpy.register_shader("watt.wave", variables="""
        uniform float u_shader_time;
        uniform vec2 u_wave_period;
        uniform vec2 u_wave_amp;
        uniform vec2 u_wave_speed;
        uniform float u_direction;
        uniform vec2 u_damp;
        uniform float u_double;
        uniform vec3 u_double_params_x;
        uniform vec3 u_double_params_y;
        uniform float u_melt;
        uniform vec3 u_melt_params_x;
        uniform vec3 u_melt_params_y;

        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200 = """
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec2 new_pos;
        vec2 wave_offset = vec2(0.0, 0.0);
        vec2 melt_offset = vec2(0.0, 0.0);
        vec2 double_offset = vec2(0.0, 0.0);
        vec2 double_pos = vec2(0.0, 0.0);
        vec2 damp = vec2(1.0, 1.0);
        vec4 new_color;
        vec4 double_color;

        if (u_damp.x >= 0.0 && u_damp.x != 1.0) {damp.x = pow(u_damp.x, v_coords.y * u_model_size.y);}
        else if (u_damp.x < 0.0) {damp.x = pow((-1.0 * u_damp.x), (1.0 - v_coords.y) * u_model_size.y);}
        if (u_damp.y >= 0.0 && u_damp.y != 1.0) {damp.y = pow(u_damp.y, v_coords.x * u_model_size.x);}
        else if (u_damp.y < 0.0) {damp.y = pow((-1.0 * u_damp.y), (1.0 - v_coords.x) * u_model_size.x);}

        if (u_direction < 2.0) {wave_offset.x = sin( u_wave_period.x * (v_coords.y + (u_shader_time * u_wave_speed.x))) * u_wave_amp.x * 0.01 * damp.x;}
        else {wave_offset.x = 0.0;}
        if (u_direction < 1.0 || u_direction >= 2.0) {wave_offset.y = sin( u_wave_period.y * (v_coords.x + (u_shader_time * u_wave_speed.y))) * u_wave_amp.y * 0.01 * damp.y;}
        else {wave_offset.y = 0.0;}

        if (u_melt >= 0.0){
            if (u_melt < 2.0) {melt_offset.x = sin( u_melt_params_x.x * (v_coords.x + (u_shader_time * u_melt_params_x.z))) * u_melt_params_x.y * 0.01 * damp.x;}
            else {melt_offset.x = 0.0;}
            if (u_melt < 1.0 || u_melt >= 2.0) {melt_offset.y = sin( u_melt_params_y.x * (v_coords.y + (u_shader_time * u_melt_params_y.z))) * u_melt_params_y.y * 0.01 * damp.y;}
            else {melt_offset.y = 0.0;}
        }
        new_pos.x = v_coords.x + wave_offset.x + melt_offset.x;
        new_pos.y = v_coords.y + wave_offset.y + melt_offset.y;

        new_color = texture2D(tex0,new_pos);

        if (u_double < 0.0) {gl_FragColor = new_color;}
        else{
            if (u_double < 2.0) {double_offset.x = sin( u_double_params_x.x * (v_coords.y + (u_shader_time * u_double_params_x.z))) * u_double_params_x.y * -0.01 * damp.x;}
            else {double_offset.x = 0.0;}
            if (u_double < 1.0 || u_double >= 2.0) {double_offset.y = sin( u_double_params_y.x * (v_coords.x + (u_shader_time * u_double_params_y.z))) * u_double_params_y.y * -0.01 * damp.y;}
            else {double_offset.y = 0.0;}
            double_pos.x = v_coords.x + double_offset.x + melt_offset.x;
            double_pos.y = v_coords.y + double_offset.y + melt_offset.y;
            double_color = texture2D(tex0,double_pos);
            gl_FragColor = mix(new_color, double_color, 0.5);
        }
    """)
    
    
    def advance_shader_time(trans, st, at):
        trans.u_shader_time = at
        return 0
    
    
    
    
    
    
    class WaveShader(object):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def __init__(self, amp = 12.0, period = 20.0, speed = 1.0, direction = "both", damp = 1.0, double=None, double_params=None, melt=None, melt_params=None, repeat=None):
            
            options_dict = {"vertical": 2.0, "y": 2.0, "horizontal": 1.0, "x": 1.0, "both": 0.0, None: -1.0}
            property_dict = {'clamp': GL_CLAMP_TO_EDGE, 'mirrored': GL_MIRRORED_REPEAT, 'mirror': GL_MIRRORED_REPEAT, 'repeat': GL_REPEAT}
            
            def float_or_tuple(param):
                if isinstance(param, (float, int)):
                    return (float(param), float(param))
                return param
            
            self.period = float_or_tuple(period)
            self.amp = float_or_tuple(amp)
            self.speed = float_or_tuple(speed)
            if direction in options_dict:
                self.dir = options_dict[direction.lower()]
            else:
                self.dir = 0.0
            
            self.damp = float_or_tuple(damp)
            
            if double is None:
                self.double = -1.0
                self.double_params_x = (0.0, 0.0, 0.0)
                self.double_params_y = (0.0, 0.0, 0.0)
            else:
                if double in options_dict:
                    self.double = options_dict[double.lower()]
                else:
                    self.double = 0.0
                if double_params is not None:
                    
                    if len(double_params) == 6:
                        self.double_params_x = double_params[0:3]
                        self.double_params_y = double_params[3:]
                    else:
                        self.double_params_x = double_params
                        self.double_params_y = double_params
                else:
                    
                    self.double_params_x = (self.period[0], self.amp[0], self.speed[0])
                    self.double_params_y = (self.period[1], self.amp[1], self.speed[1])
            
            if melt is None:
                self.melt = -1.0
                self.melt_params_x = (0.0, 0.0, 0.0)
                self.melt_params_y = (0.0, 0.0, 0.0)
            else:
                if melt in options_dict:
                    self.melt = options_dict[melt.lower()]
                else:
                    self.melt = 0.0
                if melt_params is not None:
                    
                    if len(melt_params) == 6:
                        self.melt_params_x = melt_params[0:3]
                        self.melt_params_y = melt_params[3:]
                    else:
                        self.melt_params_x = melt_params
                        self.melt_params_y = melt_params
                else:
                    
                    self.melt_params_x = (self.period[0], self.amp[0], self.speed[0])
                    self.melt_params_y = (self.period[1], self.amp[1], self.speed[1])
            
            self.repeat = None
            if isinstance(repeat, (unicode,str)):
                repeat = property_dict[repeat]
                self.repeat = (repeat, repeat)
            elif isinstance(repeat, tuple):
                self.repeat = (property_dict[repeat[0]], property_dict[repeat[1]])
            
            self.first_time = True
        
        
        
        
        def __call__(self, trans, st, at):
            if self.first_time or trans.shader != 'watt.wave':
                trans.shader = 'watt.wave'
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_wave_period = self.period
                trans.u_wave_amp = self.amp
                trans.u_wave_speed = self.speed
                trans.u_direction = self.dir
                trans.u_damp = self.damp
                trans.u_double = self.double
                trans.u_double_params_x = self.double_params_x
                trans.u_double_params_y = self.double_params_y
                trans.u_melt = self.melt
                trans.u_melt_params_x = self.melt_params_x
                trans.u_melt_params_y = self.melt_params_y
                if self.repeat != None:
                    trans.gl_texture_wrap = self.repeat
                self.first_time = False
            return advance_shader_time(trans, st, at)

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
