import sys
from List2.Piotr_Janus_236677_L2_tasks_utils import file_exists


def main(args):
    first_file = "test_file1.txt"
    second_file = "test_file2.txt"
    if file_exists(first_file) and file_exists(second_file):
        with open(first_file, "r") as f:
            content_1 = f.readlines()
        with open(second_file, "r") as f:
            content_2 = f.readlines()
    else:
        sys.exit("Such files doesn\'t exist.")

    content_1 = split_file(content_1, ' ')
    content_2 = split_file(content_2, ' ')

    sim = jaccard_similarity(content_1, content_2)
    
    print(sim)
    print(content_1)


def split_file(content, separator):
    word_list = []
    content = [line.replace('\n', '') for line in content]  # Remove \n from all strings
    if separator == ' ' or separator == '\t':
        [word_list.append(s.lower()) for line in content for s in
         line.split(separator)]  # If there is more then one line
    return word_list


def jaccard_similarity(content1, content2):
    set1 = set(content1)
    set2 = set(content2)
    return len(set1.intersection(set2)) / len(set1.union(set2))


if __name__ == '__main__':
    main(sys.argv[1:])
