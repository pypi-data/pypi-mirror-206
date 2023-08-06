# Create/update

Methods that create and update resources make use of [Pydantic](https://docs.pydantic.dev/) models that have been generated from the official [Harbor REST API Swagger schema](https://github.com/goharbor/harbor/blob/main/api/v2.0/swagger.yaml).

The endpoint methods themselves have no parameters beyond the single model instance that is passed as the request body. This is done so that models can be updated in the future without breaking the methods that use them. We are at all times beholden to the official Swagger schema, and the models are generated from that schema. To see how to disable this validation and pass arbitrary data to the API, see the [Validation](./validation.md/#validation) page.

## Create

Creating resources is done by calling the `create_*` methods on the client object. The model type expected for these methods is usually subtly different from the ones returned by `get_*` methods, and is usually named `*Req`.

```python
import asyncio
from harborapi import HarborAsyncClient
from harborapi.models import ProjectReq, ProjectMetadata

client = HarborAsyncClient(...)


async def main() -> None:
    project_path = await client.create_project(
        ProjectReq(
            project_name="test-project2",
            metadata=ProjectMetadata(
                public=True,
            ),
        )
    )
    print(f"Project created: {project_path}")


asyncio.run(main())
```

## Update

The various `update_*` methods on the client object expect a `*Req` model similar to the `create_*` methods. However, one important difference is that these methods expect one or more identifiers for the resource to update the as the first argument(s), and a model as the following argument.

```py
import asyncio
from harborapi import HarborAsyncClient
from harborapi.models import ProjectReq, ProjectMetadata

client = HarborAsyncClient(...)


async def main() -> None:
    # Update the project
    await client.update_project(
        "test-project",
        ProjectReq(
            metadata=ProjectMetadata(
                enable_content_trust="true",  # yeah, it's a string...
            ),
            # OR
            # metadata={"enable_content_trust": "true"}
        ),
    )


asyncio.run(main())
```

Generally, only a single identifier is required, but some endpoints require multiple identifiers to uniquely identify the resource to update, such as the [`update_project_member_role`][harborapi.HarborAsyncClient.update_project_member_role] method which expects both a project name/ID and a member ID.

The API implicitly updates only the fields that are set on the model instance, and leaves the rest of the values unchanged. This is not idiomatic REST when you consider that these are HTTP PUT requests, but in practice this is quite convenient for now. See the [Idiomatic REST updating](#idiomatic-rest-updating) section for more information on why this _might_ change in the future.

### Idiomatic REST updating

The update endpoints are exposed as HTTP PUT endpoints, which according to [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.4) should expect the full resource definition, not just the fields to update[^1]. However, manual testing has revealed this to not be the case; the API supports updating with partial models, and it only updates the fields that are present in the request body. When `harborapi` serializes models to JSON, it only includes fields that have been set, so this behavior is supported by default.

Despite this behavior, it might a good idea to pass the full resource definition to the `update_*` methods, as the support for partial updates through the API may change in the future independently of this library.

Below is an example demonstrating how to fetch the existing resource, use it to construct the update model, and then update the resource with the new model.

```py
import asyncio
from harborapi import HarborAsyncClient
from harborapi.models import ProjectReq

client = HarborAsyncClient(...)

async def main() -> None:
    # Get the project
    project = await client.get_project("test-project")

    # Create the update model from the existing project
    req = ProjectReq.parse_obj(
        project,
        # OR
        # optionally only include fields from the request model:
        # project.dict(include=ProjectReq.__fields__.keys()),
    )
    req.metadata.enable_content_trust = "true"

    # Update the project
    await client.update_project("test-project", req)


asyncio.run(main())
```


[`update_project()`][harborapi.client.HarborAsyncClient.update_project] expects a [`ProjectReq`][harborapi.models.Project] model, while the [`get_project()`][harborapi.client.HarborAsyncClient.get_project] method returns a [`Project`][harborapi.models.Project] model. How do we use the `Project` model to create a `ProjectReq`?

We can create a `ProjectReq` by passing the `Project` instance to the `parse_obj()` method on the `ProjectReq` class. This will create a new `ProjectReq` instance with the same values as the `Project` instance.

To only include values that are present in the `ProjectReq` model, we can first convert the model to a dictionary and use the `include` parameter with `ProjectReq.__fields__.keys()` as the argument, before passing it to `ProjectReq.parse_obj()`.


[^1]: You can defend this behavior with certain interpretations of this quote from the RFC: *When a PUT
   representation is inconsistent with the target resource, the origin
   server SHOULD either make them consistent, by transforming the
   representation or changing the resource configuration [...]*. However, this is implicit behavior that is not documented anywhere.
