from sample_config import DEFAULT_LABEL


def quick_check(label: str = DEFAULT_LABEL) -> str:
    """Return a short status message for the requested notebook check."""
    return f"{label}: ok"
