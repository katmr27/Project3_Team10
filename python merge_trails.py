import pandas as pd
import json
import os
from difflib import SequenceMatcher

def clean_trail_name(name):
    """Clean trail names for better matching"""
    cleaned = name.lower()
    # Remove common suffixes and words
    removals = [
        ' hike', ' trail', ' loop', ' point', ' falls',
        '[closed]', 'via', 'to', 'and', 'upper', 'lower',
        'state park', 'loop trail', 'hiking trail',
        'viewpoint', 'overlook', 'scenic', 'area'
    ]
    for text in removals:
        cleaned = cleaned.replace(text, '')
    
    # Standardize separators
    cleaned = cleaned.replace('-', ' ').replace('/', ' ').replace(':', ' ')
    # Remove double spaces and trim
    cleaned = ' '.join(cleaned.split())
    return cleaned.strip()

def similarity_score(name1, name2):
    """Calculate similarity between two names"""
    # Direct string similarity
    sequence_similarity = SequenceMatcher(None, name1, name2).ratio()
    
    # Word set similarity
    words1 = set(name1.split())
    words2 = set(name2.split())
    common_words = words1.intersection(words2)
    total_words = len(words1.union(words2))
    word_similarity = len(common_words) / total_words if total_words > 0 else 0
    
    return max(sequence_similarity, word_similarity)

def names_match(name1, name2):
    """Check if two trail names match using multiple criteria"""
    clean1 = clean_trail_name(name1)
    clean2 = clean_trail_name(name2)
    
    # Direct match after cleaning
    if clean1 == clean2:
        return True, 1.0
    
    # One name contains the other
    if clean1 in clean2 or clean2 in clean1:
        return True, 0.9
    
    # Calculate similarity score
    similarity = similarity_score(clean1, clean2)
    
    # Return match if similarity is high enough
    if similarity >= 0.6:  # Lower threshold for more matches
        return True, similarity
    
    return False, 0

def get_default_coordinates(trail_name):
    """Assign default coordinates based on trail location hints in the name"""
    name_lower = trail_name.lower()
    
    if any(word in name_lower for word in ['klickitat', 'lyle', 'swale']):
        return {'latitude': 45.8500, 'longitude': -121.1500}
    elif any(word in name_lower for word in ['cascade', 'locks']):
        return {'latitude': 45.6685, 'longitude': -121.8935}
    elif any(word in name_lower for word in ['hood', 'larch', 'mount']):
        return {'latitude': 45.3737, 'longitude': -121.6960}
    else:
        return {'latitude': 45.7253, 'longitude': -121.7300}

