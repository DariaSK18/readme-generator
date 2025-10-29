from inputs import getUserInputs
from template import getMarkdown
from output import write_file, load_data, FileViewer
from console import console
# import time
# import signal

def gen_file():
    user_inputs = getUserInputs()
    template = getMarkdown(user_inputs)

    load_data()
    filename = write_file(template)
    viewer = FileViewer(style='markdown')
    viewer.show_file(filename)

# def fail(sig, frame):
#     console.print("[bold red]Cancelled by user.[/bold red]", flush=True)
#     exit(0)
    
# signal.signal(signal.SIGINT, fail)
    
if __name__ == "__main__":
    try:
        gen_file()
    except KeyboardInterrupt:
        console.print("Cancelled by user.")
