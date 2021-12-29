from pytube import YouTube
from tkinter import *

window = Tk()
window.geometry("700x600")
window.config(bg="red")
window.title("YOUTUBE video downloader")

youtube_logo = PhotoImage(file= "download.png")
window.iconphoto(False, youtube_logo)

Label(window, text= "Video Downloader", font= ("Arial 30 bold"),bg= "red", fg= "black").pack(padx= 6, pady= 50)

video_link = StringVar()

Label(window, text="Enter the link:", bg="red", font= ("Arial 25 bold")).place(x=250, y=110)
link = Entry(window, width=50, font=35, textvariable=video_link,bd= 4).place(x= 115,y =200)

def video_download():
    url = YouTube(str(video_link.get()))
    video = url.streams.get_highest_resolution()
    video.download(output_path="/Users/mostafa_bashir/Desktop")
    Label(window, text="Download Completed",font= ("Arial 45 bold"), bg="red", fg="black").place(x=140, y=350)
    Label(window, text="Check your Desktop", font=("Arial 45 bold"), bg="red", fg="black").place(x=140, y=400)

Button(window, text= "Download",font=("Arial 25 bold"), bg="white", fg="black", command=video_download).place(x= 300,y= 300)



window.mainloop()
"""def done():
    print("done")

#link = input("please insert the url of the video to download it: ")

video = youtube(link)

video.streams.get_highest_resolution().download(output_path="/users/mostafa_bashir/desktop")
video.register_on_complete_callback(done())
"""