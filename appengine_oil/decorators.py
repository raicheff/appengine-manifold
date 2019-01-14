#
# AppEngine-Oil
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


import functools

from flask import current_app, request
from werkzeug.exceptions import Forbidden


CRON_HEADER = ('X-Appengine-Cron', 'true')

CRON_IP = '10.0.0.1'


def cron_route(func):
    """
    Cron service scheduled task
    """

    # https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml

    @functools.wraps(func)
    def decorated_route():
        header_name, header_value = CRON_HEADER
        criteria = (
            request.remote_addr == CRON_IP,
            request.headers.get(header_name) == header_value,
        )
        if not (all(criteria) or current_app.debug):
            # logger.warning('scheduled_task: %s', request.remote_addr)
            raise Forbidden()
        func()
        return current_app.response_class(status=200)

    return decorated_route


# EOF
