import re

text = "Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321."
pattern1 = "\w+\s\d+,\s\d+"
pattern2 = "\d+-\d+-\d+"
pattern3 = "\d+,\d+"
pattern4 = "\s(\d+)\s"

print(re.findall(pattern1, text))
print(re.findall(pattern2, text))
print(re.findall(pattern3, text))
print(re.findall(pattern4, text))