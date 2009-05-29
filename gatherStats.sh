#!/bin/sh

error_rates="0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9"
coverages="1 3 5 10 15 20 25"

cleanup ()
{
	rm -f r
	exit 1
}

trap cleanup SIGINT

for c in $coverages
do
	for e in $error_rates
	do
		echo "coverage: $c error: $e"
		i=0
		total=0
		error=0
		while [ $i -lt 10 ]
		do
			./readGen.py 30 --coverage=$c --error=$e < snps.fasta \
			| ./caller.py ref.fasta | ./verify.py snps.fasta > r &&
			t=`sed -n -e 's/total://p' r` &&
			err=`sed -n -e 's/errored://p' r`
			total=$((total+t))
			error=$((error+err))
			i=$((i+1))
		done
		echo $error
		echo $total
		echo "scale=4; $error/$total" | bc
	done
done

cleanup
