############### The second question ###############
from collections import Counter
get_list = input("Please enter elements of your list:")
repeated_elements = Counter(get_list)
max_repeated_element_ = max(repeated_elements.values())
for key,value in repeated_elements.items():
 if value == max_repeated_element_:
  print("max of repeated element:", key)

