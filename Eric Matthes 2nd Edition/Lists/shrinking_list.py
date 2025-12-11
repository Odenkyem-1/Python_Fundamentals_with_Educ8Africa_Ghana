guests = ['Mami', 'Abena', 'Odura', 'Nhyira', 'Clifford', 'Adwoa']

print("Sorry for the inconvince, only 2 people can be invited")

removed_guest_1 = guests.pop()
print(f'\nSorry Mrs. {removed_guest_1}, You are not invited to the dinner')

removed_guest_2 = guests.pop()
print(f'Sorry Mr. {removed_guest_2}, You are not invited to the dinner')

removed_guest_3 = guests.pop()
print(f'Sorry Mrs. {removed_guest_3}, You are not invited to the dinner')

removed_guest_4 = guests.pop()
print(f'Sorry Mrs. {removed_guest_4}, You are not invited to the dinner')

print(f'\nMrs. {guests[0]}, you are invited to dinner at my house')
print(f'Mrs. {guests[1]}, you are invited to dinner at my house')

del guests[0]
del guests[0]
print(guests)
