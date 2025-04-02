import requests
import datetime
import os

# GitHub repository and token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Reads from Jenkins environment
REPO_OWNER = "atomeMIF"  # Your GitHub username
REPO_NAME = "Random_C"  # Your repository name

# Generate release details
now = datetime.datetime.now()
tag_name = f"v{now.strftime('%Y%m%d_%H%M%S')}"  # e.g., v20250402_123000
release_name = f"Release {now.strftime('%Y-%m-%d %H:%M:%S')}"

# Create a release
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
release_data = {
    "tag_name": tag_name,
    "name": release_name,
    "body": "Automated release by Jenkins",
    "draft": False,
    "prerelease": False
}
response = requests.post(
    f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases",
    headers=headers,
    json=release_data
)
if response.status_code == 201:
    print("Release created successfully!")
    release = response.json()
    upload_url = release["upload_url"].split("{")[0]

    # Upload the executable
    with open("Random_C", "rb") as file:
        upload_headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Content-Type": "application/octet-stream"
        }
        upload_response = requests.post(
            f"{upload_url}?name=Random_C",
            headers=upload_headers,
            data=file
        )
        if upload_response.status_code == 201:
            print("Executable uploaded successfully!")
        else:
            print(f"Failed to upload executable: {upload_response.status_code}")
else:
    print(f"Failed to create release: {response.status_code}")

