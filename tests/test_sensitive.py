from userbot import is_sensitive

def test_emergency_word_detected():
    assert is_sensitive("hospital jaana padega") == True

def test_normal_message_not_sensitive():
    assert is_sensitive("kha liya tune?") == False

def test_urgent_detected():
    assert is_sensitive("urgent reply karo") == True