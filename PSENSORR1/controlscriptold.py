#!/usr/bin/python3.5
#Voice Recognition
import speech_recognition as sr
import os
import unidecode

#Image Capturin
import datetime
import sys
import time
import subprocess

#Store Image
import mysql.connector

#Turn on/off LEDS
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

def store(path, name):
    #Connection and insert with mysql complete
    mydb = mysql.connector.connect(host="10.0.5.246", user="LMV_ADMIN", passwd="LABORATORIOT4", database="LMV")
    mycursor = mydb.cursor()
    sql = "INSERT INTO imagespath (path, name) VALUES (%s, %s)"
    val = (path, name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")

def take_photo():
    script_dir = os.path.dirname(__file__)
    direc = os.path.dirname(os.path.abspath(__file__))
    os.system('./webcam.sh')
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    real_path = currentdate +".jpg"
    abs_file_path = os.path.join(script_dir, real_path)
    GPIO.output(21, False)
    GPIO.output(16, True)
    time.sleep(2)
    print("--------------------------------------------------")
    print(direc)
    print(abs_file_path)
    print("--------------------------------------------------")
    store(direc, abs_file_path)
    GPIO.output(16, False)
    time.sleep(2)
    return False

def listen_welcome():
    r = sr.Recognizer()
    with m as source:
        print("Adjusting noise")
        r.adjust_for_ambient_noise(source, duration=-1)
        print("Say something!")
        try:
            GPIO.output(21, False)
            GPIO.output(12, True)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            GPIO.output(12, False)
            GPIO.output(21, True)
            print("LISTENED")
            print("Trying to recognize")
            x = r.recognize_google(audio, language="es-mx")
            print(x)
            if (x=="Ok blackstar" or x=="Ok, blactar" or x=="ok, blacstar" or ("ok" in x)or ("Ok" in x)or ("Black Star" in x)):
                return True
        except sr.UnknownValueError:
            print("Error trying to understand what you say to me")
            return False
        except sr.RequestError as e:
            print("I can't reach google, it's to sad")
            return False
        except Exception as e:
            print(e)
            return  False

while True:
    try:
        r = sr.Recognizer()
        m = sr.Microphone()
        flag_order = True
        flag_start=listen_welcome()
        if flag_start:
            while flag_order:
                flag_order = take_photo()
    except ValueError:
        GPIO.cleanup()
        print("Tube un problemenshon xD")
