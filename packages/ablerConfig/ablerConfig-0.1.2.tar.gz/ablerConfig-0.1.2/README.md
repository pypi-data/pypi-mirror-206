ablerConfig
=============

简介
--

这是一个用于处理配置信息的Python包。它可以帮助应用程序读取、写入和验证配置文件。该包暂时只供彭彭项目组自用。

特点
--

*   支持JSON5格式的配置文件。
*   可以验证配置文件的格式和内容。
*   可以使用默认值填充缺失的配置项。
*   可以将配置文件转换为Python对象，以便更方便地访问和修改。
*   支持内部配置文件和本地外部配置文件。

依赖项
---

*   pyjson5
*   json5

安装
--

您可以使用pip安装abler\_config：

```bash
pip install ablerConfig
```

使用方法
----

### 加载配置文件

您可以使用`ablerConfig.Config()`函数加载配置文件。例如：

```python
import ablerConfig as config
config.Config(default='my-config', local_dir='ex-conf', show_message=my_show_message)
```

### 引用配置项

您可以使用`ablerConfig.Config.object_of()`方法引用配置文件中的配置对象，也可以使用`ablerConfig.Config.value_of()`方法将引用配置文件中的简单配置项。例如：

```python
from ablerConfig import Config, ConfigNode

conf = Config.object_of('alarm_control.state_send')
addr = tuple(Config.value_of('net_gate.tt_addr'))
```

