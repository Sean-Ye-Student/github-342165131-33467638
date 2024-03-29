import time #Importing time, random and minim modules / libraries
import random
add_library("minim")
spawn_pos_x = 900 # Offsets the zombies to the end of the map
column_pos = (80,183,279,385,467, 573) #The borders between rows from the very top to the very bottom
row_pos = (251, 334, 408, 493, 576, 654, 738, 812, 898, 987) #The borders between columns from the very left to the very right
ice_offset = 50 #Controls the ice's offset from the zamboni and the rate at which it melts
melt_rate = -3
max_amplifier = 40 #Maximum difficulty
max_easy_amplifier = 11 #Maximum difficuty for an easy wave, reduces lag as the easier waves generally have more zombies
amplifier_rate = max_amplifier**(1.0/8.0) #Will reach max_amplifier in 8 waves
easy_waves = [{"sound" : "grass", "Basic" : 2, "Cone" : 0.8}, #total hp ~800 
              {"sound" : "grass2", "Basic" : 1, "Cone" : 0.4, "Bucket" : 0.2},
              {"sound" : "grass3", "Basic" : 0.6, "Cone" : 0.2, "Bucket" : 0.4},
              {"sound" : "grass3", "Basic" : 1.6, "Bucket" : 0.4},
              {"sound" : "grass2", "Basic" : 1, "Cone" : 1},
              {"sound" : "grass", "Cone" : 0.4, "Bucket" : 0.4, "Basic" : 0.7}]

hard_waves = [{"sound" : "fast", "Zamboni" : 0.375, "Football" : 0.375}, #total hp ~1600
              {"sound" : "brain", "Gargantuar" : 0.5,  "Basic" : 1},
              {"sound" : "moon", "Bucket" : 0.375, "Door" : 0.375},
              {"sound" : "moon", "Bucket" : 0.3, "Football" : 0.45},
              {"sound" : "moon", "Door" : 0.3, "Football" : 0.45},
              {"sound" : "brain", "Gargantuar" : 0.25,  "Cone" : 0.25, "Bucket" : 0.2, "Basic" : 0.05},
              {"sound" : "fast", "Zamboni" : 0.4, "Gargantuar" : 0.3, "Basic" : 0.05}]

