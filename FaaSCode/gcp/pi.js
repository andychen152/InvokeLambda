exports.helloWorld = (req, res) => {
  var start = new Date().getTime();  
  var iter = req.body.iter;
  var multiplier = 1.0;
  var pos_or_neg = -1.0;
  var denom = 3.0;
  for (var i = 0; i < iter; i++) {
    multiplier += pos_or_neg / denom;
    denom += 2;
    pos_or_neg *= -1;
  }
  multiplier *= 4.0
  var end = (new Date().getTime() - start);
  res.status(200).send(end.toString());
};
