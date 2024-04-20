from datetime import datetime


def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return "test_user_" + time_stamp + "@yopmail.com"
