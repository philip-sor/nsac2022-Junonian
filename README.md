# nsac2022-Junonian
### This is the back-end part of application for NASA Space Apps Chalange 
### Chalange name: VISUALIZING THE JOVIAN SYSTEM LIKE NEVER BEFORE
### Team name: Junonian
### Application name: Junonian
#### ?future hosting domain?: junonian.earth 


#### front-end part: https://github.com/ivan-hryshko/nsac2022-frontend

# About
... 



# starting to work with: 
(creating virtual env)
- python -m venv ./venv/

*for mac/linux:*
- source venv/bin/activate 

*for Windows:*
- ./venv/bin/activate

(installing requirements)
- pip install -r requirements.txt

- python manage.py makemigrations
- python manage.py migrate

(creating superuser)
- python manage.py createsuperuser

(running server)
- python manage.py runserver


# urls:
  - admin page:
    - localhost/admin
  
  - adding images (r, g, b):
    - localhost/api/rgb_add/
    {image_r: *image*
     image_g: *image*
     image_b: *image*
     metadata: *metadata* (optional)
     }
     ##### django should scrap those images from a form(needs to be tested)

  - getting r, g, b images: 
    - localhost/api/rgb_list/
     ##### returns a json dict with lists of r,g,b image urls 
    
  - getting combined images:
    - localhost/api/combined_list/
     ##### returns a json dict with all combined photoes
    
    - localhost/api/combined_get/{from_images_id}
     ##### {from_images_id} is id of an object with r, g, b images from which combined photo was made.
    
     ##### returns specified combined image
    
    
    
    
