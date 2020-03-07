import sys
import re


def main(args):
    input_word = ""
    file_name = args[0]
    while input_word != "quit" and input_word != "-q":
        input_word = input("Type word: ")
        c = vowel_counter(input_word)
        if file_exist(file_name):
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
    # sys.exit(0)


def word_exists_in_file(file_content, input_word):
    exists = False
    for line in file_content:
        reg = re.findall("[a-zA-Z]", line)
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


def file_exist(file_name):
    exists = True
    try:
        f = open(file_name, "r")
        f.close()
    except:
        exists = False
    return exists


if __name__ == '__main__':
    main(sys.argv[1:])
