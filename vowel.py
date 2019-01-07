list1=["a","e","i","o","u"]
st=input()
if st in list1:
	print("Vowel")
elif st.isalpha():
	print("Consonant")
else:	
	print("Invalid")
