#!/bin/bash


meme2images=$(dirname $(which meme))/../libexec/meme-`meme -version`/meme2images

case $1 in
T1)
	$meme2images -eps results/motif.streme.klf1/streme.txt  results/motif-in.streme.klf1.text
	$meme2images -eps results/motif.streme.klf1/streme.xml  results/motif-in.streme.klf1.xml
	$meme2images -eps results/motif.streme.klf1/streme.html results/motif-in.streme.klf1.html

	[ $(ls -1 results/motif-in.streme.klf1.text/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls -1 results/motif-in.streme.klf1.xml/*.eps  | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls -1 results/motif-in.streme.klf1.html/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL

	;;

T2)
	$meme2images -eps results/motif.streme.klf1.extdna/streme.txt  results/motif-in.streme.klf1.extdna.text
	$meme2images -eps results/motif.streme.klf1.extdna/streme.xml  results/motif-in.streme.klf1.extdna.xml
	$meme2images -eps results/motif.streme.klf1.extdna/streme.html results/motif-in.streme.klf1.extdna.html

	[ $(ls -1 results/motif-in.streme.klf1.extdna.text/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls -1 results/motif-in.streme.klf1.extdna.xml/*.eps  | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls -1 results/motif-in.streme.klf1.extdna.html/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL

	;;

*)
	echo FAIL
	;;
esac
