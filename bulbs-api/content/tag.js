'use strict';

angular.module('bulbsApi').factory('Tag', function(restmod){
	return restmod.model('/tag').mix('TokenAuth', 'DebouncedModel');
});