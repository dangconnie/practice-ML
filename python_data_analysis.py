# -*- coding: utf-8 -*- 

# cipher = {'p': 'o', 'y': 'h', 't': 'n',
#           'h': 't', 'o': 'y', 'n': 'p'} 

# print(cipher['t'])
# prints n


# ========================================
# Use indexing with keys to access values
# ========================================

# def encrypt(cipher, word):
#     """encrypt word using cipher"""
#     encrypted = ""
#     for char in word:
#         encrypted += cipher[char]
#     return encrypted

# python = "python"
# enc = encrypt(cipher, python)
# print(python, enc)



# ========================================
# Use .get to check if key exists
# ========================================

# print(cipher.get('t')) #prints n
# print(cipher.get(1)) #prints None
# print(cipher.get(1, 'z')) #prints Z. If the Key 1 exists, print that value. If 1 doesn't exist, print Z.



# ========================================
# Check for keys in a dictionary
# ========================================
# mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
# print(1 in mapping) # True
# print(8 in mapping) # True

# # Values
# print(5 in mapping) #False
# print(-3 in mapping) #False

# # Both
# print(22 in mapping) #True

# # Neither
# print(82 in mapping) #False





# keys = [8, 14, 22, 25]
# for key in keys:
#     if key in mapping:
#         print(key, mapping[key])
#     else:
#         print("{} not in mapping".format(key))
#Prints: 
#(8, -3)
#14 not in mapping
#(22, 17)
#25 not in mapping



# =================================================
# Be careful with what data types you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
# =================================================

# mapping = {4.0: 2, 'a': 3, True: 'true', False: 9}
# print(mapping)

# mapping[1] = 7
# print(mapping) #{'a': 3, True: 7, 4.0: 2, False: 9}
# Python read 1 as a Boolean. As a result, it changed True to 7.

# mapping[0] = 'false'
# print(mapping) #{'a': 3, True: 'true', 4.0: 2, False: 'false'}
# Python read 0 as a Boolean. As a result, it changed False to 'false'.

# mapping[4] = 7
# print(mapping) #{'a': 3, True: 'true', 4.0: 7, False: 9}
# Updated value for 4.0

# mapping['A'] = 'abc'
# print(mapping) #{'a': 3, True: 'true', 4.0: 2, 'A': 'abc', False: 9}
# New mapping added




# =================================================
# Value lookup, iteration, order, update
# =================================================

# contacts = {'Isabella Intern': '1-111-111-1111',
#             'Johnny Junior': '2-222-222-222',
#             'Sam Senior': '3-333-333-3333'}
# print (contacts)
# print (contacts['Sam Senior'])



# Three example of dictionaries - note that dictionary keys in Python must be immutable
# simple_dict = {"Isabella" : 1, "Johnny" : 2, "Sam" : 3}
# print(simple_dict)

#bad_dict = {["Isabella, "Intern"] : 1, ["Johnny", "Junior"] : 2, ["Sam", "Senior"] : 3}
# print(bad_dict)

# good_dict = {("Isabella", "Intern") : 1, ("Johnny", "Junior") : 2, ("Sam", "Senior") : 3}
# print(good_dict)
#Use tuples b/c tuples are immutable

 
# =================================================
# +++++++++++++++++ Value lookup ++++++++++++++++++
# =================================================


# Examples of dictionary lookup
# print(simple_dict["Sam"])
# print(simple_dict["Isabella"])
# print(simple_dict["Erica"])
# print(good_dict[("Johnny", "Junior")])
# print(good_dict[("Sam", "Senior")])



# def lookup(contacts, name):
#     """
#     Lookup name in contacts and return phone number.
#     If name is not in contacts, return an empty string.
#     """
#     if name in contacts:
#         return (contacts[name])
#     else:
#         return ""



