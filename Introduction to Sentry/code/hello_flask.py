from flask import Flask

app = Flask(__name__)


def setup_raven(dsn, app):
    from raven.contrib.flask import Sentry
    sentry = Sentry(dsn=dsn)
    sentry.init_app(app)


@app.route('/div/<int:m>/<int:n>')
def div(m, n):
    return m / n

if __name__ == '__main__':
    import os
    dsn = os.environ['SENTRY_DSN']
    setup_raven(dsn, app)
    app.run()
