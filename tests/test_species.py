# Tests for CDR3 detection
from igdiscover.species import find_cdr3
from igdiscover.utils import nt_to_aa


def split(s):
	for line in s.split('\n'):
		line = line.strip()
		if line:
			yield line.split()


def assert_cdr3_detection(chain, s):
	for amino_acids, sequence in split(s):
		for offset in range(3):
			target = sequence[offset:]
			match = find_cdr3(target, chain)
			assert match is not None
			assert nt_to_aa(target[match[0]:match[1]]) == amino_acids, (chain, amino_acids, offset)


def test_cdr3_detection_heavy():
	heavy = """
	ARRLHSGSYILFDY CAGGTGACCTTGAAGGAGTCTGGTCCTGCGCTGGTGAAACCCACACAGACCCTCACGCTGACCTGCACCTTCTCTGGGTTCTCACTCAGCACTAGTGGTATGGGTGTGGGCTGGATCCGTCAGCCCTCACGGAAGACCCTGGAGTGGCTTGCACACATTTATTGGAATGATGATAAATACTACAGCACATCGCTGAAGAGCAGGCTCACCATCTCCAAGGACACCTCCAAAAACCAGGTGGTTCTAACAATGACCAACATGGACCCTGTGGACACAGCCACATATTACTGTGCACGGAGACTTCATAGTGGGAGCTACATTCTCTTTGACTACTGGGGCCAGGGAGTCCTGGTCACCGTCTCCTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGA

	ARIKWLRSPGYGYFDF CAGGTGACCTTGAAGGAGTCTGGTCCTGCGCTGGTGAGACCCACACAGACCCTCACTCTGACCTGCACCTTCTCTGGGTTCTCAATCAGCACCTCTGGAACAGGTGTGGGCTGGATCCGTCAGCCCCCAGGGAAGGCCCTGGAATGGCTTGCAAGCATTTATTGGACTGATGCTAAATACTATAGCACATCGCAGAAGAGCAGGCTCACCATCTCCAAGGACACCTCCAGAAACCAGGTGATTCTAACAATGACCAACATGGAGCCTGTGGACATAGCCACATATTTCTGTGCACGGATAAAGTGGCTGCGGTCCCCAGGCTATGGATACTTCGATTTCTGGGGCCCTGGCACCCCAATCACCATCTCCTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGA

	ARHGIAAAGTHNWFDP TCAGCCGACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCCATGGATTACTGTGCGAGACATGGGATAGCAGCAGCTGGTACCCACAACTGGTTCGACCCCTGGGGCCAGGGAACCCTGGTCACCGTCTCCTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGCAGGTTGTT
	"""
	assert_cdr3_detection('VH', heavy)


def test_cdr3_detection_kappa():
	kappa = """
QQYDSSPRT TTCAGTGGCAGTGGAGCAGGGACAGATTTCACTCTCACCATCAGCAGTCTGGAACCTGAGGATGTCGCAACTTACTACTGTCAGCAGTATGATAGCAGCCCCCGGACGTTCGGCGCTGGGACCAAGCTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG

QQYSSYPYT GAGCTGGCCTCGGGAGTCCCAGCTCGCTTCAGTGGGAGTGGGTCAGGGACTTCTTTCTCTCTCACAATCAGCAACGTGGAGGCTGAAGATGTTGCAACCTATTACTGTCAGCAGTATAGCAGTTATCCGTACACGTTCGGCGCAGGGACCAAGCTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG

LQYDSSPYT ATTCTCACCATCAGCAGCCTGCAGCCTGAAGACTTTGCAACTTACTACTGTCTACAGTATGATAGTTCCCCGTACACGTTCGGCGCAGGGACCAAGCTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG

FQYYSGRLT ACAGACTTCACTCTCACCATCAGCAGCCTGCAGCCTGAGGACATTGCAGTTTATTACTGTTTCCAGTATTACAGCGGGAGACTCACGTTCGGAGGAGGGACCCGCTTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG
	"""
	assert_cdr3_detection('VK', kappa)


def test_cdr3_detection_lambda():
	lambda_ = """
LTYHGNSGTFV GGATCCAAAAACCCCTCAGCCAATGCAGGAATTTTGCTCATCTCTGAACTCCAGAATGAGGATGAGGCTGACTATTACTGTCTGACATATCATGGTAATAGTGGTACTTTTGTATTCGGTGGAGGAACCAAGCTGACCGTCCTAGGTCAGCCCAAGTCTGCCCCCACAGTCAGCCTGTTCC

QLWDANSTV ATGGCCACACTGACCATCACTGGCGCCCAGGGTGAGGACGAGGCCGACTATTGCTGTCAGTTGTGGGATGCTAACAGTACTGTGTTCGGTGGAGGAACCACGCTGACCGTCCTAGGTCAGCCCAAGTCTGCCCCCACAGTCAGCCTGTTCCCGCCCTCCTC

GVGYSGGYV GATCGCTACTTAACCATCTCCAACATCCAGCCTGAAGACGAGGCTGACTATTTCTGTGGTGTGGGTTATAGCGGTGGTTATGTATTCGGTGGAGGAACCAAGTTGACCGTCCTAGGTCAGCCCAAGTCTGCTCCCACAGTCAGCCTGTTCCCGCCCTCCTC
	"""
	assert_cdr3_detection('VL', lambda_)