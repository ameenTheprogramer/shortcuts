import subprocess
import time
import sys


def run_command(command):
    subprocess.run(command, shell=True, check=True)

def run_with_confirmation(command):
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(b'y\n')

def xserver():
    # Get the value of $DISPLAY
    display = subprocess.run("echo $DISPLAY", shell=True, capture_output=True, text=True)
    display_value = display.stdout.strip()

    # Create .Xauthority file and set permissions
    run_command("touch ~/.Xauthority")
    run_command("chmod 600 ~/.Xauthority")

    # Export DISPLAY=:0
    run_command(f"export DISPLAY={display_value}")


def update_apt():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'xterm'])
    run_with_confirmation(['sudo', 'apt', 'install', '-y', 'python3-pip'])
    subprocess.run(['pip', 'install', 'pyautogui'])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'python3-tk', 'python3-dev'])
    

def download_and_run_script(params):
    link = f'https://raw.githubusercontent.com/ameenTheprogramer/clickininterval/main/{params}.py'
    subprocess.run(['wget', link])
    cmd = f'python {params}.py'
    subprocess.Popen(['xterm', '-e', cmd])

if __name__ == "__main__":
    update_apt()  # Update and install packages only once before entering the main loop
    xserver()
    params = sys.argv[1:]
    if params:
        download_and_run_script(params[0])
    else:
        print("Please provide the name of the script to run.")
    
