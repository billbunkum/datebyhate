import comparePageController from './compare-page.controller';
import template from './compare-page.html';

const comparePageComponent = {
    template: template,
    bindings: {
        others: '<',
        buddySocial: '<',
        getBuddySocial: '&',
        update: '&',
    },
    controller: comparePageController,
    controllerAs: 'comparePageCtrl',
}

export default comparePageComponent;