import os
def rename_file():
    file_list = os.listdir(r"/Users/zhihuixie/Downloads/alphabet")
    print (file_list)
    os.chdir(r"/Users/zhihuixie/Downloads/alphabet")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(r"/Users/zhihuixie/Downloads/alphabet")
    print file_list

rename_file()
