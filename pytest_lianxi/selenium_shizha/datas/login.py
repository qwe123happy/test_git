login_data_success = [{'username': '15603389663', 'password': 'cb698754*', 'expected': '鲨媚鱼娇'},]

login_data_error = [
    {'username': '156033', 'password': 'cb698', 'expected': ''},
    {'username': '15603389663', 'password': 'cb698', 'expected': ''},
    {'username': '156063', 'password': 'cb698754*', 'expected': ''}
]

login_data_empty = [{'username': '', 'password': '*', 'expected': '0'},
                    {'username': '', 'password': 'cb698754*', 'expected': '0'},
                    {'username': '15603389663', 'password': '', 'expected': '0'}]
