import comparePageController from './compare-page.controller';
import template from './compare-page.html';

const comparePageComponent = {
    template: template,
    bindings: {
        others: '<', // for for hate buddies
        buddySocial: '<', //value for a specific hate buddy's angst
        getBuddySocial: '&', //displays a specific hate buddy's angst
    },
    controller: comparePageController,
    controllerAs: 'comparePageCtrl',
}

export default comparePageComponent;