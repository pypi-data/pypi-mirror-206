# telegram_urls_validator

Library for validating Telegram urls and brings them to one standart.

# How method works?

1. Add prefix "https://"
2. Change all hostnames to "t.me"
3. Convert "/+" invite links to "/joinchat/" type


# Examples
```python
from telegram_urls_validator import validate_url

validated_url = validate_url(url='t.me/PavelDurov')
# >> https://t.me/PavelDurov

validated_url = validate_url(url='telegram.me/PavelDurov')
# >> https://t.me/PavelDurov


validated_url = validate_url(url='t.me/+invitehash')
# >> https://t.me/joinchat/invitehash

```


# Installing

```commandline
pip3 install telegram_urls_validator
```
