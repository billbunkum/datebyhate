//replace SNAKE CASE w/ CAMEL CASE

function interestPageController(omdbAPI, interestAPIService, filmAPIService, meService, $interval) {
    const ctrl = this;
    ctrl.searchHistory = []; //a SESSION array of all data returned from omdbapi
    ctrl.films = null; //objects of data returned from omdbapi
    ctrl.search_type = "title"; // specifies the 't' param for omdbapi
    ctrl.title = null; // string 't='
    ctrl.search_capture = null; //what is typed by user
    ctrl.interestsHistory = []; //SESSION list of saved interests
    ctrl.isDuplicate = false; //used to see if film is already in db
    ctrl.allMyHates = []; //all a user's 'hates'; used within getMyAngst
    ctrl.allHate = []; // all every hates; used within getAllHate

    function searchFilms() {
        omdbAPI.get({
            t: ctrl.search_capture
        }).$promise.then( (data) => {
            ctrl.films = data;
            ctrl.searchHistory.push(data);
            // console.log(data);
            });
//  ADD ERROR MSG if search returns 'false'
    } // END searchFilms

    function checkForDuplicates(filmRequest) {
        filmAPIService.films.get(filmRequest).$promise.then(
                (data) => {
                    if (data.user != null) { 
                        ctrl.isDuplicate = true;
                    }
                    return ctrl.isDuplicate;
                }
            );
    } // END checkForDuplicates

    function addInterest(savedInterest) { 
//ACTIVATES w/ HATE IT button; savedInterest -> ctrl.films -> interestPageCtrl.films
//  FIRST, saves film to db, THEN saves interest to db using film_id
        ctrl.savedInterest = {
            title: savedInterest.Title,
            genre: savedInterest.Genre,
            director: savedInterest.Director,
            imdbID: savedInterest.imdbID,
            plot: savedInterest.Plot,
        };
        // console.log(ctrl.savedInterest);
//  CHECKS FOR DUPLICATES in db
        // checkForDuplicates(ctrl.savedInterest);

            filmAPIService.films.save(ctrl.savedInterest).$promise.then(
                (returnData) => {
                    ctrl.interest = {
                        user: ctrl.user.id,
                        film: returnData.id,
                        imdbID: returnData.imdbID,
                    };
                   // console.log(returnData);

    //  could REFACTOR into 'addFilm()'' and call 'addInterests()'' within
                    interestAPIService.interests.save(ctrl.interest).$promise.then(
                        (data) => {
                                // console.log(data);
                                ctrl.interestsHistory = [
                                    data,
                                    ...ctrl.interestsHistory,
    // '...'' is an ES6 'spread operator'; takes every item in spread array 
    //'...ctrl.interests' and pastes into parent array 'ctrl.interests'
                                ];
                        // console.log(ctrl.interestsHistory);
                        alert('Hated!');
                        }
                    );
            });
    } // END addInterest

// gathers ALL interests
    function getAllHate() {
        interestAPIService.interests.get().$promise.then(
            (data) => {
                ctrl.hateBall = data;
                for (let x = 0; x < ctrl.hateBall.results.length; x++) {
                    ctrl.allHate.push(ctrl.hateBall.results[x]);
                }
            // console.log(ctrl.allHate);
                getMyAngst();
            }
        );
    } // END getAllHate

//  filters 'ctrl.allHate' into 'ctrl.allMyHates'
    function getMyAngst() {
        for (let x = 0; x < ctrl.allHate.length; x++) {
            if (ctrl.allHate[x].user === ctrl.user.id) {
                ctrl.allMyHates.push(ctrl.allHate[x]);
            }
        }
        compareAngst();
        // console.log(ctrl.allMyHates);
    } // END getMyAngst

//  compares 'ctrl.allMyHates' imdbID s w/ other imdbID s w/in 'ctrl.allHate'
//  stores results in 'ctrl.othersWithMe' as a 'hateBuddy' object
    function compareAngst() {
        ctrl.othersWithMe = [];
        let match = {};

        for (let x = 0; x < ctrl.allMyHates.length; x++) {
            for (let i = 0; i < ctrl.allHate.length; i++) {
                if (ctrl.allHate[i].imdbID === ctrl.allMyHates[x].imdbID) {
                    match = { 
                        hateBuddy : [ 
                            ctrl.allHate[x].user, 
                            ctrl.allHate[x].imdbID, 
                            ctrl.allHate[x].film 
                        ] 
                    };
                    ctrl.othersWithMe.push(match);
                }
                match = {};
            }
        }
        if (ctrl.othersWithMe == undefined) {
            alert('No hate matches\; keep hating to date!');
        }

        clearData();
        console.log(ctrl.othersWithMe);
    } // END compareAngst

    function clearData () {
        ctrl.allHate = [];
        ctrl.allMyHates = [];
    }

    function persistOthersWithMe() {

    } // END persistOthersWithMe

// gets current user at /me
    function getMe() {
        meService.me().then( (me) => {
            // console.log(me);
            ctrl.user = me;
        })
    }

// PAGE LOAD functions
    getMe();
    getAllHate();//calls getMyAngst() w/in 'then clause'
    $interval(getAllHate, 5000);

//  functions
    ctrl.searchFilms = searchFilms;
    ctrl.addInterest = addInterest;
    ctrl.checkForDuplicates = checkForDuplicates;
    ctrl.getAllHate = getAllHate; //gathers all 'interests/hates' into 'ctrl.hateBall'
    ctrl.getMyAngst = getMyAngst; //pulls 'my angst' from 'ctrl.hateBall'
    ctrl.compareAngst = compareAngst; // uses 'ctrl.allMyHates' & 'ctrl.allHate' to populate 'ctrl.othersWithMe'
    ctrl.clearData = clearData; // stopping aggregate 'push'to interval functions
    ctrl.persistOthersWithMe = persistOthersWithMe; // persists data comparison got from 'compareAngst'
}; // END interestPageController

export default interestPageController;