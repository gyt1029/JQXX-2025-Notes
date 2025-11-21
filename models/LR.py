# 1. 数据加载与预处理
print("=" * 60)
print("脑卒中后疲劳预测模型 - 五算法比较 (R语言风格改进版)")
print("=" * 60)

def load_and_validate_data():
    """加载并验证数据"""
    current_dir = Path.cwd()
    file_path = current_dir / "C:/Users/g2997/Desktop/Post-Stroke Fatigue Questionnaire_2.xlsx"
    
    if not file_path.exists():
        file_path = r"C:\Users\g2997\Desktop\Post-Stroke Fatigue Questionnaire_2.xlsx"
    
    try:
        df = pd.read_excel(file_path)
        print(f"成功加载数据，数据集形状: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"错误: 文件未找到: {file_path}")
        exit(1)
    except Exception as e:
        print(f"加载数据时出错: {e}")
        exit(1)

def clean_column_names(df):
    """清理列名，参考R代码的处理方式"""
    df_clean = df.copy()
    
    # 替换特殊字符
    df_clean.columns = (df_clean.columns
                       .str.replace(r'[()]', '_', regex=True)
                       .str.replace(r'[:]', '_', regex=True)
                       .str.replace(r'[ ]', '_', regex=True)
                       .str.replace(r'[,]', '_', regex=True))
    
    # 确保列名是有效的Python标识符
    import re
    def make_valid_name(name):
        # 移除开头和结尾的下划线
        name = name.strip('_')
        # 替换连续的下划线
        name = re.sub(r'_+', '_', name)
        # 确保以字母或下划线开头
        if name and not name[0].isalpha() and name[0] != '_':
            name = '_' + name
        return name
    
    df_clean.columns = [make_valid_name(col) for col in df_clean.columns]
    
    print(f"列名清理完成，示例: {list(df_clean.columns[:5])}")
    return df_clean
