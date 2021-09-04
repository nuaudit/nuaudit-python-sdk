# nuaudit. Python SDK

## Installation

`pip install nuaudit-python-sdk`

## Usage

```python
from nuaudit_python_sdk import Nuaudit

nuaudit = Nuaudit(
    api_key="API_KEY_SECRET",
    organization_id="ORGANIZATION_ID",
    trail_id="TRAIL_ID"
)

nuaudit.create_record(
    description="Added artwork to the gallery",
    resource={
        "type": "artwork",
        "id": "thepainting",
        "title": "The painting",
        "material": "canvas",
        "paint": "oil",
        "year": 2018
    },
    identity={
        "type": "human",
        "id": "jane",
        "name": "Jane",
        "email": "jane@example.org",
        "ipAddress": "127.0.0.1"
    }
)
```