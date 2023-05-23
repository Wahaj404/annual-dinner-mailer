class Student:
    def __init__(self, row):
        self.name = row[3]
        self.nu_id = row[4]
        self.roll_num = row[5]
        self.verified = row[8] == "Verified"

    def __repr__(self):
        return f"{self.name} {self.nu_id} {self.roll_num} {self.verified}"
