import math

class Rectangle:

  def __init__(self, width, height):
    self.s_width = width
    self.s_height= height

  def set_width(self, set_width):
    self.s_width = set_width

  def set_height(self, set_height):
    self.s_height= set_height

  def get_width(self):
    return self.s_width

  def get_height(self):
    return self.s_height
    
  def get_area(self):
    width = self.get_width()
    height = self.get_height()
    return width * height
  
  def get_perimeter(self):
    width = self.get_width()
    height = self.get_height()
    return 2 * width + 2 * height
  
  def get_diagonal(self):
    width = self.get_width()
    height = self.get_height()
    return (width ** 2 + height ** 2) ** 0.5
  
  def get_picture(self):
    width = self.get_width()
    height = self.get_height()
    if width > 50 or height > 50:
      return "Too big for picture."
    else:
      line = "*"*width
      shape = ""
      for i in range(height):
        shape += line + "\n"
      return shape
  
  def __str__(self):
    width = self.get_width()
    height = self.get_height()

    output = "Rectangle(width=" + str(width) + ", height=" + str(height) + ")"
    return output
  
  def get_amount_inside(self, shape):
    this_shape = self.get_area()
    passed_shape = shape.get_area()
    value = this_shape/passed_shape
    
    if this_shape % passed_shape == 0:
      return value
    elif passed_shape > 0.5*this_shape and passed_shape < this_shape:
      return 1;
    elif this_shape % passed_shape != 0 and value > 1:
      return math.floor(value)
    elif passed_shape > this_shape:
      return 0
    # return shape.get_area()

class Square(Rectangle):
  def __init__(self, side):
    self.s_width = side
    self.s_height = side
    
  def set_side(self, side):
    self.s_width = side
    self.s_height = side
  
  def get_side(self):
    return self.s_width

  def __str__(self):
    side = self.get_side()

    output = "Square(side=" + str(side) + ")"
    return output

