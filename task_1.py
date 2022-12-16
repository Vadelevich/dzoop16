import os


class ChangeDir:
    def __init__(self, name_dir):
        self.name_dir = name_dir

    def __enter__(self):
        os.chdir(self.name_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir('..')


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())

# вывод в консоль
# ['log.txt']
# ['file1.py', 'file2.py']
