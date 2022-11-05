class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_grams={}
        result=[]
        
        for str in strs:
            hash_gram_key = "".join(sorted(str))
            print(hash_gram_key)
            if hash_gram_key not in hash_grams:
                hash_grams[hash_gram_key] =[str]
            else:
                hash_grams[hash_gram_key].append(str)
        
        return hash_grams.values()
            
            
