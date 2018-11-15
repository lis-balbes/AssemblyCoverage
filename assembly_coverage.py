import sys

summary_contigs_length = 0
current_contig_length = 0
current_contig_coverage = 0.0
resulting_coverage = 0.0


def parse_header(header):
    h = header.strip().split('_')
    return int(h[3]), float(h[5])


def kmer_coverage_to_base(coverage_kmer, k, L):
    return (coverage_kmer * L) / (L - k + 1)


if len(sys.argv) < 4:
    print("Usage: python assembly_coverage.py <filename> <k> <L>")
    exit(1)
file_name = sys.argv[1]
k = int(sys.argv[2])
L = float(sys.argv[3])

with open(file_name, 'r') as inp:
    for line in inp:
        if line.startswith('>'):
            current_contig_length, kmer_coverage = parse_header(line)
            summary_contigs_length += current_contig_length
            base_coverage = kmer_coverage_to_base(kmer_coverage, k, L)
            resulting_coverage += base_coverage*current_contig_length


resulting_coverage = resulting_coverage / summary_contigs_length
print("Coverage: ", resulting_coverage)