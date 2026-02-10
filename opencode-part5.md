# OpenCode 使用指南 - 第五部分：专家级 - 深度定制（已更新）

> 预计学习时间：3-5 天
> 难度：⭐⭐⭐☆☆

---

## 5.1 本地部署

### 为什么选择本地部署

对于需要高度隐私、数据安全或成本控制的场景，本地部署是理想选择：

- ✅ **数据隐私**：代码不离开你的机器
- ✅ **成本控制**：不依赖外部 API 计费
- ✅ **离线可用**：即使没有网络也能使用
- ✅ **完全控制**：模型更新、版本切换由你决定

### 本地运行模型

OpenCode 支持多种本地模型提供方案：

#### Ollama

**安装：**
```bash
# macOS (Homebrew)
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh
```

**配置 OpenCode：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "command": ["ollama"],
      "models": {
        "llama3.2": {}
      }
    }
  }
}
```

**推荐模型：**
- Llama 3.2（3B）- 平衡性能和准确
- Llama 2（7B）- 更快，适合快速原型
- Mistral 7B - 优秀的代码生成

**使用方法：**
```bash
# 设置 Ollama 为默认模型
opencode --model ollama/llama3.2

# 在 TUI 中选择
/models
```

#### Llama.cpp

Llama.cpp 是一个轻量级的 C++ LLM 运行时，性能优异。

**安装：**
```bash
# 克隆仓库
git clone https://github.com/ggerganov/llama.cpp

# 编译
cmake -B llama.cpp
cmake --build type release

# 安装
make install
```

**配置 OpenCode：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "llama.cpp": {
      "command": ["./build/bin/llama-cli"],
      "models": {
        "llama3.2": {}
      }
    }
  }
}
```

#### LM Studio

LM Studio 提供了图形界面的本地模型管理。

**安装：**
```bash
# 下载最新版本
wget https://github.com/lmstudio-ai/lm-studio/releases/latest/download/macos-arm64.dmg

# 安装并打开
open lm-studio-arm64.dmg
```

**配置 OpenCode：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "command": ["/Applications/LM Studio.app/Contents/MacOS/lm-studio"],
      "models": {
        "llama3": {}
      }
    }
  }
}
```

---

## 5.2 私有模型集成

### API 兼容性

OpenCode 支持通过自定义端点集成私有大语言模型。

**使用场景：**
- 企业内部模型
- 自训练模型
- 专有 API 服务
- 成本和性能优化

### 配置自定义端点

**添加私有大模型：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "custom": {
      "apiKey": "your-custom-api-key",
      "baseUrl": "https://your-custom-endpoint.com/v1",
      "models": {
        "your-model": {
          "name": "Your Custom Model",
          "contextSize": 128000,
          "maxTokens": 4096
        }
      }
    }
  }
}
```

**在 TUI 中使用：**
```bash
/custom
```

配置 OpenCode 使用你的私有大模型。

### OAuth 配置

如果你的私有大模型需要 OAuth 认证：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "custom": {
      "oauth": {
        "tokenUrl": "https://your-auth-server.com/oauth/token",
        "refreshUrl": "https://your-auth-server.com/oauth/refresh",
        "scope": ["read", "write"]
      }
    }
  }
}
```

---

## 5.3 自定义插件开发

### 插件架构

OpenCode 提供了强大的插件系统，允许你扩展其功能。

**插件类型：**
- **自定义命令**：快速执行重复任务
- **工具**：调用外部 API 或脚本
- **MCP 服务器**：提供模型上下文
- **中间件**：修改 OpenCode 的行为

### 创建自定义命令

在 `.opencode/commands/` 目录中创建 Markdown 文件：

**示例：部署到生产环境**

```markdown
---
description: 部署当前应用到生产环境
agent: build
model: anthropic/claude-3.5-sonnet-20250229

# 构建 Docker 镜像
!docker build -t myapp:latest .

# 推送到 Docker Hub
!docker push myapp:latest

