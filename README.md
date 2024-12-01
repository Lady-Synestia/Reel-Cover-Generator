# Reel Cover Generator

A program made using Pillow in Python to easily generate covers for the Portsmouth Climbing Club instagram

## Installation and Usage:

- Download the latest release:[], and extract the zip.

- Add any background photos you want to use to /Uploads. (I recommend renaming them to something simple and easy to type out).

- Run `app.exe`.

### Program Options:

- `custom linebreaks [y/n] > `: `y` If you would like to set the text for each line yourself. || `n` If you would like the script to automatically add the linebreaks.

- `post title > `: Text to be displayed as the reel's title (must be set to something)

- `with [leave blank for none] > `: Text to be displayed under the "With:" subheading - leave field blank for no subheading

- `background photo name > `: Filename of the background photo you wish to use (including file extension). note: the script does not accept `.HIEC` files, please convert them to `.jpg` first. If left blank only the overlay will be generated

### Outputs:

- `overlay.png`: Transparent purple overlay image with text and logo.

- `cover.png`: Final cover image (`1080x1920`), save this to the drive and upload to Instagram. 

## Chloe's TODO list
If you have any other suggestions let me know!

- Creating packaged application using pyinstaller for easier distribution.
- Tkinter GUI for easier use.
- Option to generate same cover with multiple title options.
- Option to generate same cover with multiple background image options.
- Possibility of download/upload of images directly from the google drive?
