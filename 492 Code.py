binary_array=[[0,0,0,0]
              [0,0,0,1]
              [0,0,1,0]
              [0,0,1,1]
              [0,1,0,0]
              [0,1,0,1]
              [0,1,1,0]
              [0,1,1,1]
              [1,1,1,1]
               ]

num_rows=len(binary_array)
num_columns=len(binary_array[0])

center_x=num_rows//2
center_y=num_columns//2

for i, row in enumerate(binary_array):
    for j, cell in enumerate(row):
        print(f"\nVehicle at center: ({center_x}, {center_y})")

class Vehicle: 
    def __init__(self):
        self.started=False
    def start_car(self):
        if not self.started:
            print("Car Will Start")
            self.started=True
    def stop_car(self):
        if self.started:
            print("Car will not Start")
            self.started!=True

my_Car=Vehicle()
my_Car.start_car()
my_Car.stop_car()

class VehicleSimulation:
    def __init__(self):
        self.detected_signs = {}
        self.signs_label = "Detected Signs:\n"
        self.signs_text = ""

    def update_signs(self):
       
        self.detected_signs = self.detect_signs()

        self.display_signs()

    def detect_signs(self):
        num_signs = 3
        detected_signs = {}

        for _ in range(num_signs):
            sign_position = self.generate_random_coordinate(), self.generate_random_coordinate()
            distance = self.calculate_distance(sign_position, (0, 0))
            detected_signs[sign_position] = distance

        return detected_signs

    def generate_random_coordinate(self):
        return round((2 * (0.5 - hash(self) % 100) * 50), 2)

    def calculate_distance(self, point1, point2):
        return round(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5, 2)

    def display_signs(self):
        for position, distance in self.detected_signs.items():
            self.signs_label += f"Sign at {position}, Distance: {distance} units\n"

class VehicleSystem:
    def __init__(self):
        self.battery_charge_lvl=100
        self.current_speed=30
        self.current_position=30
        self.current_power=0
    
    def new_battery(self, newbattery):
        self.battery_charge_lvl=newbattery
    
    def new_speed(self, newspeed):
        self.current_speed=newspeed
    
    def new_position(self, newposition):
        self.current_position=newposition
    
    def new_power(self, newpower):
        self.current_power=newpower