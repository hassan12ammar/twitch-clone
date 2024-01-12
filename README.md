# twitch-clone
project for Hurry Up Hackathon 

## Installation

### Creaate venv
```bash
python -m venv venv
```

### Activate venv
```bash
source venv/bin/activate
```
### Install requirements
```bash
pip install -r requirements.txt
```

### Make migrations
```bash
python manage.py makemigrations
```

### Apply migrations
```bash
python manage.py migrate
```

## Usage
### Create SuperUser
```bash
python manage.py createsuperuse
```

### Run the server
```bash
python manage.py runserver
```

## Authentication 
Users can register (/api/signup) to create an account, authenticate (/api/signin) to access their account, retrieve a list of all profiles (/api/get_all_profile), and obtain their own profile (/api/get_profile). Authenticated users can also create (/api/create_profile) and edit (/api/edit_profile) their profiles. Responses include HTTP status codes and relevant data objects such as SigninUpOut, AuthOut, ProfileOut, and MessageOut to indicate successful operations or provide error details.
