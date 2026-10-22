import pytestfrom app import calculate_averagedef 
test_average():    assert calculate_average([80, 90, 70]) ==
80def test_single_mark():    assert calculate_average([95]) 
== 95def test_empty_marks():    with 
pytest.raises(ValueError):        calculate_average([])