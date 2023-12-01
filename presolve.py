import os.path
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv

load_dotenv()

YEAR = int(os.environ.get('YEAR', 2023))
DAY = int(os.environ.get('DAY', 1))
SESSION_COOKIE = str(os.environ.get('SESSION_COOKIE', ''))

cookies = {'session': SESSION_COOKIE}
input_response = requests.get(
    f'https://adventofcode.com/{YEAR}/day/{DAY}/input', cookies=cookies
)

if not os.path.exists(str(YEAR)):
    os.mkdir(str(YEAR))

dirname = f'{YEAR}/day{DAY}'

if not os.path.exists(dirname):
    os.mkdir(dirname)

response = requests.get(
    f'https://adventofcode.com/{YEAR}/day/{DAY}', cookies=cookies
)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
code_tags = soup.find_all('pre')
code_content_list = [code_tag.get_text() for code_tag in code_tags]
test_cases = [
    "# data = '''" + '\n# '.join(code_content.split("\n")) + r"'''.split('\n')"
    for code_content in code_content_list
]
main_content = r'''...


def solution(lines: list[str]):
    ret = 0
    ...
    return ret


''' + '\n\n'.join(test_cases) + r'''

data = open('input.txt', 'r').read().split('\n')

print(solution(data))
'''

main_path = f'{dirname}/main{len(code_content_list)}.py'
if not os.path.exists(main_path):
    with open(main_path, 'w+') as f:
        f.write(main_content)

with open(f'{dirname}/input.txt', 'w+') as f:
    f.write(input_response.content.decode().strip('\n'))
