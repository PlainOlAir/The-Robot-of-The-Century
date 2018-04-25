left_motor = "47260374648549928326927"
right_motor = "47252153627919119984829"
leftpull_motor = "47257803039701938059387"
rightpull_motor = "47258887835223006894371"

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
      return(i)
      
    def smallest_prime_fact(num):
      primes = [0] * (num + 1)
      primes[1] = 1
      
      for i in range(2, num + 1):
        if (primes[i] == 0):
          primes[i] = i
          for j in range(2 * i, num + 1, i):
            if(primes[j] == 0):
              primes[j] = i
      return(primes[num])
      
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
      return(count_main)
      
    def silly_base_two(num):
      n = str(bin(num))
      n = n[:0] + n[(2):]
      return(n)
      
    def double_caesar_cipher(num):
      i = list(str(num))
      n = list(str(3141592653))
      z = 0
      o = []
      i = i * len(n)
      index_tmp = 0
      for u in range(len(n) - 1, -1, -1):
        n[u] = int(n[u]) + int(i[index_tmp])
        index_tmp += 1
      for u in range(len(n) -1, -1, -1):
        if n[u] >= 10:
            n[u] = n[u] - 10
        z *= 10
        z += n[u]
      o = list(str(z))
      z = 0
      for t in range(len(o) - 1, -1, -1):
        z*= 10
        z += int(o[t])
      return(z)
	  
    def valid_isbn_ten(num):
      o = list(str(num))
      n = 0
      r = 10
      for i in range(0, len(o)):
        if r >= 1:
          n += int(o[i]) * r
          r -= 1
    
      if n % 11 == 0:
        print(num)
      else:
        for oof in range(1,12):
          if n%11 != 0:
            num += 1
            o = list(str(num))
            r = 10
            n = 0
            for i in range(0, len(o)):
              if r >= 1:
                n += int(o[i]) * r
                r -= 1
              else:
                pass
          else:
            pass
        return(num)
        
    def simd_four_square(num):
      i = list(str(num))
      p = []
      q = []
      numlist = []
      numnumlist = []
      l = []
      imdone = 0
      for u in range(0,5):
        if len(i)%4 != 0:
          i.insert(0, '0')
        else:
          pass
        
      i.append(i[0])
      del i[0]
      
      k = len(i)/4
      r = -1
      for o in range(0, len(i)/k):
        e = []
        for t in range(0, len(i)/4):
          e.append(i[t + r])
        p.append(e)
        r += k
      
      for urmomgay in range(0,4):
        l = p[urmomgay]
        numtemp = 0
        for nou in range(0, len(p[urmomgay])):
          numtemp *= 10
          numtemp += int(l[nou])
        q.append(str(numtemp))
      
      for gae in range(0, 4):
        n = 0
        sleeper = []
        n = (int(q[gae]) ** 2)
        sleeper = list(str(n))
        while len(sleeper) > k:
          del sleeper[0]
        numlist.append(sleeper)
      
      for k in range(0,4):
        for hm in range(0, len(numlist[k])):
          tempnumlist = numlist[k]
          numnumlist.append(tempnumlist[hm])
      
      for lol in range(0,4):
        if len(numnumlist) < len(i):
          numnumlist.insert(0, '0')
      
      for ha in range(0, len(numnumlist)):
        imdone *= 10
        imdone += int(numnumlist[ha])
      return(imdone)
