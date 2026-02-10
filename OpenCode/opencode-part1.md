# OpenCode 入门指南 - 第一部分：基础概念和安装

> 预计学习时间：1-2 小时
> 难度：⭐☆☆☆☆

---

## 1.1 OpenCode 是什么

**OpenCode** 是一个 100% 开源的 AI 编程智能体，类似于 Claude Code 或 Cursor 的 Agent 功能，但完全开源、隐私优先。

### 核心特点

- ✅ **完全开源**：代码在 GitHub 上公开，自由修改
- ✅ **隐私优先**：支持本地运行，数据不离开你的机器
- ✅ **多模型支持**：通过 AI SDK 支持 75+ LLM 提供商
- ✅ **多种使用方式**：终端、桌面应用、IDE 扩展
- ✅ **智能 Agent**：内置 build 和 plan 两种模式

### 内置 Agents

OpenCode 包含两种内置 agent，可以用 Tab 键切换：

- **build**：默认的完全访问 agent，用于开发工作
- **plan**：只读 agent，用于分析和代码探索
  - 默认拒绝文件编辑
  - 运行 bash 命令前会请求权限
  - 适合探索不熟悉的代码库或规划变更

### 与 Claude Code 的区别

| 特性 | Claude Code | OpenCode |
|------|-------------|----------|
| 开源 | ❌ 闭源 | ✅ 完全开源 |
| 价格 | 付费订阅 | ✅ 完全免费 |
| 隐私 | 云端处理 | ✅ 支持本地运行 |
| 定制 | ❌ 不可定制 | ✅ 高度可定制 |
| 模型 | 仅 Claude | ✅ 75+ LLM 提供商 |

---

## 1.2 为什么选择 OpenCode

### 适用场景

✅ **适合你使用 OpenCode：**
- 想要免费替代 Claude Code
- 关注数据隐私，希望本地化部署
- 需要使用不同的 LLM 提供商
- 团队需要统一的 AI 编程工具

❌ **不适合你使用 OpenCode：**
- 需要开箱即用的云服务
- 不愿意花时间配置环境
- 需要官方技术支持

### 核心优势

1. **成本优势**
   - 无订阅费用
   - 开源免费使用
   - 可部署在自己的服务器上

2. **隐私优势**
   - 支持本地模型（通过 Ollama 等）
   - 凭证本地存储
   - 数据完全可控

3. **灵活优势**
   - 支持 75+ LLM 提供商
   - 可自定义工作流
   - 企业级配置能力

---

## 1.3 环境要求

### 必需环境

- **操作系统**：macOS、Linux、Windows（WSL）
- **包管理器**（用于安装）：npm、Homebrew、scoop 等
- **终端**：支持 ANSI 颜色和基本交互

### 可选环境

- **IDE**：VS Code 扩展（即将推出）
- **LSP Server**：用于代码导航和诊断
  - TypeScript/JavaScript：TypeScript Language Server
  - Python：pylsp
  - Go：gopls
  - Java：Eclipse JDT Language Server

### 系统要求

- **内存**：至少 4GB RAM（推荐 8GB+）
- **存储**：至少 100MB 可用空间
- **网络**：首次运行需要下载

---

## 1.4 安装方法

### 方法 1：一键安装脚本（最简单）

```bash
curl -fsSL https://opencode.ai/install | bash
```

这个脚本会自动检测你的操作系统并安装适合的版本。

### 方法 2：使用 Homebrew（推荐 macOS/Linux）

```bash
# 推荐（总是最新版本）
brew install anomalyco/tap/opencode

# 或者使用官方 brew formula（更新较慢）
brew install opencode

# 桌面应用
brew install --cask opencode-desktop
```

### 方法 3：使用 npm（跨平台）

```bash
npm i -g opencode-ai@latest
# 或使用 bun/pnpm/yarn
```

### 方法 4：其他包管理器

```bash
# Windows (Scoop)
scoop install opencode

# Windows (Chocolatey)
choco install opencode

# Arch Linux
paru -S opencode-bin

# 使用 mise
mise use -g opencode

# 使用 nix
nix run nixpkgs#opencode
```

### 方法 5：从源码编译（高级用户）

```bash
# 1. 克隆仓库
git clone https://github.com/anomalyco/opencode.git
cd opencode

# 2. 安装依赖并运行（需要 Bun）
bun install
bun run packages/opencode/src/index.ts
```

### 验证安装

```bash
opencode --version
```

如果显示版本号，说明安装成功。

---

## 1.5 首次配置

### 配置文件位置

OpenCode 使用 JSON 或 JSONC（JSON with Comments）格式的配置文件。

**配置文件优先级（从低到高）：**

1. Remote config（从 .well-known/opencode）- 组织默认配置
2. Global config（~/.config/opencode/opencode.json）- 用户偏好
3. Custom config（OPENCODE_CONFIG 环境变量）- 自定义覆盖
4. Project config（项目中的 opencode.json）- 项目特定设置
5. .opencode 目录 - agents、commands、plugins
6. Inline config（OPENCODE_CONFIG_CONTENT 环境变量）- 运行时覆盖

