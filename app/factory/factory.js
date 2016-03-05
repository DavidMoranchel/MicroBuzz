(function (){
	'use strict'

	angular.module('MicroBuzz')
		.factoy('ApiChoferes',ApiChoferes);

	function ApiChoferes($resource){
		return $resource()
	}
})();