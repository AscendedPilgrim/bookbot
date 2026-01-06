def word_count(book_contents):
    word_list = book_contents.split()
    count = 0
    for each in word_list:
        count += 1
    
    return count

def character_count(book_contents):
    letter_db = {}
    for each in book_contents:
        letter = each.lower()
        if letter not in letter_db:
            letter_db[letter] = 1
        else:
            letter_db[letter] += 1

    return letter_db

def sort_on(e):
    return e["num"]


def sort_character_count(letter_db):
    list = []
    for each in letter_db:
        list_entry = {"char": each, "num": letter_db[each]}
        list.append(list_entry)

    list.sort(reverse=True, key=sort_on)
    return list
