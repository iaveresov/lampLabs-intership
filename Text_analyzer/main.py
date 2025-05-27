import argparse
import re
from collections import Counter

def analyze_file (file_path, top_n=10, encoding='utf-8'):

    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
            #Count number of lines
            lines_count =  len(content.split('\n'))

            #Count number of words
            words = re.findall(r'\b\w+\b', content.lower())
            words_count = len(words)

            #Count number of characters
            chars  = len(content)

            #Count top N most frequent words
            words_freq = Counter(words)
            top_words = words_freq.most_common(top_n)

            #Printing result
            print(f'Слов: {words_count}')
            print(f'Строк: {lines_count}')
            print('Топ 10 слов:')
            for i, (word, count) in enumerate(top_words, 1):
                print(f'{i}. {word} - {count}')

    except FileNotFoundError:
        print(f'Invalid file name {str(file_path)}: no such file or directory')
    except Exception as e :
        print(f'Error occurs when reading a file: {str(e)}')

def main():

    parser = argparse.ArgumentParser(description='Анализатор текстовых файлов')
    parser.add_argument('--file', required=True, type=str, help='Путь к анализируемому файлу')
    parser.add_argument('--top', type=int, default=10, help= 'Количество выводимых частых слов')
    parser.add_argument('--encoding', type=str, default='utf-8',  help='Кодировка (utf-8 по-умолчанию)')
    args = parser.parse_args()
    analyze_file(args.file,  args.top, args.encoding)

if __name__ == '__main__':
    main()