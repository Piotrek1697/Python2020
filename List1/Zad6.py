import sys
import re


def main(args):
    first_file = "first_file.txt"
    second_file = "second_file.txt"

    with open(first_file, "r") as f:
        content_1 = f.readlines()
    with open(second_file, "r") as f:
        content_2 = f.readlines()

    words_list_1 = get_words(content_1, get_separator(content_1))
    words_list_2 = get_words(content_2, get_separator(content_2))

    same_words = get_same_elements(words_list_1, words_list_2)
    same_words = sorted(same_words)

    print(same_words)


def get_words(file_content, separator):
    word_list = []
    if not file_content and isinstance(file_content, list) and all(isinstance(e, str) for e in file_content):
        sys.exit("File content must be non empty list with strings")
    file_content = [line.replace('\n', '') for line in file_content]  # Remove \n from all strings

    if separator == ' ' or separator == '\t':
        [word_list.append(s.lower()) for line in file_content for s in
         line.split(separator)]  # If there is more then one line
    else:
        word_list = file_content

    return word_list


def get_separator(file_content):
    separators = [' ', '\t', '\n']
    separator_dict = {}
    for line in file_content:
        separator_dict.update({s: line.count(s) for s in separators})

    return max(separator_dict, key=separator_dict.get)  # key=lambda k: separator_dict.get(k)


def get_same_elements(words_list_1, words_list_2):
    return list(set(words_list_1).intersection(set(words_list_2)))


if __name__ == '__main__':
    main(sys.argv[1:])
