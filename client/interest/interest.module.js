import angular from 'angular';
import 'angular-resource';

import interestAPIService from './interestAPIService';

const interestModule = angular.module('interestMod', [
        'ngResource'
        ]
    )
    .config( 
        ($resourceProvider) => {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        }
    )
    .factory('interestAPIService', interestAPIService);
//  does it matter if '.factory' is concatinated before '.config'??

//  still need to register COMPONENTS

export default interestModule;