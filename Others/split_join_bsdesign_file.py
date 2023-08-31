import os

def split(source, dest_folder, write_size):
    # Make a destination folder if it doesn't exist yet
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    else:
        # Otherwise clean out all files in the destination folder
        for file in os.listdir(dest_folder):
            os.remove(os.path.join(dest_folder, file))
    partnum = 0

    # Open the source file in binary mode
    input_file = open(source, 'rb')
    while True:
        # Read a portion of the input file
        chunk = input_file.read(write_size)

        # End the loop if we have hit EOF
        if not chunk:
            break

        # Increment partnum
        partnum += 1

        # Create a new file name
        dir1 = os.path.join(os.getcwd(), "Others\\Website_Split")
        filename = f'{dir1}\\website_file_'.replace("\\", "/") + str("".join(["1" for part in range(partnum)])) + ".bsdesign.pkl"

        # Create a destination file
        dest_file = open(filename, 'wb')

        # Write to this portion of the destination file
        dest_file.write(chunk)
        # Explicitly close
        dest_file.close()
    # Explicitly close
    input_file.close()
    # Return the number of files created by the split
    return partnum

def join(dest_file, read_size):
    # Create a new destination file
    output_file = open(os.path.join(os.getcwd(), dest_file), 'wb')

    # Get a list of the file parts
    parts = os.listdir(os.path.join(os.getcwd(), "Others\\Website_Split"))

    # Go through each portion one by one
    for file in parts:

        # Assemble the full path to the file
        path = os.path.join(os.path.join(os.getcwd(), "Others\\Website_Split"), file)

        # Open the part
        input_file = open(path, 'rb')

        while True:
            # Read all bytes of the part
            bytes = input_file.read(read_size)

            # Break out of loop if we are at end of file
            if not bytes:
                break

            # Write the bytes to the output file
            output_file.write(bytes)

        # Close the input file
        input_file.close()

    # Close the output file
    output_file.close()

# print(split("Original Website File.bsdesign", "/Website_Split/", 4000000))
join("LED Light Wall Website.bsdesign", 4000000)
