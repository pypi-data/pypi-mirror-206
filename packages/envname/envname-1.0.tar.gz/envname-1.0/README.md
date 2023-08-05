# 项目描述

为运行环境设置名称。

有时候，对于某些功能，我们也许希望在不同的环境上采用不同的方案来实现。以读写数据库为例：当程序在外网运行时，须通过数据库公网ip访问数据库；而当程序在内网运行时，我们可以通过数据库内网ip访问数据库以提高性能。

# 安装

```
pip install envname
```

# Bug提交、功能提议

您可以通过 [Github-Issues](https://github.com/lcctoor/lccpy/issues)、[微信](https://raw.githubusercontent.com/lcctoor/me/main/author/WeChatQR.jpg)、[技术交流群](https://raw.githubusercontent.com/lcctoor/me/main/ExchangeGroup/PythonTecQR.jpg) 与我联系。

# 关于作者

作者：许灿标

邮箱：lcctoor@outlook.com

[主页](https://github.com/lcctoor/me/blob/main/home.md) | [微信](https://raw.githubusercontent.com/lcctoor/me/main/author/WeChatQR.jpg) | [Python技术微信交流群](https://raw.githubusercontent.com/lcctoor/me/main/ExchangeGroup/PythonTecQR.jpg)

开源项目：[让 Python 更简单一点](https://github.com/lcctoor/lccpy#readme)

# 教程

### 创建环境名称

（cmd）：

```
envname set new_name
```

注：

1、名称不能包含空格和引号。

2、名称可以包含中⽂。

3、名称不限⻓度。

### 查看环境名称

（cmd）：

```
envname read
```

### 导入环境名称

```python
from envname import envname
```

# 支持作者1元

envname 是一个免费的开源项目，由个人维护。

每个小的贡献，都是构成车轮的一份子，可以帮助保持车轮完美旋转。

![donationQR.jpg](https://raw.githubusercontent.com/lcctoor/me/main/donation/donationQR_1rmb_200_200.jpg)
