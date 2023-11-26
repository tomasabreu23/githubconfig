import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_pos1 = 1
initial_pos2 = 4
initial_velocity1 = 1
initial_velocity2 = 2
mass1 = 1
mass2 = 1
num_frames = 100
box_size = 5 

def simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size):
    ball1_x = [initial_pos1]
    ball2_x = [initial_pos2]

    create_animation(ball1_x, ball2_x, box_size)

def create_animation(positions1, positions2, box_size):
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, box_size)
    ax.set_ylim(-0.1, 0.1)

    ball1, = ax.plot(positions1[0], 0, 'bo', markersize = 10)
    ball2, = ax.plot(positions2[0], 0, 'ro', markersize = 10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2
    
    ani = FuncAnimation(fig, update, frames = num_frames, blit = True)
    plt.show()

simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size)
    
    



