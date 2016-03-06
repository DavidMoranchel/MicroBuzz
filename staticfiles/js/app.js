(function(){
  'use strict';
  angular.module("microbuzz",['ngResource'])
  .factory("apiMapaton",apiMapaton)
  .config(configuration)
  .directive("mapaBuzz",mapaBuzz);

  configuration.$inject = ["$interpolateProvider"];
 function configuration($interpolateProvider){
   $interpolateProvider.startSymbol('{$');
   $interpolateProvider.endSymbol('$}');
 }


  apiMapaton.$inject = ["$resource"];
  function apiMapaton($resource){
    r = $resource('./server/mapaton.json',{},{});
    console.log(r);

  }

  function mapaBuzz(){
    var directive = {
      restrict: 'EA',
          templateUrl: '/templates/ctrl_home.html',
          controller: mapatonController,
          controllerAs: 'mapa',
          replace : true
        };
        return directive;
    }

    function mapatonController(apiMapaton){
      var mapa = this;
      mapa.name = "hola";

    }
})();
