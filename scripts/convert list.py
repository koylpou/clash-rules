import requests

# URL列表和对应的输出文件名
urls_and_files = [
    ("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/GoogleCNProxyIP.list", "list/GoogleCNProxyIP.list"),
    ("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list", "list/LocalAreaNetwork.list"),
    ("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/UnBan.list", "list/UnBan.list")
]

def add_prefix_to_lines_and_save(url, output_file):
    try:
        # 发送HTTP GET请求
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出HTTPError异常

        # 读取内容并分行处理
        lines = response.text.splitlines()

        # 在每一行前添加"- "，同时跳过以"#"开头的行和空行
        modified_lines = ["- " + line for line in lines if not line.strip().startswith('#') and line.strip()]

        # 将修改后的内容写入到文件
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in modified_lines:
                file.write(line + '\n')

        print(f"File saved: {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def process_multiple_urls(urls_and_files):
    for url, output_file in urls_and_files:
        add_prefix_to_lines_and_save(url, output_file)

# 调用函数处理所有URL
process_multiple_urls(urls_and_files)
