from functions.get_files_info import get_files_info 

debug1 = get_files_info("calculator", ".")
print("Result for current directory:")
print(debug1)

debug2 = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(debug2)

debug3 = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(debug3)

debug4 = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(debug4)