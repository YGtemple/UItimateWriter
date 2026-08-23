#!/usr/bin/env python3
"""AI写作痕迹扫描器
扫描中文文本中的：
  1. AI身份声明（严重，命中即不合格）
  2. 模板化套话/黑话（警告）
  3. 句式模式（警告）
  4. 占位符残留（警告）
  5. 结构层特征（警告）：句子长度方差(burstiness)、无名泛指、代词滥用、hedge过度
用法：python3 scan_ai.py <file>
"""
import re
import sys
import statistics

# 【严重】AI身份声明——命中即不合格
SEVERE_PATTERNS = [
    (r'作为(?:一个|一名)?\s*(?:AI|人工智能|语言模型|大模型|助手)', 'AI身份声明'),
    (r'本文由.{0,10}(?:AI|人工智能|模型|机器).{0,10}(?:生成|撰写|创作)', 'AI生成声明'),
    (r'我(?:是|属于|作为).{0,10}(?:AI|人工智能|语言模型|大模型|虚拟|数字人)', 'AI身份声明'),
    (r'我(?:无法|不能|没法).{0,15}(?:访问|浏览|联网|上网|获取实时|预测未来)', 'AI拒答话术'),
    (r'作为(?:AI|语言模型|人工智能).{0,20}(?:不能|无法|不应|没有)', 'AI拒答话术'),
    (r'我(?:没有|不具备).{0,10}(?:主观|个人|情绪|感情|偏见).{0,10}(?:判断|观点|看法)', 'AI身份声明'),
    (r'如果(?:您|你).{0,10}(?:还有|有其他).{0,10}(?:问题|疑问|需要).{0,15}(?:随时|欢迎|可以).{0,10}(?:提问|咨询|联系)', '客服式结尾'),
    (r'希望(?:我的|以上).{0,10}(?:回答|回复|解答).{0,10}(?:对您|能帮|有所帮助)', '客服式结尾'),
    (r'感谢(?:您的|你|大家).{0,10}(?:阅读|观看|聆听|关注|支持)', '客服式结尾'),
    (r'本助手', 'AI身份声明'),
]

# 【警告】模板化元话语/套话——提示修改，不阻塞
WARNING_WORDS = [
    '值得注意的是', '需要指出的是', '不难发现', '众所周知', '毋庸置疑',
    '不言而喻', '综上所述', '总而言之', '总的来说', '归根结底',
    '一言以蔽之', '简而言之', '换句话说', '与此同时', '在此基础上',
    '在当今', '随着社会的发展', '在这个', '的时代背景下',
    '具有重要意义', '起到了关键作用', '扮演着重要角色', '产生了深远影响',
    '有着不可替代的作用', '占据着举足轻重的地位',
    '让我们一起来看看', '首先我们需要', '接下来我将',
    '赋能', '抓手', '闭环', '底层逻辑', '颗粒度', '生态位',
    '这不仅是', '更是', '不仅……而且',
    '据悉', '据了解', '有观点认为', '有研究表明',
    '引发了广泛关注', '引发了热议', '成为了热门话题',
    '笔者', '作为一名', '作为一个',
    '在当今这个', '在如今这个', '曾几何时',
    '有力推进', '圆满完成', '再创佳绩', '砥砺前行', '不忘初心',
    '家人们', '太炸裂了', '直接封神', '赢麻了', '绝绝子',
    # 无名泛指（epistemic：gestured-at sources）
    '研究表明', '调查显示', '数据显示', '据统计', '专家认为',
    '专家表示', '业内人士表示', '业内人士指出', '专家指出', '权威人士',
]

# 【警告】句式模式
WARNING_PATTERNS = [
    (r'不是.{1,15}[，,].{0,5}而是', '平行否定"不是…而是…"'),
    (r'不仅.{1,20}而且', '"不仅…而且…"'),
    (r'一方面.{1,30}另一方面', '"一方面…另一方面…"'),
    (r'在.{1,10}的同时', '"在…的同时"'),
    (r'这使得.{1,10}能够', '翻译腔"这使得…能够…"'),
    (r'进行(?:讨论|分析|研究|调查|探索|评估|优化|改进|处理)', '名词化"进行+动词"'),
    (r'做出了?.{0,6}(?:决定|判断|选择|贡献|努力)', '名词化"做出了…"'),
    (r'被(?:认为|称为|视为|广泛关注|誉为)', '被动成瘾'),
    (r'——[^—]{10,}——', '破折号插入'),
]

