# -----------------------------------------------
# Grade Generator -Calculator
# -----------------------------------------------
import csv

print("====Welcome to Grade Generator=====")
print("Enter your assignment details below>>>>>\n")

grades = []  # list to store all assignment info

# Input Collection part
# -------------------------------
while True:
    print(" Grades")
    name = input("Enter""assignment name: ").strip()
    if not name:
        print("Assignment name cannot be empty.")
        continue

    # Category (FA/SA)
    while True:
        category = input("Enter category (FA or SA): ").strip().upper()
        if category in ["FA", "SA"]:
            break
        print(" Invalid category. Please enter 'FA' or 'SA'.")

    # Grade (0–100)
    while True:
        try:
            grade = float(input("Enter grade (0–100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric grade.")

    # Weight ( must be positive)
    while True:
        try:
            weight = float(input("Enter weight (1–100): "))
            if weight > 0:
                break
            else:
                print("Weight must be a positive number.")
        except ValueError:
            print("Please enter a numeric weight.")

    # Store data
    grades.append({"name": name, "category": category, "grade": grade, "weight": weight})

    # Continue?
    more = input("Add another assignment? (y/n): ").lower()
    if more != "y":
        break

# Calculations
# -------------------------------
fa_items = [item for item in grades if item["category"] == "FA"]
sa_items = [item for item in grades if item["category"] == "SA"]

# Totals
total_fa_weight = sum(item["weight"] for item in fa_items)
total_sa_weight = sum(item["weight"] for item in sa_items)
total_weight = total_fa_weight + total_sa_weight

# Weighted contributions
total_fa_score = sum((item["grade"] / 100) * item["weight"] for item in fa_items)
total_sa_score = sum((item["grade"] / 100) * item["weight"] for item in sa_items)
weighted_total = total_fa_score + total_sa_score

# Final grade
final_percentage = (weighted_total / total_weight) * 100 if total_weight > 0 else 0
gpa = round((final_percentage / 100) * 5.0, 4)

# Pass/Fail part
# -------------------------------
fa_pass = total_fa_score >= (0.5 * total_fa_weight) if total_fa_weight > 0 else True
sa_pass = total_sa_score >= (0.5 * total_sa_weight) if total_sa_weight > 0 else True
status = "PASS" if (fa_pass and sa_pass) else "FAIL"

# Saving to CSV
# -------------------------------
with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Assignment", "Category", "Grade", "Weight"])
    for item in grades:
        writer.writerow([item["name"], item["category"], item["grade"], item["weight"]])


# Output
# -------------------------------
print("\n Grades saved to grades.csv\n")
print("--- RESULTS ---")
print(f"Total Formative: {total_fa_score:.2f} / {total_fa_weight}")
print(f"Total Summative: {total_sa_score:.2f} / {total_sa_weight}")
print("--------------------------")
print(f"Total Grade: {final_percentage:.2f} / 100")
print(f"GPA: {gpa}")
print(f"Status: {status}")
if status == "FAIL":
    print("Resubmission: Discussion Forum")
print("--------------------------")
print(" Calculation complete.")
