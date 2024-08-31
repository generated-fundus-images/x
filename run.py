import os
import json

folders = []
print(1)
print(os.listdir("D:/_code/x58/"))

# 获取当前目录下的所有子文件夹
for folder_name in os.listdir("D:/_code/x58/"):
    print(folder_name)
    if os.path.isdir(folder_name):
        
        # 获取每个文件夹下的图片文件
        images = [f for f in os.listdir(folder_name) if f.endswith(".png")]

        # 构造folder对象
        folder = {"name": folder_name, "images": images}

        # 添加到folders列表
        folders.append(folder)

# 生成JSON
json_data = json.dumps(folders, indent=4)

print(json_data)
