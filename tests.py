from functions.get_file_content import get_file_content


main_res = get_file_content("calculator", "main.py")
print(main_res)

calc_res = get_file_content("calculator", "pkg/calculator.py")
print(calc_res)

cat_res = get_file_content("calculator", "/bin/cat")
print(cat_res)

missing_res = get_file_content("calculator", "pkg/does_not_exist.py")
print(missing_res)
