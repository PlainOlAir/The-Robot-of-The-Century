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
  
  for u in range(len(n) -1, -1, -1):
    if n[u] >= 10:
        n[u] = n[u] - 10
    z *= 10
    z += n[u]

  o = list(str(z))
  ha = 0
  
  for xd in range(len(o)-1, -1, -1):
    ha *= 10
    ha += int(o[xd])
  return(ha)
  
def valid_isbn_ten(num):
  o = list(str(num))
  n = 0
  r = 1
  for i in range(len(o) - 1, -1, -1):
    if r <= 10:
      n += int(o[i]) * r
      r += 1
    print(n)
  
  if n % 11 == 0:
    return(num)
  else:
    for xd in range(0, 1000):
      num += 1
      o = list(str(num))
      n = 0
      r = 1
      for xd in range(len(o) - 1, -1, -1):
        if r <= 10:
          n+= int(o[xd]) * r
          r += 1
      if n % 11 == 0:
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
  return(int(imdone))