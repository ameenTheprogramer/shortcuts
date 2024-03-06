import subprocess
import time

def update_apt():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    subprocess.run(['sudo', 'apt-get', 'install', 'python3-pip'])
    subprocess.run(['pip', 'install', 'pyautogui'])
    

def main():
    import pyautogui  # Import pyautogui only when needed
    try:
        while True:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(30)  # Wait for 30 seconds before the next iteration
    except KeyboardInterrupt:
        print("Process interrupted.")

if __name__ == "__main__":
    update_apt()  # Update and install packages only once before entering the main loop
    main()
