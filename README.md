# musical-art

This is a simple python script which converts a jpg image to music. It splits the image into a user-defined grid, and translates each box in the grid into a midi note. Notes are generated sequentially left->right and top->bottom. Images can either be uploaded or drawn in the app itself using an integrated simple drawing tool. Notes can also be generated in either single-note form (where the R, G, and B values in each box are averaged to become a midi tone) or chord form (where the average R, G, and B values translate into three separate tones which are played simultaneously). The length of each tone can be defined by the user, but is limited within a certain range which is generated based on the grid dimensions in order to prevent the total length of the generated music from being too short or too long. 

The demo directory contains all files necessary for a live, continuous demo of the script. It pulls images randomly from its limited collection of images, dispays them, then translates them into music automatically. 

All included images are example images which demonstrate the functionality of the script. 
