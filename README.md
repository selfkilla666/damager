# damager

Utility for adding JPEG and WEBP compression artifacts

---

## Example CLI usage
Before using it, you need to install the dependent packages by writing <br>
` pip install -r requirements.txt `

Example of using Damager through the command interface: <br> ` python damager image.png jpeg 10 `

### CLI Arguments
You can get full help for the utility with ` python damager.py -h `
| Argument          | Type                | Help                                         |
|-------------------|---------------------|----------------------------------------------|
| filename          | required positional | Path to image whats need to compress         |
| compress format   | required positional | Compress formats for image (webp, jpeg)      |
| quality           | required positional | Output file quality (in range from 1 to 100) |
| output path, -o   | optional            | Output path to save result                   |
| output format, -f | optional            | Output file format (png, webp, jpeg)         |