zombies = {"Zamboni" : {"image" : {"size" : {"x" : 185, "y" : 185}, "pos" : {"x" : spawn_pos_x + 185, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
                         "animations" : [{"file_index" : "zombies/zamboni/walk/(", #Dictionary with all the zombies
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
          "Peashooter" : { #Dictionary of all the plants
                          "image" : {"size" : {"x" : 100, "y" : 100},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/peashooter/(", "file_type" : ").png", "start" : 0,"total_frames" : 49, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 15, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "health" : 5}},
          
          "Repeater" : {
                          "image" : {"size" : {"x" : 100, "y" : 100},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/repeater/(", "file_type" : ").png", "start" : 0,"total_frames" : 49, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 0, "max_reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "max_amount" : 2, "amount" : 0, "health" : 5}},
          
           "Gatlingpea" : {
                          "image" : {"size" : {"x" : 90, "y" : 85},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/gatlingpea/(", "file_type" : ").png", "start" : 0,"total_frames" : 13, "frame_duration" : 0.09}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : -15}, "reload_time" : 0, "max_reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "max_amount" : 4, "amount" : 0, "health" : 5}},
          
          "Kernelpult" : {
                          "image" : {"size" : {"x" : 100, "y" : 82},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/kernelpult/(", "file_type" : ").png", "start" : 0,"total_frames" : 47, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : ["kernel", "butter"], "health" : 5}},
          "Cobcannon" : {
                          "image" : {"size" : {"x" : 176, "y" : 108},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/cobcannon/(", "file_type" : ").png", "start" : 0,"total_frames" : 11, "frame_duration" : 0.13}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 12, "last_shot" : 0, "projectile" : "cob", "health" : 5 }},
          
          "Spikeweed" : {
                          "image" : {"size" : {"x" : 80, "y" : 34},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/spikeweed/(", "file_type" : ").png", "start" : 0,"total_frames" : 38, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 3, "health" : 1000 }},
          
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
                    "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "reload_time" : 3, "health" : 8000 }},
          
          "Sunflower" : {
                          "image" : {"size" : {"x" : 90, "y" : 95},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/sunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 54, "frame_duration" : 0.03}},  #24
                          "Settings" : {"offset" : {"x" : -5, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "health" : 5, "reload_time" : 24, "last_shot" : 0, "projectile" : "sun"}},
          
          "Twinsunflower" : {
                          "image" : {"size" : {"x" : 83, "y" : 84},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/twinsunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 20, "frame_duration" : 0.09}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "projectile_offset" : {"x" : 0, "y" : 0}, "amount" : 0, "max_amount" : 2, "health" : 5, "reload_time" : 0, "max_reload_time" : 24, "last_shot" : 0, "projectile" : "sun"}}
}

for name in plants: #Sets the name in the plants settings to be the reference key 
    plants[name]["Settings"]["name"] = name
for name in zombies:
    zombies[name]["Settings"]["name"] = name
projectile_height = 700 #Used to control the properties of the projectile motion attacks
projectile_gravity = 98
projectiles = {"sun" : {"image" : {"name" : "plants/projectiles/sun.png", "size" : {"x" : 60, "y" : 60}, "pos" : {"x" : 0, "y" : 0}}}, #Dictionary of the projectile and their properties
               "pea" : {"image" : {"name" : "plants/projectiles/pea.png", "size" : {"x" : 21, "y" : 21}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 65, "y" : 30}, "start_x" : 0, "start" : time.time(), "speed" : 150, "damage" : 20, "is_projectile" : False}},
               "lawnmower" : {"image" : {"name" : "plants/projectiles/Lawn Mower.png", "size" : {"x" : 80, "y" : 68}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "speed" : 250, "damage" : 69420, "is_projectile" : False}},
               "kernel" : {"image" : {"name" : "plants/projectiles/kernel.png", "size" : {"x" : 21, "y" : 22}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "damage" : 20, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}},
               "butter" : {"image" : {"name" : "plants/projectiles/butter.png", "size" : {"x" : 49, "y" : 50}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 0, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "damage" : 40, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}},
               "cob" : {"image" : {"name" : "plants/projectiles/cob.png", "size" : {"x" : 107, "y" : 50}, "pos" : {"x" : 0, "y" : 0}}, "Settings" : {"offset" : {"x" : 200, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start_y" : 0, "start_velocity_y" : 0,  "start" : time.time(), "damage" : 69420, "is_projectile" : True, "target" : {"x" : 0, "y" : 0}}}}

types = (type([]), type({})) 
def copycollection(coll): #Used to copy a collection without initial reference
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
def RENDERIMAGE(object, enabled_keys): #Renders image dictionaries
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
#List of all the ingame sounds, with their properties
sounds = {"tutorial" : {"minim" : "Cipher - Electronic Light.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "intro" : {"minim" : "The_Zombies_Are_Coming.mp3", "repeat" : 1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "seed" : {"minim" : "Choose Your Seeds.mp3", "repeat" : 1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "menu" : {"minim" : "Crazy Dave Intro Theme.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True,"group" : 0}, 
          "gameover" : {"minim" : "The Zombies Ate Your Brains.mp3", "repeat" : 0, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "grass" : {"minim" : "Grasswalk (In-Game).mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "grass2" : {"minim" : "Watery Graves.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "grass3" : {"minim" : "Rigor Mormist.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, 
          "fast" : {"minim" : "Plants vs Zombies Soundtrack [Mini Games].mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0},
          "brain" : {"minim" : "Brainiac Maniac.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0},
          "moon" : {"minim" : "Moongrains.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0},
          "sun" : {"minim" : "Sun.mp3", "play_from_start" : True},
          "error" : {"minim" : "Error.mp3", "play_from_start" : True}}

sound_kys = ("minim", "repeat", "play_from_start", "isolate", "group")
def PlaySound(sound_name, enabled_keys): #Plays a specific sound following its properties
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
def RemovePlantMode(): #Enables the removing plant mode
    global removing
    removing = True

tutorial = False
def OpenTutorial(): #Opens the tutorial almanac
    global tutorial, continue_wave
    tutorial = continue_wave
    
def ContinueWaves(): #Starts the next wave
    global continue_menu, continue_wave, amplifier, max_amplifier, amplifier_rate, waves_completed, tutorial
    if not(continue_wave) or tutorial or continue_menu:
        return
    continue_wave = False
    amplifier = min(max_amplifier, amplifier * amplifier_rate) if waves_completed > 0 else 1
    StartWave()
buttons = [ {"button" : { #Dictionary of all the buttons and their properties
    "mouse" : LEFT,
    "function" : RemovePlantMode,
    "area" : {"pos" : {"x" : 130, "y" : 30}, "pos2" : {"x" : 205, "y" : 105}}},
    
    "image" : {"name" : "buttons/Shovel.png",
               "size" : {"x" : 75, "y" : 75},
                "pos" : {"x" : 130, "y" : 30},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},              

    {"button" : {
    "mouse" : LEFT,
    "function" : OpenTutorial,
    "area" : {"pos" : {"x" : 915, "y" : 30}, "pos2" : {"x" : 990, "y" : 105}}},
    
    "image" : {"name" : "buttons/Tutorial.png",
            "size" : {"x" : 75, "y" : 75},
                "pos" : {"x" : 915, "y" : 30},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }}, 
    
  
    {"button" : {
    "mouse" : LEFT,
    "function" : ContinueWaves,
    "area" : {"pos" : {"x" : 775, "y" : 485}, "pos2" : {"x" : 980, "y" : 526}}},
    
    "image" : {"name" : "buttons/continue.png",
               "size" : {"x" : 205, "y" : 41},
                "pos" : {"x" : 775, "y" : 485},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},      
]



plant_selected = None
def SELECTPLANT(name): #Assigns the selected plant
    global plant_selected
    #print(name)
    plant_selected = name
#Used to select a specific plant from the sidebar
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
#Constants for offseting the sidebar / spacing
list_x, list_y, list_y_increment, list_x_increment = 10, 30, 80, 120

sidebar = [ #List of all the plants in the sidebar
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
bar_size = 7 #The amount of plants displayed on the sidebar

selector_x, selector_y = -10000, -10000 #The position of the selector indicator
def EditSidebarButton(button, x, y, a): #Changes the position of a specific button
    global sidebar
    button["image"]["fill"]["a"] = a
    if a <= 0:
        return
    
    x2, y2 = x + button["image"]["size"]["x"], y + button["image"]["size"]["y"]
    button["image"]["pos"]["x"], button["button"]["area"]["pos"]["x"] = x, x
    button["image"]["pos"]["y"], button["button"]["area"]["pos"]["y"] = y, y
    button["button"]["area"]["pos2"]["x"], button["button"]["area"]["pos2"]["y"] = x2, y2
    
def ReloadSelector(x, y, name, visible): #Relocates the selector indicator
    global selector_x, selector_y
    if plant_selected != None and name == plant_selected.lower():
        selector_x, selector_y = x, y
#"Wallnut" : {"image" : {"size" : {"x" : 148, "y" : 125},"pos" : {"x" : 0, "y" : 0},"fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, "animation" : {"file_index" : "plants/wallnut/(", "file_type" : ").png","start" : 0,"total_frames" : 17, "frame_duration" : 0.08}}, "Settings" : {"offset" : {"x" : 30, "y" : 0}, "health" : 50}
def TutorialGrid(): #Renders the almanac
    global sidebar, plant_selected, selector_x, selector_y, tutorial_start, font, font2
    rows, columns = 2, 4
    
    if plant_selected != None:
        plant = plants[plant_selected]
        pos, s, offset = plant["image"]["pos"], plant["image"]["size"], plant["Settings"]["offset"]
        cob_offset = 45 if plant_selected == "Cobcannon" else 0
        pos["x"], pos["y"] = 818 + offset["x"] - s["x"] + cob_offset, 245 + offset["y"] -  s["y"]
        RENDERIMAGE(plants[plant_selected], ("animation", "pos", "size", "fill"))
        
        f = open("tutorial/almanac.txt", "r")
        lines = f.readlines()
        names = lines[0].strip("\n").split()
        i = names.index(plant_selected) if plant_selected in names else 0
        new_name = lines[1].strip("\n").split(",")[i]
        description = lines[i + 2].strip("\n")
        f.close()

        fill(217, 160, 53)
        textAlign(CENTER)
        textFont(font2)
        text(new_name, 493, 21, 567, 133)
        
        fill(43, 51, 97)
        textAlign(LEFT)
        textFont(font)
        text(description, 600, 325, 375, 445)
    
    for iy in range(rows):
        for ix in range(columns):
            button = sidebar[ix + iy * columns]
            x, y = 55 + ix * list_x_increment, 122 + iy * list_y_increment
            ReloadSelector(x, y, button["image"]["name"][6:len(button["image"]["name"]) - 4], True)
            EditSidebarButton(button, x, y, 255)

    for ix in range(3):
        button = sidebar[ix + rows * columns]
        x, y = 115 + ix * list_x_increment, 122 + rows * list_y_increment
        ReloadSelector(x, y, button["image"]["name"][6:len(button["image"]["name"]) - 4], True)
        EditSidebarButton(button, x, y, 255)
    
def SideBar(column_size, offset): #Renders the sidebar
    global sidebar, plant_selected, selector_x, selector_y
    for i, button in enumerate(sidebar[offset:] + sidebar[:offset]): 
        x, y = list_x, list_y + list_y_increment * i 
        ReloadSelector(x, y, button["image"]["name"][6:len(button["image"]["name"]) - 4], i < column_size)
        EditSidebarButton(button, x, y, 255 if i < column_size else 0)
                

shift = 0 #Stores the scrolling offset of the sidebar

def mouseWheel(event): #Will cycle the sidebar using the mouseWheel
    global shift, plant_selected, continue_wave
    if abs(shift) <= len(sidebar) - 2:
        shift += event.getCount()  
    else:
        shift = 0

    if continue_wave:
        return
    SideBar(bar_size, shift)
    
    
button_kys = ("area", "function", "mouse")
fallback = lambda dic, ky, default: dic[ky] if dic != None else default

press_selected = 10**6 #Stores the number of pressed before and including selecting a new plant
def TriggerButtonPress(object): #Will run the function of a button if it is pressed
    global mouse_presses, press_selected
    button = object["button"]
    a, f, m = fallback(button, "area", None), fallback(button, "function", None), fallback(button, "mouse", None)
    p, p2 = fallback(a, "pos", None), fallback(a, "pos2", None)
    x, y, x2, y2 = fallback(p, "x", 0), fallback(p, "y", 0), fallback(p2, "x", 0), fallback(p2, "y", 0)
    if min(x, x2) <= mouseX <= max(x, x2) and min(y, y2) <= mouseY <= max(y, y2):
        if f != None and mouseButton == m:
            press_selected = mouse_presses
            f()

mouse_presses = 0
def mousePressed(): #Detects mousePresses and checks if buttons are being pressed
    global mouse_presses
    for object in buttons:
        TriggerButtonPress(object)
    for object in sidebar:
        if object["image"]["fill"]["a"] > 0:
            TriggerButtonPress(object)

    if mouseButton == LEFT and mouse_presses%2 == 0:
        mouse_presses += 1
   

def mouseReleased(): #Reloads the selector
    global mouse_presses, sidebar, shift, plant_selected
    mouse_presses += 1
    for i, object in enumerate(sidebar[shift:] + sidebar[:shift]):
        x, y = list_x, list_y + list_y_increment * i 
        visible = object["image"]["fill"]["a"] > 0
        ReloadSelector(x, y, object["image"]["name"][6:len(object["image"]["name"]) - 4], visible)
    if mouseButton == LEFT and mouse_presses%2 != 0:
        mouse_presses += 1
#Checks if a plant can be placed. Checks if special plants are on their lower grade counterparts
upgradable_plants = {"Gatlingpea" : "Repeater", "Spikerock" : "Spikeweed", "Cobcannon" : "Kernelpult", "Twinsunflower" : "Sunflower"}
can_place_cobcannon = lambda x, y: rows[y]["Plants"][x - 1]["Settings"]["name"] == "Kernelpult" if x - 1 > -1 and rows[y]["Plants"][x - 1] != None else False
can_place = lambda x, y, type: rows[y]["Plants"][x] == None if not(type in upgradable_plants.keys()) else rows[y]["Plants"][x] != None and rows[y]["Plants"][x]["Settings"]["name"] == upgradable_plants[type] and (type != "Cobcannon" or can_place_cobcannon(x, y)) 
#Checks if a zombie should target a specific plant
can_detect_plant = lambda settingz, target_plant : target_plant != None and (settingz["name"] == "Zamboni" or settingz["name"] == "Gargantuar" or (target_plant["Settings"]["name"] != "Spikerock" and target_plant["Settings"]["name"] != "Spikeweed"))                                                                                                                                                                            
#Stores the prices of all the plants
plant_prices = {"Wallnut" : 50, "Peashooter" : 100, "Repeater" : 200, "Gatlingpea" : 250, "Kernelpult" : 100, "Cobcannon" : 500, "Spikeweed" : 100, "Torchwood" : 175, "Spikerock" : 125, "Sunflower" : 50, "Twinsunflower" : 150}

def Spawn(object, row, column, is_zombie): #Spawns a plant or a zombie at a specific row or column (only for plants as they are column dependant)
    new = copycollection(object)
    if is_zombie:
        new["Settings"]["last_moved"] = time.time()
        for i in range(len(new["image"]["animations"])):
            new["image"]["animations"][i]["start"] = random.randint(0, 10000)
        rows[row]["Zombies"].append(new)
        return
    else:
        settingp, imagp  = new["Settings"], new["image"]
        imagp["pos"]["y"] = column_pos[row + 1] + settingp["offset"]["y"] - imagp["size"]["y"]
        imagp["pos"]["x"] = row_pos[column + 1] + settingp["offset"]["x"] - imagp["size"]["x"]
        rows[row]["Plants"][column] = new
        if settingp["name"] == "Cobcannon":
            rows[row]["Plants"][column - 1] = new
        imagp["animation"]["start"] = random.randint(0, 10000)

def Zombies(i, row):#Runs logic for all the zombies in a specific row
    global rows
    for ii, zombie in enumerate(row["Zombies"]):    
            settingz, imagz = zombie["Settings"], zombie["image"]
            imagz["pos"]["y"] = column_pos[i + 1] + settingz["offset"]["y"] - imagz["size"]["y"]
            elapsed = time.time() - settingz["last_moved"]
            zombie["Settings"]["last_moved"] = time.time()
            x, y = GetLocation(imagz["pos"]["x"] + settingz["offset"]["x"], imagz["pos"]["y"] + imagz["size"]["y"] + settingz["ground_offset"]) #x + 1 so the zombie target plants infront and in the current tile
            
            target_plant = None if x == None or y == None else rows[y]["Plants"][x] #Detects if there is a plant on the same tile
            if not(can_detect_plant(settingz, target_plant)): #Checks if the plant can be targeted
                target_plant = None
                
            if target_plant == None:
                targest_plant = None if x == None or y == None or x + 1 >= len(rows[y]["Plants"]) else rows[y]["Plants"][x + 1] 
                #Detects if there is a plant on the tile infront
            if not(can_detect_plant(settingz, target_plant)): #Checks if the plant can be targeted
                target_plant = None 
            
            
                
            if settingz["health"] > 0: #When the zombie is alive it can deal damage and destroy the target plant
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
            
                
            if settingz["health"] <= 0: #Zombie plays a death animation and dissapears after some time
                imagz["animation_selected"] = 2
                if settingz["health"] <= 0 and settingz["death_timer"] == 1:
                    imagz["animations"][2]["start"] = time.time()
                    settingz["death_timer"] = time.time() + (imagz["animations"][2]["total_frames"] - 1) * imagz["animations"][2]["frame_duration"]

            settingz["last_attacked"] = time.time()
            RENDERIMAGE(zombie, ("animations", "animation_selected", "pos", "size", "fill"))
            
            global ice, ice_offset #Zamboni will layer ice on its row, if it is not already on ice
            if settingz["name"] == "Zamboni":
                if imagz["pos"]["x"] + ice_offset < ice[i]:
                    ice[i] = imagz["pos"]["x"] + ice_offset
            
            
    index = 0
    while index < len(row["Zombies"]): #Removes dead zombies
        settingz = row["Zombies"][index]["Settings"]
        if settingz["health"] <= 0 and settingz["death_timer"] - time.time() <= 0:
            row["Zombies"].pop(index)
        else:
            index += 1

def Plants(i, row, is_day): #Runs logic for all the plants
    global rows, continue_wave
    for ii, plant in enumerate(row["Plants"]):
            if not(plant):
                continue
            
            RENDERIMAGE(plant, ("animation", "pos", "size", "fill"))
            if continue_wave:
                continue
            settingp, imagp  = plant["Settings"], plant["image"]
            can_shoot = "last_shot" in settingp.keys()
            is_sun = can_shoot and settingp["projectile"] == "sun" #will check if the plant is able to shoot
            if can_shoot and time.time() >= settingp["last_shot"] + settingp["reload_time"] and (len(rows[i]["Zombies"]) > 0 or is_sun): 
               
                if is_sun and not(is_day): #Sun cannot be produced at night
                    continue
                
                if "max_amount" in settingp.keys(): #Allows for multiple shots before a longer reload
                    settingp["amount"] = settingp["amount"] + 1 if settingp["amount"] < settingp["max_amount"] else 1
                    #settingp["amount"] = settingp["amount"] + 1 if settingp["amount"] < settingp["max_amount"] - 1 else 0
                    #settingp["reload_time"] = 0.4 if settingp["amount"] < settingp["max_amount"] - 1 else settingp["max_reload_time"]
                    settingp["reload_time"] = 0.4 if settingp["amount"] > 1 else settingp["max_reload_time"]
                previous = settingp["last_shot"]
                settingp["last_shot"] = time.time()
                if previous < 100: #Prevents sunflowers from producing sun instantly
                    continue
                projectile = settingp["projectile"] if type(settingp["projectile"]) == type("") else settingp["projectile"][0 if random.randint(1, 100) <= 75 else 1]
                new_projectile = copycollection(projectiles[projectile]) #Creates a new projectile
                if not(is_sun): #Does not produce sun
                    new_settings, new_image = new_projectile["Settings"], new_projectile["image"]
                    new_settings["offset"]["x"] += settingp["projectile_offset"]["x"]
                    new_settings["offset"]["y"] += settingp["projectile_offset"]["y"]
                    new_settings["start"] = time.time() #Setup the properties for the projectile
                    new_settings["start_x"], new_settings["start_y"]  = imagp["pos"]["x"] + new_settings["offset"]["x"], imagp["pos"]["y"] + new_settings["offset"]["y"]
                    new_image["pos"]["y"] = new_settings["start_y"]
                    
                    if new_settings["is_projectile"]: #Utalizes projectile motion
                        new_settings["velocity"]["y"] = -(2*projectile_gravity*projectile_height)**0.5
                        new_settings["start_velocity_y"] = new_settings["velocity"]["y"] #Assigns the correct upwards launch velocity
                        new_settings["total_time"] = (-new_settings["velocity"]["y"]/projectile_gravity) + ((2.0*projectile_height)/projectile_gravity)**0.5
                    
                        closest, closest_y = 10**16, new_image["pos"]["y"]
                        for zombie in row["Zombies"]:
                            settingz, imagz = zombie["Settings"], zombie["image"]
                            d = imagz["pos"]["x"] + imagz["size"]["x"]/2.0 - (0 if settingz["blocked"] else (settingz["speed"] * new_settings["total_time"]*0.5)) #+ imagz["size"]["x"]  #projectile_time
                            closest = min(closest, d) if d > new_settings["start_x"] else closest
                            closest_y = settingz["offset"]["y"] if d > new_settings["start_x"] else closest_y #Finds the target zombie
                        new_settings["velocity"]["x"] = ((closest - new_settings["start_x"])/new_settings["total_time"])*2 #Calculate the x velocity
                        new_settings["target"]["x"], new_settings["target"]["y"] = closest, closest_y #Assign the new velocity
                    rows[i]["Projectiles"].append(new_projectile) #Projectiles are added to their respective rows and catagory
                else:
                    new_projectile["image"]["pos"]["x"] = imagp["pos"]["x"] + random.randint(0, 80) #Sun drops are added to the sun_drops array instead of being row dependant
                    new_projectile["image"]["pos"]["y"] = imagp["pos"]["y"] + random.randint(0, 80)
                    sun_drops.append(new_projectile)

                    
random_sun_drop_cooldown = 24
last_sun_drop = 0
is_day = True
def Sun(): #Logic for random sun drops and sun collection
    global sun_drops, sun, random_sun_drop_cooldown, last_sun_drop, mouse_presses, plant_selected, continue_wave, is_day
    #Checks if random sun drops shall occur
    if not(continue_wave) and time.time() >= random_sun_drop_cooldown + last_sun_drop and is_day: 
        last_sun_drop = time.time() #Reloads the cooldown for sun drops
        new_projectile = copycollection(projectiles["sun"])
        new_projectile["image"]["pos"]["x"] = random.randint(row_pos[0], row_pos[len(row_pos) - 1])
        new_projectile["image"]["pos"]["y"] = random.randint(column_pos[0], column_pos[len(column_pos) - 1])
        sun_drops.append(new_projectile) #Adds a sun drop that is randomly placed it on the map

    
    for i, sun_drop in enumerate(sun_drops):
        angle = time.time()%360.0 * 10 #Gets an angle 
        x, y = sun_drop["image"]["pos"]["x"], sun_drop["image"]["pos"]["y"]
        pushMatrix() #Spins the sun drop
        translate(x, y)
        rotate(radians(angle)) 
        RENDERIMAGE(sun_drop, ("name", "size"))

        if mouse_presses%2 == 1:
            xs, ys = sun_drop["image"]["size"]["x"], y + sun_drop["image"]["size"]["y"]
            #Checks if the sun drop was collected
            if x - xs/2.0 <= mouseX <= x + xs/2.0 and y - ys/2.0 <= mouseY <= y + ys/2.0:
                plant_selected = None
                sun_drops.pop(i)
                sun += 50
                PlaySound("sun", ("minim", "play_from_start"))
                
        popMatrix()
instakill = False #Used for debugging when you want weaker zombies
def Projectiles(i, row):
    global rows, instakill
    remove_indexes = []
    angle = 0
    for ii, projectile in enumerate(row["Projectiles"]):
            setting, imagp = projectile["Settings"], projectile["image"]
            flying = False
            already_removed = False
            if setting["is_projectile"] == False: #If its not projectile motion, just offset it using the amount of time elapsed and the speed
                imagp["pos"]["x"] = setting["start_x"] + (time.time() - setting["start"]) * setting["speed"]
            else:
                delta_time = time.time() - setting["start"]
                flying = delta_time <= setting["total_time"]*0.5
                imagp["pos"]["x"] = setting["velocity"]["x"]*delta_time + setting["start_x"] #Set the new position based on the velocity and elapsed time
                imagp["pos"]["y"] = setting["velocity"]["y"]*delta_time + setting["start_y"]  #+ projectile_gravity/2*delta_time**2 + imagp["pos"]["y"]
                setting["velocity"]["y"] = setting["start_velocity_y"] + projectile_gravity*delta_time
                angle = atan((setting["velocity"]["y"] + 0.0)/setting["velocity"]["x"]) 
                if setting["velocity"]["y"] > setting["start_velocity_y"]/2.0: #Projectile will lock on target to look more menacing
                    angle = radians(90) + atan((setting["velocity"]["y"] + 0.0)/(setting["target"]["x"] - imagp["pos"]["x"])) if (setting["target"]["x"] - imagp["pos"]["x"]) != 0 else 0
                
                pushMatrix()
                translate(imagp["pos"]["x"], imagp["pos"]["y"])
                rotate(angle) #Will rotate the projectile
                if imagp["pos"]["y"] + setting["offset"]["y"] > column_pos[i + 1]:
                    already_removed = True #Will remove the projectile if it passes the ground / column position
                    remove_indexes.append(ii)
            if not(flying): 
                if imagp["name"] == "plants/projectiles/pea.png":
                    crossed = False #Will set peas of fire if they are within the tile of a torchwood
                    for c, plant in enumerate(row["Plants"]):
                        if plant != None and plant["Settings"]["name"] == "Torchwood" and (c, i) == GetLocation(imagp["pos"]["x"], imagp["pos"]["y"] + imagp["size"]["y"]):
                            imagp["name"] = "plants/projectiles/firepea.png"
                            setting["damage"] *= 2
                    
                closest_setting, closest = None, 10**6 #Finds the closest zombie
                for zombie in row["Zombies"]:
                    settingz, imagz = zombie["Settings"], zombie["image"]
                    x_pos = imagz["pos"]["x"] + settingz["offset"]["x"] 
                    can_hit = setting["start_x"] <= x_pos <= imagp["pos"]["x"]
                    zombie_end_pos = x_pos + imagz["size"]["x"]
                    can_reach = setting["is_projectile"] and setting["start_x"] <= zombie_end_pos and (zombie_end_pos <= x_pos + imagz["size"]["x"] or abs(x_pos + imagz["size"]["x"] - imagp["pos"]["x"]) < imagp["size"]["x"]) 
                    d = x_pos - setting["start_x"]
                    if can_hit or can_reach:
                        if imagp["name"] == "plants/projectiles/Lawn Mower.png":
                            settingz["health"] = 0 #Lawn mowers will instakill any zombie that it can currently reach
                            continue
                        closest_setting = settingz
                        
                if closest_setting != None:
                    if not(already_removed):
                      
                        remove_indexes.append(ii) #Deal damage to the zombie
                    closest_setting["health"] -= setting["damage"] if not(instakill) else 69420
                    
            if not(already_removed): #Render the projectile if it was not removed
                RENDERIMAGE(projectile, ("name", "size", "pos" if not(setting["is_projectile"]) else ""))
            if setting["is_projectile"]:    
                popMatrix() #Pop the matrix, but only if it was used

            
    index, r = 0, 0 #Removes projectiles
    while len(remove_indexes) > 0: 
        if index + r == remove_indexes[0]:
            row["Projectiles"].pop(index)
            remove_indexes.pop(0)
            r += 1
        else:
            index += 1
            
transition_time = 9

def HoverShade(button): #Will darken a button on hover
    if button["image"]["fill"]["a"] <= 0:
        return
    x, y = button["image"]["pos"]["x"], button["image"]["pos"]["y"]
    xs, ys = button["image"]["size"]["x"], button["image"]["size"]["y"]
    if x <= mouseX <= x + xs and y <= mouseY <= y + ys:
        fill(0, 0, 0, 127)
        rect(x, y, xs, ys)

def Buttons(): #Runs logic for multiple buttons and interface
    global sidebar, buttons, tutorial, bar_size, shift
    global list_x, list_y, list_y_increment
    if tutorial: #Render the almanac if it is enabled
        TutorialGrid() 
    else: #Render the sidebar when the almanac is disabled
        SideBar(bar_size, shift)
    for object in sidebar: #Renders the sidebar
        RENDERIMAGE(object, ("name", "fill", "size", "pos")) 
        HoverShade(object) 
    
    buttons[0]["image"]["pos"]["x"] = 115 if tutorial else 130
    buttons[0]["image"]["pos"]["y"] = 424 if tutorial else 30 
    
    for object in buttons: #Renders buttons
        if object["image"]["name"] == "buttons/Tutorial.png" and tutorial:
            continue #tutorial button will not show up in the almanac
        RENDERIMAGE(object, ("name", "fill", "size", "pos")) 
        HoverShade(object)
       
        
    tint(255)
    if plant_selected != None: #Draws the selector indicator at the correct position
        image(loadImage("selector.png"), selector_x, selector_y, 106, 66)
        
def Save(): #Saves the amount of sun, difficulty and completed waves. Also includes the plants and mowers
    global sun, amplifier, waves_completed, rows, mowers_left
    f = open("saved/Data.txt", "w") #Write sun, amplifier and completed waves to the file
    f.writelines([str(sun) + "\n", str(amplifier) + "\n", str(waves_completed) + "\n"])
    f.close()
    
    f = open("saved/Lawn.txt", "w").close() #clears the file
    f = open("saved/Lawn.txt", "a")
    for row in rows:
        plants = list(map(lambda x : x["Settings"]["name"] if x != None else None, row["Plants"]))
        for x, plant in enumerate(plants):
           if x >= len(plants) - 1:
               break
           if row["Plants"][x] == row["Plants"][x + 1]:
               plants[x] = None #Only edit the save, don't change the actual in game rows
    
        f.write(str(plants) + "\n") #Write a row of plants to the file, each row is on their corresponding line
    f.close()
    
    f = open("saved/LawnMowers.txt", "w").close()
    f = open("saved/LawnMowers.txt", "a")
    f.write(str(mowers_left) + "\n") #Write the list of lawn mowers
    f.close()
    print("Saved")

def PastSave(): #Checks if a save file exsists
    f = open("saved/Data.txt", "r") 
    lines = f.readlines()
    f.close()
    return not(len(lines) <= 0 or len(str(lines[0]).strip()) == 0)
def LoadSave():
    global rows
    #Loads a previous save
    
    global sun, amplifier, waves_completed, rows, mowers_left
    f = open("saved/Data.txt", "r")
    lines = f.readlines() #Assign sun, amplifier and completed waves their previously saved values
    sun, amplifier, waves_completed = map(lambda x : float(x.strip("\n")), lines)
    sun = int(sun) #Amplifier is a float, so the other variables must be converted back to an integer
    waves_completed = int(waves_completed)
    f.close()
    
    f = open("saved/Lawn.txt", "r")
    lines = f.readlines() #Loads the lawn by spawning in all the plants in the file
    for r, row in enumerate(lines):
        for i, plant in enumerate(map(lambda x : str(x).strip(" ' "), row.strip("[]\n").split(","))):
            if plant != str(None): #Spawns the plant using the correct type and position in the list
                Spawn(copycollection(plants[plant]), r, i, False)
            
    f.close()
    
    f = open("saved/LawnMowers.txt", "r") #Loads the lawn mowers
    mowers_left = map(lambda x : x.strip() == "True", f.read().strip("[]\n").split(","))
    f.close()
    print("Loaded")
        
def Restart(save_data): #Resets many in game vairables
    global rows, gameover, played_gameover_sound, amplifier, waves_completed, ice, mowers_left, last_melted, continue_wave, sun, sun_drops, tutorial, highscore
    gameover = False
    played_gameover_sound = False
    
    amplifier = 1 #Maybe hard waves run after every 3 easy waves
    waves_completed = 0
    sun = 0

    last_melted = time.time()
    mowers_left = [True for i in range(len(column_pos) - 1)]
    ice = [10**16 for _ in range(len(column_pos) - 1)]
    rows = list([{"Plants" : [None for ii in range(len(row_pos) - 1)], "Projectiles" : [], "Zombies" : []} for i in range(len(column_pos) - 1)])
    sun_drops = []
    continue_wave = True
    tutorial = False
    f = open("highscore.txt", "r") #Saves the highscore
    highscore = int(f.read())
    f.close()
    if save_data:
        Save() #Only saves data when a wave has completed, not on setup
    

def Gameover(): #Plays the gameover cutscene
    global gameover, transition_time, played_gameover_sound
    if not(played_gameover_sound):
        PlaySound("gameover", ("minim", "repeat", "play_from_start", "isolate", "group"))  
        played_gameover_sound = True 
    fill(0, 0, 0, 127)
    rect(0, 0, 1000, 1000)
    tint(255, 255, 255, min(1, ((time.time() - gameover)/transition_time)) * 255)
    image(loadImage("messages/Gameover.png"), 218, 67, 564, 466)
    
    if (time.time() - gameover)/transition_time >= 1:
        Restart(True)
def LawnMower(): #Runs logic for the lawn mowers, also detects when you lose
    global mowers_left, rows, projectiles, gameover
    for x, row in enumerate(rows):  
        if mowers_left[x] == True: #Renders the lawn mower if it can be used
            image(loadImage("plants/projectiles/Lawn Mower.png"), 180, column_pos[x], 80, 68)
        
        if gameover:
            continue
        
        for zombie in row["Zombies"]:
            #Detects if the zombies in the same tile have passed the lawn mower
            settingz, imagz = zombie["Settings"], zombie["image"]
            x_pos = settingz["offset"]["x"] + imagz["pos"]["x"]
            if x_pos < row_pos[0] and settingz["health"] > 0: #Checks if the zombie has passed the mower
                if mowers_left[x] != True:
                    if x_pos < row_pos[0] - 100:
                        gameover = time.time()
                    return #No lawn mower was found, so the zombie gets past
                
                settingz["health"] = 0 #Damages the zombie, so it does not trigger a gameover
                new_mower = copycollection(projectiles["lawnmower"]) #Spawns a lawn mower projectile
                new_mower["Settings"]["start_x"], new_mower["image"]["pos"]["y"] = 180, column_pos[x]
                new_mower["Settings"]["start"] = time.time()
                rows[x]["Projectiles"].append(new_mower)
                mowers_left[x] = False #Stores that the lawn mower is no longer available
                break
        

def Ice(): #Runs logic for ice
    global ice, melt_rate, last_melted
    delta_time = time.time() - last_melted
    for i, pos in enumerate(ice): #Render and melt ice
        ice[i] -= delta_time * melt_rate #Ice will melt based on the elapsed time and the rate
        image(loadImage("ice.png"), pos, column_pos[i]+(column_pos[i+1] - column_pos[i] - 77)/2.0, 794, 77)
    last_melted = time.time() #Reset the elapsed time

def GetLocation(ax, ay): #Returns the x and y position on the lawn
    for y, y_pos in enumerate(column_pos):
        for x, x_pos in enumerate(row_pos):
            if y + 1 == len(column_pos) or x + 1 == len(row_pos):
                break
            if x_pos <= ax < row_pos[x + 1] and y_pos <= ay < column_pos[y + 1]:
                return x, y
    return None, None

wave_message = "Waves Completed" 
wave = None
wave_duration = 45
spawn_cooldown = 1
start_cooldown = 6
start_wave = -1
def StartWave(): #Starts and selectes wave 
    global amplifier, waves_completed, easy_waves, hard_waves, wave, spawn_cooldown, start_wave, start_cooldown
    is_hard = (waves_completed + 1)%4 == 0 #Decides if the wave will be from the hard_wave selection
    wave = copycollection(hard_waves[random.randint(0, len(hard_waves) - 1)] if is_hard else easy_waves[random.randint(0, len(easy_waves) - 1)])
    total_zombies = 0
    for ky in wave:
        if ky == "sound":
            continue
        wave[ky] *= amplifier if is_hard else min(max_easy_amplifier, amplifier)
        total_zombies += wave[ky]
    spawn_cooldown = (wave_duration + 0.0)/total_zombies #Assigns a spawn cooldown
    start_wave = time.time() + start_cooldown
    


def setup(): #Sets up many variables
    global font, font2, continue_menu
    size(1000, 600)
    Restart(False)
    SideBar(bar_size, 0)
    StartWave() 
    minim = Minim(this)
    for ky in sounds: #Creates sound minim objects
        sounds[ky]["minim"] = minim.loadFile("sounds/" + sounds[ky]["minim"])
    PlaySound("intro", ("minim", "repeat", "play_from_start", "isolate", "group"))
    font = createFont("SERIO___.TTF", 24) #Loads various fonts
    font2 = createFont("Barbatos.ttf", 40)
    textFont(font)
    continue_menu = PastSave() #Display the continue menu if a save file was found
    
cooldown = time.time()
start_music = time.time() + 6
projectile_removed = time.time()
projectile_remove_cooldown = 10
state = "title"
in_main_menu = True
sun_preview = 0
saved_already = False

def draw(): #Runs lots of logic and Renders everything
    global in_main_menu, sun, sun_preview
    global rows, cooldown, projectile_removed, plant_selected, state, s, yv, start_music, mouse_presses, selector_x, selector_y, gameover, wave, press_selected, is_day
    global continue_menu, saved_already
    global tutorial, buttons, continue_wave, removing
    noStroke()
    buttons[1]["image"]["fill"]["a"] = 255 if continue_wave else 0
    buttons[2]["image"]["fill"]["a"] = 255 if continue_wave and not(continue_menu) and not(tutorial) else 0
    
    if in_main_menu: #Renders the main menu
        tint(255)
        image(loadImage("Title.png"), 0, 0, 1000, 600)
        tint(125 if 149 <= mouseX <= 149 + 673 and 532 <= mouseY <= 532 + 56 else 255)
        image(loadImage("buttons/StartForTint.png"), 149, 532, 673, 56)
        PlaySound("menu", ("minim", "repeat", "play_from_start", "isolate", "group"))
        if keyPressed or mousePressed:
            in_main_menu = False #Close main menu
        return

    if tutorial: #Renders the almanac
        tint(255)
        image(loadImage("tutorial/Almanac.png"), 0, 0, 1000, 600)
        PlaySound("tutorial", ("minim", "repeat", "play_from_start", "isolate", "group"))
        Buttons()
        
        
        tint(255) #Renders a sun counter and shovel tip
        image(loadImage("suncounter.png"), 328, 434, 150, 43)
        fill(0)
        textAlign(CENTER)
        text(str(sun_preview), 260, 444, 328, 454)
        
        image(loadImage("tutorial/tip.png"), 47, 383, 159, 83)
        image(loadImage("tutorial/tip2.png"), 242, 370, 226, 173)

        sun_preview += 1
        if sun_preview > 9990:
            sun_preview = 0
        if 530 <= mouseY <= 530 + 45:
            if 555 <= mouseX <= 555 + 164:
                fill(0, 0, 0, 127)
                rect(555, 530, 164, 45)
                if mousePressed and mouseButton == LEFT:
                    plant_selected = None #Unselect the plant preview        
            
            if 830 <= mouseX <= 830 + 164: 
                fill(0, 0, 0, 127)
                rect(830, 530, 164, 45)
                if mousePressed and mouseButton == LEFT:
                    tutorial = False #Closes almanac

        return

    is_day = wave == None or wave["sound"] != "moon" #Checks if the map is daytime
    copy(loadImage("Lawn.png" if is_day else "LawnNight.png"), 0, 0, 1400, 600, 0, 0, 1400, 600)#Renders the lawn

    
    tint(255, 255, 255, 255)
    Ice() #Renders many features of the game
    LawnMower() 
    for i, row in enumerate(rows):
        Plants(i, row, is_day)
        Zombies(i, row)
        Projectiles(i, row)
    Sun()
    Buttons()
    tint(255)
    image(loadImage("suncounter.png"), 220, 30, 150, 43)
    fill(0)
    textAlign(CENTER)
    text(str(min(sun, 9990)), 210, 40, 210, 50)
    
    if gameover > 0:
        Gameover()
        return    

    
    global spawn_cooldown, waves_completed, highscore, max_amplifier, amplifier, start_wave

    textAlign(CENTER)
    textSize(25)
    fill(0, 0, 0, 255)
    ox, oy = 1, 2 #Renders the completed wave and highscore, with border
    text(str(waves_completed) + " Waves Completed", 300-ox, 550-oy, 400, 600)
    text("Highscore " + str(highscore), 555-ox, 550-oy, 655, 600)
    
    text(str(waves_completed) + " Waves Completed", 300+ox, 550+oy, 400, 600)
    text("Highscore " + str(highscore), 555+ox, 550+oy, 655, 600)
    textSize(24)
    fill(231, 191, 96, 255)
    text(str(waves_completed) + " Waves Completed", 300, 550, 400, 600)
    text("Highscore " + str(highscore), 555, 550, 655, 600)
        
    if continue_wave: #Will trigger the continue wave mode
        PlaySound("seed", ("minim", "repeat", "play_from_start", "isolate", "group"))     
        selected_plant = None
        removing = None 
        
        if continue_menu:
            tint(255) #Renders the continue wave option
            image(loadImage("continue.png"), 253, 136, 493, 270)
            if 360 <= mouseY <= 400:
                pressed = mousePressed and mouseButton == LEFT
                fill(0,0,0, 127)
                if 283 <= mouseX <= 488:
                    rect(283, 360, 205, 40)
                    if pressed:
                        LoadSave() #Will load your progress
                        continue_menu = False
                if 510 <= mouseX <= 715:
                    rect(510, 360, 205, 40)
                    if pressed: #Rests progress
                        Restart(True)
                        continue_menu = False
            return
        
        if not(saved_already):
            saved_already = True
            Save()
        return
    
    
    if wave != None: #Runs logic for the spawning of zombies and wave start / endings
        PlaySound(wave["sound"], ("minim", "repeat", "play_from_start", "isolate", "group"))  
    if start_wave != -1 and start_wave <= time.time() and wave != None and time.time() > cooldown:
        #Detects if zombies are available
        kys = list(wave.keys())
        kys.remove("sound")
        for ky in kys:
            if int(wave[ky] + 0.5) <= 0:
                wave.pop(ky)
        kys = list(wave.keys())
        kys.remove("sound")
        if len(kys) <= 0: #No more zombies, proceeds to reset
            no_zombies = True
            for row in rows:
                if len(row["Zombies"]) > 0:
                    no_zombies = False
                    break
            if no_zombies: #Wave ended and continue mode is triggered
                waves_completed += 1    
                continue_wave = True
                saved_already = False
                if waves_completed > highscore:
                    f = open("highscore.txt", "w")
                    f.write(str(waves_completed))
                    f.close() #Saves the highscore
                    highscore = waves_completed
            
        else:
            cooldown = time.time() + spawn_cooldown
            selected_type = kys[random.randint(0, len(kys) - 1)]
            wave[selected_type] -= 1 #Spawns zombies
            Spawn(zombies[selected_type], random.randint(0, 4), None, True)
    
            
    
    #Removes projectiles that are off screen
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

        if plant_selected != None:
            fill(0, 0, 0, 50) #Renders the tile selector if the mouse is on the lawn and you are placing a plant
            rect(row_pos[x], column_pos[0], row_pos[x + 1] - row_pos[x], column_pos[len(column_pos) - 1])
            rect(row_pos[0], column_pos[y], row_pos[len(row_pos) - 1], column_pos[y + 1] - column_pos[y])
            fill(255, 255, 255, 120)
            rect(row_pos[x], column_pos[y], row_pos[x + 1] - row_pos[x], column_pos[y + 1] - column_pos[y])
        if removing: #Renders shovel icon if you are removing a plant
            image(loadImage("shovel.png"), mouseX, mouseY - 75, 75, 75) 
        
        if mouse_presses%2 == 0:
            if removing and mouse_presses == press_selected + 2: #Removes a plant and completely removes a cobcannon which requires removal of two tiles
                if x - 1 > -1 and rows[y]["Plants"][x - 1] == rows[y]["Plants"][x]:
                    rows[y]["Plants"][x - 1] = None
                elif x + 1 < len(row_pos) - 1 and rows[y]["Plants"][x + 1] == rows[y]["Plants"][x]:
                    rows[y]["Plants"][x + 1] = None
                rows[y]["Plants"][x] = None #Assign no plant to the tile
            elif plant_selected != None and row_pos[x + 1] < ice[y] and mouse_presses == press_selected + 4:
                if sun >= plant_prices[plant_selected] and can_place(x, y, plant_selected):
                    sun -= plant_prices[plant_selected] #Checks if you can afford the plant and spawn the plant
                    Spawn(plants[plant_selected], y, x, False) 
                else:
                    PlaySound("error", ("minim", "play_from_start"))
                    
                


    if mouse_presses%2 == 0: #Deselects by detecting invalid clicks
        removing = False
        #print(mouse_presses, press_selected + 4)
        if mouse_presses > press_selected + 2:
            plant_selected = None
