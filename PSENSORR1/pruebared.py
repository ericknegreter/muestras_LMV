import subprocess, datetime

hosts = ('google.com', 'kernel.org', 'yahoo.com')

def ping(host):
    ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w'))
    return ret == 0

def net_is_up():
    print ("[%s] Checking if network is up..." % str(datetime.datetime.now()))

    xstatus = 1
    
    for h in hosts:
        if ping(h):
            print ("[%s] Network is up!" % str(datetime.datetime.now()))
            xstatus = 0
            break

    if xstatus:
        print ("[%s] Network is down :(" % str(datetime.datetime.datetime.now()))
    
    print(xstatus)
    return xstatus

l = net_is_up()

print(l)
