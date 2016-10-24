
function omdbAPI($resource) {
    const omdb = {
        titles: $resource("http://www.omdbapi.com/?s=space"),
    };

    return omdb;
}

export default omdbAPI;
