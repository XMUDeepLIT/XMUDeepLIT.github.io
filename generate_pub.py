import re

def parse_citation(citation_str):
    # 分割字符串为四个部分
    parts = citation_str.split('. ', 3)
    if len(parts) != 4:
        raise ValueError("输入的引文字符串格式不正确")
    
    authors_str, year, title, venue = parts
    year = year.strip()
    title = title.strip()
    venue = venue.strip()
    
    # 处理作者列表：使用更灵活的正则表达式分割
    raw_authors = re.split(r',\s*(?:and\s*)?', authors_str)
    cleaned_authors = []
    author_notes = []
    
    for author in raw_authors:
        author = author.strip()
        if not author:
            continue
        # 处理末尾的*或+
        symbol_match = re.search(r'([+*])$', author)
        if symbol_match:
            symbol = symbol_match.group(1)
            cleaned_author = re.sub(r'[+*]$', '', author).strip()
            # 处理可能的符号后多余空格（如 "Wu* " → "Wu"）
            cleaned_author = re.sub(r'\s+$', '', cleaned_author)
            note = '共同一作' if symbol == '+' else '通讯作者' if symbol == '*' else ''
        else:
            cleaned_author = author
            note = ''
        cleaned_authors.append(cleaned_author)
        author_notes.append(note)
    
    return {
        'authors': cleaned_authors,
        'author_notes': author_notes,
        'year': year,
        'title': title,
        'venue': venue
    }

# 测试用例
citation = "Yaoxiang Wang, Zhiyong Wu*, Junfeng Yao, and Jinsong Su*. 2025. TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation. Neural Networks. (CCF-B类)"
print(parse_citation(citation))