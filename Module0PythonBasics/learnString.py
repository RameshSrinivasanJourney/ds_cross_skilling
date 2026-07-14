print("************")
print("Data Types:-")
print("************")
print("\nLearn String:-")
print("==============")

#String
first_name = "Ramesh"
last_name = "Srinivasan"
full_name = first_name + " " + last_name
full_name_length = len(full_name)
full_name_with_space = "   Ramesh Srinivasan   "

print("\nFirst Name : " + first_name)
print("Last Name : " + last_name)
print("Full Name : " + full_name)

#Concatenate String with Number shows Error: TypeError - convert number to string
print("length of Full Name : " + str(full_name_length))

print("\nCharacter Position Reference")
print("----------------------------")
print("String -  R a m e s h   S r i n  i  v  a  s  a  n")
print("Indexes - 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16")

print("\nString Indexing")
print("---------------")
print("First Character : ", full_name[0])
print("Second Character : ", full_name[1])
print("Last Character : ", full_name[-1])

print("\nString Slicing")
print("---------------")
#string[start:end] start is included.end is excluded.
print("Characters [0:3] : ", full_name[0:3])
#-1 means stop before the last character (n)
print("Characters [1:-1] : ", full_name[1:-1])
print("Characters [2:] : ", full_name[2:])
print("Characters [:3] : ", full_name[:3])
print("Complete String [:] : ", full_name[:])

print("\nString Reverse")
print("---------------")
print("Reverse string : ", full_name[::-1])

print("\nString Methods")
print("---------------")
print("Length of Full Name : ", len(full_name))
print("Index of 'Ramesh : ", full_name.index("Ramesh"))
print("Count of 'Ramesh : ", full_name.count("Ramesh"))

print("\nCase Conversion Methods")
print("-----------------------")
print("Upper Case : ", full_name.upper())
print("Lower Case : ", full_name.lower())
print("Title Case : ", full_name.title())
print("Capitalize First Letter : ", full_name.capitalize())
print("Swap Upper/Lower Case : ", full_name.swapcase())

print("\nWhitespace Handling")
print("--------------------")
print("without Strip :"+ full_name_with_space)
print("Strip Leading & Trailing Space :", full_name_with_space.strip())
print("Left Strip :", full_name_with_space.lstrip())
print("Right Strip :", full_name_with_space.rstrip())

print("\nSearch and Replace")
print("--------------------")
print("Replace 'Ramesh' with 'Ram' : ", full_name.replace('Ramesh', 'Ram'))
print("Find Position of 'Srinivasan' : ", full_name.find('Srinivasan'))

print("\nMembership Testing")
print("------------------")
print("Is 'Ra' present? : ", "Ra" in full_name)
print("Is 'asdf' present? : ", "asdf" in full_name)

print("==============")