# Claude Code Routines 深度研究
*生成时间：2026-04-15 | 来源：claude.com/blog | 置信度：High*

---

## Executive Summary

Claude Code 推出 **Routines** 功能——一种自动化执行框架，让开发者可以在不依赖本地电脑开机的情况下，周期性地或通过事件触发执行 Claude Code 的 AI 任务。Routines 运行在 Claude Code 的云端基础设施上，支持定时任务、API 触发和 GitHub Webhook 三种触发方式，适用于开发工作流自动化（Backlog 管理、代码审查、部署验证等）。

---

## 1. 核心概念：什么是 Routines

**Routines = 预定义的 Claude Code 自动化任务**

与需要保持电脑开机、依赖本地 cron 的传统开发流程不同，Routines 运行在 Claude Code 的 Web 基础设施上，实现真正的云端自动化。

核心特性：
- **无需本地电脑在线** — 任务在云端执行
- **可访问仓库和 Connectors** — 继承 Claude Code 的代码库上下文和外部集成能力
- **支持定时/事件触发** — 灵活性高

---

## 2. 三种 Routines 类型

### 2.1 Scheduled Routines（定时任务）

按设定的时间表（每小时、每天、每周）自动运行。

**典型场景示例：**
> "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR."

**用途：**
- 每晚自动整理 Linear backlog，标签分配，发 Slack 汇总
- 每周扫描合并的 PR，更新过时的文档 API 引用

### 2.2 API Routines（API 触发）

每个 Routine 有独立的 endpoint 和认证 token，通过 HTTP POST 触发。

**典型场景：**
> "Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step."

**用途：**
- 接入监控告警系统（Datadog 等）
- 集成 CI/CD 流水线钩子
- 连接内部工具和部署 Webhook

### 2.3 Webhook Routines（GitHub 事件触发）

订阅 GitHub 仓库事件，PR 匹配过滤器时自动触发。

**核心能力：**
- 每个匹配的 PR 创建一个独立 session
- 持续跟踪 PR 更新（评论、CI 失败等）
- Claude 主动处理后续跟进

**典型场景：**
> "Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes."

**未来计划：** 将扩展支持更多事件源。

---

## 3. 实际应用场景（官方示例）

### Backlog 管理
- 每天自动分类新 issue
- 自动打标签、分配合适的人选
- 发 Slack 汇总通知

### 文档 Drift 检测
- 每周扫描合并的 PR
- 发现文档引用了已变更的 API
- 自动发起更新 PR

### 部署验证
- CD 流水线完成后触发
- Claude 执行冒烟测试
- 扫描错误日志检测回归
- 向发布频道发布 go/no-go 结果

### 告警整理
- Datadog 告警 → Routine endpoint
- Claude 拉取 Trace
- 关联近期部署记录
- **在 on-call 人员打开页面之前，修复方案草稿已准备好**

### 反馈处理
- 文档反馈 widget 或内部 dashboard 发送报告
- Claude 自动在对应仓库打开 session
- 起草修改方案

### 库接口同步
- Python SDK PR 合并后
- 自动触发 Routine 同步到 Go SDK
- 自动打开匹配的 PR

### 定制化代码审查
- PR 打开时自动运行团队检查清单
- 覆盖安全和性能检查
- 在人工审查之前留下内联评论

---

## 4. 定价与限制

| 计划 | 每天 Routines 上限 | 超出限制 |
|------|-------------------|----------|
| **Pro** | 5 个 | 可额外购买 |
| **Max** | 15 个 | 可额外购买 |
| **Team / Enterprise** | 25 个 | 可额外购买 |

**注意：** Routines 与交互式 Session 共用订阅用量限额。

**要求：** 需要 Claude Code on the web 已启用（Pro/Max/Team/Enterprise 计划）。

---

## 5. 如何开始使用

1. 访问 **claude.ai/code** 创建第一个 Routine
2. 或在 CLI 中输入 **/schedule**
3. 编写你的自动化 prompt，设置触发条件

---

## 6. 关键要点

- **Routines 将 Claude Code 从"需要人工触发"升级为"事件驱动的自动化引擎"**
- 支持多种触发方式（定时、API、Webhook），覆盖大多数自动化场景
- 云端执行，不占用本地资源，无需保持电脑开机
- 特别适合 DevOps 工作流、代码审查自动化、监控系统响应

---

## Sources

1. [Introducing Routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — Anthropic 官方博客
