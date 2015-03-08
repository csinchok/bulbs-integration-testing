'use strict';

describe('Content', function () {

	var Content, tester, $http;

  beforeEach(function() {
    tester = ngMidwayTester('bulbsApi');
    Content = tester.inject('Content');
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

      // Kinda a shitty way to test for published
      expect(article.published).toBeLessThan(new Date());

      done();
    });
  }, 2000);

  it('should be able to save new content', function (done) {
    var article = Content.$build({
      title: 'Just some draft content',
      doctype: 'core_article'
    });

    article.$save();

    article.$then(function() {

      expect(article.title).toBe('Just some draft content');

      article.$refresh();  // Let's make sure we can refresh

      article.$then(function() {
        expect(article.title).toBe('Just some draft content');
        done();
      });      
    });
  }, 2000);

  it('should be able to trash content', function (done) {
    var article = Content.$find(666);

    article.trash();

    article.$then(function () {
      done();
    }, function(e) {
      // We should never get here...
      expect(true).toBe(false);
      done();
    });

  }, 2000);

});