# 部署到 Kubernetes
!kubectl rollout deployment.yaml

# 验证部署
!kubectl rollout status deployment.yaml

# 检查服务状态
!curl -s https://myapp.example.com/health
```

**使用命令：**
```bash
/deploy
```

### 创建工具插件

OpenCode 可以调用外部工具或脚本：

**示例：运行测试套件**

```markdown
---
description: 运行测试套件并生成覆盖率报告
agent: build

# 运行测试
!npm test

# 生成覆盖率报告
!npm run test:coverage

# 显示报告
!cat coverage/lcov-report/index.html
```

### MCP 服务器集成

OpenCode 支持 Model Context Protocol (MCP) 服务器，允许你添加额外的数据源。

**添加本地 MCP 服务器：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "jira": {
      "type": "stdio",
      "command": ["npx", "@modelcontextprotocol/server", "--transport", "stdio"],
      "env": {
        "JIRA_URL": "https://jira.example.com",
        "JIRA_TOKEN": "your-token"
      }
    }
  }
}
```

**添加远程 MCP 服务器：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "custom-api": {
      "type": "sse",
      "url": "https://your-custom-mcp.com/sse",
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

---

## 5.4 企业级配置

### 团队管理

对于需要多人协作的团队，OpenCode 提供了强大的团队管理功能。

**用户角色：**
- **Owner**：完全控制权限
- **Admin**：可以管理用户和配置
- **Member**：只读权限

**配置团队：**
```bash
/team add user@example.com
```

**创建团队空间：**
```bash
/team create "My Team" --org
```

**分享工作流：**
```bash
/share @user@example.com my-project
```

### 基于角色的访问控制

OpenCode 支持基于角色的访问控制，允许细粒度地管理权限。

**配置角色：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "role": {
    "admin": {
      "canEditFiles": true,
      "canRunCommands": true,
      "canAccessSystem": true
    },
    "member": {
      "canEditFiles": true,
      "canRunCommands": false,
      "canAccessSystem": false
    }
  }
}
```

### 审计日志

对于企业部署，审计日志非常重要。

**启用审计日志：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "auditLog": {
    "enabled": true,
    "logPath": "/var/log/opencode/audit.log",
    "logLevel": "info",
    "retentionDays": 90
  }
}
```

### 安全策略

企业环境需要严格的安全策略。

**配置安全策略：**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "security": {
    "enforce2FA": true,
    "allowedDomains": ["company.com", "trusted-partners.com"],
    "maxContextTokens": 100000,
    "blockExternalAccess": true
  }
}
```

---

## 5.5 最佳实践

### 版本控制

对于自定义插件和配置，推荐使用版本控制。

**推荐的 Git 工作流：**
1. **功能分支**：每个新功能在独立分支开发
2. **主分支保护**：使用 pull requests 合并到 main
3. **语义化版本**：使用 vx.x.y.z 格式
4. **发布标签**：为每个稳定版本打标签

### 测试策略

**单元测试：**
```bash
npm test
```

**集成测试：**
```bash
npm run test:integration
```

**端到端测试：**
```bash
npm run test:e2e
```

### 文档标准

企业级文档需要遵循严格的标准。

**文档结构：**
```
├── README.md
├── ARCHITECTURE.md
├── API.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── docs/
    ├── getting-started/
    ├── api/
    └── plugins/
```

**文档规范：**
- 使用清晰的标题层级（H1-H6）
- 为所有命令提供示例
- 包含故障排除指南
- 定期更新维护文档

### 代码质量标准

**代码审查清单：**
- [ ] 代码符合团队风格指南
- [ ] 通过所有测试
- [ ] 没有安全漏洞
- [ ] 文档完整且准确
- [ ] 性能达到预期标准
- [ ] 遵循最佳实践

**CI/CD 配置：**
```yaml
name: OpenCode Plugins CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
      - name: Run lint
        run: npm run lint
