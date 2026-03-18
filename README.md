# diary-recorder

马伯庸式日记记录 Skill，适用于 Claude Code、OpenClaw、Codex CLI 等 skills-compatible agent。

体例出自《越缦堂日记》：细大必书，一事一条，日常直录。用户随时记录碎片，系统负责整理、打标签、生成日记和周总结。

## 功能

- **碎片记录**：用户说"记一下…"即可记录，系统自动打上时间和 Tag
- **每日整理**：将一天的碎片记录整理为结构化日记
- **Tag 体系**：扁平 Tag 列表，自然生长，自动匹配或新增
- **补录 & 修改**：支持补记往日条目、修改或删除已有记录
- **周总结**：按 Tag 分类汇总一周记录

## 安装

### Claude Code（Marketplace）

```
/plugin marketplace add yu-changqian/diary-recorder
/plugin install diary-recorder@diary-recorder
```

### Claude Code（手动）

将本仓库 clone 到项目的 `.claude/` 目录，或添加到全局 skills 路径。

### OpenClaw / Cursor

```bash
git clone https://github.com/yu-changqian/diary-recorder.git ~/.cursor/skills/diary-recorder
```

或用 symlink：

```bash
ln -s /path/to/diary-recorder ~/.cursor/skills/diary-recorder
```

### Codex CLI

```bash
git clone https://github.com/yu-changqian/diary-recorder.git ~/.codex/skills/diary-recorder
```

### npx skills

```
npx skills add git@github.com:yu-changqian/diary-recorder.git
```

## 配置

安装后打开 `skills/diary-recorder/SKILL.md`，修改配置段中的两个路径：

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

```
diary-recorder/
├── .claude-plugin/
│   ├── plugin.json          # Claude Code 插件清单
│   └── marketplace.json     # Marketplace 目录
├── skills/
│   └── diary-recorder/
│       ├── SKILL.md          # 核心指令：流程定义、触发词、配置
│       ├── diary-format.md   # 日记和周总结的格式模板
│       ├── tag-system.md     # Tag 体系管理规范
│       ├── examples.md       # 完整交互示例
│       └── scripts/
│           └── now.py        # 本地时间获取脚本
├── README.md
└── LICENSE
```

## License

MIT

---

# diary-recorder (English)

A diary recording skill for skills-compatible agents (Claude Code, OpenClaw, Codex CLI, etc.).

Inspired by the style of *Yue Man Tang Ri Ji* (越缦堂日记): record everything, one entry per matter, plain daily logging. Users jot down fragments anytime; the system handles organizing, tagging, compiling daily diaries, and generating weekly summaries.

## Features

- **Fragment recording** — Say "记一下…" (note this down) to record; the system auto-stamps time and tags
- **Daily compilation** — Organizes a day's fragments into a structured diary entry
- **Tag system** — Flat tag list that grows organically; auto-matches existing tags or creates new ones
- **Backfill & edit** — Supports recording past entries, modifying or deleting existing records
- **Weekly summary** — Groups the week's records by tag with statistics

## Installation

### Claude Code (Marketplace)

```
/plugin marketplace add yu-changqian/diary-recorder
/plugin install diary-recorder@diary-recorder
```

### Claude Code (Manual)

Clone this repo into your project's `.claude/` directory, or add it to your global skills path.

### OpenClaw / Cursor

```bash
git clone https://github.com/yu-changqian/diary-recorder.git ~/.cursor/skills/diary-recorder
```

Or symlink:

```bash
ln -s /path/to/diary-recorder ~/.cursor/skills/diary-recorder
```

### Codex CLI

```bash
git clone https://github.com/yu-changqian/diary-recorder.git ~/.codex/skills/diary-recorder
```

### npx skills

```
npx skills add git@github.com:yu-changqian/diary-recorder.git
```

## Configuration

After installation, open `skills/diary-recorder/SKILL.md` and adjust the two paths in the configuration section:

| Variable | Default | Description |
|----------|---------|-------------|
| `DIARY_HOME` | `~/diary` | Where diary data is stored |
| `SKILL_DIR` | Skill's own directory | Base path for scripts and resources |

Defaults work out of the box in most cases.

### Dependencies

- Python 3 (for the time script `scripts/now.py`)

## Usage

Use trigger words in conversation (currently Chinese triggers):

| Trigger | Action |
|---------|--------|
| `记一下，…` / `记录，…` | Record a diary entry |
| `整理日记` | Compile today's diary |
| `整理 03-16 的日记` | Compile a specific date |
| `周总结` | Generate weekly summary |
| `补记昨天，…` | Backfill a past entry |
| `改一下记录，…` | Edit an existing record |

Conversations without trigger words are not recorded.

## File Structure

```
diary-recorder/
├── .claude-plugin/
│   ├── plugin.json          # Claude Code plugin manifest
│   └── marketplace.json     # Marketplace catalog
├── skills/
│   └── diary-recorder/
│       ├── SKILL.md          # Core instructions: workflows, triggers, config
│       ├── diary-format.md   # Daily diary and weekly summary templates
│       ├── tag-system.md     # Tag management rules
│       ├── examples.md       # Full interaction examples
│       └── scripts/
│           └── now.py        # Local time helper script
├── README.md
└── LICENSE
```

## License

MIT
