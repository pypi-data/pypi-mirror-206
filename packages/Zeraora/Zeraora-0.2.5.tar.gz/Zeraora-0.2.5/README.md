<h1 align="center" style="padding-top: 32px">Zeraora</h1>

<div align="center">
    <a href="https://docs.python.org/zh-cn/3/whatsnew/index.html"><img src="https://img.shields.io/badge/Python-3.7%20%2B-blue.svg?logo=python&logoColor=yellow"></a>
    <a href="https://en.wikipedia.org/wiki/MIT_License"><img src="https://img.shields.io/badge/License-MIT-purple.svg"></a>
    <a href="https://pypi.org/project/Zeraora/"><img src="https://img.shields.io/pypi/v/zeraora?color=darkgreen&label=PyPI"></a>
    <a href=""><img src="https://img.shields.io/conda/v/conda-forge/zeraora"></a>
</div>
<div align="center">
    <i>长期维护的个人开源工具库</i>
    <br>
    <i>An utility Python package supports for my personal and company projects</i>
</div>

## 安装

使用 pip 直接安装：

```shell
pip install zeraora
```

## 用法

不能保证所有工具类和快捷函数自始至终都放在同一个子包，因此应该直接从根目录导入：

```python
from zeraora import BearTimer

with BearTimer() as bear:
    summary = 0
    for i in range(1000000):
        bear.step(f'loop to {i} now.')
        summary += i
```

亦或者：

```python
import zeraora

with zeraora.BearTimer() as bear:
    summary = 0
    for i in range(1000000):
        bear.step(f'loop to {i} now.')
        summary += i
```

但对于 `charsets` 和 `djangobase` 可以放心从子包导入：

```python
from random import choices
from zeraora.charsets import BASE64

def make_pwd(length: int) -> str:
    return ''.join(choices(BASE64, k=length))

if __name__ == '__main__':
    [
        print(make_pwd(16)) for _ in range(20)
    ]
```

## 文档

部分文档以 Markdown 格式存放在 [docs](./docs/README.md) 目录下。

源代码多数附带[类型标注](https://docs.python.org/zh-cn/3/glossary.html#term-type-hint)和[文档字符串](https://docs.python.org/zh-cn/3/glossary.html#term-docstring)（[reStructuredText](https://zh.wikipedia.org/wiki/ReStructuredText)格式），文档未尽事宜请移步源代码浏览。

## 兼容性

[Python 3.7](https://docs.python.org/zh-cn/3/whatsnew/3.7.html#summary-release-highlights) 开始 `dict` 正式按照插入顺序存储，考虑到 `dict` 是 Python 的基石，为了避免出现难以察觉的错误，因而将该版本定为兼容下限。这也是我接触过的项目中的最低运行版本，故而不太希望维护对更低版本的兼容。

项目会尽力保证向后兼容性，但还是建议在requirements中写明特定的版本号，避免因为版本更新或回退而出现棘手的错误。

## 更新

> 仅列出不兼容旧版的修改，其余变动见git历史。

### 0.2.5（2023-5-02）

- `OnionObject.__repr__()` 不再进行嵌套递归，现在嵌套的OnionObject对象会显示为 `OnionObject(...)` 。
- 去除 `OnionObject.__str__()` 方法，可以用 `import json` 后 `json.dumps(OnionObject())` 实现原来的效果。
- 更改 `BearTimer` 的默认打印格式。
- 将 `BearTimer.output()` 拆分为负责准备打印的 `record()` 和实现打印的 `handle()` 。

### 0.2.0（2023-4-12）

- 将 `JSONObject` 与 `JsonObject` 合并为 `OnionObject` ，并删去前述两个类。
