class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create an empty hash map 
        sol = {}
        #Iterate for the length of the list 
        for word in strs:
           #Check If the item is in the hash map
           key = tuple(sorted(word)) 
           if key in sol:
                #Add the string as another item on the list in the key-value pairs 
                sol[key].append(word)
           else:
                #set the value if it doesn't already exist
                sol[key] = [word]
        #return the completed hashmap
        return list(sol.values())