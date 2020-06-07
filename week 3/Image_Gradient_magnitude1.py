img=imread('cameraman.tif');
[Gx,Gy]=imgradientxy(img,'sobel');
[Gmag, Gdir] = imgradient(Gx, Gy);
%imshowpair(Gx,Gy,'montage')


%imshowpair(Gmag,Gdir,'montage')
%Uncomment the code below to visualize Gx and Gy 
%Uncomment the code below to visualize Gmag and Gdir 

