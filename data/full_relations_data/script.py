ximport random
random.seed(42)

def smaller_dataset(path):
    print("Reading ", path)
    print()
    with open(path, "r") as f:
        lines = f.readlines()
    
    no_rel, att_lines, support_lines, eq_lines = [], [], [], []

    for line in lines:
        label, seq1, seq2 = line.split("\t")
        if label == "__label__noRel":
            no_rel.append(line)
        if label == "__label__Attack":
            att_lines.append(line)
        if label == "__label__Support":
            support_lines.append(line)
        if label == "__label__Equivalent":
            eq_lines.append(line)

    #selection_no_rel = random.sample(no_rel, int(len(no_rel)*0.01))
    selection_no_rel = random.sample(no_rel, len(att_lines)+len(support_lines)+len(eq_lines))

    # Undersampling the support class
    #new_supp_lines = random.sample(support_lines, len(att_lines)+len(eq_lines))
    
    # Removing the equivalent class
    new_lines = att_lines + support_lines + selection_no_rel
    random.shuffle(new_lines)
    with open("./small_" + path.split("./")[-1][4:], "w") as f:
        for line in new_lines:
            f.write(line)
    print("Finished writing smaller_", path)

smaller_dataset("./new_test.tsv")
smaller_dataset("./new_train.tsv")
smaller_dataset("./new_dev.tsv")


