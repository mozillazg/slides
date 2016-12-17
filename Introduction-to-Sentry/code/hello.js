var app = require('express')();
var raven = require('raven');

var raven_dsn = process.env.SENTRY_DSN;

// The request handler must be the first item
app.use(raven.middleware.express.requestHandler(raven_dsn));

app.get('/div/:m/:n', function mainHandler(req, res) {
    var m = parseInt(req.params.m);
    var n = parseInt(req.params.n);
    var result = m / n;
    throw new Error('Broke!');
});

// The error handler must be before any other error middleware
app.use(raven.middleware.express.errorHandler(raven_dsn));

app.listen(3000);
