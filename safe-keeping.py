import os, errno


# Function to write a file at a given path
def WriteFileInPath(content, path):
    try:
        with open(path, "w+") as f:
            f.write(content)  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
            f.close()
            return "Created " + path
    except IOError as e:
        print(e)
        return False


# This function creates given folders.
def installFolder(folder):
    try:
        os.makedirs(folder)
        print("Created directory", folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
