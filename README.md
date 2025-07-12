# Buttplug_AHK
A method by which to control a vibration device connected to Intiface Central using AHK
 This project uses a Python-based web server to act as a bridge between AutoHotkey and Intiface Central.

## Features

*   **Hotkey Control:** Use your keyboard's numpad to instantly set vibration levels (1-9 for 10-90%, 0 for off, Enter for 100%).
*   **Simple Startup:** Just run one script (`vibe_hotkey2.ahk`) to automatically start both the server and the hotkey listener.
*   **Automatic Shutdown:** Closing the AHK script also automatically terminates the background server process.

## Requirements

To run this project, you will need the following installed:

1.  **[Intiface Central](https://intiface.com/central/)**: The application that manages the connection to your physical device.
2.  **[Python (Version 3.10.0 Recommended)](https://www.python.org/downloads/release/python-3100/)**: The script was developed and tested with this version.
3.  **[AutoHotkey (v1.1 recommended)](https://www.autohotkey.com/)**: The scripting engine for the hotkeys.

## Setup Instructions

### 1. Install Python Libraries

Once Python is installed, open a Command Prompt (`cmd.exe`) and run the following command to install the necessary libraries:

```sh
pip install "uvicorn[standard]" buttplug-py fastapi

### 2. Download Project Files

Download the vibe_server1.py and vibe_hotkey2.ahk files from this repository and place them in the same folder on your computer.

### 3. Run the Project

Start Intiface Central and ensure your device is connected and scanning.
Navigate to the folder where you saved the project files.
Double-click vibe_hotkey2.ahk.
A message box will appear confirming the script and server are running. You can now use the numpad keys to control your device.
How to Use
Numpad 0-9: Sets vibration from 0% to 90%.
Numpad Enter: Sets vibration to 100%.
Esc: Exits the script and stops the server.
License
This project is licensed under the MIT License. See the LICENSE file for details.
