#READ FROM FILE: Excercise 22 from practicepython.org

darth = 0
luke = 0
lea = 0


with open('/Users/arul.sethi/Desktop/nameslist.txt', 'r') as open_file:
    line = open_file.readline()
    while line: 
        if 'Darth' in line:
            darth += 1
        elif 'Luke' in line:
            luke += 1
        elif 'Lea' in line: 
            lea += 1
        line = open_file.readline()

print(f"Darth: {darth}\nLuke: {luke}\nRea: {lea}")

