function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}


function onClickedEstimatePrice() {
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice").value;


    // console.log(params);
    if (location == "") {
        alert("Location not set!!!");
    }
    else {
        var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
        //   var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

        var params = {
            total_sqft: parseFloat(sqft),
            location: location,
            bhk: bhk,
            bath: bathrooms,
        };

        // console.log(typeof(JSON.parse(params)));/

        // var xhr = new XMLHttpRequest();
        // xhr.open("POST", url, true);
        // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        // xhr.onreadystatechange = function () { // Call a function when the state changes.
        //     if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        //         console.log("done here 2");
        //         // Request finished. Do processing here.
        //     }
        // }
        // console.log("not done here");
        // xhr.send(params);

        // console.log(params);
        fetch(url, {
            method: 'POST',
            body: JSON.stringify(params),
            headers: {
                "Content-type": "application/json"
            }
        })
            .then(response => response.text())
            .then((text) => {
                let val = JSON.parse(text);
                let price = document.getElementById('uiEstimatedPrice');
                price.style['background'] = 'rgba(9, 139, 226, 0.864)';
                price.innerHTML = `₹ ${val['estimated_price']} Lakhs`;
                price.style['border-top']= '2px solid rgb(97, 97, 97)';
                price.style['border-left']= '2px solid rgb(97, 97, 97)';
                price.style['border-bottom']= '2px solid rgb(29, 29, 29)';
                price.style['border-right']= '2px solid rgb(29, 29, 29)';
            });
    }
};



function onPageLoad() {
    // console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards


    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false); // false for synchronous request
    xmlHttp.send(null);
    let data = JSON.parse(xmlHttp.responseText);
    // console.log(data.locations);

    var uiLocations = document.getElementById("uiLocations");
    // uiLocations.innerHTML="";
    for (var i in data.locations) {
        var opt = new Option(data.locations[i]);
        uiLocations.append(opt);
    }

}

window.onload = onPageLoad;