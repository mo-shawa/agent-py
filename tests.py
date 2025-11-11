from functions.run_python_file import run_python_file

# Test 1: Run calculator without args (should print usage instructions)
res1 = run_python_file("calculator", "main.py")
print("Test 1 - Run calculator without args:")
print(res1)
print("\n" + "="*80 + "\n")

# Test 2: Run calculator with args (should run calculation)
res2 = run_python_file("calculator", "main.py", ["3 + 5"])
print("Test 2 - Run calculator with '3 + 5':")
print(res2)
print("\n" + "="*80 + "\n")

# Test 3: Run calculator tests
res3 = run_python_file("calculator", "tests.py")
print("Test 3 - Run calculator tests:")
print(res3)
print("\n" + "="*80 + "\n")

# Test 4: Try to run file outside working directory (should error)
res4 = run_python_file("calculator", "../main.py")
print("Test 4 - Try to run '../main.py' (should error):")
print(res4)
print("\n" + "="*80 + "\n")

# Test 5: Try to run nonexistent file (should error)
res5 = run_python_file("calculator", "nonexistent.py")
print("Test 5 - Try to run 'nonexistent.py' (should error):")
print(res5)
print("\n" + "="*80 + "\n")

# Test 6: Try to run non-Python file (should error)
res6 = run_python_file("calculator", "lorem.txt")
print("Test 6 - Try to run 'lorem.txt' (should error):")
print(res6)
