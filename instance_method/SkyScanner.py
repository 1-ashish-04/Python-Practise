class SkyScanner:

    def searchFlights(self, source, destination): # pass by parameter with return statement

        noOfFlights = 1
        nameOfFlights = "Indigo"

        return "No of flights is", noOfFlights, "and name of flights is",nameOfFlights

s = SkyScanner()

# option 1 of capturing data from return
flights = s.searchFlights("Delhi", "Paris")

print(flights)

# option 2 of capturing data from return
print(s.searchFlights("Delhi","Ahemdabad"))

print(s.searchFlights.__dict__) # {}   ------> searchFlights method dictionary



