from Person import Person

def main():
    person_data = input("Enter First, Last, and Favorite Color: ")

    # Writes person_data to file
    file = open("PersonOutput.txt", 'a')
    file.write(person_data + '\n')
    file.close()

    # Reads lines from file
    file_r = open("PersonOutput.txt", 'r')
    people = []
    lines = file_r.readlines()

    # Gets people from each line, populates people array
    for line in lines:
        person_data = line
        person_data = person_data.strip()
        datalist = person_data.split(',')
        people.append(Person(datalist[0], datalist[1], datalist[2]))

    # Prints people list
    for person in people:
        print(person)

main()


