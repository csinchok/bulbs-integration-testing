'use strict';

describe('Bulbs Content API', function () {

	var Content, tester, $http;

  beforeEach(function() {
    tester = ngMidwayTester('bulbsApi');
    Content = tester.inject('Content');
    $http = tester.inject('$http');
  });

  afterEach(function() {
    tester.destroy();
    tester = null;
  });

  it('should be able to get a single piece of content', function (done) {
    var article = Content.$find(1);

    article.$then(function(){
      expect(article.id).toBe(1);
      expect(article.title).toBe('Blog: 0');

      expect(article.authors[0].getFullName()).toBe('Milque Toast');

      done();  // Need to call done, so that 
    });
  });

});