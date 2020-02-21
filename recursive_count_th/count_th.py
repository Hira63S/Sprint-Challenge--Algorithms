'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    sub = "th"                  # the sub string, technically it should be pass into the function as an attribute
    len_word = len(word)        # find the length of both the word and string for base cases
    len_sub = len(sub)
    # let's set the base case i.e.
    if len(word) == 0 and len_word < len_sub:     # simplest base case that if the length of the word is less than the string,
        return 0                                  # we return 0

    if word[0:len_sub] == sub:                   # if we go through the word were in word, we have the string present
        return count_th(word[len_sub-1:]) + 1    # we do the recursive call to the function until it reaches the base case
                                                # and then, as we find one instance, we add 1 and if we find another one, we add another
    return count_th(word[len_sub-1:])           # we can only go -1 because of the lenght of the substring. If we have a bigger substring,
                                                # we have to do negative 2, otherwise it won't iterate through the whole word and would only print the first instance
                                                # of the substring

word = "thethemthem"
print(word[0:2])
print(count_th(word))
