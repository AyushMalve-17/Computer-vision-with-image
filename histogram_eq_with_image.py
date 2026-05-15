import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Function to compute histogram
# -------------------------------------------------
def compute_histogram(image):

    hist = np.zeros(256, dtype=int)

    flat_image = image.flatten()

    for pixel in flat_image:
        hist[pixel] += 1

    return hist


# -------------------------------------------------
# Function to compute CDF
# -------------------------------------------------
def compute_cdf(hist):

    cdf = np.zeros(256, dtype=int)

    cdf[0] = hist[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    return cdf


# -------------------------------------------------
# Histogram Equalization Function
# -------------------------------------------------
def histogram_equalization(image):

    # Step 1: Histogram
    hist = compute_histogram(image)

    # Step 2: CDF
    cdf = compute_cdf(hist)

    # Step 3: Mask zeros
    cdf_masked = np.ma.masked_equal(cdf, 0)

    # Step 4: Normalize CDF
    cdf_min = cdf_masked.min()

    total_pixels = image.shape[0] * image.shape[1]

    cdf_normalized = (
        (cdf_masked - cdf_min) * 255
        / (total_pixels - cdf_min)
    )

    # Convert to uint8
    cdf_final = np.ma.filled(
        cdf_normalized,
        0
    ).astype("uint8")

    # Step 5: Map pixels
    equalized_image = cdf_final[image]

    return equalized_image, hist, cdf


# -------------------------------------------------
# Main Program
# -------------------------------------------------
def main():

    print("Starting Histogram Equalization Program...")

    # Load image named sample.jpg
    image_path = "sample.jpg"

    # Read image in grayscale
    original_image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    # Check image loaded or not
    if original_image is None:
        print("Error: sample.jpg not found.")
        return

    print("Performing Histogram Equalization...")

    # Equalization
    equalized_image, orig_hist, orig_cdf = histogram_equalization(
        original_image
    )

    # Histogram and CDF for equalized image
    eq_hist = compute_histogram(equalized_image)

    eq_cdf = compute_cdf(eq_hist)

    # -------------------------------------------------
    # Display Results
    # -------------------------------------------------
    plt.figure(figsize=(15, 10))

    # Original Image
    plt.subplot(2, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    # Original Histogram
    plt.subplot(2, 3, 2)
    plt.plot(orig_hist, color='black')
    plt.title("Original Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Original CDF
    plt.subplot(2, 3, 3)
    plt.plot(orig_cdf, color='blue')
    plt.title("Original CDF")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Cumulative Frequency")

    # Equalized Image
    plt.subplot(2, 3, 4)
    plt.imshow(equalized_image, cmap='gray')
    plt.title("Equalized Image")
    plt.axis("off")

    # Equalized Histogram
    plt.subplot(2, 3, 5)
    plt.plot(eq_hist, color='black')
    plt.title("Equalized Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Equalized CDF
    plt.subplot(2, 3, 6)
    plt.plot(eq_cdf, color='red')
    plt.title("Equalized CDF")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Cumulative Frequency")

    plt.tight_layout()

    # Save result
    plt.savefig("histogram_equalization_result.png")

    print("Result saved as histogram_equalization_result.png")

    plt.show()


# -------------------------------------------------
# Driver Code
# -------------------------------------------------
if __name__ == "__main__":
    main()