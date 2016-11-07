import angular from 'angular';
import 'angular-resource';

import interestAPIService from './interest-api.service';
import filmAPIService from '../film/film-api.service';
import omdbAPI from './interest-omdbAPI';
import hateBuddiesAngstService from './hate-buddies-angst.service';

import interestPageComponent from './interest-page.component';
import hatePageComponent from './hate-page.component';
import comparePageComponent from './compare-page.component';

const interestModule = angular.module('interestMod', [
        'ngResource'
        ]
    )
    .config( 
        ($resourceProvider) => {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        }
    )
    .factory('interestAPIService', interestAPIService)
    .factory('omdbAPI', omdbAPI)
    .factory('filmAPIService', filmAPIService)
    .factory('hateBuddiesAngstService', hateBuddiesAngstService)
    .component('interestPage', interestPageComponent)
    .component('hatePage', hatePageComponent)
    .component('comparePage', comparePageComponent);
//  still need to register COMPONENTS

export default interestModule;