# def lookup(my_dict, my_key, default_value=None):
#     """
#     Given dictionary my_dict and key my_key, 
#     return my_dict[my_key] if my_key is in my_dict
#     otherwise return default_value
#     """
#     if my_key in my_dict:
#         return my_dict[my_key]
#     else:
#         return default_value

# simple_dict = {"Isabella" : 1, "Johnny" : 2, "Sam" : 3}
# print(lookup(simple_dict, "Isabella", -1)) # prints 1
# print(lookup(simple_dict, "Iris", -1)) # prints -1
# print(lookup(simple_dict, "Iris")) # prints None (defult value ommitted)

# You can give Python a default value to print out as an argument or as a parameter if conditions are not met 


# You can use get() in place of lookup(). With get(), if the key isn't in the dictionary, you wouldn't get an error.



# contacts = {'Isabella Intern': '1-111-111-1111',
#             'Johnny Junior': '2-222-222-222',
#             'Sam Senior': '3-333-333-3333'}

# def lookup(contacts, name):
#     """
#     Lookup name in contacts and return phone number.
#     If name is not in contacts, return an empty string.
#     """
#     if name in contacts:
#         return contacts[name]
#     else:
#         return ""

# print(lookup(contacts, "Isabella Intern"))




# =================================================
# +++++++++++++++++++++ GET +++++++++++++++++++++++
# =================================================

# def lookup2(contacts, name):
#     """
#     Lookup name in contacts and return phone number.
#     If name is not in contacts, return an empty string.
#     """
#     return contacts.get(name, "")
# print lookup2(contacts, "Sam Senior")





# =================================================
# +++++++++++++++++ Iteration +++++++++++++++++++++
# =================================================

# def print_contacts(contacts):
#     """
#     Print all the names of the contacts in our contacts list.
#     """
#     for name in contacts:
#         print(name)
# print (print_contacts(contacts))




# ***************************************************
# **************** ITEMS Method *********************
# ***************************************************

# To print out both the keys and values, we can use the 𝚒𝚝𝚎𝚖𝚜 method to iterate over key-value pairs:

contacts = {'Isabella Intern': '111-111-1111',
            'Johnny Junior': '222-222-222',
            'Sam Senior': '333-333-3333'}

# def print_contact_list(contacts):
#     """
#     Print the names and phone numbers of the contacts in
#     our contacts list.
#     """
#     for name, number in contacts.items():
#         print(name, ":", number)

# print(print_contact_list(contacts))




# =================================================
# +++++++++++++++++ Order +++++++++++++++++++++++++
# =================================================
# contacts = {'hsabella Intern': '111-111-1111',
#             'cohnny Junior': '222-222-222',
#             'pam Senior': '333-333-3333'}

# def print_ordered(contacts):
#     """
#     Print the names and phone numbers of the contacts
#     in our contacts list in alphabetical order.
#     """
#     keys = contacts.keys()
#     names = sorted(keys)
#     for name in names:
#         print(name, ":", contacts[name])
# print(print_ordered(contacts))

 # If you wanted to sort by last name, you would need to first split the name strings into first and last names and then sort by last names.


# =================================================
# +++++++++++++++++ Update ++++++++++++++++++++++++
# =================================================
def add_contact(contacts, name, number):
    """
    Add a new contact (name, number) to the contacts list.
    """
    if name in contacts:
        print(name, "is already in contacts list!")
    else:
        contacts[name] = number
print(add_contact(contacts, "Melissa", "999-999-999"))
        


def update_contact(contacts, name, newnumber):
    """
    Update an existing contact's number in the contacts list.
    """
    if name in contacts:
        contacts[name] = newnumber
    else:
        print(name, "is not in contacts list!")
print(add_contact(contacts, "Melissa", "999-999-999"))




# Refactor
def add_or_update_contact(contacts, name, number):
    """
    Add contact or update it if it is already in the contacts list.
    """
    contacts[name] = number
print(add_or_update_contact(contacts, "Melissa", "999-999-999"))
