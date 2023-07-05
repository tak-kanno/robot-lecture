import numpy as np
import matplotlib.pyplot as plt

## Robot parameters
# Robot mass
m = 1
# Robot viscous friction coefficient
b = 0.1

## Simulation parameters
# Simulation time step
dt = 0.001
# Simulation time
t = np.arange(0, 5, dt)

## Control parameters
# Control gain
Kp = 30
Kd = 2
Ki = 0

## Variables
# Position
x = 0
# Velocity
dx = 0
# Position array for plotting
x_array = np.zeros(len(t))

# Target position
x_ref = 1

i = 0  # simulation step number

def simulation_step(tau):
    global x, dx
    # Compute acceleration (Equation of motion: m*ddx = tau - b*dx)
    ddx = (tau - b * dx) / m
    # Update velocity
    dx += ddx * dt
    # Update position
    x += dx * dt
    # Store position for plotting
    x_array[i] = x

def feedback_control(x_ref, x, dx):
    # Compute error
    e = x_ref - x
    # Compute control input
    tau = Kp * e - Kd * dx
    return tau

def draw_animation_frame(time, x, x_ref, tau, j):
    # Clear the plot
    plt.clf()
    # Draw the robot as a black circle
    plt.plot(x, 0, marker='o', color='k', markersize=10)
    # Draw the target position as a red cross
    plt.plot(x_ref, 0, marker='x', color='r', markersize=10)
    # Set the plot as square
    plt.axis('square')
    # x and y axis range
    plt.xlim(-0.5, 2)
    plt.ylim(-1, 1)
    # Draw time and control parameters
    plt.text(-0.4, 0.7, 'Time: {:.2f}'.format(time))
    plt.text(-0.4, 0.5, 'Kp: {:.1f} Kd: {:.1f} Ki: {:.1f}'.format(Kp, Kd, Ki))
    # Draw tau as bar
    plt.plot([x, x + tau / 100], [0, 0], linewidth=3, color='c')
    # Write animation frames to files
    plt.savefig('frames_2/{}.png'.format(j))

def simulation():
    j = 0  # animation frame number
    global i
    for i in range(len(t)):
        # Compute control input
        tau = feedback_control(x_ref, x, dx)
        # Simulate one step
        simulation_step(tau)
        # Print variables per 100 samples
        if i % 100 == 0:
            print('t= {:.3f} x= {:.3f} dx= {:.3f}'.format(t[i], x, dx))
        # Draw animation frame per 33 samples
        if i % 33 == 0:
            draw_animation_frame(t[i], x, x_ref, tau, j)
            j += 1
    
if __name__ == '__main__':
    simulation()
    # Open a new plot
    plt.figure()
    # Plot the position
    plt.plot(t, x_array)
    plt.xlabel('Time [s]')
    plt.ylabel('Position [m]')
    # save the figure
    plt.savefig('position.png')