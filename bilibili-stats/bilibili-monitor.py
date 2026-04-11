#!/usr/bin/env python3
"""
B站 UP主监控脚本
目标: 红色幻想乡B号机形态 (UID: 8803699)
功能: 监控直播状态、视频发布，生成统计报告
"""

import json
import os
import sys
import time
import hashlib
from datetime import datetime
from pathlib import Path

# Bilibili API endpoints
API_BASE = "https://api.bilibili.com"

# Target UP主
TARGET_UID = "8803699"
TARGET_NAME = "红色幻想乡B号机形态"

# Data directory
DATA_DIR = Path.home() / "my-obsidian" / "bilibili-stats"
STATS_FILE = DATA_DIR / "stats.json"
HTML_FILE = DATA_DIR / "index.html"
MD_FILE = DATA_DIR / "report.md"

# Config
CRON_MARKER = "# bilibili-monitor-cron"


def get_json(url: str, headers: dict = None) -> dict:
    """Fetch JSON from URL with retry."""
    import urllib.request
    import urllib.error

    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://www.bilibili.com",
    }
    if headers:
        default_headers.update(headers)

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=default_headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
            else:
                return {"code": -1, "message": str(e)}
    return {"code": -1, "message": "failed"}


def get_user_info(uid: str) -> dict:
    """获取用户基本信息."""
    url = f"{API_BASE}/x/space/acc/info?mid={uid}&jsonp=jsonp"
    return get_json(url)


def get_live_status(uid: str) -> dict:
    """获取用户直播状态."""
    url = f"{API_BASE}/x/user/publicinfo?mid={uid}"
    return get_json(url)


def get_live_room_info(uid: str) -> dict:
    """获取直播间信息."""
    url = f"{API_BASE}/xlive/web-room/v2/index/getRoomPlayInfo?room_id=0&uid={uid}&req_type=2"
    return get_json(url)


def get_video_list(uid: str, pn: int = 1, ps: int = 30) -> dict:
    """获取用户视频列表."""
    url = f"{API_BASE}/x/space/wbi/arc/search?mid={uid}&pn={pn}&ps={ps}&jsonp=jsonp"
    return get_json(url)


def get_videos_all(uid: str, max_pages: int = 5) -> list:
    """获取用户所有视频 (最多 max_pages 页)."""
    all_videos = []
    for pn in range(1, max_pages + 1):
        data = get_video_list(uid, pn=pn, ps=30)
        if data.get("code") != 0:
            break
        vlist = data.get("data", {}).get("list", {}).get("vlist", [])
        if not vlist:
            break
        all_videos.extend(vlist)
        # 检查是否还有更多
        page_count = data.get("data", {}).get("page", {}).get("count", 0)
        if pn * 30 >= page_count:
            break
        time.sleep(0.5)
    return all_videos


def load_stats() -> dict:
    """加载现有统计数据."""
    if STATS_FILE.exists():
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "up_name": TARGET_NAME,
        "uid": TARGET_UID,
        "created_at": datetime.now().isoformat(),
        "updated_at": "",
        "live_sessions": [],
        "videos": [],
        "last_live_check": None,
        "last_video_check": None,
    }


def save_stats(stats: dict):
    """保存统计数据."""
    stats["updated_at"] = datetime.now().isoformat()
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def record_id(*args) -> str:
    """生成唯一记录ID."""
    return hashlib.md5("-".join(str(a) for a in args).encode()).hexdigest()[:12]


def format_duration(seconds: int) -> str:
    """格式化时长."""
    if seconds < 60:
        return f"{seconds}秒"
    elif seconds < 3600:
        m = seconds // 60
        s = seconds % 60
        return f"{m}分{s}秒"
    else:
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h}小时{m}分{s}秒"


def format_duration_short(seconds: int) -> str:
    """格式化时长 (短格式)."""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds//60}m"
    else:
        return f"{seconds//3600}h{seconds%3600//60}m"


