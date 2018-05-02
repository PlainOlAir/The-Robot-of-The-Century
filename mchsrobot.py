leftfront = "47252153627919119984829"
leftback = "47257803039701938059387"
leftlift = "47250928910558050271349"
rightfront = "47260374648549928326927"
rightback = "47248357212803989927318"
rightlift = "47245107631008836712594"
rfid = "51964702830827894976874"

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
  if num == 0:
      return(0)
    
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

  for k in range(0, 10):
    count_tmp = 0
    for o in range(0, len(u)):
      if u[o] == k:
        count_tmp += 1
    count_list.append(count_tmp)
  print(count_list)
  
  for m in range (1,10):
    print(m)
    if count_list[m] >= count_list[count_main]:
      count_main = m
      
  return(count_main)
  
def silly_base_two(num):
  n = str(bin(num))
  n = n[:0] + n[(2):]
  return(int(n))
  
def double_caesar_cipher(num):
  i = list(str(num))
  n = list(str(3141592653))
  z = 0
  o = []
  i = i * len(n)
  index_tmp = len(i) - 1

  for u in range(len(n) - 1, -1, -1):
    n[u] = int(n[u]) + int(i[index_tmp])
    index_tmp -= 1
  
  for u in range(0, len(n)):
    if n[u] >= 10:
        n[u] = n[u] - 10
    z *= 10
    z += n[u]
  
  return(z)
  
def valid_isbn_ten(num):
    for xd in range(0, 1000):
      o = list(str(num))
      n = 0
      r = 1
      for xd in range(len(o) - 1, -1, -1):
        if r <= 10:
          n+= int(o[xd]) * r
          r += 1
      if n % 11 == 0:
        return(num)
      else:
        num += 1
      
      

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
  return(int(imdone))


def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    def drive(speed, i): #+/- 0-0.5, -1 = forward/backward 1 = turning
        speed = speed * -1
        Robot.set_value(leftfront, "duty_cycle", i * speed)
        Robot.set_value(leftback, "duty_cycle", i * speed)
        Robot.set_value(rightfront, "duty_cycle", speed)
        Robot.set_value(rightback, "duty_cycle", speed)
    
    drive(0.5, -1)
    await Actions.sleep(0.75)
    drive(0, 1)
    await Actions.sleep(0.5)
    drive(0.5, 1)
    await Actions.sleep(4)
    drive(0, 1)
    

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
        Robot.set_value(leftlift, "duty_cycle", 0.9 * speed)
        Robot.set_value(rightlift, "duty_cycle", -1 * speed)
    
    if Gamepad.get_value("r_bumper") == 1 and Gamepad.get_value("l_bumper") == 1:
        stop()

    Robot.set_value(leftfront, "duty_cycle", -1 * Gamepad.get_value("joystick_left_y")/3)
    Robot.set_value(leftback, "duty_cycle", -1 * Gamepad.get_value("joystick_left_y")/2)
    Robot.set_value(rightfront, "duty_cycle", Gamepad.get_value("joystick_right_y")/2)
    Robot.set_value(rightback, "duty_cycle", Gamepad.get_value("joystick_right_y")/2)
    
    if Gamepad.get_value("button_a") == 1:
        lift(-0.2)
    if Gamepad.get_value("button_y") == 1:
        lift(0.2)
    if Gamepad.get_value("button_x") == 1:
        lift(0)
    if Gamepad.get_value("dpad_up") == 1:
        Robot.set_value(leftlift, "duty_cycle", 0.2)
    if Gamepad.get_value("dpad_down") == 1:
        Robot.set_value(leftlift, "duty_cycle", -0.2)
    if Gamepad.get_value("dpad_left") == 1:
        Robot.set_value(rightlift, "duty_cycle", 0.2)
    if Gamepad.get_value("dpad_right") == 1:
        Robot.set_value(rightlift, "duty_cycle", -0.2)
        
    if Robot.get_value(rfid, "tag_detect"):
        xd = Robot.decode_message(Robot.get_value(rfid, "id"))
        print("Attempt to decode was ", xd)
        return(xd)