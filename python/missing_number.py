

# Find sum of all number, subtract from sum of all indices
# The result shows the missing number 
def find_missing_number_1(num_list):
    
    sum = 0
    for i in range(len(num_list)):
        num = num_list[i]
        #print (i, " value ", num)
        sum += i
        sum = sum - num
    
    print ("Missing number ", abs(sum))

# Using XOR mechanism
# XOR for all numbers in the list would result the missing number
def find_missing_number_2(num_list):
    
    xor = len(num_list)
    for i in range(len(num_list)):
        num = num_list[i]
        #print (i, " value ", num)
        xor = xor ^ i ^ num
    
    print ("Missing number ", xor)

if __name__ == "__main__":
    num_list = [1, 2, 5, 6, 0, 4]
    find_missing_number_1(num_list)
    find_missing_number_2(num_list)