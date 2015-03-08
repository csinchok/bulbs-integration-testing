'use strict';

describe('Authors', function () {

	var Author, tester;

  beforeEach(function() {
    tester = ngMidwayTester('bulbsApi');
    Author = tester.inject('Author');
  });

  afterEach(function() {
    tester.destroy();
    tester = null;
  });

  it('should be able to get a single author', function (done) {
    var author = Author.$find(2);

    author.$then(function(){
      expect(author.id).toBe(2);
      expect(author.getFullName()).toBe('Milque Toast');
      done();
    });
  });

});