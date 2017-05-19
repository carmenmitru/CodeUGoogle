# -*- coding: utf-8 -*-
''' Given two strings, write a method to decide if one is a permutation of the other.
Example:
	
	Listen, Silent ⇒ True
	Triangle, Integral ⇒ True
	Apple, Pabble ⇒ False 
	
	First step is to determine the special cases
		1) s1 or s2 is null ⇒ False
		2) s1 and s2 are empty strings ⇒ True
		3) Length s1 != s2 ⇒ False
	
	Second step is to see if it is case sensitive

	In the first example :
		Listen  & Silent ⇒ True  that means that is not case sensitive but for computer 's' ! = 'S'

	So to eliminate this cases we should transform both strings to lowercase

	The first way to solve this problem is to sort this arrays and see if those arrays are equal

	Complexity :

		Time: O(n log n)
		Space : O (n)

	The second way to solve it's looping through all the letters of each string and count the frequency of each letter(HashMap)
	Key a : Value 1
	To do that first we have to transform both string to lowercase
	 Silent -> silent
	 Listen -> listen

	 s1) e i l n s t
	     1 1 1 1 1 1
	 s2) e i l n s t
	     1 1 1 1 1 1	
 	Then we can check if the arrays with frequncy are equal

 	Complexity: 
 	Time : O(n)
 	Space : O(n)
'''

# 

def check_permutation_v1(str1, str2):
    	if str1 is None or str2 is None:
    		return False
		if len(str1) != len(str2):
    		return False

		return sorted(str1) == sorted(str2)

def check_permutation_v1(str1, str2):
		if str1 is None or str2 is None:
    		return False
		if len(str1) != len(str2):
    		return False

    	for char in str1:
            unique_char1[char] += 1
    	for char in str2:
            unique_char1[char] += 1


def main():

	check_permutation("Listen", "Silent")
	check_permutation_v1("Triangle", "Integral")

if __name__ == "__main__":
    main()## with