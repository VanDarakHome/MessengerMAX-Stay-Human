import json



class GameEngine:

    
    def __init__(self, map_file='locations.json'):
        self.load_map(map_file)
        self.current_location = 'start'
        self.visited_locations = ['start']

    
    def load_map(self, map_file):
        with open(map_file, 'r', encoding='utf-8') as f:
            self.game_map = json.load(f)

    
    def get_current_location_info(self):
        location = self.game_map[self.current_location]
        return {
            'id': location['id'],
            'name': location['name'],
            'next': location.get('next', []),
            'is_finish': 'finish' in location,
            'finish_type': location.get('finish')
        }

    
    def get_available_moves(self):
        current_info = self.get_current_location_info()
        spisok = [] 
        for i in current_info['next']:
            location = self.game_map[i]
            spisok.append({
                'id': location_id,
                'name': location['name']
            }) 
        return spisok

    
    def move_to(self, location_id):
        current_info = self.get_current_location_info()
        if location_id in current_info['next']:
            self.current_location = location_id
            if location_id not in self.visited_locations:
                self.visited_locations.append(location_id)
            return True
        else:
            return False

    
    def is_game_finished(self):
        return self.get_current_location_info()['is_finish']

    
    def get_game_result(self):
        if self.is_game_finished():
            return self.get_current_location_info()['finish_type']
        return None

    
    def get_visited_locations(self):
        return [self.game_map[i]['name'] for i in self.visited_locations]

    
    def reset_game(self):
        self.current_location = 'start'
        self.visited_locations = ['start']
