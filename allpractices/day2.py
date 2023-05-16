# my_house = {
#     'brand': 'mansion',
#     'rooms': 'large',
#     'area': 'langata'
# }

# # Set key, value using subscript operator []

# my_house['age_years'] = 5
# print(my_house)

# # In case the key is not present in dictionary KeyError is raised.
# # print(my_house['house_color'])


# # The values() method gets the values of the dictionary:

# house = {'brand': 'mansion', 'age_years':5}
# for value in house.values():
#     print(value)


#     # The keys() method gets the keys of the dictionary:

#  house = {'brand': 'mansion', 'age_years':5}
# # There is no need to use .keys() since by default you will loop through keys:
# for key in house:
#         print(key)


# # Using the keys(), values(), and items() methods, a for loop can iterate over
# # the keys, values, or key-value pairs in a dictionary, respectively.
# house = {'brand': 'mansion', 'age': 5}
# for key, value in house.items():
#     print(f'key: {key} Value: {value}')


#  # Run the following code in the python shell
# # by simply running python3
# Me = {'name': 'Morgan', 'age': 25}
# f'My name is {Me.get("name")}'

# f'My age is {Me.get("age")}'

# f'I am deeply in love with {Me.get("wife")}'

# # i can change the default value None to something of my choice

# f'I am deeply in love with {Me.get("wife", "MaryJane")}'

# # run in python shell
# house = {'brand': 'mansion', 'age_years':5}
# if 'has_pool' not in house:
#     house['has_pool'] = True
#     house

# # run in python shell
# # removing any item
# house = {'brand': 'mansion', 'age_years':5}
# house.pop('age')
# house

# # run in python shell
# # removes the last item in the list
# house = {'brand':'mansion', 'age_years':5}
# house.popitem()
# house

# # run in python shell
# # removes item based on a key
# house = {'brand': 'mansion', 'age_years':5}
# del house['brand']
# house


# # removes all items in the list
# house = {'brand': 'mansion', 'age_years':5}
# house.clear()
# house


# #checking keys in dictionary
# house = {'brand': 'mansion', 'age_years':5}
# 'brand' in house.keys()


# 'height' in house.keys()

# # You can omit keys()
# 'skin' in house


# # Checking values in the dictionary
# house = {'brand': 'mansion', 'age_years':5}
# 'brand' in house.values()
# 5 in house.values()

# # pretty printing
# import pprint
# house = {'brand': 'mansion', 'age_years':5}
# pprint.pprint(house)

# house_a = {'a': 1, 'b': 2}
# house_b = {'b': 3, 'c': 4}
# house_c = {**house_a, **house_b}
# house_c


library = {
    "1": {"author": "FaithK", "title": "How to win", "year": 2020, "ISBN": 100},
    "2": {"author": "Kym", "title": "How to Sleep", "year": 2023, "ISBN": 10032},
}

# author_removed = library["1"].pop("author")
# print(author_removed)
# print(library)


# # updating using the key
# library["2"]["title"] = "Mastering the Art of Sleep"

# print(library["2"])


# # Retrieving a book based on the author
# author = "FaithK"
# books_by_author = []

# for book_id, book_info in library.items():
#     if book_info["author"] == author:
#         books_by_author.append(book_info)

# print(books_by_author)

# Accessing the book based on the ISBN number
ISBN_number = 10032
book = None

for book_id, book_info in library.items():
    if book_info["ISBN"] == ISBN_number:
        book = book_info
        break

print(book)
