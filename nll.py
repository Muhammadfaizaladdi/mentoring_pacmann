# Debug this code
import math

def nll(actual, predicted_proba):
	'''return the negative loglikelihood. Return NLL (float)'''
	N = len(actual)
	sum_ = 0
	for i in range(N):
		sum_ += (actual[i] * math.log(predicted_proba[i]) + (1-actual[i]) * math.log(1 - predicted_proba[i]))
	nll = -1/N * sum_
	return nll
  


# Input


res = nll(actual, predicted_proba)
print("Nilai Negative Likelyhood adalah:",res)
# Should be 0.16836656419122908