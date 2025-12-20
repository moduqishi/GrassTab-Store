<div align="center">

# 🛒 GrassTab Store

**GrassTab 扩展的官方应用和小部件数据仓库**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green)](https://moduqishi.github.io/GrassTab-Store/)
[![Data](https://img.shields.io/badge/Data-JSON-blue)]()

[🌐 在线预览 Store 界面](https://moduqishi.github.io/GrassTab-Store/)

</div>

---

## 📖 简介

这是一个静态数据仓库，为 GrassTab 扩展提供在线应用商店和组件市场的数据支持。所有的应用信息、小部件定义和图标映射都托管在这里。

GrassTab 扩展会定期从这里拉取最新的 `apps.json` 和 `widgets.json`，确保用户能第一时间获取最新的资源。

---

## 📁 数据结构

### 1. [apps.json](apps.json)
包含所有已收录的快捷方式应用数据。

```json
[
  {
    "id": "com.example.app",    // 唯一标识符
    "name": "Example App",      //应用名称
    "description": "这是描述",   // 简短描述
    "icon": "https://...",      // 图标 URL (推荐 unavatar.io)
    "category": "Productivity", // 分类
    "url": "https://example.com"// 目标链接
  }
]
```

### 2. [widgets.json](widgets.json)
包含所有可用的小部件定义。

```json
[
  {
    "id": "com.widget.clock",
    "name": "时钟",
    "type": "clock",           // 小部件内部类型
    "defaultSize": "2x1",      // 默认尺寸
    "preview": "https://..."   // 预览图 URL
  }
]
```

---

## 🛠️ 辅助工具

本项目包含一些 Python 脚本，用于维护数据质量：

- **`extract_names.py`**: 从数据文件中提取所有应用名称，用于生成 AI 关键词或索引。
- **`import_descriptions.py`**: 批量导入或更新应用描述。

---

## 🤝 贡献指南

如果您想推荐一个网站或小部件加入 GrassTab Store：

1. **Fork 本仓库**。
2. 编辑 `apps.json`，追加您的网站信息。
   - 请确保 `id` 全局唯一（建议使用反向域名格式，如 `com.google.mail`）。
   - 图标建议使用 `https://icon.horse/icon/[domain]` 或 `https://unavatar.io/[domain]`。
3. 提交 Pull Request。

### 图标要求
为了保证视觉统一，请优先使用高清晰度的透明背景 PNG 图标，或使用我们推荐的图标 API 服务。

---

## 📄 许可证

本项目数据采用 [CC0 1.0 通用](LICENSE) (CC0 1.0 Universal) 协议，即放弃所有版权，您可以自由复制、修改、分发这些数据。
