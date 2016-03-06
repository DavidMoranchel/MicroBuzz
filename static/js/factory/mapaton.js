(function(){
  'use strict';
  angular.module("microbuzz")
  .factory('apiMapaton',apiMapaton);

  apiMapaton.$inject = ["$resource"];
  function apiMapaton($resource){
    return $resource("../server/mapaton.json",{},{});
  }


})();
