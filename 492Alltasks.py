import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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
        print(newbattery)

    def new_speed(self, newspeed):
        self.current_speed = newspeed
        print(newspeed)

    def new_position(self, newposition):
        self.current_position = newposition
        print(newposition)

    def new_power(self, newpower):
        self.current_power = newpower
        print(newpower)

class DetectionVehicle: 
    def __init__(self):
        self.distance = 0
    
    def distancecheck(self):
        popup = tk.Tk()
        popup.title('Distance Information')

        label = tk.Label(popup, text='Enter the distance:')
        label.pack(pady=10)

        entry = tk.Entry(popup)
        entry.pack(pady=10)

        button = tk.Button(popup, text='OK', command=lambda: self.set_distance(entry.get(), popup))
        button.pack(pady=10)

        popup.mainloop()

    def set_distance(self, distance, popup):
        try:
            self.distance = float(distance)
            print(f"Distance from stop sign is: {self.distance} meters")
        except ValueError:
            print("Invalid input. Please enter a numeric value for distance.")

        popup.destroy()

class VehicleApp:
    def __init__(self, master, vehicle, vehicle_system, detection_vehicle):
        self.master = master
        self.master.title("Vehicle Control and Telemetry App")
        
        self.vehicle = vehicle
        self.vehicle_system = vehicle_system
        self.detection_vehicle = detection_vehicle

        self.create_widgets()

    def create_widgets(self):
        # Matplotlib figure
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

        # Embed Matplotlib figure in Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Vehicle control buttons
        self.start_button = ttk.Button(self.master, text="Start", command=self.start_car)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_car)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Telemetry GUI
        self.battery_label = tk.Label(self.master, text="Battery Charge Level:")
        self.battery_label.pack()
        self.battery_entry = tk.Entry(self.master)
        self.battery_entry.pack()

        self.speed_label = tk.Label(self.master, text="Current Speed:")
        self.speed_label.pack()
        self.speed_entry = tk.Entry(self.master)
        self.speed_entry.pack()

        self.position_label = tk.Label(self.master, text="Current Position:")
        self.position_label.pack()
        self.position_entry = tk.Entry(self.master)
        self.position_entry.pack()

        self.power_label = tk.Label(self.master, text="Current Power:")
        self.power_label.pack()
        self.power_entry = tk.Entry(self.master)
        self.power_entry.pack()

        self.update_button = ttk.Button(self.master, text="Update Values", command=self.update_values)
        self.update_button.pack()

    def start_car(self):
        self.vehicle.start_car()

    def stop_car(self):
        self.vehicle.stop_car()

    def update_values(self):
        new_battery = float(self.battery_entry.get())
        new_speed = float(self.speed_entry.get())
        new_position = float(self.position_entry.get())
        new_power = float(self.power_entry.get())

        self.vehicle_system.new_battery(new_battery)
        self.vehicle_system.new_speed(new_speed)
        self.vehicle_system.new_position(new_position)
        self.vehicle_system.new_power(new_power)

if __name__ == "__main__":
    my_vehicle = Vehicle()
    vehicle_system = VehicleSystem()
    detection_vehicle = DetectionVehicle()

    root = tk.Tk()
    app = VehicleApp(root, my_vehicle, vehicle_system, detection_vehicle)

    detection_vehicle.distancecheck()  # Display distance input window

    root.mainloop()
