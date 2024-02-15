import subprocess
import pygetwindow as gw
import os


def get_cwd():
    return os.path.dirname(os.path.realpath(__file__))


# 打开Edge浏览器的隐私窗口
subprocess.run(
    [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "-inprivate",
        f"{get_cwd()}/index.html",
    ]
)

while True:
    try:
        edge = gw.getWindowsWithTitle("start-min-edge - [InPrivate] - Microsoft​ Edge")[
            0
        ]
        edge.minimize()
        break
    except IndexError:
        pass
