# Image Resizer
This project is to increase the image size to match a 43:18 ratio. The purpose of this was to make it match my screen size to prevent stretch when using it as a wallpaper. It's similar to a Photoshop Edit Canvas Size (Alt + Ctrl + C). The extra space is only generated on width, not height, and it is filled in white. You can adjust (line 19)[https://github.com/podpah/image-resizer/blob/main/resizer.py#L19] to make it match a different ratio.
```console
python resizer.py -p images -f
```
```console
python resizer.py -p Downloads/images
```
## Flags
* -f forces the change. Basically, instead of creating a duplicate in the folder, it overrides the current image
* -p allows you to select the path for the folder where the images are
