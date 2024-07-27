from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SHAPE = "square"
LEFT = 180
MAX_Y = 250
MIN_Y = -250


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed_of_cars = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(0, 6) == 1:
            car1 = Car()
            self.cars.append(car1)
        else:
            pass

    def move_cars(self):
        for car in self.cars:
            car.go_forward(self.speed_of_cars)

    def update_speed(self):
        self.speed_of_cars += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(LEFT)
        self.create_random_location()

    def create_random_location(self):
        y_cor = random.randint(MIN_Y, MAX_Y)
        self.goto(x=300, y=y_cor)

    def go_forward(self, move_distance):
        self.forward(move_distance)

