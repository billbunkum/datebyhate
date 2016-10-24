

function interestPageController(omdbAPI) {
    const ctrl = this;
    ctrl.films = null;

    function searchFilms() {
        omdbAPI.titles.get().$promise.then( 
            (data) => {
                ctrl.films = data.Search; 
                // console.log(data);
            });
    }

    ctrl.searchFilms = searchFilms;
};

export default interestPageController;