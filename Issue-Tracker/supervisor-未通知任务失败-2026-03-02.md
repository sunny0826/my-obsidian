---
created: 2026-03-02T22:17:00.000Z
severity: high
component: supervisor
type: bug
status: open
---

# Supervisor 巡视未通知任务失败

Cron 任务失败时，Supervisor 巡视未通知用户。

## 问题描述

- **问题**: Supervisor 巡视只运行健康检查脚本，未检查其他 Cron 任务状态
- **影响**: 趋势研究-晚间任务失败，但用户未收到通知
- **发现时间**: 2026-03-02 晚间

## 问题根源

1. Supervisor 巡视只运行健康检查脚本，未检查其他 Cron 任务状态
2. delivery.mode 是 "announce"（发到主会话），不是直接通知用户
3. 即使发现其他任务失败，也没有通知逻辑

## 解决方案

1. 修改 Supervisor 巡视任务，增加检查所有 cron 任务状态的逻辑
2. 配置正确的 delivery 方式，确保任务失败时发消息给用户

## 元信息

- **严重程度**: high
- **类型**: bug
- **组件**: supervisor
- **状态**: open
- **创建时间**: 2026/3/2 22:17

---

## 跟踪记录

| 时间 | 操作 | 说明 |
|------|------|------|
| 2026/3/2 22:17 | 创建 | 记录 Supervisor 巡视未通知任务失败问题 |
