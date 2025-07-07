import os
import datetime
import sys

def count_subdirectories():
    """
    计算当前Python文件所在文件夹内的子文件夹数量
    (不包括文件、当前目录(.)和上级目录(..))
    
    返回:
        int: 子文件夹数量+1
    """
    try:
        # 获取当前.py文件所在的目录路径
        current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        
        # 列出目录中的所有条目
        all_entries = os.listdir(current_dir)
        
        # 筛选出子文件夹（排除文件和特殊目录）
        subdirectories = [
            entry for entry in all_entries
            if os.path.isdir(os.path.join(current_dir, entry))
            and entry not in ('.', '..')  # 排除当前目录和上级目录
        ]
        
        return len(subdirectories)+1
    
    except Exception as e:
        print(f"计算子文件夹数量时出错: {e}")
        return 0   
    
def create_directory_and_file():
    # 获取ID
    directory_id = count_subdirectories()
    
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 创建文件夹路径
    directory_path = os.path.join(os.getcwd(), str(directory_id))
    
    # 创建文件夹
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"成功创建文件夹: {directory_path}")
    except OSError as e:
        print(f"创建文件夹失败: {e}")
        return
    
    # 创建文件路径
    file_path = os.path.join(directory_path, "index.md")
    
    # 文件内容
    content = f"""---
title: 
date: {current_date}
---

<!--more-->"""
    
    # 写入文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"成功创建文件: {file_path}")
    except OSError as e:
        print(f"创建文件失败: {e}")

if __name__ == "__main__":
    create_directory_and_file()    