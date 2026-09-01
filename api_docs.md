# Restful-Booker API 接口文档

> **Base URL:** `https://restful-booker.herokuapp.com`
> **数据格式:** JSON（`Content-Type: application/json`）
> **接口数量:** 7 个

---

## 目录

1. [认证方式 (Authentication)](#1-认证方式)
2. [状态码说明 (Status Codes)](#2-状态码说明)
3. [数据模型 (Booking Object)](#3-数据模型)
4. [接口详情 (Endpoints)](#4-接口详情)
   - 4.1 获取 Token `POST /auth`
   - 4.2 查询订单 ID 列表 `GET /booking`
   - 4.3 创建订单 `POST /booking`
   - 4.4 查询订单详情 `GET /booking/{id}`
   - 4.5 整体更新订单 `PUT /booking/{id}`
   - 4.6 部分更新订单 `PATCH /booking/{id}`
   - 4.7 删除订单 `DELETE /booking/{id}`

---

## 1. 认证方式

该 API 支持两种认证方式，用于需要鉴权的接口（PUT / PATCH / DELETE）。

**方式一：Cookie Token**
```
Cookie: token=<token>
```

**方式二：HTTP Basic 认证**
```
Authorization: Basic base64(admin:password123)
```

Token 通过 `POST /auth` 接口获取，详见 [4.1](#41-获取-token-post-auth)。

---

## 2. 状态码说明

| 状态码 | 说明 |
|---|---|
| 200 | OK，请求成功 |
| 201 | Created，资源创建成功 |
| 400 | Bad Request，参数或请求体不合法 |
| 401 | Unauthorized，未认证 |
| 403 | Forbidden，鉴权失败，无权限 |
| 404 | Not Found，资源不存在 |
| 405 | Method Not Allowed，方法不允许（如目标资源不存在）|
| 418 | I'm a teapot，`Content-Type` 不受支持 |
| 500 | Internal Server Error，服务器内部错误 |

---

## 3. 数据模型

**Booking 对象** 是订单的基础数据结构，创建、更新、查询均围绕该结构。

```json
{
  "firstname": "Sally",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2013-02-23",
    "checkout": "2014-10-23"
  },
  "additionalneeds": "Breakfast"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `firstname` | string | 是 | 名 |
| `lastname` | string | 是 | 姓 |
| `totalprice` | number | 是 | 订单总价 |
| `depositpaid` | boolean | 是 | 押金是否已支付 |
| `bookingdates` | object | 是 | 入住/离店日期 |
| `bookingdates.checkin` | string | 是 | 入住日期，格式 `YYYY-MM-DD` |
| `bookingdates.checkout` | string | 是 | 离店日期，格式 `YYYY-MM-DD` |
| `additionalneeds` | string | 否 | 附加需求，如 `"Breakfast"` |

---

## 4. 接口详情

### 4.1 获取 Token `POST /auth`

登录并获取访问 Token，是后续鉴权接口的前置步骤。

**请求头**

| 参数 | 值 |
|---|---|
| `Content-Type` | `application/json` |

**请求体**

```json
{
  "username": "admin",
  "password": "password123"
}
```

**请求示例**

```bash
curl -X POST https://restful-booker.herokuapp.com/auth \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password123"}'
```

**成功响应 `200 OK`**

```json
{
  "token": "abc123"
}
```

**失败响应 `200 OK`**（携带 `reason` 字段）

```json
{
  "reason": "Bad credentials"
}
```

---

### 4.2 查询订单 ID 列表 `GET /booking`

获取所有订单的 ID 列表，支持按条件筛选。

**查询参数（可选，可组合）**

| 参数 | 类型 | 说明 |
|---|---|---|
| `firstname` | string | 按名字筛选 |
| `lastname` | string | 按姓氏筛选 |
| `checkin` | string | 按入住日期筛选（`YYYY-MM-DD`）|
| `checkout` | string | 按离店日期筛选（`YYYY-MM-DD`）|

**请求示例**

```bash
curl -X GET "https://restful-booker.herokuapp.com/booking?firstname=Sally&checkin=2013-02-23"
```

**成功响应 `200 OK`**

```json
[1, 2, 3]
```

---

### 4.3 创建订单 `POST /booking`

创建一笔新订单。

**请求头**

| 参数 | 值 |
|---|---|
| `Content-Type` | `application/json` |

**请求体**

订单数据结构，参见 [第 3 节 数据模型](#3-数据模型)。

**请求示例**

```bash
curl -X POST https://restful-booker.herokuapp.com/booking \
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
      "checkin": "2018-01-01",
      "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
  }'
```

**成功响应 `200 OK`**

```json
{
  "bookingid": 1,
  "booking": {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
      "checkin": "2018-01-01",
      "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
  }
}
```

**失败响应**

| 状态码 | 场景 |
|---|---|
| 400 | 字段值不合法 |
| 418 | `Content-Type` 不是 `application/json` |

---

### 4.4 查询订单详情 `GET /booking/{id}`

按 ID 查询单笔订单详情。

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `id` | number | 订单 ID |

**响应格式**（可选）

| 参数 | 值 |
|---|---|
| `Accept` | `application/json`（默认）或 `application/xml` |

**请求示例**

```bash
curl -X GET https://restful-booker.herokuapp.com/booking/1 \
  -H "Accept: application/json"
```

**成功响应 `200 OK`**

```json
{
  "firstname": "Sally",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2013-02-23",
    "checkout": "2014-10-23"
  },
  "additionalneeds": "Breakfast"
}
```

**失败响应**

| 状态码 | 场景 |
|---|---|
| 404 | 订单不存在 |

---

### 4.5 整体更新订单 `PUT /booking/{id}`

全量更新一笔订单，**请求体必须包含所有字段**。需要鉴权。

**请求头**

| 参数 | 值 |
|---|---|
| `Content-Type` | `application/json` |
| `Cookie` | `token=<token>` |

**请求体**

完整订单数据结构，参见 [第 3 节 数据模型](#3-数据模型)。

**请求示例**

```bash
curl -X PUT https://restful-booker.herokuapp.com/booking/1 \
  -H "Content-Type: application/json" \
  -H "Cookie: token=abc123" \
  -d '{
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
      "checkin": "2018-01-01",
      "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
  }'
```

**成功响应 `200 OK`**

返回更新后的完整订单对象：

```json
{
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
}
```

**失败响应**

| 状态码 | 场景 |
|---|---|
| 400 | 请求体不合法 |
| 403 | 未鉴权或鉴权失败 |
| 405 | 订单不存在 |

---

### 4.6 部分更新订单 `PATCH /booking/{id}`

仅更新指定字段，**请求体只需包含要修改的字段**。需要鉴权。

**请求头**

| 参数 | 值 |
|---|---|
| `Content-Type` | `application/json` |
| `Cookie` | `token=<token>` |

**请求体**

仅需传入要修改的字段：

```json
{
  "firstname": "James"
}
```

**请求示例**

```bash
curl -X PATCH https://restful-booker.herokuapp.com/booking/1 \
  -H "Content-Type: application/json" \
  -H "Cookie: token=abc123" \
  -d '{"firstname": "James"}'
```

**成功响应 `200 OK`**

返回更新后的完整订单对象：

```json
{
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
}
```

**失败响应**

| 状态码 | 场景 |
|---|---|
| 400 | 请求体不合法 |
| 403 | 未鉴权或鉴权失败 |
| 405 | 订单不存在 |

---

### 4.7 删除订单 `DELETE /booking/{id}`

删除一笔订单。需要鉴权。

**请求头**

| 参数 | 值 |
|---|---|
| `Cookie` | `token=<token>` |

**请求示例**

```bash
curl -X DELETE https://restful-booker.herokuapp.com/booking/1 \
  -H "Cookie: token=abc123"
```

**成功响应 `201 Created`**

响应体为空。

**失败响应**

| 状态码 | 场景 |
|---|---|
| 403 | 未鉴权或鉴权失败 |
| 405 | 订单不存在 |
