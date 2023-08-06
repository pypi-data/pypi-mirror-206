import webview
import os
import sys

from .webview import create_window, start

from .handle_build import handle_build_copy
from .generated import Api

_window = None

build_dir = "./Pequena/build"

base_directory = None
if os.name == 'posix':  # for *nix systems
    base_directory = os.path.join(os.path.expanduser('~'), '.pywebview')
elif os.name == 'nt':  # for Windows
    base_directory = os.path.join(os.environ['APPDATA'], 'pywebview')

exposed_fcs = []


def expose_functions(*fc):
    for f in fc:
        exposed_fcs.append(f)


def init_window(src="client/index.html", window_name="Hello World!", width=800, height=600,
                x=None, y=None, resizable=True, fullscreen=False, min_size=(200, 100),
                hidden=False, frameless=False, easy_drag=True,
                minimized=False, on_top=False, confirm_close=False, background_color='#FFFFFF',
                transparent=False, text_select=False, zoomable=False, draggable=False):
    global _window
    client_dir = os.path.dirname(src)
    build_html = build_dir + "/" + os.path.basename(src)
    if not getattr(sys, 'frozen', False):
        handle_build_copy(client_dir, build_dir, build_html)
    print("Build_html: ", build_html)

    _window = create_window(title=window_name, url=build_html, js_api=Api(_window), width=width, height=height,
                            x=x, y=y, resizable=resizable, fullscreen=fullscreen, min_size=min_size,
                            hidden=hidden, frameless=frameless, easy_drag=easy_drag,
                            minimized=minimized, on_top=on_top, confirm_close=confirm_close, background_color=background_color,
                            transparent=transparent, text_select=text_select, zoomable=zoomable, draggable=draggable)
    return _window


def start_window(port=None, debug=True):

    for fc in exposed_fcs:
        _window.expose(fc)
    start(gui='edgechromium', debug=debug,
          http_port=port, storage_path=base_directory)
