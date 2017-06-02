from collections import Counter
import numpy as np

def check_permutation_v1(str1, str2):
	if str1 is None or str2 is None:
		return None
	if len(str1) != len(str2):
		return None
	s1 = str1.lower()
	s2 = str1.lower()
	return Counter(s1) == Counter(s2)

def check_permutation_v2(str1, str2):
    if str1 is None or str2 is None:
			return False
    if len(str1) != len(str2):
			return False  
    s1 = str1.lower()
    s2 = str2.lower()
    unique_char = np.zeros(26,dtype=np.int)
    for char in s1:
    	unique_char[np.int(ord(char)-97)]+=1
    for char in s2:
    	unique_char[np.int(ord(char)-97)]-=1
    
	for x in unique_char:
	    if unique_char[x] != 0:
	        return False
    return True

def main():
	print check_permutation_v1("Test","SteT")
	print check_permutation_v2("aPple","test")
	
if __name__ == "__main__":
    	main()

