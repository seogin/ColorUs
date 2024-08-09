import { useState } from "react";
import React, { useRef } from "react";
import "./App.css";

function App() {
    const [file, setFile] = useState();
    const fileInputRef = useRef(null);

    const handleSpanClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            // Process the uploaded file here
            console.log("File uploaded:", file);
            label.classList.add("hidden");
            startButton.classList.remove("invisible")
            image.classList.remove("hidden");
            setFile(URL.createObjectURL(file));
        }
    };

    return (
        <>
            <div className="app-container">
                <header className="app-header">
                    <div className="logo">ColorUs</div>
                </header>
                <main className="main-content">
                    <div className="image-placeholder">
                        <span
                            id="label"
                            className="flex items-center justify-center w-full h-full rounded-xl p-2"
                            onClick={handleSpanClick}>
                            Upload an image
                        </span>
                        <input
                            type="file"
                            id="fileInput"
                            name="img"
                            accept="image/*"
                            ref={fileInputRef}
                            className="hidden"
                            onChange={handleFileChange}
                        />
                        <img
                            id="image"
                            className="hidden w-full h-full rounded-full"
                            src={file}
                            onClick={handleSpanClick}
                        />
                    </div>
                </main>
                <button id="startButton" className="invisible m-8 bg-transparent text-blue-700 font-semibold py-2 px-4 border border-blue-500 rounded text-2xl">
                  Start!
                </button>
            </div>
        </>
    );
}

export default App;
