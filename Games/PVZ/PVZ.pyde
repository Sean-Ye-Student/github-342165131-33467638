import time
import random
add_library("minim")
spawn_pos_x = 900
column_pos = (80,183,279,385,467, 573) #The borders between rows from the very top to the very bottom
row_pos = (251, 334, 408, 493, 576, 654, 738, 812, 898, 987) #The borders between columns from the very left to the very right
rows = list([{"Plants" : [None for ii in range(len(row_pos) - 1)], "Projectiles" : [], "Zombies" : []} for i in range(len(column_pos) - 1)])

zombies = {"Football" : {"image" : { "name" : "football", "size" : {"x" : 360, "y" : 203}, "pos" : {"x" : spawn_pos_x, "y" : 0}, "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255},
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
                        "Settings" : {"offset" : {"x" : 150, "y" : 0}, "speed" : 40, "last_moved" : time.time(), "last_attacked" : time.time(), "blocked" : False, "health" : 20, "dps" : 3, "death_timer" : 1},
                        }, 
                         
                         
                         
                         
                         
           
           "Basic" :  {"image" : {
                                    "name" : "dancer",
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
                                                "speed" : 10, 
                                                "last_moved" : time.time(), 
                                                "last_attacked" : time.time(), 
                                                "blocked" : False, 
                                                "health" : 200,
                                                "dps" : 1,
                                                "death_timer" : 1}
        },
           
           
        "Cone" :  {"image" : {
                                        "name" : "dancer",
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
                          "Settings" : {"offset" : {"x" : 15, "y" : -30}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "amount" : 1, "health" : 5}},
          
          "Kernelpult" : {
                          "image" : {"size" : {"x" : 100, "y" : 82},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/kernelpult/(", "file_type" : ").png", "start" : 0,"total_frames" : 47, "frame_duration" : 0.04}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "kernel", "amount" : 1, "health" : 5, "target" : {"x" : 0, "y" : 0} }},
          
          "Sunflower" : {
                          "image" : {"size" : {"x" : 100, "y" : 106},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/sunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 54, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "amount" : 1, "health" : 5}}
        }

projectile_height = 160
projectile_time = 2
projectile_gravity = 9.8
projectiles = {"pea" : {"image" : {"name" : "plants/projectiles/pea.png", "size" : {"x" : 21, "y" : 21}, "pos" : {"x" : 0, "y" : 0}},
                    "Settings" : {"offset" : {"x" : 65, "y" : 30}, "start_x" : 0, "start" : time.time(), "speed" : 150, "damage" : 20, "is_projectile" : False}},
                "kernel" : {"image" : {"name" : "plants/projectiles/kernel.png", "size" : {"x" : 21, "y" : 22}, "pos" : {"x" : 0, "y" : 0}},
                    "Settings" : {"offset" : {"x" : 0, "y" : 0}, "velocity" : {"x" : 0, "y" : 0}, "start_x" : 0, "start" : time.time(), "damage" : 20, "is_projectile" : True}}
                
}

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

for name in plants:
    plants[name]["Settings"]["name"] = name

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

    tint(fallback(f, "r", 255), fallback(f, "g", 255), fallback(f, "b", 255), fallback(f, "a", 255))
    image(loadImage(img_name), fallback(pos, "x", 0), fallback(pos, "y", 0), fallback(img_size, "x", 100), fallback(img_size, "y", 100))   

sounds = {"tutorial" : {"minim" : "Cipher - Electronic Light.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}, "intro" : {"minim" : "The_Zombies_Are_Coming.mp3", "repeat" : 1, "play_from_start" : True, "isolate" : True, "group" : 0}, "menu" : {"minim" : "Crazy Dave Intro Theme.mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True,"group" : 0}, "game" : {"minim" : "Grasswalk (In-Game).mp3", "repeat" : -1, "play_from_start" : True, "isolate" : True, "group" : 0}}

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

plant_selected = None
def SELECTPLANT(name):
    global plant_selected
    print(name)
    plant_selected = name
    

def SELECTPEASHOOTER():
    SELECTPLANT("Peashooter")
def SELECTWALLNUT():
    SELECTPLANT("Wallnut")
def SELECTSUNFLOWER():
    SELECTPLANT("Sunflower")
def SELECTKERNELPULT():
    SELECTPLANT("Kernelpult")

buttons = [
           {"button" : {
    "mouse" : LEFT,
    "function" : SELECTPEASHOOTER,
    "area" : {"pos" : {"x" : 10, "y" : 0}, "pos2" : {"x" : 116, "y" : 66}}},
    
    "image" : {"name" : "icons/peashooter.png",
               "size" : {"x" : 106, "y" : 66},
                "pos" : {"x" : 10, "y" : 0},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},
           
           
      {"button" : {
    "mouse" : LEFT,
    "function" : SELECTWALLNUT,
    "area" : {"pos" : {"x" : 10, "y" : 80}, "pos2" : {"x" : 116, "y" : 146}}},
    
    "image" : {"name" : "icons/wallnut.png",
               "size" : {"x" : 106, "y" : 66},
                "pos" : {"x" : 10, "y" : 80},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},
      
    {"button" : {
    "mouse" : LEFT,
    "function" : SELECTSUNFLOWER,
    "area" : {"pos" : {"x" : 10, "y" : 160}, "pos2" : {"x" : 116, "y" : 246}}},
    
    "image" : {"name" : "icons/sunflower.png",
               "size" : {"x" : 106, "y" : 66},
                "pos" : {"x" : 10, "y" : 160},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }},
    
     {"button" : {
    "mouse" : LEFT,
    "function" : SELECTKERNELPULT,
    "area" : {"pos" : {"x" : 10, "y" : 240}, "pos2" : {"x" : 116, "y" : 306}}},
    
    "image" : {"name" : "icons/kernelpult.png",
               "size" : {"x" : 106, "y" : 66},
                "pos" : {"x" : 10, "y" : 240},
                "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}
    }}
           ]



button_kys = ("area", "function", "mouse")
fallback = lambda dic, ky, default: dic[ky] if dic != None else default
def mousePressed():
    for object in buttons:
        button = object["button"]
        a, f, m = fallback(button, "area", None), fallback(button, "function", None), fallback(button, "mouse", None)
        p, p2 = fallback(a, "pos", None), fallback(a, "pos2", None)
        x, y, x2, y2 = fallback(p, "x", 0), fallback(p, "y", 0), fallback(p2, "x", 0), fallback(p2, "y", 0)
        if min(x, x2) <= mouseX <= max(x, x2) and min(y, y2) <= mouseY <= max(y, y2):
            if f != None and mouseButton == m:
                f()

can_place = lambda x, y: rows[y]["Plants"][x] == None
def Spawn(object, row, column, is_zombie):
    new = copycollection(object)
    if is_zombie:
        new["Settings"]["last_moved"] = time.time()
        rows[row]["Zombies"].append(new)
    else:
        settingp, imagp  = new["Settings"], new["image"]
        imagp["pos"]["y"] = column_pos[row + 1] + settingp["offset"]["y"] - imagp["size"]["y"]
        imagp["pos"]["x"] = row_pos[column + 1] + settingp["offset"]["x"] - imagp["size"]["x"]
        rows[row]["Plants"][column] = new

def Zombies(i, row):
    global rows
    
    for ii, zombie in enumerate(row["Zombies"]):    
            settingz, imagz = zombie["Settings"], zombie["image"]
            imagz["pos"]["y"] = column_pos[i + 1] + settingz["offset"]["y"] - imagz["size"]["y"]
            elapsed = time.time() - settingz["last_moved"]
            zombie["Settings"]["last_moved"] = time.time()
            x, y = GetLocation(imagz["pos"]["x"] + settingz["offset"]["x"], imagz["pos"]["y"] + imagz["size"]["y"]/1.4) #x + 1 so the zombie target plants infront and in the current tile
            # print(imagz["pos"]["x"] + settingz["offset"]["x"], imagz["pos"]["y"] + imagz["size"]["y"]/2, x, y)
            # if x != None and y != None:
            #     tint(125)
            #     fill(255, 0, 0, 255)
            #     print(x, y)
            #     rect(row_pos[x], column_pos[y], row_pos[x + 1] - row_pos[x], column_pos[y + 1] - column_pos[y])
            #     # if x + 2 < len(row_pos) and y + 2 < len(column_pos):
            #     #     rect(row_pos[x + 1], column_pos[y + 1], row_pos[x + 2] - row_pos[ + 1], column_pos[y + 2] - column_pos[y + 1])

            target_plant = None if x == None or y == None else rows[y]["Plants"][x] 
            if target_plant == None:
                targest_plant = None if x == None or y == None or x + 1 >= len(rows[y]["Plants"]) else rows[y]["Plants"][x + 1]
            settingz["blocked"] = True if target_plant != None else False
            if settingz["health"] > 0:
                
                            
                if target_plant != None:
                    target_plant["Settings"]["health"] -= (time.time() - settingz["last_attacked"]) * settingz["dps"]
                    if target_plant["Settings"]["health"] <= 0:
                        rows[y]["Plants"][x] = None
                
                if not(settingz["blocked"]):
                    imagz["pos"]["x"] -= settingz["speed"] * elapsed        
                    imagz["animation_selected"] = 0
                else:
                    imagz["animation_selected"] = 1
            else:
                imagz["animation_selected"] = 2
                if settingz["health"] <= 0 and settingz["death_timer"] == 1:
                    imagz["animations"][2]["start"] = time.time()
                    settingz["death_timer"] = time.time() + (imagz["animations"][2]["total_frames"] - 1) * imagz["animations"][2]["frame_duration"]

            
            settingz["last_attacked"] = time.time()
            RENDERIMAGE(zombie, ("animations", "animation_selected", "pos", "size", "fill"))
            
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
            #print(row)
            settingp, imagp  = plant["Settings"], plant["image"]
            if "last_shot" in settingp.keys() and time.time() >= settingp["last_shot"] + settingp["reload_time"] and len(rows[i]["Zombies"]) > 0: 
                settingp["last_shot"] = time.time()
                new_projectile = copycollection(projectiles[settingp["projectile"]])
                new_settings, new_image = new_projectile["Settings"], new_projectile["image"]
                new_settings["start"] = time.time()
                new_settings["start_x"], new_image["pos"]["y"]  = imagp["pos"]["x"] + new_settings["offset"]["x"], imagp["pos"]["y"] + new_settings["offset"]["y"]
                
                if new_settings["is_projectile"]:
                    closest = 10**16
                    for zombie in row["Zombies"]:
                        settingz, imagz = zombie["Settings"], zombie["image"]
                        d = settingz["offset"]["x"] + (imagz["pos"]["x"]*1.2) - settingz["speed"] * projectile_time
                        closest = min(closest, d) if d > new_settings["start_x"] else closest
                    fill(255, 0, 0, 255)
                    rect(new_settings["start_x"], 0, closest - new_settings["start_x"], 50)
                    new_settings["velocity"]["x"] = (closest - new_settings["start_x"])/projectile_time
                    new_settings["velocity"]["y"] = -(projectile_height - 0.5*projectile_gravity*(projectile_time**2))/projectile_time
                    print(new_settings["velocity"]["y"])
                rows[i]["Projectiles"].append(new_projectile)
            
            RENDERIMAGE(plant, ("animation", "pos", "size", "fill"))

def Projectiles(i, row):
    global rows
    remove_indexes = []
    for i, projectile in enumerate(row["Projectiles"]):
            setting, imagp = projectile["Settings"], projectile["image"]
            
            if setting["is_projectile"] == False:
                imagp["pos"]["x"] = setting["start_x"] + (time.time() - setting["start"]) * setting["speed"]
            else:
                delta_time = time.time() - setting["start"]
                imagp["pos"]["x"] = setting["velocity"]["x"]*delta_time + setting["start_x"]
                imagp["pos"]["y"] = setting["velocity"]["y"]*delta_time + projectile_gravity/2*delta_time**2 + imagp["pos"]["y"]
                setting["velocity"]["y"] += projectile_gravity * delta_time
                #column_pos = (80,183,279,385,467, 573)
                print(imagp["pos"]["y"] > column_pos[i + 1], time.time())
                if len(row["Zombies"]) <= 0 or imagp["pos"]["y"] > column_pos[i + 1]:
                    print("does it lag")
                    #remove_indexes.append(i)
            
            
            closest_setting, closest = None, 10**6
            for zombie in row["Zombies"]:
                settingz, imagz = zombie["Settings"], zombie["image"]
                can_hit = setting["start_x"] <= zombie["image"]["pos"]["x"] + settingz["offset"]["x"] <= imagp["pos"]["x"]
                can_reach = setting["is_projectile"] and setting["start_x"] <= zombie["image"]["pos"]["x"] + settingz["offset"]["x"]
                d = zombie["image"]["pos"]["x"] + settingz["offset"]["x"] - setting["start_x"]
                if can_hit:
                    closest_setting = settingz
                    closest = d 

            if closest_setting != None:
                remove_indexes.append(i)
                closest_setting["health"] -= setting["damage"]
            
            RENDERIMAGE(projectile, ("name", "size", "pos"))
            
    index, r = 0, 0
    while len(remove_indexes) > 0:
        if index + r == remove_indexes[0]:
            row["Projectiles"].pop(index)
            remove_indexes.pop(0)
            r += 1
        else:
            index += 1

def GetLocation(ax, ay):
    for y, y_pos in enumerate(column_pos):
        for x, x_pos in enumerate(row_pos):
            if y + 1 == len(column_pos) or x + 1 == len(row_pos):
                break
            if x_pos <= ax < row_pos[x + 1] and y_pos <= ay < column_pos[y + 1]:
                return x, y
    return None, None



def setup():
    size(1000, 600)
    minim = Minim(this)
    for ky in sounds:
        sounds[ky]["minim"] = minim.loadFile("sounds/" + sounds[ky]["minim"])
    PlaySound("intro", ("minim", "repeat", "play_from_start", "isolate", "group"))
cooldown = time.time()
start_music = time.time() + 6
projectile_removed = time.time()
projectile_remove_cooldown = 10
state = "title"

xv, yv = 200, 200
xp, yp = 0, 0
s = time.time()
def draw():
    global cooldown, projectile_removed, plant_selected, state, s, yv, start_music

    if start_music <= time.time():    # if mousePressed:
        PlaySound("game", ("minim", "repeat", "play_from_start", "isolate", "group"))   
    
    if time.time() >= cooldown:        
        options = ("Football",)#tuple(zombies.keys()) 
        Spawn(zombies[options[random.randint(0, len(options) - 1)]], random.randint(0,4), None, True)
        cooldown = time.time() + 3
    
    copy(loadImage("Lawn.png"), 0, 0, 1400, 600, 0, 0, 1400, 600)
    
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
        #print(mouseX, mouseY, x, y, rows[y]["Plants"][x], rows[4]["Plants"])
        noStroke()
        fill(255, 255, 255, 125)
        rect(row_pos[x], column_pos[y], row_pos[x + 1] - row_pos[x], column_pos[y + 1] - column_pos[y])
                
        if mousePressed and mouseButton == LEFT and can_place(x, y):
            if plant_selected != None:
                Spawn(plants[plant_selected], y, x, False) 
                
    for object in buttons:
        RENDERIMAGE(object, ("name", "fill", "size", "pos"))   
        
    for i, row in enumerate(rows):
        Plants(i, row)
        Zombies(i, row)
        Projectiles(i, row)
        dt = time.time() - s
