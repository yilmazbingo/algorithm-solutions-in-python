# given a string containing only paranthesis determine if it is valid. the string is valid if all parentheses close.

class Solution:
    def isValid(self, input: str) -> bool:
        # those are only parantheses that string will include
        parentheses = {"(": ")", "[": "]", "{": "}"}
        seen_left_brackets = []
        # if it is empty- "", it is valid
        if len(input) == 0:
            return True
        for i in range(len(input)):
            # we are checking if we see left paranthesis

            if input[i] in parentheses:
                seen_left_brackets.append(input[i])
            # I put this emptyArray.pop() returns IndexError in python. js returns undefined
            elif len(seen_left_brackets) == 0:
                return False
            else:
                last_of_left_brackets = seen_left_brackets.pop()
                correct_bracket = parentheses[last_of_left_brackets]
                if correct_bracket != input[i]:
                    return False
        return len(seen_left_brackets) == 0




