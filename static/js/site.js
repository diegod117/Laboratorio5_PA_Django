// Entradas por scroll y vista previa de integrantes.
(function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // CV pages: stagger the parts of the sheet without touching each template.
    var auto = document.querySelectorAll('.cv-header > *, .cv-section, .cv-section .exp, .cv .back');
    auto.forEach(function (el, n) {
        if (!el.hasAttribute('data-reveal')) {
            el.setAttribute('data-reveal', '');
            el.style.setProperty('--d', String(n % 3));
        }
    });

    var items = document.querySelectorAll('[data-reveal]');
    if (reduce || !('IntersectionObserver' in window)) {
        items.forEach(function (el) { el.classList.add('is-in'); });
    } else {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) {
                    e.target.classList.add('is-in');
                    io.unobserve(e.target);
                }
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
        items.forEach(function (el) { io.observe(el); });
    }

    // Home: pointing at (or opening) a member shows their picture in the fixed frame.
    var bars = document.querySelectorAll('.barra[data-preview]');
    var imgs = document.querySelectorAll('.vista-img');
    function show(n) {
        imgs.forEach(function (img, k) { img.classList.toggle('on', k === Number(n)); });
    }
    bars.forEach(function (bar) {
        var n = bar.getAttribute('data-preview');
        bar.addEventListener('mouseenter', function () { show(n); });
        bar.addEventListener('focusin', function () { show(n); });
        bar.addEventListener('toggle', function () {
            if (bar.open) {
                bars.forEach(function (other) { if (other !== bar) other.open = false; });
                show(n);
            }
        });
    });
})();
