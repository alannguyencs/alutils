import os
import platform
import glob
from random import shuffle






def num2String(number, num_char=6):
    str_number = str(number)
    while(len(str_number) < num_char):
        str_number = "0" + str_number
    return str_number

def gen_dir(new_dir):
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    return (new_dir + '/')

def gen_train_val_test(data_path, result_path, p_train=80, p_test=20):
    data_path = data_path if data_path[-1]=='/' else data_path + '/'
    result_path = result_path if result_path[-1]=='/' else result_path + '/'

    def gen_dataset(data_list, data_name):
        csv_file = open(result_path + data_name + '.csv', 'w')
        csv_file.write('file_name\n')
        for file_path in data_list:
            file_name = file_path.replace('\\', '/').split('/')[-1]
            csv_file.write(file_name + '\n')

    data = glob.glob(data_path + "*")
    shuffle(data)

    assert(p_train + p_test <= 100)
    if p_train + p_test == 100:
        num_train = int(p_train / 100 * len(data))
        gen_dataset(data[:num_train], 'train')
        gen_dataset(data[num_train:], 'test')
    else:
        num_train = int(p_train / 100 * len(data))
        num_test = int(p_test / 100 * len(data))
        gen_dataset(data[:num_train], 'train')
        gen_dataset(data[:(num_train + num_test)], 'test')
        gen_dataset(data[(num_train + num_test):], 'val')
