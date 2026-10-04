from importguard_app.parser import extract_imports

def test_extract_imports_finds_requests():
    result = extract_imports("sample.py")
    assert "requests" in result

def test_extract_imports_finds_stdlib():
    result = extract_imports("sample.py")
    assert "os" in result
    assert "collections" in result