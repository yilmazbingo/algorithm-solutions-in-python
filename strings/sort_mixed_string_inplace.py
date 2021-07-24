class Solution:
    def sort_mixed(self,string:str)->str:
        numbers = []
        strings = []
        new_string = ""

        for i in range(len(string)):
            if string[i].isnumeric():
                numbers.append(string[i])
                if strings:
                    sub_strings = "".join(sorted(strings))
                    new_string += sub_strings
                    strings = []
                if numbers and i == len(string) - 1:
                    sub_numbers = "".join(sorted(numbers))
                    new_string += sub_numbers
            else:
                strings.append(string[i])
                if numbers:
                    sub_numbers = "".join(sorted(numbers))
                    new_string += sub_numbers
                    numbers = []
                if strings and i == len(string) - 1:
                    sub_numbers = "".join(sorted(numbers))
                    new_string += sub_numbers
        return new_string
s=Solution()
print(s.sort_mixed("abcs14212sjkdsj")
)

