list_a = [1, 2, 3]
print(f'Sebelum: {list_a}')

# edit data yang paling tengah
list_a[1] = 99
print(f'Sesudah: {list_a}')

print("==================================")
list_a = [1]
set_a = {1, 39}

print('[Sebelum]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')

list_a.append(10)
list_a.append(50)

set_a.add(50)
set_a.add(100)

print('[Sesudah]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')
