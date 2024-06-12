#word_counter.py

import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"cannot find file: {file_path}")
        return None
    
def split_into_words(text):
    result = text.lower()
    print(result)
    result = re.sub(r"[^a-zA-Z|\w\'\w?]", " ", result)
    result = result.split()
    #words = re.sub(r"[^a-zA-Z]", " ", result)
    #print(words)

    return result

def count_word_frequencies(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def print_word_frequencies(word_frequencies):
    list_pair = list(word_frequencies.items()) #items() 호출 시 리스트로 변환
    ordered_list_pair = sorted(list_pair, key=lambda x: x[1], reverse=True) #빈도수 기준으로 정렬
    for (word, frequency) in ordered_list_pair :
        print(f"{word}: {frequency}")
    return

def save_word_frequencies(word_frequencies, output_file):
    try:
        with open(output_file, 'w') as file:
            for (word, frequency) in word_frequencies.items():
                file.write(f"{word}, {frequency}\n")
        print("saved word count result.")
    except IOError as e:
        print(f"error occurred while saving the file: {e}")


file_path = 'sample.txt'

file_content = read_file(file_path)
if file_content is not None:
    words = split_into_words(file_content)
    word_frequencies = count_word_frequencies(words)
    print_word_frequencies(word_frequencies)
    save_word_frequencies(word_frequencies, 'word_frequencies.csv')