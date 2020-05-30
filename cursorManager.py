#Python set cursor position in windows terminal

###################################################################
#https://rosettacode.org/wiki/Terminal_control/Cursor_positioning
from ctypes import *
 
STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def setCursorPosition(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
#####################################################################
    
import cursor
hideCursor = lambda: cursor.hide()
showCursor = lambda: cursor.show()
