from pathlib import Path
# What the current directory is ? 

cwd = Path.cwd()
parent = cwd.parent
print ('Current working directory :\n' + str(cwd))

# Create full path name by joining path and filename
new_file = Path.joinpath(cwd, 'new_file')
print('Full path:\n' + str(new_file))

print('\n----Directory Contents----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)