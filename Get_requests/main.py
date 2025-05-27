import requests
import argparse

def fetch_posts(url):
    try:
        response = requests.get(url)

        posts = response.json()
        print('Первые 5 постов:')

        for post in posts[:5]:
            print(f'\nID: {post['id']}')
            print(f'Title {post['title']}')
            print(f'Body:{post['body']}')
    except requests.exceptions.RequestException as e:
        print(f'Request error: {str(e)}')
    except ValueError as e:
        print(f'JSON error: {str(e)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запрос к публичному API')
    parser.add_argument("--url", type=str, default='https://jsonplaceholder.typicode.com/posts')

    arguments = parser.parse_args()
    fetch_posts(arguments.url)
