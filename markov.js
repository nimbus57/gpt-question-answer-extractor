// markov text generator
// take some input text and train on it
// read in the text - parse it - for each word pair, add it to an accumulator in a set
//      so, (1,2,3) => [(1,2), (1,3), (2,3)]


// input text - start with a five hundred word snippet to train on
// easiest delimiter is just on space, but this makes the end result wors
// choose a look forward amount: one - essentially a lookup table
// start with an input word, limited to something in the text
// you randomly select the next word based on  