const axios = require('axios');

const getCoordinates = (location) => {
    axios
    .get('https://us1.locationiq.com/v1/search.php', {
        params: { 
            key: 'pk.3af299d6e0524830860d19ff1c6cc8bf',
            q: location,
            format: 'json'
        },},
    )
    .then(function (response) {
        let lat = response.data[0]['lat'];
        let lon = response.data[0]['lon'];
        console.log(lat,lon);
    })
    .catch(function (error) {
        console.error(error);
    });
}

getCoordinates('petra')