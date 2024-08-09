import React, { useRef, useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      document.getElementById("label").classList.add("hidden");
      document.getElementById("startButton").classList.remove("invisible");
      document.getElementById("image").classList.remove("hidden");
      document.getElementById("image").src = URL.createObjectURL(selectedFile);
    }
  };

  const analyzeImage = () => {
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/analyze', {
      method: 'POST',
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
      })
      .catch((err) => console.error("Error", err));
  }

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
              onClick={() => fileInputRef.current.click()}
            >
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
              alt="Uploaded"
            />
          </div>
        </main>
        <button
          id="startButton"
          className="invisible m-8 bg-transparent text-blue-700 font-semibold py-2 px-4 border border-blue-500 rounded text-2xl"
          onClick={analyzeImage}
        >
          Start!
        </button>
      </div>
    </>
  );
}

export default App;
