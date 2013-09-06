function HomeCtrl($scope, $routeParams) {
}

function SearchCtrl($scope, $http) {
  $scope.users = [];
  $scope.currentQuery = '';
  $scope.nameIndex = -1;
  $scope.busy = false;

  //Name splitting function
  $scope.nameSplit = function(input) {
    return input.name.split(' ')[$scope.nameIndex]
  }

  //set first name sort mode
  $scope.firstNameSort = function () {
    $scope.nameIndex = 0;
  }

  //set last name sort mode
  $scope.lastNameSort = function () {
    $scope.nameIndex = 1;
  }

  //reset sort
  $scope.resetSort = function () {
    $scope.nameIndex = -1;
  }

  //name search request
  $scope.searchName = function () {
    //reset users and search name
    $scope.users = [];
    $scope.currentQuery = '';
    $scope.nameIndex = -1;
    var params = {
      'name': $scope.nameQuery
    }
    //set busy status
    $scope.busy = true;
    $http({
      url: '/api/v1/users',
      method: 'GET',
      params: params
    }).
      success(function (data, status, headers, config) {
        $scope.users = $scope.users.concat(data);
        $scope.busy = false;
        $scope.currentQuery = params.name;
      }).
      error(function (data, status, headers, config) {
        $scope.busy = false;
        $scope.currentQuery = '';
      });
  }
}
