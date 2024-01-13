import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

class Vehicle: 
    def __init__(self):
        self.started = False

    def start_car(self):
        if not self.started:
            print("Car Starts")
            self.started = True

    def stop_car(self):
        if self.started:
            print("Car Stops")
            self.started = False

class VehicleSystem:
    def __init__(self):
        self.battery_charge_lvl = 0
        self.current_speed = 0
        self.current_position = 0
        self.current_power = 0

    def new_battery(self, newbattery):
        self.battery_charge_lvl = newbattery

    def new_speed(self, newspeed):
        self.current_speed = newspeed

    def new_position(self, newposition):
        self.current_position = newposition

    def new_power(self, newpower):
        self.current_power = newpower

    def generate_random_values(self):
        self.new_battery(random.uniform(0, 100))
        self.new_speed(random.uniform(0, 100))
        self.new_position(random.uniform(0, 1000))
        self.new_power(random.uniform(0, 100))

class DetectionVehicle: 
    def __init__(self):
        self.distance = 0
        self.road_signs = ["Stop Sign", "Yield Sign", "Traffic Light", "Pedestrian Crossing"]
        self.road_sign = ""
        self.random_distance = 0
        self.popup = None
        self.road_sign_label = None
        self.entry = None

    def distancecheck(self):
        self.randomize_and_update()

        self.popup = tk.Tk()
        self.popup.title('Vehicle Information')

        self.road_sign_label = tk.Label(self.popup, text=f"Randomized Road Sign: {self.road_sign}")
        self.road_sign_label.pack(pady=10)

        label = tk.Label(self.popup, text='Enter the distance:')
        label.pack(pady=10)

        self.entry = tk.Entry(self.popup)
        self.entry.insert(0, f"{self.random_distance:.2f}")
        self.entry.pack(pady=10)

        ok_button = tk.Button(self.popup, text='OK', command=self.update_values)
        ok_button.pack(pady=10)

        randomize_button = tk.Button(self.popup, text='Randomize Again', command=self.randomize_and_update)
        randomize_button.pack(pady=10)

        self.popup.mainloop()

    def randomize_and_update(self):
        self.road_sign = random.choice(self.road_signs)
        self.random_distance = random.uniform(0, 100)
        self.update_labels()

    def update_labels(self):
        if self.road_sign_label:
            self.road_sign_label.config(text=f"Randomized Road Sign: {self.road_sign}")
        if self.entry:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"{self.random_distance:.2f}")

    def update_values(self):
        try:
            self.distance = float(self.entry.get())
            print(f"Distance from the chosen road sign is: {self.distance} meters")
        except ValueError:
            print("Invalid input. Please enter a numeric value for distance.")

        self.update_labels()

        print(f"Randomized Road Sign: {self.road_sign}")
        print(f"Randomized Distance: {self.random_distance:.2f}")

class VehicleApp:
    def __init__(self, master, vehicle, vehicle_system, detection_vehicle):
        self.master = master
        self.master.title("Vehicle Control and Telemetry App")
        self.vehicle = vehicle
        self.vehicle_system = vehicle_system
        self.detection_vehicle = detection_vehicle
        self.create_grid()
        self.create_telemetry()
        self.create_controls()
        self.detection_vehicle.distancecheck()  

    def create_grid(self):
        binary_array = [
            [1, 1, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        num_rows = len(binary_array)
        num_columns = len(binary_array[0])
        center_x = num_rows // 2
        center_y = num_columns // 2
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks(range(num_columns + 1))
        self.ax.set_yticks(range(num_rows + 1))
        self.ax.grid(True, which='both')
        self.ax.plot(center_y, center_x, marker='X', markersize=10, markerfacecolor='blue', label='Vehicle')
        for i, row in enumerate(binary_array):
            for j, cell in enumerate(row):
                if cell == 1:
                    self.ax.add_patch(plt.Rectangle((j, num_rows - 1 - i), 1, 1, fill=True, color='gray'))
        self.ax.legend()
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Grid Map')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def create_telemetry(self):
        self.telemetry_frame = ttk.Frame(self.master)
        self.telemetry_frame.pack(side=tk.TOP, pady=10)

        self.battery_label = tk.Label(self.telemetry_frame, text="Battery Charge Level:")
        self.battery_label.grid(row=0, column=0)
        self.speed_label = tk.Label(self.telemetry_frame, text="Current Speed:")
        self.speed_label.grid(row=1, column=0)
        self.position_label = tk.Label(self.telemetry_frame, text="Current Position:")
        self.position_label.grid(row=2, column=0)
        self.power_label = tk.Label(self.telemetry_frame, text="Current Power:")
        self.power_label.grid(row=3, column=0)

        self.battery_entry = tk.Entry(self.telemetry_frame)
        self.battery_entry.insert(0, f"{self.vehicle_system.battery_charge_lvl:.2f}")
        self.battery_entry.grid(row=0, column=1)

        self.speed_entry = tk.Entry(self.telemetry_frame)
        self.speed_entry.insert(0, f"{self.vehicle_system.current_speed:.2f}")
        self.speed_entry.grid(row=1, column=1)

        self.position_entry = tk.Entry(self.telemetry_frame)
        self.position_entry.insert(0, f"{self.vehicle_system.current_position:.2f}")
        self.position_entry.grid(row=2, column=1)

        self.power_entry = tk.Entry(self.telemetry_frame)
        self.power_entry.insert(0, f"{self.vehicle_system.current_power:.2f}")
        self.power_entry.grid(row=3, column=1)

        self.update_button = tk.Button(self.telemetry_frame, text="Update Values", command=self.update_values)
        self.update_button.grid(row=4, column=0, columnspan=2)

    def create_controls(self):
        self.controls_frame = ttk.Frame(self.master)
        self.controls_frame.pack(side=tk.TOP, pady=10)

        self.start_button = ttk.Button(self.controls_frame, text="Start", command=self.vehicle.start_car)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(self.controls_frame, text="Stop", command=self.vehicle.stop_car)
        self.stop_button.pack(side=tk.LEFT, padx=10)

    def update_values(self):
        self.vehicle_system.generate_random_values()
        self.battery_entry.delete(0, tk.END)
        self.battery_entry.insert(0, f"{self.vehicle_system.battery_charge_lvl:.2f}")

        self.speed_entry.delete(0, tk.END)
        self.speed_entry.insert(0, f"{self.vehicle_system.current_speed:.2f}")

        self.position_entry.delete(0, tk.END)
        self.position_entry.insert(0, f"{self.vehicle_system.current_position:.2f}")

        self.power_entry.delete(0, tk.END)
        self.power_entry.insert(0, f"{self.vehicle_system.current_power:.2f}")

if __name__ == "__main__":
    vehicle = Vehicle()
    vehicle_system = VehicleSystem()
    detection_vehicle = DetectionVehicle()

    root = tk.Tk()
    app = VehicleApp(root, vehicle, vehicle_system, detection_vehicle)
    root.mainloop()
