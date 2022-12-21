# capture multiple arguments into a single parameter
# The asterisk is called SPLAT operator.



def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	# output: Got one and ('two',)
varargs("one", "two", "three") # output: Got one and ('two', 'three')

# all the arguments that don't match a 
# required parameter are packed into a single tuple.

# Remember that a tuple is an iterable, just like a list.
#  That means if we want to
#  access 
# each of the arguments passed over individually, we can use a loop:
def varargs(arg1, *args):
    for blah in args:
        print(blah) #why it doesn't print one?
varargs("one", "two", "three") # output: two, three (on separate lines)

