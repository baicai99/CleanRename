import os
import re

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        # 重命名文件
        for name in files:
            rename_file_or_directory(root, name)

        # 重命名文件夹
        for name in dirs:
            rename_file_or_directory(root, name)

def rename_file_or_directory(root, name):
    old_path = os.path.join(root, name)
    new_name = replace_special_characters(name)
    new_path = os.path.join(root, new_name)
    # 重命名
    if new_path != old_path:
        os.rename(old_path, new_path)
        print(f"Renamed '{old_path}' to '{new_path}'")

def replace_special_characters(name):
    # 使用正则表达式替换连续的'-'、中文破折号、空格以及单引号为'_'
    return re.sub("[-\s'\u2014\u2015]+", '_', name)

# 在命令行提示输入路径
directory_path = input("请输入要处理的目录路径: ").replace("'", '')
rename_files_in_directory(directory_path)
