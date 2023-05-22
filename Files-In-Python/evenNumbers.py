# filename = "even_numbers.txt": This line assigns the string value "even_numbers.txt"
# to the variable filename.
# This variable will be used later to specify the name of the file we want to create and write to.

filename = "even_numbers.txt"


# with open(filename, "w") as file::
# This line uses the open() function to open the file specified by filename in write mode ("w").
# The with statement ensures that the file is properly closed after writing, even if an exception occurs.
# The opened file is assigned to the variable file, which can be used to perform operations on the file.
with open(filename, "w") as file:
    # for number in range(0, 21, 2)::
    # This for loop iterates over a range of numbers from 0 to 20 (exclusive) with a step of 2.
    # This means it will generate even numbers from 0 to 20 (inclusive), as the step of 2 ensures only even numbers
    # are generated.

    for number in range(0, 21, 2):
        # file.write(str(number) + "\n"):
        # Inside the loop, the write() method of the file object is used to write each even number to the file. s
        # tr(number) converts the current number to a string, and "\n" appends a
        # newline character after each number. This ensures each number is written on a separate line in the file.

        file.write(str(number) + "\n")


# filename = "even_numbers.txt"
# with open(filename, "w") as file:

#     for number in range(0, 21, 2):
#         file.write(str(number) + "\n")
