import sys
import re
from collections import Counter

from List2.Piotr_Janus_236677_L2_tasks_utils import file_exists


def main(args):
    first_file = "catProtein.fasta"
    second_file = "catProtein2.fasta"
    separator_file = "separators.txt"

    ignore_separators = True
    letters = False

    if file_exists(first_file) and file_exists(second_file):
        with open(first_file, "r") as f:
            content_1 = split_file(f.readlines(), ' ')
        with open(second_file, "r") as f:
            content_2 = split_file(f.readlines(), ' ')
    else:
        sys.exit("Such files doesn\'t exist.")

    if file_exists(separator_file):
        with open(separator_file, "r") as f:
            separators = split_file(f.readlines(), ' ')
    else:
        sys.exit(separator_file + " Such file doesn\'t exist.")

    if ignore_separators:
        content_1 = remove_separators(content_1, separators)
        content_2 = remove_separators(content_2, separators)

    gram1 = create_gram_letters(content_1, 8)
    print(gram1)
    gram2 = create_gram_letters(content_2, 8)
    print(gram2)

    sim = jaccard_similarity(gram1, gram2)
    print(sim)


def create_gram_words(content, n):
    gram_list = []
    for i in range(0, len(content)):
        gram = ''
        for j in range(i, i + n):
            if j < len(content):
                gram += content[j] + ' '
            else:
                gram = ''

        gram_list.append(gram.rstrip())
    return remove_empty_elements(gram_list)


def create_gram_letters(content, n):
    """
    Parameters
    -----------
    content : list[string]
    """
    gram_list = []
    for word in content:
        for i in range(0, len(word)):
            gram = ''
            for j in range(i, i + n):
                if j < len(word):
                    gram += word[j]
                else:
                    gram = ''
            gram_list.append(gram)
    return remove_empty_elements(gram_list)


def is_from_alphabet(string):
    return any(c.isalpha() for c in string)


def remove_separators(content, separators):
    """
    Parameters
    -----------
    content : list[string]
    separators : list[string]
    """
    for i in range(0, len(content)):
        for s in separators:
            if s == content[i]:
                content[i] = ''
            elif s in content[i] and not is_from_alphabet(s):
                content[i] = content[i].replace(s, '')

    return remove_empty_elements(content)


def remove_empty_elements(content):
    return list(filter(None, content))


def split_file(content, separator):
    word_list = []
    content = [line.replace('\n', '') for line in content]  # Remove \n from all strings
    [word_list.append(s.lower()) for line in content for s in line.split(separator)]  # If there is more then one line
    return word_list


def jaccard_similarity(content1, content2):
    if len(content1) < len(content2):
        inter = intersection(content1, content2)
    else:
        inter = intersection(content2, content1)

    if len(content1) == 0 and len(content2) == 0:
        return 1
    else:
        return len(inter) / (len(content1 + content2) - len(inter))


def intersection(list1, list2):
    return [value for value in list1 if value in list2]


if __name__ == '__main__':
    main(sys.argv[1:])
