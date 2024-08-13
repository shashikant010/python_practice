import json
def load_data():
    try:
        with open('./youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print (f"{index}. {video["name"]} , Duratin : {video["time"]}")

def add_video(videos):
    name= input("Enter video Name: ")
    time= input("Enter video time: ")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update"))
    if 1<=index<=len(videos):
        name=input("Enter new name")
        time=input("Enter new time")
        videos[index-1]={"name":name,"time":time}
        save_data_helper(videos)
    else:
        print("invalid index")
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to delete"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid index")


def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | Choose a option")
        print("1. List all Youtube videos ")
        print("2. Add a youtube video")
        print("3. Update a youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the app")
        choice=input("Enter your choice")
        print(videos)
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__=="__main__":
    main()