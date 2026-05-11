from config import MAX_CHARS
from functions.get_file_content import get_file_content

lorem_test = get_file_content("calculator", "lorem.txt")

print(len(lorem_test))

if len(lorem_test) > MAX_CHARS:
    truncated = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    print(truncated in lorem_test)

test_case1 = get_file_content("calculator", "main.py")
print(test_case1)

test_case2 = get_file_content("calculator", "pkg/calculator.py")
print(test_case2)

test_case3 = get_file_content("calculator", "/bin/cat")
print(test_case3)

test_case4 = get_file_content("calculator", "pkg/does_not_exist.py")
print(test_case4)