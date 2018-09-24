
lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):

  total = (float(sum(numbers))/len(numbers))
  return total

def get_average(student):
  homework = .1 * average(student["homework"])
  quizzes = .3 * average(student["quizzes"])
  tests = .6 * average(student["tests"])

def get_class_average(class_list):

  results = []

  for student in class_list:
    get_average(student)
    results.append()
  return average(results)

student = [lloyd,alice,tyler]

get_class_average(student)

print("*****************************************************************************")

