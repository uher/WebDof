from engine import BMEngine


class NewEngine(BMEngine):

    version = '0.3'
    checkCode = "second"

    def __init__(self):
        print('Initialized Engine Version: ' + self.version)
    
    def printTest(self):
        print('checkCode : ' + self.checkCode)

