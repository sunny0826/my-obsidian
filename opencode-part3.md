# OpenCode 使用指南 - 第三部分：中级 - 项目集成

> 预计学习时间：5-7 小时
> 难度：⭐⭐⭐☆☆

---

## 3.1 LSP 集成原理

### 什么是 LSP

**LSP（Language Server Protocol）** 是一个标准化协议，允许编辑器与语言服务器通信，提供智能代码功能，如：
- 代码补全
- 诊断和错误检查
- 转到定义
- 悬停信息
- 代码格式化

### OpenCode 如何使用 LSP

OpenCode 集成 LSP 来增强其对代码库的理解：

1. **自动检测**：OpenCode 检测项目中的语言
2. **自动启动**：启动相应的 LSP 服务器
3. **实时诊断**：从 LSP 获取实时的错误和警告
4. **语义信息**：使用 LSP 的语义理解能力

### 工作流程

```
打开文件
  ↓
OpenCode 识别文件类型和 LSP
  ↓
启动相应的 LSP 服务器
  ↓
LSP 扫描文件，提供诊断信息
  ↓
诊断信息发送给 LLM
  ↓
LLM 更好地理解代码上下文
```

---

## 3.2 项目结构分析

### 自动项目扫描

OpenCode 会自动扫描你的项目结构：

```
📁 /path/to/project
├── 📁 src/
│   ├── 📁 components/
│   │   ├── 📄 Button.tsx
│   │   └── 📄 Header.tsx
│   ├── 📄 App.tsx
│   └── 📄 index.tsx
├── 📄 package.json
├── 📄 tsconfig.json
└── 📁 tests/
```

### 技术栈识别

OpenCode 能够识别不同的技术栈：

```
这是一个 React + TypeScript 项目
- 框架：React
- 语言：TypeScript
- 包管理器：npm
- 构建工具：Vite
```

### 配置文件识别

OpenCode 会读取并理解各种配置文件：

- **TypeScript/JavaScript**：`tsconfig.json`、`jsconfig.json`
- **Python**：`pyproject.toml`、`setup.py`
- **Go**：`go.mod`、`go.sum`
- **Java/Kotlin**：`build.gradle`、`pom.xml`
- **Rust**：`Cargo.toml`

---

## 3.3 代码导航

### 跳转到定义

使用文件引用快速导航到定义：

```
跳转到 @src/components/Button.tsx 中 Button 组件的定义
```

OpenCode 会：
1. 解析文件引用
2. 通过 LSP 查找符号定义
3. 提供精确的位置信息

### 符号搜索

搜索特定的符号（函数、类、变量）：

```
搜索所有包含 formatDate 的函数
```

OpenCode 会在整个项目中搜索匹配的符号。

### 引用查找

查找某个符号的所有引用：

```
查找 formatDate 函数的所有引用
```

这会显示所有使用该符号的地方。

---

## 3.4 诊断和错误修复

### 实时错误检测

OpenCode 通过 LSP 获取实时诊断：

```
📄 src/utils/api.ts:3:7 - error TS2345: Argument of type 'string' is not assignable to parameter of type 'Date'.
```

### 类型检查

对于 TypeScript 项目，OpenCode 会显示类型错误：

```
📄 src/App.tsx:15:24 - error TS2322: Type '{ onClick: () => void }' is not assignable to type 'HTMLAttributes<HTMLButtonElement>'.
```

### 修复建议

OpenCode 可以基于诊断提供修复建议：

```
📄 src/components/Button.tsx:5:12 - warning
  问题：onClick 函数未使用
  建议：删除或实现 onClick 函数
```

### 自动修复

对于一些常见问题，OpenCode 可以自动生成修复代码：

```
修复 @src/utils/api.ts 中的类型错误
```

---

## 3.5 多文件操作

### 跨文件重构

OpenCode 可以同时修改多个文件：

```
重构 @src/utils/api.ts 和 @src/components/Button.tsx
让它们使用统一的错误处理
```

