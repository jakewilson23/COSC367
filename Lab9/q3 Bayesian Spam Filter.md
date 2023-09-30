## Bayesian Spam Filter
In the next three questions, you are asked to develop the learning and classification components of a naive Bayes classifier (a spam filter).

The file spam-labelled.csv describes 200 emails, labelled as spam or non-spam by human users. Each email is specified by 12 binary attributes, indicating the presence of features such as “Lottery”, “MILLION DOLLARS”, significant amounts of text in CAPS, an invalid reply-to address, and so on.

The layout of the data is that each row is an example (one email), and columns correspond to attributes (features), which are binary. There are 12 input features (X1 to X12). The last (right-most) column is the class label where 1 means the example is spam (positive) and 0 means non-spam (negative). 

Note that there are 2^12 =4096 possible input patterns; in other words, the data set only contains a small proportion of all possible input patterns. This is a common scenario in machine learning.

The file has Unix-like line breaks. Windows users need to open the file in a proper text editor that supports different line endings. You do not need a spreadsheet to open the file.

In Python, the csv module may come in handy. You can load the content of the file as a list of tuples using the following:

``` Python
with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
```
In the next three questions, the above file is available on the server (in the current directory). Therefore a statement like the one above, would read the file. Your function will be tested on the same file format and header but the content (the examples) may vary. Make sure your solution works with the original copy of the file, not your own format.