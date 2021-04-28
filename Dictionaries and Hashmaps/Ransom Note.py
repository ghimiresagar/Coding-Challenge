if __name__ == '__main__':
    magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
    note = ['give', 'one', 'grand', 'today']

    # convert the magazine list into a hash map so we can keep the count of numbers and see if they exist in linear time
    # O(n)
    magazineHash = {}
    for x in magazine:
        # if exists increment the key/value
        if magazineHash.get(x):
            magazineHash[x] += 1
            continue
        # doesn't exist, create a new key/value
        magazineHash[x] = 1
    # we now have a magazineHash of the given magazine array
    # go over all the words in the note and see if we can match them
    # flag variable to see if hash was found
    flag = False
    for x in note:
        if magazineHash.get(x) and magazineHash[x] > 0:
            # word in note is present in the maganizeHash and is available
            magazineHash[x] -= 1
            continue
        else:
            flag = True
            break

    print("Yes") if not flag else print("No")
