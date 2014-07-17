#this code works both with python 2 and python 3
import hashlib

#Change your group name here as given in the email.
groupname = "140 City Py - int 00:00"

hash_object = hashlib.md5(groupname.encode())
print("The self-enrollment key for group %s is:" % (groupname))
print(hash_object.hexdigest()[:8])
