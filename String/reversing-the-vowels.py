

def reverseVowels(sting):
	vowels=['a', 'e', 'i', 'o', 'u']
	temp=[]
	c=0
	res=[]
	for i in sting:
		if i in vowels:
			temp.append(i)
			c+=1
	for i in sting:
		if i in vowels:
			res.append(temp[c-1])
			c-=1
		else:
			res.append(i)
	print(" ".join(res))
			

def reverseVowelsEff(str):
	vowels=['a', 'e', 'i', 'o', 'u']
	i=0
	j=len(str)-1
	while i<j:
		if str[i] not in vowels:
			i+=1
			continue
		if str[j] not in vowels:
			j-=1
			continue
	
		str[i],str[j]=str[j],str[i]
		i+=1
		j-=1
	print(" ".join(str))


if __name__=='__main__':
	str="hello"
	reverseVowels(str)
	reverseVowelsEff(list(str))