def check_live_status(stats: dict) -> dict:
    """检查直播状态，返回更新信息."""
    result = {"live": False, "message": "", "started_at": None}

    # 方法1: 获取直播间信息
    room_data = get_live_room_info(TARGET_UID)
    room_info = room_data.get("data", {}) if room_data.get("code") == 0 else {}

    live_status = room_info.get("live_status", 0)
    room_id = room_info.get("room_id")

    if live_status == 1:
        result["live"] = True
        uname = room_info.get("uname", TARGET_NAME)
        title = room_info.get("title", "直播中")
        result["message"] = f"【直播中】{uname} - {title} (房间号:{room_id})"

        # 检查是否是新开始的直播
        last_session = stats.get("live_sessions", [])
        ongoing = [s for s in last_session if s.get("end_time") is None]
        if not ongoing:
            # 新直播
            now = datetime.now()
            new_session = {
                "id": record_id("live", TARGET_UID, now.isoformat()),
                "room_id": room_id,
                "title": title,
                "start_time": now.isoformat(),
                "end_time": None,
                "duration_seconds": 0,
                "platform": "bilibili",
            }
            stats.setdefault("live_sessions", []).insert(0, new_session)
            result["started_at"] = now.isoformat()
            result["new_session"] = new_session
    else:
        # 直播结束了？
        last_session = stats.get("live_sessions", [])
        ongoing = [s for s in last_session if s.get("end_time") is None]
        if ongoing:
            now = datetime.now()
            for session in ongoing:
                # 计算时长
                start = datetime.fromisoformat(session["start_time"])
                duration = int((now - start).total_seconds())
                session["end_time"] = now.isoformat()
                session["duration_seconds"] = duration
                result["ended_session"] = session
                result["message"] = f"【直播结束】{TARGET_NAME} 直播了 {format_duration(duration)}"

    stats["last_live_check"] = datetime.now().isoformat()
    return result


def check_videos(stats: dict) -> dict:
    """检查新视频，返回更新信息."""
    result = {"new_videos": [], "message": ""}

    videos = get_videos_all(TARGET_UID, max_pages=5)
    if not videos:
        return result

    existing_bvids = {v.get("bvid") for v in stats.get("videos", [])}
    new_videos = []

    for v in videos:
        bvid = v.get("bvid")
        if bvid and bvid not in existing_bvids:
            pubdate = v.get("pubdate", 0)
            pubdate_str = datetime.fromtimestamp(pubdate).strftime("%Y-%m-%d %H:%M:%S") if pubdate else "未知"
            duration = v.get("length", "00:00")
            # 解析时长为秒
            duration_seconds = 0
            try:
                parts = duration.split(":")
                if len(parts) == 2:
                    duration_seconds = int(parts[0]) * 60 + int(parts[1])
                elif len(parts) == 3:
                    duration_seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            except Exception:
                pass

            video_entry = {
                "id": record_id("video", bvid),
                "bvid": bvid,
                "title": v.get("title", ""),
                "description": v.get("description", ""),
                "pubdate": pubdate,
                "pubdate_str": pubdate_str,
                "duration": duration,
                "duration_seconds": duration_seconds,
                "play": v.get("play", 0),
                "video_review": v.get("video_review", 0),
                "aid": v.get("aid", 0),
                "pic": v.get("pic", ""),
                "owner_name": v.get("owner", {}).get("name", ""),
                "first_seen": datetime.now().isoformat(),
            }
            new_videos.append(video_entry)

    if new_videos:
        stats.setdefault("videos", []).insert(0, new_videos[0])  # 只加最新的一个
        result["new_videos"] = new_videos
        result["message"] = f"【新视频】{TARGET_NAME} 发布了《{new_videos[0]['title']}》"

    stats["last_video_check"] = datetime.now().isoformat()
    return result


