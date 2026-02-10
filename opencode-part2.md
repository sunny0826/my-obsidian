# OpenCode 使用指南 - 第二部分：初级 - 基本使用（已更新）

> 预计学习时间：3-4 小时
> 难度：⭐⭐☆☆☆

---

## 2.1 终端模式（TUI）入门

### 启动 TUI

OpenCode 默认启动交互式终端界面（TUI）：

```bash
# 在当前目录启动
opencode

# 在指定目录启动
opencode /path/to/project
```

### TUI 界面概览

首次启动后，你会看到一个友好的终端界面：

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  OpenCode - The open source AI coding agent         │
│                                                     │
│  What would you like to do?                          │
│                                                     │
│  Type a message or use Ctrl+X to open commands     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 基本交互方式

在 TUI 中，你可以：

1. **直接输入消息**：像聊天一样与 AI 交互
2. **使用文件引用**：用 @ 符号引用文件
3. **运行 shell 命令**：用 ! 符号运行命令
4. **使用 slash 命令**：用 / 执行快速操作
5. **使用快捷键**：Ctrl+X 作为 leader 键

### Leader 键

OpenCode 使用 `Ctrl+X` 作为默认的 leader 键，用于访问命令快捷键。

```
Ctrl+X ?  显示可用快捷键
Ctrl+X C  压缩当前会话
Ctrl+X D  切换工具执行详情
Ctrl+X E  打开外部编辑器
Ctrl+X H  显示帮助
Ctrl+X N  开始新会话
Ctrl+X M  列出可用模型
Ctrl+X Q  退出 OpenCode
Ctrl+X U  撤销上一条消息
```

---

## 2.2 基本命令

### Slash 命令

在 TUI 中，你可以输入 `/` 后跟命令名来快速执行操作。

#### `/connect` - 连接到提供商

```bash
/connect
```

这会显示可用的 LLM 提供商列表，你可以选择并添加 API 密钥。

#### `/models` - 列出可用模型

```bash
/models
```

显示所有可用的 LLM 模型，以及当前选中的模型。

#### `/help` - 显示帮助

```bash
/help
```

显示所有可用命令的详细说明。

#### `/new` - 开始新会话

```bash
/new
```

或使用 `/clear`，这会清除当前对话历史。

#### `/compact` - 压缩会话

```bash
/compact
```

或使用 `/summarize`，这会压缩当前会话内容，减少上下文使用。

#### `/exit` - 退出 OpenCode

```bash
/exit
```

或使用 `/quit`、`/q`。

#### `/themes` - 列出主题

```bash
/themes
```

显示所有可用的 TUI 主题。

#### `/thinking` - 切换思考显示

```bash
/thinking
```

切换是否显示模型的思考/推理过程（适用于支持扩展思考的模型）。

#### `/export` - 导出对话

```bash
/export
```

将当前对话导出为 Markdown 并在默认编辑器中打开。

#### `/share` - 分享会话

```bash
/share
```

创建一个可分享的会话链接。

#### `/sessions` - 会话管理

```bash
/sessions
```

列出和切换会话。也可使用 `/resume`、`/continue`。

#### `/details` - 切换详情

```bash
/details
```

切换是否显示工具执行的详细信息。

#### `/editor` - 打开编辑器

```bash
/editor
```

在配置的外部编辑器中编写消息（使用 `EDITOR` 环境变量）。

#### `/init` - 初始化 Agent 配置

```bash
/init
```

创建或更新 AGENTS.md 文件。用于配置自定义 agent 行为和规则。

#### `/undo` - 撤销上一条消息

```bash
/undo
```

撤销上一条消息、所有后续响应，以及任何文件修改。

**重要：** 
- OpenCode 使用 Git 管理文件变更，所以你的项目需要是一个 Git 仓库
- 可以多次使用 `/undo` 撤销多个更改

#### `/redo` - 重做已撤销的操作

```bash
/redo
```

重做之前用 `/undo` 撤销的操作。

**注意：**
- 需要先使用 `/undo` 撤销
- 可以在 `/undo` 后继续使用 `/redo`
- 仅限于最后一次撤销的操作

#### `/unshare` - 取消分享

```bash
/unshare
```

取消当前会话的分享链接。

---

## 2.6 Agent 模式切换

### 切换 Agent

使用 `Tab` 键在两种内置 agent 之间切换：

#### Build Agent（build）

