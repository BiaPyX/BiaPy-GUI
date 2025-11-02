from datetime import datetime, timezone, timedelta

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
creds = Credentials.from_service_account_file('sa.json', scopes=['https://www.googleapis.com/auth/drive'])
svc = build('drive','v3',credentials=creds, cache_discovery=False)

print("Google Drive Quota:")
about = svc.about().get(fields="storageQuota").execute()
q = about["storageQuota"]
print("Total:", int(q["limit"])/1e9, "GB")
print("Used:", int(q["usage"])/1e9, "GB")
print("Used in Drive:", int(q["usageInDrive"])/1e9, "GB")
print("Trash:", int(q.get("usageInDriveTrash", 0))/1e9, "GB")

cutoff = datetime.now(timezone.utc) - timedelta(days=14)
q = "'me' in owners and trashed = false"
page_token = None
to_delete = []

while True:
    resp = svc.files().list(
        q=q,
        fields="nextPageToken, files(id,name,createdTime,size)",
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
        orderBy="createdTime",
        pageToken=page_token,
        pageSize=1000,
    ).execute()
    for f in resp.get("files", []):
        ct = datetime.fromisoformat(f["createdTime"].replace("Z","+00:00"))
        if ct < cutoff:   # or: if f["name"].endswith(".zip"): ...
            to_delete.append(f)
    page_token = resp.get("nextPageToken")
    if not page_token:
        break

print(f"Will delete {len(to_delete)} files")
for f in to_delete:
    print("Deleting", f["name"], f["id"])
    svc.files().delete(fileId=f["id"]).execute()  # permanent delete


svc.files().emptyTrash().execute()

print("After cleanup:")
about = svc.about().get(fields="storageQuota").execute()
q = about["storageQuota"]
print("Total:", int(q["limit"])/1e9, "GB")
print("Used:", int(q["usage"])/1e9, "GB")
print("Used in Drive:", int(q["usageInDrive"])/1e9, "GB")
print("Trash:", int(q.get("usageInDriveTrash", 0))/1e9, "GB")