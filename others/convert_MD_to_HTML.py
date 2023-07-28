import os

main_folder = "assets/markdown"

top_level_dir = os.listdir(f"{main_folder}")

# Go through each folder in "assets/markdown"
for dir in top_level_dir:
    sub_dir = os.listdir(f"{main_folder}/{dir}")
    # Go through each file in that folder
    for file in sub_dir:
        # Get the name of the file
        filename = file.split(".")[0]

        # Create a array
        file_contents = []

        # Get each line from the file
        with open(f"{main_folder}/{dir}/{file}", "r") as lines:
            # Store it into the array
            for line in lines:
                file_contents.append(line.strip())

        # Add some template code to the array
        file_contents.insert(0, '')
        file_contents.insert(0, '')
        file_contents.insert(0, '    <script src="https://rawcdn.githack.com/oscarmorrison/md-page/master/md-page.js"></script><noscript>')
        file_contents.insert(0, '    <!-- Markdown display script by Oscar Morrison: https://github.com/oscarmorrison/md-page/ -->')
        file_contents.insert(0, '')
        file_contents.insert(0, '    <link rel="stylesheet" type="text/css" href="assets/css/markdownFormat.css"/>')
        file_contents.insert(0, f'    <title>{filename} - LED Light Wall</title>')
        file_contents.insert(0, '<html>')
        file_contents.append('')
        file_contents.append('')
        file_contents.append('</html>')

        # Save it to a new file with name_of_orig_file.html as the filename to "assets/templates"
        with open(f"documentation/{dir}/{filename}.html", "w") as new_file:
            new_file.write("\n".join(file_contents))

print("\nCompleted converting markdown files to HTML.\n")
