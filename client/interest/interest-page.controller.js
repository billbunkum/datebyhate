

function interestPageController(omdbAPI) {
    const ctrl = this;
    ctrl.searchHistory = []; //an array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user

    function searchFilms() {
            omdbAPI.get({
                t: ctrl.search_capture
            }).$promise.then( (data) => {
                ctrl.films = data;
                ctrl.searchHistory.push(data);
                console.log(data);
                });

//  ADD ERROR MSG if search returns 'false'

    } // END searchFilms

    ctrl.searchFilms = searchFilms;
};

export default interestPageController;