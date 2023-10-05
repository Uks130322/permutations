def permutations_0(s, string="", result=None, first_time=True):
    
    if first_time:
        result = set()
        
    if len(s) <= 1:
        return [s]
    elif len(s) == 2:        
        result |= {string + s, string + s[::-1]}
    else:
        
        for letter in s:
            permutations_0(s.replace(letter, "", 1), string + letter, result, False)

    return list(result)

# print(permutations_0(""))
# print(permutations_0("ab"))
# print(len(permutations_0("abcdefgh")))


def move(string: str, index: int, ahead=True) -> str:
    """If ahead is True, the letter by index steps ahead, else it steps back"""
    if ahead:
        return string[:index] + string[index + 1] + string[index] + string[index + 2:]
    else:
        return string[:index - 1] + string[index] + string[index - 1] + string[index + 1:]


def permutations(string: str) -> list[str]:
    
    if len(string) < 3:
        return list({string, string[::-1]})
    
    else:
        result = {string, }
        root = string[:3]
        suffix = string[3:]
        
        for i in range(3):
            letter = root[0]
            
            for j in range(2):
                root = root[:j] + root[j + 1] + letter + root[j + 2:]
                result |= {root + suffix, }
                
        if not suffix:
            
            return list(result)
        
        for k in range(3, len(string)):
            my_set = set()
            
            for word in result:
                root = word[:k + 1]
                suffix = word[k + 1:]
                letter = word[k]
                for m in range(len(root) - 1, 0, -1):
                    root = root[:m - 1] + letter + root[m - 1] + root[m + 1:]
                    my_set |= {root + suffix, }
            result |= my_set           

        return list(result)
        

print(permutations("ab"))
print(permutations("aabb"))
print(permutations("abcd"), len(permutations("abcd")))
# print(len(permutations("abcdefghij")))
print(permutations(""))


def permutations_2(s):
    """Solution from Codewars"""
    
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations_2(s[:i] + s[i+1:]))


print(len(permutations_2("abcdefghij")))
