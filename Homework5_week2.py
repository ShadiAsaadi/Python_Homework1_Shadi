############### The fifth question ###############
phrase = "The Beautiful Mind"
seperated_phrase_list = list(phrase)
revised_seperated_phrase_list = []
for char in seperated_phrase_list:
 if char.isupper():
  char = char.lower()
  revised_seperated_phrase_list.append(char)
 else:
  char = char.upper()
  revised_seperated_phrase_list.append(char)
print("".join(revised_seperated_phrase_list))



