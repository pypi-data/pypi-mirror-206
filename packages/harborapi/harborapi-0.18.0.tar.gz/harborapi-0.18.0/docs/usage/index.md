# Usage

Most of the time you'll be instantiating a `harborapi.HarborAsyncClient` object and using it to interact with the Harbor API.

The `HarborAsyncClient` strives to provide most endpoints in the Harbor API spec as methods. See [Endpoints](../endpoints/index.md) for a complete list of implemented endpoints on `HarborAsyncClient`.

The methods are all asynchronous, and must be used in an async context, meaning they must be awaited inside an async function. If you are unsure how to do this, the FastAPI package's docs has a [good section on `async` and `await`](https://fastapi.tiangolo.com/async/#async-and-await). The examples in [Recipes](../recipes/index.md) should give a fairly good idea of how to use the client.


```python
from harborapi import HarborAsyncClient

client = HarborAsyncClient(...)
```

There are multiple ways to authenticate with the Harbor API, and they are documented on the [Authentication](authentication.md) page. The [Methods](methods) page shows basic usage of the different types of methods exposed by the client object. For more advanced usage, check out the [Recipes](/recipes) section.
