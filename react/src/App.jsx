import { useState } from 'react'
import './App.css'

function App() {
  return (
    <>
      <div className="app-container">
        <header className="app-header">
          <div className="logo">ColorUs</div>
        </header>
        <main className="main-content">
          <div className="image-placeholder">
            <span>Upload an image</span>
          </div>
        </main>
      </div>
    </>
  )
}

export default App
