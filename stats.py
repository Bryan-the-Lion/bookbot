def count_words(book):
    word_list = book.split()
    
    return len(word_list), word_list

def count_char(list_words):
    letter_dict = {}

    for i in range(0, len(list_words)):
        
        for j in range(0, len(list_words[i])):
            char_extract = str(list_words[i][j]).lower()
            
            if char_extract in letter_dict and letter_dict[char_extract] >= 1:
                letter_dict[char_extract] += 1
            else:
                letter_dict[char_extract] = 1
    
    return letter_dict

def sort_dict(dictionary):
    list_dict = [{"char":k, "num":v} for k, v in dictionary.items()]
    list_dict.sort(reverse=True, key=lambda list_dict: list_dict["num"])

    return list_dict
