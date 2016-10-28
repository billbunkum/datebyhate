//replace SNAKE CASE w/ CAMEL CASE

function interestPageController(omdbAPI, interestAPIService, filmAPIService, meService) {
    const ctrl = this;
    ctrl.searchHistory = []; //a SESSION array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user
    ctrl.interestsHistory = []; //SESSION list of saved interests
    ctrl.isDuplicate = false; //used to see if film is already in db

    function searchFilms() {
        omdbAPI.get({
            t: ctrl.search_capture
        }).$promise.then( (data) => {
            ctrl.films = data;
            ctrl.searchHistory.push(data);
            // console.log(data);
            });
//        return ctrl.films;
//  ADD ERROR MSG if search returns 'false'
    } // END searchFilms

    function checkForDuplicates(filmRequest) {
        filmAPIService.films.get(filmRequest).$promise.then(
                (data) => {
                    if (data != null) { 
                        ctrl.isDuplicate = true;
                    }
                    return ctrl.isDuplicate;
                }
            );
    } // END checkForDuplicates

    function addInterest(savedInterest) { //ctrl.films -> interestPageCtrl.films
//  FIRST, saves film to db, THEN saves interest to db using film_id
        ctrl.savedInterest = {
            // user: 1, //mock user
            title: savedInterest.Title,
            genre: savedInterest.Genre,
            director: savedInterest.Director,
        };

//  CHECKS FOR DUPLICATES in db
        checkForDuplicates(ctrl.savedInterest);

        if (ctrl.isDuplicate == false) {
            filmAPIService.films.save(ctrl.savedInterest).$promise.then(
                (returnData) => {
                    ctrl.interest = {
                        user: ctrl.user.id,
                        film: returnData.id,
                    };

    //                console.log(returnData);
    //  could REFACTOR into 'addFilm()'' and call 'addInterests()'' within
                    interestAPIService.interests.save(ctrl.interest).$promise.then(
                        (data) => {
                                console.log(data);
                                ctrl.interestsHistory = [
                                    data,
                                    ...ctrl.interestsHistory,
    // '...'' is an ES6 'spread operator'; takes every item in spread array 
    //'...ctrl.interests' and pastes into parent array 'ctrl.interests'
                                ];
                        console.log(ctrl.interestsHistory);
                        alert('Hated!');
                            }
                        );
            });
        } else {
            alert('Already Hated!');
        }
        ctrl.isDuplicate = false;
    } // END addInterest

// on pageLoad gets current user
    function getMe() {
        meService.me().then( (me) => {
            // console.log(me);
            ctrl.user = me;
        })
    }
    getMe();

//  functions
    ctrl.searchFilms = searchFilms;
    ctrl.addInterest = addInterest;
    ctrl.checkForDuplicates = checkForDuplicates;
}; // END interestPageController

export default interestPageController;