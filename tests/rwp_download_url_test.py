from unittest.mock import Mock, patch

from pytest import CaptureFixture

from rwp_example.rwp_download_url import download_url


# Mocking the requests library for testing purposes
@patch("rwp_example.rwp_download_url.urllib3.request")
def test_download_url_successful(mock_request: Mock) -> None:
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 200
    mock_response.data = b"Sample response data"
    mock_request.return_value = mock_response

    url = "https://example.com"
    file_path = "sample_file.txt"

    assert download_url(url, file_path) is True

    # Ensure that the file was saved correctly
    with open(file_path, "r") as f:
        assert f.read() == "Sample response data\n"


@patch("rwp_example.rwp_download_url.urllib3.request")
def test_download_url_failure(mock_request: Mock) -> None:
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 404
    mock_request.return_value = mock_response

    url = "https://example.com"
    file_path = "sample_file.txt"

    assert download_url(url, file_path) is False


@patch("rwp_example.rwp_download_url.urllib3.request")
def test_download_url_no_file(mock_request: Mock, capsys: CaptureFixture[str]) -> None:
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 200
    mock_response.data = b"Sample response data"
    mock_request.return_value = mock_response

    url = "https://example.com"

    assert download_url(url) is True

    expected = "Sample response data\n\n"
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == expected
