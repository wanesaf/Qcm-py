import os

def print_with_frame(lines):
    terminal_width = os.get_terminal_size().columns
    frame_width = terminal_width - 2 

    border = "-" * frame_width
    print(border)
    for line in lines:
        print("|" + line.center(frame_width - 2) + "|")
    print(border)
    
    