leftfront = "47252153627919119984829"
leftback = "47257803039701938059387"
leftlift = "47250928910558050271349"
rightfront = "47260374648549928326927"
rightback = "47248357212803989927318"
rightlift = "47245107631008836712594"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
	pass

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    
    def stop():
        Robot.set_value(leftlift, "duty_cycle", 0)
        Robot.set_value(rightlift, "duty_cycle", 0)
        Robot.set_value(leftfront, "duty_cycle", 0)
        Robot.set_value(leftback, "duty_cycle", 0)
        Robot.set_value(rightfront, "duty_cycle", 0)
        Robot.set_value(rightback, "duty_cycle", 0)
    
    def lift(speed):
        Robot.set_value(leftlift, "duty_cycle", speed)
        Robot.set_value(rightlift, "duty_cycle", speed)
        
    print("smile")
    
    if Gamepad.get_value("r_bumper") == 1 and Gamepad.get_value("l_bumper") == 1:
        stop()

    Robot.set_value(leftfront, "duty_cycle", -1 * Gamepad.get_value("joystick_left_y")/3)
    Robot.set_value(leftback, "duty_cycle", -1 * Gamepad.get_value("joystick_left_y")/2)
    Robot.set_value(rightfront, "duty_cycle", Gamepad.get_value("joystick_right_y")/2)
    Robot.set_value(rightback, "duty_cycle", Gamepad.get_value("joystick_right_y")/2)
    
    if Gamepad.get_value("button_a") == 1:
        lift(0.2)
    if Gamepad.get_value("button_y") == 1:
        lift(-0.2)
    if Gamepad.get_value("button_x") == 1:
        lift(0)
    if Gamepad.get_value("dpad_up") == 1:
        Robot.set_value(leftlift, "duty_cycle", -0.2)
    if Gamepad.get_value("dpad_down") == 1:
        Robot.set_value(leftlift, "duty_cycle", 0.2)