
function omdbAPI($resource) {
    // const omdb = {
    //     titles: $resource("http://www.omdbapi.com/?"),
    // };

    // return omdb;
    // return $resource("https://www.omdbapi.com/?");
    return $resource("http://www.omdbapi.com/?i=tt3896198&apikey=8500307e/?");

}

export default omdbAPI;