def generate_html(stats: dict):
    """生成HTML页面."""
    live_sessions = stats.get("live_sessions", [])
    videos = stats.get("videos", [])

    # 计算直播统计
    total_live_hours = sum(s.get("duration_seconds", 0) for s in live_sessions) / 3600
    completed_sessions = [s for s in live_sessions if s.get("end_time")]
    ongoing_sessions = [s for s in live_sessions if not s.get("end_time")]

    # 计算视频统计
    total_video_duration = sum(v.get("duration_seconds", 0) for v in videos)
    total_plays = sum(v.get("play", 0) for v in videos)

    # 最近直播
    recent_lives = live_sessions[:10]
    recent_videos = videos[:20]

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>B站 UP主监控 - {TARGET_NAME}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f0f2f5; color: #333; line-height: 1.6; }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
  h1 {{ color: #00a1d6; margin-bottom: 20px; font-size: 28px; }}
  h2 {{ color: #222; margin: 25px 0 12px; font-size: 20px; border-left: 4px solid #00a1d6; padding-left: 10px; }}
  .card {{ background: #fff; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px; }}
  .stat-box {{ background: linear-gradient(135deg, #00a1d6, #23c8ff); color: #fff; border-radius: 10px; padding: 18px; text-align: center; }}
  .stat-box.orange {{ background: linear-gradient(135deg, #ff6b35, #f7c948); }}
  .stat-box.green {{ background: linear-gradient(135deg, #2ecc71, #27ae60); }}
  .stat-box.purple {{ background: linear-gradient(135deg, #9b59b6, #8e44ad); }}
  .stat-number {{ font-size: 32px; font-weight: bold; }}
  .stat-label {{ font-size: 13px; opacity: 0.9; margin-top: 4px; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th {{ background: #f7f9fa; text-align: left; padding: 10px 12px; font-size: 13px; color: #666; border-bottom: 2px solid #e8e8e8; }}
  td {{ padding: 10px 12px; font-size: 14px; border-bottom: 1px solid #f0f0f0; }}
  tr:hover {{ background: #fafbfc; }}
  .badge {{ display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold; }}
  .badge-live {{ background: #ff4757; color: #fff; }}
  .badge-done {{ background: #2ed573; color: #fff; }}
  .time {{ color: #888; font-size: 12px; }}
  .duration {{ color: #00a1d6; font-weight: bold; }}
  .title-link {{ color: #00a1d6; text-decoration: none; }}
  .title-link:hover {{ text-decoration: underline; }}
  .up-avatar {{ width: 80px; height: 80px; border-radius: 50%; margin-bottom: 10px; }}
  .header-info {{ display: flex; align-items: center; gap: 20px; }}
  .empty {{ color: #aaa; text-align: center; padding: 30px; font-size: 14px; }}
  .footer {{ text-align: center; color: #aaa; font-size: 12px; padding: 20px; }}
  .tag {{ background: #e8f4f8; color: #00a1d6; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; display: inline-block; margin-bottom: 3px; }}
  @media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: 1fr 1fr; }} table {{ font-size: 12px; }} }}
</style>
</head>
<body>
<div class="container">
  <h1>📺 B站 UP主监控面板</h1>

  <div class="card">
    <div class="header-info">
      <img class="up-avatar" src="https://api.bilibili.com/x/space/wbi/avatar?mid={TARGET_UID}&jsonp=jsonp" alt="avatar" onerror="this.src='https://static.hdslb.com/images/akari.jpg'">
      <div>
        <h2 style="border:none;padding:0;margin:0">{TARGET_NAME}</h2>
        <p class="time">UID: {TARGET_UID} · 最后更新: {stats.get('updated_at', 'N/A')}</p>
      </div>
    </div>
  </div>

  <div class="stats-grid">
    <div class="stat-box">
      <div class="stat-number">{len(live_sessions)}</div>
      <div class="stat-label">直播场次</div>
    </div>
    <div class="stat-box orange">
      <div class="stat-number">{total_live_hours:.1f}h</div>
      <div class="stat-label">累计直播时长</div>
    </div>
    <div class="stat-box green">
      <div class="stat-number">{len(videos)}</div>
      <div class="stat-label">发布视频数</div>
    </div>
    <div class="stat-box purple">
      <div class="stat-number">{format_duration_short(total_video_duration)}</div>
      <div class="stat-label">视频总时长</div>
    </div>
  </div>

  <h2>📡 直播记录</h2>
  <div class="card">
    <table>
      <thead>
        <tr>
          <th>状态</th>
          <th>开始时间</th>
          <th>结束时间</th>
          <th>直播时长</th>
          <th>房间号</th>
        </tr>
      </thead>
      <tbody>
"""

    if recent_lives:
        for s in recent_lives:
            badge_class = "badge-live" if s.get("end_time") is None else "badge-done"
            badge_text = "🔴 直播中" if s.get("end_time") is None else "✅ 已结束"
            start = s.get("start_time", "")[:19] if s.get("start_time") else "-"
            end = s.get("end_time", "")[:19] if s.get("end_time") else "进行中"
            dur = format_duration(s.get("duration_seconds", 0)) if s.get("end_time") else "进行中"
            room = s.get("room_id", "-")
            html += f"""        <tr>
          <td><span class="badge {badge_class}">{badge_text}</span></td>
          <td class="time">{start}</td>
          <td class="time">{end}</td>
          <td class="duration">{dur}</td>
          <td>{room}</td>
        </tr>
"""
    else:
        html += '        <tr><td colspan="5"><div class="empty">暂无直播记录</div></td></tr>\n'

    html += """      </tbody>
    </table>
  </div>

  <h2>🎬 视频列表</h2>
  <div class="card">
    <table>
      <thead>
        <tr>
          <th>标题</th>
          <th>发布于</th>
          <th>时长</th>
          <th>播放</th>
          <th>弹幕</th>
        </tr>
      </thead>
      <tbody>
"""

    if recent_videos:
        for v in recent_videos:
            title = v.get("title", "")
            bvid = v.get("bvid", "")
            pubdate = v.get("pubdate_str", "-")
            duration = v.get("duration", "-")
            play = v.get("play", 0)
            review = v.get("video_review", 0)
            html += f"""        <tr>
          <td><a class="title-link" href="https://www.bilibili.com/video/{bvid}" target="_blank">{title}</a></td>
          <td class="time">{pubdate}</td>
          <td class="duration">{duration}</td>
          <td>{play:,}</td>
          <td>{review:,}</td>
        </tr>
"""
    else:
        html += '        <tr><td colspan="5"><div class="empty">暂无视频记录</div></td></tr>\n'

    html += """      </tbody>
    </table>
  </div>

  <div class="footer">
    <p>由 Bilibili Monitor Agent 生成 · 更新时间: """ + stats.get("updated_at", "N/A") + """</p>
    <p>数据来源: Bilibili API</p>
  </div>
</div>
</body>
</html>"""

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] HTML generated: {HTML_FILE}")


def generate_markdown(stats: dict):
    """生成 Markdown 报告."""
    live_sessions = stats.get("live_sessions", [])
    videos = stats.get("videos", [])
    total_live_secs = sum(s.get("duration_seconds", 0) for s in live_sessions)
    total_video_secs = sum(v.get("duration_seconds", 0) for v in videos)

    md = f"""# B站 UP主监控报告

## {TARGET_NAME}

- **UID**: {TARGET_UID}
- **更新时间**: {stats.get('updated_at', 'N/A')}

---

## 直播统计

| 指标 | 数值 |
|------|------|
| 直播场次 | {len(live_sessions)} |
| 累计直播时长 | {format_duration(total_live_secs)} |
| 最后检查时间 | {stats.get('last_live_check', 'N/A')} |

### 直播记录

| 状态 | 开始时间 | 结束时间 | 时长 | 房间号 |
|------|----------|----------|------|--------|
"""

    for s in live_sessions[:20]:
        status = "🟢 直播中" if s.get("end_time") is None else "⚪ 已结束"
        start = s.get("start_time", "")[:19] if s.get("start_time") else "-"
        end = s.get("end_time", "")[:19] if s.get("end_time") else "进行中"
        dur = format_duration(s.get("duration_seconds", 0)) if s.get("end_time") else "进行中"
        md += f"| {status} | {start} | {end} | {dur} | {s.get('room_id', '-')} |\n"

    md += f"""
---

## 视频统计

| 指标 | 数值 |
|------|------|
| 视频数量 | {len(videos)} |
| 视频总时长 | {format_duration(total_video_secs)} |
| 最后检查时间 | {stats.get('last_video_check', 'N/A')} |

### 最近视频

| 标题 | 发布时间 | 时长 | 播放 | 弹幕 |
|------|----------|------|------|------|
"""

    for v in videos[:30]:
        title = v.get("title", "")[:40]
        pubdate = v.get("pubdate_str", "-")
        duration = v.get("duration", "-")
        play = v.get("play", 0)
        review = v.get("video_review", 0)
        bvid = v.get("bvid", "")
        md += f"| [{title}](https://www.bilibili.com/video/{bvid}) | {pubdate} | {duration} | {play:,} | {review:,} |\n"

    md += f"""
---

*由 Bilibili Monitor Agent 生成 · {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    with open(MD_FILE, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"[OK] Markdown report generated: {MD_FILE}")


def send_notification(message: str, channel: str = "openclaw-weixin"):
    """发送微信通知."""
    try:
        from main import BilibiliAllInOne
        import asyncio
        app = BilibiliAllInOne()

        async def do_notify():
            # 使用 message 工具发送通知
            pass

        asyncio.run(do_notify())
    except Exception:
        pass

    # 实际使用 message 工具
    print(f"[NOTICE] {message}")


def main():
    print(f"[{datetime.now().isoformat()}] === Bilibili Monitor Started ===")
    print(f"Target: {TARGET_NAME} (UID: {TARGET_UID})")

    # 加载现有数据
    stats = load_stats()
    print(f"Loaded existing stats: {len(stats.get('live_sessions',[]))} live sessions, {len(stats.get('videos',[]))} videos")

    # 检查直播状态
    print("Checking live status...")
    live_result = check_live_status(stats)
    if live_result.get("message"):
        print(f"  -> {live_result['message']}")

    # 检查视频
    print("Checking video list...")
    video_result = check_videos(stats)
    if video_result.get("message"):
        print(f"  -> {video_result['message']}")

    # 保存数据
    save_stats(stats)
    print(f"Saved stats to {STATS_FILE}")

    # 生成报告
    generate_html(stats)
    generate_markdown(stats)

    # 发送通知
    notify_msg = None
    if live_result.get("new_session"):
        notify_msg = f"🔴 【开播提醒】{TARGET_NAME} 开始了直播！"
    elif live_result.get("ended_session"):
        dur = live_result["ended_session"].get("duration_seconds", 0)
        notify_msg = f"⚪ 【下播通知】{TARGET_NAME} 直播结束，累计 {format_duration(dur)}"
    elif video_result.get("new_videos"):
        v = video_result["new_videos"][0]
        notify_msg = f"🎬 【新视频】{TARGET_NAME} 发布了《{v['title']}》"

    if notify_msg:
        print(f"\n[NOTIFICATION] {notify_msg}")
        try:
            import subprocess
            result = subprocess.run(
                ["openclaw", "message", "send", "--channel", "openclaw-weixin", "--message", notify_msg],
                capture_output=True, text=True, timeout=10
            )
            print(f"Notification sent: {result.returncode}")
        except Exception as e:
            print(f"Notification failed: {e}")

    print(f"[{datetime.now().isoformat()}] === Bilibili Monitor Finished ===")


if __name__ == "__main__":
    main()
