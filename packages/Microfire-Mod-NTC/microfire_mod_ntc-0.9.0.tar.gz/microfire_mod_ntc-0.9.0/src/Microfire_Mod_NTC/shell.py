#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
if int(str(range(3))[-2]) == 2:
  sys.stderr.write("You need python 3.0 or later to run this script\n")
  exit(1)

import cmd, sys
import Microfire_Mod_NTC
ntc = Microfire_Mod_NTC.i2c()

fw_compatible = 1
hw_compatible = 2

class Mod_Temp_Shell(cmd.Cmd):
    intro="Type `help` for a list of commands\n`enter` repeats the last command"
    prompt = '> '

    def do_config(self, a):
        """prints out all the configuration data\nparameters: none"""
        print("Mod-Temp Config: ", end='')
        if ntc.connected():
            print_green('connected')
            ntc.update()
            if (ntc.fwVersion != fw_compatible) or (ntc.hwVersion != hw_compatible):
                print_red("*This version of shell was designed for a different hardware revision or firmware version*")

            print("β: ", end='')
            print("{:.2f}".format(ntc.beta)) 

            print("hardware:firmware version: ", end='')
            print(ntc.hwVersion, end='')
            print(":", end='')
            print(ntc.fwVersion)
        else:
             print_red('**disconnected**')


    def do_reset(self, a):
        """reset all saved values\nparameters: none"""
        ntc.reset()
        self.do_config(self)

    def do_temp(self, temp_C):
        """measures the temperature\nparameters: none"""
        ntc.measureTemp()
        if ntc.status:
            print_red(ntc.status_string[ntc.status])

        print("{:.3f}".format(ntc.tempC) + " °C")
        print("{:.3f}".format(ntc.tempF) + " °F")
        print("{:.3f}".format(ntc.tempK) + " K")

    def do_beta(self, line):
        """Set beta value\nparameters: beta"""
        data = [s for s in line.split()]
        if len(data) >= 1:
            ntc.setBeta(float(data[0]))

        self.do_config(self)

    def do_i2c(self, line):
        """changes the I2C address"""
        i2c_address = int(line, 16)

        if ((i2c_address <= 0x07) or (i2c_address > 0x7f)):
            print("Error: I2C address not in valid range")
        else:
            ntc.setI2CAddress(i2c_address);

    def do_exit(self, s):
        """Exits\nparameters: none"""
        return True

def print_red(txt): print("\033[91m {}\033[00m" .format(txt)) 
def print_green(txt): print("\033[92m {}\033[00m" .format(txt)) 

ntc.begin()
Mod_Temp_Shell().cmdloop()
