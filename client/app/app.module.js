import angular from 'angular';

import appComponent from './app.component';

const AppModule = angular.module('root', [
])
    .component('app', appComponent);

export default AppModule;
