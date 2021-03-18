## New Words Extractor

The script will open the existing dictionary and news input and generate new words.

# Issues

1.  The news only has 11458 words which are relatively small. Tunning parameters could largely affect the number of new words generated. 

    While setting min_aggregation to 50 is quite reasonable, 0.1 increment of entropy can double the new words. 

    Increasing both parameters can eliminate both good new words and bad words.  

# Ideas

Base on information from the original article, the script should reach higher efficiency when more words included. And tuning parameters shouldn't largely affect the words generated.

One solution I can think of is: 

    a. Extract new words from the original news, with relatively lower values of min_aggregation and min_entropy. The purpose is to catch all real new words but not shown frequently; 

    b. Fetch more news under the same topic and generate a bigger set of new words. This set should have much higher accuracy;

    c. Crossmatch the two sets, filter out words that didn't show in the bigger set. 
