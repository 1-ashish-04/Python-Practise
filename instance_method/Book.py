class BookMyShow:
    def __init__(self):
        print("self address", self)
        self.movieName = None

    def assignMovieName(self):
        print("assignSelf", self)
        self.movieName = "Dhoom"

print("object 1")
b = BookMyShow()
print("object address",b)
print(b.movieName)

b.movieName = "Drndr"
print(b.movieName)

b.assignMovieName()
print(b.movieName)

print("***********************************************************************************")
print("object 2")
b1 = BookMyShow()
print("object address",b1)
print(b1.movieName)

b1.movieName = "Drndr"
print(b1.movieName)

b1.assignMovieName()
print(b1.movieName)