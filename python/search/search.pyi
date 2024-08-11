def get_djs(response_text: str) -> str:
    """Gets the d.js element from the response text.

    Args:
        response_text (str): The response text.

    Returns:
        str: The d.js URL.

    Raises:
        RuntimeError: d.js was not found.
    """

def get_page_layout_from_djs(djs: str) -> str:
    """Gets the page layout from the d.js script content.

    Args:
        djs (str): The d.js script content.

    Returns:
        str: The page layout (unparsed JSON).
    """
