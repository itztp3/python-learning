import os
import hashlib

def get_file_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except Exception as e:
        print("Error:", e)
        return None


def find_duplicates(folder_path):
    file_hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):

        for filename in files:
            file_path = os.path.join(root, filename)

            file_hash = get_file_hash(file_path)

            if file_hash:
                if file_hash in file_hashes:
                    duplicates.append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    return duplicates


folder = input("Enter folder path: ")

if os.path.isdir(folder):
    result = find_duplicates(folder)

    print("\n===== DUPLICATE FILE REPORT =====")

    if result:
        for file in result:
            print("Duplicate:", file)
    else:
        print("No duplicate files found!")

    print("\nTotal duplicates:", len(result))

else:
    print("Invalid folder path!")