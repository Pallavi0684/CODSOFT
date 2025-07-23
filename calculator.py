print("🧮 Simple Calculator")

# Step 1: Get two numbers from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("❌ Please enter valid numbers.")
    exit()

# Step 2: Display operation choices
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Get user choice
choice = input("Enter your choice (1/2/3/4): ")

# Step 4: Perform calculation
if choice == '1':
    result = num1 + num2
    operation = "+"
elif choice == '2':
    result = num1 - num2
    operation = "-"
elif choice == '3':
    result = num1 * num2
    operation = "*"
elif choice == '4':
    if num2 == 0:
        print("❌ Cannot divide by zero.")
        exit()
    result = num1 / num2
    operation = "/"
else:
    print("❌ Invalid choice.")
    exit()

# Step 5: Show result
print(f"\n✅ Result: {num1} {operation} {num2} = {result}")

