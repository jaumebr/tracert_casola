import os
 
ip = 'localhost'

def demanar_ip():
  global ip 
  ip = raw_input("A quina ip vols fer tracert?")

def fer_tracert():
  for ttl in range (1, 10): 
    result = os.popen('ping -c 1 -t ' + str(ttl) + ' ' + ip)
    aux = result.read().split("\n")
    print 'Per ttl = ' + str(ttl) + ' obtenim: ' + aux[1]

if __name__ == "__main__":
  demanar_ip()
  print ip
  fer_tracert()

