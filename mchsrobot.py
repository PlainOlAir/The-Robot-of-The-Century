left_motor = "47252153627919119984829"
right_motor = "47258887835223006894371"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    def rightjoymove():
        if abs(Gamepad.get_value("joystick_right_y")) >= 0.1 or abs(Gamepad.get_value("joystick_right_x")) >= 0.1:
            return 3    
    def drive(leftmotor, rightmotor):
        Robot.set_value(left_motor, "duty_cycle", leftmotor)
        Robot.set_value(right_motor, "duty_cycle", rightmotor)
    hello = (Gamepad.get_value("joystick_right_y") + Gamepad.get_value("joystick_right_x"))/2
    bye = (Gamepad.get_value("joystick_right_y") - Gamepad.get_value("joystick_right_x"))/2
    if(3 == rightjoymove())
        drive(-1 * bye, hello)
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
    print(hello)