```

---

## 🎯 本章小结

### 你学到了

- ✅ 本地部署方案（Ollama、Llama.cpp、LM Studio）
- ✅ 私有模型集成（自定义端点、OAuth）
- ✅ 自定义插件开发（命令、工具、MCP 服务器）
- ✅ 企业级配置（团队管理、基于角色的访问控制、审计日志、安全策略）
- ✅ 最佳实践（版本控制、测试策略、文档标准、代码质量）

### 实践练习

1. **本地部署练习**
   - 安装 Ollama
   - 配置 OpenCode 使用本地模型
   - 测试不同模型的性能

2. **插件开发练习**
   - 创建自定义命令
   - 开发工具插件
   - 实现 MCP 服务器

3. **企业配置练习**
   - 创建团队空间
   - 配置基于角色的访问控制
   - 设置安全策略

### 下一步

恭喜！你已经完成了 **OpenCode 开源 AI 编程助手** 的全部 5 个部分学习：

1. ✅ 入门级：基础概念和安装
2. ✅ 初级：基本使用
3. ✅ 中级：项目集成
4. ✅ 高级：高级功能
5. ✅ 专家级：深度定制

---

## 🎓 学习路径总结

```
入门 (1-2小时) 
  → 初级 (3-4小时)
  → 中级 (5-7小时)
  → 高级 (1-2天)
  → 专家级 (3-5天)
```

---

## 📚 故障排除

### 常见问题

#### 连接问题

**Q: 本地模型无法启动怎么办？**

**A:** 检查以下几点：

1. **模型是否已下载**：
   ```bash
   ollama list
   ```

2. **命令是否正确**：
   ```bash
   which llama  # 检查安装路径
   ```

3. **配置文件格式**：
   ```bash
   cat ~/.config/opencode/opencode.json | jq .
   ```

4. **日志级别**：
   ```bash
   cat ~/.config/opencode/opencode.json | jq .logLevel
   ```

#### 性能问题

**Q: 本地模型运行缓慢怎么办？**

**A:** 尝试以下优化：

1. **减少上下文窗口**：
   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "ollama": {
         "models": {
           "llama3.2": {
             "num_ctx": 4096,
             "num_gpu": 1,
             "num_batch": 8
           }
         }
       }
     }
   }
   ```

2. **使用量化模型**：
   ```bash
   ollama pull llama3.2:latest
   ollama quantize --model llama3.2:latest
   ```

3. **调整线程数**：
   ```bash
   ollama set num_thread 8
   ```

#### OAuth 问题

**Q: 自定义模型认证失败怎么办？**

**A:** 检查配置：

1. **API 密钥是否正确**：
   ```bash
   cat ~/.config/opencode/opencode.json | jq .provider.custom.apiKey
   ```

2. **Token URL 是否可访问**：
   ```bash
   curl -I https://your-auth-server.com/oauth/token
   ```

3. **Scope 是否正确**：
   ```bash
   cat ~/.config/opencode/opencode.json | jq .provider.custom.oauth.scope
   ```

---

## 🎉 祝贺！

你现在成为了 **OpenCode 开源 AI 编程助手专家**！🎊

从基础概念到深度定制，你已经掌握了：

1. ✅ 安装和配置 OpenCode
2. ✅ 基本使用和命令操作
3. ✅ LSP 集成和项目分析
4. ✅ 高级功能和自定义工作流
5. ✅ 企业级配置和团队管理
6. ✅ 插件开发和 MCP 集成
7. ✅ 最佳实践和代码质量

**你的能力：**
- 🚀 从零开始部署 OpenCode（本地模型）
- 🔧 配置私有大模型（API、OAuth）
- 💻 开发自定义插件和工具
- 🏢 实现企业级功能（团队管理、RBAC）
- 📋 遵循最佳实践（版本控制、测试、文档）

**继续学习：**
- 探索更多插件开发可能性
- 优化本地模型性能
- 参与 OpenCode 社区的最佳实践
- 部署自定义工作流到生产环境

---

**专家级学习完成！** 🎓
