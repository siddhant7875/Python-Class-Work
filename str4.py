#removing spaces from beginning and at the end

name="        siddhant       "
final_name=name.strip()
print("the final input is",final_name)

#removing left space and right space
lspace=name.lstrip()
print("the final input is",final_name)

rspace=name.lstrip()
print("the right space removed",rspace)

#str.replace(old, new): this method replaces all occurrences of the "old" substring
#with the "new" substring in the string

sentence = "I like apples, and I like pineapple."
new_sentence = sentence.replace("like","love")
print(new_sentence)
#"I love apples, and I love pineaaple"