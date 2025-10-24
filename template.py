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
     