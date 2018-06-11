/**
 * Responds to any HTTP request that can provide a "message" field in the body.
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */
exports.helloWorld = (req, res) => {
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
    
    var n = req.body.n;
    spectralnorm(n).toFixed(9);
    var end = (new Date().getTime() - start);
    res.status(200).send(end.toString());
};