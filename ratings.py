"""Restaurant rating lister."""
with open("scores.txt", 'r') as dic_list:

    file_reader = open(dic_list)

def restaurant_rating_file(file_reader):
    dictionary_file = {}
    for rate in file_reader.items():
        dictionary = rate.sort()
        dictionary_file.append(dictionary)
    return dictionary_file


print(restaurant_rating_file("V\scores.txt"))
# put your code here
