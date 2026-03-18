# diary-recorder

马伯庸式日记记录 Skill，适用于 Cursor / OpenClaw 等 skills-compatible agent。

体例出自《越缦堂日记》：细大必书，一事一条，日常直录。用户随时记录碎片，系统负责整理、打标签、生成日记和周总结。

## 功能

- **碎片记录**：用户说"记一下…"即可记录，系统自动打上时间和 Tag
- **每日整理**：将一天的碎片记录整理为结构化日记
- **Tag 体系**：扁平 Tag 列表，自然生长，自动匹配或新增
- **补录 & 修改**：支持补记往日条目、修改或删除已有记录
- **周总结**：按 Tag 分类汇总一周记录

## 安装

### Cursor / OpenClaw

将本仓库 clone 或 symlink 到你的 skills 目录：

```bash
# 方式一：clone
git clone https://github.com/yu-changqian/diary-recorder.git ~/.cursor/skills/diary-recorder

# 方式二：symlink（如果你已经 clone 到其他位置）
ln -s /path/to/diary-recorder ~/.cursor/skills/diary-recorder
```

### 配置

安装后打开 `SKILL.md`，修改配置段中的两个路径：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `DIARY_HOME` | `~/diary` | 日记数据存放目录 |
| `SKILL_DIR` | Skill 所在目录 | 脚本等资源的引用基准 |

大多数情况下默认值即可直接使用。

### 依赖

- Python 3（用于时间获取脚本 `scripts/now.py`）

## 使用

在对话中使用触发词即可：

| 触发词 | 效果 |
|--------|------|
| `记一下，…` / `记录，…` | 记录一条日记 |
| `整理日记` | 整理当天日记 |
| `整理 03-16 的日记` | 整理指定日期 |
| `周总结` | 生成本周总结 |
| `补记昨天，…` | 补录往日条目 |
| `改一下记录，…` | 修改已有记录 |

不使用触发词的对话不会被记录。

## 文件说明

| 文件 | 内容 |
|------|------|
| `SKILL.md` | 核心指令：流程定义、触发词、配置 |
| `diary-format.md` | 日记和周总结的格式模板 |
| `tag-system.md` | Tag 体系管理规范 |
| `examples.md` | 完整交互示例 |
| `scripts/now.py` | 本地时间获取脚本 |

## License

MIT
