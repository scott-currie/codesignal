def main():
	print(studentsAge([15, 56, 52, 27, 84, 94, 40, 25, 73, 49, 1, 48, 47, 8, 30, 52, 26, 37, 7, 29, 77, 82, 25, 5, 72, 29, 61, 89, 73, 8, 24, 29, 51, 70, 28, 13, 58, 16, 54, 92, 45, 73, 51, 5, 83, 71, 95, 53, 75, 47, 73, 58, 75, 25, 9, 23, 88, 29, 68, 49, 81, 28, 39, 92, 35, 8, 4, 0, 56, 44, 72, 64, 85, 26, 39, 43, 94, 55, 60, 78, 62, 2, 18, 43, 56, 21, 28, 78, 4, 67, 66, 34, 68, 40, 61, 36, 31, 57, 19]))

def studentsAge(students):
    pairs = 0
    for n in range(len(students) - 1 ):
        if n < len(students) - 1:
            for o in range(n + 1, len(students)):
#                print("students[o]", students[o], " - students[n]", students[n], " = ", students[o] - students[n])
                if students[o] - students[n] == 1:
                    pairs += 1

    return pairs


if __name__ == "__main__":
	main()