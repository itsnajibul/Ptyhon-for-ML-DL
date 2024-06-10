string1 = 'LearningStringInPython'

#string methods:
print('initial string: ',string1)
print('first character of the string is: ',string1[0])
print('last character of the string is: ',string1[-1])

print('slicing character from 8th index to 20th index: ',string1[8:21])
                                                            #string_val[m:n+1] //here m and n are indexes
print('slicing character from' + '8th index to 2nd last character: ',string1[8:-2])
print('reading from 8th characters: ',string1[8:])

print(string1.find('Py')) #output = 16 means 'Py' start from 16th index

#string1 has multiple 'i' in it
print('find between 1-8th index: ',string1.find('i',1,9))

#split_function:
string2= 'Learning String In Python'
print(string2.split()) #it splited where the spaces between

print('replace In-With: ',string1.replace('In','With'))

#reversed:
print("reversing string: ",string1[::-1])