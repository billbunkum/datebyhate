import hatePageController from './hate-page.controller';

import template from './hate-page.html';

const hatePageComponent = {
    template: template,
    bindings: {
        hate: '<',
        myangst: '&', //don't know if this needs camelCase or kabob-case
    },
    controller: hatePageController,
    controllerAs: 'hatePageCtrl',
}

export default hatePageComponent;