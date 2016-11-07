import angular from 'angular';

import appComponent from './app.component';
import interestModule from '../interest/interest.module';
import meService from '../me/me.service';
import angularFilter from 'angular-filter';

import FlashesModule from '../flashes/flashes.module';

const AppModule = angular.module('root', [
    interestModule.name,
    FlashesModule.name,
    angularFilter,
])
    .config(function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .factory('meService', meService)
    .component('app', appComponent);

export default AppModule;