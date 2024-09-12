from sacrebleu.metrics import BLEU

refs = ["The first to arrive at the finish line, after three hours and 13 minutes was Fred Lorz."]
syss = ["Fred Lorz was the first to cross the finish line after three hours and 13 minutes."]

bleu = BLEU()
bleu.corpus_score(syss, refs)
bleu
#BPE byte pair encoding 