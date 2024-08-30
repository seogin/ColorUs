# ColorUs

## 📖 Project Description

A mobile-first web app that uses image classification AI model to classify an image of a person into 4 categories or personal colour based on the person's skin tone.

## 💞 Names of Contributors

-   Seogin Hong ([@seogin](https://github.com/seogin))
-   Shawn Rim ([@Shawn-Rim](https://github.com/Shawn-Rim))
-   David (Sungjin) Suh ([@SungJin-Suh](https://github.com/SungJin-Suh))

## 💻 Technologies and Resources Used

List technologies (with version numbers).

-   Python
-   JavaScript, CSS
-   [Tailwind v3.4.3](https://tailwindcss.com/)
-   [React v18.3.3](https://react.dev/)
-   [dlib v19.24.4](https://pypi.org/project/dlib/)
-   [sklearn v1.5.0](https://scikit-learn.org/stable/)
-   [Pandas v2.2.2](https://pandas.pydata.org/)
-   [Numpy v1.26.4](https://numpy.org/)
-   [opencv-python v4.10.0.84](https://opencv.org/)
-   [Flask v3.0.3](https://flask.palletsprojects.com/en/3.0.x/)
-   [google_images_download v2.8.0](https://pypi.org/project/google_images_download/)
-   [Selenium v4.22.0](https://www.selenium.dev/)

### Image Resources Used

-   [Google Images](https://images.google.com/)

## ⚙️ Complete setup/installion/usage

Here's how to get started once you've cloned the project:

-   Download [VS Code](https://code.visualstudio.com/)
-   Download cmake (https://cmake.org/download/)
-   Navigate to personal_color directory folder
-   `pip/pip3 install -r requirements.txt`
-   Run Flask using `flask run` on terminal
-   Navigate to react directory
-   npm i: Install all dependencies
-   Run React using `npm run dev` on different terminal

## 🪲 Known Bugs and Limitations

-   Layout optimized for iPhone 14 Pro Max environment, but have not tested on an actual phone.

## 🔮 Features for Future

-   Integrate usage of built-in camera to run the program.
-   Deployment.

## 📂 Contents of Project Folder

### Top level of project folder:

```
├── .gitignore          # Git ignore file
├── index.html          # Test for frontend
├── main.py
├── personalColor.pickle    # Trained model (More accurate)
├── personalColor2.pickle   # Trained model
└── README.md           # Project overview, instructions, and documentation
```

### Subfolders and files:

```
├── csv_file            # Extracted data
│   ├── data.py
│   ├── data1.csv
│   └── data2.csv
├── etc                 # Unused, but important files
│   ├── chatGPT_models.py
│   ├── color_extract_new.py
│   ├── detect_face_new.py
│   ├── modify_img.py
│   ├── personal.py
│   ├── scrape_images.py
│   └── tone_analysis.py
├── personal_color      # Machine learning algorithm
│   ├── app.py
│   ├── color_converter.py
│   ├── color_extract.py
│   ├── ColorUs.code-workspace
│   ├── detect_face.py
│   ├── personal_color.py
│   ├── requirements.txt
│   └── shape_predictor_68_face_landmarks.dat
├── react               # Frontend
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
```
