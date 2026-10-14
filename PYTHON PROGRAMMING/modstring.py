text=input("enter a string:")
if len(text)<3:
    mod_str=text
elif text.endswith("ing"):
    mod_str=text+"ly"
else:
    mod_str=text+"ing"
print("Modified string:",mod_str)
