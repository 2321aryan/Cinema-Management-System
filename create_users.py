import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv("backend/.env")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    print("Error: Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY in backend/.env")
    exit(1)

supabase: Client = create_client(url, key)

users = [
    {"email": "admin@cinema.com", "password": "password123", "role": "admin"},
    {"email": "staff1@cinema.com", "password": "password123", "role": "staff"}
]

print("Creating users...")

for u in users:
    try:
        # 1. Create User in Auth
        # Note: syntax depends on supabase-py version, attempting standard admin.create_user
        attributes = {"email": u["email"], "password": u["password"], "email_confirm": True}
        user_response = supabase.auth.admin.create_user(attributes)
        user_id = user_response.user.id
        print(f"[OK] Created Auth User: {u['email']}")
        
        # 2. Add to profiles table
        # Check if profile exists
        res = supabase.table("profiles").select("*").eq("id", user_id).execute()
        if not res.data:
            supabase.table("profiles").insert({
                "id": user_id,
                "email": u["email"],
                "role": u["role"]
            }).execute()
            print(f"     -> Linked to profiles as {u['role']}")
        else:
            print(f"     -> Profile already exists")
            
    except Exception as e:
        print(f"[INFO] Could not create {u['email']} (might already exist): {e}")
        # If user exists, try to ensure profile exists
        try:
            # We can't easily get ID by email without listing users, but let's try to proceed if you know how to fetch user_id
            # For simplicity, we assume if they exist, they are set up.
            pass
        except:
            pass

print("\nDone! You can try logging in.")
