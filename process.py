def process_config(input_file, output_file):
    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 找到 "rules:" 开始的行号
    start_index = 0
    for index, line in enumerate(lines):
        if line.strip() == 'rules:':
            start_index = index + 1
            break
    
    # 初始化处理后的文件内容
    processed_lines = [
        '[General]\n',
        'bypass-system = true\n',
        'skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, e.crashlytics.com, captive.apple.com\n',
        'bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,224.0.0.0/4,255.255.255.255/32\n',
        '[Rule]\n'
    ]
    
    # 处理 rules 部分
    for line in lines[start_index:]:
        # 删除行首的 "- "
        if line.startswith('- '):
            line = line[2:]
        
        # 替换 "🚀 节点选择" 为 "PROXY"
        line = line.replace('🚀 节点选择', 'PROXY')
        
        processed_lines.append(line)
    
    # 替换最后一行的 "MATCH" 为 "FINAL"
    if processed_lines[-1].startswith('MATCH'):
        processed_lines[-1] = processed_lines[-1].replace('MATCH', 'FINAL')
    
    # 写入到新文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

# 调用函数处理文件
process_config("clash-verge.yaml", "shadowrocket.conf")