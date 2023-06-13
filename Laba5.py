class Action():

    def __init__(self, line = None):
        self.line = line

    def counting(self):
        print(f"Результаты вычислений {self.line} = {self._res}")

class Math(Action):
    def __init__(self, line):
        super().__init__(line)
        self._res = None

    def action_math(self):
        self._res = eval(self.line)

class Rectangle(Action):
    def __init__(self, line = None):
        super().__init__(line)
        self._res = None
        self.length = ""
        self.width = ""

    def rectangle_area(self):
        self._res = self.length*self.width

class Convert(Rectangle):
    def __init__(self, line):
        super().__init__(line)


    def _convert_line(self):
        line = list(self.line)

        i = 0
        second_bool = False
        while i != len(line):
            if second_bool == False and line[i] != " " and line[i] != ",":
                self.length = self.length + line[i]
            elif line[i] == " " or line[i] == ",":
                line.pop(i)
                i -= 1
                second_bool = True
            else: 
                self.width = self.width + line[i]
            i += 1

        self.length = int(self.length)
        self.width = int(self.width)


mathematic = Math("10*10+3")
mathematic.action_math()
mathematic.counting()


rect = Convert("15,64")
rect._convert_line()
rect.rectangle_area()
rect.counting()


