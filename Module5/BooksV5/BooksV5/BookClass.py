class BookClass:
    # default parameter value
    fPrice = 0.0 
    # Accepts 9 parameters corresponding to the properties listed above,  and assigns them to the 9 internal properties.
    def __init__(self, sID, sTitle, sGenre, fPrice, sPaperback, iOnHand, sAuthorFirst, sAuthorLast, sPublisher):
        self.id = sID
        self.title = sTitle
        self.genre = sGenre
        self.price = fPrice
        self.paperback = sPaperback
        self.onHand = iOnHand
        self.authorFname = sAuthorFirst
        self.authorLname = sAuthorLast
        self.publisher = sPublisher
    # prints out a comma-delimited list of the 9 properties in this instance of the object.
    def printBookInfo(self):
        print(self.id + ", " + self.title + ", " + self.genre + ", " + str(self.price) + ", " + self.paperback + ", " + str(self.onHand) + ", " + 
              self.authorFname + ", " + self.authorLname + ", " + self.publisher)
    #  Accepts a file handle as a parameter, and writes out a comma-delimited list of the 9 properties in this instance of the object. 
    #  Write to the file handle that was passed into the function.   
    def writeBookInfo(self, file2):
        file2.write(self.id + ", " + self.title + ", " + self.genre + ", " + str(self.price) + ", " + self.paperback + ", " + str(self.onHand) + ", " + 
              self.authorFname + ", " + self.authorLname + ", " + self.publisher + "\n")
    
    # Takes an integer as a parameter, and adds the number passed into the iOnHand property.
    def addToOnHand(self, iOnHand):
        self.onHand = iOnHand
        print(iOnHand)
    # Takes a float as a parameter and replaces the value of the fPrice property with the new value.
    def setPrice(self, fPrice):
        self.price = fPrice
        print(fPrice)
        
#test the books class
#x = BookClass()
#x.printBookInfo("1234", "JJ's", "FIC", 22.99, "Y", 5, "John", "Smith", "Pubbies")
#x.addToOnHand(3)
#x.setPrice(22.99)