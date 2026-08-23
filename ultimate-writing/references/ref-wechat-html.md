# 微信排版规范（HTML 内联样式）

当用户需要把文章排版成可直接粘贴到微信公众号后台、且样式不丢失的 HTML 时，用本文件。默认交付 Markdown，用户明确要 HTML 时才走这里。

核心约束：**所有样式必须内联（`style="..."`）**。禁止 `<style>` 标签、class、id、JS、外链 CSS、`position`、浮动。公众号后台只认内联样式。

---

## 一、基础排版参数

| 参数 | 推荐值 | 说明 |
|---|---|---|
| 字号 | 15-17px（正文） | 15 偏精致，17 偏舒适，中老年向偏大 |
| 行高 | 1.75-2.0 | 太密压眼，太松散 |
| 段间距 | 1 行（约 8-12px） | 空一行分隔 |
| 容器宽度 | max-width 677px 居中 | 手机屏舒适宽度 |
| 配色 | ≤ 3 种 | 主色 + 灰 + 强调色，多了显乱 |
| 段落 | 一段不超过 4 行 | 手机屏一屏塞不下两段 |
| 字体 | 系统字体栈 | 不指定花哨字体（手机端不生效） |

## 二、组件体系（全部内联 style 实现）

用组件打破长文节奏，避免"一坨纯文字"。常用组件：

1. **章节卡片标题**：浅色底 + 左侧 6px 主色竖条 + 可选胶囊标签。每章 1 个。
2. **小节标题**：小色块 + 文字。每章 2-4 个。
3. **彩色标签段落**：蓝=定义、绿=解析、橙=影响、红=警示。全文 5-15 次。
4. **金句卡片**：米色底 + 金色左边线 + 斜体引语 + 出处。每章 1-2 个。
5. **数据卡片**：大数字（主色、26px）+ 说明（灰、12px），三列。全文 2-5 次。
6. **纵向时间线**：竖线 + 圆点 + 年份 + 一句话。需要时间叙事时 1 次。
7. **要点列表**：`▪` 符号 + 缩进。每章 0-1 组。
8. **配图容器**：圆角 8px + 居中图注。每 1500-3000 字 1 张。
9. **分隔符**：居中 `・・・`。章节间或转折处。
10. **参考资料**：灰底块，纯文字不放链接。
11. **作者署名区**：头像 + 名字 + 简介 + 全文完。

### 内联样式示例

```html
<!-- 章节卡片标题 -->
<div style="background:#eef4f1;border-left:6px solid #2d5f4f;padding:12px 16px;margin:24px 0 12px;font-size:18px;font-weight:bold;color:#1f3b33;">一、发生了什么</div>

<!-- 金句卡片 -->
<div style="background:#faf9f5;border-left:4px solid #c9b879;padding:14px 18px;margin:16px 0;font-style:italic;color:#444;">「真正的问题不在于技术，而在于人愿不愿意改变。」</div>

<!-- 数据卡片（三列用 table） -->
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr>
<td style="text-align:center;padding:10px;"><div style="font-size:26px;font-weight:bold;color:#2d5f4f;">23%</div><div style="font-size:12px;color:#999;">用户增长</div></td>
<td style="text-align:center;padding:10px;"><div style="font-size:26px;font-weight:bold;color:#2d5f4f;">410</div><div style="font-size:12px;color:#999;">企业客户</div></td>
<td style="text-align:center;padding:10px;"><div style="font-size:26px;font-weight:bold;color:#2d5f4f;">91%</div><div style="font-size:12px;color:#999;">续费率</div></td>
</tr></table>
```

## 三、配图规范

- **图注是正文延伸，不是图片说明。**
  - 好："这家开在巷子里的小店，菜单已经换了三回。"
  - 差："图为某店铺照片。"
- **网络搜图标注"图源：某某平台"**，发布前提醒用户重新上传（避免外链失效）。
- **AI 生成图不要求生成文字**（模型生成中文常出错）。
- **必须真实的实体（人物/产品/地点）用真实图片，不用 AI 生成。**

## 四、主题配色（十套）

| 主题 | 主色 | 主色浅底 | 主色高亮 |
|---|---|---|---|
| bamboo 竹青（默认） | #2d5f4f | #eef4f1 | #dcebe5 |
| tech-blue 科技蓝 | #1f6fb5 | #eaf2f9 | #d5e6f4 |
| warm-orange 暖橙 | #d97706 | #fdf3e7 | #f8e3c7 |
| forest 森林绿 | #2f7d4f | #edf6f0 | #d7ebde |
| elegant-purple 典雅紫 | #7c5cbf | #f1edf9 | #e3dbf2 |
| china-red 中国红 | #c0392b | #fbeceb | #f4d7d4 |
| ink-dark 墨黑 | #34495e | #eef1f4 | #dde3e9 |
| sunset 日落橘 | #e0643a | #fcefeb | #f7dcd2 |
| teal 青蓝 | #0f766e | #e8f4f2 | #d1e8e5 |
| rose 玫红 | #be4977 | #f9edf3 | #f0d7e3 |

蓝=定义、绿=解析、橙=影响、红=警示 四个功能标签色固定不变，不随主题切换。

**换色原则**：主题只换"主色、主色浅底、主色高亮"三个值，功能标签色和布局不动。手动改色容易漏，建议定稿后用脚本批量替换，不逐处手改。

## 五、禁止项（公众号后台会丢样式/报错）

- ❌ `<style>` 标签、外部 CSS 文件
- ❌ `class` / `id` 选择器
- ❌ JavaScript
- ❌ `position: absolute/fixed`（时间线等用 margin 实现，不用 position）
- ❌ 浮动 `float`
- ❌ 外链图片（发布后易失效，需重新上传）
- ❌ 过于花哨的动画、特效

## 自检清单

- [ ] 所有样式都内联了吗？有没有 `<style>` 或 class？
- [ ] 容器宽度、字号、行高、段距符合规范吗？
- [ ] 配色 ≤ 3 种吗？
- [ ] 有没有用组件打破长文节奏（不是一坨纯文字）？
- [ ] 图注是正文延伸吗？
- [ ] 网络搜图标注图源、提醒重新上传了吗？
- [ ] 有没有 position/float/JS？
- [ ] 复制到公众号后台测试过不丢样式吗？
