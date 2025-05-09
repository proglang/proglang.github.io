// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item "><a href="home.html">Home</a></li><li class="chapter-item "><a href="team.html">Team</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="team/thiemann.html">Prof. Dr. Peter Thiemann</a></li><li class="chapter-item "><a href="team/jost.html">Marlis Jost</a></li><li class="chapter-item "><a href="team/van-den-heuvel.html">Dr. Bas van den Heuvel</a></li><li class="chapter-item "><a href="team/saffrich.html">Hannes Saffrich</a></li><li class="chapter-item "><a href="team/weidner.html">Marius Weidner</a></li><li class="chapter-item "><a href="team/spaderna.html">Janek Spaderna</a></li><li class="chapter-item "><a href="team/mieschendahl.html">Leonardo Mieschendahl</a></li></ol></li><li class="chapter-item "><a href="teaching.html">Teaching</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="teaching/25ss.html">Summer 2025</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="teaching/25ss/cc.html">Compiler Construction</a></li><li class="chapter-item "><a href="teaching/25ss/eopl.html">Essentials of Programming Languages</a></li><li class="chapter-item "><a href="teaching/25ss/popl.html">Principles of Programming Languages (Seminar)</a></li></ol></li><li class="chapter-item "><a href="teaching/24ws.html">Winter 2024</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="teaching/24ws/eidp.html">Einführung in die Programmierung</a></li><li class="chapter-item "><a href="teaching/24ws/fp.html">Functional Programming</a></li></ol></li><li class="chapter-item "><a href="teaching/24ss.html">Summer 2024</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="teaching/24ss/compiler-construction.html">Compiler Construction</a></li><li class="chapter-item "><a href="teaching/24ss/concurrency.html">Concurrency</a></li><li class="chapter-item "><a href="teaching/24ss/ocaml.html">Real World OCaml (Seminar)</a></li></ol></li></ol></li><li class="chapter-item "><a href="about.html">About</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0].split("?")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
