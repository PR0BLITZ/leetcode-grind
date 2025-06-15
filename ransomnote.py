def canConstruct(self, ransomNote: str, magazine: str) -> bool:
  # letter - times 
  hash_table = {}
  
  for i in magazine: #creating a hash table for letter
      if i in hash_table: #add one for occurence
          hash_table[i] += 1
      else:
           hash_table[i] = 1
      
  for i in ransomNote:
      if i in hash_table and hash_table[i] != 0: # if in hash
          hash_table[i] -= 1
      else:
          return False
  return True
