# print statements 
def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2, 4, 10, 16] 5
# >>>2
# >>>[2, 4, 10, 16]
# >>>4
# >>>[2, 4, 10, 16]
# >>>10
# >>>[2, 4, 10, 16]
# >>>16
# >>>[2, 4, 10, 16]

# Learning to search effectively is a skill that's built over time. Don't forget to always specify the programming language you're working with. Over time Google will learn that you're a developer, but until then, you may even have to specify that you're looking for information on the Python programming language, not trying to purchase a pet snake
# Aha! Here's some unexpected output. Now we know how to use print statements to find out where a problem is occurring. Once we've discovered that, we can make an educated guess as to what we should be searching. Formulating a good search is a skill best learned by trial and error. Try searching "unable to modify list value in for loop python"
# Learning to use print statements to their greatest advantage and how to correctly search for answers are not one-time skills.

