# shape thingy 
import math
from enum import Enum
def get_valid_input(prompt, type_func, error_msg="Invalid input."):
    while True:
        try:
            value = type_func(input(prompt))
            break
        except ValueError:
            print(error_msg)
        return value
def get_valid_measurment(prompt,error_msg="invalid measurement try meters or centimeters"):
    valid_measurements = ("m","metres","cm","centimetres","mm","milemetres")
    print(*valid_measurements)
    print("these are the valid measurements")
    while True:
        value = input(prompt).lower
        if value in valid_measurements:
            break
        else:
            print(error_msg)
    return value
def get_valid_shape(prompt,error_msg="invalid shape choose one from the list"):
    valid_shapes = [
        "circle",
        "semicircle",
        "quater circle",
        "square",
        "rectangle",
        "paralellagram",
        "trianlge",
        "diamond",
        "trapezium",
        "pentagon",
        "hexagon",
        "heptagon",
        "octagon",
        "nonagon"
    ]
    print(*valid_shapes)
    while True:
        value = input(prompt)
        if prompt in valid_shapes:
            break
        else:
            print(error_msg)
    return value

class shape_type(Enum):
    CIRCLE = "circle"
    SEMICIRCLE = "semicircle"
    QUATERCIRCLE = "quater circle" 
    SQUARE = "square"
    RECTANGLE = "rectangle"
    PARALELLAGRAM ="paralellagram"
    TRIANGLE = "trianlge"
    DIAMOND = "diamond"
    TRAPIZIUM = "trapezium"
    PENTAGON = "pentagon"
    HEXAGON = "hexagon"
    HEPTAGON = "heptagon"
    OCTAGON = "octagon"
    NONAGON = "nonagon"
    DECAGON = "decagon"
    class Find_shape():
        def shape(self):
            shape = input("")
            if shape == [shape_type.SQUARE,shape_type.RECTANGLE,shape_type.PARALELLAGRAM,shape_type.TRIANGLE]:
                width = get_valid_input("what is the width of the object",int)
                height = get_valid_input("what is the height of the object",int)
                unit = get_valid_measurment("type a valid measurement")
            elif shape == [shape_type.CIRCLE,shape_type.SEMICIRCLE]:
                width = get_valid_input("whats is the width",int)
                unit = get_valid_measurment("what is the measurement you will be using")
            elif shape == shape_type.DIAMOND:
                perimeter = get_valid_input("what is the permiter of your shape",int)
                angle = get_valid_input("what is 1 angle from the shape",int)
                unit = get_valid_measurment("type a valid measurement")
            elif shape == shape_type.TRAPIZIUM:
                height = get_valid_input("what is the height of the shape",int)
                lineA = get_valid_input("what is the length of line a (the samllest line at the top)",int)
                lineB = get_valid_input("what is the largest line at the botto(the base)",int)
                unit = get_valid_measurment("type a valid measurement")
            elif shape == [shape_type.DECAGON,shape_type.PENTAGON,shape_type.HEPTAGON,shape_type.HEXAGON,shape_type.OCTAGON]:
                perimeter = get_valid_input("what is the perimeter of the shape",int)
                unit = get_valid_measurment("tpye a valid measurement")
    class twodshapes():
        def area(self,shape = "circle",width=0,perimeter=0,height=0,unit="cm",angle=0,lineA=0,lineB=0):
            if shape == shape_type.SQUARE or shape_type.RECTANGLE or shape_type.PARALELLAGRAM:
                return width * height + f"{unit}2"
            elif shape == shape_type.TRIANGLE:
                return (width * height)/2 + f"{unit}2"
            elif shape == shape_type.DIAMOND:
                return (((perimeter/4)*perimeter/4)*math.sin(angle)) + f"{unit}2"
            elif shape == shape_type.CIRCLE:
                return ((width/2)**2)* round(math.pi,3) + f"{unit}2"
            elif shape == shape_type.SEMICIRCLE:
                return shape_type.twodshapes.area("circle",width) / 2 + f"{unit}2"
            elif shape == shape_type.QUATERCIRCLE:
                return shape_type.twodshapes.area("circle",width) / 4 +f"{unit}2"
            elif shape == shape_type.TRAPIZIUM:
                return (((lineA + lineB)/2)*height) + f"{unit}2"
            elif shape == shape_type.PENTAGON:
                return ((0.5 * (((perimeter/5)/2)* math.tan(180/5)))*perimeter)+ f"{unit}2"
            elif shape == shape_type.HEXAGON:
                return((((perimeter/6)**2)**(1/3))/2) + f"{unit}2"
            elif shape == shape_type.HEPTAGON:
                return (7/4 * (((perimeter/7)**2)*(math.cot(180/7)))) + f"{unit}2"
            elif shape == shape_type.OCTAGON:
                return (2 * (1+math.sqrt(2)) ** (perimeter/8)) + f"{unit}2"
            elif shape ==  shape_type.NONAGON:
                return (9/4 * (((perimeter/9)**2)*(math.cot(180/9)))) + f"{unit}2"
            elif shape == shape_type.DECAGON:
                return (5/2*(perimeter/10**2)) * (math.sqrt(7*(math.sqrt(5)))) + f"{unit}2"
