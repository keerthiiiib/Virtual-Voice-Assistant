import pyautogui
import datetime

def take_screenshot():
    # Define the directory to save the screenshot
    save_path = r"C:\Users\91903\Pictures\Screenshots"
    
    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{save_path}\\screenshot_{timestamp}.png"
    
    # Take and save the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved at {filename}")



