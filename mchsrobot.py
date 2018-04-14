left_motor = "47260374648549928326927"
right_motor = "47258887835223006894371"
leftpull_motor = "47257803039701938059387"
rightpull_motor = "47252153627919119984829"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    quicc = 1
    slow = 0.5 #drive
    def lift(speed):
        Robot.set_value(leftpull_motor, "duty_cycle", speed)
        Robot.set_value(rightpull_motor, "duty_cycle", -speed)
    def drive(leftmotor,rightmotor): #drive function
        Robot.set_value(left_motor, "duty_cycle", (-1 * leftmotor))
        Robot.set_value(right_motor, "duty_cycle", rightmotor)
    
    #lift
    if(Gamepad.get_value("button_y") == 1):
        lift(0.25)
    elif(Gamepad.get_value("button_a") == 1):
        lift(-0.15)
    elif(Gamepad.get_value("button_x") == 1):
        lift(0)
    elif(Gamepad.get_value("dpad_up") == 1):
        Robot.set_value(leftpull_motor, "duty_cycle", 0.25)
    elif(Gamepad.get_value("dpad_down") == 1):
        Robot.set_value(leftpull_motor, "duty_cycle", -0.15)
    elif(Gamepad.get_value("dpad_right") == 1):
        Robot.set_value(rightpull_motor, "duty_cycle", -0.25)
    elif(Gamepad.get_value("dpad_left") == 1):
        Robot.set_value(rightpull_motor, "duty_cycle", 0.15)
    
    
        #motors will drive at 0.5 due to speed
    else:
        #these two take half the joystick value and move motors
        Robot.set_value(left_motor, "duty_cycle", (-1 * Gamepad.get_value("joystick_left_y"))) 
        Robot.set_value(right_motor, "duty_cycle", (Gamepad.get_value("joystick_right_y")))
    print("smile") #end line to test if program runs all the way
    
def Robot_decode():
    
    def next_power(num):
        count = 0
        if(num == 0):
          return 1
        elif(num & (num - 1) == 0):
          return num
        while(num != 0):
            num >>= 1
            count += 1
        return 1 << count
    
    def reverse_digits(num):
        i = 0
        u = 0
        while(num > 0):
          u = num % 10
          i = (i*10) + u
          num = num//10
            
    def smallest_prime_fact(num):
      primes = [0] * (num + 1)
      primes[1] = 1
      
      for i in range(2, num + 1):
        if (primes[i] == 0):
          primes[i] = i
          for j in range(2 * i, num + 1, i):
            if(primes[j] == 0):
              primes[j] = i
      print(primes[num])
      
    def most_common_digit(num):
      i = str(num)
      u = []
      count_tmp = 0
      count_list = []
      count_main = 0
      for digit in i:
        u.append(int(digit))
    
      for k in range(1, 9):
        count_tmp = 0
        for o in range(0, len(u) - 1):
          if u[o] == k:
            count_tmp += 1
        count_list.append(count_tmp)
        
      for m in range (1,9):
        if count_list[m-1] >= count_main:
          count_main = m
      print(count_main)
      
    def silly_base_two(num):
      n = str(bin(num))
      n = n[:0] + n[(2):]
      print(n)