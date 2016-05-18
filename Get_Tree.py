import subprocess
from Bio import Phylo
from matplotlib import pyplot as plt
import argparse


class GetTree(object):

    def __init__(self, muscle_exe, infile, outfile, fast_tree_exe, edited_file, tree_file):
        """
        Constructor run with path to ini file with settings.
        :param muscle_exe: MUSCLE exe file
        :param infile: single file with sequences in fasta format
        :param outfile: file with aligned sequences (MUSCLE output)
        :param fast_tree_exe: the exe file of Fast Tree program
        :param edited_file: alignment file after editing
        :return tree_file : phylogenetic tree file in 'newick' format
         """

        self.muscle_exe = muscle_exe
        self.infile = infile
        self.outfile = outfile
        self.fast_tree_exe = fast_tree_exe
        self.edited_file = edited_file
        self.tree_file = tree_file

    def run_muscle(self):
        """
        Runs MUSCLE program that aligns the sequences given in the single file in the fasta format.
        """

        subprocess.call([self.muscle_exe, "-in", self.infile, "-out", self.outfile])

    def edit_alignment(self, cutoff_value):
        """
        Edits the alignment file to get rid of too many not aligned positions.
        :param cutoff_value: the maximum value of the lines without alignment
        """

        fasta_dict = {}
        species = ""
        seq = ""

        with open(self.outfile, "r") as f:
            for line in f:
                line = line.rstrip()
                if line.startswith('>'):
                    if species != "":
                        fasta_dict[species] = seq
                    species = line[1:]
                    seq = ""
                else:
                    if line != "":
                        seq += line
            fasta_dict[species] = seq

        print('Done!', len(fasta_dict), 'sequences')

        not_aligned_positions = []
        for i in range(len(seq)):
            counter = 0
            for name, sequence in fasta_dict.items():
                if '-' in sequence[i]:
                    counter += 1

            if counter > cutoff_value:
                not_aligned_positions.append(i)

        with open(self.edited_file, 'w') as f:
            for name, sequence in fasta_dict.items():
                edited_seq = ''
                for i in range(len(seq)):
                    if i not in not_aligned_positions:
                        edited_seq += sequence[i]
                print('>' + name, edited_seq, sep='\n', file=f)

    def run_fasttree(self):
        """
        Runs Fast Tree program using the edited alignment file and creates a phylogenetic tree
        from the edited alignment file.
        """

        with open(self.tree_file, "w") as f:
            fasttree_output = subprocess.check_output([self.fast_tree_exe, self.edited_file]).decode('utf-8')
            print(fasttree_output, file=f)

    def draw_tree(self):
        """
        Draws the phylogenetic tree from the tree file in 'newick' format.
        """
        tree = Phylo.read(self.tree_file, 'newick')

        Phylo.draw(tree)
        plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('infile', help='File in sequences in fasta format for alignment')
    parser.add_argument('outfile',  help='Muscle output file, alignment in fasta format')
    parser.add_argument('edited_file',  help='Alignment file after editing')
    parser.add_argument('tree_file',  help='Fast Tree output file, used to generate the phylogenetic tree')

    parser.add_argument('--muscle_exe', default="external/muscle3.8.31_i86win32.exe",
                        help='Muscle file to run the program ')
    parser.add_argument('--fast_tree_exe', default="external/FastTree.exe",
                        help='Fast Tree file to run the program')
    parser.add_argument('--cutoff_value', default=2, type=int,
                        help='It is the maximum value of the lines without alignment, have to int')

    args = parser.parse_args()

    param = GetTree(args.muscle_exe, args.infile, args.outfile, args.fast_tree_exe, args.edited_file, args.tree_file)

    param.run_muscle()
    param.edit_alignment(args.cutoff_value)
    param.run_fasttree()
    param.draw_tree()
