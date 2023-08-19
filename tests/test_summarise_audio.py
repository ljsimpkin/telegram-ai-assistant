import pytest
from models.summarise_audio import query, summarise_audio
from unittest.mock import Mock, patch

def test_query():
    # TODO: Add test cases for the query function

@patch('models.summarise_audio.query')
def test_summarise_audio(mock_query):
    # Mock the query function to return a specific value
    mock_query.return_value = "This is a test transcription"
    
    # Mock the update and context objects
    mock_update = Mock()
    mock_context = Mock()
    
    # Call the summarise_audio function
    result = summarise_audio(mock_update, mock_context)
    
    # Assert that the result is a string (text)
    assert isinstance(result, str)

def test_true_is_true():
    assert True is True
