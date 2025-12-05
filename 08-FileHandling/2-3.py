###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'
text = []

# read the content of the original file
with open(original_file, 'r') as file:
    content = file.read()
text.append(content)

# write the content to the target file (copy)
with open(target_file, 'w') as file:
    for line in text:
        file.write(line)