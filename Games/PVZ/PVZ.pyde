import time
import random
add_library("minim")
spawn_pos_x = 900
column_pos = (80,183,279,385,467, 573) #The borders between rows from the very top to the very bottom
row_pos = (251, 334, 408, 493, 576, 654, 738, 812, 898, 987) #The borders between columns from the very left to the very right

ice_offset = 50
melt_rate = -3
max_amplifier = 5
amplifier_rate = 5**(1.0/30.0) #1.055#will reach max_amplifier in 30 waves

easy_waves = [{"sound" : "moon", "Bucket" : 5, "Door" : 5},
              {"sound" : "grass", "Basic" : 5, "Cone" : 2},
              {"sound" : "fast", "Zamboni" : 2, "Football" : 2},
              {"sound" : "brain", "Gargantuar" : 5,  "Basic" : 5}]
        #   "Basic" : 0,
        #   "Cone" : 0,
        #   "Gargantuar" : 5},

        # {"Football" : 0,
        #   "Basic" : 5,
        #   "Cone" : 0,
        #   "Gargantuar" : 5},
        
        # {"Football" : 0,
        #   "Basic" : 0,
        #   "Cone" : 5,
        #   "Gargantuar" : 5}]
hard_waves = easy_waves #[{"Football" : 15,
#           "Basic" : 0,
#           "Cone" : 0},

#         {"Football" : 0,
#           "Basic" : 15,
#           "Cone" : 0},
        
#         {"Football" : 0,
#           "Basic" : 0,
#           "Cone" : 15},
        
#         {"Football" : 5,
#           "Basic" : 5,
#           "Cone" : 5}] 

