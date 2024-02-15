# Start Microsoft Edge Minimized

_a solution for the problem of sala dict `window creation is resricted...`_

Run this script at startup by add the following code to `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autostart.vbs`

```vbs
Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run"python /path/to/start-min-edge", 0, False
```

You can also use `glazewm` to hide the window.

```yaml
- command: "move to workspace 9"
  match_title: "/C0BF384C333E479C9C01884375881FBC.+/"
  match_class_name: "Chrome_WidgetWin_1"
```
