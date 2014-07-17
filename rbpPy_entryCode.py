import hashlib

groupname = "140 City Py - int 00:00"

# Assumes the default UTF-8
hash_object = hashlib.md5(groupname.encode())
print("The self-enrollment key for group %s is:" % (groupname))
print(hash_object.hexdigest()[:8])
