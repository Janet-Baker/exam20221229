if __name__ == '__main__':
    dateStr = input("Enter a date (mm/dd/yyyy):")

    month = int(dateStr[0:2])
    monthLookup = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    print("The converted date is:", end='')
    print(monthLookup[(month - 1)], end=' ')
    print(dateStr[3:5], end=',')
    print(dateStr[6:])
