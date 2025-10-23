from urllib.parse import urlparse
from pathlib import Path


# get user inputs 
def getUserInputs():
    data = {}
    
    data['main_title'] = input('Title of the project: ')
    data['main_subtitle'] = input('Subtitle of the project or short description: ')
    data['description'] = input('Description of the project: ')
    data['repository_link'] = input('Repository link: ')
    # data['link'] = input('Link to live demo: ')
    # url = data['repository_link']
    # folder = Path(url).name
    # data['repository_folder'] = folder
    path = urlparse(data['repository_link']).path
    project = path.split('/')[-1]
    data['repository_folder'] = project.replace('.git', '')
    # print(data['repository_folder'])
    
    return data

def getMarkdown(data):
    template = {
        'title': f'# {data['main_title']} \n',
        'subtitle': f'{data['main_subtitle']} \n',
        'descriptionTitle': '## Description \n',
        'description': f'{data['description']} \n',
        'installationTitle': '## Installation \n',
        'installationInstruction':(
            '1. Clone this repository: \n'
            '```bash \n git clone'
            f'{data['repository_link']} \n'
            f'cd {data['repository_folder']} \n'
            '2. Create a virtual environment: \n'
            'python -m venv venv \n'
            '3. Activate the virtual environment: \n'
            '- **Windows** \n'
            'venv\Scripts\\activate \n'
            '- **macOS / Linux** \n'
            'source venv/bin/activate \n'
            '4. Install dependencies: \n'
            'pip install -r requirements.txt \n'
            '``` \n'),
        'usageTitle': '## Usage \n',
        'usageInstruction': ('1. Run the script: \n'
            'python main.py\n'
            '2. Answer the interactive questions in the terminal \n'
            '3. The program will generate a README.md file in the project directory based on your answers \n'
            '4. Open the generated file in VS Code or preview it on GitHub to see the final result.')
        }
    return template
    
    
    
with open('README.md', 'w') as file:
    template = getMarkdown(getUserInputs())
    content = '\n'.join(f'{value}' for key, value in template.items())
    # print(content)
    file.write(content)
    