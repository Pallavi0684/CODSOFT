import random
import string

# Step 1: Ask user for password length
length = int(input("Enter desired password length: "))

# Step 2: Define character sets
letters = string.ascii_letters      # a-z + A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # Special characters like !@#$%

# Step 3: Combine all characters
all_chars = letters + digits + symbols

# Step 4: Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

# Step 5: Display the password
print("Generated Password:", password)









