zombies = {"Zamboni" : {"image" : {"size" : {"x" : 185, "y" : 185}, "pos" : {"x" : spawn_pos_x + 185, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                         "animations" : [{"file_index" : "zombies/zamboni/walk/(", 
                        "file_type" : ").png", 
                        "start" : 0,
                        "total_frames" : 32, 
                        "frame_duration" : 0.03}, 
                                    
                                            {"file_index" : "zombies/zamboni/walk/(",
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 32, 
                                            "frame_duration" : 0.03},
    
                                            {"file_index" : "zombies/zamboni/died/(", 
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 20, 
                                            "frame_duration" : 0.1}]},
                        "Settings" : {"offset" : {"x" : 92, "y" : -25}, "ground_offset" : -14, "speed" : 10, "last_moved" : time.time(), "last_attacked" : time.time(), "blocked" : False, "health" : 1350, "dps" : 1000, "death_timer" : 1},
                        }, 
           
           
           "Gargantuar" : {"image" : {"size" : {"x" : 360, "y" : 203}, "pos" : {"x" : spawn_pos_x, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                         "animations" : [{"file_index" : "zombies/gargantuar/walk/(", 
                        "file_type" : ").png", 
                        "start" : 0,
                        "total_frames" : 196, 
                        "frame_duration" : 0.09}, 
                                    
                                            {"file_index" : "zombies/gargantuar/eat/(",
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 48, 
                                            "frame_duration" : 0.09},
    
                                            {"file_index" : "zombies/gargantuar/died/(", 
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 83, 
                                            "frame_duration" : 0.09}]},
                        "Settings" : {"offset" : {"x" : 150, "y" : -25}, "ground_offset" : -30, "speed" : 5, "last_moved" : time.time(), "last_attacked" : time.time(), "blocked" : False, "health" : 2800, "dps" : 232, "death_timer" : 1},
                        }, 
           
           "Football" : {"image" : {"size" : {"x" : 360, "y" : 203}, "pos" : {"x" : spawn_pos_x, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                         "animations" : [{"file_index" : "zombies/football/walk/(", 
                        "file_type" : ").png", 
                        "start" : 0,
                        "total_frames" : 15, 
                        "frame_duration" : 0.09}, 
                                    
                                            {"file_index" : "zombies/football/eat/(",
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 25, 
                                            "frame_duration" : 0.04},
    
                                            {"file_index" : "zombies/died/(", 
                                            "file_type" : ").png", 
                                            "start" : 0,
                                            "total_frames" : 202, 
                                            "frame_duration" : 0.04}]},
                        "Settings" : {"offset" : {"x" : 150, "y" : 0}, "ground_offset" : -90, "speed" : 40, "last_moved" : time.time(), "last_attacked" : time.time(), "blocked" : False, "health" : 1670, "dps" : 3, "death_timer" : 1},
                        }, 
            "Bucket" :  {"image" : {
                                    "size" : {"x" : 360, "y" : 203}, 
                                    "pos" : {"x" : spawn_pos_x, "y" : 0}, 
                                    "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                                    "animation_selected" : 0,
                                    "animations" : [{"file_index" : "zombies/bucket/walk/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 82, 
                                                   "frame_duration" : 0.04}, 
                                    
                                                   {"file_index" : "zombies/bucket/eat/(",
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 27, 
                                                   "frame_duration" : 0.04},
           
                                                   {"file_index" : "zombies/died/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 202, 
                                                   "frame_duration" : 0.04}]
                                    }, 
           
                        "Settings" : {"offset" : {"x" : 180, "y" : 0}, 
                                                "ground_offset" : -68,
                                                "speed" : 10,
                                                "last_moved" : time.time(), 
                                                "last_attacked" : time.time(), 
                                                "blocked" : False, 
                                                "health" : 1370,
                                                "dps" : 1,
                                                "death_timer" : 1}
           },
           
           "Door" :  {"image" : {
                                    "size" : {"x" : 360, "y" : 203}, 
                                    "pos" : {"x" : spawn_pos_x, "y" : 0}, 
                                    "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                                    "animation_selected" : 0,
                                    "animations" : [{"file_index" : "zombies/door/walk/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 85, 
                                                   "frame_duration" : 0.04}, 
                                    
                                                   {"file_index" : "zombies/door/eat/(",
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 28, 
                                                   "frame_duration" : 0.04},
           
                                                   {"file_index" : "zombies/died/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 202, 
                                                   "frame_duration" : 0.04}]
                                    }, 
                    "Settings" : {"offset" : {"x" : 180, "y" : 0}, 
                                            "ground_offset" : -68,
                                            "speed" : 10,
                                            "last_moved" : time.time(), 
                                            "last_attacked" : time.time(), 
                                            "blocked" : False, 
                                            "health" : 1370,
                                            "dps" : 1,
                                            "death_timer" : 1}
            },
           
                         
                         
           
           "Basic" :  {"image" : {
                                    "size" : {"x" : 360, "y" : 203}, 
                                    "pos" : {"x" : spawn_pos_x, "y" : 0}, 
                                    "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                                    "animation_selected" : 0,
                                    "animations" : [{"file_index" : "zombies/basic/walk/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 77, 
                                                   "frame_duration" : 0.04}, 
                                    
                                                   {"file_index" : "zombies/basic/eat/(",
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 28, 
                                                   "frame_duration" : 0.04},
           
                                                   {"file_index" : "zombies/died/(", 
                                                   "file_type" : ").png", 
                                                   "start" : 0,
                                                   "total_frames" : 202, 
                                                   "frame_duration" : 0.04}]
                                    },
                    "Settings" : {"offset" : {"x" : 180, "y" : 0}, 
                                "ground_offset" : -68,
                                "speed" : 10,
                                "last_moved" : time.time(), 
                                "last_attacked" : time.time(), 
                                "blocked" : False, 
                                "health" : 200,
                                "dps" : 1,
                                "death_timer" : 1}
        },
           
           
"Cone" :  {"image" : {
                            "size" : {"x" : 360, "y" : 203}, 
                            "pos" : {"x" : spawn_pos_x, "y" : 0}, 
                            "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                            "animation_selected" : 0,
                            "animations" : [{"file_index" : "zombies/cone/walk/(", 
                                        "file_type" : ").png", 
                                        "start" : 0,
                                        "total_frames" : 85, 
                                        "frame_duration" : 0.04},
                            
                                        {"file_index" : "zombies/cone/eat/(",
                                        "file_type" : ").png", 
                                        "start" : 0,
                                        "total_frames" : 55, 
                                        "frame_duration" : 0.04},

                                        {"file_index" : "zombies/died/(", 
                                        "file_type" : ").png", 
                                        "start" : 0,
                                        "total_frames" : 202, 
                                        "frame_duration" : 0.04}]
                                        },
                                        "Settings" : {"offset" : {"x" : 180, "y" : 0}, 
                                                    "ground_offset" : -68,
                                                    "speed" : 10,
                                                    "last_moved" : time.time(), 
                                                    "last_attacked" : time.time(), 
                                                    "blocked" : False, 
                                                    "health" : 640,
                                                    "dps" : 1,
                                                    "death_timer" : 1}
            },
           
}

plants = {"Wallnut" : {"image" : {"size" : {"x" : 148, "y" : 125},"pos" : {"x" : 0, "y" : 0},"fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, "animation" : {"file_index" : "plants/wallnut/(", "file_type" : ").png","start" : 0,"total_frames" : 17, "frame_duration" : 0.08}}, "Settings" : {"offset" : {"x" : 30, "y" : 0}, "health" : 50}},
          "Peashooter" : {
                          "image" : {"size" : {"x" : 100, "y" : 100},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/peashooter/(", "file_type" : ").png", "start" : 0,"total_frames" : 49, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 15, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "amount" : 1, "health" : 5}},
          
          "Repeater" : {
                          "image" : {"size" : {"x" : 100, "y" : 100},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/repeater/(", "file_type" : ").png", "start" : 0,"total_frames" : 49, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "max_amount" : 2, "amount" : 1, "health" : 5}},
          
           "Gatlingpea" : {
                          "image" : {"size" : {"x" : 90, "y" : 85},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/gatlingpea/(", "file_type" : ").png", "start" : 0,"total_frames" : 13, "frame_duration" : 0.09}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : -15}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "max_amount" : 4, "amount" : 3, "health" : 5}},
          
          "Kernelpult" : {
                          "image" : {"size" : {"x" : 100, "y" : 82},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/kernelpult/(", "file_type" : ").png", "start" : 0,"total_frames" : 47, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : ["kernel", "butter"], "amount" : 1, "health" : 5}},
          "Cobcannon" : {
                          "image" : {"size" : {"x" : 176, "y" : 108},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/cobcannon/(", "file_type" : ").png", "start" : 0,"total_frames" : 11, "frame_duration" : 0.13}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 3, "last_shot" : 0, "projectile" : "cob", "amount" : 1, "health" : 5 }},
          
          "Spikeweed" : {
                          "image" : {"size" : {"x" : 80, "y" : 34},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/spikeweed/(", "file_type" : ").png", "start" : 0,"total_frames" : 38, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 3, "amount" : 1, "health" : 1000 }},
          
          "Torchwood" : {
                          "image" : {"size" : {"x" : 66, "y" : 90},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/torchwood/(", "file_type" : ").png", "start" : 0,"total_frames" : 82, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : -5, "y" : -30}, "health" : 5 }},
          
          "Spikerock" : {
                    "image" : {"size" : {"x" : 80, "y" : 34},
                                "pos" : {"x" : 0, "y" : 0},
                                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                "animation" : {"file_index" : "plants/spikerock/(", "file_type" : ").png", "start" : 0,"total_frames" : 33, "frame_duration" : 0.04}}, 
                    "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 3, "amount" : 1, "health" : 8000 }},
          
          "Sunflower" : {
                          "image" : {"size" : {"x" : 90, "y" : 95},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/sunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 54, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : -5, "y" : -30}, "amount" : 1, "health" : 5}},
          
          "Twinsunflower" : {
                          "image" : {"size" : {"x" : 83, "y" : 84},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/twinsunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 20, "frame_duration" : 0.09}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "amount" : 1, "health" : 5}}
}

for name in plants:
    plants[name]["Settings"]["name"] = name
for name in zombies:
    zombies[name]["Settings"]["name"] = name
projectile_height = 700
projectile_gravity = 98
projectiles = {"pea" : {"image" : {"name" : "plants/projectiles/pea.png", "size" : {"x" : 21, "y" : 21}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 65, "y" : 30}, "start_x" : 0, "start" : time.time(), "speed" : 150, "damage" : 20, "is_projectile" : False}},
               "lawnmower" : {"image" : {"name" : "Lawn Mower.png", "size" : {"x" : 80, "y" : 68}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "speed" : 250, "damage" : 69420, "is_projectile" : False}},
               "kernel" : {"image" : {"name" : "plants/projectiles/kernel.png", "size" : {"x" : 21, "y" : 22}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "damage" : 20, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}},
               "butter" : {"image" : {"name" : "plants/projectiles/butter.png", "size" : {"x" : 49, "y" : 50}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "damage" : 40, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}},
               "cob" : {"image" : {"name" : "plants/projectiles/cob.png", "size" : {"x" : 107, "y" : 50}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 200, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start_y" : 0, "start_velocity_y" : 0,  "start" : time.time(), "damage" : 20, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}}}

types = (type([]), type({}))
def copycollection(coll):
    is_list, is_dict = type(coll) == types[0], type(coll) == types[1]
    n = [copycollection(n) for n in coll] if is_list else ({} if is_dict else None)
    if n == None:
        return coll

    if is_dict:
        for ky in coll.keys():
            n[ky] = copycollection(coll[ky])

    return n



img_kys = ("name", "size", "pos", "fill", "animation", "animations", "animation_selected")
fallback = lambda dic, ky, default: dic[ky] if dic != None else default
def RENDERIMAGE(object, enabled_keys): #object is a dictionary, enabled_keys is a tuple storing all the keys that are in the object (assumed to be there)
    img = object["image"]
    img_name, img_size, pos, f, anim, anims, anim_selected = map(None, (img[ky] if ky in enabled_keys else None for ky in img_kys))
    if anims != None and anim_selected != None:
        anim = anims[anim_selected]
        
    if anim != None:
        fd, tf = anim["frame_duration"], anim["total_frames"], 
        elapsed = (time.time() - anim["start"]) % (tf * fd) if tf * fd > 0 else 1
        img_name = anim["file_index"] + str(int(elapsed/fd if fd > 0 else 1)) + anim["file_type"]

    if img_name == None:
        return
    xs, ys = fallback(img_size, "x", 100), fallback(img_size, "y", 100)
    tint(fallback(f, "r", 255), fallback(f, "g", 255), fallback(f, "b", 255), fallback(f, "a", 255))
    image(loadImage(img_name), fallback(pos, "x", -int(xs/2) if xs != None else 0), fallback(pos, "y", -int(ys/2) if ys != None else 0), xs, ys)   

sounds = {"tutorial" : {"minim" : "Cipher - Electronic Light.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "intro" : {"minim" : "The_Zombies_Are_Coming.mp3", "repeat" : 1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "seed" : {"minim" : "Choose Your Seeds.mp3", "repeat" : 1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "menu" : {"minim" : "Crazy Dave Intro Theme.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True,"group" : 0}, 
          "gameover" : {"minim" : "The Zombies Ate Your Brains.mp3", "repeat" : 0, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "grass" : {"minim" : "Grasswalk (In-Game).mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "fast" : {"minim" : "Plants vs Zombies Soundtrack [Mini Games].mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0},
          "brain" : {"minim" : "Brainiac Maniac.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0},
          "moon" : {"minim" : "Moongrains.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}}

sound_kys = ("minim", "repeat", "play_from_start", "isolate", "group")
def PlaySound(sound_name, enabled_keys):
    if not(sound_name in sounds.keys()):
        return
    
    sound = sounds[sound_name]
    m, repeat, play_from_start, isolate, group = map(None, (sound[ky] if ky in enabled_keys else None for ky in sound_kys))
    if m == None:
        return
    if isolate == True:
        for ky in sounds:
            if ky == sound_name:
                continue
            same_group = True if "group" in sounds[ky].keys() and sounds[ky]["group"] == group else False
            if same_group:
                sounds[ky]["minim"].pause()

    if m.isPlaying() == False:
        if play_from_start == True:
            m.rewind()
        if repeat == -1:
            m.loop()
        else:
            m.play()

removing = False
def RemovePlantMode():
    global removing
    removing = True
    
buttons = [ {"button" : {
    "mouse" : LEFT,
    "function" : RemovePlantMode,
    "area" : {"pos" : {"x" : 150, "y" : 30}, "pos2" : {"x" : 225, "y" : 105}}},
    
    "image" : {"name" : "buttons/Shovel.png",
               "size" : {"x" : 75, "y" : 75},
                "pos" : {"x" : 150, "y" : 30},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},       
]



plant_selected = None
def SELECTPLANT(name):
    global plant_selected
    print(name)
    plant_selected = name

def SELECTPEASHOOTER():
    SELECTPLANT("Peashooter")
def SELECTREPEATER():
    SELECTPLANT("Repeater")
def SELECTGATLINGPEA():
    SELECTPLANT("Gatlingpea")
def SELECTSUNFLOWER():
    SELECTPLANT("Sunflower")
def SELECTTWINSUNFLOWER():
    SELECTPLANT("Twinsunflower")
def SELECTWALLNUT():
    SELECTPLANT("Wallnut")
def SELECTTORCHWOOD():
    SELECTPLANT("Torchwood")
def SELECTSPIKEWEED():
    SELECTPLANT("Spikeweed")
def SELECTSPIKEROCK():
    SELECTPLANT("Spikerock")
def SELECTKERNELPULT():
    SELECTPLANT("Kernelpult")
def SELECTCOBCANNON():
    SELECTPLANT("Cobcannon")

list_x, list_y, list_y_increment = 10, 30, 80

sidebar = [
    {"button" : {"mouse" : LEFT, "function" : SELECTSUNFLOWER, "area" : {"pos" : {"x" : 10, "y" : 160}, "pos2" : {"x" : 116, "y" : 246}}}, "image" : {"name" : "icons/sunflower.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 160}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},       
    {"button" : {"mouse" : LEFT, "function" : SELECTTWINSUNFLOWER, "area" : {"pos" : {"x" : 10, "y" : 160}, "pos2" : {"x" : 116, "y" : 246}}}, "image" : {"name" : "icons/twinsunflower.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 160}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},     
    {"button" : {"mouse" : LEFT, "function" : SELECTPEASHOOTER, "area" : {"pos" : {"x" : 10, "y" : 0}, "pos2" : {"x" : 116, "y" : 66}}}, "image" : {"name" : "icons/peashooter.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 100000, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},    
    {"button" : {"mouse" : LEFT, "function" : SELECTREPEATER, "area" : {"pos" : {"x" : 10, "y" : 0}, "pos2" : {"x" : 116, "y" : 66}}}, "image" : {"name" : "icons/repeater.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 100000, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTGATLINGPEA, "area" : {"pos" : {"x" : 10, "y" : 0}, "pos2" : {"x" : 116, "y" : 66}}}, "image" : {"name" : "icons/gatlingpea.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 100000, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTWALLNUT, "area" : {"pos" : {"x" : 10, "y" : 80}, "pos2" : {"x" : 116, "y" : 146}}}, "image" : {"name" : "icons/wallnut.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 80}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTTORCHWOOD,"area" : {"pos" : {"x" : 10, "y" : 160}, "pos2" : {"x" : 116, "y" : 246}}}, "image" : {"name" : "icons/torchwood.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 160}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTSPIKEWEED, "area" : {"pos" : {"x" : 10, "y" : 240}, "pos2" : {"x" : 116, "y" : 306}}}, "image" : {"name" : "icons/spikeweed.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 240}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTSPIKEROCK, "area" : {"pos" : {"x" : 10, "y" : 240}, "pos2" : {"x" : 116, "y" : 306}}}, "image" : {"name" : "icons/spikerock.png", "size" : {"x" : 106, "y" : 66}, "pos" : {"x" : 10, "y" : 240}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTKERNELPULT, "area" : {"pos" : {"x" : 10, "y" : 240}, "pos2" : {"x" : 116, "y" : 306}}},"image" : {"name" : "icons/kernelpult.png","size" : {"x" : 106, "y" : 66},"pos" : {"x" : 10, "y" : 240},"fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}},
    {"button" : {"mouse" : LEFT, "function" : SELECTCOBCANNON, "area" : {"pos" : {"x" : 10, "y" : 320}, "pos2" : {"x" : 116, "y" : 386}}}, "image" : {"name" : "icons/cobcannon.png","size" : {"x" : 106, "y" : 66},"pos" : {"x" : 10, "y" : 320},"fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}}}]
bar_size = 7
selector_x, selector_y, is_selected = -10000, -10000, False
def ReloadSelector(x, y, name, visible):
    global selector_x, selector_y, is_selected
    if plant_selected != None and name == plant_selected.lower():
        selector_x, selector_y = x, y
        is_selected = visible
    
def SideBar(column_size, offset):
    global sidebar, is_selected, plant_selected, selector_x, selector_y
    for i, button in enumerate(sidebar[offset:] + sidebar[:offset]): 
        x, y = list_x, list_y + list_y_increment * i 
        ReloadSelector(x, y, button["image"]["name"][6:len(button["image"]["name"]) - 4], i < column_size)
        if i < column_size:
            for c in button["image"]["fill"].keys():
                button["image"]["fill"][c] = 255
           
            x2, y2 = button["image"]["size"]["x"], y + button["image"]["size"]["y"]
            button["image"]["pos"]["x"], button["button"]["area"]["pos"]["x"] = x, x
            button["image"]["pos"]["y"], button["button"]["area"]["pos"]["y"] = y, y
            button["button"]["area"]["pos2"]["x"], button["button"]["area"]["pos2"]["y"] = x2, y2
        else:
            for c in button["image"]["fill"].keys():
                button["image"]["fill"][c] = 0

shift = 0
SideBar(bar_size, 0)
def mouseWheel(event):
    global shift, plant_selected
    if abs(shift) <= len(sidebar) - 2:
        shift += event.getCount()  
    else:
        shift = 0
        
    SideBar(bar_size, shift)
    
    
button_kys = ("area", "function", "mouse")
fallback = lambda dic, ky, default: dic[ky] if dic != None else default

def TriggerButtonPress(object):
    button = object["button"]
    a, f, m = fallback(button, "area", None), fallback(button, "function", None), fallback(button, "mouse", None)
    p, p2 = fallback(a, "pos", None), fallback(a, "pos2", None)
    x, y, x2, y2 = fallback(p, "x", 0), fallback(p, "y", 0), fallback(p2, "x", 0), fallback(p2, "y", 0)
    if min(x, x2) <= mouseX <= max(x, x2) and min(y, y2) <= mouseY <= max(y, y2):
        if f != None and mouseButton == m:
            f()

mouse_presses = 0
def mousePressed():
    for object in buttons:
        TriggerButtonPress(object)
    for object in sidebar:
        if object["image"]["fill"]["a"] > 0:
            TriggerButtonPress(object)

def mouseReleased():
    global mouse_presses, sidebar, shift
    mouse_presses += 1
    for i, object in enumerate(sidebar[shift:] + sidebar[:shift]):
        x, y = list_x, list_y + list_y_increment * i 
        visible = object["image"]["fill"]["a"] > 0
        ReloadSelector(x, y, object["image"]["name"][6:len(object["image"]["name"]) - 4], visible)

upgradable_plants = {"Gatlingpea" : "Repeater", "Spikerock" : "Spikeweed", "Cobcannon" : "Kernelpult", "Twinsunflower" : "Sunflower"}
can_place_cobcannon = lambda x, y: rows[y]["Plants"][x - 1]["Settings"]["name"] == "Kernelpult" if x - 1 > -1 and rows[y]["Plants"][x - 1] != None else False
can_place = lambda x, y, type: rows[y]["Plants"][x] == None if not(type in upgradable_plants.keys()) else rows[y]["Plants"][x] != None and rows[y]["Plants"][x]["Settings"]["name"] == upgradable_plants[type] and (type != "Cobcannon" or can_place_cobcannon(x, y)) 

can_detect_plant = lambda settingz, target_plant : target_plant != None and (settingz["name"] == "Zamboni" or settingz["name"] == "Gargantuar" or (target_plant["Settings"]["name"] != "Spikerock" and target_plant["Settings"]["name"] != "Spikeweed"))                                                                                                                                                                            

def Spawn(object, row, column, is_zombie): 
    new = copycollection(object)
    if is_zombie:
        new["Settings"]["last_moved"] = time.time()
        for i in range(len(new["image"]["animations"])):
            new["image"]["animations"][i]["start"] = random.randint(0, 10000)
        rows[row]["Zombies"].append(new)
    else:
        settingp, imagp  = new["Settings"], new["image"]
        imagp["pos"]["y"] = column_pos[row + 1] + settingp["offset"]["y"] - imagp["size"]["y"]
        imagp["pos"]["x"] = row_pos[column + 1] + settingp["offset"]["x"] - imagp["size"]["x"]
        rows[row]["Plants"][column] = new
        if settingp["name"] == "Cobcannon":
            rows[row]["Plants"][column - 1] = new
        imagp["animation"]["start"] = random.randint(0, 10000)

def Zombies(i, row):
    global rows
    for ii, zombie in enumerate(row["Zombies"]):    
            settingz, imagz = zombie["Settings"], zombie["image"]
            imagz["pos"]["y"] = column_pos[i + 1] + settingz["offset"]["y"] - imagz["size"]["y"]
            elapsed = time.time() - settingz["last_moved"]
            zombie["Settings"]["last_moved"] = time.time()
            x, y = GetLocation(imagz["pos"]["x"] + settingz["offset"]["x"], imagz["pos"]["y"] + imagz["size"]["y"] + settingz["ground_offset"]) #x + 1 so the zombie target plants infront and in the current tile
            
            target_plant = None if x == None or y == None else rows[y]["Plants"][x]
            if not(can_detect_plant(settingz, target_plant)):
                target_plant = None
                
            if target_plant == None:
                targest_plant = None if x == None or y == None or x + 1 >= len(rows[y]["Plants"]) else rows[y]["Plants"][x + 1]

            if not(can_detect_plant(settingz, target_plant)):
                target_plant = None
            
            
                
            if settingz["health"] > 0:    
                if target_plant != None:
                    special_damage = settingz["name"] == "Zamboni" and (target_plant["Settings"]["name"] == "Spikeweed" or target_plant["Settings"]["name"] == "Spikerock")
                    if special_damage:
                        settingz["health"] = 0
                        target_plant["Settings"]["health"] -= settingz["dps"]
                    else:
                        target_plant["Settings"]["health"] -= (time.time() - settingz["last_attacked"]) * settingz["dps"]
                    if target_plant["Settings"]["health"] <= 0:
                        rows[y]["Plants"][x] = None
                        
                settingz["blocked"] = True if target_plant != None else False
                if not(settingz["blocked"]):
                    imagz["pos"]["x"] -= settingz["speed"] * elapsed        
                    imagz["animation_selected"] = 0
                else:
                    imagz["animation_selected"] = 1
            
                
            if settingz["health"] <= 0:
                imagz["animation_selected"] = 2
                if settingz["health"] <= 0 and settingz["death_timer"] == 1:
                    imagz["animations"][2]["start"] = time.time()
                    settingz["death_timer"] = time.time() + (imagz["animations"][2]["total_frames"] - 1) * imagz["animations"][2]["frame_duration"]

            settingz["last_attacked"] = time.time()
            RENDERIMAGE(zombie, ("animations", "animation_selected", "pos", "size", "fill"))
            
            global ice, ice_offset
            if settingz["name"] == "Zamboni":
                if imagz["pos"]["x"] + ice_offset < ice[i]:
                    ice[i] = imagz["pos"]["x"] + ice_offset
            
            
    index = 0
    while index < len(row["Zombies"]):
        settingz = row["Zombies"][index]["Settings"]
        if settingz["health"] <= 0 and settingz["death_timer"] - time.time() <= 0:
            row["Zombies"].pop(index)
        else:
            index += 1

def Plants(i, row):
    global rows
    for ii, plant in enumerate(row["Plants"]):
            if not(plant):
                continue

            settingp, imagp  = plant["Settings"], plant["image"]
                
            if "last_shot" in settingp.keys() and time.time() >= settingp["last_shot"] + settingp["reload_time"] and len(rows[i]["Zombies"]) > 0: 
                if "max_amount" in settingp.keys():
                    settingp["amount"] = settingp["amount"] + 1 if settingp["amount"] < settingp["max_amount"] - 1 else 0
                    settingp["reload_time"] = 0.4 if settingp["amount"] < settingp["max_amount"] - 1 else 1.5
                    
                settingp["last_shot"] = time.time()
                projectile = settingp["projectile"] if type(settingp["projectile"]) == type("") else settingp["projectile"][0 if random.randint(1, 100) <= 75 else 1]
                new_projectile = copycollection(projectiles[projectile])
                new_settings, new_image = new_projectile["Settings"], new_projectile["image"]
                new_settings["offset"]["x"] += settingp["projectile_offset"]["x"] 
                new_settings["offset"]["y"] += settingp["projectile_offset"]["y"] 
                new_settings["start"] = time.time()
                new_settings["start_x"], new_settings["start_y"]  = imagp["pos"]["x"] + new_settings["offset"]["x"], imagp["pos"]["y"] + new_settings["offset"]["y"]
                new_image["pos"]["y"] = new_settings["start_y"]
                if new_settings["is_projectile"]:
                    new_settings["velocity"]["y"] = -(2*projectile_gravity*projectile_height)**0.5
                    new_settings["start_velocity_y"] = new_settings["velocity"]["y"]
                    new_settings["total_time"] = (-new_settings["velocity"]["y"]/projectile_gravity) + ((2.0*projectile_height)/projectile_gravity)**0.5
                    
                    closest, closest_y = 10**16, new_image["pos"]["y"]
                    for zombie in row["Zombies"]:
                        settingz, imagz = zombie["Settings"], zombie["image"]
                        d = imagz["pos"]["x"] + imagz["size"]["x"]/2.0 - settingz["speed"] * new_settings["total_time"]*0.5 #+ imagz["size"]["x"]  #projectile_time
                        closest = min(closest, d) if d > new_settings["start_x"] else closest
                        closest_y = settingz["offset"]["y"] if d > new_settings["start_x"] else closest_y
                    new_settings["velocity"]["x"] = ((closest - new_settings["start_x"])/new_settings["total_time"])*2
                    new_settings["target"]["x"], new_settings["target"]["y"] = closest, closest_y
                rows[i]["Projectiles"].append(new_projectile)
            
            RENDERIMAGE(plant, ("animation", "pos", "size", "fill"))
instakill = False
def Projectiles(i, row):
    global rows, instakill
    remove_indexes = []
    angle = 0
    for ii, projectile in enumerate(row["Projectiles"]):
            setting, imagp = projectile["Settings"], projectile["image"]
            flying = False
            already_removed = False
            if setting["is_projectile"] == False:
                imagp["pos"]["x"] = setting["start_x"] + (time.time() - setting["start"]) * setting["speed"]
            else:
                delta_time = time.time() - setting["start"]
                flying = delta_time <= setting["total_time"]*0.5
                imagp["pos"]["x"] = setting["velocity"]["x"]*delta_time + setting["start_x"]
                imagp["pos"]["y"] = setting["velocity"]["y"]*delta_time + setting["start_y"]  #+ projectile_gravity/2*delta_time**2 + imagp["pos"]["y"]
                setting["velocity"]["y"] = setting["start_velocity_y"] + projectile_gravity*delta_time
                angle = atan((setting["velocity"]["y"] + 0.0)/setting["velocity"]["x"]) 
                if setting["velocity"]["y"] > setting["start_velocity_y"]/2.0:
                    angle = radians(90) + atan((setting["velocity"]["y"] + 0.0)/(setting["target"]["x"] - imagp["pos"]["x"])) if (setting["target"]["x"] - imagp["pos"]["x"]) != 0 else 0
                
                pushMatrix()
                translate(imagp["pos"]["x"], imagp["pos"]["y"])
                rotate(angle)
                if imagp["pos"]["y"] + setting["offset"]["y"] > column_pos[i + 1]:
                    already_removed = True
                    remove_indexes.append(ii)
            if not(flying):
                if imagp["name"] == "plants/projectiles/pea.png":
                    crossed = False
                    for c, plant in enumerate(row["Plants"]):
                        if plant != None and plant["Settings"]["name"] == "Torchwood" and (c, i) == GetLocation(imagp["pos"]["x"], imagp["pos"]["y"] + imagp["size"]["y"]):
                            imagp["name"] = "plants/projectiles/firepea.png"
                            setting["damage"] *= 2
                
                closest_setting, closest = None, 10**6
                for zombie in row["Zombies"]:
                    settingz, imagz = zombie["Settings"], zombie["image"]
                    x_pos = imagz["pos"]["x"] + settingz["offset"]["x"] 
                    can_hit = setting["start_x"] <= x_pos <= imagp["pos"]["x"]
                    can_reach = setting["is_projectile"] and setting["start_x"] <= x_pos + imagz["size"]["x"] <= imagp["pos"]["x"]
                    d = x_pos - setting["start_x"]
                    if can_hit or can_reach:
                        if imagp["name"] == "Lawn Mower.png":
                            settingz["health"] = 0 
                            continue
                        closest_setting = settingz
                        
                if closest_setting != None:
                    if not(already_removed):
                        
                        remove_indexes.append(ii)
                    closest_setting["health"] -= setting["damage"] if not(instakill) else 69420
                    
            if not(already_removed):
                RENDERIMAGE(projectile, ("name", "size", "pos" if not(setting["is_projectile"]) else ""))
            if setting["is_projectile"]:    
                popMatrix()

            
    index, r = 0, 0
    while len(remove_indexes) > 0:
        if index + r == remove_indexes[0]:
            row["Projectiles"].pop(index)
            remove_indexes.pop(0)
            r += 1
        else:
            index += 1
            
transition_time = 9

def Restart():
    global rows, gameover, played_gameover_sound, amplifier, waves_completed, ice, mowers_left, last_melted, continue_wave
    gameover = False
    played_gameover_sound = False
    
    amplifier = 1 #Maybe hard waves run after every 3 easy waves
    waves_completed = 0

    last_melted = time.time()
    mowers_left = [True for i in range(len(column_pos))]
    ice = [10**16 for _ in range(len(column_pos) - 1)]
    rows = list([{"Plants" : [None for ii in range(len(row_pos) - 1)], "Projectiles" : [], "Zombies" : []} for i in range(len(column_pos) - 1)])
    continue_wave = False
Restart()
def Gameover():
    global gameover, transition_time, played_gameover_sound
    if not(played_gameover_sound):
        PlaySound("gameover", ("minim", "repeat", "play_from_start", "isolate", "group"))  
        played_gameover_sound = True 
    fill(0, 0, 0, 127)
    rect(0, 0, 1000, 1000)
    tint(255, 255, 255, min(1, ((time.time() - gameover)/transition_time)) * 255)
    image(loadImage("messages/Gameover.png"), 218, 67, 564, 466)
    
    if (time.time() - gameover)/transition_time >= 1:
        if keyPressed and key == "r":
            Restart()
def LawnMower():
    global mowers_left, rows, projectiles, gameover
    for x, row in enumerate(rows):  
        if mowers_left[x] == True:
            image(loadImage("Lawn Mower.png"), 180, column_pos[x], 80, 68)
        
        if gameover:
            continue
        
        for zombie in row["Zombies"]:
            
            
            settingz, imagz = zombie["Settings"], zombie["image"]
            x_pos = settingz["offset"]["x"] + imagz["pos"]["x"]
            if x_pos < row_pos[0] and settingz["health"] > 0:
                if mowers_left[x] != True:
                    gameover = time.time()
                    return
                na, y = GetLocation(row_pos[0], imagz["pos"]["y"] + imagz["size"]["y"] + settingz["ground_offset"])
                if y != None:
                    settingz["health"] = 0
                    new_mower = copycollection(projectiles["lawnmower"])
                    new_mower["Settings"]["start_x"], new_mower["image"]["pos"]["y"] = 180, column_pos[y]
                    new_mower["Settings"]["start"] = time.time()
                    rows[y]["Projectiles"].append(new_mower)
                    mowers_left[y] = False
                    break
        

def Ice():
    global ice, melt_rate, last_melted
    delta_time = time.time() - last_melted
    for i, pos in enumerate(ice):
        ice[i] -= delta_time * melt_rate
        image(loadImage("ice.png"), pos, column_pos[i]+(column_pos[i+1] - column_pos[i] - 77)/2.0, 794, 77)
    last_melted = time.time()

def GetLocation(ax, ay):
    for y, y_pos in enumerate(column_pos):
        for x, x_pos in enumerate(row_pos):
            if y + 1 == len(column_pos) or x + 1 == len(row_pos):
                break
            if x_pos <= ax < row_pos[x + 1] and y_pos <= ay < column_pos[y + 1]:
                return x, y
    return None, None

wave_message = "Waves Completed" 
wave = None
wave_duration = 10 #45
spawn_cooldown = 1
start_cooldown = 6
start_wave = -1
def StartWave():
    global amplifier, waves_completed, easy_waves, hard_waves, wave, spawn_cooldown, start_wave, start_cooldown
    is_hard = (waves_completed + 1)%4 == 0
    wave = copycollection(hard_waves[random.randint(0, len(hard_waves) - 1)] if is_hard else easy_waves[random.randint(0, len(easy_waves) - 1)])
    total_zombies = 0
    for ky in wave:
        if ky == "sound":
            continue
        wave[ky] *= amplifier
        total_zombies += wave[ky]
    spawn_cooldown = (wave_duration + 0.0)/total_zombies
    start_wave = time.time() + start_cooldown
StartWave() #You can rig this to a start button later on

def setup():
    size(1000, 600)
    minim = Minim(this)
    for ky in sounds:
        sounds[ky]["minim"] = minim.loadFile("sounds/" + sounds[ky]["minim"])
    PlaySound("intro", ("minim", "repeat", "play_from_start", "isolate", "group"))
    font = createFont("SERIO___.TTF", 24)
    textFont(font)
cooldown = time.time()
start_music = time.time() + 6
projectile_removed = time.time()
projectile_remove_cooldown = 10
state = "title"

def draw():
    global rows, cooldown, projectile_removed, plant_selected, is_selected, state, s, yv, start_music, removing, mouse_presses, selector_x, selector_y, gameover, wave
    copy(loadImage("Lawn.png" if wave == None or wave["sound"] != "moon" else "LawnNight.png"), 0, 0, 1400, 600, 0, 0, 1400, 600)
    tint(255, 255, 255, 255)
    Ice() 
    LawnMower()
    for i, row in enumerate(rows):
        Plants(i, row)
        Zombies(i, row)
        Projectiles(i, row)
    
    for object in sidebar:
        RENDERIMAGE(object, ("name", "fill", "size", "pos"))  
    for object in buttons:
        RENDERIMAGE(object, ("name", "fill", "size", "pos"))   
    
    if plant_selected != None and is_selected:
        image(loadImage("selector.png"), selector_x, selector_y, 106, 66)
    
    if gameover > 0:
        Gameover()
        return    
    
    global spawn_cooldown, waves_completed, max_amplifier, amplifier, start_wave, continue_wave
    print(start_wave <= time.time(), wave if wave != None else None, waves_completed, continue_wave)
    if continue_wave:
        PlaySound("seed", ("minim", "repeat", "play_from_start", "isolate", "group"))      
        if keyPressed and key == "c":
            continue_wave = False
            waves_completed += 1
            amplifier = min(max_amplifier, amplifier * amplifier_rate)
            StartWave()
        return
    
    if start_wave != -1 and start_wave <= time.time() and wave != None and time.time() > cooldown:
        PlaySound(wave["sound"], ("minim", "repeat", "play_from_start", "isolate", "group"))      
        kys = list(wave.keys())
        kys.remove("sound")
        for ky in kys:
            if int(wave[ky]) <= 0:
                wave.pop(ky)
        kys = list(wave.keys())
        kys.remove("sound")
        if len(kys) <= 0:
            no_zombies = True
            for row in rows:
                if len(row["Zombies"]) > 0:
                    no_zombies = False
                    break
                
            continue_wave = no_zombies
        else:
            cooldown = time.time() + spawn_cooldown
            selected_type = kys[random.randint(0, len(kys) - 1)]
            wave[selected_type] -= 1
            Spawn(zombies[selected_type], random.randint(0,4), None, True)
           
    if time.time() >= projectile_removed + projectile_remove_cooldown:
        projectile_removed = time.time()
        for row in rows:
            i = 0
            while i < len(row["Projectiles"]):
                if row["Projectiles"][i]["image"]["pos"]["x"] > width:
                    row["Projectiles"].pop(i)
                else:
                    i += 1
    x, y = GetLocation(mouseX, mouseY)
    if x != None and y != None:
        noStroke()
        fill(0, 0, 0, 50)
        rect(row_pos[x], column_pos[0], row_pos[x + 1] - row_pos[x], column_pos[len(column_pos) - 1])
        rect(row_pos[0], column_pos[y], row_pos[len(row_pos) - 1], column_pos[y + 1] - column_pos[y])
        fill(255, 255, 255, 120)
        rect(row_pos[x], column_pos[y], row_pos[x + 1] - row_pos[x], column_pos[y + 1] - column_pos[y])
        if removing:
            image(loadImage("shovel.png"), mouseX, mouseY - 75, 75, 75) 
        if mousePressed and mouseButton == LEFT and mouse_presses%2 == 0:
            mouse_presses += 1
            if removing:
                if x - 1 > -1 and rows[y]["Plants"][x - 1] == rows[y]["Plants"][x]:
                    rows[y]["Plants"][x - 1] = None
                elif x + 1 < len(row_pos) - 1 and rows[y]["Plants"][x + 1] == rows[y]["Plants"][x]:
                    rows[y]["Plants"][x + 1] = None
                rows[y]["Plants"][x] = None
            elif plant_selected != None and is_selected and can_place(x, y, plant_selected) and row_pos[x + 1] < ice[y]:
                Spawn(plants[plant_selected], y, x, False) 
            removing = False
    fill(231, 191, 96, 255)
    textAlign(CENTER)
    text(str(waves_completed) + " Waves Completed", 300, 550, 400, 600)
    
