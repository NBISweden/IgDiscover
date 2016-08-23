# Tests for CDR3 detection
from igdiscover.species import CDR3_REGEX
from igdiscover.utils import nt_to_aa


def split(s):
	for line in s.split('\n'):
		line = line.strip()
		if line:
			yield line.split()


def assert_cdr3_detection(chain, s):
	for amino_acids, sequence in split(s):
		match = CDR3_REGEX[chain].search(sequence)
		assert match
		assert nt_to_aa(match.group('cdr3')) == amino_acids


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

LQYDSSPYT ATTACTGTACCCGGGGGGGGCCAGTCAGAGTGTTAGTAGTTCCTTAAACTGGTATCAGCAGAAACCAGGGCAAGTTCCTAAACTCCTGATCTATTGGGCAATCAGCTTGGCATCTGGGGTCCCATCGAGGTTCAGTGGCAGTGGTTATGGGACAGATTTCATTCTCACCATCAGCAGCCTGCAGCCTGAAGACTTTGCAACTTACTACTGTCTACAGTATGATAGTTCCCCGTACACGTTCGGCGCAGGGACCAAGCTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG

FQYYSGRLT CACGATGTATTAGGGGGGGCTTCAGCAGGGACTCAGAGTGAACCATGGAAGCCTTGGCTCTGCTCCTCTGCCTCCTGGTACTAAAGCTCCCAGATACCACTGGACAAACCCTGCTGACTCAGACTCCAGACTCTCTGGCTGTGTCTCCTGGAGAAACAGTCACTCTCAGCTGCAGGGCCAGTCAGGGTGTGAGTAACTACCTAGAATGGTACCAGCAGAAACCTGGGCAGGCTCCCAGACTCCTCATCTATACTGCCTCTAGCAGGGCCACTGGTGTCCCAGCCCGGTTCAGTGGCAGCAGATCAGGGACAGACTTCACTCTCACCATCAGCAGCCTGCAGCCTGAGGACATTGCAGTTTATTACTGTTTCCAGTATTACAGCGGGAGACTCACGTTCGGAGGAGGGACCCGCTTGGAAATCAAACGGAGTGTGCAGAAGCCAACTATCTCCCTCTTCCCTCCATCATCTGAGGAGG
	"""
	assert_cdr3_detection('VK', kappa)


def test_cdr3_detection_lambda():
	lambda_ = """
LTYHGNSGTFV GGATCCAAAAACCCCTCAGCCAATGCAGGAATTTTGCTCATCTCTGAACTCCAGAATGAGGATGAGGCTGACTATTACTGTCTGACATATCATGGTAATAGTGGTACTTTTGTATTCGGTGGAGGAACCAAGCTGACCGTCCTAGGTCAGCCCAAGTCTGCCCCCACAGTCAGCCTGTTCC

QLWDANSTV ATGGCCACACTGACCATCACTGGCGCCCAGGGTGAGGACGAGGCCGACTATTGCTGTCAGTTGTGGGATGCTAACAGTACTGTGTTCGGTGGAGGAACCACGCTGACCGTCCTAGGTCAGCCCAAGTCTGCCCCCACAGTCAGCCTGTTCCCGCCCTCCTC

GVGYSGGYV GATCGCTACTTAACCATCTCCAACATCCAGCCTGAAGACGAGGCTGACTATTTCTGTGGTGTGGGTTATAGCGGTGGTTATGTATTCGGTGGAGGAACCAAGTTGACCGTCCTAGGTCAGCCCAAGTCTGCTCCCACAGTCAGCCTGTTCCCGCCCTCCTC
	"""
	assert_cdr3_detection('VL', lambda_)
