asa = '123,654,678,987,089,123'
cleaned_number = ''
for i in asa:
    if i in '0123456789':
        cleaned_number = cleaned_number + i

print(cleaned_number)