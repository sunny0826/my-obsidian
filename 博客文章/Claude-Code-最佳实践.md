---
title: GitHub 最火 Claude Code 最佳实践：12 个技巧深度解析
date: 2026-02-25
tags: [AI, ClaudeCode, DevTools, 编程]
---

# GitHub 最火 Claude Code 最佳实践：12 个技巧深度解析

## 引言

GitHub 上有一个仓库，描述是"practice makes claude perfect"，近 400 forks，持续更新。

这个仓库就是 [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)，汇集了 Claude Code 创始人 **Boris Cherny** 和全球开发者的实战经验。

---

## 一、Claude Code 核心概念

| 功能 | 作用 |
|------|------|
| **Skills** | 可重用的知识和工作流，按需加载 |
| **Agents** | 自定义子代理，有自己的工具和权限 |
| **Memory** | 持久上下文，通过 CLAUDE.md 文件 |
| **Rules** | 模块化主题指令 |
| **Hooks** | 确定性脚本，在特定事件时运行 |
| **MCP Servers** | 外部工具、数据库、API 的连接 |

---

## 二、Boris Cherny 的 12 个定制技巧

来自 Claude Code 创始人 Boris Cherny 的 2026年2月分享：

**1. 配置终端**
- 运行 `/config` 设置明暗主题
- 启用 shift+enter 换行

**2. 调整努力级别**
- `/model` 选择 Low/Medium/High
- **Boris 偏好：全部使用 High**

**3. 安装插件和 MCP**
- 从官方市场安装 LSPs、MCPs、Skills
- 可创建公司内部市场

**4. 创建自定义代理**
- `.claude/agents/` 中放入 `.md` 文件
- 可自定义名称、颜色、工具集、模型

**5. 预批准权限**
- 使用通配符：`Bash(npm run *)`
- 减少每次确认

**6. 启用沙箱**
- `/sandbox` 启用文件和网络隔离

**7. 添加状态行**
- 显示模型、目录、上下文，成本

**8. 自定义快捷键**
- 每个按键都可重新映射

**9. 设置钩子**
- 任务结束自动继续
- 权限请求自动路由到 Slack

**10. 自定义动词**
- 定制 spinner 动词列表

**11. 输出风格**
- Explanatory：解释代码模式
- Learning：指导你修改
- Custom：自定义

**12. 团队配置**
- `settings.json` 签入 git 共享

---

## 三、作者实战经验

**工作流**：
- ✅ Claude.md 不超过 150 行
- ✅ 用 commands 而非 agents
- ✅ 始终从 plan 模式开始
- ✅ 子任务足够小，50% 上下文内完成
- ✅ 频繁提交

**MCP 精选**：
> *"装了 15 个 MCP 以为越多越好，最后只用 4 个。"*

推荐每日使用：
- **Context7**：最新文档，防止幻觉
- **Playwright**：浏览器自动化
- **Claude in Chrome**：调试用户问题
- **DeepWiki**：仓库结构文档

---

## 四、RPI 工作流

**RPI** = Research → Plan → Implement

带验证门的系统化开发流程：

```
1. Research → RESEARCH.md + GO/NO-GO 判定
2. Plan → pm.md, ux.md, eng.md, PLAN.md
3. Implement → 阶段 PASS → 下一阶段
```

---

## 五、调试技巧

- `/doctor` 诊断问题
- 终端作为后台任务查看日志
- MCP 让 Claude 自己查控制台
- 提供问题截图

---

## 六、总结

这个仓库是 Claude Code 用户的宝藏：

1. **可定制性**是 Claude Code 的核心优势
2. **团队共享** `settings.json` 提升效率
3. **精选 MCP** 而非贪多
4. **RPI 工作流** 防止做无用功

> *"Claude Code works great out of the box, but when you do customize, check your settings.json into git so your team can benefit too."*

---

*参考资料：https://github.com/shanraisshan/claude-code-best-practice*
