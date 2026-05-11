from config import MAX_CHARS
from functions.write_file import write_file

test_case1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(test_case1)

test_case2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(test_case2)

test_case3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(test_case3)