# VideoEncoder - Fixed Version (Mangoi Compatible)

import logging
import os
import requests
import zipfile
import io

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO
)

# 🔹 CONFIG
UPSTREAM_REPO = "https://github.com/Harsha7668/datascience"
UPSTREAM_BRANCH = "SH24BOTS"


# 🔥 SAFE UPDATE FUNCTION (NO GIT, NO PERMISSION ISSUES)
def update_from_github():
    try:
        logging.info("Starting update from GitHub (ZIP method)...")

        zip_url = f"{UPSTREAM_REPO}/archive/refs/heads/{UPSTREAM_BRANCH}.zip"

        response = requests.get(zip_url)
        if response.status_code != 200:
            logging.error("Failed to download update!")
            return

        # Extract ZIP
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall("update_folder")

        # Find extracted folder
        extracted_folder = f"update_folder/datascience-{UPSTREAM_BRANCH}"

        # Copy files to current directory
        for root, dirs, files in os.walk(extracted_folder):
            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(".", os.path.relpath(src, extracted_folder))

                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                    fdst.write(fsrc.read())

        logging.info("✅ Successfully updated from GitHub (ZIP)")

    except Exception as e:
        logging.error(f"Update failed: {e}")


# 🚀 RUN UPDATE (optional - you can comment this if not needed)
if UPSTREAM_REPO:
    update_from_github()
