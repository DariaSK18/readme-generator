from urllib.parse import urlparse
from questionary import prompt, Style
# from rich.console import Console
from console import console

# console = Console()
style = Style([
    ('qmark', 'fg:#00FF7F bold'),
    ('question', 'fg:#00BFFF'),
    ('answer', 'fg:#FFD700'),
    ('pointer', 'fg:#FF69B4 bold'),
    ('highlighted', 'fg:#ADFF2F bold'),
])

def getUserInputs():
    # console.print("\n[bold red]Cancelled by user.[/bold red]")
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
