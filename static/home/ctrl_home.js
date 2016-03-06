(function(){
  'use strict';

  angular.module('microbuzz')
  .controller('homeCtrl',homeCtrl);

  homeCtrl.$inject = ['mapaton'];
  function homeCtrl(mapaton){
    var home = this;
    home.mapaton = mapaton;
  }
})();
