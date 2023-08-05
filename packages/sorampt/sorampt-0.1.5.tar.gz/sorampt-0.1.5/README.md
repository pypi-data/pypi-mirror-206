# Sorampt

用于控制台交互的提示工具包。

完全支持打字。 还支持异步！


## 安装

```bash
pip install sorampt
```

## 用法

### 输入

```python
from sorampt import InputPrompt

InputPrompt("What is your name?", validator=lambda string: True).prompt()
await InputPrompt("What is your name?", validator=lambda string: True).prompt_async()
```

### 确认

```python
from sorampt import ConfirmPrompt

ConfirmPrompt("Are you sure?", default_choice=False).prompt()
await ConfirmPrompt("Are you sure?", default_choice=False).prompt_async()
```

### 列表

```python
from sorampt import ListPrompt, Choice

ListPrompt("What is your favorite color?", choices=[Choice("Red"), Choice("Blue")]).prompt()
await ListPrompt("What is your favorite color?", choices=[Choice("Red"), Choice("Blue")]).prompt_async()
```

### 复选

```python
from sorampt import CheckboxPrompt, Choice

CheckboxPrompt("Choose your favorite colors", choices=[Choice("Red"), Choice("Blue")]).prompt()
await CheckboxPrompt("Choose your favorite colors", choices=[Choice("Red"), Choice("Blue")]).prompt_async()
```

## 选择数据

您可以将数据添加到选项中。 结果类型可以从数据类型推断出来。

```python
from sorampt import ListPrompt, Choice

result: Choice[str] = ListPrompt(
    "What is your favorite color?",
    choices=[
        Choice("Red", data="#FF0000"),
        Choice("Blue", data="#0000FF"),
    ],
).prompt()
print(result.data)
```

## 默认和取消


```python
from sorampt import InputPrompt

result = InputPrompt("Press Ctrl-C to cancel.").prompt(default="Cancelled")
assert result == "Cancelled"
```

```python
from sorampt import InputPrompt, CancelledError

try:
    InputPrompt("Press Ctrl-C to cancel.").prompt()
except CancelledError:
    # Do something
    pass
```

## 样式指南

有关更多信息，请参阅提示类的文档字符串。

```python
from sorampt import InputPrompt
from prompt_toolkit.styles import Style

InputPrompt("What is your name?").prompt(style=Style([("input": "#ffffff"), ("answer": "bold")]))
```

禁用 ansi 颜色：

```python
from sorampt import InputPrompt

InputPrompt("What is your name?").prompt(no_ansi=True)
```

## 从命令行尝试

```bash
sorampt -h
```
