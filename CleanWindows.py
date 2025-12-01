import os
import shutil
import getpass

# Get username automatically
user = getpass.getuser()

# Safe folders to clean
paths = [
    f"C:/Users/{user}/AppData/Local/Temp",
    "C:/Windows/Temp",
    "C:/Windows/Prefetch",
    "C:/Windows/Logs"
]

print("CleanWindows\n")
print("This script is cleaning following folders")


deleted_items = 0
skipped_items = 0

for path in paths:
    print(f"{path}")
    
    if os.path.exists(path):
        try:
            items = os.listdir(path)
        except PermissionError:
            print(f"[Skipped] Cannot access: {path}")
            skipped_items += 1
            continue

        for item in items:
            item_path = os.path.join(path, item)

            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    if not os.path.exists(item_path):
                        deleted_items += 1
                    else:
                        skipped_items += 1

                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    if not os.path.exists(item_path):
                        deleted_items += 1
                    else:
                        skipped_items += 1

                else:
                    skipped_items += 1  # Not a file or folder

            except:
                skipped_items += 1

    else:
        print(f"[Not Found] {path}")

# Summary Output
print("\nSummary")
print(f"Items deleted: {deleted_items}")
print(f"Items skipped: {skipped_items}\n")
print("Cleaning complete! Thank you!\n")


# Professional Footer
print("Prepared by Golam Oyalieul Hasan. Implemented in Python")
print("Requests Admin privileges via Windows manifest")
print("For support or feedback, contact me at contactoyalieul@gmail.com\n")

# Pause so console stays open
input("\nPress Enter to exit...")