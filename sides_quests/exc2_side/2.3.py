class Pixel:
    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        """
        Initializes a Pixel object with a red, green, and blue value of 0.
        Initializes the x and y coordinates to 0.
        """
        # set the x and y coordinates to 0
        self._x = x
        self._y = y
        # set the red, green, and blue values to 0
        self._red = red
        self._green = green
        self._blue = blue
    
    def set_coords(self, x, y):
        """
        Sets the x and y coordinates of the pixel to the given values.
        """
        self._x = x
        self._y = y
    
    def set_grayscale(self):
        """
        Sets the red, green, and blue values of the pixel to the average of the three.
        Then we get a grayscale pixel.
        """
        average = (self._red + self._green + self._blue) // 3
        self._red = average
        self._green = average
        self._blue = average
    
    def print_pixel_info(self):
        """
        Prints the x and y coordinates and the red, green, and blue values of the pixel.
        """
        print("x:", self._x,"Y:", self._y, "Color:", (self._red, self._green, self._blue))
    
def main():
    """
    Create a Pixel object and test the set_grayscale method.
    Print the pixel information before and after setting the pixel to grayscale.
    """
    pixel = Pixel(5, 6, 250, 0, 0)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()

if __name__ == '__main__':
    main()