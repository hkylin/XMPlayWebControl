# -*- coding: UTF-8 -*-
import cgi
import win32gui

class Titles():
    
    def __init__(self):
        self.windows = []

    def _win_enum_handler(self,hwnd,ctx):
        if win32gui.IsWindowVisible(hwnd):
            self.windows.append(win32gui.GetWindowText(hwnd))
            
    def _load_titles(self):
        win32gui.EnumWindows(self._win_enum_handler,None)

    def get_current_song_title(self):       
        self._load_titles()
        title = "0XMPlay window not found"
        for item in self.windows:
            if (item.startswith("XMPlay")):
                title = "1" + (item[9:])

        if not title[1:]:
        	title = "0XMPlay it's not playing anything. Press play!"
        return title

print("Content-Type: text/html;charset=windows-1252")
print()

print(Titles().get_current_song_title())