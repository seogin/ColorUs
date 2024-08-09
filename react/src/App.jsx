import { useState } from 'react'
import React, { useRef } from 'react'
import './App.css'

function App() {
  const fileInputRef = useRef(null);

  const handleSpanClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Process the uploaded file here
      console.log('File uploaded:', file);
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
            <span id="img" className="flex items-center justify-center w-full h-full rounded-xl p-2" style={{verticalAlign: "middle"}} onClick={handleSpanClick}>
              Upload an image
            </span>
            <input type="file" id="fileInput" name="img" accept="image/*" ref={fileInputRef} style= {{ display: "none" }} onChange={handleFileChange}/>
          </div>
        </main>
      </div>
    </>
  )
}

export default App
