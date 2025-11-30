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

print("=====================================")
print("CleanWindows                         ")
print("This script is cleaning              ")
print("following folders                    ")
print("=====================================")

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
print("=====================================")


# Summary Output
print("Summary                              ")
print("=====================================")
print(f"Total items deleted: {deleted_items}")
print(f"Items skipped:       {skipped_items}")
print("=====================================")
print("✔ Cleaning complete!")
print("Thank you!")


# Professional Footer
print("=====================================")
print("Prepared by Golam Oyalieul Hasan     ")
print("Implemented in Python                ")
print("Requests Admin privileges            ")
print("via Windows manifest                 ")
print("For support or feedback              ")
print("contactoyalieul@gmail.com            ")
print("=====================================\n")

# Pause so console stays open
input("\nPress Enter to exit...")