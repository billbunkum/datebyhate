import comparePageController from './compare-page.controller';
import template from './compare-page.html';

const comparePageComponent = {
    template: template,
    bindings: {
        others: '<', // scalar for getBuddySocial
        getBuddySocial: '&', //displays a specific hate buddy's social link (email)
        othersAngst: '<', // scalar for getBuddyAngst
        getBuddyAngst: '&', //displays a specific hate buddy's angst
        hateBuddySocial: '<', //used to display social in a modal
    },
    controller: comparePageController,
    controllerAs: 'comparePageCtrl',
}

export default comparePageComponent;