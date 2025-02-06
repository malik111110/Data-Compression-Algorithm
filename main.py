from PIL import Image
import numpy as np

# Définition des grammaires affinées pour une meilleure compression
grammars = {
    1: {'C': '0', 'D': '1'},
    2: {'A': 'CD', 'B': 'DC', 'S': 'CC', 'K': 'DD'},
    3: {'H': 'CDC', 'I': 'CK', 'P': 'DCD', 'L': 'DS', 'J': 'SC', 'M': 'SD', 'O': 'KC', 'Z': 'KD'},
    4: {'U': 'HCD', 'V': 'ICD', 'W': 'LCK', 'X': 'JSD', 'Y': 'PKC', 'Q': 'ZDS'},
    5: {'E': 'UVW', 'N': 'XYZ', 'R': 'QVU', 'T': 'WYX', 'F': 'VQU', 'G': 'TWR'},
    6: {'AA': 'UEV', 'BB': 'VWX', 'CC': 'XQY', 'DD': 'YZN', 'EE': 'RWF', 'FF': 'GTU'},
    7: {'GG': 'AABB', 'HH': 'CCDD', 'II': 'EEFF', 'JJ': 'GGHH', 'KK': 'IIJJ'},
    8: {'LL': 'GGKK', 'MM': 'HHJJ', 'NN': 'LLMM', 'OO': 'NNLL', 'PP': 'MMOO'},
    9: {'QQ': 'LLNN', 'RR': 'OOPP', 'SS': 'QQRR', 'TT': 'SSQQ', 'UU': 'RRSS'},
    10: {'VV': 'UUTT', 'WW': 'VVUU', 'XX': 'WWVV', 'YY': 'XXWW', 'ZZ': 'YYXX'},
}

# Fonction pour appliquer les règles de compression avec indexation de manière récursive
def apply_compression(data, grammars):
    applied_grammars = []
    changed = True
    while changed:
        changed = False
        for level in sorted(grammars.keys()):
            rules = grammars[level]
            for symbol, pattern in rules.items():
                if pattern in data:
                    data = data.replace(pattern, symbol)
                    applied_grammars.append(level)
                    changed = True
    return data, applied_grammars

# Fonction pour appliquer la compression par comptage de séquences
def sequence_compression(data):
    compressed = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        compressed += (str(count) if count > 1 else '') + data[i]
        i += 1
    return compressed

# Fonction pour décompresser les données en utilisant les index des grammaires
def apply_decompression(data, grammars, applied_grammars):
    for level in sorted(set(applied_grammars), reverse=True):
        rules = grammars[level]
        for symbol, pattern in rules.items():
            data = data.replace(symbol, pattern)
    return data

# Fonction pour décompresser les données compressées par comptage de séquences
def sequence_decompression(data):
    decompressed = ""
    i = 0
    while i < len(data):
        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        decompressed += data[i] * (int(count) if count else 1)
        i += 1
    return decompressed

# Calcul de la perte de données
def calculate_loss(original, decompressed):
    original_bits = len(original)
    decompressed_bits = len(decompressed)
    min_length = min(original_bits, decompressed_bits)
    difference = sum(1 for o, d in zip(original[:min_length], decompressed[:min_length]) if o != d)
    loss_percentage = (difference / original_bits) * 100
    return loss_percentage

# Charger et convertir l'image en binaire
def load_image_to_binary(image_path):
    image = Image.open(image_path).convert('1')  # Convertir en noir et blanc
    binary_array = np.array(image).flatten()
    binary_string = ''.join(['0' if pixel == 0 else '1' for pixel in binary_array])
    return binary_string, image.size

# Sauvegarder l'image décompressée
def save_decompressed_image(binary_string, size, output_path):
    expected_length = size[0] * size[1]
    if len(binary_string) < expected_length:
        binary_string += '0' * (expected_length - len(binary_string))  # Compléter avec des zéros
    elif len(binary_string) > expected_length:
        binary_string = binary_string[:expected_length]  # Tronquer à la longueur attendue

    binary_array = np.array([int(bit) * 255 for bit in binary_string], dtype=np.uint8)
    image_array = binary_array.reshape((size[1], size[0]))
    Image.fromarray(image_array).save(output_path)

# Fonction principale de compression et décompression
def compress_and_decompress(image_path, output_path):
    # Convertir l'image en binaire
    binary_string, image_size = load_image_to_binary(image_path)

    # Compression par grammaires
    compressed_data, applied_grammars = apply_compression(binary_string, grammars)
    print(f'Données compressées (grammaires) : {compressed_data[:100]}...')

    # Compression par séquences
    final_compressed_data = sequence_compression(compressed_data)
    print(f'Données compressées (séquences) : {final_compressed_data[:100]}...')

    # Décompression
    sequence_decompressed = sequence_decompression(final_compressed_data)
    decompressed_data = apply_decompression(sequence_decompressed, grammars, applied_grammars)

    # Sauvegarder l'image décompressée
    save_decompressed_image(decompressed_data, image_size, output_path)

    # Calcul du taux de compression
    original_size = len(binary_string)
    compressed_size = len(final_compressed_data)
    compression_ratio = (original_size - compressed_size) / original_size * 100
    print(f'Taux de compression : {compression_ratio:.2f}%')

    # Calcul de la perte de données
    loss_percentage = calculate_loss(binary_string, decompressed_data)
    print(f'Pourcentage de perte : {loss_percentage:.2f}%')

# Chemin de l'image d'origine
image_path = 'OIP (1).png'
output_path = 'decompressed_image.png'

# Exécution de la fonction principale
compress_and_decompress(image_path, output_path)


