def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""
    return bin(decimal).replace("0b", "")

