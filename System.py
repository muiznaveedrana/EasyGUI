import win32con
import win32api



class System:
    class ButtonClicked:
        def __init__(self, window):
            self.window = window
        
        def Clicked(self, button = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "shift", "tab", "enter", 
    "escape", "space","ctrl" ,"left", "right", "up", "down", "alt", "1", "2", "3", "4", "5", 
    "6", "7", "8", "9", "0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"
]):         
            if isinstance(button, str):
                match button.lower():
                    # Numbers 0-9
                    case '0':
                        return win32api.GetAsyncKeyState(ord('0')) != 0
                    case '1':
                        return win32api.GetAsyncKeyState(ord('1')) != 0
                    case '2':
                        return win32api.GetAsyncKeyState(ord('2')) != 0
                    case '3':
                        return win32api.GetAsyncKeyState(ord('3')) != 0
                    case '4':
                        return win32api.GetAsyncKeyState(ord('4')) != 0
                    case '5':
                        return win32api.GetAsyncKeyState(ord('5')) != 0
                    case '6':
                        return win32api.GetAsyncKeyState(ord('6')) != 0
                    case '7':
                        return win32api.GetAsyncKeyState(ord('7')) != 0
                    case '8':
                        return win32api.GetAsyncKeyState(ord('8')) != 0
                    case '9':
                        return win32api.GetAsyncKeyState(ord('9')) != 0

                    # Alphabet A-Z
                    case 'a':
                        return win32api.GetAsyncKeyState(ord('A')) != 0
                    case 'b':
                        return win32api.GetAsyncKeyState(ord('B')) != 0
                    case 'c':
                        return win32api.GetAsyncKeyState(ord('C')) != 0
                    case 'd':
                        return win32api.GetAsyncKeyState(ord('D')) != 0
                    case 'e':
                        return win32api.GetAsyncKeyState(ord('E')) != 0
                    case 'f':
                        return win32api.GetAsyncKeyState(ord('F')) != 0
                    case 'g':
                        return win32api.GetAsyncKeyState(ord('G')) != 0
                    case 'h':
                        return win32api.GetAsyncKeyState(ord('H')) != 0
                    case 'i':
                        return win32api.GetAsyncKeyState(ord('I')) != 0
                    case 'j':
                        return win32api.GetAsyncKeyState(ord('J')) != 0
                    case 'k':
                        return win32api.GetAsyncKeyState(ord('K')) != 0
                    case 'l':
                        return win32api.GetAsyncKeyState(ord('L')) != 0
                    case 'm':
                        return win32api.GetAsyncKeyState(ord('M')) != 0
                    case 'n':
                        return win32api.GetAsyncKeyState(ord('N')) != 0
                    case 'o':
                        return win32api.GetAsyncKeyState(ord('O')) != 0
                    case 'p':
                        return win32api.GetAsyncKeyState(ord('P')) != 0
                    case 'q':
                        return win32api.GetAsyncKeyState(ord('Q')) != 0
                    case 'r':
                        return win32api.GetAsyncKeyState(ord('R')) != 0
                    case 's':
                        return win32api.GetAsyncKeyState(ord('S')) != 0
                    case 't':
                        return win32api.GetAsyncKeyState(ord('T')) != 0
                    case 'u':
                        return win32api.GetAsyncKeyState(ord('U')) != 0
                    case 'v':
                        return win32api.GetAsyncKeyState(ord('V')) != 0
                    case 'w':
                        return win32api.GetAsyncKeyState(ord('W')) != 0
                    case 'x':
                        return win32api.GetAsyncKeyState(ord('X')) != 0
                    case 'y':
                        return win32api.GetAsyncKeyState(ord('Y')) != 0
                    case 'z':
                        return win32api.GetAsyncKeyState(ord('Z')) != 0

                    # Special Keys
                    case 'tab':
                        return win32api.GetAsyncKeyState(win32con.VK_TAB) != 0
                    case 'shift':
                        return win32api.GetAsyncKeyState(win32con.VK_SHIFT) != 0
                    case 'ctrl':
                        return win32api.GetAsyncKeyState(win32con.VK_CONTROL) != 0
                    case 'alt':
                        return win32api.GetAsyncKeyState(win32con.VK_MENU) != 0
                    case 'space':
                        return win32api.GetAsyncKeyState(win32con.VK_SPACE) != 0
                    case 'enter':
                        return win32api.GetAsyncKeyState(win32con.VK_RETURN) != 0
                    case 'escape':
                        return win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0

                    # Arrow Keys
                    case 'left_arrow':
                        return win32api.GetAsyncKeyState(win32con.VK_LEFT) != 0
                    case 'right_arrow':
                        return win32api.GetAsyncKeyState(win32con.VK_RIGHT) != 0
                    case 'up_arrow':
                        return win32api.GetAsyncKeyState(win32con.VK_UP) != 0
                    case 'down_arrow':
                        return win32api.GetAsyncKeyState(win32con.VK_DOWN) != 0

                    # Function Keys (F1-F12)
                    case 'f1':
                        return win32api.GetAsyncKeyState(win32con.VK_F1) != 0
                    case 'f2':
                        return win32api.GetAsyncKeyState(win32con.VK_F2) != 0
                    case 'f3':
                        return win32api.GetAsyncKeyState(win32con.VK_F3) != 0
                    case 'f4':
                        return win32api.GetAsyncKeyState(win32con.VK_F4) != 0
                    case 'f5':
                        return win32api.GetAsyncKeyState(win32con.VK_F5) != 0
                    case 'f6':
                        return win32api.GetAsyncKeyState(win32con.VK_F6) != 0
                    case 'f7':
                        return win32api.GetAsyncKeyState(win32con.VK_F7) != 0
                    case 'f8':
                        return win32api.GetAsyncKeyState(win32con.VK_F8) != 0
                    case 'f9':
                        return win32api.GetAsyncKeyState(win32con.VK_F9) != 0
                    case 'f10':
                        return win32api.GetAsyncKeyState(win32con.VK_F10) != 0
                    case 'f11':
                        return win32api.GetAsyncKeyState(win32con.VK_F11) != 0
                    case 'f12':
                        return win32api.GetAsyncKeyState(win32con.VK_F12) != 0

                    case _:
                        return False  # Return False if no matching case
