"""A file containing a helper function for processing multiple files"""

def process_header(file):
    """Function to process the header of our file."""
    
    header_num = 0
    
    f = open(file)
    lines = f.readlines()
    molecule_name = lines[0].split("=")[1].strip()

    for line in lines:
        if line[0] == "#":
            header_num = header_num + 1
    f.close()
    
    # Subtract 1 because the last line ends in #
    header_num = header_num - 1
                
    return molecule_name, header_num
