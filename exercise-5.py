# ============================================================================
# TODO: Use a For Loop with a Range 

#Create a function called repeat. 
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================

def repeat(string, count):
    newString = ""
    for i in range(count):
        newString += string
    return newString

print(repeat("hi ", 3))