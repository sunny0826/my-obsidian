# sync-schedule.js 删除原因

## 删除时间

**Commit ID**: 1fa5c9d89ca986eec9769ea1cde06c76de48d5e9
**Commit Date**: 2026-02-10 21:53:58 (08:00)
**Commit Message**: Remove schedule reminder functionality

## 删除原因

根据 commit 记录，这次删除是为了**简化系统**：

- Delete schedule-reminder.js
- Clean up HEARTBEAT.md - remove REMINDER_CHECK cron job
- Clean up SCHEDULE.md - remove reminder logic and examples

## 删除内容

**删除的文件：**
- `schedule-reminder.js` - 日程提醒脚本
- HEARTBEAT.md 中的 REMINDER_CHECK cron job 配置
- SCHEDULE.md 中的提醒逻辑和示例

**删除的同步脚本：**
- `sync-schedule.js` - 从 schedule.json 同步到 Google Calendar 的脚本

**修改的文件：**
- `HEARTBEAT.md` - 移除提醒相关配置
- `SCHEDULE.md` - 移除提醒逻辑和示例
- `schedule.json` - 简化（去除了部分配置）
- `skills/schedule.js` - 调整了相关逻辑

## 删除时的想法（推测）

根据 commit 消息和当时上下文，可能的原因：

1. **简化系统**：日程提醒功能增加复杂度，决定移除
2. **避免重复功能**：可能有其他方式（如 Google Calendar 自带提醒）
3. **降低维护成本**：少维护一个脚本和 cron job

## 问题出现

**副作用：**
- 删除 sync-schedule.js 后，`schedule.json` 无法自动从 Google Calendar 同步
- 导致晨间简报显示"今日暂无安排"
- 用户需要在 Google Calendar 中新增日程后，手动同步到 `schedule.json`

## 解决方案

**已创建的双向同步脚本：**
- `skills/calendar-bidirectional-sync.js` - 从 Google Calendar 同步到 schedule.json
- 晨间简报 cron 已更新为先生成简报前先运行双向同步

## 建议

保留以下同步脚本（根据使用场景选择）：

1. **sync-schedule.js**（已删除，如需恢复可从 git 历史恢复）：
   - 功能：从 `schedule.json` 同步到 Google Calendar
   - 适用：在本地添加日程后，同步到云端

2. **calendar-bidirectional-sync.js**（新建）：
   - 功能：从 Google Calendar 同步到 `schedule.json`
   - 适用：在 Google Calendar 添加日程后，同步到本地
   - 已集成到晨间简报 cron 中

3. **calendar-sync.js**（已存在）：
   - 功能：查看、添加、同步日程
   - 适用：手动管理日程

如果需要完全的双向自动同步，可以考虑：
- 恢复 `sync-schedule.js`
- 配置两个 cron job：
  - 定时从 Google Calendar 同步到 `schedule.json`
  - 定时从 `schedule.json` 同步到 Google Calendar
