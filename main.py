myVariable = 0
DT_L_Velocity = 0
DT_R_Velocity = 0
Intake_Voltage = 0
Voltage_step = 0
Number_of_steps = 0
Ramp_delay = 0

def when_started1():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    while True:
        DT_L1.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L2.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_L3.spin(FORWARD, (controller_1.axis3.position() / 1), VOLT)
        DT_R1.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R2.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        DT_R3.spin(FORWARD, (controller_1.axis2.position() / 1), VOLT)
        wait(5, MSEC)

def when_started2():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    Ramp_delay = 0.01
    Voltage_step = 0.25
    Number_of_steps = 12 / Voltage_step

def onauton_autonomous_0():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    pass

def onauton_autonomous_1():
    global myVariable, DT_L_Velocity, DT_R_Velocity, Intake_Voltage, Voltage_step, Number_of_steps, Ramp_delay
    while True:
        Stage1Motor.spin(FORWARD, Intake_Voltage, VOLT)
        wait(5, MSEC)

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
