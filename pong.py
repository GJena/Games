# Implementation of the classic arcade game Pong
 
import simplegui
import random
 
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400      
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
BALL_COLOUR = "White"
player1 = "Red"
player2 = "Blue"
message = ""
mes_colour = "Red"
mes_pos = [0,0]
 
def input_handler1(text1):
    global player1
    player1 = text1
     
def input_handler2(text2):
     
    global player2
    player2 = text2
   
 
# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0,0]
     
    if right:
         
        ball_vel[0] = random.randrange(120,240)/60
        ball_vel[1] = - random.randrange(60,180)/60

    else:
         
        ball_vel[0] = - random.randrange(120,240)/60
        ball_vel[1] = - random.randrange(60,180)/60
 
 
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, message  # these are floats
    global score1, score2  # these are ints
    restart = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/star-wars/yoda/yoda_doordonot.wav")
    restart.play()
    paddle1_pos = (HEIGHT-PAD_HEIGHT)/2
    paddle2_pos = (HEIGHT-PAD_HEIGHT)/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    message = ""
    start_serve = random.randrange(0,2)
    if (start_serve == 0):
        ball_init(False)
    else:
        ball_init(True)
 
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_COLOUR, message, mes_colour, mes_pos 

    # update paddle's vertical position, keep paddle on the screen
    if (((paddle1_pos + paddle1_vel) >= 0) and ((paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT)): 
        paddle1_pos += paddle1_vel
         
    if (((paddle2_pos + paddle2_vel) >= 0) and ((paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT)): 
        paddle2_pos += paddle2_vel
         
         
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") #left gutter
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") #right gutter
     
    # draw paddles
    c.draw_polygon([ [0,paddle1_pos], [PAD_WIDTH,paddle1_pos] , [PAD_WIDTH,paddle1_pos+PAD_HEIGHT], [0,paddle1_pos+PAD_HEIGHT]  ],1, "Grey", "Red")
    c.draw_polygon([[WIDTH,paddle2_pos], [WIDTH-PAD_WIDTH,paddle2_pos] , [WIDTH-PAD_WIDTH,paddle2_pos+PAD_HEIGHT], [WIDTH,paddle2_pos+PAD_HEIGHT]  ], 1, "Grey", "Blue")
      
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
     
    #collision and reflection off of canvas top and bottom
    if (ball_pos[1] <= BALL_RADIUS) or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
         
    #touches left gutter line
    if((ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH):
        #paddle hit
        if((ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= (paddle1_pos + PAD_HEIGHT))):
           hit.play()
           ball_vel[0] = - ball_vel[0]
           ball_vel[0] += ball_vel[0]*0.10
           message = "Good!"
            
        #gutter hit
        else:
            miss.play()
            score2 += 1
            ball_init(True)
            message = "Missed!"
         
        mes_colour = "Red"
        mes_pos = [125,200]
         
    #touches right gutter line
    if((ball_pos[0] + BALL_RADIUS) >= (WIDTH-PAD_WIDTH)):
        #paddle hit
        if((ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= (paddle2_pos+PAD_HEIGHT))):
            hit.play()
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.10
            message = "Good!"
                        
             
             
        #gutter hit
        else:
            miss.play()
            score1 += 1
            ball_init(False)
            message = "Missed!"
             
        mes_colour = "Blue"
        mes_pos = [400,200]
             
             
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS, 2, "Green", BALL_COLOUR)
    c.draw_text(player1,[180,40],30,"Red")
    c.draw_text(str(score1), [200, 80], 30, "Red")
    c.draw_text(player2,[370,40],30,"Blue")
    c.draw_text(str(score2), [400, 80], 30, "Blue")
    c.draw_text(message, mes_pos, 20, mes_colour)
    c.draw_text("Use 'W' 'S' (Player 1) or 'up' 'down' (Player 2) for paddle movement.",[30,350],20,"White")
    c.draw_text("Please turn your speakers on for the entire experience.",[140,380],15,"White")
         
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['up']):
        paddle2_vel=-5
    elif(key == simplegui.KEY_MAP['down']):
            paddle2_vel=5
    elif(key == simplegui.KEY_MAP['w']):
            paddle1_vel=-5
    elif(key == simplegui.KEY_MAP['s']):
            paddle1_vel=5
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['up']):
            paddle2_vel=0
    elif(key == simplegui.KEY_MAP['down']):
            paddle2_vel=0
    elif(key == simplegui.KEY_MAP['w']):
            paddle1_vel=0
    elif(key == simplegui.KEY_MAP['s']):
            paddle1_vel=0
 
 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
frame.add_input("Enter Player 1 name",input_handler1,100)
frame.add_input("Enter Player 2 name",input_handler2 ,100)
 
#sounds
hit = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/beep/beep-03.wav")
miss = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/beep/beep-02.wav")
 
# start frame
init()
frame.start()