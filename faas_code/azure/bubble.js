// TODO(ac): translate to azure function equivalent

module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.name || (req.body && req.body.array)) {
        var start = new Date().getTime();

        // array to sort
        var array = req.body.array;

        // swap function helper
        function swap(array, i, j) {
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }


        // be careful: this is a very basic implementation which is nice to understand the deep principle of bubble sort (going through all comparisons) but it can be greatly improved for performances
        function bubbleSortBasic(array) {
            for(var i = 0; i < array.length; i++) {
                for(var j = 1; j < array.length; j++) {
                    if(array[j - 1] > array[j]) {
                        swap(array, j - 1, j);
                    }
                }
            }
            // return array;
        }

        bubbleSortBasic(array);
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