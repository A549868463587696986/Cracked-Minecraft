import psutil
import os
import subprocess
import time




tag = r"""
------------------------------------
              _                  _   
     /\      | |                | |  
    /  \   __| |_   ____ _ _ __ | |_ 
   / /\ \ / _` \ \ / / _` | '_ \| __|
  / ____ \ (_| |\ V / (_| | | | | |_ 
 /_/    \_\__,_| \_/ \__,_|_| |_|\__|
                                     
-------------------------------------    
"""


info = r"""

------------------------------------
  _____        __      
 |_   _|      / _|     
   | |  _ __ | |_ ___  
   | | | '_ \|  _/ _ \ 
  _| |_| | | | || (_) |
 |_____|_| |_|_| \___/    

 Designed by xSv4
-------------------------------------   

This program is made to capture a start key from the Minecraft process 
when it runs and modify it for the username to be a cracked username.
These accounts that are created will not be granted access to join 
premium servers. 


The only servers that these accounts will work on is 
cracked servers like blocksmc.com


Press Enter to continue: 
"""



def find_javaw_process():
    return next((p.info['pid'] for p in psutil.process_iter(['pid', 'name']) if p.info['name'] == 'javaw.exe'), None)

def get_command_line_by_pid(process_id):
    try:
        return psutil.Process(process_id).cmdline()
    except psutil.NoSuchProcess:
        return None

def terminate_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            try:
                process = psutil.Process(pid)
                process.terminate()
                # print(f"PID {pid} terminated")
            except psutil.NoSuchProcess:
                print(f"Process {process_name} (PID {pid}) not found.")
            except psutil.AccessDenied:
                print(f"Access denied to terminate process {process_name} (PID {pid}).")

def clr():
    for i in range(15):
        print("\n\n\n\n")

def launch():
    file_path = 'info.log'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                command = line.strip()
                print("[LOGS] Launching Minecraft")
                try:
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error launching Minecraft: {e}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

previous_statement = ""
while True:
    clr()
    print(tag)
    option = int(input("1 = Run Minecraft\n2 = Delete data\n3 = Info\n:"))

    if option == 1:
        file_path = "info.log"

        # Check if info.log exists
        if os.path.exists(file_path):
            with open(file_path, "r") as info_file:
                lines = info_file.readlines()

            # Print the original content
            # print("Original content of info.log:")
            # print("".join(lines))

            # Ask for a new username
            clr()
            print(tag)
            new_username = input("Username: ")

            # Search for --username and replace the value after it with the new one
            for i, line in enumerate(lines):
                if "--username" in line:
                    parts = line.split()
                    username_index = parts.index("--username")
                    if username_index + 1 < len(parts):
                        parts[username_index + 1] = new_username
                        lines[i] = " ".join(parts)

            # Write the modified contents back to info.log
            with open(file_path, "w") as info_file:
                print("[LOGS] Launching Minecraft")
                info_file.writelines(lines)
                # Print the modified command before launching
                modified_command = " ".join(parts)
                # print(f"Modified command: {modified_command}")
                subprocess.run(modified_command, shell=True, check=True)

        else:
            # If info.log doesn't exist, perform the original logic
            while True:
                javaw_process_id = find_javaw_process()

                if javaw_process_id and (command_line := get_command_line_by_pid(javaw_process_id)):
                    clr()
                    print(tag)
                    print("[LOGS] Obtained start key")
                    terminate_process_by_name('javaw.exe')
                    terminate_process_by_name('MinecraftLauncher.exe')
                    # Add quotes around the first four parts of the command line
                    modified_command_line = ['"' + part + '"' if i < 2 else part for i, part in enumerate(command_line)]

                    # Print the complete modified command line
                    # print("Modified command line:", " ".join(modified_command_line))

                    # Ask for a new username
                    new_username = input("Username: ")

                    # Update the username in the modified command line
                    for i, part in enumerate(modified_command_line):
                        if part == "--username" and i + 1 < len(modified_command_line):
                            modified_command_line[i + 1] = new_username

                    # Print the updated command line
                    # print("Updated command line:", " ".join(modified_command_line))

                    # Write the modified command line to info.log
                    with open(file_path, "w") as info_file:
                        info_file.write(" ".join(modified_command_line))
                        command = " ".join(modified_command_line)
                        # print(f"\n\n\n\n\n\n{command}")
                        # print("info.log created with the modified command line.")
                    # Print the modified command before launching
                    modified_command = " ".join(modified_command_line)
                    # print(f"Modified command: {modified_command}")
                    launch()

                    break
                statement = "Unable to retrieve command line for javaw.exe process." if javaw_process_id else "Minecraft not open or detected. Make sure to have Minecraft open and running"
                if previous_statement != statement:
                    clr()
                    print(tag)
                    print(statement)
                    previous_statement = statement

    elif option == 2:
        file_path = "info.log"
        clr()
        print(tag)
        print("[LOGS] Deleted data successfully")
        seconds = 5
        for i in range(seconds, 0, -1):
            print(f"Returning in {i}", end='\r')
            time.sleep(1)


        # restarts the program
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")

        # Continue to the next iteration of the loop
        continue


    elif option == 3:
        clr()
        input(info)

