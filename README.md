# Data Compression Algorithm - First Version

## Overview

This project implements an algorithm for **data compression and decompression** using a **grammar-based** approach and **sequence compression** techniques. The primary objective is to reduce the size of binary data derived from images while maintaining the integrity of the original data (lossless compression).

The algorithm uses a set of defined grammar rules for data compression, followed by sequence-based compression. The compressed data can then be decompressed to recover the original content.

## Features

- **Grammar-Based Compression**: This method applies predefined grammar rules to compress repetitive data patterns.
- **Sequence Compression**: Uses a run-length encoding-like technique to further compress the data based on consecutive repeating elements.
- **Lossless Decompression**: The algorithm ensures no data is lost during compression, and the decompressed data matches the original binary representation.
- **Compression Ratio and Loss Calculation**: The system calculates the compression ratio and the percentage of data loss (if any).

## Functions

1. **apply_compression(data, grammars)**: 
   - Applies the grammar rules recursively to compress the input data.

2. **sequence_compression(data)**: 
   - Compresses the data by counting repeating sequences and replacing them with shorter representations.

3. **apply_decompression(data, grammars, applied_grammars)**:
   - Reverses the compression process by applying grammar rules in reverse order to recover the original data.

4. **sequence_decompression(data)**:
   - Decompresses the data that was compressed using sequence compression by expanding the run-length encoded sequences.

5. **calculate_loss(original, decompressed)**:
   - Calculates the percentage of data loss by comparing the original and decompressed binary data.

6. **load_image_to_binary(image_path)**:
   - Loads an image from the provided path and converts it to a binary string for compression.

7. **save_decompressed_image(binary_string, size, output_path)**:
   - Saves the decompressed binary string as an image at the specified output path.

8. **compress_and_decompress(image_path, output_path)**:
   - The main function that orchestrates the compression and decompression process. It handles the loading of the image, application of the compression algorithms, and saving the decompressed image.

## Results (Sample Output)

After running the algorithm, the following results are generated for the image compression process:

- **Compressed Data (Grammars)**:  
  Example: `AAAAAAAAAAAAAAAAAAAAAAADAKKKKKKKKKKADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...`

- **Compressed Data (Sequences)**:  
  Example: `24ADA10KAD98AD49AC3AC2AC2ACACACACACASASASACACACACACACACACACACACACACAJASASASASJAC2ACAC15ADAD2AD10AZ33...`

- **Compression Ratio**: 68.89%

- **Loss Percentage**: 0.00%

These results demonstrate the high effectiveness of the compression algorithm, achieving a compression ratio of **68.89%** with no data loss (**0.00%** loss).

## Requirements

- Python 3.x
- **Pillow** library for image processing: Install using `pip install Pillow`
- **NumPy** library for array manipulation: Install using `pip install numpy`

## How to Use

1. Clone or download this repository.
2. Ensure that you have the required dependencies (`Pillow` and `NumPy`).
3. Update the path to your image file in the script (variable `image_path`).
4. Run the script to compress and decompress the image:
   ```bash
   python compress_and_decompress.py
   ```
5. The decompressed image will be saved to the path specified in `output_path`.

## Limitations (First Version)

- The grammar rules are predefined, and their efficiency may vary depending on the input data. Further optimization could improve compression performance.
- The algorithm is primarily designed for **binary images**. Support for other image types may require additional processing steps.
- As this is the first version, further testing and optimization are needed to improve scalability and runtime performance for larger datasets.

## Conclusion

This compression algorithm demonstrates an effective approach to compressing binary image data using both grammar-based and sequence-based methods. The implementation ensures that the original data is perfectly recoverable after decompression with no loss.

Future improvements can include optimizing the grammar rules, enhancing performance for larger files, and extending support for various data types beyond binary images.
