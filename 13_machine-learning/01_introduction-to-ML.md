# Machine Learning 

## What is Machine Learning (ML)?

Most basic Machine Learning (ML) concepts are not alien to those of us who have studied statistical modeling. The core concepts often overlap with regularly used statistical techniques like OLS, GLS, survey index construction, etc. -- although note that the ML community sometimes uses different terminology, which can obscure the relationship between ML and conventional statistics. 

### Defining ML

Per Wikipedia, 
> Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to carry out tasks without explicit instructions, such as by using pattern recognition and inference. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, where it is difficult or infeasible to develop conventional algorithms to perform the needed tasks. 
(source: wikipedia page for Machine Learning as of 4/8/2020, [link](https://en.wikipedia.org/wiki/Machine_learning))

Note that terminology can obscure how much basic ML concepts differ from those used in conventional statistical modeling. Core ML concepts often overlap with regularly used statistical techniques like OLS, GLS, survey index construction, cross-validation, etc.

### Key(s) to understanding ML

The key to understanding ML is to understand its purpose: **prediction.**
* Most classical social science statistical techniques can be used for *prediction* or *explanation*.
* In contrast, ML is (almost) exclusively used for *prediction* only. 

> Note that in political science, we are usually interested in explanation, so ML techniques are often most useful for categorizing/cleaning data.  

To understand ML, it is also useful to recognize that most of the funding for ML research is from the private sector. 
* In general, companies are more interested in prediction than explanation (making money is more important than why you are making money).
* Companies often have access to massive datasets. 
* Less culture of peer review and rapid growth of the knowledge base. 


## How is ML used in political science?

Common political science applications include 
* Categorization 
* Matching 
* Predicting outcomes (e.g. election outcomes, gerrymandering, etc.)


## Branches of ML

There are two (canonical) branches of ML. 
1. Supervised
2. Unsupervised

### 1. Supervised ML

Supervised ML methods try to use input variables (IV) to predict an outcome variable (DV). 

Supervised ML is similar to using cross-validation to check for model overfit. The basic procedure involves the following... 
* split data into training and testing groups
* fit models that are 'good' in training dataset
* test whether model 'goodness' using (out-of-sample) testing data 

Supervised ML requires making several important design choices, including: 
* How to judge whether a model is 'good' and threshold of acceptable 'goodness' (aka what are we optimizing)?
* What models to test?
* How to compare performance and determine final result?

Examples of Supervised ML: 
* Image recognition and categorization (e.g. identifying photos of a particular type of object like street signs or cars).
* OCR (turning images of documents into computer-readable text)
* Scaling-up hand-coded categories 

|Pros						| Cons   					|
|---						|---						|
| - clearer interpretation of categories  	| - (usually) more expensive			|
| - usually trusted more than unsupervised ML  	| - depends on unbiasness of training dataset	|
| - researcher has more control over coding  	|   						|



### 2. Unsupervised ML 

Unsupervised ML methods try to identify patterns in the data using only input (IV) variables. In other words, they use input variables to identify rather than predict outcome variables. 

Note that there may be a number of methods in social science that use unsupervised methods but are not called ML like ideological scaling or index construction. 

Two main methods: (a) Principle component analysis (PCA) and (b) Cluster analysis. 

(a) Principle component analysis (PCA) 
* closely related to factor analysis 
* create new variables (using all variables) that are linearly uncorrelated

(b) Cluster analysis 
* group observations such that objects in the same group are more similar to each other than to other groups 
* see Tim's network analysis code for examples 

Examples of Unsupervised ML: 
* Topic modeling 
* Dimension reduction (e.g. index/scale construction)

|Pros							| Cons   							|
|---							|---								|
| - human biases not imposed on coding (in theory)  	| - results can be highly sensitive to (arbitrary) choices 	|
| - cheap and fast to implement				| - often unclear how to interpret results			|
| - can help solve high-domensional data problems  	|   								|


For more information about using unsupervised ML to analyze text data, see the following paper: Grimmer, J., & Stewart, B. M. (2013). Text as data: The promise and pitfalls of automatic content analysis methods for political texts. Political analysis, 21(3), 267-297. [link](https://web.stanford.edu/~jgrimmer/tad2.pdf).


## Importance of Pre-processing Decisions 

*Different dataset construction decisions can completely change the results of your analysis.* 

Most ML techniques do not generate variables; they work with the variables that you create during the pre-processing stage. If so, you will need to first decide how to convert unstructured raw data like text, image, or sound into a structured dataset with defined variables. 

Example: text data
* What is your unit of analysis? Documents? Pragraphs? Sentences? 
* Do you create variables for each word? What about special characters, sequences of words, sentence synax? Do any of these attributes matter? If so, do they need to be coded? 
* What complexity can be stripped away? 


## Other Misc. Thoughts

Historically, variance and significance calculations have not been a priority of ML research.


## Resources

Check out the following cheatsheets: 
* Machine learning in R using [mlr](https://github.com/rstudio/cheatsheets/blob/master/mlr.pdf)
* Deep learning in R using [keras](https://github.com/rstudio/cheatsheets/blob/master/keras.pdf)

Since ML often involves big data, the following cheatsheets may also be helpful: 
* For important and manipulating large datasets, see [Data transformation with data.table](https://github.com/rstudio/cheatsheets/blob/master/datatable.pdf).
* For information about parallel computing in R, see [Parallel Computing](https://github.com/rstudio/cheatsheets/blob/master/parallel_computation.pdf).