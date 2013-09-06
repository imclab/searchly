angular.module('searchly', ['infinite-scroll'])
  .config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider) {
    $routeProvider.
      when('/home', {templateUrl: 'static/html/home.html', controller: HomeCtrl}).
      otherwise({redirectTo: '/home'});
  }]);
