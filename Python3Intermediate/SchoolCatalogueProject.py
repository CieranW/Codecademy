class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getNumberOfStudents(self):
        return self.numberOfStudents

    def setNumberOfStudents(self, newnumberOfStudents):
        self.numberOfStudents = newnumberOfStudents

    def __repr__(self):
        phrase = "A {level} school named {name} with {numberOfStudents} students.".format(
            level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)
        return phrase


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        phrase = super().__repr__()
        add_phrase = "The pickup policy is {pickupPolicy}".format(
            pickupPolicy=self.pickupPolicy)
        return phrase + add_phrase


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def getSportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        phrase = super().__repr__()
        return phrase + "\nWe have the following sports teams: {sportsTeams}.".format(sportsTeams=self.sportsTeams)


a = School("Dat'sNuts", "High", 420)
print(a)
b = PrimarySchool("DeezNuts", 690, "Pickup Allowed.")
print(b)
c = HighSchool("MyNuts", 89890, ["Football",
               "Basketball", "Swimming", "Volleyball"])
print(c)
