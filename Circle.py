import win32gui
import win32api
import win32con
class Circle:
    def __init__(self, window, x, y, radius, color=0xFFFFFF, draggable=False):
        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.draggable = draggable
        self.is_dragging = False
        self.offset_x = 0
        self.offset_y = 0
        window.add_circle(self)
    def draw(self, hWnd):
        hdc = win32gui.GetDC(hWnd)
        # Create a brush for the circle color
        brush = win32gui.CreateSolidBrush(self.color)

        # Fill the circle
        win32gui.SelectObject(hdc, brush)
        win32gui.Ellipse(hdc, self.x - self.radius, self.y - self.radius,
                          self.x + self.radius, self.y + self.radius)

        # Cleanup
        win32gui.DeleteObject(brush)
        win32gui.ReleaseDC(hWnd, hdc)

    def check_click(self, mouse_x, mouse_y):
        # Check if the mouse click is inside the circle
        if (mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2 <= self.radius ** 2:
            return True
        return False

    def toggle_drag(self, hWnd):
        mouse_x, mouse_y = win32api.GetCursorPos()  # Get the global mouse position
        mouse_down = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)  # Check if left mouse button is down
        mouse_x, mouse_y = win32gui.ScreenToClient(hWnd, (mouse_x, mouse_y))  # Convert to client coordinates

        # Check if the mouse is within the circle when clicked
        if mouse_down:
            # Check if dragging is not active and mouse is within circle bounds
            if not self.is_dragging and (mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2 <= self.radius ** 2:
                self.is_dragging = True
                # Calculate offset for smooth dragging
                self.offset_x = mouse_x - self.x
                self.offset_y = mouse_y - self.y

        else:
            # Stop dragging if the mouse is not down
            self.is_dragging = False

        # If dragging is active, update the circle's position
        if self.is_dragging:
            # Invalidate the old position
            self.InvalidateRect(self.x, self.y, self.radius, True)

            # Update position based on mouse movement
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y

            # Invalidate the new position
            self.InvalidateRect(self.x, self.y, self.radius, True)

    def InvalidateRect(self, x, y,radius, Erase):
        radius = radius * 2
        rect = (
            x - radius,
            y - radius,
            x + radius,
            y + radius
        )
        win32gui.InvalidateRect(self.window.hWnd, rect, Erase)
    
    def colliderect(self, rect, otherRects):
        if isinstance(rect, Circle):  # Ensure that the provided object is a Rect
            for otherRect in otherRects:
                if otherRect != rect:  # Skip checking itself
                    # Check for collision between `rect` and `otherRect`
                    if (
                        rect.x < otherRect.x + otherRect.width and
                        rect.x + rect.width > otherRect.x and
                        rect.y < otherRect.y + otherRect.height and
                        rect.y + rect.height > otherRect.y
                    ):
                        return True  # Collision detected
        return False  # No collision
    
    def moveRectBy(self, x = 0, y = 0):
        old_x, old_y = self.x, self.y  # Store old position for invalidation
                        
        self.x += x  # Set new x position
        self.y += y  # Keep the y position unchanged (or modify as needed)
                        
                        # Invalidate both the old and new areas
        self.InvalidateRect(self.x, self.y, self.radius, True)