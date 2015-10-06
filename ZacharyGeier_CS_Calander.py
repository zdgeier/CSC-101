#Calendar Project - Zachary Geier

again = 'y'

while again == 'y':
    days = eval(input("Number of days?: "))
    day_start = eval(input("Start day?(1-7): ")) - 1

    print("\n Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", sep='  ')
    print("-" * 35)

    print(format('  ', '>5s') * day_start, end = '')

    #Prints calendar numbers
    for index in range(day_start, days + day_start):
        if (index % 7 == 0):
            print()

        #Prints day 
        print(format(str(index - (day_start - 1)), '>4s'), end=' ')

    again = input("\n\nAgain?(y/n): ")