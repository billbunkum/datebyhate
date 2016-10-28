function hatePageController(){
    const ctrl = this;

    function viewMyAngst() {
        alert('my angst');
    }

    function viewTheirAngst() {
        alert('their angst');
    }

// functions
    ctrl.viewMyAngst = viewMyAngst;
    ctrl.viewTheirAngst = viewTheirAngst;
};

export default hatePageController;