# states:
# 0: this is the rest state -> "Rudy" is waitong for somebody to press the button
# 1: The wheels start to spin and the mics are on
# 2: The sound is to loud and rude state is triggered
# 3: Win state is triggered because gthe magnet was reached
# 4: To much time have passed so Rudy stop to play

from machine import Timer
from Button import Button
from time import sleep

reset_timer = Timer(-1)

game_state = 0

winning_player = 0

speed = 0

def change_state(new_state):
    print(f"change of state to {new_state}")
    global game_state
    if new_state == 0:
        display.clear()
        display.write("  play with me")
        display.move(0, 1)
        display.write("  press button")
        
    if new_state == 1:
        display.clear()
        display.write("    2 players")
        display.move(0, 1)
        display.write("   fastest wins")
        
    if new_state == 2:
        display.clear()
        display.write("game ongoing")
        display.move(0, 1)
        display.write("2 players")
    
    if new_state == 3:
        display.clear()
        display.write("  the winner is")
        display.move(0, 1)
        display.write(f"player {winning_player}")
        # start reset time

    game_state = new_state
    
def loudness():
    if threshold < 20000
        speed = 1
    if threshold < 30000
        speed = 2
    if threshold < 40000
        speed = 3
    

    
    #Motor R turning def
def motorRturn():
    global speedR
    speedR = speedR + 1
    # replace + 1 with any value for speed increase

    #Motor L turning def
def motorLturn():
    global speedL
    speedL = speedL + 1
    # replace + 1 with any value for speed increase
    
def buttonAaction(little_pin, massive_event):
    if massive_event == Button.RELEASED:
        sleep(3) # some time to let people prepare
        change_state(1) # this is the button needed to transit from a rest state to active (wheel speen, etc...)
        return
    
# define when the rude state is triggered
def rudeAction(little_pin, massive_event):
    if loud == soundthreshold > 40000: # when to loud that trigger the servo "rude flag"
        servoR.motor(90) ... # define servo motor action
        kitR.motor(80) # define the behaviour of the motor
        sleep(0.1)
        kitR.motor(90) and kitL.motor(90) # both motor continuing to the same side
        sleep(0.1)
        change_state(0)
        
# define when the rude state is triggered
def winAction(little_pin, massive_event):
    if magnet == magnetSensor(1): # when the magnet is reconised
        servoL.motor(90) ... # define servo motor action
        sleep(0.1)
        change_state(0)

buttonA = Button(26, rest_state = True, callback = buttonAaction)

change_state(0)

#this is the timer off (state 5)
def reset_game(timer_object):
    change_state(0)
    
while(True):
    if game_state == 0:
        reset_timer.init(period = 3000, mode = Timer.ONE_SHOT, callback = reset_game)
        buttonA.update()
        pass

    if game_state == 1:
        # do game state things
        motor1.update()
        motor2.update()
        mic1.update()
        mic2.update()
        magnetSensor.update()
        pass
    
    if game_state == 2:
        # game is running
        servoR.update()
        buttonB.update()
        pass
    
    if game_state == 3:
        servoL.update()
        pass

