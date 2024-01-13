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
python manage.py createsuperuser
```

## Environment Setup

Before running the application, you need to set up your environment variables by creating a `.env` file in the root directory of the project. Below is an example of the required content for the `.env` file:

```env
# Django secret key for cryptographic signing.
SECRET_KEY=mysecretkey123
# Set DEBUG to True for development, and False for production.
DEBUG=True
```

### Run the server
```bash
python manage.py runserver
```

## Authentication 
Users can register (/api/signup) to create an account, authenticate (/api/signin) to access their account, retrieve a list of all profiles (/api/get_all_profile), and obtain their own profile (/api/get_profile). Authenticated users can also create (/api/create_profile) and edit (/api/edit_profile) their profiles. Responses include HTTP status codes and relevant data objects such as SigninUpOut, AuthOut, ProfileOut, and MessageOut to indicate successful operations or provide error details.

## Video Management
Perform video-related operations using the following API endpoints:
- Create a Video (/api/videos/create_video): Create a new video.
- Get All Videos (/api/videos/get_all_videos): Retrieve a list of all videos.
- Get Video by ID (/api/videos/get_video/{video_id}): Retrieve a specific video by its ID.
- Update Video (/api/videos/update_video/{video_id}): Update a specific video.
- Delete Video (/api/videos/delete_video/{video_id}): Delete a specific video.

Responses include relevant data objects such as VideoOut and MessageOut to indicate successful operations or provide error details. Authentication may be required for certain operations.