- **完全访问**：可以编辑文件和运行命令
- **默认 agent**：用于日常开发工作
- **权限**：无限制
- **适用场景**：编码、重构、测试

#### Plan Agent（plan）

- **只读模式**：默认拒绝文件编辑
- **权限请求**：运行 bash 命令前会请求权限
- **适用场景**：代码探索、分析不熟悉的项目、规划变更

### 何时使用哪个 Agent

**使用 build agent（默认）时：**
- 编写新代码
- 重构现有代码
- 修复 bug
- 运行测试

**使用 plan agent 时：**
- 分析项目结构
- 阅读和理解代码
- 探索不熟悉的项目
- 规划大规模重构
- 审查代码

### Agent 切换快捷键

```
Tab  - 在 build 和 plan agent 之间切换
Ctrl+X A  - 查看所有 agent
```

---

## 2.7 非交互模式

### 单次提示模式

使用 `-p` 参数运行单次提示并打印到终端：

```bash
# 运行单次提示
opencode -p "解释 Go 中的 context 用法"
```

### 静默模式

使用 `-q` 参数不显示 spinner（对脚本有用）：

```bash
opencode -p "解释 Go 中的 context 用法" -q
```

### JSON 格式输出

使用 `-f json` 获取响应的 JSON 格式（适合脚本和自动化）：

```bash
opencode -p "解释 Go 中的 context 用法" -f json
```

### 继续上次会话

```bash
# 使用 --continue 继续上次会话
opencode --continue

# 使用 --session 指定会话 ID
opencode --session abc123
```

### 服务器模式

OpenCode 提供了服务器模式，允许通过 web 或 ACP（Agent Client Protocol）访问：

```bash
# 启动 web 服务器
opencode web --port 4096 --hostname 0.0.0.0

# 启动 ACP 服务器
opencode serve

# 在另一个终端，附加 TUI 到远程后端
opencode attach http://10.20.30.40:4096
```

这允许你在浏览器或移动设备上使用 OpenCode。

---

## 2.8 完整快捷键列表

### Leader 键（Ctrl+X）

```
Ctrl+X ?  - 显示所有可用快捷键
Ctrl+X A  - 显示所有 agent
Ctrl+X C  - 压缩当前会话
Ctrl+X D  - 切换工具执行详情
Ctrl+X E  - 打开外部编辑器
Ctrl+X H  - 显示帮助
Ctrl+X I  - 创建/更新 AGENTS.md
Ctrl+X L  - 列出/切换会话
Ctrl+X M  - 列出可用模型
Ctrl+X N  - 开始新会话
Ctrl+X Q  - 退出 OpenCode
Ctrl+X R  - 重做已撤销的操作
Ctrl+X S  - 分享当前会话
Ctrl+X T  - 列出可用主题
Ctrl+X U  - 撤销上一条消息
Ctrl+X X  - 导出当前对话到 Markdown
```

### 其他快捷键

```
Tab      - 在 agent 之间切换（build/plan）
Enter     - 发送消息
Esc       - 取消当前输入
Ctrl+C    - 中断当前操作
```

---

## 2.3 文件操作

### 文件引用

在消息中使用 `@` 符号引用文件，OpenCode 会自动读取文件内容：

```
请解释 @packages/functions/src/api/index.ts 中的认证逻辑
```

这会进行模糊文件搜索，并自动添加文件内容到对话上下文中。

### 多文件引用

你可以同时引用多个文件：

```
分析 @src/App.tsx 和 @src/Header.tsx 的关系
```

### 目录引用

使用 `@` 引用目录会列出该目录的内容：

```
@src/components/
```

### 文件编辑

OpenCode 的 `build` agent 可以直接编辑文件：

```
把 @src/Button.tsx 中的 onClick 处理器改为异步的
```

OpenCode 会：
1. 读取文件内容
2. 应用修改
3. 显示修改的差异
4. 写入文件

### 文件创建

你可以让 OpenCode 创建新文件：

```
创建一个新文件 src/utils/helpers.ts，包含一个 formatCurrency 函数
```

### 文件删除

```
删除 @deprecated/old-util.js 文件
```

### 文件搜索

```
搜索包含 "API" 的所有文件
```

OpenCode 会在当前项目中搜索匹配的文件。

---

## 2.4 简单的代码补全

### 内联补全

在代码中，你可以让 OpenCode 提供补全建议：

```
帮我完成这个函数：

function formatDate(date: Date) {
  // TODO: 实现日期格式化
}
```

### 代码生成

