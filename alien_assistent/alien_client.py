import random
import pgzrun
import time
WIDTH=500
HEIGHT=500
text="I CAN SEE YOU"
msg=''
death=''
more=0
alien=Actor('alien.png')
print("Hello Welcome to alien client. You may move me around. You may not click me. You may ask me questions in the terminal below. (: ")
msg=" Hello Welcome to alien client.\n\n You may move me around.\n\n You may not click me.\n\n You may ask me questions in the \n\n terminal below. (: "
def draw():
    screen.fill('blue')
    alien.draw()
    screen.draw.text(msg,(0,150), fontsize=35)
    screen.draw.text(death,(70,250),fontsize=100,color='red')
def update():
    global msg
    global death
    global more
    if keyboard.left:
        alien.x-=10
    if keyboard.right:
        alien.x+=10
    if keyboard.up:
        alien.y-=10
    if keyboard.down:
        alien.y+=10
    if alien.x>500:
         alien.x=300
         alien.y=300
         msg="DON'T PUSH ME IN THE WALL"
    if alien.y>500:
         alien.x=300
         alien.y=300
         msg="DON'T PUSH ME IN THE WALL"#
    if alien.x<0:
         alien.x=300
         alien.y=300
         msg="DON'T PUSH ME IN THE WALL"
    if alien.y<0:
         alien.x=300
         alien.y=300
         msg="DON'T PUSH ME IN THE WALL"
def alien_clicker():
    alien.x=random.randint(0,500)
    alien.y=random.randint(0,500)
def on_mouse_down(pos):
    global msg
    global death
    global more
    if alien.collidepoint(pos):
        alien_clicker()
        if more==0:
            msg="DON'T TOUCH ME"
            more+=1
        elif more==1:
            msg="I TOLD DON'T TOUCH ME"
            more+=1
        elif more==2:
            msg="I TOLD DON'T TOUCH ME"
            more+=1
        elif more==3:
            msg="STOP I'LL KILL YOU!!!!!!"
            more+=1
        elif more==4:
            msg="ONE MORE TIME AND YOU'RE DEAD!!!"
            more+=1
        elif more==5:
            death='YOU DIED!!!'
            file = open("file.txt","a")
            file.write("\n"+text)
    else:
         msg="Imagine trying to touch me and failing misrebly"
pgzrun.go()