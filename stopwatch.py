# template for "Stopwatch: The Game"
 
import simplegui

#to store player name
player_name = "Player"

# define global variables
time = 0  #to check if clock is on(1) or off(0)
clock = 0
position = [150,150]
string = ""
total_stop=0  #to count total no. of stops
right_stop=0  #to count no. of successful stops
curr_time=0  #to record current time
message = ""
rules = "You are awarded a point if you stop the watch \n at a whole second. Press 'start' to commence."
rules2 = ""
  
def input_handler(text):
    global player_name
    player_name = text
     
def draw(canvas):
    global time,position,string
    string = format(time)
    canvas.draw_text(string,position,36,"Aqua")
    canvas.draw_text("Score: "+str(right_stop)+"/"+str(total_stop),[20,20],15,"Blue")
    canvas.draw_text(message,[130,200],20,"Blue")
    canvas.draw_text(rules,[20,250],20,"Red")
    canvas.draw_text(rules2,[20,280],20,"Red")
     
# helper function that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_second = t % 10
    second = t//10
     
    if(second > 59):
        second = second % 60
         
    if(second < 10):
        seconds = "0" + str(second)
     
    else:
        seconds = str(second)
 
    minute = t // 600

    #global string
    st = str(minute) + ":" + seconds + "." + str(tenth_second)
    return st
     
     
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    global time,total_stop,right_stop, message
    total_stop = 0
    right_stop = 0
    time = 0
    timer.stop()
    message = ""
     
def start():
    global clock,message
    clock = 1
    message = ""
    timer.start()
     
def stop():
    global total_stop,time,right_stop,clock,message,player_name
     
    if(clock == 1):
    
        total_stop += 1
        timer.stop()
     
        if(time % 10 == 0):
            message = "Good job " + player_name + "! :)"
            right_stop += 1
        else:
            message = "Try again " + player_name + "! :("
             
        clock = 0
     
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
     
# create frame
frame = simplegui.create_frame("Stopwatch",400,300)
 
# register event handlers
timer = simplegui.create_timer(100,tick)
start_button = frame.add_button("Start",start,100)
stop_button = frame.add_button("Stop",stop,100)
reset_button = frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)
#global player_name
frame.add_input("Enter your name",input_handler,100)
 
# start timer and frame
frame.start()
