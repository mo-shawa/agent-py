from functions.write_file import write_file

res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(res1)

res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(res2)

res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(res3)
