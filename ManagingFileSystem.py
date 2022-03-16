from pathlib import Path
# Where am I ? 

cwd = Path.cwd()
print(cwd)

#Combine parts to create full path and file name

new_file = Path.joinpath(cwd, 'new_file.txt')
print(new_file)

print(new_file.is_file())

print(new_file.exists())