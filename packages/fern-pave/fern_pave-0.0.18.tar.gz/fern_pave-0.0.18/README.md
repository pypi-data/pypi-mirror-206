
# Pave Python Library

[![pypi](https://img.shields.io/pypi/v/fern-pave.svg)](https://pypi.python.org/pypi/fern-pave)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Documentation

API documentation is available at <https://docs.pave.dev/>.

## Installation

```bash
pip install fern-pave
# or
poetry add fern-pave
```

## Usage

```python
import datetime as dt
from pave.client import Pave

pave_client = Pave(api_key="YOUR_API_KEY")

user_financial_health = pave_client.cashflow.get_financial_health(
    user_id='USER_ID',
    start_date=dt.datetime(2020, 5, 17),
    end_date=dt.datetime(2022, 2, 15),
)

print(user_financial_health)
```

## Async client

This SDK also includes an async client, which supports the `await` syntax:

```python
import asyncio
from pave.client import AsyncPave

pave_client = AsyncPave(api_key="YOUR_API_KEY")

async def get_user_financial_health() -> None:
    user_financial_health = await pave_client.cashflow.get_financial_health(
        user_id='USER_ID',
        start_date=dt.datetime(2020, 5, 17),
        end_date=dt.datetime(2022, 2, 15),
    )
    print(user_financial_health)

asyncio.run(get_user_financial_health())
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
