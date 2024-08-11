from .primp import Response


def raise_for_status(res: Response) -> None:
    assert res.status_code == 200, (
        "Request failed with status code %s\nResponse:\n%s"
        % (res.status_code, res.text)
    )
