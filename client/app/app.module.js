import angular from 'angular';

import appComponent from './app.component';
import interestModule from '../interest/interest.module';


const AppModule = angular.module('root', [
    interestModule.name,
])
    .component('app', appComponent);

export default AppModule;
