# Write your code here
from student import Student

def main():
    student = Student("Ken", 10)
    student.randomizeScores(10, 75, 100)
    print(student)
    print("Mean:", student.getMean())
    print("Median:", student.getMedian())
    print("Mode:", student.getMode())
    print("Standard deviation:", student.getStd())
    student.randomizeScores(10, 50, 100)
    print(student)
    print("Mean:", student.getMean())
    print("Median:", student.getMedian())
    print("Mode:", student.getMode())
    print("Standard deviation:", student.getStd())


if __name__ == "__main__":
    main()