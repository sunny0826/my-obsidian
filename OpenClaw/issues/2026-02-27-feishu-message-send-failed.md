---
title: "飞书消息发送失败 - research agent 无法发送消息到飞书群聊"
status: in_progress
priority: high
type: bug
created: "2026-02-27T16:13:00+08:00"
---

## 问题描述

- research agent 执行趋势研究后无法发送消息到飞书群聊
- 错误信息：Cross-context messaging denied: action=send target provider "feishu" while bound to "webchat"
- 目标群聊：oc_15f72eb48cb1ca05e0985f9ea0d7c4a0

## 错误原因分析

- subagent 运行在 webchat channel，无法直接发送飞书消息
- 需要使用主会话或特定配置来发送飞书消息

## 可能的解决方案

1. 在主会话中配置消息转发机制
2. 使用 message tool 的 gatewayToken/gatewayUrl 参数绑定到正确的飞书上下文
3. 考虑在 subagent 中配置 channel 映射
