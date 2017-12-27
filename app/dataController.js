app.controller("dataCtrl", function ($scope, $http) {
  $scope.top = [];
  $scope.active;
  $scope.request = (search) => $http({
        method: 'POST',
        url: '/data',
        data: {type: search},
        headers: {'Content-Type': 'application/json'}
      }).then(function successCallback(response) {
          $scope.top = response.data;
          $scope.active = search;
          if (search.includes('js'))
            $scope.total = 24099
            if (search.includes('py'))
            $scope.total = 27169
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
        });
})