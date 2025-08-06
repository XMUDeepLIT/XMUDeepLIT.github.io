import os
import shutil

def renumber_subfolders(target_num):
    """
    删除指定编号的子文件夹，并将后续文件夹重新编号前移
    :param target_num: 要删除的文件夹编号（整数）
    """
    # 获取当前脚本所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取所有数字命名的子文件夹
    subfolders = []
    for name in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, name)) and name.isdigit():
            subfolders.append(int(name))
    
    if not subfolders:
        print("未找到数字命名的子文件夹")
        return
    
    # 检查目标文件夹是否存在
    if target_num not in subfolders:
        print(f"文件夹 {target_num} 不存在")
        return
    
    # 删除目标文件夹
    target_path = os.path.join(base_dir, str(target_num))
    shutil.rmtree(target_path)
    print(f"已删除文件夹: {target_num}")
    
    # 获取需要重命名的文件夹（比目标编号大的）
    to_rename = [f for f in subfolders if f > target_num]
    to_rename.sort()  # 从小到大排序
    
    # 依次重命名后续文件夹
    for folder_num in to_rename:
        old_name = str(folder_num)
        new_name = str(folder_num - 1)
        old_path = os.path.join(base_dir, old_name)
        new_path = os.path.join(base_dir, new_name)
        
        # 检查新路径是否已存在（理论上不应该存在）
        if os.path.exists(new_path):
            print(f"警告：路径 {new_path} 已存在，跳过重命名")
            continue
            
        os.rename(old_path, new_path)
        print(f"已将 {old_name} 重命名为 {new_name}")

# 使用示例 - 删除编号为2的文件夹
renumber_subfolders(126)