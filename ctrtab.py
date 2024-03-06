
import pyautogui  # Import pyautogui only when needed
import time



def main():
    try:
        while True:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(30)  # Wait for 30 seconds before the next iteration
    except KeyboardInterrupt:
        print("Process interrupted.")

if __name__ == "__main__":
    main()
