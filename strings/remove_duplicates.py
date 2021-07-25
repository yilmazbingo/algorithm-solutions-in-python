class Solution:
    # this will not return in order
    def remove_with_set(self,input:str)->str:
        if len(input)==0:
            return "Please enter a valid input"
        store=set()
        for i in range(len(input)):
            store.add(input[i])
        return "".join(store)
    def remove_with_dict(self,input:str)->str:
        if len(input)==0:
            return "Please enter a valid input"
        store={}
        new_string=""
        for i in range(len(input)):
            if input[i] in store:
                store[input[i]]+=1
            else:
                store[input[i]]=1
        for key in store:
            new_string+=key
        return new_string

s=Solution()

print(s.remove_with_set("dadadasd"))
print(s.remove_with_dict("dadadasd"))



