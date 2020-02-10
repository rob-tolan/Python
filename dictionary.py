# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:41:19 2020

@author: Owner
"""

#photo dictionary from Gallic's course
photo = {}
print(type(photo))
## <class 'dict'>
my_dict = { "id": "1",
  "description": "A Photo of the Old Port of Marseille.",
  "loc": "5.3772133, 43.302424",
}
print(my_dict)
my_dict["user"] = "Bob"
print(my_dict)
print(my_dict["description"])
second_dict = {"user": "5.3692712, 43.2949627"}
print(second_dict)
my_dict.update(second_dict)
print(my_dict)

