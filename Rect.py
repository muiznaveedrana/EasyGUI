import win32gui
import win32api
import win32con
import Text
class Rect:
    def __init__(self, window, x, y, width, height, color=0x000000, draggable = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_dragging = False
        self.dragable = draggable
        self.window = window
        #self.add_text = add_text
        # Automatically add this rectangle object to the window's rectangle list
        window.add_rect(self)

    def draw(self, hWnd):
        # Get the device context for the window
        hdc = win32gui.GetDC(hWnd)
        # Create a brush with the specified color
        hBrush = win32gui.CreateSolidBrush(self.color)

        # Select the brush into the device context
        win32gui.SelectObject(hdc, hBrush)
        #print(hdc)
        # Draw the rectangle
        win32gui.Rectangle(hdc, self.x, self.y, self.x + self.width, self.y + self.height)
        
        # Clean up
        #win32gui.DeleteObject(hBrush)
        

        win32gui.ReleaseDC(hWnd, hdc)

    def is_clicked(self, hWnd):
        """Check if the left mouse button was clicked inside this rectangle."""
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
            # Get current mouse position
            mouse_x, mouse_y = win32gui.ScreenToClient(hWnd, win32api.GetCursorPos())

            
            # Check if the mouse is within the rectangle bounds
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                #print('TAKEN')

                return True
        
        return False
    
    def toggle_drag(self,hWnd):
        mouse_x, mouse_y = win32api.GetCursorPos()  # Get the mouse position
        mouse_down = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)  # Check if left mouse button is down
        mouse_x, mouse_y = win32gui.ScreenToClient(hWnd, (mouse_x, mouse_y))

        if mouse_down:
            # If mouse is clicked within the rect and dragging is not active
            if not self.is_dragging:
                if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                    self.is_dragging = True
                    # Calculate offset for smooth dragging
                    self.offset_x = mouse_x - self.x
                    self.offset_y = mouse_y - self.y
        else:
            # Stop dragging if mouse is not down
            self.is_dragging = False

        # If dragging is active, update the rectangle's position
        if self.is_dragging:
    # Get the current rectangle area before moving
            old_rect = (self.x, self.y, self.x + self.width, self.y + self.height)

            # Update the position based on mouse coordinates
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y

            # Get the new rectangle area after moving
            new_rect = (self.x, self.y, self.x + self.width, self.y + self.height)

            # Combine both areas to be invalidated and repainted
            combined_rect = (
                min(old_rect[0], new_rect[0]),
                min(old_rect[1], new_rect[1]),
                max(old_rect[2], new_rect[2]),
                max(old_rect[3], new_rect[3])
            )

            # Invalidate only the combined area instead of the entire window
            self.InvalidateRect(hWnd, combined_rect, True)
    
    def InvalidateRect(self, hWnd, rect, Erase):
        win32gui.InvalidateRect(hWnd, rect, Erase)
    
    def colliderect(self, rect, otherRects = []):
        if isinstance(rect, Rect):  # Ensure that the provided object is a Rect
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
        self.InvalidateRect(self.window.hWnd, (old_x, old_y, old_x + self.width, old_y + self.height), True)  # Invalidate old position
        self.InvalidateRect(self.window.hWnd, (self.x, self.y, self.x + self.width, self.y + self.height), True)  # Invalidate new position
    
    def moveRectTo(self, x = 0 , y = 0):
        old_x, old_y = self.x, self.y  # Store old position for invalidation
                        
        self.x = x  # Set new x position
        self.y = y  # Keep the y position unchanged (or modify as needed)
                        
                        # Invalidate both the old and new areas
        self.InvalidateRect(self.window.hWnd, (old_x, old_y, old_x + self.width, old_y + self.height), True)  # Invalidate old position
        self.InvalidateRect(self.window.hWnd, (self.x, self.y, self.x + self.width, self.y + self.height), True)  # Invalidate new position


