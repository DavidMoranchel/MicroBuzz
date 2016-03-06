(function(){
  'use strict';
  angular.module("microbuzz",[])
  .controller("microController", microController);

  function microController(){
    var micro = this;
    micro.name = "Nekro Rockwell";
  }
})();
