def permute_a_palindrome(input):
    letters_odd = []
    for character in input:
        if character not in letters_odd:
            letters_odd.append(character)
        elif character in letters_odd:
            letters_odd.remove(character)

    return len(letters_odd) < 2


if __name__ == '__main__':
    assert permute_a_palindrome('a') == True
    assert permute_a_palindrome('aa') == True
    assert permute_a_palindrome('bbbaa') == True
    assert permute_a_palindrome('aaabc') == False
