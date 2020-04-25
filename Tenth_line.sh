a=0
while read p
do
	if [ $a -eq 9 ]
	then
		echo $p
	fi
	((a++))
done < file.txt