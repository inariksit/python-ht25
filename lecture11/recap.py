############################################################
## Define a class Teacher so that the following code runs ##
############################################################

class Teacher:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def getCourses(self):
        return self.courses

    def addCourse(self,course):
        self.courses.append(course)


my_teacher = Teacher("Inari", ["DAT425", "DAT315", "DAT446", "DAT457"])

print(my_teacher.getCourses()) ## Should print ["DAT425", "DAT315", "DAT446", "DAT457"]

####

my_teacher.addCourse("XXX999")
print(my_teacher.getCourses()) ## Should print ["DAT425", "DAT315", "DAT446", "DAT457", "XXX999"]

############################################################
## Define a class Lecture so that the following code runs ##
############################################################

class Lecture:
    def __init__(self, ccode, weekday, start, end):
        self.ccode = ccode
        self.weekday = weekday
        self.start = start
        self.end = end

    def getDuration(self):
        return self.end - self.start

my_lecture = Lecture("DAT425", "Monday", 8, 10)

print(my_lecture.getDuration()) ## should print 2