import win32api
import win32con
import win32gui
import time

class Window:
    def __init__(self, width = 800, height = 600, title="Window", icon_path= None, FPS = 60, bg= (211,211,211), cursor = None):
        self.width = width
        self.height = height
        self.title = title
        self.text_objects = []
        self.text_input_objects = []
        self.circle_objects = []
        self.line_objects = []  # List to hold text objects
        self.FPS = FPS
        self.frame_duration = 1.0 / FPS
        self.bg = bg
        # Register the window class
        self.hInstance = win32api.GetModuleHandle(None)
        wndClass = win32gui.WNDCLASS()
        wndClass.lpfnWndProc = self.window_proc  # Set the window procedure
        wndClass.hInstance = self.hInstance
        wndClass.lpszClassName = self.title
        wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        
        if icon_path != None:
            wndClass.hIcon = win32gui.LoadImage(self.hInstance, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
        if cursor != None:
            wndClass.hCursor = win32gui.LoadImage(self.hInstance, cursor, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
        
        classAtom = win32gui.RegisterClass(wndClass)
        self.rect_objects = []
        # Create the window
        self.hWnd = win32gui.CreateWindow(
            classAtom,
            self.title,
            win32con.WS_OVERLAPPEDWINDOW,
            100, 100,  # Window position (x, y)
            self.width, self.height,  # Window size (width, height)
            0, 0,  # No parent window or menu
            self.hInstance,
            None
        )
        self.stopped = False

        # Show the window
        win32gui.ShowWindow(self.hWnd, win32con.SW_SHOWNORMAL)
        win32gui.UpdateWindow(self.hWnd)

    def add_text(self, text_object):
        self.text_objects.append(text_object)

    def add_line(self, line_object):
        self.line_objects.append(line_object)

    def add_rect(self, rect_object):
        self.rect_objects.append(rect_object)  # Add text object to the list

    def add_circle(self, circle_object):
        self.circle_objects.append(circle_object)  # Add text object to the list
  # Add text object to the list

    def window_proc(self, hWnd, msg, wParam, lParam):
        if msg == win32con.WM_CLOSE:
            win32gui.DestroyWindow(hWnd)
            win32gui.PostQuitMessage(0)  # Post a quit message to exit the program
            return 0  # Return 0 after handling the close message
        elif msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            self.stopped = True
            return 0
        elif msg == win32con.WM_PAINT:
            self.paint(hWnd)
            return 0
        else:
            return win32gui.DefWindowProc(hWnd, msg, wParam, lParam)

         
       
        
    def paint(self, hWnd):

        if not win32gui.IsWindow(hWnd):
            return
        #print(hWnd)
        # Begin painting and get the paint structure
        hdc, ps = win32gui.BeginPaint(hWnd)

        rect = win32gui.GetClientRect(hWnd)
        bg_color = self.Colour(self.bg[0], self.bg[1], self.bg[2])
        brush = win32gui.CreateSolidBrush(bg_color)

    # Fill the rectangle with the brush
        win32gui.FillRect(hdc, rect, brush)
        # Loop through text objects and draw them
        for text in self.text_objects:
            text.draw(hWnd)
        for circle in self.circle_objects:
            circle.draw(hWnd)
            if circle.draggable:
# Call the toggle_drag method to enable dragging
                circle.toggle_drag(hWnd)
        for rect in self.rect_objects:
            rect.draw(hWnd)
            if rect.dragable:
# Call the toggle_drag method to enable dragging
                rect.toggle_drag(hWnd)
        for line in self.line_objects:
            line.draw(hWnd)
            

        # End painting
        win32gui.EndPaint(hWnd, ps)

    def TransMessage(self):
    # Main message loop
        msg = win32gui.GetMessage(self.hWnd, 0, 0)
            
        if msg:
            # If there's a message, process it
            win32gui.TranslateMessage(msg[1])
            win32gui.DispatchMessage(msg[1])

    
    def Colour(self, red, green, blue):
        return win32api.RGB(red, green, blue)
    
    def main(self):
        start_time = time.time()
        self.TransMessage()
        #self.paint(self.hWnd)
        
        elapsed_time = time.time() - start_time
        time_to_sleep = self.frame_duration - elapsed_time
            
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)  # 

    def close(self):
    # Use the DestroyWindow function to destroy the window
        win32gui.DestroyWindow(self.hWnd)
        self.stopped = True
    # Post a quit message to ensure the program ends after the window is destroyed
        win32gui.PostQuitMessage(0)
