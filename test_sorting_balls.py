def test_rack_one_ball():
    rack = Rack()
    rack.add(20)

    assert rack.balls() == [20]
