import pytest
from unittest.mock import Mock, patch
from rwp_example.rwp_download_url import download_url


# Mocking the requests library for testing purposes
@patch('rwp_example.rwp_download_url.urllib3.request')
def test_download_url_successful(mock_request):
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 200
    mock_response.data = b"Sample response data"
    mock_request.return_value = mock_response

    url = "https://example.com"
    file_path = "sample_file.txt"

    assert download_url(url, file_path) is True

    # Ensure that the file was saved correctly
    with open(file_path, "rb") as f:
        assert f.read() == b"Sample response data"


@patch('rwp_example.rwp_download_url.urllib3.request')
def test_download_url_failure(mock_request):
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 404
    mock_request.return_value = mock_response

    url = "https://example.com"
    file_path = "sample_file.txt"

    assert download_url(url, file_path) is False


@patch('rwp_example.rwp_download_url.urllib3.request')
def test_download_url_no_file(mock_request, capsys):
    # Mock the response object
    mock_response = Mock()
    mock_response.status = 200
    mock_response.data = b"Sample response data"
    mock_request.return_value = mock_response

    url = "https://example.com"

    assert download_url(url) is True

    expected = "b'Sample response data'\n"
    captured = capsys.readouterr()
    assert captured.err == ''
    assert captured.out == expected
