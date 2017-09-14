#Function to linearly search through a list of elements
def linear_search(unsorted_list, elem):

    if unsorted_list == None or elem == None:
        return None

    else:
        list_len = len(unsorted_list)

        if list_len == 0:
            return -1

        i = 0
        
        while (i < list_len):

            if unsorted_list[i] == elem:
                return i

            i += 1

        return -1

#Funtion to implement binary search through list of elements
def binary_search(unsorted_list, elem):

    #print("List inbound: " + str(unsorted_list))

    if unsorted_list == None or elem == None:
        return None

    else:
        sorted_list = sorted(unsorted_list)
        
        list_len = len(unsorted_list)

        if list_len == 0:
            return -1

        mid_index = list_len//2
        #print("Mid index: " + str(mid_index))

        if elem == sorted_list[mid_index]:
            return mid_index

        elif elem < sorted_list[mid_index]:
            #print("Checking left-side")
            return binary_search(sorted_list[0:mid_index],elem)

        else:
            #print("Checking right-side")
            return len(sorted_list[mid_index+1:]) + 1 + binary_search(sorted_list[mid_index+1:],elem)

#Testing ...
print(linear_search([1,2,3,4,5],3))
print(binary_search([1,2,3,4,5],3))
print(linear_search([1,2,3],0))
print(binary_search([1,2,3],0))
print(linear_search([],3))
print(binary_search([],3))
print(linear_search(None,4))
print(binary_search(None,4))
print(linear_search([31,32],None))
print(binary_search([31,32],None))

#Extra tests for binary search
print(binary_search([1,2,3,4,11,15],3))
print(binary_search([1,2,3,4,11],4))
print(binary_search([1,2,3,4,11],2))

#Function to implement sorting grouped lists by list number
def sort_coupled_lists(nested_lists,list_index):

    #Eg. there are 3 lists, we want to sort all the lists by the 3rd list
    # and return list of tuples

    #Avoid input shennanigans
    if len(nested_lists) == 0 or list_index >= len(nested_lists) or list_index < 0:
        return -1

    #Otherwise, first zip all the lists
    zipped_lists = list(zip(*nested_lists))

    #Then sort by index
    sorted_lists = sorted(zipped_lists, key = lambda x: x[list_index])

    return sorted_lists

#Test ...
a = [5,4,3,2,1]
b = [5,3,1,2,4]
c = [1,5,3,4,2]
print(sort_coupled_lists([a,b,c],0))
print(sort_coupled_lists([a,b,c],1))
print(sort_coupled_lists([a,b,c],2))
print(sort_coupled_lists([a,b,c],3))
        



    

    
    
