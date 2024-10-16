# PoreQC
An automated nextflow pipeline read basecalling, quality control and adapter removal

![PoreQC Logo](https://github.com/OZTaekOppa/PoreQC/blob/main/images/PoreQC_Logo.png)


## Brief Background
**PoreQC** is a [Nextflow](https://github.com/nextflow-io/nextflow) pipeline for Oxford nanopore reads ([Slow5](https://github.com/hasindu2008/slow5tools), [Pod5](https://github.com/nanoporetech/pod5-file-format) and [Fastq](https://en.wikipedia.org/wiki/FASTQ_format)). Integrating with [Guppy](https://community.nanoporetech.com/docs/prepare/library_prep_protocols/Guppy-protocol/v/gpb_2003_v1_revax_14dec2018/guppy-software-overview), [Dorado](https://github.com/nanoporetech/dorado), [Buttery-eel](https://github.com/Psy-Fer/buttery-eel), [Cutadapt](https://github.com/marcelm/cutadapt), and [Sequali](https://github.com/rhpvorderman/sequali), the automated pipeline can work for basecalling, quality control and removal adapters. We (Hyungtaek Jung and the [National Centre for Indigenous Genomics](https://ncig.anu.edu.au/) at [The Australian National University](https://www.anu.edu.au/), Australia) initially started this project to provide comprehensive data management at the [National Computational Infrastructure](https://nci.org.au/) for biologists. As a command-line interface (CLI) application, we have tested it for ONT long-read data focusing on whole genome shotgun datasets that can be widely used by the greater research community. However, please note that basecalling and visualising a big dataset would require large computational resources on HPC or Cloud. 


## Citation
Hyungtaek Jung et al.: **PoreQC**: An automated nextflow pipeline for oxford nanopore read basecalling, quality control and adapter removal, [Preparation for Submission](https://www.biorxiv.org/XXXX).


## Contents:
+ STABLE
+ INSTALLATION
+ LICENSE 
+ GETTING STARTED
+ FAQ
+ WIKI PAGE
+ AUTHORS
+ COPYRIGHT


## STABLE (version 0.0.XXX)
- **PoreQC** comprises two key features (basecalling and quality control) and four interactive steps with open-source programs (See LICENSE). 


## INSTALLATION
Please download the program from [this link](https://github.com/OZTaekOppa/PoreQC)
!!! Please note, that programs and dependencies can also be installed via Bioconda. For any other issues, we highly encourage users to use the [Issues](https://github.com/OZTaekOppa/PoreQC/issues).

    ~~~
    Create the virtual environment
    Need to be updated
    
    Get source
    Need to be updated
    
    Install packages
    Need to be updated
    
    Run
    Need to be updated
    ~~~

## License

**PoreQC** is provided under the MIT license and is based on other open-source software:

[Guppy](https://community.nanoporetech.com/docs/prepare/library_prep_protocols/Guppy-protocol/v/gpb_2003_v1_revax_14dec2018/guppy-software-overview) for  basecalling and processing raw signal data from nanopore sequencing devices, providing accurate DNA sequence information.

[Dorado](https://github.com/nanoporetech/dorado) for Oxford Nanopore long-read sequencing data, offering enhanced accuracy in detecting structural variants and single nucleotide variants.

[Buttery-eel](https://github.com/Psy-Fer/buttery-eel) for a Slow5 file reader and basecalling wrapper for Guppy and Dorado.

[Cutadapt](https://github.com/marcelm/cutadapt) for removing adapters, primers, and other unwanted sequences from high-throughput sequencing data.

[Sequali](https://github.com/rhpvorderman/sequali) for evaluating the quality of sequencing data through the generation of comprehensive metrics and visualizations.

[Nextflow](https://github.com/nextflow-io/nextflow) for a data-driven computational workflow engine designed to facilitate scalable and reproducible scientific workflows.

[In-house Perl Script (fqreqdstats.pl)](https://github.com/OZTaekOppa/PoreQC/blob/main/scripts/fqreadstats.pl) for calculating basic statistics of a FASTQ file in-house.


### Tested Datasets
Reference genome(https://www.ncbi.nlm.nih.gov/assembly/GCF_000001735.3/#/st)
Oxford Nanopore reads(https://ngdc.cncb.ac.cn/gsa/browse/CRA004538) and (https://www.sciencedirect.com/science/article/pii/S1672022921001741)

## GETTING STARTED

**PoreQC**, integrated with Nextflow, has two specific features: a basecalling (Slow5) and a result summary and visualisation of quality control (Fastq). The data input/output enables end-to-end file selection. The result summary and visualisation are mainly designed to visualise the outcome for quality control. Please note that all required input files (e.g. Slow5) must be prepared from [Slow5tools](https://github.com/hasindu2008/slow5tools) to have a seamless experience of **PoreQC**. However, users can use Fastq files for quick quality control. 

![PoreQC Workflow](https://github.com/OZTaekOppa/PoreQC/blob/main/images/PoreQC_Flowchart.png)

### Slow5 format:
- Slow5 tools: Please see the official page of [Slow5tools](https://github.com/hasindu2008/slow5tools) to make a proper Slow5 format from the ONT data.

### Buttery-eel:
- Requriment: The pipeline of buttery-eel requires both CPU and GPU resources.
- Computing environment: Please use an HPC or Cloud to facilitate the CPU and GPU resources with a proper queue job submission.
- Buttery-eel.pbs.sh: Secure the [buttery-eel-guppy](https://github.com/hasindu2008/nci-scripts/blob/main/basecall/buttery-eel-guppy.pbs.sh) or [butter-eel-dorado](https://github.com/hasindu2008/nci-scripts/blob/main/basecall/buttery-eel-dorado.pbs.sh) pipelines
- Input: Slow5 secured from Slow5tools.
- Output: Basecalled and trimmed Fastq file.
- Select model: Depending on ONT library preparation and sequencing kits, users must select the proper model in the pipeline.
- Module load: Users can choose two options between buttery-eel (v0.4.2) + guppy (v6.5.7) and buttery-eel (v0.4.2) + dorado (v7.2.13). Please check the page of Butter-eel [Buttery-eel](https://github.com/Psy-Fer/buttery-eel) for the latest versions.
- Default mode: This mode will do the basic basecalling with detection and removal of adapters.
1. Usage: Execute this command in the terminal.
```
qsub -v MERGED_SLOW5=/ONT_raw_data/QTXXXX230285_reads.blow5,BASECALL_OUT=/ONT_raw_data/OutFQDrdT2 ./buttery-eel_QT0285.pbs.sh
```
  
- Advanced mode: This mode will do the basecalling, removal adapters and split reads.
1. Add parameters: Add these parameters "--detect_mid_strand_adapter --trim_adapters --detect_adapter --do_read_splitting" in the pipeline, specifically after "--max_queued_reads 20000."
1. Usage: Execute this command in the terminal.
```
qsub -v MERGED_SLOW5=/ONT_raw_data/QTXXXX230285_reads.blow5,BASECALL_OUT=/ONT_raw_data/OutFQDrdT2 ./buttery-eel_QT0285.pbs.sh
```


### Reads Stats:
- Requirement: The script of Perl/bash requires a Perl library.
- Input: Fastq file generated from buttery-eel pipeline.
- Output: A summary of csv file for the Fastq.
- Perl script: An in-house script to calculate the basic stats of Fastq file (including compressed file format).
1. Usage: Execute this command in the terminal.
1. Mandatory parameters: --input.fq and --out para
1. Optional parameters: --t and --mem
1. Help: perl fqreadstats.pl --help
```
perl fqreadstats.pl --input.fq test_reads.fq.gz --out test_reads.csv --t 2 --mem 40
```

### Cutadapt 
- Installation and Requirement: Please see the page of [Cutadapt](https://github.com/marcelm/cutadapt)
- Input: Fastq file generated from buttery-eel pipeline.
- Output: Trimmed Fastq file.
1. Usage: Execute this command in the terminal.
1. Mandatory parameters: -g, -a, or -b (adapter sequences), -o (output directory), and input.fastq/fq (input fastq file)
```
cutadapt -g TTTTTTTTCCTGTACTTCGTTCAGTTACGTATTGCT -o /output_folder/ input.fastq
```


### Sequali:
- Installation and Requirement: Please see the page of [Sequali](https://github.com/rhpvorderman/sequali) 
- Input: Fastq file generated from buttery-eel pipeline or Cutadapt.
- Output: A summary of html and json file for the Fastq.
1. Usage: Execute this command in the terminal.
1. Mandatory parameters: input.fastq/fq (input fastq file) --adapter-file (adapter sequences as .tsv), --outdir (output directory), and -t (CPU number)
```
sequali input.fastq --adapter-file "$ASFL" --outdir /output_folder/ -t 2
```


### Nextflow:
- Installation and Requirement: Please see the page of [Nextflow](https://github.com/rhpvorderman/sequali???????) 
- Input: Slow5 file generated from [Slow5tools](https://github.com/hasindu2008/slow5tools).
- Output: Cleaned Fastq and its summary with html and json files.
- Interaction: A user can indicate the input/output folder/file for their convenience.
- Resume: An interrupted stage/step can be resumed via Nextflow management.
1. Usage: Execute this command in the terminal.
1. Mandatory parameters: input.fastq/fq (input fastq file) --adapter-file (adapter sequences as .tsv), --outdir (output directory), and -t (CPU number)
```
sequali input.fastq --adapter-file "$ASFL" --outdir /output_folder/ -t 2
```


## FAQ

We encourage users to use the [Issues](https://github.com/OZTaekOppa/PoreQC/issues).


## WIKI PAGE

Please see GitHub page.


## AUTHORS

**Hyungtaek Jung** and the [**National Centre for Indigenous Genomics**](https://ncig.anu.edu.au/).


## COPYRIGHT

The full **PoreQC** is distributed under the MIT license. 

