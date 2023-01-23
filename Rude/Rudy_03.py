from machine import Timer
from machine import ADC, Pin
from machine import Pin, PWM
from Button import Button
from time import sleep
from servo import Servo
# Servo print
SERVO_PIN_NUMBER = 16 # change pin number
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin)
SERVO_PIN_NUMBER2 = 19# change pin number
servo_pin = PWM(Pin(SERVO_PIN_NUMBER2))
servo_motor2 = Servo(servo_pin)
# Mic pin
microphone_l = ADC(28)
microphone_2 = ADC(26)

# motor
base_freq = 80
base_duty_cycle = 0
# create a controllable PWM Pin
motor_right = PWM(Pin(19))
motor_left = PWM(Pin(20))
# create id for the motor
MOTOR_LEFT = 0
MOTOR_RIGHT = 1
speed = 0

# internal timer
reset_timer = Timer(-1)
# end_game = Timer()

game_state = 0

 # Where to put Global
def change_state(new_state):
    print(f"change of state to {new_state}")
    global game_state
    if new_state == 0:
        pass
    if new_state == 1:
        pass
    if new_state == 2:
        pass
    if new_state == 3:
        pass

    game_state = new_state


def loudnessR():
    while True:
        sound_level_1 = microphone_l.read_u16()
        print(sound_level_1)
        if(sound_level_1 < 600 and sound_level_1 > 39999):
            change_speed(20, 1)# put the value corresponding to motor power
            print('turn1')
            change_speed(0,1) # return to original state
        if(sound_level_1 > 40000 and sound_level_1 < 44999):
            change_speed(30, 1)# put the value corresponding to motor power
            print('turn2')
            sleep(0.5)
            change_speed(0,1) # return to original state
        if(sound_level_1 > 45000):
            print("rude!")
            rudeAction()
            sleep(0.5)

def loudnessL():
    while True:
        sound_level_2 = microphone_2.read_u16()
        print(sound_level_2)
        if(sound_level_2 < 600 and sound_level_2 > 39999):
            change_speed(20, 0)# put the value corresponding to motor power
            print('turn1')
            sleep (0.5)
            change_speed(0,0) # return to original state
        if(sound_level_2 > 40000 and sound_level_2 < 44999):
            change_speed(30,0)
            print('turn2')
            sleep(0.5)
            change_speed(0,0) # return to original state
        if(sound_level_2 > 45000):
            print("rude!")
            rudeAction()
            sleep(0.5)

def change_speed(speed, motor_id):
    if motor_id == MOTOR_RIGHT:
        motor_right.freq(base_freq)
        motor_right.duty_u16(speed)
    if motor_id == MOTOR_LEFT:
        motor_left.freq(base_freq)
        motor_left.duty_u16(speed)

def servo_action():
    while(1):
        servo_motor.goto(0)
        sleep(1)
        servo_motor.goto(90)
        sleep(1)

def servo_action2():
    while(1):
        servo_motor2.goto(0)
        sleep(1)
        servo_motor2.goto(90)
        sleep(1)

'''''
def magnet1_action(pin,event) :
    if game_state == 1 and event == Button.PRESSED :
        game_state(3)
        return
'''

def buttonAaction(little_pin, massive_event):
    if massive_event == Button.RELEASED:
        sleep(1) # some time to let people prepare
        print("hey")
        game_state == 1 # this is the button needed to transit from a rest state to active (wheel speen, etc...)
        return

# define when the rude state is triggered
def rudeAction():
    # if loud == soundthreshold > 40000: # when to loud that trigger the servo "rude flag"
    servo_motor.goto(90) # define servo motor action
    change_speed(20, 1) # define the behaviour of the motor
    sleep(0.1)
    change_speed(20,1) and change_speed(20,0) # both motor continuing to the same side
    sleep(5)
    game_state(0)

'''''
# define when the rude state is triggered
def winAction():
    if magnet1_action(True): # when the magnet is reconised
        servo_motor(20,0) # define servo motor action
        sleep(1)
        game_state(0)
'''''
buttonA = Button(4, rest_state = True, callback = buttonAaction)
'''''
magnetA = Button(26, rest_state = True, callback = magnet1_action) # change pin
'''''
#this is the timer off (state 5)
def reset_game():
    game_state(0)
# states:
# 0: this is the rest state -> "Rudy" is waitong for somebody to press the button
# 1: The wheels start to spin and the mics are on
# 2: The sound is to loud and rude state is triggered
# 3: Win state is triggered because gthe magnet was reached
# 4: To much time have passed so Rudy stop to play
while(True):
    if game_state == 0:
        # reset_timer.init(period = 3000, mode = Timer.ONE_SHOT)
        buttonA.update()
        pass

    if game_state == 1:
        print("I'm in state one")
        motor_right.update()
        motor_left.update()
        microphone_l.update()
        microphone_2.update()
        #magnetA.update()
        pass
    if game_state == 2:
        servo_motor.update()
        buttonA.update()
        pass

    if game_state == 3:
        servo_motor.update()
        pass