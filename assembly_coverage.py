import sys

summary_contigs_length = 0
current_contig_length = 0
current_contig_coverage = 0.0
resulting_coverage = 0.0


def parse_header(header):
    h = header.strip().split('_')
    return int(h[3]), float(h[5])



file_name = sys.argv[1]
if file_name == '':
    print("Usage: python assembly_coverage.py <filename>")
    exit(1)

with open(file_name, 'r') as inp:
    for line in inp:
        if line.startswith('>'):
            current_contig_length, current_contig_coverage = parse_header(line)
            summary_contigs_length += current_contig_length
            resulting_coverage += current_contig_coverage*current_contig_length


resulting_coverage = resulting_coverage / summary_contigs_length
print("Coverage: ", resulting_coverage)