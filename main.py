#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
DT_L1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
DT_L2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
DT_L3 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
DT_R1 = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
DT_R2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
DT_R3 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
Stage1Motor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
Stage2Motor = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)


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



# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # check the buttonL1/buttonL2 status
            # to control DT_L2
            if controller_1.buttonL1.pressing():
                DT_L2.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                DT_L2.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                DT_L2.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control DT_L1
            if controller_1.buttonR1.pressing():
                DT_L1.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                DT_L1.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                DT_L1.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

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

when_started1()
