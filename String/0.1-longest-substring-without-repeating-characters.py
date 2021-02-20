# https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0
# https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/
# hard need to study
# Python3 program to find and print longest 
# substring without repeating characters. 

# Function to find and print longest 
# substring without repeating characters. 

# same as *smallest-distant-window

'''
traverse string and store its last occurrence in a hash table

'''

def findLongestSubstring(string): 

	n = len(string) 
	
	# Hash Map to store last occurrence 
	# of each already visited character. 
	pos = {} 

	# starting point of current substring. 
	st = 0

	# maximum length substring without 
	# repeating characters. 
	maxlen = 0

	# starting index of maximum 
	# length substring. 
	start = 0

	

	# Last occurrence of first 
	# character is index 0 
	pos[string[0]] = 0

	for i in range(1, n): 

		# If this character is not present in hash, 
		# then this is first occurrence of this 
		# character, store this in hash. 
		if string[i] not in pos: 
			pos[string[i]] = i 

		else: 
			# If this character is present in hash then 
			# this character has previous occurrence, 
			# check if that occurrence is before or after 
			# starting point of current substring. 
			if pos[string[i]] >= st: 

				# find length of current substring and 
				# update maxlen and start accordingly. 
				currlen = i - st 
				if maxlen < currlen: 
					maxlen = currlen 
					start = st 

				# Next substring will start after the last 
				# occurrence of current character to avoid 
				# its repetition. 
				st = pos[string[i]] + 1
			
			# Update last occurrence of 
			# current character. 
			pos[string[i]] = i 
		
	# Compare length of last substring with maxlen 
	# and update maxlen and start accordingly. 
	if maxlen < i - st: 
		maxlen = i - st 
		start = st 
	
	# The required longest substring without 
	# repeating characters is from string[start] 
	# to string[start+maxlen-1]. 
	return string[start : start + maxlen] 

# Driver Code 
if __name__ == "__main__": 

	string = "EERGE"
	print(findLongestSubstring(string)) 

# This code is contributed by Rituraj Jain 


"""
0 1 2 3 4 5
G E E R G E

i=0,st=0, s=0, ml=0
pos{g:0}

i=1,st=0, s=0, ml=0
pos{g:0,e:1}

i=2
cl=2
ml=2
s=0
st=2
pos{g:0,e:2}

i=3,st=2, s=0, ml=2
pos{g:0,e:2,r:3}

i=4,st=2, s=0, ml=2
pos{g:4,e:2,r:3}

i=5,
cl=3
ml=3
s=2
st=5
pos{g:4,e:5,r:3}

str[2:5]
erg

n=len(str)
st=0
ml=0
start=0
pos={}
pos[str[0]]=0

for i in range(1, n):
  if pos[str[i]] not in pos:
    pos[str[i]]=i
  else
    if pos[str[i]]>=st:
      cl=i-st
      if ml<cl:
        ml = cl
        start = st
      st=pos[str[i]]+1
    pos[str[i]]=i
"""

