from requests_api import RequestsCollector
from database_manager import DatabaseManager
from algorithm_functions import solve_algorithm

if __name__ == '__main__':
    rc = RequestsCollector()
    with DatabaseManager() as db:
        db.create_database()
        maps = rc.get_maps()
        coords = rc.get_coords()

        algorithm_res = solve_algorithm(maps, coords)

        db.add_data(algorithm_res)

