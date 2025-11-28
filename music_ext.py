import plistlib
import os 
# example for Unix based systems file paths 
# xml_file = os.path.expanduser('~/Music/Music/Music Library.xml')

xml_file_path = r"C:\Users\nened\Music\iTunes\iTunes Music Library.xml" 

def extract_music_data(xml_path):
    """
    Parses the Apple Music/iTunes Library XML file to extract song names and artists.
    """
    # 1. Check if the file exists
    if not os.path.exists(xml_path):
        print(f"Error: XML file not found at {xml_path}")
        return []

    try:
        # 2. Use plistlib to load the XML data into a Python dictionary
        with open(xml_path, 'rb') as f:
            library_data = plistlib.load(f)
            
    except Exception as e:
        print(f"Error reading or parsing XML file: {e}")
        return []

    # 3. The actual track data is usually under the 'Tracks' key
    tracks = library_data.get('Tracks', {})
    song_list = []

    # 4. Iterate through each track dictionary
    for track_id, track_info in tracks.items():
        # Check if the required keys exist and if it's a music file (not a video/podcast, etc.)
        if 'Name' in track_info and 'Artist' in track_info and track_info.get('Kind') != 'Home Video':
            song_list.append({
                'Name': track_info['Name'],
                'Artist': track_info['Artist']
            })

    return song_list

# --- MAIN EXECUTION ---
songs_and_artists = extract_music_data(xml_file_path)

if songs_and_artists:
    print(f"✅ Successfully extracted {len(songs_and_artists)} songs.\n")
    print("--- First 10 Songs ---")
    
    # Print the first 10 entries
    for i, song in enumerate(songs_and_artists[:10]):
        print(f"{i+1}. **{song['Name']}** by {song['Artist']}")
        
    print("----------------------")

# You can now process the full list 'songs_and_artists' further (e.g., save to CSV)
# import csv
# with open('my_apple_music_library.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Name', 'Artist']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(songs_and_artists)
