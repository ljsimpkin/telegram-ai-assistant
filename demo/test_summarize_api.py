import pytest
from summarize_api import summarize_text

def test_summarize_text():
    print("\n\n\n amazing this is where its at \n\n\n")
    text = "This is a long text that needs to be summarized."
    summary = summarize_text(text)
    assert len(summary) < len(text), "The summary is not shorter than the original text."
    assert summary != "", "The summary is empty."
