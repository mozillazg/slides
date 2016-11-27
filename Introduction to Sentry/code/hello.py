def setup_raven(dsn):
    from raven import Client
    from raven.conf import setup_logging
    from raven.handlers.logging import SentryHandler
    client = Client(dsn)
    handler = SentryHandler(client)
    setup_logging(handler)


def div(m, n):
    return m / n

if __name__ == '__main__':
    import logging
    import os
    dsn = os.environ['SENTRY_DSN']
    logging.basicConfig()
    setup_raven(dsn)
    m, n = 10, 0
    try:
        div(m, n)
    except Exception as e:
        logging.exception(e)
