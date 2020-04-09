# Resources for R 

Note: more resources for data visualization in R can be found in the data visualization lecture subfolder. 

## The Internet 

When you have a problem, google it! Pay special attention to any StackOverflow links in the search results. 

> *Tip:* before googling, figure out if you are using a tidyverse package like dplyr. If so, include the name of the package in your google search. For example, if you can't figure out how to add a variable to a dataframe, search "R add variable dataframe dplyr" or "R add variable dataframe tidyverse". 

### Miminal reproducible example 

Chances are you're going to use StackOverFlow a lot to solve a pressing problem you face. However, other can't understand/be interested in your problem unless you can provide an example which they can understand with minimal efforts. Such example is called a minimal reproducible example. 

Read [this StackOverFlow post](https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example) to understand the concept and best practices.

Simply put, a MRE consists of the following items:

- A minimal dataset 
- the minimal burnable code
- the necessary information on package, R version, system (use sessionInfo())
- (for random process) a seed for reproducibility (set.seed())


## Berkeley Initiatives 

[D-lab](https://dlab.berkeley.edu/): initiative includes working groups, free consulting, trainings, and other resources for learning data science tools 
* D-lab's training materials can be found on its [GitHub page](https://github.com/dlab-berkeley).
* [Link](https://github.com/dlab-berkeley/R-Fundamentals) to D-Lab's R Fundementals course materials. 

[Digital Humanities](http://digitalhumanities.berkeley.edu/): Digital Humanities at Berkeley supports the thoughtful application of digital tools and methodologies to humanistic inquiry by offering project consulting, summer workshops, grants, etc.


## Useful Websites

### Reference guides

[Quick-R](https://www.statmethods.net/index.html): basic syntax and base R functions

[tidyverse.org](https://www.tidyverse.org/): tidyverse packages like dplyr, ggplot2, readr, tibble, tidyr, and purr

[rdrr.io](https://rdrr.io/): better-formatted version of R package documentation; for some packages, also shows source code. 

[Rmarkdown](https://kbroman.org/knitr_knutshell/pages/Rmarkdown.html): basic RMarkdown options

[Cookbook for R](http://www.cookbook-r.com/Graphs/): great ggplot2 reference 


### Resource lists

Anything on Ed Rubin's website. Until recently, Ed Rubin was a grad student and GSI in the agricultural economics department at Berkeley. His website includes a running list of [useful software](http://edrub.in/links.html) and a list of [R resources](http://edrub.in/ARE212/resources.html). 

Dan Nguyen's ["Best and free R-language resources shortlist"](http://blog.danwin.com/best-and-free-r-language-resources/).



### Other sites

Ed Rubin's [Spring 2918 section notes](http://edrub.in/ARE212/index.html): excellently organized and commented R code as well as useful tricks for analyzing data in R

The [tidytusday project](https://thomasmock.netlify.com/post/tidytuesday-a-weekly-social-data-project-in-r/) [project](https://github.com/rfordatascience/tidytuesday): weekly social data project focused on using tidyverse packages to clean, wrangle, tidy, and plot data; see also 
* Sara Stoudt's tidytuesday posts can be found [here](https://sastoudt.github.io/tidytuesday/).
* The [tidytuesday GitHub page] includes links to tidytuesday posts and datasets as well as a list of resources for learning R

[Rebecca Barter's blog](http://www.rebeccabarter.com/blog/) has numerous articles about tidyverse and efficient R programming. 

Hadley Wickham’s Advanced R](http://adv-r.had.co.nz/): covers advanced programming topics; especially useful when writing functions or packages

[Efficient R programming](https://csgillespie.github.io/efficientR/) by Colin Gillespie and Robin Lovelace

[R-bloggers](https://www.r-bloggers.com/)


## Vignettes

Per [r-project.org](https://www.r-project.org/help.html):

> Many packages include vignettes, which are discursive documents meant to illustrate and explain facilities in the package. You can discover vignettes by accessing the help page for a package, or via the browseVignettes() function: the command browseVignettes() opens a list of vignettes from all of your installed packages in your browser, while browseVignettes(package=package-name) (e.g., browseVignettes(package="survival")) shows the vignettes, if any, for a particular package. vignette() is employed similarly, but displays a list of vignettes in text form.
> 
> You can also use the vignette("vignette-name") command to view a vignette (possibly specifying the name of the package in which the vignette resides, if the vignette name is not unique): for example, vignette("timedep") or vignette("timedep", package="survival") (which are, in this case, equivalent).
> 
> Vignettes may also be accessed from the CRAN page for the package (e.g. survival), if you wish to review the vignette for a package prior to installing and/or using it.
> 
> Packages may also include extended code demonstrations (“demos”). The command demo() lists all demos for all packages in your library, while demo(package="package-name") (e.g., demo(package="stats")) lists demos in a particular package. To run a demo, call the demo() function with the quoted name of the demo (e.g., demo("nlm")), specifying the name of the package if the name of the demo isn’t unique (e.g., demo("nlm", package="stats"), where, in this case, the package name need not be given explicitly).

Example(s):
* [dplyr](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html)


## Cheat Sheets 

RStudio produces and publishes 'cheat sheets' covering a wide variety of subjects. The full set can be found [here](https://www.rstudio.com/resources/cheatsheets/) (see also the RStudio GitHub page [here](https://github.com/rstudio/cheatsheets)).

Julia's favorite cheatsheets include: 
* [Manipulating strings with stringr](https://github.com/rstudio/cheatsheets/blob/master/strings.pdf).
* [Date variables with lubridate](https://github.com/rstudio/cheatsheets/blob/master/lubridate.pdf).

Some useful cheatsheets for navigating baser and our programming environment: 
* [Base R](https://github.com/rstudio/cheatsheets/blob/master/base-r.pdf).
* [R Markdown](https://github.com/rstudio/cheatsheets/blob/master/rmarkdown-2.0.pdf).
* [R Studio](https://github.com/rstudio/cheatsheets/blob/master/rstudio-ide.pdf).
* [R Syntax Comparison](https://github.com/rstudio/cheatsheets/blob/master/syntax.pdf)

The following cheatsheets cover important tidyverse packages: 
* [Importing data with readr](https://github.com/rstudio/cheatsheets/blob/master/data-import.pdf).
* [Data transformation with dplyr](https://github.com/rstudio/cheatsheets/blob/master/data-transformation.pdf).
* [Data visualization with ggplot2](https://github.com/rstudio/cheatsheets/blob/master/data-visualization-2.1.pdf).

These cheatsheets are useful for manipulating text data:
* [Regular expressions](https://github.com/rstudio/cheatsheets/blob/master/regex.pdf).
* [Manipulating strings with stringr](https://github.com/rstudio/cheatsheets/blob/master/strings.pdf).
* Manage and analyze text data using the [quanteda package](https://github.com/rstudio/cheatsheets/blob/master/quanteda.pdf)

If you are doing machine learning or using big data, check out the following: 
* For important and manipulating large datasets, see [Data transformation with data.table](https://github.com/rstudio/cheatsheets/blob/master/datatable.pdf).
* For information about parallel computing in R, see [Parallel Computing](https://github.com/rstudio/cheatsheets/blob/master/parallel_computation.pdf).
* Machine learning in R using [mlr](https://github.com/rstudio/cheatsheets/blob/master/mlr.pdf)
* Deep learning in R using [keras](https://github.com/rstudio/cheatsheets/blob/master/keras.pdf)

Other useful cheatsheets include:
* For manipulating factor variables, use either baser functions or see [Factors with forecats](https://github.com/rstudio/cheatsheets/blob/master/factors.pdf).
* For functions to randomize experiments, see [randomizr](https://github.com/rstudio/cheatsheets/blob/master/randomizr.pdf)
* For embedding python code in R, see [Using Python with R with reticulate](https://github.com/rstudio/cheatsheets/blob/master/reticulate.pdf)
* If you are familiar with Stata, check out [Stata to R](https://github.com/rstudio/cheatsheets/blob/master/stata2r.pdf). 











## (Free) Interactive Tutorials 

RStudio has also started publishing [interactive tutorials](https://rstudio.cloud/learn/primers). These tutorials are similar to the ones that you've been assigned in DataCamp, but they will remain available to you after the end of this semester. 

`swirl` is a package that turns the R console into an interactive learning environment. More information can be found on the [swirl website](https://swirlstats.com/). 


## Related Topics 

### RMarkdown 

[R Markdown: The Definitive Guide](https://bookdown.org/yihui/rmarkdown/) by Yihui Xie, J. J. Allaire, Garrett Grolemund.

### Markdown 

Most of the text outside of code chunks in RMarkdown documents uses markdown syntax. More information about markdown can be found [here](https://daringfireball.net/projects/markdown/). 

For help with markdown syntax, see [this cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

To create a markdown document like this one, just open a text editor (i.e. Notepad on Windows or TextEdit on a Mac) and add '.md' at the end of your file name. 

### LaTeX 

To write equations in an RMarkdown document, you can use LaTeX syntax. However, note that this feature tends to be buggy.

Useful links: 
* [Detexify](http://detexify.kirelabs.org/classify.html): looks up LaTeX command that matches a shape that you have drawn using your mouse. 
* [List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols): good reference if you detexify doesn't find the symbol that you want 
* [https://mathpix.com/](https://mathpix.com/): generates LaTeX code based on pictures of equations from class notes, textbook, etc.









