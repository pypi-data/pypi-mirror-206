from CirclesLocalLoggerPython.LoggerServiceSingleton import locallgr


def test_add():
    object_to_insert_1 = {
        'ipv4': 'ipv4-py',
        'ipv6': 'ipv6-py',
        'latitude': 33,
        'longitude': 35,
        'user_id': 0,
        'profile_id': 0,
        'activity': 'test from python',
        'activity_id': 0,
        'payload': 'payload from python',
        'updated_user_id': 0
    }
    locallgr.log(object=object_to_insert_1)
    conn = locallgr.get_pool().get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT payload FROM logger.logger_table ORDER BY timestamp DESC LIMIT 1;')
    result = cursor.fetchone()
    assert result[0] == object_to_insert_1['payload']


def test_add_message():
    message = 'message error from python'
    locallgr.log(message)
    conn = locallgr.getPool().get_connection()
    cursor = conn.cursor()
    sql = f"""SELECT payload FROM logger.logger_table WHERE payload = '{message}' ORDER BY timestamp DESC LIMIT 1;"""
    cursor.execute(sql)
    result = cursor.fetchone()
    assert result[0] == message
