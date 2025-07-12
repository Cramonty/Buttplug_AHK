#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
#SingleInstance, Force

; --- Start the Python/Uvicorn Server and get its Process ID (PID) ---
Run, cmd.exe /c uvicorn vibe_server1:app --host 127.0.0.1 --port 8765, %A_ScriptDir%, Hide, UvicornPID

; --- Add a label to run when the script exits ---
OnExit, ShutdownServer

MsgBox,
(
AHK Control Script is running.
The server has been started in the background.
Use Numpad keys 1-9 for intensity, 0 for off, and Enter for 100.
)

; --- Hotkeys ---
Numpad0::SendVibration(0.0)
Numpad1::SendVibration(0.1)
Numpad2::SendVibration(0.2)
Numpad3::SendVibration(0.3)
Numpad4::SendVibration(0.4)
Numpad5::SendVibration(0.5)
Numpad6::SendVibration(0.6)
Numpad7::SendVibration(0.7)
Numpad8::SendVibration(0.8)
Numpad9::SendVibration(0.9)
NumpadEnter::SendVibration(1.0)

; --- Function to Send Command ---
SendVibration(intensity) {
    static API_URL := "http://127.0.0.1:8765/vibrate"

    http := ComObjCreate("WinHttp.WinHttpRequest.5.1")
    http.Open("POST", API_URL, true)
    http.SetRequestHeader("Content-Type", "application/json")

    body := "{""intensity"":" . intensity . "}"
    body := StrReplace(body, ",", ".")

    http.Send(body)

    http.WaitForResponse()
    if (http.Status == 200) {
        ToolTip, % "Vibration: " . (intensity * 100)
    } else {
        ToolTip, % "Error: " . http.Status . " " . http.StatusText
    }
    SetTimer, RemoveToolTip, -1500
}

RemoveToolTip:
    ToolTip
return

; --- This section runs automatically when the script is closed ---
ShutdownServer:
    ; Use taskkill to forcefully terminate the process by its PID.
    ; /t also terminates any child processes (the python server).
    ; /f forces the termination.
    Run, taskkill /PID %UvicornPID% /t /f, , Hide
ExitApp

Esc::ExitApp