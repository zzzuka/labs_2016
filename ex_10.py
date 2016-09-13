s = input()
s1 = s[0:(s.find('h')+1)]
s2 = s[(s.find('h')+1):(s.rfind('h'))]
s3 = s[(s.rfind('h')):]

print(s1+s2.replace('h','H')+s3)