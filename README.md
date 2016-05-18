# MSA-phylogenetic-tree
It is a small pipeline for alignment and drawing the phylogenetic tree from the file containging sequnces in fasta format.  
### Requirements 
To use it some tools need to be instaled:

-[Biopython](http://biopython.org/wiki/Biopython)

-[matplotlib](http://matplotlib.org)

-[MUSCLE](http://www.drive5.com/muscle/)

-[FastTree](http://meta.microbesonline.org/fasttree/)

-[Python 3.5.1.](https://docs.python.org/3/) 

### Instalation 

Git can be used to get the copy of the code and example:

https://github.com/agakrawczyk/MSA-phylogenetic-tree.git

### How to run 
The exe files of both MUSCLE and Fast Tree should be in the same repository. 

The input file has to be a single file with sequences in fasta format ( starting with ">"). 

( eg. >Brachylophosaurus_canadensis
GATGAPGIAGAPGFPGARGPSGPQGPSGAPGPKGVQGPPGPQGPRGLTGPIGPPGPAGAPGDKGEAGPSGPPGPTGARGS
AGPPGATGFPGAAGRGETGPAGPAGPPGPAGAR)

For the edition of the file the treshold for the not aligned positions in alignment file obtained from MUSCLE is set to 2, however it can be changed in the arguments - cutoff_value. 
                
                

                

