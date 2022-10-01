# nsac2022-Junonian

starting to work with: 
(creating virtual env)
- python -m venv ./venv/

(installing requirements)
- pip install -r requirements.txt

- python manage.py makemigrations
- python manage.py migrate

(creating superuser)
- python manage.py createsuperuser

(running server)
- python manage.py runserver


urls:
  admin page:
    localhost/admin
  
  adding images (r, g, b):
    localhost/api/rgb_add/
    {image_r: *image*
     image_g: *image*
     image_b: *image*
     }
    #### django should scrap those images from a form(needs to be tested)

  getting images: 
    localhost/api/rgb_get/
    ##### returns a json dict with lists of image urls 
    
    
    
    
