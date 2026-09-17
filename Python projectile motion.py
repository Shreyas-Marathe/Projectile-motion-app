# imports
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


# main program
def projectile_motion_calculator():

    # ---------------- CALCULATION FUNCTIONS ----------------

    def calculate_components_of_initial_velocity(initial_velocity, angle) -> tuple:
        '''
        Calculates the horizontal and vertical components
        of the initial velocity based on the launch angle.
        '''

        angle_rad = np.radians(angle)

        initial_velocity_horizontal = initial_velocity * np.cos(angle_rad)
        initial_velocity_vertical = initial_velocity * np.sin(angle_rad)

        return initial_velocity_horizontal, initial_velocity_vertical


    def calculate_time_of_flight_and_final_velocity(
        initial_velocity_horizontal,
        initial_velocity_vertical,
        acceleration,
        initial_height
    ):
        '''
        Calculates the time of flight and final velocity.
        '''

        time_of_flight = (
            initial_velocity_vertical
            + np.sqrt(
                initial_velocity_vertical**2
                - 2 * acceleration * initial_height
            )
        ) / -acceleration

        final_velocity_horizontal = initial_velocity_horizontal
        final_velocity_vertical = (
            initial_velocity_vertical
            + acceleration * time_of_flight
        )

        final_velocity = np.sqrt(
            final_velocity_horizontal**2
            + final_velocity_vertical**2
        )

        return final_velocity, time_of_flight


    def calculate_horizontal_and_vertical_distance(
        initial_velocity_horizontal,
        initial_velocity_vertical,
        acceleration,
        initial_height,
        time_of_flight
    ):
        '''
        Calculates the maximum height and horizontal distance.
        '''

        max_height = (
            initial_height
            + (initial_velocity_vertical**2) / (2 * -acceleration)
        )

        horizontal_distance = (
            initial_velocity_horizontal * time_of_flight
        )

        return max_height, horizontal_distance


    # ---------------- GRAPH ----------------

    def plot_trajectory(
        initial_velocity_horizontal,
        initial_velocity_vertical,
        acceleration,
        initial_height,
        time_of_flight
    ):
        '''
        Plots the trajectory of the projectile motion.
        '''

        time_points = np.linspace(0, time_of_flight, num=100)

        x_points = initial_velocity_horizontal * time_points

        y_points = (
            initial_height
            + initial_velocity_vertical * time_points
            + 0.5 * acceleration * time_points**2
        )

        plt.figure(figsize=(10, 5))

        plt.plot(x_points, y_points)

        plt.title("Projectile Motion Trajectory")
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")

        plt.grid()

        plt.xlim(0, max(x_points) * 1.1)
        plt.ylim(0, max(y_points) * 1.1)

        plt.axhline(0, color="black", lw=0.5)
        plt.axvline(0, color="black", lw=0.5)

        plt.show()


    # ---------------- RESULTS WINDOW ----------------

    def display_results(
        final_velocity,
        time_of_flight,
        max_height,
        horizontal_distance
    ):
        '''
        Displays the results in a new Tkinter window.
        '''

        results_window = tk.Toplevel(window)

        results_window.title("Projectile Motion Results")
        results_window.geometry("400x300")

        tk.Label(
            results_window,
            text=(
                f"Final velocity: {final_velocity:.2f} m/s\n\n"
                f"Time of flight: {time_of_flight:.2f} s\n\n"
                f"Maximum height: {max_height:.2f} m\n\n"
                f"Horizontal distance: {horizontal_distance:.2f} m"
            ),
            font=("Arial", 12)
        ).pack(pady=30)


    # ---------------- SIMULATION ----------------

    def simulate():
        '''
        Gets the values from the Tkinter input boxes
        and runs the projectile motion calculations.
        '''

        try:

            # Get values from the input boxes
            initial_velocity = float(velocity_entry.get())
            angle = float(angle_entry.get())
            acceleration = float(acceleration_entry.get())
            initial_height = float(height_entry.get())


            # Validate inputs
            if initial_velocity < 0:
                raise ValueError("Initial velocity must be non-negative.")

            if angle < 0 or angle > 90:
                raise ValueError("Launch angle must be between 0 and 90 degrees.")

            if acceleration >= 0:
                raise ValueError("Acceleration must be negative.")

            if initial_height < 0:
                raise ValueError("Initial height must be non-negative.")


            # Calculate velocity components
            initial_velocity_horizontal, initial_velocity_vertical = (
                calculate_components_of_initial_velocity(
                    initial_velocity,
                    angle
                )
            )


            # Calculate time of flight and final velocity
            final_velocity, time_of_flight = (
                calculate_time_of_flight_and_final_velocity(
                    initial_velocity_horizontal,
                    initial_velocity_vertical,
                    acceleration,
                    initial_height
                )
            )


            # Calculate maximum height and horizontal distance
            max_height, horizontal_distance = (
                calculate_horizontal_and_vertical_distance(
                    initial_velocity_horizontal,
                    initial_velocity_vertical,
                    acceleration,
                    initial_height,
                    time_of_flight
                )
            )


            # Display results
            display_results(
                final_velocity,
                time_of_flight,
                max_height,
                horizontal_distance
            )


            # Display graph
            plot_trajectory(
                initial_velocity_horizontal,
                initial_velocity_vertical,
                acceleration,
                initial_height,
                time_of_flight
            )


        except ValueError as error:

            messagebox.showerror(
                "Invalid Input",
                str(error)
            )


    # ---------------- TKINTER WINDOW ----------------

    window = tk.Tk()

    window.title("Projectile Motion Calculator")
    window.geometry("400x400")


    # Title
    tk.Label(
        window,
        text="Projectile Motion Calculator",
        font=("Arial", 16)
    ).pack(pady=20)


    # Initial velocity
    tk.Label(
        window,
        text="Initial velocity (m/s)"
    ).pack()

    velocity_entry = tk.Entry(window)
    velocity_entry.pack(pady=5)


    # Launch angle
    tk.Label(
        window,
        text="Launch angle (degrees)"
    ).pack()

    angle_entry = tk.Entry(window)
    angle_entry.pack(pady=5)


    # Acceleration
    tk.Label(
        window,
        text="Acceleration (m/s²)"
    ).pack()

    acceleration_entry = tk.Entry(window)
    acceleration_entry.pack(pady=5)


    # Initial height
    tk.Label(
        window,
        text="Initial height (m)"
    ).pack()

    height_entry = tk.Entry(window)
    height_entry.pack(pady=5)


    # Simulate button
    tk.Button(
        window,
        text="SIMULATE",
        command=simulate
    ).pack(pady=20)


    # Start the Tkinter application
    window.mainloop()


projectile_motion_calculator()
