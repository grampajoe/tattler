class FakeClass(object):
    def method(self):
        return self

fake_object = FakeClass()

def fake_function():
    pass

def fake_factory():
    """Create an object after import."""
    return FakeClass()
