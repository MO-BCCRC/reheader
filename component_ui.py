'''
Created on Jun 10, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='reheader',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This script is used to change the header of a bam file
                   it uses picard tool AddOrReplaceReadGroups to add information
                   in the bam header. This is required if we want to use the bam file
                   with a utility from GATK''')

# required arguments
parser.add_argument('--infile', metavar='INPUT',
                    help='A BAM file to be reheaded')

parser.add_argument('--outfile', metavar='OUTPUT',
                    help='Reheaded BAM file')

args, x = parser.parse_known_args()
