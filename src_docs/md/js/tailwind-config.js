// this_file: src_docs/md/js/tailwind-config.js
// Tailwind Play CDN settings for the utility classes posts use via attr_list
// (rounded-lg, shadow, grid, w-1/2, float-right, ...). Loaded right after
// https://cdn.tailwindcss.com in extra_javascript. Preflight is off so Tailwind's base
// reset cannot clobber the theme; utilities are scoped to article content.
tailwind.config = {
  corePlugins: { preflight: false },
  important: ".md-typeset",
};
