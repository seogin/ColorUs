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


- [Demonstration/Presentation Video](https://youtu.be/t0nDQmW4I10)


## 🪲 Known Bugs and Limitations

- Layout optimized for iPhone 14 Pro Max environment

## 🔮 Features for Future

- Integration with real-time criminal data APIs to provide up-to-date and localized crime information.
- AI-driven recommendations for protection services tailored to specific crime patterns and user location data.

## 📂 Contents of Project Folder

###     Top level of project folder:
 ```
├── .gitignore          # Git ignore file
├── .env                # Server environment variables (injected by dotenv)
├── package-lock.json   # Ensures consistent installations of dependencies across environments
├── package.json        # Defines the project's metadata, dependencies, scripts, and configuration
├── README.md           # Project overview, instructions, and documentation
├── tailwind.config.js  # Configuration file for customizing Tailwind CSS settings


```
### Subfolders and files:
```
├── .vscode                  # Folder for VS Code settings
│   └── settings.json        # Live server settings
│
├── public                   # Folder for images
│   ├── Ashe.webp
│   ├── Braum.webp
│   ├── Daniel.jpeg
│   ├── David.jpeg
│   ├── Draven.webp
│   ├── Ezreal.webp
│   ├── Hwei.webp
│   ├── Jhin.webp
│   ├── Jinx.webp
│   ├── Kaisa.webp
│   ├── Karma.webp
│   ├── logo.png
│   ├── logoWName.png
│   ├── Luxanna.webp
│   ├── Milio.webp
│   ├── Mundo.webp
│   ├── Olaf.webp
│   ├── Pyke.webp
│   ├── Samira.webp
│   ├── Sarah.webp
│   ├── seogin.png
│   ├── Seraphine.webp
│   ├── Sett.webp
│   ├── Shaco.webp
│   ├── Shauna.webp
│   ├── Shawn.jpeg
│   ├── Silco.webp
│   ├── Sivir.webp
│   ├── Talon.webp
│   ├── Taric.webp
│   ├── Tobias.webp
│   ├── Udyr.webp
│   ├── Varus.webp
│   ├── Vi.webp
│   ├── Viktor.webp
│   ├── Yasuo.webp
│   ├── Yeali.jpg
│   └── Zeri.webp
│
├── scripts                  # Folder for scripts
│   └── server.js            # Main server-side JavaScript file
│
└── views                    # Folder for view templates
    ├── templates            # EJS templates for rendering the frontend
    │    ├── filter.ejs                   # Template for filtering criminal data on map
    │    ├── footer.ejs                   # Footer section of the web pages
    │    ├── header.ejs                   # Header section with navigation
    │    ├── headerHamburgerOnly.ejs      # Header with hamburger menu only
    │    ├── orderHistory.ejs             # User's history of ordered protection solutions
    │    └── orderSummary.ejs             # Summary of a user's current order
    ├── cybersecurity.ejs            # Information and services for cybersecurity threats
    ├── drones.ejs                   # Information about security drone services
    ├── index.ejs                    # Home page showing login and signup
    ├── list.ejs                     # List view displaying criminal data
    ├── login.ejs                    # User login page
    ├── loginErrorPage.ejs           # Error page for login failures
    ├── map.ejs                      # Map view displaying criminal data
    ├── profile.ejs                  # User profile page
    ├── protection.ejs               # Details of available protection solution types
    ├── resetPassword.ejs            # Page for resetting user password
    ├── resetPasswordProfile.ejs     # Page for password reset from profile page
    ├── robots.ejs                   # Information about guardian robot services
    └── signup.ejs                   # User signup page
```

