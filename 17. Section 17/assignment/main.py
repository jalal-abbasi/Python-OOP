class Body:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __gt__(self, other):
        return (self.height > other.height
                and self.weight > other.weight)

    def __ge__(self, other):
        return (self.height >= other.height
                and self.weight >= other.weight)

    def __eq__(self, other):
        return (self.height == other.height
                and self.weight == other.weight)

    def __ne__(self, other):
        return (self.height != other.height
                and self.weight != other.weight)

    def __le__(self, other):
        return (self.height <= other.height
                and self.weight <= other.weight)

    def __lt__(self, other):
        return (self.height < other.height
                and self.weight < other.weight)


my_Body = Body(170, 64)
ahmad_body = Body(185, 110)
hamid_body = Body(188, 120)
farshad_body = Body(170, 64)

print(my_Body == farshad_body)
print(my_Body < farshad_body)
print(my_Body < ahmad_body)