import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)

#read data is back in a dictionary variable now, just as if it was defined with:
#data1 = {'a': [1, 2.0, 3, 4+6j],
#         'b': ('string', u'Unicode string'),
#         'c': None}
data1['a'][0] += 10
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

#again data2 is valid list variable
data2[1] *= 2
pprint.pprint(data2)

pkl_file.close()
