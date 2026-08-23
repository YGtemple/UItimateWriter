---
name: ultimate-writing
description: 全品类中文写作系统。当用户需要写文章、写稿、创作、改写、润色、去AI味、仿写风格时使用。覆盖公众号长文、议论文、报告总结、科研论文、技术科普、营销文案、短视频脚本、网文小说、经验贴，以及文风定制（女娲风格提取/文艺/商务/口语/学术）、重度去AI重构、逻辑修复、节奏调整、去重去同质化。触发词包括：写文章、写稿、写作、润色、改写、去AI味、去味、humanize、仿写、模仿风格、写小说、写网文、写论文、写报告、写公众号、写文案、写脚本、polish、rewrite。
---

# 全品类写作系统

一个 Skill 通吃全品类写作：去AI味、文风定制、小说、论文、公众号、报告、文案、改写润色、自查。

## 核心原则

**先像人，再像文章。** 好文字听起来像一个聪明的真人在思考、在说话，而不是一台机器在输出"平衡、全面、专业"的正确废话。

**具体碾压抽象。** "一份卖38块，比去年贵11块"永远胜过"价格涨幅明显"。

**减法优先。** 六个字能说清的事，不要用十二个字。能删的一律删。

**事实零容忍编造。** 所有数字、日期、人名、机构名、引语必须来自真实素材或用户提供。宁可短，不可编。

## 工作流

### 第1步：识别需求

判断用户要做什么，缺关键参数时只问最必要的问题（主题、用途、字数、文风、立场），不打断节奏。

### 第2步：加载内核（每次必做）

写任何正文前，读取并遵守：
- `core/core-humanize.md` — 去AI味内核（表层词汇 + 话语结构 + 中文特有 + 人类纹理）
- `core/core-rules.md` — 写作铁律
- `core/core-self-check.md` — 分级自检体系

### 第3步：按需加载场景模块（只加载一个）

根据用户需求，**只读取对应的一个 mode 文件**，禁止多文件混用：

| 用户要什么 | 加载文件 |
|---|---|
| 公众号长文、深度文章、爆款文 | `mode/mode-wechat.md` |
| 议论文、感悟文、美文、时评 | `mode/mode-essay.md` |
| 工作报告、总结、汇报、纪要 | `mode/mode-report.md` |
| 科研论文、学术写作、文献综述 | `mode/mode-paper.md` |
| 技术科普、知识解析、教程 | `mode/mode-tech.md` |
| 种草文案、营销文案、带货文、广告 | `mode/mode-copy.md` |
| 短视频脚本、口播文案、直播话术 | `mode/mode-video.md` |
| 网文小说、长篇连载、短篇故事 | `mode/mode-novel.md` |
| 考研/考公/学习/上岸经验贴 | `mode/mode-experience.md` |

如果用户只说"帮我写点东西"但没说类型，根据主题和语境判断；判断不了就问一句。

### 第4步：按需叠加文风（可选，最多一个）

用户指定文风或提供风格样本时，叠加一个 style 文件：

| 文风需求 | 加载文件 |
|---|---|
| 模仿某作者/某品牌/某人风格、提取文风 | `style/style-nuwa.md`（女娲风格提取与复刻） |
| 文艺、高级、有质感、文学性 | `style/style-literary.md` |
| 商务、稳重、专业、职场 | `style/style-business.md` |
| 口语化、接地气、像聊天、真人口播 | `style/style-oral.md` |
| 学术、严谨、克制、正式 | `style/style-academic.md` |

用户提供了风格样本（过往文章/逐字稿/截图文字）但没说具体风格名，走 `style/style-nuwa.md` 提取。

### 第5步：按需加载改写模块（用户要求改写/润色时）

用户的请求是"改写/润色/优化/去AI/修逻辑"而非从零写时，加载对应 revise 文件：

| 改写需求 | 加载文件 |
|---|---|
| 去AI味、去味、太AI了、像ChatGPT写的 | `revise/revise-deai.md` |
| 润色、文笔提升、改得更好、polish | `revise/revise-polish.md` |
| 逻辑不通、论证有问题、结构乱 | `revise/revise-logic.md` |
| 节奏问题、太密/太散、长短句调整 | `revise/revise-rhythm.md` |
| 重复、同质化、段落雷同、去重 | `revise/revise-dedup.md` |

改写类任务：先读 `core/` 三个内核文件，再读对应的一个 revise 文件，再读原文对应的 mode 文件（了解场景规范）。

