from pathlib import Path

for i in range(1, 101):
    folder_name = f"Day_{i}"

    Path.mkdir(folder_name, parents=True, exist_ok=True)

print("Successfully created 100 days' folders! 🎉")