### 创建全局配置

```bash
# 创建配置目录
mkdir -p ~/.config/opencode

# 创建配置文件
touch ~/.config/opencode/opencode.json
```

### 基本配置示例

```json
{
  "$schema": "https://opencode.ai/config.json",
  "theme": "opencode",
  "model": "anthropic/claude-sonnet-4-5",
  "autoupdate": true
}
```

### 添加凭证

OpenCode 不直接在配置文件中存储 API 密钥，而是使用 `/connect` 命令安全添加：

```bash
# 启动 OpenCode
opencode

# 在 OpenCode 中运行
/connect
```

这会引导你连接到支持的 LLM 提供商（OpenAI、Anthropic 等）。

### 推荐的模型

OpenCode 支持 75+ LLM 提供商，以下是推荐的擅长代码生成和工具调用的模型：

- **GPT 5.2**
- **GPT 5.1 Codex**
- **Claude Opus 4.5**
- **Claude Sonnet 4.5**
- **Gemini 3 Pro**
- **Minimax M2.1**

### 模型配置格式

模型 ID 格式为：`provider_id/model_id`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5"
}
```

如果使用自定义 provider，则使用配置中的 key。

---

## 1.6 第一个对话

### 启动 OpenCode

```bash
# 在项目目录中启动
cd /path/to/your/project
opencode
```

### 基本交互

首次启动时，OpenCode 会提示你连接到 LLM 提供商：

```
Welcome to OpenCode! 🚀

OpenCode helps you build, refactor, and understand code.

To get started, please connect to an LLM provider.

Run /connect to begin.
```

### 连接到提供商

运行 `/connect` 命令后，你会看到可用的提供商列表：

```
Available providers:

1. OpenAI
2. Anthropic
3. Google
4. Azure OpenAI
5. Custom provider

Select a provider to connect:
```

选择提供商后，OpenCode 会安全地存储你的 API 密钥。

### 简单对话示例

**用户：**
```
帮我查看当前目录结构
```

**OpenCode：**
```
I'll examine the current directory structure for you.

This appears to be a web project with the following structure:

📁 /path/to/your/project
├── 📁 src/
│   ├── 📁 components/
│   │   ├── 📄 Button.tsx
│   │   └── 📄 Header.tsx
│   ├── 📄 App.tsx
│   └── 📄 index.tsx
├── 📄 package.json
├── 📄 tsconfig.json
└── 📄 README.md

Would you like me to analyze any specific file or component?
```

### 切换 Agent

你可以用 Tab 键切换 agent：

- **build agent**：默认，可以进行文件编辑和运行命令
- **plan agent**：只读，适合代码探索和分析

切换 agent：

```
按 Tab 键切换到 [plan] agent
```

---

## 🎯 本章小结

### 你学到了

- ✅ OpenCode 是什么，以及它的核心特点
- ✅ 为什么选择 OpenCode（成本、隐私、灵活性）
- ✅ 环境要求和准备工作
- ✅ 5 种安装方法（一键脚本、Homebrew、npm、其他包管理器、源码编译）
- ✅ 配置文件格式和位置
- ✅ 如何安全地添加 API 凭证
- ✅ 第一个对话如何进行
- ✅ 如何切换不同的 agent

### 下一步

进入 **第二部分：初级 - 基本使用**，学习：
- 终端模式的基本命令
- 文件操作
- 简单的代码补全
- 上下文理解

---

## 💡 常见问题

### Q: 安装后找不到 opencode 命令

**A:** 检查安装位置是否在 PATH 中：

```bash
which opencode
```

如果找不到，检查安装目录是否在 PATH 中。如果使用 Homebrew 安装，通常在 `/opt/homebrew/bin/opencode` 或 `/usr/local/bin/opencode`。

### Q: 如何添加多个 API 提供商

**A:** 你可以多次运行 `/connect` 命令来添加多个提供商。OpenCode 会安全地存储所有凭证。

### Q: 支持哪些本地模型

**A:** OpenCode 支持通过 Ollama、LM Studio 等工具运行本地模型。配置本地模型时，provider ID 通常是工具提供商的标识符。

### Q: 如何更新 OpenCode

**A:** 如果启用了 `autoupdate: true`，OpenCode 会自动检查更新。你也可以手动更新：

```bash
# Homebrew
brew upgrade opencode

# npm
npm update -g opencode-ai

# 重新运行安装脚本
curl -fsSL https://opencode.ai/install | bash
```

### Q: 桌面应用和终端版本有什么区别

**A:** 桌面应用提供了图形界面，更适合喜欢 UI 交互的用户。终端版本更轻量，适合在 SSH 会话或偏好命令行的用户。两者的功能基本相同。

---

**第一部分完成！** 🎉

准备好进入第二部分了吗？
