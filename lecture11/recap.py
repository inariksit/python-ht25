############################################################
## Define a class Teacher so that the following code runs ##
############################################################

class Teacher:
    ## Modified the constructor to allow for two new ways:
    ## 1) Teacher("Only Name")
    ## 2) Teacher("Name", "A single course")
    def __init__(self, name, courses=[]):
                           # Default argument
                           # courses=[]: if not given, use []
        self.name = name

        ## Checking the type of the argument courses
        if type(courses) == list:
            self.courses = courses
        else:
            self.courses = [courses]

    def getCourses(self):
        return self.courses

    def addCourse(self,course):
        self.courses.append(course)


my_teacher = Teacher("Inari", ["DAT425", "DAT315", "DAT446", "DAT457"])

## Constructor that only takes teacher name
new_teacher = Teacher("N. N.")
new_teacher.addCourse("NNN111")

## Constructor that takes teacher name and a single course as string
another_teacher = Teacher("M. M.", "MMM222")

print(my_teacher.getCourses())

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

    ## Silly but valid Python: define addition and comparison for lectures
    def __add__(self, other):
        return self.getDuration() + other.getDuration()

    def __gt__(self, other):
        return self.getDuration() > other.getDuration()

class ChoirRehearsal:
    def __init__(self, cname, weekday, start, end):
        self.cname = cname
        self.weekday = weekday
        self.start = start
        self.end = end

    def getDuration(self):
        return self.end - self.start

    ## Again silly but valid: arithmetic operations for choir rehearsals!
    def __add__(self, other):
        return self.getDuration() + other.getDuration()

    def __gt__(self, other):
        return self.getDuration() > other.getDuration()


my_lecture = Lecture("DAT425", "Monday", 8, 10)
my_choir = ChoirRehearsal("Chalmers sångkör", "Monday", 18, 21)

## We can even compare lectures and choir rehearsals
## my_lecture + my_choir will give a result
## my_lecture > my_choir will give a result

print(my_lecture.getDuration()) ## should print 2