leftfront = "47252153627919119984829"
leftback = "47257803039701938059387"
test = "47260374648549928326927"
rightback = ""

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
    Robot.set_value(leftfront, "duty_cycle", Gamepad.get_value("joystick_left_y")/3)
    Robot.set_value(leftback, "duty_cycle", Gamepad.get_value("joystick_left_y")/2)
    Robot.set_value(test, "duty_cycle", Gamepad.get_value("joystick_right_y")/2)