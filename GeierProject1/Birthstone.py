#Zachary Geier - Birthstone

monthNames = ['January', 'Febuary', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December']

birthstones = ['Garnet', 'Amethyst', 'Aquamarine',
               'Diamond', 'Emerald', 'Pearl',
               'Ruby', 'Peridot', 'Sapphire',
               'Opal', 'Topaz', 'Turquoise']

month = input("Input birth month: ")
monthNum = 0

#Gets index of month (zero-indexed)
for i in range(0,12):
    if monthNames[i] == month:
        monthNum = i

print("Your birthstone is", birthstones[monthNum])