import math
import random
import turtle
from turtle import Turtle

from matplotlib import pyplot as plt

turtle.tracer(0, 0)


def estimate_pressure(sprite):
    total_change_in_momentum = sum(sum(v) for v in sprite.speeds)
    total_updates = len(sprite.speeds)
    if total_updates > 0:
        return total_change_in_momentum / total_updates
    return 0


class Sprite(Turtle):
    def __init__(self, x, y, heading, speed):
        super().__init__()
        self.speeds = list()
        self.up()
        self.goto(x, y)
        self.speed(speed)
        self.shape('circle')
        self.setheading(heading)

    def step(self):
        current_pos_x, current_pos_y = self.position()
        velocity_vector = (self.speed() * math.cos(math.radians(self.heading())),
                           self.speed() * math.sin(math.radians(self.heading())))
        new_x = current_pos_x + velocity_vector[0]
        new_y = current_pos_y + velocity_vector[1]
        self.speeds.append(velocity_vector)
        width = turtle.window_width()
        height = turtle.window_height()
        if abs(new_x) >= width // 2:
            self.setheading(180 - self.heading())
        if abs(new_y) >= height // 2:
            self.setheading(-self.heading())
        self.goto(new_x, new_y)


num_particles_range = range(50, 501, 50)
average_velocity_range = range(5, 51, 5)
pressures = []
sprites = list()
for i in num_particles_range:
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
    sprite = Sprite(x, y, random.randint(1, 360), random.randint(3, 7))
    sprites.append(sprite)

while True:
    for sprite in sprites:
        sprite.step()
        pressure = estimate_pressure(sprite)
        pressures.append(pressure)

    if len(pressures) == len(num_particles_range):
        # print(len(num_particles_range))
        break

    turtle.update()

plt.plot(num_particles_range, pressures)
plt.xlabel('Number of Particles (N)')
plt.ylabel('Pressure (P)')
plt.title('Pressure (P) versus Number of Particles (N)')
plt.show()

# Plot the graph for P versus V
# for v in average_velocity_range:
#     for sprite in sprites:
#         sprite.speed(v)

plt.plot(average_velocity_range, pressures)
plt.xlabel('Average Velocity (V)')
plt.ylabel('Pressure (P)')
plt.title('Pressure (P) versus Average Velocity (V)')
plt.show()
