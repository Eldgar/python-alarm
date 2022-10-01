import pafy
import vlc
import random

music_list = []

with open('music.txt', 'r') as f:
     music_list = [line.rstrip() for line in f]
f.close()
#print(music_list)


def play_song(url):
    is_opening = False
    is_playing = False

    video = pafy.new(url)
    best = video.getbestaudio()
    play_url = best.url

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()
    player.set_media(media)
    player.play()

    good_states = [
    	"State.Playing", 
    	"State.NothingSpecial", 
    	"State.Opening"
    ]
    
    while str(player.get_state()) in good_states:
        if str(player.get_state()) == "State.Opening" and is_opening is False:
            print("Status: Loading")
            is_opening = True

        if str(player.get_state()) == "State.Playing" and is_playing is False:
            print("Status: Playing")
            is_playing = True

    print("Status: Finish")
    player.stop()

#play_song(music_list[random.randint(0, len(music_list)-1)])