import win32con
import win32gui
import win32ui

class Text:
    def __init__(self, window, content, x, y, font_size=50, color=0x000000, font = "Arial", bold = False, strikeOut=0, italic=0, underline=0, superBold = False, ultraBold = False):
        self.content = content
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.window = window
        self.font = font
        self.bold = bold
        self.strikeOut = strikeOut
        self.underline = underline
        self.italic = italic
        self.superBold = superBold
        self.ultraBold = ultraBold
        # Automatically add this text object to the window's text list
        window.add_text(self)

    def draw(self, hWnd):
        if self.bold:
            hFont = win32ui.CreateFont({
                'name': self.font,               # Font name (e.g., "Arial")
                'height': self.font_size,         # Height of the font
                'weight': win32con.FW_BOLD,     # Font weight
                'italic': self.italic,                      # Italic (0 = no, 1 = yes)
                'underline': self.underline,                   # Underline (0 = no, 1 = yes)
                'strike out': self.strikeOut,                   # StrikeOut (0 = no, 1 = yes)
                'pitch and family': win32con.DEFAULT_PITCH | win32con.FF_DONTCARE
            })
        elif self.ultraBold:
            hFont = win32ui.CreateFont({
                'name': self.font,               # Font name (e.g., "Arial")
                'height': self.font_size,         # Height of the font
                'weight': win32con.FW_ULTRABOLD,     # Font weight
                'italic': self.italic,                      # Italic (0 = no, 1 = yes)
                'underline': self.underline,                   # Underline (0 = no, 1 = yes)
                'strike out': self.strikeOut,                   # StrikeOut (0 = no, 1 = yes)
                'pitch and family': win32con.DEFAULT_PITCH | win32con.FF_DONTCARE
            })
        elif self.superBold:
            hFont = win32ui.CreateFont({
                    'name': self.font,               # Font name (e.g., "Arial")
                    'height': self.font_size,         # Height of the font
                    'weight': win32con.FW_EXTRABOLD,     # Font weight
                    'italic': self.italic,                      # Italic (0 = no, 1 = yes)
                    'underline': self.underline,                   # Underline (0 = no, 1 = yes)
                    'strike out': self.strikeOut,                   # StrikeOut (0 = no, 1 = yes)
                    'pitch and family': win32con.DEFAULT_PITCH | win32con.FF_DONTCARE
                })
        else:
            hFont = win32ui.CreateFont({
                'name': self.font,               # Font name (e.g., "Arial")
                'height': self.font_size,         # Height of the font
                'weight': win32con.FW_NORMAL,     # Font weight
                'italic': self.italic,                      # Italic (0 = no, 1 = yes)
                'underline': self.underline,                   # Underline (0 = no, 1 = yes)
                'strike out': self.strikeOut,                   # StrikeOut (0 = no, 1 = yes)
                'pitch and family': win32con.DEFAULT_PITCH | win32con.FF_DONTCARE
            })
            # Get device context
        hdc = win32gui.GetDC(hWnd)
        hOldFont = win32gui.SelectObject(hdc, hFont.GetSafeHandle())

        # Select the font
        #win32gui.SelectObject(hdc, hFont)

        # Set text color
        win32gui.SetTextColor(hdc, self.color)
        
        # Set the background mode for transparency
        win32gui.SetBkMode(hdc, win32con.TRANSPARENT)

        # Draw the text
        rect = (self.x, self.y, self.x + 200, self.y + 50)  # Rectangle for text area
        win32gui.DrawText(hdc, self.content, -1, rect, win32con.DT_SINGLELINE | win32con.DT_NOCLIP | win32con.OBJ_FONT)

        # Clean up
        #win32gui.DeleteObject(hFont)
        win32gui.ReleaseDC(hWnd, hdc) 

    def updateText(self, new_text):
        self.content = f'{new_text}'
        # Invalidate the region where the text is displayed to trigger a repaint
        win32gui.InvalidateRect(self.window.hWnd, (self.x, self.y, self.x + 200, self.y + 50), True)