### 第6步：按需参考模板和词表

- 需要结构大纲时，读 `templates/` 下对应模板
- 需要选题、想标题时（公众号/小红书/短视频/知乎/文案），读 `references/ref-title-topic.md`
- 需要查禁用词时，读 `references/ref-banned-words.md`
- 需要前后对照案例时，读 `references/ref-before-after.md`
- 写非虚构内容需要核查事实、评估来源时，读 `references/ref-source-eval.md`
- 用户要设定人设/声音但没给样本时，读 `references/ref-voice-profiles.md`
- 需要微信 HTML 排版时，读 `references/ref-wechat-html.md`
- 写小说需要工艺细节（节奏、反转、情绪值）时，读 `references/ref-novel-craft.md`

### 第7步：写作

按加载的模块规范写作。长文分章节推进，写完一章确认方向再继续。

### 第8步：自检（定稿前必做）

按 `core/core-self-check.md` 执行分级自检。不通过就改，改到通过再交付。

## 写作铁律（以下规则任何场景不可违反）

1. **禁止编造事实。** 数字、日期、人名、引语、机构必须有来源。没有来源就不写具体数字，用模糊表达或标注待核实。
2. **禁止空话凑字。** 每句话必须携带新信息或推进论证/叙事。删掉这句话文章不受损，就删。
3. **禁止机械排比。** 不写"不是A，不是B，而是C"的三连；不写三段结构完全相同的句子；排比只在真正需要节奏时用。
4. **禁止元话语。** 不写"值得注意的是""需要指出的是""总而言之""综上所述""让我们一起来看看"。
5. **禁止空洞升华。** 结尾不喊口号，不写"在这个……的时代""让我们一起……"。
6. **禁止翻译腔。** 不写"作为一个……的人""这使得……能够……""进行+动词"。
7. **禁止AI自曝身份。** 不写"作为AI""本文由AI生成""我无法访问互联网"等。AI/大模型作为讨论对象时可以正常提及。
8. **保护作者声音。** 改写时保留原文的具体细节、对话、个人经历、独特比喻，不把活的文字压成光滑的摘要。
9. **段落要短。** 手机阅读一段不超过4行。长段落拆开。
10. **写完读一遍。** 默读全文，绊嘴的句子就改，听着像通稿的段落就重写。

## 输出规范

- 用与用户相同的语言回复（中文提问用中文）。
- 长文用 Markdown 格式交付；用户要求 HTML/Word 等其他格式时按需转换。
- 改写任务默认输出：润色后全文 + 主要修改点（3-6条）。用户只要结果就只给结果。
- 不确定的事实标注"待核实"，不假装确定。
- 不添加 emoji 除非用户要求或场景本身需要（如小红书）。

## 文件索引

```
core/
  core-humanize.md    去AI味内核（表层+话语层+中文+人类纹理）
  core-rules.md       写作铁律详解
  core-self-check.md  分级自检（P0-P4）
mode/
  mode-wechat.md      公众号长文
  mode-essay.md       议论文/感悟文
  mode-report.md      报告/总结
  mode-paper.md       科研论文
  mode-tech.md        技术科普
  mode-copy.md        营销/种草文案
  mode-video.md       短视频脚本
  mode-novel.md       网文小说
  mode-experience.md  经验贴
style/
  style-nuwa.md       女娲风格提取与复刻
  style-literary.md   文艺高级风
  style-business.md   商务稳重风
  style-oral.md       极致口语风
  style-academic.md   学术严谨风
revise/
  revise-deai.md      重度去AI重构
  revise-polish.md    高级润色
  revise-logic.md     逻辑修复
  revise-rhythm.md    节奏调整
  revise-dedup.md     去重去同质
references/
  ref-banned-words.md 禁用词总表（中英）
  ref-before-after.md 前后对照案例
  ref-title-topic.md  选题与标题方法论
  ref-source-eval.md  来源评估与事实核查
  ref-voice-profiles.md 声音画像（5种人设）
  ref-wechat-html.md  微信排版规范（内联样式）
  ref-novel-craft.md  小说工艺细节
templates/
  tpl-wechat.md       公众号长文模板
  tpl-report.md       报告模板
  tpl-paper.md        论文模板
  tpl-novel.md        小说章节模板
  tpl-video.md        短视频脚本模板
scripts/
  word_count.py       中文字数统计
  scan_ai.py          AI痕迹扫描
```
