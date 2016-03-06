(function(){
  'use strict';

  angular.module("microbuzz")
  .config(configuration);

  mapatonData.$inject = ["apiMapaton"];
  function mapatonData(apiMapaton){

  }

  configuration.$inject = ["$routeProvider"];
  function configuration($routeProvider){
    $routeProvider
    .when('/',
    {
      templateUrl: '/home/home.html',
      controller: 'homeCtrl',
      controllerAs:'home',
      resolve: {
        mapaton: mapatonData,
      }
    })
    .otherwise({
      redirectTo : '/'
    });
    }
})();
