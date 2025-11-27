def input_student_name() -> str:
  """Correct input of student name."""
  while True:
    # Get student name, remove whitespace and capitalize first letter
    name = input("Enter the student's name: ").strip().capitalize()
    # Check if name is not empty
    if not name:
      print("Error: Student name cannot be empty.")
      continue
    return name


def student_list_is_not_empty(students: list) -> bool:
  # Check if students list contains at least one student
  if not students:
    print("The student list is empty.")
    return False
  return True


def add_new_student(students: list) -> None:
  """Add a new student if not already present."""
  # Get name for new student
  name = input_student_name()

  # Check if student with this name already exists
  if any(student['name'] == name for student in students):
    print(f"Student {name} already exists.")
    return
    
  # Add new student with empty grades list
  students.append({'name': name, 'grades': []})


def add_grades_for_student(students: list) -> None:
  """Add grades for an existing student."""
  # Get name of student to add grades for
  name = input_student_name()
  # Find student by name (returns None if not found)
  student = next((s for s in students if s['name'] == name), None)
  if not student:
    print(f"Student {name} not found.")
    return
    
  # Continuous grade input until user types 'done'
  while True:
    grade_input = input("Enter a grade (or 'done' to finish): ").strip()
    # Exit loop if user is done entering grades
    if grade_input.lower() == 'done':
        break

    try:
      # Convert input to integer
      grade = int(grade_input)
      # Validate grade range (0-100)
      if not (0 <= grade <= 100):
        raise Exception("Grade must be between 0 and 100")
        # Add valid grade to student's grade list
        student['grades'].append(grade)
    except ValueError:
      print("Invalid input. Please enter a number.")
    except Exception as e:
      print(e)    


def calc_average_grade(student) -> float | None:
  # Calculate average grade, handle division by zero for empty grade lists
  try:
    return sum(student['grades'])/len(student['grades'])
  except ZeroDivisionError:
    return None


def generate_report(students: list) -> None:
  """Display report of all students' grades and statistics."""
  print("--- Student Report ---")
  averages = []
  # Process each student in the list
  for student in students:
    name = student['name']
    avg = calc_average_grade(student)

  # Handle students with no grades
  if avg is None:
    print(f"{name}'s average grade is N/A.")
  else:
    averages.append(avg)
    print(f"{name}'s average grade is {avg:.1f}")

  # Calculate and display overall statistics if grades exist
  if averages:
    max_avg = max(averages)
    min_avg = min(averages)
    overall_avg = sum(averages) / len(averages)
    print("-" * 20)
    print(f"Max Average: {max_avg:.1f}")
    print(f"Min Average: {min_avg:.1f}")
    print(f"Overall Average: {overall_avg:.1f}")
  else:
    print("-" * 20)
    print("No grades available to calculate overall statistics.")


def find_top_performer(students: list) -> None:
  """Find and display the student with the highest average grade."""
  # Filter students who have at least one grade
  students_with_grades = [s for s in students if s.get('grades') and len(s['grades']) > 0]
    
  # Check if any students have grades
  if not students_with_grades:
    print("No students with grades available.")
    return
		
  try:
    # Find student with highest average grade using max() with lambda function
    top_student = max(students_with_grades, key=lambda student: sum(student["grades"]) / len(student["grades"]))
    # Calculate average grade for top performer
    avg_grade = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student['name']} with a grade of {avg_grade:.1f}")
  except (ZeroDivisionError, KeyError, ValueError) as e:
    print(f"Error calculating top performer: {e}")


def display_menu() -> None:
  """Display the main menu options."""
  print("--- Student Grade Analyzer ---")
  print("1. Add a new student\n" \
  "2. Add grades for a student\n" \
  "3. Show report (all students)\n" \
  "4. Find top performer\n" \
  "5. Exit")


def main() -> None:
  # Initialize empty list to store students
  students = []

  # Main program loop
  while True:
    display_menu()
    try:
    	# Get user menu choice
      choice = int(input("Enter your choice: "))
    except ValueError:
      print("Error: incorrect number")
      continue  # Continue to next iteration if input is invalid

        # Process user choice using match-case
    match choice:
      case 1:
        add_new_student(students)
      case 2:
        # Only proceed if students list is not empty
        if student_list_is_not_empty(students):
          add_grades_for_student(students)
      case 3:
        # Only proceed if students list is not empty
        if student_list_is_not_empty(students):
          generate_report(students)
      case 4:
        # Only proceed if students list is not empty
        if student_list_is_not_empty(students):
          find_top_performer(students)
      case 5:
        print("Exiting program.")
        break  # Exit the program loop
      case _:
        print("Error: selected option does not exist")


if __name__ == "__main__":
  main()