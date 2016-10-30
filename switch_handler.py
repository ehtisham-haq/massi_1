import RPi.GPIO as GPIO
import sys
import os
import time

class setup_pinout:

    def __init__(self):
        self.A = 8
        self.B = 16
        self.C = 11
        self.D = 22
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.A,GPIO.OUT)
        GPIO.setup(self.B,GPIO.OUT)
        GPIO.setup(self.C,GPIO.OUT)
        GPIO.setup(self.D,GPIO.OUT)

    def get_status(self):
        try:
            with open('status', 'r') as file:
                self.data = file.readlines()
                file.close()
        except IOError:
            print "Warning: status file is used by another process"

        #print self.data
        return self.data

    def set_output(self, pin_code, state):
        self.pin_code = pin_code
        self.state = state.rsplit()[1]
        # print self.state
        # print self.pin_code
        if self.state == "ON":
            # print self.state
            GPIO.output(self.pin_code,GPIO.HIGH)
        else:
            GPIO.output(self.pin_code, GPIO.LOW)

    def switch_handler(self):
        self.status = self.get_status()
        # print self.status[13].rsplit()
        # print self.status[17].rsplit()
        # print self.status[21].rsplit()
        # print self.status[25].rsplit()

        self.set_output(self.A, self.status[13])    ##Do not change this numbers
        self.set_output(self.B, self.status[17])    ##Do not change this numbers
        self.set_output(self.C, self.status[21])    ##Do not change this numbers
        self.set_output(self.D, self.status[25])    ##Do not change this numbers

    def test_switch(self):
        wait = .5
        self.set_output(self.A, "> ON")
        time.sleep(wait)
        self.set_output(self.A, "> OFF")
        self.set_output(self.B, "> ON")
        print "Done!!: testing switch A"
        time.sleep(wait)
        self.set_output(self.B, "> OFF")
        self.set_output(self.C, "> ON")
        print "Done!!: testing switch B"
        time.sleep(wait)
        self.set_output(self.C, "> OFF")
        self.set_output(self.D, "> ON")
        print "Done!!: testing switch C"
        time.sleep(wait)
        self.set_output(self.D, "> OFF")
        print "Done!!: testing switch D"
        print "All switches are working correctly"

    # def test_switch(self, pin_code, state):
    #     self.pin_code = pin_code
    #     self.state = state
    #     self.switch_pin = 'z'
    #
    #     if self.pin_code == 'A':
    #         self.switch_pin = self.A
    #
    #     elif self.pin_code == 'B':
    #         self.switch_pin = self.B
    #
    #     elif self.pin_code == 'C':
    #         self.switch_pin = self.C
    #
    #     elif self.pin_code == 'D':
    #         self.switch_pin = self.D
    #
    #     if self.state == "HIGH":
    #         GPIO.output(self.switch_pin,GPIO.HIGH)
    #     else:
    #         GPIO.output(self.switch_pin, GPIO.LOW)