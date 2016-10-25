
function omdbAPI($resource) {
    const omdb = {
        titles: $resource("http://www.omdbapi.com/?"),
    };

    return omdb;
}

export default omdbAPI;
