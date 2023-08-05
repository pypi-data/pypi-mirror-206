# pyssg - Static Site Generator written in Python

Generates HTML files from MD files for a static site, personally using it for a blog-like site.

Initially inspired by Roman Zolotarev's [`ssg5`](https://rgz.ee/bin/ssg5) and [`rssg`](https://rgz.ee/bin/rssg), Luke Smith's [`lb` and `sup`](https://github.com/LukeSmithxyz/lb) and, pedantic.software's [`blogit`](https://pedantic.software/git/blogit/).

## Features and to-do

**NOTE:** WIP, there will be changes that will break `pyssg` generations/config setup.

- [x] Build static site parsing `markdown` files ( `*.md` -> `*.html`)
	- [x] Uses [`jinja`](https://jinja.palletsprojects.com/en/3.0.x/) for templating.
	- [x] Preserves hand-made `*.html` files.
	- [x] Tag functionality, useful for blog-style sites.
- [x] Build `sitemap.xml` file.
	- [ ] Include manually added `*.html` files.
- [x] Build `rss.xml` file.
	- [ ] Include manually added `*.html` files.
- [x] YAML for configuration file, uses [`PyYAML`](https://pyyaml.org/).
	- [x] Support for multiple "documents". `PyYAML` supports this. In `pyssg` context, it means it can generate multiple websites (I personally use it for subdomains).
	- [x] Support for more complex directory structure to support configuration on a per directory basis.
- [x] File checksum checking for modification of files.
- [ ] Option/change to using an SQL database instead of the custom solution.
- [ ] Use external markdown extensions.
  - [x] So far only extension configuration is for my own extension [pymdvar](https://github.com/luevano/pymdvar).

### Markdown features

This program uses the base [`markdown` syntax](https://daringfireball.net/projects/markdown/syntax) plus additional syntax, all thanks to [`python-markdown`](https://python-markdown.github.io/) that provides [extensions](https://python-markdown.github.io/extensions/). The following extensions are used:

- Extra (collection of QoL extensions).
- Meta-Data.
- Sane Lists.
- SmartyPants.
- Table of Contents.
  - With `permalink=True` and `baselevel=2`, for more: [python-markdown toc](https://python-markdown.github.io/extensions/toc/).
- WikiLinks.
- [pymdvar](https://github.com/luevano/pymdvar) (made by me).
- [yafg - Yet Another Figure Generator](https://git.sr.ht/~ferruck/yafg)
- [Markdown Checklist](https://github.com/FND/markdown-checklist)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
	- [Caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret/)
	- [Tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/)
	- [Mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/)

## Installation

Install with `pip`:

```sh
pip install pyssg
```

Probably will add a PKBUILD (and possibly submit it to the AUR) in the future.

## Usage

1. Get the default configuration file:

```sh
pyssg --copy-default-config -c <path/to/config>
```

- Where `-c` is optional as by default `$XDG_CONFIG_HOME/pyssg/config.yaml` is used.

2. Edit the config file created as needed.

- `config.yaml` is parsed using [`PyYAML`](https://pyyaml.org/), [more about the config file](#config-file).

3. Initialize the directory structures (source, destination, template) and move template files:

```sh
pyssg -i
```

- You can modify the basic templates as needed (see [variables available for Jinja](#available-jinja-variables)).

- Strongly recommended to edit the `rss.xml` template.

4. Place your `*.md` files somewhere inside the source directory. It accepts sub-directories. Optionally configure for subdirectories if they are to be treated a bit different.

- Recommended (no longer mandatory) metadata keys that can be added to the top of `.md` files:

```
title: the title of your blog entry or whatever
author: your name or online handle
	another name maybe for multiple authors?
lang: the language the entry is written on
summary: a summary of the entry
tags: english
	short
	tutorial
	etc
```

- You can add more meta-data keys as long as it is [Python-Markdown compliant](https://python-markdown.github.io/extensions/meta_data/), and these will ve [available as Jinja variables](#available-jinja-variables) in the `meta` object (`dict[str, Any]`).

5. Build the `*.html` with:

```sh
pyssg -b
```

- After this, you have ready to deploy `*.html` files from the `dst` directory.

## Config file

All sections/options need to be compliant with [`PyYAML`](https://pyyaml.org/) which should be compliant with [`YAML 1.2`](https://yaml.org/spec/1.2.2/). Additionaly, I've added the custom tag `!join` which concatenates strings from an array, which an be used as follows:

```yaml
variable: &variable_reference_name "value"
other_variable: !join [*variable_reference_name, "other_value", 1]
```

Which would produce `other_variable: "valueother_value1"`. Also **environment variables will be expanded internally**.

**Note**: URL's shouldn't have the trailing slash `/`.

The following is a list of config items that need to be present in the config unless stated otherwise:

```yaml
%YAML 1.2
---
# not needed, shown here as an example of the !join tag
define: &root "$HOME/path/to/" # $HOME expands to /home/user, for example

title: "Example site"
path:
  src: !join [*root, "src"] # $HOME/path/to/src
  dst: "$HOME/some/other/path/to/dst"
  plt: "plt"
  db: !join [*root, "src/", "db.psv"]
url:
  main: "https://example.com"
  # I personally use a "static" url for images/scripts/css/etc, not necessary
  static: "https://static.example.com"
fmt:
  date: "%a, %b %d, %Y @ %H:%M %Z"
  list_date: "%b %d" # not necessary
  list_sep_date: "%B %Y" # not necessary
dirs:
  /: # root "dir_path", whatever is sitting directly under "src"
    cfg:
      plt: "page.html" # each page template, relative to path/plt
      tags: False
      index: True
      rss: True
      sitemap: True
      exclude_dirs: ["articles", "blog"] # optional; list of subdirs to exclude when parsing this "dir_path"
...
```

So far only [pymdvar](https://github.com/luevano/pymdvar) can be configured by including the following to the config:

```yaml
exts:
  pymdvar:
    variables:
      SOME_VAR: "some value"
      some_other_variable: 123
    enable_env: True # to read environment variables
```

The config under `dirs` are just per-subdirectory configuration of directories under `src`, which I called "dir_paths" for lack of creativity. Only the `/` "dir_path" is required as it is the config for the root `src` path files. Mandatory config items for each "dir_path":

```yaml
cfg:
  plt: "template.html"
  tags: True
  index: True
  rss: True
  sitemap: True
  exclude: [] # not necessary
```

So that extra "dir_paths" can be added under `dirs`:

```yaml
dirs:
  /:
    cfg:
      ...
  articles:
    cfg:
      ...
  gallery:
    cfg:
      ...
  etc:
    ...
```

The following will be added on runtime to the configuration:

```yaml
%YAML 1.2
---
fmt:
  rss_date: "%a, %d %b %Y %H:%M:%S GMT" # fixed
  sitemap_date: "%Y-%m-%d" # fixed
info:
  version: "x.y.z" # current 'pyssg' version (0.5.1.dev16, for example)
  debug: True/False # depending if --debug was used when executing
rss_run_date: # date the program was run, formatted with 'fmt.rss_date'
sitemap_run_date: # date the program was run, formatted with 'fmt.sitemap_date'
...
```

You can add any other option/section that you can later use in the Jinja templates via the exposed config object.


## Available Jinja variables

These variables are exposed to use within the templates. The below list is displayed in the form of *variable (type) (available from): description*. `field1/field2/field3/...` describe config file section from the YAML file and option and `object.attribute` corresponding object and it's attribute.

- `config` (`dict[str, Any]`) (all): parsed config file plus the added options internally (as described in [config file](#config-file)).
- `dir_config` (`dict[str, Any]`) (all*): parsed dir_config file plus the added options internally (as described in [config file](#config-file)). *This is for all of the specific "dir_path" files, as per configured in the YAML file `dirs.dir_path.cfg` (for exmaple `dirs./.cfg` for the required dir_path).
- `all_pages` (`list(Page)`) (all): list of all the pages, sorted by creation time, reversed.
- `page` (`Page`) (`page.html`): contains the following attributes (genarally these are parsed from the metadata in the `*.md` files):
	- `title` (`str`): title of the page.
	- `author` (`list[str]`): list of authors of the page.
	- `lang` (`str`): page language, used for the general `html` tag `lang` attribute.
	- `summary` (`str`): summary of the page, as specified in the `*.md` file.
	- `content` (`str`): actual content of the page, this is the `html`.
    - `toc` (`str`): table of contents as taken from `md.toc`.
    - `toc_tokens` (`list[dict[str, Any]]`): table of contents tokens as taken from `md.toc_tokens`.
	- `cdatetime` (`datetime.datetime`): creation datetime object of the page.
	- `cdate` (`method(FMT: str)`): takes the name of the `fmt.FMT` and applies it to the `cdatetime` object.
	- `cdate_rss` (`str`): formatted `cdatetime` as required by rss.
	- `cdate_sitemap` (`str`): formatted `cdatetime` as required by sitemap.
	- `mdatetime` (`datetime.datetime`): modification datetime object of the page. Defaults to `None`.
	- `mdate` (`method(FMT: str)`): takes the name of the `fmt.FMT` and applies it to the `mdatetime` object.
	- `mdate_rss` (`str`): formatted `mdatetime` as required by rss.
	- `mdate_sitemap` (`str`): formatted `mdatetime` as required by sitemap.
	- `tags` (`list[tuple[str]]`): list of tuple of tags of the page, containing the name and the url of the tag, respectively. Defaults to empty list.
	- `url` (`str`): url of the page, this already includes the `url/main` from config file.
	- `next/previous` (`Page`): reference to the next or previous page object (containing all these attributes). Defaults to `None`.
	- `meta` (`dict[str, list[str]]`): meta dict as obtained from `python-markdown`, in case you use a meta tag not directly supported, it will be available there.
- `tag` (`tuple[str]`) (`tag.html`): tuple of name and url of the current tag.
- `tag_pages` (`list[Page]`) (`tag.html`): similar to `all_pages` but contains all the pages for the current tag.
- `all_tags` (`list[tuple[str]]`) (all): similar to `page.tags` but contains all the tags.
