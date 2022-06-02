text = input("Please, enter your text: ")
text = text.upper()
letter1 = input("Please, introduce the first letter you want to search: ")
letter1 = letter1.upper()
letter2 = input("Please, introduce the second letter you want to search: ")
letter2 = letter2.upper()
letter3 = input("Please, introduce the third letter you want to search: ")
letter3 = letter3.upper()
letterlist = [letter1,letter2,letter3]

letter1count = text.count(letter1)
letter2count = text.count(letter2)
letter3count = text.count(letter3)

print(f"The first letter, {letter1} ,appears {letter1count} times.")
print(f"The second letter, {letter2} ,appears {letter2count} times.")
print(f"The third letter, {letter3} ,appears {letter3count} times.")

list_text = text.split()
list_text = list(list_text)
n_words = len(list_text)

print(f"This text have {n_words} words.")