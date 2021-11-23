import pathlib

BASE_DIR = pathlib.Path(__file__).parent

# Django import style.
# Or use class ..?
service_list = [
    'work_service'
]


# Way 2 
from work_service.service import Service as WorkSerivce
service_list = [
    WorkSerivce,
]
