# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this program.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# Implementation of the classic arcade game Pong
 
# Importing modules    
import simplegui
import random
 
# Initializing global variables for the game
WIDTH = 600                      # Height of canvas
HEIGHT = 400                     # Width of canvas
BALL_RADIUS = 20                 # Radius of ball
PAD_WIDTH = 8                    # Width of paddle
PAD_HEIGHT = 80                  # Height of paddle
HALF_PAD_WIDTH = PAD_WIDTH / 2   # Half of paddle width
HALF_PAD_HEIGHT = PAD_HEIGHT / 2 # Half of paddle height
BALL_COLOR = "White"             # Color of ball
msg = ""						 # Message to be displayed
msg_pos = [0,0]					 # Position of message		
msg_col = "Red"                # Color of message
 
# Declare 2 players, initialize them to different colors
player_1 = "Red"
player_2 = "Blue"

# Helper functions for input handlers
def input_handler_1(text_1):
    global player_1
    player_1 = text_1
          
def input_handler_2(text_2):
     
    global player_2
    player_2 = text_2
   
 
# Helper function ball_init that spawns a ball,
# returns a position vector and a velocity vector. It accepts
# right as an input. If right is True, it spawns a ball to the
# right, else it spawns a ball to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0,0]
     
    if right:
        ball_vel[0] = random.randint(120,240)/60
        ball_vel[1] = - random.randint(60,180)/60

    else: 
        ball_vel[0] = - random.randint(120,240)/60
        ball_vel[1] = - random.randint(60,180)/60
        
# Declare a function keydown that accepts key as input and 
# performs some actions when certain keys are down        
def keydown(key):
    global paddle_1_vel, paddle_2_vel
    if(key == simplegui.KEY_MAP['up']):
        paddle_2_vel=-5
    elif(key == simplegui.KEY_MAP['down']):
            paddle_2_vel=5
    elif(key == simplegui.KEY_MAP['w']):
            paddle_1_vel=-5
    elif(key == simplegui.KEY_MAP['s']):
            paddle_1_vel=5
            
# Declare a function keyup that accepts key as input and 
# performs some actions when certain keys are up
def keyup(key):
    global paddle_1_vel, paddle_2_vel
    if(key == simplegui.KEY_MAP['up']):
            paddle_2_vel=0
    elif(key == simplegui.KEY_MAP['down']):
            paddle_2_vel=0
    elif(key == simplegui.KEY_MAP['w']):
            paddle_1_vel=0
    elif(key == simplegui.KEY_MAP['s']):
            paddle_1_vel=0

# Declare a function init that is used to initialize
# the game and other variables 
def init():
    # Global variables
    global paddle_1_pos, paddle_2_pos # Paddle positions (float)
    global paddle_1_vel, paddle_2_vel # Paddle velocities (float)
    global message  				  # Display message (string)
    global score_1, score_2  	      # Scores (integer)

    # Initialize variables
    paddle_1_pos = (HEIGHT-PAD_HEIGHT)/2
    paddle_2_pos = (HEIGHT-PAD_HEIGHT)/2
    paddle_1_vel = 0
    paddle_2_vel = 0
    score_1 = 0
    score_2 = 0
    message = ""
    
    restart_sound.play() # Play sound on restarting
     
    # Call ball_init with random boolean values    
    start_serve = random.randrange(0,2) 
    if (start_serve == 0): 
        ball_init(False)
    else:
        ball_init(True)
        
# Declare a function draw that sketches out different components
# on the canvas
def draw(canvas):
    
    #Global variables
    global score_1, score_2, paddle_1_pos, paddle_2_pos, ball_pos, ball_vel, BALL_COLOR, message, msg_col, msg_pos
    
    # Update paddle's vertical position, keep paddle on the screen
    if (((paddle_1_pos + paddle_1_vel) >= 0) and ((paddle_1_pos + paddle_1_vel) <= HEIGHT - PAD_HEIGHT)): 
        paddle_1_pos += paddle_1_vel
         
    if (((paddle_2_pos + paddle_2_vel) >= 0) and ((paddle_2_pos + paddle_2_vel) <= HEIGHT - PAD_HEIGHT)): 
        paddle_2_pos += paddle_2_vel
         
         
    # Draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # Left gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # Right gutter
     
    # Draw paddles
    canvas.draw_polygon([[0,paddle_1_pos], [PAD_WIDTH,paddle_1_pos] , 
                         [PAD_WIDTH,paddle_1_pos+PAD_HEIGHT], [0,paddle_1_pos+PAD_HEIGHT]],
                         1, "Grey", "Red")
    canvas.draw_polygon([[WIDTH,paddle_2_pos], [WIDTH-PAD_WIDTH,paddle_2_pos],
                         [WIDTH-PAD_WIDTH,paddle_2_pos+PAD_HEIGHT], [WIDTH,paddle_2_pos+PAD_HEIGHT]],
                         1, "Grey", "Blue")
    # Update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
     
    # Handle collision and reflection off of canvas top and bottom
    if (ball_pos[1] <= BALL_RADIUS) or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
         
    # Handle touching left gutter line
    if((ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH):
        #paddle hit
        if((ball_pos[1] >= paddle_1_pos) and (ball_pos[1] <= (paddle_1_pos + PAD_HEIGHT))):
           hit_sound.play()
           ball_vel[0] = - ball_vel[0]
           ball_vel[0] += ball_vel[0]*0.10
           message = "Good!"
            
        #gutter hit
        else:
            miss_sound.play()
            score_2 += 1
            ball_init(True)
            message = "Missed!"
         
        msg_col = "Red"
        msg_pos = [125,200]
         
    # Handle touching right gutter line
    if((ball_pos[0] + BALL_RADIUS) >= (WIDTH-PAD_WIDTH)):
        #paddle hit
        if((ball_pos[1] >= paddle_2_pos) and (ball_pos[1] <= (paddle_2_pos+PAD_HEIGHT))):
            hit_sound.play()
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.10
            message = "Good!"    
        #gutter hit
        else:
            miss_sound.play()
            score_1 += 1
            ball_init(False)
            message = "Missed!"
             
        msg_col = "Blue"
        msg_pos = [400,200]
             
             
    # draw ball and scores
    canvas.draw_circle(ball_pos,BALL_RADIUS, 2, "Green", BALL_COLOR)
    canvas.draw_text(player_1,[180,40],30,"Red")
    canvas.draw_text(str(score_1), [200, 80], 30, "Red")
    canvas.draw_text(player_2,[370,40],30,"Blue")
    canvas.draw_text(str(score_2), [400, 80], 30, "Blue")
    canvas.draw_text(message, msg_pos, 20, msg_col)
    canvas.draw_text("Use 'W' 'S' (Player 1) or 'up' 'down' (Player 2) for paddle movement.",[30,350],20,"White")
    canvas.draw_text("Please turn your speakers on for the entire experience.",[140,380],15,"White")
         
            
# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
frame.add_input("Enter Player 1 name",input_handler_1, 100)
frame.add_input("Enter Player 2 name",input_handler_2, 100)
 
# Sound files for hit and miss of shot
restart_sound = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/star-wars/yoda/yoda_doordonot.wav")
hit_sound = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/beep/beep-03.wav")
miss_sound = simplegui.load_sound("http://www.mediacollege.com/downloads/sound-effects/beep/beep-02.wav")


init() # Initialize the game by calling init function
frame.start() # Start the frame animation
