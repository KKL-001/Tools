from shutil import copy

def trasfer_process(load_path, unload_path, file_txt):
    """
    将一个文件夹中目标序号的图片复制到另一个文件夹中，序号在txt文件中说明 eg: 1 2 3
    为png格式 1.png 2.png 3. png
    load_path: 图片存储的路径
    unload_path: 图片转移的路径
    file_txt: 需要转移图片的序号, 存储在txt文件中 eg:1 2 3 4
    :return: null
    """

    file_open = open(file_txt, encoding='utf-8')
    file_read = file_open.read()
    file_name = file_read.split(sep=' ')

    for i in range(len(file_name)):
        file_name[i] += '.png'

    for i in file_name:
        copy(load_path + i, unload_path)

    print(file_name)


if __name__ == '__main__':
    l_path = 'F:\\dataset\\tolian\\GF2-tiff-process\\'
    u_path = 'F:\\dataset\\tolian\\GF2-tiff-select-2\\'
    f_txt = 'F:\\dataset\\tolian\\select.txt'
    trasfer_process(l_path, u_path, f_txt)
