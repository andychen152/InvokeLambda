exports.handler = (event, context, callback) => {
  var start = new Date().getTime();  
  var iter = event.iter;
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
  callback(null, end.toString());
}