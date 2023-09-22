'''

Roy wants to change his profile picture on facebook. Now facebook
has some restrictions over the dimensions of the picture that
we can upload.
Minimum dimension of the picture can be L x L, where L IS the
length of the side of square.
Now Roy has N photos of various dimensions.
Dimension ofa photo is denoted as W x H, where W
width of the photo and H - Height of the photo

When any photo is uploaded following events may occur:
1. If any of the width or height is less than L, user is prompted
to upload another one. Print "UPLOAD ANOTHER" in this
case.
2. If width and height, both are large enough and
  a. if the photo is already square then it is accepted. Print
  "ACCEPTED" in this case.
  b. else user prompted to crop it then print "CROPP IT" in this case

Given L, N, W and H as Input, print appropriate text as output.

Input Format:

First line contains L.
Second line contains N, number of photos.
Following N lines each contains two space separated integers W and H.

Output Format:

Print appropriate text for each photo in a new line.

Sample Input:

180
3
640 480
120 300
180 180

Sample Output:

CROP IT
UPLOAD ANOTHER
ACCEPTED


'''

size=int(input())
n=int(input())
for in range (n):
  n1,n2= map(int,input().split())
  if(n1<size or n2<size):
    print("UPLOAD ANOTHER")
  elif(n1==size and n2== size):
    print ("ACCEPTED" )
  else:
    print("CROP IT")
