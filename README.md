# plugin-dify

在 Amrita 内接入 Dify

## 使用方法

1. 安装插件

```shell
amrita plugin install amrita_plugin_dify
```

2. 配置插件

在 Bot 项目的.env 或者直接配置环境变量：

```dotenv
DIFY_API_KEY=<Dify API Key> # Dify API Key
DIFY_API_BASE=<Dify API Base> # Dify API Base URL(Default to `https://api.dify.ai/v1`)
```

之后在 Amrita 的**Chat 插件**配置文件的`[extra]`字段中，配置如下字段：

```toml
[extra]
...
DIFY_ENABLED = true # 是否启用Dify扩展
```
