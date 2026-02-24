# Issue: Supervisor 巡视投递失败

- **创建时间**: 2026-02-22 09:38 GMT+8
- **严重程度**: high
- **组件**: cron
- **状态**: resolved

## 描述

巡视报告生成正常，但投递到飞书失败，连续失败多次。

错误信息：cron announce delivery failed

## 解决

- **解决时间**: 2026-02-22 10:06 GMT+8
- **解决方案**: 已将 payload.kind 从 agentTurn 改为 systemEvent

## 追踪

- **问题类型**: 投递失败
- **失败阶段**: 巡视报告生成正常，投递失败
- **错误信息**: cron announce delivery failed
