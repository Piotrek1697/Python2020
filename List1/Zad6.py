"""Similar words finder

This script allows user to find similar words from two chosen text files
"""

import sys
from List1.tasks_utils import file_exists


def main(args):
    input_files = args

    if len(input_files) == 1:  # When input is like: fileName1.txt,fileName2.txt
        input_files = input_files[0].split(",")
    if len(input_files) != 2:
        sys.exit("Input must have 2 file names")

    first_file = input_files[0]
    second_file = input_files[1]
    if file_exists(first_file) and file_exists(second_file):

        with open(first_file, "r") as f:
            content_1 = f.readlines()
        with open(second_file, "r") as f:
            content_2 = f.readlines()

        words_list_1 = get_words(content_1, get_separator(content_1))
        words_list_2 = get_words(content_2, get_separator(content_2))

        same_words = get_same_elements(words_list_1, words_list_2)
        same_words = sorted(same_words)

        pretty_print(same_words)
    else:
        sys.exit("Such files doesn\'t exist.")


def get_words(file_content, separator):
    """Parse file content into array of words

    Remove all '\n' and then split every element of list with separator

    Parameters
    ----------
    file_content : List[str]
        Content of file. Every element of list represents line of file
    separator :
        Separator that separate words

    Returns
    -------
    list
         List of words from file content. Every element represents separated word
    """
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
    """Find the most often used separator in text

    This function is looking for the often used separator in file content.
    Base separators (' ', '\t', '\n') was defined in function body and they are used to searching

    Parameters
    ----------
    file_content : List[str]
        Content from opened file. Words separated with one of base separators

    Returns
    -------
    str
        One of separator
    """
    separators = [' ', '\t', '\n']
    separator_dict = {}
    for line in file_content:
        separator_dict.update({s: line.count(s) for s in separators})

    return max(separator_dict, key=separator_dict.get)  # key=lambda k: separator_dict.get(k)


def get_same_elements(*words_list):
    """Finds same elements from several lists

    Parameters
    ----------
    *words_list : list
        Variable length argument. Single argument is list with words

    Returns
    -------
    list
        List of similar words
    """
    return list(set(words_list[0]).intersection(*words_list))


def pretty_print(words_list):
    """Print and enumerate similar words.

    This function distinguish if input list is empty and displays appropriate message

    Parameters
    ----------
    words_list : list
        List of similar words
    """
    if len(words_list) > 0:
        print('Similar words in files: ')
        for number, letter in enumerate(words_list):
            print(f'{number + 1}.', letter)
    else:
        print('There are no similar words in files')


if __name__ == '__main__':
    main(sys.argv[1:])
