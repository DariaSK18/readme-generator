from rich.markdown import Markdown
import time
from rich.progress import Progress
from rich.console import Console

console = Console()

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