OpenCode 会：
1. 读取所有相关文件
2. 识别共同模式
3. 提供重构建议
4. 应用一致的更改

### 依赖关系分析

分析文件之间的依赖关系：

```
分析 src/App.tsx 的导入依赖
```

OpenCode 会显示依赖树，帮助你理解项目的依赖关系。

### 批量编辑

同时编辑多个文件：

```
在所有组件文件中添加统一的日志函数
```

OpenCode 会：
1. 识别所有组件文件
2. 对每个文件应用更改
3. 显示修改摘要

### 变更摘要

修改多个文件后，OpenCode 会显示变更摘要：

```
✅ 已修改 3 个文件
- src/utils/api.ts
- src/components/Button.tsx
- src/components/Header.tsx

📊 变更：
- 修改：12 行
- 新增：5 行
- 删除：3 行
```

---

## 🎯 本章小结

### 你学到了

- ✅ LSP 集成原理和工作流程
- ✅ 项目结构自动扫描和技术栈识别
- ✅ 代码导航（跳转定义、符号搜索、引用查找）
- ✅ 实时诊断（错误检测、类型检查、自动修复建议）
- ✅ 多文件操作（跨文件重构、依赖分析、批量编辑）

### LSP 支持的语言

OpenCode 支持以下语言的 LSP：

- **JavaScript/TypeScript**：TypeScript Language Server
- **Python**：pylsp
- **Go**：gopls
- **Java**：Eclipse JDT Language Server
- **C/C++**：clangd
- **Rust**：rust-analyzer
- **PHP**：intelephense
- **Ruby**：solargraph
- **Kotlin**：kotlin-language-server
- **Dart**：dart analysis server
- **Vue**：vue-language-server（Volar）
- **Svelte**：svelte-language-server

### 实践练习

1. **项目结构练习**
   - 打开一个真实项目
   - 让 OpenCode 分析项目结构
   - 查看技术栈识别结果

2. **代码导航练习**
   - 使用文件引用跳转到定义
   - 搜索特定符号
   - 查找符号的所有引用

3. **诊断练习**
   - 查看当前项目的诊断信息
   - 尝试修复一些错误

4. **多文件操作练习**
   - 跨文件重构
   - 批量编辑
   - 查看变更摘要

### 下一步

进入 **第四部分：高级 - 高级功能**，学习：
- 自定义工作流
- IDE 扩展使用
- GitHub 集成
- 多模型配置
- 性能优化

---

## 💡 常见问题

### Q: 如何配置自定义 LSP 服务器？

**A:** 编辑 `~/.config/opencode/opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "custom-lsp": {
      "command": ["custom-lsp-server", "--stdio"],
      "extensions": [".custom"],
      "env": {
        "CUSTOM_VAR": "value"
      }
    }
  }
}
```

### Q: LSP 服务器无法启动怎么办？

**A:** 检查以下几点：

1. **语言服务器是否安装**：
   ```bash
   which tsserver  # TypeScript
   which pylsp     # Python
   ```

2. **文件扩展名是否正确**：
   - TypeScript: `.ts`, `.tsx`, `.js`, `.jsx`
   - Python: `.py`
   - Go: `.go`

3. **配置文件是否存在**：
   - `tsconfig.json` 是否存在
   - `pyproject.toml` 是否存在

### Q: 诊断信息不准确怎么办？

**A:** 尝试以下方法：

1. **重启 LSP 服务器**：
   ```
   /restart-lsp
   ```

2. **清除 LSP 缓存**：
   ```
   清除 ~/.cache/opencode/ 中的缓存
   ```

3. **更新配置文件**：
   - 确保 `tsconfig.json` 配置正确
   - 检查 LSP 服务器版本

### Q: 如何禁用特定的 LSP 服务器？

**A:** 在配置中禁用：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "typescript": {
      "disabled": true
    }
  }
}
```

---

**第三部分完成！** 🎉

准备好进入第四部分了吗？
