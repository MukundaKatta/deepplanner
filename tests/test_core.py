from src.core import Planner
def test_init(): assert Planner().get_stats()["ops"] == 0
def test_op(): c = Planner(); c.decompose(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Planner(); [c.decompose() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Planner(); c.decompose(); c.reset(); assert c.get_stats()["ops"] == 0
