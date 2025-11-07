#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
DT_L1 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
DT_L2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
DT_L3 = Motor(Ports.PORT18, GearSetting.RATIO_6_1, True)
DT_R1 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
DT_R2 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
DT_R3 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
Stage1Motor = Motor(Ports.PORT7, GearSetting.RATIO_6_1, True)
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
            # to control Stage2Motor
            if controller_1.buttonL1.pressing():
                Stage2Motor.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                Stage2Motor.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                Stage2Motor.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control Stage1Motor
            if controller_1.buttonR1.pressing():
                Stage1Motor.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                Stage1Motor.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                Stage1Motor.stop()
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

def ondriver_drivercontrol_0():
    # Synchronizes The velocity to The Left And Right Drivetrain Motors With The Controller's Joystick Input
    Stage1Motor.stop()
    while True:
        DT_L1.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L2.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L3.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_R1.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R2.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R3.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        wait(5, MSEC)

def ondriver_drivercontrol_1():
    # Set stage one and two motors to 100 velocity at the start of the match
    Stage1Motor.set_velocity(100, PERCENT)
    Stage2Motor.set_velocity(100, PERCENT)
    Stage1Motor.set_max_torque(100, PERCENT)
    Stage2Motor.set_max_torque(100, PERCENT)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )
    driver_control_task_1 = Thread( ondriver_drivercontrol_1 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()
    driver_control_task_1.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )
