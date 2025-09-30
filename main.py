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
Stage1Motor = Motor(Ports.PORT21, GearSetting.RATIO_6_1, False)
Stage2Motor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
Preload_Arm = DigitalOut(brain.three_wire_port.a)


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

myVariable = 0
DT_L_Velocity = 0
DT_R_Velocity = 0
Intake_Voltage = 0
Voltage_step = 0
Number_of_steps = 0
Ramp_delay = 0

def when_started1():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    # Initializes required variables during robot startup
    Ramp_delay = 0.01
    Voltage_step = 0.25
    Number_of_steps = 12 / Voltage_step

def when_started2():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    # Synchronizes The Voltage Of The Left And Right Drivetrain Motors With The Controller's Joystick Input
    while True:
        DT_L1.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L2.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L3.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_R1.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R2.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R3.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        wait(5, MSEC)

def onauton_autonomous_0():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    # Sets Drive Train Left And Right Motor's To 0 Volts At The Start Of Autonomous

def onauton_autonomous_1():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    # Initiates intake and vertical stage motors upon autonomous startup

def onauton_autonomous_2():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    pass

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    auton_task_1 = Thread( onauton_autonomous_1 )
    auton_task_2 = Thread( onauton_autonomous_2 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()
    auton_task_1.stop()
    auton_task_2.stop()

def vexcode_driver_function():
    # Start the driver control tasks

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

ws2 = Thread( when_started2 )
when_started1()
