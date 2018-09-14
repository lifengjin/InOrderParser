import sys
from nltk.tree import Tree as Tree

with open(sys.argv[1]) as ofh:
    trees = []
    for line in ofh:
        words_and_tags = line.strip().split(' ')
        cur_frag = None
        whole_len = len(words_and_tags)
        for word_index in range(0, whole_len, 2):
            preterm = Tree(words_and_tags[word_index+1], [words_and_tags[word_index],])
            if not cur_frag:
                cur_frag = preterm
            else:
                cur_frag = Tree('V' , [cur_frag, preterm])
        print(cur_frag.pformat(margin=1000000))