# given a mixed string sort the numvers to the beginnig and attach sorted letters.
class Solution:
    def sort_mixed(self,string:str)->str:
        numbers=[]
        strings=[]
        for i in range(len(string)):
            if  string[i].isnumeric():
                numbers.append(string[i])
            else:
                strings.append(string[i])
        return "".join(sorted(numbers))+"".join(sorted(strings))

ins=Solution()

print(ins.sort_mixed("skdghf23jk23jk32"))