A histogram is simply a graph that shows:

X-axis: Pixel intensity values (0 to 255 for an 8-bit grayscale image)
0 = Black
255 = White
Y-axis: Number of pixels having that intensity

For example:

If most pixels are near 0–50 → image is dark.
If most pixels are near 200–255 → image is bright.
If pixels occupy only 100–150 → image has low contrast.

Suppose a dark image uses only intensity values from 40 to 100.

Instead of using the full range 0 to 255, the image uses only a small portion.

Histogram equalization redistributes these values over the full range:

Before: 40 ───────── 100

After : 0 ───────────────────────────── 255

This makes dark regions darker, bright regions brighter, and details more visible.

The method works by:

Calculating the histogram.
Finding the cumulative distribution function (CDF).
Using the CDF to map old pixel values to new ones.
Producing an image with a more uniform histogram.

