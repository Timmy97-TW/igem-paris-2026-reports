/* language switch (中 / EN). The choice lives in localStorage on this device only;
   with nothing stored, each page shows the language it was written in. */
(function () {
  var root = document.documentElement, KEY = 'paris2026.lang', btn = document.getElementById('lang');
  var orig = root.getAttribute('data-orig') || 'en';
  var titles = { }, alt = document.querySelector('meta[name="title-alt"]');
  titles[orig] = document.title; titles[orig === 'zh' ? 'en' : 'zh'] = alt ? alt.content : document.title;
  window.siteLang = function () { return root.getAttribute('data-lang') || orig; };
  var hidden = function (b) {
    var L = root.getAttribute('data-lang');
    return L ? b.getAttribute('data-l') !== L : b.hasAttribute('data-tr');
  };
  /* twin blocks repeat ids: only the showing copy keeps them, so anchors land */
  var fixIds = function () {
    [].slice.call(document.querySelectorAll('[data-l]')).forEach(function (b) {
      var off = hidden(b);
      [b].concat([].slice.call(b.querySelectorAll('[id],[data-id]'))).forEach(function (el) {
        if (off && el.id) { el.dataset.id = el.id; el.removeAttribute('id'); }
        else if (!off && el.dataset.id && !el.id) { el.id = el.dataset.id; }
      });
    });
  };
  var paint = function () {
    var L = window.siteLang();
    root.lang = L === 'zh' ? 'zh-Hant' : 'en';
    document.title = titles[L];
    if (btn) [].slice.call(btn.querySelectorAll('[data-k]')).forEach(function (s) {
      s.classList.toggle('on', s.dataset.k === L);
    });
    fixIds();
  };
  var set = function (L) {
    root.setAttribute('data-lang', L);
    try { localStorage.setItem(KEY, L); } catch (e) {}
    paint();
    document.dispatchEvent(new CustomEvent('langchange', { detail: { lang: L } }));
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
  };
  if (btn) btn.addEventListener('click', function () { set(window.siteLang() === 'zh' ? 'en' : 'zh'); });
  paint();
  if (location.hash) { var t0 = document.getElementById(location.hash.slice(1)); if (t0) t0.scrollIntoView(); }
})();

/* nav: mobile menu + scroll progress */
(function () {
  var menu = document.getElementById('menu'), links = document.getElementById('nlinks');
  if (menu && links) menu.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    menu.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  var prog = document.getElementById('nprog');
  if (prog) {
    var tick = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, window.scrollY / h) : 0) + ')';
    };
    addEventListener('scroll', tick, { passive: true }); tick();
  }
})();

/* doc pages: wrap tables for horizontal scroll, build the table of contents */
(function () {
  var prose = document.getElementById('prose'), toc = document.getElementById('toc');
  if (!prose) return;

  prose.querySelectorAll('table').forEach(function (t) {
    if (t.parentElement.classList.contains('tbl')) return;
    var d = document.createElement('div'); d.className = 'tbl';
    t.parentNode.insertBefore(d, t); d.appendChild(t);
  });

  if (!toc) return;
  var slug = function (s) {
    return s.toLowerCase().replace(/[^\w一-鿿]+/g, '-').replace(/^-+|-+$/g, '') || 'section';
  };
  var seen = {}, made = [];
  [].slice.call(prose.querySelectorAll('h2, h3')).forEach(function (h) {
    if (!h.id && !h.dataset.id) { var b = slug(h.textContent); seen[b] = (seen[b] || 0) + 1; h.id = seen[b] > 1 ? b + '-' + seen[b] : b; }
  });
  /* rebuilt on every language switch: only headings that are showing */
  var build = function () {
    [].slice.call(toc.querySelectorAll('a')).forEach(function (a) { a.remove(); });
    made = [];
    [].slice.call(prose.querySelectorAll('h2, h3')).forEach(function (h) {
      if (!h.id || !h.offsetParent) return;
      var a = document.createElement('a');
      a.href = '#' + h.id; a.textContent = h.textContent;
      if (h.tagName === 'H3') a.className = 'lv3';
      toc.appendChild(a); made.push({ a: a, h: h });
    });
    toc.style.display = made.length ? '' : 'none';
    sync();
  };
  var sync = function () {
    if (!made.length) return;
    var y = window.scrollY + 110, cur = made[0];
    made.forEach(function (m) { if (m.h.offsetTop <= y) cur = m; });
    made.forEach(function (m) { m.a.classList.toggle('on', m === cur); });
  };
  addEventListener('scroll', sync, { passive: true });
  document.addEventListener('langchange', build);
  build();
})();

/* shared: filterable list helper */
window.filterList = function (opts) {
  var input = document.getElementById(opts.input),
      count = document.getElementById(opts.count),
      rows = [].slice.call(document.querySelectorAll(opts.rows)),
      empty = document.getElementById(opts.empty),
      seg = opts.seg ? document.getElementById(opts.seg) : null,
      filter = 'all';

  var apply = function () {
    var q = (input && input.value || '').trim().toLowerCase(), n = 0;
    rows.forEach(function (r) {
      var okF = filter === 'all' || (r.dataset.group || '').split('|').indexOf(filter) > -1;
      var okQ = !q || (r.dataset.search || r.textContent).toLowerCase().indexOf(q) > -1;
      var okX = !opts.extra || opts.extra(r);
      var show = okF && okQ && okX;
      r.hidden = !show; if (show) n++;
    });
    if (count) count.textContent = n + ' ' + (n === 1 ? opts.noun : opts.nounPlural || opts.noun + 's');
    if (empty) empty.hidden = n > 0;
    if (opts.onApply) opts.onApply();
  };

  if (input) input.addEventListener('input', apply);
  if (seg) seg.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    seg.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); });
    filter = b.dataset.f; apply();
  });
  apply();
  return apply;
};

/* shared: tick rows off, remembered on this device only.
   localStorage can throw or come back empty (private window, cleared site data),
   so every read and write is guarded and the page renders fine without it. */
window.tickList = function (opts) {
  var list = typeof opts.list === 'string' ? document.getElementById(opts.list) : opts.list;
  if (!list) return;
  var KEY = opts.key, done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { done = {}; }

  var save = function () { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} };
  var rows = [].slice.call(list.querySelectorAll(opts.rows));
  var progress = function () {
    var tickable = rows.filter(function (r) { return r.querySelector('input[type=checkbox]'); });
    var n = tickable.filter(function (r) { return done[r.dataset.id]; }).length,
        bar = document.getElementById(opts.bar || 'seen-bar'),
        lab = document.getElementById(opts.lab || 'seen-lab');
    if (bar) bar.style.width = (tickable.length ? (n / tickable.length * 100) : 0) + '%';
    if (lab) lab.textContent = n + ' of ' + tickable.length + ' ' + (opts.verb || 'done');
  };

  rows.forEach(function (r) {
    var cb = r.querySelector('input[type=checkbox]');
    if (!cb) return;
    if (done[r.dataset.id]) { cb.checked = true; r.classList.add('done'); }
    cb.addEventListener('change', function () {
      if (cb.checked) { done[r.dataset.id] = 1; } else { delete done[r.dataset.id]; }
      r.classList.toggle('done', cb.checked); save(); progress();
    });
  });
  progress();
};

/* floor plan */
(function () {
  var list = document.getElementById('targets');
  if (list) window.tickList({ list: list, rows: '.row', key: 'paris2026.visited',
                              verb: 'visited' });
})();
