(function () {
  var root = (document.currentScript && document.currentScript.src) ? document.currentScript.src.replace(/assets\/site\.js.*$/, '') : '/';

  // The nav is always open on wide screens, a collapsible menu on narrow ones.
  var wrap = document.querySelector('details.nav-wrap');
  if (wrap) {
    var sync = function () { wrap.open = window.innerWidth > 880; };
    sync();
    window.addEventListener('resize', sync);
  }

  // "On this page" scroll-spy.
  var links = [].slice.call(document.querySelectorAll('.toc-right a'));
  if (links.length && 'IntersectionObserver' in window) {
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = targets.indexOf(e.target);
        if (i > -1 && e.isIntersecting) {
          links.forEach(function (l) { l.classList.remove('active'); });
          links[i].classList.add('active');
        }
      });
    }, { rootMargin: '-10% 0px -70% 0px' });
    targets.forEach(function (t) { if (t) io.observe(t); });
  }

  // Search: a static index built with the pages.
  var input = document.getElementById('q');
  var box = document.getElementById('results');
  if (!input || !box) return;
  var index = null;
  var load = function () {
    if (index) return Promise.resolve(index);
    return fetch(root + 'assets/search-index.json').then(function (r) { return r.json(); }).then(function (j) { index = j; return j; });
  };
  var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var run = function () {
    var terms = input.value.toLowerCase().split(/\s+/).filter(function (t) { return t.length > 1; });
    if (!terms.length) { box.hidden = true; return; }
    load().then(function (pages) {
      var hits = [];
      pages.forEach(function (p) {
        var score = 0, snippet = '';
        terms.forEach(function (t) {
          if (p.title.toLowerCase().indexOf(t) > -1) score += 6;
          if (p.headings.toLowerCase().indexOf(t) > -1) score += 3;
          var low = p.text.toLowerCase(), at = low.indexOf(t);
          if (at > -1) {
            score += Math.min(low.split(t).length - 1, 6);
            if (!snippet) snippet = p.text.slice(Math.max(0, at - 50), at + 90);
          }
        });
        if (score) hits.push({ p: p, score: score, snippet: snippet });
      });
      hits.sort(function (a, b) { return b.score - a.score; });
      box.innerHTML = hits.slice(0, 8).map(function (h) {
        return '<a href="' + root + h.p.url + '">' + esc(h.p.title) + '<small>' + esc(h.snippet) + '</small></a>';
      }).join('') || '<a href="#" tabindex="-1">No results<small>Try different words.</small></a>';
      box.hidden = false;
    });
  };
  input.addEventListener('input', run);
  input.addEventListener('focus', run);
  document.addEventListener('click', function (e) { if (!e.target.closest('.search')) box.hidden = true; });
  input.addEventListener('keydown', function (e) { if (e.key === 'Escape') { box.hidden = true; input.blur(); } });
})();
