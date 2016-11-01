import hatePageController from './hate-page.controller';

import template from './hate-page.html';

const hatePageComponent = {
    template: template,
    bindings: {
        hates: '<',
    },
    controller: hatePageController,
    controllerAs: 'hatePageCtrl',
}

export default hatePageComponent;