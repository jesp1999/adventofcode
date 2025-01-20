import os.path
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv

load_dotenv()

YEAR = int(os.environ.get('YEAR', time.localtime().tm_year))
DAY = int(os.environ.get('DAY', time.localtime().tm_mday))
SESSION_COOKIE = str(os.environ.get('SESSION_COOKIE', ''))

cookies = {'session': SESSION_COOKIE}
while time.localtime().tm_hour != 0:
    ...


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
main_content = r'''import pyperclip as pc

...


def solution(lines: list[str]):
    ret = 0
    for line in lines:
        ...
    ...
    return ret


''' + '\n\n'.join(test_cases) + r'''

# data = open('input.txt', 'r').read().strip().split('\n')

s = solution(data)
print(s)
pc.copy(s)
'''

main_path = f'{dirname}/main{len(code_content_list)}.py'
if not os.path.exists(main_path):
    with open(main_path, 'w+') as f:
        f.write(main_content)

with open(f'{dirname}/input.txt', 'w+') as f:
    f.write(input_response.content.decode().strip('\n'))
