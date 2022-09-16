contacts_name = ['Gov' , 'Jov' , 'Cof' , 'Pov']
contacts_number = ['347-348' , '287-918' , '198-284' , '287-398']
print('Press 1 to search by name')
print('Press 2 to search by number')
answer = input()
if answer == '1':
  print('Search by name:')
  name_search = input()
  if name_search in contacts_name:
    position = contacts_name.index(name_search)
    print(contacts_number[position])
  else: 
    print('Contact not found. Enter a new name:')
    answer = input()
    contacts_name.append(answer)
    print('New contact number:')
    aNswer = input()
    contacts_number.append(aNswer)
    print(contacts_name)
    print(contacts_number)
elif answer == '2':
  print('Search by number:')
  number_search = input()
  if number_search in contacts_number:
    position = contacts_number.index(number_search)
    print(contacts_name[position])
  else: 
    print('Contact not found. Enter a new number:')
    answer = input()
    contacts_number.append(answer)
    print('New contact name:')
    aNswer = input()
    contacts_name.append(aNswer)
    print(contacts_name)
    print(contacts_number)


