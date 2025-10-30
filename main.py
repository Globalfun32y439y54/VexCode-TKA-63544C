#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
DT_L1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
DT_L2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
DT_L3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
DT_R1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
DT_R2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
DT_R3 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
Stage1Motor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
Stage2Motor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project: PushbackDTCodePhilosophers
#	Author: BrayDog2010
#	Created: 9/10/25
#	Description: VEXcode V5 Python Project For Team TKA 63544C
# 
# ------------------------------------------

DT_L_Velocity = 0
DT_R_Velocity = 0
Intake_Voltage = 0
Velocity_step = 0
Number_of_steps = 0
Ramp_delay = 0
Ramp_voltage = 0

def when_started1():
    global DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Velocity_step, Number_of_steps, Ramp_delay, Ramp_voltage
    # Synchronizes The Voltage Of The Left And Right Drivetrain Motors With The Controller's Joystick Input
    while True:
        DT_L1.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L2.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L3.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_R1.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R2.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R3.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        wait(5, MSEC)

def when_started2():
    global DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Velocity_step, Number_of_steps, Ramp_delay, Ramp_voltage
    # Push down on R1 to activated long goal scoring
    while True:
        if controller_1.buttonR1.pressing():
            Stage1Motor.spin(FORWARD, 10, VOLT)
            Stage2Motor.spin(FORWARD, 10, VOLT)
        if not controller_1.buttonR1.pressing():
            Stage1Motor.stop()
            Stage2Motor.stop()
        wait(5, MSEC)

ws2 = Thread( when_started2 )
when_started1()
