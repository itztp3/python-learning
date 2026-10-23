def organize_file(filename):
    extension = filename.lower().split(".")[-1]

    categories = {
        "Images": ["jpg", "jpeg", "png", "gif"],
        "Documents": ["pdf", "docx", "txt", "doc"],
        "Videos": ["mp4", "mkv", "avi"],
        "Audio": ["mp3", "wav"],
        "Programs": ["py", "exe", "java"]
    }

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Other Files"


print("===== SMART FILE ORGANIZER =====")

files = [
    "photo.jpg",
    "notes.pdf",
    "movie.mp4",
    "song.mp3",
    "project.py",
    "data.xyz"
]

for filename in files:
    category = organize_file(filename)
    print(filename, "->", category)
