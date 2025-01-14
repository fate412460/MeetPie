$(document).ready(function() {

    $('#searchButton').click(function(e){
        console.log('Clicked Search !');
        e.preventDefault();
        startSearch();
    });

});


function startSearch() {

    var queryData;

    var locationArray = [];

    var typeArray = [];

    jsonData = {
        url: 'http://localhost:8080/',
        type: 'POST',
        dataType: 'json',
        data: {
            keyword: $('#keywordInput').val(),
            host: "",
            location: locationArray,
            type: typeArray,
            date: {
                start: "",
                end: ""
            },
            fee: {
                lower: "",
                upper: ""
            },
            number_of_people: {
                lower: "",
                upper: ""
            }
        }
    };

    $.ajax(jsonData)
        .done(function(data) {
            console.log("Success Get Data Back !");
            console.log(data);
            clean();
            for (var i = 0; i < data.length; i++) {
                showObject(data[i]);
            }
            // Scroll to Bottom
            $('html, body').animate({
                scrollTop: $("section.result").offset().top
            }, 1500);
        })
        .fail(function(data) {
            console.log("Ajax Error !");
        })
        .always(function(data) {
            console.log("No Matter What, Ends !");
        });

}

function clean() {
    $('div.resultDiv').remove();
}

var resultBlock = '';

function showObject(inputData) {
    console.log('Add 1 Result Div !');

    resultBlock =
    '<div class="resultDiv">' +
        '<a href="' + inputData.url + '" class="imgLink" target="_blank" style="background-image: url(' + inputData.image_url + ')">' +
        '</a>' +
        '<a href="' + inputData.url + '" class="titleLink" target="_blank">' +
            '<h2>' + inputData.title + '</h2>' +
        '</a>' +
        '<p>' + inputData.description + '</p>' +
    '</div>' ;

    $('p#foo').after(resultBlock);
}
