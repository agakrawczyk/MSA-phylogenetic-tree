# MSA-phylogenetic-tree
It is a small pipeline for alignment and drawing the phylogenetic tree from the file containging sequnces in fasta format.  
### Requirements 
To use it some tools need to be instaled:

-[Biopython](http://biopython.org/wiki/Biopython)

-[matplotlib](http://matplotlib.org)

-[MUSCLE](http://www.drive5.com/muscle/)

-[FastTree](http://meta.microbesonline.org/fasttree/)

-[Python 3.5.1.](https://docs.python.org/3/) 

### How to run 
The exe files of both MUSCLE and Fast Tree should be in the same repository. 

The input file has to be a single file with sequences in fasta format ( starting with ">"). 

( eg. >Brachylophosaurus_canadensis
GATGAPGIAGAPGFPGARGPSGPQGPSGAPGPKGVQGPPGPQGPRGLTGPIGPPGPAGAPGDKGEAGPSGPPGPTGARGS
AGPPGATGFPGAAGRGETGPAGPAGPPGPAGAR)

The treshold for the not aligned positions is set to 2, however it can be changed here :
```javascript 
not_aligned_positions = []
        for i in range(len(seq)):
            counter = 0
            for name, sequence in fasta_dict.items():
                if '-' in sequence[i]:
                    counter += 1

            if counter > 2:
                not_aligned_positions.append(i)
                
                

                

