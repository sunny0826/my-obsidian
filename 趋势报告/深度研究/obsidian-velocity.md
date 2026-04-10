# Obsidian Velocity: Deep Research Report

*Generated: 2026-04-10 | Sources: 6 | Confidence: High*

---

## Executive Summary

**Obsidian Velocity** (GitHub: `Gonzalo-D-Sales/obsidian-velocity`) is a radically modern, macOS-inspired theme for Obsidian.md — developed over **14 months** by a single independent developer (Gonzalo-D-Sales). Despite being a one-person project with no company backing, it has garnered **974 stars** and **26 forks**, demonstrating strong community resonance. The theme positions itself as a "future-forward, cold-austere" aesthetic — deliberately avoiding the rainbow-folder trends common in the Obsidian theme ecosystem. Development is active, with v2.1.0 released February 2026 and consistent updates over the past 4 months.

---

## 1. Project Overview

| Metric | Value |
|--------|-------|
| **Repository** | [Gonzalo-D-Sales/obsidian-velocity](https://github.com/Gonzalo-D-Sales/obsidian-velocity) |
| **Stars** | 974 ⭐ |
| **Forks** | 26 |
| **Language** | SCSS |
| **License** | GNU GPLv3 |
| **Created** | 2024-12-23 |
| **Last Push** | 2026-02-16 |
| **Latest Release** | v2.1.0 (2026-02-03) |
| **Primary Contributor** | Gonzalo-D-Sales (656 commits) |
| **Topics** | obsidian-theme, light-theme, dark-theme, obsidian-md |

---

## 2. Design Philosophy

### 2.1 "Radically Modern" Aesthetic
Velocity's stated goal: **"The theme of tomorrow, in your hands today."**

Key design principles:
- **Cold, austere, near-totally neutral** — intentionally devoid of decorative distraction
- **macOS-native inspired** — strong influence from Cupertino theme
- **Fluid over Tactile** — current "Fluid" design language emphasizes smooth interactions, reduces visual noise
- **Premium and polished** — like "straight out of a native macOS app"

### 2.2 Deliberate Omissions
The developer has intentionally left out popular features:
- ❌ Rainbow folders and headings (conflicts with visual identity)
- ❌ Tactile/retro-futuristic decorations (evolved past them)
- ✅ Focus on refinement over novelty

### 2.3 Evolution: Four Generations

| Generation | Design Language | Period |
|------------|-----------------|--------|
| 1st | Retro-futuristic (2000s racing game aesthetic) | Early development |
| 2nd | Kinetic | Mid-development |
| 3rd | Tactile | Pre-2.0 |
| 4th | **Fluid** (current) | v2.0+ |

---

## 3. Key Features

### 3.1 CSSClasses System
Velocity provides **note-level styling utilities** via CSSclasses:

| Class | Function |
|-------|----------|
| `override` | Disable other cssclasses in the note |
| `hide-metadata` | Hide properties panel |
| `hide-title` / `show-title` | Toggle inline title visibility |
| `style-justify` | Justify paragraph/blockquote/callout text |
| `style-margin-top` | Add top padding |
| `style-wide` | Disable readable width limit |
| `large-heading` | Larger H1 heading |
| `super-heading` | Extra-bold H1 without underline |
| `simple-title` | Standard heading style for inline title |

### 3.2 Auto-Hide Sidebars
Originally pioneered by MicroMike's "mini-mode" — sidebars automatically hide when window width is too narrow, preventing cramped layouts.

**Can be disabled via Style Settings.**

### 3.3 Math Callouts
Custom callout syntax: `> [!math]` with optional color: `> [!math-red]`
- Inspired by outlined mathematics textbook aesthetics
- Supports all default Obsidian rainbow colors

### 3.4 Plugin Support
- **Full support**: Pretty Properties (v2.1.0)
- **Partial support**: Alternative Checkboxes (prototype in v2.1.0)
- **Styled**: Calendar plugin sidebar, PDF viewer controls, Bases Table/Card views, Ribbon icons

### 3.5 Style Settings Integration
Two configuration layers:
- **Quick Settings**: Easy layout and color changes
- **Configurator**: Deep dive into Velocity's features

---

## 4. Color Schemes

Velocity ships with multiple paint schemes for both light and dark mode:
- ✅ Light and dark mode variants
- ✅ Multiple color schemes
- ✅ Mobile responsive
- **Style Settings plugin** required for customization

---

## 5. Development & Community

### 5.1 Release History (Recent)

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.1.0 | 2026-02-03 | Pretty Properties support, Alternative Checkboxes prototype, tab interaction refinement |
| v2.0.0 | 2026-01-06 | Major redesign — "Fluid" design language, reduced visual noise |
| v1.3.0 | 2025-09-01 | Math callouts, new dark mode colors, FAB improvements |
| v1.1.3 | 2025-07-31 | Stacked Tabs, custom icons, dashed list styling |

### 5.2 Known Issues
> [!WARNING]
> As of 2026-02-03, maintainer was sick — new issues not worked on for 1-2 weeks.

> [!CAUTION]
> **Critical Issue #101**: Users with **out-of-date Obsidian installer versions** experience crashes/blank screen due to newer CSS features incompatibility. **Fix: Reinstall Obsidian.**

### 5.3 Issues Policy
- Issues only read/worked on **during weekends**
- No guarantee of same-week resolution
- Feature requests welcome but evaluated case-by-case

---

## 6. Competitive Landscape

| Theme | Stars | Focus | License |
|-------|-------|-------|---------|
| **Velocity** | 974 | Modern, macOS-inspired, austere | GPLv3 |
| Sanctum | ? | Typography-focused | ? |
| Cupertino | ? | macOS native | ? |
| Border | ? | Border aesthetics | ? |
| Mado | ? | Minimal flow | ? |

**Velocity's differentiation**: Deliberately anti-trend (no rainbow folders), premium polish, Fluid interaction design, strong typography.

---

## 7. Inspirations & Credits

### Theme Influences
- **Sanctum** — typography, icon modifications
- **Cupertino** — macOS interaction design, overall layout
- **Border, Mado, Composer** — earlier code references
- **Primary** — modernist synthesis, attention to detail
- **Willemstad** — community themes page styling
- **MicroMike** — Auto-hide feature origin
- **Maple** — document search styling
- **CreArts** — preview images for color schemes

### Key People
- **bladeacer** — close friend, fellow theme dev, Flexcyon creator, encouraged SCSS migration
- **kapirklaa/ElsaTam** — Fancy-a-Story theme developer, CSS advice early in development

---

## 8. Technical Notes

### Requirements
- Obsidian.md (latest installer version — **important!**)
- Style Settings plugin (for customization)

### Installation
1. Install via Obsidian Community Themes browser
2. Or clone to `.obsidian/themes/`

### SCSS-based
- Converted from plain CSS to SCSS for better structure
- Single main contributor (Gonzalo-D-Sales)

---

## 9. Key Takeaways

1. **One-person passion project** with professional-grade output (974 stars in ~4 months)
2. **Design evolution story** — from retro-futuristic to cold-austere modern (4 generations)
3. **Anti-trend positioning** — deliberately excludes rainbow folders, popular in Obsidian ecosystem
4. **Active maintenance** — regular updates despite single-dev constraint
5. **Known compatibility risk** — requires latest Obsidian installer (CSS feature dependency)
6. **Community-driven** — credits multiple other theme devs, collaborative ecosystem
7. **GPLv3** — open source but copyleft

---

## Sources

1. [GitHub - obsidian-velocity](https://github.com/Gonzalo-D-Sales/obsidian-velocity) — Main repository
2. [v2.1.0 Release](https://github.com/Gonzalo-D-Sales/obsidian-velocity/releases/tag/v2.1.0) — Latest release notes
3. [v2.0.0 Release](https://github.com/Gonzalo-D-Sales/obsidian-velocity/releases/tag/v2.0.0) — Fluid design language intro
4. [Obsidian.md](https://obsidian.md) — Platform
5. [Style Settings Plugin](https://obsidian.md/plugins?id=obsidian-style-settings) — Required plugin
6. [Alternative Checkboxes Reference Set](https://github.com/damiankorcz/Alternative-Checkboxes-Reference-Set) — Planned feature

---

*Report generated by OpenClaw Deep Research | Data: 2026-04-10*
