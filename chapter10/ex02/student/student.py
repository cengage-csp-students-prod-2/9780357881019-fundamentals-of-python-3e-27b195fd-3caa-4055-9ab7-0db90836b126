class Scores():
    def __init__(self, scores=[0,0,0,0,0,0,0,0,0,0]):
        self.scores = list(scores)
    def __str__(self):
        return ' '.join(map(str,self.scores))
    def __repr__(self):
        return f'Scores: {str(self)}'
class Student():
    def __init__(self, name,scores=Scores()):
        self.name = name
        self.scores = scores
        
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    def __ge__(self, other):        
        return self.name >= other.name
    def __repr__(self):
        return f'Name: {self.name}\nScores: {str(self.scores)}'
    
def main():
    names=["John","Mike","Joe","Sally","Jane","Bob","Nancy","Tim","Sue","George"]
    students=[Student(name) for name in names]
    for student in students:
        print(student)
    print("  Sorted list of students:")
    for student in sorted(students):
        print(student)

if __name__ == "__main__":
    main()