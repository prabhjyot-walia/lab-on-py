print('Creating and Modifying:'.upper())
dic = {'name': 'TV', 'age': 21}
dic['age'] = 22
dic['city'] = 'New Delhi'
print(dic)

print('\nAccessing and Removing Elements:'.upper())
print('Name:',dic.get('name'))
dic.pop('name')
print(dic)

print('\nIterating Through Dictionary Items:'.upper())
for key, value in dic.items():
    print(f"{key}: {value}")
print("THIS PROGRAM IS WRITTEN BY Prabhjyot :- 0221BCA065")