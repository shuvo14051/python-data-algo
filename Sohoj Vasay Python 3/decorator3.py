class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return self.fname + " " + self.lname


if __name__ == "__main__":
    name = Name('Younus', 'Ahamed')
    print(name.full_name)
    name.full_name = "Shuvo Mia"
    print(name.full_name)
