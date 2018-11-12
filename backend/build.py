import shutil
import os


ignore = shutil.ignore_patterns('__pycache__')


def build(build_name):
    dest_path = os.path.join('dist', build_name)
    shutil.copytree(build_name, dest_path, ignore=ignore)
    common_dir = 'common'
    for folder in os.listdir(common_dir):
        common_sub_dir = os.path.join(common_dir, folder)
        if os.path.isdir(common_sub_dir):
            shutil.copytree(common_sub_dir, os.path.join(dest_path, folder),
                            ignore=ignore)


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