# 【警告】hedge 过度（AI 默认 hedge，即使该确定时）
HEDGE_WORDS = ['可能', '或许', '也许', '似乎', '大概', '大致',
               '在一定程度上', '某种意义上', '一般来说', '通常来说', '往往', '往往来说']

# 【警告】占位符
PLACEHOLDER_PATTERNS = [
    r'TODO', r'XXX+', r'待补充', r'待完善', r'占位',
    r'example\.com', r'在这里写', r'此处省略',
    r'图为某某', r'封面图注',
]


def split_sentences(text: str) -> list:
    """按中文/英文标点切分句子，返回非空句子列表。"""
    text = re.sub(r'\s+', '', text)  # 去掉空白，避免影响句子长度
    parts = re.split(r'[。！？!?…；;]', text)
    return [p for p in parts if len(p) > 0]


def compute_burstiness(text: str) -> dict:
    """计算句子长度方差（burstiness）。
    人类写作句子长短剧烈交替（CV 高），AI 写作句子长度高度均匀（CV 低）。
    返回 {sentences, cv, mean, verdict}。
    """
    sents = split_sentences(text)
    if len(sents) < 8:
        return {'sentences': len(sents), 'cv': None, 'mean': None,
                'verdict': '句子太少，无法判断节奏'}

    lengths = [len(s) for s in sents]
    mean = statistics.mean(lengths)
    if mean == 0:
        return {'sentences': len(sents), 'cv': 0.0, 'mean': 0.0,
                'verdict': '异常'}

    cv = statistics.pstdev(lengths) / mean  # 变异系数 = 标准差/均值

    if cv >= 0.55:
        verdict = '节奏自然（句子长短有落差，接近人类写作）'
    elif cv >= 0.35:
        verdict = '节奏偏均匀（建议增加长短句落差）'
    else:
        verdict = '机器节奏（句子长度高度均匀，AI 味重，必须调整）'

    return {'sentences': len(sents), 'cv': round(cv, 3), 'mean': round(mean, 1),
            'verdict': verdict}


def compute_pronoun_ratio(text: str) -> dict:
    """代词分布：AI 倾向滥用"我们"，少用"我/你"。"""
    we = len(re.findall(r'我们', text))
    wo = len(re.findall(r'我', text)) - we  # 去掉"我们"里的"我"
    you = len(re.findall(r'你', text))
    total_chars = len(re.findall(r'[\u4e00-\u9fff]', text)) or 1
    we_density = round(we / (total_chars / 1000), 1)
    return {'我们': we, '我': max(wo, 0), '你': you, '我们密度': we_density}


def compute_hedge_density(text: str) -> dict:
    """hedge 密度：每 1000 字出现多少 hedge 词。AI 默认 hedge。"""
    total = len(re.findall(r'[\u4e00-\u9fff]', text)) or 1
    count = 0
    hits = []
    for w in HEDGE_WORDS:
        n = text.count(w)
        if n > 0:
            count += n
            hits.append((w, n))
    density = round(count / (total / 1000), 2)
    return {'count': count, 'density': density, 'hits': hits}


def scan(text: str) -> dict:
    results = {'severe': [], 'warnings': [], 'placeholders': [],
               'burstiness': None, 'pronoun': None, 'hedge': None}

    # 严重问题
    for pattern, label in SEVERE_PATTERNS:
        for m in re.finditer(pattern, text):
            ctx = get_context(text, m.start(), m.end())
            results['severe'].append((label, m.group(), ctx))

    # 警告词
    for word in WARNING_WORDS:
        start = 0
        while True:
            idx = text.find(word, start)
            if idx == -1:
                break
            ctx = get_context(text, idx, idx + len(word))
            results['warnings'].append(('套话/黑话', word, ctx))
            start = idx + len(word)

    # 警告句式
    for pattern, label in WARNING_PATTERNS:
        for m in re.finditer(pattern, text):
            ctx = get_context(text, m.start(), m.end())
            results['warnings'].append((label, m.group(), ctx))

    # 占位符
    for pattern in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            ctx = get_context(text, m.start(), m.end())
            results['placeholders'].append((m.group(), ctx))

    # 结构层检查
    results['burstiness'] = compute_burstiness(text)
    results['pronoun'] = compute_pronoun_ratio(text)
    results['hedge'] = compute_hedge_density(text)

    return results


