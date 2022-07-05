

def test_conf_file(get_spark_session_from_conf_file):
    assert "spark" in get_spark_session_from_conf_file