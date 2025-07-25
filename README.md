# Buttplug_AHK

Use these scripts to control **[Buttplug.io](https://Buttplug.io)** compatible vibration devices using AutoHotkey. This project uses a Python-based web server to act as a bridge between AutoHotkey and Intiface Central, allowing for global hotkey control over your device's vibration level.

## Important Note:

**This has only been tested on one device (the one I own) and *only for the function of vibration*. IF you have a device with other functions, I won't be able to help you with that. However, I encourage anyone to use this code as an example to improve and expand upon.** 

***Code was written with AI assistance.***

## Features

*   **Global Hotkeys:** Use your keyboard's numpad to instantly set vibration levels, even when you are in another application.
*   **Simple Startup:** Just run one script (`vibe_hotkey.ahk`) to automatically start both the server and the hotkey listener.
*   **Automatic Shutdown:** Closing the AHK script also automatically terminates the background server process, leaving no cleanup needed.

## Requirements

To run this project, you will need the following installed:

1.  **[Intiface Central](https://intiface.com/central/)**: The application that manages the connection to your physical device.
2.  **[Python (Version 3.10.0 Recommended)](https://www.python.org/downloads/release/python-3100/)**: The project was developed and tested using this version.
3.  **[AutoHotkey (v1.1 or newer recommended)](https://www.autohotkey.com/)**: The scripting engine for the hotkeys.

## Setup Instructions

### 1. Install Python Libraries

Once Python is installed, open a Command Prompt (`cmd.exe`) and run the following command to install the required libraries:

```sh
pip install "uvicorn[standard]" buttplug-py fastapi
```

### 2. Download Project Files

Download the `vibe_server1.py` and `vibe_hotkey.ahk` files from this repository and place them **in a folder together** on your computer.

### 3. Run the Project

1.  Start **Intiface Central** and ensure your device is connected and functioning.
2.  Navigate to the folder where you saved the two project files.
3.  Double-click **`vibe_hotkey.ahk`** to run the AHK script.

A message box will appear confirming the script and server are running. You can now use the numpad keys to control your device.

## How to Use

*   **Numpad 0-9**: Sets vibration from 0% to 90%.
*   **Numpad Enter**: Sets vibration to 100%.
*   **Esc**: Exits the script and stops the server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
