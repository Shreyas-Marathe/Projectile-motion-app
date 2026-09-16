#imports
import matplotlib.pyplot as plt
import numpy as np

# into

print("-----------------------WELCOME TO THE PROJECTILE MOTION CALCULATOR!-----------------------")

# function defentitions

def collect_user_input():
    '''
    Collects user input for initial velocity, launch angle, acceleration, and initial height.
    '''
    global initial_velocity, angle, acceleration, initial_height, horizontal_acceleration
    initial_velocity = float(input("Enter the initial velocity (m/s) : "))
    angle = float(input("Enter the launch angle (degrees) : "))  
    acceleration = -1 * float(input("Enter the acceleration (m/s^2) : "))
    initial_height = float(input("Enter the initial height (m) : "))
    horizontal_acceleration = 0  # Assuming no horizontal acceleration

# input validation
    if initial_velocity < 0 or angle < 0 or acceleration > 0 or initial_height < 0:
        print("Invalid input. Please enter positive values for initial velocity, launch angle, and initial height, and a negative value for acceleration.")
        collect_user_input()
    elif angle > 90:
        print("Invalid input. Please enter a launch angle between 0 and 90 degrees.")
        collect_user_input()
    elif initial_height < 0:
        print("Invalid input. Please enter a non-negative value for initial height.")
        collect_user_input()
    elif initial_velocity == 0:
        print("Invalid input. Please enter a non-zero value for initial velocity.")
        collect_user_input()
    elif acceleration == 0:
        print("Invalid input. Please enter a non-zero value for acceleration.")
    else:
        print("User input collected successfully.")

def calculate_components_of_initial_velocity() -> tuple:
    '''
    calculates the horizontal and vertical components of the initial velocity based on the launch angle.
    '''

    global initial_velocity_horizontal, initial_velocity_vertical
    angle_rad = np.radians(angle)

    initial_velocity_horizontal = initial_velocity * np.cos(angle_rad)
    initial_velocity_vertical = initial_velocity * np.sin(angle_rad)

    return initial_velocity_horizontal, initial_velocity_vertical

def calculate_time_of_flight_and_final_velocity():
    '''
    calculates the time of flight and final velocity of the projectile.
    '''
    time_of_flight = (initial_velocity_vertical + np.sqrt(initial_velocity_vertical**2 - 2 * acceleration * initial_height)) / -acceleration

    final_velocity_horizontal = initial_velocity_horizontal
    final_velocity_vertical = initial_velocity_vertical + acceleration * time_of_flight

    final_velocity = np.sqrt(final_velocity_horizontal**2 + final_velocity_vertical**2)

    return final_velocity, time_of_flight

def calculate_horizontal_and_vertical_distance(time_of_flight):
    '''
    calculates the vertical and horizontal distances reached by the projectile.
    '''
    max_height = initial_height + (initial_velocity_vertical**2) / (2 * -acceleration)
    horizontal_distance = initial_velocity_horizontal * time_of_flight
    return max_height, horizontal_distance

#graphing function

def plot_trajectory(time_of_flight):
    '''
    Plots the trajectory of the projectile motion.
    '''
    time_points = np.linspace(0, time_of_flight, num=100)
    x_points = initial_velocity_horizontal * time_points
    y_points = initial_height + initial_velocity_vertical * time_points + 0.5 * acceleration * time_points**2

    plt.figure(figsize=(10, 5))
    plt.plot(x_points, y_points)
    plt.title("Projectile Motion Trajectory")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.grid()
    plt.xlim(0, max(x_points) * 1.1)
    plt.ylim(0, max(y_points) * 1.1)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.show()

# call all of the functions

collect_user_input()
calculate_components_of_initial_velocity()
final_velocity, time_of_flight = calculate_time_of_flight_and_final_velocity()
max_height, horizontal_distance = calculate_horizontal_and_vertical_distance(time_of_flight)
plot_trajectory(time_of_flight)