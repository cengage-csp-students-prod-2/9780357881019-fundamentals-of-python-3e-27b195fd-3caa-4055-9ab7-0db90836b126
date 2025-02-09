# Write your code here
class Student():
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    # def __le__(self, other):
    #     return self.name <= other.name
    # def __gt__(self, other):
    #     return self.name > other.name
    def __ge__(self, other):        
        return self.name >= other.name
    
def main():
    s1 = Student("John")
    s2 = Student("Mike")
    print(s1 == s2,": ",s1.name == s2.name)
    print(s1 < s2,": ",s1.name < s2.name)
    print(s1 <= s2,": ",s1.name <= s2.name)
    print(s1 > s2,": ",s1.name > s2.name)
    print(s1 >= s2,": ",s1.name >= s2.name)
    print(s1 != s2,": ",s1.name != s2.name)

if __name__ == "__main__":
    main()