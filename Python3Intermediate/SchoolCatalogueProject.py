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
        phrase = print("A {level} school named {name} with {numberOfStudents} students.".format(
            level=self.level, name=self.name, numberOfStudents=self.numberOfStudents))
        return phrase


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        add_phrase = print("The pickup policy is {pickupPolicy}".format(
            pickupPolicy=self.pickupPolicy))
        return parentRepr + add_phrase


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def getSportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr, "We have the following sports teams: {sportsTeams}.".format(sportsTeams=self.sportsTeams)


c = HighSchool("MyNuts", 89890, ["Football",
               "Basketball", "Swimming", "Volleyball"])
try:
    print(c)
except TypeError:
    # Code throws up an type error if I don't put this try clause in. Still trying to figure out why.
    print("Fuck this shit bro, why won't it work?? Keeps giving me an error.")
