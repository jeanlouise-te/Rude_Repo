from machine import Timer
from machine import ADC, Pin
from machine import Pin, PWM
from Button import Button
from time import sleep
from servo import Servo

SERVO_PIN_NUMBER = 21 # change pin number
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin)

# Mic pin
microphone_l = ADC(28)
microphone_2 = ADC(26)

# internal timer 
reset_timer = Timer(-1)
#end_game = Timer(30)

# motor
base_freq = 80
base_duty_cycle = 0

# create a controllable PWM Pin
motor_right = PWM(Pin(19))
motor_left = PWM(Pin(20))

# create id for the motor
MOTOR_LEFT = 0
MOTOR_RIGHT = 1

game_state = 0

speed = 0



def change_state(new_state):
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

def change_speed(speed, motor_id):
    if motor_id == MOTOR_RIGHT:
        motor_right.freq(base_freq)
        motor_right.duty_u16(speed)
    if motor_id == MOTOR_LEFT:
        motor_left.freq(base_freq)
        motor_left.duty_u16(speed)


def buttonAaction(little_pin, massive_event):
    if massive_event == Button.RELEASED:
        sleep(1) # some time to let people prepare
        print("hey")
        game_state == 1 # this is the button needed to transit from a rest state to active (wheel speen, etc...)
        return
buttonA = Button(4, rest_state = True, callback = buttonAaction)
    


while(True):
    if game_state == 0:
        # reset_timer.init(period = 3000, mode = Timer.ONE_SHOT)
        buttonA.update()
        pass

    if game_state == 1:
        motor_right.update()
        motor_left.update()
        microphone_l.update()
        microphone_2.update()
        #magnetA.update()
        pass
