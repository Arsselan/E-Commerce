import os

# Schreibt in 
#   edited by XYZ
# die erste Zeile einer jeden Datei 
# Von dem du ein commit erstellt hast.
#   git_username - der author name laut git, z. B. kann "Miles.*" sowohl "Miles " als auch "Miles Sasportas" sein
#   nameInFile - Was im Endeffekt inder Datei als name im header sstehen soll.

git_username = 'DEIN GIT NAME'
nameInFile = 'WAS IN DER DATEI STHEEN SEOLL'

def add_header(file_path, header):
    with open(file_path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(header + '\n' + content)

def process_file(file_path):
    supported_extensions = {'py', 'vue', 'js'}

    file_extension = file_path.split('.')[-1].lower()
    if file_extension not in supported_extensions:
        return

    if not os.path.exists(file_path):
        print(f"\tFile doesn't exist: {file_path}")
        return

    header = f'# edited by {nameInFile}' if file_extension == 'py' else \
             f'<!-- edited by {nameInFile}-->' if file_extension == 'vue' else \
             f'// edited by {nameInFile}' if file_extension == 'js' else None

    if header:
        add_header(file_path, header)


def main():
    # Replace 'your_git_username' with your actual Git username
    command = f'git log --author="{git_username}" --name-only --oneline --pretty=format: --all'
    print(command)

    result = os.popen(command).read()
    files = set(result.splitlines())
    print(files)

    for file_path in files:
        process_file(file_path)

if __name__ == "__main__":
    main()
