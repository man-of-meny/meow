# shape thingy 
import math
class shapes():
    class get_shape():
        def shape(self):
            dimentions = input("what dimension does the object reside in")
            shape = input("what is the shape")
            if shape in ("circle","rectangle","parralelagram"):
                width = int(input("what is the width"))
                height = int(input("what is the height"))
                unit = input("what is the measurement")
            elif shape in ("triangle"):
                width = int(input("what is the width"))
                height = int(input("what is the height"))
                unit = input("what is the measurement")
            elif shape in ("circle","semicircle"):
                width = int(input("what is the width"))
                height = int(input("what is the height"))
                angle = int(input(f"this shape needs 1 interior angle from the {shape}"))        
                unit = input("what is the measurement")
            elif shape in ("diamond"):
                perimeter = int(input("what is the perimeter of the shaper"))
                angle = int(input(f"this shape needs 1 angle from the {shape}"))
                unit = input("what is the measurement")
            elif shape in ("trapezium"):
                height = int(input("what is the height"))
                lineA = int(input("what is the length of line a (the top line)"))
                lineB = int(input("what is the length of line b (the bottom line, alos the largest line)"))
                unit = input("what is the measurement")   
            elif shape in ("pentagon"):
                perimeter = int(input("what is the premiter of the shape"))
    class twodshapes():
        def area(self,shape: str,width=0,perimeter=0,height=0,unit="cm",angle=0,lineA=0,lineB=0):
            if shape == "square" or "rectangle" or "paralellagram":
                return width * height + "cm2"
            elif shape == "triangle":
                return (width * height)/2 + "cm2"
            elif shape == "diamond":
                return (((perimeter/4)*perimeter/4)*math.sin(angle)) + "cm2"
            elif shape == "circle":
                return ((width/2)**2)* round(math.pi,3) + "cm2"
            elif shape == "semi circle":
                return shapes.twodshapes.area("circle",width) / 2 + "cm2"
            elif shape == "trapezium":
                return (((lineA + lineB)/2)*height) + "cm2"
            elif shape in ("pentagon"):
                apoethem = (((perimeter/5)/2)* math.tan(180/5))
                area = (((0.5) * apoethem)*perimeter)
                return area + "cm2"
            





