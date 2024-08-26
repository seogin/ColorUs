# ColorUs

## Installation

Prerequisite: Install Homebrew

```
brew install cmake
pip install -r requirements.txt
```
## 📖 Project Description



## 💞 Names of Contributors

- Seogin Hong ([@seogin](https://github.com/seogin))
- Shawn Rim ([@Shawn-Rim](https://github.com/Shawn-Rim))
- David (Sungjin) Suh ([@SungJin-Suh](https://github.com/SungJin-Suh))


## 💻 Technologies and Resources Used

List technologies (with version numbers).

- Python
- JavaScript, CSS
- [Tailwind v3.4.3](https://tailwindcss.com/)
- [React v18.3.3](https://react.dev/)
- [dlib v19.24.4](https://pypi.org/project/dlib/)
- [sklearn v1.5.0](https://scikit-learn.org/stable/)
- [Pandas v2.2.2](https://pandas.pydata.org/)
- [Numpy v1.26.4](https://numpy.org/)
- [opencv-python v4.10.0.84](https://opencv.org/)
- [Flask v3.0.3](https://flask.palletsprojects.com/en/3.0.x/)
- [google_images_download v2.8.0](https://pypi.org/project/google_images_download/)
- [Selenium v4.22.0](https://www.selenium.dev/)


### Image Resources Used

- [Google Images](https://images.google.com/)

## ⚙️ Complete setup/installion/usage

Here's how to get started once you've cloned the project:

- Download [VS Code](https://code.visualstudio.com/)
- Download cmake (https://cmake.org/download/)
- Navigate to personal_color directory folder
- ```pip/pip3 install -r requirements.txt```
- Run Flask using ```flask run``` on terminal
- Navigate to react directory
- npm i: Install all dependencies
- Run React using ```npm run dev``` on different terminal


### Usage

- Upload a 


## 🪲 Known Bugs and Limitations

- Layout optimized for iPhone 14 Pro Max environment

## 🔮 Features for Future

- Integration with real-time criminal data APIs to provide up-to-date and localized crime information.
- AI-driven recommendations for protection services tailored to specific crime patterns and user location data.

## 📂 Contents of Project Folder

###     Top level of project folder:
```
├── .gitignore          # Git ignore file
├── index.html
├── main.py
├── personalColor.pickle
├── personalColor2.pickle
└── README.md           # Project overview, instructions, and documentation
```

### Subfolders and files:
```
├── .idea                  
│   ├── inspectionProfiles
│   │   ├── profiles_settings.xml
│   │   └── Project_Default.xml
│   ├── .gitignore
│   ├── ColorUs.iml
│   ├── misc.xml
│   ├── modules.xml
│   └── vsc.xml
├── csv_file                   
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── data.cpython-312.pyc
│   ├── data.py
│   ├── data1.csv
│   └── data2.csv
├── etc
│   ├── chatGPT_models.py
│   ├── color_extract_new.py
│   ├── detect_face_new.py
│   ├── modify_img.py
│   ├── personal.py
│   ├── scrape_images.py
│   └── tone_analysis.py
├── personal_color                  
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── data.cpython-312.pyc
│   │   ├── color_converter.cpython-312.pyc
│   │   ├── color_extract.cpython-312.pyc
│   │   ├── detect_face.cpython-312.pyc
│   │   └── personal_color.cpython-312.pyc
│   ├── app.py
│   ├── color_converter.py
│   ├── color_extract.py
│   ├── ColorUs.code-workspace
│   ├── detect_face.py
│   ├── personal_color.py
│   ├── requirements.txt
│   └── shape_predictor_68_face_landmarks.dat
├── react                    
│   ├── components            
│   │   ├── fall.jsx                   
│   │   ├── spring.jsx                  
│   │   ├── summer.jsx
│   │   └── winter.jsx   
│   ├── public  
│   │   ├── background_image.png
│   │   └── vite.svg            
│   ├── src     
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx             
│   ├── .eslintrx.cjs                    
│   ├── .gitignore
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   └── vite.config.js
└── src                    
    ├── fall          
    ├── spring          
    ├── summer
    └── winter 
```
