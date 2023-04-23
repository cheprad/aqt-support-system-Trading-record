# text = "The quick brown fox jumps over the lazy dog"

# # Split the text into a list of words
# words = text.split()

# # Initialize counters for different types of words
# num_nouns = 0
# num_verbs = 0
# num_adjectives = 0
# num_other = 0

# # Loop through the words and count the occurrences of different types of words
# for word in words:
#     if word.endswith('s') or word.endswith('es'):
#         num_nouns += 1
#     elif word.endswith('ed') or word.endswith('ing'):
#         num_verbs += 1
#     elif word.endswith('ful') or word.endswith('ous'):
#         num_adjectives += 1
#     else:
#         num_other += 1

# # Print the counts for each type of word
# print("Nouns: ", num_# สร้าง Dictionary ชื่อตัวแปรเดิมและชื่อตัวแปรใหม่
variables = {'a': 'x', 'b': 'y', 'c': 'z'}

# สร้าง list ของตัวแปรเดิม
old_variables = list(variables.keys())

# เปลี่ยนชื่อตัวแปรตามลูป
for old_var in old_variables:
    new_var = variables[old_var]
    exec(f"{new_var} = {old_var}")
    del variables[old_var]

# ตัวอย่างการใช้งาน
a = 1
b = 2
c = 3

# แสดงค่าตัวแปรก่อนเปลี่ยนชื่อ
print(f"a = {a}, b = {b}, c = {c}")

# เรียกใช้งานการเปลี่ยนชื่อตัวแปร
variables = {'a': 'x', 'b': 'y', 'c': 'z'}

# เปลี่ยนชื่อตัวแปรตามลูป
for old_var in old_variables:
    new_var = variables[old_var]
    exec(f"{new_var} = {old_var}")
    del variables[old_var]

# แสดงค่าตัวแปรหลังเปลี่ยนชื่อ
print(f"x = {x}, y = {y}, z = {z}")nouns)
# print("Verbs: ", num_verbs)
# print("Adjectives: ", num_adjectives)
# print("Other: ", num_other)



# Define a string
my_string = "Hello, World!"

# Cut the string using slicing
substring = my_string[:-4]

# Print the substring
print(substring)