def get_context(text: str, start: int, end: int, radius: int = 18) -> str:
    s = max(0, start - radius)
    e = min(len(text), end + radius)
    ctx = text[s:e].replace('\n', ' ')
    prefix = '…' if s > 0 else ''
    suffix = '…' if e < len(text) else ''
    return f'{prefix}{ctx}{suffix}'


def main():
    if len(sys.argv) < 2:
        print('用法：python3 scan_ai.py <file>')
        sys.exit(2)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f'错误：文件不存在：{filepath}')
        sys.exit(2)
    except Exception as e:
        print(f'错误：{e}')
        sys.exit(2)

    # 去除HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    results = scan(text)

    print(f'扫描文件：{filepath}')
    print('=' * 50)

    # 严重问题
    if results['severe']:
        print(f'\n❌ 【严重】AI身份声明/拒答话术（{len(results["severe"])}处，必须修复）：')
        for label, match, ctx in results['severe']:
            print(f'  [{label}] "{match}"')
            print(f'    上下文：{ctx}')
    else:
        print('\n✅ 未发现AI身份声明')

    # 警告：套话 + 句式
    if results['warnings']:
        print(f'\n⚠️  【警告】模板化表达（{len(results["warnings"])}处，建议修改）：')
        shown = set()
        for label, match, ctx in results['warnings']:
            key = (label, match)
            if key in shown:
                continue
            shown.add(key)
            print(f'  [{label}] "{match}"')
            print(f'    上下文：{ctx}')
    else:
        print('\n✅ 未发现模板化套话')

    # 占位符
    if results['placeholders']:
        print(f'\n⚠️  【警告】占位符残留（{len(results["placeholders"])}处）：')
        for match, ctx in results['placeholders']:
            print(f'  "{match}"')
            print(f'    上下文：{ctx}')
    else:
        print('\n✅ 未发现占位符残留')

    # 结构层检查
    print('\n' + '─' * 50)
    print('【结构层检查】（认知特征，比词汇更难伪装）')

    b = results['burstiness']
    print(f'\n· 句子长度方差（burstiness）：CV = {b["cv"]}（{b["sentences"]}句，平均句长 {b["mean"]}字）')
    print(f'  → {b["verdict"]}')

    p = results['pronoun']
    print(f'\n· 代词分布：我们×{p["我们"]}，我×{p["我"]}，你×{p["你"]}（"我们"密度 {p["我们密度"]}/千字）')
    we_heavy = p['我们'] >= 8 or p['我们密度'] >= 15
    if we_heavy and (p['我'] + p['你']) <= p['我们']:
        print(f'  ⚠️  "我们"滥用：出现 {p["我们"]} 次（密度 {p["我们密度"]}/千字），但"我/你"很少。')
        print(f'     AI 倾向用"我们"制造集体口号，建议把部分"我们"换成具体的"我"或"你"。')
    elif p['我们'] >= 15 or p['我们密度'] >= 25:
        print(f'  ⚠️  "我们"出现 {p["我们"]} 次，偏多，检查是否有重复的集体口号式表达。')
    else:
        print(f'  ✅ 代词分布正常')

    h = results['hedge']
    print(f'\n· hedge 密度：{h["density"]} 次/千字（共 {h["count"]} 处）')
    if h['density'] >= 6:
        print(f'  ⚠️  hedge 过度：AI 默认 hedge（"可能""或许""在一定程度上"），即使该确定时也含糊。')
        print(f'     确定的地方直接断言，删掉不必要的 hedge。')
    else:
        print(f'  ✅ hedge 密度正常')

    print('\n' + '=' * 50)

    # 综合结论
    has_structure_issue = (
        (b['cv'] is not None and b['cv'] < 0.35) or
        (h['density'] >= 6)
    )
    if results['severe']:
        print('结论：❌ 未通过——存在AI身份声明，必须修复后才能交付')
        sys.exit(1)
    elif results['warnings'] or results['placeholders'] or has_structure_issue:
        print('结论：⚠️  基本通过——建议处理警告项后交付')
        sys.exit(0)
    else:
        print('结论：✅ 通过')
        sys.exit(0)


if __name__ == '__main__':
    main()
