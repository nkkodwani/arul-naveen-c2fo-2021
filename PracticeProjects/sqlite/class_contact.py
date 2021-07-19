class Contact:
    #contact class to add to contacts db - pulled this code from a YT video

    def __init__(self, first, last, email, phone): #constructor
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone

    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    