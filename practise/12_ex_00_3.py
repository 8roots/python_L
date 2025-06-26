'''
虽然我们可以使用套接字库手动通过 HTTP 发送和接收数据，但在 Python 中执行这项常见任务有一种更简单的方法，即使用 urllib 库。

使用 urllib，你可以像处理文件一样处理网页。你只需指明想要检索哪个网页，urllib 会处理所有的 HTTP 协议和头部细节。

使用 urllib 从 Web 读取 romeo.txt 文件的等效代码如下：'''
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# 代码: https://www.py4e.com/code3/urllib1.py
# 头部信息仍然被发送，但 urllib 代码会消耗掉头部信息，只将数据返回给我们。
'''
以下是逐行解析这段 Python 代码的功能和执行流程，该代码通过 `urllib.request` 模块从网络获取文本文件内容并打印：

---

### **1. 导入模块**
```python
import urllib.request
```
- 导入 Python 标准库中的 `urllib.request` 模块，用于打开和读取 URL 资源。

---

### **2. 打开网络连接**
```python
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
```
- **`urlopen()`** 函数：
  - 向指定的 URL (`http://data.pr4e.org/romeo.txt`) 发起 HTTP GET 请求
  - 返回一个 **类文件对象**（类似于打开的文件句柄）
  - 自动处理 HTTP 协议细节（如建立连接、发送请求头等）

---

### **3. 逐行读取并打印内容**
```python
for line in fhand:
    print(line.decode().strip())
```
- **`for line in fhand:`**：
  - 迭代读取返回的类文件对象
  - 每次迭代返回一行数据（以 `bytes` 类型存储）

- **`line.decode()`**：
  - 将字节数据（`bytes`）解码为字符串（`str`）
  - 默认使用 UTF-8 编码（可指定其他编码，如 `decode('gbk')`）

- **`strip()`**：
  - 移除每行首尾的空白字符（如换行符 `\n`、空格等）
  - 避免打印多余的空行

---

### **4. 隐式资源清理**
- 当 `with` 块结束时（或脚本结束时），`urlopen()` 返回的连接会自动关闭
- 无需手动调用 `fhand.close()`

---

### **代码执行流程**
```mermaid
sequenceDiagram
    participant Python
    participant Server
    Python->>Server: HTTP GET /romeo.txt
    Server->>Python: 返回HTTP响应 + 文本数据
    loop 逐行处理
        Python->>Python: 读取一行(bytes)
        Python->>Python: decode()转为字符串
        Python->>Python: strip()清理空白
        Python->>输出: 打印内容
    end
```

---

### **关键注意事项**
1. **编码问题**：
   - 如果解码失败（如编码不匹配），会抛出 `UnicodeDecodeError`
   - 可显式指定编码：`decode('utf-8')` 或 `decode('latin-1')`

2. **网络错误处理**：
   - 实际代码应添加异常处理：
     ```python
     try:
         fhand = urllib.request.urlopen(url)
         # ...处理数据...
     except urllib.error.URLError as e:
         print(f"网络错误: {e.reason}")
     ```

3. **性能优化**：
   - 对于大文件，建议使用 `with` 语句确保资源释放：
     ```python
     with urllib.request.urlopen(url) as fhand:
         for line in fhand:
             print(line.decode().strip())
     ```

---

### **扩展知识**
- 返回的 `fhand` 对象实际上是 `http.client.HTTPResponse` 实例
- 可通过以下方法获取更多信息：
  ```python
  print(fhand.status)      # HTTP状态码（如200）
  print(fhand.getheaders()) # 响应头信息
  ```

---

### **对比其他方法**
| 方法                | 优点                      | 缺点                      |
|---------------------|--------------------------|--------------------------|
| `urllib.request`    | Python 内置，无需安装      | 接口较底层                |
| `requests` 库       | 更简洁的API               | 需额外安装                |
| `socket` 原始操作   | 完全控制协议细节           | 代码复杂度高              |

例如用 `requests` 实现相同功能：
```python
import requests
response = requests.get('http://data.pr4e.org/romeo.txt')
for line in response.text.splitlines():
    print(line.strip())
```

这段代码展示了 Python 中最简单的网络文本读取操作，适合处理小型文本资源。
'''