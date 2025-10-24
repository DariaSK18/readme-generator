from inputs import getUserInputs
from template import getMarkdown
from output import write_file, load_data, show_file
from console import console


def gen_file():
    user_inputs = getUserInputs()
    template = getMarkdown(user_inputs)

    load_data()
    filename = write_file(template)
    show_file(filename)

console.print("[bold red]Cancelled by user.[/bold red]")
# if __name__ == "__main__":
try: 
    gen_file()
except KeyboardInterrupt:
    console.print("[bold red]Cancelled by user.[/bold red]")