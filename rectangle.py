''' Q.Description: You are tasked with creating a Rectangle class with the following requirements:
An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle classqa
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

'''

class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle class with a given length and width (parameters)
        Both must be integer type.
        """
        self.length = length
        self.width = width

    def __iter__(self):
        """
        Allow iteration over the Rectangle.
        When looping over Rectangle, it will give us firstly length (as a dictionary),
        then its width.
        """
        # First yield the length in dictionary form
        yield {"length": self.length}
        
        # Then yield the width in dictionary form
        yield {"width": self.width}


# Example usage:
# Create a rectangle with length 10 and width 5
rect = Rectangle(10, 5)

# Iterate over the rectangle to see its attributes
for attribute in rect:
    print(attribute)