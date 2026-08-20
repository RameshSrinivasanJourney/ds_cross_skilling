import httpx


ALLOWED_ENDPOINTS = {
    "users": "https://jsonplaceholder.typicode.com/users",
    "posts": "https://jsonplaceholder.typicode.com/posts",
}


def call_rest_api(
    resource: str,
) -> dict:
    """
    Call an approved REST API resource.
    """

    if resource not in ALLOWED_ENDPOINTS:
        raise ValueError(
            f"Unsupported API resource: {resource}"
        )

    url = ALLOWED_ENDPOINTS[resource]

    try:

        response = httpx.get(
            url,
            timeout=10.0
        )

        response.raise_for_status()

        return {
            "resource": resource,
            "status_code": response.status_code,
            "data": response.json(),
        }

    except httpx.HTTPError as exc:

        return {
            "resource": resource,
            "error": str(exc),
        }