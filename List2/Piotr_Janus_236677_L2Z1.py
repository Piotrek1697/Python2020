import sys

from List2.Piotr_Janus_236677_L2_tasks_utils import file_exists


def main(args):
    if len(args) == 1:  # When input is like: first,second,...
        args = args[0].split(",")
    if len(args) != 7:
        sys.exit("Input must have 7 elements, like:\n"
                 "First file - file name with extension\n"
                 "Second file - file name with extension\n"
                 "Switch - work with 'letters' or 'words'\n"
                 "Separators file - file name with extensions"
                 "Ignore tokens - True or False"
                 "*File to save - file name with extension *optional (if none, type: '-')"
                 "*N - gram length - *optional, default n = 1 (if none, type '-')")

    first_file = args[0]
    second_file = args[1]
    letters = True if args[2] == 'letters' else False
    separator_file = args[3]

    if args[4] in ('True', 'False'):
        ignore_separators = bool(args[4])
    else:
        sys.exit('Ignore token property must be True or False!')

    save_file = '' if args[5] == '-' else args[5]
    n = '1' if args[6] == '-' else args[6]
    try:
        n = int(n)
    except ValueError:
        sys.exit('Gram length must be integer number')

    if file_exists(first_file) and file_exists(second_file):
        with open(first_file, "r", encoding="utf8") as f:
            content_1 = split_file(f.readlines(), ' ')
        with open(second_file, "r", encoding="utf8") as f:
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

    if letters:
        gram1 = create_gram_letters(content_1, n)
        gram2 = create_gram_letters(content_2, n)
    else:
        gram1 = create_gram_words(content_1, n)
        gram2 = create_gram_words(content_2, n)

    sim = jaccard_similarity(gram1, gram2)
    print('Jaccard index: ', sim)

    if save_file != '':
        positions1 = position_in_file(first_file, intersection(gram1, gram2))
        save_positions(save_file, positions1)
        positions2 = position_in_file(second_file, intersection(gram1, gram2))
        save_positions(save_file, positions2)


def save_positions(file_name, positions):
    """
    Save position elements into file. If file doesn't exists creates new file, else append existing file

    Parameters
    ----------
    file_name : str
        Save file name
    positions : list[list,str]
        list that contains list of grams position and analyzed file name
    """
    if file_exists(file_name):
        file = open(file_name, 'a')
    else:
        file = open(file_name, 'w')
    file.write(f"\nGrams in {positions[1]}:\n")
    for pos in positions[0]:
        file.write(f"{pos[0]} - row: {pos[1]} column: {pos[2]}\n")
    file.close()


def position_in_file(file_name, intersection_list):
    """
    Load file and get position of grams in file

    Parameters
    ----------
    file_name : str
    intersection_list : list[str]
        list of grams that are common for two files

    Returns
    -------
    list[list,str]
        list that contains list of grams position and analyzed file name
    """
    with open(file_name, 'r', encoding="utf8") as f:
        content = [line.lower() for line in f.readlines()]

    return [get_grams_position(content, intersection_list), file_name]


def get_grams_position(content, intersection_list):
    """
    Get position of grams in intersection list. Every position has row and column.

    Parameters
    ----------
    content : list[str]
        content of file, every element of list represents file line
    intersection_list : list[string]
        list of grams that are common for two files

    Returns
    -------
    list
        Every element of list is [gram, row_number, column_number]
    """
    list_of_index = []
    row = 0
    for line in content:
        for gram in intersection_list:
            column = line.find(gram)
            if column != -1:
                list_of_index.append([gram, row, column])
        if '\n' in line:
            row += 1
    return list_of_index


def create_gram_words(content, n):
    """
        Creates n - gram with letters
        Parameters
        -----------
        content : list[str]
        n : int

        Returns
        ---------
        list
            list of n-grams with no empty elements
        """
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
    Creates n - gram with letters

    Parameters
    -----------
    content : list[str]
    n : int

    Returns
    ---------
    list[str]
        list of n-grams with no empty elements
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
    """
    Check if input string is word

    Parameters
    -----------
    string : str - string  that has some characters

    Returns
    -------
    bool
        boolean that represents answer if input is word
    """
    return any(c.isalpha() for c in string)


def remove_separators(content, separators):
    """
    Remove

    Parameters
    -----------
    content : list[str]
    separators : list[str]

    Returns
    -------
    list[str]
        list of content without specific separators
    """
    for i in range(0, len(content)):
        for s in separators:
            if s == content[i]:
                content[i] = ''
            elif s in content[i] and not is_from_alphabet(s):
                content[i] = content[i].replace(s, '')

    return remove_empty_elements(content)


def remove_empty_elements(content):
    """
    Remove empty elements from content list. Empty element is like ''

    Parameters
    ----------
    content : list[str]

    Returns
    -------
    list[str]
        List with non empty elements
    """
    return list(filter(None, content))


def split_file(content, separator):
    """
    Parse file content into array of words

    Remove all '\n' and then split every element of list with separator

    Parameters
    ----------
    content : List[str]
        Content of file. Every element of list represents line of file
    separator :
        Separator that separate words

    Returns
    -------
    list
        List of words from file content. Every element represents separated word
    """
    word_list = []
    content = [line.replace('\n', '') for line in content]  # Remove \n from all strings
    [word_list.append(s.lower()) for line in content for s in line.split(separator)]  # If there is more then one line
    return word_list


def jaccard_similarity(content1, content2):
    """
    Calculates Jaccard index with equation: J(A,B) = |intersection(A,B)|/|union(A,B)|

    Parameters
    ----------
    content1 : list[str]
        Content with n-grams. Every string represents n-gram.
    content2 : list[str]
        Content with n-grams. Every string represents n-gram.
    """
    inter = intersection(content1, content2)
    if len(content1) == 0 and len(content2) == 0:
        return 1
    else:
        return len(inter) / (len(content1 + content2) - len(inter))


def intersection(list1, list2):
    """
    Intersection of two lists, with repetitions.

    Parameters
    ----------
    list1 : list[str]
        List with string elements
    list2 : list[str]
        List with string elements

    Returns
    -------
    list[str]
    """
    if len(list1) < len(list2):
        return [value for value in list1 if value in list2]
    else:
        return [value for value in list2 if value in list1]


if __name__ == '__main__':
    main(sys.argv[1:])
