import subprocess
import pygetwindow as gw
import os
from time import sleep


def get_cwd():
    return os.path.dirname(os.path.realpath(__file__))


subprocess.Popen(
    [r"D:\Source\GlazeWM\GlazeWM.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE
)

sleep(1)


command_1 = subprocess.run(
    [r"D:\Source\GlazeWM\GlazeWM.exe", "command", '"focus workspace 9"']
)

# 打开Edge浏览器的隐私窗口
subprocess.run(
    [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "-inprivate",
        f"{get_cwd()}/index.html",
    ]
)

command_2 = subprocess.run(
    [r"D:\Source\GlazeWM\GlazeWM.exe", "command", '"focus workspace 1"']
)

while True:
    edge = gw.getWindowsWithTitle(
        "C0BF384C333E479C9C01884375881FBC - [InPrivate] - Microsoft​ Edge"
    )
    if edge != []:
        edge[0].minimize()
        break
