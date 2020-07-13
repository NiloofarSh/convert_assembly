Manipulated by Niloofar Shirvanizadeh July 2020.

Copyright (c) 1999-2011 The European Bioinformatics Institute and
Genome Research Limited.  All rights reserved.

This software is distributed under a modified Apache license.
For license details, please see

http://www.ensembl.org/info/about/code_licence.html

Please email comments or questions to the public Ensembl
developers list at <http://lists.ensembl.org/mailman/listinfo/dev>.

Questions may also be sent to the Ensembl help desk at
<http://www.ensembl.org/Help/Contact>

Summary
=======

A program to map slices from GRCh38 assembly to GRCh37 assembly.


Documentation
=============

For a summary of command line flags, run:

  perl GRCh38_to_GRCh37.pl --help

Usage:

  GRCh38_to_GRCh37.pl --species=species --file=filename
  
  For example:
  perl GRCh38_to_GRCh37.pl -s human -f sample_input.in

    --species / -s  Name of species.

    --genomes / -g  Automatically sets DB params for e!Genomes

    --file / -f     Name of file containing a list of slices to map to
                    the most recent assembly.  The format of the data
                    is the same as the output of the name() method on a
                    Slice object:

                      coord_system:version:seq_region_name:start🔚strand

                    For example:
                    chromosome:GRCh38:10:25000:30000:1
                      
                     NB:  Mappings are only available for chromosomes 
                    from the latest assembly (GRCh38) to the old assembly 
                    (GRCh37).

                    If the strand is missing, the positive ("1") strand
                    will be used.

                    If the start is missing, it is taken to be "1".  If
                    the end is missing, it is taken to be the end of the
                    seq_region.

    --help    / -h  To see this text.

Example usage:

  GRCh38_to_GRCh37.pl -s human -f assemblymapper.in

An example input file (sample_input.in) is provided with this script.
