from functions.get_files_info import get_files_info

current_dir_res = get_files_info("calculator", ".")
print(
    f"""
Result for current directory:
{current_dir_res}"""
)

pkg_res = get_files_info("calculator", "pkg")
print(
    f"""
Result for 'pkg' directory:
{pkg_res}"""
)

bin_res = get_files_info("calculator", "/bin")
print(
    f"""
Result for '/bin' directory:
{bin_res}"""
)

parent_dir_res = get_files_info("calculator", "../")
print(
    f"""
Result for '../' directory:
{parent_dir_res}"""
)
