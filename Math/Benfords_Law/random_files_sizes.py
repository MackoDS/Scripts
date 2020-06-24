# This script creates file with 100 random files byte sizes

import random
import os
import pathlib

n = 100
output_file = open('random_files_sizes.txt', 'w+')
os.chdir('C:\\')


all_directories = []
for (dirpath, dirnames, filenames) in os.walk('C:'):
    all_directories.append(dirpath)


# very inefective, but enough for little disk. Better idea would be to pick random files in time without putting every dir on disk in list.
not_empty_random_directories = []
while n > 0:
    random_dir = random.choice(all_directories)
    # get all files but not directories
    files = next(os.walk(random_dir))[2]

    # if there are no files in directory
    if not files:
        pass
    else:
        random_file = random.choice(files)
        random_file_path = random_dir + '\\' + random_file
        file_size = str(pathlib.Path(random_file_path).stat().st_size) + '\n'
        output_file.write(file_size)
        n -= 1

output_file.close()
