import time
spawn_pos_x = 1027
column_pos = (80,183,279,385,467, 573) #The borders between rows from the very top to the very bottom
row_pos = (251, 334, 408, 493, 576, 654, 738, 812, 898, 987) #The borders between columns from the very left to the very right
rows = list([{"Plants" : [None for ii in range(len(row_pos) - 1)], "Projectiles" : [], "Zombies" : []} for i in range(len(column_pos) - 1)])

plants = {"Wallnut" : {"image" : {"size" : {"x" : 148, "y" : 125},"pos" : {"x" : 0, "y" : 0},"fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, "animation" : {"file_index" : "plants/wallnut/(", "file_type" : ").png","start" : 0,"total_frames" : 17, "frame_duration" : 0.08}}, "Settings" : {"offset" : {"x" : 30, "y" : 0}, "health" : 50}},
          "Peashooter" : {
                          "image" : {"size" : {"x" : 100, "y" : 100},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/peashooter/(", "file_type" : ").png", "start" : 0,"total_frames" : 49, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 15, "y" : -30}, "reload_time" : 1.5, "last_shot" : 0, "projectile" : "pea", "amount" : 1, "health" : 5}},
          "Sunflower" : {
                          "image" : {"size" : {"x" : 100, "y" : 106},
                                     "pos" : {"x" : 0, "y" : 0},
                                     "fill" : {"r" : 255, "g" : 255, "b" : 255, "a" : 255}, 
                                     "animation" : {"file_index" : "plants/sunflower/(", "file_type" : ").png", "start" : 0,"total_frames" : 54, "frame_duration" : 0.03}}, 
                          "Settings" : {"offset" : {"x" : 0, "y" : -30}, "amount" : 1, "health" : 5}}
        }

            
projectiles = {"pea" : {"image" : {"name" : "plants/projectiles/pea.png", "size" : {"x" : 21, "y" : 21}, "pos" : {"x" : 0, "y" : 0}},
                    "Settings" : {"offset" : {"x" : 65, "y" : 30}, "start_x" : 0, "start" : time.time(), "speed" : 150, "damage" : 20}}
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

def Plants(i, row):
    global rows
    for ii, plant in enumerate(row["Plants"]):
            if not(plant):
                continue
            #print(row)
            settingp, imagp  = plant["Settings"], plant["image"]
            if "last_shot" in settingp.keys() and time.time() >= settingp["last_shot"] + settingp["reload_time"]: #Maybe later check if their are any zombies using len(rows[i]["Zombies"]) > 0
                settingp["last_shot"] = time.time()
                new_projectile = copycollection(projectiles[settingp["projectile"]])
                new_settings, new_image = new_projectile["Settings"], new_projectile["image"]
                new_settings["start"] = time.time()
                new_settings["start_x"], new_image["pos"]["y"]  = imagp["pos"]["x"] + new_settings["offset"]["x"], imagp["pos"]["y"] + new_settings["offset"]["y"]
                rows[i]["Projectiles"].append(new_projectile)
            
            RENDERIMAGE(plant, ("animation", "pos", "size", "fill"))

def Projectiles(i, row):
    global rows
    for i, projectile in enumerate(row["Projectiles"]):
            setting, imagp = projectile["Settings"], projectile["image"]
            imagp["pos"]["x"] = setting["start_x"] + (time.time() - setting["start"]) * setting["speed"]
            RENDERIMAGE(projectile, ("name", "size", "pos"))

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
    
def draw():
    copy(loadImage("Lawn.png"), 0, 0, 1400, 600, 0, 0, 1400, 600)
     
    x, y = GetLocation(mouseX, mouseY)
    if x != None and y != None:
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
        Projectiles(i, row)
            
