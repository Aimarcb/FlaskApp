class Contact():
    def __init__(self, name, phone_number, date, genre) :
        self.name = name
        self.phone_number = phone_number
        self.date = date
        self.genre = genre

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPhone(self, phone_number):
        self.phone_number = phone_number

    def getPhone(self):
        return self.phone_number
    
    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date
    
    def setDate(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def to_json(self):
        var = {
                    "name"          : self.name,
                    "phone_number"  : self.phone_number,
                    "date"          : self.date,
                    "genre"         : self.genre
                }
        return var

    def isAdult(self):
        year = int(self.date.split('-')[0])

        return True if year  <= 2003 else False