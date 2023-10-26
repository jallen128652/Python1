class BookClass:
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
    def printBookInfo(self):