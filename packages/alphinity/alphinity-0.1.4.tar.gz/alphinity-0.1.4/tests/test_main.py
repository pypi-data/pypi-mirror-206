import subprocess


def test_command_line_interface() -> None:
    # Test encoding a value of 0
    result = subprocess.run(
        ["python3", "-m", "alphinity", "0"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "a"

    # Test encoding a value of 1
    result = subprocess.run(
        ["python3", "-m", "alphinity", "1"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "ba"

    # Test encoding a value of 2
    result = subprocess.run(
        ["python3", "-m", "alphinity", "2"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "bb"

    # Test encoding a value of 27
    result = subprocess.run(
        ["python3", "-m", "alphinity", "27"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "caa"

    # # Test encoding bad arguments
    result = subprocess.run(
        ["python3", "-m", "alphinity", "arf"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "Usage: alphinity [value_to_encode]"

    # Test passing no arguments
    result = subprocess.run(
        ["python3", "-m", "alphinity"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "Usage: alphinity [value_to_encode]"
