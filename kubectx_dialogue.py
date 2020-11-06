#!/usr/bin/env python3
import subprocess
import sys


def get_context_number():
    try:
        context_number = int(input("Please enter the number of corresponding context to switch to: "))
        return context_number
    except ValueError:
        return get_context_number()


def run_command(command):
    process = subprocess.Popen(command,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           bufsize=1,
                           universal_newlines=True,
                           text=True)
    stdout, stderr = process.communicate()
    retrun_code = process.returncode

    if stderr != None:
        print(f"There was an error gathering context(s): {stderr}")
        sys.exit(1)

    return stdout.rstrip(), retrun_code


current_context, return_code = run_command(['kubectx', '--current'])
if return_code != 0:
    print(f"Current context is not set")
else:
    print(f"Current context is {current_context}")


contextes_out, return_code = run_command(['kubectx'])
contextes = contextes_out.split("\n")
contextes_count = len(contextes)

context_dict = {}
for list_counter, context in enumerate(contextes):
    context_counter = list_counter + 1
    context_dict[context_counter] = context
    print(f"{context_counter}: {context}")


context_number = get_context_number()
while not(0 < context_number <= contextes_count):
    context_number = get_context_number()

result, return_code = run_command(['kubectx', f'{context_dict[context_number]}'])
print(result)
