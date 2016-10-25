

function interestPageController(omdbAPI) {
    const ctrl = this;
    ctrl.search_history = []; //an array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user

    function searchFilms($http) {
//        if (ctrl.search_type == "title") {

//don't understand!!!!
//http://www.omdbapi.com/?"
            ctrl.films = omdbAPI.titles.query({
                t: ctrl.search_capture
            }).$promise.then( (data) => {
                ctrl.films = data.Search;
                console.log(data);
                }
            );

            ctrl.search_history.push(ctrl.films);
            ctrl.films = null;
            console.log(ctrl.search_history);
    }

    ctrl.searchFilms = searchFilms;
};

export default interestPageController;