list = [10, 20, 30, 40, 50]
print(" Question 1: ", list[2])

list2 = ['red', 'green', 'blue']
list2[2] = 'yellow'
print(" Question 2: ", list2)

list2.append('purple')
print(" Question 3: ", list2)

list3 = [1, 2, 3, 4, 5]
list3.remove(3)
print(" Question 4: ", list3)


name_list = ['Alice', 'Bob', 'Charlie']
name_length = []
for name in name_list:
    name_length.append(len(name))
print(" Question 5, the lengths are: ", name_length)

list_nums = [4, 1, 3, 9, 2]
list_nums.sort()
print(" Question 6: ", list_nums)

new_list = [22, 13, 4, 5, 3, 5, 6, 7, 8]
def even_numbers_in_list(new_list):
    even_list = []
    for numbers in new_list:
        if numbers % 2 == 0:
            even_list.append(numbers)
    return even_list

print(" Question 7: ", even_numbers_in_list(new_list))

a = [1, 2, 3]
b = [4, 5, 6]

new_list1 = a + b
print(" Question 8: ", new_list1)

aa = ["lamb", "kit", "yam", "kings", "dogs", "man"]
def strings_with_more_than_three_characters(aa):
    new_aa = []
    for character in aa:
        if len(character) > 3:
            new_aa.append(character)
    return new_aa
print(" Question 9: ", strings_with_more_than_three_characters(aa))






