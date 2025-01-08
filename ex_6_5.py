str = "X-DSPAM-Confidence:    0.8475"
#desired output- 0.8475.. use find and string slicing
f =  str.find('0')
sl = str[f:]
print(float(sl))
