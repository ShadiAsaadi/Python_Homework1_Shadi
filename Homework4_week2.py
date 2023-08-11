############### The fourth question ###############
my_list1 = list(set(input("Please enter first list: ")))
my_list2 = list(set(input("Please enter second list: ")))
merge_differences_elements=[]
def difference_Lists(my_list1,my_list2):
 for i in my_list1:
  if i not in my_list2:
   merge_differences_elements.append(i)  
 for j in my_list2:
  if j not in my_list1:
   merge_differences_elements.append(j) 
difference_Lists(my_list1,my_list2)   
print("Merging the differences of two lists:",merge_differences_elements)