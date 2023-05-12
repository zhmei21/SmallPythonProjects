class apartments:
    def __init__(self, name, location, beds, price):
        """
        initialise new apartments
        * nameOfApartment (str): name of the apartments
        * locationOfApartment (str): location of the apartments
        * bedsOfApartment (int): number of beds in apartment
        * priceOfApartment (float): prices of different apartment
        """

        self.__nameOfApartment = name
        self.__locationOfApartment = location
        self.__bedsOfApartment = beds
        self.__priceOfApartment = price

    def getName(self):
        """
        return name from apartment

        :return:
        """
        return self.__nameOfApartment

    def getLocation(self):
        """
        return location from apartment

        :return:
        """
        return self.__locationOfApartment

    def getBeds(self):
        """
        return beds from apartment

        :return:
        """

        return self.__bedsOfApartment

    def getPrice(self):
        """
        return prices from apartment

        :return:
        """

        return self.__priceOfApartment

apartments1 = apartments("Sweeet Home", "Zuerich", "35", 88.50)
apartments2 = apartments("Golden Sun", "Bern", "55", 79.90)
apartments3 = apartments("Sunrise Clouds", "Geneva", "80", 100.00)


print("First Apartment: ", apartments1.getName(), "|Location:", apartments1.getLocation(), "|Beds:", apartments1.getBeds(), "|Price:", apartments1.getPrice())
print("Second Apartment: ", apartments2.getName(), "|Location:", apartments2.getLocation(), "|Beds:", apartments2.getBeds(), "|Price:", apartments2.getPrice())
print("Third Apartment: ", apartments3.getName(), "|Location:", apartments3.getLocation(), "|Beds:", apartments3.getBeds(), "|Price:", apartments3.getPrice())

input("Exit")