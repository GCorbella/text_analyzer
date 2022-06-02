text = input("Please, enter your text: ")
text = text.upper()
letter1 = input("Please, introduce the first letter you want to search: ")[0]
letter1 = letter1.upper()
letter2 = input("Please, introduce the second letter you want to search: ")[0]
letter2 = letter2.upper()
letter3 = input("Please, introduce the third letter you want to search: ")[0]
letter3 = letter3.upper()

letter1count = text.count(letter1)
letter2count = text.count(letter2)
letter3count = text.count(letter3)

print(f"The first letter, {letter1} ,appears {letter1count} times.")
print(f"The second letter, {letter2} ,appears {letter2count} times.")
print(f"The third letter, {letter3} ,appears {letter3count} times.")

list_text = text.split()

print(f"This text have {len(list_text)} words.")

fword = list_text[0]
lword = list_text[-1]
fletter = list(fword)[0]
lletter = list(lword)[-1]

print(f"The first letter in the text is '{fletter}' and the last letter in the text is '{lletter}'")

list_text.reverse()
text_backwards = " ".join(list_text)

print(f"This is the text backwards:\n{text_backwards}")

s_python = "PYTHON" in text
dic = {True:"does",False:"doesn't"}

print(f"The word Python {dic[s_python]} appear in the text")