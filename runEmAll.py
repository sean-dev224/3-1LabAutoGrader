import sys
import subprocess
import time

volume_path = sys.argv[1]
tax_path = sys.argv[2]
weather_path = sys.argv[3]


print("----- RUNNING VOL -----")
vol = subprocess.Popen(["python3", "volumeRun.py", volume_path])

time.sleep(5)
print()
print()


print("----- RUNNING tax -----")
tax = subprocess.Popen(["python3", "taxRun.py", tax_path])
time.sleep(5)
print()
print()

print("----- RUNNING weather -----")
weather = subprocess.Popen(["python3", "weatherRun.py", weather_path])
time.sleep(5)
print()
print()