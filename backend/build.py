import shutil
import os


ignore = shutil.ignore_patterns('__pycache__')


def build(build_name):
    dest_path = os.path.join('dist', build_name)
    shutil.copytree(build_name, dest_path, ignore=ignore)
    shutil.copytree('common', dest_path, ignore=ignore)

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    try:
        shutil.rmtree('dist')
    except Exception as e:
        print(e)
    try:
        os.mkdir('dist')
    except Exception as e:
        print(e)
    build('api')
    build('db_init')
    build('worker')
