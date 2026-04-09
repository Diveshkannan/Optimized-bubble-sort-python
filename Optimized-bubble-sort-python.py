def sort_list(y):
    length=len(y)
    for s in range(length-1):
            swapped=False
            r=0
            while r<(length-1)-s:
                  if y[r]>y[r+1]:
                       y[r],y[r+1]=y[r+1],y[r]
                       swapped=True
                  r+=1
            if not swapped:
                 break
    return y
def get_input(comment):
    list_input=[]
    print(comment)
    while True:
        n=int(input("Elements:"))
        list_input.append(n)
        check=input("Enter 'Y' to continue and 'N' to stop:")
        checking=check.upper()
        if checking=='Y':
            pass
        elif checking=='N':
            print("List created successfully")
            break
        else:
            print("Invalid command!")
    return list_input
print("List creation...")
List=get_input("Initializing list creation->Please enter numbers as follows!")
if len(List)>1:
    print("Sorting....")
    sort_the_list=sort_list(List)
    print("Sorted list:",sort_the_list)
else:
    print("A list with 1 element cannot be sorted!!!")

            
        
        
