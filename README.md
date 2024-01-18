# PoreQC
An automated nextflow pipeline read basecalling, quality control and adapter removal


## Brief Background
PoreQC is a nextflow pipeline for Oxford nanopore reads (Slow5, Pod5 and Fastq). Integrating with Guppy, Dorado, Buttery-eel, Cutadapt, and Sequali, the automated pipeline can work for basecalling, quality control and removal adapters. We (Hyungtaek Jung and National Centre for Indigenous Genomics @ The Australian National University, Australia) initially started this project to provide comprehensive data management @ National Computational Infrastructure for biologists. As a CLI application, we have tested it for ONT long-read data focusing on medium and large-scale whole genome shotgun datasets that can be widely used to the greater research community. However, please note that basecalling and visualising a big dataset would require large computational resources on HPC or Cloud. 


## Citation
Hyungtaek Jung, Kirat Alreja, Kosar Hooshmand, Hadi Nazem-Bokaee, Hasindu Gamaarachchi, Hardip Patel: PoreQC: An automated nextflow pipeline for oxford nanopore read basecalling, quality control and adapter removal, [PLoS Comp Biol Submitted](https://www.biorxiv.org/XXXX).


## Contents:
    STABLE
    INSTALLATION
    LICENSE 
    GETTING STARTED
    FAQ
    WIKI PAGE
    AUTHOR
    COPYRIGHT


## STABLE (version 0.0.XXX)
Release date: January 2024
PoreQC comprises two key features (basecalling and quality control) and four interactive steps with open-source programs (See LICENSE), mainly written in Nextflow. 


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

PoreQC is provided under the MIT license and is based on other open-source software:

[Guppy] (https://community.nanoporetech.com/docs/prepare/library_prep_protocols/Guppy-protocol/v/gpb_2003_v1_revax_14dec2018/guppy-software-overview) for  basecalling and processing raw signal data from nanopore sequencing devices, providing accurate DNA sequence information.

[Dorado] (https://github.com/nanoporetech/dorado) for Oxford Nanopore long-read sequencing data, offering enhanced accuracy in detecting structural variants and single nucleotide variants.

[Buttery-eel] (https://github.com/Psy-Fer/buttery-eel) for a Slow5 file reader and basecalling wrapper for Guppy and Dorado.

[Cutadapt] (https://github.com/marcelm/cutadapt) for removing adapters, primers, and other unwanted sequences from high-throughput sequencing data.

[Sequali] (https://github.com/rhpvorderman/sequali) for evaluating the quality of sequencing data through the generation of comprehensive metrics and visualizations.

[Nextflow] (https://github.com/nextflow-io/nextflow) for a data-driven computational workflow engine designed to facilitate scalable and reproducible scientific workflows.

[In-house Perl Script] for calculating basic statistics of a FASTQ file in-house.


## Tested Datasets
Reference genome (https://www.ncbi.nlm.nih.gov/assembly/GCF_000001735.3/#/st)
Oxford Nanopore reads (https://ngdc.cncb.ac.cn/gsa/browse/CRA004538) and (https://www.sciencedirect.com/science/article/pii/S1672022921001741)

## GETTING STARTED

PoreQC, integrated with Nextflow, has two specific features: a basecalling (Slow5) and a result summary and visualisation of quality control (Fastq). The data input/output enables end-to-end file selection. The result summary and visualisation are mainly designed to visualise the outcome for quality control. Please note that all required input files (e.g. Slow5) must be prepared from [Slow5tools] (https://github.com/hasindu2008/slow5tools) to have a seamless experience of PoreQC. However, users can use Fastq files for quick quality control. 


### Slow5 format:
- Slow5 tools: Please see the official page of [Slow5tools] (https://github.com/hasindu2008/slow5tools) to make a proper Slow5 format from the ONT data.

### Buttery-eel:
- Requriment: The pipeline of buttery-eel requires both CPU and GPU resources.
- Computing environment: Please use an HPC or Cloud to facilitate the CPU and GPU resources with a proper queue job submission.
- Buttery-eel.pbs.sh: Secure the [buttery-eel-guppy] (https://github.com/hasindu2008/nci-scripts/blob/main/basecall/buttery-eel-guppy.pbs.sh) or [butter-eel-dorado] (https://github.com/hasindu2008/nci-scripts/blob/main/basecall/buttery-eel-dorado.pbs.sh) pipelines
- Input: Slow5 secured from Slow5tools.
- Select model: Depending on ONT library preparation and sequencing kits, users must select the proper model in the pipeline.
- Module load: Users can choose two options between buttery-eel (v0.4.2) + guppy (v6.5.7) and buttery-eel (v0.4.2) + dorado (v7.2.13). Please check the page of Butter-eel [Buttery-eel] (https://github.com/Psy-Fer/buttery-eel) for the latest versions.
- Default mode: This mode will do the basic basecalling with detection and removal of adapters.
      Usage: Execute this command in the terminal.
          qsub -v MERGED_SLOW5=/ONT_raw_data/QTXXXX230285_reads.blow5,BASECALL_OUT=/ONT_raw_data/OutFQDrdT2 ./buttery-eel_QT0285.pbs.sh
  
- Advanced mode: This mode will do the basecalling, removal adapters and split reads.
      Add parameters: Add these parameters "--detect_mid_strand_adapter --trim_adapters --detect_adapter --do_read_splitting" in the pipeline, specifically after "--max_queued_reads 20000."
      Usage: Execute this command in the terminal.
          qsub -v MERGED_SLOW5=/ONT_raw_data/QTXXXX230285_reads.blow5,BASECALL_OUT=/ONT_raw_data/OutFQDrdT2 ./buttery-eel_QT0285.pbs.sh


### Reads Stats:
- Input: Fastq file generated from buttery-eel pipeline. 
- Caln50 package: Taek
- ASMGENE: Taek
- QUAST: Taek
- Any other tools and suggestions: Assemblytics, VGP pipeline

### Detection of telomere and centromere 
- In-house pipeline: Kirat
- Any other tools and suggestions:

### Annotations:
- Human RefSeq transcripts:
- RepeatMasker:
- WindowMasker:
- RepeatModeler:
- Any other tools and suggestions:





