#!/usr/bin/env python3
"""中文字数统计工具
统计口径：中文字符数 + 英文单词数 + 数字串数，与 Word/WPS 中文字数统计一致。
用法：python3 word_count.py <file> [--min MIN] [--max MAX]
"""
import re
import sys
import argparse


def count_words(text: str) -> dict:
    # 去除HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 去除HTML注释
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # 去除script/style块
    text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # 反转义HTML实体
    text = text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")

    # 中文字符
    chinese = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))
    # 英文单词
    english = len(re.findall(r'[a-zA-Z]+', text))
    # 数字串
    numbers = len(re.findall(r'\d+', text))

    total = chinese + english + numbers
    return {
        'chinese': chinese,
        'english': english,
        'numbers': numbers,
        'total': total,
    }


def main():
    parser = argparse.ArgumentParser(description='中文字数统计')
    parser.add_argument('file', help='要统计的文件（.md/.txt/.html）')
    parser.add_argument('--min', type=int, default=None, help='最低字数')
    parser.add_argument('--max', type=int, default=None, help='最高字数')
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f'错误：文件不存在：{args.file}')
        sys.exit(2)
    except Exception as e:
        print(f'错误：{e}')
        sys.exit(2)

    r = count_words(text)
    print(f'文件：{args.file}')
    print(f'中文字符：{r["chinese"]}')
    print(f'英文单词：{r["english"]}')
    print(f'数字串数：{r["numbers"]}')
    print(f'总字数：{r["total"]}')

    ok = True
    if args.min is not None and r['total'] < args.min:
        print(f'❌ 不足：少于最低要求 {args.min} 字（差 {args.min - r["total"]} 字）')
        ok = False
    if args.max is not None and r['total'] > args.max:
        print(f'⚠️ 超标：超过最高限制 {args.max} 字（多 {r["total"] - args.max} 字）')
        ok = False
    if ok and (args.min is not None or args.max is not None):
        print('✅ 字数达标')

    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
