class Car:
    def __init__(self):
        self.petrol = 100

    def display_tank(self):
        print(f"The car contains {self.petrol} litres of fuel.")

    def drive(self, km):
        if self.petrol <= 0:
            print(f"You've run out of petrol, fill up!")
            return

        self.petrol -= (km * 5) / 100

        if self.petrol < 10:
            print(f"You will soon be out of petrol!")

        self.display_tank()

    def fill_up(self):
        self.petrol = 100
        print("You can go back!")
