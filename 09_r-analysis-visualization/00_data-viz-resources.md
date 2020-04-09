# Data Visualization Resources 

> ### Contents
> 
> * Resources for designing good plots (e.g. choosing colors, visual design, vector drawing software, etc.).
> * Resources for plotting using `ggplot2` and `baser`.
> * Resources for mapping in R.



## A. Visual design 

These books (free with the Berkeley libarary login) describe good and bad design principles:
* [Visualize This by Nathan Yau](https://ebookcentral.proquest.com/lib/berkeley-ebooks/detail.action?docID=693541)
* [Data Points: Visualization That Means Something by Nathan Yau](https://ebookcentral.proquest.com/lib/berkeley-ebooks/detail.action?docID=1158630)

Other guides for good plot design: 
* [Flowing Data Guides](https://flowingdata.com/category/guides/)
* [Guides and advice from The Pudding](https://pudding.cool/topics/#how)
* [Choosing plot types](http://experception.net/Franconeri_ExperCeptionDotNet_DataVisQuickRef.pdf)

### A.1. Colors 

Websites for picking colors: 
* [Colorbrewer website](http://colorbrewer2.org) allows users to browse color pallets available through the `colorbrewer` R package. 
* [Adobe Colorwheel](https://color.adobe.com/create/color-wheel/) helps to find compatable colors. 

R Packages: 
* [Viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)
* [Colorbrewer](https://www.r-bloggers.com/how-to-expand-color-palette-with-ggplot-and-rcolorbrewer/)

### A.2. Editing vector images

Normally, you want to save plots as .pdfs rather than pictures because they will be saved as *vector* rather than *raster* graphics. Unlike raster graphics, which are composed of pixles, vector graphics are composed of geometry (think lines and points). Importantly, you can zoom into vector plots without the image pixelating or losing clarity. For more information, google "vector vs raster" or see these guides: [link 1](https://www.geeksforgeeks.org/vector-vs-raster-graphics/) or [link 2](https://www.shutterstock.com/blog/raster-vs-vector-file-formats). 

If you need to make small adjustments to an existing (.pdf) graph, consider using a vector drawing software (like photoshop but better for graphs). With the university Adobe license, you may be able to get a free copy of [Adobe Illustrator](https://www.adobe.com/products/illustrator.html). Alternatively, you can use a free, opensource software called [Inkscape](https://inkscape.org/). For more information about using Inkscape, see these [Inkscape tutorials](https://inkscape.org/learn/tutorials/). 


## B. Tidyverse (ggplot2)

**Best ggplot2 resource** for finding template code for different plot types: [Cookbook for R](http://www.cookbook-r.com/Graphs/). You may also find the [ggplot2 cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/data-visualization-2.1.pdf) helpful. 

Note that for more advanced plots or plot options, you may need to look for a stackoverflow thread or consult another resource. 

### B.1. Combining ggplot plots 

As shown in the analysis folder, there are multiple packages that we can use to combine ggplot plots: 

1. `grid` and `gridExtra` packages - learn more about using these packages by looking at the examples in [this vignette](https://cran.r-project.org/web/packages/egg/vignettes/Ecosystem.html) and on [this webpage](http://edrub.in/ARE212/section08.html). 
2. `patchwork` package - learn more about using this package by looking at the examples in [this vignette](https://gotellilab.github.io/GotelliLabMeetingHacks/NickGotelli/ggplotPatchwork.html).

As a rule of thumb, `patchwork` is a newer package and easier to use (it uses syntax similar to ggplot2). The older `gridExtra` package is slightly less intuitive, but may be more flexible, especially when it comes to adding labels to the combined plot. 

### B.2. More themes 

`ggthemes` contains additional themes for ggplot. More information can be found [here](https://mran.microsoft.com/snapshot/2016-12-03/web/packages/ggthemes/vignettes/ggthemes.html). 

### B.3. Other misc resources

To change the text and order of categorical labels, consider converting character variables to factor variables (but remember that having factors at earlier stages can create problems!). See this [factor cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/factors.pdf) for help making or editing factor variables. 

When possible, use tidyverse to load and transform data as well
* [Import data](https://github.com/rstudio/cheatsheets/blob/master/data-import.pdf) using readr and other packages.
* Modify data with [dplyr](https://github.com/rstudio/cheatsheets/blob/master/data-transformation.pdf) or [tidyr](https://github.com/rstudio/cheatsheets/blob/master/data-import.pdf).
* Loop through data using the `map()` function from [purr](https://github.com/rstudio/cheatsheets/blob/master/purrr.pdf)

To get robust OLS estimates and CI, consider using `lm_robust()` from the `estimatr` package ([cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/estimatr.pdf)). 

You can use the [gganimate](https://github.com/thomasp85/gganimate) package to animate plots ([cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/gganimate.pdf))

To use unique shapes as background images or points, see [Add silhouettes with rphylopic](https://github.com/rstudio/cheatsheets/blob/master/rphylopic.pdf).

## C. Base R

In general, plan to use `ggplot2` and `tidyverse` packages to make plots for presentations and papers. However, sometimes you will need to use base R plot functions. For example, some packages like `rdrobust` have plotting functions that are built on base r instead of ggplot. 

If you ever need to make a plot using base R, the following resources may be helpful... 
* [Base R plot margins/spacing cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/how-big-is-your-graph.pdf)
* [Base R cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/base-r.pdf)


## D. Mapping in R

[Geocomputation with R](https://geocompr.robinlovelace.net/) by Robin Lovelace, Jakub Nowosad, Jannes Muenchow is an excelent and in-depth discussion of mapping in R. 
* It goes through many advanced mapping techniques including [animated maps](https://geocompr.robinlovelace.net/adv-map.html#animated-maps) and [interactive maps](https://geocompr.robinlovelace.net/adv-map.html#interactive-maps). 
* The book references scripts with example code which can be found [here](https://github.com/Robinlovelace/geocompr/tree/master/code).

You might also want to check out Ed Rubin's website ([page 1](http://edrub.in/ARE212/section12.html) and [page 2](http://edrub.in/ARE212/section13.html)).

Other resources: 
* [leaflet cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/leaflet.pdf) -- note `leaflet` is package used for making interactive plots, see [section 8.4](https://geocompr.robinlovelace.net/adv-map.html#interactive-maps) of [Geocomputation with R](https://geocompr.robinlovelace.net/) for more details. 


### D.1. `sf` plotting

Recall that plotting in R uses either the `sp` or `sf` framework. The code for this course relies more heavily on `sp` plotting, but you may want to use the newer `sf` instead. 

The `sf` (simple feature) package ([documentation here](https://cran.r-project.org/web/packages/sf/sf.pdf)) is a newer (but sometimes slower) method of mapping in R ([cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/sf.pdf)). 

More resources for sf mapping can be found here: 
* [https://cran.r-project.org/web/packages/sf/vignettes/sf1.html](https://cran.r-project.org/web/packages/sf/vignettes/sf1.html)
* [http://strimas.com/r/tidy-sf/](http://strimas.com/r/tidy-sf/)
* [https://r-spatial.github.io/sf/](https://r-spatial.github.io/sf/)
* [https://ggplot2.tidyverse.org/reference/ggsf.html](https://ggplot2.tidyverse.org/reference/ggsf.html)
* [https://dcl-2017-01.github.io/curriculum/notes/spatial-vis.html](https://dcl-2017-01.github.io/curriculum/notes/spatial-vis.html)

For more information about the difference between `sp` and `sf`, see ["Should I learn sf or sp for spatial R programming"](https://www.r-bloggers.com/should-i-learn-sf-or-sp-for-spatial-r-programming/). 

Note that some packages now allow you to download `sf` spatial data in addition to the data that you are mapping. For example...
* `tidycensus` ([github repo](https://github.com/walkerke/tidycensus)) - add the "geometry=TRUE" argument to `tidycensus::get_decennial()` or `tidycensus::get_acs()`
* `eurostat` ([cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/eurostat.pdf)) - run `eurostat::get_eurostat_geospatial()` and merge with output from `eurostat::get_eurostat()`


## E. Misc Other

[Ways to change plot size in Rmarkdown documents](https://sebastiansauer.github.io/figure_sizing_knitr/). 
