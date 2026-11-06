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
  var heads = [].slice.call(prose.querySelectorAll('h2, h3')), seen = {}, made = [];
  heads.forEach(function (h) {
    if (!h.id) { var b = slug(h.textContent); seen[b] = (seen[b] || 0) + 1; h.id = seen[b] > 1 ? b + '-' + seen[b] : b; }
    var a = document.createElement('a');
    a.href = '#' + h.id; a.textContent = h.textContent;
    if (h.tagName === 'H3') a.className = 'lv3';
    toc.appendChild(a); made.push({ a: a, h: h });
  });
  if (!made.length) { toc.style.display = 'none'; return; }

  var sync = function () {
    var y = window.scrollY + 110, cur = made[0];
    made.forEach(function (m) { if (m.h.offsetTop <= y) cur = m; });
    made.forEach(function (m) { m.a.classList.toggle('on', m === cur); });
  };
  addEventListener('scroll', sync, { passive: true }); sync();
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
      var show = okF && okQ;
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

/* floor plan: remember ticked teams on this device */
(function () {
  var list = document.getElementById('targets'); if (!list) return;
  var KEY = 'paris2026.visited';
  var done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { done = {}; }

  var save = function () { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} };
  var progress = function () {
    var rows = [].slice.call(list.querySelectorAll('.row')),
        n = rows.filter(function (r) { return done[r.dataset.id]; }).length,
        bar = document.getElementById('seen-bar'), lab = document.getElementById('seen-lab');
    if (bar) bar.style.width = (rows.length ? (n / rows.length * 100) : 0) + '%';
    if (lab) lab.textContent = n + ' of ' + rows.length + ' visited';
  };

  list.querySelectorAll('.row').forEach(function (r) {
    var cb = r.querySelector('input[type=checkbox]');
    if (done[r.dataset.id]) { cb.checked = true; r.classList.add('done'); }
    cb.addEventListener('change', function () {
      if (cb.checked) { done[r.dataset.id] = 1; } else { delete done[r.dataset.id]; }
      r.classList.toggle('done', cb.checked); save(); progress();
    });
  });
  progress();
})();
