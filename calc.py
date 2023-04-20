import math, random, string

def main():
    print("Hello. Input a response (ex: exit).")
    print("Choices: [1] Equation [2] Temperature [3] Unit Conversion [4] Shape Area/Volume [5] String Generation [6] Coordinate Distance")
    
    response = input("Reponse: ")

    if response.lower() in ["quit", "exit"]:
        print("Goodbye!")
        return
    else:
        if not response.isdigit():
            print("Reponse must be a number.")
            return

    response = int(response)

    if response == 1:
        print("Calculation Types: [1] Basic [2] Complex")

        calculation_type = input("Calculation Type: ")

        if not calculation_type.isdigit():
            print("Type must be a number.")
            return
        
        calculation_type = int(calculation_type)

        if calculation_type == 1:
            equation = input("Equation: ")
            
            if equation.lower() in ["quit", "exit"]:
                print("Goodbye!")
                return
            else:
                parts = equation.split()

                if len(parts) != 3:
                    print("Equation must have the format 'number operator number'")
                    return

                if "/" in parts[0]:
                    numerator, denominator = parts[0].split("/")

                    if not (numerator.isdigit() and denominator.isdigit()):
                        print("Numerator and denominator of the fraction must be valid numeric values.")
                        return

                    parts[0] = str(float(numerator) / float(denominator))

                if "/" in parts[2]:
                    numerator, denominator = parts[2].split("/")

                    if not (numerator.isdigit() and denominator.isdigit()):
                        print("Numerator and denominator of the fraction must be valid numeric values.")
                        return

                    parts[2] = str(float(numerator) / float(denominator))

                if not (parts[0].replace('.', '', 1).isdigit() and parts[2].replace('.', '', 1).isdigit()):
                    print("Numbers must be valid numeric values.")
                    return

                if parts[1] not in "+-*/":
                    print("Operator must be one of: +, -, *, /")
                    return

                result = float

                if parts[1] == "+":
                    result = float(parts[0]) + float(parts[2])
                elif parts[1] == "-":
                    result = float(parts[0]) - float(parts[2])
                elif parts[1] == "*":
                    result = float(parts[0]) * float(parts[2])
                elif parts[1] == "/":
                    result = float(parts[0]) / float(parts[2])

                print(f"Result: {result}")
        elif calculation_type == 2:
            equation = input("Equation: ")
            
            if equation.lower() in ["quit", "exit"]:
                print("Goodbye!")
                return
            else:
                equation = equation.replace("pow", "math.pow")
                equation = equation.replace("sqrt", "math.sqrt")

                result = eval(equation)
                
                print(f"Result: {result}")
    elif response == 2:
        degrees = input("Degrees: ")

        if not degrees.isdigit():
            print("Degrees must be a number.")
            return

        degrees = int(degrees)

        scale = input("Scale (To): ").lower()

        if scale not in ["f", "c", "k", "r", "fahrenheit", "celcius", "kelvin", "rankine"]:
            print("Scale must be one of: f, c, k, r, fahrenheit, celcius, kelvin, rankine")
            return

        result = int

        if scale in ["f", "fahrenheit"]:
            result = int((degrees * 1.8) + 32)
        elif scale in ["c", "celcius"]:
            result = int((degrees - 32) * 0.5)
        elif scale in ["k", "kelvin"]:
            result = int(degrees + 273.15)
        elif scale in ["r", "rankine"]:
            result = int((degrees + 459.67) * 1.8)

        print(f"Result: {result}")
    elif response == 3:
        value = input("Value: ")

        if not value.replace('.', '', 1).isdigit():
            print("Value must be a valid numeric value.")
            return

        value = float(value)

        unit_from = input("From Unit (in, cm): ").lower()

        if unit_from not in ["in", "cm", "inch", "centimeter", "centimeters"]:
            print("From unit must be one of: in, cm, inch, centimeter, centimeters")
            return

        unit_to = input("To Unit (in, cm): ").lower()

        if unit_to not in ["in", "cm", "inch", "centimeter", "centimeters"]:
            print("To unit must be one of: in, cm, inch, centimeter, centimeters")
            return

        result = float

        if unit_from in ["in", "inch"]:
            if unit_to in ["cm", "centimeter", "centimeters"]:
                result = value * 2.54
        elif unit_from in ["cm", "centimeter", "centimeters"]:
            if unit_to in ["in", "inch"]:
                result = value / 2.54

        print(f"Result: {result}")
    elif response == 4:
        print("Shape Types: [1] Circle [2] Square [3] Rectangle [4] Cube")

        shape_type = input("Shape Type: ")

        if not shape_type.isdigit():
            print("Type must be a number.")
            return

        shape_type = int(shape_type)

        if shape_type == 1:
            radius = input("Radius: ")

            if not radius.replace('.', '', 1).isdigit():
                print("Radius must be a valid numeric value.")
                return

            radius = float(radius)

            area = math.pi * radius ** 2

            print(f"Area: {area}")
        elif shape_type == 2:
            length = input("Length: ")

            if not length.replace('.', '', 1).isdigit():
                print("Length must be a valid numeric value.")
                return

            length = float(length)

            area = length ** 2

            print(f"Area: {area}")
        elif shape_type == 3:
            length = input("Length: ")
            width = input("Width: ")

            if not (length.replace('.', '', 1).isdigit() and width.replace('.', '', 1).isdigit()):
                print("Length and width must be valid numeric values.")
                return

            length = float(length)
            width = float(width)

            area = length * width

            print(f"Area: {area}")
        elif shape_type == 4:
            length = input("Length: ")

            width = input("Width: ")
            height = input("Height: ")

            if not (length.replace('.', '', 1).isdigit() and width.replace('.', '', 1).isdigit() and height.replace('.', '', 1).isdigit()):
                print("Length, width, and height must be valid numeric values.")
                return

            length = float(length)

            width = float(width)
            height = float(height)

            volume = length * width * height

            print(f"Volume: {volume}")
        else:
            print("Invalid shape type.")
            return
    elif response == 5:
        print("Select an operation: [1] Generate random integer [2] Generate random float [3] Generate random string [4] Generate random boolean")

        operation = input("Operation: ")

        if not operation.isdigit():
            print("Operation must be a number.")
            return

        operation = int(operation)

        if operation == 1:
            lower_bound = input("Lower bound: ")
            upper_bound = input("Upper bound: ")

            if not (lower_bound.isdigit() and upper_bound.isdigit()):
                print("Bounds must be valid numeric values.")
                return

            lower_bound = int(lower_bound)
            upper_bound = int(upper_bound)

            if lower_bound > upper_bound:
                print("Lower bound cannot be greater than upper bound.")
                return

            result = random.randint(lower_bound, upper_bound)

            print(f"Result: {result}")
        elif operation == 2:
            lower_bound = input("Lower bound: ")
            upper_bound = input("Upper bound: ")

            if not (lower_bound.replace('.', '', 1).isdigit() and upper_bound.replace('.', '', 1).isdigit()):
                print("Bounds must be valid numeric values.")
                return

            lower_bound = float(lower_bound)
            upper_bound = float(upper_bound)

            if lower_bound > upper_bound:
                print("Lower bound cannot be greater than upper bound.")
                return

            result = random.uniform(lower_bound, upper_bound)

            print(f"Result: {result}")
        elif operation == 3:
            length = input("Length of string: ")

            if not length.isdigit():
                print("Length must be a number.")
                return

            length = int(length)

            chars = string.ascii_letters + string.digits

            result = ''.join(random.choice(chars) for _ in range(length))
            print(f"Result: {result}")
        elif operation == 4:
            result = random.choice([True, False])

            print(f"Result: {result}")
        else:
            print("Invalid operation.")
    elif response == 6:
        first_point = input("Enter the coordinates of point 1 (in x,y,z format): ")
        second_point = input("Enter the coordinates of point 2 (in x,y,z format): ")

        x1, y1, z1 = map(int, first_point.split(","))
        x2, y2, z2 = map(int, second_point.split(","))

        distance = math.sqrt((x2 - x1) **2 + (y2 - y1) **2 + (z2 - z1) **2)

        print(f"The distance between the two points is: {distance}")

if __name__ == "__main__":
    main()
