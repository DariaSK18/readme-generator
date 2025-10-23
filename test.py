from rich.console import Console
from rich.table import Table
from rich import print
from rich.style import Style
# from pathlib import Path

# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()
# with open("readme.md") as readme:
#     markdown = Markdown(readme.read())
# console.print(markdown)

'''

Foreground Color Name	Background Color Name
black	                                on black
red	                                    on red
green	                                on green
yellow	                                on yellow
blue	                                on blue
magenta	                                on magenta
cyan	                                on cyan
white	                                on white
default (resets to terminal default)	on default



'''

basicStyle = Style(color="blue", bold=False, italic=True)

data = {}
# print(f"[italic {basicStyle}]JEW JEW JEW[/italic {basicStyle}] World!")

# data['title'] =  input('Heading title: '),
# data['description'] = input('Description:'),
# data['heading'] = input('heading'),
# data['content'] = input('content')

# dataTwo = {
#     'title': input('title: '),
#     'desc': input('desc: ')
# } pick any method both work 

# print(dataTwo['title'])

def getUserInputs():
    data = {}
    data['title'] =  input('Heading title: ')
    data['description'] = input('Description: ')
    data['heading'] = input('heading: ')
    data['content'] = input('content: ')
    return data

def genMarkdown(data):
   # HERE DO WITH OPEN
   with open('readme.md', 'w') as f:
       # new line i 
       f.write(f'# {data['title']} \n## {data['description']}\n## {data['heading']}\n## {data['content']}')
    # print(data['title']) run it
    # print(data['description'])
    # print(data['heading'])
    # print(data['content'])
# does it print title? yes and one letter agaoin :)

# find more templates also make another function that creates basic readme.md without user input
TEMPLATES = {
    "Basic README": "# Project Title\n\n## Description\n\n## Installation\n\n## Usage\n\n## License\n",}


# btw that was the easy part :) now you have to do use github format to style the readme
# now instead of printing it should be writing? why are you using two function? 
genMarkdown(getUserInputs())

    
# but how will i get the data? store it globaly when u return it will become global i beleive , try it out real quick? re run

# def getUserInputs(heading, title, content, etc)

# why do u write this way data['title'] i am weird ?? but it just makes ur code more readable , do ur way real q
# def create_file(userInputs):
#     with open('readme.md', 'w') as file:
#             # using the file see what you can do with it?
#         file.write(userInputs)
 
#     print(f'[italic {basicStyle}]file created [/italic {basicStyle}]')

# create_file(userInputs)
'''

1. get user input for what the heading will be called?

2. short project des

YOU GONNA NEED TWO function 

userInput():
    this should get the following heading, title , description,content?


can i store it in dict?
yes but show me example of dict?
+ 


genMarkdown()


'''
# create_file()
# def fancyFile(file):
    
#     file = str(f'')

