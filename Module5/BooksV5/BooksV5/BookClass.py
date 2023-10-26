class BookClass:
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
    
    #  Accepts a file handle as a parameter, and writes out a comma-delimited list of the 9 properties in this instance of the object. 
    #  Write to the file handle that was passed into the function.   
    def writeBookInfo(self):
    
    # Takes an integer as a parameter, and adds the number passed into the iOnHand property.
    def addToOnHand(self):
        
    # Takes a float as a parameter and replaces the value of the fPrice property with the new value.
    def setPrice(self):