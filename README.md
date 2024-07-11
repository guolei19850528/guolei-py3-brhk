## 介绍

**天津博瑞皓科 API**

[官方文档](https://www.yuque.com/lingdutuandui)

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-brhk
```

## 目录说明

### Speaker Api 示例

```python
from guolei_py3_brhk.speaker import Api as SpeakerApi

speaker_api = SpeakerApi(
    base_url="https://speaker.17laimai.cn",
    token="token",
    id="id",
    version=1
)

# 通知语音播报
state = speaker_api.notify(message="测试推送通知")
if state:
    print("发送成功")
```
