# api-test-framework 项目计划

> Restful-Booker 接口自动化测试框架（Day 5-6 合并日）
> 技术栈：pytest + requests + pytest-html

## 目标

用 pytest + requests 对 Restful-Booker 搭接口自动化框架，第一批跑绿 10~12 条用例。

## 官方资料（写用例的依据）

| 资源 | 网址 |
|---|---|
| 接口文档（主） | https://restful-booker.herokuapp.com/apidoc/index.html |
| GitHub 仓库 | https://github.com/mwinteringham/restful-booker |
| Postman 合集 | https://www.postman.com/automation-in-testing/restful-booker-collections |

### 接口清单（7 个）

| 接口 | 方法 | 鉴权 | 功能 |
|---|---|---|---|
| /booking | GET | 无 | 查订单列表 |
| /booking/{id} | GET | 无 | 查订单详情 |
| /booking | POST | 无 | 创建订单 |
| /booking/{id} | PUT | 需 token | 整体更新 |
| /booking/{id} | PATCH | 需 token | 部分更新 |
| /booking/{id} | DELETE | 需 token | 删除订单 |
| /auth | POST | 无 | 登录拿 token |

### 已知怪癖（面试可讲）

- POST /booking 返回 200（文档说 201）
- DELETE /booking/{id} 返回 201（规范应是 200/204）
- 错误密码登录返回 200 + {"reason": "Bad credentials"}（而非 4xx）
- 无效参数可能返回 500（而非 400）
- 数据每 10 分钟重置（测试要"自创建、自清理"）

### 鉴权方式

- 账号：admin / password123
- PUT/PATCH/DELETE 需要 token，用 Cookie 头传递：`Cookie: token=xxx`

## 目录结构（目标）

```
api-test-framework/
├── tests/
│   ├── conftest.py              ← token/base_url fixture（全局）
│   ├── test_auth.py             ← 登录成功/失败
│   ├── test_booking_create.py   ← 创建 + 参数化边界
│   ├── test_booking_get.py      ← 列表/详情/404
│   ├── test_booking_update.py   ← PUT/PATCH + 无token拒绝
│   └── test_booking_delete.py   ← DELETE + 无token拒绝
├── pytest.ini                   ← testpaths + addopts
├── requirements.txt             ← requests, pytest, pytest-html
└── README.md                    ← Day 6 写
```

## 分步执行（每步做完验收再下一步）

### 第 1 步：创建目录结构（5 分钟）
- PyCharm 新建项目：D:\暑假学习\api-test-framework（勾 venv）
- 项目 Terminal 装依赖：pip install requests pytest pytest-html
- 建 tests/ 文件夹

### 第 2 步：配置（10 分钟）
- pytest.ini：testpaths = tests / addopts = -v --tb=short
- tests/conftest.py：token fixture + base_url fixture

### 第 3 步：第一批用例（40 分钟）
- test_auth.py：2 条（成功 token 非空 / 错误密码含 reason）
- test_booking_create.py：4~6 条（创建成功 + 参数化边界 4 组 + 缺字段）
- test_booking_get.py：3 条（列表 200 / 详情一致 / 不存在 404）

### 第 4 步：增删改 + 鉴权（40 分钟）
- test_booking_update.py：3 条（PUT 成功 / 无token 403 / PATCH 部分更新）
- test_booking_delete.py：3 条（DELETE 201 / 无token 403 / 删后 GET 404）

### 第 5 步：全量 + 报告（15 分钟）
- pytest 全量跑
- pytest --html=report.html 生成报告

## 铁律

1. 代码自己写，opencode 只给提示和检查
2. 每步做完贴验收，确认后才下一步
3. 跑之前先看接口文档（挂代理）
4. 遇报错先自己读（看报错信息 → 想原因 → 不行再问）
5. 断言预期值以实际行为为准（怪癖要记录）
6. 测试数据要"自创建、自清理"（不依赖共享数据）