//replace SNAKE CASE w/ CAMEL CASE

function interestPageController(omdbAPI, interestAPIService, filmAPIService) {
    const ctrl = this;
    ctrl.searchHistory = []; //a SESSION array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user
    ctrl.interestsHistory = []; //SESSION list of saved interests

    function searchFilms() {
        omdbAPI.get({
            t: ctrl.search_capture
        }).$promise.then( (data) => {
            ctrl.films = data;
            ctrl.searchHistory.push(data);
//            console.log(data);
            });
        return ctrl.films;
//  ADD ERROR MSG if search returns 'false'
    } // END searchFilms

    function addInterest(savedInterest) { //ctrl.films -> interestPageCtrl.films
//  FIRST, saves film to db, THEN saves interest to db using film_id
        ctrl.savedInterest = {
            user: 1, //mock user
            title: savedInterest.Title,
            genre: savedInterest.Genre,
            director: savedInterest.Director,
        };

//  HOW TO CHECK FOR DUPLICATES in db?
        filmAPIService.films.save(ctrl.savedInterest).$promise.then(
            () => {alert('film saved');
        });

        // interestAPIService.interests.save(ctrl.savedInterest)
        //     .$promise.then( (data) => {
        //         ctrl.interestsHistory = [
        //             data,
        //             ...ctrl.interestsHistory,
        //         ];
        //     });
// '...'' is an ES6 'spread operator'; takes every item in spread array 
//'...ctrl.interests' and pastes into parent array 'ctrl.interests'
    } // END addInterest

//  functions
    ctrl.searchFilms = searchFilms;
    ctrl.addInterest = addInterest;
};

export default interestPageController;