# 1
fav_movies = ["Memento", "Interstellar", "Inception", "The Dark Knight", "Oppenheimer"]
print(fav_movies[0])
print(fav_movies[1])
print(fav_movies[2])
print(fav_movies[3])
print(fav_movies[4])
# 2
total = 0

for i in range(4):
    grade = int(input("What is your grade? "))
    total = total + grade
    
average = total / 4
print("Average:", average)
# 3
size = int(input("What is the size? "))
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()
# 4
size = int(input("What is the size? "))
for i in range(size + 1):
    for j in range(i):
        print("*", end="")
    print()
# 5
def Task1(list):
    for i in list:
        print(i)

Task1(["Memento", "Interstellar", "Inception", "The Dark Knight", "Oppenheimer"])

def Task2(num1, num2, num3, num4):
    average = (num1 + num2 + num3 + num4)/4
    return average

print(Task2(100, 90, 80, 70))

def Task3(size):
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()

Task3(7)

def Task4(size):
    for i in range(size + 1):
        for j in range(i):
            print("*", end="")
        print()

Task4(7)