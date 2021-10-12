export PYTHONPATH=.:$PYTHONPATH
for file in examples/*.py ; do
	echo $file
	python3 $file
done
