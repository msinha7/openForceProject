var result = 0;
var actualLength = 0;
var url = 'http://ron-swanson-quotes.herokuapp.com/v2/quotes';

async function showRandomSizeQuotes(size) {
    result = 0;
    actualLength = 0;
    var minLength;
    var maxLength;

    if (size === 'small') {
        minLength = 1;
        maxLength = 4;

    }
    else if (size === 'medium') {
        minLength = 5;
        maxLength = 12;
    }
    else if (size === 'large') {
        minLength = 13;
        maxLength = Infinity;
    }
    else {
        minLength = 1;
        maxLength = Infinity;
    }
    console.log("Min : " + minLength);
    console.log("Max :" + maxLength);


    var trying = 0;
    while ((actualLength <= minLength || actualLength > maxLength) && trying < 250) {
        const response = await fetch(url, {});
        const json = await response.json();
        result = json[0];
        actualLength = result.split(" ").length;

        trying++;
    }

    console.log("Outside Result :: " + result);
    return result;
}