# Ultimate Writing · 全品类写作 Skill

一个 Skill 通吃全品类中文写作：去AI味、文风定制、小说、论文、公众号、报告、文案、改写润色、自查。

融合 30+ 个 GitHub 顶级写作 Skill 的方法论，单入口 + 按需加载，不爆上下文。

## 特性

- **全品类覆盖**：公众号长文、议论文、报告总结、科研论文、技术科普、营销文案、短视频脚本、网文小说、经验贴
- **三层去AI味**：表层（词汇/句式）+ 话语层（结构/开头/结尾/叙事方式）+ 认知层（句子长度方差、代词分布、hedge、情绪具体性），不只换词，连结构和底层特征一起改
- **选题与标题方法论**：四个价值锚点、爆款选题公式、五类高打开率选题、六类标题公式
- **女娲文风系统**：从样本提取 5 维风格画像（词汇/句法/段落/修辞/声音），复刻任意作者或品牌文风
- **5 种文风 + 5 种声音画像**：文艺、商务、口语、学术 + 女娲自定义；直接/温和/权威/叙述/对话五种人设
- **5 种改写模式**：重度去AI、高级润色、逻辑修复、节奏调整、去重去同质
- **分级自检 + 量化质量门**：P0-P4 五级严重度，外加直接/节奏/可信/真诚/密度五维打分（低于 35/50 打回重写）
- **来源评估与事实核查**：来源四级分级、交叉验证、事实/观点/宣传区分
- **微信排版规范**：内联样式组件体系、十套主题配色、公众号粘贴不丢样式
- **中文优先**：针对中文 AI 味（翻译腔、的的不休、互联网黑话、欧化长句、代词滥用）专门设计
- **按需加载**：主入口约 8.5KB，每次只加载一个场景模块，单次最大加载约 45KB，不爆 64KB 限制
- **工具脚本**：中文字数统计、AI痕迹扫描（含结构层检测）

## 安装

### Claude Code

```bash
# 克隆到 skills 目录
git clone https://github.com/你的用户名/ultimate-writing.git ~/.claude/skills/ultimate-writing
```

### Codex / 其他支持 SKILL.md 的 Agent

```bash
# 复制到你的 skills 目录
cp -r ultimate-writing ~/.codex/skills/
```

### 手动安装

1. 下载本仓库
2. 将整个文件夹放入你的 Agent skills 目录
3. 重启 Agent 或重新加载 skills

## 使用

直接用自然语言告诉 Agent 你的写作需求即可：

```
帮我写一篇关于AI取代客服的公众号文章，3000字，口语化风格

帮我把这段文字去AI味

用文艺的文风写一篇关于老城区拆迁的散文

帮我润色这份Q3工作报告

模仿我之前文章的风格写一篇新的（粘贴你的样本）

帮我写一篇短视频脚本，主题是时间管理，60秒

帮我写小说第三章，前面的设定是……
```

Agent 会自动识别需求，加载对应的场景模块和文风模块。

## 架构

```
ultimate-writing/
├── SKILL.md                    # 主入口+路由器（约8.5KB）
├── README.md
├── LICENSE
├── core/                       # 内核层（每次必加载）
│   ├── core-humanize.md        # 去AI味内核（表层+话语层+中文+人类纹理）
│   ├── core-rules.md           # 写作铁律
│   └── core-self-check.md      # 分级自检（P0-P4）
├── mode/                       # 场景层（按需加载一个）
│   ├── mode-wechat.md          # 公众号长文
│   ├── mode-essay.md           # 议论文/感悟文
│   ├── mode-report.md          # 报告/总结
│   ├── mode-paper.md           # 科研论文
│   ├── mode-tech.md            # 技术科普
│   ├── mode-copy.md            # 营销/种草文案
│   ├── mode-video.md           # 短视频脚本
│   ├── mode-novel.md           # 网文小说
│   └── mode-experience.md      # 经验贴
├── style/                      # 文风层（可选叠加一个）
│   ├── style-nuwa.md           # 女娲风格提取与复刻
│   ├── style-literary.md       # 文艺高级风
│   ├── style-business.md       # 商务稳重风
│   ├── style-oral.md           # 极致口语风
│   └── style-academic.md       # 学术严谨风
├── revise/                     # 改写层（按需加载一个）
│   ├── revise-deai.md          # 重度去AI重构
│   ├── revise-polish.md        # 高级润色
│   ├── revise-logic.md         # 逻辑修复
│   ├── revise-rhythm.md        # 节奏调整
│   └── revise-dedup.md         # 去重去同质
├── references/                 # 参考资料（按需查阅）
│   ├── ref-banned-words.md     # 禁用词总表（中英）
│   ├── ref-before-after.md     # 前后对照案例
│   ├── ref-title-topic.md      # 选题与标题方法论
│   ├── ref-source-eval.md      # 来源评估与事实核查
│   ├── ref-voice-profiles.md   # 声音画像（5种人设）
│   ├── ref-wechat-html.md      # 微信排版规范（内联样式）
│   └── ref-novel-craft.md      # 小说工艺细节
├── templates/                  # 结构模板（按需使用）
│   ├── tpl-wechat.md
│   ├── tpl-report.md
│   ├── tpl-paper.md
│   ├── tpl-novel.md
│   └── tpl-video.md
└── scripts/                    # 工具脚本
    ├── word_count.py           # 中文字数统计
    └── scan_ai.py              # AI痕迹扫描
```

