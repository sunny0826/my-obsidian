# OpenCode 使用指南 - 第四部分：高级 - 高级功能

> 预计学习时间：1-2 天
> 难度：⭐⭐⭐☆☆

---

## 4.1 自定义工作流

### 什么是工作流

工作流（Workflow）是 OpenCode 的强大功能，允许你创建可重复使用的自定义命令和提示模板。

### 为什么需要工作流

- ✅ **提高效率**：一次配置，多次使用
- ✅ **标准化流程**：团队统一操作流程
- ✅ **减少重复**：避免每次都重复相同的内容
- ✅ **知识固化**：将最佳实践固化为可复用的模板

### 创建自定义命令

在 `.opencode/commands/` 目录中创建 Markdown 文件：

```markdown
---
description: 创建新的 API 端点
agent: build
model: anthropic/claude-3-5-sonnet-20250229

创建一个新的 RESTful API 端点：
1. 定义路由
2. 实现控制器
3. 添加错误处理
4. 编写测试
```

**使用方法：**
```
/endpoint
```

### 使用参数和占位符

工作流支持动态参数：

```markdown
---
description: 创建一个新的 React 组件
agent: build
model: anthropic/claude-3-5-sonnet-20250229

创建一个名为 $ARGUMENTS 的 React 组件：
- 包含 TypeScript 类型
- 使用 styled-components
- 添加基本的 prop 类型
```

**支持的占位符：**
- `$ARGUMENTS`：所有参数
- `$1`、`$2`、`$3`：位置参数
- `$FILE`：文件内容
- `$DIR`：目录内容

---

## 4.2 IDE 扩展使用

### VS Code 扩展

OpenCode 提供了 VS Code 扩展，允许你在编辑器中直接使用 AI 功能。

#### 安装 VS Code 扩展

1. 打开 VS Code
2. 点击扩展图标（⬇️）
3. 搜索 "OpenCode"
4. 点击 "安装"

#### 主要功能

- **内联代码补全**：在编辑器中直接获得补全建议
- **快速命令**：使用 `/opencode` 命令
- **上下文感知**：编辑器知道当前打开的文件
- **错误高亮**：实时显示诊断信息

#### 常用 VS Code 命令

```bash
# 在当前目录启动 OpenCode
/opencode
```

### JetBrains IDE 集成

对于 JetBrains IDEs（IntelliJ IDEA、PyCharm、WebStorm 等），OpenCode 也提供了集成。

#### 安装插件

1. 打开插件市场
2. 搜索 "OpenCode"
3. 安装 OpenCode 插件

#### 主要功能

- **代码补全**：JetBrains 标准的代码补全
- **诊断显示**：在 IDE 中显示错误和警告
- **快速操作**：一键发送消息给 OpenCode

---

## 4.3 GitHub 集成

### 安装 GitHub Agent

OpenCode 的 GitHub Agent 可以自动化你的仓库操作，比如：
- 审查和合并 PR
- 自动回复 Issue
- 运行测试

#### 安装步骤

```bash
# 使用 OpenCode 命令安装 GitHub Agent
opencode github install
```

这会：
1. 在你的仓库中创建 GitHub Actions workflow
2. 添加必要的密钥（会引导你配置）

#### 使用 GitHub Agent

```bash
# 运行 GitHub Agent
opencode github run
```

#### 配置 GitHub Agent

在 `.opencode/commands/` 目录创建 GitHub 工作流：

```markdown
---
description: 审查并合并 PR
agent: github

审查最新的 5 个 PR：
1. 检查 CI/CD 状态
2. 审查代码变更
3. 检查冲突
4. 提供合并建议
```

#### 在 CI/CD 中使用

```bash
# 在 GitHub Actions 中运行
opencode github run --event pull_request
```

---

## 4.4 多模型配置

### 切换模型

在不同场景中使用不同的模型：

```bash
# 查看可用模型
/models
```

选择最适合当前任务的模型：

- **快速响应**：Claude Sonnet 4.5
- **深度思考**：Claude Opus 4.5
- **代码生成**：GPT-5.2
- **成本优化**：GPT-4 Turbo

### 配置多个提供商

OpenCode 支持同时连接多个 LLM 提供商：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "apiKey": "sk-xxx",
      "models": {
        "gpt-4": {
          "options": {
            "reasoningEffort": "high"
          }
        }
      }
    },
    "anthropic": {
      "apiKey": "sk-ant-xxx"
    }
  }
}
```

### 按语言选择模型

为不同语言选择不同的模型：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "models": {
        "claude-3.5-sonnet": {
          "language": "typescript"
        },
        "claude-3.5-sonnet": {
          "language": "python"
        }
      }
    }
  }
}
```

---

## 4.5 性能优化

### LSP 服务器优化

优化 LSP 性能：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "typescript": {
      "env": {
        "NODE_OPTIONS": "--max-old-space-size=4096"
      }
    }
  }
}
```

### 大文件处理

对于大型项目，优化性能：

1. **选择性加载**：只为当前打开的文件启用 LSP
2. **延迟启动**：在真正需要时才启动 LSP 服务器
3. **限制上下文**：控制发送给 LLM 的上下文大小

### 并发处理

OpenCode 支持并发操作：

- **多文件编辑**：同时编辑多个文件
- **批量诊断**：一次获取多个文件的诊断
- **并行 LSP 调用**：同时从多个语言服务器获取信息

---

## 🎯 本章小结

### 你学到了

- ✅ 如何创建自定义工作流（命令和模板）
- ✅ 工作流中的参数和占位符
- ✅ VS Code 扩展安装和配置
- ✅ JetBrains IDE 集成
- ✅ GitHub Agent 安装和自动化
- ✅ 多模型配置和切换
- ✅ 性能优化策略（LSP、大文件、并发）

### 实践练习

1. **创建自定义命令**
   - 定义一个常用的代码生成模板
   - 使用参数和占位符
   - 在 TUI 中测试命令

2. **使用 VS Code 扩展**
   - 安装扩展
   - 尝试内联代码补全
   - 使用 `/opencode` 命令

3. **配置 GitHub Agent**
   - 在测试仓库中安装
   - 创建 PR 审查工作流
   - 在 CI/CD 中使用

4. **优化模型配置**
   - 为不同任务选择不同的模型
   - 测试不同模型的响应速度
   - 平衡成本和质量

### 下一步

进入 **第五部分：专家级 - 深度定制**，学习：
- 本地部署
- 私有模型集成
- 自定义插件开发
- 企业级配置
- 最佳实践

---

## 💡 常见问题

### Q: 工作流和自定义命令有什么区别？

**A:**
- **自定义命令**：存储在 `.opencode/commands/` 目录，使用 Markdown 定义
- **工作流**：存储在 `opencode` 中，使用 JSON 配置
- **工作流更强大**：支持更多高级功能（条件逻辑、多步骤操作）

### Q: 如何在 CI/CD 中使用 OpenCode？

**A:**
- 安装 GitHub Agent：`opencode github install`
- 创建 GitHub Actions workflow
- 在 workflow 中使用：`opencode github run`

### Q: VS Code 扩展不工作怎么办？

**A:**
- 确保 OpenCode TUI 正在运行：`opencode` 或 `opencode attach`
- 检查扩展是否已启用
- 尝试禁用后重新启用

### Q: 如何减少 API 调用成本？

**A:**
- 使用更快的模型（GPT-4 Turbo、Claude Sonnet 4.5）
- 限制上下文窗口大小
- 使用缓存机制
- 优化 LSP 配置（延迟启动）

---

**第四部分完成！** 🎉

准备好进入第五部分了吗？
