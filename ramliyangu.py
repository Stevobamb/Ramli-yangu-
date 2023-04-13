# Assigning values to each letter
values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 20, 
    'L': 30, 'M': 40, 'N': 50, 'O': 60, 'P': 70, 'Q': 80, 'R': 90, 'S': 100, 'T': 200, 'U': 300, 
    'V': 400, 'W': 500, 'X': 600, 'Y': 700, 'Z': 800
}

# Assigning daily values to each day
daily_values = {
    'Sunday': 13, 'Monday': 611, 'Tuesday': 1033, 'Wednesday': 275, 'Thursday': 710, 'Friday': 118, 'Saturday': 462
}

# Assigning colors to remainders
colors = {
    1: 'Matatizo ya kiJini', 2: 'Husda umefanyiwa na mwanamke', 3: 'Nuksi kali sana', 4: 'Kuna mwanamke umekutana nae kimwili', 5: 'Jini wa kiume ndo anakuchafua', 6: 'upepo wa kitabia, balaa na vifungo', 7: 'Asili yako imefunikwa',
    8: 'nyota ipo salama ila una nuksi', 9: 'nyota imechafuliwa', 10: 'uchawi wa kibinaadamu', 11: 'jini wa kike ndie anakutia matatizo', 12: 'una uadui mwingi sana'
}

# Getting user input
name = input("Enter a name: ")
day = input("Enter a day: ")

# Computing name value
name_value = sum(values.get(char, 0) for char in name.upper())

# Adding daily value to name value
name_value += daily_values.get(day.title(), 0)

# Computing remainder and color
remainder = name_value % 12
color = colors.get(remainder)

# Printing result
print(f"Uzito wa Jina lako ni {name_value} Na chanzo cha matatizo yako ni {color}")
