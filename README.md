# smsir

Python client for the [SMS.ir](https://sms.ir) REST API.

## Installation

```bash
pip install smsir
```

## Requirements

- Python >= 3.12
- httpx
- pydantic

## Usage

### Create Client

```python
from smsir import SMSIRClient

client = SMSIRClient("your-api-key")
```

Async client is also available:

```python
from smsir import AsyncSMSIRClient

async with AsyncSMSIRClient("your-api-key") as client:
    ...
```

### Send Bulk SMS

Send a message to multiple recipients from your dedicated line:

```python
from smsir import SMSIRClient
from smsir.endpoints import BulkSend

client = SMSIRClient("your-api-key")
result = client.execute(BulkSend(
    line_number=30004505000017,
    message_text="Your message here",
    mobiles=["09121234567", "09191234567"],
))
print(result.pack_id, result.message_ids, result.cost)
```

### Send Like-to-Like SMS

Send different messages to different numbers, paired one-to-one:

```python
from smsir.endpoints import LikeToLikeSend

result = client.execute(LikeToLikeSend(
    line_number=30004505000017,
    message_texts=["Message for user 1", "Message for user 2"],
    mobiles=["09121234567", "09191234567"],
))
```

### Send Scheduled SMS

Add `send_datetime` to any send endpoint for scheduled delivery:

```python
from datetime import datetime, timedelta

result = client.execute(BulkSend(
    line_number=30004505000017,
    message_text="Scheduled message",
    mobiles=["09121234567"],
    send_datetime=datetime.now() + timedelta(hours=2),
))
```

### Cancel Scheduled SMS

```python
from smsir.endpoints import CancelScheduledSend

result = client.execute(CancelScheduledSend(pack_id="2b99e63c-9bf8-4a21-..."))
print(result.returned_credit_count, result.sms_count)
```

### Send Verification Code

Send OTP/verification codes using a predefined template:

```python
from smsir.endpoints import VerifySend

result = client.execute(VerifySend(
    mobile="09191234567",
    template_id=123456,
    parameters={"Code": "12345"},
))
print(result.message_id, result.cost)
```

### Send via URL

Send a single SMS using username/password authentication:

```python
from smsir.endpoints import SendByURL

result = client.execute(SendByURL(
    username="your-username",
    password="your-api-key",
    line=30004505000017,
    mobile="09121234567",
    text="Hello!",
))
```

### Message Report

Get the status of a specific message:

```python
from smsir.endpoints import MessageReport

report = client.execute(MessageReport(message_id=86522023))
print(report.delivery_state, report.cost)
```

### Pack Report

Get all messages in a send pack:

```python
from smsir.endpoints import PackReport

messages = client.execute(PackReport(pack_id="2b99e63c-9bf8-4a21-..."))
for msg in messages:
    print(msg.mobile, msg.delivery_state)
```

### Pack List Report

List all send packs from today:

```python
from smsir.endpoints import PackListReport

packs = client.execute(PackListReport(page_size=50, page_number=1))
```

### Live Send Report

Get today's sent messages:

```python
from smsir.endpoints import LiveSendReport

messages = client.execute(LiveSendReport(page_size=100, page_number=1))
```

### Archived Send Report

Get sent messages from previous days:

```python
from datetime import datetime
from smsir.endpoints import ArchiveSendReport

messages = client.execute(ArchiveSendReport(
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 6, 1),
    page_size=100,
))
```

### Latest Received Messages

Get the most recent unread received messages:

```python
from smsir.endpoints import LatestReceive

messages = client.execute(LatestReceive(count=50))
```

### Live Received Messages

Get today's received messages:

```python
from smsir.endpoints import LiveReceive

messages = client.execute(LiveReceive(
    page_size=20,
    page_number=1,
    sort_by_newest=True,
))
```

### Archived Received Messages

Get received messages from previous days:

```python
from smsir.endpoints import ArchiveReceive

messages = client.execute(ArchiveReceive(
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 6, 1),
))
```

### Get Credit

Get your current account credit:

```python
from smsir.endpoints import GetCredit

credit = client.execute(GetCredit())
print(credit)  # 165.3
```

### Get Line Numbers

Get your available send lines:

```python
from smsir.endpoints import GetLines

lines = client.execute(GetLines())
print(lines)  # [10002155613464, 30004505000017]
```

## Error Handling

```python
from smsir.exceptions import APIError, AuthenticationError, RateLimitError

try:
    client.execute(BulkSend(...))
except AuthenticationError:
    print("Invalid API key")
except RateLimitError:
    print("Too many requests")
except APIError as e:
    print(f"API error: {e.message}")
    print(f"Status code: {e.api_status}")  # StatusCode enum
```

## License

MIT
