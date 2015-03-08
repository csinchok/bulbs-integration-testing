'use strict';

angular.module('bulbsApi').factory('Content', function(restmod){
	return restmod.model('/content').mix('TokenAuth', 'DebouncedModel', {
		tags: {belongsToMany: 'Tag'},
		authors: {belongsToMany: 'Author'}
	});
});