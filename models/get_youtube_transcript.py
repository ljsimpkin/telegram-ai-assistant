from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    video_id = video_url.split("v=")[1]
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = " ".join([segment['text'] for segment in transcript_list])
    return transcript
