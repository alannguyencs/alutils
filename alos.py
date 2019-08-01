import os

def get_file_name(file_path, with_extension=False):
    file_path = file_path.replace('\\', '/')
    [file_name, ext] = file_path.split('/')[-1].split('.')
    if with_extension:
        return file_name + '.' + ext
    else:
        return file_name

def gen_dir(new_dir, remove_old=False):
    import os
    if remove_old:
        import shutil
        if os.path.exists(new_dir):
            shutil.rmtree(new_dir)
        os.mkdir(new_dir)

    elif not os.path.exists(new_dir):
        os.mkdir(new_dir)

    return (new_dir + '/')