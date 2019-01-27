#ipconfig Tool

restart = 0
import os

while restart == 0:
    command = 'ipconfig -all'
    os.system(command)
    input()
    os.system('CLS')
