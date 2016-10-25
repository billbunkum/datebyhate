//replace SNAKE CASE w/ CAMEL CASE

function interestPageController(omdbAPI, interestAPIService) {
    const ctrl = this;
    ctrl.searchHistory = []; //an array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user

    ctrl.interests = []; //list of saved interests

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

    function addInterest(savedInterest) {
        ctrl.savedInterest = {
            "film": 1,
            "user": 1,
        };
//  THIS ISN'T PERSISTING DATA FROM OMDBAPI
//  I THINK THERE IS A FOUL-UP W/MY MODELS - THE LOGIC BETWEEN THEM
//  AND HOW I'M THINKING THE DJANGOREST & ANGULAR WORK TOGETHER

        interestAPIService.interests.save(ctrl.savedInterest)
            .$promise.then( (data) => {
                ctrl.interests = [
                    data,
                    ...ctrl.interests,
                ];
            });
// '...'' is an ES6 'spread operator'; takes every item in spread array 
//'...ctrl.interests' and pastes into parent array 'ctrl.interests'
    } // END addInterest

//  functions
    ctrl.searchFilms = searchFilms;
    ctrl.addInterest = addInterest;
};

export default interestPageController;