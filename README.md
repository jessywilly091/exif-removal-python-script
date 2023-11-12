<h1 align="center">Python Script to Remove Exif Data from an Image</h1><br>
This is a python script which creates a new image by copying only the pixel values and thereby removing exif data.<br>
Input is read as path of the image. Output file is stored in the directory containing the script.<br>
However it is seen that the size of the file reduces and shows a decrease in color(brightness) which might be due to lossy compression or differences in PIL encoder.<br>
Any alternate apporaches that can preserve image quality is welcome.