## 工作流

1. **识别需求**：判断写作类型、字数、文风、立场
2. **加载内核**：去AI味规则 + 写作铁律 + 自检体系
3. **加载场景**：只加载对应的一个 mode 文件
4. **叠加文风**：可选加载一个 style 文件
5. **加载改写模块**：改写任务加载对应 revise 文件
6. **写作**：按规范写作
7. **自检**：P0-P4 分级自检，不通过就改
8. **交付**：成品 + 自检结果

## 工具脚本

### 字数统计

```bash
python3 scripts/word_count.py article.md --min 2000 --max 5000
```

统计口径：中文字符 + 英文单词 + 数字串，与 Word/WPS 一致。

### AI痕迹扫描

```bash
python3 scripts/scan_ai.py article.md
```

扫描 AI 身份声明（严重）、模板化套话（警告）、占位符残留（警告），以及结构层特征（句子长度方差、无名泛指、代词"我们"滥用、hedge 密度）。

## 设计理念

### 三层去AI味

只换词不够。研究显示，即使把AI文章的所有禁用词换掉，仅靠话语结构特征（开头方式、结尾方式、是否留悬念、是否有具体人名数字）仍能以超过90%的准确率识别出AI写作。更进一步，2025-2026 年的检测研究把 AI 痕迹分成五类线索，其中最底层、最难伪装的是认知特征：句子长度方差（burstiness）、代词分布、hedge 时机、情绪具体性。

所以本 Skill 分三层清理：

1. **表层**：词汇、句式、标点。
2. **话语层**：开头、结尾、推进方式、叙事结构。
3. **认知层**：burstiness、代词、"我们"滥用、hedge 悖论、情绪具体性缺失。

三层全过，才真正读起来像人。

### 减法优先

80%的AI味靠删就能解决。不编造"人类纹理"来假装真人——宁可短，不可假。

### 保护作者声音

改写时保留原文的具体细节、对话、个人经历、独特比喻。不把活的文字压成光滑的摘要。

### 事实零容忍编造

所有数字、日期、人名、引语必须有来源。宁可写"待核实"，不编。

## 致谢

本 Skill 的方法论融合了以下开源项目的精华：

- [blader/humanizer](https://github.com/blader/humanizer)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)
- [avectats7/anti-ai-writing](https://github.com/avectats7/anti-ai-writing)
- [lguz/humanize-writing-skill](https://github.com/lguz/humanize-writing-skill)
- [woderfulmagic/humanized-chinese-writing-polisher](https://github.com/woderfulmagic/humanized-chinese-writing-polisher)
- [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill)
- [KKKKhazix/Khazix-Skills](https://github.com/KKKKhazix/Khazix-Skills)
- [jimliu/baoyu-skills](https://github.com/jimliu/baoyu-skills)
- [kaiak-io/claude-code-skills](https://github.com/kaiak-io/claude-code-skills)
- [wgwtest/novel-writing](https://github.com/wgwtest/novel-writing)
- [mou-fang/fictionist-skill](https://github.com/mou-fang/fictionist-skill)
- [imerzzhu/ai-novel-writing-skills](https://github.com/imerzzhu/ai-novel-writing-skills)
- [li-debug-eng/write-compliant-fiction-serial](https://github.com/li-debug-eng/write-compliant-fiction-serial)
- [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)
- [lianjx2025/humanize](https://github.com/lianjx2025/humanize)

## License

MIT
