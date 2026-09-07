# Verbi Italiani · 意大利语动词变位表

自包含单文件 HTML 的意大利语动词变位查询工具。

## 特性
- **684 个主流意大利语动词**（含不规则、前缀派生、自反形式，自反与普通形式各自独立呈现）
- **完整时态体系**：直陈式 / 虚拟式 / 条件式 / 命令式 共 **15 组变位** + **6 个非人称形式**（原形、复合原形、副动词、复合副动词、现在分词、过去分词）
- **三组规则变位**：`-are` / `-ere` / `-ire`（含 `-isc` 插入、`-care/-gare` h 插入、`-ciare/-giare/-sciare` 拼写修正、`-iare` 重读/非重读区分）
- **完全不规则动词**：essere / avere / andare / stare / fare / dire / bere / dovere / potere / venire / porre / trarre / condurre / -durre 家族 等手写模型
- **零依赖**：单 HTML 文件，内嵌数据 + 变位引擎 + UI，双击即可离线使用
- **响应式**：桌面 / 手机自适应，支持中文释义搜索与 A–Z 字母索引

## 用法
直接打开 `index.html`（或 `verbo-italiano.html`）。搜索框输入动词或中文，点击字母索引快速跳转，点开动词查看全部时态。

## 重新生成
```bash
# 1) 修正 gen_italian.py 的动词数据 / 引擎后：
python3 gen_italian_html.py      # 运行 node 断言测试并生成 verbo-italiano.html
# 2) 浏览器验收（可选，需要 playwright + Edge）
python3 verify_browser.py
```

## 文件结构
| 文件 | 说明 |
|---|---|
| `gen_italian.py` | 动词数据 + JS 变位引擎（单一数据源） |
| `gen_italian_html.py` | Node 断言测试 + 序列化为自包含 HTML |
| `verbo-italiano.html` | 生成产物（单文件） |
| `index.html` | 同 `verbo-italiano.html`，供 GitHub Pages 根路径访问 |
| `verify_browser.py` | Playwright + Edge 验收脚本 |

## 部署
GitHub Pages，分支 `main`，根目录。

---
由 WorkBuddy 自动生成。
