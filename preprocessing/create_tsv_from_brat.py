import os

def create_tsv_for_relation_classification(input_dir, output_file):
    """
    Function to create a tsv file with random negative samples from corpus.
    :param input_dir: directory with .txt and .ann files
    :param output_file: tsv file to write the output to
    :return: None
    """


    for f in os.listdir(input_dir):
        if '.ann' in f:
            links = {}
            relations = {}
            components = {}
            useful_pairs = []
            useless_pairs = []
            f_name = f[:-4]
            print("Name of the file: ", f_name)
            # open ann file and get components and relations
            with open(input_dir + f_name + '.ann', 'r', encoding='utf-8') as fann:
                lines = fann.read().splitlines()
                for line in lines:
                    line = line.split('\t')
                    
                    if 'T' in line[0]:
                        components[line[0]] = line[2].replace('\n', '')
                    elif 'R' in line[0]:
                        rel = line[1].split()[1:]
                        links[rel[0][5:]] = rel[1][5:]
                        relations[rel[0][5:]] = line[1].split()[0]
            
            assert len(relations.keys()) == len(links.keys())
            
            for c_i in components.keys():
                for c_j in components.keys():
                    if c_i == c_j:
                        continue
                    elif c_i in links.keys() and c_j == links[c_i]:
                        useful_pairs.append('__label__'+relations[c_i] + '\t' + components[c_i] + '\t' + components[c_j])
                    else:
                        
                        if c_i in list(links.values()) or c_j in links.keys() or c_j in list(links.values()) or c_i in links.keys():
                            useful_pairs.append('__label__noRel\t' + components[c_i] + '\t' + components[c_j])
                        else:
                            useless_pairs.append('__label__noRel\t' + components[c_i] + '\t' + components[c_j])                                                            
            
            with open(output_file + '.tsv', 'a', encoding='utf-8') as fout:
                for pair in useful_pairs:
                    fout.write(pair + '\n')
                    
            print("Useful lines: ", len(useful_pairs))
            print("Useless lines: ", len(useless_pairs))
                    

def main():

    #input_dir = '../data/glaucoma_test/glaucoma/'
    input_dir = '/Users/pgoffred/Documents/CompRelDetection/brat2CoNLL-main/output/val/'
    
    #output = '../data/glaucoma'
    output_file = '/Users/pgoffred/Documents/CompRelDetection/brat2CoNLL-main/final_outputs/dev'

    create_tsv_for_relation_classification(input_dir, output_file)
    #create_tsv_for_multiple_choice(input_dir, output)

if __name__ == "__main__":
    
    main()