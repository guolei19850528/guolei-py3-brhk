# guolei-py3-brhk

### a python3 library for brhk

### [Document](https://www.yuque.com/lingdutuandui/ugcpag/umbzsd#yG8IS)

## Example

```python
from guolei_py3_brhk.library.spearker import Api as SpeakerApi

speaker_api: SpeakerApi = SpeakerApi(
    base_url="https://speaker.17laimai.cn/",
    token="your token",
    id="your id",
    version=1
)

state: bool = speaker_api.notify(message="测试推送通知")
```
