class Pen:
    def __init__(self, color, has_grip):
        print("Creating a new pen")
        self.color = color
        self.grip = has_grip
    def write(self, message):
        print("The pen wrote a message:")
        print(message)
        return self

bic = Pen("blue", False)
print(bic.color)
print(bic.grip)

papermate = Pen("black", False)
print(papermate.color)
print(papermate.grip)

bic.write("Hello! I am the bic pen!").write("I am chaining methods!").write("One more method chain!")

