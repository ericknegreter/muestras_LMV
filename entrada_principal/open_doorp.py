import RPi.GPIO as GPIO
import os
import mysql.connector
from mysql.connector import Error
import time
import subprocess, datetime

#Active GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)

#test host
hosts = ('google.com', 'kernel.org', 'yahoo.com')
localhost = ('10.0.5.246')

def ping(host):
    ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w'))
    return ret == 0

def net_is_up():
    print ("[%s] Checking if local network is up..." % str(datetime.datetime.now()))
    
    xstatus = 1
    if ping(localhost):
        print ("[%s] Local network is up!" % str(datetime.datetime.now()))
        xstatus = 0

    if xstatus:
        time.sleep(10)
        print ("[%s] Local network is down :(" % str(datetime.datetime.now())) 
        time.sleep(25)
    
    return xstatus

while True:
    if(net_is_up() == 0):
        #Connection to database LMV and update record in e_extraccion table with mysql
        mydb = mysql.connector.connect(host="10.0.5.246", user="LMV_ADMIN", passwd="LABORATORIOT4", database="LMV")
        mycursor = mydb.cursor()
        sql = "SELECT estado FROM e_extraccion WHERE dispositivo='puerta'"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        print(mycursor.rowcount, "record selected.")
        for row in records:
            estado = int(row[0])
        if estado == 0:
            #os.system('gpio -g mode 22 out')
            GPIO.output(22, True)
            time.sleep(15)
            sql2 = "UPDATE r_muestras SET estado = 1 WHERE dispositivo='puerta'"
            mycursor.execute(sql2)
            mydb.commit()
            print(mycursor.rowcount, "record affected.")
            GPIO.output(22, False)
            sql2 = "UPDATE r_muestras SET estado = 0 WHERE dispositivo='puerta'"
            mycursor.execute(sql2)
            mydb.commit()
            print(mycursor.rowcount, "record affected.")
            time.sleep(1)
            #END of mysql
        elif estado == 1:
            print("<p>close the laboratory door<p>")
            #os.system('gpio -g mode 26 out')
            #time.sleep(10)
            #os.system('gpio -g mode 26 in')
        break
