#!/bin/bash
#Author: Matthew Wollenweber
#Email: mjw@insomniac.technology


#configuration
START=`date --date '-2 hour' "+%Y/%m/%d:%H"`;
DATA_DIR='/tmp/silkweb'; #changeme
OUTFILE=`date  "+%Y-%m-%d.%H.csv"`
HOME_NET="128.164.0.0/16,161.253.0.0/16"; #changeme

mkdir $DATA_DIR &> /dev/null

#configuration for rwfilter looking for top external destination traffic that in the last 2 hours
RWFILTER="/usr/bin/rwfilter";
RWFARGS=" --class=all --proto=0-255 --not-dcidr=$HOME_NET --start-date=$START --pass=stdout ";

#configuration for rwstats. Currently only looking for traffic >1%
RWSTATS="/usr/bin/rwstats";
RWSARGS=" --fields=dip --percentage=1  --no-titles"

$RWFILTER $RWFARGS | $RWSTATS $RWSARGS > $DATA_DIR/$OUTFILE
