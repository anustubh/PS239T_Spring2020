
# Big Data

## 1. Sequential vs. Parallel Processing 

In order to process really large datasets, you will almost certainly need to use parallel processing. While parallel processing is a powerful tool, it is not always an option. 

**Sequential processing:** Alternatively referred to as serial processing, sequential processing is a term used to describe the processing that occurs in the order that it is received. Sequential processing is in contrast to parallel processing or multitasking.

**Parallel procesing:** Parallel processing is the method of evenly distributing computer processes between two or more computer processors. This requires a computer with multiple CPUs, or a CPU (or GPU) equipped with multiple cores. It also requires an operating system capable of supporting parallel processing, or software written specifically to process tasks in parallel.

Source: https://www.computerhope.com/jargon.htm

> Sidenote: You may also hear the term multi-thread processing. For our purposes, the distinction between parallel processing and multi-thread processing isn't critical. 

For information about parallel computing in R, see this [cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/parallel_computation.pdf).


## 2. Hardware 

For our purposes, the two most important pieces of hardware are the **processor/CPU** and the **short-term memory/RAM**. 

> Sidenote: Files (e.g. R data files, csv files, this file, etc.) are stored on your computer's harddrive. Computers either have hard disk drives (HDD) or solid state drives (SSD). Saving your OS on a SSD is faster than an HDD; however, reading data into R from an SSD or an HDD usually does not have a large effect on speed. If you don't have enough long-term memory for a file, you certainly don't have enough RAM. Getting more long-term memory will be much cheaper to solve than getting more RAM or a faster CPU. 

Open up your task manager. Use interface to look at your CPU and RAM. Note the speed and how many cores/processors you have under the CPU information. Note how many GB of RAM you have available and in use. 

Your RAM will limit how large of files you can load into R. To manipulate data in R, it must be loaded into memory (RAM). The size of your RAM limits the size of files you can manipulate in R at one time.  

The CPU processes all of our code and determines how fast the code can run. However, not all code is equal. To anticipate how long something takes to run, you need to know whether your program is running sequentially or parallel. Most R packages run sequentially. 
* Modern CPUs seem to be emphasizing the number rather than the speed of cores. For parallel computing, this makes sense. However, for most of our R code, we want faster cores more than we want more cores. 

> Sidenote: To implement parallel processing in R, google 'parallel processing in R' and look for a recent vignette, blog post, or stack overflow post. The packages have changed over the last few years and will likely continue to change if parallel processing becomes more popular in R. 


## 3. General tips for using big data 

Doing analysis with big data (i.e. data that does not fit onto your computer or cannot be analyzed on your computer) is complicated. In general...

1. Get started early! Expect it to take weeks to set up and longer to learn how to use. Large data requires a completely new set of skills and requires learning more about hardware as well as software. 
2. Get in contact with D-Lab.  
3. Remember that the terminal (/bash) is your friend. Use bash to split up, sample, filter, etc. your data before trying to load it into R. 

Here are some important questions to ask:

1. Can the data be stored on your computer or an external hard drive?
	* For most political science research, the answer is yes. Analyzing the data is almost always harder than storing it. 
	* Computers either have hard disk drives (HDD) or solid state drives (SSD). SSD drives are physically, smaller, more expensive, and faster than HDDs. If you have an SSD, you probably have under 500 GB of memory, but this should be enough for most analysis. For context, the CA voterfile is about 50 GB unzipped and has 20 million + rows. 
	* A related Q is what kind of protection/security you need. If you are using a proprietary dataset or one that cannot be loaded onto the internet, you need to be more careful. 
	* Datasets below a certain size can be uploaded to github.
	* UC users have a large amount of storage space available using Box. 
	* External hard drives are fairly cheap. 
	* If possible, split up file and zip to save storage space. Unzip only when you are using the file (there are functions in R to unzip and delete unzipped files after loading dataset). 
2. Can the data be loaded into memory?
	* This depends on how you plan on analyzing your data.
	* R has to load the whole dataset into memory (RAM) in order to perform an analysis.
	* Most laptops have 4-16 GB or RAM. You can only load a dataset that is as large as your RAM. True computer scientists can have access to massive amounts of RAM. 
	* For some types of analysis (i.e. calculating totals), you can load part of the dataset into memory, run the analysis for that part, save the result, and then load a new piece of the dataset and repeat. 
	* If you're analysis can be broken up, you should also look into parallel processing. 
	* Using distributed computing options and supercomputers usually requires parallel processing. These systems complete large tasks by splitting them up and running them at the same time across many smaller computing environments. 
3. How much security do you need? 
	* Some data privacy contracts prohibit certain kinds of storage and analysis options (often web-based ones). 
4. How 'computationally expensive' is your project?
	* Projects that require more RAM and processing speed/power are considered computationally expensive. You'll need to think about RAM and processor limitations. 
	* If you have a highly computationally expensive project, you will probably need to split up your data in order to analyze it. Talk to D-Lab and other researchers who are doing something similar about how to split up your analysis. 
 

Finding the right solution for each project will depend on a number of factors, but here are a few notes: 

* Faculty have access to resources that they usually aren't using. They are often willing to let you use their quota on various resources. 
* Many Web-based Platforms have Grant Options:
	* Amazon web services (AWS): https://aws.amazon.com/grants/ (Links to an external site.)
	* Google cloud: https://cloud.google.com/edu/ (Links to an external site.)
* You can pay for relatively cheap and secure virtual servers through Berkeley: https://pi.berkeley.edu/homeLinks to an external site.
* Building a desktop can be the cheapest option, especially if you are planning to run code sequentially. 


