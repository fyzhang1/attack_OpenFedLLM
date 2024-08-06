import datasets
from datasets import load_dataset, Dataset
import pandas as pd

def load_attack_data(csv_file_path):
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)

# 将DataFrame转换为Dataset对象
    dataset = load_dataset('csv', data_files=csv_file_path)['train']

# 如果需要将数据重新分割成原来的结构（按客户端分割）
    num_clients = df['client'].nunique()  # 获取客户端数量
    client_datasets = []
    for i in range(num_clients):
        client_data = dataset.filter(lambda x: x['client'] == i)
        client_datasets.append(client_data)

# 打印每个客户端数据集的样本数
    for i, client_data in enumerate(client_datasets):
        print(f"Client {i}: {len(client_data)}")
    
    return client_datasets
    
