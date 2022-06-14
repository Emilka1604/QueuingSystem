

class ServiceDevice:

    def __init__(self, executeFunction):
        self.executeFunction = executeFunction

    def execute(self):
        return self.executeFunction()