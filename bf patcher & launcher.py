#!/bin/sh
import os
import subprocess
import time

os.chdir(r"H:\\Documents\\1.0.6 Frosty")

subprocess.Popen(os.getcwd() + '\\ModLimitFixer.exe')
subprocess.Popen(os.getcwd() + '\\FrostyModManager.exe')

time.sleep(45)

subprocess.call(["taskkill","/F","/IM","ModLimitFixer.exe"])
subprocess.call(["taskkill","/F","/IM","FrostyModManager.exe"])