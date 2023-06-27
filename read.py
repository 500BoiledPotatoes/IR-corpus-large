import os

path_read = []
def check_if_dir(file_path):

    temp_list = os.listdir(file_path)
    for temp_list_each in temp_list:
        if os.path.isfile(file_path + '/' + temp_list_each):
            temp_path = file_path + '/' + temp_list_each
            # if os.path.splitext(temp_path)[-1] == '.txt':    #自己需要处理的是.log文件所以在此加一个判断
            if temp_list_each == ".DS_Store":
                continue
            else:
                path_read.append(temp_path)
        else:
            check_if_dir(file_path + '/' + temp_list_each)    #loop traversal
    print(path_read)

check_if_dir("documents")
