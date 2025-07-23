'use strict';

/* global default_theme, default_dark_theme, default_light_theme, hljs, ClipboardJS */

// Fix back button cache problem
window.onunload = function() { };

(function sidebar() {
    const sidebar = document.getElementById('sidebar');
    const sidebarLinks = document.querySelectorAll('#sidebar a');
    const sidebarToggleButton = document.getElementById('sidebar-toggle');
    const sidebarResizeHandle = document.getElementById('sidebar-resize-handle');
    const sidebarCheckbox = document.getElementById('sidebar-toggle-anchor');
    let firstContact = null;


    /* Because we cannot change the `display` using only CSS after/before the transition, we
       need JS to do it. We change the display to prevent the browsers search to find text inside
       the collapsed sidebar. */
    if (!document.documentElement.classList.contains('sidebar-visible')) {
        sidebar.style.display = 'none';
    }
    sidebar.addEventListener('transitionend', () => {
        /* We only change the display to "none" if we're collapsing the sidebar. */
        if (!sidebarCheckbox.checked) {
            sidebar.style.display = 'none';
        }
    });
    sidebarToggleButton.addEventListener('click', () => {
        /* To allow the sidebar expansion animation, we first need to put back the display. */
        if (!sidebarCheckbox.checked) {
            sidebar.style.display = '';
            // Workaround for Safari skipping the animation when changing
            // `display` and a transform in the same event loop. This forces a
            // reflow after updating the display.
            sidebar.offsetHeight;
        }
    });

    function showSidebar() {
        document.documentElement.classList.add('sidebar-visible');
        Array.from(sidebarLinks).forEach(function(link) {
            link.setAttribute('tabIndex', 0);
        });
        sidebarToggleButton.setAttribute('aria-expanded', true);
        sidebar.setAttribute('aria-hidden', false);
        try {
            localStorage.setItem('mdbook-sidebar', 'visible');
        } catch (e) {
            // Ignore error.
        }
    }

    function hideSidebar() {
        document.documentElement.classList.remove('sidebar-visible');
        Array.from(sidebarLinks).forEach(function(link) {
            link.setAttribute('tabIndex', -1);
        });
        sidebarToggleButton.setAttribute('aria-expanded', false);
        sidebar.setAttribute('aria-hidden', true);
        try {
            localStorage.setItem('mdbook-sidebar', 'hidden');
        } catch (e) {
            // Ignore error.
        }
    }

    // Toggle sidebar
    sidebarCheckbox.addEventListener('change', function sidebarToggle() {
        if (sidebarCheckbox.checked) {
            const current_width = parseInt(
                document.documentElement.style.getPropertyValue('--sidebar-target-width'), 10);
            if (current_width < 150) {
                document.documentElement.style.setProperty('--sidebar-target-width', '150px');
            }
            showSidebar();
        } else {
            hideSidebar();
        }
    });

    sidebarResizeHandle.addEventListener('mousedown', initResize, false);

    function initResize() {
        window.addEventListener('mousemove', resize, false);
        window.addEventListener('mouseup', stopResize, false);
        document.documentElement.classList.add('sidebar-resizing');
    }
    function resize(e) {
        let pos = e.clientX - sidebar.offsetLeft;
        if (pos < 20) {
            hideSidebar();
        } else {
            if (!document.documentElement.classList.contains('sidebar-visible')) {
                showSidebar();
            }
            pos = Math.min(pos, window.innerWidth - 100);
            document.documentElement.style.setProperty('--sidebar-target-width', pos + 'px');
        }
    }
    //on mouseup remove windows functions mousemove & mouseup
    function stopResize() {
        document.documentElement.classList.remove('sidebar-resizing');
        window.removeEventListener('mousemove', resize, false);
        window.removeEventListener('mouseup', stopResize, false);
    }

    document.addEventListener('touchstart', function(e) {
        firstContact = {
            x: e.touches[0].clientX,
            time: Date.now(),
        };
    }, { passive: true });

    document.addEventListener('touchmove', function(e) {
        if (!firstContact) {
            return;
        }

        const curX = e.touches[0].clientX;
        const xDiff = curX - firstContact.x,
            tDiff = Date.now() - firstContact.time;

        if (tDiff < 250 && Math.abs(xDiff) >= 150) {
            if (xDiff >= 0 && firstContact.x < Math.min(document.body.clientWidth * 0.25, 300)) {
                showSidebar();
            } else if (xDiff < 0 && curX < 300) {
                hideSidebar();
            }

            firstContact = null;
        }
    }, { passive: true });
})();

(function themes() {
    const html = document.querySelector('html');
    const themeToggleButton = document.getElementById('theme-toggle');
    const themePopup = document.getElementById('theme-list');
    const themeColorMetaTag = document.querySelector('meta[name="theme-color"]');
    const themeIds = [];
    themePopup.querySelectorAll('button.theme').forEach(function(el) {
        themeIds.push(el.id);
    });
    const stylesheets = {
        ayuHighlight: document.querySelector('#ayu-highlight-css'),
        tomorrowNight: document.querySelector('#tomorrow-night-css'),
        highlight: document.querySelector('#highlight-css'),
    };

    function showThemes() {
        themePopup.style.display = 'block';
        themeToggleButton.setAttribute('aria-expanded', true);
        themePopup.querySelector('button#' + get_theme()).focus();
    }

    function updateThemeSelected() {
        themePopup.querySelectorAll('.theme-selected').forEach(function(el) {
            el.classList.remove('theme-selected');
        });
        const selected = get_saved_theme() ?? 'default_theme';
        let element = themePopup.querySelector('button#' + selected);
        if (element === null) {
            // Fall back in case there is no "Default" item.
            element = themePopup.querySelector('button#' + get_theme());
        }
        element.classList.add('theme-selected');
    }

    function hideThemes() {
        themePopup.style.display = 'none';
        themeToggleButton.setAttribute('aria-expanded', false);
        themeToggleButton.focus();
    }

    function get_saved_theme() {
        let theme = null;
        try {
            theme = localStorage.getItem('mdbook-theme');
        } catch (e) {
            // ignore error.
        }
        return theme;
    }

    function delete_saved_theme() {
        localStorage.removeItem('mdbook-theme');
    }

    function get_theme() {
        const theme = get_saved_theme();
        if (theme === null || theme === undefined || !themeIds.includes(theme)) {
            if (typeof default_dark_theme === 'undefined') {
                // A customized index.hbs might not define this, so fall back to
                // old behavior of determining the default on page load.
                return default_theme;
            }
            return window.matchMedia('(prefers-color-scheme: dark)').matches
                ? default_dark_theme
                : default_light_theme;
        } else {
            return theme;
        }
    }

    let previousTheme = default_theme;
    function set_theme(theme, store = true) {
        let ace_theme;

        if (theme === 'dark' || theme === 'navy') {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = false;
            stylesheets.highlight.disabled = true;

            ace_theme = 'ace/theme/tomorrow_night';
        } else if (theme === 'ayu') {
            stylesheets.ayuHighlight.disabled = false;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = true;
            ace_theme = 'ace/theme/tomorrow_night';
        } else {
            stylesheets.ayuHighlight.disabled = true;
            stylesheets.tomorrowNight.disabled = true;
            stylesheets.highlight.disabled = false;
            ace_theme = 'ace/theme/dawn';
        }

        setTimeout(function() {
            themeColorMetaTag.content = getComputedStyle(document.documentElement).backgroundColor;
        }, 1);

        if (window.ace && window.editors) {
            window.editors.forEach(function(editor) {
                editor.setTheme(ace_theme);
            });
        }

        if (store) {
            try {
                localStorage.setItem('mdbook-theme', theme);
            } catch (e) {
                // ignore error.
            }
        }

        html.classList.remove(previousTheme);
        html.classList.add(theme);
        previousTheme = theme;
        updateThemeSelected();
    }

    const query = window.matchMedia('(prefers-color-scheme: dark)');
    query.onchange = function() {
        set_theme(get_theme(), false);
    };

    // Set theme.
    set_theme(get_theme(), false);

    themeToggleButton.addEventListener('click', function() {
        if (themePopup.style.display === 'block') {
            hideThemes();
        } else {
            showThemes();
        }
    });

    themePopup.addEventListener('click', function(e) {
        let theme;
        if (e.target.className === 'theme') {
            theme = e.target.id;
        } else if (e.target.parentElement.className === 'theme') {
            theme = e.target.parentElement.id;
        } else {
            return;
        }
        if (theme === 'default_theme' || theme === null) {
            delete_saved_theme();
            set_theme(get_theme(), false);
        } else {
            set_theme(theme);
        }
    });

    themePopup.addEventListener('focusout', function(e) {
        // e.relatedTarget is null in Safari and Firefox on macOS (see workaround below)
        if (!!e.relatedTarget &&
            !themeToggleButton.contains(e.relatedTarget) &&
            !themePopup.contains(e.relatedTarget)
        ) {
            hideThemes();
        }
    });

    // Should not be needed, but it works around an issue on macOS & iOS:
    // https://github.com/rust-lang/mdBook/issues/628
    document.addEventListener('click', function(e) {
        if (themePopup.style.display === 'block' &&
            !themeToggleButton.contains(e.target) &&
            !themePopup.contains(e.target)
        ) {
            hideThemes();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) {
            return;
        }
        if (!themePopup.contains(e.target)) {
            return;
        }

        let li;
        switch (e.key) {
        case 'Escape':
            e.preventDefault();
            hideThemes();
            break;
        case 'ArrowUp':
            e.preventDefault();
            li = document.activeElement.parentElement;
            if (li && li.previousElementSibling) {
                li.previousElementSibling.querySelector('button').focus();
            }
            break;
        case 'ArrowDown':
            e.preventDefault();
            li = document.activeElement.parentElement;
            if (li && li.nextElementSibling) {
                li.nextElementSibling.querySelector('button').focus();
            }
            break;
        case 'Home':
            e.preventDefault();
            themePopup.querySelector('li:first-child button').focus();
            break;
        case 'End':
            e.preventDefault();
            themePopup.querySelector('li:last-child button').focus();
            break;
        }
    });
})();

