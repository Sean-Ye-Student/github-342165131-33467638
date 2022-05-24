import time

player_scale = 10
player_offset = (250, 250)
player_angle = 0
player_velocity_angle = 0
player_origin = [250, 250] #spawn location, but will change when player moves
player_velocity = [0,0]#will change when player moves
player_acceleration = 5
player_friction = 65
player_control_minimum_range = 10
player_reload_time = 0.25
player_last_shot = 0
time_elapsed = time.time()
player_points = [lambda s, a, o: s*cos(a) + o, lambda s, a, o: s*sin(a) + o,
        lambda s, a, o: -s*cos(-a + 150) + o, lambda s, a, o: s*sin(-a + 150) + o,
        lambda s, a, o: -s*(2.5/6)*cos(a) + o, lambda s, a, o: -s*(2.5/6)*sin(a) + o,
        lambda s, a, o: -s*cos(a + 150) + o, lambda s, a, o: -s*sin(a + 150) + o]

def ScreenEdgeTeleport(origin, sizeX, sizeY):
    new_originX =  -sizeX if origin[0] > width + sizeX else (width + sizeX if origin[0] < -sizeX else origin[0])
    new_originY =  -sizeY if origin[1] > height + sizeY else (height + sizeY if player_origin[1] < -sizeY else origin[1])
    return new_originX, new_originY

def PlayerController():
    global  player_angle, player_origin, player_velocity, time_elapsed, player_acceleration, player_velocity_angle, player_last_shot
    offsetX = mouseX - player_origin[0] + 0.0
    offsetY = -(mouseY - player_origin[1] + 0.0)
    if (offsetX**2 + offsetY **2)**0.5 >= player_control_minimum_range:
        player_angle = -atan(offsetY/offsetX) if offsetX != 0 else 0
        player_angle = -(atan(offsetY/offsetX)+3.1) if offsetX != 0 and offsetX < 0 else player_angle
    
    #INSERT LAZER LOGIC HERE
    
    if keyPressed and key == "w":
        player_velocity_angle = player_angle
        player_velocity[0] += cos(player_velocity_angle) * player_acceleration * (time.time() - time_elapsed)
        player_velocity[1] += sin(player_velocity_angle) * player_acceleration * (time.time() - time_elapsed)
    else:
        friction = player_friction*(time.time() - time_elapsed)
        player_velocity[0] *= min(0.99, friction)
        player_velocity[1] *= min(0.99, friction)
            
    player_origin[0] += player_velocity[0]
    player_origin[1] += player_velocity[1]
    player_origin[0], player_origin[1] = ScreenEdgeTeleport(player_origin, player_scale, player_scale)
    time_elapsed = time.time()
    
    
def DrawPlayer():
    points = tuple(formula(player_scale, player_angle, player_origin[0] if i%2 == 0 else player_origin[1]) for i, formula in enumerate(player_points))
    line(points[0], points[1], points[2], points[3])
    line(points[2], points[3], points[4], points[5])
    line(points[4], points[5], points[6], points[7])
    line(points[6], points[7], points[0], points[1])

def setup():
    size(1000, 500)
    
def draw():
    background(0)
    stroke(255)
    PlayerController()
    DrawPlayer()
        
