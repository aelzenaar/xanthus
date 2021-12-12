## High-level overview

The basic workflow is as follows:

 * Edit files inside some root directory
 * Periodically run the `xp' command to:
  - git commit and push to a backup
  - compile the root directory into a static HTML structure and push to the web


## File system format

 * Metadata is to be stored in a .file in each directory inside the root: the `.xanthus` file
   will be in .json format and may contain the following top-level keys:
  - `"links"` -  a list of URLs to include links to
  - `"photos"` - a list of images to include in a gallery
  - `"pinned"` - a list of files contained in the directory to pin at the top of the page, user added
  - `"autopinned"` - list of autopinned files (see `"autopins"` below)
  - `"texts"` - a list of short text messages to include
  - `"fortune"` - a single text to include at the bottom of the page, randomly generated at compile time when the `.xanthus` file is generated

 * The root directory `.xanthus` file will necessarily contain key-value `"root": true` (this is to prevent the user accidentally running commands in a deeper directory, so we can search
   back up the file tree and find the root directory).
  - The root directory is also the git root directory
  - Compiled HTML files should not be placed in the root directory - compilation process should be deterministic (based only on contents of the directory tree at compile time). The `"htmldir"` key may be
    used to specify the output directory. Default will be `~/xanthus.out/`.

 * The following directives if appearing in a `.xanthus` file will propagate down to the directories contained in the current one:
  - `"autopins"` - a list of regexps which will be compared with filenames; matching files in each subdirectory will be added to the `"autopinned"` list of that subdirectory
    when `x autopin` is run. For instance, one might want all the PDFs to be listed at the top level.
  - `"project"` - a short human-readable name for the project that this subdirectory tree corresponds to

## Commands needed

 * `x addlink` - add link to current directory
 * `x addphoto` - add file in current directory to `photos` list
 * `x addpin` - pin file to top of current directory
 * `x minifortune` - get a short fortune & print to the command line
 * `x maxifortune` - get a long fortune & print it to the command line
 * `x autopins -l` - print the list of files to be automatically pinned by `x autopins`
 * `x autopins` - append files to `"autopinned"` which match a regex and which don't yet appear in the list
 * `x autopins -r` - clear list of automatic pins from the current directory and regenerate from scratch
 * `x backup` or `xb` - git commit and push to specified backup
 * `x compile` or `xc` - compile to static HTML directory structure
 * `x web` or `xw` - push compiled HTML to web


## HTML pages

```

  HEADER
  ======

  SHORT FORTUNE


  LIST OF PINS

  LIST OF LINKS

  LIST OF PHOTOS

  LIST OF AUTOPINS

  ===

  LIST OF FILES WITH CREATE/MODIFY DATES ETC

  ===
  FOOTER

```

