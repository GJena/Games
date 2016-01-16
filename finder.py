# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.
# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

#Implementation of a simple occurrence finder
 
import simplegui
import re
 
#Loading images
img1 = simplegui.load_image("https://www.dropbox.com/s/pubr7xl6paftf4j/Grishma.jpg?dl=1")
img2 = simplegui.load_image("https://www.dropbox.com/s/kvimyhx7n3rft80/CHirag2.jpg?dl=1")
 
#Global declarations
about_founders = False
about_finder = False
array = []
input_string = ""
string = ""
ans = ""
check = ""
message = "Welcome to Finder!"
message2 = ""
pos=[340,300]
 
# Handler to draw on canvas
def draw(canvas):
    if about_founders:
        x = 50
        img1_width = img1.get_width()
        img1_height = img1.get_height()
        img2_width = img2.get_width()
        img2_height = img2.get_height()
        canvas.draw_text("About the Founders", [320,70],40,"White","sans-serif")
        canvas.draw_text("Grishma Jena",[x,150] ,30,"White","sans-serif")
        canvas.draw_text("Grishma is a second year Computer Engineering student.",[x,200] ,25,"Silver","sans-serif")
        canvas.draw_text("She likes to code interactive programs in Python.",[x,230] ,25,"Silver","sans-serif")
        canvas.draw_image(img1, [img1_width // 2, img1_height// 2], [img1_width, img1_height], 
            [850,190], [150,175])
        canvas.draw_text("Chirag Shah",[x,320] ,30,"White","sans-serif")
        canvas.draw_text("Chirag is a second year Computer Engineering student.",[x,370] ,25,"Silver","sans-serif")
        canvas.draw_text("He likes software testing and development.",[x,400] ,25,"Silver","sans-serif")
        canvas.draw_image(img2, [img2_width // 2, img2_height// 2], [img2_width, img2_height], 
            [850,380], [150,185])
         
    elif about_finder:
        canvas.draw_text("About the Finder", [320,70],40,"White","sans-serif")
        canvas.draw_text("The finder is used to search for certain occurrences in a given string.",[50,150] ,25,"Silver","sans-serif")
        canvas.draw_text("The occurrence maybe at the beginning, at the end or anywhere in the string.",[50,180] ,25,"Silver","sans-serif")
        canvas.draw_text("The finder works on the principle of 'Regular Expressions'.",[50,250] ,25,"Silver","sans-serif")
        canvas.draw_text("Regular expressions are specific patterns that provide concise and flexible means to",[50,320] ,25,"Silver","sans-serif")
        canvas.draw_text("match strings of text such as particular characters, words, or patterns of characters.",[50,350] ,25,"Silver","sans-serif")
        canvas.draw_text("The finder was developed on 24th March, 2013 for Theory of Computation course.",[50,420] ,25,"Silver","sans-serif")
          
    elif not about_founders and not about_finder:
        canvas.draw_text(message, pos, 40, "White")
        canvas.draw_text("; ".join(array),[55,250],40,"Blue")
        canvas.draw_text(message2, [55,350],40,"White")
        canvas.draw_text(input_string,[50,70],40,"White")
        canvas.draw_text(string,[255,70],40,"Blue")
 
#About the founders
def founders():
    global about_founders
    about_founders = not about_founders
 
#About the finder
def finder():
    global about_finder
    about_finder = not about_finder
     
#Go back
def back():
    global about_founders, about_finder
    about_founders = about_finder = False
     
#Handler for text string
def text_handler(text):
    global string, message
    message = ""
    string = text
    global input_string
    input_string = "Input string: "
     
#Handler for begins with
def begin_handler(text):
    global check, message, pos, array
    array = []
    message = "Words that begin with '"+text+"' are:"
    pos = [50,150]
    check = "^"+text
    compute()  
                       
#Handler for occurrence of
def all_handler(text):
    global check, message, pos, array
    array = []
    message = "Words that have occurrence of '"+text+"' are:"
    pos = [50,150]
    check = text
    compute()
     
#Handler for ends with
def end_handler(text):
    global check, message, pos, array
    array = []
    message = "Words that end with '"+text+"' are:"
    pos = [50,150]
    check = text+"$"
    compute()
     
#Compuation
def compute():
    words = string.split()
    for w in words:
        match(w)
     
#Evaluation    
def match(w):
    global check, message2
    if(re.findall(check,w,re.IGNORECASE)):
        global array
        array.append(w)
        frame.set_draw_handler(draw)
    message2 = "Total no.of words satisfying search criterion = "+str(len(array))  
 
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home",1010, 600)
frame.set_draw_handler(draw)
frame.add_label("Information:")
frame.add_button("About the finder",finder,200)
frame.add_button("About the founders",founders,200)
 
frame.add_button("Go back",back,200)
frame.add_label(" ")
frame.add_label("Computation:")
text_string = frame.add_input("Enter the string to be searched:",text_handler,200)
begin_string = frame.add_input("Begins with:",begin_handler,200)
all_string = frame.add_input("Occurrence anywhere of:",all_handler,200)
end_string = frame.add_input("Ends with:",end_handler,200)
frame.add_label(" ")
frame.add_label("\nPlease press the Enter key after entering any input.")
frame.set_draw_handler(draw)
 
# Start the frame animation
frame.start()