# TAT 防御模块

[![TAT Defense](https://img.shields.io/badge/TAT-防御-blue)](../docs/defense/README.zh.md)
[![License](https://img.shields.io/badge/License-自定义-red)](../../LICENSE)
[![Status](https://img.shields.io/badge/Status-实验性-yellow)](../docs/defense/README.zh.md)

基于 TAT 的多层异常检测和洪流管理模块。

## 功能
- 结构故障检测（发散）
- 一致性损失跟踪（和谐）
- 时间异常检测
- 洪流重定向
- 图加密和偏移

## 配置
两种运行模式：
- **高精度** — 最小化误报。
- **高召回** — 最大化异常检测。

## 结果
在合成基准测试中：**F1 高达 0.757**，精度 1.0。

## 许可证
自定义 TAT 许可证 — 见 [LICENSE](../../LICENSE)。

## 状态
✅ 原型就绪，测试已完成。
