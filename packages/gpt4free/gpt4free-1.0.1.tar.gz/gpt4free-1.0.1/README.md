[![PyPI version](https://badge.fury.io/py/gpt4free.svg)](https://badge.fury.io/py/gpt4free)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Downloads](https://static.pepy.tech/personalized-badge/gpt4free?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/gpt4free)

# gpt4free

decentralising the Ai Industry, just some language model api's... based on [gpt4free repository](https://github.com/xtekky/gpt4free)

## Supported Stable Api's
1. you
2. theb
3. forefront
4. usesless

## How Use ?

### Example Usage For You

```python

from gpt4free import you

# simple request with links and details
response = you.Completion.create(
    prompt="hello world",
    detailed=True,
    include_links=True, )

print(response.dict())

# {
#     "response": "...",
#     "links": [...],
#     "extra": {...},
#         "slots": {...}
#     }
# }

# chatbot

chat = []

while True:
    prompt = input("You: ")
    if prompt == 'q':
        break
    response = you.Completion.create(
        prompt=prompt,
        chat=chat)

    print("Bot:", response.text)

    chat.append({"question": prompt, "answer": response.text})
```

### Example Usage For Theb

```python
# import library
from gpt4free import theb

# simple streaming completion
for token in theb.Completion.create('hello world'):
    print(token, end='', flush=True)
print("")
```

### Example Usage For Forefront

```python

from gpt4free import forefront

# create an account
token = forefront.Account.create(logging=True)
print(token)

# get a response
for response in forefront.StreamingCompletion.create(token=token, prompt='hello world', model='gpt-4'):
    print(response.text, end='')

```


### Example Usage For Usesless

```python
from gpt4free import usesless

message_id = ""
while True:
    prompt = input("Question: ")
    if prompt == "!stop":
        break

    req = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)

    print(f"Answer: {req['text']}")
    message_id = req["id"]
```

