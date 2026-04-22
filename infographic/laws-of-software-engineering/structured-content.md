# 软件工程定律大全 · 55条核心原则

## Overview
本信息图系统整理了软件工程领域最具影响力的 55 条定律，按 7 大维度分类呈现，涵盖架构、团队、规划、质量、规模、设计与决策。

## Learning Objectives
1. 了解软件工程的 7 大维度
2. 掌握每个维度最具代表性的定律
3. 理解这些定律如何在实际工作中指导技术决策

---

## 模块 1：Architecture（架构）

**核心主题**：系统架构决定了软件的演化路径与边界

**定律列表**：
- **Conway's Law**：组织的沟通结构决定了系统的设计
- **Hyrum's Law**：足够多的 API 用户会依赖你系统的所有可观察行为
- **Gall's Law**：复杂系统能工作，必然是从一个能工作的简单系统演化而来
- **The Law of Leaky Abstractions**：所有非平凡抽象在一定程度上都是漏的
- **Tesler's Law**：每个应用都有不可消除的固有复杂性，只能转移不能消除
- **CAP Theorem**：分布式系统只能同时保证一致性、可用性、分区容错中的两个
- **Second-System Effect**：小型成功系统之后往往跟着过度工程的替代品
- **Fallacies of Distributed Computing**：新手设计师常犯的 8 大分布式系统错误假设
- **Law of Unintended Consequences**：改变复杂系统时，预期会有意外
- **Zawinski's Law**：每个程序都会扩展到能读取邮件为止

**视觉元素**：三角形/层级结构示意，展示架构层级

---

## 模块 2：Teams（团队）

**核心主题**：人的协作方式决定了软件的产出质量

**定律列表**：
- **Brooks's Law**：给已经延期的项目加人会使其更延期
- **Dunbar's Number**：一个人能维持的稳定关系认知上限约为 150 人
- **The Ringelmann Effect**：团队规模越大，个人生产力越低
- **Price's Law**：参与者总数的平方根做了 50% 的工作
- **Putt's Law**：懂技术的人不管技术，管技术的人不懂技术
- **Peter Principle**：在层级中，每个员工都会晋升到其能力不胜任的级别
- **Bus Factor**：项目损失最少人员就会陷入严重困境的最小人数
- **Dilbert Principle**：公司倾向于提拔不称职的员工到管理层以限制其破坏力

**视觉元素**：人物剪影 + 组织结构图，引用符号 ♪ = 每条定律

---

## 模块 3：Planning（规划）

**核心主题**：时间与资源管理的核心约束

**定律列表**：
- **Premature Optimization (Knuth's Principle)**：过早优化是万恶之源
- **Parkinson's Law**：工作会膨胀到填满可用时间为止
- **The Ninety-Ninety Rule**：代码前 90% 占开发时间前 90%；剩余 10% 占后 90%
- **Hofstadter's Law**：事情总是比你预期的要久，即便你考虑了 Hofstadter's Law
- **Goodhart's Law**：当一个指标成为目标时，它就不再是好指标了
- **Gilb's Law**：任何需要量化的东西都有比不量化更好的测量方式

**视觉元素**：时间轴 + 进度条，示意时间压力

---

## 模块 4：Quality（质量）

**核心主题**：代码质量与测试的核心原则

**定律列表**：
- **The Boy Scout Rule**：让代码比你发现时更干净
- **YAGNI**：不要在必要之前添加功能
- **Murphy's Law**：任何会出错的事都会出错
- **Postel's Law**：对自己做事实保守，对别人接受的持开放态度
- **Broken Windows Theory**：不要留下未修复的破窗户（坏设计、错误决策、糟糕代码）
- **Technical Debt**：技术债务是所有拖慢我们速度的东西
- **Linus's Law**：足够的眼睛关注，所有 bug 都浅显
- **Kernighan's Law**：调试比写代码难一倍
- **Testing Pyramid**：项目应有大量快速单元测试、更少集成测试、少量 UI 测试
- **Pesticide Paradox**：重复运行相同测试，有效性会逐渐降低
- **Lehman's Laws of Software Evolution**：反映现实世界的软件必须演化，演化有可预测的极限
- **Sturgeon's Law**：90% 的东西都是垃圾

**视觉元素**：金字塔/测试三角形，示意测试层级

---

## 模块 5：Scale（规模）

**核心主题**：性能与网络效应的扩展规律

**定律列表**：
- **Amdahl's Law**：并行化加速受限于无法并行化的部分比例
- **Gustafson's Law**：通过增大问题规模可以实现并行处理的显著加速
- **Metcalfe's Law**：网络价值与用户数的平方成正比

**视觉元素**：扩展曲线图 + 网络节点连接示意

---

## 模块 6：Design（设计）

**核心主题**：代码与接口设计的核心哲学

**定律列表**：
- **DRY (Don't Repeat Yourself)**：每条知识必须有单一、明确、权威的表示
- **KISS (Keep It Simple, Stupid)**：设计越简单越好
- **SOLID Principles**：五大原则使代码更易维护和扩展（单一职责、开闭原则、里氏替换、接口隔离、依赖倒置）
- **Law of Demeter**：对象只应与直接朋友交互，不应与陌生人交互
- **Principle of Least Astonishment**：软件和接口的行为应最大程度减少对用户和其他开发者的意外

**视觉元素**：积木/模块组合，示意 SOLID 可组合性

---

## 模块 7：Decisions（决策）

**核心主题**：技术与管理的认知偏差与思维模型

**定律列表**：
- **Dunning-Kruger Effect**：对某事了解越少，越容易过度自信
- **Hanlon's Razor**：对于可以用愚蠢或疏忽解释的事，不要归于恶意
- **Occam's Razor**：最简单的解释往往是最准确的
- **Sunk Cost Fallacy**：即使放弃能帮助你，但因为已投入时间或精力而坚持选择
- **The Map Is Not the Territory**：我们对现实的表示不等于现实本身
- **Confirmation Bias**：倾向于支持现有信念或想法的信息
- **The Hype Cycle & Amara's Law**：短期高估技术效果，长期低估
- **The Lindy Effect**：事物使用时间越长，继续使用的可能性越大
- **First Principles Thinking**：将复杂问题分解为最基本单元再重建
- **Inversion**：通过考虑相反结果再反向推导来解决问题
- **Pareto Principle (80/20 Rule)**：80% 的问题来自 20% 的原因
- **Cunningham's Law**：在网上得到正确答案的最好方式不是提问，而是发布错误答案

**视觉元素**：天平/决策树，示意认知偏差与决策框架

---

## Data Points（关键引用原文）

- "Premature optimization is the root of all evil." — Donald Knuth
- "Adding manpower to a late software project makes it later." — Fred Brooks
- "Given enough eyeballs, all bugs are shallow." — Eric S. Raymond（Linus's Law）
- "Debugging is twice as hard as writing the code in the first place." — Brian Kernighan
- "Work expands to fill the time available for its completion." — Cyril Northcote Parkinson
- "A distributed system can guarantee only two of: consistency, availability, and partition tolerance." — Eric Brewer（CAP Theorem）
- "The value of a network is proportional to the square of the number of users." — Robert Metcalfe
- "80% of the problems result from 20% of the causes." — Vilfredo Pareto
- "Anything that can go wrong will go wrong." — Edward A. Murphy
- "We tend to overestimate the effect of a technology in the short run and underestimate the impact in the long run." — Roy Amara

---

## Design Instructions

- **语言**：全部中文
- **风格**：Corporate Memphis，扁平矢量插图，人物造型夸张，背景白或浅色
- **布局**：dense-modules（7 个模块网格，7 大维度）
- **尺寸**：竖版 portrait（9:16）
- **颜色**：紫色、橙色、青色、黄色等高饱和亮色
- **标题**：软件工程定律大全
- **副标题**：55条核心原则 · 7大维度
