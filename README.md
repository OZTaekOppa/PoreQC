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

[Guppy] (https://community.nanoporetech.com/docs/prepare/library_prep_protocols/Guppy-protocol/v/gpb_2003_v1_revax_14dec2018/guppy-software-overview) for for basecalling and processing raw signal data from nanopore sequencing devices, providing accurate DNA sequence information.

[Dorado] (https://github.com/nanoporetech/dorado) for Oxford Nanopore long-read sequencing data, offering enhanced accuracy in detecting structural variants and single nucleotide variants.

[Buttery-eel] (https://github.com/Psy-Fer/buttery-eel) for a Slow5 file reader and basecalling wrapper for Guppy and Dorado.

[Cutadapt] (https://github.com/marcelm/cutadapt) for removing adapters, primers, and other unwanted sequences from high-throughput sequencing data.

[Sequali] (https://github.com/rhpvorderman/sequali) for evaluating the quality of sequencing data through the generation of comprehensive metrics and visualizations.

[Nextflow] (https://github.com/nextflow-io/nextflow) for a data-driven computational workflow engine designed to facilitate scalable and reproducible scientific workflows.

[In-house Perl Script] for calculating basic statistics of a FASTQ file in-house.


### Assembly:
- Hifiasm: Using long reads, the phased contigs will be generated (Taek)

### Contamination and manual curation:
- Organell reads (e.g. mtGenome): Taek

### Assembly summary statistics:
- In-house script: Taek
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

### Detection of NRSs: 
- NUCmer/MUMmer package: The phased contigs will be aligned to T2T-CHM13 and hg38 (Taek).
- Bedtools: To generate fasta files containing only the unaligned portions of the NRSs.
- Any other tools and suggestions:

### Detection of SVs:
- CuteSV: Read mapping approach (Taek)
- Phased Assembly Variant (PAV), SVIM-ASM, MUM&Co: Assembly (fa) vs Assembly (fa) mapping approach (Taek)
- RepeatMasker & Assemblytics: To analyse for repetitive sequences and detect SVs in the final NRSs.
- primatR: To detect the hotspots of novel sequences
- Any other tools and suggestions:

### Anchoring the NRSs to the T2T-CHM13 and hg38:
- perEditor: To generate an extended reference genome (T2T-CHM13-NRS and hg38-NRS)
- Any other tools and suggestions:

### Synteny analysis to the T2T-CHM13 and hg38:
- Chromsyn: 
- Any other tools and suggestions:

### Variant calling using T2T-CHM13, hg38, T2T-CHM13-NRS, and hg38-NRS:
- Long-read variant caller: ???? GATK
- Short-read variant caller: ???? GATK
- Lift-over: 
- Any other tools and suggestions:

### Identification of gained SNVs in T2T-CHM13-NRS and hg38-NRS:
- ANNOVAR, lift-over and LostGained tool: 
- Any other tools and suggestions:

### Variant Effect Predictor:
- VEP: dipcall align to T2T-CHM13 and hg38
- Any other tools and suggestions:

### Heterozygosity analysis:
- Mummer and SyRi: SNP and small indels
- Any other tools and suggestions:

### Gene duplication analysis:
- Gencode v29 & minimap2: The genomic sequence of each gene will be re-mapped to both HPRC-HG002 v1.0 maternal and paternal assemblies. 
- Liffoff: To detect duplicated genes relative to T2T-CHM13 and hg38
- Any other tools and suggestions:

### List of medically relevant genes:
- Any deleterious variant (or frameshift) for medically relevant genes >> residing on human autosomes and X/Y-chromosomes
- Any potential gene rearrangement? 
- Any other tools and suggestions:

### Visualisations:
- RIdeogram: To visualise the SV distribution and enrichment significance on chromosomes.
- Gfvase & bandage: To extract subgraphs of SVs and visualise 
- GraphAligner: Gene positions in the subgraphs
- Gggenes: Linear structural visualisation of all structural haplotypes
- VRPG: An interactive web viewer for reference-projected pangenome graph.
- MashMap: Dot-plots to visualise mappings.
- Sequence tube map: Visualisation of genomic sequence graphs.
- Odgi draw + dogi viz + odgi inject: To provide a set of tools ranging from graph manipulation, layouting, extracting loci, over graph statistics to graph visualization, validation, and gene annotation liftovers.
- Any other tools and suggestions: 