(function clipboard() {
    const clipButtons = document.querySelectorAll('.clip-button');

    function hideTooltip(elem) {
        elem.firstChild.innerText = '';
        elem.className = 'clip-button';
    }

    function showTooltip(elem, msg) {
        elem.firstChild.innerText = msg;
        elem.className = 'clip-button tooltipped';
    }

    const clipboardSnippets = new ClipboardJS('.clip-button', {
        text: function(trigger) {
            hideTooltip(trigger);
            const playground = trigger.closest('pre');
            return playground_text(playground, false);
        },
    });

    Array.from(clipButtons).forEach(function(clipButton) {
        clipButton.addEventListener('mouseout', function(e) {
            hideTooltip(e.currentTarget);
        });
    });

    clipboardSnippets.on('success', function(e) {
        e.clearSelection();
        showTooltip(e.trigger, 'Copied!');
    });

    clipboardSnippets.on('error', function(e) {
        showTooltip(e.trigger, 'Clipboard error!');
    });
})();

(function scrollToTop() {
    const menuTitle = document.querySelector('.menu-title');

    menuTitle.addEventListener('click', function() {
        document.scrollingElement.scrollTo({ top: 0, behavior: 'smooth' });
    });
})();

(function controllMenu() {
    const menu = document.getElementById('menu-bar');

    (function controllPosition() {
        let scrollTop = document.scrollingElement.scrollTop;
        let prevScrollTop = scrollTop;
        const minMenuY = -menu.clientHeight - 50;
        // When the script loads, the page can be at any scroll (e.g. if you refresh it).
        menu.style.top = scrollTop + 'px';
        // Same as parseInt(menu.style.top.slice(0, -2), but faster
        let topCache = menu.style.top.slice(0, -2);
        menu.classList.remove('sticky');
        let stickyCache = false; // Same as menu.classList.contains('sticky'), but faster
        document.addEventListener('scroll', function() {
            scrollTop = Math.max(document.scrollingElement.scrollTop, 0);
            // `null` means that it doesn't need to be updated
            let nextSticky = null;
            let nextTop = null;
            const scrollDown = scrollTop > prevScrollTop;
            const menuPosAbsoluteY = topCache - scrollTop;
            if (scrollDown) {
                nextSticky = false;
                if (menuPosAbsoluteY > 0) {
                    nextTop = prevScrollTop;
                }
            } else {
                if (menuPosAbsoluteY > 0) {
                    nextSticky = true;
                } else if (menuPosAbsoluteY < minMenuY) {
                    nextTop = prevScrollTop + minMenuY;
                }
            }
            if (nextSticky === true && stickyCache === false) {
                menu.classList.add('sticky');
                stickyCache = true;
            } else if (nextSticky === false && stickyCache === true) {
                menu.classList.remove('sticky');
                stickyCache = false;
            }
            if (nextTop !== null) {
                menu.style.top = nextTop + 'px';
                topCache = nextTop;
            }
            prevScrollTop = scrollTop;
        }, { passive: true });
    })();
    (function controllBorder() {
        function updateBorder() {
            if (menu.offsetTop === 0) {
                menu.classList.remove('bordered');
            } else {
                menu.classList.add('bordered');
            }
        }
        updateBorder();
        document.addEventListener('scroll', updateBorder, { passive: true });
    })();
})();
