def get_num_words(string):
    split_by_words = string.split()
    return len(split_by_words)


def get_char_counts(string):
    string = string.lower()

    result_dict = {}
    for char in string:
        if char in result_dict.keys():
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    
    return result_dict

def get_sorted_char_list(char_dict):
    char_list = []

    for key in char_dict.keys():
        char_list.append(   {
                                "char": key, 
                                "count": char_dict[key]    
                            }
                        )
    
    char_list.sort(reverse=True, key=lambda dct: dct["count"])

    return char_list

