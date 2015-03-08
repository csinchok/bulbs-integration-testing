angular.module('bulbsApi', ['restmod']).config(function(restmodProvider) {
    restmodProvider.rebase({
        $config: {
        	style: 'AMSApi',
            urlPrefix: 'http://127.0.0.1:8000/cms/api/v1'
        }
    });
});