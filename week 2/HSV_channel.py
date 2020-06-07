RGB = imread('image1.jpg');
imshow(RGB)
%Convert the RGB image to the HSV colorspace by using the rgb2hsv function.
hsvImage = rgb2hsv(RGB);

%Split the HSV image into its compotent hue, saturation, and value channels.
[h,s,v] = imsplit(hsvImage);

montage({h,s,v},'Size',[1 4])

