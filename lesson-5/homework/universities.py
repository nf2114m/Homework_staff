universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    students = [i[1] for i in data]
    tuitions = [i[2] for i in data]
    return students, tuitions

def mean(lst):
    return sum(lst)/len(lst)

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n//2
    if n%2 == 0:
        return (sorted_lst[mid-1]+sorted_lst[mid])/2
    else:
        return sorted_lst[mid]


students, tuitions = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuitions)

mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)


print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,.0f}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,.0f}")
print("******************************")
