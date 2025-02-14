import subprocess
import time
import sys

inputList = [["10.5", "3"], ["22", "1.5"]]

filepath = sys.argv[1]
file_name = filepath.split("/")[-1]
exec_name = file_name.split(".")[0]
cwd = "/".join(filepath.split("/")[0:-1])

args = ["gcc", file_name, "-o", exec_name]

compile = subprocess.Popen(args, cwd=cwd)

#give time to compile
time.sleep(1)

for inputs in inputList:
    print(f"run with: {inputs}")


    process = subprocess.Popen([f"./{exec_name}"], cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send input to the program
    for input_str in inputs:
        #encodes string to utf-8 and adds a newline character to the end
        #b means it converts the string to a byte
        process.stdin.write(input_str.encode() + b"\n")


    # Capture output
    stdout, stderr = process.communicate()

    print("Output:")
    print(stdout.decode())

    if stderr:
        print("Error:")
        print(stderr.decode())

    print("-----------------")

print("Answers should be: 1039.08, 2280.79")