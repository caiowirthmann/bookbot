dict_test = {'p': 6121,'r': 20818,'o': 25225, 'j': 504,'e': 46043,'c': 9243}

list_dict = []

def list_sort(dict):
    return dict['quantity']

for letter, quantity in dict_test.items():
    temp_dict =  {"letter" : letter, 'quantity' : quantity}
    list_dict.append(temp_dict)

list_dict.sort(reverse=True, key=list_sort)

print (list_dict)                                                       