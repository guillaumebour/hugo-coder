# Hugo-coder-photo

This is a simple theme for Hugo. It is based on the [hugo-coder](https://github.com/luizdepra/hugo-coder) theme 
from Luiz F. A. De Prá. The major difference lies in the gallery feature (see below).

![](https://github.com/guillaumebour/hugo-coder/blob/master/images/screenshot_3.png)

![](https://github.com/guillaumebour/hugo-coder/blob/master/images/screenshot_4.png)


## Features

This theme provides blog posts along with a photo gallery.

![](https://github.com/guillaumebour/hugo-coder/blob/master/images/screenshot_2.png)

### Blog

One can create posts with a support for Math, Code, Table, etc. See the exampleSite for more details.

### Gallery

One can add a location and/or a description to each picture (altering the way a picture is displayed). Note that you may encounter performance issues when trying to load big pictures.

![](https://github.com/guillaumebour/hugo-coder/blob/master/images/screenshot_5.png)


## How to use this theme

To use `hugo-coder` go through the following steps.

### Download

Clone this repository into your Hugo project.

```
git clone https://github.com/guillaumebour/hugo-coder.git themes/coder
```

### Configuration

Add the following lines to your `config.toml`.

```toml
theme = "coder"

languagecode = "en"

paginate = 20
canonifyurls = true

# disqusShortname = "yourdiscussshortname"

[params]
    author = "John Doe"
    description = "John Doe's personal website"
    keywords = "blog,developer,personal"
    info = "Full Stack DevOps and Magician"
    # info2 = "..."
    avatarurl = "images/avatar.jpg"

[[params.social]]
    name = "Github"
    weight = 1
    url = "https://github.com/johndoe/"
[[params.social]]
    name = "Twitter"
    weight = 2
    url = "https://twitter.com/johndoe/"
[[params.social]]
    name = "LinkedIn"
    weight = 3
    url = "https://www.linkedin.com/in/johndoe/"

[[menu.main]]
    name = "Blog"
    weight = 1
    url  = "/posts/"
[[menu.main]]
    name = "Gallery"
    weight = 2
    url  = "/gallery/"
[[menu.main]]
    name = "About"
    weight = 3
    url = "/about/"
```

### Build & Test

To update or generate the minified CSS file:

```
make build
```

To build your site and test, run:

```
hugo server
```

### Disqus support
Copy the following line to your config, ```disqusShortname = "yourdiscussshortname"```. 
This will enable disqus on all posts.
 
To disable comments for a post, add the following to the page meta data.
```disable_comments: true```


## Contribute

### Using the exampleSite

The exampleSite directory contains everything needed to work easily on the project.
To populate the site with random texts and images just go in the `exampleSite` and run `python3 populate.py`.

You can change the number of images that are downloaded by the script by changing the `NB_IMG` variable.

### To Do

- Tags, Categories and Series
- Improving the picture's layout when displayed in "single" mode  


## License

Coder is licensed under the [MIT license](https://github.com/guillaumebour/hugo-coder/blob/master/LICENSE.md).


## Authors

[Luiz de Prá](https://luizdepra.com) (author of the original project [hugo-coder](https://github.com/luizdepra/hugo-coder))   
[Guillaume Bour](https://guillaumebour.fr)

Some code in this project is inspired from the original project but might have required changes.
See the commit messages for more details.
