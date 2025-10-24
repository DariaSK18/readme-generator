from urllib.parse import urlparse
from pathlib import Path
from questionary import prompt, Style
from rich.console import Console
import json
from rich.markdown import Markdown
import time
from rich.progress import Progress

console = Console()
style = Style([
    ('qmark', 'fg:#00FF7F bold'),
    ('question', 'fg:#00BFFF'),
    ('answer', 'fg:#FFD700'),
    ('pointer', 'fg:#FF69B4 bold'),
    ('highlighted', 'fg:#ADFF2F bold'),
])

def getUserInputs():
    console.print('\n')
    console.rule(f'[bold blue]README Generator[/bold blue]')
    console.print('\n')
    questions = [
        {
            'type': 'input',
            'name': 'main_title',
            'message': 'Title of the project: '
        },
        {
            'type': 'input',
            'name': 'main_subtitle',
            'message': 'Subtitle of the project or short description: '
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description of the project: '
        },
        {
            'type': 'input',
            'name': 'repository_link',
            'message': 'Repository link: '
        },
        {
            'type': 'list',
            'name': 'license',
            'message': 'Choose a license: ',
            'choices': ['MIT', 'Apache 2.0', 'GPL', 'BSD']
        },
        {
            'type': 'input',
            'name': 'author_name',
            'message': 'Author name: '
        },
        {
            'type': 'input',
            'name': 'contact_info',
            'message': 'Contact info (e-mail): '
        },
    ]
    answers = prompt(questions, style=style)
    # print(answers)
    path = urlparse(answers['repository_link']).path
    project = path.split('/')[-1]
    answers['repository_folder'] = project.replace('.git', '')
    # print(answers['repository_folder'])
    # print(answers)
    return answers

def getMarkdown(data):
    template = {
        'title': f'# {data["main_title"]} \n',
        'subtitle': f'{data["main_subtitle"]} \n',
        'descriptionTitle': '## Description \n',
        'description': f'{data["description"]} \n',
        'installationTitle': '## Installation \n',
        'installationInstruction':(
            '1. Clone this repository: \n'
            f'```bash \n git clone {data["repository_link"]} \n'
            '``` \n'
            '```bash \n '
            f'cd {data["repository_folder"]} \n'
            '``` \n'
            '2. Create a virtual environment: \n'
            '```bash \n '
            'python -m venv venv \n'
            '``` \n'
            '3. Activate the virtual environment: \n'
            '- **Windows** \n'
            '```bash \n '
            'venv\Scripts\\activate \n'
            '``` \n'
            '- **macOS / Linux** \n'
            '```bash \n '
            'source venv/bin/activate \n'
            '``` \n'
            '4. Install dependencies: \n'
            '```bash \n '
            'pip install -r requirements.txt \n'
            '``` \n'),
        'usageTitle': '## Usage \n',
        'usageInstruction': ('1. Run the script: \n'
            'python main.py\n'
            '2. Answer the interactive questions in the terminal \n'
            '3. The program will generate a README.md file in the project directory based on your answers \n'
            '4. Open the generated file in VS Code or preview it on GitHub to see the final result.\n'),
        'licenseTitle': '## License \n',
        'licenseInfo': f'This project is licensed under the {data["license"]} License — you are free to use, modify, and distribute it.\n',
        'authorNameTitle': '## Author\n',
        'authorName': f'{data["author_name"]}',
        'contactInfo': f'- Contact: [{data["contact_info"]}](mailto:{data["contact_info"]})'
        }
    return template
     
with open('readme.md', 'w') as file:
    template = getMarkdown(getUserInputs())
    content = '\n'.join(f'{value}' for key, value in template.items())
    # print(content)
    file.write(content)
    
with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=10)
    for _ in range(10):
        time.sleep(0.1)
        progress.update(task, advance=1) 

with open("readme.md", 'r') as readme:
    markdown = Markdown(readme.read())
console.print(markdown)