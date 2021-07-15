#!/bin/bash


meme2images=$(dirname $(which meme))/../libexec/meme-`meme -version`/meme2images

case $1 in
T1)
	$meme2images -eps results/motif.streme.klf1/streme.txt  results/motif-in.streme.klf1.text
	$meme2images -eps results/motif.streme.klf1/streme.xml  results/motif-in.streme.klf1.xml
	$meme2images -eps results/motif.streme.klf1/streme.html results/motif-in.streme.klf1.html

	[ $(ls results/motif-in.streme.klf1.extdna.text/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls results/motif-in.streme.klf1.extdna.xml/*.eps  | wc -l) -ge 1 ] && echo PASS || echo FAIL
	[ $(ls results/motif-in.streme.klf1.extdna.html/*.eps | wc -l) -ge 1 ] && echo PASS || echo FAIL
	;;
*)
	echo FAIL
	;;
esac
