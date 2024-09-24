import requests

def fetch_links(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def clean_links(links):
    cleaned_links = []
    for link in links:
        cleaned_link = link.split('$')[0].strip()  # 删除“$”及其后的内容
        if cleaned_link:  # 只保留非空行
            cleaned_links.append(cleaned_link)
    return cleaned_links

def write_to_file(links, filename='iptv.m3u'):
    with open(filename, 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/n3rddd/CTVLive/refs/heads/main/litelive.m3u"
    links = fetch_links(url)
    cleaned_links = clean_links(links)
    write_to_file(cleaned_links)
    print("处理完成，结果已写入iptv.m3u")
