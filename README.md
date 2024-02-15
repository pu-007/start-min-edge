# Start Microsoft Edge Minimized

*a solution for saladict*

Run this script at startup by add the flowwing code to`C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autostart.vbs`

```vbs
Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run"python /path/to/start-min-edge", 0, False
```
