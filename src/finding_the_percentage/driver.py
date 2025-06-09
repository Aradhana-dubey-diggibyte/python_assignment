from srs.finding_the_percentage.util import find_average

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        entry = input().split()
        name, scores = entry[0], list(map(float, entry[1:]))
        student_marks[name] = scores

    query_name = input()
    result = find_average(student_marks, query_name)
    print(f"{result:.2f}")
