from pathlib import Path

cmd = Path.cwd()

demo_file = Path(Path.joinpath(cmd,'demo.txt'))

# Get the file name

print('\nfile name: ' + demo_file.name)

print ('\nfile suffix : '+ demo_file.suffix)

print('\nfile folder : '+ demo_file.parent.name)

print('\nfile size : ' + str(demo_file.stat().st_size) + '\n')