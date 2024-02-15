# Start Microsoft Edge Minimized

_a solution for the problem of sala dict `window creation is resricted...`_

Run this script at startup by add the following code to `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autostart.vbs`

```vbs
Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run"python /path/to/start-min-edge", 0, False
```

support for `glazewm`, it will store the window to workspace 9.
