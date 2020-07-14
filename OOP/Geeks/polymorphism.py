class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")

    def language(self):
        print("Bangla is the most widely spoken language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_bd = Bangladesh()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
