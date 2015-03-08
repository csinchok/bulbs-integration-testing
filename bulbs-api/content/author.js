'use strict';

angular.module('bulbsApi').factory('Author', function(restmod){
	return restmod.model('/author').mix('TokenAuth', 'DebouncedModel', {
		$extend: {
			getFullName: function() {
				return this.first_name + ' ' + this.last_name;
			}
		}
	});
});