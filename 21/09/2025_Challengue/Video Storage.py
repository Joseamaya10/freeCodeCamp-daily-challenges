units = {
   "B" : 1,
   "KB" : 1000,
   "MB" : 1000000,
   "GB"	: 1000000000,
   "TB"	: 1000000000000
}
def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit in ["B", "KB", "MB", "GB", "TB"] and drive_unit in ["GB", "TB"]:
        amount_videos = (drive_size * units[drive_unit]) / (video_size * units[video_unit])
        if int(amount_videos) > 4000:
            return "Invalid video unit"
        return int(amount_videos)
    else:
        return "Invalid drive unit"
print(number_of_videos(500, "MB", 100, "GB"))
print(number_of_videos(2000, "B", 1, "TB"))
print(number_of_videos(2000, "MB", 100000, "MB"))
print(number_of_videos(500000, "KB", 2, "TB"))
print(number_of_videos(1.5, "GB", 2.2, "TB"))