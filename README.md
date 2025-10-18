# 🔥 SmartFire - 智能消防监控管理系统

SmartFire 是一个基于 **Django** 的轻量级智能消防监控管理系统，支持设备监控、报警记录与权限区分（管理员 / 普通用户），可在 **Arch Linux** 与 **Windows** 平台运行。

---

## 🚀 一、在 Arch Linux 上运行

### 1️⃣ 克隆项目

```bash
git clone https://github.com/RetiredGuitar64/smartfire.git
cd smartfire
```

### 2️⃣ 创建虚拟环境并安装依赖

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ 启动服务

```bash
python manage.py runserver
```

浏览器访问：
> <http://127.0.0.1:8000/>

> ✅ 默认已包含演示数据，无需手动导入或迁移数据库。

---

## 🪟 二、在 Windows 上运行

### 1️⃣ 克隆项目

```bash
git clone https://github.com/RetiredGuitar64/smartfire.git
cd smartfire
```

### 2️⃣ 创建虚拟环境并安装依赖

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ 启动服务

```bash
python manage.py runserver
```

打开浏览器访问：
> <http://127.0.0.1:8000/>

> ✅ 系统自带演示数据，可直接使用。

---

## 📍 三、主要访问路径

| 页面 | 地址 |
|------|------|
| 设备管理 | <http://127.0.0.1:8000/devices/> |
| 报警记录 | <http://127.0.0.1:8000/alarms/> |
| 统计分析 | <http://127.0.0.1:8000/stats/dashboard/> |
| 管理后台（仅管理员） | <http://127.0.0.1:8000/admin/> |

---

## 🛠 常用命令

| 操作 | 命令 |
|------|------|
| 启动服务 | `python manage.py runserver` |
| 清理缓存 | `find . -type d -name "__pycache__" -exec rm -rf {} +` |

---
