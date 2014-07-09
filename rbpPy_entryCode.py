# Get the ASCII number of a character
secret = []
for char in "www.bit.ly/rbp_mc_faq":
  number = ord(char)
  secret.append(number)

print secret
#secret = [119, 119, 119, 46, 98, 105, 116, 46, 108, 121, 47, 114, 98, 112, 95, 109, 99, 95, 102, 97, 113]

# Get the character given by an ASCII number
message = ""
for i in secret:
  char = chr(i) 
  message += char

print message
