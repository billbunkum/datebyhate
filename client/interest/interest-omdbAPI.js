
function omdbAPI($resource) {
    // const omdb = {
    //     titles: $resource("http://www.omdbapi.com/?"),
    // };

    // return omdb;
    return $resource("http://www.omdbapi.com/?");

}

export default omdbAPI;