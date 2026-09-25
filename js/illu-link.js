// this_file: src_docs/md/js/illu-link.js
// Wrap each blog-index thumbnail (.illu-thumb) in an anchor that points at
// the same URL as the post's H2 title link. Decorative — the title link is
// the canonical accessible name, so we mark the image link aria-hidden and
// remove it from the tab order to avoid duplicate stops for keyboard users.
(() => {
  const wrap = () => {
    document.querySelectorAll(".md-post--excerpt").forEach((post) => {
      const img = post.querySelector(".illu-thumb");
      if (!img || img.parentElement?.tagName === "A") return;
      const titleLink = post.querySelector("h1 a, h2 a, h3 a");
      if (!titleLink) return;
      const a = document.createElement("a");
      a.href = titleLink.href;
      a.className = "illu-thumb-link";
      a.setAttribute("aria-hidden", "true");
      a.tabIndex = -1;
      img.replaceWith(a);
      a.appendChild(img);
    });
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wrap);
  } else {
    wrap();
  }
})();