def merge_trail_data(json_path, csv_path, output_path=None):
    # Read JSON file and extract only trail names and coordinates
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    # Create coordinates lookup dictionary from JSON
    coordinates = {}
    for trail in json_data:
        if '_geoloc' in trail:
            coordinates[trail['name']] = {
                'latitude': round(trail['_geoloc']['lat'], 6),
                'longitude': round(trail['_geoloc']['lng'], 6)
            }
    
    # Read original CSV file
    csv_df = pd.read_csv(csv_path)
    
    # Print some debugging information
    print("\nDebugging information:")
    print(f"Number of trails in JSON: {len(json_data)}")
    print(f"Number of trails in CSV: {len(csv_df)}")
    
    # Manual matches dictionary (expanded with more accurate matches)
    manual_matches = {
        'Balfour-Klickitat Loop Hike': 'Klickitat Trail',
        'Cape Horn Overlooks Hike': 'Cape Horn Trail',
        'Cascade Locks West Loop Hike': 'Bridge of the Gods Trail',
        'Catherine Creek Universal Access Hike': 'Catherine Creek',
        'Catherine Creek West Loop Hike': 'Catherine Creek Loop',
        'Catherine Creek-Rowland Basin Loop Hike': 'Catherine Creek Trail',
        'Chenoweth Tableland Loop Hike': 'Chenoweth Ridge',
        'Columbia Gorge Traverse Hike': 'Gorge Trail',
        'Coyote Wall Hike': 'Coyote Wall',
        'Fairy Falls Loop Hike': 'Wahkeena Falls Loop',
        'Labyrinth Hike': 'Labyrinth and Coyote Wall Loop',
        'She Who Watches Hike': 'Horsethief Butte',
        'Ponytail Falls Hike': 'Horsetail Falls Trail',
        'Mosier Twin Tunnels Hike': 'Historic Columbia River Highway State Trail',
        'Hood River Waterfront Hike': 'Hood River Pipeline Trail',
        'Eagle Creek to Punch Bowl Falls Hike': 'Eagle Creek Trail',
        'Elowah Falls Loop Hike': 'Elowah Falls',
        'Horsetail Falls Loop Hike': 'Horsetail Falls Loop',
        'Wind Mountain Hike': 'Wind Mountain Trail'
    }
    
    # Add latitude and longitude columns
    csv_df['latitude'] = None
    csv_df['longitude'] = None
    
    matches = 0
    for index, row in csv_df.iterrows():
        csv_name = row['trail_name']
        matched = False
        
        # Try manual matches first
        if csv_name in manual_matches:
            json_name = manual_matches[csv_name]
            if json_name in coordinates:
                csv_df.at[index, 'latitude'] = coordinates[json_name]['latitude']
                csv_df.at[index, 'longitude'] = coordinates[json_name]['longitude']
                matches += 1
                if matches <= 10:
                    print(f"\nFound manual match:")
                    print(f"  CSV name: {csv_name}")
                    print(f"  JSON name: {json_name}")
                matched = True
        
        # If no manual match, try fuzzy matching
        if not matched:
            best_match = None
            best_score = 0
            best_coords = None
            
            for json_name, coords in coordinates.items():
                is_match, score = names_match(csv_name, json_name)
                if is_match and score > best_score:
                    best_match = json_name
                    best_score = score
                    best_coords = coords
            
            if best_match and best_coords:
                csv_df.at[index, 'latitude'] = best_coords['latitude']
                csv_df.at[index, 'longitude'] = best_coords['longitude']
                matches += 1
                if matches <= 10:
                    print(f"\nFound fuzzy match (similarity: {best_score:.2f}):")
                    print(f"  CSV name: {csv_name}")
                    print(f"  JSON name: {best_match}")
                matched = True
        
        # Use default coordinates as last resort
        if not matched:
            default_coords = get_default_coordinates(csv_name)
            csv_df.at[index, 'latitude'] = default_coords['latitude']
            csv_df.at[index, 'longitude'] = default_coords['longitude']
            print(f"Using default coordinates for: {csv_name}")
    
    # Generate output path if not provided
    if output_path is None:
        output_dir = os.path.dirname(csv_path)
        output_path = os.path.join(output_dir, 'merged_trails.csv')
    
    # Save to CSV
    csv_df.to_csv(output_path, index=False)
    
    return {
        'total_trails': len(csv_df),
        'trails_with_matches': matches,
        'trails_with_defaults': len(csv_df) - matches,
        'output_path': output_path
    }

if __name__ == "__main__":
    # File paths
    json_path = r"C:\Users\riley\School Challenges\Project3_Team10\Oregon (1).json"
    csv_path = r"C:\Users\riley\School Challenges\Project3_Team10\resources\cleaned_data\all_trails_data_clean_df.csv"
    
    try:
        # Change this line from all_trail_merge_data to merge_trail_data
        results = merge_trail_data(json_path, csv_path)
        print(f"\nMerge completed successfully!")
        print(f"Total trails in dataset: {results['total_trails']}")
        print(f"Trails with matched coordinates: {results['trails_with_matches']}")
        print(f"Trails using default coordinates: {results['trails_with_defaults']}")
        print(f"\nMerged data saved to: {results['output_path']}")
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")