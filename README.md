# api-test-framework

基于 pytest + requests 的 Restful-Booker API 自动化测试框架。

## 技术栈

- Python 3.x
- pytest
- requests
- pytest-html

## 被测对象

Restful-Booker（开源接口测试靶场）：https://restful-booker.herokuapp.com

## 项目结构

```
├── tests/
│   ├── conftest.py              # 全局 fixture（base_url / token / booking）
│   ├── test_auth.py             # 登录鉴权
│   ├── test_booking_create.py   # 创建订单（含参数化边界值）
│   ├── test_booking_get.py      # 查询订单
│   ├── test_booking_update.py   # 更新订单（PUT / PATCH）
│   └── test_booking_delete.py   # 删除订单
├── pytest.ini
└── requirements.txt
```

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv .venv

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行测试
pytest

# 4. 生成测试报告
pytest --html=report.html
```

## 测试设计要点

- 使用 pytest fixture 管理测试数据（自创建自清理）
- 使用参数化覆盖边界值
- 覆盖接口鉴权（无 token 被拒）
