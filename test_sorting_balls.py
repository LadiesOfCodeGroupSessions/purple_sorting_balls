from rack import Rack



def test_rack():
    rack = Rack()
    rack.add(20)
    rack.add(10)

    assert rack.balls() == [10,20] 

