from importguard_app.checker import check_module, check_method

def test_stdlib_module_detected():
    assert check_module("os") == "stdlib"

def test_installed_module_detected():
    assert check_module("requests") == "installed"

def test_missing_module_detected():
    assert check_module("this_package_definitely_does_not_exist_xyz") == "missing"

def test_real_method_exists():
    assert check_method("requests", "get") is True

def test_fake_method_does_not_exist():
    assert check_method("requests", "get_jsonnn") is False