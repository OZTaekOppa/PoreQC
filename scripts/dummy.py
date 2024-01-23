# fqreadstats.pl (written by Hyungtaek Jung and Hardip Patel @ NCIG/ANU) to calculate a basic stats of
 FQ/FASTQ file.

#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Long;
use File::Basename;

# Initialize default values for optional parameters
my $num_cpus = 1;
my $memory = 10;
my $help;

# Get command line options
GetOptions(
    'input-fq=s' => \my $input_fq,
    'out=s'      => \my $output_csv,
    't=i'        => \$num_cpus,
    'mem=i'      => \$memory,
    'help'       => \$help,
);

# Display help and exit if --help is specified
if ($help) {
    print_help();
    exit;
}

# Check mandatory parameters
unless ($input_fq && $output_csv) {
    die("Error: Both --input-fq and --out are mandatory parameters. Use --help for more information.\n
");
}

# Check if input file exists
unless (-e $input_fq) {
    die("Error: Input file '$input_fq' not found.\n");
}

# Check if input file is compressed and decompress if necessary
if ($input_fq =~ /\.(fq\.gz|fastq\.gz)$/) {
    my $output_fq = decompress($input_fq);
    $input_fq = $output_fq if $output_fq;
} elsif ($input_fq !~ /\.(fq|fastq)$/) {
    die("Error: Not a proper fastq file format. Please provide a readable file format to call the 'fqr
eadstats' module.\n");
}

# Run fqreadstats command
my $fqreadstats_cmd = "cat \"$input_fq\" | sed -n '1~4s/^@/>/p;2~4p' | perl -lne 'if(\$_=~/>/){push(\@
l,length(\$s));\$s=\"\";}else{\$s.=\$_;\$total+=length(\$_);\$gc+=\$_=~tr/[GC]//;\$ncount+=\$_=~tr/N//
;}END{push(\@l,length(\$s));shift\@l;\@l=sort{\$b<=>\$a}\@l;\$n9p=0;\$n5p=0;foreach(\@l){\$n+=\$_;if(\
$n>=\$total*0.5 && \$n5p==0){\$n5p=\$_}elsif(\$n>=\$total*0.9 && \$n9p==0){\$n9p=\$_}}; print \"\$tota
l,\".scalar(\@l).\",\".(sprintf \"%.02f\", ((\$gc*100)/\$total)).\",\$ncount,\".(sprintf \"%.02f\", \$
total/scalar(\@l)).\",\".(\$l[int(scalar(\@l)/2)]).\",\$l[0],\$l[\$#l],\$n5p,\$n9p' > \"$output_csv\""
;

# Run fqreadstats command with specified performance parameters
my $log_file = "fqreadstats_log.txt";
my $run_command = "perl fqreadstats.pl --input-fq $input_fq --out $output_csv";
$run_command .= " --t $num_cpus" if $num_cpus;
$run_command .= " --mem $memory" if $memory;
$run_command .= " 2>&1 | tee $log_file";

# Execute the fqreadstats command
system($run_command);

# Subroutine to decompress a file and return the decompressed filename
sub decompress {
    my ($input) = @_;
    my ($base, $ext) = fileparse($input, qr/\.[^.]*/);
    my $output = "${base}_decompressed$ext";
    my $decompress_cmd = "gzip -dc $input > $output";
    system($decompress_cmd);
    return (-e $output) ? $output : undef;
}

# Subroutine to print help information
sub print_help {
    print <<HELP;
Usage: perl $0 --input-fq <input_file> --out <output_csv> [--t <num_cpus>] [--mem <memory>] [--help]

--input-fq: Indicate the input file (fq or fastq) and path.
--out: Indicate the output file (csv) and path.
--t: Number of CPUs with only numbers (integers).
--mem: Number of memory with only numbers (integers).
--help: Display this help message.

Example: perl $0 --input-fq test_in.fq --out output_files.csv --t 1 --mem 2
HELP
}

