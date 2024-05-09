class pytesting:
    
    gene_num = [];
    gene_name = [];
    pcor_all = [];
    pcor_sampling_num = [];
    coexpressed_cell_num = [];
    samples_num = [];
    RoundNumber = [];
    SigEdges = [];
    
    def __init__(self, round_num ):
        
        print('Calculating pcor in %d iterations.\n' %round_num)
