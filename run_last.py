__author__ = 'flashton'

import os

# reference = '/Users/flashton/Dropbox/H58_minion/data/refs/ST2_contigs'
# query = '/Users/flashton/Dropbox/H58_minion/data/H566_ON/2014.08.11.H566_ON_both.fasta'
# outhandle = '/Users/flashton/Dropbox/H58_minion/results/H566_ON/2014.08.11.H566_ON_both_vs_ST2_contigs'

def run_last(reference, query, outdir):
    reference_path = os.path.splitext(reference)[0]
    reference_name = os.path.basename(reference_path)
    query_name = os.path.splitext(os.path.basename(query))[0]
    print '### indexing reference for last alignment ###'
    os.system('lastdb -Q 0 %s.lastindex %s' % (reference_path, reference))
    print '### LAST is aligning the query against the reference ###'
    os.system('lastal -s 2 -T 0 -Q 0 -a 1 %s.lastindex %s > %s/%s_vs_%s.last.txt' % (reference_path, query, outdir,
     query_name, reference_name))
    print '### converting the last format to blast format using maf-convert.py ###'
    os.system('maf-convert.py blast %s/%s_vs_%s.last.txt > %s/%s_vs_%s.blast.txt' % (outdir, query_name, reference_name, outdir,
                                                                                   query_name, reference_name))


