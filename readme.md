# proglang.github.io

Built with [mdBook](https://rust-lang.github.io/mdBook/) 0.5.4. The binaries in
`bin/` are checked in so no toolchain is needed; to upgrade, drop new ones from
the [releases page](https://github.com/rust-lang/mdBook/releases) and re-apply
the customisations in `theme/` (see below).

## usage

- `./publish "message"`:
  - runs pull rebase autostash
  - builds locally to `docs/` directory
  - pushes changes to master
- `./watch`
  - runs pull rebase autotash
  - builds locally to `docs/` directory
  - watches changes and rebuilds automatically
  - launches web server to see changes at `localhost:3000`

## unlisted pages

mdBook only builds pages listed in `src/SUMMARY.md`. `./sync-summary` — run by
`./build`, `./watch` and `./publish`, so you never call it yourself — appends
every `src/**/*.md` that is not listed by hand to an `# Unlisted` section at the
end of the file. A rule at the bottom of `theme/css/chrome.css` hides that whole
section from the sidebar, so those pages are built and reachable by URL but do
not show up in the navigation.

Drop a markdown file anywhere under `src/` and it is live at the matching `.html`
path on the next build. To give it a spot in the navigation instead, add it to
the list above the `# Unlisted` heading; it disappears from the generated section
by itself.

## theme

`theme/` overrides the mdBook default theme. Deviations from the stock 0.5.4
files:

- `index.hbs`: keyboard-shortcut popup, print/repo/edit buttons and the
  previous/next chapter navigation are commented out; theme picker offers only
  Auto/Light/Dark.
- `book.js`: `chapterNavigation()` removed (there is no prev/next nav), with the
  Escape-closes-a-zoomed-image bit from it added back at the end of the file; the
  dark theme uses the tomorrow-night highlight stylesheet.
- `css/variables.css`: our colour palette, only `light` and `dark` themes.
- `css/chrome.css`: menu title alignment, `menu-icon`, unlisted-pages rule.
- `css/general.css`: table alignment/overflow.
- `fonts/fonts.css`, `highlight.js`: local fonts, extra languages.
