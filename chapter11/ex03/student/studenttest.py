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
    n=int(input("Enter action:\n1. Add score\n2. Delete score\n3. Replace score\n4. Exit\n"))
    while n!=4:
        if n==1:
            student.addScore(int(input("Enter score: ")))
            print(student)
            print("Mean:", student.getMean())
            print("Median:", student.getMedian())
            print("Mode:", student.getMode())
            print("Standard deviation:", student.getStd())
        elif n==2:
            student.deleteScore(int(input("Enter index: ")))
            print(student)
            print("Mean:", student.getMean())
            print("Median:", student.getMedian())
            print("Mode:", student.getMode())
            print("Standard deviation:", student.getStd())
        elif n==3:
            student.setScore(int(input("Enter index: ")), int(input("Enter score: ")))
            print(student)
            print("Mean:", student.getMean())
            print("Median:", student.getMedian())
            print("Mode:", student.getMode())
            print("Standard deviation:", student.getStd())
        n=int(input("Enter action:\n1. Add score\n2. Delete score\n3. Replace score\n4. Exit\n"))


if __name__ == "__main__":
    main()