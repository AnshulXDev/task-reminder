# GitHub - @AnshulXDev

# Modules
import time
import winsound

# Code
print("--Welcome to Task Remainder--")
task=input("\nEnter task to remind: ")
delay=int(input("Please enter a time to set the reminder (in second): "))
print("Reminder set successfully!")
def reminder(task, delay):
    time.sleep(delay)
    print("\nReminder!", task)
    winsound.Beep(1000, 500)
    time.sleep(0.5)
    winsound.Beep(1000, 500)
    time.sleep(0.5)
    winsound.Beep(1000, 1000)

reminder(task, delay)