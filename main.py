import instaloader
insta = instaloader.Instaloader()
acc = input("acc")
insta.download_profile(acc, profile_pic_only=False)