要求 OpenCode 生成新的代码片段：

```
用 TypeScript 写一个 React hook，用于管理 API 请求状态
```

### 代码重构

让 OpenCode 重构现有代码：

```
重构 @src/utils/api.ts，使用 async/await 替代 Promise 链
```

### 代码解释

要求 OpenCode 解释代码：

```
解释 @src/components/Button.tsx 中的代码
```

### 代码审查

让 OpenCode 审查代码：

```
审查 @src/App.tsx 中的代码，指出潜在问题
```

---

## 2.5 上下文理解

### 项目结构理解

OpenCode 能够理解整个项目结构：

```
帮我理解这个项目的架构
```

OpenCode 会扫描项目，提供结构化的项目分析。

### 依赖关系分析

```
分析 src/ 下的文件依赖关系
```

### 代码导航

使用文件引用快速导航：

```
跳转到 @src/components/Button.tsx 的第 50 行
```

### 跨文件分析

OpenCode 可以跨多个文件分析代码：

```
检查 @src/App.tsx 中是否正确使用了 @src/utils/api.ts 的函数
```

### 上下文记忆

OpenCode 会记住对话上下文，你可以引用之前的讨论：

```
继续完善我们刚才讨论的那个组件
```

### 会话压缩

当对话很长时，使用 `/compact` 命令压缩会话：

```
/compact
```

这会保留重要信息，减少 token 使用。

---

## 🎯 本章小结

### 你学到了

- ✅ 如何启动和导航 TUI
- ✅ 基本 slash 命令的使用（包括 /init、/undo、/redo、/unshare）
- ✅ 如何使用快捷键（Ctrl+X）
- ✅ 非交互模式（-p、-f、-q、--continue）
- ✅ Agent 切换（build vs plan）
- ✅ 服务器模式（web、serve、attach）
- ✅ 文件引用和操作（读取、编辑、创建、删除）
- ✅ 代码补全、生成、重构、解释、审查
- ✅ 项目结构理解和跨文件分析
- ✅ 上下文记忆和会话管理

### 实践练习

1. **文件引用练习**
   - 引用单个文件
   - 引用多个文件
   - 引用目录

2. **代码操作练习**
   - 生成新代码
   - 重构现有代码
   - 解释复杂代码

3. **命令练习**
   - 使用 `/models` 切换模型
   - 使用 `/new` 开始新会话
   - 使用 `/undo` 撤销操作
   - 使用 `/redo` 重做操作
   - 使用 `/init` 配置 agent

4. **Agent 练习**
   - 使用 Tab 键切换 agent
   - 尝试用 plan agent 探索代码
   - 使用 build agent 进行编辑

### 下一步

进入 **第三部分：中级 - 项目集成**，学习：
- LSP 集成原理
- 项目结构深度分析
- 代码导航和跳转
- 诊断和错误修复
- 多文件协同编辑

---

## 💡 常见问题

### Q: 如何撤销文件修改

**A:** 使用 `/undo` 命令：

```
/undo
```

这会撤销上一条消息及其所有文件修改。OpenCode 使用 Git 管理文件变更，所以你的项目需要是一个 Git 仓库。

### Q: 文件引用找不到文件怎么办

**A:** 确保文件路径正确，并且使用相对路径：

```
# 正确
@src/utils/api.ts

# 错误（如果不在项目根目录）
/Users/username/project/src/utils/api.ts
```

### Q: 如何切换到不同的 agent

**A:** 使用 Tab 键在 `build` 和 `plan` agent 之间切换。

- **build agent**：可以编辑文件和运行命令
- **plan agent**：只读，适合代码探索

### Q: 如何在 TUI 中运行 shell 命令

**A:** 使用 `!` 前缀运行命令：

```
!ls -la
!npm test
!git status
```

命令输出会自动添加到对话上下文中。

### Q: 如何在脚本中使用 OpenCode

**A:** 使用非交互模式：

```bash
# 单次提示
opencode -p "解释这段代码"

# JSON 格式输出
opencode -p "解释这段代码" -f json

# 静默模式（无 spinner）
opencode -p "解释这段代码" -q
```

### Q: /undo 和 /redo 的工作原理

**A:** OpenCode 使用 Git 管理：
- `/undo` 会回退到上一个 commit
- `/redo` 会前进到下一个 commit
- 项目必须是 Git 仓库
- 可以多次使用 `/undo` 撤销多个更改

---

**第二部分完成！** 🎉

准备好进入第三部分了吗？
