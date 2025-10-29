from rich.markdown import Markdown
import time
from rich.progress import Progress
from rich.console import Console

console = Console()

def write_file(template, filename = 'readme.md'):
    with open(filename, 'w') as file:
        content = '\n'.join(f'{value}' for key, value in template.items())
        # print(content)
        file.write(content)
        return filename

def load_data():
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...", total=10)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(task, advance=1) 

class FileViewer:
    def __init__(self, style='markdown'):
        self.console = console
        self.style = style
        
    def show_file(self, filename):
        with open(filename, 'r') as f:
            markdown = Markdown(f.read())
        self.console.print(markdown)