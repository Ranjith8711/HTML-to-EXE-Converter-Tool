# ================================================================
#  HTML TO EXE CONVERTER — Auto-generated Launcher
#  Developed by BEST_TEAM  ·  v2.0
#  DO NOT EDIT — this file is generated automatically
# ================================================================
import sys
import os
import webview

def resource_path(relative_path):
    """
    Return the absolute path to a bundled resource.
    Works both when running as a plain .py and as a frozen .exe.
    """
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS          # PyInstaller extraction folder
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)

# Resolve the HTML file and build a file:/// URL
html_file = resource_path("min.html")
app_url   = "file:///" + html_file.replace("\\", "/")

# Launch the desktop window
webview.create_window(
    title      = "min",
    url        = app_url,
    width      = 1280,
    height     = 720,
    resizable  = True,
    fullscreen = False,
    min_size   = (400, 300),
)
webview.start(debug=False)
