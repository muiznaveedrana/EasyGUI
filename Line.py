import win32api
import win32con
import win32gui

class Line:
    def __init__(self, window, x1, y1, x2, y2, color=win32api.RGB(0, 0, 0)):
        self.window = window  # Reference to the window
        self.x1 = x1  # Starting x-coordinate
        self.y1 = y1  # Starting y-coordinate
        self.x2 = x2  # Ending x-coordinate
        self.y2 = y2  # Ending y-coordinate
        self.color = color  # Line color

        window.add_line(self)
    def draw(self, hWnd):
        # Get the device context for the window
        hdc = win32gui.GetDC(hWnd)
        
        # Set the line color
        pen = win32gui.CreatePen(win32con.PS_SOLID, 2, self.color)  # Thickness = 2
        old_pen = win32gui.SelectObject(hdc, pen)

        # Draw the line
        win32gui.MoveToEx(hdc, self.x1, self.y1)
        win32gui.LineTo(hdc, self.x2, self.y2)

        # Clean up
        win32gui.SelectObject(hdc, old_pen)
        win32gui.DeleteObject(pen)
        win32gui.ReleaseDC(hWnd, hdc)
