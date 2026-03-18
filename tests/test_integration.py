"""Integration tests for Deepplanner."""
from src.core import Deepplanner

class TestDeepplanner:
    def setup_method(self):
        self.c = Deepplanner()
    def test_10_ops(self):
        for i in range(10): self.c.decompose(i=i)
        assert self.c.get_stats()["ops"] == 10
    def test_service_name(self):
        assert self.c.decompose()["service"] == "deepplanner"
    def test_different_inputs(self):
        self.c.decompose(type="a"); self.c.decompose(type="b")
        assert self.c.get_stats()["ops"] == 2
    def test_config(self):
        c = Deepplanner(config={"debug": True})
        assert c.config["debug"] is True
    def test_empty_call(self):
        assert self.c.decompose()["ok"] is True
    def test_large_batch(self):
        for _ in range(100): self.c.decompose()
        assert self.c.get_stats()["ops"] == 100
