

module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.name || (req.body && req.body.num)) {
        var start = new Date().getTime();  
        var iter = Number(req.body.num);
        var multiplier = 1.0;
        var pos_or_neg = -1.0;
        var denom = 3.0;

        for (var i = 0; i < iter; i++) {
            multiplier += pos_or_neg / denom;
            denom += 2;
            pos_or_neg *= -1;
        }

        multiplier *= 4.0
        var end = (new Date().getTime() - start);;

        context.res = {
            // status: 200, /* Defaults to 200 */
            body: "" + end
        };
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass a name on the query string or in the request body"
        };
    }
    context.done();
};