from functions.run_python import run_python_file

test_case1 = run_python_file("calculator", "main.py")
print(test_case1)

test_case2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(test_case2)

test_case3 = run_python_file("calculator", "tests.py")
print(test_case3)

test_case4 = run_python_file("calculator", "../main.py")
print(test_case4)

test_case5 = run_python_file("calculator", "nonexistent.py")
print(test_case5)

test_case6 = run_python_file("calculator", "lorem.txt")
print(test_case6)

