

module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.name || (req.body && req.body.num)){
        var start = new Date().getTime();
        function A(i,j) {
            return 1/((i+j)*(i+j+1)/2+i+1);
        }
        function Au(u,v) {
            for (var i=0; i<u.length; ++i) {
                var t = 0;
                for (var j=0; j<u.length; ++j)
                t += A(i,j) * u[j];
                v[i] = t;
            }
        }
        
        function Atu(u,v) {
            for (var i=0; i<u.length; ++i) {
                var t = 0;
                for (var j=0; j<u.length; ++j)
                t += A(j,i) * u[j];
                v[i] = t;
            }
        }
        
        function AtAu(u,v,w) {
            Au(u,w);
            Atu(w,v);
        }
        
        function spectralnorm(n) {
            var i, u=new Float64Array(n), v=new Float64Array(n), w=new Float64Array(n), vv=0, vBv=0;
            for (i=0; i<n; ++i) {
                u[i] = 1; v[i] = w[i] = 0;
            }
            for (i=0; i<10; ++i) {
                AtAu(u,v,w);
                AtAu(v,u,w);
            }
            for (i=0; i<n; ++i) {
                vBv += u[i]*v[i];
                vv  += v[i]*v[i];
            }
            return Math.sqrt(vBv/vv);
        }

        var n = Number(req.body.num);

        spectralnorm(n)
        var end = (new Date().getTime() - start);


        context.res = {
            status: 200,
            body:"" + end
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