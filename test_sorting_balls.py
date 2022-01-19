from rack import Rack



def test_rack():
    rack = Rack()
    rack.add(20)

    assert rack.balls() == [20] 

