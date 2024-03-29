
class phone:
    def call(self):
        print("You Can Call")
    def message(self):
        print("You can message")


class Samsung(phone):  # here samsung inherit phone class by using syntext (phone)
    def photo(self):
        print("You can take Photo")


s = Samsung()
s.message()
s.call()
s.photo()