import re
import os


def get_file_list(file_url):
    # 把路径转化为绝对路径
    file_url = os.path.abspath(file_url)

    # 判断输入是文件还是路径
    if os.path.isdir(file_url):
        return [os.path.join(file_url,file_name) for file_name in os.listdir(file_url) if file_name.endswith('.md')]

    elif os.path.isfile(file_url):
        return [file_url]

    else:
        return False


def read_file(file_url):
    # 读取单个文件里的字符串，返回列表
    with open(file_url, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_file(file_url, file_line):
    print(file_url)
    # 写入文件
    # 修改文件名
    filename = os.path.split(file_url)
    file_url = os.path.join(filename[0],r"new-" + filename[1])

    # 写入文件
    with open(file_url, 'w', encoding='utf-8') as file:
        file.writelines(file_line)

        return True


def repair_image(file_line):
    # 去除链接后缀
    pattern1 = re.compile(r"!\[[a-zA-z.]*\]\(https:\/\/cdn\.nlark\.com[\w\/\-.]*")
    pattern2 = re.compile(r"#.*?\)")

    # 先匹配，如果匹配上就替换
    file_line = [re.sub(pattern2, r")" , line) if re.match(pattern1, line) else line for line in file_line]

    return file_line



# 输入文件路径
# file_url = input("请输入.md文件所在路径：\n")
file_url = r"C:\Users\a\Downloads\Python数据分析课件资料"

for file_list_i in get_file_list(file_url):
    write_file(file_list_i, repair_image(read_file(file_list_i)))





