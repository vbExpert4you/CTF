#Information
Files can always be changed in a secret way. Can you find the flag? cat.jpg

Hints:
1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}


Found a steganography site: https://stegonline.georgeom.net/upload
It also has a CTF checklist: https://stegonline.georgeom.net/checklist

Tried running:
ls -lisan cat.jpg
4472036 860 -rw-r--r-- 1 1000 1000 878136 Mar 15 14:24 cat.jpg

Ran:
strings -n 7 -t x cat.jpg | grep Pico
     37 PicoCTF
    23b     <rdf:li xml:lang='x-default'>PicoCTF</rdf:li>

Ran:
binwalk -Me cat.jpg

Scan Time:     2021-04-24 05:34:41
Target File:   /home/kali/Documents/repos/CTF/picoCTF/Information/cat.jpg
MD5 Checksum:  96a7f666c0bf82891135e98c8c2e5bea
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02

Ran:
pngcheck -vtp7f cat.jpg                                                                                                                        127 ⨯
File: cat.jpg (878136 bytes)
  this is neither a PNG or JNG image nor a MNG stream
ERRORS DETECTED in cat.jpg

Uploaded the image to the stegonline page and looked at the bit planes. Saved the file to cat_bitplanes.jpg.

Uploaded the image to http://exif.regex.info/exif.cgi and looked at the data. Saved it to Image Metadata Viewer.html.

Ran:
steghide extract -sf cat.jpg                                                                                                                   127 ⨯
Enter passphrase: (tried using PicoCTF)
steghide: could not extract any data with that passphrase!

Ran:
steghide extract -sf cat.jpg                                                                                                                   127 ⨯
Enter passphrase: (tried using 41)
steghide: could not extract any data with that passphrase!


