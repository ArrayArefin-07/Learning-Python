# Write all content of a given file into a new file by skipping line number 5
# See:
#
#
# Create a test.txt file and add the below content to it.
#
# Given test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7
# Expected Output: new_file.txt
#
# line1
# line2
# line3
# line4
# line6
# line7
#read test.text
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
