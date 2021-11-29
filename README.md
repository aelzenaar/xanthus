# xanthus

> just finished the iliad for the first time & can say decisively that the funniest moment in all 24 books is when a horse who has previously never spoken speaks just long enough to prophesy Achilles' death & Achilles, very understandably, is like "shut the fuck up. you're a horse"


I should be writing a conference talk for Thursday and working on my thesis, but instead I am working on a replacement for [the bad pensieve](https://github.com/aelzenaar/bucephalus) which I wrote
three years ago.

## To remind myself
[(Original list)](https://github.com/aelzenaar/bucephalus/blob/master/lessons.md)

### The good
 * I like the templating features of `bucvac`.
 * I like `/v/coffee`.
 * Random long and short fortunes.
 * Archiving things worked perfectly.
 * Tags worked well.
 * Geogebra embedding was useful, I wish I had a better use for it.
 * The task manager (`buctask`) worked well and I used it a lot.
 * Pinning a document to the front page. (I like the restriction to a single thing.)
 * The idea of a recent documents page.

### The bad
 * No way of 'linking' related documents together in a linear way.
 * No way of hyperlinking between documents easily.
 * No way of storing related documents/files together (e.g. images with source code).
 * Running `bucvac` was really slow.
 * No way of linking to external URLs easily so I could find them again.
 * JSON databases are not scalable.

### The ugly
 * Search!
 * The document interface (the iframe holding PDF) was clunky.
 * The document storage backend was kind of hacky.
 * Version control is hard when storing PDFs.
 * The implementation of the recent docs page was really hacky.


## Another list
 * [Writing Xournal++ plugins in Lua](https://xournalpp.github.io/guide/plugins/plugins/)
 * [A similar system written in Mathematica](http://drorbn.net/AcademicPensieve/About.html)
 * [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 * [XKCD 1024](https://xkcd.com/1024/), [XKCD 1743](https://xkcd.com/1743/)
 * [SE api](https://api.stackexchange.com/)


## Thus, a list of features for the new thing.
 * Tags
 * Long/short fortunes
 * Recent documents
 * Search (?)
 * Xournal++ integration
 * Heirachical structure with top-level indexes that can store related links (external links, and "see also" links) etc --- store files in the filesystem (so editable) with metadata in hidden files
   and then run a script to generate HTML and push online
 * Embed images
 * Embed PDFs
 * Version control integration
 * Task manager
 * Pinning documents

## Things not to be included
 * LaTeX integration (too much hassle & too annoying)
 * Geogebra embedding (not very useful)
