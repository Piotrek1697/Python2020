import sys
import re

from List1.Piotr_Janus_236677_L1_tasks_utils import file_exists


def main(args):
    input_word = ""
    file_name = args[0]
    while input_word != "quit" and input_word != "-q":
        input_word = input("Type word: ")
        if input_word != "quit" and input_word != "-q":
            c = vowel_counter(input_word)
            if file_exists(file_name):
                with open(file_name, "r") as f:
                    content = f.readlines()

                if word_exists_in_file(content, input_word):
                    print("This word already exists in file")
                else:
                    with open(file_name, "a") as f:
                        f.write(f'\n{input_word}\t{c}')

            else:
                with open(file_name, "w") as f:
                    f.write(f'{input_word}\t{c}')
    print("End")


def word_exists_in_file(file_content, input_word):
    exists = False
    for line in file_content:
        reg = re.findall("[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]", line)
        word = ''.join(reg)
        print(f'Parse word: {word}, input: {input_word}')
        exists = word == input_word
        if exists:
            break
    return exists


def vowel_counter(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó')
    word = word.lower()

    vowels_dict = {v: word.count(v) for v in vowels}
    count = sum(vowels_dict.values())
    return count


if __name__ == '__main__':
    main(sys.argv[1:])
