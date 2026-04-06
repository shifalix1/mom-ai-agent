from unittest.mock import patch, MagicMock
from ai import get_ai_reply

@patch("ai.add_to_memory")
@patch("ai.load_memory", return_value=[])
@patch("ai.client.chat.completions.create")
def test_get_reply_returns_string(mock_create, mock_load, mock_add):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "haan mumma aa rahi hoon"
    mock_create.return_value = mock_response

    result = get_ai_reply("kab aaogi?")
    
    assert isinstance(result, str)
    assert len(result) > 0