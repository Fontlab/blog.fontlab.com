The paths are relative to the root of the git repo. 

## Writable references

Write easy build scripts and Github Actions modern as of May 2026. You may push to the repos, if you have write access. 

### ./reference/fontlab-partners/

This is an MkDocs + MaterialX theme site hosted at https://partners.fontlab.com/ via Github Pages — I’ve developed it last month. It includes customizations to the MaterialX theme that is relatively lightweight. 

Very importantly, it uses a shared menu and footer via a remotely-loaded web component from https://i.fontlab.com/menu/ 

Also, it adds Tailwind CSS and daisyUI. Overall, I like the design that is used there. Some pages are HTML, and some (like https://partners.fontlab.com/downloads/ ) are mainly Markdown. 

You may write here if you find some really obvious bugs. But overall this repo is in good shape. 

### ./reference/fldoc/

This includes a an older version at https://help.fontlab.com/fontlab/8/ that is also hosted on Github Pages. 

It was built with the predecessor of ProperDocs (MkDocs), with the predecessor of MaterialX (MkDocs Material 8/9). It includes many more styling customizations. Also, importantly, it uses a lot of plugins and extensions. 

- reference/fldoc/src/fontlab/8/mk-base.yml 
- reference/fldoc/src/fontlab/8/mk-fontlab-8.yml

You should modernize this repo to fix the most glaring problems. But overall this repo is in okay shape. 

### twardown packages 

You can incorporate these into our project if useful. And you can modernize them if needed. Make sure each is easily publishable. Prepare them for publishing to PyPI and NPM. Publish them. Write easy build scripts and Github Actions modern as of May 2026. 

- ./reference/twardown-docs/ 
- ./reference/twardown-js/
- ./reference/twardown-org/
- ./reference/twardown-py/

## Read-only references

### ./reference/FontLabVI-help/

This includes an even more ancient site, more for FontLab VI and 7. If you find everything you need in ./reference/fontlab-partners/ and in ./reference/fldoc/ — you don’t need this one. 

### ./reference/fontlab-com-oldpub/

This includes old content exported from WordPress to an old form of blog. Esp. ./reference/fontlab-com-oldpub/2013/ to ./reference/fontlab-com-oldpub/2023/ and also some aggregate older info in ./reference/fontlab-com-oldpub/about/index.html 

## Writable Python tools 

Below are some Python packages. You can contribute it and push there, because the folders are independent repos we control. 

Make sure all our Python tools are ready to be published to PyPI. 

They should use 'uv publish', and 'uvx hatch test' and 'uvx hatch build'. Make sure we use hatch-vcs with git semver tags, with __version__.py being in .gitignore. 

In each, prepare ./build.sh and ./publish.sh , and Github Actions modern as of May 2026. You may push to the repos, if you have write access. 

We ALSO MUST MODERNIZE the ProperDocs/MkDocs-dependent code so it’s compatible with https://github.com/mkdocs/mkdocs v1.6.1. 

We must modernize the Python Markdown-dependent code so it’s compatible with the most recent https://github.com/Python-Markdown/markdown v3.10.2 and Python 3.12+. 

### ./reference/vexy-mkdocs-output-as-input/

This is a ProperDocs plugin that’s useful and that we should be using. 

### ./reference/reference/vexy-mkdocs-strip-number-prefix/

This is a ProperDocs plugin that’s useful and that we should be using. 

### ./reference/vexy-mkdocs-text-export/

This is a ProperDocs plugin that’s useful and that we should be using. 

We’ve migrated this repo from 'twardoch' and 'vexyart' org on Github. We should rename the package inside to 'vexy-mkdocs-text-export', and adjust everything accordingly. 

### ./reference/vexy-mkdocs-markdown-in-template/

This is a ProperDocs plugin that’s useful and that we should be using. 

We’ve migrated this repo from 'twardoch' and 'vexyart' org on Github. We should rename the package inside to 'vexy-mkdocs-markdown-in-template', and adjust everything accordingly. 

### ./reference/vexy-mkdocs-tags/

This is a ProperDocs plugin that’s useful and that we should be using. 

We’ve migrated this repo from 'twardoch' and 'vexyart' org on Github. We should rename the package inside to 'vexy-mkdocs-tags', and adjust everything accordingly. 

### ./reference/vexy-mkdocs-tools/

This is a tool we should create and develop. This would include a Fire-based CLI tool that would help with the development of FontLab-specific MkDocs sites. All functionality that’s NOT a MkDocs plugin or a Python Markdown extension should go there. 

Ultimately it should wrap things, it should specify the dependencies, and provide a CLI tool, so it’s possible to do 'uvx vexy-mkdocs-tools build' and a site builds. 

### ./reference/vexy-marktripy/

This is a useful tool to consider in the workflow. 

We’ve migrated them from 'twardoch' and 'vexyart' org on Github. We should rename the package inside to 'vexy-marktripy', and adjust everything accordingly. 

We ALSO MUST MODERNIZE the code so it’s compatible with Python 3.12+. 

### ./reference/vexy-python-markdown-steroids/

This is a set of Python Markdown extensions. 

We’ve migrated them from 'twardoch' and 'vexyart' org on Github. We should rename the package inside to 'vexy-python-markdown-steroids', and adjust everything accordingly. 

We ALSO MUST MODERNIZE the code so it’s compatible with the most recent Python Markdown and Python 3.12+. 

## Read-only Python tools

### ./reference/properdocs/

This is the readonly clone of the new maintained fork of MkDocs. We must migrate everything we do from MkDocs to ProperDocs. MkDocs is 'end of life' and future MkDocs v2 is supposed to have breaking changes. 

You must MODERNIZE ALL OUR CODE TO WORK WITH PROPERDOCS, including all writable Python tools and MkDocs plugins. 

### ./reference/mkdocs-materialx/ 

This is the readonly clone of the theme that follows-up to the original end-of-life "MkDocs Material". It's the theme from which we build our sites. Make sure our new site works perfectly with it, and surgically extends it. 

You must MODERNIZE ALL OUR CODE that used MkDocs Material to work with ProperDocs and MaterialX, including all writable Python tools and MkDocs plugins. 

Here are also three MaterialX plugins for ProperDocs:

- https://jaywhj.github.io/mkdocs-materialx/plugins/optimize.html 
- https://jaywhj.github.io/mkdocs-materialx/plugins/tags.html
- https://jaywhj.github.io/mkdocs-materialx/plugins/blog.html — this is ABSLUTELY CRUCIAL

### Python ProperDocs (MkDocs) plugins

There are local clones of established MkDocs plugins. If they’re truly deployed to PyPI, we add them to the requirements of vexy-mkdocs-tools. If they’re not deployed to PyPI, fork them to new repos inside ./reference/github.vexyart/ folder with a `vexy-` prefix and for the https://github.com/vexyart org. Create all the right scaffolding (hatch, uv, build.sh, publish.sh etc.). And then commit, push, and publish. Then add these new forks to the requirements of vexy-mkdocs-tools.

- ./reference/mkdocs-awesome-nav/
- ./reference/mkdocs-include-markdown-plugin/ 
- ./reference/mkdocs-pagenav-generator/ 
- ./reference/mkdocs-ezlinks-plugin/ or ./reference/mkdocs-roamlinks-plugin/ (analyze and pick one)
- ./reference/mkdocs-link-embeds/ 
- ./reference/mkdocs-llmstxt/ 
- ./reference/mkdocs-copy-to-llm/

### Python Markdown extensions

- ./reference/pymdown-extensions/ 

## Goal

The overall goal is that we create a modern (as of 2026) ProperDocs-based site for https://blog.fontlab.com/ that is published to Github Pages. The publishing will go to the `docs/` folder. The folder should include the sources for the site: the ProperDocs configuration and other necessary tools, and in `src_docs/md/` the Markdown sources. 

The goal is that inside our current codebase we’ll make a SIMPLE CLI tool that uses `uv` and calls `vexy-mkdocs-tools` to build the https://blog.fontlab.com/ site. The tool should also be able to explicitly publish it to Github Pages. The tool should also be invokable by a Github Action that runs on every git tagging.  

You also must create blog content that will be compatible with https://jaywhj.github.io/mkdocs-materialx/plugins/blog.html 

You need to take content from ./reference/fontlab-com-oldpub/ and ./reference/fldoc/ and ./reference/FontLabVI-help/ and incorporate it into the new site. 

- For pages/posts that are written as blog posts, don’t heavily modify them. For documents from that are written as blog posts, don’t heavily modify them. Only port "blog-style" content from there. 
- For content from ./reference/fldoc/ and ./reference/FontLabVI-help/ only provide short summaries. Again, only port "blog-style" content from there ("news")
- DO NOT port announcements about promos/sales. We retire them. 
- Use date-times of the original content, if available. 

## Tasks

- Into ./spec/ write a 12-chapter specification of the new site (one markdown file per chapter). Start with ./spec/00-toc.md  which should contain a ToC and a TLDR of each chapter. Then write ./spec/01.md to ./spec/12.md
- Into ./TODO.md write a list of tasks to be done, based on the spec. Prefix each with a `- [ ]` 
- As you write on the implementation, update ./TODO.md with the tasks you've completed, and update ./CHANGELOG.md with the changes you've made. 

## Writing style 

WRITING RULES: Before you start writing, ultrathink about the right structure and narrative. Then write the story, and follow these rules: Lead strong: First line earns attention for what follows. No throat-clearing. Plain language (No jargon, passive voice, or corporate fluff.) Concise (Every sentence must count.) Show, don’t tell (Specific examples over abstractions.) UX matters (Error messages are user experience, make them helpful.) Edit ruthlessly (If rereading is needed, rewrite). Remove: Fluff, bloat, corpo jargon, hype words like "revolutionary". Light, understated humor is allowed with a hint of the personality of Norm Macdonald mixed with Stephen Fry; but clarity wins. Generally follow Stephen King’s writing advice. 