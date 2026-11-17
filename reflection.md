# Reflection – XeroxFlow

## What I Got Wrong at the Start

At first I thought that predicting rush hours would be as simple as just counting the number of customers at the photocopy shop. As I got a bit deeper into the problem though, I realised that the number of customers isn't necessarily a good indicator of the actual amount of work that's being done. A customer who wants 100 pages printed is going to keep a printer busy for a lot longer than a customer who just wants a few copies. That changed my approach and I started to look at print volume as well as queue length.

## What I Would Cut

If I'd had any more time I initially wanted to go down the route of building a rather complex dashboard with a whole host of features. What I quickly realised was that the primary purpose of this was to be of use to the shopkeeper. I'd strip away all the unnecessary visualisations and concentrate much more on the actual workload estimation, peak hour identification and the practical recommendations.

## Where AI Helped

AI helped me work out how to structure the project, how to organise the CSV data, how to write the Python code and what the various approaches to the analysis of customer traffic might be. It was also very useful in helping me to debug errors and improve the structure of the code in general which in turn saved a lot of development time.

## Where AI Wasted Time

On occasion the AI would suggest features and solutions that were in fact far more complex than this small business actually required. I also had to go through the generated code very carefully as it was likely to be based on assumptions (e.g. printer tray capacity, paper consumption etc) that wouldn't necessarily be in line with the actual way the shop operated.

## Final Learning

This project taught me that if you're going to solve a real world problem you need to understand the people you're solving it for before you write a line of code. A simple tool based on what you actually observe in the field is going to be far more useful than a complex application built on a whole bunch of assumptions.