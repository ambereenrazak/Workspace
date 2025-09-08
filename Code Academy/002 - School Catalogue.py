class School:
  def __init__(self, primary, middle, high):
    self.primary = primary
    self.middle = middle
    self.high = high
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  def set_numberOfStudents(self, new_numberOfStudents):
    self.numberOfStudents = new_numberOfStudents
  def __repr__(self):
    print("A {level} school named {name} with {numberOfStudents} students".format(level = self.level, name = self.name, numberOfStudents = self.numberOfStudents))