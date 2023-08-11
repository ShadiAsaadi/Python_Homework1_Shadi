############### The third question ###############
from collections import Counter
get_list = input("Please enter elements of your list:")
repeated_elements = Counter(get_list)
max_repeated_element_ = max(repeated_elements.values())
for key,value in repeated_elements.items():
 if value == 2:
  print("duplicate of repeated elements:", key)