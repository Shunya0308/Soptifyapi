import os

from spotifyclient import SpotifyClient


def main():
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                    os.getenv("SPOTIFY_USER_ID"))

    # get last played tracks
    num_tracks_to_visualise = int(input("直前に聴いた曲を何曲反映したいですか? "))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

    print(f"\nこれが最後にあなたがSpotifyで聞いた {num_tracks_to_visualise} 曲です。:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")

    # choose which tracks to use as a seed to generate a playlist
    indexes = input("\n起点にしたい曲を5つまで選択してください。曲の合間はスペースで区切ってください。: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    # get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nこの50曲をプレイリストに挿入します。:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    # get playlist name from user and create playlist
    playlist_name = input("\nプレイリストの名前は? :")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nプレイリスト名 '{playlist.name}' 新規作成完了!")

    # populate playlist with recommended tracks
    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nプレイリスト名'{playlist.name}'が正常にアップロードされました。")


if __name__ == "__main__":
    main()