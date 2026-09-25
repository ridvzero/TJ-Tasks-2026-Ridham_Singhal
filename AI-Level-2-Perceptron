#TJ club tasks AI medium Perceptron
#Ridham Singhal , 26SCSE1010788

W1 = 3.5
W2 = 2.0
bias = -3
raw_hours = float(input("Enter your study hours:"))
attendance_percentage = float(input("Enter your attendance percentage:"))

study_hours= raw_hours / 10 
attendance = attendance_percentage / 100

weighted_sum = W1*study_hours + W2*attendance + bias
print("\n===========================")
print(f"1. Raw Inputs: {raw_hours}hrs, {attendance_percentage}%")
print(f"2. Normalized Inputs (0 to 1): x1 = {study_hours}, x2 = {attendance}")
print(f"3. Weight Multiplication: (x1 * w1) = {study_hours * W1:.2f}, (x2 * w2) = {attendance * W2:.2f}")
print(f"4. Summation (+ bias): {study_hours * W1:.2f} + {attendance * W2:.2f} + ({bias}) = {weighted_sum:.2f}")

if weighted_sum >= 0:
    print("5. Activation Decision: PASS")
else:
    print("5. Activation Decision: FAIL")
print("===========================\n")
