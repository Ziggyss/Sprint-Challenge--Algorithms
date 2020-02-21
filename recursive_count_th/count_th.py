'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1:   #Base case
        return 0
    elif word[0] == "t" and word[1] == "h": 
        word = word[2:]
        return 1 + count_th(word)  # If the letters are found - remove them and                              add 1 to the return value
    else:
        word = word[1:]            # If "t" is not found, remove that letter                                 and continue checking from the next one
        return count_th(word)


    
  
